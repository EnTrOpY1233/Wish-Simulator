#Genshin Wish Simulator
import random
fivestaruplist=["Wanderer"]
fivestarlist=["Keqing","Qiqi","Diluc","Jean","Mona","Tighnari"]
fourstarlist=["Gorou","Yanfei","Faruzan","Four star character","Four star weapon"]

fivestarpulls=[]
fourstarpulls=[]
numberofpull=0

class Fourstar:
    def __init__(self,name,type,number):
        self.name=name
        self.type=type
        self.number=number

class Fivestar(Fourstar):
    def __init__(self,name,type,number):
        self.name=name
        self.type=type
        self.number=number

fourstarinitialize=Fourstar("4 test","good",0)
fourstarpulls.append(fourstarinitialize)
fivestarinitialize=Fivestar("5 test","good",0)
fivestarpulls.append(fivestarinitialize)
def fiftyfifty():
    a=random.randint(1,2)
    if a==1:
        return (fivestaruplist[0],"good")
    else:
        return (random.choice(fivestarlist),"bad")

def fourstarpulling():
    a=random.randint(1,2)
    if a==1:
        return (fourstarlist[4],"bad")
    else:
        b=random.randint(0,3)
        if b==3:
            return (fourstarlist[b],"bad")
        else:
            return (fourstarlist[b],"good")

def fivestarpity():
    if fivestarpulls[-1].type=="bad":
        tenwishes.append("Wanderer")
        fivestar=Fivestar("Wanderer","good",numberofpull)
        fivestarpulls.append(fivestar)
    else:
        fiftyfifty()
        tenwishes.append(fiftyfifty()[0])
        fivestar=Fivestar(fiftyfifty()[0],fiftyfifty()[1],numberofpull)
        fivestarpulls.append(fivestar)
    
def fourstarpity():
    if fourstarpulls[-1].type=="bad":
        tenwishes.append(fourstarlist[random.randint(0,2)],)
        fourstar=Fourstar(fourstarlist[random.randint(0,2)],"good",numberofpull)
        fourstarpulls.append(fourstar)
    else:
        fourstarpulling()
        tenwishes.append(fourstarpulling()[0])
        fourstar=Fourstar(fourstarpulling()[0],fourstarpulling()[1],numberofpull)
        fourstarpulls.append(fourstar)


    


while (True):
    userinput=input("Do you want to pull? 1 for yes.")
    if userinput=="1":
        tenwishes=[]
        print(fourstarpulls[-1].number)
        print(fivestarpulls[-1].number)
        for i in range(10):
            numberofpull+=1
            
            if numberofpull-fivestarpulls[-1].number>=90:
                fivestarpity()
            elif numberofpull-fourstarpulls[-1].number>=10:
                fourstarpity()
            else:
                a=random.randint(1,1000)
                if a<=6:
                    fiftyfifty()
                    tenwishes.append(fiftyfifty()[0])
                    fivestar=Fivestar(fiftyfifty()[0],fiftyfifty()[1],numberofpull)
                    fivestarpulls.append(fivestar)
                elif 6<a<=57:
                    tenwishes.append(fourstarpulling()[0])
                    fourstar=Fourstar(fourstarpulling()[0],fourstarpulling()[1],numberofpull)
                    fourstarpulls.append(fourstar)
                else:
                    tenwishes.append("Three star weapon")
        print(tenwishes)
        cost=numberofpull*160
        print("Cost: "+str(cost)+" Primogens")
        print("Cost: "+str(round((cost/6480*139.99),2))+" CAD")
        
    else:
        exit()


