---
id: Sentry
title: Sentry
---
Sentry is an open-source error tracking that helps developers monitor and fix crashes in real time. To integrate Sentry with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Sentry integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Sentry" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Sentry

1. Log in to your Sentry account. Go to "Project Settings".
2. Click the "Settings" tab from the left hand menu.
3. Click on "Webhooks" under "Legacy Integrations".
4. Paste the webhooks url you copied earlier under "Callback URLs".

![](/img/Integrations/Sentry/1.png)

1. Click "Save".
2. Zenduty will create incidents whenever Sentry detects an error.
