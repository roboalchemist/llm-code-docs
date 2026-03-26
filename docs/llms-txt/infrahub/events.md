# Source: https://docs.infrahub.app/topics/events.md

# Infrahub Events framework

Under Construction

This page is still under construction and is not complete yet. Please reach out on Discord if you have some questions about **Infrahub events**

The **Event framework** in Infrahub tracks all significant operations and changes within the system. Every key mutation generates a corresponding event, creating a comprehensive record of what happens in your infrastructure.

For example, some of the events include:

* `infrahub.node.created`
* `infrahub.node.updated`
* `infrahub.node.deleted`
* `infrahub.group.member_added`
* `infrahub.group.member_removed`
* `infrahub.branch.created`
* `infrahub.branch.deleted`

You can find the exhaustive list of events in the [Infrahub events](/reference/infrahub-events.md) page.

These events serve multiple purposes:

* They feed the [activity log](/topics/activity-log.md), providing a detailed, chronological timeline of system changes.
* They enable event-driven automation, such as triggering [webhooks](/topics/webhooks.md) and [event rules and actions](/topics/event-actions.md).
