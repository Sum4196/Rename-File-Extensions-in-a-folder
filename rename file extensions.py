import os,sys
folder = 'C:\Users\mbmenden\Desktop\FIX ME'
for filename in os.listdir(folder):
       infilename = os.path.join(folder,filename)
       if not os.path.isfile(infilename): continue
       oldbase = os.path.splitext(filename)
       newname = infilename.replace('.bak', '.dwg')
       output = os.rename(infilename, newname)
