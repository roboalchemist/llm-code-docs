# Source: https://docs.firehydrant.com/docs/managing-subscribers.md

# Managing Subscribers

Users can subscribe to FireHydrant's status pages to receive updates on incidents. The current subscription methods supported include **email** and **RSS**.

## Update Triggers

<Image alt="Example incident opened notice via email" align="center" width="650px" src="https://files.readme.io/9de2180-image.png">
  Example incident opened notice via email
</Image>

Subscribers to FireHydrant's status pages can expect the following types of updates:

* **24-Hour Maintenance Notice** - If your organization has configured a [Scheduled Maintenance](https://docs.firehydrant.com/docs/scheduled-maintenances) and opt to post this to a status page, then subscribers to the status page will receive a notice of the upcoming maintenance 24 hours before it starts.
* **Incident/Scheduled Maintenance Started** - When an incident is declared or scheduled maintenance is started, and responders decide to post to the status page, subscribers will be sent a new RSS entry and email.
* **Important Detail Changes** - Changes to essential details like the incident's title will trigger subscribers' updates.
* **Incident/Maintenance Notes and Updates** - If a responder posts an incident note to the status page (e.g., with `/fh update`), subscribers will also receive news updates.
* **Incident/Maintenance Resolution** - Subscribers will receive updates once a responder resolves the incident.

## Removing Subscribers

If subscribers to a status page want to stop receiving updates, they can either remove themselves or be removed by a <Glossary>Member</Glossary> or <Glossary>Owner</Glossary> of the FireHydrant organization:

* Users can click "Unsubscribe from this list" in one of the status page update emails
* As a Member or Owner of the organization, you can navigate to **Status Pages** in the top navigation and then click the Subscribers count next to the status page you'd like to remove the subscriber from. Find the subscriber in question on the next page, and then click the context menu/ellipses > Remove subscriber.

<Image alt="Accessing the subscribers list for a particular status page" align="center" width="650px" src="https://files.readme.io/f8e567f-Screenshot_2024-01-25_at_5.48.33_PM.png">
  Accessing the subscribers list for a particular status page
</Image>