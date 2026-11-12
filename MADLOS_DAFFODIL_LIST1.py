def manage_data():
    items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"] 
    print("Original List: ", ", ".join(items))
    
    update_index = int(input("Input Index to Update: "))
    new_value = input("Input New Value: ")
    
    slice_start = int(input("Enter Slice Range 1: "))
    slice_end = int(input("Enter Slice Range 2: "))
    
    search_item = input("Enter Search Item: ")
    
    print("\n--- Output ---")
    print(f"Index to Update: {update_index}")
    print(f"New Value: {new_value}")
        
    sliced_list = items[slice_start:slice_end]
    print(f"Sliced List: ({slice_start}:{slice_end}) {', '.join(sliced_list)}")
    
    if search_item in sliced_list:
        print(f"Search Result (from sliced array): {search_item} is found")
    else:
        print(f"Search Result (from sliced array): {search_item} is NOT found")
        
    items[update_index] = new_value
    print(f"Updated List: {', '.join(items)}")

if __name__ == "__main__":
    manage_data()