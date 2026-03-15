# Source: https://docs.firehydrant.com/docs/auto-watch-incidents.md

# Watched Incident Notifications

Get notified on changes to a specific incident or any incident that match parameters that concern you.

Subscribe to specific saved incident searches to utilize the "Auto-Watch" capability. When an active incident matches your saved filter you will be added as a "Watcher" to the incident. Watching an incident enables email notifications that allow you to stay informed without having to join the incident channel or monitor its status page.

## What Notifications Do Watchers Receive?

Watchers receive email notifications when:

* **Severity changes**: You'll be notified whenever the incident's severity is escalated or de-escalated
* **Milestone changes**: You'll be notified whenever the incident moves to a different milestone (e.g., Acknowledged → Investigating → Mitigated → Resolved)

These notifications help you stay updated on critical incident status changes without needing to actively monitor incident channels.

# Create and Subscribe to Saved Incident View

In the Incidents search view, you can save sets of filters as "Saved Views", quickly allowing you to find incidents that you are interested in.

## Create a Saved View

To save your first incident filter:

1. Navigate to the **Incidents** list in the FireHydrant UI
2. Select any number of filters to specify your search
3. Click the **Save as new View** drop down menu on the left side of the quick filter options
4. In this drop down, choose the Save as new view
5. In the pop-up modal, provide a descriptive name and set the configuration:
   1. **Private saved view**: Restrict access to the saved view to only you
   2. **Set as default view**: Personal configuration to show this saved view when you navigate to the Incidents page by default
6. You will also be asked if you’d like to subscribe to the new saved view.

> If you enable this toggle, you will be added as a watcher for every incident that matches the saved view’s configured filters, whether the incident is declared with those attributes or is updated to have them later

7. Saved views that you are subscribed to will show in the saved views dropdown with a **bell icon indicator** (🔔), making it easy to identify which views you're actively watching.

<Image align="center" border={false} caption="Saved Views configuration flow" src="https://files.readme.io/0e55de1c9cf328c7763903e2e0128b2759dfc4a9d837bd7ea310590a9417d084-image.png" />

# Watch Incidents

Watching incidents will add them to a specific watch section of your home page in the FireHydrant UI, as well as sending notifications for any milestone or severity update.

<Image align="center" border={false} caption="Watched incident widget on homepage and notification email" src="https://files.readme.io/013b5435da740515afd90831dc206079d2996120ea67e118e9d971efee8184c9-image.png" />

## Auto-watch an Incident

Follow the steps above to define and subscribe to a saved view in order to automatically watch active incidents. You can also subscribe to existing views available to you within the **Incidents** page.

### Subscribe to an Existing Saved View

To subscribe to a saved view that already exists:

1. Navigate to the **Incidents** page
2. Click the saved views dropdown
3. Find the saved view you want to subscribe to
4. Click the subscribe option for that view
5. The view will now show with a bell icon indicator, and you'll be added as a watcher to matching incidents

### Unsubscribe from a Saved View

To unsubscribe from a saved view:

1. Navigate to the **Incidents** page
2. Click the saved views dropdown
3. Find the saved view with the bell icon that you want to unsubscribe from
4. Click the unsubscribe option for that view
5. You will no longer be automatically added as a watcher to incidents matching that view's filters

<Image align="center" border={false} caption="Subscribe to existing saved view in the drop down menu" src="https://files.readme.io/bb84c0b2b38ff0c405e26b25eb05fcee19e5ab447974b9ae3a65ca5984e35c43-image.png" />

## Manually watch an Incident

From within an incident page, you can select the **Watch** button, to the right of the severity and priority tags.

<Image align="center" border={false} caption="Watch button on far right of Incident icons" src="https://files.readme.io/ed14d3e6866981b16a81a62d04e1a8ed32ecb7ec46bce6d13b568801b4b5f0d4-image.png" />

## Unwatch an Incident

If you are watching an incident, but no longer want to receive notifications on each milestone or severity update, you can select the **Unwatch** button on the incident page, from the home page incident tile, or from within the search view on the **Incidents** page. Incidents that are unwatched will not be automatically watched from any saved views you are subscribed to. If you’d like to rewatch the incident, you may do so manually.

<Image align="center" border={false} caption="Unwatch button locations" src="https://files.readme.io/28a5fa4dbdc5141417eecd1c55784728134f6d5deea1473e7145d139cebd42ca-image.png" />

<br />