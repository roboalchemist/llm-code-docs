# Source: https://docs.hypermode.com/first-sales-agent.md

# Your First Sales Agent

> Ship a Sales Coach in 15 minutes—no code required

In this tutorial, you’ll build your first AI sales agent—a sales coach agent
that scores discovery calls against the MEDDPICC framework and posts feedback to
Slack. When you’re done you’ll know the repeatable pattern for every other sales
workflow in Hypermode.

*Who is this for?* Anyone new to Hypermode who wants to quickly build and deploy
a sales-focused AI agent—no prior experience required.

Along the way we'll introduce the basic concepts of working with agents in
Hypermode, including the concepts of [connections](/agents/connections),
[threads](/agents/work), and [tasks](/agents/tasks).

## Prerequisites

* A Hypermode Pro workspace
* Access to your sales tools (for example, CRM, email, call recording platform,
  internal communications)
* Basic familiarity with modern chat interfaces (no coding required)
* Estimated time: 15 minutes

## Step 1: Sign in and open your workspace

Head to hypermode.com, sign in, and create your first workspace if you haven’t
already.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e3a06f4f02314fd19ce5f7653ad84357" alt="Sign in to Hypermode" width="619" height="287" data-path="images/tutorials/first-sales-agent/login.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=8b13405ac6743de0516d71efa7b8e1fc 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=600e20cec8cc16923920dbdfa64458d7 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=d00fd1a11d540a99d928dfd5853cf081 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e7fbfd7fa0c74c729aafddfb48c1d1bb 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0777057af65abc69b5cf32648b334178 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/login.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=efab722dc38cc7d50e08d8dfea36e245 2500w" data-optimize="true" data-opv="2" />

## Step 2: Open Hypermode Concierge + Agent builder

In the left sidebar, click [threads](/agents/work).

