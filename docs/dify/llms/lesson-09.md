# Source: https://docs.dify.ai/en/use-dify/tutorials/workflow-101/lesson-09.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lesson 9: Layout Designer (Template)

In Lesson 8, we successfully built a powerful Agent that can think and search. However, you might have noticed a tiny issue: even though we asked the final LLM to list the answers, sometimes the formatting can be a bit messy or inconsistent (e.g., mixing bullet points with paragraphs).

To fix this, we need a dedicated format assistant to organize the answers into a beautiful, standardized format before the final LLM writes the email.

## Template

It takes the original data (like your list of answers), follows a strict design template/standards you provide, and generates a perfectly formatted block of text, ensuring consistency every single time.

## Hands-On: Polish the Email Layout

<Steps>
  <Step title="Update the LLM Node">
    Since the Template node will be handling the greetings, we need to tell LLM to focus solely on the questions and answers. Copy and paste the prompt below or feel free to edit it.

    ```plaintext wrap theme={null}
    Combine all answers for the original email. Write a complete, clear, and friendly reply that only includes the summarized answers.

    IMPORTANT: Focus SOLELY on the answers. Do NOT include greetings (like "Hi Name"), do
    NOT write intro paragraphs (like "Thank you for reaching out"), and do NOT include
    signatures.
    ```
  </Step>

  <Step title="Add User Message">
    List the different variables respectively.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson09-editllmnode.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=c729de58258cc17d5bf7e932fc4b40e4" alt="Edit LLM Node" width="1476" height="1126" data-path="images/difyworkflow101-lesson09-editllmnode.png" />
    </Frame>
  </Step>

  <Step title="Add Template Node">
    After LLM node, click to add Template node.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson09-addtemplatenode.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=64984937cd3120256c60b6d39b788d2d" alt="Add Template Node" width="1006" height="216" data-path="images/difyworkflow101-lesson09-addtemplatenode.png" />
    </Frame>
  </Step>

  <Step title="Set up the Input Variables">
    Click the Template node, go to the Input Variables section, and add these two items:

    * `customer`: Choose `User Input / {x} customer_name String`
    * `body`: Choose `LLM / {x} text String`

      <Frame>
          <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson09-templateinputvariable.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=c9206965f2dc1abaac71fec83a35e68e" alt="Template Input Variable" width="1222" height="510" data-path="images/difyworkflow101-lesson09-templateinputvariable.png" />
      </Frame>
  </Step>

  <Step title="Format with Jinja">
    **What is Jinja2?**

    In simple terms, Jinja2 is a tool that allows you to format variables (like your list of answers) into a text template exactly how you want. It uses simple symbols to mark where variables go and perform basic logic. With it, we can turn a raw list of data into a neat, standardized text block.

    Here, we can put together opening, signatures, and email body to make sure the email is professional and consistent every time.

    Copy and paste this exact layout into the Template code box:

    ```jinja  theme={null}
    Hi {{ customer }},

    Thank you for reaching out to us, and we are more than happy to provide you with the information you are seeking.

    Here are the details regarding your specific questions:

    {{ body }}

    ---
    Thank you for reaching out to us!
    Best regards,
    Anne
    ```
  </Step>
</Steps>

Here's the final workflow.

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson09-thefinalworkflow.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=6e5b9601149e1b71fcb7eec04f6d6161" alt="Final Workflow" width="2524" height="390" data-path="images/difyworkflow101-lesson09-thefinalworkflow.png" />
</Frame>

Click **Test Run**. Ask multiple questions in one email. Notice how your final output has a perfectly written custom intro, the LLM's beautifully summarized answers in the middle, and a standard, professional signature at the bottom.

## Mini Challenge

1. How would you change the Jinja2 code to make a numbered list (1. Answer, 2. Answer) instead of bullet points?

   <Tip>
     Check the [Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/) or ask an LLM about it.
   </Tip>
2. What else can Template node do?


Built with [Mintlify](https://mintlify.com).