# Source: https://docs.base44.com/Building-your-app/AI-chat-modes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the AI Chat in Base44

> Describe your idea, and the AI builds it for you. Use chat modes and AI controls to fine-tune your app and get the results you want.

## About the AI chat

The Base44 AI chat is more than just a code generator. It works as your intelligent assistant, understands your goal, and uses the right tools to get you there. Your apps become more accurate, context-aware, and flexible, so you can focus on building complex features quickly, with smart automation working in the background.

Unlike traditional AI that only responds with text, the agentic AI knows when to search the web, check your files, or pull in data from other sources. It also uses automatic model selection to choose state-of-the-art models based on what your prompt needs, so you get real solutions without needing to manage models or technical details yourself.

<Card color="#FF983C" icon="lightbulb-exclamation-on" title="What does this mean in practice? Here are some examples:">
  * Share a public website link with the chat to instantly copy the design, layout, and visible content into your app. For example: “Copy the layout from `https://example.com`.”
  * Ask the agent to help you follow best practices by searching for ready-made code or common solutions. For example: “Show me the standard pattern for user authentication.”
  * Pull lists or content from other websites and use it in your app, such as importing product catalogs or gathering site text and images. For example: “Import the product list from `https://example.com`.”
  * Directly update your app’s database with simple, clear instructions. For example: “Give Emily a point for doing her homework.”
</Card>

The AI chat also suggests useful next steps as you build. These suggestions appear below the chat and are tailored to your current workflow, helping you discover new features and make the most of your app.

<img src="https://mintcdn.com/base44/qWZBi826o5-9eVfw/images/2025-10-30_14-48-411.png?fit=max&auto=format&n=qWZBi826o5-9eVfw&q=85&s=58b9d65fe56b446b4711ea8c619d9b8a" alt="AI chat providing suggestions for next steps as you build your app." width="1608" height="1132" data-path="images/2025-10-30_14-48-411.png" />

***

## Using the AI chat modes

When you are building your app, there are 3 chat modes:

* **Default:** Acts instantly on your prompts.
* **Discuss:** Lets you plan and refine ideas safely before applying changes.
* **Visual Edit:** Lets you click elements in your preview to adjust visuals directly.

You can switch between modes anytime to brainstorm ideas, make design tweaks, or apply instant changes, all in one chat.

### Default mode

Type what you need, and the AI acts right away. This mode is perfect for quick edits and feature requests. To get the best results, be as specific as possible. The more detail you give, the more precisely the AI builds your app.

> **For example:** Create a fitness tracking app for busy professionals who only have 20 minutes a day to exercise. Help them log short workouts and track weekly progress.

<img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/AIchatfitnessapp.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=3b6a3656b6b007013db9edf2e6126953" alt="Example of creating a fitness app with the AI chat." className="mx-auto" style={{ width:"80%" }} width="1746" height="852" data-path="images/AIchatfitnessapp.png" />

<Tip>
  For more examples and prompt frameworks, check out the [<u>Prompt Guide</u>](/Getting-Started/Prompt-guide).
</Tip>

### Discuss mode

Click **Discuss** in the AI chat to have a conversation with the AI to brainstorm, clarify, or explore ideas before making any changes to your app. It is a safe space to ask questions, get suggestions, or talk through options without affecting your project. In Discuss mode, you can freely chat and refine your goals with the AI, but no app changes take place. Each message in Discuss mode uses 0.3 credits.

Once you are ready for the AI to implement changes in your app, turn off **Discuss** and ask the AI to make the changes.

> **For example:** Discuss the best way to structure the workout logging flow for your fitness tracking app. Should people enter workouts manually or choose from preset options?

<img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/AIDiscussMode.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=36d5089a963f0b0f7803a5ce3c974c1a" alt="Using Discuss mode in the Base44 AI chat to plan and refine ideas before making changes." className="mx-auto" style={{ width:"80%" }} title="Using Discuss mode in the Base44 AI chat to plan and refine ideas before making changes." width="825" height="867" data-path="images/AIDiscussMode.png" />

<Tip>
  Discuss mode helps you save credits by avoiding unnecessary trial and error before finalizing changes.
</Tip>

### Visual Edit mode

Use **Visual Edit** to make changes to the design of your app. You can do it manually or ask the AI to make the changes for you.

**To make changes to the design of your app:**