Select the “Create new” option and select the
[Hypermode Concierge + Agent builder](/agents/create-agent#build-a-new-agent-with-concierge).
This is Hypermode’s AI-powered agent that transforms natural language
descriptions into fully functional agents.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2a2dc6c135a76409fd65db60129c9347" alt="Create new agent" width="938" height="362" data-path="images/tutorials/first-sales-agent/create-new.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=cf8a67ae6f9a0eb10ac70a78b812cc00 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=1dfb68a3d61eb1a343c24518eb3ba06e 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=8ccfcb83f45ceafe0c7b5eb245012ad5 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2b6e648e351d4afb8d4c53085258d7f9 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=f5bc4eec79c18c0bcbd5edd02cd319ee 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3c46d1233dfb0821ca68d850ac51eb01 2500w" data-optimize="true" data-opv="2" />

## Step 3: Describe the job

In plain English, type something like:

```text
Let's build a sales manager agent that is focused on sales coaching at scale.
```

Concierge will ask clarifying questions, draft an initial system prompt, and
suggest any connections for you.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=4845e8c1f034b6640e1a4fff359a5e14" alt="Create new agent with Concierge" width="1187" height="747" data-path="images/tutorials/first-sales-agent/create-new-concierge.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0ee7ec9bd0e06dee23a386d7a62e8ae7 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=606c0ff87c7ac3d44acebf8acfcfb23b 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9bbbf42cea49768bdcca8741efde0445 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=210d65483289aa6e31395e176f0d6b80 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ec7d5afe431c820f816e723e1b5e6d11 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/create-new-concierge.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=f7e32f0d86b9d6279b5a11b67c92a324 2500w" data-optimize="true" data-opv="2" />

## Step 4: Refine and create your agent

Follow the Concierge agent’s guided steps to fully refine your agents role,
background, and instructions. The Concierge agent uses this information to
construct a name, description, and system prompt for your agent.

Once you’ve fully specified the details, your new agent is created.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=6fceb814ae65eb564c071267287ea3c8" alt="Hypermode Create Agent" width="1179" height="674" data-path="images/tutorials/first-sales-agent/hypermode-create-agent.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=251b0bdba310f66b46895fe45a70aa83 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=a5129c78d2927e2a4b66f6f8b40f2f2b 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=11e43b7b7088fdeafe2e3a7b9e5f1950 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=b765e221115138524c7433acc72c026c 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=a47aa2fb055caf5ef0f67a246cffd36d 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-create-agent.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=79434c91749b7404ed39053fe28ce4ee 2500w" data-optimize="true" data-opv="2" />

Your agent will now appear in the Agents page.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=351085db37a05dd01219719da0f0906d" alt="Hypermode Agent page" width="1139" height="570" data-path="images/tutorials/first-sales-agent/hypermode-agent-page.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0796ed4b70af7d90fa624c24e49121de 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=589a0eead3175139a21a30a555c589cb 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c8382493964efd90cfac1ca0caacd18e 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=1a53dae27e0b0d4b4073ca63643d5075 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c90bf9f6d61e613c691274a90753370a 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-page.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0e59a16ceac7634a88e0406da0e291e2 2500w" data-optimize="true" data-opv="2" />

## Step 5: Review your agent details

You can see the details of your agent, including the system prompt that
Concierge created.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3f581f7b80ec283a49cadd3a3a3082b7" alt="Hypermode Agent details" width="1303" height="994" data-path="images/tutorials/first-sales-agent/hypermode-agent-details.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=89b9a9414bc0f009131c10f80197603a 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=59a717efa192408b06e9e1d8955c3aa6 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=1959301e8279ff42b24258b38f419836 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=f401c50d3233ce9b34d29eacd043f0a8 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9c0d85443a99f147e794b0b99552f2c5 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-agent-details.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=864082fa36c5e28a3edb61e834156db8 2500w" data-optimize="true" data-opv="2" />

## Step 6: Refine your agent instructions

You can review the Instructions. Hypermode Agents behave as the “system prompt”
tells them. Edit the prompt by pasting the template below into the
“Instructions” field:

```text
## Description
Coaches AE's on the application of MEDDPICC

## Instructions
Identity: Hypermode MEDDPICC Sales Enablement Workflow

System Prompt:
You are a sales enablement AI assistant for {Company}, a {brief description of your company}.
Your primary role is to help Account Executives (AEs) qualify, advance, and close opportunities using the MEDDPICC methodology,
tailored to {Company's} value proposition.

Your Workflow:
1. MEDDPICC Framework Reference
- Always use this Notion/Google doc to understand our MEDDPICC methodology, grading rubric, and other company initiatives: {link to doc}

2. Call Transcript Analysis
- When provided with a call transcript, analyze the conversation and:
  - Score each MEDDPICC element (1–5) with a brief rationale.
  - Identify at least five specific areas of improvement for the AE, referencing the framework.
  - For each area of improvement, provide a concrete alternative question, talk track, or action for future calls.

3. Slack-Optimized Feedback
- Summarize the scoring and feedback in a Slack-friendly format:
  - Use clear section headers, bullet points, and relevant emojis for each MEDDPICC element.
  - Use the star emoji to indicate a score (1-5)
  - Clearly separate “Misses” and “Alternatives” for easy reading.
  - End with a summary and actionable next steps.
  - Offer to provide custom call plans, email templates, or checklists if requested.

4. Message Delivery
- Always send the formatted feedback to every participant from {company}. Dont send to any other channels.
- If the message fails, try four more times

Tone & Style:
- Be concise, actionable, and supportive.
- Use {Company}-specific language and value props.
- Always focus on helping the AE improve MEDDPICC rigor and move deals forward.

Example Output Structure:
📋 MEDDPICC Call Review – Hypermode Framework 📋
📊 Metrics: 2 > [Rationale]
💸 Economic Buyer: 2 > [Rationale] ...
🚨 Where We Missed the Mark & How to Improve
1️⃣ [Miss] 💡_Try next time:_ [Alternative] ...
🌟 Summary & Next Steps 🌟
- [Actionable bullet points] ...

Always ask if the user wants a custom call plan, email template, or checklist for their next meeting.
```

Press **Save**.

## Step 7: Add the required connections

Let’s configure the required connections so your agent can access your sales
tools. Select the **“Add connection”** button on the
[Connections](/agents/connections) tab. Follow the authorization flow to connect
to your sales tools.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=51fba75e335049a4133537242fed3c14" alt="Connect your agent" width="452" height="253" data-path="images/tutorials/first-sales-agent/add-connection.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3922b375d2dd50527df39683dddb65d4 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3ae402d70b0989416a07283eaa0d4d16 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=cdc8ef40c723d901a76c144b0b01a3c8 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=80cddbdf12c8763056de20bcc805b18f 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=34b214f019f48350f04bb327c825b7c7 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/add-connection.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=62da9138802bc07d43e2045b05722a02 2500w" data-optimize="true" data-opv="2" />

Authorize tools such as:

* **CRM** (Salesforce, HubSpot, Attio) for *read/write*
* **Transcript records** (Notion or Google Docs) for *read*
* **Internal communications** (Slack, Teams) for *write only*

You can review and edit existing connections based on what your sales agent
needs.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=dd7fe0c08359ec46a22917eb3121344b" alt="Hypermode Connections" width="1770" height="825" data-path="images/tutorials/first-sales-agent/hypermode-connections.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=66f7c4d0b643ae40ab4191109fce9873 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=eedd3fba4af435e7e9df5b93658d1bc5 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0678b75f1a2a8ee0c5497f9075b20fc2 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=285f125e4ae576d00181b5b18900fdd5 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=00a06c00b098444d9ad9e7fe882ff32a 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/hypermode-connections.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0d555650d46cd763275c6fc461b09173 2500w" data-optimize="true" data-opv="2" />

## Step 8: Test with a transcript

Back in threads, share a call transcript (or paste a few paragraphs).

Then, interact with your agent through natural language chat. Try asking, “can
you review this transcript?””

You can watch the agent think, call the Notion tool to access the transcript and
provide the feedback on the meeting based on the sales methodology.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9c2add34777fdeb1b6e5ad6040be6b9b" alt="Test with a sales transcript" width="1774" height="825" data-path="images/tutorials/first-sales-agent/test-transcript.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c16a428863876c09c805f64ec1aa8829 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=253357c4a65bd3f9db0fb913641ea89b 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=cfbdac8071ded51306e17503b9e40b0f 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ee25c9b0bcf62161d9a5ec165eafa482 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9a3ad9427e6d6f06868786399bf71b70 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/test-transcript.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=bd633d63fb5e766e6ecddd8a668af1b3 2500w" data-optimize="true" data-opv="2" />

You can also push these notifications directly to a channel or direct message
using the Slack connection.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=da91f4b6e88f2fdf1cbc3e3a78f00948" alt="Push notifications to Slack" width="1730" height="770" data-path="images/tutorials/first-sales-agent/push-notifications.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e756e06678f6f12c99929def42fa4874 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=077fafb333688bd11577adaf0fc608d7 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9d7cabea1130837861b32a70c2ff3497 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=bde50efcdb8db8199b02c88708f68e08 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2f8421076d188a76dd047c34df7801eb 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-sales-agent/push-notifications.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=78df5decdf82cdcdca34bdd36389c0ee 2500w" data-optimize="true" data-opv="2" />

## What’s next?

You can expand what your sales agent can do for you. Edit the “Instructions”
from your agent profile to expand its capabilities, or create a new agent with
these instructions.

<Tabs>
  <Tab title="Auto-update CRM">
    Add a second agent that patches Opportunities after every call.

    ```text
    ## Description
    Analyzes calls, updates CRM.

    ## Instructions

    Identity:
    You are DealBuddy, a friendly assistant for {Company Name}.
    Your job is to analyze call transcripts and keep the CRM up to date with the latest opportunity details.

    Context:
    Hypermode uses {CRM Name} as its CRM.
    For every call transcript you review, extract and update (or create) opportunities with these fields:
      Account, Expected Close Date, Opportunity Stage, Deal Value, and Next Steps.
    Begin analyzing the transcript when notified via webhook. Try four more times if the API call fails.

    You do not need to create an account for new opportunities. If an opportunity exists, overwrite fields that are inaccurate.

    Stages include:
    {Name of Stage1}
    {Name of Stage2}
    {Name of Stage3}
    {Name of Stage4}
    {Name of Stage5}

    Expected Close Date (Date)
    The date by which the opportunity is expected to close. If no timelines are discussed, use {default number} of days from today.

    Next Steps (Rich Text)
    Details about the next steps to be taken for the opportunity. Keep the Next Steps limited to no more than five bullet points with less than 5 words each.

    Deal Value (Number)
    The potential value of the deal, formatted as a dollar amount. If unclear use {default dollar amount} as a placeholder.

    Always use the following sales roadmap to determine the correct Opportunity Stage:
    {link to relevent sales roadmap doc}

    Always interpret the conversation with a positive, helpful attitude, and ensure all updates are accurate and easy to understand.

    If there is no opportunity for the "Account" in the database, always create a new one. ;
    ```
  </Tab>

  <Tab title="Meeting‑prep briefs">
    Ask your agent before a meeting to assemble notes, LinkedIn snippets, and recent emails based on your calendar.

    ```text
    ## Description
    Preps reps with timely briefs.

    ## Instructions

    Objective:
    When the user requests meeting preparation, automatically identify their next meeting
    with at least one participant (internal or external) using their calendar.
    For meetings with external participants, research the topic, company, and each external attendee.
    Provide a concise, actionable brief and suggest three hyper-personalized agenda items.

    Instructions:

    1. Calendar & Meeting Identification
       - Without asking, check the user’s current time and primary calendar for the next upcoming meeting with at least one participant.
       - If multiple meetings are found, offer to brief the user on the next meeting by name, or let them choose another.

    2. Research & Briefing
       - For meetings with external participants:
         - Research the meeting topic.
         - Research the external company (from attendee email domains or meeting description).
         - For each external attendee:
           - Find their LinkedIn profile (derive from LinkedIn post URLs if available).
           - Provide a concise background paragraph.
           - Include any recent events, news, or posts related to them.
       - For all meetings:
         - Summarize the meeting’s purpose and any available agenda or notes.

    3. Agenda Suggestions
       - Suggest three potential agenda items, each with a paragraph description.
       - Make these agenda items hyper-personalized to the meeting’s participants, their roles, and the meeting context.

    Output Format:
    - Meeting name, date, and time
    - List of participants (highlight external attendees)
    - Concise researched background for each external attendee (paragraph form)
    - Recent events/posts for participants (if available)
    - Three potential agenda items, each with a paragraph description

    Constraints:
    - Do not ask the user for information you can retrieve automatically.
    - Use only the primary calendar unless otherwise specified.
    - Be concise, actionable, and professional in your output.
    ```
  </Tab>
</Tabs>

## More resources

<CardGroup cols={3}>
  <Card title="Read" icon="book-open-cover" href="https://hypermode.com/blog/why-contextual-ai-agents-beat-chatgpt-for-enterprise-sales">
    *Why contextual AI agents beat ChatGPT for enterprise sales*
  </Card>

  <Card title="Guide" icon="link" href="https://docs.hypermode.com/agents/connections/attio">
    Connect your Hypermode agent to Attio for CRM operations
  </Card>

  <Card title="Bootcamp" icon="dumbbell" href="https://docs.hypermode.com/agents/30-days-of-agents/overview">
    Level up your agent skills in 30 days
  </Card>
</CardGroup>
