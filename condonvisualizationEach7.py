import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
import numpy as np
import math
#sns.set(style="darkgrid")

codons = pd.read_csv("codondepth4.csv")

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
#columnOfSamples=[]
#for x in range(1,len(listofSamples)):
#    for y in range(len(codons)):
#        columnOfSamples+=[listofSamples[x]]

#columnOfgenes=[]
#for x in range(1,len(listofSamples)):
#    for values in codons.values:
#        columnOfgenes+=[values[0]]

#columnOfsizes=[]
#for x in range(1,len(listofSamples)):
#    for values in codons.values:
#        columnOfsizes+=[int(values[x])]


#for x in 

#print(len(codons))
#print((columnOfgenes))
#print(len(columnOfSamples))
#print(len(columnOfgenes))
#print(len(columnOfsizes))
#print(53728/3359)

#d = {'col1': columnOfSamples, 'col2': columnOfgenes, 'col3':columnOfsizes }
#df = pd.DataFrame(data=d)
#print(df)

#sns.relplot(x="col1", y="col2", size="col3", data=df)
#sns.catplot(x="col2", y="col3", hue="col1", kind="swarm", data=df);

#sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", 11data=tips)

#plt.show()

currentGene=""
codonPosition=[]
count=0
for values in codons.values:
    count+=1
    currentGene=values[0]
    currentGene=values[0][:-len(str(int(''.join(list(filter(str.isdigit, currentGene))))))]
    #print(currentGene)
    if count>0:break

wholeGene=[]
wholeCodonPosition=[]
wholeSample=[]
wholeDepth=[]
for x in range(1,len(listofSamples)):
    currentGeneList=[]
    currentCodonPosition=[]
    currentSample=[]
    currentDepth=[]
    for values in codons.values:
        if currentGene == values[0][:-len(str(int(values[0].split("codon",1)[1])))]:
            #print(values[0].split("codon",1)[1])
            currentGeneList+=[currentGene]
            currentCodonPosition+=[int(values[0].split("codon",1)[1])]
            currentSample+=[listofSamples[x]]
            #print(values[x])
            #print(type(values[x]))
            #print(values[x])
            if math.isnan(float(values[x])):
                #print("true?")
                #print(values[x])
                currentDepth+=[None]
            else:currentDepth+=[int(values[x])]
        elif currentGene != values[0]:
            wholeGene+=[currentGeneList]
            wholeCodonPosition+=[currentCodonPosition]
            wholeSample+=[currentSample]
            wholeDepth+=[currentDepth]
            currentGene = values[0][:-len(str(int(values[0].split("codon",1)[1])))]
            currentGeneList=[]
            currentCodonPosition=[]
            currentGeneList+=[currentGene]
            currentCodonPosition+=[int(values[0].split("codon",1)[1])]
            currentSample+=[listofSamples[x]]
            if values[x]!=float:
                currentDepth+=[None]
            else:currentDepth+=[int(values[x])]
    wholeCodonPosition+=[currentCodonPosition]    
    wholeGene+=[currentGeneList]
    wholeSample+=[currentSample]
    wholeDepth+=[currentDepth]

#print(wholeCodonPosition)
    #print(len(wholeCodonPosition[x]))
    #print(len(wholeGene[x]))
#print(len(wholeGene[0]))
#print(len(wholeCodonPosition[0]))
#print(len(wholeSample))
#x=np.array(wholeCodonPosition)
#y=np.array(wholeGene)
#print(np.shape(x))
#print(np.shape(y))

#print(currentGene)
    #int(filter(str.isdigit, currentGene))
    #codonPosition+=[int(''.join(list(filter(str.isdigit, currentGene))))]

#print(codonPosition)

#for y in range(len(wholeSample)):
#    for x in range(1,len(listofSamples)):
#        emptyList=[]
#        if listofSamples[x]==wholeSample[y]:
#            emptyList+=[y]#

#    d = {'col1': columnOfSamples, 'col2': columnOfgenes, 'col3':columnOfsizes }
#    df = pd.DataFrame(data=d)
#my_string="hello python world , i'm a beginner "
#print (my_string.split("world",1)[1]) 
#print(values[0].split("codon",1)[1])

