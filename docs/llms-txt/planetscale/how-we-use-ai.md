# Source: https://planetscale.com/docs/how-we-use-ai.md

# How PlanetScale uses AI

> Which PlanetScale features use generative AI, and how we ensure customer data stays secure and private.

## Overview

PlanetScale uses generative AI to power two [Insights](/docs/postgres/monitoring/query-insights) features. This overview explains those features and how PlanetScale ensures safety and privacy of customer data.

## Which features use generative AI

Two features of [Insights](/docs/postgres/monitoring/query-insights) use generative AI:

* Postgres [index recommendations](/docs/postgres/monitoring/schema-recommendations) use a large language model to interpret query patterns and identify potential indexes that could improve performance of those patterns. The prompt sent to the LLM includes one or more query patterns and one or more table schemas. Query patterns and table schemas include the names of tables and columns, but not any actual row data. This process runs automatically on each database each night.
* Query summaries for both [Postgres](/docs/postgres/monitoring/query-insights#query-deep-dive) and [Vitess](/docs/vitess/monitoring/query-insights#query-deep-dive) use a large language model to convert a query pattern to a one-sentence description. The prompt sent to the LLM contains a query pattern. This feature is invoked only when a user clicks on the "Summarize query" button on an Insights query-details page.

## Privacy and security

All AI use is covered by PlanetScale's existing [terms of service](https://planetscale.com/legal/agreement) and [subprocessor list](https://planetscale.com/legal/subprocessors). Our LLM provider, [Google Gemini](https://cloud.google.com/gemini/docs/discover/data-governance), encrypts all communication in transit, does not use prompts for training, and retains prompts only long enough to screen for abuse.

## Opting out

We understand that not every customer wants to use AI. You can disable the LLM-based features for all the databases in your account or organization on the organization settings page.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt