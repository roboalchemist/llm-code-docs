# Source: https://docs.anchorbrowser.io/examples/buyer-intent.md

# Buyer Intent Discovery

The following example use-case shows how to find buyer-intent data based on Github stargazers of a Github project named 'Airflow'. A star from a person that works for a significant corporation can be a hint of buying intent in the data pipelines space.

```tsx node.js theme={null}
import { chromium } from 'playwright';

const browser = await chromium.connectOverCDP(connectionString); // Fill in the browser CDP string
const context = browser.contexts()[0];
const ai = context.serviceWorkers()[0];
const page = context.pages()[0];

await page.goto("https://github.com/apache/airflow/stargazers?page=1");

const result = await ai.evaluate('On the current stargazers list, return the GitHub profile URLs of all users that are a part of a well-known company. Then, do this for the first 3 pages using the "page" query parameter. Return a JSON array result: ["url1", "url2", ...].')
console.log(result);
```
