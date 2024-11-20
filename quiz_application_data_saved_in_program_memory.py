#REGISTRATION FORM 
print("===============================   REGISTRATION FORM  ==================================")
first_name = input("FIRST NAME: ")
last_name = input("LAST NAME: ")
email = input("EMAIL: ")
mobileNo = input("MOBILE NUMBER: ")
gender = input("GENDER(Enter M OR F): ")
username = input("CREATE A USERNAME: ")
password = input("CREATE PASSWORD: ")
print("REGISTRATION SUCCESSFUl")            
print("========================================================================================")
print()

#LOGIN 
print("====================================== LOGIN ===========================================")
bool = True
while bool == True:
    Uname = input("Enter the Username: ")
    passW = input("Enter the Password: ") 
    if (Uname == username and passW == password):
        print("LOGIN SUCCESSFUL")
        bool = False
    elif (Uname != username or passW != password):
        print("Wrong Username or Password")
print("========================================================================================")
print()

#QUIZ ATTEMPT
DSA_ques = {1:["Ques1. A data structure in which linear sequence is maintained by pointers is known as: ", "A. Array", "B. Stack", "C. Linked list"
               , "D. Pointer-based data structure", "C"],
            2:["Ques2. which of the following data structure works on the principle of First Come First Serve: "
               , "A. priority queue", "B. Heap", "C. Stack", "D. Queue", "D"],
            3:["Ques3. A _____ is a linear collection of self-referential structures, called nodes, connected by pointer links: ", "A. Queue", "B. Linked list", "C. Tree"
               , "D. Stack", "B"],
            4:["Ques4. A queue where all elements have equal priority is a: ", "A. ILFO data structure", "B. LILO data structure", "C. FIFO data structure"
               , "D. LIFO data structure", "C"],
            5:["Ques5.A file that is only read by a program is known as: ", "A. Input file", "B. Temporary file", "C. Work file"
               , "D. Input/Output file", "A"]} 

DBMS_ques = {1:["Ques1. An entity set without sufficient attributes to form a primary key is called: "
               , "A. Acid entity set ", "B. Non-primary entity set", "C. Weak entity set", "D. Strong entity set", "C"],
             2:["Ques2. In the Hierarchical model records are organised in the form of a: "
               , "A. Linked list", "B. Data tables", "C. Tree", "D. Graph", "D"],
             3:["Ques3. In an ER diagram attributes are represented using: "
               , "A. Ellipse", "B. Diamond", "C. Rectangle", "D. Dotted rectangle", "A"],
             4:["Ques4. What are the different types of realtionships in RDBMS: "
               , "A. One to many", "B. One to one", "C. One to multiple", "D. A & B", "D"],
             5:["Ques5.Which of the following are not the disadvantages of a file system to store data: "
               , "A. Data redundancy and in consistency", "B. Difficulty in accessing data", "C. Data isolation is not present"
               , "D. High cost", "D"]}
 
Python_ques = {1:["Ques1. What is Python: "
               , "A. C++ library", "B. Web browser", "C. IDE(Integrated Developer Environment)", "D. Programming language", "C"],
               2:["Ques2. Who created Python: "
               , "A. Denis Ritchie", "B. Tom cruise", "C. Guido Van Rossum", "D. James Gosling", "C"],
               3:["Ques3. In python which keyword is used to start function: "
               , "A. import", "B. def", "C. function", "D. try", "B"],
               4:["Ques4. Python was released publicly in which year: "
               , "A. 1991", "B. 1981", "C. 1961", "D. 1971", "A"],
               5:["Ques5.In python which is the correct method to load a module: "
               , "A. include math", "B. #include math.h", "C. using math", "D. import math", "D"]}

               
DSA_score = 0
DSA_total_score = 5
print("DSA Multiple Choice Questions")
print()
for val in range(1,6): 
    for ele in range(5):
        print(DSA_ques[val][ele])
    print()
    answer= (input("Enter your Answer (A/B/C/D): ")).upper()
    print()
    if answer == DSA_ques[val][5]:
        print("Correct Answer")
        DSA_score +=1
        print("your score is: ", DSA_score, "/", DSA_total_score)
        print()
    else:
        print("Wrong Answer")
        print("Correct Answer is: ", DSA_ques[val][5])
        print("your score is: ", DSA_score, "/", DSA_total_score)
        print()     
print("Your DSA score is: ", DSA_score, "/", DSA_total_score)

print("========================================================================================")
print()

DBMS_score = 0
DBMS_total_score = 5
print("DBMS Multiple Choice Questions")
print()
for val in range(1,6):
    for ele in range(5):
        print(DBMS_ques[val][ele])
    print()
    answer= (input("Enter your Answer (A/B/C/D): ")).upper()
    print()
    if answer == DBMS_ques[val][5]:
        print("Correct Answer")
        DBMS_score +=1
        print("your score is: ", DBMS_score, "/", DBMS_total_score)
        print()
    else:
        print("Wrong Answer")
        print("Correct Answer is: ", DBMS_ques[val][5])
        print("your score is: ", DBMS_score, "/", DBMS_total_score)
        print()
               
print("Your DBMS score is: ", DBMS_score, "/", DBMS_total_score)

print("========================================================================================")
print()

Python_score = 0
Python_total_score = 5
print("Python Multiple Choice Questions")
print()
for val in range(1,6): 
    for ele in range(5):
        print(Python_ques[val][ele])
    print()
    answer= (input("Enter your Answer (A/B/C/D): ")).upper()
    print()
    if answer == Python_ques[val][5]:
        print("Correct Answer")
        Python_score +=1
        print("your score is: ", Python_score, "/", Python_total_score)
        print()
    else:
        print("Wrong Answer")
        print("Correct Answer is: ", Python_ques[val][5])
        print("your score is: ", Python_score, "/", Python_total_score)
        print()
              
print("Your Python score is: ", Python_score, "/", Python_total_score)

print("========================================================================================")
print()

#RESULT OF QUIZ
Total_score = DSA_score + DBMS_score + Python_score
Maximum_marks = DSA_total_score + DBMS_total_score + Python_total_score
print("Your Total Score is: ", Total_score, "/", Maximum_marks)
print("Percentage of correct answers: ", (Total_score/Maximum_marks)*100, "%")

print("========================================================================================")
print()

#END OF QUIZ
print("You have successfully completed this quiz")