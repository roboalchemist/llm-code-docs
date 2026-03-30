# Instructions:
## Summarize:
In clear and concise language, summarize the key points and themes presented in the essay.

## Interesting Questions:
Generate three distinct and thought-provoking questions that can be asked about the content of the essay. For each question:
- After "Q: ", describe the problem
- After "A: ", provide a detailed explanation of the problem addressed in the question.
- Enclose the ultimate answer in <>.

## Write a report
Using the essay summary and the answers to the interesting questions, create a comprehensive report in Markdown format.
```

</details>

#### Strategies we used:

- **Step-by-step instructions**: This strategy is inspired by the chain-of-thought prompting that enables LLMs to use a series of intermediate reasoning steps to tackle complex tasks. It's often easier to solve complex problems when we decompose them into simpler and small steps and it's easier for us to debug and inspect the model behavior. In our example, we break down the task into three steps: summarize, generate interesting questions, and write a report. This helps the language to think in each step and generate a more comprehensive final report.
- **Example generation**: We can ask LLMs to automatically guide the reasoning and understanding process by generating examples with the explanations and steps. In this example, we ask the LLM to generate three questions and provide detailed explanations for each question.
- **Output formatting**: We can ask LLMs to output in a certain format by directly asking "write a report in the Markdown format".

## Personalization
LLMs excel at personalization tasks as they can deliver content that aligns closely with individual users. In this example, we create personalized email responses to address customer questions.


<table class="prompt-example">
    <tr>
        <td>User</td>
        <td>Dear mortgage lender, <br/><br/>
        What's your 30-year fixed-rate APR, how is it compared to the 15-year fixed rate? <br/><br/>
        Regards, <br/>
        Anna</td>
    </tr>
    <tr>
        <td>Assistant</td>
        <td>
        Dear Anna, <br/><br/>
        Thank you for your inquiry regarding our fixed-rate mortgage options.
        Our current 30-year fixed-rate interest rate is 6.403% with an Annual Percentage Rate (APR) of 6.484%. In comparison, our 15-year fixed-rate interest rate is 5.705% with an APR of 5.848%.<br/><br/>
        As you can see, the 15-year fixed-rate option has a lower interest rate and APR compared to the 30-year fixed-rate option. This means that you would pay less in interest over the life of the loan if you choose the 15-year option. However, the monthly payments would be higher due to the shorter loan term.<br/><br/>
        Please let us know if you have any other questions or if we can assist you further in choosing the best mortgage option for your needs.<br/><br/>
        Best regards,<br/>
        Lender Customer Support
        </td>
    </tr>
</table>


<details>
<summary><b>Prompt</b></summary>

```
You are a mortgage lender customer service bot, and your task is to create personalized email responses to address customer questions. Answer the customer's inquiry using the provided facts below. Ensure that your response is clear, concise, and directly addresses the customer's question. Address the customer in a friendly and professional manner. Sign the email with "Lender Customer Support."