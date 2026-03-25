# Source: https://documentation.onesignal.com/docs/en/email-warm-up.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email warm up guide

> Warm-up ensures inbox providers trust your email sends. Learn how to gradually increase volume while maintaining high engagement and low complaint rates.

## What is Email Warm Up and why does it matter?

Inbox providers are inherently cautious. They’re unlikely to trust large volumes of email from domains that are new to sending or have recently changed behavior.

Email warm up is the process of gradually increasing your sending volume while maintaining high-quality performance—low spam complaints, minimal bounces, and strong engagement (opens and clicks).

A successful warm up shows inbox providers your emails are wanted, expected, and trustworthy. It also gives you a chance to catch deliverability issues early on.

<Note>
  A gradual warm up reduces risk and helps surface issues early—before they escalate into lasting damage to your deliverability or sending reputation.
</Note>

Warming up isn’t just about ramping volume—it’s about proving that your sending behavior is healthy and your audience is engaged.

Make sure you are following [Email Reputation Best Practices](./email-reputation-best-practices).

***

## Do I need to Warm Up my email sending?

You should warm up your sending if:

* **You send over 2,000 emails per day.**
* **You're new to OneSignal Email.** Our IPs are warm, but sending from new IPs resets trust with inbox providers.
* **You're using a new sending domain or subdomain.**
* **You're increasing your daily volume by more than 20%.**
* **You haven’t sent high volumes in the past 30 days.**

Even at lower volumes, consistently maintaining good sender reputation and engagement is essential.

***

## How long does warm up take?

It depends on your sending goals—how much you ultimately need to send daily.

As a rule of thumb:

* **Increase daily send volume by \~20%.**
* **Advanced senders** with excellent reputation may ramp up by **30% daily**, but only if engagement stays high.

<Tip>
  Use [Google Postmaster Tools](./google-postmaster-tools) to monitor Spam Rate and domain reputation.
</Tip>

Here are conservative warm up time estimates based on a **20% daily** increase, **starting at 300** emails:

| **Target Daily Volume** | **Days to Reach** |
| ----------------------- | ----------------- |
| 50,000                  | 29 days           |
| 100,000                 | 33 days           |
| 150,000                 | 35 days           |
| 200,000                 | 37 days           |
| 300,000                 | 39 days           |
| 500,000                 | 42 days           |
| 1,000,000               | 46 days           |

**Note**: These are *approximate estimates*. Your timeline may shorten if you:

* Increase volume by **30% daily**
* Start from a **higher baseline** (e.g., 1,000/day)

Only increase Warm Up speed if you have good reputation, high engagement and low spam reports.

<Danger>
  If your Spam Rate is high or Engagement Rates are low, you may need to pause Warm Up and ensure you are following [Email Reputation Best Practices](./email-reputation-best-practices) before proceeding.
</Danger>

***

## How do I Warm Up my email sending?

Email warm up is all about **gradual volume increase** and **strong engagement**.

### 🔑 Start with your most engaged recipients

Begin with your most active users—those who open, click, and engage with your emails.

<Warning>
  Do **not** start by sending to dormant, inactive, or outdated email addresses. Low engagement, spam reports, high unsubscribes and high bounce rates early in the process can negatively impact your deliverability.
</Warning>

### Warm Up methods

#### 1. Implement low-volume campaigns first

Start with smaller, behavior-based sends like:

* Welcome emails
* Rewards or loyalty emails

These are naturally lower in volume and show consistent performance—ideal for early-stage warm up.

#### 2. Use OneSignal’s Email Auto Warm Up feature

OneSignal’s **Auto Warm Up** automatically distributes a single email over time.

Great for non-urgent, delay-tolerant emails such as:

* Newsletters
* Evergreen content
* Onboarding flows

Specify your audience and let OneSignal pace the delivery to avoid volume spikes. Run multiple Auto Warm Up emails back-to-back until you reach your desired daily volume.

