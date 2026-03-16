# Source: https://docs.rootly.com/integrations/opsgenie.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Opsgenie

> Integrate with Opsgenie to import services, create alerts from incidents, and synchronize incident management workflows.

<Warning>
  Atlassian announced the end of life for Opsgenie. Seamlessly migrate to Rootly On-call today. **See how** [**Rootly compares to Opsgenie.**](https://rootly.com/comparisons/opsgenie-vs-rootly-on-call "Rootly Vs.  Opsgenie.")
</Warning>

## Why

**Opsgenie** Integration allows you to:

* Import **Opsgenie** services into Rootly Services.
* **Create** a Rootly alert when creating an incident in Opsgenie.
* **Create** a Opsgenie incident when creating an incident in Rootly.
* **Resolve** a Opsgenie incident right from Rootly.
* Page Directly from Slack ( if Slack Integration enabled ).

**Note:** This integration required an Opsgenie account with at least the **Standard** plan. [https://www.atlassian.com/software/opsgenie/pricing](https://www.atlassian.com/software/opsgenie/pricing "https://www.atlassian.com/software/opsgenie/pricing")﻿

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=26c69da350bc0c338715591b8616fd2a" width="923" height="576" data-path="images/integrations/opsgenie/images-1.webp" />
</Frame>

<Note>
  We recommend you integrating with a **service account** to make sure the integration doesn't break if a user leaves your company.
</Note>

## Import or link services

You can **import** your current Opsgenie services or **link** existing services with Opsgenie services from the **services** page.

Every time and incident will be created with a service linked to Opsgenie, the team associated with this service in Opsgenie will be paged.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-2.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=dbc0a605b7b31ff9e757e1004a6fb2b6" width="918" height="422" data-path="images/integrations/opsgenie/images-2.webp" />
</Frame>

## Configuration

Log into your Opsgenie account then navigate to Settings > Integrations > New Integration

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-3.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=ab1f405d1660369e219bd34dfacc1d53" width="913" height="512" data-path="images/integrations/opsgenie/images-3.webp" />
</Frame>

Select the API integration tile

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-4.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=17e691ccced0109f339e3f5b846c2496" width="919" height="721" data-path="images/integrations/opsgenie/images-4.webp" />
</Frame>

**Access Rights** needs to be: **Read, Create and Update, Configuration Access**

**Note:** The API Key would need to be a **Global** key and can not be scoped to a Team.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-5.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=2d65c2f4e3e0f72b9b1de78ceb39a481" width="920" height="861" data-path="images/integrations/opsgenie/images-5.webp" />
</Frame>

Copy the API integration key back into Rootly

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-6.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=e9e26f1c79211834d027d2e3be20ebfd" width="913" height="573" data-path="images/integrations/opsgenie/images-6.webp" />
</Frame>

Let's now configure webhooks:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-7.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=7c7b4333c6ab3d8dde918349690d5568" width="918" height="997" data-path="images/integrations/opsgenie/images-7.webp" />
</Frame>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-8.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=0f9b742bbe57846ab7aeac0ade2038fb" width="915" height="673" data-path="images/integrations/opsgenie/images-8.webp" />
</Frame>

Add webhook as below:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-9.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=2b613a7b87d927beda4a673d331183fc" width="910" height="579" data-path="images/integrations/opsgenie/images-9.webp" />
</Frame>

All done !

## Auto Assign On-calls to Incident Roles

If you'd like to automatically assign on-calls of a given Opsgenie Schedule to an Incident Role (e.g. Commander), please follow the instructions on the [PagerDuty integration page](/integrations/pagerduty).

## Paging Automatically via Genius Workflows

Set up automated workflows to page various on-call schedules and escalation policies based on the condition of an incident (e.g SEV1 or greater pages Infrastructure).

<Frame>
  <iframe src="https://www.loom.com/embed/54ce8947e9bf423bba175bb94d45c703?sid=9b7fca01-7149-434b-95fa-4c7897203b87" frameborder="0" allowfullscreen width="100%" height="400px" />
</Frame>

## Paging

You can page Opsgenie teams right from Slack using our integration.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/opsgenie/images-10.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=ff8cd514f24ab13bf617fb8455572ae3" width="918" height="867" data-path="images/integrations/opsgenie/images-10.webp" />
</Frame>


Built with [Mintlify](https://mintlify.com).