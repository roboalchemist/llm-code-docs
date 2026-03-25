# Source: https://pipedream.com/docs/workflows/building-workflows/code/nodejs/browser-automation.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Automation With Node.js

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/RXlCDTQc8xI" title="Browser automation with Node.js in Pipedream" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

You can leverage headless browser automations within Pipedream workflows for web scraping, generating screenshots, or programmatically interacting with websites - even those that make heavy usage of frontend JavaScript.

Pipedream manages a [specialized package](https://www.npmjs.com/package/@pipedream/browsers) that includes Puppeteer and Playwright bundled with a specialized Chromium instance that’s compatible with Pipedream’s Node.js Execution Environment.

All that’s required is importing the [`@pipedream/browsers`](https://www.npmjs.com/package/@pipedream/browsers) package into your Node.js code step and launch a browser. Pipedream will start Chromium and launch a Puppeteer or Playwright Browser instance for you.

## Usage

The `@pipedream/browsers` package exports two modules: `puppeteer` & `playwright`. Both modules share the same interface:

* `browser(opts?)` - method to instantiate a new browser (returns a browser instance)
* `launch(opts?)` - an alias to browser()
* `newPage()` - creates a new page instance and returns both the page & browser

### Puppeteer

First import the `puppeteer` module from `@pipedream/browsers` and use `browser()` or `launch()` method to instantiate a browser.

Then using this browser you can open new [Pages](https://pptr.dev/api/puppeteer.page), which have individual controls to open URLs:

```javascript  theme={null}
 import { puppeteer } from '@pipedream/browsers';
 
export default defineComponent({
  async run({steps, $}) {
    const browser = await puppeteer.browser();
 
    // Interact with the web page programmatically
    // See Puppeeter's Page documentation for available methods:
    // https://pptr.dev/api/puppeteer.page
    const page = await browser.newPage();
 
    await page.goto('https://pipedream.com/');
    const title = await page.title();
    const content = await page.content();
 
    $.export('title', title);
    $.export('content', content);
 
    // The browser needs to be closed, otherwise the step will hang
    await browser.close();
  },
})
```

#### Screenshot a webpage

Puppeteer can take a full screenshot of a webpage rendered with Chromium. For full options [see the Puppeteer Screenshot method documentation.](https://pptr.dev/api/puppeteer.page.screenshot)

<Tabs>
  <Tab title="Save screenshot to `/tmp`">
    Save a screenshot within the local `/tmp` directory:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        await page.screenshot({ path: '/tmp/screenshot.png' });
        await browser.close();
      },
    });

    ```
  </Tab>

  <Tab title="Return screenshot as a base64 encoded string">
    Save the screenshot as a base 64 encoded string:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com/');
        const screenshot = await page.screenshot({ encoding: 'base64' });
        await browser.close();
        return screenshot;
      },
    });
    ```
  </Tab>
</Tabs>

#### Generate a PDF of a webpage

Puppeteer can render a PDF of a webpage. For full options [see the Puppeteer Screenshot method documentation.](https://pptr.dev/api/puppeteer.page.pdf)

<Tabs>
  <Tab title="Save PDF to `/tmp`">
    Save the PDF locally to `/tmp`:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        await page.pdf({ path: '/tmp/screenshot.pdf' });
        await browser.close();
      },
    });

    ```
  </Tab>

  <Tab title="Return the PDF as a base64 encoded string">
    Save the PDF as a base 64 encoded string:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        const pdfBuffer = await page.pdf();
        const pdfBase64 = pdfBuffer.toString('base64');
        await browser.close();
        return pdfBase64;
      },
    });
    ```
  </Tab>
</Tabs>

#### Scrape content from a webpage

Puppeteer can scrape individual elements or return all content of a webpage.

<Tabs>
  <Tab title="Extract the h1 tag from a webpage">
    Extract individual elements with a CSS selector:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        const h1Content = await page.$eval('h1', el => el.textContent);
        await browser.close();
        return h1Content;
      },
    });

    ```
  </Tab>

  <Tab title="Retrieve all HTML content from a webpage">
    Extract all HTML content form a webpage:

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        const content = await page.content();
        await browser.close();
        return content;
      },
    });
    ```
  </Tab>
</Tabs>

#### Submit a form

Puppeteer can also programmatically click and type on a webpage.

