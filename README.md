🏧 Python Bank ATM System

📌 Project Overview

The Python Bank ATM System is a console-based application developed using Python. It simulates basic ATM banking operations such as checking account balance, depositing money, withdrawing money, and viewing transaction history.

The project uses JSON file handling to store customer account details and transaction records permanently.

✨ Features

- PIN Authentication
- Limited PIN Login Attempts (3 Attempts)
- Check Account Balance
- Deposit Money
- Withdraw Money
- Transaction History
- Insufficient Balance Validation
- Input Validation
- Automatic Data Storage Using JSON
- Save and Retrieve Account Information

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

📂 Project Structure

Python-ATM-System/
│
├── atm_project.py
├── atm_data.json
└── README.md

⚙️ How to Run the Project

Step 1: Clone the repository.

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open the project folder.

Step 3: Run the Python file.

python atm_project.py

Step 4: Enter the PIN to access the ATM menu.

💳 ATM Menu

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit

💾 Data Storage

The application uses a JSON file ("atm_data.json") to store:

- Customer Name
- Account PIN
- Account Balance
- Transaction History

Account information is automatically saved whenever a transaction is completed.

👩‍💻 Author

Akshaya S

GitHub: https://github.com/akshaya1024

📌 Note

This is an educational Python project created for learning purposes. It is not intended for real banking transactions. The sample implementation stores account information locally and does not use production-grade security.
