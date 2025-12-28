print("Welcome")


data  = []
dataset = {}

def input_data():
    global data
    
    print("Choose :")
    print("1. 1D List")
    print("2. 2D List")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        print("Enter Data for 1D array(separated by spaces)")
        data = list(map(int,input().split()))
        return data

    elif ch ==2:
        matrix = []        
        for i in range(3):
            row = []
            for j in range(3):
                x = int(input(f"Enter Data for 2D [{i+1}][{j+1}] :"))
                row.append(x)
            matrix.append(row)

        for i in matrix:
            print(*i)
        return matrix
    else:
        print("Invalid choice")
        return None

def f_data(data):
    flat = []
    if isinstance(data[0], list):
        for row in data:
            for value in row:
                flat.append(value)
    else:
        flat = data
    return flat

def display_dataset(data):
    global dataset

    if data is None:
        print("input data first")
        return
     
    flat = f_data(data)
    
    dataset = {
        "Total elements": len(flat),
        "Minimum": min(flat),
        "Maximum": max(flat),
        "Sum": sum(flat),
        "Average":sum(flat)/ len(flat)
    }

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

def display_filter():
    t = int(input("Enter a threshold value: "))
    flat = f_data(data)
        
    t_val = list(filter(lambda x: x >= t, flat))
    print(f"Filtered Data (values >= {t}):")
    print(t_val)
    
def sort_data():
    if data is None:
        print("Input data first")

    print("Choose Data Type:")
    print("1. 1D List")
    print("2. 2D List")
    dtype = int(input("Enter your choice: "))

    print("Choose Sorting Order:")
    print("1. Ascending")
    print("2. Descending")
    order = int(input("Enter your choice: "))


    if dtype == 1 and not isinstance(data[0], list):
        if order == 1:
            data.sort()
            print("1D Data Sorted in Ascending Order:")
        else:
            data.sort(reverse=True)
            print("1D Data Sorted in Descending Order:")
        print(data)

   
    elif dtype == 2 and isinstance(data[0], list):
        if order == 1:
            sorted_matrix = [sorted(row) for row in data]
            print("2D Data Sorted in Ascending Order:")
        else:
            sorted_matrix = [sorted(row, reverse=True) for row in data]
            print("2D Data Sorted in Descending Order:")
    
        for row in sorted_matrix:
            print(*row)
        

def multiple_statistics(data):

    flat = f_data(data)
    return min(flat), max(flat), sum(flat), sum(flat) / len(flat)


def show_kwargs(**kwargs):
    print("Dataset Summary (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def show_args(*args):
    print("Values using *args:")
    for value in args:
        print(value, end=" ")
    print()
        
def main_menu():
    print("Menu")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

data = None

while True:
    main_menu()
    ch = int(input("Please enter your choice: "))

    if ch == 1:
        data = input_data()
        if data is not None:
            print("Data has been stored successfully!")
            show_args(*f_data(data))
            
            
    elif ch == 2:
        if data is not None:
            display_dataset(data)
            show_kwargs(**dataset)
        else:
            print("Please input data first.")

    elif ch == 3:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial {num} is: {fact(num)}")
   
    elif ch == 4:
        display_filter()
    
    elif ch == 5:
        sort_data()
    
    elif ch == 6:
        if data is None:
            print("Input data first")
        else:
            mn, mx, sm, avg = multiple_statistics(data)
            print("Min:", mn, "Max:", mx, "Sum:", sm, "Average:", avg)

    elif ch == 7:
        break
    