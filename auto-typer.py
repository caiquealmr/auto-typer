import time  # To add delays
import pyperclip  # To access clipboard text
import pyautogui  # To simulate keyboard actions

# Function to simulate typing
def auto_typing():
    text = pyperclip.paste()  # Get text from clipboard
    
    if not text:
        print("The clipboard is empty. Please copy the text before running the script.")
        return  # Exit if no text is found
    
    print("Text captured from clipboard.")
    print("Place the cursor where you want to type.")
    time.sleep(5)  # Wait for 5 seconds

    print("Typing started...")
    for char in text:
        pyautogui.write(char)  # Type the current character
        time.sleep(0.05)  # Small delay between keystrokes
    
    print("Text typed successfully!")

# Run the function if executed directly
if __name__ == "__main__":
    print("Make sure to copy the text before running the script.")
    auto_typing()
