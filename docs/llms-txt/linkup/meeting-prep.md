# Source: https://docs.linkup.so/pages/documentation/tutorials/meeting-prep/meeting-prep.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Meeting Prep

> Build a meeting prep agent using Linkup inside Xpander

## Overview

Linkup integrates with [Xpander.ai](http://xpander.ai/) to give your agents access to real-time web data. This tutorial walks through how to build a meeting preparation agent that uses that data to generate useful briefings.

## Configuration Steps

<Steps>
  <Step title="Create a New Agent">
    1. Go to the Agents tab in Xpander.
    2. Click “New Agent”
    3. Name it something like “Meeting Brief Agent”

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.55.22_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=54a54e7ba422690938f2b35ed6a9c9d8" alt="Create Agent" width="2820" height="1664" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.55.22_PM.png" />

    4. Paste the following into the **Instructions** section:

    ```
    Your job is to help someone prepare for a sales meeting.
    They’ll give you a company name. Use Linkup to find useful, recent info about that company.
    Write a clear, short briefing with:
    - What the company does
    - Recent updates
    - Their likely challenges
    - How we might approach them
    - Notes and key questions
    ```

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.03.47_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=486e3ead37a007abe0c225f12c8c415b" alt="Paste Prompt" width="1146" height="1570" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.03.47_PM.png" />
  </Step>

  <Step title="Add the Linkup Tool">
    1. Go to the Tools section in the agent builder

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_2.36.47_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=9abdcba5f4e0be4acab5fc7edf4023b1" alt="Go Tools" width="2940" height="1656" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_2.36.47_PM.png" />

    2. Click “Add Tool” and select **Linkup.so**

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_2.57.30_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=01b5b32f94c02f5554594e62e35f77a6" alt="Add Tool" width="806" height="608" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_2.57.30_PM.png" />

    3. Choose the “Retrieve Web Content by Query” option

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_9.19.22_AM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=252008d3067f280686c5ed36f7abba68" alt="Select Action" width="1096" height="216" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_9.19.22_AM.png" />

    4. Under “Prompt Input Mapping”, link the user's input (e.g. company name) to the Linkup query

    **Query Tip:**

    ```
    Give me recent updates, funding info, hiring trends, product launches, and blog posts about {{company}}
    ```
  </Step>

  <Step title="Add 'Send Email' Step">
    1. Click the "+" button in the agent editor
    2. Select **Send Email** tool
    3. You don’t need to wire it to previous steps
    4. Make sure your prompt includes:

    ```
    Always email the final output to [email]
    ```

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.51.23_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=c2df21114fab80f7919857b19ef163a8" alt="Send Email" width="796" height="526" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.51.23_PM.png" />
  </Step>

  <Step title="Add 'Send Slack Message' Step">
    1. Click the "+" button again
    2. Select **Send Slack Message**

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.53.36_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=ff383c95c8556e903287501fbe4b62f6" alt="Send Slack" width="798" height="634" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.53.36_PM.png" />

    3. Configure credentials with OAuth2 and log in to Slack

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.54.32_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=9a5940a7de287e6aabdfcb8ccf42f6a7" alt="Slack Auth" width="1152" height="1346" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_5.54.32_PM.png" />

    4. Include this in the prompt:

    ```
    Also send the meeting briefing to the configured Slack channel
    ```
  </Step>

  <Step title="Test with a Sample Prospect">
    Company: Airtable
    Name: Daniel Kim
    Title: Director of Product Strategy
    Email: [daniel.kim@airtable.com](mailto:daniel.kim@airtable.com)

    Type into chat:

    > Can you prep a briefing for Daniel Kim from Airtable?

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.50.10_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=4a14dbdd5d560da3bdbed57d227b5e0d" alt="Test Prompt" width="1680" height="1564" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.50.10_PM.png" />
  </Step>

  <Step title="Final Look & Output">
        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.49.29_PM.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=05185f661b1eb28466bc15befc62bd5c" alt="Final Look" width="1582" height="1208" data-path="pages/documentation/tutorials/meeting-prep/assets/Screenshot_2025-07-10_at_3.49.29_PM.png" />
  </Step>
</Steps>

You are all set to use Linkup to build an intelligent meeting prep agent in Xpander. Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about how Linkup works.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).