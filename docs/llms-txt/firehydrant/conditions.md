# Source: https://docs.firehydrant.com/docs/conditions.md

# Service Catalog Conditions

FireHydrant allows customizing and tracking the conditions of your Catalog components when marking them on incidents. This allows you to specify the degree or severity with which a Service, Functionality, or Environment may be impacted in the incident.

## Default Conditions

<Image alt="Default conditions provided in FireHydrant" align="center" width="650px" src="https://files.readme.io/e144588-CleanShot_2024-08-13_at_17.58.18.png">
  Default conditions provided in FireHydrant
</Image>

The default conditions are:

* **Unavailable**: The component is not functioning.
* **Degraded**: The component is somewhat functioning, but not at maximum capacity. This could mean major performance issues or bugs that heavily impact usability.
* **Bug**: The component is mostly functioning as expected, but may have issues impacting an aspect not core to the component's function.
* **Operational**: The component is fully functioning as expected.

## Customizing and Using

These conditions can be customized according to your organization's needs. To configure, you can edit the existing Conditions by clicking the Edit pencil next to the appropriate entry, or by clicking "+ Add condition" to create a new condition.

Just like with [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities), conditions can be re-ordered in the user interface which will affect how they are ordered when shown elsewhere, such as on a chat application form or in the web UI when declaring incidents or updating component conditions.

Once configured, they are usable when marking impacted components on incidents and in several other product areas like Severity Matrix.

<Image alt="Example Custom Condition in the Conditions selection in Slack. This is also available via Web UI" align="center" width="400px" src="https://files.readme.io/6929447-image.png">
  Example Custom Condition in the Conditions selection in Slack. This is also available via Web UI
</Image>

## Next Steps

* See how to use these conditions [in tandem with Severity Matrix](https://docs.firehydrant.com/docs/severity-matrix) to automatically set Severity by component and condition
* Read more about how to customize [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities)