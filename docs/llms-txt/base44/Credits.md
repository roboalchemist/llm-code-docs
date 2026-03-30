# Source: https://docs.base44.com/Account-and-billing/Credits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Credits

> Credits power your app building and operations in Base44. Learn how credits work so you can build confidently without hitting limits.

## About credits in Base44

Credits are the units Base44 uses when you interact with Base44's AI or connect your app to external tools. Credit usage adjusts dynamically based on how much work the builder needs to do behind the scenes.

<iframe src="https://www.youtube.com/embed/Dc2Pe5Kp-So" title="YouTube video player" frameborder="0" className="w-full aspect-video rounded-xl" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share; fullscreen" allowFullScreen />

**Types of credits**

Base44 uses 2 types of credits to support your app building and operations:

<AccordionGroup>
  <Accordion title="Message credits">
    Used when you interact with Base44's AI while building apps. Message credits are used for prompts that plan, update, or fix parts of your app.

    **Examples:**

    * Asking the AI to add or refine a small feature.
    * Debugging or fixing logic in a specific part of your app.
    * Getting the AI to rewrite copy or microcopy.
    * Applying AI-suggested changes from the chat.
  </Accordion>

  <Accordion title="Integration credits">
    Used whenever your app uses Base44's services for advanced functionality. Integration credits are used when your app triggers tools that send data, process content, or call external services.

    **Examples:**

    * Calling an LLM through Base44's built-in LLM integration. Integration credits are not used if you call your own LLM using backend functions.
    * Sending emails using Base44's built-in email integration with a custom email domain uses 2 integration credits. If you send emails using your own email service through backend functions, integration credits are not used.
    * Uploading, downloading, or analyzing a file.
    * Generating or understanding an image.
    * Using [AI agents](/Building-your-app/AI-agents).
  </Accordion>
</AccordionGroup>

