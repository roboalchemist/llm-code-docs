# Source: https://documentation.onesignal.com/docs/en/labels.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Labels

> Organize and manage messages across push, email, SMS, and in-app channels with Labels in OneSignal. Easily filter, categorize, and streamline your campaign workflow.

## Overview

Labels in OneSignal help you categorize and organize messages across push, email, SMS, and in-app channels. Labels make it easier to filter messages, locate templates, and collaborate across teams.

Once a label is applied, it can be used to filter and group content, improving visibility and navigation within your dashboard.

<Frame caption="New labels column on the push index.">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6f6e2a6-Labels.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=d823f7c25262b7952fce3e43c8fcca52" width="1325" height="605" data-path="images/docs/6f6e2a6-Labels.png" />
</Frame>

### Suggested use cases

Organize your messages by:

* Team or message creator
* Status or priority
* Campaign topic or goal
* Language or geography
* Event or seasonal theme
* Message type (promo, transactional, etc.)
* Top Performers

To get the most value out of Labels, we recommend:

1. Defining clear criteria for when and why to use labels.
2. Establishing consistent naming conventions.
3. Brainstorming and planning label types before applying them.
4. Aligning with team members and cross-functional partners.
5. Reviewing and adjusting labels periodically to keep your dashboard clean and useful.

***

## Add or edit a Label

You can apply up to **five labels** per message or template. Each label can be up to **100 characters** long and must be unique. Labels are **shared across all channels**, enabling you to group related content across push, email, SMS, and in-app messages.

### When sending a message

Use the **Labels dropdown** when composing a new message. Select existing labels or start typing to create new ones.

<Frame caption="Labels dropdown in the message composer.">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/add-label.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=6e942e68e4ae981d832359d1829064e4" width="1220" height="478" data-path="images/docs/add-label.png" />
</Frame>

### On an existing message

To label an existing message:

<Steps>
  <Step title="Go to the Messages and select the channel." />

  <Step title="Find the message you want to label.">
    Click the **three dots** on the right side of the message and select **Edit Labels**.

    <Frame caption="Edit labels for each index item through the options menu.">
      <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/edit-label.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=2cc70706ef71a0aa77d2aa7fefba2acf" width="1506" height="676" data-path="images/docs/edit-label.png" />
    </Frame>
  </Step>

  <Step title="Choose existing labels or start typing to make a new one.">
    <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/create-label.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=588e070d6aaeefa5c320a7453a874eaa" width="872" height="420" data-path="images/docs/create-label.png" />
  </Step>

  <Step title="Click Update to save." />
</Steps>

***

## Filter by label

Apply filters to show only messages with selected labels. You can use up to **five label filters** at once. Filters use **AND logic**, meaning only messages that match *all* selected labels will appear.

Example: Filtering by `Label A` and `Label B` will only show messages tagged with *both*.

<Frame caption="Use the filter to find items with that label applied. Limit 5.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7973ab6-Labels_-_Filter.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=f74887b340a95a333badfdacbd5b1be5" width="1331" height="411" data-path="images/docs/7973ab6-Labels_-_Filter.png" />
</Frame>

### Rename or delete a Label across all messages

To change or remove a label globally:

1. Use **Add Filter > Label** to find messages with a specific label.
2. Click **Manage Labels** in the top right corner.
3. Choose **Rename Labels** or **Delete Labels**.
4. Confirm your changes:
   * **Rename**: Enter a new name and click **Rename**.
   * **Delete**: Confirm removal to delete the label from all messages.

<Frame caption="Rename or delete all instances of a label in the dashboard.">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/58dd739-Labels_-_Delete.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=7bbd8562d483a39b9ffa9d32aea7a8fe" width="1590" height="524" data-path="images/docs/58dd739-Labels_-_Delete.png" />
</Frame>

***

## FAQ

### If I use the same label across different channels, will it group those messages together?

Yes. Labels are shared across all messaging channels. For example, the label "Super Bowl 2023" can be used on push, email or any other channel and will appear consistently in filters.

### Can I see labels when I export my messages?

Yes. When exporting your messages from **Delivery > Sent Messages** the labels for these messages will be included in the exported CSV.

***

Built with [Mintlify](https://mintlify.com).
