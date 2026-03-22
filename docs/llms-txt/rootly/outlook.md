# Source: https://docs.rootly.com/integrations/outlook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Outlook

> Schedule Microsoft Outlook calendar events associated with incidents for meeting coordination and response planning.

## Why

**Microsoft Outlook** Integration allows you to:

* **Schedule an Outlook event** associated with an incident.

## Oauth Permissions

Your selected workspace needs the following OAuth permissions:

* **offline\_access**
  * Allows the app to see and update the data you gave it access to, even when users are not currently using the app. This does not give the app any additional permissions.
* **User.Read**
  * Allows you to sign in to the app with your organizational account and let the app read your profile. It also allows the app to read basic company information.
* **Calendars.ReadWrite.Shared**
  * Allows the app to read, update, create and delete events in all calendars in your organization you have permissions to access. This includes delegate and shared calendars.

## Installation

You can set up this integration as a **logged in Admin user in Rootly** in the integrations page. You DO NOT need to be an admin user of your company's Outlook account.

<Note>
  We recommend integrating with a **service account** to make sure the integration doesn't break if a user leaves your company.
</Note>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/outlook/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=577ece20e3128ba76536fd5249640488" width="882" height="832" data-path="images/integrations/outlook/images-1.webp" />
</Frame>

Select the `Setup` to begin installation. You'll be asked to accept the request to install.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/outlook/images-2.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=8effb2e939f6183bdf524b3a19bc9cda" width="526" height="937" data-path="images/integrations/outlook/images-2.webp" />
</Frame>

## Configuration

Rootly's Outlook integration relies on workflows to automate the scheduling of events. The most common setup is to run the **Create an Outlook Event** when an incident resolves.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/outlook/images-3.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=c2e901161c1d1d88b24fb616735726fe" width="868" height="1153" data-path="images/integrations/outlook/images-3.webp" />
</Frame>

### Name

This field is automatically set for you. You can rename this field to whatever best describes your action. The value in this field does not affect how the workflow action behaves.

### Calendar

Pick the calendar that you would like to schedule the event to.

### Summary

Enter the title of your scheduled event. This field accepts Liquid syntax.

### Description

Enter a more detailed description of your scheduled event.

### Attendees

Enter the emails of the attendees you'd like to invite. This field accepts Liquid syntax.

### Time Zone

Enter the timezone in which you'd like the meeting to be booked in. The value you select later in the `Time of Meeting` field will be in the timezone selected here.

### Days Until Meeting

Enter the number of days you'd like to schedule the event into. Rootly starts counting from the time when the workflow is run. For example, if the value set in this field is `3` and the workflow was run on January 1st, the event will be scheduled 3 days from January 1st.

### Meeting Duration

Enter the length of the event you'd like to schedule. This field accepts Liquid syntax.

### Time of Meeting

This is the time in which the event will be scheduled at. The time entered here will be in the timezone specified in the `Time Zone` field.

### Exclude Weekends

Checking this option will not include weekends in the count for `Days Until Meeting`.

### Post to Incident Timeline

Checking this option will post the workflow run to the incident timeline.

## Uninstall

1. Login to your **Microsoft Teams Meeting** account.
2. Click **Manage > Installed Apps** or search for the **Rootly** App.
3. Click the **Rootly** app.
4. Click **Uninstall**.


Built with [Mintlify](https://mintlify.com).