<Frame caption="Graph displaying send volume over time based on an auto-recommended schedule for a warm up email, based on total audience size.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1de3d58-Auto_Warm_Up_-_Rec_Schedule.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=daf384f7251ce65ac2711cc6ab238c00" width="3168" height="1886" data-path="images/docs/1de3d58-Auto_Warm_Up_-_Rec_Schedule.png" />
</Frame>

<br />

<br />

<Accordion title="How to use Auto Warm Up">
  ### Select Auto Warm Up

  1. Compose Your Email: Start creating your email message as usual.
  2. Select Auto Warm Up: Within the "Delivery Schedule" section, you'll find the option to "Send with Auto Warm Up".

  OneSignal will automatically generate and display a sending schedule. This schedule is generated based on your past email delivery volumes, scheduled Auto Warm Up emails, and the size of your current audience.

  <Frame caption="Select Auto Warm Up">
    <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e2748b8-Auto_Wam_Up.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=d79808aea9a80c66514d0f85436e8e9f" width="2598" height="1258" data-path="images/docs/e2748b8-Auto_Wam_Up.png" />
  </Frame>

  <Warning>
    OneSignal calculates the send schedule based on sending activity of the last 3 weeks. If there is a time gap in sending, the system might assume a lower baseline volume, which affects the recommended warm up schedule.
  </Warning>

### Monitoring the Auto Warm Up

  After sending, you can monitor the progress of sending by viewing the scheduled and total sent messages in the [Email message report](./email-message-reports).

  <Frame caption="Auto Warm Up report">
    <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8515b46-Auto_Warm_Up_-_Report_2.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=7f3b931ed3a64dd8eeff0ec0c767f1d3" width="3168" height="2332" data-path="images/docs/8515b46-Auto_Warm_Up_-_Report_2.png" />
  </Frame>

### Adjusting the start date of your message

  To set a different start date (default is to start the next day), ensure "Send with Auto Warm Up" is selected.

  Then:

  1. Click on the **Edit Auto Warm Up**
  2. Select **Start Date & Time** change the date.

  Typically, Auto Warm Up will start the next time it is 9am, which might be a day ahead. You might notice that you can't change the start time for a recommended schedule, to change the **Start Date and Time** select **Custom Schedule** first.

  <Frame caption="Recommended Sending Time">
    <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/168aa8e-Frame_2.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=34d69130c78f63d9b7732d58a3c351a1" width="1782" height="1048" data-path="images/docs/168aa8e-Frame_2.png" />
  </Frame>

  <Info>
    Recipients are selected at random from your audience, and the email sends are distributed throughout the day. Your Audience members will only receive the Email once per Auto Warm Up campaign.
  </Info>

  <Accordion title="Advanced Auto Warm Up Options">
    ### Customize your Warm Up schedule

    If needed, you may customize the warm up schedule to be more aggressive or conservative.

    1. Access the Schedule: Click **Edit Auto Warm Up** to view all Auto Warm Up Schedules and to customize the schedule.
    2. Make Adjustments: You can adjust the number of emails sent each day or the duration of the warm up period.
    3. Save Your Custom Schedule: Once you've made your changes, save the schedule.

    <Frame caption="Customize the sending schedule of your Warm Up emails.">
      <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7c51acd-Auto_Warm_Up_-_Custom_Schedule.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=5537d7cbc445eb66a5e75b6ed1a7a45b" width="3128" height="1878" data-path="images/docs/7c51acd-Auto_Warm_Up_-_Custom_Schedule.png" />
    </Frame>

    If you customize part of your schedule, OneSignal can auto-fill the remainder based on your adjustments. This ensures a continuous and effective warm-up process. The auto-fill will use the default incremental increase of the sending volume by 20% per day.

    <Frame caption="Auto-complete schedule">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8921401-image.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=1606d83f00b3ee445252d2d636cb5972" width="809" height="534" data-path="images/docs/8921401-image.png" />
    </Frame>

    ### Sending multiple Auto Warm Up emails

    When conducting an Auto Warm Up process, reaching your desired daily volume may require sending more than one email. Sending Sequential Auto Warm Up Emails to achieve your target daily email sending volume.

    📈 *This approach ensures a gradual increase in volume, aligning with best practices for Auto Warm Up.*

    <Frame caption="Scheduling multiple Auto Warm Ups">
      <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/55ff8ad-Auto_Warm_Up_-_Rec_Schedule.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=5559deba0e7c8986b654e8de9e092fad" width="3168" height="1886" data-path="images/docs/55ff8ad-Auto_Warm_Up_-_Rec_Schedule.png" />
    </Frame>

    #### Scheduling your second email

    When you're ready to send a second Auto Warm Up email, OneSignal automatically schedules it for the next available time slot.

    * 🕒 This usually occurs after the completion of your first email's Auto Warm Up cycle.
    * 🧠 No need to manually adjust the date for the second email; OneSignal calculates the optimal time for you.

    <Info>
      You are more than welcome to move the start date, and customise the schedule of any Auto Warm Up emails. We recommend making sure that the total volume of emails being sent meets the recommended warm up schedule. If you have any questions, always reach out to `support@onesignal.com`.
    </Info>
  </Accordion>