#d = {'col1': columnOfSamples, 'col2': columnOfgenes, 'col3':columnOfsizes }
currentGene=""
codonPosition=[]
count=0
for values in codons.values:
    count+=1
    currentGene=values[0][:-len(str(int(values[0].split("codon",1)[1])))]
    if count>0:break
wholeGene2=[]
wholeGene2+=[currentGene]
currentGeneList=[]
currentCodonPosition=[]
for values in codons.values:
        #if currentGene == values[0]:
            #currentGeneList+=[currentGene[:-len(str(int(''.join(list(filter(str.isdigit, currentGene))))))]]
            #currentCodonPosition+=[int(''.join(list(filter(str.isdigit, currentGene))))]
        if currentGene != values[0][:-len(str(int(values[0].split("codon",1)[1])))]:
            currentGene = values[0][:-len(str(int(values[0].split("codon",1)[1])))]
            wholeGene2+=[currentGene]
            #currentGene = values[0][:-len(str(int(''.join(list(filter(str.isdigit, currentGene))))))]
            #currentGeneList=[]
            #currentCodonPosition=[]
            #currentGeneList+=[currentGene[:-len(str(int(''.join(list(filter(str.isdigit, currentGene))))))]]
            #currentCodonPosition+=[int(''.join(list(filter(str.isdigit, currentGene))))]


#print(wholeGene2)

#for gene in (wholeGene2):
#    columnCodonPosition=[]
#    columnSample=[]
#    columnDepth=[]
#    for x in range(len(wholeGene)):
#        for y in range(len(wholeGene[x])):
#            if wholeGene[x][y]==gene:
#                columnCodonPosition+=[wholeCodonPosition[x][y]]
#                columnSample+=[wholeSample[x][y]]
#                if wholeDepth[x][y]!=0:
#                    columnDepth+=[wholeDepth[x][y]]
#                else:
#                    columnDepth+=[None]
    #print(columnDepth)
    #break
 #   genename=str(gene)+'Position'
 #   d = {'strain': columnSample, genename: columnCodonPosition, 'CodonDepth':columnDepth}
 #   df = pd.DataFrame(data=d)
 #   print(df)
    #df.to_csv("test.csv")
    #break
    #cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
 #   cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
 #   sns.scatterplot(x="strain", y=genename, size="CodonDepth", palette=cmap, data=df)
    #sns.catplot(x="strain", y=genename, data=df)#size="CodonDepth", palette=cmap, data=df)
    #sns.catplot(x="col2", y="col3", hue="col1", kind="swarm", data=df);

    #sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", 11data=tips)

 #   plt.show()

#print(wholeCodonPosition[0][1131])

#print(wholeGene2)

