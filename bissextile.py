# -*-coding:Utf-8 -*
# programme pour déterminer si une année est bissextile ou pas
annee = input ("entrer une année : ")
annee=int(annee) # pour que l'année ne soit plus une chaine de donnée.
if annee %400==0 or ( annee%4==0 and annee%100 != 0):
   print("bissextile")
else:
   print("pas bissextile")
