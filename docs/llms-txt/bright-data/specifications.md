# Source: https://docs.brightdata.com/datasets/scraper-studio/specifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scraper Studio Specifications

> Bright Data Scraper Studio infrastructure limits, billing model, and data retention rules.

This reference covers Bright Data Scraper Studio's infrastructure limits, billing model, and data retention rules.

## Billing

Bright Data Scraper Studio billing is based on page loads and file downloads.

| Item           | Unit                   | Rate                                                                  |
| -------------- | ---------------------- | --------------------------------------------------------------------- |
| Page loads     | CPM (1,000 page loads) | See [Pricing page](https://brightdata.com/pricing/web-scraper/custom) |
| File downloads | Per GB                 | Billed separately from page loads                                     |

**What counts as a page load:** One URL request processed by Bright Data Scraper Studio infrastructure, regardless of response size.

<Note>
  File downloads are billed at a separate per-GB rate and do not count toward CPM. Check your [Billing dashboard](https://brightdata.com/cp/billing/overview) for current rates.
</Note>

## Infrastructure limits

| Item                | Limit              | Behavior when exceeded                 |
| ------------------- | ------------------ | -------------------------------------- |
| Parallel batch jobs | 1,000 simultaneous | Additional jobs queue automatically    |
| Job queue size      | Unlimited          | Jobs run as capacity becomes available |

## Data retention

| Data type                | Retention period | Behavior after expiry |
| ------------------------ | ---------------- | --------------------- |
| Batch collection results | 16 days          | Permanently deleted   |
| Real-time results        | 7 days           | Permanently deleted   |

<Warning>
  Export your data before the retention period expires. Bright Data does not recover expired data.
</Warning>

## Frequently asked questions

<AccordionGroup>
  <Accordion title="What happens when I exceed 1,000 parallel jobs?">
    Additional jobs queue automatically. No jobs are dropped or cancelled. Jobs run in the order they were submitted as capacity becomes available.
  </Accordion>

  <Accordion title="What happens to my data after the retention period?">
    Data is permanently deleted after 16 days (batch) or 7 days (real-time). Bright Data does not recover expired data. Export your results before expiry.
  </Accordion>

  <Accordion title="Are file downloads included in my CPM billing?">
    No. File downloads are billed separately at a per-GB rate. CPM covers page loads only. Both charges appear in your [Billing dashboard](https://brightdata.com/cp/billing/overview).
  </Accordion>

  <Accordion title="What counts as a page load?">
    One page load equals one URL request processed by Bright Data Scraper Studio infrastructure, regardless of page size or response content.
  </Accordion>
</AccordionGroup>

## Related

<CardGroup cols={2}>
  <Card title="Understanding Scraper Studio" icon="book-open" href="/datasets/scraper-studio/introduction">
    Understand how Scraper Studio works and when to use it
  </Card>

  <Card title="Pricing & Billing" icon="credit-card" href="https://brightdata.com/cp/billing/overview">
    Full billing details for all Bright Data products
  </Card>
</CardGroup>
