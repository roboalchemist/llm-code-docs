# Source: https://docs.anchorbrowser.io/examples/configuration-collection.md

# Configuration Collection

The following example shows how to collect configuration data that is not exposed through an API from a SaaS service (Grafana) configuration page.

```tsx node.js theme={null}
import { chromium } from 'playwright';

const browser = await chromium.connectOverCDP(connectionString);
const context = browser.contexts()[0];
const ai = context.serviceWorkers()[0];
const page = context.pages()[0];

await page.goto("https://play.grafana.org/a/grafana-k8s-app/navigation/nodes?from=now-1h&to=now&refresh=1m", { waitUntil: 'domcontentloaded' });
const result = await ai.evaluate('Collect the node names and their CPU average %, return in JSON array')
console.log(result);
```
