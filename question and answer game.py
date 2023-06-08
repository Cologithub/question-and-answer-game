#start date:03/06/23
#end date-03/6/23
#ENJOYYY:)

name=(input("What is your first name? "))

print ("Hiii "+ name +" !")
print("Welcome to my computer quizzz:) dont worry its not quadratics:>")

playing=input("U wanna play? Answer with Yes or a No plaese: ")
print(playing)

if playing!="Yes":
    print("awww:( thought u wanted to playy:(")
    quit()

print("YAYY THEN LESS PLAYY:>")

#q1 meaning question 1, q2,q3, etc.

score=0

q1_answer=input("What does the IPOS cycle stand for? ")

if q1_answer=="input, processing, output, storage":
    print("correct:)")
    score+=1

else:
    print("sorry, wrong:(")



q2_answer=input("What is the sqaure root of 144? ")

if q2_answer==("12"):
    print("correct:)")
    score+=1

else:
    print("sorry, wrong:(")



q3_answer=input("What year did St.Lucia become indendent? if udk that well boy...  ")

if q3_answer==("1979"):
    print("correct:)")
    score+=1

else:
    print("sorry, wrong:(")



q4_answer=input("If a=26, b=42 and c=15, find c-b+a ")

if q4_answer==("53"):
    print("correct:)")
    score+=1

else:
    print("sorry, wrong:(")



q5_answer=input("How many groups of 2 can you find in 1000? ")

if q5_answer==("500"):
    print("correct:)")
    score+=1

else:
    print("sorry, wrong:(")


print("You got a score of " + str(score) + " questions correct. ")

if score==(5):
    print("WELL DONE! " + name + " YOU GOT ALL CORRECT:>")











