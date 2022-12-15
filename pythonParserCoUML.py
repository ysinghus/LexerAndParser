from tkinter import *
import re
#Mytokens=[]
Mytokens=[("key","float"),("id","myvar"),("op","="),("int","5"),("op","+"),("int","6"),("op","+"),("float","2.3"),("sep",";")]
inToken = ("empty","empty")
outputList3=[]
parserCounter=0
def accept_token():
    global inToken
    print("     accept token from the list:"+inToken[1])
    inToken=Mytokens.pop(0)

def math():
    global outputList3
    print("\n----parent node math, finding children nodes:")
    outputList3.append("\n----parent node math, finding children nodes:")
    global inToken
    if(inToken[0]=="float_lit"):
        print("child node (internal): float")
        outputList3.append("child node (internal): float")
        print("   float has child node (token):"+inToken[1])
        outputList3.append("   float has child node (token):"+inToken[1])
        accept_token()
    elif (inToken[0]=="int_lit"):
        print("child node (internal): int")
        outputList3.append("child node (internal): int")
        print("   int has child node (token):"+inToken[1])
        outputList3.append("   int has child node (token):"+inToken[1])
        accept_token()
    
    else:
        print("error, math expects float or int")

    if(inToken[1]=="+"):
        print("child node (token):"+inToken[1])
        outputList3.append("child node (token):"+inToken[1])
        accept_token()

        print("child node (internal): math")
        outputList3.append("child node (internal): math")
        math()
            
    elif(inToken[1]=="*"):
        print("child node (token):"+inToken[1])
        outputList3.append("child node (token):"+inToken[1])
        accept_token()

        print("child node (internal): math")
        outputList3.append("child node (internal): math")
        math()
    
    elif(inToken[1]==">"):
        print("child node (token):"+inToken[1])
        outputList3.append("child node (token):"+inToken[1])
        accept_token()

        print("child node (internal): math")
        outputList3.append("child node (internal): math")
        math()
        
    
    else:
        outputList3.append("there is no operator after the int/float")




    
def exp():
    print("\n----parent node exp, finding children nodes:")
    global outputList3
    outputList3.append("entering exp() function")
    outputList3.append("----parent node exp, finding children nodes:")
    global inToken;
    typeT,token=inToken;
    
    if(typeT=="key"):
        print("child node (internal): key")
        outputList3.append("child node (internal): key")
        print("   key has child node (token):"+token)
        outputList3.append("   key has child node (token):"+token)
        accept_token()
    else:
        print("expect key as the first element of the expression!\n")
        outputList3.append("expect key as the first element of the expression!\n")
        return
    typeT,token=inToken;
    if(typeT=="id"):
        print("child node (internal): identifier")
        outputList3.append("child node (internal): identifier")
        print("   identifier has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect identifier as the second element of the expression!\n")
        outputList3.append("expect identifier as the second element of the expression!\n")
        return
    typeT,token=inToken;
    if(token=="="):
        print("child node (token):"+token)
        outputList3.append("child node (token):"+token)
        accept_token()
    else:
        print("expect = as the third element of the expression!")
        outputList3.append("expect = as the third element of the expression!")
        return

    print("Child node (internal): math")
    outputList3.append("Child node (internal): math")
    math()

def if_exp():
    print("\n----parent node exp, finding children nodes:")
    global outputList3
    outputList3.append("entering if_exp() function")
    outputList3.append("----parent node exp, finding children nodes:")
    global inToken;
    typeT,token=inToken;
    
    if(typeT=="key"):
        print("child node (internal): key")
        outputList3.append("child node (internal): key")
        print("   key has child node (token):"+token)
        outputList3.append("   key has child node (token):"+token)
        accept_token()
    else:
        print("expect key as the first element of the expression!\n")
        outputList3.append("expect key as the first element of the expression!\n")
        return
    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect seperator as the second element of the expression!\n")
        outputList3.append("expect seperator as the second element of the expression!\n")
        return
    
    typeT,token=inToken;
    if(typeT=="id"):
        print("child node (internal): identifier")
        outputList3.append("child node (internal): identifier")
        print("   identifier has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect identifier as the third element of the expression!\n")
        outputList3.append("expect identifier as the third element of the expression!\n")
        return
    
    typeT,token=inToken;
    if(token=="=="or ">" or "<"):
        print("child node (token):"+token)
        outputList3.append("child node (token):"+token)
        accept_token()
    else:
        print("expect ==,<,> as the fourth element of the expression!")
        outputList3.append("expect ==,<,> as the fourth element of the expression!")
        return
    
    typeT,token=inToken;
    if(typeT=="id"):
        print("child node (internal): identifier")
        outputList3.append("child node (internal): identifier")
        print("   identifier has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect identifier as the fifth element of the expression!\n")
        outputList3.append("expect identifier as the fifth element of the expression!\n")
        return

    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   seperator has child node (token):"+token)
        accept_token()
    else:
        print("expect seperator as the sixth element of the expression!\n")
        outputList3.append("expect seperator as the sixth element of the expression!\n")
        return
    
    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        #accept_token()
    else:
        print("expect seperator as the seventh element of the expression!\n")
        outputList3.append("expect seperator as the seventh element of the expression!\n")
        return

    #print("Child node (internal): math")
    #outputList3.append("Child node (internal): math")
    #math()

