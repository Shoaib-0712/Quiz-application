import random

# Global variables
login_status = False
login_user = ''
results_file = 'results.txt'

# Question Banks
DSA_ques = {
    1: ["Ques. A data structure in which linear sequence is maintained by pointers is known as: ",
        "A. Array", "B. Stack", "C. Linked list", "D. Pointer-based data structure", "C"],
    2: ["Ques. Which of the following data structure works on the principle of First Come First Serve: ",
        "A. Priority queue", "B. Heap", "C. Stack", "D. Queue", "D"],
    3: ["Ques. A _____ is a linear collection of self-referential structures, called nodes, connected by pointer links: ",
        "A. Queue", "B. Linked list", "C. Tree", "D. Stack", "B"],
    4: ["Ques. A queue where all elements have equal priority is a: ",
        "A. ILFO data structure", "B. LILO data structure", "C. FIFO data structure", "D. LIFO data structure", "C"],
    5: ["Ques. A file that is only read by a program is known as: ",
        "A. Input file", "B. Temporary file", "C. Work file", "D. Input/Output file", "A"]
}

DBMS_ques = {
    1: ["Ques. An entity set without sufficient attributes to form a primary key is called: ",
        "A. Acid entity set", "B. Non-primary entity set", "C. Weak entity set", "D. Strong entity set", "C"],
    2: ["Ques. In the Hierarchical model records are organised in the form of a: ",
        "A. Linked list", "B. Data tables", "C. Tree", "D. Graph", "C"],
    3: ["Ques. In an ER diagram attributes are represented using: ",
        "A. Ellipse", "B. Diamond", "C. Rectangle", "D. Dotted rectangle", "A"],
    4: ["Ques. What are the different types of relationships in RDBMS: ",
        "A. One to many", "B. One to one", "C. One to multiple", "D. A & B", "D"],
    5: ["Ques. Which of the following are not the disadvantages of a file system to store data: ",
        "A. Data redundancy and inconsistency", "B. Difficulty in accessing data", "C. Data isolation is not present", "D. High cost", "D"]
}

Python_ques = {
    1: ["Ques. What is Python: ",
        "A. C++ library", "B. Web browser", "C. IDE(Integrated Developer Environment)", "D. Programming language", "D"],
    2: ["Ques. Who created Python: ",
        "A. Denis Ritchie", "B. Tom Cruise", "C. Guido Van Rossum", "D. James Gosling", "C"],
    3: ["Ques. In Python which keyword is used to start function: ",
        "A. import", "B. def", "C. function", "D. try", "B"],
    4: ["Ques. Python was released publicly in which year: ",
        "A. 1991", "B. 1981", "C. 1961", "D. 1971", "A"],
    5: ["Ques. In Python which is the correct method to load a module: ",
        "A. include math", "B. #include math.h", "C. using math", "D. import math", "D"]
}

# Function for registration
def registration():
    name = input("Enter Name: ")
    city = input("Enter City: ")
    enroll = input("Enter Enrollment ID: ")
    pwd = input("Enter Password: ")

    # Store registration details
    with open('registration.txt', 'a') as reg_file:
        reg_file.write(f"{name},{city},{enroll},{pwd}\n")

    # Store login details
    with open('login_details.txt', 'a') as login_file:
        login_file.write(f"{enroll},{pwd}\n")
    print("Registration Successful!")

# Function for login
def login():
    global login_status, login_user
    enroll = input("Enter Enrollment ID: ")
    password = input("Enter Password: ")
    user_data = {}

    with open('login_details.txt', 'r') as login_file:
        for line in login_file:
            user, pwd = line.strip().split(',')
            user_data[user] = pwd

    if enroll in user_data and user_data[enroll] == password:
        print(f"Welcome, {enroll}!")
        login_status = True
        login_user = enroll
    else:
        print("Invalid login credentials. Please try again.")

# Function to attempt the quiz
def attempt_quiz():
    if not login_status:
        print("Please log in to attempt the quiz.")
        return

    subjects = {"1": DSA_ques, "2": DBMS_ques, "3": Python_ques}
    print("\nSelect a subject for the quiz:")
    print("1. DSA\n2. DBMS\n3. Python")
    subject_choice = input("Enter your choice: ")

    if subject_choice not in subjects:
        print("Invalid choice!")
        return

    question_bank = subjects[subject_choice]

    # Shuffle questions
    question_ids = list(question_bank.keys())
    random.shuffle(question_ids)
    score = 0

    for q_id in question_ids[:5]:
        q = question_bank[q_id]
        print(f"\n{q[0]}")
        for option in q[1:5]:
            print(option)
        answer = input("Your Answer: ").strip().upper()
        if answer == q[5]:
            score += 1

    with open(results_file, 'a') as result_file:
        result_file.write(f"{login_user},{score}\n")

    print(f"Quiz completed! You scored {score}/3.")

# Function to show profile
def show_profile():
    if not login_status:
        print("Please log in to view your profile.")
        return

    with open('registration.txt', 'r') as reg_file:
        for line in reg_file:
            name, city, enroll, pwd = line.strip().split(',')
            if enroll == login_user:
                print(f"\nName: {name}")
                print(f"City: {city}")
                print(f"Enrollment ID: {enroll}")
                return

    print("Profile not found.")

# Function to show result
def show_result():
    if not login_status:
        print("Please log in to view your result.")
        return

    with open(results_file, 'r') as result_file:
        for line in result_file:
            enroll, score = line.strip().split(',')
            if enroll == login_user:
                print(f"\nYour Quiz Score: {score}/3")
                return

    print("No results found.")

# Main function
def main():
    while True:
        print("""
        1. Register
        2. Login
        3. Attempt Quiz
        4. Show Profile
        5. Show Result
        6. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            registration()
        elif choice == '2':
            login()
        elif choice == '3':
            attempt_quiz()
        elif choice == '4':
            show_profile()
        elif choice == '5':
            show_result()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
