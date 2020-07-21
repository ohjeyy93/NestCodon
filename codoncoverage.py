import subprocess
from subprocess import check_output
import csv

#dir=input("Enter directory of bam file : ") 

## create dummy file to write down all the strains
file="test.txt"

#out=check_output(['samtools', 'depth', '-a', dir])#, '>', out])

f = open(file, "w")

## extract all the strains from the bam file
subprocess.run(['ls', '/home/momo/Desktop/CDC/DhruviPatel-Haiti_Test_bam/Haiti_Test_bam/'], stdout=f)

#subprocess.run(['samtools', 'depth', '-a', dir], stdout=f)

## create the output file
filename = "codondepth.csv"


f2 = open(file, "r")

## create a list of strains

list=["codon"]
for line in f2:
    list+=[line.strip('\n')]

## open csv file
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(list) 
    #csvwriter.writerows(rows) 

count=0
sum=0
currentname=""
codonnum=1
file2="text.txt"
k = open(file2, "w")

f2 = open(file, "r")


### create list of codon depth for each strains
list3=[]
listname=[]
samplenum=0
for line in f2:
    #print('/home/momo/Desktop/CDC/DhruviPatel-Haiti_Test_bam/Haiti_Test_bam/'+line.strip('\n')+'/alignments/output_FM_SR_DD_RG.bam')
    #out=check_output(['samtools', 'depth', '-a', '/home/momo/Desktop/CDC/DhruviPatel-Haiti_Test_bam/Haiti_Test_bam/'+line.strip('\n')+'/alignments/output_FM_SR_DD_RG.bam'])
    k = open(file2, "w")
    ## run samtools to obtain depth of each nucleotide base
    subprocess.run(['samtools', 'depth', '-a', '/home/momo/Desktop/CDC/DhruviPatel-Haiti_Test_bam/Haiti_Test_bam/'+line.strip('\n')+'/alignments/output_FM_SR_DD_RG.bam'], stdout=k)
    k2 = open(file2, "r")
    count=0
    sum=0
    currentname=""
    codonnum=1
    list2=[]
    samplenum+=1
    
    ## sum the depth of nucleotide base untill 3 of them is covered for each codon
    for line in k2:
        if count<3:
            currentname=(line.split()[0])
            sum+=int(line.split()[2])
            count+=1
        elif count==3:
            currentname=(line.split()[0])
            sum=int(line.split()[2])
            count=1
            if samplenum==1:
                listname+=[currentname+"codon"+str(codonnum)]
                list2+=[sum]
            else:
                list2+=[sum]
            codonnum+=1
    if samplenum==1:
        list3+=[listname]
        list3+=[list2]
    else:
        list3+=[list2]

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(list) 
    csvwriter.writerows(zip(*list3)) 


#print(list3)
    #for line in out:
    #    print(line)
    #if count<3:
    #    currentname=(line.split()[0])
    #    sum+=line.split()[2]
    #    count+=1
    #elif count==3:
    #    codonnum+=1
    #    currentname=(line.split()[0])
    #    sum=line.split()[2]
    #    count=0

#f2.close()