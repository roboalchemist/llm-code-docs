# Source: https://docs.firehydrant.com/docs/jira-field-mapping.md

# Jira Field Mapping

<Image alt="Field Mapping tab in Jira projects" align="center" width="650px" src="https://files.readme.io/8529e4f-image.png">
  Field Mapping tab in Jira projects
</Image>

FireHydrant's incidents have [numerous out-of-box fields](https://docs.firehydrant.com/docs/incident-fields) as well as [custom fields](https://docs.firehydrant.com/docs/incident-custom-fields). Subsequently, organizations may need to map these FireHydrant fields to Jira fields when creating tickets. FireHydrant allows for this via the Field Mapping tab.

This step is required if your organization's Jira project(s) have custom required fields, in which case these mappings must be configured, or API calls will fail.

## Prerequisites

* **You will need<Glossary>Owner</Glossary> permissions on FireHydrant to configure integrations**.
* **You must have already created at least one Jira project**.
  * If not, see the guides for [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration) or [Jira Server (On-Premise)](https://docs.firehydrant.com/docs/jira-server-on-premise-integration).

## Default mappings

When you [create Jira incident tickets](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue) or [follow-up tickets](https://docs.firehydrant.com/docs/managing-follow-ups) from FireHydrant, these are the following default behaviors. You must set up custom field mappings if you'd like anything more or to override/customize the behaviors below when creating Jira tickets.

### Incident tickets

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Jira Field Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Summary**
      </td>

      <td>
        Whatever you set inside the [Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue).
      </td>
    </tr>

    <tr>
      <td>
        **Description**
      </td>

      <td>
        Whatever you set inside the [Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-jira-issue). A link back to the incident that executed this step will be appended at the end.
      </td>
    </tr>

    <tr>
      <td>
        **Status**
      </td>

      <td>
        Maps the status according to what you configured for **Milestone Mappings** under **Incident Tickets** tab when configuring the project. Any changes to the incident's Milestone will automatically update the status of the corresponding Jira ticket.

        * \*Note\*\*: Changes made to the ticket status directly will be overwritten by changes to FireHydrant incident milestone.
      </td>
    </tr>

    <tr>
      <td>
        **Reporter**
      </td>

      <td>
        Attempts to set the user who started the incident by matching email addresses, otherwise falls back to the default authorized user that configured the integration (**Note: Jira Cloud only**).
      </td>
    </tr>

    <tr>
      <td>
        **Labels**
      </td>

      <td>
        Includes the incident's **Severity**, **Priority**, and "firehydrant" always.
      </td>
    </tr>
  </tbody>
</Table>

### Follow-Up tickets

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Jira Field Name
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Summary**
      </td>

      <td>
        Whatever you fill for **Title** when creating the Follow-Up within FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        **Description**
      </td>

      <td>
        Whatever you fill for **Description** within FireHydrant
      </td>
    </tr>

    <tr>
      <td>
        **Linked issues**
      </td>

      <td>
        Relates to the original Incident Jira ticket using the relationship you specified when configuring the project, if such a ticket exists
      </td>
    </tr>

    <tr>
      <td>
        **Status**
      </td>

      <td>
        Maps the status according to **Folow up status mappings** under the **Follow Ups** tab when configuring the project.

        * \*Note\*\*: This parameter is 2-way. Changes to the follow-up ticket's status in Jira will change the follow-up's status in FireHydrant.
      </td>
    </tr>

    <tr>
      <td>
        **Reporter**
      </td>

      <td>
        Attempts to match the user who created the Follow-Up by matching email addresses, otherwise falls back to the default authorized user that configured the integration (**Note: Jira Cloud only**)
      </td>
    </tr>

    <tr>
      <td>
        **Labels**
      </td>

      <td>
        Includes the incident's **Severity**, **Priority**, and "firehydrant" always, along with any ticket tags you set when creating the Follow-Up in FireHydrant
      </td>
    </tr>
  </tbody>
</Table>

## When do I need to configure custom mappings for fields?

There are multiple scenarios where you **must** configure field mappings for FireHydrant to be able to create tickets in your project(s):

* **When you want more than the default mappings/behavior** - See the previous section
* **When you have custom, required fields** - If a specific project has any required fields that are not set automatically above, especially if they are custom issue fields, then you'll need to configure them in FireHydrant so we know what to set for those fields
* **(Sometimes) When using the Epic issue type** - Some organizations have configurations in place such that when creating a ticket of type **Epic**, both **Summary** and **Epic Name** fields are required. In this instance, you must create a mapping for **Epic Name** (you can set it to a dynamic value, like `{{ incident.name }}`, see below)

## How to configure field mapping

Assuming you're in a situation where you must map fields, follow the instructions below.

1. Navigate to the Jira settings page and click on the project you'd like to configure, then the **Field Mapping** tab.
2. Click '+ Add mapping' to create a new mapping.
3. A drawer will come out on the right where you can select between two choices:
   1. **Basic mapping** allows you to always set fields in Jira to the same values.
   2. **Advanced mapping** allows conditional logic to map different fields to different values in Jira based on various parameters within FireHydrant.

<Image alt="Custom field mappings in Jira" align="center" width="650px" src="https://files.readme.io/7ad7796-image.png">
  Custom field mappings in Jira
</Image>

3. You can select a Jira field once you've selected between basic vs. advanced mapping.
   1. If **Basic**, you can set the field's value, and this will apply each time you create the ticket and whenever any detail on the incident is updated.
   2. If **Advanced**, you can select conditions and values that should apply when those conditions are met, along with an **Else** default value if no conditions are met.

> 📘 Note:
>
> Field mappings for a project and its tickets are evaluated and applied upon every incident update. For example, if you have a condition to "set Jira ticket Severity field to `SEV1` whenever the incident is is `SEV1`, otherwise default to `SEV3`," this will evaluate each time you make updates on the incident so that if the severity is escalated/de-escalated, the field in Jira will change accordingly.

4. For values, you will see multiple possibilities depending on the field's configuration in Jira:
   1. **For single-select fields**: You will see a dropdown to choose an existing value from Jira
   2. **For all other fields**: You can choose between preset FireHydrant parameters and "Use a custom value." If you select Custom Value, you can input any value you'd like, and the field will also support [Template Variables](https://docs.firehydrant.com/docs/template-variables). Note that what you can insert as a custom value will depend on the field's settings in Jira. For in-depth examples, visit the [section below](#custom-field-mapping-values).
5. Once this field's mapping has been configured to your liking, click **Save** to persist. Rinse and repeat these steps for all fields you'd like to map.

> 📘 Note:
>
> **Currently, the integration is one-way only**. Changes to mapped fields for linked Jira tickets will not propagate back to FireHydrant.

### Advanced Mapping Conditions

The following conditions are available for configuring advanced if/else if/else rules in Jira Field mapping:

* **Current severity** - Current incident's severity
* **Current milestone** - Current incident's milestone
* **Incident name**
* **Incident number**
* **Ticket priority** - Priority of the Follow-up created on FireHydrant (not Incident)
* **Ticket tags** - Tags of the Follow-up created on FireHydrant (not Incident)
* **Incident impacted infrastructure** - Which [Service Catalog components](https://docs.firehydrant.com/docs/intro-to-service-catalog) are impacted on an incident
* **Fields]** - Any\*\* - Any [Incident Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields) configured by users
* **Entered\[milestone] at** - If timestamp for the specified milestone exists and has been filled in

## Custom field mapping values

<Image alt="Custom values for Jira field mapping" align="center" width="400px" src="https://files.readme.io/1cb79bd-318561780-90c236bd-0c8f-4c47-82e9-d76db9952165.png">
  Custom values for Jira field mapping
</Image>

Custom values allow you to input what you'd like us to send to Jira. Remember to check the type of the Jira field you are attempting to map, as some formats and inputs may not be accepted.

* The value entered must be valid for the target field for literal values.
* For things like datetimes, the value must be a valid JSON datetime.
* For options, the string value must match a valid option exactly.
* For arrays of strings, you can specify comma-separated values.
* Jira component-type fields can be handled by passing in an array as a literal value. For example, Liquid templating is supported if the dynamically generated text data type matches the Jira destination field.

### Example Usage

In this example, we’ll pass the following dynamic variables to the Jira Labels field:

* Impacted functionalities
* Incident severity
* Incident number

#### 1. Configure the field mapping

From the Integrations tiles, choose to edit the Jira configuration.  For a Jira project of interest, add a literal value field mapping with the destination as the Jira **Labels** External field.

#### 2. Impacted functionalities liquid syntax

The [impacted functionalities array](/docs/template-variables/#service-related-fields) contains the name and ID, but we only want the name.

In this example, we’ve replaced any spaces in functionality names with a “-”. This is the Liquid code to pass in an array of impacted functionality names where each impacted functionality will get its own Jira label:

```liquid
{{ incident.functionalities | map: "name" | join: "," | replace: " ", "-" }}
```

#### 3. Incident severity liquid syntax

Now, we'll add a label for the current incident severity, which looks like this:

```liquid
{{ incident.severity }}
```

#### 4. Incident number liquid syntax

Lastly, we'll add a label for the incident number, which looks like this:

```liquid
{{ incident.number }}
```

#### 5. Putting it all together

Here is the liquid code all together:

```liquid
{{ incident.functionalities | map: "name" | join: "," | replace: " ", "-" }}, {{ incident.severity }}, {{ incident.number }}
```

Copy this into the **Value** field. Click **Update field mapping** to save the configuration.

#### 6. Use the mapping in a Jira incident ticket

Create a runbook step pointing to the Jira project with your new Label mapping.

When an incident ticket is created with the mapped project fields, the impacted functionalities, incident number, and severity are passed to the Jira Labels field.

<Image alt="Custom labels mapped on an incident ticket in Jira" align="center" width="650px" src="https://files.readme.io/968defd-image.png">
  Custom labels mapped on an incident ticket in Jira
</Image>

Once the field mapping is configured, the mappings will be applied to other tickets - incident or follow-up - created in the same project.

<Image alt="The same mappings for a Follow-Up created in the same project" align="center" width="650px" src="https://files.readme.io/662db56-image.png">
  The same mappings for a Follow-Up created in the same project
</Image>

## Next Steps/Resources

* Learn more about FireHydrant's [Template Variables](https://docs.firehydrant.com/docs/template-variables)
* Look at [FireHydrant's Liquid Playground](https://liquidjs.com/playground.html#I0ZpcmVIeWRyYW50IExpcXVpZCBFeGFtcGxlcwpEb2NzOiBodHRwczovL3Nob3BpZnkuZGV2L2FwaS9saXF1aWQKRm9yIG1vcmUgZXhhbXBsZXM6IGh0dHBzOi8vZ2l0aHViLmNvbS9maXJlaHlkcmFudC9saXF1aWQtdGVtcGxhdGUtZXhhbXBsZXMKCiMjQmFzaWMgRXhhbXBsZXMKSW5jaWRlbnQgbmFtZToge3tpbmNpZGVudC5uYW1lfX0KQ2hhbm5lbCBuYW1lOiB7e2luY2lkZW50LmNoYW5uZWxfbmFtZX19ClRhZ3MKICB7JS0gZm9yIHRhZyBpbiBpbmNpZGVudC50YWdfbGlzdCAlfQogICAgKiB7eyB0YWcgfX0KICB7JS0gZW5kZm9yICV9CkppcmEgVGlja2V0CiAgeyUtIGZvciB0aWNrZXQgaW4gaW5jaWRlbnQuaW5jaWRlbnRfdGlja2V0c1swXS5hdHRhY2htZW50cyAlfQogICAgKiB7eyB0aWNrZXQuZGlzcGxheV90ZXh0IH19IHwge3sgdGlja2V0LmhyZWZfdXJsIH19CiAgeyUtIGVuZGZvciAlfQpOb3RlOiBUaGUgJ3JldHJvJyBvYmplY3QgaXMgb25seSBhdmFpYWxibGUgYWZ0ZXIgYSByZXRyb3NwZWN0aXZlIGhhcyBiZWVuIHN0YXJ0ZWQgYW5kIGluIHRoZSBjb250ZXh0IG9mIGEgJ3JldHJvIGV4cG9ydCcgcnVuYm9vayBzdGVwLgoqIFJldHJvIHB1Ymxpc2hlZCBhdDoge3tyZXRyby5wdWJsaXNoZWRfYXR9fQ==,ewoJImluY2lkZW50IjogewoJCSJpZCI6ICJpbmNpZGVudF9pZCIsCgkJIm5hbWUiOiAiVGVzdCBJbmNpZGVudCIsCgkJImNyZWF0ZWRfYXQiOiAiMjAyMi0wNS0yMFQxNTo0Mjo0NC42MjlaIiwKCQkic3RhcnRlZF9hdCI6ICIyMDIyLTA1LTIwVDE1OjQyOjQ0LjcxOFoiLAoJCSJzdW1tYXJ5IjogIlN1bW1hcnkiLAoJCSJjdXN0b21lcl9pbXBhY3Rfc3VtbWFyeSI6IG51bGwsCgkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkiY3VycmVudF9taWxlc3RvbmUiOiAicmVzb2x2ZWQiLAoJCSJudW1iZXIiOiAxNjYsCgkJInByaW9yaXR5IjogIlA0IiwKCQkic2V2ZXJpdHkiOiAiU0VWMyIsCgkJInNldmVyaXR5X2ltcGFjdCI6IG51bGwsCgkJInNldmVyaXR5X2NvbmRpdGlvbiI6IG51bGwsCgkJInRhZ19saXN0IjogWwoJCQkidGFnMSIsICJ0YWcyIgoJCV0sCgkJInByaXZhdGVfaWQiOiAieHh4eHh4eCIsCgkJIm9yZ2FuaXphdGlvbl9pZCI6ICJvcmdfaWQiLAoJCSJpbmNpZGVudF9yb2xlcyI6IFtdLAoibWlsZXN0b25lcyI6IFsKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNDQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDQ3WiIsCiJ0eXBlIjogInN0YXJ0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxMzoxMDoxOS4wMDBaIiwKImR1cmF0aW9uIjogbnVsbAp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNTJaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wODZaIiwKInR5cGUiOiAiZGV0ZWN0ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNDoxMzo1NS4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgzTTM2UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTA6MTkuNjg5WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDkyWiIsCiJ0eXBlIjogImFja25vd2xlZGdlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE1OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wNjVaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNDowNy4wOThaIiwKInR5cGUiOiAiaW52ZXN0aWdhdGluZyIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE2OjEzOjU2LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSCIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDcwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTA0WiIsCiJ0eXBlIjogImlkZW50aWZpZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxNzoxMzo1Ny4wMDBaIiwKImR1cmF0aW9uIjogIlBUMUgxUyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMDc1WiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTQ6MDcuMTEwWiIsCiJ0eXBlIjogIm1pdGlnYXRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDE4OjEzOjU4LjAwMFoiLAoiZHVyYXRpb24iOiAiUFQxSDFTIgp9LAp7CiJpZCI6ICJ1bmlxdWVfbWlsZXN0b25lX2lkIiwKImNyZWF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNTZaIiwKInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zODNaIiwKInR5cGUiOiAicmVzb2x2ZWQiLAoib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQyMjoxNzoxMi4zNDdaIiwKImR1cmF0aW9uIjogIlBUNEgzTTE0UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzQwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MTg6NDAuMzcwWiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fc3RhcnRlZCIsCiJvY2N1cnJlZF9hdCI6ICIyMDIyLTA2LTA0VDIyOjE4OjQwLjMzM1oiLAoiZHVyYXRpb24iOiAiUFQxTTI3UyIKfSwKewoiaWQiOiAidW5pcXVlX21pbGVzdG9uZV9pZCIsCiJjcmVhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTIwWiIsCiJ1cGRhdGVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTY0WiIsCiJ0eXBlIjogInBvc3Rtb3J0ZW1fY29tcGxldGVkIiwKIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMjI6MzI6NTMuNTA5WiIsCiJkdXJhdGlvbiI6ICJQVDE0TTEzUyIKfQpdLAoJCSJhY3RpdmUiOiB0cnVlLAoJCSJsYWJlbHMiOiB7fSwKCQkicm9sZV9hc3NpZ25tZW50cyI6IFtdLAoJCSJzdGF0dXNfcGFnZXMiOiBbXSwKCQkiaW5jaWRlbnRfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbmNpZGVudF9pZC9pbmNpZGVudC9vdmVydmlldyIsCgkJInByaXZhdGVfc3RhdHVzX3BhZ2VfdXJsIjogImh0dHBzOi8vYXBwLmZpcmVoeWRyYW50LmlvL2luY2lkZW50cy9pbnRlcm5hbC9zdGF0dXNfcGFnZS8zMTk3MDgyNi14eHh4LXh4eHgteHh4eC04ZTU5ZTJiNzI5MzUveHh4eHgiLAoJCSJvcmdhbml6YXRpb24iOiB7CgkJCSJuYW1lIjogIlRlc3QgQWNjb3VudCIsCgkJCSJpZCI6ICJvcmdfaWQiCgkJfSwKCQkiY3VzdG9tZXJzX2ltcGFjdGVkIjogMCwKCQkibW9uZXRhcnlfaW1wYWN0IjogbnVsbCwKCQkibW9uZXRhcnlfaW1wYWN0X2NlbnRzIjogbnVsbCwKCQkibGFzdF91cGRhdGUiOiBudWxsLAoJCSJsYXN0X25vdGUiOiBudWxsLAoJCSJyZXBvcnRfaWQiOiBudWxsLAoJCSJzZXJ2aWNlcyI6IFt7CgkJCSJuYW1lIjogImZpc2giLAoJCQkiaWQiOiAic3R1ZmYiCgkJfV0sCgkJImVudmlyb25tZW50cyI6IFtdLAoJCSJmdW5jdGlvbmFsaXRpZXMiOiBbXSwKCQkiY2hhbm5lbF9uYW1lIjogImluY2lkZW50LTE2NiIsCgkJImNoYW5uZWxfcmVmZXJlbmNlIjogIjwjQzAzR0M1U0tENUh8aW5jaWRlbnQtMTY2PiIsCgkJImNoYW5uZWxfaWQiOiAiQzAzR0M1U0tENUgiLAoJCSJjaGFubmVsX3N0YXR1cyI6ICJvcGVyYXRpb25hbCIsCgkJImluY2lkZW50X3RpY2tldHMiOiBbewoJCQkiaWQiOiAidGlja2V0X2lkIiwKCQkJInN1bW1hcnkiOiAiVGVzdCBjcmVhdGVkIGluIHVpIiwKCQkJImRlc2NyaXB0aW9uIjogIkRlc2NyaXB0aW9uIiwKCQkJInN0YXRlIjogImluX3Byb2dyZXNzIiwKCQkJInR5cGUiOiAiaW5jaWRlbnQiLAoJCQkiYXNzaWduZWVzIjogW10sCgkJCSJjcmVhdGVkX2J5IjogewoJCQkJImlkIjogInVzZXJfaWQiLAoJCQkJIm5hbWUiOiAiSm9obiBTbWl0aCIsCgkJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkJImVtYWlsIjogImpzbWl0aEBnbWFpbC5jb20iCgkJCX0sCgkJCSJhdHRhY2htZW50cyI6IFt7CgkJCQkidHlwZSI6ICJsaW5rIiwKCQkJCSJkaXNwbGF5X3RleHQiOiAiWFhYLTEwMjIiLAoJCQkJImhyZWZfdXJsIjogImh0dHBzOi8vY29tcGFueS5hdGxhc3NpYW4ubmV0L2Jyb3dzZS9YWFgtMTAyMiIsCgkJCQkiaWNvbl91cmwiOiAiaHR0cHM6Ly9hcHAuY29tcGFueS5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9qaXJhX2Nsb3VkL2Zhdmljb24ucG5nIgoJCQl9XQoJCX1dLAoJCSJpbXBhY3RzIjogW10sCgkJImNvbmZlcmVuY2VfYnJpZGdlcyI6IFtdLAoJCSJpbmNpZGVudF9jaGFubmVscyI6IFt7CgkJCSJpZCI6ICJDMDNHQzVTS0Q1SCIsCgkJCSJuYW1lIjogImluY2lkZW50LTE2NiIsCgkJCSJzb3VyY2UiOiAic2xhY2siLAoJCQkic291cmNlX25hbWUiOiAiU2xhY2siLAoJCQkic291cmNlX2lkIjogInNvdXJjZV9pZCIsCgkJCSJ1cmwiOiAiaHR0cHM6Ly9maHRlc3RhY2NvdW50LnNsYWNrLmNvbS9tZXNzYWdlcy9DMDNHQzVTS0Q1SCIsCgkJCSJpY29uX3VybCI6ICJodHRwczovL2FwcC5maXJlaHlkcmFudC5pby8vaW50ZWdyYXRpb25zLWFzc2V0cy9zbGFjay9mYXZpY29uLnBuZyIsCgkJCSJzdGF0dXMiOiAib3BlcmF0aW9uYWwiCgkJfV0sCgkJInJldHJvX2V4cG9ydHMiOiBbXSwKCQkiY3JlYXRlZF9ieSI6IHsKCQkJImlkIjogInVzZXJfaWQiLAoJCQkibmFtZSI6ICJKb2UgU21pdGgiLAoJCQkic291cmNlIjogImZpcmVoeWRyYW50X3VzZXIiLAoJCQkiZW1haWwiOiAiam9lX3NtaXRoQGdtYWlsLmNvbSIKCQl9LAoJCSJjb250ZXh0X29iamVjdCI6IG51bGwsCgkJInJlc3RyaWN0ZWQiOiBmYWxzZSwKCQkiZXhwbGljaXRfb3JnYW5pemF0aW9uX3VzZXJfaWRzIjogW10KCX0sCgoKCSJyZXRybyI6IHsKICAgICJuYW1lIjogIlRlc3QgSW5jaWRlbnQiLAogICAgInB1Ymxpc2hlZF9hdCI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJxdWVzdGlvbnMiOiBbewoJCQkidGl0bGUiOiAidGl0bGUiLAoJCQkiYm9keSI6ICJib2R5IiwKCQkJInVwZGF0ZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dLAoJCSJjb250cmlidXRpbmdfZmFjdG9ycyI6IFt7CgkJCSJzdW1tYXJ5IjogInN1bW1hcnkiLAoJCQkicG9zaXRpb24iOiAicG9zaXRpb24iLAoJCQkiY3JlYXRlZF9ieSI6ICJKYW5lIFNtaXRoIDxKYW5lU21pdGhAZ21haWwuY29tPiIKCQl9XSwKCQkiaW5jaWRlbnRfcm9sZXMiOiBbewoJCQkibmFtZSI6ICJyb2xlIG5hbWUiLAoJCQkiZGVzY3JpcHRpb24iOiAiUm9sZSBEZXNjcmlwdGlvbiIsCgkJCSJ1c2VyIjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJInN0YXR1cyI6ICJzdGF0dXMiCgkJfV0sCgkJImluY2lkZW50X2FjdGl2ZV9kdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCSJpbXBhY3RzIjogW3sKCQkJInR5cGUiOiAiaW1wYWN0IHR5cGUiLAoJCQkibmFtZSI6ICJpbXBhY3QgbmFtZSIsCgkJCSJzZXZlcml0eSI6ICJTRVYzIiwKCQkJImNvbmRpdGlvbiI6ICJjb25kaXRpb24gbmFtZSIKCQl9XSwKCgkJInN0YXJyZWRfZXZlbnRzIjogW3sKCQkJIm9jY3VycmVkX2F0IjogIjIwMjItMDYtMDRUMTk6MTU6NTYuMDA4WiIsCgkJCSJjcmVhdGVkX2J5IjogIkphbmUgU21pdGggPEphbmVTbWl0aEBnbWFpbC5jb20+IiwKCQkJImJvZHkiOiAiU3RhcnRlZCBFdmVudCBUZXh0IgoJCX1dLAoJCSJtaWxlc3RvbmVzIjogW3sKCQkJInR5cGUiOiAic3RhcnRlZCIsCgkJCSJkdXJhdGlvbiI6ICIyMDIyLTA2LTA0VDE5OjE1OjU2LjAwOFoiLAoJCQkib2NjdXJyZWRfYXQiOiAiMjAyMi0wNi0wNFQxOToxNTo1Ni4wMDhaIgoJCX1dCgl9Cn0=)
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)