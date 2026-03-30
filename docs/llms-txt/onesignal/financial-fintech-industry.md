# Source: https://documentation.onesignal.com/docs/en/financial-fintech-industry.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Financial / fintech industry

> Messaging and strategic best practices tailored for the financial / fintech industry.

## New User Verification

Security and compliance are paramount for the finance industry, particularly because personal and financial information are involved. Messaging is an effective way to ensure users complete necessary compliance steps required by your organization and/or the industry.

A key first compliance step is new user verification. New users need to create, activate, and/or verify their account within the app to enforce compliance.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/lp0eY99IjCE?si=ODnjmTiGPSSfIc5q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### The Multi-channel Approach to Verification

We’ve seen OneSignal customers successfully encourage users to activate or verify their accounts by taking a multi-channel approach – sending them messaging through more than one channel – such as a user receiving an email, push message, and SMS over the course of a few days.

<Check>
  Don’t rely on email alone for new user verification
</Check>

### Promote Account Verification Promptly

We recommend promoting account completion and/or verification within the first 48 hours. Not only are these first 48 hours critical for ensuring that your user is set up correctly, but they are just as important to engage them in using your platform.

### Simplify New User Verification with Journeys

The OneSignal [Journeys feature](./journeys-overview) allows you to easily create a new user verification campaign that will automatically send account verification reminders across multiple channels AND within the first few days, as well as messages around trading, buying, and making transactions right away. Try sending new users a promotion where \$10 will go towards their first trade or transaction!

## Security

Effectively keeping sensitive user information secure is always top of mind for companies in the finance industry. Messaging can actually help customers enforce necessary compliance.

Today, most users are familiar with Two Factor Authentication, or 2FA, which is an extra layer of protection used to ensure the security of online accounts beyond just a username and password. Messaging can be used to help customers set up 2FA and reduce security risks.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/WTlQ5fOCySw?si=suAQ6p5Dz9O727hg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### 2FA Set up Messaging in 2 steps

<Steps>
  <Step title="Identify users that have not enabled 2FA">
    To encourage 2FA set up, you will need to identify which users have not yet enabled 2FA. Within OneSignal, we recommend using [data tags](./add-user-data-tags) to specify these users, which then allows you to segment or target them directly with specific messaging.
  </Step>

  <Step title="Utilize Journeys to Automate 2FA messaging">
    With [Journeys](./journeys-overview), you can automate both push and in-app messaging to send periodic reminders to customers to complete the set-up and better secure their accounts.
  </Step>
</Steps>

## New User Promotions

Getting new users active right away is important for their continued usage and engagement within your mobile app. Promotions are a great way to encourage activity quickly.

### New User Promotions in 2 Steps

<Steps>
  <Step title="Establish your new user messaging cadence">
    We recommend first establishing a new user or onboarding cadence that works for your business. A cadence that we have seen work well within the financial industry is the following: Day 1, Day 2, Day 4, Day 6 - essentially messaging your users on Day 1, Day 2, Day 4 and Day 6 of becoming a new user within your app.
  </Step>

  <Step title="Incorporate a specific “first action” promotion">
    In addition to highlighting the benefits of your app/business, we recommend messaging for the specific cadence days that includes a promotion or coupon to complete a first transaction – such as:

    <Columns cols={3}>
      <Card title="Deposit" icon="money-bill" />

      <Card title="Trade" icon="money-bill-transfer" />

      <Card title="Payment" icon="cart-shopping" />
    </Columns>

    Additionally, leveraging the [Journeys feature](./journeys-overview) allows you to easily execute an automated onboarding flow that adheres to your desired new user cadence with the specific promotion. We recommend creating an onboarding flow to get new users to complete a “first action” promotion within their first 2-3 days of using or downloading your app.

    Creating a tailored new users promotion strategy and cadence that prompts action will improve engagement and start your users on the right path to continuously use your app.
  </Step>
</Steps>

## Transactional Messages

Transactions are a staple within the financial industry - money sent or received, trades made, deposits made, etc. And as such, message updates around the specific transactions being made are integral.

Utilize our robust and powerful [API](/reference/create-user) to send [transactional messages](./transactional-messages) so your users are kept up to date. Effective financial / fintech transactional messaging includes:

* Transaction status
* Money received
* Bank balance
* Payments made
* Identify verification confirmation

Providing transparency to users on the status of their transactions and payments ensures they are informed of any changes to their account.

***

Built with [Mintlify](https://mintlify.com).
