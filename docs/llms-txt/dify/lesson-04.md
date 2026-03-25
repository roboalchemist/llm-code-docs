# Source: https://docs.dify.ai/en/use-dify/tutorials/workflow-101/lesson-04.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lesson 4: The Cheat Sheet (Knowledge Retrieval)

In the previous lessons, our AI email assistant can draft basic emails. But what if a customer asks about specific pricing plans or refund policy, the AI might start Hallucinating—which is a fancy way of saying it's confidently making things up.

How do we stop the AI from hallucination? We give it a Cheat Sheet.

## What is Retrieval Augmented Generation (RAG)

The technical name for this is RAG (Retrieval-Augmented Generation). Think of it as turning the AI from a chef who memorizes general recipes into a chef who has a Specific Cookbook right on the counter.

It happens in three simple steps:

**1. Retrieval (Find the Recipe)**

When a user asks a question, the AI flips through your Cookbook (the files you uploaded) to find the most relevant pages.

Example: Someone asks for Grandma's Special Apple Pie. You go find that specific recipe page.

**2. Augmentation (Prepare the Ingredients)**

The AI takes that specific recipe and puts it right in front of its eyes so it doesn't have to rely on memory.

Example: You lay the recipe on the counter and get the exact apples and cinnamon ready.

**3. Generation (The Baking)**

The AI writes the answer based only on the facts it just found.

Example: You bake the pie exactly as the recipe says, ensuring it tastes like Grandma's, not a generic store-bought version.

## The Knowledge Retrieval Node

Think of this as placing a stack of reference materials right next to your AI Assistant. When a user asks a question, the AI first flips through this Cheat Sheet to find the most relevant pages. Then, it combines those findings with the user's original question to think of the best answer.

In this practice, we will use the Knowledge Retrieval node to provide our AI Assistant with official Cheat Sheets, ensuring its answers are always backed by facts!

### Hands-On 1: Create the Knowledge Base

<Steps>
  <Step title="Enter the Library">
    Click **Knowledge** in the top navigation bar and click **Create Knowledge**.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-createknowledge.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=b9cb6784c8b3104422b58c1db84ce116" alt="Create Knowledge" width="1789" height="334" data-path="images/difyworkflow101-lesson04-createknowledge.png" />
    </Frame>

    In Dify, you can sync from Notion or a website, but for today, let's upload a file from your device. Click [here](https://drive.google.com/file/d/1imExB0-rtwASbmKjg3zdu-FAqSSI7-7K/view) to download Dify Intro for the upload later.
  </Step>

  <Step title="Upload the File">
    Click **Import from file**. Then, select the file we just downloaded for upload.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-importfromfile.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=337303d51eb437b26cacc0b5290a8e67" alt="Import From File" width="1686" height="894" data-path="images/difyworkflow101-lesson04-importfromfile.png" />
    </Frame>
  </Step>

  <Step title="The 'Chopping' Step (Text Segmentation)">
    High-relevance chunks are crucial for AI applications to provide precise and comprehensive responses. Imagine a long book. It's hard to find one sentence in 500 pages. Dify chops the book into different Knowledge Cards so it can find the right answer faster.

    **Chunk Structure**

    Here, Dify automatically splits your long text into smaller, easier-to-retrieve chunks. We'll just stick with the General Mode here.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-chunkstructure.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=90f43d062007b5276ee6286aede3e202" alt="Chunk Structure" width="846" height="429" data-path="images/difyworkflow101-lesson04-chunkstructure.png" />
    </Frame>

    **Index Method**

    * **High Quality**: Use LLM model to process documents for more precise retrieval helps LLM generate high-quality answers
    * **Economical**: Using 10 keywords per chunk for retrieval, no tokens are consumed at the expense of reduced retrieval accuracy

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-indexmethod.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=1c6081d06cb8fe88d489f396f3c13897" alt="Index Method" width="846" height="156" data-path="images/difyworkflow101-lesson04-indexmethod.png" />
    </Frame>
  </Step>

  <Step title="Retrieval Settings">
    After the document has been processed, we need to do one final check on the retrieval settings. Here, you can configure how Dify looks up the information.

    In Economical mode, only the inverted index approach is available.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-retrievalsetting.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=439e70ae71d019fdc39bbfb2909cba75" alt="Retrieval Setting" width="846" height="249" data-path="images/difyworkflow101-lesson04-retrievalsetting.png" />
    </Frame>

    * **Inverted Index**

      This is the default structure Dify uses. Think of it like the Index at the back of a book—it lists key terms and tells Dify exactly which pages they appear on.

      This allows Dify to instantly jump to the right knowledge card based on keywords, rather than reading the whole book from start.
    * **Top K**

      You'll see a slider set to 3. This tells Dify: When the user asks a question, find the top 3 most relevant Knowledge Cards from the cookbook to show the AI.

      If you set it higher, the AI gets more context to read, but if it's too high, it might get overwhelmed with too much information.

    For now, let's just keep the default settings—they are already perfectly suited for our needs.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-documentprocessing.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=cda5d4b8fe45fc2eff16d54cc62087a8" alt="Document Processing" width="846" height="913" data-path="images/difyworkflow101-lesson04-documentprocessing.png" />
    </Frame>
  </Step>

  <Step title="Save and Process">
    Click **Save and Process**. Your knowledge base is ready!
  </Step>
