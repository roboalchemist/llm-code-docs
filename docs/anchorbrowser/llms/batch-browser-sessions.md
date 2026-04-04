# Source: https://docs.anchorbrowser.io/advanced/batch-browser-sessions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch Browser Sessions

> Create and manage multiple browser sessions simultaneously for large-scale automation tasks

Create up to 5,000 browser sessions in a single API call for large-scale automation, web scraping, and load testing.

## Quick Start

### 1. Create a Batch

```javascript  theme={null}
const response = await fetch('https://api.anchorbrowser.io/v1/batch-sessions', {
  method: 'POST',
  headers: {
    'anchor-api-key': process.env.ANCHOR_API_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    count: 10,
    configuration: {
      browser: {
        headless: { active: true },
        viewport: { width: 1440, height: 900 }
      },
      session: {
        timeout: { idle_timeout: 10, max_duration: 300 }
      }
    },
    metadata: {
      project: 'web-scraping'
    }
  })
});

const batch = await response.json();
const batchId = batch.data.batch_id;
console.log('Batch ID:', batchId);
```

### 2. Monitor Progress

```javascript  theme={null}
const response = await fetch(`https://api.anchorbrowser.io/v1/batch-sessions/${batchId}`, {
  headers: { 'anchor-api-key': process.env.ANCHOR_API_KEY }
});

const status = await response.json();
console.log(`Progress: ${status.data.progress.percentage}%`);
console.log(`Completed: ${status.data.completed_requests}/${status.data.total_requests}`);
```

### 3. Use Sessions

```javascript  theme={null}
import { chromium } from 'playwright';

const sessions = status.data.sessions.filter(s => s.status === 'completed');

for (const session of sessions) {
  const browser = await chromium.connectOverCDP(session.cdp_url);
  const page = await browser.contexts()[0].newPage();
  
  await page.goto('https://example.com');
  // ... your automation logic
  
  await browser.close();
}
```

## Polling Strategy

```javascript  theme={null}
async function waitForBatchCompletion(batchId, maxWaitMinutes = 10) {
  const maxWaitMs = maxWaitMinutes * 60 * 1000;
  let checkInterval = 5000;
  const startTime = Date.now();
  
  while (Date.now() - startTime < maxWaitMs) {
    const response = await fetch(`https://api.anchorbrowser.io/v1/batch-sessions/${batchId}`, {
      headers: { 'anchor-api-key': process.env.ANCHOR_API_KEY }
    });
    
    const data = await response.json();
    
    if (data.data.status === 'completed') return data.data.sessions;
    if (data.data.status === 'failed') throw new Error(`Batch failed: ${data.data.error}`);
    
    await new Promise(resolve => setTimeout(resolve, checkInterval));
    checkInterval = Math.min(checkInterval * 1.5, 30000);
  }
  
  throw new Error(`Batch did not complete within ${maxWaitMinutes} minutes`);
}
```

## Parameters

<ResponseField name="count" type="number" required>
  Number of browser sessions to create (1-1000)
</ResponseField>

<ResponseField name="configuration" type="object">
  Session configuration that applies to all sessions in the batch
</ResponseField>

<ResponseField name="metadata" type="object">
  Optional key-value pairs for batch identification
</ResponseField>

## Status States

**Batch States**: `pending` → `processing` → `completed` / `failed`

**Session States**: `pending` → `processing` → `completed` / `failed`

## Available Endpoints

* `POST /v1/batch-sessions` - Create batch sessions
* `GET /v1/batch-sessions/{batch_id}` - Get batch status

<Note>
  Additional endpoints for listing, canceling, and retrying batches are planned for future releases.
</Note>

## Limits

* **Maximum batch size**: 1,000 sessions
* **Session lifetime**: Up to 24 hours
* Large batches may take several minutes to provision
