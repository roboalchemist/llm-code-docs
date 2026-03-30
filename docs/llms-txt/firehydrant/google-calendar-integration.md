# Source: https://docs.firehydrant.com/docs/google-calendar-integration.md

# Google Calendar

The Google Calendar integration is a new capability that improves upon current Google Suite users who may be using the existing [Google Meet](https://docs.firehydrant.com/docs/google-meet-integration) integration.

With a Calendar integration, FireHydrant can create Google Meet bridges and invite the FireHydrant AI Copilot to join the meeting, scribe the conversation, and use the transcript as context for any contextual tasks like providing summaries and answers to prompts. Learn more about our [AI features here](https://docs.firehydrant.com/docs/ai-powered-incident-management)

## Prerequisites

* You'll need <Glossary>Owner</Glossary> permissions in FireHydrant to configure integrations
* You'll need a **generic service account**/**user** with administrative privileges in your Google Workspace.
  * FireHydrant recommends using a generic Google service account or user rather than an individual named user - this prevents problems if the named employee were to depart the organization

## Installing the Google Calendar integration

<Image alt="Finding the Google Calendar integration" align="center" width="650px" src="https://files.readme.io/1cc90da-CleanShot_2024-05-28_at_17.05.53.png">
  Finding the Google Calendar integration
</Image>

1. On FireHydrant's [Integrations page](https://app.firehydrant.io/organizations/integrations), search for the **Google Calendar** app and click the '+'. Then, on the next page, click "Authorize Application."
2. Follow the on-screen steps to allow FireHydrant to access the service account's calendar.

   <Image alt="Granting FireHydrant permissions to the service account's calendar" align="center" width="650px" src="https://files.readme.io/30700d3-CleanShot_2024-05-28_at_17.11.21.png">
     Granting FireHydrant permissions to the service account's calendar
   </Image>

   If completed successfully, you should be returned to the Google Calendar integration's page in FireHydrant. No other configuration is needed at the configuration level.

## Scheduling Retrospectives

<Image alt="Example screenshots of Retrospective scheduling capabilities enabled with Google Calendar" align="center" width="650px" src="https://files.readme.io/a5ec6bf-image.png">
  Example screenshots of Retrospective scheduling capabilities enabled with Google Calendar
</Image>

Once Google Calendar has been configured, you can use it to easily schedule retrospectives in FireHydrant. A "Schedule Retrospective" button will appear at the top of the incident page, and clicking it will take you to Google Calendar's new event page with information pre-filled such as a link to the Incident and all of the responders included as invitees.

Lastly, once the retro has been scheduled, we will also display the date/time it was scheduled for directly in FireHydrant's interface.

**Note:** When scheduling the retrospective, you can use Zoom or any other meeting provider installed in your Google Suite.

## Next Steps

Once the calendar integration is set up, it's time to make use of it in your incident management processes.

* Use the Runbook step [Create a Google Calendar Event](https://docs.firehydrant.com/docs/runbook-step-create-a-google-calendar-event) to create a meeting for the incident and invite the incident scribe automatically

> 📘 Limited Use Disclaimer:
>
> FireHydrant’s use and transfer to any other app of information received from Google APIs will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes), including the Limited Use requirements.