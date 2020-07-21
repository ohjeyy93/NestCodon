import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
sns.set(style="darkgrid")

codons = pd.read_csv("codondepth2.csv")

#print(codons.values)

count=0
listofSamples=[]
for line in codons:
    count+=1
    if count==1:
        for word in codons:
            #print(word)
            listofSamples += [word]
    else:break

#listOfSizes=[]
#wholeListofSizes=[]
#count=0
#for row in codons:
#    listOfSizes=[]
#    count+=1
#    if count>1:
#        for size in row:
            #print(size)
#            listOfSizes += [size]
#    wholeListofSizes+=[listOfSizes]

#codons["codons"] = codons.apply(make_a_real_date, axis=1)

df = DataFrame(codons, columns = listofSamples[1::])

#df.loc[(df['Color'] == 'Green') | (df['Shape'] == 'Rectangle')]

#print(df)
#print(codons[2])111
#print(listofSamples[1::])
#print(wholeListofSizes)


#condons = sns.load_dataset(data)
#print(codons)
#sns.relplot(df);

# Scatterplot arguments
#sns.lmplot(x='Attack', y='Defense', data=codons,
 #          fit_reg=False, # No regression line
 #          hue='Stage')   # Color by evolution stage

#sns.relplot(x="total_bill", y="tip", size="size", data=tips)
#data = {'sample':["sample1", "sample2", "sample3"], 'gene':["gene1","gene2","gene3"], 'size':[1,100,300]}
#sns.relplot(x='sample', y='gene', size='size', data=data)
#tips = sns.load_dataset("tips")
#print(tips)

#print(listofSamples[1::])
#print(len(codons))

#for values in codons.values:
#    print(values[0])

#break 
columnOfSamples=[]
for x in range(1,len(listofSamples)):
    for y in range(len(codons)):
        columnOfSamples+=[listofSamples[x]]

columnOfgenes=[]
for x in range(1,len(listofSamples)):
    for values in codons.values:
        columnOfgenes+=[values[0]]

columnOfsizes=[]
for x in range(1,len(listofSamples)):
    for values in codons.values:
        columnOfsizes+=[int(values[x])]


#for x in 

#print(len(codons))
#print((columnOfgenes))
#print(len(columnOfSamples))
#print(len(columnOfgenes))
#print(len(columnOfsizes))
#print(53728/3359)

d = {'col1': columnOfSamples, 'col2': columnOfgenes, 'col3':columnOfsizes }
df = pd.DataFrame(data=d)
print(df)

#sns.relplot(x="col1", y="col2", size="col3", data=df)
sns.catplot(x="col2", y="col3", hue="col1", kind="swarm", data=df);

plt.show()