# Source: https://documentation.mailgun.com/docs/mailgun/faq/tracking.md

# FAQ: Tracking

### Can I use Mailgun to track what happens with my emails?

Yep, Mailgun tracks all of the typical events that occur with emails:
Opens, Link Clicks, Bounces, Unsubscribes and Spam Complaints. We make
that data available to you via the Control Panel or through the API. In
addition, you can set up webhooks and we will post events to your URL.
Take a look at our [tracking
documentation](https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages)
for more information.

### What about Email List Management?

Mailgun does have features to help you with list management. First of
all, we will not deliver again to recipients that have hard bounced,
unsubscribed, or complained of spam. This is to maintain your email
reputation. You can remove emails from these do not send lists if it was
a temporary issue. You can always access this information via the API or
Control Panel to update your lists.

### What is the difference between hard and soft bounces and how do you handle them?

You can think of hard bounces like permanent errors and soft bounces as
temporary errors. We will stop attempting delivery after one hard
bounce. With soft bounces, we keep trying to deliver but eventually we
will stop trying to delivery in accordance with the receiving ESP's
feedback.

### Do I control the unsubscribe handling or do you?

It's up to you. You can use Mailgun's unsubscribe handling. You can
include our unsubscribe variables: `%unsubscribe_url%` (for the entire
domain) and `%tag_unsubscribe_url%` (for just emails with this tag) and
we will take care of the unsubscribe handling for you. Take a look at
our [unsubscribe
documentation](https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/#unsubscribing)
for more information.

### How do I create Campaigns in Mailgun?

It's very simple, just tag your emails with the appropriate `o:tag`
parameter and Mailgun will group all of the events that occur to emails
with that tag. Our analytics reports include those tags as one of the
dimensions by which you can view and filter data. You can have multiple
tags per email and up to 4,000 total tags. Take a look at our [tagging
documentation](https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/#tagging)
for more information.

### Do you support A/B testing?

Since creating a campaign is as easy as including an arbitrary tag, yes.
You can easily view which campaign is performing best by viewing the
data grouped by tag in the `Analytics` tab of the Mailgun control panel.

### How do I track which email a recipient has replied to?

This has been a popular question, so we wrote a [blog
post](https://www.mailgun.com/blog/tracking-replies-in-mailgun-or-any-other-email/)
about it. Basically, the Message-ID in the original email is included in
the In-Reply-To header in the reply email. So you can use that to track
which specific email was replied to. Mailgun will automatically include
a unique Message-ID or you can set your own.