# Source: https://docs.rootly.com/integrations/zoom/installation.md

# Source: https://docs.rootly.com/integrations/webex/installation.md

# Source: https://docs.rootly.com/integrations/trello/installation.md

# Source: https://docs.rootly.com/integrations/slack/installation.md

# Source: https://docs.rootly.com/integrations/service-now/installation.md

# Source: https://docs.rootly.com/integrations/pagerduty/installation.md

# Source: https://docs.rootly.com/integrations/new-relic/installation.md

# Source: https://docs.rootly.com/integrations/linear/installation.md

# Source: https://docs.rootly.com/integrations/jira/installation.md

# Source: https://docs.rootly.com/integrations/google-meet/installation.md

# Source: https://docs.rootly.com/integrations/google-docs/installation.md

# Source: https://docs.rootly.com/integrations/google-calendar/installation.md

# Source: https://docs.rootly.com/integrations/generic-webhook-alert-source/installation.md

# Source: https://docs.rootly.com/integrations/dropbox-paper/installation.md

# Source: https://docs.rootly.com/integrations/datadog/installation.md

# Source: https://docs.rootly.com/integrations/confluence/installation.md

# Source: https://docs.rootly.com/integrations/coda/installation.md

# Source: https://docs.rootly.com/integrations/clickup/installation.md

# Source: https://docs.rootly.com/integrations/backstage/installation.md

# Source: https://docs.rootly.com/integrations/asana/installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation

> Install and configure the Asana integration to automatically create tasks from Rootly incidents and action items.

## Why

**Asana** Integration allows you to:

* Creating an incident in **Rootly** will create a task in **Asana** if you choose to.
* Creating an action item in **Rootly** will create a task in **Asana** if you choose to. Attached as **subtasks** if incident has been created in **Asana** as well.
* **Changing** incident **title, description,** **status** in **Rootly** will update the task in **Asana.**
* **Changing** action item **title, description,** **status** in **Rootly** will update the task in **Asana.**
* **Changing** Asana incident issue attributes **will not** update incident attributes in **Rootly**.
* **Changing** Asana action item issue status **will not** update action item status in **Rootly**. ( Coming soon )

## Installation

You can setup this integration as a **logged in admin user** in the integrations page:

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/yHcXrOapKHrppc-2/images/integrations/asana/installation/installation-1.webp?fit=max&auto=format&n=yHcXrOapKHrppc-2&q=85&s=51d16a4f4af07125ef54411a19bd0b1c" width="868" height="393" data-path="images/integrations/asana/installation/installation-1.webp" />
</Frame>

<Note>
  We recommend integrating with a **service account** to make sure the integration doesn't break if a user leaves your company.
</Note>

## Settings

You can specify which **workspace** and what **project** you want to create tasks in

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/yHcXrOapKHrppc-2/images/integrations/asana/installation/installation-2.webp?fit=max&auto=format&n=yHcXrOapKHrppc-2&q=85&s=c93326552eafde3861b9829c82721704" width="871" height="682" data-path="images/integrations/asana/installation/installation-2.webp" />
</Frame>

## Uninstall

You can **uninstall** this integration in the integrations panel by clicking **Configure > Delete**


Built with [Mintlify](https://mintlify.com).