def print_exp():
    
    print("\n----parent node exp, finding children nodes:")
    global outputList3
    outputList3.append("entering print_exp() function")
    outputList3.append("----parent node exp, finding children nodes:")
    global inToken;
    typeT,token=inToken;
    if(typeT=="id"):
        print("child node (internal): identifier")
        outputList3.append("child node (internal): identifier")
        print("   identifier has child node (token):"+token)
        outputList3.append("   identifier has child node (token):"+token)
        accept_token()
    else:
        print("expect identifier as the second element of the expression!\n")
        outputList3.append("expect identifier as the second element of the expression!\n")
        return
    
    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   seperator has child node (token):"+token)
        accept_token()
    else:
        print("expect seperator as the sixth element of the expression!\n")
        outputList3.append("expect seperator as the sixth element of the expression!\n")
        return
    
    typeT,token=inToken;
    if (typeT=="string_lit"):
        print("child node (internal): string")
        outputList3.append("child node (internal): string")
        print("   string has child node (token):"+token)
        outputList3.append("   string has child node (token):"+token)
        accept_token()
    
    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   seperator has child node (token):"+token)
        accept_token()
    else:
        print("expect seperator as the sixth element of the expression!\n")
        outputList3.append("expect seperator as the sixth element of the expression!\n")
        return
    
    typeT,token=inToken;
    if(typeT=="sep"):
        print("child node (internal): seperator")
        outputList3.append("child node (internal): seperator")
        print("   seperator has child node (token):"+token)
        outputList3.append("   seperator has child node (token):"+token)
        #accept_token()
    else:
        print("expect seperator as the sixth element of the expression!\n")
        outputList3.append("expect seperator as the sixth element of the expression!\n")
        return
    
    print("Child node (internal): math")
    outputList3.append("Child node (internal): math")
    math()

def parser():
    global inToken
    global outputList3
    inToken=Mytokens.pop(0)
    print("printing type of inToken, should be tuple")
    print(type(inToken))
    
    print("printing inToken")
    print(inToken)
    global parserCounter 
    parserCounter = parserCounter + 1
    print("parserCounter is now: ")
    print(parserCounter)
    if(parserCounter == 1):
        outputList3.append("entering parserCounter==1 if statement, parserCounter value is:")
        outputList3.append(parserCounter)
        exp()
        if(inToken[1]==";"):
            print("\nparse tree line 1 building success!")
        
    elif(parserCounter == 2):
    #line 2
        outputList3.append("entering parserCounter==2 if statement, parserCounter value is:")
        outputList3.append(parserCounter)
        exp()
        if(inToken[1]==";"):
            print("\nparse tree line 2 building success!")
        
    elif(parserCounter == 3):
        outputList3.append("entering parserCounter==3 if statement, parserCounter value is:")
        outputList3.append(parserCounter)
        if_exp()
        if(inToken[1]==";"):
            print("\nparse tree line 3 building success!") 
        
    elif(parserCounter == 4):
        outputList3.append("entering parserCounter==4 if statement, parserCounter value is:")
        outputList3.append(parserCounter)
        #print()
        print_exp()
        if(inToken[1]==";"):
            print("\nparse tree line 4 building success!")
    
    return


