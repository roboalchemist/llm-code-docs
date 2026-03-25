# Source: https://docs.dify.ai/en/use-dify/tutorials/workflow-101/lesson-08.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lesson 8: The Agent Node

Let's look back the upgrades we've made for our email assistants.

* Learned to Read: It can search a Knowledge Base
* Learned to Choose: It uses Conditions to make decisions
* Learned to Multitask: It handles multiple questions via Iteration
* Learned to Use Tools: It can access the Internet via Google Search

You might have noticed that our workflow is no longer just a straight line (Step 1 → Step 2 → Step 3).

It's becoming a system that analyzes, judges, and calls upon different abilities to solve problems. This advanced pattern is what we call an Agentic Workflow.

## Agentic Workflow

An Agentic Workflow isn't just Input > Process > Output.

It involves thinking, planning, using tools, and adjusting based on results. It transforms the AI from a simple Executor (who just follows orders) into an intelligent Agent (who solves problems autonomously).

## Agent Strategies

To make Agents work smarter, researchers designed Strategies—think of these as different modes of thinking that guide the Agent.

* **ReAct (Reason + Act)**

  The Think, then Do approach. The Agent thinks (What should I do?), acts (calls a tool), observes the result, and then thinks again. It loops until the job is done.
* **Plan-and-Execute**

  Make a full plan first, then do it step-by-step.
* **Chain of Thought (CoT)**

  Writing out the reasoning steps before giving an answer to improve accuracy.
* **Self-Correction**

  Checking its own work and fixing mistakes.
* **Memory**

  Equipping the Agent with short-term or long-term memory allows it to recall previous conversations or key details, enabling more coherent and personalized responses.

In Lesson 7, we manually built a Brain using Knowledge Retrieval -> LLM to Decide-> If/Else -> Search. It worked, but it was complicated to build.

Is there a simpler way? Yes, and here it is.

## Agent Node

The Agent Node is a highly packaged intelligent unit.