1. Go to the AI chat in your app editor.
2. Click **Visual Edit**.
3. Make changes to the design:
   * **Manually:** Select an element in your app preview to make the changes directly. For example, you can change background colors, text colors, or spacing. You can also quickly access the element's code to make changes, adjust tailwind classes directly to fine-tune spacing, typography, layout, and responsiveness, or remove the selected element or section with the **Delete** icon in the Visual Edit toolbar. This method does not use credits.

     <img src="https://mintcdn.com/base44/SAWAxSekZl32mUAN/images/visualedit.png?fit=max&auto=format&n=SAWAxSekZl32mUAN&q=85&s=bd57fbd7e6915be585b277fccf5ac2dd" alt="Manual Visual Edit to make design changes in Base44" title="Manual Visual Edit to make design changes in Base44" style={{ width:"85%" }} width="1758" height="865" data-path="images/visualedit.png" />
   * **Using the AI chat:** Select an element in the app preview and then ask the AI chat to make the changes. The AI automatically knows which element you selected. This method uses message credits. The number of credits depends on the size and complexity of the change.

     <img src="https://mintcdn.com/base44/XO15fdr3TGKz2psR/images/visualeditsviaAI.png?fit=max&auto=format&n=XO15fdr3TGKz2psR&q=85&s=e2840debb5c0fd2a1a0f7d8aa70faaa7" alt="Visual Edit using the AI chat in Base44" width="1416" height="283" data-path="images/visualeditsviaAI.png" />

<Tip>
  If you have multiple elements that repeat, you can apply bulk changes to them. Click the element and all repeating elements are highlighted, so you can apply changes to all of them at once.

    <img src="https://mintcdn.com/base44/VZaHE3DGMgbxxddn/images/bulkvisualchanges.png?fit=max&auto=format&n=VZaHE3DGMgbxxddn&q=85&s=bb3a183e070ba2581b0d5453e5cd324b" alt="Bulk design changes using Visual Edit in Base44" width="1056" height="285" data-path="images/bulkvisualchanges.png" />
</Tip>

***

## Queuing messages in the chat

When the AI chat is already working on a prompt, you do not need to wait before asking something else. You can keep typing, add more prompts, and attach files. The AI chat adds them to a message queue and sends them one by one as each response finishes.

<Frame caption="Queued messages waiting to run while the AI finishes the current prompt">
  <img src="https://mintcdn.com/base44/FxfXpIzW9poqdXvQ/images/messagequeue.png?fit=max&auto=format&n=FxfXpIzW9poqdXvQ&q=85&s=b0b9e716c69615f9750e1006dd4c1ec5" alt="Messagequeue" title="Messagequeue" className="mx-auto" style={{ width:"68%" }} width="878" height="636" data-path="images/messagequeue.png" />
</Frame>

<Note>
  **Notes:**

  * The queue appears above the chat input and shows all pending prompts in the order they will run.
  * You can queue up to 7 messages at once.
  * Queued messages do not send if you close the app editor. When you reopen the editor, any queued messages will resume.
</Note>

You can edit your queue at any time. Drag and drop messages to change their order, edit a queued message inline before it is sent, remove individual messages or clear the entire queue if you change your mind. You can also pause or resume the queue whenever you need.

***

## Customizing the AI chat

You can tailor how the AI behaves and set custom controls.

### Choosing your AI model

Choose a model manually when you want more control. Each model brings unique strengths, so you can pick the best fit for your prompt.

