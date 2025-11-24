# Source: https://docs.anchorbrowser.io/examples/research-task.md

# Deep Research

The following example demonstrates how to use Anchor Browser to perform web research tasks.

```tsx node.js theme={null}
import { chromium } from 'playwright';

const browser = await chromium.connectOverCDP(connectionString);
const context = browser.contexts()[0];
const ai = context.serviceWorkers()[0];
const page = context.pages()[0];

await page.goto("http://docs.anchorbrowser.io/", { waitUntil: 'domcontentloaded' });

const result = await ai.evaluate('Find the most recent NBA game played by the Milwaukee Bucks and provide the result.')
console.log(result);

const author = await ai.evaluate('Find an article discussing the game and provide the author\'s name.')
console.log(author);
```
