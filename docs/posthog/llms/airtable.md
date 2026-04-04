# Source: https://posthog.com/docs/cdp/destinations/airtable.md

# Send PostHog analytics to Airtable - Docs

It’s easier than ever to export realtime PostHog data to satisfy the Airtable fanatics in your life.

## Configuring Airtable

With data pipelines enabled, let’s get Airtable connected.

First, [create](https://airtable.com/create/tokens/new) a **personal access token** in your Airtable account. You’ll need to add the `data.records:write` scope so that PostHog can create new records.

Then add the **base** you want to create new records in.

Next, you’ll want to visit Airtable’s [API reference](https://airtable.com/developers/web/api/introduction) to get your base ID, table name, and field names.

## Configuring PostHog’s Airtable destination

You should have these details now:

-   Access token
-   Base ID
-   Table name
-   Field names

With them, we’re ready to set up the Airtable destination.

1.  In PostHog, click the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in the left sidebar.
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=airtable) tab.
3.  Click **New destination** and choose Airtable's **Create** button.

Now we can plug in the above values.

The **Fields** editor enables you to map whatever PostHog [values](/docs/cdp/destinations.md#input-formatting) you like to columns in your Airtable base. The keys on the left should match the names you’ve already set for columns in Airtable. Values on the right can be any property on a `person` or `event` instance.

### Filtering

In its experimental state, the Airtable destination will not batch its output to your base. If you trigger on events that happen more than five times per second, you’ll hit the Airtable API [rate limit](https://airtable.com/developers/web/api/rate-limits).

So be selective about the events you forward to Airtable. Instead of every pageview, for example, just send the high-impact events like conversions. Use the **Filters** panel to set this up.

### Testing

Once you’ve configured your Airtable destination, click **Start testing** to verify everything works the way you want. Switch off **Mock out async functions** in order to send a test event to Airtable and see a new record.

### A note on data types

Where possible, Airtable will convert values into native datatypes set in your columns. So, if you pass `event.timestamp` to an Airtable `Date` column, that will work just fine.

---

## FAQ

### Is the source code for this destination available?

PostHog is open-source and so are all the destination on the platform. The [source code](https://github.com/PostHog/posthog/blob/master/posthog/cdp/templates/airtable/template_airtable.py) is available on GitHub.

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