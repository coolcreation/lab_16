#  Jeff Bohn
#  10/26/2024
#  Chapter 16 - Working with OOP
#  Lab_16-1
#  main.py



from menus import display_menu, display_tasklist_menu
from validations import validate_category_number, validate_tasklist_command, validate_completed_number
from business_classes import Personal, PersonalItems, Business, BusinessItems


# Personal Data Functions
def all_personal_todos(personal_items):
    for i, obj in enumerate(personal_items):
        if obj.is_complete == False:
            print(f"{i+1}. {obj.task:<25}")
        elif obj.is_complete == True:
            print(f"{i+1}. {obj.task:<25}  (DONE!)")
    print()

def add_personal_todo(answer, personal_items):
    personal_item = Personal(task= f"{answer.title()}", is_complete= False)
    personal_items.add_item(personal_item)
    personal_items.save_items_to_csv()
    print(f"'{answer.title()}'  has been added\n")


# Business Data Functions
def all_business_todos(business_items):
    for i, obj in enumerate(business_items):
        if obj.is_complete == False:
            print(f"{i+1}. {obj.task:<25}")
        elif obj.is_complete == True:
            print(f"{i+1}. {obj.task:<25}  (DONE!)")
    print()

def add_business_todo(answer, business_items):
    business_item = Business(task= f"{answer.title()}", is_complete= False)
    business_items.add_item(business_item)
    business_items.save_items_to_csv()
    print(f"'{answer.title()}'  has been added\n")



def main():
    print("Main")
    display_menu()
    display_tasklist_menu()
    
    personal_items = PersonalItems()
    business_items = BusinessItems()

    personal_items.load_items_from_csv()
    business_items.load_items_from_csv()

    tasklist_category = validate_category_number("Enter number to select task list: ")  
    
    def tasklist_choice(tasklist_category):
        if tasklist_category == 1:
            while True:
                task_command = validate_tasklist_command("Command: ")
                
                if task_command == "list":
                    all_personal_todos(personal_items)
                elif task_command == "add":
                    answer = input("Description: ")
                    add_personal_todo(answer, personal_items)
                elif task_command == "complete":
                    count = personal_items.get_item_count()

                    num = validate_completed_number("Number: ", count)
                    for i, obj in enumerate(personal_items):
                        if i == (num - 1):
                            obj.is_complete = True
                            print(f"Number {num} has been marked as Completed\n")
                    personal_items.save_items_to_csv()        
                    
                    
                elif task_command == "delete":
                    print("Delete elif") 
                elif task_command == "switch":
                    tasklist_category = validate_category_number("Enter number to select task list: ")
                    tasklist_choice(tasklist_category)  
                        
                elif task_command == "exit":
                    break 
      
            
        elif tasklist_category == 2:
            while True:
                task_command = validate_tasklist_command("Command: ")
                
                if task_command == "list":
                    all_business_todos(business_items)
                elif task_command == "add":
                    answer = input("Description: ")
                    add_business_todo(answer, business_items)                
                elif task_command == "complete":
                    count = business_items.get_item_count()

                    num = validate_completed_number("Number: ", count)
                    for i, obj in enumerate(business_items):
                        if i == (num - 1):
                            obj.is_complete = True
                            print(f"Number {num} has been marked as Completed\n")
                    business_items.save_items_to_csv()    
                    
                elif task_command == "delete":
                    print("Delete business elif") 
                elif task_command == "switch":
                    tasklist_category = validate_category_number("Enter number to select task list: ")
                    tasklist_choice(tasklist_category)   
                elif task_command == "exit":
                    break   
            
        print("Bye!\n")  
        exit()
    tasklist_choice(tasklist_category)
    
main()