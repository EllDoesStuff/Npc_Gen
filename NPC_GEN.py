
import random
import time

#Creates basic parameters for NPC Name Generation 
first_name = ["John","Glix","Gorp","Spingle", "Gorgenspock","Jimspop","Timbop","Spingleglorpjixjohn"]
last_name =["Wells","Lil'Jit","Pillars","Glingles","Pin","Shemeems","Greg","Slimps"]

#Makes certain number of NPC's
NPCnumb = int(input("How many NPC's would you like there to be?")) + 1
increment = 0





while NPCnumb > -1:
    yes_or_no = input("Would you like to speak to an NPC?")
   #shows NPC
    if yes_or_no == "yes" or "Yes" or " yes" or " Yes" and NPCnumb != 0:
        print(f"You are speaking to {random.choice(first_name) + " " + random.choice(last_name)}. They have {random.randint(5,100)} attack, {random.randint(1,20)} defense, and {random.randint(10,200)} health. Their special number is {random.random()}")
        NPCnumb -= increment
        increment += 1
el_fin = input("Finished?")
#end statement
if el_fin == "yes" or "Yes" or " yes" or " Yes":
    print("Goodbye!")
else:
    print("Please try again if unsatisfied.")



