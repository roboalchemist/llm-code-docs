# Source: https://posthog.com/docs/data-warehouse/sources/attio.md

# Source: https://posthog.com/docs/cdp/sources/attio.md

# Source: https://posthog.com/docs/cdp/destinations/attio.md

# Create and update Attio CRM contacts from analytics events - Docs

You can use your PostHog event data to create and update contacts in Attio. Here's everything you need to get started.

## Configuring Attio

First, [create](https://attio.com/help/reference/integrations-automations/generating-an-api-key) a new **access token** in your Attio workspace. You’ll need to set read-write on the `Records` and `Object Configuration` scopes so that PostHog can communicate with Attio.

Close the scopes section and copy your new access token for the next step.

## Configuring PostHog’s Attio destination

1.  In PostHog, click the **[Data pipeline](https://app.posthog.com/data-management/destinations)** tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=attio) tab.
3.  Click **New destination** and choose Attio's **Create** button.

Paste in your access token and then add any other values you want to pipe from PostHog person properties into Attio, using **additional person attributes**.

### Filtering

At a minimum, you should filter to only send events that have an email property set, as Attio will use this to identify contacts.

### Testing

Once you’ve configured your Attio destination, click **Start testing** to verify everything works the way you want. Switch off **Mock out async functions** in order to send a test event to Attio and see a new record.

---

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/attio/template_attio.py) is available on GitHub.

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