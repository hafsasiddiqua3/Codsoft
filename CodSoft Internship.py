#!/usr/bin/env python
# coding: utf-8

# # TASK 1 : TO-DO LIST

# In[ ]:


import json
import os
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['date']}")

def add_task(title):
    tasks = load_tasks()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({'title': title, 'date': date})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTO-DO LIST\n")
        tasks = load_tasks()
        display_tasks(tasks)

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            index = int(input("Enter task index to remove: "))
            remove_task(index)
        elif choice == '3':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


# # TASK 2 : CALCULATOR
# 

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    

    print(" ====Simple Calculator====")
    print("PRESS")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter operation choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please enter a valid operation.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    else:
        result = divide(num1, num2)
        operation = "Division"

    print(f"{operation} result: {result}")

if __name__ == "__main__":
    calculator()


# # TASK 3: PASSWORD GENERATOR

# In[3]:


import random
import string

def generate_password(length):
    # Define the character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(length, 8)

    # Generate a random password using the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired length for the password: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()


# # TASK 4: ROCK-PAPER-SCISSORS GAMES

# In[5]:


import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, the computer's choice, and the result."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}\n")

def play_game():
    """Play a single round of the Rock-Paper-Scissors game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result

def main():
    """Main function to run the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye :)")
            break

if __name__ == "__main__":
    main()


# # TASK 5: CONTACT BOOK
# 

# In[ ]:


class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contact_list(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts
                   if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

# User Interface
contact_book = ContactBook()

while True:
    print("**** Contact Book Menu ****")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        contact_book.add_contact(contact)

    elif choice == "2":
        contact_book.view_contact_list()

    elif choice == "3":
        keyword = input("Enter name or phone number to search: ")
        contact_book.search_contact(keyword)

    elif choice == "4":
        name = input("Enter name of contact to update: ")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        contact_book.update_contact(name, new_phone_number, new_email, new_address)

    elif choice == "5":
        name = input("Enter name of contact to delete: ")
        contact_book.delete_contact(name)

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:




