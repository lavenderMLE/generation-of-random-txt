import numpy as np
import random
import re



cross_symbol = []
emo = []
bio_1 = []
bio_2=[]
snap = []
username = []
Outputs = []
with open('./dataset/-.txt') as f:
    lines = f.readlines()
    for sub in lines:
        cross_symbol.append( re.sub('\n','',sub))    

with open('./dataset/(EMOJI).txt', encoding="utf8") as f:
    lines = f.readlines()
    for sub in lines:
        emo.append( re.sub('\n','',sub))
    
with open('./dataset/BIO_LINE_1.txt', encoding="utf8") as f:
    lines = f.readlines()
    bio_1 = lines
with open('./dataset/BIO_LINE_2.txt', encoding="utf8") as f:
    lines = f.readlines()
    bio_2 =  lines
with open('./dataset/Snap.txt', encoding="utf8") as f:
    lines = f.readlines()
    for sub in lines:
        snap.append( re.sub('\n','',sub))    
    
with open('./dataset/USERNAME.txt') as f:
    lines = f.readlines()
    for sub in lines:
        username.append( re.sub('\n','',sub))    
    


#  preprocessing txt

print( len(['sd','sd','sdf']))


for i in range( len(username) ):
    Bio1 = bio_1[ random.randint(0, len(bio_1)-1) ]
    snap_idx = random.randint(0, len(snap)-1)    
    
    Snap = snap[ snap_idx ]
    Cross = cross_symbol[ random.randint(0, len(cross_symbol))-1]
    User = username[ i ]
    Emo = emo[ random.randint(0, len(emo))-1 ]
    Bio2 = bio_2[ random.randint(0, len(bio_2))-1 ]

    Output = '=====================\n' + Bio1 + Snap + Cross + User +'('+ Emo +')\n'+ Bio2
    Outputs.append(Output)
    

with open('out.txt', 'w',encoding='utf8') as f:
    for Output in Outputs:
        f.write(Output)
        f.write('\n')

