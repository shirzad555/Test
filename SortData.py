
import tkFileDialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import os


savedFileLocationDirectory = open('C:\\Users\\Public\\PR_SortData.txt' , 'a+')
savedFileName = savedFileLocationDirectory.read()
savedFileLocationDirectory.close()
if len(savedFileName) > 0:
	sourceFile = tkFileDialog.askopenfilename(initialdir=savedFileName)
else :
        sourceFile = tkFileDialog.askopenfilename()

openedFile = open(sourceFile) 
statinfo = os.stat (sourceFile)

CH1_V  = []
CH2_V  = []
CH3_V  = []
CH4_V  = []

for line in openedFile:
    #print 'test'
    if len(line.split(",")) > 10 :
        #print line
        vectoredLine = line.split(",") 
 #       Cahnnels = [[0 for x in 500/10] for y in 16]
        for x in range(0, len(vectoredLine)/31-1):
#            Cahnnels[]
            CH1_V.append(vectoredLine[x*31])   
            CH2_V.append(vectoredLine[x*31+1]) 
            CH3_V.append(vectoredLine[x*31+2])
            CH4_V.append(vectoredLine[x*31+3])
        #print vectoredLine[0]
        
print CH1_V
#         if len(vectoredLine) >= (31*(500/10)) #and vectoredLine[6] == 'lb':
#             print "test" 
openedFile.close()   

fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(212)  
#ax1.grid(True)
#ax1.set_ylim(ymin = -2, ymax = 3)
#ax1.set_ylabel(' Status',fontsize = 10)
ax1.plot(CH1_V,'.')   
ax1.plot(CH2_V,'.') 
ax1.plot(CH3_V,'.') 
ax1.plot(CH4_V,'.')  

print 'channel length: ' + str(len(CH1_V) )