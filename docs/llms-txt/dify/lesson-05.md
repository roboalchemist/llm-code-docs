# Source: https://docs.dify.ai/en/use-dify/tutorials/workflow-101/lesson-05.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lesson 5: The Crossroads of Your Workflow (Sorting and Executing)

Right now, our Email Assistant treats every message following the same path of the workflow. That's not smart enough. An email asking about Dify's price should be handled differently than an email on bug reporting.

To make our assistant truly intelligent, we need to teach it how to Read the Room. We're going to set up a Crossroads that sends different types of emails down different tracks.

## The If/Else Node

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-ifelsenode.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=8d3b24822a5c0e2b92595190539b75e0" alt="If/Else Node" width="315" height="156" data-path="images/difyworkflow101-lesson05-ifelsenode.png" />
</Frame>

If/Else node is just like a traffic light. It checks a condition (like Does this email mention pricing? ) and sends the flow left or right based on the result.

### Hands-On 1: Set up the Crossroads

Let's upgrade our assistant so it can tell the difference between Dify-related emails and Everything else.

<Steps>
  <Step title="Insert the Node">
    Hover over the line between the Start and Knowledge Retrieval nodes. Click the **Plus (+)** icon and select the **If/Else** node.
  </Step>

  <Step title="Set the Rules">
    1. Click the node to open the panel
    2. Click **+ Add Condition** in the IF section. Choose the variable: `{x} email_content`

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-settings1.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=c9a78ad8fb996bc62623e70733da9a25" alt="Add Condition" width="405" height="342" data-path="images/difyworkflow101-lesson05-settings1.png" />
    </Frame>

    3. The Logic: Keep it as **Contains**. Type **Dify** in the input box

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-settings2.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=05a2cea115a6f2a26e3181d3acfa7a76" alt="Contains" width="396" height="246" data-path="images/difyworkflow101-lesson05-settings2.png" />
    </Frame>

    Now, the complete logic for the IF branch is: `If the email content contains the word Dify`.
  </Step>
</Steps>

<Info>
  **Understanding the Traffic Light**

  When setting conditions, Dify offers several ways to judge information, much like the different signals at a crossroads:

  * **Is / Is Not**

    Like a perfect key for a lock. The content must match your value exactly.
  * **Contains / Not Contains**

    Like a magnifying glass. It checks if a specific keyword exists anywhere in the text. This is what we are using today.
  * **Starts with / Ends with**

    Check if the text begins or ends with specific characters.
  * **Is Empty / Is Not Empty**

    Check if the variable has any content. For example: Checking if a user actually uploaded an attachment. Understanding these helps you set accurate and flexible rules, building a much smarter workflow!
</Info>

### Hands-On 2: Plan Different Paths

Now that we have the crossroad here, we need to decide what happens on each road.

#### A. The Dify-Related Email Track (IF Branch)

Click the **plus (+)** icon on the right side of the IF branch, drag out a line, and connect it to **Knowledge Retrieval** node.

What this means: When the email contains the word Dify, the flow will execute the professional reply process we built in the last lesson (which looks up information in the Knowledge Base).

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-connectifbranch.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=bdbec92caf6eb7b18c99bca6eb0cacb8" alt="Connect IF Branch" width="1260" height="131" data-path="images/difyworkflow101-lesson05-connectifbranch.png" />
</Frame>

#### B. The Unrelated Email Track (ELSE Branch)

For emails that are not related or mention Dify, we want to create a simple, polite, and general reply process.

<Steps>
  <Step title="Create a new Node">
    Click the **(+)** next to ELSE and select a new **LLM Node (LLM 2)**
  </Step>

  <Step title="Add Prompt to this LLM node">
    Copy and paste the prompt below

    ```plaintext wrap theme={null}
    You are a professional customer service manager. Based on the customer's email, kindly inform the user that no relevant information was found and provide relevant guidance.

    Requirements:
    1. Address the customer name in a friendly tone.
    2. Thank them for their letter.
    3. Keep the tone professional and friendly.
    4. Sign off as "Anne."
    ```
  </Step>

  <Step title="Add User Message">
    1. Click **Add Message** button below system.
    2. In the User Message box, type **customer name:**.
    3. Press `/` on your keyboard.
    4. You can see the Variable Selection menu pops out, and click `customer_name`.
    5. Press Enter to start a new line, and type **email content:**
    6. Press the / key again and click on `email_content`.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-finalpromptforllm2.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=d1f138a43e0cb763e7164d975260ceb7" alt="Prompt for LLM 2" width="860" height="670" data-path="images/difyworkflow101-lesson05-finalpromptforllm2.png" />
    </Frame>
  </Step>
</Steps>

Now we have two tracks generating two different replies. Imagine if we had 10 tracks, our workflow would look like a messy plate of spaghetti.

To keep things clean, we use a Variable Aggregator. Think of it as a Traffic Hub where all the different roads merge back into one main highway.

## Variable Aggregator

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-variableaggregator.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=8358bd3a6cf6c51b0d046584a5db42f4" alt="Variable Aggregator" width="449" height="221" data-path="images/difyworkflow101-lesson05-variableaggregator.png" />
</Frame>

Variable Aggregator is like a traffic hub where all the different roads merge back into one main highway.

### Hands-On 3: Add Variable Aggregator

<Steps>
  <Step title="Add the Aggregator">
    1. Select the connection line between the End Node and the LLM node and delete it.
    2. Right-click on the canvas, select **Add Node**, and choose the **Variable Aggregator** node.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-addvariableaggregator.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=eca3dde9146bc1df3d3aa5791840c6ea" alt="Add Variable Aggregator" width="910" height="472" data-path="images/difyworkflow101-lesson05-addvariableaggregator.png" />
    </Frame>
  </Step>

  <Step title="Merge the Paths">
    Connect LLM and LLM 2 node to the Variable Aggregator.
  </Step>

  <Step title="Assign the Output">
    1. Click the Variable Aggregator node.
    2. Click the **plus (+)** icon next to **Assign Variables**.
    3. Select the **text** from LLM 1 AND the **text** from LLM 2.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-assignvariable.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=dff84354a7e8afccc6c76e8d68793c5f" alt="Assign Variable" width="826" height="840" data-path="images/difyworkflow101-lesson05-assignvariable.png" />
    </Frame>

    Now, no matter which LLM node generates the response, the Variable Aggregator node gathers the content and hands it to the Output Node.
  </Step>

  <Step title="The Final Step">
    1. Connect the Variable Aggregator to the Output node.
    2. Update the Output Variable to the Variable Aggregator's result instead of previous LLM results.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-updateoutputvariable.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=12783d0414315afb2c9739c618704bc0" alt="Update Output Variable" width="826" height="478" data-path="images/difyworkflow101-lesson05-updateoutputvariable.png" />
    </Frame>

    Here's how the workflow looks:

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson05-finalworkflow.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=01c59f2beadad24f67e718cb0e521259" alt="Final Workflow" width="2300" height="428" data-path="images/difyworkflow101-lesson05-finalworkflow.png" />
    </Frame>
  </Step>

  <Step title="Test and Run">
    Click **Test Run**, enter a customer name, and try testing with inputs that both include and exclude the keyword Dify to see the different results.
  </Step>
</Steps>

## Mini Challenge

For business inquiry emails, how should we edit this workflow to generate proper response?

<Tip>
  Don't forget to update knowledge base with business-related files.
</Tip>


Built with [Mintlify](https://mintlify.com).