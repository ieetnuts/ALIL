from sys import argv
#from time import sleep

def initmem(memlen:int) -> dict[int,int]:
 mem={}
 for i in range(0,memlen):
  mem[i]=0
 return mem

def split(text:str) -> list[str]:
 text += "\0"
 res=[]
 i=""
 j=0
 while text[j] != "\0":
  if text[j] in " \r\n\t,":
   res.append(i)
   i=""
  else:
   i+=text[j]
  j+=1
 if i != "": res.append(i)
 return res

if len(argv)>1 and argv[1].endswith(".alil"):
 code=open(argv[1],"r").read()
else:
 raise Exception("Usage: %s file.alil" % argv[0])
p=split(code)
iptr=0
sptr=0
a=0
x=0
y=0
z=0
memlen=32
mem=initmem(memlen)
proc={}
cmp=["0","0"]
print(p)
while iptr < len(p):
 if p[iptr].endswith(":"):
  proc[p[iptr][:-1]]=iptr
  iptr+=1
 if "_main" in list(proc.keys()):
  if p[iptr] == "sta":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    a=mem[int(p[iptr][1:])]
   else:
    a=int(p[iptr])
  elif p[iptr] == "stx":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    x=mem[int(p[iptr][1:])]
   else:
    x=int(p[iptr])
  elif p[iptr] == "sty":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    y=mem[int(p[iptr][1:])]
   else:
    y=int(p[iptr])
  elif p[iptr] == "stz":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    z=mem[int(p[iptr][1:])]
   else:
    z=int(p[iptr])
  elif p[iptr] == "lda":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    mem[int(p[iptr][1:])]=a
   else:
    raise SyntaxError("error :(")
  elif p[iptr] == "ldx":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    mem[int(p[iptr][1:])]=x
   else:
    raise SyntaxError("error :(")
  elif p[iptr] == "ldy":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    mem[int(p[iptr][1:])]=y
   else:
    raise SyntaxError("error :(")
  elif p[iptr] == "ldz":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    mem[int(p[iptr][1:])]=z
   else:
    raise SyntaxError("error :(")
  elif p[iptr] == "str":
   iptr+=1
   if p[iptr].startswith("@") and int(p[iptr][1:]) < memlen:
    mem[int(p[iptr][1:])] = int(p[iptr+1])
   else:
    raise SyntaxError("memory address (@<1-%d>) expected" % memlen)
   iptr+=1
  elif p[iptr] == "sup":
   if a == 1:
    exit(x)
   elif a == 2:
    print(chr(x),end="")
  elif p[iptr] == "inc":
   a+=1
   if a > 255:
    a=0
  elif p[iptr] == "dec":
   a-=1
   if a < 0:
    a=255
  elif p[iptr] == "cmp":
   if a == int(p[iptr+1]):
    cmp[0]=1
   else:
    cmp[0]=0
   if a > int(p[iptr+1]):
    cmp[1]=1
   elif a < int(p[iptr+1]):
    cmp[1]=2
   else:
    cmp[1]=0
   iptr+1
  elif p[iptr] == "jmp":
   iptr+=1
   if p[iptr] in list(proc.keys()):
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jeq":
   iptr+=1
   if cmp[0]==1:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jlt":
   iptr+=1
   if cmp[1]==2:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jgt":
   iptr+=1
   if cmp[1]==1:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jle":
   iptr+=1
   if cmp[0]==1 or cmp[1]==1:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jge":
   iptr+=1
   if cmp[0]==1 or cmp[1]==2:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "jne":
   iptr+=1
   if cmp[0]!=1:
    sptr=iptr
    iptr=proc[p[iptr]]
  elif p[iptr] == "ret":
   iptr=sptr
   sptr=0
 iptr+=1
 #sleep(0.5)
