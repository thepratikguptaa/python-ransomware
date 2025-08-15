# Python Ransomware (Proof of Concept)

This project is a simple proof-of-concept implementation of a ransomware using Python. It uses the `cryptography` library to find and encrypt files in the same directory.

**This script is for educational purposes only.** Do not use it for any malicious activities.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.x

### Installation

1.  **Clone the repository (or download the files):**
    ```sh
    git clone "https://github.com/thepratikguptaa/python-ransomware"
    cd python-ransomware
    ```

2.  **Create and activate a virtual environment:**

    *   On Windows:
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```

    *   On macOS & Linux:
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage (Encryption)

**Important:** This script will encrypt files in its directory. Make sure you have backups of any important files before running it.

1.  Make sure you have completed the "Getting Started" steps.
2.  Run the encryption script:
    ```sh
    python the_malware.py
    ```
3.  This will encrypt all target files (like `.txt` files, etc.) in the directory and create a `thekey.key` file.

## How to Decrypt Your Files

If your files have been encrypted by the script, you can decrypt them using the `decrypt.py` tool.

*   You must know the secret phrase.

**Steps:**

1.  Run the decryption script from your terminal:
    ```sh
    python decrypt.py
    ```

2.  You will be prompted to enter a secret phrase:
    ```
    Say my name: 
    ```

3.  Type the secret phrase, which is `pratik`, and press Enter.

4.  If the phrase is correct, the script will decrypt all the files and you will see a confirmation message:
    ```
    Files decrypted successfully.
    ```
Your files are now back to their original state. If you enter the wrong phrase, you will see a "Wrong name." message.