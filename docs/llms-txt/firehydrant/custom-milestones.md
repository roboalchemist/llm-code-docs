# Source: https://docs.firehydrant.com/docs/custom-milestones.md

# Custom Milestones and Metrics

Custom Milestones allow organizations to modify our existing [Lifecycle Phases](https://docs.firehydrant.com/docs/lifecycle-phases) feature. You are able to create, edit, and reorder milestones inside of a “Lifecycle” phase to match your own internal policies for how incidents progress

> 📘 Note:
>
> Customizing milestones requires an Enterprise license and Owner permissions within your organization.

## Managing milestones

### Creating milestones

In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. On the top right of each Lifecycle Phase, click "Edit".

In the add milestone modal, you’ll have the following fields:

1. Milestone Name (required): The name as it will appear on forms and in the UI. The milestone name must be unique across  “Lifecycle Phases” and  currently configured custom milestones.
2. Milestone Description: A brief explanation of the milestone. A best practice is to include when the milestone is used. This only appears on the **Incident milestones** page

All incidents declared after creating a custom milestone will have the field available to fill in Slack, MS Teams  and web UI. In addition, if you use a ticketing integration like Jira, custom milestones will be available as ticket states.

<Image alt="Adding a Milestone" align="center" width="650px" src="https://files.readme.io/49b87552f67d5d8cc16bb1c4c26f7f64ac69906f7628b8de14d1c857bf5d7e44-create-custom-milestone1008.jpg">
  Adding a Milestone
</Image>

> 📘 Note
>
> Organizations are currently limited to 20 custom milestones per Life Cycle Phase. This is across all Organizations existing within the Account.

### Editing milestones

In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. On the top right of each Lifecycle Phase, click "Edit".  Find the milestone you would like to edit, click the Edit icon.

You will be able to modify the display name and description settings for all fields.

> 📘 Note:
>
> When an incident is declared, any milestones on it adopt whatever settings were configured at the moment of declaration. For example, if you create an incident, then add a new custom milestone, those changes will not reflect on the incident you created since it was declared before creating the new milestone.

We do not support propagating new custom milestone changes to old incidents.

### Reordering milestones

1. In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. On the top right of each Lifecycle Phase, click "Edit".
2. Click the dots next to each milestone on the left to drag and move them up or down. These changes are reflected in every area where you can view and select them.

> 📘 Note:
>
> You cannot move milestones between Lifecycle Phases You will need to create a new milestone for that Lifecycle Phase.

### Removing milestones

<Image alt="Removing milestones" align="center" width="650px" src="https://files.readme.io/ca628811eb9f1f6c2ac4b58110c7ae52b0aa6c7b4c3d05259115a51f06a0b46d-remove-custom-milestone-1920x1008.jpg">
  Removing milestones
</Image>

In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. On the top right of each Lifecycle Phase, click "Edit".  Find the milestone you would like to edit, select the Delete icon.

Removing a custom milestone from your configuration will only impact future incidents. Any existing incidents with the custom milestone will continue to have that milestone.

> 🚧 Note
>
> Modifying milestones (creating, deleting, or reordering) will impact your analytics data. Choose milestones carefully and adjust only when necessary. Regularly export analytics data to preserve historical reports.

## Using Custom Milestones

Once you've created custom milestones, they will be made available on any Incidents declared after the milestones settings were saved.

After an incident has been declared, you can select the custom milestone in the web UI, Slack and MS Teams.

**To select a custom milestone from the web:**

1. After a new incident has been declared, go to that incident
2. Locate the Milestone dropdown
3. Select milestone from list

**To select a custom milestone in Slack you can use /fh update:**

You will see a modal with a Milestone dropdown with Lifecycle phases and milestones grouped in their respective categories.

<Image alt="Custom Milestones and Lifecycle Phase in Slack" align="center" width="400px" src="https://files.readme.io/1e2e98f659ac1ae946049e290dbfbff3d1d0e90c740c494b0bdc019effd181c2-slack.jpg">
  Custom Milestones and Lifecycle Phase in Slack
</Image>

**To select a custom milestone in MS Teams you can use`@firehydrant` update or use the Milestone drop down from the FireHydrant Tab:**

You will see a modal with a Milestone dropdown with Lifecycle phases and milestones grouped in their respective categories.

<Image alt="MS Teams tab" align="center" width="400px" src="https://files.readme.io/2284e95da5d80e75597192fefbe831455398f8fdff8535b7a53a8e06bc6d88a6-ms-teams.jpg">
  MS Teams tab
</Image>

## Searching custom milestones

You can filter your search for incidents in the FireHydrant UI by milestones, including custom milestones. Because custom milestones can change over time, you’ll see both the active and inactive milestones (previous milestones that were deleted). This allows you to remove custom milestones from your current settings but still find historical incidents using previous data.

1. Navigate to **Incidents** in the navigation:
2. Select Add filter button
3. Select Milestones
4. Select the milestone you want to filter on

<Image alt="Filter by Milestone" align="center" width="400px" src="https://files.readme.io/c1b2247576d3530c21d84ffc8a0bb82e7071e93c40d132ef17ad736a02aee079-fillter.jpg">
  Filter by Milestone
</Image>

## Using custom milestones in Liquid templates

Custom milestones can be referenced anywhere Template Variables are supported. They are referenced the same way our out of the box milestones are referenced.

```liquid
{{ incident.current_milestone }}
```

You can also use Liquid’s powerful control flow and iteration tags to output exactly what you need. For example, to iterate through all milestones set in an incident, when they occurred and their duration, you can use:

```liquid
{% for milestone in incident.milestones %}
Milestone: {{ milestone.type }}
Occurred At: {{ milestone.occurred_at }}
Duration: {{ milestone.duration }}
{% endfor %}
```

For more information, visit the [Template Variables](https://docs.firehydrant.com/docs/template-variables) documentation.

## Custom MTTx Metrics

Users, alongside customizing their milestones, can customize their MTTx metrics to match them.

In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. Scroll down to **Measurement Definitions** and click "Add measurement".

In the Create measurement  modal, you’ll have the following fields:

1. Name (required): The name as it will appear on forms and in the UI. The measurement name must be unique.
2. Slug (required): The slug for the measurement. This will be automatically generated from the name if left blank
3. Description: A brief explanation of the measurement.
4. Starting Milestone (required): The milestone where the measurement should start.
5. Ending Milestone (required): The milestone where the measurement should end.

<Image alt="Create custom MTTX measurement" align="center" width="400px" src="https://files.readme.io/ba44e18b93d1251ae0884e7db0bc5da5d9c4cfde5d82abf6e796ee3999c63ecd-measurement.jpg">
  Create custom MTTX measurement
</Image>

> 📘 Note:
>
> Accounts are currently limited to ten different measurements.

### Healthiness Measurement

You can choose which milestones your Healthiness measurement is based on. By default, it is calculated based on the Started and Mitigated milestones. Healthiness is calculated as the sum of the measurement duration for all selected incidents divided by the total time window, approximating an uptime calculation.

In the FireHydrant UI navigation, select **Settings** or **⚙️** and then **Incident milestones**. Scroll down to **Measurement Definitions**

1. Select the measurement you want to use for your Healthiness measurement
2. Click the kebab menu for that measurement
3. In the modal select the “Use measurement for healthiness” option

<Image alt="Select healthiness measurement" align="center" width="400px" src="https://files.readme.io/78f5fb7cec3f2599154bc2b77836d87528d065b4a4bb257476bfa37f9c70c375-healthiness.jpg">
  Select healthiness measurement
</Image>