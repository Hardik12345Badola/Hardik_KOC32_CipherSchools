N=int(input("In how many pieces you want to cut the cake: "))
if 0<=N<=360 and 360%N==0:
    print("Cut the cake in",N,"equal pieces: Possible")
else:
    print("Cut the cake in",N,"equal pieces: Not Possible")    

if 0<=N<=360:
    print("Cut the cake in",N,"pieces if any size: Possible")
else:
    print("Cut the cake in",N,"pieces if any size: Not Possible")   

if N*N+1<=720:
    print("Cut the cake in",N,"pieces such that no two of them are equal: Possible")   
else:
    print("Cut the cake in",N,"pieces such that no two of them are equal: Not Possible")