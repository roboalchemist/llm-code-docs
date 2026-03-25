# Source: https://docs.firehydrant.com/docs/analytics-exporting-data.md

# Exporting Data

FireHydrant has multiple ways to export data from its platform.

## API

FireHydrant approaches all development API-first. For the vast majority of functions and capabilities in the FireHydrant platform, a public-facing API endpoint is available for customers to programmatically access.

To access the API, visit the [API documentation here](https://developers.firehydrant.com/#/). There will be example API calls on the site for each endpoint.

## Webpages

### Analytics

<Image align="center" alt="**Download CSV** option for the MTTx table" border={false} caption="**Download CSV** option for the MTTx table" src="https://files.readme.io/bb864e2-CleanShot_2024-08-05_at_10.09.14.png" width="650px" />

Individual graphs and tables within the Analytics pages provide a button to **Download CSV**. This allows users to filter the data on the pages at the top and then export tables according to the visuals they're looking for.

### Incidents

<Image align="center" alt="The Incidents page with a couple filters" border={false} caption="The Incidents page with a couple filters" src="https://files.readme.io/a3ce3d0-CleanShot_2024-07-03_at_16.28.122x.png" width="650px" />

The **Incidents** page allows filtering the list of incidents and exporting that list to CSV file. Clicking "Export to CSV" will trigger an asynchronous background job to generate the data. Once finished, you will receive an email with a link to access the generated CSV.

The list of columns that will be included on the Incidents page export are as follows:

| Field Name                    | Description                                                                                                                                                    | Docs Link                                                                                           |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **number**                    | FireHydrant-assigned number. Counts incrementally up from 1 from the start of the organization's incident history on FireHydrant. This number is not editable. | *N/A*                                                                                               |
| **environments**              | List of comma-delimited Environments impacted on the incident                                                                                                  | [Intro to Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)                                            |
| **functionalities**           | List of comma-delimited Functionalities impacted on the incident                                                                                               | [Intro to Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)                                            |
| **services**                  | List of comma-delimited Services impacted on the incident                                                                                                      | [Intro to Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)                                            |
| **name**                      | Name of the incident                                                                                                                                           | *N/A*                                                                                               |
| **severity**                  | The severity of the incident                                                                                                                                   | [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities)                                          |
| **priority**                  | The priority of the incident                                                                                                                                   | [Severities and Priorities](https://docs.firehydrant.com/docs/severities-and-priorities)                                          |
| **slack**                     | The name of the Slack channel, if one was created for the incident                                                                                             | [Create or rename Incident Slack channel](https://docs.firehydrant.com/docs/runbook-step-create-or-rename-incident-slack-channel) |
| **tickets**                   | Comma-delimited list of follow-ups created in the incident, listed via their ticket codes (e.g., ABC-123)                                                      | [Managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups)                                                      |
| **active\_duration**          | Total duration of the incident listed in `PT##S` format where the number represents the total duration                                                         | [Incident Milestones](https://docs.firehydrant.com/docs/incident-milestones)                                                      |
| **opened\_at**                | The timestamp of when the incident was opened                                                                                                                  | *N/A*                                                                                               |
| **started\_by**               | The person who create the incident in the format of `Name (email)`                                                                                             | [Starting Incidents](https://docs.firehydrant.com/docs/starting-incidents)                                                        |
| **customer\_impact\_summary** | The customer impact statement                                                                                                                                  | [The Command Center](https://docs.firehydrant.com/docs/the-command-center)                                                        |
| **assigned\_teams**           | Comma-delimited list of teams that were assigned to the incident if any                                                                                        | [Team Management](https://docs.firehydrant.com/docs/team-management)                                                              |
| **unassigned\_teams**         | Comma-delimited list of any teams that were unassigned throughout the incident                                                                                 | [Team Management](https://docs.firehydrant.com/docs/team-management)                                                              |
| **tags**                      | Comma-delimited list of tags on the incident if they exist                                                                                                     | [Incident Tags](https://docs.firehydrant.com/docs/incident-tags)                                                                  |
| **\[milestone]\_at**          | The exact timestamps of when the incident reached each milestone. These values will vary according to your milestone configuration                             | [Incident Milestones](https://docs.firehydrant.com/docs/incident-milestones)                                                      |
| **(any custom fields)**       | Any custom fields defined by your organization                                                                                                                 | [Incident Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields)                                                |

### Users

<Image align="center" alt="Users page with filters expanded" border={false} caption="Users page with filters expanded" src="https://files.readme.io/bda2727-CleanShot_2024-08-13_at_17.00.47.png" width="650px" />

The Users page on FireHydrant shows a complete directory of all users in your organization. You can also filter the list of users according to what you're looking for before exporting everything to CSV.

Downloading the CSV will generate the CSV in the browser and open a download modal for you to choose a location to save the file. The downloaded CSV will include:

| Field                            | Description                                                                                                                                                                      |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **id**                           | The UUID assigned by FireHydrant to the user                                                                                                                                     |
| **name**                         | User's full name                                                                                                                                                                 |
| **email**                        | User's email address                                                                                                                                                             |
| **role**                         | The [access role](https://docs.firehydrant.com/docs/role-based-access-controls) the user has                                                                                                                   |
| **enabled**                      | Whether the user is active ("TRUE") or disabled ("FALSE")                                                                                                                        |
| **slack\_connected**             | Whether the user's FireHydrant account is [linked](https://docs.firehydrant.com/docs/slack-integration#linking-users) with their Slack account                                   |
| **alert\_notification\_methods** | Which alerting methods the user has configured for [Signals alerting](https://docs.firehydrant.com/docs/signals-introduction). Values available are: `email`, `slack`, `sms`, `voice`, `whatsapp`, and `push`. |
| **assigned\_teams**              | Comma-separated list of team slugs for which the user is a member of.                                                                                                            |