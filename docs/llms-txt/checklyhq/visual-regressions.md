# Source: https://checklyhq.com/docs/detect/synthetic-monitoring/browser-checks/visual-regressions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Visual Monitoring with Checkly

> Visual monitoring for more consistent UIs and complex assertions

export const CLITip = ({children}) => {
  return <div className="border border-gray-200 dark:border-gray-700 rounded-lg p-5 my-4 bg-gray-50 dark:bg-gray-800">
      <div className="flex items-center gap-2 font-semibold text-base mb-4 text-gray-800 dark:text-gray-200">
        <Icon icon="rectangle-terminal" />
        Checkly CLI tip
      </div>
      <div className="mb-4 text-gray-600 dark:text-gray-300 leading-relaxed">
        {children}
      </div>
      <a className="text-[#0075FF] dark:text-blue-400 no-underline text-sm font-medium inline-block hover:underline" href="/cli/overview">
        Get started with the Checkly CLI →
      </a>
    </div>;
};

export const YoutubeEmbed = ({id, allowFullScreen = true, end, loading = "eager", start, title = "YouTube video"}) => {
  if (!id) {
    console.error("YouTube component requires an id prop");
  }
  const params = new URLSearchParams();
  if (start) params.append("start", start.toString());
  if (end) params.append("end", end.toString());
  const src = `https://www.youtube.com/embed/${id}?${params.toString()}`;
  return <iframe src={src} title={title} loading={loading} className="w-full aspect-video rounded-xl" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen={allowFullScreen} />;
};

Playwright Test gives you the ability to do visual regression testing and snapshot testing. With Checkly, you can run these tests
against production, 24x7.

Visual regression testing is useful for testing the visual appearance of your applications and making sure production-specific issues like bad deploys,
flaky 3rd party dependencies, CMS changes and user-generated content do not impact to general layout and visual consistency of your
core screens on production.

Have a look at this video for a quick explainer:

<YoutubeEmbed id="uTm40YOtj_g" title="Add Visual Regression Testing to your Synthetic Monitoring" />

The TL;DR is that you can:

* Use the `.toHaveScreenshot()` assertion to visually compare a screenshot of your page to a golden image / reference snapshot.
* Use the `.toMatchSnapshot()` assertion to compare any `string` or `Buffer` value to a golden image / reference snapshot.

