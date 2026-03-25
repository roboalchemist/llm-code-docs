# Source: https://docs.sinch.com/whatsapp/instructions-and-good-practices/learn-more-about-tiers.md

# Learn More About Tiers

The indicators shown on [Channel Rules](https://docs-latam.messaging.sinch.com/whatsapp/instructions-and-good-practices/channel-rules) influence your message sending limitation.

The message deliverability limitations determine to how many unique users your company can send messages daily. This includes new chats and existing chats with users.

Your message limit does **NOT** restrict the number of messages your company can send, only the amount of users who can receive them.

It does also NOT apply to messages sent in reply to a message initiated by the user within a 24-hour period.

## **Understanding the Tiers**

Upon registering its phone number, a company begins at **Level 1**, which has a limit of **1,000** messages sent **every 24 hours**.

* **Tier 1** - Allows you to send messages to 1,000 unique users every 24h.
* **Tier 2** - Allows you to send messages to 10,000 unique users every 24h.
* **Tier 3** - Allows you to send messages to 100,000 unique users every 24h.

A number that is in Tier 3 **can drop to a lower tier due to poor quality.**

## **How to Upgrade Your Tier?**

A company’s phone number will be upgraded to the following level if:

1. Its quality rating is not too low.
2. The cumulative number of users to whom it sends notifications adds up to twice the current message limit within a 7-day period. A company will be upgraded from Level 1 to Level 2 when it sends messages to a total of 2,000 users within a 7-day period, for instance.

The minimum amount of time in which this change can occur is **48 hours after the 1st trigger**.

A few possible scenarios below:

**Scenario 1:** Every number begins at tier 1. The company will move up to the following level once it sends messages to a total of 2,000 users within a 7-day period, for example, and has a good quality rating.

![Scenario 1](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGelOpGGK_hRcfivfS%2F0.png?generation=1633457739744324\&alt=media)

**​Scenario 2:** A low quality level (Red) causes the number’s status to change from Connected to Flagged.

During its Flagged period, the number had good quality (Green/Yellow) in its deliveries. After the 7-day period, the customer goes up to the next Tier.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FaFHsvvf7DDHmn99Q32eK%2Fimage.png?alt=media\&token=6c935f48-5d93-4c41-abb3-d5773ae0cee9)

**Scenario 3:** A low quality level (**Red**) causes the number’s status to change from Connected to Flagged.

​

![Scenario 3](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGar7zO0jt7HSPWe7y%2F-MlGelOrU0lmC4wLXStr%2F2.png?generation=1633457739751866\&alt=media)

During its Flagged period, the number continues to have poor quality (red). After the 7-day period, the customer goes back to the previous Tier, which allows their company to send a smaller number of messages.