<Tabs>
  <Tab title="With `Page.type`">
    `Page.type` accepts a CSS selector and a string to type into the field.

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ steps, $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();

        await page.goto('https://example.com/contact');
        await page.type('input[name=email]', 'pierce@pipedream.com');
        await page.type('input[name=name]', 'Dylan Pierce');
        await page.type('textarea[name=message]', "Hello, from a Pipedream workflow.");
        await page.click('input[type=submit]');

        await browser.close();
      },
    });
    ```
  </Tab>

  <Tab title="With `Page.click` and `Page.keyboard.type`">
    `Page.click` will click on the element to focus on it, then `Page.keyboard.type` emulates keyboard keystrokes.

    ```javascript  theme={null}
    import { puppeteer } from '@pipedream/browsers';

    export default defineComponent({
      async run({ steps, $ }) {
        const browser = await puppeteer.browser();
        const page = await browser.newPage();

        await page.goto('https://example.com/contact');
        await page.click('input[name=email]')
        await page.keyboard.type('pierce@pipedream.com');
        await page.click('input[name=name]')
        await page.keyboard.type('Dylan Pierce');
        await page.click('textarea[name=message]')
        await page.keyboard.type("Hello, from a Pipedream workflow.");
        await page.click('input[type=submit]');

        await browser.close();
      },
    });
    ```
  </Tab>
</Tabs>

### Playwright

First import the `playwright` module from `@pipedream/browsers` and use `browser()` or `launch()` method to instantiate a browser.

Then using this browser you can open new [Pages](https://playwright.dev/api/class-page), which have individual controls to open URLs, click elements, generate screenshots and type and more:

```javascript  theme={null}
import { playwright } from '@pipedream/browsers';
 
export default defineComponent({
  async run({steps, $}) {
    const browser = await playwright.browser();
 
    // Interact with the web page programmatically
    // See Playwright's Page documentation for available methods:
    // https://playwright.dev/api/class-page
    const page = await browser.newPage();
 
    await page.goto('https://pipedream.com/');
    const title = await page.title();
    const content = await page.content();
 
    $.export('title', title);
    $.export('content', content);
 
    // The browser context and browser needs to be closed, otherwise the step will hang
    await page.context().close();
    await browser.close();
  },
})
```

<Note>
  **Don’t forget to close the browser context**

  Playwright differs from Puppeteer slightly in that you have to close the page’s browser context before closing the browser itself.

  ```javascript  theme={null}
  // Close the context & browser before returning results
  // Otherwise the step will hang
  await page.context().close();
  await browser.close();
  ```

</Note>

#### Screenshot a webpage

Playwright can take a full screenshot of a webpage rendered with Chromium. For full options [see the Playwright Screenshot method documentation.](https://playwright.dev/api/class-page#page-screenshot)

<Tabs>
  <Tab title="Save screenshot to `/tmp`">
    Save a screenshot within the local `/tmp` directory:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        await page.screenshot({ path: '/tmp/screenshot.png' });

        await page.context().close();
        await browser.close();
      },
    });

    ```
  </Tab>

  <Tab title="Return screenshot as a base64 encoded string">
    Save the screenshot as a base 64 encoded string:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com/');

        const screenshotBuffer = await page.screenshot();
        const screenshotBase64 = screenshotBuffer.toString('base64');

        await page.context().close();
        await browser.close();

        return screenshotBase64;
      },
    });
    ```
  </Tab>
</Tabs>

#### Generate a PDF of a webpage

Playwright can render a PDF of a webpage. For full options [see the Playwright Screenshot method documentation.](https://playwright.dev/api/class-page#page-pdf)

<Tabs>
  <Tab title="Save PDF to `/tmp`">
    Save a PDF locally to `/tmp`:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        await page.pdf({ path: '/tmp/screenshot.pdf' });

        await page.context().close();
        await browser.close();
      },
    });

    ```
  </Tab>

  <Tab title="Return screenshot as a base64 encoded string">
    Save the screenshot as a base 64 encoded string:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.launch();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com/');

        const screenshotBuffer = await page.pdf();
        const screenshotBase64 = screenshotBuffer.toString('base64');

        await page.context().close();
        await browser.close();

        return screenshotBase64;
      },
    });
    ```
  </Tab>
</Tabs>

#### Scrape content from a webpage

Playwright can scrape individual elements or return all content of a webpage.

<Tabs>
  <Tab title="Extract the h1 tag from a webpage">
    Extract individual HTML elements using a CSS Selector:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        const h1Content = await page.$eval('h1', el => el.textContent);

        await page.context().close();
        await browser.close();

        return h1Content;
      },
    });

    ```
  </Tab>

  <Tab title="Retrieve all HTML content from a webpage">
    Extract all HTML content from a webpage with `Page.content`:

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ $ }) {
        const browser = await playwright.browser();
        const page = await browser.newPage();
        await page.goto('https://pipedream.com');
        const content = await page.content();

        await page.context().close();
        await browser.close();

        return content;
      },
    });
    ```
  </Tab>
</Tabs>

#### Submit a form

Playwright can also programmatically click and type on a webpage.

<Tabs>
  <Tab title="With `Page.type`">
    `Page.type` accepts a CSS selector and a string to type into the selected element.

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ steps, $ }) {
        const browser = await playwright.browser();
        const page = await browser.newPage();

        await page.goto('https://example.com/contact');
        await page.type('input[name=email]', 'pierce@pipedream.com');
        await page.type('input[name=name]', 'Dylan Pierce');
        await page.type('textarea[name=message]', "Hello, from a Pipedream workflow.");
        await page.click('input[type=submit]');

        await page.context().close();
        await browser.close();
      },
    });
    ```
  </Tab>

  <Tab title="With `Page.click` and `Page.keyboard.type`">
    `Page.click` will click on the element to focus on it, then `Page.keyboard.type` emulates keyboard keystrokes.

    ```javascript  theme={null}
    import { playwright } from '@pipedream/browsers';

    export default defineComponent({
      async run({ steps, $ }) {
        const browser = await playwright.browser();
        const page = await browser.newPage();

        await page.goto('https://example.com/contact');
        await page.click('input[name=email]')
        await page.keyboard.type('pierce@pipedream.com');
        await page.click('input[name=name]')
        await page.keyboard.type('Dylan Pierce');
        await page.click('textarea[name=message]')
        await page.keyboard.type("Hello, from a Pipedream workflow.");
        await page.click('input[type=submit]');

        await page.context().close();
        await browser.close();
      },
    });
    ```
  </Tab>
