# Source: https://pipedream.com/docs/components/contributing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pipedream Registry

When developing workflows with pre-built actions and triggers, under the hood you’re using [components](/components/contributing/) from the [Pipedream Registry GitHub repository](https://github.com/PipedreamHQ/pipedream).

Components contributed to the [Pipedream Registry GitHub repository](https://github.com/PipedreamHQ/pipedream) are published to the [Pipedream marketplace](https://pipedream.com/apps) and are listed in the Pipedream UI when building workflows.

<Note>
  What is a component?

  If you haven’t yet, we recommend starting with our Component Development Quickstart Guides for [sources](/components/contributing/sources-quickstart/) and [actions](/components/contributing/actions-quickstart/) to learn how to build components and privately publish them to your account.
</Note>

## Registry Components Structure

All Pipedream registry components live in [this GitHub repo](https://github.com/PipedreamHQ/pipedream) under the [`components`](https://github.com/PipedreamHQ/pipedream/tree/master/components) directory.

Every integrated app on Pipedream has a corresponding directory that defines the actions and sources available for that app. Below is a simplified version of the [Airtable app directory](https://github.com/PipedreamHQ/pipedream/tree/master/components/airtable) within the registry:

🗁 airtable<br />
  🗎 README.md<br />
  🗎 airtable.app.mjs<br />
  🗎 package.json<br />
  🗁 actions<br />
    🗁 get-record<br />
      🗎 get-record.mjs<br />
  🗁 node\_modules<br />
    🗎 ...here be dragons<br />
  🗁 sources<br />
    🗁 new-records<br />
      🗎 new-records.mjs<br />

In the example above, the `components/airtable/actions/get-record/get-record.mjs` component is published as the **Get Record** action under the **Airtable** app within the workflow builder in Pipedream.

<Note>
  The repository is missing the app directory I’d like to add components for

  You can request to have new apps integrated into Pipedream.

  Once the Pipedream team integrates the app, we’ll create a directory for the app in the [`components`](https://github.com/PipedreamHQ/pipedream/tree/master/components) directory of the GitHub repo.
</Note>

## Contribution Process

Anyone from the community can build [sources](/workflows/building-workflows/triggers/) and [actions](/components/contributing/#actions) for integrated apps.

To submit new components or update existing components:

1. Fork the public [Pipedream Registry GitHub repository](https://github.com/PipedreamHQ/pipedream).
2. Create a new component within the corresponding app’s directory within the `components` directory (if applicable).
3. [Create a PR for the Pipedream team to review](https://github.com/PipedreamHQ/pipedream/compare).
4. Address any feedback provided by Pipedream based on the best practice [Component Guidelines & Patterns](/components/contributing/guidelines/).
5. Once the review is complete and approved, Pipedream will merge the PR to the `master` branch
6. The component will be available for use within workflows for all Pipedream developers! 🎉

### Component Development Discussion

Join the discussion with other Pipedream component developers at the [#contribute channel](https://pipedream-users.slack.com/archives/C01E5KCTR16) in Slack or [on Discourse](https://pipedream.com/community/c/dev/11).

<Note>
  Not sure what to build?

  Need inspiration? Check out [sources](https://github.com/PipedreamHQ/pipedream/issues?q=is%3Aissue+is%3Aopen+%5BSOURCE%5D+in%3Atitle) and [actions](https://github.com/PipedreamHQ/pipedream/issues?q=is%3Aissue+is%3Aopen+%5BACTION%5D+in%3Atitle+) requested by the community!
</Note>

## Reference Components

The following components are references for developing sources and actions for Pipedream’s registry.

### Reference Sources

| Name                                                                                                                                                          | App          | Type                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------- |
| [New Card](https://github.com/PipedreamHQ/pipedream/blob/master/components/trello/sources/new-card/new-card.mjs)                                              | Trello       | Webhook                          |
| [New or Modified Files](https://github.com/PipedreamHQ/pipedream/blob/master/components/google_drive/sources/new-or-modified-files/new-or-modified-files.mjs) | Google Drive | Webhook + Polling                |
| [New Submission](https://github.com/PipedreamHQ/pipedream/blob/master/components/jotform/sources/new-submission/new-submission.mjs)                           | Jotform      | Webhook (with no unique hook ID) |

### Reference Actions

| Name                                                                                                                                               | App           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [Add Multiple Rows](https://github.com/PipedreamHQ/pipedream/blob/master/components/google_sheets/actions/add-multiple-rows/add-multiple-rows.mjs) | Google Sheets |
| [Send Message](https://github.com/PipedreamHQ/pipedream/blob/master/components/discord_bot/actions/send-message/send-message.mjs)                  | Discord       |
| [Append Text](https://github.com/PipedreamHQ/pipedream/blob/master/components/google_docs/actions/append-text/append-text.mjs)                     | Google Docs   |
| [`GET` request](https://github.com/PipedreamHQ/pipedream/blob/master/components/http/actions/get-request/get-request.mjs)                          | HTTP          |

Built with [Mintlify](https://mintlify.com).
