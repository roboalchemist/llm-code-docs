# Source: https://documentation.onesignal.com/docs/en/journeys-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journeys overview

> Create personalized, automated omnichannel messaging flows with OneSignal Journeys to drive engagement, conversion, and retention.

OneSignal Journeys let you build personalized, automated messaging flows across **email**, **push notifications**, **SMS**, **in-app messaging**, and **web push**—all without writing a single line of code.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/T-pZBTlYPyQ?si=D2asPQCb5eMCDIfx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## What you can do with Journeys

Journeys allow you to automate lifecycle messaging based on user behavior, time delays, or profile attributes. Common use cases include:

* **Onboarding sequences** to guide new users to their "aha" moment and ensure early success.
* **Re-engagement campaigns** that target users who haven’t returned after a certain period.
* **Abandoned cart flows** that remind users to complete purchases and recover lost revenue.
* **Upsells, cross-sells, and announcements** to increase feature adoption and promote new offerings.
* **Behavioral followups** that trigger messages when users perform specific actions or meet criteria.

<Frame caption="Example Journey.">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8aca954d35a58b2afe46e7b752cdea04f55a4a3f4f4bf19c5a22073ef4cdc9f2-Screenshot_2025-01-30_at_2.02.07_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=ed5d49c3f226cfe4f01442a473a991e9" width="1918" height="1590" data-path="images/docs/8aca954d35a58b2afe46e7b752cdea04f55a4a3f4f4bf19c5a22073ef4cdc9f2-Screenshot_2025-01-30_at_2.02.07_PM.png" />
</Frame>

<Note>
  For questions on how many Journeys you can use in your account, please refer to [the pricing page](https://onesignal.com/pricing).
</Note>

***

## Best practices for multichannel journeys

Journeys work best when you leverage multiple channels thoughtfully to meet users where they are.

### Mix channels for maximum engagement

Use different messaging types strategically:

* Start with a **welcome email**
* Follow up with a **push notification**
* Announce promotions via **in-app message**
* Send time-sensitive reminders through **SMS**

Mixing channels improves visibility, reduces fatigue, and ensures messages are relevant in context.

### Use External IDs to unify your users

To avoid sending confusing or duplicate messages across channels, assign an **External ID** to every user.

If an External ID is **not set**:

* Each subscription (email, device, SMS number) is treated as a **separate user**
* You may **over-message or confuse** your users

With an External ID:

* OneSignal links all subscriptions to a **single user profile**
* You get accurate targeting and smoother Journeys

<Columns cols={2}>
  <Card title="Users" href="./users" arrow={true}>
    Learn how to define and manage users, assign External IDs, and track user-level engagement across channels.
  </Card>

  <Card title="Subscriptions" href="./subscriptions" arrow={true}>
    Understand how OneSignal tracks user activity across devices and channels, and how it ties back to unified user profiles.
  </Card>
</Columns>

***

## Journey components

Journeys are made up of modular components that give you complete control over who enters, what they receive, and when.

<Columns cols={2}>
  <Card title="Journey settings" href="./journeys-settings" arrow={true}>
    Set how users enter or exit a Journey, define re-entry logic, and control when Journeys are active. These foundational settings ensure your flow behaves exactly as expected.
  </Card>

  <Card title="Journey messages" href="./journeys-messages" arrow={true}>
    Learn about message steps—like push, email, SMS, and in-app—and how to configure each to deliver personalized, timely content.
  </Card>

  <Card title="Journey actions" href="./journeys-actions" arrow={true}>
    Add branching logic, wait steps, split paths, and delays to build dynamic, conditional flows that react to user behavior and timing.
  </Card>

  <Card title="Journey webhooks" href="./journeys-webhook" arrow={true}>
    Send real-time updates from your Journey to other tools (like CRMs or analytics platforms) to keep your stack in sync and trigger external automations.
  </Card>
</Columns>

***

## Journey analytics and management

Understand how your Journeys are performing and keep them optimized over time.

<Columns cols={2}>
  <Card title="Journey analytics" href="./journeys-analytics" arrow={true}>
    Monitor key metrics like completion rate, conversions, drop-offs, and per-message performance. Identify bottlenecks and optimize with confidence.
  </Card>

  <Card title="Managing Journeys" href="./managing-journeys" arrow={true}>
    Learn how to pause, edit, duplicate, archive, and version control your Journeys to keep them up-to-date and effective.
  </Card>
</Columns>

***

## Journeys Examples

Need inspiration or a quick-start template? These examples walk through common Journey flows you can adapt for your use case.

<Card title="Journeys Examples" href="./journeys-examples" arrow={true}>
  Step-by-step walkthroughs for onboarding, re-engagement, abandoned carts, and more.
</Card>

***

If you’ve previously used Automated Messages, Journeys offer a more powerful, flexible way to orchestrate cross-channel campaigns. We recommend migrating to Journeys for more advanced use cases and streamlined management.

***

Built with [Mintlify](https://mintlify.com).
