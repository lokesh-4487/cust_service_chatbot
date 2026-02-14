# cust_service_chatbot
Step 1: Understanding the Requirements

Before writing any code, I first understood what problem I wanted to solve. In real companies, customer support teams receive repetitive questions like “What is my order status?”, “What is your return policy?”, or “Tell me about this product.”

So, I decided to build a chatbot that can handle such common questions automatically.

For this project, I used:

Python programming language

VS Code as the code editor

Basic Python libraries like json and random

At this stage, the focus was not on complex AI, but on understanding the basic working structure of a chatbot.

Step 2: Creating the Project Structure

I created a proper project folder to keep everything organized. Inside the main project folder, I added:

chatbot.py – main Python file

responses.json – file containing predefined questions and answers

requirements.txt – list of required libraries

Maintaining a clean folder structure is very important in real-world development. It makes the project professional and easy to manage.

Step 3: Designing the Chatbot Responses

Instead of hardcoding all responses inside Python, I created a separate responses.json file.

In this file, I defined:

Different categories (like greetings, order status, return policy)

Keywords or patterns that users might type

Possible responses for each category

For example:
If a user types “hello” or “hi”, the chatbot responds with a greeting.
If a user types “order status”, the chatbot asks for the order ID.

Using a JSON file makes the chatbot flexible. In the future, new questions and answers can be added without changing the main code.

Step 4: Writing the Chatbot Logic (Rule-Based System)

In the chatbot.py file, I wrote simple logic:

Take input from the user

Convert it into lowercase

Check if any keyword from the JSON file matches

If matched → return a random response

If not matched → show a default message

This is called a Rule-Based Chatbot because it works on predefined rules and keyword matching.

The chatbot runs inside the terminal. The user can type messages continuously until they type “exit” to stop the program.

This step helped me understand:

How input/output works in Python

How loops work

How conditions are used

How external files (JSON) are loaded and used

Step 5: Running and Testing the Chatbot

After writing the code, I tested the chatbot in the VS Code terminal.

Example interaction:

User: hello
Bot: Hello! How can I help you?

User: return policy
Bot: Our return policy allows returns within 7 days.

Testing is very important. I checked different inputs to make sure:

The chatbot responds correctly

It does not crash

It handles unknown inputs properly

This step gave me practical experience in debugging and improving user interaction.

What I Learned

Through this project, I learned:

Basic chatbot architecture

How customer service automation works

File handling in Python

JSON data structure

Rule-based AI logic

Importance of clean project structure

This project is simple but powerful for beginners. It builds a strong foundation before moving to advanced NLP-based chatbots using machine learning.
