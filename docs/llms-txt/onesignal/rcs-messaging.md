# Source: https://documentation.onesignal.com/docs/en/rcs-messaging.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rich Communication Services (RCS)

> Learn how to use OneSignal’s RCS feature to send branded, interactive messages and track engagement.

## Introduction to RCS

Rich Communication Services (RCS) is the next generation of text messaging. Unlike traditional SMS, RCS enables **branded sender identification**, **rich media content** (images, videos, GIFs), and **interactive messaging features** that help you create more engaging customer experiences.

👉 [Sign up for a demo of RCS](https://onesignal.com/rcs#contact)

<Frame caption="RCS allows you to send media rich content with interactive features, directly from a branded sender identifier.">
    <img src="https://mintcdn.com/onesignal/hKGnttzPRIm_99fl/images/docs/rcs-first-image.png?fit=max&auto=format&n=hKGnttzPRIm_99fl&q=85&s=5f835ddbd525c8a0d6105d65334174e8" alt="" width="600" height="500" data-path="images/docs/rcs-first-image.png" />
</Frame>

### Key Benefits

* **Branding and verified sending**\
  Messages display your brand’s logo, colors, and identity directly in the conversation, increasing recognition and trust. Verified sender status ensures your messages come from your legitimate business.

* **Advanced engagement analytics**\
  Track who has read a message and use this data for segmentation and journey orchestration.

* **Rich content (coming soon)**\
  Enhance your messages with interactive content like quick replies, carousels, and suggested actions.

### Requirements

* **OneSignal SMS**: Requires a **[Pro+ plan](https://onesignal.com/pricing)**.
* **RCS enabled sender**: [Apply for an RCS sender](#applying-for-an-rcs-sender)

<Note>
  More details can be found on our blog:

* [RCS Approval: Which carriers support it & how to get access](https://onesignal.com/blog/rcs-approval-which-carriers-support-it-how-to-get-access/?utm_source=docs\&utm_medium=docs\&utm_campaign=rcs-messaging)
* [What is the difference between RCS and SMS?](https://onesignal.com/blog/what-is-the-difference-between-sms-and-rcs/?utm_source=docs\&utm_medium=docs\&utm_campaign=rcs-messaging)
* [RCS Marketing Examples: Use Cases & Best Practices](https://onesignal.com/blog/rcs-marketing-examples-use-cases-best-practices/?utm_source=docs\&utm_medium=docs\&utm_campaign=rcs-messaging)
</Note>

***

## Setup RCS

<Steps>
  <Step title="Apply for an RCS sender">
    [See instructions below Applying for an RCS Sender.](#applying-for-an-rcs-sender)
  </Step>

  <Step title="Select an RCS Enabled Sender when sending a message.">
    <Frame caption="An RCS enabled sender">
            <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/rcs-enabled-sender.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=fa326e7e2d593e011c409cf15a3a415d" alt="" width="611" height="91" data-path="images/docs/rcs-enabled-sender.png" />
    </Frame>

    * If a recipient’s device or carrier does not support RCS, messages automatically
      **fall back to SMS**.
  </Step>

  <Step title="Access read analytics">
    These include read rate, RCS read rate, campaign stats, and audience
    activity. [See below for more information.](#rcs-analytics)

    <Frame caption="RCS Analytics">
            <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/rcs-top-analytics.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=25a17c87600ea50863a38bc75a65bd34" alt="" width="1000" height="550" data-path="images/docs/rcs-top-analytics.png" />
    </Frame>
  </Step>

  <Step title="Use read events to branch Journeys or create segments.">
    Use a [message event filter](./segmentation#message-event-filters) to
    use your RCS read receipts to create a segment, or use a [wait until
    node](./journeys-actions#wait-until) or a [yes/no branch
    node](./journeys-actions#yes%2Fno-branch) in a journey to control the
    journey's flow based on your RCS read receipts.

    <Frame caption="A wait until journey node using RCS read">
            <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/rcs-journey-example.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=817d450899dcac4d65a118989ffb524a" alt="" width="644" height="313" data-path="images/docs/rcs-journey-example.png" />
    </Frame>
  </Step>

  <Step title="View RCS read events directly on the User Profile">
    Click into a [user's profile](./users) to see the RCS read receipts for
    that particular user.
  </Step>
</Steps>

***

## Applying for an RCS Sender

<Note>Applying for an RCS sender typically takes **8–12 weeks**.</Note>

<Steps>
  <Step title="Work with your OneSignal account manager to prepare your application">
    This includes brand assets, contact information, expected sending countries,
    opt-in/out flows, and sample campaigns. Make sure that your SMS operations adheres to the following standards: [Registration Requirements](./sms-registration-requirements)
  </Step>

  <Step title="OneSignal will submit your application to **Google and relevant carriers** for approval">
    * ⚠️ Once submitted, applications are final and require re-application to
      make changes.
  </Step>
</Steps>

***

## Types of RCS Messages

* **Basic**: Messages under 160 characters, sent via your branded sender, with read receipts.
* **Single**: Messages over 160 characters or containing media (e.g., images, GIFs).

***

## RCS Analytics

RCS introduces new reporting data within SMS Message Reports:

* **Breakdown of RCS Delivered vs. SMS Delivered**
* **Read Rate**: Reads ÷ Delivered
* **RCS Reads**: The number of recipients that read an RCS message.

👉 See [SMS Message Reports](./sms-message-reports) for the full analytics overview.

<Frame caption="RCS Analytics">
    <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/rcs-full-analytics.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=3008c30c517ed09196215c999d786c80" alt="" width="1000" height="1460" data-path="images/docs/rcs-full-analytics.png" />
</Frame>

***

## FAQ

**Q: How should I think about compliance for RCS?**\
A: RCS compliance follows the same rules as SMS.

**Q: How many senders should I apply for, and can I send both promotional and transactional messages?**\
A: Apply for one sender per brand. This single sender can be used for both **promotional** and **transactional** messages, ensuring customers receive all communications from a unified branded identity.

***

## Next Steps

* [Contact OneSignal to apply for RCS](https://onesignal.com/rcs#contact)
* Explore [SMS Message Reports](./sms-message-reports)
* Reach out to your account manager for eligibility and setup assistance

Built with [Mintlify](https://mintlify.com).