You just need to set a Goal for it through instructions and provide the Tools it might need. Then, it can autonomously think, plan, select, and call tools internally (using the selected Agent Strategy, such as ReAct, and the model's Function Calling capability) until it completes your set goal.

In Dify, this greatly simplifies the process of building complex Agentic Workflows.

## Hands-on 1: Build with Agent Node

Our goal is to replace that complex manual logic inside our Iteration loop with a single, smart Agent Node.

<Steps>
  <Step title="Clean up the Iteration">
    Go to the sub-process of the Iteration. Keep knowledge retrieval node, and delete other nodes in side it.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-iteration.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=ad64ffb128d0da484683f532f80f7915" alt="Iteration" width="1168" height="466" data-path="images/difyworkflow101-lesson08-iteration.png" />
    </Frame>
  </Step>

  <Step title="Add the Agent Node">
    Add an Agent node right after the Knowledge Retrieval node.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-addagentnode.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=ff7277126cac98b1752d9f9b441597ca" alt="Add Agent Node" width="1168" height="466" data-path="images/difyworkflow101-lesson08-addagentnode.png" />
    </Frame>
  </Step>

  <Step title="Install Agent Strategy">
    Since we haven't used this before, we need to install a strategy from the Marketplace.

    Click the Agent node. In the right panel, look for Agent Strategy. Click Find more in Marketplace.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-searchagentstrategy.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=2f792f181f91bae5af184292d9a31fd7" alt="Search Agent Strategy" width="1168" height="904" data-path="images/difyworkflow101-lesson08-searchagentstrategy.png" />
    </Frame>
  </Step>

  <Step title="Pick an Agent Strategy">
    In the Marketplace, find Dify Agent Strategy and install it.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-chooseagentnode.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=0aaaf8a2209277f70df516e478399f8e" alt="Choose Agent Strategy" width="2940" height="1000" data-path="images/difyworkflow101-lesson08-chooseagentnode.png" />
    </Frame>
  </Step>

  <Step title="Select ReAct">
    Back in your workflow (refresh if needed), select ReAct under Agent Strategy.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-selectreact.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=749e9f5fae48debdcc35f75df3488f96" alt="Select ReAct" width="1395" height="848" data-path="images/difyworkflow101-lesson08-selectreact.png" />
    </Frame>

    **Why ReAct here?**

    ReAct (Reason + Act) is a strategy that mimics human problem-solving using a Think → Do → Check loop.

    1. Reason: The Agent thinks, What should I do next? (e.g., Check the Knowledge Base).
    2. Act: It performs the action.
    3. Observe: It checks the result. If the answer isn't found, it repeats the cycle (e.g., Okay, I need to search Google).

    This thinking-while-doing approach is perfect for complex tasks where the next step depends on the previous result.
  </Step>

  <Step title="Choose a Model">
    ReAct is a thinking strategy, but to actually pull off the action part, AI needs the right "physical" skills which is called **Function Calling**. Select a model that supports Function Calling. Here, we choose gpt-5.

    **Why Function Calling?**

    One of the core capabilities of an Agent Node is to autonomously call tools. Function Calling is the key technology that allows the model to understand when and how to use the tools you provide (like Google Search).

    If the model doesn't support this feature, the Agent cannot effectively interact with tools and loses most of its autonomous decision-making capabilities.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-chooseamodel.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=a9e00a7533ec778019e10ef875779c03" alt="Choose a Model" width="1136" height="620" data-path="images/difyworkflow101-lesson08-chooseamodel.png" />
    </Frame>
  </Step>

  <Step title="Add Tool">
    Click Agent node. Click plus(+) icon in tool list and select Google Search.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-addtool.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=2ac3ec9f72ee63741de01182dd844d9d" alt="Add Tool" width="1136" height="810" data-path="images/difyworkflow101-lesson08-addtool.png" />
    </Frame>
  </Step>

  <Step title="Add Instructions">
    We need to tell the Agent specifically what to do with the tools and context we are giving it. Use and paste the instructions into the Instruction field:

    ```plaintext wrap theme={null}
    Goal: Answer user questions about Dify products.

    Steps:
    1. I have provided a relevant internal knowledge base retrieval result. First, judge if this result can fully answer the user's questions.
    2. If the context clearly answers it, generate the final answer based on the context.
    3. If the answer is insufficient or irrelevant, use the Google Search tool to find the latest information and generate the answer based on search results.

    Requirement: Keep the final answer concise and accurate.
    ```

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-addinstructions.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=f7a31e98567d2b55fe3a95062e6b4a89" alt="Add Instructions" width="1106" height="940" data-path="images/difyworkflow101-lesson08-addinstructions.png" />
    </Frame>
  </Step>

  <Step title="Context and Query">
    Your configuration here is crucial for the Agent to see the data.

    * **Context**: Select `Knowledge Retrieval / (x) result Array[Object]` from the Knowledge Retrieval node (This passes the knowledge base content to the Agent).
    * **Query**: Select `Iteration/{x} item` from the Iteration node.

    **Why item instead of the original email\_content?**

    We used the Parameter Extractor to extract a list of questions (`question_list`) from the `email_content`. The Iteration node is processing this list one by one, where item represents the specific question currently being handled.

    Using item as the query input allows Agent to focus on the current task, improving the accuracy of decision-making and actions.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-contextandquery.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=c6c28a18d422e13d525cfa8494d63e79" alt="Context and Query" width="1106" height="346" data-path="images/difyworkflow101-lesson08-contextandquery.png" />
    </Frame>
  </Step>

  <Step title="Set Iteration Output">
    Click `Agent/{x}text String` as the output variables.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-iterationoutput.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=be7bfa83e2d27fcde806ea85d2dda09c" alt="Set Iteration Output" width="1150" height="594" data-path="images/difyworkflow101-lesson08-iterationoutput.png" />
    </Frame>
  </Step>
</Steps>

<Check>
  🎉 The Iteration node is now upgraded.
</Check>

Since the Iteration node generates a list of answers, we need to stitch them back together into one email.

## Hands-on 2: Final Assembly

<Steps>
  <Step title="The Final Editor (LLM)">
    1. Add an LLM node after the Iteration node.
    2. Click on it and add prompt into the system. Feel free to check on the prompt below, or edit by yourself.

       ```plaintext wrap theme={null}
       Combine all answers for the original email.
       Write a complete, clear, and friendly reply to the customer.
       Signature: Anne
       ```
    3. Add user message to replace answers, email content and customer name with variables respectively. Here's how the LLM looks like right now.

       <Frame>
           <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-finalllm.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=c8180caf21decdaedb326162cab0ce69" alt="Final LLM" width="1492" height="1024" data-path="images/difyworkflow101-lesson08-finalllm.png" />
       </Frame>
  </Step>

  <Step title="Add Output Node">
    Set the output variable to the LLM's text and name it `email_reply`.

    <Frame>
            <img src="https://mintcdn.com/dify-6c0370d8/WgJjOgES2eUiT-XF/images/difyworkflow101-lesson08-addoutputnode.png?fit=max&auto=format&n=WgJjOgES2eUiT-XF&q=85&s=b002fd5b00932d29b4115862635f83ee" alt="Add Output Node" width="1106" height="450" data-path="images/difyworkflow101-lesson08-addoutputnode.png" />
    </Frame>
  </Step>
</Steps>

Here comes the final workflow.

<Frame>
    <img src="https://mintcdn.com/dify-6c0370d8/zfXwSj_rDFo02Qjb/images/difyworkflow101-lesson08-finalworkflow.png?fit=max&auto=format&n=zfXwSj_rDFo02Qjb&q=85&s=83be31bdafecbc7f9dd222181c6d6bfc" alt="Final Workflow" width="2466" height="488" data-path="images/difyworkflow101-lesson08-finalworkflow.png" />
</Frame>

Click **Test Run**. Ask a mix of questions. Watch how the Agent Node autonomously decides when to use the context and when to use Google search.

## Mini Challenge

1. Could we use an Agent Node to replace the entire Iteration loop? How would you design the prompt to handle a list of questions all at once?
2. What other information could you feed into the Agent's Context field to help it make better decisions?


Built with [Mintlify](https://mintlify.com).