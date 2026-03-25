# Source: https://documentation.onesignal.com/docs/en/iam-triggers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app triggers

> Options for displaying in-app messages to users.

## Overview

Use triggers to display in-app messages to users within the audience at a time of your choosing. Unlike push, email, and SMS that just send the message at a specific time, in-app messages require a trigger to determine when to show the message to users while in your app.

<Note>
  Triggers determine when to display the message. To set how often the message should be displayed, see [Schedule and frequency](./in-app-messages-setup#schedule-%26-frequency).
</Note>

<Frame caption="Set a trigger when creating an In-App Message within the OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/sfRFE3uPEhgSxmaa/images/iam/triggers.png?fit=max&auto=format&n=sfRFE3uPEhgSxmaa&q=85&s=dba1e928eb406fc5bd6f2008f4c30869" width="1138" height="382" data-path="images/iam/triggers.png" />
</Frame>

### Requirements

* Review the [In-app message overview](./in-app-messages-setup) for additional setup and requirements.
* Some triggers (documented below) are programmatic and require code to be added to your app before the message can be displayed.
* **Users must be within the audience before a new session starts for the trigger to display the message.** A new session starts when the app is out of focus for at least 30 seconds. See [How in-app messages are shown](./in-app-messages-setup#how-in-app-messages-are-shown).

***

## Trigger types

There are four types of triggers. Each can be combined with **AND** and **OR** operators to only show under very specific conditions.

### On app open

**No code required.** Show message upon next app open. Users within the audience will be eligible to receive the message when they open the app.

* For audience segments that require tags or specific actions that a user joins during a session, they will need to start a new session for the message to be displayed on the next app open.
* For audience segments that target all users or app version filters, the message will be displayed when the user opens the app. Even if a brand new user.

### In-app trigger

**Code required.** Show message when user performs certain actions. Requires a `key` and `value` to be passed into the [`addTrigger` method](./mobile-sdk-reference#in-app-messages) within your app.

<Frame caption="Set a programmatic in-app trigger.">
  <img src="https://mintcdn.com/onesignal/sfRFE3uPEhgSxmaa/images/iam/in-app-trigger.png?fit=max&auto=format&n=sfRFE3uPEhgSxmaa&q=85&s=0732451f4ff8c8bf2f43231432b99a4a" width="1334" height="652" data-path="images/iam/in-app-trigger.png" />
</Frame>

Example will display the in-app message when your app calls the method `addTrigger('trigger', '1')`. Keep in mind the user must be within the audience before a new session starts for the trigger to display the message. See above [Requirements](#requirements) for more details.

#### Important in-app trigger requirements

* `keys` and `values` are space and case sensitive. Check for accidental spaces or casing when setting the trigger.
* You can require multiple `keys` and `values` to be present for the message to display.
  * Each key-value pair using an `AND` condition must be satisfied for the trigger to display the message.
  * Key-value pairs using an `OR` condition will display the message if any of the key-value pairs are satisfied.
* When requiring multiple triggers, you can use the [`removeTrigger` method](./mobile-sdk-reference#in-app-messages#remove-trigger) to remove a trigger if needed.
* `Greater than` and `less than` conditions work for number values eventhough they are set as strings in the code.
  * If you want to display a message when a user reaches level 5. You would set the audience as all users, but would set your trigger to be "level is 5". Each time a user grows a level, you would call `addTrigger("level", "x")` where "x" is the level they reached. This continues to increment until `addTrigger("level", "5");` is called, then the In-App Message will show to the user.

### Session duration

**No code required.** Show message after a specific number of seconds within the current app session. The user must be within the audience before a new session starts for the trigger to display the message. See above [Requirements](#requirements) for more details.

### Duration since last in-app

**No code required.** Show message after a specific number of seconds since the most recent in-app message. The user must be within the audience before a new session starts for the trigger to display the message. See above [Requirements](#requirements) for more details.

This is helpful to include in less urgent or lower priority messages so they do not display too closely to more important messages.

***

## When should this message dismiss?

This option allows you to control how long the message should stay on the screen.

* **Show until dismissed**: The message will show until physically acted upon. Either a close button is clicked or the message is swiped away.
* **Dismiss after certain amount of time**: Set the number of seconds in which the message will be displayed before it is automatically removed from screen. This is helpful if the message is informative and doesn't require user action.

***

## How often do you want to show this message?

While triggers determine when to display the message, this option allows you to control how often the message should be displayed. See [Schedule and frequency](./in-app-messages-setup#schedule-%26-frequency) for more details.

<Frame caption="Image showing the ability to schedule an In-App Message">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/fb6d705-Screen_Shot_2022-09-28_at_3.44.24_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=f52d005f9b59abb767c2968c24359fd2" width="1766" height="642" data-path="images/docs/fb6d705-Screen_Shot_2022-09-28_at_3.44.24_PM.png" />
</Frame>

### Set when and how many times the message shows

**Only once** is default. The in-app message will only show 1 time to the Subscription.

**Every time trigger conditions are satisfied** will show this message each time the Trigger conditions are met.

* For in-app triggers, this may be multiple times a session. For other triggers, it is only once per session.

**Multiple times** allows you to set the specific amount of times this message can be shown and how long to wait in between each display.

* If you set: "`2` times with a gap of `1` **hour** in between" - The message will be allowed to trigger a total of `2` times. The first time when the triggers are met, then the 2nd time when the triggers are met and `1` hour has passed.
* If you set "`12` times with a gap of `30` **days** in between" - The message will show roughly once a month for a year.

***

## FAQ

### Are triggers tags?

Triggers are not tags. Triggers are key-value pairs set within the [Trigger methods of our SDK](./mobile-sdk-reference#in-app-messages). [Tags](./add-user-data-tags) are user data that you can set and use to target users in your audience.

Set tags for segments to use in the audience and use triggers to display the message.

### Can I use multiple triggers?

Yes, you can use multiple triggers. See [Important in-app trigger requirements](#important-in-app-trigger-requirements) for more details.

***

Built with [Mintlify](https://mintlify.com).
