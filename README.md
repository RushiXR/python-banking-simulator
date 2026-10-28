# Python Banking Simulator

A command-line banking simulator built with Python and Pydantic. This project explores object-oriented programming, modular code organization, user registration, login validation, and basic banking operations.

## Features

- User registration with username, email, and password confirmation
- Email validation using Pydantic's `EmailStr`
- Password confirmation using a Pydantic model validator
- Login using registered credentials
- Deposit and withdrawal operations
- Balance display and account details
- Separate modules for authentication, validation, banking operations, and application flow

## Technologies Used

- Python
- Pydantic
- Email validation via `email-validator`

## Project Structure

```text
banking-simulator/
├── main.py
├── Login.py
├── operations.py
├── validator.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   cd banking-simulator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate it.

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Current Limitations

- User accounts are stored in memory and are lost when the program exits.
- Account balances are not persisted between sessions.
- Passwords are currently stored and checked as plain text.
- This is an educational simulator, not a production banking application.

## Future Improvements

- Persistent storage with SQLite or PostgreSQL
- Secure password hashing
- Improved input handling and error messages
- Automated unit tests
- Transaction history
- A FastAPI backend and web interface

## Disclaimer

This project is intended for educational purposes only. It should not be used to store real credentials, manage real money, or process actual financial transactions.