# Source: https://docs.base44.com/Building-your-app/Creating-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating automations for your app

> Run backend work automatically, on a schedule or when data changes.

***

Use automations when you want to take work off your plate, such as sending summary emails, generating reports, syncing or cleaning up data, or running recurring maintenance tasks.

Automations let you run backend functions automatically, either on a schedule or when data in your app changes.

<Card color="#FF5500" icon="clock" title="What can I use automations for?">
  You can use automations for any backend work you want to happen automatically. Common examples include:

  * Sending emails or messages, such as daily welcome emails or weekly newsletters.
  * Generating reports or summaries, for example a daily revenue report.
  * Checking conditions and alerting only when something changes, such as low inventory.
  * Reacting to changes in your data, such as sending admins a message when a new product is added.
  * Scheduling posts on social media.
  * Running recurring maintenance or housekeeping tasks, like archiving old records or refreshing caches.
  * Backing up your app's data (e.g. to Google Drive) every week.
</Card>

***

## How do they work?

When you create an automation, you choose how it starts. It can run on a schedule you define, or in response to a data event such as a record being created, updated, or deleted. Each automation runs a backend function in your app and records the run so you can see what happened.

You can set up one-time automations or recurring daily, weekly, or monthly automations, and you can stop them after a certain date or after a set number of runs. This gives you automation that happens quietly, reliably, and without ongoing attention.

<Frame caption="Automations for your app in Base44">
    <img src="https://mintcdn.com/base44/MnQU968z-fErGCmR/automations.png?fit=max&auto=format&n=MnQU968z-fErGCmR&q=85&s=2c95c6d57f109929df7cdb50c5ee3241" alt="Automations for your app in Base44" width="1286" height="614" data-path="automations.png" />
</Frame>

Every automation has logs so you can always see when it ran, whether it succeeded, and any errors that occurred. This makes automations useful for anything from sending emails to backing up data, and keeps everything transparent and safe.

<Warning>
  **Important:**

  * You must have a **Builder plan** or higher to use automations.
  * Each time an automation runs, it uses **1 integration credit**.
  * Each automation run can last for a maximum of 3 minutes. If it takes longer, the run fails. For example, if your automation sends 1,000 emails but can only send 600 within 3 minutes, only the first 600 are sent and the rest are not processed.
  * The minimum interval between automation runs is 5 minutes.
</Warning>

***

## Creating with the AI chat

Ask the AI chat to set up an automation for you. For example, you can use a prompt like the one below:

`Set up recurring email reminders to my email name@email.com for my tasks on my to-do list every Sunday at 17:00.`

The automation is created in **Automations** in your app's dashboard. You can view the automation and make changes as needed.

<Frame caption="Setting up an automation using the AI chat">
    <img src="https://mintcdn.com/base44/MnQU968z-fErGCmR/creatingautomationinchat.png?fit=max&auto=format&n=MnQU968z-fErGCmR&q=85&s=3e147af635dbf3f357f79c46dbfb8b78" alt="Setting up an automation using the AI chat" width="1915" height="953" data-path="creatingautomationinchat.png" />
</Frame>

***

## Creating from the dashboard

Manually configure your automation from your app's dashboard. You can choose whether it runs on a schedule or when data changes.

### Scheduled automations

Use scheduled automations when you want a backend function to run at specific times. This is helpful for recurring work like daily digests, weekly reports, or regular maintenance jobs that you want to happen on a predictable schedule.

**To create a scheduled automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click **New Automation**.
4. Select **Scheduled**.
5. Enter a name and short description for the automation, for example “Daily welcome emails.”
6. Select the backend function you want the automation to run. If you need to create or edit a function, ask the AI chat to do it for you.
7. Under **Type**, select whether the automation is:
   * **Recurring:** For automations that run on a repeating schedule, such as daily or weekly. Set how often the automation runs, the time of day, which days it should run, and when it should end.
   * **One Time:** For automations that run once at a specific date and time.
8. Click **Save**.