<Note>
  **Note:** Credits renew at different times depending on your plan. [Learn more below](#credit-resets).
</Note>

***

## How credits are used

There is no set credit amount used per message. Different actions use credits in different ways, depending on what you ask the AI to do.

### Understanding credit usage

Short, focused prompts usually require less work behind the scenes, while broader prompts that touch several pages or components can require more. Manual visual edits, such as dragging elements, changing layouts, or editing text directly in the editor, do not use credits.

Even when a request looks simple or your message is very short, the AI still has a lot to do in the background. It needs to read what you already built, understand your request, figure out the safest way to change it, and apply the update without breaking other parts of your app.

Credits are based on how much work the system has to do, not on how small the change looks. This is why something that feels like a quick tweak, such as “translate the whole app” or “rebuild this page for mobile,” can still use a few credits as the AI has to review many files and make complex updates that you do not always see.

### Examples of typical credit usage

These examples show how the scope of your request can affect credit usage.

| Type of request              | What it usually does                                                                               | Typical credits used | Example prompts                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| Simple visual or text change | A lightweight update that touches a single element or short piece of text.                         | \~ 0.5 credits       | - `Change this button’s background to red`<br /> - `Increase the padding on this section`    |
| Improving a small feature    | Inspects a few files and adjusts logic, so usage is higher than a simple style tweak.              | \~ 1 credit          | - `Fix the validation on this form` <br /> - `Update the logic for this button click`        |
| Adding a complex module      | Larger upgrade that includes entities, flows, and logic, requiring deeper planning and more steps. | \~ 2 credits         | `Add an employee time-tracking feature with a form, data entities, and an admin review page` |

### Viewing credits used per message

You can see how many credits a prompt used. Click the **More Actions** icon <Icon icon="ellipsis" /> under your prompt to open the menu, then look under **Credits Used** to see the cost for that specific message.

<Frame caption="Viewing how many credits were used in a message in the AI chat">
  <img src="https://mintcdn.com/base44/TgJsEd6fH4e8d2-d/images/creditsused.png?fit=max&auto=format&n=TgJsEd6fH4e8d2-d&q=85&s=6738b221d64b947a2643465e51a3deea" alt="Viewing how many credits were used in a message in the AI chat" title="Viewing how many credits were used in a message in the AI chat" className="mx-auto" style={{ width:"67%" }} width="1130" height="1118" data-path="images/creditsused.png" />
</Frame>

### Maximizing your credits

Get more out of your Base44 credits with these practical tips. Open each tip below to see how you can save credits and keep your workflow efficient.

<AccordionGroup>
  <Accordion title="Plan your builds before prompting">
    Planning before you start helps you save both time and credits.

    Start by deciding what your app should do and outlining its main parts. You can use any AI tool to organize your thoughts and write a clear prompt. List the key features you want and describe how people will use your app, step by step.

    You can also ask another AI tool to help you draft a ready-to-use prompt for Base44, then paste it directly into your project.
  </Accordion>

  <Accordion title="Use the automatic AI model">
    Keep the AI model set to **Automatic** unless you have a specific need to choose a manual model. Base44 automatically routes each prompt to the AI models best suited for your task, so you get accurate results while your credit usage stays efficient, without needing to worry about the technical details.

    Manually choosing a model is less predicatable and can use more credits, especially for complex work.
  </Accordion>

  <Accordion title="Keep your prompts focused">
    Write short, focused prompts for each message instead of one very broad request. Focused  prompts often use fewer credits and lead to better results. Ask the AI to work on specific files, pages, or functions instead of your entire app, and clearly state what change you want to make.

    For example, you could say: `Update the Home page text to match the new pricing plan`. 
  </Accordion>

  <Accordion title="Use Discuss mode to explore ideas">
    Use **Discuss** mode to brainstorm, ask questions, or refine ideas without changing your app. Each message in Discuss mode uses **0.3 message credits**. When you are ready to apply changes, switch back to the regular chat.  [Learn more about Discuss mode](/Building-your-app/AI-chat-modes#discuss-mode).

    Use the regular chat mode only when you are ready to make direct changes to your app.
  </Accordion>

  <Accordion title="Use Visual Edit mode">
    For UI tweaks, select the element in **Visual Edit** before you describe the change so the AI does not need to scan your entire layout.
  </Accordion>

  <Accordion title="Avoid repeated automatic fixes">
    If a change is not what you wanted, click the \*\*Revert \*\*icon on that message instead of using extra prompts to debug or undo it.

    If you encounter errors, try using the automatic fix once or twice. If the problem is not resolved, avoid repeating the auto-fix. Switch to **Discuss** mode, explain what is not working, and ask the AI to help you find a solution.
  </Accordion>

  <Accordion title="Add and test features in small steps">
    Add new features or make changes to your app one step at a time. Start by building the basics, such as pages, navigation, and a consistent design. Then add new features like forms, search, analytics, or integrations gradually, testing after each change.

    This step-by-step method helps you catch issues early, makes troubleshooting easier, and reduces the risk of using more credits on major fixes.
  </Accordion>

  <Accordion title="Track your credit usage">
    Keep an eye on your credit usage by checking your balance while editing your app, or from your workspace settings.

    Monitoring your credits helps you spot actions that use the most credits and plan resets or upgrades if needed, so you can avoid interruptions to your workflow.

    You can also see [how many credits a specific prompt used](#Viewing-credits-used-per-message) from the **More Actions** icon <Icon icon="ellipsis" />  under that prompt in the builder.
  </Accordion>
</AccordionGroup>

***

## Checking your credit balance

The number of credits you have depends on your plan. Your balance is updated in real time to help you plan ahead and avoid interruptions. You can see your current balance and usage at any time in your Base44 dashboard.

**To check your balance:**

1. Click your profile icon at the top-right of your workspace.
2. Click **Settings**.
3. Click **Credit Usage** under **Workspace** to see your used and remaining credits for the current billing cycle.

<Frame caption="Viewing your credit usage in your Base44 account">
    <img src="https://mintcdn.com/base44/KKc6awBfhSg9Deqm/images/creditusage.png?fit=max&auto=format&n=KKc6awBfhSg9Deqm&q=85&s=1f6a71bc4670dbd26d91c2ac3748b26e" alt="Viewing your credit usage in Base44" width="1459" height="655" data-path="images/creditusage.png" />
</Frame>

<Tip>
  You can also view your remaining credits while working in your app editor by clicking the Base44 logo at the top left.
</Tip>

***

## Credit resets

Your credits refresh automatically based on your plan:

* **Free plan:** You can use up to 5 credits a day, up to a total of 25 credits each month. Once you reach your daily limit, features that require credits are unavailable until your daily balance resets, as long as you still have monthly credits left.
* **Paid plans:** Message and integration credits reset monthly on your reset date, which is the same day of the month you subscribed. For example, if you subscribed on July 5, your credits reset on the 5th of every month.

<Note>
  Credits do not roll over:

  * **Free plan:** Unused credits expire when your daily limit resets.
  * **Paid plans:** Unused credits expire at the end of your monthly credit cycle, on your reset date.
</Note>

If you reach your credit limit, actions that require credits pause until your next reset. If you prefer not to wait, you can upgrade or adjust your plan from your [**billing dashboard**](https://app.base44.com/billing?utm_source=Mintlify\&utm_medium=Billing\&utm_content=credits).

***

## Using credits with teams

Each paid member in a Base44 workspace has their own message and integration credits, based on their plan. Credits are not shared across teammates, even when you collaborate on the same app.

**When working together on an app:**

* **Message credits:** Each team member uses their own credits when prompting the AI.
* **Integration credits:** These belong to the app owner. Any integration actions (API calls, emailing, image generation, etc.) use the app owner’s integration credits.

<Tip>
  You can transfer paid seats between team members in the workspace if plans need to be reassigned.
</Tip>

***

## Sharing your app and earning credits

You can earn 20 credits by sharing your Base44 project on LinkedIn or X. Spread the word about your app and get rewarded with extra credits to keep building. Once your post is approved, the credits are added to your account and work like regular credits.

<Note>
  **Notes:**

  * You can only earn these credits once per Base44 account by sharing an app on **LinkedIn or X**.
  * Your account must have more than 100 followers.
</Note>

**To earn free credits:**

1. Click the **Base44** icon at the top left corner of your app editor.
2. Click **Win Free Credits**.
3. In the popup, review the **Sharing Guidelines**.
4. After you share, copy the link to your **LinkedIn** or **X** post.
5. In the same popup, click **support system**.

   **Note:** This opens the support system where you can submit a ticket that connects directly to your app.
6. Paste the link to your post in your ticket and submit it.

<img src="https://mintcdn.com/base44/EN6XL5aRl3B1nAdQ/images/winfreecredits.png?fit=max&auto=format&n=EN6XL5aRl3B1nAdQ&q=85&s=30cd9ca62e1e66fe72c2f433f1825e08" alt="Win Free Credits panel with social sharing guidelines in the Base44 editor." className="mx-auto" style={{ width:"61%" }} width="600" height="696" data-path="images/winfreecredits.png" />

***

## FAQs

Click a question below to learn more about credits.

<AccordionGroup>
  <Accordion title="How does credit usage differ between prompts?">
    Credit usage depends on how much work the builder needs to do behind the scenes.

    Simple, focused prompts usually require fewer steps, so they tend to use fewer credits. For example, changing a button color or adjusting padding is often a lightweight update.

    Larger or more complex prompts, such as adding new pages, features, or integrations, often involve planning, updating multiple files, and running more checks. These usually use more credits, although in some cases the builder can complete a large task efficiently in a single pass.
  </Accordion>

  <Accordion title="Why does Base44 use two types of credits?">
    Message credits cover your building process, while integration credits cover your app’s live operations and automations. Separating them makes it easier to understand and manage the cost of development versus runtime activity.
  </Accordion>

  <Accordion title="Why were credits deducted for AI mistakes, and how do I request a refund or reset?">
    We understand that issues can arise, and we are here to support you. Credits are non-refundable for tool behavior and AI mistakes. Each prompt still requires work from the builder, even if the result is not what you expected.

    If something remains unresolved or you need further assistance, contact support with a detailed description of the issue, screenshots, and a link to your app.
  </Accordion>

  <Accordion title="What are promotional and free credits?">
    Base44 may issue extra credits for sign-ups, campaigns, or promo codes. These credits appear in your dashboard and work like regular credits, but are often one-time or limited-time.

    For example, you can earn credits by sharing your project on LinkedIn or X.
  </Accordion>

  <Accordion title="How do I redeem a credits coupon code?">
    Base44 may occasionally provide coupon codes that add extra credits to your account.

    **To redeem a credits coupon code:**

    1. Click your profile icon at the top right of your workspace.
    2. Click **Settings**.
    3. Click **Credit Usage** under **Workspace**.
    4. Enter your coupon code in the field next to **Have a credits coupon code?**
    5. Click **Apply**.

    If the code is valid, your credits are updated immediately.

    <Frame>
            <img src="https://mintcdn.com/base44/CwjoW9ZpdQSAyR0b/images/couponcode.png?fit=max&auto=format&n=CwjoW9ZpdQSAyR0b&q=85&s=2f6f2dac0d8d4338347007f3a25d0cbe" alt="Applying a coupon code in your Base44 account" width="987" height="816" data-path="images/couponcode.png" />
    </Frame>
  </Accordion>

  <Accordion title="Do automatic AI fixes use credits?">
    On the Free plan, both **Resolve with AI** and automatic error fix messages consume message credits. Each message and automatic fix counts as work, so both draw from your message credit balance.

    On paid plans, automatic AI fixes are free and do not use credits.
  </Accordion>

  <Accordion title="Can I purchase AI credits without upgrading my plan?">
    It is not possible to purchase standalone AI credits. You can either wait for your credit cycle to reset, or [upgrade your plan](/Account-and-billing/Billing-and-plans#upgrading-your-plan) to a higher tier for immediate access to higher limits.

    If you upgrade your plan, you immediately receive the full number of credits included in the new plan. You are only charged a prorated amount for the difference between your current plan and the upgraded plan for the rest of your billing cycle. You can switch back to your original plan next month if you prefer.
  </Accordion>

  <Accordion title="What happens if I run out of integration credits?">
    If you are using integrations and run out of integration credits:

    * We email you when your integration credits run out.
    * Any action you perform that requires integration credits fails and shows an error that you have used all your integration credits.

    If someone using your app attempts an action that uses integration credits, for example subscribing to your app and triggering an email, they receive a generic error message without any reference to integration credits:

    <img src="https://mintcdn.com/base44/BonfmDdzrhrmw7cY/images/2025-10-05_15-10-14.png?fit=max&auto=format&n=BonfmDdzrhrmw7cY&q=85&s=4eccea4a7ddea5c7b8d8214e2d733280" alt="An example of an error message when integration credit limit is reached." className="mx-auto" style={{ width:"73%" }} width="1384" height="1284" data-path="images/2025-10-05_15-10-14.png" />
  </Accordion>

  <Accordion title="Why haven't my credits refreshed yet?">
    Your message and integration credits reset each cycle at the exact time your subscription was purchased, based on Coordinated Universal Time (UTC), not just on the calendar date in your own time zone.

    For example, if your reset date is the 5th and you are several hours behind UTC, your credits may refresh while it is still the 4th where you are, or later in the day on the 5th.

    If your credits have not refreshed after your reset time has passed in UTC and you checked your billing cycle and current credit usage, wait and check again later in the day. Your credits should update once your reset time passes.
  </Accordion>

  <Accordion title="Why are my backend functions blocked on a paid plan?">
    Backend functions depend on the plan of the member who owns the app, not just the workspace plan. For backend functions to work, the app owner who originally created the app needs an active seat on a Builder plan or higher. If the workspace owner has a Builder plan but the app owner is on a Free or Starter plan, backend functions are blocked.

    To fix this, make sure the app owner has a Builder plan or higher. The workspace owner can assign or upgrade plans for members from the workspace settings.

    <Note>
      **Note:** Once backend functions are enabled by an app or workspace owner on a Builder plan or higher, collaborators with an Admin role on a Starter plan can create new backend functions, update existing ones, and manually edit backend code files for that app. Their ability to work with backend functions depends on the app owner's plan, not their own seat plan.
    </Note>
  </Accordion>

  <Accordion title="What should I do if the AI chat gets stuck or will not revert changes?">
    If AI chat is unresponsive, gets stuck processing, or does not undo changes as expected, there are a few ways to recover.

    For step-by-step solutions, including how to use **Version History** or the **Revert** option, unstick a frozen prompt, or get help if the chat panel is completely unresponsive, see the [Troubleshooting Issues](/Community-and-support/Troubleshooting) article.
  </Accordion>

  <Accordion title="Do you offer student discounts?">
    If you are an educator, please reach out directly to [highered@base44.com](mailto:highered@base44.com). For other inquiries or details about upcoming learning events, visit our [Base44 Higher Ed](https://base44.com/highered) page.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).