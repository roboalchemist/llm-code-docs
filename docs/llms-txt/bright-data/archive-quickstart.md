# Source: https://docs.brightdata.com/archive-quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Archive Overview

> The Web Archive gives you access to Bright Data's stored web traffic - a continuously growing repository of pages collected through our Unlocker and SERP APIs.

## What it does

Instead of running your own crawlers, you search the archive, filter what you need (by time range, domain, URL patterns, language, blocking signals), and export ready-to-use datasets as HTML files + metadata.

## Common use cases

* **LLM training and RAG pipelines**: Build or refresh training corpora from targeted web segments
* **Search and indexing**: Backfill indexes with historical content across large domain sets
* **Search product augmentation**: Improve coverage for sites with advanced blocking, supporting reliable page retrieval at scale

## How it works

<Card title="Run a search" icon="search" href="/api-reference/archive-api/run-a-search" iconType="duotone" arrow="true" horizontal>
  Filter by time range, domains, URL patterns, language, or signals (CAPTCHA, robots blocks, etc.)
</Card>

<Card title="Review the estimate" icon="clipboard-list" href="/api-reference/archive-api/get-search-status" iconType="duotone" arrow="true" horizontal>
  See matched file count, snapshot size, expected duration, and cost
</Card>

<Card title="Create and deliver a dump" icon="file-export" href="/api-reference/archive-api/deliver-to-cloud" iconType="duotone" arrow="true" horizontal>
  Export the snapshot as HTML files + metadata (URL, timestamp, collection attributes) to Amazon S3, Azure Blob Storage, or via webhook
</Card>
