# Source: https://docs.anchorbrowser.io/examples/form-filling.md

# Form Filling Automation

The following example shows form filling, including the ability to self-complete missing data in the form filling process.

```tsx node.js theme={null}
import { chromium } from 'playwright';

const browser = await chromium.connectOverCDP(connectionString);
const context = browser.contexts()[0];
const ai = context.serviceWorkers()[0];
const page = context.pages()[0];

page.goto('https://www.wix.com/demone2/nicol-rider');

const result = await ai.evaluate('Read the resume, understand the details, and complete the form at https://formspree.io/library/donation/charity-donation-form/preview.html as if you were her. Limit the donation to $10.');
console.info(result);
```