<Frame caption="Setting up a new scheduled automation from your app's dashboard">
  <img src="https://mintcdn.com/base44/FqrO4aN4hBhcbFuM/scehduled.png?fit=max&auto=format&n=FqrO4aN4hBhcbFuM&q=85&s=3dbadc9a2a1128479b94e70c7007c776" alt="Setting up a new scheduled automation from your app's dashboard" title="Setting up a new scheduled automation from your app's dashboard" className="mx-auto" style={{ width:"85%" }} width="928" height="530" data-path="scehduled.png" />
</Frame>

### Data event automations

Use data event automations when you want a backend function to run in response to changes in your data. This is ideal for reacting to events like new records being created, existing records being updated, or items being deleted, so you can send notifications, sync data, or clean things up automatically.

**To create a data event automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click **New Automation**.
4. Select **Data event**.
5. Enter a name and short description for the automation so you know what it does.
6. Select the backend function you want the automation to run. If you need to create or edit a function, ask the AI chat to do it for you.
7. Under **Runs when**, set when the automation should start:
   * In the first drop-down, select the item or entity to watch.
   * In the second drop-down, select the event, such as **Created**, **Updated**, or **Deleted**.
8. Click **Save**.

<Frame caption="Setting up a new data event automation from your app's dashboaard">
  <img src="https://mintcdn.com/base44/j-g9fQ-dvXb1qrEN/images/dataevent.png?fit=max&auto=format&n=j-g9fQ-dvXb1qrEN&q=85&s=947df0f7791d58fd84a819c22f887319" alt="Setting up a new data event automation from your app's dashboaard" className="mx-auto" style={{ width:"86%" }} width="928" height="530" data-path="images/dataevent.png" />
</Frame>

***

## Managing automations

After you start using automations, you can control when they run, change their settings, trigger them on demand, or clean up automations you no longer need. You can pause automations without deleting them, and you can duplicate an existing automation when you want a similar setup with small changes.

<Note>
  **Note:** When you turn an automation off, Base44 stops scheduling future runs, but existing logs stay available. You can turn the automation back on at any time.
</Note>

### Turning an automation on or off

Pause an automation at any time if you want to stop it running, and turn it on again when you need it.

**To turn an automation on or off:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click the toggle on the left of the automation name to turn it on or off.

<Frame caption="Turning an automation on and off">
    <img src="https://mintcdn.com/base44/FqrO4aN4hBhcbFuM/turnautomationoff.png?fit=max&auto=format&n=FqrO4aN4hBhcbFuM&q=85&s=594fa3712b07d29f40f18c31bef07c3c" alt="Turning an automation on and off" width="1286" height="614" data-path="turnautomationoff.png" />
</Frame>

### Editing an automation

Make changes to an automation at any time. The changes affect future runs only.

**To edit an automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click the **More Actions** icon <Icon icon="ellipsis" /> on the automation.
4. Click **Edit** **automation**.
5. Update the automation details.
6. Click **Save**.

<Frame caption="Editing an automation in your app">
    <img src="https://mintcdn.com/base44/aSMFXtSXQCb3elTY/images/editautomation.png?fit=max&auto=format&n=aSMFXtSXQCb3elTY&q=85&s=7754aa17e7e32a1a5aa9bc623ab6c3a5" alt="Editing an automation in your app" width="2324" height="1162" data-path="images/editautomation.png" />
</Frame>

### Duplicating an automation

Easily create new automations by duplicating existing ones and editing the new automation.

**To duplicate an automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click the **More Actions** icon <Icon icon="ellipsis" /> on the automation.
4. Click **Duplicate**.
5. Update the new automation’s details if needed, and click **Save**.

<Frame caption="Duplicating an automation in your app">
    <img src="https://mintcdn.com/base44/aSMFXtSXQCb3elTY/images/duplicateaut.png?fit=max&auto=format&n=aSMFXtSXQCb3elTY&q=85&s=5e8cee320481fcfd70d592548a4d6c35" alt="Duplicating an automation in your app" width="2324" height="1162" data-path="images/duplicateaut.png" />
