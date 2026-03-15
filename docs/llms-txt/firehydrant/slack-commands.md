# Source: https://docs.firehydrant.com/docs/slack-commands.md

# Slack Commands

Running incidents and executing Runbooks can be done directly in Slack, where your team is already accustomed to working. This article details the complete list of FireHydrant bot's Slack commands.

Multiple command aliases can be used to execute FireHydrant Slack bot commands:

* **/fh**
* **/firehydrant**
* **/incident**

For this article, we will utilize `/fh`.

Specific commands can be run anywhere, while others can only be run in an active incident channel. We will denote these contexts as **general** vs. **incident** commands.

## General Commands

These commands can be run anywhere within Slack and at any time, **including within incident channels.**

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Command + Notes
      </th>

      <th>
        **Unlicensed User Accessible?**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Help**
      </td>

      <td>
        `/fh`

        `/fh help`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **Browse alerts**
      </td>

      <td>
        `/fh alerts`

        **Note**: While unlicensed users can see the list of alerts and their descriptions from within Slack, they won't be able to access the FireHydrant web UI to view additional details.
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **Enable Beta Features**
      </td>

      <td>
        `/fh beta`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Search Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog)**
      </td>

      <td>
        `/fh catalog`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **Manage Channel Settings**
      </td>

      <td>
        `/fh channel`

        **Note:** Use to configure settings for the specific channel you run this command in. Can be used to configure [Triage Channels in Slack](https://docs.firehydrant.com/docs/triage-channels-in-slack)  and other team-specific settings, if the channel is associated with a specific team.
      </td>

      <td>
        ✅ (read only)
      </td>
    </tr>

    <tr>
      <td>
        **[Ask for On-Call Coverage](https://docs.firehydrant.com/docs/signals-on-call-schedules)**
      </td>

      <td>
        `/fh cover me`

        **Note:** For [FireHydrant's Signals](https://docs.firehydrant.com/docs/signals-introduction)  only. 3rd-party tools should handle coverage requests in their respective tool
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[New Retroactive Incident](https://docs.firehydrant.com/docs/retroactive-incidents)**
      </td>

      <td>
        `/fh create-resolved`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Link](https://docs.firehydrant.com/docs/slack-integration)**
      </td>

      <td>
        `/fh link`

        **Note:** FireHydrant will attempt to link users automatically, but this command exists as a fallback in case auto-linking fails
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **List/search incidents**
      </td>

      <td>
        `/fh list`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[New Incident](https://docs.firehydrant.com/docs/starting-incidents)**
      </td>

      <td>
        `/fh new`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[On-Call Lookup (Signals)](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `/fh signals-on-call`

        **Note:** This applies specifically to on-call lookup for [Signals](https://docs.firehydrant.com/docs/signals-introduction). In order for Unlicensed users/guests to run this command, an <Glossary>Owner</Glossary> will need to enable this setting in **Settings** > **Integration List** > **Slack** > **Configuration** > **Allow guests to view on-call schedules?**
      </td>

      <td>
        ✅\*\*
      </td>
    </tr>

    <tr>
      <td>
        **[On-Call Lookup (3rd-party)](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `/fh oncall`

        `/fh on-call`

        **Note:** These commands apply for services and functionalities [linked to 3rd-party alerting providers](https://docs.firehydrant.com/docs/import-and-link-components) . For Signals, use `/fh signals-on-call`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Paging](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `/fh page`

        `/fh page [service] [service name]` \*\*

        `/fh page [functionality] [functionality name]` \*\*

        \*\***Note:** These commands apply for services and functionalities [linked to 3rd-party alerting providers](https://docs.firehydrant.com/docs/import-and-link-components) . For Signals, use `/fh page`.
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Service Lookup](https://docs.firehydrant.com/docs/intro-to-service-catalog)**
      </td>

      <td>
        `/fh service [service name]`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **Manage General Slack Settings**
      </td>

      <td>
        `/fh settings`

        **Note:** Use to configure how alerts and notifications look when posted into channels. These settings apply across all Slack channels.
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Switch Organization](https://docs.firehydrant.com/docs/organizations)**
      </td>

      <td>
        `/fh switch org`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Tutorial](https://docs.firehydrant.com/docs/tutorial-runbooks)**
      </td>

      <td>
        `/fh tutorial`
      </td>

      <td>
        ❌
      </td>
    </tr>
  </tbody>
</Table>

## Incident Commands

These are **incident commands** that can only be run inside an incident channel created by FireHydrant.

### Details and Updates

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Command + Notes
      </th>

      <th>
        **Unlicensed User Accessible?**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **[Add Link](https://docs.firehydrant.com/docs/adding-external-links)**
      </td>

      <td>
        `/fh add link`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **Add Environment**
        **Add Functionality**
        **Add Service**
      </td>

      <td>
        `/fh add environment`

        `/fh add functionality`

        `/fh add service`

        `/fh add impact`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Add Status Page](https://docs.firehydrant.com/docs/external-status-pages)**
      </td>

      <td>
        `/fh add status-page`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **Edit Details**
      </td>

      <td>
        `/fh edit`

        `/fh tags`

        `/fh add tags`

        **Note:** The `/fh edit` command respects existing required fields and supports custom field values in the edit modal.
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Related Incidents](https://docs.firehydrant.com/docs/related-incidents)**
      </td>

      <td>
        `/fh related incidents`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Resolve](https://docs.firehydrant.com/docs/resolving-incidents)**
      </td>

      <td>
        `/fh resolve`

        **Note:** Takes you to the same screen as `/fh update`, but with milestone preset to "Resolved"
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Restrict Incident](https://docs.firehydrant.com/docs/private-incidents)**
      </td>

      <td>
        `/fh restrict`
        `/fh private`

        **Note:** You must have `Access Private Incidents` permission to complete this command.
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[View Runbooks](https://docs.firehydrant.com/docs/runbook-basics)**
      </td>

      <td>
        `/fh runbooks`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Add Runbooks](https://docs.firehydrant.com/docs/runbook-basics)**
      </td>

      <td>
        `/fh add runbook`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Start Retro](https://docs.firehydrant.com/docs/conducting-retrospectives)**
      </td>

      <td>
        `/fh start retro`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **View Incident Status/Details**
      </td>

      <td>
        `/fh status`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Manage Status Pages](https://docs.firehydrant.com/docs/external-status-pages)**
      </td>

      <td>
        `/fh status-pages`
      </td>

      <td>
        ✅ (read only)
      </td>
    </tr>

    <tr>
      <td>
        **[Summary](https://docs.firehydrant.com/docs/ai-powered-incident-summaries)**
      </td>

      <td>
        `/fh summary`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Update](https://docs.firehydrant.com/docs/posting-updates)**
      </td>

      <td>
        `/fh update`

        `/fh add note`

        `/fh post`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Invite Scribe to Zoom Bridge](https://docs.firehydrant.com/docs/runbook-step-invite-scribe-to-zoom-meeting)**
      </td>

      <td>
        `/fh scribe`
      </td>

      <td>
        ❌
      </td>
    </tr>
  </tbody>
</Table>

### Personnel and Teams

| Action                                    | Command + Notes    | **Unlicensed User Accessible?** |
| :---------------------------------------- | :----------------- | :------------------------------ |
| **[Assign Role](https://docs.firehydrant.com/docs/adding-responders)**  | `/fh assign role`  | ❌                               |
| **[Assign Team](https://docs.firehydrant.com/docs/adding-responders)**  | `/fh assign team`  | ❌                               |
| **Handoff Role**                          | `/fh handoff`      | ❌                               |
| **[Update Roles](https://docs.firehydrant.com/docs/adding-responders)** | `/fh update roles` | ❌                               |

### Task Management

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Command + Notes
      </th>

      <th>
        **Unlicensed User Accessible?**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **[Add Follow-up](https://docs.firehydrant.com/docs/managing-follow-ups)**
      </td>

      <td>
        `/fh add follow-up`

        `/fh add followup`

        `/fh follow-up`

        `/fh followup`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Add Task](https://docs.firehydrant.com/docs/managing-tasks)**
      </td>

      <td>
        `/fh add task`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[Add Task List](https://docs.firehydrant.com/docs/managing-tasks)**
      </td>

      <td>
        `/fh add task-list`
      </td>

      <td>
        ❌
      </td>
    </tr>

    <tr>
      <td>
        **[View Follow-ups](https://docs.firehydrant.com/docs/managing-follow-ups)**
      </td>

      <td>
        `/fh follow-ups`
      </td>

      <td>
        ✅ (read only)
      </td>
    </tr>

    <tr>
      <td>
        **[View Tasks](https://docs.firehydrant.com/docs/managing-tasks)**
      </td>

      <td>
        `/fh tasks [@user | all]`
      </td>

      <td>
        ✅
      </td>
    </tr>
  </tbody>
</Table>

## Custom Commands

In FireHydrant, you can create custom commands that return templated replies or make HTTP requests to external systems. If you have any custom commands, they will also appear on the command list when you run `/fh help`.

To learn more, see [Command Extensions](https://docs.firehydrant.com/docs/command-extensions).