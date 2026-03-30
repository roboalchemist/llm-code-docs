# Source: https://docs.xano.com/building-backend-features/custom-report-generation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Report Generation

## Report Generation using Database Views

Xano offers an easy way to share read-only views of your database tables. If the data is already presented in a readable format, you can quickly share it with others, even if they are not Xano users.

<Card href="/the-database/database-basics/database-views">
  Database View
</Card>

## Report Generation in the Function Stack

Sometimes, your data may not be in what would be considered a human readable format, and you need to make modifications to it, or present it in an alternative format.

### Using APIs

If you need reports to be generated on demand, use an API endpoint for this functionality.

<Card href="/the-function-stack/building-with-visual-development/apis">
  APIs
</Card>

### Using Background Tasks

If you want to generate reports based on a schedule, utilize a background task.

<Card href="/the-function-stack/building-with-visual-development/background-tasks">
  Background Tasks
</Card>

### Key Functions and Concepts

For most report generation, you'll want to ensure familiarity with the following concepts, depending on your specific needs.

<CardGroup cols={3}>
  <Card title="Query All Records" href="/the-function-stack/functions/database-requests/query-all-records">
    For retrieving data from your database
  </Card>

  <Card title="For Each Loops" href="/the-function-stack/functions/data-manipulation/loops#for-each-loop">
    For iterating through retrieved records and transforming the data
  </Card>

  <Card title="Filters" href="/the-function-stack/filters">
    Filters are typically used to apply modifications to pieces of data, such as math operations or comparing values.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).