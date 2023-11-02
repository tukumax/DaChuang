""" 利用 SWISS-MODEL API，将本地的病毒序列提交到 SWISS-MODEL 网站上进行结构预测。 """
# 参考：https://swissmodel.expasy.org/docs/help#modelling_api

import requests
import time
import os
from Bio import SeqIO
import wget
from uncompress import un_gz


def swiss_model(token, target_seq, seq_id, outpath):
    # 创建建模项目
    response = requests.post(
        "https://swissmodel.expasy.org/automodel",
        headers={"Authorization": f"Token {token}"},
        json={
            "target_sequences": target_seq,
            "project_title": seq_id
        },
        timeout=10)

    # 查看运行状态并返回结果下载链接
    project_id = response.json()["project_id"]  ## 获取 project id
    url_list = []
    while True:
        ## 每隔10s不断地查看运行状态，完成或失败都会终止并输出信息
        time.sleep(10)
        # proxies = {"http": None, "https": None}
        response = requests.get(
            f"https://swissmodel.expasy.org/project/{project_id}/models/summary/",
            headers={"Authorization": f"Token {token}"})
        response_object = response.json()
        status = response_object["status"]

        if status == "COMPLETED":
            for model in response_object['models']:
                ## 举例： model 的内容是 {'model_id': '01', 'status': 'COMPLETED', 'gmqe': 0.05, 'coordinates_url':
                # 'https://swissmodel.expasy.org/project/WbWWJA/models/01.pdb.gz'}
                url_list.append(model['coordinates_url'])
            print("Completed!")
            break
        elif status == "FAILED":
            print("Failed!")
            break
        else:
            print("It's still running...")

    # 下载最高分（平均局部最高分）对应的结构
    max_struct = url_list[0]
    wget.download(max_struct, out=outpath+seq_id+".pdb.gz")
    un_gz(outpath+seq_id+".pdb.gz")
    os.remove(outpath+seq_id+".pdb.gz")

def swiss_model_single_file(token,inf_fa, outPath): ##
    # 单个序列的提交，token（swiss-model提供的令牌）inf_fa（输入文件，fasta格式）；outpath（输入文件路径）
    for record in SeqIO.parse(inf_fa, "fasta"):
        target_seq = str(record.seq)
        seq_id = record.id
        seq_id = seq_id.replace("|", "_")
        swiss_model(token=token, target_seq=target_seq,seq_id=seq_id,outpath=outPath)