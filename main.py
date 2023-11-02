import configparser
import os
import sys

from Bio import SeqIO
from PyQt5.QtWidgets import QApplication

from UiMainFunc import UiMainFunc
from moduller import swiss_model_single_file, swiss_model

if __name__ == '__main__':
    # for record in SeqIO.parse("rcsb_pdb_1BZQ.fasta", "fasta"):
    #     print(record)
    #     target_seq = str(record.seq)
    #     seq_id = record.id
    #     seq_id = seq_id.replace("|", "_")
    #     print(seq_id+": "+target_seq)
        # 1BZQ_1_Chains: KETAAAKFERQHMDSSTSAASSSNYCNQMMKSRNLTKDRCKPVNTFVHESLADVQAVCSQKNVACKNGQTNCYQSYSTMSITDCRETGSSKYPNCAYKTTQANKHIIVACEGNPYVPVHFDASV

    app = QApplication([])
    one = UiMainFunc()
    one.show()
    app.exec_()
#     config = configparser.ConfigParser()
#     config.read('config.ini')
#     token = config['SWISS-MODEL']['token']
#     seq1 = "seq_id|H"+"\n"+"seqs"
#     if seq1 is not "":
#         id_seq = seq1.split("\n")
#         id  = id_seq[0].replace("|","_")
#         print(id+": "+id_seq[1])
#         # swiss_model(token=token, target_seq=target_seq, seq_id=seq_id, outpath=outPath)
#     seq2 = "seq_id|L"+"\n"+"seqs"
#     if seq2 is not "":
#         id_seq = seq2.split("\n")
#         id = id_seq[0].replace("|", "_")
#         print(id+": "+id_seq[1])

    # one = sys.argv[1]
    # two = sys.argv[2]
    # swiss_model_single_file(token, "rcsb_pdb_1BZQ.fasta", "./")
    # swiss_model_single_file(token, one, two)
    # # os.system('./enter.sh {} {}'.format(os.path.join('outFiles', receptor_name), os.path.join(
    # #     'outFiles', ligand_name)))
    # os.system('./enter.sh {} {}'.format(os.path.join('outFiles', '1BZQ_1_Chains'), os.path.join(
    #     'outFiles', '1BZQ_2_Chains')))
