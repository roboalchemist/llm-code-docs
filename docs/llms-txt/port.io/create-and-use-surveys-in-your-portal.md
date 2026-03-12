# Source: https://docs.port.io/guides/all/create-and-use-surveys-in-your-portal.md

# Create & use surveys in your portal

[YouTube video player](https://www.youtube.com/embed/TJo0FXoEIiE)

<br />

This guide will walk you through the setup and use of surveys in your portal.

We will learn how to configure a survey, collect responses, and view feedback insights from developers to drive engineering improvements.

## Overview[â](#overview "Direct link to Overview")

Surveys help you gather direct, valuable feedback from developers across your organization.<br /><!-- -->Port allows you to run surveys and view their results in your portal, allowing for:

* Easy survey setup from templates.
* A convenient way to publish developer surveys to Port users.
* A familiar way for Port users to respond to surveys.
* A response pipeline that feeds insights into a dashboard.

### New components[â](#new-components "Direct link to New components")

When you set up a survey, Port automatically creates the following components to enable survey distribution and feedback collection:

#### Blueprints

These blueprints model the survey data and are only created the first time you install a survey:

`Survey Template` â Defines the structure of a survey that can be reused multiple times.

`Survey` â Represents each **instance** of a survey template.

`Question Template` â Defines reusable question formats like "text" or "selection".

`Question` â Contains the actual questions being asked in a particular survey.

`Response` â Stores individual survey responses submitted by users.

![](/img/guides/surveyBlueprints.png)

<br />

<br />

#### Self-service action

A self-service action will be created for each survey instance.

<br />

<!-- -->

This action allows developers to respond to the survey.

You can control who can respond to the survey via the action's permissions.

#### Dashboard page

Visualizes survey submissions and aggregates trends in developer sentiment.

#### Additional resources

To capture responses, the experience also includes a webhook data source that ingests survey responses when submitted via the self-service action.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

To set up surveys in your portal, you will need admin permissions in your portal.

Once you have set up one or more surveys, you will need:

* A communication channel (e.g., Slack, email) to distribute survey links.
* Clarity on who should respond (teams, roles, or org-wide).

## Set up a survey[â](#set-up-a-survey "Direct link to Set up a survey")

1. Go to your [software catalog](https://app.getport.io/organization/catalog).

2. Click on the `+ New` button in the left sidebar, then choose `New experience`.

3. In the modal, choose `New Survey`.

4. Choose a survey type and give it a unique identifier (this will allow you to run this survey multiple times and track its results over time).

   ![](/img/guides/surveyChooseName.png)

5. To finish, click `Create`.

## Configure & distribute the survey[â](#configure--distribute-the-survey "Direct link to Configure & distribute the survey")

1. **Adjust Survey Visibility:**

   * Go to the [self-service](https://app.getport.io/self-serve) page of your portal.
   * Find the survey, then click the `...` button and select `Edit`.
   * Go to the `Permissions` tab and configure who can respond to the survey (i.e. who can execute this action).

2. **Distribute the Survey:**

   * Hover over the action card, then click on the chain icon to copy the link to the survey.

     ![](/img/guides/surveyCopyActionLink.png)

   * Share the link with your team via Slack, email, or other internal channels.

## View results[â](#view-results "Direct link to View results")

Navigate to the survey dashboard created in the "Surveys" folder in your [software catalog](https://app.getport.io/organization/catalog).

Once responses are submitted, you'll see developer sentiment and trends visualized in real time.

![](/img/guides/surveySeeSurveyDashboard.png)

<br />

<br />

These insights help platform and engineering teams understand friction points, monitor developer experience, and prioritize where to invest future resources.
