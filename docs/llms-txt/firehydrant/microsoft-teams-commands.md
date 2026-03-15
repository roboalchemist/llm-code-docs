# Source: https://docs.firehydrant.com/docs/microsoft-teams-commands.md

# Microsoft Teams Commands

The FireHydrant Microsoft Teams bot allows your responders to conduct incidents from end to end without leaving their chat app. Microsoft Teams features 'Tabs,' a flexible web interface that can be added to any chat or channel. FireHydrant's bot introduces a Command Center tab, designed to mirror many of the capabilities of the FireHydrant web UI and provide a familiar interface.

Incident actions may be available through Tab UI, as direct commands typed into the incident channel's chat/posts, or both. All chat commands start with`@FireHydrant`.

## Non-Licensed Users

Non-licensed users (e.g., don't have FireHydrant accounts) by default cannot interact with the FireHydrant MS Teams bot. However, a licensed user can run `@FireHydrant add bot token`. This sets an API key for the bot, and this will allow non-licensed users to execute only a basic subset of commands like `new` or `help`. For more information, see [Enabling non-licensed users to declare incidents](https://docs.firehydrant.com/docs/microsoft-teams-integration#enabling-non-licensed-users-to-declare-incidents).

## General Actions

General actions are actions or commands you can run outside of an incident channel and are not contextually tied to a specific incident.

| Action                                                    | Command                        | Available in Tab? | Unlicensed User Accessible? |
| :-------------------------------------------------------- | :----------------------------- | :---------------- | :-------------------------- |
| **Add Bot Token**                                         | `@FireHydrant add bot token`   | -                 | ❌                           |
| **Help/List Commands**                                    | `@FireHydrant help`            | -                 | ✅                           |
| **Login**                                                 | `@FireHydrant login`           | -                 | ❌                           |
| **Logout**                                                | `@FireHydrant logout`          | -                 | ❌                           |
| **[New Incident](https://docs.firehydrant.com/docs/starting-incidents)**                | `@FireHydrant new`             | -                 | ✅                           |
| **[New Retroactive Incident](https://docs.firehydrant.com/docs/retroactive-incidents)** | `@FireHydrant create-resolved` | -                 | ✅                           |
| **Tutorial**                                              | `@FireHydrant tutorial`        | -                 | ❌                           |

## Incident Actions

Incident actions must be taken within the context of an incident channel, whether as a chat command or using the attached Tab. We further split incident actions into multiple categories to make it easier to organize them.

**Currently, no incident actions can be run by unlicensed users.**

### Details and Updates

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Command
      </th>

      <th>
        Available in Tab?
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **[Edit Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields)**
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Edit Incident Fields](https://docs.firehydrant.com/docs/incident-fields)**
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Environments](https://docs.firehydrant.com/docs/intro-to-service-catalog)**\
        **[Functionalities](https://docs.firehydrant.com/docs/intro-to-service-catalog)**\
        **[Services](https://docs.firehydrant.com/docs/intro-to-service-catalog)**
      </td>

      <td>
        `@FireHydrant add service`\
        `@FireHydrant add functionality`\
        `@FireHydrant add environment`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        \*\*[External Links (Add/Edit)](https://docs.firehydrant.com/docs/adding-external-links) \*\*
      </td>

      <td>
        `@FireHydrant add external-link`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Labels (Add/Edit)](https://docs.firehydrant.com/docs/incident-labels)**
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Related Incidents](https://docs.firehydrant.com/docs/related-incidents)**
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        \*\*[Resolve](https://docs.firehydrant.com/docs/resolving-incidents) \*\*
      </td>

      <td>
        `@FireHydrant resolve`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Runbooks (Add/View)](https://docs.firehydrant.com/docs/introduction-to-runbooks)**\
        **Retry Runbook Steps**
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Starring Images](https://docs.firehydrant.com/docs/incident-timeline)**
      </td>

      <td>
        * Go to message > ellipses > more actions > Star/Unstar message
      </td>

      <td />
    </tr>

    <tr>
      <td>
        **[Start Retro](https://docs.firehydrant.com/docs/conducting-retrospectives)**
      </td>

      <td>
        `@FireHydrant start retro`
      </td>

      <td>
        ✅ (after resolved)
      </td>
    </tr>

    <tr>
      <td>
        \*\*[Status Pages](https://docs.firehydrant.com/docs/external-status-pages) \*\*
      </td>

      <td>
        `@FireHydrant add status-page`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        \*\*[Tags (Add/Edit)](https://docs.firehydrant.com/docs/incident-tags) \*\*
      </td>

      <td>
        *
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Summary (AI)](https://docs.firehydrant.com/docs/ai-powered-incident-summaries)**
      </td>

      <td>
        `@FireHydrant summary`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        **[Update](https://docs.firehydrant.com/docs/posting-updates)**
      </td>

      <td>
        `@FireHydrant update`
      </td>

      <td>
        ✅
      </td>
    </tr>
  </tbody>
</Table>

### Personnel and Teams

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action
      </th>

      <th>
        Command
      </th>

      <th>
        Available in Tab?
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        \*\*[Assign Role](https://docs.firehydrant.com/docs/incident-roles)&#x20;**&#xA;**[Update Roles](https://docs.firehydrant.com/docs/incident-roles) \*\*
      </td>

      <td>
        `@FireHydrant assign role`\
        `@FireHydrant update roles`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        \*\*[Assign Team](https://docs.firehydrant.com/docs/team-management) \*\*
      </td>

      <td>
        `@FireHydrant assign team`
      </td>

      <td>
        ✅
      </td>
    </tr>

    <tr>
      <td>
        \*\*[On-Call Lookup (3rd-Party)](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) \*\*
      </td>

      <td>
        `@FireHydrant oncall`
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        \*\*[On-Call Lookup (Signals)](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)  \*\*
      </td>

      <td>
        `@FireHydrant signals-on-call`
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        **[Page](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `@FireHydrant page`
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        \*\*[Page a Functionality](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) \*\*
      </td>

      <td>
        `@FireHydrant page functionality`
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        **[Page a Service](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `@FireHydrant page service`
      </td>

      <td>
        *
      </td>
    </tr>

    <tr>
      <td>
        **[Page a Team](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)**
      </td>

      <td>
        `@FireHydrant page team`
      </td>

      <td>
        *
      </td>
    </tr>
  </tbody>
</Table>

### Task Management

| Action                                               | Command                      | Available in Tab? |
| :--------------------------------------------------- | :--------------------------- | :---------------- |
| **[Follow-Ups (Add/Edit)](https://docs.firehydrant.com/docs/managing-follow-ups)** | `@FireHydrant add follow-up` | ✅                 |
| **[Tasks (Add/Edit)](https://docs.firehydrant.com/docs/managing-tasks)**           | `@FireHydrant add task`      | ✅                 |
| **[Task Lists (Add)](https://docs.firehydrant.com/docs/managing-tasks)**           | -                            | ✅                 |