<Note>Visual regression & snapshot testing is available on our [Team and Enterprise plans](https://www.checklyhq.com/pricing/#features).</Note>

## Visual regression testing

Starting with visual regression testing takes just three easy steps:

1. Add a single `expect(page).toHaveScreenshot()` line of code to
   your browser check script, like the example below.

   <CodeGroup dropdown>
     ```ts visual-comparison.spec.ts theme={null}
     import { test, expect } from '@playwright/test';

     test('Playwright homepage', async ({ page }) => {
        await page.goto('https://playwright.dev')
        await expect(page).toHaveScreenshot()
     })
     ```

     ```js visual-comparison.spec.js theme={null}
     const { expect, test } = require('@playwright/test')

     test('Playwright homepage', async ({ page }) => {
        await page.goto('https://playwright.dev')
        await expect(page).toHaveScreenshot()
     })
     ```
   </CodeGroup>

2. Run your browser check. The first time you run it, you will get an error indicating that no golden image / reference
   snapshot exists yet.

   ```
   A snapshot doesn't exist at /tmp/19g67loplhq0j/script.spec.js-snapshots/Playwright-homepage-1-chromium-linux.png.
   ```

3. Generate a golden image / reference snapshot by clicking the "Run script and update golden image" option in the "run script" button.

<video controls className="w-full aspect-video rounded-xl" src="https://mintcdn.com/checkly-422f444a/YgQcQD6j5p9gqjr5/images/docs/images/browser-checks/visual_comparison_1st_run.mp4?fit=max&auto=format&n=YgQcQD6j5p9gqjr5&q=85&s=e1249a53e6775f66971164957bc91774" data-path="images/docs/images/browser-checks/visual_comparison_1st_run.mp4" />

This will generate the golden image, which you can inspect in the "golden files" tab in the editor. You can now save
your check and on each check run the golden image will be compared to the actual screenshot.

<CLITip>
  If you are using the Checkly CLI, you can also generate a golden image / reference snapshot by running the following
  command in your terminal:

  ```
  npx checkly test --update-snapshots
  ```
</CLITip>

Now, when your check fails due to a visual difference, you will see a diff of the golden image and the actual screenshot
in your check result.

<video controls className="w-full aspect-video rounded-xl" src="https://mintcdn.com/checkly-422f444a/YgQcQD6j5p9gqjr5/images/docs/images/browser-checks/visual_comparison_diff_modal.mp4?fit=max&auto=format&n=YgQcQD6j5p9gqjr5&q=85&s=bc2dcd6208bec336be162a32ae6da657" data-path="images/docs/images/browser-checks/visual_comparison_diff_modal.mp4" />

### Configuring visual regression testing

To create accurate and actionable screenshot comparisons, Playwright gives you a ton of options to tweak how the `.toHaveScreenshot()`
should behave. What are acceptable differences in color, size, position, etc.? Do you want to match the full screen, or ignore
some dynamic elements that might screw up your comparison?

Let's look at some examples, or check [the official reference docs](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1).

### Example 1: setting pixel ratios and color thresholds

You can control the margin of error you find acceptable between your golden image and the actual image using the following
options:

* `maxDiffPixelRatio`: An acceptable ratio of pixels that are different to the total amount of pixels, between `0` and `1`
* `maxDiffPixels`: A total acceptable amount of pixels that could be different.
* `threshold`: An acceptable perceived color difference in the [YIQ color space](https://en.wikipedia.org/wiki/YIQ) between
  the same pixel in compared images, between `0` (strict) and `1` (lax).

<CodeGroup dropdown>
  ```ts thresholds.spec.ts theme={null}
  import { test, expect } from '@playwright/test';

  test('Playwright homepage', async ({ page }) => {
     await page.goto('https://playwright.dev')
     await expect(page).toHaveScreenshot({ maxDiffPixelRatio: 0.2 })
     await expect(page).toHaveScreenshot({ maxDiffPixels: 1000 })
     await expect(page).toHaveScreenshot({ threshold: 0.2 })
  })
  ```

  ```js thresholds.spec.js theme={null}
  const { test, expect } = require('@playwright/test')

  test('Playwright homepage', async ({ page }) => {
     await page.goto('https://playwright.dev')
     await expect(page).toHaveScreenshot({ maxDiffPixelRatio: 0.2 })
     await expect(page).toHaveScreenshot({ maxDiffPixels: 1000 })
     await expect(page).toHaveScreenshot({ threshold: 0.2 })
  })
  ```
</CodeGroup>

### Example 2: ignoring specific screen elements

A typical homepage can have dynamic elements that change on each page load, or change based on the geographical region.
Think of a "latest blog posts" section, a cookie banner or a region / language selector. Playwright allows you to ignore
these elements when doing a visual comparison using the `mask` option and using one or more `page.locator()` selectors.

The example below hides the cookie banner and optional CTA popup from Intercom on the Checkly docs pages.

<CodeGroup dropdown>
  ```ts ignoring.spec.ts theme={null}
  import { test, expect } from '@playwright/test';

  test('Ignore cookie banner & cta popup', async ({ page }) => {
     await page.goto('https://docs.checklyhq.com')
     await expect(page).toHaveScreenshot({
        mask: [
           page.locator('.optanon-alert-box-wrapper'),
           page.locator('#intercom-container-body')
        ]
     })
  })
  ```

  ```js ignoring.spec.js theme={null}
  const { test, expect } = require('@playwright/test')

  test('Playwright homepage', async ({ page }) => {
     await page.goto('https://docs.checklyhq.com')
     await expect(page).toHaveScreenshot({
        mask: [
           page.locator('.optanon-alert-box-wrapper'),
           page.locator('#intercom-container-body')
        ]
     })
  })
  ```
</CodeGroup>

### Example 3: disabling animations

In some cases, any ongoing animations can cause a visual difference between your golden image and the actual screenshot.
You can disable any CSS animations and transitions using the `animations` option.

<CodeGroup dropdown>
  ```ts disable-anims.spec.ts theme={null}
  import { test, expect } from '@playwright/test';

  test('Disable animations', async ({ page }) => {
     await page.goto('https://playwright.dev')
     await expect(page).toHaveScreenshot({ animations: 'disabled' })
  })
  ```

  ```js disable-anims.spec.js theme={null}
  const { test, expect } = require('@playwright/test')

  test('Disable animations', async ({ page }) => {
     await page.goto('https://playwright.dev')
     await expect(page).toHaveScreenshot({ animations: 'disabled' })
  })
  ```
</CodeGroup>

## Snapshot testing

Snapshot testing, using the `expect().toMatchSnapshot(snapshotName)` assertion, is a great way to test the output of
any arbitrary `string` or `Buffer` value. Note that it is not optimized for visual regression testing.

<CodeGroup dropdown>
  ```ts snapshot.spec.ts theme={null}
  import { test, expect } from '@playwright/test'

  test('Match hero text', async ({ page }) => {
     await page.goto('https://playwright.dev')
     expect(await page.textContent('.hero__title')).toMatchSnapshot('hero.txt')
  })
  ```

  ```js snapshot.spec.js theme={null}
  const { test, expect } = require('@playwright/test')

  test('Match hero text', async ({ page }) => {
     await page.goto('https://playwright.dev')
     expect(await page.textContent('.hero__title')).toMatchSnapshot('hero.txt')
  })
  ```
</CodeGroup>

Creating or updating the golden image / reference snapshot works the same as with visual regression testing.

Check [the official reference docs](https://playwright.dev/docs/api/class-snapshotassertions#snapshot-assertions-to-match-snapshot-1)
for all options.

## Embedding in your CI/CD workflow

Using the [Checkly CLI](/cli/overview) you can code and configure visual regression and snapshot testing on your local machine
and deploy any changes either directly from your local machine or from your CI/CD pipeline of choice.

In a typical scenario, you would follow the steps below:

1. Create or update a browser check with visual regression or snapshot testing on your local machine.
2. Generate the golden image / reference snapshot(s).
   ```bash  theme={null}
   npx checkly test --update-snapshots
   ```
   The resulting files are stored in a `some-file-prepend.ts-snapshots` folder next to your browser check script.
3. Commit the browser check script and the golden image / reference snapshot(s) to your version control system.
4. Push your code to your CI/CD pipeline.
5. In your CI/CD pipeline, optionally run your checks again. Maybe add the `--record` flag to record the test in
   Checkly.
   ```bash  theme={null}
   npx checkly test --record 
   ```
6. If your tests pass, deploy your checks to production. The CLI will push your snapshot to the
   Checkly cloud automatically.
   ```bash  theme={null}
   npx checkly deploy
   ```

Learn more about setting up the Checkly CLI for your CI/CD pipeline 👇

<Cards>
  <Card title="GitHub Actions" href="/integrations/ci-cd/github/actions" icon="github" />

  <Card title="GitLab CI/CD" href="/integrations/ci-cd/gitlab" icon="gitlab" />

  <Card title="Jenkins" href="/integrations/ci-cd/jenkins" icon="jenkins" />

  <Card title="Vercel" href="/integrations/ci-cd/vercel" icon="vercel" />
</Cards>

## Known limitations

* Checkly currently only supports the Chromium and Chrome browsers.

## Automatic screenshots on error

Whenever your Playwright script encounters an error, we will automatically snap a screenshot the moment the error
occurs. This is different than Visual Regression Monitoring Here is an example from real life!

<Steps>
  <Step title="Script Action">
    Your script clicks on a button using a selector `wait page.click(".my-button-class")`.
  </Step>

  <Step title="Element Issue">
    For some reason, that button does not exist or is not clickable.
  </Step>

  <Step title="Playwright Error">
    Playwright waits for the button with the selector to appear. It does not and Playwright throws an error.
  </Step>

  <Step title="Automatic Screenshot">
    Checkly automatically calls `page.screenshot()` a screenshot. The screenshot indicates that that specific button was missing.
  </Step>
</Steps>

## Playwright resources

* [The official Playwright guide on visual comparison and snapshot testing](https://playwright.dev/docs/test-snapshots)
* The `.toHaveScreenshot()` [API reference](https://playwright.dev/docs/api/class-pageassertions#page-assertions-to-have-screenshot-1)
* The `.toMatchSnapshot()` [API reference](https://playwright.dev/docs/api/class-snapshotassertions#snapshot-assertions-to-match-snapshot-1)


Built with [Mintlify](https://mintlify.com).