</Steps>

<Check>
  **Awesome!**

  You have successfully created your first Knowledge Base. Next, we'll use this Knowledge Base to upgrade our AI Email Assistant.
</Check>

### Hands-On 2: Add the Knowledge Retrieval Node

<Steps>
  <Step title="Add the Node">
    1. Go back to your Email Assistant Workflow.
    2. Hover over the line between the Start and LLM nodes.
    3. Click the **Plus (+)** icon and select the **Knowledge Retrieval** node.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-addknowledgetrievalnode.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=d5d0286eefa8cce0edc330316b9f94c2" alt="Add Knowledge Retrieval Node" width="1090" height="600" data-path="images/difyworkflow101-lesson04-addknowledgetrievalnode.png" />
    </Frame>
  </Step>

  <Step title="Connect Knowledge Base">
    1. Click the node, and head to the right panel.
    2. Click the **plus (+)** button next to **Knowledge** to add knowledge.

       <Frame>
           <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-addknowledge.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=a7b6fd690c00615465fd8377fd4a4da0" alt="Add Knowledge" width="407" height="289" data-path="images/difyworkflow101-lesson04-addknowledge.png" />
       </Frame>
    3. Choose **What's Dify**, and click **Add**.

       <Frame>
           <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-selectknowledge.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=7ba5436dbd2275ae70ed591cd0053e06" alt="Select Knowledge" width="504" height="289" data-path="images/difyworkflow101-lesson04-selectknowledge.png" />
       </Frame>
  </Step>

  <Step title="Configure Query Text">
    Now the knowledge base is ready, how can we make sure that AI is looking through the knowledge base to search the answer with the email?

    Stay at the panel, navigate to **Query text** above, and select `email_content`.

    By doing this, we are telling AI: Take the customer's message and use it as a search keyword to flip through our cookbook and find the matching info. Without a query, the AI is just staring at a closed book.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-querytext.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=66a29efbe7616ac566acdf49a8a077df" alt="Query Text" width="408" height="355" data-path="images/difyworkflow101-lesson04-querytext.png" />
    </Frame>
  </Step>
</Steps>

In this way, the Email Assistant will use the customer's original email as a search keyword to find the most relevant answers in the Knowledge Base.

### Hands-On 3: Upgrade the Email Assistant

Now, the knowledge base is ready. We need to tell the LLM node to actually read the knowledge as context before generating the reply.

<Steps>
  <Step title="Add Context">
    1. Click the **LLM Node**. You'll see a new section called **Context**.
    2. Click it and select **result** from the Knowledge Retrieval node.

       <Frame>
           <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-addcontext.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=71a9597ea9a901c900f4269fa7d30db7" alt="Add Context" width="401" height="408" data-path="images/difyworkflow101-lesson04-addcontext.png" />
       </Frame>
  </Step>

  <Step title="Update the Prompt">
    We need to tell the AI to generate reply based on the context.

    In **System**, add additional requirement **Generate response based on** `/` and select **Context**.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson04-updateprompt.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=02742c4ee55cc6d762744f2e3776a514" alt="Update Prompt" width="1214" height="474" data-path="images/difyworkflow101-lesson04-updateprompt.png" />
    </Frame>
  </Step>
</Steps>

**Whoo!** You've just completed the most challenging part. Now, your email assistant has a knowledge base to check when generating responses. Let's see how it works.

Feel free to use the sample texts below to do the testing.

<CodeGroup>
  ```text Sample Email for Testing theme={null}
  Customer Name: Amanda

  Original Email:
  Hi,

  What does the name 'Dify' actually stand for, and what can it do for my business?

  Best regards,
  Amanda
  ```
</CodeGroup>

Check on the result and you'll find that instead of a generic guess, the AI will look at the knowledge base and explain what Dify stands for.

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/zOZf7YVVQWm9rYof/images/difyworkflow101-lesson04-testresult.png?fit=max&auto=format&n=zOZf7YVVQWm9rYof&q=85&s=6a09f42c4878803fdb0cbae5e0fe6e33" alt="Test Result" width="401" height="657" data-path="images/difyworkflow101-lesson04-testresult.png" />
</Frame>

## Mini Challenge

1. What happens if a customer asks a question that isn't in the knowledge base?
2. What kind of information could you upload as a knowledge base?
3. Explore Chunk Structure, Index Method, and Retrieval Setting.


Built with [Mintlify](https://mintlify.com).