</Frame>

### Running an automation immediately

Run an automation right away when you want to trigger its backend function on demand. This helps you test changes, confirm that your configuration works, or handle something urgent between scheduled runs.

<Note>
  **Note:** Run now triggers the backend function one time in addition to any schedule or data event you configured. The run appears in the automation logs.
</Note>

**To run an automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click the **More Actions** icon <Icon icon="ellipsis" iconType="regular" /> on the automation.
4. Select **Run now**.

<Frame caption="Running an automation immediately">
    <img src="https://mintcdn.com/base44/rGcCOplgSQIZW5QD/images/runnowaut.png?fit=max&auto=format&n=rGcCOplgSQIZW5QD&q=85&s=52d7d0d6e64e87599be8e1dfab0c0507" alt="Running an automation immediately" width="2324" height="1162" data-path="images/runnowaut.png" />
</Frame>

### Archiving an automation

If you do not need an automation anymore, you can move it to Archive to keep your active list clean.

**To archive an automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Find the relevant automation in the list.
4. Click the **More Actions** icon <Icon icon="ellipsis" /> on the automation.
5. Click **Archive**.

<Frame caption="Archiving an automation">
    <img src="https://mintcdn.com/base44/IIK5Nw53Dsz4qhFW/images/archiveaut.png?fit=max&auto=format&n=IIK5Nw53Dsz4qhFW&q=85&s=065d803d1fb9060756805401f504f83b" alt="Archiving an automation" width="2324" height="1162" data-path="images/archiveaut.png" />
</Frame>

***

## Monitoring runs and using logs

Every automation keeps its own log so you can see when it ran, how long it took, and whether it succeeded. When something goes wrong, logs help you understand what failed and where to look in your backend code, without guessing.

<Tip>
  **Tip:** Use logs to confirm that new automations are running at the right time after you first set them up.
</Tip>

**To view logs for an automation:**

1. Click **Dashboard** in your app editor.
2. Click **Automations**.
3. Click the automation you want to inspect.
4. Click the **Logs** tab.
5. Review the list of runs, including the timestamp, duration, and status of each run.

<Frame caption="Viewing the logs of an automation">
  <img src="https://mintcdn.com/base44/FqrO4aN4hBhcbFuM/ss.png?fit=max&auto=format&n=FqrO4aN4hBhcbFuM&q=85&s=2d44eb7084a126876576a7f50671ce83" alt="Viewing the logs of an automation" className="mx-auto" style={{ width:"83%" }} width="691" height="451" data-path="ss.png" />
</Frame>

***

## FAQs

Click a question below to learn more.

<AccordionGroup>
  <Accordion title="How do I investigate a failed automation run?">
    When an automation fails, you see a **Failed** label in the **Last run** column and a **Fix with AI** option on the same row.

        <img src="https://mintcdn.com/base44/kuqIWwAAwM4Jrcht/images/failed-2.png?fit=max&auto=format&n=kuqIWwAAwM4Jrcht&q=85&s=695e3a0d7a75b5c6b61bb476a6993c11" alt="Failed 2" width="1289" height="603" data-path="images/failed-2.png" />

    **To fix a failed run:**

    1. Click **Dashboard** in your app editor.
    2. Click **Automations**.
    3. Click **Fix with AI** on the failed automation.
    4. In the AI chat, review the explanation of what went wrong and how it affects your automation. Accept the suggested fix so the AI can update your code or automation configuration.
    5. When the AI finishes applying the fix, use the **Run now** action from  **Automations**  and check the logs to confirm the automation succeeds.

    <Tip>
      **Tip:** For more detail about what happened, open the automation, go to the **Logs** tab, and review the failed run entry. You can also ask the AI in your dashboard to explain any error messages that appear.
    </Tip>
  </Accordion>

  <Accordion title="Can I create automations from an app agent?">
    Not yet. You currently cannot use the in-app agent to create or edit automations. To set up automations, go to **Automations** in your app's dashboard and configure them there.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).