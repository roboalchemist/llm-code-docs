# Source: https://docs.unifygtm.com/reference/deliverability/mailbox-configuration.md

# Mailbox Configuration

> Provision Unify-managed mailboxes for your team to send from.

## Mailbox registration and ownership

Once your domain is verified and activated you can start setting up mailboxes in Unify. When setting up a mailbox you will provider the names of your senders to your CSM. Unify will choose then create email mailboxes for you (e.g. `jane@mybusiness.io`).&#x20;

#### Sending emails

Through the Unify Sequencing product you will be able to send emails using your Unify managed mailboxes. The email signature and display name will be pulled from the owning user. Unify will automatically schedule your emails and manage the sending volume across your mailboxes.

#### Receiving emails

Replies to [`jane@mybusiness.io`](mailto:jane@mybusiness.io) will be forwarded to the user that owns the mailbox. For example, email replies sent to the Unify managed mailbox [`jane@mybusiness.io`](mailto:jane@mybusiness.io) will be forwarded to `Jane Doe's` primary email [`jane@mybusiness.com`](mailto:jane@mybusiness.com).

## Mailbox warmup

When a mailbox is created we will automatically start warming the mailbox to ensure high deliverability. Warming works by automatically sending emails to emails in a “warming network”. These emails will be automatically opened and replied to. If the warming emails land in the spam folder they will be taken out of the spam folder (a so called "spam rescue"). This tells the email service providers that your emails are high-quality and thus your deliverability improves. We continuously monitor the warmup process and after 3 weeks it will complete and your mailboxes will be ready to send. Once your mailboxes are warmed, we will send up to 65 emails per mailbox per day. By default, our send times are set to 9 AM - 4 PM PT on business days.

## Secondary forward

There are situations (such as vacation cover) where you need a second user to monitor an inbox of another user. You can set up a "Secondary forward" user. This user will receive a copy of all the replies sent to the mailbox. For example, if `John Doe` is helping `Jane Doe` out during her vacation, all emails sent to [`jane@mybusiness.io`](mailto:jane@mybusiness.io) will be forwarded to [`john@mybusiness.com`](mailto:john@mybusiness.com) (John's primary email). If you would like a secondary forwarding user set up on your Unify managed Gmail mailboxes, please contact [support@unifygtm.com](mailto:support@unifygtm.com) or your CSM.&#x20;
