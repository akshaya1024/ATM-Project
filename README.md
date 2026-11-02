🏧 Python Bank ATM System

📌 Project Overview

The Python Bank ATM System is a console-based banking application developed using Python. It simulates basic ATM operations and allows users to securely access their account through PIN verification.

The application provides essential banking functionalities such as checking account balance, depositing money, withdrawing money, and viewing transaction history.

It uses JSON file handling to store and retrieve customer account information and transaction records.

✨ Features

- PIN-Based Authentication
- Limited Login Attempts (3 Attempts)
- Check Account Balance
- Deposit Money
- Withdraw Money
- View Transaction History
- Insufficient Balance Validation
- Input Validation
- Automatic Data Storage Using JSON
- Persistent Account Information

🛠️ Technologies Used

- Python
- JSON
- File Handling
- Exception Handling

🐍 Python Concepts Used

- Functions
- Conditional Statements
- While Loop
- For Loop
- Lists and Dictionaries
- Exception Handling
- JSON Serialization and Deserialization
- File Handling
- Modular Programming

📂 Project Structure

ATM-Project/
│
├── atm_project.py
├── .gitignore
└── README.md

⚙️ How to Run the Project

Step 1: Clone the Repository

git clone https://github.com/akshaya1024/ATM-Project.git

Step 2: Navigate to the Project Folder

cd ATM-Project

Step 3: Run the Python File

python atm_project.py

Step 4: Enter the PIN

Enter the account PIN to access the ATM menu.

💳 ATM Menu

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit

💾 Data Storage

The application uses a JSON file named "atm_data.json" to store:

- Customer Name
- Account PIN
- Account Balance
- Transaction History

Account information is automatically saved whenever a transaction is completed.

👩‍💻 Author

Akshaya S

GitHub: https://github.com/akshaya1024

📌 Note

This project is developed for educational purposes to demonstrate Python programming, file handling, and basic banking operations. It is not intended for real-world banking transactions.
