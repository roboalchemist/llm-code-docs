# Source: https://docs.firehydrant.com/docs/servicenow-field-mapping.md

# ServiceNow Field Mapping

Field mapping allows for fields from FireHydrant to be mapped with fields in ServiceNow tickets. ServiceNow is complex and highly configurable, so sometimes custom mappings need to be made between FireHydrant's incident fields and ServiceNow's ticket fields.

Ticket types with custom fields need to be mapped to FireHydrant incident fields.

## Prerequisites

* You will need to have installed [ServiceNow](https://docs.firehydrant.com/docs/servicenow-integration)  integration.

## Default Mappings

By default before any custom field mapping, the following items will be synchronized between FireHydrant and ServiceNow automatically or based on different tabs/settings:

* **Title/Summary** - The name of the incident or follow-up will automatically sync with the summary (short description) in ServiceNow
* **Description** - The description of the incident or follow-up ticket will automatically sync with the same (long description) in ServiceNow
* **Status/Milestone** - This is mapped according to the **Incident Tickets** and **Follow Ups** tabs
* **Assignee** - FireHydrant will automatically find matching user(s) with the same email address between both tools to automatically assign a user to the ticket in ServiceNow.

The above mappings are bi-directional, so changes in one tool will propagate and synchronize changes in the other tool.

## When do I need to configure custom mappings for fields?

There are multiple scenarios where you **must** configure field mappings for FireHydrant to be able to create tickets in your project(s):

* **When you have custom, required fields** - If a specific project has any required fields that are not set automatically, especially if they are custom issue fields, then you'll need to configure them in FireHydrant so we know what to set for those fields

## How to configure field mapping

### Outbound Field Mapping (FireHydrant to ServiceNow)

<Image alt="ServiceNow field mapping" align="center" width="650px" src="https://files.readme.io/20d2e778d72e84bb16815fc771a641d46df16fc7f56e620abe42eb4dcecf9c94-servicenow-fieldmapping.png">
  ServiceNow outbound field mapping
</Image>

1. Navigate to the ServiceNow settings page and click on the project you'd like to configure, then selet the **Field Mapping** tab.
2. Click '+ Add mapping' to create a new mapping.
3. A drawer will come out on the right where you can select between two choices:
   1. **Basic mapping** allows you to always set fields in ServiceNow to the same values.
   2. **Advanced mapping** allows conditional logic to map different fields to different values in ServiceNow based on various parameters within FireHydrant.
      > 📘 Note:
      >
      > Field mappings for a project and its tickets are evaluated and applied upon every incident update. For example, if you have a condition to "set ServiceNow ticket Severity field to `SEV1` whenever the incident is is `SEV1`, otherwise default to `SEV3`," this will evaluate each time you make updates on the incident so that if the severity is escalated/de-escalated, the field in ServiceNow will change accordingly.
4. You can select a ServiceNow field once you've selected between basic vs. advanced mapping.
   1. If **Basic**, you can set the field's value, and this will apply each time you create the ticket and whenever any detail on the incident is updated.
   2. If **Advanced**, you can select conditions and values that should apply when those conditions are met, along with an **Else** default value if no conditions are met.
5. For values, you will see the following:
   1. You can choose between preset FireHydrant parameters and "Use a custom value." If you select Custom Value, you can input any value you'd like, and the field will also support [Template Variables](https://docs.firehydrant.com/docs/template-variables). Note that what you can insert as a custom value will depend on the field's settings in ServiceNow.
6. Once this field's mapping has been configured to your liking, click **Save** to persist. Rinse and repeat these steps for all fields you'd like to map.

### Advanced mapping conditions

The following conditions are available for configuring advanced if/else if/else rules in ServiceNow Field mapping:

* **Current severity** - Current incident's severity
* **Current milestone** - Current incident's milestone
* **Incident name**
* **Incident number**
* **Incident description**
* **Ticket priority** - Priority of the Follow-up created on FireHydrant (not Incident)
* **Ticket tags** - Tags of the Follow-up created on FireHydrant (not Incident)
* **Incident impacted infrastructure** - Which [Service Catalog components](https://docs.firehydrant.com/docs/intro-to-service-catalog) are impacted on an incident
* **ustom Fields]**\*\* - Any [Incident Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) configured by users
* **Entered\[milestone] at** - If timestamp for the specified milestone exists and has been filled in

### Inbound Field Mapping (ServiceNow to FireHydrant)

<Image alt="ServiceNow inbound field mapping" align="center" src="https://files.readme.io/b0ae83479fd5666c6b1d13255ca1d8e669f733606350748920ad325c0758f539-inbound-field-mapping.png">
  ServiceNow inbound field mapping
</Image>

Inbound field mapping allows you to control how ServiceNow ticket fields map back to FireHydrant incident fields.  This is especially useful when you have custom fields in ServiceNow that need to be mapped to a specific field in FireHydrant

To configure inbound field mapping:

1. Navigate to your integrations page, and select the ServiceNow integration
2. Click on the project you want to set up inbound field mapping for
3. Navigate to the Inbound Field Mapping tab
4. Click the '+ Add mapping' button
5. In the drawer that appears:
   * Select the FireHydrant field you want to create the inbound field mapping for
   * Select the corresponding ServiceNow field
   * Click Save to persist your changes

Important notes about inbound field mapping:

* Inbound field mapping is only available for basic mapping and not advanced mapping
* Repeat the process to add additional field mappings as needed
* Test your inbound field mapping via your [Runbook step](runbook-step-create-a-servicenow-ticket)

## Common ServiceNow field mappings

### Impact and Urgency matrix

ServiceNow uses a matrix for impact and urgency to visually represent the priority of an incident or issue by considering both the severity of its potential impact on business operations ("impact") and the time sensitivity of resolving it ("urgency"), allowing for a more nuanced assessment of how quickly a problem needs to be addressed based on its potential consequences.

You can set up field mapping in FireHydrant to match your ServiceNow impact and urgency matrix, Using custom fields in FireHydrant.

1. **Create Impact and Urgency custom fields**
   1. In the FireHydrant UI navigation, select **Settings** and then **Incident settings**. On the top right, click  "+ Add custom field".
      1. **Display name** (required): Set the display name to be either **Impact** or **Urgency**
      2. **Help text**: A helpful description for completing the field that appears in tooltips in the web and Slack for your responders
      3. **Type** (required): set this to be the`Multi-select` type.
         1. Enter the following values for `1`, `2`, and `3`
      4. **Field Settings**: Specifies whether the field is required and/or should be immediately visible on the declaration form for users.
2. **Set up Impact and Urgency field mapping**
   1. Navigate to the ServiceNow settings page and click on the project you'd like to configure, then the Field Mapping tab.
   2. Click '+ Add mapping' to create a new mapping.
   3. A drawer will come out on the right;  select the **Basic Mapping** option
   4. Select either **Impact** or **Urgency** from the ServiceNow dropdown
   5. Map that field to the custom field set up from the FireHydrant dropdown
   6. Custom Fields in FireHydrant will be prepended with "Incident". Impact will display as Incident Impact in the dropdown.

<Image alt="Example of an ServiceNow impact and urgency matrix set up in FireHydrant" align="center" src="https://files.readme.io/0d6c114f95eb5967609311a869216f455b93bd9652387eda1e77ce486a0ef7d2-servicenow-impact-urgency.png">
  Mapping Impact and Urgency using Custom Fields
</Image>

### Impacted Service

> 🚧 Note:
>
> This requires for you to have set up the ServiceNow integration in FireHydrant to link with the SNOW CMDB table. See [ServiceNow](https://docs.firehydrant.com/docs/servicenow-integration) instructions or [ServiceNow CMDB](https://docs.firehydrant.com/docs/servicenow-cmdb) for more information.

It's typical for customers to use the SNOW CMDB to track infrastructure and services. FireHydrant's Catalog can synchronize with the ServiceNow CMDB and also automatically mark the correct services as impacted on an incident.

<Image alt="Inbound field mapping" align="center" width="650px" src="https://files.readme.io/b277727a26a00c66eab1d881fdfa37a5bec65df1459f1ce1e4d1d673f1e6412c-CleanShot_2025-03-26_at_17.47.18.png">
  Inbound field mapping
</Image>

1. **Configure inbound mapping** - This enables choosing an impacted service on the ServiceNow incident and automatically marking the same linked service as impacted in FireHydrant.
   1. Navigate to **Settings** > **Integrations list** > **ServiceNow** and select the project you want to map.
   2. In the project settings, go to the **Inbound Field Mapping** tab and add click "+ Add mapping."
   3. In the drawer, choose **Incident impacted infrastructure** for the FireHydrant field and **Service** for the ServiceNow field. Then click "Save."

<Image alt="Outbound field mapping" align="center" width="650px" src="https://files.readme.io/95eabc7327710e22330bb0d0b1d68870e80e7d465d63273894fe4f1834ec5856-CleanShot_2025-03-26_at_17.52.52.png">
  Outbound field mapping
</Image>

2. **Configure outbound mapping** - This enables choosing an impacted service in a FireHydrant incident and automatically marking the same linked service as impacted in ServiceNow
   1. Navigate to **Settings** > **Integrations list** > **ServiceNow** and select the project you want to map.
   2. In the project settings, go to the **Outbound Field Mapping** tab and add click "+ Add mapping."
   3. In the drawer, choose **Service** for the ServiceNow field and **Incident impacted infrastructure** for the FireHydrant field. Then click "Save."