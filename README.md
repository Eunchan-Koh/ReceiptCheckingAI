# ReceiptCheckingAI
AI reads the receipt given, organizes the info and save them into an excel file.<\br>

# Process
<img width="1501" height="273" alt="process" src="https://github.com/user-attachments/assets/ad416276-420e-4ff7-896e-230178621c66" />
Puts the image, then EasyOCR finds the words from the receipt image.</br>
Then compare found words' y position, and if the difference is small, assume they are on the same line, combine them into a single string.</br>
Then reorganize the array of the strings into a single string, with \n at the ends of each line.</br>
Then put that as the input to the Agentic AI, with prompt to organize the receipt. It will call the Items_on_List by the tool added.</br>
Agentic AI will create a correct parameter with my custom class based on BaseModel, so use the parameter to fill in the required sections.</br>
In my code, it will automaticall fill in the cells and save it as the excel file.</br>

#point
