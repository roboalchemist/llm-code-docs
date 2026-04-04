Source: https://docs.slack.dev/changelog/2016/08/11/user-id-format-changes

# User ID format changes

August 11, 2016

As Slack works to serve the needs of larger businesses by building an enterprise product offering, some aspects of our infrastructure and platform are evolving.

## What's changing? {#whats-changing}

The following changes apply only to platform features and API requests used in conjunction with teams using Slack's upcoming Enterprise product.

### Some user IDs may now begin with the letter "W" {#some-user-ids-may-now-begin-with-the-letter-w}

Typically, user IDs encountered throughout the Slack platform begin with `U`. From now on, you may also encounter team members with a user ID beginning with `W`. Treat these user IDs just as you would those beginning with `U`.

### Some user objects may contain a new field {#some-user-objects-may-contain-a-new-field}

If your application or integration is installed by an Enterprise-enabled team, you may notice user objects containing a new field called `enterprise_user`. This field includes a hash of attributes describing that user's status as part of an enterprise organization.

At this time, there's not much for developers to do with this field. We'll provide more detail on the meaning of each attribute in the coming weeks.

## What do I need to do to prepare? {#what-do-i-need-to-do-to-prepare}

Most developers need do nothing at all. If you don't inspect the first character of the user ID string, everything should be all right. You also probably won't see user IDs beginning with `W` very often.

But please do make sure that your code, database, and other plumbing all support user IDs beginning with the letter `W`, or any UTF-8 character.

Ideally, your code and business logic shouldn't contain any assumptions about the specific characters composing an ID.

## Are there any known issues? {#are-there-any-known-issues}

We [recently updated](https://github.com/slackhq/node-slack-sdk/releases/tag/3.5.4) our [node-slack-sdk](https://github.com/slackhq/node-slack-sdk) library to better handle some unfortunate assumptions we previously made.

If you're the developer of a library, we recommend reviewing your code and ensuring these minor changes are compatible.

## What's next? {#whats-next}

We'll be sharing more detail on our Enterprise product and how to ready your apps and integrations to work with the larger businesses in the months to come.

**Tags:**

* [Announcement](/changelog/tags/announcement)
