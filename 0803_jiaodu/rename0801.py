import os
cwd=os.getcwd()
res=os.listdir(cwd)

fileType = '.msh'
#fileType2 = '.msh'

for i in res:
 if fileType in i:
  pathsepa = os.path.splitext(i)
#  l1 = len(pathsepa)
  s = pathsepa[0]
#  k=0
#  for k in range(0,l1-1):
#   s = s.join(pathsepa)[k]

  
  print (s)
  s1 = s.replace('0720','0731') + fileType
  print (s1)
  os.rename(os.path.join(cwd,i),os.path.join(cwd,s1))
