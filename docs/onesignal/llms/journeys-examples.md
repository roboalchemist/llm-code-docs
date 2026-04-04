# Source: https://documentation.onesignal.com/docs/en/journeys-examples.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey examples

> Common examples to get your journey started.

<div style={{ display: "flex", justifyContent: "center", margin: "2rem 0" }}>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/TnsBCXe_Opw?si=feFpzblCm_Hcpbd4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</div>

<Note>
  For additional resources, check out our blog!

* [Maximizing User Engagement: The Synergy of Push Notifications and Email](https://onesignal.com/blog/use-push-notifications-and-email-together/)
* [Consistently Drive Value with Journeys](https://onesignal.com/blog/consistently-drive-value-with-journeys/)
* [Increase Engagement with Email for Cross-Channel Journeys](https://onesignal.com/blog/increase-engagement-with-email-for-cross-channel-journeys/)
* [Improve Retention with In-App and SMS for Journeys](https://onesignal.com/blog/improve-retention-with-in-app-and-sms-for-journeys/)
</Note>

***

## Onboarding

| Journey setting    | Description                                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry rules**    | **User matches the segment criteria.** Subscribed users, future additions only (you only want people who subscribe going forward; you don't want existing users to receive this). |
| **Exit rules**     | **They moved through the entire journey.**                                                                                                                                        |
| **Re-entry rules** | No                                                                                                                                                                                |
| **Content**        | Welcome new users to your app or website; encourage them to accomplish certain tasks over the first several days or weeks.                                                        |

<Frame caption="Onboarding welcome journey example">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6f27e25-Onboarding.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=d78551d919bedfaa6c9e9f84d33544b8" width="1427" height="1470" data-path="images/docs/6f27e25-Onboarding.png" />
</Frame>

## Re-engagement campaign

| Journey setting    | Description                                                                                                                                                                              |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry rules**    | **User's last session is greater than 7 days;** subscribed users. (You may want to **exclude certain segments** like paid customers if your goal is to get more free users coming back.) |
| **Exit rules**     | **They moved through the entire journey or meet certain conditions** — exit when the user becomes active in your app/website.                                                            |
| **Re-entry rules** | **Yes, after a certain amount of time: 7 days** (re-engagement can happen whenever they haven't opened your app in a while).                                                             |
| **Content**        | Remind users to come back to your app when they haven't opened it in a while, and entice them with rewards or discounts.                                                                 |

<Frame caption="Re-engagement campaign journey example">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/eb69395-Reengagement.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=a3afdfa3aec10e56ed49095ed5b0ef61" width="1427" height="1495" data-path="images/docs/eb69395-Reengagement.png" />
</Frame>

## Abandoned cart

<Card title="Abandoned cart example" href="./abandoned-cart" icon="money-bill" cta="Learn more">
  Use Custom Events or Tags to track cart activity and send abandoned cart messages.
</Card>

## Promotional campaign

| Journey setting    | Description                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry rules**    | **User matches the segment criteria.** Subscribed users or target the segment your promotional campaign is relevant to.                                      |
| **Exit rules**     | **They moved through the entire journey or meet certain conditions.** Select a segment that defines the goal you want to target (e.g., users who purchased). |
| **Re-entry rules** | **No** (if this is a one-off campaign, send it once).                                                                                                        |
| **Content**        | Prepare them for the event, remind them when it starts, and offer a discount or reward as it gets close to ending.                                           |

<Frame caption="Promotional campaign journey example">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b643432-Promo.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=a7a4f73dc5a9d32244e60d89802890b2" width="1487" height="1596" data-path="images/docs/b643432-Promo.png" />
</Frame>

## Send message after user leaves app if action incomplete

### Initial setup

1. Use [data tags](./add-user-data-tags) to mark that the action needs to be performed by the user. Remove the tag when the action is completed.
2. Set up the [segment](./segmentation) for this tag.

| Journey setting    | Option                                                        | Description                                                                               |
| ------------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Entry rules**    | The user's last session is greater than the amount of time.   | The amount of time you determine the user has been last active on your app or website.    |
| **Audience**       | Include the segment you want to target with the tag.          | These are the users eligible to receive the message.                                      |
| **Exit rules**     | Exit when the user no longer matches the audience conditions. | When the user leaves the segment, they are no longer eligible for the journey message.    |
| **Re-entry rules** | Yes, after a certain amount of time.                          | The amount of time you want to wait for the user to be eligible to get the message again. |

### Journey steps

<Steps>
  <Step title="Add the desired message(s)">
    Add the desired message(s).
  </Step>

  <Step title="Set a wait node for the amount of time you want the user to wait">
    This can be a high or low number depending on if you want the message to
    show again as a reminder. In the example, we use 104 weeks (2 years).
  </Step>
</Steps>

## A/B test within a journey

Using a **split branch** node, you can set a 50/50 split within your journey. Create two different message templates and as your users flow through, half will get "Template A" and the other "Template B".

You can then export your message data to check the [analytics](./analytics-overview) as desired.

<Frame caption="An A/B test">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e9092ab-small-Screenshot_2023-05-10_at_2.47.50_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=838b3da11cb249654df32addd7db4005" width="1608" height="772" data-path="images/docs/e9092ab-small-Screenshot_2023-05-10_at_2.47.50_PM.png" />
</Frame>

## Display in-app messages in order and once per day

In this example, we want to display 3+ in-app messages in a row, but only show them once per day. If a user doesn't open the app, they will still see it next time they open the app.

### Initial setup

<Steps>
  <Step title="Create a new segment">
    Create a segment called `iam_journey` with filter: User Tag `iam_journey` is `1`

    1. You can change `iam_journey` to whatever name you choose.
    2. This tag will be set on each user that finishes the journey and gets all messages.

    <Frame caption="Segment creation screen">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/87ac3eb-Screenshot_2023-09-07_at_5.19.11_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=af6519e08ca43ab89576073245f641b8" width="803" height="433" data-path="images/docs/87ac3eb-Screenshot_2023-09-07_at_5.19.11_PM.png" />
    </Frame>
  </Step>

  <Step title="Create the in-app messages">
    See [design in-app messages with drag and drop](./design-your-in-app-message) for more.
  </Step>

  <Step title="Set up the following journey">
    | Journey setting    | Option                                | Description                                                                              |
    | ------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------- |
    | **Entry rules**    | User matches the segment criteria     | These are the users eligible to receive the message.                                     |
    | **Audience**       | Include segment & exclude segment     | Include the "Subscribed Users" segment. Exclude the "`iam_journey`" segment from step 1. |
    | **Exit rules**     | They moved through the entire journey | No additional conditions necessary.                                                      |
    | **Re-entry rules** | Yes, after a certain amount of time   | 2 minutes                                                                                |

    ### Journey steps

    Repeat this order for the number of messages you want to display. In this example, we will display 3 in-app messages (IAM 1, IAM 2, IAM 3).

    1. **Add an in-app message step.**
       1. Name the message, for example: `IAM 1`.
       2. At the bottom of the message, set **delivery schedule** to **1 day**.

    2. **Add a yes/no branch action before the in-app message step.**
       1. Set your branching condition: previous message behavior: "`IAM 1` viewed".
       2. **Follow the No branch**
          1. Drag the `IAM 1` to the No branch.
          2. Add a wait step for 1 day.
       3. **Follow the Yes branch**
          1. Within the Yes branch, repeat steps 1 & 2 for all messages, replacing `IAM 1` with the new in-app message (e.g., `IAM 2`, `IAM 3`).
          2. At the final Yes branch, add **tag user** action.
             1. Tag the same key used in Initial setup → Step 1 segment.
                1. Example `iam_journey : 1`.

    <Frame caption="The complete journey">
      <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b5b9c74-Screenshot_2023-09-15_at_12.04.09_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=4e19ed5c3c321711bbd6131f1a86c111" width="1376" height="1522" data-path="images/docs/b5b9c74-Screenshot_2023-09-15_at_12.04.09_PM.png" />
    </Frame>
  </Step>
</Steps>

## Limited entry journey

Ensure users can only enter a journey a limited number of times while controlling the experience at each stage.

| Journey setting    | Description                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry rules**    | User matches the segment criteria (for example, subscribed users or any relevant target segment).                                                   |
| **Audience**       | Include your target segment. Exclude users with the tag <code>journey\_count = 2</code> to cap entries at two times.                                |
| **Exit rules**     | They moved through the entire journey.                                                                                                              |
| **Re-entry rules** | Yes, after a certain amount of time: 15 days.                                                                                                       |
| **Content**        | Provide a first-time experience on initial entry, and a tailored second-time experience on re-entry. Prevent any further entries beyond the second. |

<Frame caption="Limited entry settings">
  <img src="https://mintcdn.com/onesignal/Kryww3qVcdmjY27T/images/journeys/limited-entry-settings.png?fit=max&auto=format&n=Kryww3qVcdmjY27T&q=85&s=71647a50f354d2174200298b11678e6b" width="646" height="1490" data-path="images/journeys/limited-entry-settings.png" />
</Frame>

### Initial setup

<Steps>
  <Step title="Prepare your tag strategy">
    Use a user tag named <code>journey\_count</code> to track entries.\
    You don’t need to pre-create tags; they’ll be added when you set them in the journey.\
    See <a href="./journeys-actions#tag-user">tag action for details</a>.
  </Step>

  <Step title="Configure audience include/exclude">
    In journey audience:

    * Include your target segment (for example, “Subscribed Users”).
    * Exclude users where user tag <code>journey\_count</code> is <code>2</code>.
  </Step>

  <Step title="Set re-entry rules">
    Set re-entry rules to “Yes, after a certain amount of time: 15 days.”\
    This allows exactly one re-entry between the first and second runs.
  </Step>
</Steps>

### Journey steps

<Frame caption="Limited entry flow">
  <img src="https://mintcdn.com/onesignal/Kryww3qVcdmjY27T/images/journeys/limited-entry.png?fit=max&auto=format&n=Kryww3qVcdmjY27T&q=85&s=3d8652adedf2610bb444ee217eb52856" width="932" height="1468" data-path="images/journeys/limited-entry.png" />
</Frame>

<Steps>
  <Step title="Add a yes/no branch at the start">
    Condition: user tag <code>journey\_count</code> equals <code>1</code>.

    * **Yes branch** = returning users (second entry).
    * **No branch** = first-time users (no tag present yet).
  </Step>

  <Step title="No branch (first time entry)">
    * Add tag user action: set <code>journey\_count</code> to <code>1</code>.
    * Send your first-time messages and actions.
    * Continue to end or additional logic as needed.
  </Step>

  <Step title="Yes branch (second time entry)">
    * Add tag user action: set <code>journey\_count</code> to <code>2</code>.
    * Send your returning-user messages and actions.
    * Continue to end or additional logic as needed.
  </Step>

  <Step title="Enforce the limit">
    Because the audience excludes users with <code>journey\_count = 2</code>, any attempted third entry will be blocked automatically.
  </Step>
</Steps>

## Recurring journeys for specific days

Send recurring messages that align with a specific day of the week (e.g., weekly promotions, event reminders).

| Journey setting    | Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| **Entry rules**    | User matches the segment criteria (for example, subscribed users or another relevant target segment). |
| **Audience**       | Include your target segment.                                                                          |
| **Exit rules**     | They moved through the entire journey.                                                                |
| **Re-entry rules** | Yes, after a certain amount of time: 7 days.                                                          |
| **Content**        | A weekly message sent on a specific day (e.g., every Friday).                                         |

<Frame caption="Recurring journey settings">
  <img src="https://mintcdn.com/onesignal/lYMMkFJp3v40a2sJ/images/journeys/recurring-journey-settings.png?fit=max&auto=format&n=lYMMkFJp3v40a2sJ&q=85&s=774b448a2c3789fcf5173ad71630d2aa" width="648" height="1446" data-path="images/journeys/recurring-journey-settings.png" />
</Frame>

### Initial setup

<Steps>
  <Step title="Configure audience">
    Include your target segment so eligible users can enter the journey at any time during the week.
  </Step>

  <Step title="Set re-entry rules">
    Set re-entry rules to “Yes, after a certain amount of time: 7 days” to enable weekly recurrence.
  </Step>
</Steps>

### Journey steps

<Frame caption="Recurring journey flow">
  <img src="https://mintcdn.com/onesignal/lYMMkFJp3v40a2sJ/images/journeys/recurring-journey-steps.png?fit=max&auto=format&n=lYMMkFJp3v40a2sJ&q=85&s=12657ad8e9b0cfc2de32a9d87f9eed2c" width="598" height="1460" data-path="images/journeys/recurring-journey-steps.png" />
</Frame>

<Steps>
  <Step title="Add a time window node (first step)">
    Configure the time window to filter for your target day of week (e.g., Friday).\
    Users entering the journey will wait until the next matching day.
  </Step>

  <Step title="Add your message after the time window">
    Place the message node immediately after the time window so it sends when the day is reached.
  </Step>

  <Step title="End the journey">
    Let users exit after the message sends. With re-entry at 7 days, they will rejoin and repeat weekly.
  </Step>
</Steps>

<Note>
  Caveat: update the message content regularly to avoid repeating the same copy each week.
</Note>

## Progressive journeys ([event-driven](./custom-events#custom-events))

Escalate engagement depending on user progression, monitored with [wait until](./journeys-actions#wait-until) conditions on custom events.

| Journey setting    | Description                                                                                                                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Entry rules**    | **Custom Event** = `Progression_Level`, with filter `progression_level = 0`.                                                                                                                                                                                                                                                          |
| **Audience**       | Optional segment filter. You can run this for all users or restrict to a subset; no tags required.                                                                                                                                                                                                                                    |
| **Exit rules**     | - They moved through the entire journey.<br />- Or when maximum progression level is reached (e.g., `progression_level = 3`).<br />- Optionally: exit when a **Wait Until** node expires.<br />- Optionally: branch from a **Wait Until** node to tag users who do not complete the event, leading them into a re-engagement journey. |
| **Re-entry rules** | No                                                                                                                                                                                                                                                                                                                                    |
| **Content**        | Stage-based messages that escalate as users complete milestones (emails in this example).                                                                                                                                                                                                                                             |

<Frame caption="Progression journey flow">
  <img src="https://mintcdn.com/onesignal/86gjHZhU_WHClFAO/images/journeys/progression-journeys.png?fit=max&auto=format&n=86gjHZhU_WHClFAO&q=85&s=d1115ca7a2a7c06aa0cc0fa4b81a0533" width="690" height="1482" data-path="images/journeys/progression-journeys.png" />
</Frame>

### Journey steps

<Steps>
  <Step title="User enters the journey">
    All eligible users enter based on entry rules.\
    Trigger: **Custom Event** `Progression_Level` with `progression_level = 0`.\
    Start: **Immediately**.
  </Step>

  <Step title="Level 1">
    * Wait until custom event `Progression_Level` occurs with `progression_level = 1`.
    * Send: **Level 1 Complete!** message.
    * (Optional) Apply expiration on the wait node → exit user if milestone not reached.
    * (Optional) Branch: if expiration hits, tag the user and send them into a re-engagement journey.
  </Step>

  <Step title="Level 2">
    * Wait until custom event `Progression_Level` occurs with `progression_level = 2`.
    * Send: **Level 2 Complete, you are doing great!** message.
    * (Optional) Apply expiration or branch/tag to re-engagement.
  </Step>

  <Step title="Level 3">
    * Wait until custom event `Progression_Level` occurs with `progression_level = 3`.
    * Send: **You’ve reached level 3!** message.
    * (Optional) Apply expiration or branch/tag to re-engagement.
  </Step>

  <Step title="Exit">
    End the journey once users complete Level 3, or when a Wait Until node expires.\
    Optionally, use branch/tag paths to route stalled users into a re-engagement track.\
    Schedule: **Start immediately**, **Never stops**.
  </Step>
</Steps>

<Note>
  Benefit: this method ensures progression happens only when real engagement signals occur.\
  Adding expiration and branch/tag logic lets you gracefully handle stalled users — either exiting them or re-routing into a re-engagement journey.
</Note>

***

Built with [Mintlify](https://mintlify.com).
