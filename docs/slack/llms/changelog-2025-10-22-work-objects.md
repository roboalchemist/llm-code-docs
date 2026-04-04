Source: https://docs.slack.dev/changelog/2025/10/22/work-objects

# Introducing Work Objects

October 22, 2025

As you may have spied in the [Slack CLI v3.9.0 release](/changelog/2025/10/21/slack-cli) yesterday, support for Work Objects is now generally available! 🎉

[Work Objects](/messaging/work-objects-overview) allow you to represent and collaborate on data from third-party services where the work is already happening, right in Slack. They have two primary components: an [unfurl component](/messaging/work-objects-overview#unfurl), and a [flexpane component](/messaging/work-objects-overview#flexpane).

We've also introduced a new [`entity_details_requested`](/reference/events/entity_details_requested) event and the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method, and have added support for Work Objects to the [`chat.unfurl`](/reference/methods/chat.unfurl/) API method. SDK support for these API updates is coming soon.

To learn how it all comes together to create a seamless experience for your users, check out the [full documentation](/messaging/work-objects-overview)!

**Tags:**

* [Announcement](/changelog/tags/announcement)
* [New Feature](/changelog/tags/new-feature)
