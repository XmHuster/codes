
import sys
import os

global cnt
cnt = 0




def pushLocalFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@LCL\n"
    res += "D=M+D\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n" 
    fo.write(res) 
    
    
def pushArgumentFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@ARG\n"
    res += "D=M+D\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n" 
    fo.write(res)
   
def pushThisFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@THIS\n"
    res += "D=M+D\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n" 
    fo.write(res)
    
def pushThatFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@THAT\n"
    res += "D=M+D\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n" 
    fo.write(res)
    
def pushConstantFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n"
    fo.write(res)

def pushStaticFun(elements, fo, fileName):   
    rawName = fileName.split(".")[0]     
    res = "@" + rawName + "." + elements[2] + "\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n"
    fo.write(res)
    
    
def pushTempFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@5\n"
    res += "D=D+A\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n"
    fo.write(res)
     
    
    
def pushPointerFun(elements, fo):
    if elements[2] == "0":
        res = "@THIS\n"
    else:
        res = "@THAT\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M+1\n"
    fo.write(res)
    
    
    
def pushFun(elements, fo, fileName):
    print(elements)
    if elements[1] == 'local':
        pushLocalFun(elements, fo)
    elif elements[1] == 'argument':
        pushArgumentFun(elements, fo)
    elif elements[1] == 'this':
        pushThisFun(elements, fo)
    elif elements[1] == 'that':
        pushThatFun(elements, fo)
    elif elements[1] == 'constant':
        pushConstantFun(elements, fo)
    elif elements[1] == 'static':
        pushStaticFun(elements, fo, fileName)
    elif elements[1] == 'temp':
        pushTempFun(elements, fo)
    elif elements[1] == 'pointer':
        pushPointerFun(elements, fo)
 
def popLocalFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@LCL\n"
    res += "D=D+M\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@addr\n"
    res += "A=M\n"
    res += "M=D\n"
    fo.write(res)

    

def popArgumentFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@ARG\n"
    res += "D=D+M\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@addr\n"
    res += "A=M\n"
    res += "M=D\n"
    fo.write(res)

def popThisFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@THIS\n"
    res += "D=D+M\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@addr\n"
    res += "A=M\n"
    res += "M=D\n"
    fo.write(res)

def popThatFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@THAT\n"
    res += "D=D+M\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@addr\n"
    res += "A=M\n"
    res += "M=D\n"
    fo.write(res)

def popStaticFun(elements, fo, fileName):
    rawName = fileName.split(".")[0]
    res = "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@" + rawName + "." + elements[2] + "\n"
    res += "M=D\n"
    fo.write(res)

def popTempFun(elements, fo):
    res = "@" + elements[2] + "\n"
    res += "D=A\n"
    res += "@5\n"
    res += "D=D+A\n"
    res += "@addr\n"
    res += "M=D\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    res += "@addr\n"
    res += "A=M\n"
    res += "M=D\n"
    fo.write(res)

def popPointerFun(elements, fo):
    res = "@SP\n"
    res += "M=M-1\n"
    res += "A=M\n"
    res += "D=M\n"
    if elements[2] == "0":
        res += "@THIS\n"
    else:
        res += "@THAT\n"
    res += "M=D\n"
    fo.write(res)
    
def popFun(elements, fo, fileName):
    if elements[1] == 'local':
        popLocalFun(elements, fo)
    elif elements[1] == 'argument':
        popArgumentFun(elements, fo)
    elif elements[1] == 'this':
        popThisFun(elements, fo)
    elif elements[1] == 'that':
        popThatFun(elements, fo)
    elif elements[1] == 'static':
        popStaticFun(elements, fo, fileName)
    elif elements[1] == 'temp':
        popTempFun(elements, fo)
    elif elements[1] == 'pointer':
        popPointerFun(elements, fo)
    
def addFun(elements, fo):
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D+M\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=0\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    
def subFun(elements, fo):
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D-M\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "@SP\n"
    res += "A=M\n"
    res += "M=0\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    
def negFun(elements, fo):
    res = "@SP\n"
    res += "A=M-1\n"
    res += "D=M\n"
    res += "M=-D\n"
    fo.write(res)   
    
    
def egFun(elements, fo):
    global cnt
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D-M\n"
    res += "@EQ" + str(cnt) + "\n"
    res += "D;JEQ\n"
    res += "D=0\n"
    res += "@CONTINUE" + str(cnt) + "\n"
    res += "0;JMP\n"
    res += "(EQ" + str(cnt) + ")\n"
    res += "D=-1\n"
    res += "(CONTINUE" + str(cnt) + ")\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    cnt += 1

def gtFun(elements, fo):
    global cnt
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D-M\n"
    res += "@GT" + str(cnt) + "\n"
    res += "D;JGT\n"
    res += "D=0\n"
    res += "@CONTINUE" + str(cnt) + "\n"
    res += "0;JMP\n"
    res += "(GT" + str(cnt) + ")\n"
    res += "D=-1\n"
    res += "(CONTINUE" + str(cnt) + ")\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    cnt += 1
    
