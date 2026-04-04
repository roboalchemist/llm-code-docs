# Source: https://documentation.onesignal.com/docs/en/journeys-actions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey actions

> Define wait periods, branch journeys based on user behavior, and tag users using journey steps.

Use **Journey actions** to control how and when users move through your Journey, personalize experiences, and test outcomes.

## Wait

Delay the user's Journey progression by a specific amount of time—minutes, hours, days, or weeks.

Use it to:

* Space out messages and steps
* Allow time for users to engage with a message before branching

<Frame caption="A wait node with users currently waiting to progress in the journey">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/docs/wait-node.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=13178c10c8f9d0e439c47e601ad00978" width="644" height="391" data-path="images/docs/wait-node.png" />
</Frame>

***

## Wait Until

Hold a user at this step until they meet specific conditions:

* Entering a segment
* Triggering a message event (e.g., specific message delivered, opened, or clicked)
  * **Only one message event per wait until step** is supported at this time.
* Triggering a custom event (e.g., onboarding complete, purchase made)

You can **add multiple conditions** and branch users based on the *first condition they meet*. If those conditions are not met in a certain amount of time, you can set an **expiration branch** to continue users through the Journey or exit them completely.

<Note>
  If a user already qualifies for a condition when they reach this step, they'll move down that branch straight away without waiting. Conditions are evaluated in order (top to bottom / A–Z).
</Note>

