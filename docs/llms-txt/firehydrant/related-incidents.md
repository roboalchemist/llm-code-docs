# Source: https://docs.firehydrant.com/docs/related-incidents.md

# Related Incidents

<Image align="center" width="650px" src="https://files.readme.io/eae390d-related-incidents-overview.png" />

Related Incidents connect multiple incidents in a simple parent/child relationship for multiple use cases:

* Coordinating efforts across multiple incidents with similar root causes
* Organizing a large, complex incident into multiple smaller incidents
* Otherwise relating multiple incidents together for your own needs and criteria

You can relate incidents with a Slack command or on the Command Center on the web. To keep things simple, incidents can either be a parent or a child (but not both!), so all hierarchies are limited to one generation of parent and child(ren).

## Adding Related Incidents

### In Slack

In Slack, you can relate an incident to another incident from inside either incident’s Slack channel. Run the command `/fh related incidents` and you’ll find the modal below.

<Image alt="Related incidents modal in Slack" align="center" width="400px" src="https://files.readme.io/bfd6dba-related-incidents-slack-modal.png">
  Related incidents modal in Slack
</Image>

You can add the appropriate related incident from that modal. Once you’ve added a related incident, you will see an announcement of the new relationship in the incident Slack channel. This announcement is posted on the thread of the pinned message in the related incidents’ Slack channels. You can add additional children from the Parent incident channel.

### In Command Center

In the web UI, you can add related incidents from the Command Center. Locate the “Related Incidents” section of the sidebar and click the pencil icon to edit. You’ll see a similar modal as you would in Slack, allowing you to add either a parent or multiple children to the current incident.

<Image alt="Related incidents modal in the UI" align="center" width="650px" src="https://files.readme.io/2d06eb3-related-incidents-web-modal.png">
  Related incidents modal in the web UI
</Image>

You can use the sidebar to quickly navigate between related incidents.

### Relating Private Incidents

To keep private incidents secure, only private incidents can be related to other incidents marked as private. You can always convert existing incidents to private if you need to relate them to other private incidents.

## Slack Notifications for Related Incidents

Anytime that a related incident posts an update, that update will be shared on the thread of the pinned message of the other related incidents’ Slack channels. When the parent incident is pushing these notifications, they will also be posted to the child incidents’ main channel (using the “Also post to channel” option in Slack).

<Image alt="Example notification to child incident channel" align="center" src="https://files.readme.io/eb4e347-related-incidents-parent-notification.png">
  Example notification to child incident channel
</Image>

## Resolving and Archiving Related Incidents

When resolving an incident with children, you will have the option to:

* **Resolve all Children** - This ensures that child incidents will be included in any analytics or exports.
* **Archive all Children** - This ensures that child incidents will be excluded in any analytics or exports.
* **Do Nothing** - In cases where active work is still happening in child incidents, you may want to leave them open so that responders in those incidents can resolve or archive them when the child incident is wrapped up.

<Image align="center" width="650px" src="https://files.readme.io/722ee67-related-incidents-parent-resolve.png" />

You will see these options when resolving an incident from Slack or from the web UI.\
When archiving a parent incident, all child incidents will also be archived.

## Next Steps

* Look at how to [Resolve Incidents](https://docs.firehydrant.com/docs/resolving-incidents)
* Read more about [Archiving Incidents](https://docs.firehydrant.com/docs/archiving-incidents)