def ltFun(elements, fo):
    global cnt
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D-M\n"
    res += "@LT" + str(cnt) + "\n"
    res += "D;JLT\n"
    res += "D=0\n"
    res += "@CONTINUE" + str(cnt) + "\n"
    res += "0;JMP\n"
    res += "(LT" + str(cnt) + ")\n"
    res += "D=-1\n"
    res += "(CONTINUE" + str(cnt) + ")\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M-1\n"
    res += "M=D\n"  
    fo.write(res)
    cnt += 1
    
def andFun(elements, fo):
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D&M\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    
    
def orFun(elements, fo):
    res = "@2\n"
    res += "D=A\n"
    res += "@SP\n"
    res += "A=M-D\n"
    res += "D=M\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "D=D|M\n"
    res += "@SP\n"
    res += "M=M-1\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    
def notFun(elements, fo):
    res = "@SP\n"
    res += "A=M-1\n"
    res += "D=!D\n"
    res += "@SP\n"
    res += "A=M-1\n"
    res += "M=D\n"
    fo.write(res)
    
def labelFun(elements, fo):
    #null$LABEL
	res = "(null$" + elements[1] + ")\n"
	fo.write(res)

def gotoFun(elements, fo):
	res = "@null$" + elements[1] + "\n"
	res += "0;JMP\n"
	fo.write(res)

def ifgotoFun(elements, fo):
	res = "@SP\n"
	res += "M=M-1\n"
	res += "A=M\n"
	res += "D=M\n"
	res += "@null$" + elements[1] + "\n"
	res += "D;JGT\n"
	fo.write(res)

def callFun(elements, fo):
	res = "\n"
	fo.write(res)

def functionFun(elements, fo, fileName):
    for i in range(int(elements[2])):
        parse("push constant 0" , fo, fileName)
        print(fo.read(100))
        #parse("pop local " + str(i), fo, fileName)

def returnFun(elements, fo):
	res = "\n"
	fo.write(res)

def parse(line, fo, fileName):
    print(line)
    elements = line.split(' ')
    if elements[0] == 'push':
        pushFun(elements, fo, fileName)
    elif elements[0] == 'pop':
        popFun(elements, fo, fileName)
    elif elements[0] == 'add':
        addFun(elements, fo)
    elif elements[0] == 'sub':
        subFun(elements, fo)
    elif elements[0] == 'neg':
        negFun(elements, fo)
    elif elements[0] == 'eq':
        egFun(elements, fo)
    elif elements[0] == 'gt':
        gtFun(elements, fo)
    elif elements[0] == 'lt':
        ltFun(elements, fo)
    elif elements[0] == 'and':
        andFun(elements, fo)
    elif elements[0] == 'or':
        orFun(elements, fo)
    elif elements[0] == 'not':
        notFun(elements, fo)
    elif elements[0] == 'label':
    	labelFun(elements, fo)
    elif elements[0] == 'goto':
    	gotoFun(elements, fo)
    elif elements[0] == 'if-goto':
    	ifgotoFun(elements, fo)
    elif elements[0] == 'call':
    	callFun(elements, fo)
    elif elements[0] == 'function':
        functionFun(elements, fo, fileName)
    elif elements[0] == 'return':
        returnFun(elements, fo)		



def readFromFiles(fileName, fo):
    #Read the vm file.
    fi = open(fileName, "r")
    
    fis = fi.readlines()
    for line in fis:
        #Remove '\n' in a line string.
        line=line.strip('\n')
        #Remove the space in the beginning of string. It can't deal with space line.
        line = line.strip()    
        #print(line)
        #Remove the line begin with //. if // appear behind of the command, it can't be handled.
        x = line.find('//')     
        #print(x)
        if x != 0 and line != "":
            fo.write("// " + line + "\n")
            parse(line, fo, fileName) 
    fi.close()

def readCmds(inputfilePath):
    commands = []


    if os.path.isdir(inputfilePath):
        print("it's a directory")
        outPutfilename = inputfilePath + ".asm"
        fo = open(outPutfilename, "a+")
        datanames = os.listdir(inputfilePath)
        for dataname in datanames:
            if os.path.splitext(dataname)[1] == '.vm':
                fileName = "./"+ inputfilePath + "/" + dataname 
                print(fileName)
                readFromFiles(fileName, fo)
        fo.close()
    elif os.path.isfile(inputfilePath):
        print("it's a normal file")
        outPutfilename = inputfilePath.split('.')[0]
        outPutfilename = outPutfilename + ".asm"
        fo = open(outPutfilename, "a+")
        readFromFiles(inputfilePath, fo)
        fo.close()
    else:
        print("Not a correct path!")


    


if __name__ == '__main__':
    #Got the vm file path.
    #print(sys.argv)
    #global inputfile
    #In main function, we don't need define global variable.
    inputfilePath = (sys.argv)[1]
    readCmds(inputfilePath)
