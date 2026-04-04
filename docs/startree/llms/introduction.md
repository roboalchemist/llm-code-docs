# Source: https://docs.startree.ai/api-reference/introduction.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Learn about StarTree Cloud APIs for managing tables and querying data at scale.

# StarTree Cloud APIs

StarTree Cloud provides **powerful APIs**, enabling users to **manage tables, schemas, and query data efficiently at scale**.

<CardGroup cols={2}>
  <Card title="Controller APIs" icon="toolbox" iconType="light" color="#0673fb" href="/api-reference/table/lists-all-tables-in-cluster">
    Create and manage tables, schemas, and indexes with programmatic control.
  </Card>

  <Card title="Broker APIs" icon="magnifying-glass" iconType="light" color="#0673fb" href="/api-reference/dataplane/query">
    Query real-time data at scale with low latency and high concurrency.
  </Card>
</CardGroup>

***

## **Authentication & Prerequisites**

To interact with StarTree Cloud APIs, follow these steps:

<Steps>
  <Step title="Log in to StarTree Cloud">
    Access the [StarTree Cloud Console](https://startree.ai/saas-signup) and log in to your account.
  </Step>

  <Step title="Generate a Bearer Token">
    Navigate to the **API Access** section in the console and generate your **Bearer Token**.\
    This token must be included in every API request for authentication.
  </Step>

  <Step title="Retrieve Your Workspace ID">
    The **Workspace ID** can be found in the **top navigation bar** of the console.\
    This ID must be passed in the `database` HTTP header for all API calls.

    <Note>
      Workspace ID is required **only for multi-tenant clusters** (e.g., Free Tier).\
      It is **not needed for dedicated clusters** (Standard or Premium plans).
    </Note>
  </Step>

  <Step title="Start Calling APIs">
    Explore the API reference in the following pages to learn how to use the Bearer Token and Workspace ID in API requests.
  </Step>
</Steps>

Built with [Mintlify](https://mintlify.com).
