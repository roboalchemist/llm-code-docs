# Source: https://developers.openai.com/apps-sdk/deploy/submission.md

# Submit your app

## App submission overview

Once you have built and [tested your app](https://developers.openai.com/apps-sdk/deploy/testing) in Developer Mode, you can submit your app to the ChatGPT Apps Directory to make it publicly available.

Only submit your app if you intend for it to be accessible to all users. Submitting an app initiates a review process, and you’ll be notified of its status as it moves through review.



Before submitting, make sure your app complies with our [App Submission
  Guidelines](https://developers.openai.com/apps-sdk/app-submission-guidelines).



If your app is approved, it can be listed in the ChatGPT Apps Directory.
Initially, users will be able to discover your app in one of the following ways:

- By clicking a direct link to your app in the directory
- By searching for your app by name

Apps that demonstrate strong real-world utility and high user satisfaction may be eligible for enhanced distribution opportunities—such as directory placement or proactive suggestions.

## Pre-requisites

### Organization verification

Your organization needs to be verified on the OpenAI Platform to be able to submit an app.

You can complete individual or business verification in the [OpenAI Platform Dashboard general settings](https://platform.openai.com/settings/organization/general). Once you’ve verified the profile you plan to publish under, that identity will be available to pick during app submission.

### Owner role

You must have the **Owner** role in an organization to complete verification and create and submit apps for review.

If you aren’t currently an Owner, your organization’s current owners will need to grant you this role to proceed.

## Submission process

If the pre-requisites are met, you can submit your app for review from the [OpenAI Platform Dashboard](http://platform.openai.com/apps-manage).

### MCP server requirements

- Your MCP server is hosted on a publicly accessible domain
- You are not using a local or testing endpoint
- You defined a [CSP](https://developers.openai.com/apps-sdk/build/mcp-server#content-security-policy-csp) to allow the exact domains you fetch from (this is required to submit your app for security reasons)

### Start the review process

From the dashboard:

1. Add your MCP server details (as well as OAuth metadata if OAuth is selected)
2. Confirm that your app complies with OpenAI policies.
3. Complete the required fields in the submission form and check all confirmation boxes.
4. Click **Submit for review**.

Once submitted, your app will enter the review queue.

While you can publish multiple, unique apps within a single Platform organization, each may only have one version in review at a time.



Note that for now, projects with EU data residency cannot submit apps for
  review. Please use a project with global data residency to submit your apps.
  If you don't have one, you can create a new project in your current
  organization from the OpenAI Dashboard.



## After Submission

You can review the status of the review within the Dashboard and will receive an email notification informing you of any status changes.

### Publish your app

Once your app is approved, you can publish it to the ChatGPT Apps Directory by clicking the **Publish** button in the Dashboard.
This will make your app discoverable by ChatGPT users.

### Reviews and checks

We may perform automated scans or manual reviews to understand how your app works and whether it may conflict with our policies. If your app is rejected or removed, you will receive feedback and may have the opportunity to appeal.

### Maintenance and removal

Apps that are inactive, unstable, or no longer compliant may be removed. We may reject or remove any app from our services at any time and for any reason without notice, such as for legal or security concerns or policy violations.

### Re-submission for changes

Once your app is published, tool names, signatures, and descriptions are locked for safety. To add or update your app’s tools or metadata, you must resubmit the app for review. Once your resubmission is approved, you can publish the update which will replace the previous version of your app.