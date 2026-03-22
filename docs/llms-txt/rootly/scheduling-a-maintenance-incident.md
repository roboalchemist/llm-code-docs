# Source: https://docs.rootly.com/incidents/incident-operations/scheduling-a-maintenance-incident.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduling Maintenance Incidents

> Learn how to schedule and manage maintenance incidents for planned service interruptions, including Slack channel creation and status page integration.

<iframe src="https://www.loom.com/embed/72b6b01740c74af7a639222408d20ade" title="Loom video player" frameborder="0" className="w-full aspect-video rounded-xl" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />

Maintenance incidents allow your teams to plan, coordinate, and communicate progress of your planned downtime and maintenance windows.

Create a Maintenance Incident in the Rootly web app under **Incidents** > **Maintenance**. 

<Info>
  Rootly does not automatically generate a Slack channel for Maintenance Incidents. Create one by selecting the Slack icon under the incident title in the web app.
</Info>

After the maintenance incident has been created, share it on your [Status Pages](https://docs.rootly.com/configuration/status-pages).

# Schedule a Maintenance Incident from the web app

<Steps>
  <Step title="Step 1">
    Go to **Incidents > Maintenance** and click **Schedule Maintenance** in the top-right corner.

        <img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.09.01@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=8db27f3cf1ae96910e9c5951e9cc8add" alt="Clean Shot2025 11 18at16 09 01@2x Pn" width="3388" height="1028" data-path="images/CleanShot2025-11-18at16.09.01@2x.png" />
  </Step>

  <Step title="Step 2">
    Fill in the *Maintenance Incident* form. If you want to gather more details, the form can be completely customized in the **Configuration** > **Forms** section of the web application.

        <img src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/maintenance/main2.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=2ef25cb95ab5d8c0c5267ca1ceb89b17" alt="Maintenance incident web form." width="591" height="681" data-path="images/maintenance/main2.webp" />

    The default *Maintenance Incident* form includes:

    | Field                                                               | Content                                                                                      |
    | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
    | Title                                                               | Title of the incident. This will be used to create the channel name along with today's date. |
    | Summary                                                             | A summary of the incident.                                                                   |
    | [Severity](https://docs.rootly.com/configuration/severities)        | Defaults: Severity level from SEV3 to SEV0.                                                  |
    | [Type](https://docs.rootly.com/configuration/incident-types)        | The type of incident. Defaults: Cloud, Security, Customer facing, Default.                   |
    | [Services](https://docs.rootly.com/configuration/services#services) | The service or services impacted.                                                            |
  </Step>

  <Step title="Step 3">
    Click **Create Incident** to save.

        <img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.11.18@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=02c9c9b4b7f1ae89641e13b2c764a439" alt="Clean Shot2025 11 18at16 11 18@2x Pn" width="3386" height="1980" data-path="images/CleanShot2025-11-18at16.11.18@2x.png" />
  </Step>
</Steps>

# Schedule a Maintenance Incident from Slack

<Steps>
  <Step title="Step 1">
    Enter the Slack command **/rootly maintenance**. Press *enter* or click *the paper plane icon* to run the command and open the \_maintenance incident \_form.
  </Step>

  <Step title="Step 2">
    Fill in the *maintenance incident* form. *Scheduled for* and *Scheduled until* dates and times are required.

        <img src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/maintenance/Slackmaintenanceschedule.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=d6e614238ef6917197ab81d67531d840" alt="Maintenance incident Slack form." width="1078" height="1318" data-path="images/maintenance/Slackmaintenanceschedule.webp" />

    Most of the fields in the *maintenance incident* form can be customized and new fields can be added. If you want to gather more details, the form can be completely customized in the **Configuration** > **Forms** section of the web application.

    The default *maintenance incident* form includes:

    | Field                                                               | Content                                                                                      |
    | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
    | Title                                                               | Title of the incident. This will be used to create the channel name along with today's date. |
    | Summary                                                             | A summary of the incident.                                                                   |
    | [Severity](https://docs.rootly.com/configuration/severities)        | Defaults: Severity level from SEV3 to SEV0.                                                  |
    | [Type](https://docs.rootly.com/configuration/incident-types)        | The type of incident. Defaults: Cloud, Security, Customer facing, Default.                   |
    | [Services](https://docs.rootly.com/configuration/services#services) | The service or services impacted.                                                            |
  </Step>

  <Step title="Step 3">
    Click **Schedule** to save.

        <img src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/maintenance/mainschedslack.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=0113ad639842ced007ff5487c6d9b030" alt="New maintenance incident notification in Slack." width="537" height="295" data-path="images/maintenance/mainschedslack.webp" />

    The maintenance incident is now available in the Rootly web app. To manage the incident in Slack, select *View in Rootly,* then click the Slack icon under the incident title.
  </Step>
</Steps>

# Update a maintenance incident

## **Change the status**

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.14.43@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=b30d9045a802a22522eaf841c1c2a90a" alt="Clean Shot2025 11 18at16 14 43@2x Pn" width="3402" height="1988" data-path="images/CleanShot2025-11-18at16.14.43@2x.png" />

Maintenance incidents can have the following statuses:

* Planning
* Scheduled
* In Progress
* Verifying
* Completed
* Cancelled

Change the status by clicking **Incident Status** in the top-right corner, or in Slack using the `/rootly status` command.

## **Update details** 

Click **Edit** in the top-right corner to update the incident.

Default fields include:

| Field                                                                                    | Content                                                                                                                               |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Scheduled start and end time                                                             | The planned time for the maintenance to take place.                                                                                   |
| Title                                                                                    | The title of the maintenance incident. This will only be visible in the Rootly web app or the incident Slack channel (if applicable). |
| [Severity](https://docs.rootly.com/configuration/severities)                             | Defaults: Severity level from SEV3 to SEV0.                                                                                           |
| [Type](https://docs.rootly.com/configuration/incident-types)                             | The type of incident. Defaults: Cloud, Security, Customer facing, Default.                                                            |
| [Services](https://docs.rootly.com/configuration/services#services)                      | The service or services impacted.                                                                                                     |
| [Environments](https://docs.rootly.com/configuration/environments)                       | The environment the incident will impact. E.g. Dev or Production.                                                                     |
| [Functionalities](https://docs.rootly.com/configuration/functionalities#functionalities) | Specific functionalities impacted. E.g. Checkout or Search.                                                                           |
| [Teams](https://docs.rootly.com/configuration/teams#teams)                               | The relevant teams involved in this maintenance incident.                                                                             |

The form can be edited from **Configuration** > **Forms & Fields** > **Update Maintenance Incident.**

## **Assign Roles**

Pre-assign roles to this maintenance incident by selecting "Assign Roles"  under the incident title.

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.16.42@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=c29e860e6d1076ecf4fdc32d471374af" alt="Clean Shot2025 11 18at16 16 42@2x Pn" width="1302" height="1080" data-path="images/CleanShot2025-11-18at16.16.42@2x.png" />

## **Create a Slack channel**

Select the Slack icon under the incident title to create a Slack channel for this maintenance incident.

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.16.59@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=054f650335eb6fcd4007364a26d0a6b5" alt="Clean Shot2025 11 18at16 16 59@2x Pn" width="898" height="592" data-path="images/CleanShot2025-11-18at16.16.59@2x.png" />

# Publish your maintenance incident to a status page

Communicate your upcoming and active maintenance windows to your stakeholders through the Rootly Status Page.

Navigate to your maintenance window, select the **Status Page** tab, then **Publish Incident**.

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.20.31@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=eb00eb07bc1fcb2c9290b373f4fcd2a5" alt="Clean Shot2025 11 18at16 20 31@2x Pn" width="2158" height="1030" data-path="images/CleanShot2025-11-18at16.20.31@2x.png" />

Select the status page you'd like to publish an update to and fill in the subsequent information to include in the update.

Rootly will automatically surface any Maintenance Windows at the top of the status page.

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.23.30@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=af0de9e91b8fa2d28904ce80d69c04ac" alt="Clean Shot2025 11 18at16 23 30@2x Pn" width="1922" height="728" data-path="images/CleanShot2025-11-18at16.23.30@2x.png" />

Further, any services attached to your Maintenance Window will automatically be shown as \*\*In Maintenance \*\*if the update published to the status page is either **In Progress** or **Verifying.**

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.24.14@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=71544d5775f0a7d0ae9990d2b0e1e27a" alt="Clean Shot2025 11 18at16 24 14@2x Pn" width="1920" height="688" data-path="images/CleanShot2025-11-18at16.24.14@2x.png" />

<Info>
  To give you full control over how maintenance windows are communicated to your stakeholder, Rootly will not automatically update your status page based on the maintenance incident's current status: updates must be manually published to the status page.
</Info>

# Building workflows for maintenance incidents

You can build automations for your Maintenance Incidents using [Rootly's Workflow builder](/workflows/incident-workflows). Follow the instructions to create a workflow in the linked documentation.

To create a workflow specific to Maintenance Windows, ensure your workflow has a **Kind** condition set to**Scheduled Maintenance**  so that the workflow will only fire on your maintenance incidents.

<img src="https://mintcdn.com/rootly/FHjTy6rO-WKtCUfQ/images/CleanShot2025-11-18at16.30.08@2x.png?fit=max&auto=format&n=FHjTy6rO-WKtCUfQ&q=85&s=48a7a2076e0cf4345e227e6494802404" alt="Clean Shot2025 11 18at16 30 08@2x Pn" width="1652" height="702" data-path="images/CleanShot2025-11-18at16.30.08@2x.png" />

# Converting a maintenance incident

Sometimes, unexpected complexity might occur during your maintenance incident, and it requires a regular incident to be declared.

Rootly lets you convert an existing maintenance incident into a regular incident directly in Rootly Web, or via Slack.

## Converting to a regular incident on web

While viewing your Maintenance Incident on web, select (...), then**Convert to incident** .

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-06-18at13.52.12@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=2c7495756fb01372a8a43967b48abfbc" alt="Clean Shot2025 06 18at13 52 12@2x Pn" width="716" height="636" data-path="images/CleanShot2025-06-18at13.52.12@2x.png" />

Clicking on this button will trigger your Rootly **Create Incident** form, as well as a 'Reason for conversion' field for your commanders to fill out to give additional context for why the incident is being converted. The information provided in this field will be added to the incident's timeline.

## Converting to a regular incident on Slack

To convert your maintenance incident on Slack, in your maintenance incident's Slack channel use the `/rootly convert maintenance` command.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-06-18at14.03.35@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=6755d3c1a7cfc7aa5eb16b09ebd769b8" alt="Clean Shot2025 06 18at14 03 35@2x Pn" width="1100" height="1352" data-path="images/CleanShot2025-06-18at14.03.35@2x.png" />

This will trigger your Rootly **Create Incident** form, as well as a 'Reason for conversion' field for your commanders to fill out to give additional context for why the incident is being converted. The information provided in this field will be added to the incident's timeline.

Once your maintenance incident is converted to a regular incident, all of your related automations and workflows will trigger much like they do when a new incident is created.


Built with [Mintlify](https://mintlify.com).