inp=input('Europe floor?')
try :
	usf=int(inp)+1
except :
	usf=-1

if usf > 0 :
	print("Nice job!")
else : 
	print ("Not a number")
