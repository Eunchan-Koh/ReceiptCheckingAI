# ReceiptCheckingAI
AI reads the receipt given, organizes the info and save them into an excel file.</br>

# How It Looks Like
https://www.youtube.com/watch?v=-ixL8PClKUg
or
[Watch the video](./video.mp4)

# Problem Statement
Recently, most of people uses cards to pay things. However, there are still cases that we use our cash, or moments we need to split our payments in a single receipt. I thought that it will be beneficial if there is an agentic ai that can organize our receipt into a digital format using our picture. So, we can get digital data of our payments just by simply taking a picture of our receipt.

# Process
<img width="1501" height="273" alt="process" src="https://github.com/user-attachments/assets/ad416276-420e-4ff7-896e-230178621c66" />
Puts the image, then EasyOCR finds the words from the receipt image.</br>
Then compare found words' y position, and if the difference is small, assume they are on the same line, combine them into a single string.</br>
Then reorganize the array of the strings into a single string, with \n at the ends of each line.</br>
Then put that as the input to the Agentic AI, with prompt to organize the receipt. It will call the Items_on_List by the tool added.</br>
Agentic AI will create a correct parameter with my custom class based on BaseModel, so use the parameter to fill in the required sections.</br>
In my code, it will automaticall fill in the cells and save it as the excel file.</br>

# point of improvement
1. Reduce the cost
   - Agent function in LangChain is calling out the LLM two times with the same input, doubling the token cost. Since this process only requires a single LLM call to create correct input parameter then to call the tool using that parameter, this can be improved. 
2. Higher accuracy
   - EasyOCR is often omitting or misreading the words and numbers on the receipt image. This can be improved for better performance
      1. Use other OCRs like Google Document AI API
          - Pros: It can increase the accuracy
          - Cons: Cost.
      2. Run EasyOCR multiple times for a single request, and return common outputs
          - Pros: can have better accuracy with the EasyOCR
          - Cons: takes longer time and/or cost. Running it parallely can decrease the time but still lots of problems. 
3. Security
   - Some information in the receipt can be containing personal information.
     1. Can include a guide what to do when taking a picture of the receipt
     2. Add a function that can remove the line  if a specific word related to security is found.

# Next Step
I will try to put this code inside the backend of cloud service, such as AWS or Google cloud, so people can try using it easily by uploading their receipt image into the website. Purpose is to experience backend+frontend steps by myself by this project, and to use this system when I need to.
