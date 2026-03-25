# Source: https://docs.firehydrant.com/docs/asana-integration.md

# Asana

Integrating FireHydrant with Asana enables you to create and sync incidents and action items created in FireHydrant with tickets in Asana.

At the end of this guide you'll be able to:

1. Automatically create Asana tickets when incidents are declared in FireHydrant
2. Create follow up tasks in Asana from FireHydrant
3. Map additional fields from FireHydrant into Asana

Let's ride!

## Prerequisites

* Ensure you have <Glossary>Owner</Glossary> permissions. Only users with the Owner role can manage integrations in FireHydrant.
* You'll need a **service account**/**user** with administrative permissions in Asana.

> 📘 Note:
>
> FireHydrant will create and manage data as the user that is logged in to Asana when performing the installation. FireHydrant recommends using a generic Asana service account rather than an individual named user to avoid problems if the named employee were to depart the organization.

## Installing the integration

1. Go to the [Integrations page](https://app.firehydrant.io/organizations/integrations) and search for the Asana tile.

<Image alt="Settings -> Integrations -> Search 'Asana'" align="center" width="650px" src="https://files.readme.io/e22aabf-image.png">
  Settings -> Integrations -> Search 'Asana'
</Image>

2. Once here, click the `[ + ]` button to kick off the OAuth flow between FireHydrant and Asana. You should see a screen that looks like this:

<Image alt="Authorize FireHydrant in Asana" align="center" width="400px" src="https://files.readme.io/1996cba-image.png">
  Authorize FireHydrant in Asana
</Image>

3. Once you've authorized FireHydrant, you'll be brought back to the integration page to see the new integration connected! 🙌

## Configuring projects

Once FireHydrant has been authorized to Asana, you'll need to add projects in Asana to FireHydrant so that we can create and manage tasks appropriately. *This is a mandatory step for the integration to work properly!*

When you select the projects you want, it unlocks the ability to:

1. Create incident tickets in Asana from a Runbook
2. Create follow-ups in Asana from incident follow-ups in FireHydrant

<Image alt="Add an Asana project to FireHydrant" align="center" width="400px" src="https://files.readme.io/4cdc05c-image.png">
  Add an Asana project to FireHydrant
</Image>

### (Optional) Custom field mapping

FireHydrant's incidents have [numerous out-of-box fields](https://docs.firehydrant.com/docs/incident-fields) as well as [custom fields](https://docs.firehydrant.com/docs/incident-custom-fields) of information you can track. Subsequently, it may be crucial for organizations to map these FireHydrant fields to specific fields in the created Asana tasks, and FireHydrant's field mapping allows for this.

This step is also critical if your organization's Asana project(s) have custom required fields, in which case these mappings must be configured on FireHydrant so it can create tickets that pass the validations. Otherwise, the calls will fail.

If you do need to map fields, proceed with the following steps:

1. Click '+ Add mapping' to create a new mapping.
2. A drawer will come out on the right where you can select between two choices:
   1. **Basic mapping** allows you to always set fields in Asana to the same values.
   2. **Advanced mapping** allows conditional logic to map different fields to different values in Asana based on various parameters within FireHydrant.
3. After picking basic vs. advanced mapping, you can select an Asana field to map.
   1. If **Basic**, you can set the field's value, and this will apply each time you create the ticket and whenever any detail on the incident is updated.
   2. If **Advanced**, you can select conditions and values that should apply when those conditions are met, along with an **Else** default value if no conditions are met.

<Image alt="Mapping a field in Asana to a value" align="center" width="400px" src="https://files.readme.io/0cbf766-image.png">
  Mapping a field in Asana to a value
</Image>

> 📘 Note:
>
> Field mappings for a project and its tickets are evaluated and applied upon every incident update. For example, if you have a condition to "set Asana task Severity field to `SEV1` whenever the incident is is `SEV1`, otherwise default to `SEV3`," this will evaluate each time you make updates on the incident so that if the severity is escalated/de-escalated in FireHydrant, the field in Asana will also change accordingly.

## Next Steps

Now that you've configured Asana, it's time to understand how to use it during your incident management:

* Look at the [Create an Asana Task](https://docs.firehydrant.com/docs/runbook-step-create-an-asana-task) Runbook step to see how you can automatically create an Asana ticket for each incident
* [Create follow-up tickets in Asana](https://docs.firehydrant.com/docs/managing-follow-ups) so you can schedule and prioritize work uncovered during incidents
* Browse [the rest of our integrations](https://docs.firehydrant.com/docs/integrations-overview)