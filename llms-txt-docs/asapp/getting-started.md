# Source: https://docs.asapp.com/generativeagent/getting-started.md

# Source: https://docs.asapp.com/autosummary/getting-started.md

# Source: https://docs.asapp.com/generativeagent/getting-started.md

# Getting Started

To get started with GenerativeAgent, let's create a GenerativeAgent that can help a customer from your knowledge base. By the end, you'll have a working GenerativeAgent that can answer customer questions using your own content.

<Note>
  This is a basic example to get you started quickly. As you develop more sophisticated GenerativeAgent solutions, you'll want to explore [additional use cases](/generativeagent/build/adding-a-use-case) and consider the [comprehensive design](/generativeagent/build-overview) of your implementation.
</Note>

## Before you begin

Before you begin, make sure you have:

* Followed the [Set up your account](/getting-started/setup) guide to get access to the ASAPP AI Console.
* A customer-facing knowledge base URL (such as your help center or support documentation)

## Step 1: Connect Your Knowledge Base

The first step is to import your knowledge base content so GenerativeAgent can use it to answer customer questions.

We will use the Import from URL to import your knowledge base content but you have other options on how to [connect your knowledge base](/generativeagent/configuring/connecting-your-knowledge-base).

<Steps>
  <Step title="Navigate to 'GenerativeAgent > Knowledge' in the AI Console" />

  <Step title="Click 'Add content' and select 'Import from URL'">
    <Frame>
      <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=f38db99a6a736c50832f5be91b581fa9" alt="Import from URL" data-og-width="678" width="678" data-og-height="292" height="292" data-path="images/generativeagent/getting-started/import-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=280&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=d6e28412897daa4422fe3be5673864c7 280w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=560&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=55c23f6ffbc31eab59489e5c95aa4dd3 560w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=840&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=b80874bf801cf7bec3dc7ce7df3cece0 840w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=1100&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=7f8c998368271be05b55233971f2e25b 1100w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=1650&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=a92e3e4c3e9312b8e914f7f4b0bde529 1650w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/import-url.png?w=2500&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=6b196116bc7fe97378dd025a6f7afb69 2500w" />
    </Frame>
  </Step>

  <Step title="Enter your knowledge base URL in the 'External content URL' field">
    Optionally, you can import specific sections of your site by specifying [allowed URL Prefix or Excluded URLs](/generativeagent/configuring/connecting-your-knowledge-base#step-1%3A-importing-your-knowledge-base).
  </Step>

  <Step title="Click 'Import content' to start the process">
    Your content will be imported and placed in a **Pending Review** state.
  </Step>
</Steps>

## Step 2: Review and Publish Your Content

After crawling your knowledge base, we will create a list of articles that could be added to the GenerativeAgent knowledge base.

You need to review and publish the articles:

<Steps>
  <Step title="Look for the notification">
    At the top of the Knowledge Base page, look for the notification indicating articles need review.

    <Frame>
      <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=634df9e3941bec57684f2b7adcec8ee5" alt="New notification" data-og-width="737" width="737" data-og-height="284" height="284" data-path="images/generativeagent/getting-started/new-notification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=280&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=9fdfd4c033680897248cbc9851eb6835 280w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=560&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=182cb870174121c8ebcee1ef63a0a0d0 560w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=840&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=5763bd40307aabaf7fadd5f44f152b4d 840w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=1100&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=52c5910861aa6ab06f4e1693cbf30160 1100w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=1650&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=39739b7d39cdbf7da16959c89b7a1fac 1650w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/new-notification.png?w=2500&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=50c4c7e690535490f59cfb2bb7882f54 2500w" />
    </Frame>
  </Step>

  <Step title="Click to review the imported articles" />

  <Step title="Review each article:">
    For each article:

    * Choose between the cleaned-up or raw version
    * Add relevant query examples that customers might ask (e.g., "What is your return policy?")
    * Click **Publish** when you're satisfied with the content
  </Step>
</Steps>

## Step 3: Create a Basic Task

Now that your knowledge base is set up, let's create a simple task for GenerativeAgent to handle customer inquiries.

A task is a set of instructions that tells GenerativeAgent what to do. We go into more detail about tasks and functions in the [Learn More About Tasks and Functions](/generativeagent/configuring) guide.

<Steps>
  <Step title="Navigate to 'GenerativeAgent > Tasks'" />

  <Step title="Click 'Create task'" />

  <Step title="Define the task">
    Here we provide sample names and instructions, but you are in full control of GenerativeAgent's behavior and can customize them to fit your needs.

    Fill in the following fields:

    * **Task name**: "Answer\_Customer\_Questions"
    * **Task selector description**: "Use this task when customers ask questions about our products, services, or policies."
    * **General Instructions**: "Answer customer questions clearly and concisely using information from the knowledge base. If the answer isn't in the knowledge base, politely explain that you don't have that information and offer to help them find other information."

    <Frame>
      <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=6fe52f0b70a1030edb19a788b87adc5b" alt="Dashboard Create task" data-og-width="1202" width="1202" data-og-height="507" height="507" data-path="images/generativeagent/getting-started/create-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=280&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=857fdb3b4fab44a3ffa1b8abf51bd3c6 280w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=560&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=d0b2962eccd2bcd8f7ce3031f457817c 560w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=840&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=2bdd59b47484f9e6e9d7e9487f48eef3 840w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=1100&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=446cc897b2d9448a2a48f737d7ece00e 1100w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=1650&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=02bdfb9f76341877fbf8155de92e219b 1650w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/create-task.png?w=2500&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=38b1834e5b96fdc6ed167c1c2781197f 2500w" />
    </Frame>
  </Step>

  <Step title="Save the task" />
</Steps>

## Step 4: Try It Out in the Previewer

Now let's test your GenerativeAgent with the [Previewer](/generativeagent/configuring/previewer):

1. Navigate to **GenerativeAgent > Previewer**
2. Select **Draft** environment from the dropdown
3. Type a test question related to your knowledge base content (e.g., "What is your return policy?")
4. Send the message and observe GenerativeAgent's response
5. Use the Turn Inspector panel on the right to see which knowledge base articles were used and how GenerativeAgent processed the request

<Frame>
  <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=6c80e7762e3e8ea2885a4b1e63630364" alt="The previewer side panel" data-og-width="1209" width="1209" data-og-height="673" height="673" data-path="images/generativeagent/getting-started/try-out-previewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=280&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=733b9cf2d08713422fe7aa5bf6eb42ad 280w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=560&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=988c3ef189a9c60da9216b23eda36632 560w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=840&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=620d4e7794cfadc0a64fe00dfde8f9f1 840w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=1100&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=ceee1b86cfac0acf81d14184cd237a40 1100w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=1650&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=ce98c2c6d751322a4424fc816c857599 1650w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/getting-started/try-out-previewer.png?w=2500&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=1e1fba185d3861977151983b28d0d80c 2500w" />
</Frame>

## Safety

GenerativeAgent is has been developed with a safety-first approach.

ASAPP ensures GenerativeAgent's accuracy and quality with rigorous testing and continuous updates, preventing hallucinations through advanced validation. Our team has incorporated Safety Layers that provide benefits such as reliability and response trust.

Our safety standards include:

* Safety Layers
* Hallucination Control
* Data Redaction
* IP Blocking
* Customer Info and Sensitive Data Protection

<Tip>
  You can learn more about this in [Safety and Troubleshooting](/generativeagent/configuring/safety-and-troubleshooting).
</Tip>

## What's Next

Congratulations on setting up a basic GenerativeAgent to answer customer questions using your knowledge base!

Now that you have a working GenerativeAgent, here are the recommended next steps to understand GenerativeAgent more holistically and build a complete solution:

<CardGroup>
  <Card title="Build Overview" href="/generativeagent/build-overview">
    Get a comprehensive understanding of how GenerativeAgent works and the complete build process.
  </Card>

  <Card title="Adding a Use Case" href="/generativeagent/build/adding-a-use-case">
    Learn how to design and implement specific use cases for your contact center needs.
  </Card>

  <Card title="Previewer" href="/generativeagent/configuring/previewer">
    Test and refine your GenerativeAgent before deploying to production.
  </Card>

  <Card title="Integrate" href="/generativeagent/integrate">
    Connect your CCaaS and backend systems to create a complete GenerativeAgent solution.
  </Card>
</CardGroup>
