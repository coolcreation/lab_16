from csv_functions import read_Personal_from_csv, save_Personal_to_csv, save_Business_to_csv, read_Business_from_csv
from dataclasses import dataclass

##### Personal Choice
@dataclass
class Personal:
    task: str = ""
    is_complete: bool = False


@dataclass    
class PersonalItems:
    def __init__(self):
        self.__items = []
        
    def add_item(self, item: Personal):
        self.__items.append(item)
        
    def delete_item(self, index):
        self.__items.pop(index)
        
    def load_items_from_csv(self):
        items = read_Personal_from_csv(Personal)  
        self.__items = items  
        
    def save_items_to_csv(self):
        save_Personal_to_csv(self.__items)  

    def get_item_count(self):
        return len(self.__items)
            
    def __iter__(self):
        for item in self.__items:
            yield item
            
            
##### Business Choice
@dataclass
class Business:
    task: str = ""
    is_complete: bool = False


@dataclass    
class BusinessItems:
    def __init__(self):
        self.__items = []
        
    def add_item(self, item: Business):
        self.__items.append(item)
        
    def delete_item(self, index):
        self.__items.pop(index)
        
    def load_items_from_csv(self):
        items = read_Business_from_csv(Business)  
        self.__items = items  
        
    def save_items_to_csv(self):
        save_Business_to_csv(self.__items)  
    
    def get_item_count(self):
        return len(self.__items)
       
    def __iter__(self):
        for item in self.__items:
            yield item


            
            
            
            
            
