# ReceiptCheckingAI
AI reads the receipt given, organizes the info and save them into an excel file.

# Process
<img width="1501" height="273" alt="process" src="https://github.com/user-attachments/assets/ad416276-420e-4ff7-896e-230178621c66" />
Puts the image, then EasyOCR finds the words from the receipt image.
Then compare found words' y position, and if the difference is small, assume they are on the same line, combine them into a single string.
