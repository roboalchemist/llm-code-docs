# Source: https://docs.firehydrant.com/docs/retroactive-incidents.md

# Retroactive Incidents

When an incident doesn't require active incident management, you can create a retroactive incident (called Resolved Incidents in the platform). Resolved incidents start at the "Resolved" milestone and skip any automation you have configured, including not alerting any teams that own Services, Functionalities, and Environments. This is useful for logging incidents that have already occurred.

> 📘 Note:
>
> Resolved incidents allow users to manually add runbooks, so you can use Incident Types to ensure that Resolved Incidents use the appropriate runbooks for non-active incidents. Learn more about [Incident Types](https://docs.firehydrant.com/docs/incident-types).

## via Slack

In a Slack workspace with the FireHydrant bot installed, you can run `/fh create-resolved` to create a resolved incident.

<Image alt="Create resolved incident Slack form" align="center" width="400px" src="https://files.readme.io/5ff906e-create-resolved-slack-form.png">
  Create resolved incident Slack form
</Image>

In Slack, users will be required to enter a start date and time as well as an end date and time. The rest of the form will follow the logic of your [incident fields settings](https://docs.firehydrant.com/docs/incident-fields), including required fields, visible fields, and custom fields. [Incident Types](https://docs.firehydrant.com/docs/incident-types) field will be visible if you have any Types configured, but it is optional.

Just as in the web interface, you can explicitly add a Runbook to this Resolved Incident for any automation you may need. Where applicable, incident types can also be used to add Runbooks to Resolved Incidents by selecting a Runbook when defining the incident type.

## via Web UI

From any screen in the FireHydrant web application, click the dropdown to the right of the "Declare Incident" button and select "Create Resolved Incident".

<Image alt="Create resolved incident button" align="center" width="650px" src="https://files.readme.io/dcfeb1a8a4203a4d91951fd60d2d89ecd60c8e372f0cb8202ec2d8de3caa237b-CleanShot_2025-01-13_at_18.08.16.png">
  Create resolved incident button
</Image>

In the Create Resolved Incident form, you will be required to add a name, a start date and time, an end date and time, and any other required fields.

Additionally, you can select an incident type or add any additional details by selecting additional fields at the bottom of the form. Like the Slack form, these fields will be required or visible according to what you've configured in your [Incident Fields settings](https://docs.firehydrant.com/docs/incident-fields).

<Image alt="Create resolved incident web form" align="center" width="650px" src="https://files.readme.io/38c50668d8f10627f8e52c6d09b35652c59c354cf5d764b053532aa31601c509-CleanShot_2025-01-13_at_18.07.21.png">
  Create resolved incident web form
</Image>

Once the details are completed, click "Create Incident" to create the incident and view the resolved incident page.

## via the API

You can create a Resolved Incident via the API by using the same standard [Create Incident endpoint](https://developers.firehydrant.com/#/operations/postV1Incidents), but with the `milestone` field set with milestones for both `started` and `resolved`. For example:

```curl cURL
curl --request POST \
  --url https://api.firehydrant.io/v1/incidents \
  --header 'Authorization: Beaerer ${FH_API_KEY}' \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "Example Resolved Incident",
  "milestones": [
    {
      type: "started",
      occurred_at: "2023-01-24T14:15:22Z"
    },
    {
      type: "resolved",
      occurred_at: "2023-01-24T14:17:34Z"
    }
  ]
}'
```

## Next Steps

* Read about how to conduct [Scheduled Maintenances](https://docs.firehydrant.com/docs/scheduled-maintenances) on FireHydrant
* Look at [Conducting Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives)
* Explore [the integrations](https://docs.firehydrant.com/docs/integrations-overview) FireHydrant offers
* See a [recipe for bulk importing historical incidents](/recipes/bulk-create-resolved-incidents)