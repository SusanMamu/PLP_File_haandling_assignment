def create_file():
    try:
        with open("my_file.txt","w") as file :
            file.write("My name is Susan\n")
            file.write("I am a PLP scholar\n")
            file.write("age: 20 years old.\n")
    except FileNotFoundError():
        print("File not found.")

    except PermissionError():
        print("Permission denied access to create file ")

    finally :
        print("File created successifully")

def reading_and_display_file():
    try:
        with open("my_file.txt","r") as file:
            contents = file.read()
            print("Contents of the file: ")
            print(contents)

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission denied to read the file")

    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        with open("my_file.txt","a") as file:
            file.write("I am new to coding\n")
            file.write("I love music\n")
            file.write("I scored 80 marks in maths in KCSE\n")

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission denied to append to file")

    finally:
        print("File appending process completed.")

def main():
    create_file()
    print()
    reading_and_display_file()
    print()
    append_to_file()
    print()
    reading_and_display_file()

if __name__ == "__main__":
    main()