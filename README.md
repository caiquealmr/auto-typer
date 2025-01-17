# Auto Typer

**Auto Typer** is a simple Python script that simulates automatic typing of text copied to the clipboard. It's ideal for situations where copy-pasting is blocked, but manual typing is allowed.

## 📋 How It Works

1. Copy the text you want to type (CTRL+C).
2. Run the script.
3. Position the cursor in the desired field.
4. After 5 seconds, the script will start typing the text automatically.

## 🛠️ Dependencies

- **Python 3.6 or higher**
- Python libraries:
  - `pyperclip` (to access clipboard text)
  - `pyautogui` (to simulate typing)

## ⚙️ Installation and Execution

### 1. Clone the Repository

Open the terminal (or command prompt) and run the following command to clone the repository:

```bash
git clone https://github.com/caiquealmr/auto-typer.git
```

### 2. Install Python and Libraries

Verify that Python is installed:

```bash
python --version
```

If needed, download and install from [python.org](https://www.python.org/).

Install the necessary libraries:

```bash
pip install pyperclip pyautogui
```

### 3. Run the Script

Navigate to the repository folder:

```bash
cd path/to/directory/auto-typer
```

Run the script:

```bash
python auto-typer.py
```

## 💡 Tips and Adjustments

- Adjust the waiting time by changing the value in `time.sleep(5)`.
- Modify typing speed by altering `time.sleep(0.05)` within the loop.

## 🚨 Important Notes

- Copy the text before running the script.
- Position the cursor in the desired location before typing begins.
- Use the script responsibly, as it simulates manual typing on your computer.