</Tabs>

## FAQ

### Can I use this package in sources or actions?

Yes, the same `@pipedream/browsers` package can be used in [actions](/components/contributing/actions-quickstart/) as well as [sources](/components/contributing/sources-quickstart/).

The steps are the same as usage in Node.js code. Open a browser, create a page, and close the browser at the end of the code step.

<Warning>
  **Memory limits**

  At this time it’s not possible to configure the allocated memory to a Source. You may experience a higher rate of Out of Memory errors on Sources that use Puppeteer or Playwright due to the high usage of memory required by Chromium.
</Warning>

### Workflow exited before step finished execution

Remember to close the browser instance *before* the step finishes. Otherwise, the browser will keep the step “open” and not transfer control to the next step.

### Out of memory errors or slow starts

For best results, we recommend increasing the amount of memory available to your workflow to 2 gigabytes. You can adjust the available memory in the [workflow settings](/workflows/building-workflows/settings/#memory).

### Which browser are these packages using?

The `@pipedream/browsers` package includes a specific version of Chromium that is compatible with Pipedream Node.js execution environments that run your code.

For details on the specific versions of Chromium, puppeeter and playwright bundled in this package, visit the package’s [README](https://github.com/PipedreamHQ/pipedream/tree/master/packages/browsers).

### How to customize `puppeteer.launch()`?

To pass arguments to `puppeteer.launch()` to customize the browser instance, you can pass them directly to `puppeteer.browser()`.

For example, you can alter the `protocolTimeout` length just by passing it as an argument:

```javascript  theme={null}
import { puppeteer } from '@pipedream/browsers';
 
export default defineComponent({
  async run({steps, $}) {
    // passing a `protocolTimeout` argument to increase the timeout length for a puppeteer instance
    const browser = await puppeteer.browser({ protocolTimeout: 480000 });
    // rest of code
  },
})
 
```

Please see the [`@pipedream/browsers` source code](https://github.com/PipedreamHQ/pipedream/blob/17888e631857259a6535f9bd13c23a1e7ff95381/packages/browsers/index.mjs#L14) for the default arguments that Pipedream provides.

### How do I use `puppeteer.connect()`?

To use `puppeteer.connect()` to connect to a remote browser instance, you can use the [`puppeteer-core`](https://github.com/puppeteer/puppeteer/tree/main?tab=readme-ov-file#puppeteer-core) package:

```javascript  theme={null}
import puppeteer from "puppeteer-core";
```

`puppeteer-core` does not download Chrome when installed, which decreases the size of your deployment and can improve cold start times.

To connect to a remote browser instance using Playwright, you can use the [`playwright-core`](https://www.npmjs.com/package/playwright-core) package, which is the no-browser Playwright package:

```javascript  theme={null}
import playwright from "playwright-core";
```

Built with [Mintlify](https://mintlify.com).
