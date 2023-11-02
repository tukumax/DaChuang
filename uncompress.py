import gzip


# 解压.gz文件
def un_gz(file_name, out_path=None):
    # 获取文件的名称，去掉后缀名
    if not out_path:
        f_name = file_name.replace(".gz", "")
    else:
        f_name = out_path
    # 开始解压
    g_file = gzip.GzipFile(file_name)
    # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()