Using the Custom Events entry rule you can also add [Event Matching](#event-matching) to control which instance of the user to progress through the Journey if you enter them multiple times.

<Frame caption="Wait Until user is in a segment or triggers a custom event">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/journeys/journeys-wait-until-action.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=1a27c7d1bb9e26bc68a9980d9662b400" width="952" height="1462" data-path="images/journeys/journeys-wait-until-action.png" />
</Frame>

When a custom cvent matches a condition, that event is stored on behalf of the user and may be [referenced in Liquid syntax](./custom-events#liquid-syntax-for-custom-events) when sending Journey messages.

### Event Matching

Using the Custom Events entry rule, you can have users enter a Journey multiple times. With the Wait Until step's **Event Matching** setting, you can control which instance of the user to progress through the Journey.

Requirements:

* Set the Journey Entry Rules to use a custom event.
* Include an event property when entering users into the Journey.

For example, you have a "Survey Reminder" Journey. You have multiple surveys which means users can enter the Journey multiple times (once for each survey). You want to send a reminder message if they did not complete the survey or remove them if they did.

You can use the **Event Matching** setting to control which instance of the user to progress through the Journey.

**Example**:

<Steps>
  <Step title="Set the Journey Entry Rules and custom event properties">
    Set the Journey Entry Rules to use a custom event. **Example**: `survey_start`

    <Frame caption="Journey Entry Rules using a custom event">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/journeys/survey_start.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=146924d7b2a759c1894496745a078c4f" width="469" height="298" data-path="images/journeys/survey_start.png" />
    </Frame>

    Users will enter the Journey via the [Custom Event API](/reference/create-custom-events).

    The custom event will have the `name` set to `survey_start` and a `payload` property `survey_id` with a value of the survey they are taking (e.g., `survey_1`).

    ```json Entrance Trigger Event Example theme={null}
    {
      "events": [
        {
          "external_id": "UserA",
          "name": "survey_start",
          "properties": {
              "survey_id": "survey_1"
          }
        }
      ]
    }
    ```
  </Step>

  <Step title="Create a Wait Until step and custom event properties">
    Set the Wait Until condition to use a custom event. **Example**: `survey_complete`

    Set the **Event Matching** option to specify which instance of the user to progress through the Wait Until step by matching the:

    * **Trigger Event Property**: set in the Journey entrance trigger event (e.g., `survey_id`)
    * **Wait Event Property**: set in the Wait Until event (e.g., `survey_type`)

    ```json Wait Until Event Example theme={null}
    {
      "events": [
        {
          "external_id": "UserA",
          "name": "survey_complete",
          "properties": {
              "survey_type": "survey_1"
          }
        }
      ]
    }
    ```

    When the value of `survey_id` matches the value of `survey_type`, that instance of the user will progress through the Journey.

    <Warning>
      You can use the same properties (e.g., `survey_id`) in both the **Trigger Event Property** and the **Wait Event Property**. The example uses different properties (e.g., `survey_id` and `survey_type`) to demonstrate the concept.

      Properties are case-sensitive! `survey_1` does not equal `Survey_1`.
    </Warning>

    **Expiration branch**:

    If the Wait Until event does not occur within the expiration time, the user will progress through the Journey. This example gives the user 1 week to complete the survey.

    <Frame caption="Wait Until step using a custom event">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/journeys/survey_complete.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=59ad63e1af649a09f5c3a18a32a979b8" width="488" height="648" data-path="images/journeys/survey_complete.png" />
    </Frame>
  </Step>

  <Step title="Add a message step">
    To complete the example, add a message step within the Expiration branch to send the reminder.

    <Frame caption="Message step within the Expiration branch">
      <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/journeys/survey_reminder.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=1a367c270dec75e70a6409b3c66be36e" width="955" height="572" data-path="images/journeys/survey_reminder.png" />
    </Frame>
  </Step>

  <Step title="Test it out!">
    After following the steps above, you can test it:

    * Replace the `external_id` in the [Custom Event API](/reference/create-custom-events) with your external ID
    * Trigger the `survey_start` event with a `survey_id` of `survey_1`
      * You will see your user enter the Journey and flow into the Wait Until step

    <Warning>
      Events are not immediate but very quick! You may need to wait a few minutes before the event is processed.

      Check the Custom Events list to see if the event was processed.
    </Warning>

    * Trigger another `survey_start` event with a `survey_id` of `survey_2`
      * You will see 2 users enter the Journey and Wait Until step
    * Trigger the `survey_complete` event with a `survey_type` of `survey_1`
      * You will see your user progress through the Journey
    * Trigger another `survey_complete` event with a `survey_type` of `survey_2`
      * You will see both instances of your user progress through the Journey and exit

    <Check>
      You completed the Journey custom event example with Event Matching!
    </Check>
  </Step>
</Steps>

***

## Time Window

Restrict when users can move to the next step in the Journey based on **specific days and times**.

**Example**: Only allow users to receive a message on weekends in the evening.

<Frame caption="Screenshot showing an example of a time window node">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/31f4664-Screenshot_2024-03-21_at_15.56.12.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=07267995ec158e725ecd0c6afb28af20" width="540" height="448" data-path="images/docs/31f4664-Screenshot_2024-03-21_at_15.56.12.png" />
</Frame>

### How time window behavior works

If a user enters this node outside the allowed time:

* OneSignal sets a timer to delay the user until the **next available window**
* The **entry time into the window is randomized**

**Example**:
If your time window is Tuesdays from 1:00 PM to 6:00 PM PST, and a user hits the node on Monday, they may continue Tuesday at a random time like 5:45 PM.

***

## Yes/No branch

Branch users based on **segment membership** or **message behavior**.

### Segment membership

Create branches based on what segment a user is in.

**Example**:
If users are tagged by plan type:

* “Free” branch = promote upgrade
* “Paid” branch = highlight premium features

### Message behavior

Branch based on interaction with previous messages in the Journey:

* **Push**: Clicked, Delivered
* **Email**: Clicked, Opened, Delivered

**Note**: Safari does not support Confirmed Delivery.

***

## Split Branch

Randomly distribute users across different paths to test messaging, channels, or Journey flows.

<Frame caption="An example of a 3-way split branch">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b7a62545ad25878949fe7b0fffc1b64ddee30730dbe351cd51eaea5ed8e9964f-Screenshot_2024-12-23_at_1.37.49_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=b9f67d64e3721cba629798663860be3f" width="1916" height="1430" data-path="images/docs/b7a62545ad25878949fe7b0fffc1b64ddee30730dbe351cd51eaea5ed8e9964f-Screenshot_2024-12-23_at_1.37.49_PM.png" />
</Frame>

<Warning>
  Once a Journey is live, you **cannot edit** a Split Branch. To change the number of branches, create a new Journey.
</Warning>

### How it works

* Up to 20 branches
* Set equal or custom percentage splits
* Percentages round to whole numbers (e.g., 3-way split becomes 34/33/33)
* Distribution may vary slightly with small sample sizes

<Frame caption="Split branch settings">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/517165a9f4f78a584ce252ae7581c6fc48f05e040a0ba921d759392577218988-Screenshot_2024-12-23_at_11.28.53_AM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=57308fa43c451864c80af0c97a4a9cfa" width="460" height="456" data-path="images/docs/517165a9f4f78a584ce252ae7581c6fc48f05e040a0ba921d759392577218988-Screenshot_2024-12-23_at_11.28.53_AM.png" />
</Frame>

By default, users are re-randomized each time they re-enter a Journey.
To keep them on the same branch, turn off **Randomize on re-entry**.

Use the **Tag User** action to track which branch a user followed.

### A/B/N Tests

Use nested Split Branches to test more than two variants simultaneously.

**Example**:
To split users equally across 3 variants:

1. First branch: 33% vs 67%
2. Under the 67% branch, add another 50/50 Split Branch

This gives \~33% on each path.

### Control Groups

Test the impact of messaging by leaving one branch empty (no message nodes). This lets you compare against users who receive no message at all.

### Choosing a Winner

Once a winning variant is identified, update the branch to send **100%** of traffic down that path.

To continue measuring impact over time, consider keeping a small **holdout group**—a percentage of users who don't receive the winning message.

***

## Tag User

Use this action to apply or remove tags during a Journey.

**Common use cases**:

* Track Journey progress (e.g., `journeyStep: welcome`)
* Power in-app messages by tagging users at key moments
* Exclude users from other Journeys using active tags

<Frame caption="A simple onboarding/welcome flow">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/99f568ee808ea29f528fd83830bf9a7ebed7e590e95d34047e6495fc810015f2-image.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=cb4cbbbe43b252f44f22f08379b9b709" width="237" height="485" data-path="images/docs/99f568ee808ea29f528fd83830bf9a7ebed7e590e95d34047e6495fc810015f2-image.png" />
</Frame>

### Example: onboarding flow control

1. First step: Add a tag (e.g., `onboardingJourney: active`)
2. Use this tag to create a segment for exclusion from other Journeys
3. Last step: Remove the tag by setting the value to blank

<Frame caption="A tag node settings to remove the tag from the user">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d4199348801030819f94a56976af9b180a77434be6f8b76fd24c7c5a283fc0ba-image.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=004b49369e6eb2a13a55dfa1b93855bf" width="651" height="193" data-path="images/docs/d4199348801030819f94a56976af9b180a77434be6f8b76fd24c7c5a283fc0ba-image.png" />
</Frame>

***

### Best practice: Using tags with webhooks or personalization

When you add or remove tags in a Journey, it can take a short time before those changes are ready to use in the next step. To make sure everything works smoothly:

* **For Webhooks**: Add a short wait after setting a tag before sending data with a webhook.
* **For Personalization**: Add a short wait after setting or removing a tag before using it in an email to personalize content.

<Tip>
  We recommend adding a **15-minute Wait node** between the Tag action and the next step. This ensures the tag is fully ready, so your webhook or email always includes the correct data.
</Tip>

***

Built with [Mintlify](https://mintlify.com).