## Cancelling an active Warm Up email

  To cancel an active Auto Warm Up email message:

  1. Navigate to the Email page of your OneSignal Dashboard.
  2. Navigate to the email you want to cancel.
  3. Click on the options menu (three vertical dots) on the right side.
  4. Select "Cancel".

  <Frame caption="Cancel Auto Warm Up">
    <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0d1af98-CSV_Template_Example_3.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=7adb46387602e55b07ad2430e6b216f3" width="832" height="421" data-path="images/docs/0d1af98-CSV_Template_Example_3.png" />
  </Frame>
</Accordion>

#### 3. Use Split Branching in Journeys

For Journey-based sends, combine:

* **[Split Branches](./journeys-actions#split-branch)**
* **[Wait Nodes](./journeys-actions#wait)**

This lets you control volume across multi-step flows while maintaining logic and timing.

<Frame caption="Warm Up using Split Branches + Wait Nodes">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/email/split-branch-with-wait-node.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=1c2ed342b01f7d36fa210b482b853673" width="999" height="1197" data-path="images/email/split-branch-with-wait-node.png" />
</Frame>

***

## Summary

Warm up is essential when:

* You’re new to a platform or domain.
* Your volume is increasing significantly.
* You’ve had sending inactivity.

Start small. Prioritize engagement. Monitor performance.

A strong warm up leads to better deliverability, long-term inbox placement, and higher ROI.

Learn more about [Google Postmaster Tools](./google-postmaster-tools) and [Email Deliverability Best Practices](./email-reputation-best-practices).

<br />

<br />

<Accordion title="Email Warm Up FAQ">
  ### Do I need to warm my subdomain, if my domain is already warm?

  Yes, it's advisable to warm up each subdomain separately, even if the main domain has a good reputation. Each subdomain is treated uniquely by ISPs.

### Why do I need to send more than one Warm Up Email?

  Having multiple warm up email messages is necessary if your first warm up email message only gets you to half the desired volume

  Multiple email messages ensure a gradual and steady increase in email volume, which is crucial for building a solid sender reputation without triggering spam filters.

  For example, if you're trying to warm your domain to your full audience volume, you might have to send out multiple emails to your full audience because each warm up email is distributed over many days.

### What is the difference between Domain & IP Warm Up?

#### Domain Warm-Up

* **Necessity**: Domain warm up is essential whenever you migrate to a new email platform.
* **Purpose**: Gradually building a positive reputation for your new or inactive email domain.
* **Process**: Involves sending emails in increasing volumes over time to establish trust with Inbox Service Providers (ISPs).
* **Target Audience**: Particularly crucial for new customers transitioning to a platform like OneSignal.
* **OneSignal Advantage**: 🌟 *OneSignal can automate this process, making it seamless and efficient for users to establish a strong domain reputation without the hassle.*

#### IP Warm-Up

* **When It's Needed**: This is required if you're using dedicated IP addresses that haven't previously been warmed up.
* **Focus**: Centers on establishing a good reputation for your email server's IP address.
* **OneSignal Advantage**: 🌟 \_OneSignal automates this process in the background. We offer dedicated IPs and can help manage the warming process on your behalf. Reach out to us to inquire about dedicated IPs.

### OneSignal vs. Bring Your Own ESP

* **With Third-Party ESPs** (e.g., SendGrid, Mailchimp, Mailgun): You're responsible for managing both your IP address and domain reputation.
* **With OneSignal Email Delivery**: We manage your IP reputation, but ensuring your domain is 'warm' and has a good reputation remains your responsibility.

### Considerations for High-Volume Senders

* **Transitioning Platforms**: High-volume senders typically start a new subdomain when moving to another platform, as using the same subdomain across different ISPs can lead to DNS issues.
* **Avoiding Complications**: Starting fresh with a new subdomain for warming is often simpler than transferring an established domain, especially to avoid disruptions in email sending during the transition.

### What's our recommended Warm Up Schedule?

  This is the schedule to follow for sending emails that will increase the likelihood of deliverability and reduce ISPs' greylisting, rate-limiting, or blocking your domain or IP address.

  | Stage | Total email sends / day           |
  | ----- | --------------------------------- |
  | 1     | 300                               |
  | 2     | 360                               |
  | 3     | 432                               |
  | 4     | 518                               |
  | 5     | 622                               |
  | 6     | 727                               |
  | 7     | 896                               |
  | 8     | 1075                              |
  | 9     | 1548                              |
  | 10    | 2229                              |
  | 11    | 2675                              |
  | 12    | 3210                              |
  | 13    | 3852                              |
  | 14    | 4622                              |
  | 15    | 5547                              |
  | 16    | 20% increase in send volume daily |

  <Info>
    Follow a 20% daily increase for your send volume from day one. If you have a period of significantly lower sending, and you want to send a message to a larger segment, we recommend lowering your sending amount to align with your recent sending habits, and then increasing it again by 20% a day.
  </Info>

  Another example schedule is: If your highest send volume in the last 21 days is 700, and you want to hit an audience of 2000 recipients, your schedule should look like:

  | Day | Number |
  | --- | ------ |
  | 1   | 700    |
  | 2   | 840    |
  | 3   | 1008   |
  | 4   | 1210   |
  | 5   | 1452   |
  | 6   | 1742   |
  | 7   | 2000   |

### Why are only some of my emails failing?

  When emails fail during warmup, this can indicate the volume is too high for the domain's current reputation with the ISPs. Typically, this failure reason surrounding this issue would be indicated by a `602(too old)` error.

  You may notice that the failure only occurs with certain ISPs such as Google or Outlook. This would also be a characteristic of throttling from the ISP due to reputation.

  If you are seeing the `602` error within the [Audience Activity](/reference/export-csv-of-events) failures, the recommendation would be to pull back your volume to the amount that was previously successfully delivered and slowly increase daily.

### How can I edit an email that is being warmed up?

  Editing is not yet available if your email warm up send has already started. To cancel a sending or scheduled email message, navigate to the email index, click on the three dots on the right side of the row to open up options, and select "Cancel". The status of the email will update to `Canceled`.

### How do I A/B Test my Auto Warm Up email?

  You will need to create two separate email messages with different segments and customize the schedule of both. If you're looking to send a 50/50 split AB test, Create two segments of the appropriate size, then for each email, select auto warm up and customize the start date and sending volume for each stage so that they sum to recommended values.

### Dedicated IP vs Shared IP

  By default, your messages are sent from a shared IP address that helps maintain reputation, which means you only need to worry about warming your domains.

  You can also set up a dedicated IP—an IP address for sending email employed by a single user or account. Since only your email will be sent from that IP, only you will determine the volume of mail and the reputation of the IP. To get a dedicated IP, reach out to `support@onesignal.com` to learn more.
</Accordion>

Built with [Mintlify](https://mintlify.com).
