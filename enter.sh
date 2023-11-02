echo "Success"
# python main.py
# $1 outFiles/1BZQ_1_Chains
# $1 outFiles/1BZQ_2_Chains
# $one outFiles/1BZQ_1_Chains
# $two outFiles/1BZQ_2_Chains
receptor="$1"".pdb"
ligand="$2"".pdb"
receptor_m="$1""_m.pdb"
ligand_m="$2""_m.pdb"
zdock_out="$1"".out"
cd zdock
mark_sur $receptor $receptor_m
mark_sur $ligand $ligand_m
zdock -R $receptor_m -L $ligand_m -o $zdock_out
create.pl $zdock_out
cd ..
#one=outFiles/1BZQ_1_Chains
#two=outFiles/1BZQ_2_Chains
#one=/root/PythonProjs/Proj1/outFiles/1BZQ_1_Chains
#two=/root/PythonProjs/Proj1/outFiles/1BZQ_2_Chains
#receptor="$one.pdb"
#ligand="$two.pdb"
#receptor_m="$one""_m.pdb"
#ligand_m="$two""_m.pdb"
#zdock_out="$one"".out"
#(DaChuang) root@VM-4-10-ubuntu:~/PythonProjs/Proj1# mark_sur $receptor $receptor_m
#open: No such file or directory
#python predict.py -p rcsb_pdb_1BZQ.fasta -o ./outFiles/

