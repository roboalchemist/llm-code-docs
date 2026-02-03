# Source: https://developers.notion.com/page/examples.md

# Source: https://developers.notion.com/guides/resources/examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

## Introductory

<CardGroup cols={2}>
  <Card color="#0076d7" title="Create a Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/1-add-block.ts" icon="github" cta="See sample code">
    In this introductory codebase, start by learning the basics of Notion's Public API: creating a new block.
  </Card>

  <Card color="#0076d7" title="Create a linked Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/2-add-linked-block.ts" icon="github" cta="See sample code">
    Build on the previous example by creating a block in Notion and adding a link to it.
  </Card>

  <Card color="#0076d7" title="Create a styled/linked Notion block" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/basic/3-add-styled-block.ts" icon="github" cta="See sample code">
    Extend the previous example further by styling a block of text that links to an external website.
  </Card>

  <Card color="#0076d7" title="Get text from any type of block" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/parse-text-from-any-block-type" icon="github" cta="Fork repository on GitHub">
    This integration shows how to get a list of blocks from a Notion page and parse the text from any type of block.
  </Card>
</CardGroup>

## Intermediate

<CardGroup cols={2}>
  <Card color="#0076d7" title="Create a Notion database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/1-create-a-database.ts" icon="github" cta="See sample code">
    Create your first Notion database with a defined set of properties.
  </Card>

  <Card color="#0076d7" title="Add new pages to a database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/2-add-page-to-database.ts" icon="github" cta="See sample code">
    Build on the previous example by creating a database and adding new pages to it.
  </Card>

  <Card color="#0076d7" title="Query pages in a database" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/3-query-database.ts" icon="github" cta="See sample code">
    Learn how to filter your database rows (pages) after creating them from scratch.
  </Card>

  <Card color="#0076d7" title="Filter and sort database pages" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/4-sort-database.ts" icon="github" cta="See sample code">
    Filter and sorts pages after adding them to a new database.
  </Card>

  <Card color="#0076d7" title="Upload files to a page" href="https://github.com/makenotion/notion-cookbook/blob/main/examples/javascript/intro-to-notion-api/intermediate/5-upload-file.ts" icon="github" cta="See sample code">
    Create, send, and attach a file upload to a page's contents and as a comment attachment.
  </Card>

  <Card color="#0076d7" title="Build a full-stack Notion integration" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/web-form-with-express" icon="github" cta="Fork repository on GitHub">
    Learn how to build a Notion integration with an interactive front-end. This codebase is referenced in the [Build your first integration guide](/guides/get-started/create-a-notion-integration).
  </Card>
</CardGroup>

## Advanced

<CardGroup cols={2}>
  <Card color="#0076d7" title="Sync Spotify Playlists with Notion" href="/guides/tutorials/spotify" icon="book" cta="See guide here">
    This integration populates a Notion database with track metadata from a Spotify playlist.
  </Card>

  <Card color="#0076d7" title="Integrate Mailchimp Campaigns with Notion" href="/guides/tutorials/integrate-mailchimp-campaigns-with-notion-databases" icon="book" cta="See guide here">
    This integration populates a Notion database with Mailchimp campaign information, including subscriber contact information.
  </Card>

  <Card color="#0076d7" title="Log Strava Activity in Notion" href="/guides/tutorials/log-strava-activity-in-notion" icon="book" cta="See guide here">
    This integration syncs a Strava athlete's activity metadata within a Notion database.
  </Card>

  <Card color="#0076d7" title="Add rows (pages) to an existing database" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/generate-random-data" icon="github" cta="Fork repository on GitHub">
    This integration finds the first database that your bot has access to, and creates correctly-typed random rows of data.
  </Card>

  <Card color="#0076d7" title="Sync Notion with GitHub issues" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/notion-github-sync" icon="github" cta="Fork repository on GitHub">
    This Notion integration syncs GitHub Issues for a specific repo to a Notion database. This example shows a one-way sync — changes in GitHub cause an update in Notion.
  </Card>

  <Card color="#0076d7" title="Send an email from a Notion trigger" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/database-email-update" icon="github" cta="Fork repository on GitHub">
    This Notion integration sends an email whenever the *Status* property of a page in a database is updated. This sample shows how to use Notion to cause an external action. In this case, the integration sends emails using SendGrid's API.
  </Card>

  <Card color="#0076d7" title="Sync Notion with GitHub PRs" href="https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/notion-task-github-pr-sync" icon="github" cta="Fork repository on GitHub">
    This Notion integration updates Notion tasks when a linked Github PR is closed/merged. This integration requires the Notion task link be mentioned in the PR description.
  </Card>
</CardGroup>
