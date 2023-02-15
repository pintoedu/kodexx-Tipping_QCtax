# Tipping_QCtax
Program to calculate QC tax and tipping on served meals

Concordia University - Intro to Python course Jan-Apr/23 - Winter 2023
Assignment 1 – Tip Calculator

Description and Purpose
The purpose of this assignment is to allow you to take the theory we learned in class and apply it practically on your computer, using Python.
Your task is to produce the code required to answer the various questions, test the code, and formalize it before delivering it.
This assignment is meant to be used as an introduction to programming.

Learning Objective(s)
1) Ability to understand and apply the following Python functions:
a) print
b) print.format
c) input
d) while/for/in
e) Python math functions
f) Python string functions
2) Reading a CSV file
3) Looping through records of a CSV file
4) Parsing data from CSV records
5) Converting parsed data to a usable format.
6) Aggregate data.
7) Present data in a report format.

Program #1 – Tip Calculator

Description
Code a “tip calculator” program that calculates the price per person for a meal.
Input
The program should ask the user several questions including:
1. The number of diners
2. The price of the meal, before tax
3. The tip percentage (Horrible = 0%, Basic service = 10%,
Good service = 15%, Exceptional Service = 20%)

Output
The program will then display the following information, with the prices properly formatted and rounded.
1. The number of diners
2. The price of the meal before tax
3. The Quebec tax added (Federal)
4. The Quebec tax added (Provincial)
5. The total including tax
6. The tip amount (based on the price before tax)
7. The grand total including tax
8. The amount owed per person

Guidelines
• The tip percentage should be shown as choices: 1) Exceptional 20% , 2) Good 15%, 3) Basic 10%, 4) Horrible 0%
• If the user chooses 2, then the tip percentage is 15%
• If the user chooses something not in the menu choice list, the program should ask them to choose again and tell them the input was not correct.
• If the user enters a value other than a number (for money amounts), the program should ask them to input the value again.
• There are no “exit” choices in any of the menus, once the program starts, we expect the user to complete the process.
• Comments should be used where applicable.
• Regional settings are not necessary.
• Quebec sales tax rules are here: https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/
