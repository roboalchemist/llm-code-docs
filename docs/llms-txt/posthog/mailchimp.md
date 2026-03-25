# Source: https://posthog.com/docs/data-warehouse/sources/mailchimp.md

# Source: https://posthog.com/docs/cdp/sources/mailchimp.md

# Source: https://posthog.com/docs/cdp/destinations/mailchimp.md

# Create and update Mailchimp contacts from analytics events - Docs

You can use your PostHog event data to create and update contacts in Mailchimp. Here's everything you need to get started.

## Configuring Mailchimp

First, [create](https://mailchimp.com/help/about-api-keys/) a new **API key** in your Mailchimp account.

You'll also need your **[Mailchimp audience ID](https://mailchimp.com/help/find-audience-id/)**.

Finally, while logged into Mailchimp, check the subdomain of your account. You'll need this to configure the destination, as your `Mailchimp datacenter id`.

## Configuring PostHog’s Mailchimp destination

1.  In PostHog, click the **[Data pipeline](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=mailchimp) tab.
3.  Click **New destination** and choose Mailchimp's **Create** button.

Insert your API key, audience ID, and datacenter ID. You can also choose a different property to use as the contact's email; PostHog will default to `person.properties.email`.

You can additionally forward all event properties to Mailchimp, or select specific ones using the **merge field** section.

### Filtering

As you'll be collecting or updating contact emails, you should configure the destination filter to only accept events that have an email property set.

### Testing

Once you’ve configured your Mailchimp destination, click **Start testing** to verify everything works the way you want.

---

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/mailchimp/template_mailchimp.py) is available on GitHub.

### Who maintains this?

This is maintained by PostHog. If you have issues with it not functioning as intended, please [let us know](https://us.posthog.com/#panel=support%3Asupport%3Aapps%3A%3Atrue)!

### What if I have feedback on this destination?

We love feature requests and feedback. Please [tell us what you think](https://us.posthog.com/#panel=support%3Afeedback%3Aapps%3Alow%3Atrue).

### What if my question isn't answered above?

We love answering questions. Ask us anything via [our community forum](/questions.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better