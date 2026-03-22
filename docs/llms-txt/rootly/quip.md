# Source: https://docs.rootly.com/integrations/quip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quip

> Integrate Rootly with Quip to automatically create postmortem pages for incident documentation and retrospective analysis.

## Why

**Quip** Integration allows you to:

* Create a Quip page postmortem

## Installation

You can setup this integration as a **logged in admin user** in the integrations page

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/quip/images-1.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=078284360e39d7b53a1a3581180f5d91" width="885" height="705" data-path="images/integrations/quip/images-1.webp" />
</Frame>

## Create an API KEY

Visit [admin.quip.com](https://admin.quip.com "admin.quip.com") and go to **Settings > Integrations**

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/quip/images-2.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=a5f3e5fc24ed2db9bbb8d9284c8a59b0" width="940" height="2220" data-path="images/integrations/quip/images-2.webp" />
</Frame>

Create an API KEY with the following parameters:

* Permissions `USER_READ` and `USER_WRITE`
* Redirect URI: [https://rootly.com/auth/quip/callback](https://rootly.com/auth/quip/callback "https://rootly.com/auth/quip/callback")﻿

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/quip/images-3.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=720bbcceb46ad8c7a6fd98a93a2a421e" width="874" height="681" data-path="images/integrations/quip/images-3.webp" />
</Frame>

Enter Client ID and Client Secret generated into Rootly:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/TIlGh9cK2EiEJpcz/images/integrations/quip/images-4.webp?fit=max&auto=format&n=TIlGh9cK2EiEJpcz&q=85&s=119260c8999c33020a41bcc748ccd35c" width="886" height="934" data-path="images/integrations/quip/images-4.webp" />
</Frame>

You are all set! Go under workflow to configure your new task!


Built with [Mintlify](https://mintlify.com).