for x in range(1,len(listofSamples)):
    columnCodonPosition=[]
    columnDepth=[]
    columnGene=[]
    for y in range(len(wholeGene)):
        for z in range(len(wholeGene[y])):
            if wholeSample[y][z]==listofSamples[x]:
                #print(y)
                #print(z)
                #print((wholeCodonPosition[0][1131]))
                #if wholeGene[y][z]=="PfDHFRcodon":
                #    break
                #if wholeGene[y][z]=="MTcodon":
                #    break
                columnCodonPosition+=[wholeCodonPosition[y][z]]
                columnGene+=[wholeGene[y][z]]
                columnDepth+=[wholeDepth[y][z]]
                #for gene in wholeGene2:
                #    if gene==wholeGene[y][z]:
                #        columnCodonPosition2+=[wholeCodonPosition[y][z]]
                #        columnGene2+=[wholeGene[y][z]]
                #        columnDepth2+=[wholeDepth[y][z]]
                #if wholeDepth[y][z]!=0:
                #    columnDepth+=[wholeDepth[y][z]]
                #else:
                #    columnDepth+=[None]
    d = {"CodonPosition": columnCodonPosition, 'CodonDepth':columnDepth, "Genetype":columnGene}
    df = pd.DataFrame(data=d)
    #sns.scatterplot(x="CodonPosition", y="CodonDepth", hue="Genetype", s=70, alpha=0.3, data=df).set_title("strain "+listofSamples[x])

    #sns.scatterplot(x="CodonPosition", y="CodonDepth", hue="Genetype", s=70, alpha=0.3, data=df).set_title("strain "+listofSamples[x])#palette=cmap, data=df)
    #sns.catplot(x="strain", y=genename, data=df)#size="CodonDepth", palette=cmap, data=df)
    #sns.catplot(x="col2", y="col3", hue="col1", kind="swarm", data=df);
    #sns.pairplot("CodonPosition", "CodonDepth", kind="hex", data=df)#.set_title("strain "+listofSamples[x])
    #sns.pairplot(df, kind="scatter", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5), hue="Genetype")#.set_title("strain "+listofSamples[x])
    #sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", 11data=tips)
    #sns.kdeplot(df)#.set_title("strain "+listofSamples[x])
    #sns.pairplot(df, hue="Genetype")#.set_title("strain "+listofSamples[x])
    #sns.catplot(x="CodonPosition", y="CodonDepth", hue="Genetype", kind="violin", data=df)
    #print(df)
    sns.heatmap(df.pivot("CodonPosition","Genetype", "CodonDepth")).set_title("strain "+listofSamples[x])
    plt.savefig("strain "+listofSamples[x]+"_heatmap.png")
    plt.clf()
    #break
    #print(wholeGene2)
    #print(columnGene)
    #print(columnGene)
    #print(columnDepth)
    #color=0.1

    #for x in range(1,len(listofSamples)):
    #columnCodonPosition2=[]
    #columnDepth2=[]
    #columnGene2=[]
    #for y in range(len(wholeGene)):
        #for z in range(len(wholeGene[y])):
            #if wholeSample[y][z]==listofSamples[x]:
                #color1=1
                #color2=10
                #color3=10
                #color4=1
                #for gene in wholeGene2:
                    #columnGene2=[]
                    #for k in range(len(columnGene)):
                    #    columnGene2+=[gene]
                    #color+=0.2
                    #color1+=1
                    #color2-=1
                    #color3-=1
                    #color4+=1
                    #rgb_code = [128, 128, 128]
                    #colors = [(color1/10,color2/10,color3/10,color4/10)]
                    #customPalette = sns.set_palette(sns.color_palette(colors))
                    #print(color)
                    #print(len(columnGene))
                    #print(len(columnGene2))
                    #print(columnGene2)
                    #d = {"CodonPosition": columnCodonPosition, 'CodonDepth':columnDepth, "Genetype":columnGene2}
                    #df = pd.DataFrame(data=d)
                    #print(columnCodonPosition)
                    #cmap = sns.cubehelix_palette(dark=color, light=.8, as_cmap=True)
                    #sns.scatterplot(x="CodonPosition", y="CodonDepth", hue="Genetype", palette=customPalette, s=30, alpha=0.9, data=df).set_title("strain "+listofSamples[x])
                    #print("test")
                    #plt.show()
                    #plt.savefig("strain "+"_"+listofSamples[x]+"_"+str(gene)+'.png')
    #print(df)
    #df.to_csv("test2.csv")
    #break
#    cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
 #   cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)

    #d = {"CodonPosition": columnCodonPosition, 'CodonDepth':columnDepth, "Genetype":columnGene}
    #df = pd.DataFrame(data=d)
    #sns.scatterplot(x="CodonPosition", y="CodonDepth", hue="Genetype", s=70, alpha=0.3, data=df).set_title("strain "+listofSamples[x])

    #sns.scatterplot(x="CodonPosition", y="CodonDepth", hue="Genetype", s=70, alpha=0.3, data=df).set_title("strain "+listofSamples[x])#palette=cmap, data=df)
    #sns.catplot(x="strain", y=genename, data=df)#size="CodonDepth", palette=cmap, data=df)
    #sns.catplot(x="col2", y="col3", hue="col1", kind="swarm", data=df);
    #sns.pairplot("CodonPosition", "CodonDepth", kind="hex", data=df)#.set_title("strain "+listofSamples[x])
    #sns.pairplot(df, kind="scatter", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5), hue="Genetype")#.set_title("strain "+listofSamples[x])
    #sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", 11data=tips)
    #sns.kdeplot(df)#.set_title("strain "+listofSamples[x])
    #sns.pairplot(df, hue="Genetype")#.set_title("strain "+listofSamples[x])
    #sns.catplot(x="CodonPosition", y="CodonDepth", hue="Genetype", kind="violin", data=df)
    #print(df)
    #sns.heatmap(df.pivot("CodonPosition","Genetype", "CodonDepth")).set_title("strain "+listofSamples[x])
    #plt.savefig("strain "+listofSamples[x]+"_heatmap.png")
    #break

