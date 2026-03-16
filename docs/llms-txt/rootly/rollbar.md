# Source: https://docs.rootly.com/integrations/rollbar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rollbar

> Connect Rootly with Rollbar for error monitoring and automated incident creation from application errors and exceptions.

## Why

**Rollbar** Integration allows you to:

* Ingest issues as alerts
* Create an incident if alerts > count ( you can specify )

## Installation

As an admin, go to `https://rollbar.com/<your-company-slug>/<your-project-slug>/settings/notifications/`

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/rollbar/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=5f4b9f36ff18c9c8ab6a2af088924b3b" width="951" height="1185" data-path="images/integrations/rollbar/images-1.webp" />
</Frame>

Select Webhook

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/rollbar/images-2.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=06c4155521f87a6643a3ebfa0872637a" width="916" height="281" data-path="images/integrations/rollbar/images-2.webp" />
</Frame>

Configure URL you see in Rootly

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/rollbar/images-3.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=ba899048253c5c29513ae44a691f5e51" width="923" height="420" data-path="images/integrations/rollbar/images-3.webp" />
</Frame>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/rollbar/images-4.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=31e2df0bc3a3df268492a78a9b7a7c0e" width="916" height="515" data-path="images/integrations/rollbar/images-4.webp" />
</Frame>

Configure rules you want to enabled ( We support all of them except deploys ) and you are good to go!

## Alerts

Now every time a new issue is declared, they will be ingested as alerts as shown below. Use it in workflow with fetch alerts task to automatically linked recent alerts to your incident.

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/rollbar/images-5.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=c50b744088c7909a19a021f0c3b58b41" width="916" height="435" data-path="images/integrations/rollbar/images-5.webp" />
</Frame>

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).