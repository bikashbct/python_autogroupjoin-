## README.md

# Python Autojoin

A simple Python application that automatically joins Telegram groups using the Telethon library.

## Requirements

- Python 3.7+
- `telethon` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python_autojoin.git
   cd python_autojoin
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Telegram API credentials:
   - Create a file named `config.py` in the project directory.
   - Add your API ID, API hash, and phone number to the `config.py` file:
     ```python
     api_id = 'YOUR_API_ID'
     api_hash = 'YOUR_API_HASH'
     phone_number = 'YOUR_PHONE_NUMBER'
     ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License.
