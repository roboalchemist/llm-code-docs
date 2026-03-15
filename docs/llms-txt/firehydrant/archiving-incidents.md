# Source: https://docs.firehydrant.com/docs/archiving-incidents.md

# Archiving Incidents

FireHydrant allows you to archive incidents so they’re hidden from the UI and not counted in your analytics. You may want to archive incidents because:

* You’ve been testing the FireHydrant platform, and you may want to clear all incidents for a “fresh start” in your account
* You accidentally created an incident, and you want to remove it so it’s not counted in your analytics

When you archive an incident, it is hidden from the FireHydrant UI and also from the Analytics data and API.

> 📘 Note:
>
> Archiving an incident will immediately halt any attached Runbooks and executing Runbook steps, as well as exclude the incident data from any Analytics and Metrics calculations. It will also hide the incident by default on the **Incidents** page.

## Archiving incidents

### From the Command Center

<Image alt="Archiving an incident from its Command Center" align="center" width="650px" src="https://files.readme.io/16d1931-Screenshot_2023-12-07_at_5.20.13_PM.png">
  Archiving an incident from its Command Center
</Image>

1. Navigate to the incident you wish to archive.
2. Click the Ellipses next to the "Resolve incident" button.
3. Select **Archive incident**.

### With the API

You can archive incidents using our [Archive an Incident](https://developers.firehydrant.com/#/operations/deleteV1IncidentsIncidentId) API endpoint. Here is an example API call using `cURL`:

```bash cURL
curl --request DELETE \
  --url https://api.firehydrant.io/v1/incidents/${YOUR_INCIDENT_ID} \
  --header 'Authorization: ${YOUR_AUTH_TOKEN}' \
  --header 'Content-Type: application/json'
```

## Unarchiving Incidents

f you decide that you want to retrieve any previously-archived incidents, there are two ways you can do so.

### Via UI

<Image alt="Showing the unarchive button next to Archived incidents" align="center" src="https://files.readme.io/e2a6752-Screenshot_2023-12-07_at_5.26.10_PM.png">
  Showing the unarchive button next to Archived incidents
</Image>

1. In the web UI, go to the Incidents page at the top navigation
2. Adjust the filters so you see only **Archived** incidents.
3. Next to the incident(s) you want to unarchive, click the crossed-out trashbin.

### Via API

You can use the [Unarchive Incident](https://developers.firehydrant.com/#/operations/postV1IncidentsIncidentIdUnarchive) API endpoint. Here is an example API call using`cURL`:

```bash cURL
curl --request POST \
  --url https://api.firehydrant.io/v1/incidents/${YOUR_INCIDENT_ID}/unarchive \
  --header 'Authorization: ${YOUR_AUTH_TOKEN}' \
  --header 'Content-Type: application/json'
```

### Other Recipes and Scripts

Visit the [Recipes](/recipes) section of the documentation website for various example recipes. For example:

* [Archiving all Incidents](/recipes/archive-all-incidents)

## Next Steps

* Continue exploring FireHydrant's capabilities via [Reopening Incidents](https://docs.firehydrant.com/docs/reopening-incidents), creating [historical, resolved incidents](https://docs.firehydrant.com/docs/historical-incidents), or [Scheduled Maintenances](https://docs.firehydrant.com/docs/scheduled-maintenances)
* Look at [Conducting Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives) and see how FireHydrant keeps your responders focused when reviewing incidents
* Check out [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview) for a comprehensive list of all of FireHydrant's integrations