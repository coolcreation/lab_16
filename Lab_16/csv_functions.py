import csv

def read_Personal_from_csv(personal_class):

    items = []
    with open('personal_items.csv', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            task, is_complete = row[0], row[1] == 'True'  
            items.append(personal_class(task= task, is_complete= is_complete)) 
    return items


def save_Personal_to_csv(items_list):

    with open('personal_items.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        for item in items_list:
            writer.writerow([item.task, item.is_complete])  
            

def read_Business_from_csv(business_class):

    items = []
    with open('business_items.csv', newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            task, is_complete = row[0], row[1] == 'True'  
            items.append(business_class(task= task, is_complete= is_complete)) 
    return items

            
def save_Business_to_csv(items_list):

    with open('business_items.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        for item in items_list:
            writer.writerow([item.task, item.is_complete])          
            