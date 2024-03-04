def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name"

    return inner



@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."
    
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments. Use 'change [name] [new phone number]'."
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to {new_phone}."
    else:
        return f"Contact {name} not found."
    
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments. Use 'phone [name]'."
    
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    if not contacts:
        return "No contacts available."

    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()