print("welcome to my game:")
game=input("you want to want: ")

if game.lower()!="yes":
    quit()
    
print("yah let's play ")

score=0

ans=input("csk ")
if ans.lower()=="chennai super kings":
    print("correct!")
    score+=1
else:
    print("incorrect")

ans=input("mi ")
if ans.lower()=="mumbai indians":
    print("correct!")
    score+=1
else:
    print("incorrect")

ans=input("rcb ")
if ans.lower()=="royal chall banglore":
    print("correct!")
    score+=1
else:
    print("incorrect")

ans=input("dc ")
if ans.lower()=="delhi capitals":
    print("correct!")
    score+=1
else:
    print("incorrect")

print("you scored"+ str(score)+"points")
print("you scored"+ str((score/4)*100)+"%")
g
