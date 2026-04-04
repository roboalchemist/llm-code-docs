# Source: https://momentic.ai/docs/performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance

> Momentic's performance characteristics and benchmarks

## Execution speed

The runtime of a Momentic test largely depends on how it is crafted and the
state of the system under test.

A Momentic test that only attempts to achieve feature parity with a traditional
testing tool such as Playwright or Cypress will run at approximately the same
speed. Due to [intelligent caching](/step-cache), over 99% of steps that run on
the Momentic platform execute in under 500ms:

| Preset action                      | Average runtime |
| ---------------------------------- | --------------- |
| Click                              | 250ms           |
| Type                               | 340ms           |
| Choosing from a `<select>` element | 275ms           |
| Pressing a key                     | \<5ms           |
| Scroll                             | \<5ms           |
| Page check attempt                 | 220ms           |
| Element check attempt              | 210ms           |
| Visual diff                        | 620ms           |

However, any enhanced steps that require AI completions can incur greater
runtime costs. These steps provide outsized value, power, and flexibility to
developers at the cost of duration. The approximate **first-time** execution
speed of each AI-enhanced action supported by Momentic is listed below. In many
cases, Momentic [caches](/step-cache) AI results to reduce subsequent runtime.

| AI-enhanced action                          | First-time runtime range |
| ------------------------------------------- | ------------------------ |
| Locating an element                         | 4-8 seconds              |
| Evaluating an assertion once                | 5-8 seconds              |
| Extracting data from the page               | 5-8 seconds              |
| Generating a single command in an AI action | 6-12 seconds             |
| Classifying a test failure                  | 20-30 seconds            |
| Auto-healing a section                      | 30+ seconds              |

## Benchmarks

### Overview

We have published a basic benchmark comparing Momentic against Playwright in
this publicly accessible test automation
[environment](https://practicetestautomation.com/practice-test-login/).

The results illustrate that cached Momentic steps are **only 52ms slower** on
average than comparable Playwright functions. Non-cached steps that require AI
to execute run on average **6354ms** slower. Over 99% of all steps executed on
the Momentic platform are cached.

Note that this benchmark does not exhaustively test all Momentic step types,
many of which do not have analogs in Playwright, Cypress, or any traditional
tooling (e.g. [AI check](/steps/ai-check), [Visual diff](/steps/visual-diff)).

### Method

We built a Momentic test that logs into the practice automation site, as well as
an equivalent Playwright script that performs the same sequence of actions. We
obtained three different sets of measurements:

* The "Steps only" category only measures the time spent executing steps in both
  software.
* The "End-to-end" category includes Momentic's fixed bootstrap (e.g. API key
  check) and test result upload times. For Playwright, the end-to-end time
  includes CLI initialization time but does not involve any upload of data.
* The "First-run" category ran with caching explicitly disabled and thus
  includes the runtime of 4 fresh AI completions.

All measurements were completed on a M3 Max Macbook Pro with 36GB RAM running
Mac OS Sonoma.

### Results

All values are P50 milliseconds measured over 10 independent samples.

|                      | Playwright | Momentic |
| -------------------- | ---------- | -------- |
| Steps only           | 961ms      | 1173ms   |
| End-to-end           | 1870ms     | 3998ms   |
| First-run steps only | N/A        | 26379ms  |

The source used for this benchmark is provided below:

<CodeGroup>
  ```yaml benchmark.test.yaml theme={null}
  fileType: momentic/test
  id: 48f763e2-3ace-4ac8-ba7d-36f3bf0496a2
  name: Log in practice test automation
  baseUrl: https://practicetestautomation.com/practice-test-login/
  schemaVersion: 1.0.13
  advanced:
    disableAICaching: false
  retries: 1
  envs: []
  steps:
    - id: c0f25128-3dfe-4b79-9353-5d11eca5a15b
      type: PRESET_ACTION
      command:
        id: 72e7f915-1262-4558-9d60-4a7805fb00c7
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        clearContent: true
        pressEnter: false
        type: TYPE
        target:
          type: description
          elementDescriptor: the username input
        value: student
    - id: 
      type: PRESET_ACTION
      command:
        id: 243fc113-511f-4f25-bdea-c68af30bd077
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        clearContent: true
        pressEnter: false
        type: TYPE
        target:
          type: description
          elementDescriptor: the password input
        value: Password123
    - id: b46c7d74-b549-4921-9b94-d3a48c4d24ff
      type: PRESET_ACTION
      command:
        id: 52153871-0237-4847-8b33-86a7bf709246
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        type: CLICK
        target:
          type: description
          elementDescriptor: the submit button
        doubleClick: false
        rightClick: false
    - id: 4f2d060e-716e-4b26-b821-6d1d170fbccb
      type: PRESET_ACTION
      command:
        id: 21003652-329b-4f13-8891-21a31cd40aa6
        type: PAGE_CHECK
        assertion:
          type: CONTENT
          value: Logged In
  ```

  ```javascript benchmark.spec.js theme={null}
  import { chromium } from "playwright";

  async function main() {
    console.log("starting steps", Date.now());
    const browser = await chromium.launch({
      headless: true,
    });
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto("https://practicetestautomation.com/practice-test-login/");
    await page.locator("#username").fill("student");
    await page.locator("#password").fill("Password123");
    await page.locator("#submit").click();
    await page.getByText("Logged In Successfully").waitFor({ state: "visible" });
    console.log("done", Date.now());
    process.exit(0);
  }

  void main();
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).