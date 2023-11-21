def main():
    # Get user input for name, department, and something about themselves
    your_name = input("Enter your name: ")
    name_of_department = input("Enter the name of your department: ")
    about_you = input("Share something about yourself: ")

    # Generate the output
    output = f"Hello, I am {your_name}. I love {name_of_department} and I love being in the Backend even more!\nOne thing about me is that {about_you}."

    # Print the output
    print(output)

if __name__ == "__main__":
    main()
