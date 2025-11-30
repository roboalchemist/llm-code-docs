# Source: https://dagshub.com/docs/integration_guide/jenkins/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/jenkins.md "Edit this page")

# Jenkins[¶](#jenkins "Permanent link")

[Jenkins](https://www.jenkins.io/) is the most popular and mature open source tool for CI/CD and automation, and it\'s also usable for automating Data Science and Machine Learning workflows.

DagsHub has an [official Jenkins plugin](https://plugins.jenkins.io/dagshub-branch-source/) that you can use to automatically scan your DagsHub repos, and execute custom pipelines on each:

- Git branch push
- Git tag creation
- Pull request

## How to install Jenkins plugin for DagsHub?[¶](#how-to-install-jenkins-plugin-for-dagshub "Permanent link")

Just go to your Jenkins\' plugin management UI, and search for DagsHub. The plugin should be listed as \"Available\", and you can just install it.

To use it:

1.  Create a new [Multibranch Pipeline Project](https://plugins.jenkins.io/workflow-multibranch/)
2.  Select DagsHub as a branch source [![DagsHub branch source](../assets/jenkins/dagshub-branch-src.png)](../assets/jenkins/dagshub-branch-src.png)
3.  (Optional) If the repo is private, you need to supply Jenkins with credentials to access it. We suggest [using an access token](https://DagsHub.com/user/settings/tokens).
4.  Input your repo URL, e.g.: `https://dagshub.com/username/reponame`
5.  Select the behaviors you want - whether to build on all branch pushes, only pull requests, etc. All behaviors supported by the DagsHub plugin start with the word `(DagsHub)` for your convenience.

[![DagsHub branch source settings](../assets/jenkins/dagshub-branch-src-settings.png)](../assets/jenkins/dagshub-branch-src-settings.png)

## How to automatically trigger builds using webhooks?[¶](#how-to-automatically-trigger-builds-using-webhooks "Permanent link")

The DagsHub plugin currently doesn\'t automatically install any webhook on the repo for you. This means new builds won\'t run after pushing branches etc. until you manually trigger a branch scan in the Jenkins project.

To solve this, you can:

1.  Install the [Multibranch Scan Webhook Trigger Jenkins plugin](https://plugins.jenkins.io/multibranch-scan-webhook-trigger/)
2.  Configure the \"Scan Multibranch Pipeline Triggers\" - activate the \"Scan by webhook\" option
3.  Choose a secret token\
    [![Jenkins multibranch webhook trigger](../assets/jenkins/multibranch-webhook-trigger.png)](../assets/jenkins/multibranch-webhook-trigger.png)
4.  Copy the URL: `https://YOUR-JENKINS-SERVER/multibranch-webhook-trigger/invoke?token=[YOUR-TRIGGER-TOKEN]`, replace the server address and trigger token.
5.  Go to your DagsHub repo\'s webhook settings screen, e.g. https://dagshub.com/username/reponame/settings/hooks
6.  Click on \"Add Webhook\" then choose the \"DagsHub\" hook type\
    [![DagsHub webhook creation](../assets/jenkins/dagshub-webhook.png)](../assets/jenkins/dagshub-webhook.png)
7.  Define the Jenkins webhook URL from the previous steps, and chosoe the event types which should trigger it. The recommended set is marked in the following screenshot:\
    [![DagsHub webhook definition](../assets/jenkins/dagshub-webhook-definition.png)](../assets/jenkins/dagshub-webhook-definition.png)
8.  Click on \"Add Webhook\".\
    Now, whenever a branch or pull request is created/updated/deleted, Jenkins will receive a notification, rescan your project and trigger any required builds.

## Jenkins Examples[¶](#jenkins-examples "Permanent link")

If you\'re looking for examples on how to create ML automations with Jenkins, check out this article series written by one of our community members:

- [Part 1](https://dagshub.com/blog/cml-with-jenkins-in-dagshub/) is a high level overview of how Jenkins can be used in an ML project setting.
- [Part 2](https://dagshub.com/blog/in-depth-tour-of-jenkinsfile/) is an in depth guide into creating an ML project with Jenkins, where models are automatically trained when new code versions are pushed to DagsHub.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).