<Note>
  **Notes:**

  * You need a [**Builder plan**](https://base44.com/pricing) or higher to choose an AI model.
  * When you choose a model manually, credit usage varies by model and may use more credits than **Automatic**. Check the exact cost under **Credits Used** for each message.
</Note>

* **Gemini 3.1 Pro:** Ideal for logic-heavy and code-heavy work, especially when you include visuals, structured data, or multiple files in your prompt.
* **Sonnet 4.6:** A great default for most prompts, balancing quality and speed for day-to-day building, writing, refactoring, and troubleshooting.
* **Opus 4.6:** Best for deep reasoning and hard problems like complex debugging, architecture decisions, data modeling, and edge-case analysis.
* **GPT-5.4:** Well suited to long, detailed prompts, large codebases, and multi-step workflows where it needs to plan and update several parts of your app in a single run.
* **GPT-5:** A good choice when you want strong reasoning and planning with a focus on stability across large or evolving projects.

<Frame caption="Choosing an AI model in the Base44 AI chat settings">
  <img title="Newmodel" className="mx-auto hidden dark:block" style={{ width:"69%" }} src="https://mintcdn.com/base44/W4dNTaxSUasjI0i_/images/aimodels-3.png?fit=max&auto=format&n=W4dNTaxSUasjI0i_&q=85&s=c71684e7a9db47eec8c94d296d1aff5e" alt="Choosing an AI model in the Base44 AI chat settings" width="1122" height="734" data-path="images/aimodels-3.png" />

  <img title="Newmodel" className="mx-auto dark:hidden" style={{ width:"69%" }} src="https://mintcdn.com/base44/W4dNTaxSUasjI0i_/images/aimodels-2.png?fit=max&auto=format&n=W4dNTaxSUasjI0i_&q=85&s=dbbe811518034c62160ecef58f7c5a9b" alt="Choosing an AI model in the Base44 AI chat settings" width="1122" height="734" data-path="images/aimodels-2.png" />
</Frame>

**To choose a model manually:**

1. Go to your app editor.
2. Click the **Settings** icon <Icon icon="gear" /> at the bottom of the chat.
3. Click **AI Model**.
4. Click **Manual**.
5. Select the model you want to use.

<Tip>
  Not sure which model to choose? Keep **Automatic** and Base44 selects the best model for each request.
</Tip>

### Setting AI controls

AI controls let you define how the AI interacts with your app. They help you set consistent rules and protect important areas from accidental edits.

Click the **Settings** icon <Icon icon="gear" /> at the bottom of the chat, then select **AI Controls** to open the panel:

* **Custom Instructions:** Add default guidance for every AI interaction, such as tone, design standards, or preferred behavior.
* **Freeze Files:** Lock specific files or entities so the AI does not modify them.

<img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/AIControls.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=208450818c6146ecefc3470bc4e10c72" alt="Adjusting AI Controls in Base44 settings." className="mx-auto" style={{ width:"61%" }} width="497" height="741" data-path="images/AIControls.png" />

<Tip>
  Clear, well-defined AI controls keep your app consistent and prevent accidental overwrites.
</Tip>

***

## Reverting changes

Experiment freely and try new ideas, knowing you can always undo your changes at any time. You can roll your app back to a specific prompt, restore a previous version into the editor, or publish a previous version directly from Version History without changing what you are currently working on.

### **Reverting a specific prompt**

Hover over the relevant message in your chat history and click the **Revert** icon under it to roll your app back to the state it was in just before that change. Any changes made after that point are also undone, so you can quickly return to an earlier version of your app.

If you want to change what you asked instead of just undoing it, click the **Edit** icon on that earlier message. The chat opens an **Edit this message and resend** panel. When you resend, Base44 reverts any changes made after that message and then applies your updated request.

<Frame caption="Revert and edit options under a message in the Base44 AI chat">
    <img src="https://mintcdn.com/base44/EHm1bYyl6CvNnoNT/revertandedit.png?fit=max&auto=format&n=EHm1bYyl6CvNnoNT&q=85&s=a3e8e570b1d2f4f290523680f33affb1" alt="Revert and edit options under a message in the Base44 AI chat." width="872" height="587" data-path="revertandedit.png" />
</Frame>

### Restoring or publishing a previous version

Click the **Version History** icon at the top of the chat to open your version list. From there you can preview versions, publish a previous version without changing your current draft, revert your editor to an older version, view the code, or jump back to the chat message that created that version.

<img src="https://mintcdn.com/base44/kVxckvtxI6o4baYE/VixFileslol.png?fit=max&auto=format&n=kVxckvtxI6o4baYE&q=85&s=68e6d43eed10c7aedaa2406a771984f4" alt="The Version History options available in Base44." className="mx-auto" style={{ width:"85%" }} width="598" height="380" data-path="VixFileslol.png" />

Click a version in the list to load it in the preview. For each version, click the **More Actions** icon and choose:

* **Publish this version:** Publish this version to your live app while keeping your current draft open in the editor so you can keep working.
* **Revert to this version:** Replace your current draft in the app editor with this version.
* **View code:** Open the code for this version.
* **Go to message in chat:** Jump to the chat message that created this version.

***

## FAQs

Click a question below to learn more about AI chat modes and controls.

<AccordionGroup>
  <Accordion title="How do I preview my app in full screen?">
    Click the **Hide chat panel** icon above the preview window to display your app exactly as visitors see it, without any editor panels or chat tools.

        <img src="https://mintcdn.com/base44/W2j3JS-KBq8LdV2O/images/HideChatPanel.png?fit=max&auto=format&n=W2j3JS-KBq8LdV2O&q=85&s=82babb46b07c45d49920618c7c7e005f" alt="Hiding the chat panel to preview your app in full screen." width="1351" height="48" data-path="images/HideChatPanel.png" />
  </Accordion>

  <Accordion title="How can I fix my app if it freezes after an AI action?">
    If your app freezes or behaves unexpectedly, try these steps to get back on track:

    * **Refresh the page** to reload your latest working version.
    * **Clear your browser cache** and reload your app to remove any stored conflicts.
    * **Try a private window** or another browser to rule out extension conflicts.
    * **Disable browser extensions** temporarily if the issue persists.
    * **Check your credits and plan limits**, since running out of credits can interrupt AI actions.
    * **Revert the last AI action** in the chat by clicking the **Revert** icon under that message, or use **Version History** to roll back to a stable version.

    For more help, see the [Troubleshooting guide](/Community-and-support/Troubleshooting).
  </Accordion>

  <Accordion title="Can I request credit refunds for AI mistakes?">
    Base44 does not offer refunds or credit reversals for AI actions. You can use [**Version History**](#reverting-changes) to undo changes and restore your app.
  </Accordion>

  <Accordion title="What can the Base44 agentic AI do with its tools?">
    The agentic AI uses a wide range of tools to help you build and manage your app, including:

    **Database tools:**

    * Read, create, update, and delete records in your app’s database. It can filter, sort, paginate, or update or delete in bulk. For example, add test people, mark old messages as read, or remove expired records.

    **Web tools:**

    * Perform web searches to find relevant documentation or features. This works like a search engine with relevant pages, titles, and descriptions.
    * Fetch website data from any URL. Retrieve markdown or HTML, for example to scrape documentation or get live page content.

    **Code and file tools:**

    * Smart file search. Quickly find files or code snippets needed for your workflow.
    * Read the contents of any project file before editing. This is useful for reviewing your app’s code structure.
    * Modify files in your project. Edit pages, components, entities, functions, or layouts, and support targeted partial edits. For example, fix bugs, add features, or update styling.
    * Inspect logs and console output to help with debugging or understanding errors.

    **Configuration tools:**

    * Set or update environment variables and secrets as needed. For example, add or update API keys like `OPENAI_API_KEY` or `STRIPE_SECRET_KEY`.

    The agent automatically chooses and combines these tools based on what you need, so you can focus on describing your goals instead of the technical steps.
  </Accordion>

  <Accordion title="Are there things the Base44 agentic AI cannot do?">
    The agentic AI can fetch and interpret content from public website pages and other static data, but it cannot automatically access or migrate complex backend logic, databases, or private integrations. If your project requires backend features, connections to other services, or secure data, you still need to set these up manually.

    For example, if you ask the agent to copy content or features from another app, it can match layouts, text, and the overall look based on what is visible on the public site, but it does not copy any backend logic, migrate private integrations, or access protected database content.

    For any work that goes beyond the public front end, manual setup is required to complete your app.
  </Accordion>

  <Accordion title="How is the time zone determined or managed in the builder?">
    All times in the Base44 builder are managed and displayed using Coordinated Universal Time (UTC). This keeps everything consistent across different regions and makes it easier to coordinate actions or schedules, no matter where you or the people using your app are located. There is no option to change the time zone within the builder at this time.
  </Accordion>

  <Accordion title="Can I speak to the AI chat instead of typing?">
    Yes, you can use your voice to interact with the AI chat in Base44. Click the microphone icon in the chat box to turn on speech-to-text, then speak your question or request. The AI transcribes your speech and responds as usual, so you can get help hands-free.

    <Frame>
            <img src="https://mintcdn.com/base44/j-h9Uf3gLbgV2PFd/images/2025-11-23_15-12-49.png?fit=max&auto=format&n=j-h9Uf3gLbgV2PFd&q=85&s=29a9707eeca53a778593d2fb19b06005" alt="Speaking to the AI chat in Base44" width="501" height="140" data-path="images/2025-11-23_15-12-49.png" />
    </Frame>
  </Accordion>

  <Accordion title="What should I do if AI chat gets stuck or cannot revert changes?">
    If AI chat is unresponsive, gets stuck processing, or does not undo changes as expected, there are ways to recover.

    Check out the full troubleshooting guide for step-by-step solutions, including how to:

    * Use Version History or the **Revert** icon under a previous message to safely undo actions.
    * Unstick a frozen prompt or stop button.
    * Get help if the chat panel is completely unresponsive.

    For detailed instructions and workarounds, see the [Troubleshooting Issues](/Community-and-support/Troubleshooting) article.
  </Accordion>

  <Accordion title="How does automatic model selection work?">
    Base44 uses automatic model selection to match each request with the engine best suited for the job. Design tweaks, layout changes, and deep logic updates may all use different AI models. The chat handles this in the background, so you can stay focused on describing what you want to build.

    * For small visual or copy tweaks, it chooses fast, efficient models that optimize for speed and responsiveness.
    * For larger architectural changes or data flows, it uses deeper reasoning models that can plan across files, entities, and logic.
    * When something fails or runs into an error, it can switch strategies or models to recover and try again.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).