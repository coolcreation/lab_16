
def validate_category_number(category_number):
    while True:
        try:
            num = int(input(category_number))
            if num == 1:
                print("Personal task list was selected.\n")
                return int(num)
            elif num == 2 :
                print("Business task list was selected.\n")
                return int(num)
            else:
                print("Must be the number 1 or 2")
        except ValueError as e:
            print(e, "\n Must be the number 1 or 2")  



def validate_tasklist_command(task_command):
    while True:
        try:
            task = input(task_command).lower()
            if check_tasks(task):
                #print(f"{task}")
                return task
            else:
                print("Please enter a valid selection")
        except ValueError as e:
            None
 
 
 
#  validate a completed item submission :  int() required           
def validate_completed_number(question, count):
    while True:
        try:
            num = int(input(question))
            if num >= 1 and num <= count:
                return int(num)
            else:
                print(f"Must be between 1 and {count}")
        except ValueError as e:
            print(e, f"Must be between 1 and {count}")  
            
            
                        
def check_tasks(task_command):
    tasks = ("list", "add", "delete", "complete", "switch", "exit")
    
    for i in tasks:
        if i == task_command:
            return i
        