def click():
    position = sentence.get('1.0', END)  # retrieves position
    pos = int(position)  # turns position into countable integer
    pos += 1
    position = pos + 1.0

    sentence.delete('1.0', END)

    sentence.insert(END, pos)  # prints current line


    front = int(position) - 1.0
    front = str(front)  # front of reading line
    entered_text = textentry.get(front, position)  # this will collect the text from the text entry box

    line = entered_text

    flag = False
    outputList = []
    outputList2= []
    global x
    global outputList3
    outputList3=[]
    for index in range(len(line)):

        # check for keyword
        foundKey = re.match('(int|float|if|else|string)', line)
        if (foundKey != None):
            strKey = '<key,{}>'.format(foundKey.group(0))
            outputList.append(strKey)
            
            
            tupleKey=("key",foundKey.group(0))
            outputList2.append(tupleKey)
            
            line = line[foundKey.end():]
            line = line.strip()

        # check for identifier
        foundID = re.match('[a-zA-Z]+\d*', line)
        if (foundID != None):
            strID = '<id,{}>'.format(foundID.group(0))
            outputList.append(strID)
            
            tupleID=("id",foundID.group(0))
            outputList2.append(tupleID)
            
            line = line[foundID.end():]
            line = line.strip()

        # check for operator
        foundop = re.match('[=+>*]', line)
        if (foundop != None):
            strOP = '<op,{}>'.format(foundop.group(0))
            outputList.append(strOP)
            
            tupleOP=("op",foundop.group(0))
            outputList2.append(tupleOP)
            
            line = line[foundop.end():]
            line = line.strip()

        # check for  float literal
        floatlit = re.match('\d+.\d+', line)
        if (floatlit != None):
            strLIT = '<float_lit,{}>'.format(floatlit.group(0))
            outputList.append(strLIT)
            
            tupleLIT=("float_lit",floatlit.group(0))
            outputList2.append(tupleLIT)
            
            line = line[floatlit.end():]
            line = line.strip()

        # check for  int literal
        intlit = re.match('\d+', line)
        if (intlit != None):
            strLIT = '<int_lit,{}>'.format(intlit.group(0))
            outputList.append(strLIT)
            
            tupleLIT=("int_lit",intlit.group(0))
            outputList2.append(tupleLIT)
            
            line = line[intlit.end():]
            line = line.strip()

        # check for separator
        foundsep = re.match('^[(|)|;|:|"|"]', line)
        if (foundsep != None):
            strSEP = '<sep,{}>'.format(foundsep.group(0))
            outputList.append(strSEP)
            
            tupleSEP=("sep",foundsep.group(0))
            outputList2.append(tupleSEP)
            
            line = line[foundsep.end():]
            line = line.strip()

        # check for  String literal
        strlit = re.match('["](?!").+(?=")["]', line)
        if (strlit != None):
            strLIT = '<string_lit,{}>'.format(strlit.group(0))
            outputList.append(strLIT)
                
            tupleLIT=("string_lit",foundsep.group(0))
            outputList2.append(tupleLIT)
                
            line = line[strlit.end():]
            line = line.strip()
            

    print("printing Mytokens")
    global Mytokens
    Mytokens = outputList2
    #print(Mytokens)
    for i in outputList:
        textoutput.config(state=NORMAL)
        textoutput.insert(END, i)
        print("printing I")
        print(i)
        
        textoutput.config(state=DISABLED)

        textoutput.config(state=NORMAL)
        textoutput.insert(END, "\n")
        textoutput.config(state=DISABLED)
        print("\n")
    #print("printing textoutput type")
    #print(type(textoutput2))
    #Mytokens.append(textoutput2)
    parser()
    print("printing outputList3 now")
    #global outputList3
    print (outputList3)
    for i2 in outputList3:
        textoutput2.config(state=NORMAL)
        textoutput2.insert(END, i2)
        textoutput2.config(state=DISABLED)

        textoutput2.config(state=NORMAL)
        textoutput2.insert(END, "\n")
        textoutput2.config(state=DISABLED)
        print("\n")
    print("printing textoutput2")
    print(type(textoutput2))
### main:
if __name__ == '__main__':
    
    
    window = Tk()
    window.title("Lexical Analyzer for TinyPie")
    window.configure(background="white")

    # create label
    Label(window, text="Source Code Input: ", bg="white", fg="black", font="none 12 bold").grid(row=1, column=0,
                                                                                                sticky=W)

    # create a text entry box
    textentry = Text(window, width=30, height=30, background="light blue")  # entry???
    textentry.grid(row=2, column=0, columnspan=2, sticky=W)

    # create another label
    Label(window, text="\nCurrent Processing Line:", bg="white", fg="black", font="none 12 bold").grid(row=3, column=0,
                                                                                                       sticky=W)

    # create a text box
    sentence = Text(window, width=4, height=1, bg="light gray")
    sentence.grid(row=3, column=2, sticky=W)
    sentence.insert(END, 0)

    # add a next line button
    Button(window, text="Next Line", width=8, command=click).grid(row=4, column=1, sticky=W)

    # create yet another label
    Label(window, text="Lexer: ", bg="white", fg="black", font="none 12 bold").grid(row=1, column=3, sticky=W)

    # create another text box
    textoutput = Text(window, width=30, height=50, background="light blue")
    textoutput.grid(row=2, column=3, sticky=W)

    # create yet another label
    Label(window, text="Parser: ", bg="white", fg="black", font="none 12 bold").grid(row=1, column=5,sticky=W)

    # create another text box
    textoutput2 = Text(window, width=60, height=50, background="light blue")
    textoutput2.grid(row=2, column=5, sticky=W)


    # exit function
    def close_window():
        window.destroy()


    # add a quit button
    Button(window, text="Quit", width=8, command=close_window).grid(row=4, column=3, sticky=W)

    ###run the main loop


    window.mainloop()

#float mathresult1 = 5 * 4.3 + 2.1;  
#float mathresult2 = 4.1 + 2 * 5.5;  
#if (mathresult1 > mathresult2):
	#print(“I just built some parse trees”);