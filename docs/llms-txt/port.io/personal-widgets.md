# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/dashboards/personal-widgets.md

# Personal widgets

Personal widgets are user-specific widgets that display information tailored to the logged-in user, such as their entities, recently viewed items, and recently used actions.

Home page only

Personal widgets are only available on the [Home page](https://app.getport.io/organization/home) dashboard. They cannot be added to entity page dashboards or custom dashboard pages.

## My entities[â](#my-entities "Direct link to My entities")

This widget displays entities that are assigned to or owned by the logged-in user.

![](/img/software-catalog/widgets/myEntitiesWidget.png)

## Recently viewed[â](#recently-viewed "Direct link to Recently viewed")

This widget displays entities that the logged-in user has recently viewed in Port.

![](/img/software-catalog/widgets/recentlyUsedEntitiesWidget.png)

## Recently used actions[â](#recently-used-actions "Direct link to Recently used actions")

This widget displays self-service actions that the logged-in user has recently executed.

![](/img/software-catalog/widgets/recentlyUsedActionsWidget.png)

## Widget type identifiers (Terraform)[â](#widget-type-identifiers-terraform "Direct link to Widget type identifiers (Terraform)")

When creating widgets using [Port's Terraform provider](https://registry.terraform.io/providers/port-labs/port-labs/latest/docs/resources/port_page), you need to provide the widget type's identifier in the `type` key.<br /><!-- -->The following table lists the identifiers for each personal widget type:

| Widget type           | Identifier                 |
| --------------------- | -------------------------- |
| My entities           | `my-entities`              |
| Recently viewed       | `recently-viewed-entities` |
| Recently used actions | `recently-used-actions`    |
