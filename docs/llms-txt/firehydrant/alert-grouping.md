# Source: https://docs.firehydrant.com/docs/alert-grouping.md

# Alert Grouping

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Plans
      </th>

      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        * <Glossary>Signals</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        * `Manage Alert Grouping`
      </td>
    </tr>
  </tbody>
</Table>

Alert Grouping allows you to configure rules that combine related alerts to reduce notification noise for your team. When alerts come into FireHydrant, they are checked against your grouping rules to determine if they should be combined with existing alerts.

<Image align="center" alt="Create an Alert Group" border={false} caption="Create an Alert Group" src="https://files.readme.io/f73cf356942e1eb8cfb9951b632184d4da31a7cdb5193609c10210314730ee7e-create-alert-group.png" width="650px" />

## Creating an Alert Group

1. Navigate to **Signals** > **Alert Grouping** and then click "Add an Alert Group."
2. You'll be presented with options to configure your grouping rules:
   1. The string matching section allows you to specify text patterns to match in alerts

   2. You can select which fields to search in: Summary, Description, or Tags

   3. A live preview shows examples of previous alerts that would match your current configuration
   > Note: You can add multiple tags to the same alert group rule as a separate "Match String"

### Configuring time windows

After setting up your matching criteria, you'll need to configure a time window that determines how long FireHydrant looks for matching alerts.

1. Select the time window type:
   * **Absolute** - The window starts when the first matching alert is received
2. Set the duration in minutes or hours
   * The default duration is 30 minutes
3. A timeline preview will show you how alerts will be grouped based on your settings

### Setting actions and states

The final step is to configure what happens when alerts match your rules.

1. Choose the action for matching alerts:

   * **Link** - A new alert is created and shown as "linked." Any pages or communications that would normally have been sent to an on-call user are suppressed.
   * **FYI Only** - This will also create an alert and show it as "linked." However, it will also send a notification that an alert has been linked to specified Slack channel(s).
2. Review the timeline preview to see how your alerts will appear with the chosen settings
3. Click **Create Group** to save your configuration

When an alert is created and linked with a previous, the **state** will indicate as such, and there will be no actions you can take on the linked alert.

<Image align="center" border={false} caption="Example of a linked alert in the web app" src="https://files.readme.io/b707fcd70fd55e7f55450400d71c4c65f64f13416da2835b8560f118961ad3c3-image.png" width="650px" />

If you had chosen to use an **FYI alert** above, you'll also see a message sent to your configured alerts channel about the FYI linked alert notification, like so:

<Image align="center" border={false} caption="Example FYI linked alert in Slack" src="https://files.readme.io/2ffaebfadcdf6c4682038c3d2360b7eb6da18bf6487a94be04a0c5707d988aa2-image.png" width="650px" />

## Best Practices

* Start with broader time windows and adjust based on alert patterns
* Use the live preview to validate matching criteria before implementation
* Review grouped alerts periodically to ensure desired behavior

## Permissions

Users with <Glossary>Member</Glossary> permissions can configure alert grouping within their teams. Users with <Glossary>Owner</Glossary> permissions can configure alert grouping for all teams regardless of membership.

For more information about permissions, visit [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).