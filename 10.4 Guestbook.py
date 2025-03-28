while True:
    name = input("Enter your name (or type 'quit' to exit): ")
    if name.lower() == 'quit':
        print("Goodbye!")
        break
    
    print(f"Hello, {name}! Welcome!")
    
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")
