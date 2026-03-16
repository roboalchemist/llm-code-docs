# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandPage.md

# StagehandPage<!-- -->

Enhanced Playwright Page with Stagehand AI methods.

### Hierarchy

* Page
  * *StagehandPage*

## Index[**](#Index)

### Properties

* [**clock](#clock)
* [**coverage](#coverage)
* [**keyboard](#keyboard)
* [**mouse](#mouse)
* [**request](#request)
* [**touchscreen](#touchscreen)

### Methods

* [**\[asyncDispose\]](#\[asyncDispose])
* [**$](#$)
* [**$$](#$$)
* [**$$eval](#$$eval)
* [**$eval](#$eval)
* [**act](#act)
* [**addInitScript](#addInitScript)
* [**addListener](#addListener)
* [**addLocatorHandler](#addLocatorHandler)
* [**addScriptTag](#addScriptTag)
* [**addStyleTag](#addStyleTag)
* [**agent](#agent)
* [**bringToFront](#bringToFront)
* [**check](#check)
* [**click](#click)
* [**close](#close)
* [**consoleMessages](#consoleMessages)
* [**content](#content)
* [**context](#context)
* [**dblclick](#dblclick)
* [**dispatchEvent](#dispatchEvent)
* [**dragAndDrop](#dragAndDrop)
* [**emulateMedia](#emulateMedia)
* [**evaluate](#evaluate)
* [**evaluateHandle](#evaluateHandle)
* [**exposeBinding](#exposeBinding)
* [**exposeFunction](#exposeFunction)
* [**extract](#extract)
* [**fill](#fill)
* [**focus](#focus)
* [**frame](#frame)
* [**frameLocator](#frameLocator)
* [**frames](#frames)
* [**getAttribute](#getAttribute)
* [**getByAltText](#getByAltText)
* [**getByLabel](#getByLabel)
* [**getByPlaceholder](#getByPlaceholder)
* [**getByRole](#getByRole)
* [**getByTestId](#getByTestId)
* [**getByText](#getByText)
* [**getByTitle](#getByTitle)
* [**goBack](#goBack)
* [**goForward](#goForward)
* [**goto](#goto)
* [**hover](#hover)
* [**innerHTML](#innerHTML)
* [**innerText](#innerText)
* [**inputValue](#inputValue)
* [**isChecked](#isChecked)
* [**isClosed](#isClosed)
* [**isDisabled](#isDisabled)
* [**isEditable](#isEditable)
* [**isEnabled](#isEnabled)
* [**isHidden](#isHidden)
* [**isVisible](#isVisible)
* [**locator](#locator)
* [**mainFrame](#mainFrame)
* [**observe](#observe)
* [**off](#off)
* [**on](#on)
* [**once](#once)
* [**opener](#opener)
* [**pageErrors](#pageErrors)
* [**pause](#pause)
* [**pdf](#pdf)
* [**prependListener](#prependListener)
* [**press](#press)
* [**reload](#reload)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**removeLocatorHandler](#removeLocatorHandler)
* [**requestGC](#requestGC)
* [**requests](#requests)
* [**route](#route)
* [**routeFromHAR](#routeFromHAR)
* [**routeWebSocket](#routeWebSocket)
* [**screenshot](#screenshot)
* [**selectOption](#selectOption)
* [**setChecked](#setChecked)
* [**setContent](#setContent)
* [**setDefaultNavigationTimeout](#setDefaultNavigationTimeout)
* [**setDefaultTimeout](#setDefaultTimeout)
* [**setExtraHTTPHeaders](#setExtraHTTPHeaders)
* [**setInputFiles](#setInputFiles)
* [**setViewportSize](#setViewportSize)
* [**tap](#tap)
* [**textContent](#textContent)
* [**title](#title)
* [**type](#type)
* [**uncheck](#uncheck)
* [**unroute](#unroute)
* [**unrouteAll](#unrouteAll)
* [**url](#url)
* [**video](#video)
* [**viewportSize](#viewportSize)
* [**waitForEvent](#waitForEvent)
* [**waitForFunction](#waitForFunction)
* [**waitForLoadState](#waitForLoadState)
* [**waitForNavigation](#waitForNavigation)
* [**waitForRequest](#waitForRequest)
* [**waitForResponse](#waitForResponse)
* [**waitForSelector](#waitForSelector)
* [**waitForTimeout](#waitForTimeout)
* [**waitForURL](#waitForURL)
* [**workers](#workers)

## Properties<!-- -->[**](#Properties)

### [**](#clock)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5179)externalinheritedclock

**clock: Clock

Inherited from Page.clock

Playwright has ability to mock clock and passage of time.

### [**](#coverage)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5187)externalinheritedcoverage

**coverage: Coverage

Inherited from Page.coverage

**NOTE** Only available for Chromium atm.

Browser-specific Coverage implementation. See [Coverage](https://playwright.dev/docs/api/class-coverage) for more details.

### [**](#keyboard)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5189)externalinheritedkeyboard

**keyboard: Keyboard

Inherited from Page.keyboard

### [**](#mouse)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5191)externalinheritedmouse

**mouse: Mouse

Inherited from Page.mouse

### [**](#request)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5200)externalinheritedrequest

**request: APIRequestContext

Inherited from Page.request

API testing helper associated with this page. This method returns the same instance as [browserContext.request](https://playwright.dev/docs/api/class-browsercontext#browser-context-request) on the page's context. See [browserContext.request](https://playwright.dev/docs/api/class-browsercontext#browser-context-request) for more details.

### [**](#touchscreen)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5202)externalinheritedtouchscreen

**touchscreen: Touchscreen

Inherited from Page.touchscreen

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncDispose])[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5204)externalinherited\[asyncDispose]

* ****\[asyncDispose]**(): Promise\<void>

- Inherited from Page.\[asyncDispose]

  #### Returns Promise\<void>

### [**](#$)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L319)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L330)externalinherited$

* ****$**\<K>(selector, options): Promise\<null | ElementHandleForTag\<K>>
* ****$**(selector, options): Promise\<null | ElementHandle\<HTMLElement | SVGElement>>

- Inherited from Page.$

  **NOTE** Use locator-based [page.locator(selector\[, options\])](https://playwright.dev/docs/api/class-page#page-locator) instead. Read more about [locators](https://playwright.dev/docs/locators).

  The method finds an element matching the specified selector within the page. If no elements match the selector, the return value resolves to `null`. To wait for an element on the page, use [locator.waitFor(\[options\])](https://playwright.dev/docs/api/class-locator#locator-wait-for).

  ***

  #### Parameters

  * ##### externalselector: K

    A selector to query for.

  * ##### externaloptionaloptions: { strict: boolean }
    * ##### externalstrict: boolean

  #### Returns Promise\<null | ElementHandleForTag\<K>>

### [**](#$$)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L340)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L349)externalinherited$$

* ****$$**\<K>(selector): Promise\<ElementHandleForTag\<K>\[]>
* ****$$**(selector): Promise\<ElementHandle\<HTMLElement | SVGElement>\[]>

- Inherited from Page.$$

  **NOTE** Use locator-based [page.locator(selector\[, options\])](https://playwright.dev/docs/api/class-page#page-locator) instead. Read more about [locators](https://playwright.dev/docs/locators).

  The method finds all elements matching the specified selector within the page. If no elements match the selector, the return value resolves to `[]`.

  ***

  #### Parameters

  * ##### externalselector: K

    A selector to query for.

  #### Returns Promise\<ElementHandleForTag\<K>\[]>

### [**](#$$eval)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L513)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L543)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L573)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L603)externalinherited$$eval

* ****$$eval**\<K, R, Arg>(selector, pageFunction, arg): Promise\<R>
* ****$$eval**\<R, Arg, E>(selector, pageFunction, arg): Promise\<R>
* ****$$eval**\<K, R>(selector, pageFunction, arg): Promise\<R>
* ****$$eval**\<R, E>(selector, pageFunction, arg): Promise\<R>

- Inherited from Page.$$eval

  **NOTE** In most cases, [locator.evaluateAll(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-locator#locator-evaluate-all), other [Locator](https://playwright.dev/docs/api/class-locator) helper methods and web-first assertions do a better job.

  The method finds all elements matching the specified selector within the page and passes an array of matched elements as a first argument to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-all-option-expression). Returns the result of [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-all-option-expression) invocation.

  If [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-all-option-expression) returns a \[Promise], then [page.$$eval(selector, pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-eval-on-selector-all) would wait for the promise to resolve and return its value.

  **Usage**

  ```
  const divCounts = await page.$$eval('div', (divs, min) => divs.length >= min, 10);
  ```

  ***

  #### Parameters

  * ##### externalselector: K

    A selector to query for.

  * ##### externalpageFunction: PageFunctionOn\<HTMLElementTagNameMap\[K]\[], Arg, R>

    Function to be evaluated in the page context.

  * ##### externalarg: Arg

    Optional argument to pass to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-all-option-expression).

  #### Returns Promise\<R>

### [**](#$eval)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L383)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L416)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L449)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L482)externalinherited$eval

* ****$eval**\<K, R, Arg>(selector, pageFunction, arg): Promise\<R>
* ****$eval**\<R, Arg, E>(selector, pageFunction, arg): Promise\<R>
* ****$eval**\<K, R>(selector, pageFunction, arg): Promise\<R>
* ****$eval**\<R, E>(selector, pageFunction, arg): Promise\<R>

- Inherited from Page.$eval

  **NOTE** This method does not wait for the element to pass actionability checks and therefore can lead to the flaky tests. Use [locator.evaluate(pageFunction\[, arg, options\])](https://playwright.dev/docs/api/class-locator#locator-evaluate), other [Locator](https://playwright.dev/docs/api/class-locator) helper methods or web-first assertions instead.

  The method finds an element matching the specified selector within the page and passes it as a first argument to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-option-expression). If no elements match the selector, the method throws an error. Returns the value of [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-option-expression).

  If [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-option-expression) returns a \[Promise], then [page.$eval(selector, pageFunction\[, arg, options\])](https://playwright.dev/docs/api/class-page#page-eval-on-selector) would wait for the promise to resolve and return its value.

  **Usage**

  ```
  const searchValue = await page.$eval('#search', el => el.value);
  const preloadHref = await page.$eval('link[rel=preload]', el => el.href);
  const html = await page.$eval('.main-container', (e, suffix) => e.outerHTML + suffix, 'hello');
  // In TypeScript, this example requires an explicit type annotation (HTMLLinkElement) on el:
  const preloadHrefTS = await page.$eval('link[rel=preload]', (el: HTMLLinkElement) => el.href);
  ```

  ***

  #### Parameters

  * ##### externalselector: K

    A selector to query for.

  * ##### externalpageFunction: PageFunctionOn\<HTMLElementTagNameMap\[K], Arg, R>

    Function to be evaluated in the page context.

  * ##### externalarg: Arg

    Optional argument to pass to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-eval-on-selector-option-expression).

  #### Returns Promise\<R>

### [**](#act)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L151)act

* ****act**(instruction, options): Promise<[ActResult](https://crawlee.dev/js/api/stagehand-crawler/interface/ActResult.md)>

- Perform an action on the page using natural language.

  * **@example**

    ```
    await page.act('Click the login button');
    await page.act('Fill in email with test@example.com');
    await page.act('Scroll down to load more items');
    ```

  ***

  #### Parameters

  * ##### instruction: string

    Natural language instruction for the action

  * ##### optionaloptions: Omit<[ActOptions](https://crawlee.dev/js/api/stagehand-crawler/interface/ActOptions.md), page>

    Optional configuration for the action

  #### Returns Promise<[ActResult](https://crawlee.dev/js/api/stagehand-crawler/interface/ActResult.md)>

  Promise that resolves with the action result

### [**](#addInitScript)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L307)externalinheritedaddInitScript

* ****addInitScript**\<Arg>(script, arg): Promise\<void>

- Inherited from Page.addInitScript

  Adds a script which would be evaluated in one of the following scenarios:

  * Whenever the page is navigated.
  * Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the newly attached frame.

  The script is evaluated after the document was created but before any of its scripts were run. This is useful to amend the JavaScript environment, e.g. to seed `Math.random`.

  **Usage**

  An example of overriding `Math.random` before the page loads:

  ```
  // preload.js
  Math.random = () => 42;
  ```

  ```
  // In your playwright script, assuming the preload.js file is in same directory
  await page.addInitScript({ path: './preload.js' });
  ```

  ```
  await page.addInitScript(mock => {
    window.mock = mock;
  }, mock);
  ```

  **NOTE** The order of evaluation of multiple scripts installed via [browserContext.addInitScript(script\[, arg\])](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script) and [page.addInitScript(script\[, arg\])](https://playwright.dev/docs/api/class-page#page-add-init-script) is not defined.

  ***

  #### Parameters

  * ##### externalscript: PageFunction\<Arg, any> | { content?<!-- -->: string; path?<!-- -->: string }

    Script to be evaluated in the page.

  * * ##### externaloptionalcontent: string
    * ##### externaloptionalpath: string

    ##### externaloptionalarg: Arg

    Optional argument to pass to [`script`](https://playwright.dev/docs/api/class-page#page-add-init-script-option-script) (only supported when passing a function).

  #### Returns Promise\<void>

### [**](#addListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1321)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1342)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1362)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1382)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1388)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1394)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1409)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1414)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1419)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1424)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1429)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1445)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1474)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1481)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1500)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1506)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1512)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1517)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1523)externalinheritedaddListener

* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this
* ****addListener**(event, listener): this

- Inherited from Page.addListener

  Emitted when the page closes.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#addLocatorHandler)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2025)externalinheritedaddLocatorHandler

* ****addLocatorHandler**(locator, handler, options): Promise\<void>

- Inherited from Page.addLocatorHandler

  When testing a web page, sometimes unexpected overlays like a "Sign up" dialog appear and block actions you want to automate, e.g. clicking a button. These overlays don't always show up in the same way or at the same time, making them tricky to handle in automated tests.

  This method lets you set up a special function, called a handler, that activates when it detects that overlay is visible. The handler's job is to remove the overlay, allowing your test to continue as if the overlay wasn't there.

  Things to keep in mind:

  * When an overlay is shown predictably, we recommend explicitly waiting for it in your test and dismissing it as a part of your normal test flow, instead of using [page.addLocatorHandler(locator, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-add-locator-handler).
  * Playwright checks for the overlay every time before executing or retrying an action that requires an [actionability check](https://playwright.dev/docs/actionability), or before performing an auto-waiting assertion check. When overlay is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't perform any actions, the handler will not be triggered.
  * After executing the handler, Playwright will ensure that overlay that triggered the handler is not visible anymore. You can opt-out of this behavior with [`noWaitAfter`](https://playwright.dev/docs/api/class-page#page-add-locator-handler-option-no-wait-after).
  * The execution time of the handler counts towards the timeout of the action/assertion that executed the handler. If your handler takes too long, it might cause timeouts.
  * You can register multiple handlers. However, only a single handler will be running at a time. Make sure the actions within a handler don't depend on another handler.

  **NOTE** Running the handler will alter your page state mid-test. For example it will change the currently focused element and move the mouse. Make sure that actions that run after the handler are self-contained and do not rely on the focus and mouse state being unchanged.

  For example, consider a test that calls [locator.focus(\[options\])](https://playwright.dev/docs/api/class-locator#locator-focus) followed by [keyboard.press(key\[, options\])](https://playwright.dev/docs/api/class-keyboard#keyboard-press). If your handler clicks a button between these two actions, the focused element most likely will be wrong, and key press will happen on the unexpected element. Use [locator.press(key\[, options\])](https://playwright.dev/docs/api/class-locator#locator-press) instead to avoid this problem.

  Another example is a series of mouse actions, where [mouse.move(x, y\[, options\])](https://playwright.dev/docs/api/class-mouse#mouse-move) is followed by [mouse.down(\[options\])](https://playwright.dev/docs/api/class-mouse#mouse-down). Again, when the handler runs between these two actions, the mouse position will be wrong during the mouse down. Prefer self-contained actions like [locator.click(\[options\])](https://playwright.dev/docs/api/class-locator#locator-click) that do not rely on the state being unchanged by a handler.

  **Usage**

  An example that closes a "Sign up to the newsletter" dialog when it appears:

  ```
  // Setup the handler.
  await page.addLocatorHandler(page.getByText('Sign up to the newsletter'), async () => {
    await page.getByRole('button', { name: 'No thanks' }).click();
  });

  // Write the test as usual.
  await page.goto('https://example.com');
  await page.getByRole('button', { name: 'Start here' }).click();
  ```

  An example that skips the "Confirm your security details" page when it is shown:

  ```
  // Setup the handler.
  await page.addLocatorHandler(page.getByText('Confirm your security details'), async () => {
    await page.getByRole('button', { name: 'Remind me later' }).click();
  });

  // Write the test as usual.
  await page.goto('https://example.com');
  await page.getByRole('button', { name: 'Start here' }).click();
  ```

  An example with a custom callback on every actionability check. It uses a `<body>` locator that is always visible, so the handler is called before every actionability check. It is important to specify [`noWaitAfter`](https://playwright.dev/docs/api/class-page#page-add-locator-handler-option-no-wait-after), because the handler does not hide the `<body>` element.

  ```
  // Setup the handler.
  await page.addLocatorHandler(page.locator('body'), async () => {
    await page.evaluate(() => window.removeObstructionsForTestIfNeeded());
  }, { noWaitAfter: true });

  // Write the test as usual.
  await page.goto('https://example.com');
  await page.getByRole('button', { name: 'Start here' }).click();
  ```

  Handler takes the original locator as an argument. You can also automatically remove the handler after a number of invocations by setting [`times`](https://playwright.dev/docs/api/class-page#page-add-locator-handler-option-times):

  ```
  await page.addLocatorHandler(page.getByLabel('Close'), async locator => {
    await locator.click();
  }, { times: 1 });
  ```

  ***

  #### Parameters

  * ##### externallocator: Locator

    Locator that triggers the handler.

  * ##### externalhandler: (locator) => Promise\<any>

    Function that should be run once [`locator`](https://playwright.dev/docs/api/class-page#page-add-locator-handler-option-locator) appears. This function should get rid of the element that blocks actions like click.

  *
    ##### externaloptionaloptions: { noWaitAfter?<!-- -->: boolean; times?<!-- -->: number }
    * ##### externaloptionalnoWaitAfter: boolean

      By default, after calling the handler Playwright will wait until the overlay becomes hidden, and only then Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of this behavior, so that overlay can stay visible after the handler has run.

    * ##### externaloptionaltimes: number

      Specifies the maximum number of times this handler should be called. Unlimited by default.

  #### Returns Promise\<void>

### [**](#addScriptTag)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2044)externalinheritedaddScriptTag

* ****addScriptTag**(options): Promise\<ElementHandle\<Node>>

- Inherited from Page.addScriptTag

  Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload fires or when the script content was injected into frame.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { content?<!-- -->: string; path?<!-- -->: string; type?<!-- -->: string; url?<!-- -->: string }
    * ##### externaloptionalcontent: string

      Raw JavaScript content to be injected into frame.

    * ##### externaloptionalpath: string

      Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory.

    * ##### externaloptionaltype: string

      Script type. Use 'module' in order to load a JavaScript ES6 module. See [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details.

    * ##### externaloptionalurl: string

      URL of a script to be added.

  #### Returns Promise\<ElementHandle\<Node>>

### [**](#addStyleTag)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2073)externalinheritedaddStyleTag

* ****addStyleTag**(options): Promise\<ElementHandle\<Node>>

- Inherited from Page.addStyleTag

  Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { content?<!-- -->: string; path?<!-- -->: string; url?<!-- -->: string }
    * ##### externaloptionalcontent: string

      Raw CSS content to be injected into frame.

    * ##### externaloptionalpath: string

      Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory.

    * ##### externaloptionalurl: string

      URL of the `<link>` tag.

  #### Returns Promise\<ElementHandle\<Node>>

### [**](#agent)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L200)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L201)agent

* ****agent**(config): StreamingAgentInstance
* ****agent**(config): NonStreamingAgentInstance

- Create an autonomous agent for multi-step workflows.

  * **@example**

    ```
    const agent = page.agent({ task: 'Find and add cheapest laptop to cart' });
    await agent.execute();
    ```

  ***

  #### Parameters

  * ##### config: [AgentConfig](https://crawlee.dev/js/api/stagehand-crawler.md#AgentConfig) & { stream: true }

    Configuration for the agent

  #### Returns StreamingAgentInstance

  Agent instance that can execute complex workflows

### [**](#bringToFront)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2094)externalinheritedbringToFront

* ****bringToFront**(): Promise\<void>

- Inherited from Page.bringToFront

  Brings page to front (activates tab).

  ***

  #### Returns Promise\<void>

### [**](#check)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2122)externalinheritedcheck

* ****check**(selector, options): Promise\<void>

- Inherited from Page.check

  **NOTE** Use locator-based [locator.check(\[options\])](https://playwright.dev/docs/api/class-locator#locator-check) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method checks an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-check-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-check-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is already checked, this method returns immediately.
  3. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-check-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  4. Scroll the element into view if needed.
  5. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to click in the center of the element.
  6. Ensure that the element is now checked. If not, this method throws.

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-check-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

  #### Returns Promise\<void>

### [**](#click)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2191)externalinheritedclick

* ****click**(selector, options): Promise\<void>

- Inherited from Page.click

  **NOTE** Use locator-based [locator.click(\[options\])](https://playwright.dev/docs/api/class-locator#locator-click) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method clicks an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-click-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-click-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-click-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  3. Scroll the element into view if needed.
  4. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to click in the center of the element, or the specified [`position`](https://playwright.dev/docs/api/class-page#page-click-option-position).
  5. Wait for initiated navigations to either succeed or fail, unless [`noWaitAfter`](https://playwright.dev/docs/api/class-page#page-click-option-no-wait-after) option is set.

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-click-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { button?<!-- -->: left | right | middle; clickCount?<!-- -->: number; delay?<!-- -->: number; force?<!-- -->: boolean; modifiers?<!-- -->: (Alt | Control | ControlOrMeta | Meta | Shift)\[]; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalbutton: left | right | middle

      Defaults to `left`.

    * ##### externaloptionalclickCount: number

      defaults to 1. See \[UIEvent.detail].

    * ##### externaloptionaldelay: number

      Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalmodifiers: (Alt | Control | ControlOrMeta | Meta | Shift)\[]

      Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.

    * ##### externaloptionalnoWaitAfter: boolean

      Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.

      * **@deprecated**

        This option will default to `true` in the future.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

  #### Returns Promise\<void>

### [**](#close)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2274)externalinheritedclose

* ****close**(options): Promise\<void>

- Inherited from Page.close

  If [`runBeforeUnload`](https://playwright.dev/docs/api/class-page#page-close-option-run-before-unload) is `false`, does not run any unload handlers and waits for the page to be closed. If [`runBeforeUnload`](https://playwright.dev/docs/api/class-page#page-close-option-run-before-unload) is `true` the method will run unload handlers, but will **not** wait for the page to close.

  By default, `page.close()` **does not** run `beforeunload` handlers.

  **NOTE** if [`runBeforeUnload`](https://playwright.dev/docs/api/class-page#page-close-option-run-before-unload) is passed as true, a `beforeunload` dialog might be summoned and should be handled manually via [page.on('dialog')](https://playwright.dev/docs/api/class-page#page-event-dialog) event.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { reason?<!-- -->: string; runBeforeUnload?<!-- -->: boolean }
    * ##### externaloptionalreason: string

      The reason to be reported to the operations interrupted by the page closure.

    * ##### externaloptionalrunBeforeUnload: boolean

      Defaults to `false`. Whether to run the [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers.

  #### Returns Promise\<void>

### [**](#consoleMessages)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2291)externalinheritedconsoleMessages

* ****consoleMessages**(): Promise\<ConsoleMessage\[]>

- Inherited from Page.consoleMessages

  Returns up to (currently) 200 last console messages from this page. See [page.on('console')](https://playwright.dev/docs/api/class-page#page-event-console) for more details.

  ***

  #### Returns Promise\<ConsoleMessage\[]>

### [**](#content)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2296)externalinheritedcontent

* ****content**(): Promise\<string>

- Inherited from Page.content

  Gets the full HTML contents of the page, including the doctype.

  ***

  #### Returns Promise\<string>

### [**](#context)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2301)externalinheritedcontext

* ****context**(): BrowserContext

- Inherited from Page.context

  Get the browser context that the page belongs to.

  ***

  #### Returns BrowserContext

### [**](#dblclick)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2331)externalinheriteddblclick

* ****dblclick**(selector, options): Promise\<void>

- Inherited from Page.dblclick

  **NOTE** Use locator-based [locator.dblclick(\[options\])](https://playwright.dev/docs/api/class-locator#locator-dblclick) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method double clicks an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-dblclick-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-dblclick-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-dblclick-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  3. Scroll the element into view if needed.
  4. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to double click in the center of the element, or the specified [`position`](https://playwright.dev/docs/api/class-page#page-dblclick-option-position).

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-dblclick-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  **NOTE** `page.dblclick()` dispatches two `click` events and a single `dblclick` event.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { button?<!-- -->: left | right | middle; delay?<!-- -->: number; force?<!-- -->: boolean; modifiers?<!-- -->: (Alt | Control | ControlOrMeta | Meta | Shift)\[]; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalbutton: left | right | middle

      Defaults to `left`.

    * ##### externaloptionaldelay: number

      Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalmodifiers: (Alt | Control | ControlOrMeta | Meta | Shift)\[]

      Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

  #### Returns Promise\<void>

### [**](#dispatchEvent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2440)externalinheriteddispatchEvent

* ****dispatchEvent**(selector, type, eventInit, options): Promise\<void>

- Inherited from Page.dispatchEvent

  **NOTE** Use locator-based [locator.dispatchEvent(type\[, eventInit, options\])](https://playwright.dev/docs/api/class-locator#locator-dispatch-event) instead. Read more about [locators](https://playwright.dev/docs/locators).

  The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element, `click` is dispatched. This is equivalent to calling [element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

  **Usage**

  ```
  await page.dispatchEvent('button#submit', 'click');
  ```

  Under the hood, it creates an instance of an event based on the given [`type`](https://playwright.dev/docs/api/class-page#page-dispatch-event-option-type), initializes it with [`eventInit`](https://playwright.dev/docs/api/class-page#page-dispatch-event-option-event-init) properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

  Since [`eventInit`](https://playwright.dev/docs/api/class-page#page-dispatch-event-option-event-init) is event-specific, please refer to the events documentation for the lists of initial properties:

  * [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)
  * [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)
  * [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
  * [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
  * [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
  * [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
  * [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
  * [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
  * [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
  * [WheelEvent](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/WheelEvent)

  You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

  ```
  // Note you can only create DataTransfer in Chromium and Firefox
  const dataTransfer = await page.evaluateHandle(() => new DataTransfer());
  await page.dispatchEvent('#source', 'dragstart', { dataTransfer });
  ```

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaltype: string

    DOM event type: `"click"`, `"dragstart"`, etc.

  * ##### externaloptionaleventInit: EvaluationArgument

    Optional event-specific initialization properties.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#dragAndDrop)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2477)externalinheriteddragAndDrop

* ****dragAndDrop**(source, target, options): Promise\<void>

- Inherited from Page.dragAndDrop

  This method drags the source element to the target element. It will first move to the source element, perform a `mousedown`, then move to the target element and perform a `mouseup`.

  **Usage**

  ```
  await page.dragAndDrop('#source', '#target');
  // or specify exact positions relative to the top-left corners of the elements:
  await page.dragAndDrop('#source', '#target', {
    sourcePosition: { x: 34, y: 7 },
    targetPosition: { x: 10, y: 20 },
  });
  ```

  ***

  #### Parameters

  * ##### externalsource: string

    A selector to search for an element to drag. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaltarget: string

    A selector to search for an element to drop onto. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; sourcePosition?<!-- -->: { x: number; y: number }; steps?<!-- -->: number; strict?<!-- -->: boolean; targetPosition?<!-- -->: { x: number; y: number }; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalsourcePosition: { x: number; y: number }

      Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used.

    * ##### externaloptionalsteps: number

      Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltargetPosition: { x: number; y: number }

      Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

  #### Returns Promise\<void>

### [**](#emulateMedia)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2571)externalinheritedemulateMedia

* ****emulateMedia**(options): Promise\<void>

- Inherited from Page.emulateMedia

  This method changes the `CSS media type` through the `media` argument, and/or the `'prefers-colors-scheme'` media feature, using the `colorScheme` argument.

  **Usage**

  ```
  await page.evaluate(() => matchMedia('screen').matches);
  // → true
  await page.evaluate(() => matchMedia('print').matches);
  // → false

  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => matchMedia('screen').matches);
  // → false
  await page.evaluate(() => matchMedia('print').matches);
  // → true

  await page.emulateMedia({});
  await page.evaluate(() => matchMedia('screen').matches);
  // → true
  await page.evaluate(() => matchMedia('print').matches);
  // → false
  ```

  ```
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.evaluate(() => matchMedia('(prefers-color-scheme: dark)').matches);
  // → true
  await page.evaluate(() => matchMedia('(prefers-color-scheme: light)').matches);
  // → false
  ```

  ***

  #### Parameters

  * ##### externaloptionaloptions: { colorScheme?<!-- -->: null | light | dark | no-preference; contrast?<!-- -->: null | no-preference | more; forcedColors?<!-- -->: null | active | none; media?<!-- -->: null | screen | print; reducedMotion?<!-- -->: null | reduce | no-preference }
    * ##### externaloptionalcolorScheme: null | light | dark | no-preference

      Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. Passing `null` disables color scheme emulation. `'no-preference'` is deprecated.

    * ##### externaloptionalcontrast: null | no-preference | more

      Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. Passing `null` disables contrast emulation.

    * ##### externaloptionalforcedColors: null | active | none

      Emulates `'forced-colors'` media feature, supported values are `'active'` and `'none'`. Passing `null` disables forced colors emulation.

    * ##### externaloptionalmedia: null | screen | print

      Changes the CSS media type of the page. The only allowed values are `'screen'`, `'print'` and `null`. Passing `null` disables CSS media emulation.

    * ##### externaloptionalreducedMotion: null | reduce | no-preference

      Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. Passing `null` disables reduced motion emulation.

  #### Returns Promise\<void>

### [**](#evaluate)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L124)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L175)externalinheritedevaluate

* ****evaluate**\<R, Arg>(pageFunction, arg): Promise\<R>
* ****evaluate**\<R>(pageFunction, arg): Promise\<R>

- Inherited from Page.evaluate

  Returns the value of the [`pageFunction`](https://playwright.dev/docs/api/class-page#page-evaluate-option-expression) invocation.

  If the function passed to the [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate) returns a \[Promise], then [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate) would wait for the promise to resolve and return its value.

  If the function passed to the [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate) returns a non-\[Serializable] value, then [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate) resolves to `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

  **Usage**

  Passing argument to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-evaluate-option-expression):

  ```
  const result = await page.evaluate(([x, y]) => {
    return Promise.resolve(x * y);
  }, [7, 8]);
  console.log(result); // prints "56"
  ```

  A string can also be passed in instead of a function:

  ```
  console.log(await page.evaluate('1 + 2')); // prints "3"
  const x = 10;
  console.log(await page.evaluate(`1 + ${x}`)); // prints "11"
  ```

  [ElementHandle](https://playwright.dev/docs/api/class-elementhandle) instances can be passed as an argument to the [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate):

  ```
  const bodyHandle = await page.evaluate('document.body');
  const html = await page.evaluate<string, HTMLElement>(([body, suffix]) =>
    body.innerHTML + suffix, [bodyHandle, 'hello']
  );
  await bodyHandle.dispose();
  ```

  ***

  #### Parameters

  * ##### externalpageFunction: PageFunction\<Arg, R>

    Function to be evaluated in the page context.

  * ##### externalarg: Arg

    Optional argument to pass to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-evaluate-option-expression).

  #### Returns Promise\<R>

### [**](#evaluateHandle)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L221)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L266)externalinheritedevaluateHandle

* ****evaluateHandle**\<R, Arg>(pageFunction, arg): Promise\<SmartHandle\<R>>
* ****evaluateHandle**\<R>(pageFunction, arg): Promise\<SmartHandle\<R>>

- Inherited from Page.evaluateHandle

  Returns the value of the [`pageFunction`](https://playwright.dev/docs/api/class-page#page-evaluate-handle-option-expression) invocation as a [JSHandle](https://playwright.dev/docs/api/class-jshandle).

  The only difference between [page.evaluate(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate) and [page.evaluateHandle(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate-handle) is that [page.evaluateHandle(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate-handle) returns [JSHandle](https://playwright.dev/docs/api/class-jshandle).

  If the function passed to the [page.evaluateHandle(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate-handle) returns a \[Promise], then [page.evaluateHandle(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate-handle) would wait for the promise to resolve and return its value.

  **Usage**

  ```
  // Handle for the window object.
  const aWindowHandle = await page.evaluateHandle(() => Promise.resolve(window));
  ```

  A string can also be passed in instead of a function:

  ```
  const aHandle = await page.evaluateHandle('document'); // Handle for the 'document'
  ```

  [JSHandle](https://playwright.dev/docs/api/class-jshandle) instances can be passed as an argument to the [page.evaluateHandle(pageFunction\[, arg\])](https://playwright.dev/docs/api/class-page#page-evaluate-handle):

  ```
  const aHandle = await page.evaluateHandle(() => document.body);
  const resultHandle = await page.evaluateHandle(body => body.innerHTML, aHandle);
  console.log(await resultHandle.jsonValue());
  await resultHandle.dispose();
  ```

  ***

  #### Parameters

  * ##### externalpageFunction: PageFunction\<Arg, R>

    Function to be evaluated in the page context.

  * ##### externalarg: Arg

    Optional argument to pass to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-evaluate-handle-option-expression).

  #### Returns Promise\<SmartHandle\<R>>

### [**](#exposeBinding)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L912)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L964)externalinheritedexposeBinding

* ****exposeBinding**(name, playwrightBinding, options): Promise\<void>
* ****exposeBinding**(name, playwrightBinding, options): Promise\<void>

- Inherited from Page.exposeBinding

  The method adds a function called [`name`](https://playwright.dev/docs/api/class-page#page-expose-binding-option-name) on the `window` object of every frame in this page. When called, the function executes [`callback`](https://playwright.dev/docs/api/class-page#page-expose-binding-option-callback) and returns a \[Promise] which resolves to the return value of [`callback`](https://playwright.dev/docs/api/class-page#page-expose-binding-option-callback). If the [`callback`](https://playwright.dev/docs/api/class-page#page-expose-binding-option-callback) returns a \[Promise], it will be awaited.

  The first argument of the [`callback`](https://playwright.dev/docs/api/class-page#page-expose-binding-option-callback) function contains information about the caller: `{ browserContext: BrowserContext, page: Page, frame: Frame }`.

  See [browserContext.exposeBinding(name, callback\[, options\])](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-binding) for the context-wide version.

  **NOTE** Functions installed via [page.exposeBinding(name, callback\[, options\])](https://playwright.dev/docs/api/class-page#page-expose-binding) survive navigations.

  **Usage**

  An example of exposing page URL to all frames in a page:

  ```
  const { webkit } = require('playwright');  // Or 'chromium' or 'firefox'.

  (async () => {
    const browser = await webkit.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.exposeBinding('pageURL', ({ page }) => page.url());
    await page.setContent(`
      <script>
        async function onClick() {
          document.querySelector('div').textContent = await window.pageURL();
        }
      </script>
      <button onclick="onClick()">Click me</button>
      <div></div>
    `);
    await page.click('button');
  })();
  ```

  ***

  #### Parameters

  * ##### externalname: string

    Name of the function on the window object.

  * ##### externalplaywrightBinding: (source, arg) => any

  *
    ##### externaloptions: { handle: true }
    * ##### externalhandle: true

  #### Returns Promise\<void>

### [**](#exposeFunction)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2653)externalinheritedexposeFunction

* ****exposeFunction**(name, callback): Promise\<void>

- Inherited from Page.exposeFunction

  The method adds a function called [`name`](https://playwright.dev/docs/api/class-page#page-expose-function-option-name) on the `window` object of every frame in the page. When called, the function executes [`callback`](https://playwright.dev/docs/api/class-page#page-expose-function-option-callback) and returns a \[Promise] which resolves to the return value of [`callback`](https://playwright.dev/docs/api/class-page#page-expose-function-option-callback).

  If the [`callback`](https://playwright.dev/docs/api/class-page#page-expose-function-option-callback) returns a \[Promise], it will be awaited.

  See [browserContext.exposeFunction(name, callback)](https://playwright.dev/docs/api/class-browsercontext#browser-context-expose-function) for context-wide exposed function.

  **NOTE** Functions installed via [page.exposeFunction(name, callback)](https://playwright.dev/docs/api/class-page#page-expose-function) survive navigations.

  **Usage**

  An example of adding a `sha256` function to the page:

  ```
  const { webkit } = require('playwright');  // Or 'chromium' or 'firefox'.
  const crypto = require('crypto');

  (async () => {
    const browser = await webkit.launch({ headless: false });
    const page = await browser.newPage();
    await page.exposeFunction('sha256', text =>
      crypto.createHash('sha256').update(text).digest('hex'),
    );
    await page.setContent(`
      <script>
        async function onClick() {
          document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
        }
      </script>
      <button onclick="onClick()">Click me</button>
      <div></div>
    `);
    await page.click('button');
  })();
  ```

  ***

  #### Parameters

  * ##### externalname: string

    Name of the function on the window object

  * ##### externalcallback: Function

    Callback function which will be called in Playwright's context.

  #### Returns Promise\<void>

### [**](#extract)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L172)extract

* ****extract**\<T>(instruction, schema, options): Promise\<T>

- Extract structured data from the page using natural language and a Zod schema.

  * **@example**

    ```
    const data = await page.extract(
      'Get product title and price',
      z.object({
        title: z.string(),
        price: z.number(),
      })
    );
    ```

  ***

  #### Parameters

  * ##### instruction: string

    Natural language description of what to extract

  * ##### schema: ZodType\<T, unknown, $ZodTypeInternals\<T, unknown>>

    Zod schema defining the structure of the data

  * ##### optionaloptions: Omit<[ExtractOptions](https://crawlee.dev/js/api/stagehand-crawler/interface/ExtractOptions.md), page>

    Optional configuration for the extraction

  #### Returns Promise\<T>

  Promise that resolves with the extracted data matching the schema

### [**](#fill)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2676)externalinheritedfill

* ****fill**(selector, value, options): Promise\<void>

- Inherited from Page.fill

  **NOTE** Use locator-based [locator.fill(value\[, options\])](https://playwright.dev/docs/api/class-locator#locator-fill) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method waits for an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-fill-option-selector), waits for [actionability](https://playwright.dev/docs/actionability) checks, focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string to clear the input field.

  If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled instead.

  To send fine-grained keyboard events, use [locator.pressSequentially(text\[, options\])](https://playwright.dev/docs/api/class-locator#locator-press-sequentially).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalvalue: string

    Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#focus)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2715)externalinheritedfocus

* ****focus**(selector, options): Promise\<void>

- Inherited from Page.focus

  **NOTE** Use locator-based [locator.focus(\[options\])](https://playwright.dev/docs/api/class-locator#locator-focus) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method fetches an element with [`selector`](https://playwright.dev/docs/api/class-page#page-focus-option-selector) and focuses it. If there's no element matching [`selector`](https://playwright.dev/docs/api/class-page#page-focus-option-selector), the method waits until a matching element appears in the DOM.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#frame)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2746)externalinheritedframe

* ****frame**(frameSelector): null | Frame

- Inherited from Page.frame

  Returns frame matching the specified criteria. Either `name` or `url` must be specified.

  **Usage**

  ```
  const frame = page.frame('frame-name');
  ```

  ```
  const frame = page.frame({ url: /.*domain.*/ });
  ```

  ***

  #### Parameters

  * ##### externalframeSelector: string | { name?<!-- -->: string; url?<!-- -->: string | RegExp | (url) => boolean }

    Frame name or other frame lookup options.

    * ##### externaloptionalname: string

      Frame name specified in the `iframe`'s `name` attribute. Optional.

    * ##### externaloptionalurl: string | RegExp | (url) => boolean

      A glob pattern, regex pattern or predicate receiving frame's `url` as a \[URL] object. Optional.

  #### Returns null | Frame

### [**](#frameLocator)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2774)externalinheritedframeLocator

* ****frameLocator**(selector): FrameLocator

- Inherited from Page.frameLocator

  When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements in that iframe.

  **Usage**

  Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like

  ```
  <iframe
  id="my-frame">
  ```

  :

  ```
  const locator = page.frameLocator('#my-iframe').getByText('Submit');
  await locator.click();
  ```

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to use when resolving DOM element.

  #### Returns FrameLocator

### [**](#frames)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2779)externalinheritedframes

* ****frames**(): Frame\[]

- Inherited from Page.frames

  An array of all frames attached to the page.

  ***

  #### Returns Frame\[]

### [**](#getAttribute)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2792)externalinheritedgetAttribute

* ****getAttribute**(selector, name, options): Promise\<null | string>

- Inherited from Page.getAttribute

  **NOTE** Use locator-based [locator.getAttribute(name\[, options\])](https://playwright.dev/docs/api/class-locator#locator-get-attribute) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns element attribute value.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalname: string

    Attribute name to get the value for.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<null | string>

### [**](#getByAltText)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2826)externalinheritedgetByAltText

* ****getByAltText**(text, options): Locator

- Inherited from Page.getByAltText

  Allows locating elements by their alt text.

  **Usage**

  For example, this method will find the image by alt text "Playwright logo":

  ```
  <img alt='Playwright logo'>
  ```

  ```
  await page.getByAltText('Playwright logo').click();
  ```

  ***

  #### Parameters

  * ##### externaltext: string | RegExp

    Text to locate the element for.

  * ##### externaloptionaloptions: { exact?<!-- -->: boolean }
    * ##### externaloptionalexact: boolean

      Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

  #### Returns Locator

### [**](#getByLabel)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2856)externalinheritedgetByLabel

* ****getByLabel**(text, options): Locator

- Inherited from Page.getByLabel

  Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the `aria-label` attribute.

  **Usage**

  For example, this method will find inputs by label "Username" and "Password" in the following DOM:

  ```
  <input aria-label="Username">
  <label for="password-input">Password:</label>
  <input id="password-input">
  ```

  ```
  await page.getByLabel('Username').fill('john');
  await page.getByLabel('Password').fill('secret');
  ```

  ***

  #### Parameters

  * ##### externaltext: string | RegExp

    Text to locate the element for.

  * ##### externaloptionaloptions: { exact?<!-- -->: boolean }
    * ##### externaloptionalexact: boolean

      Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

  #### Returns Locator

### [**](#getByPlaceholder)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2886)externalinheritedgetByPlaceholder

* ****getByPlaceholder**(text, options): Locator

- Inherited from Page.getByPlaceholder

  Allows locating input elements by the placeholder text.

  **Usage**

  For example, consider the following DOM structure.

  ```
  <input type="email" placeholder="name@example.com" />
  ```

  You can fill the input after locating it by the placeholder text:

  ```
  await page
      .getByPlaceholder('name@example.com')
      .fill('playwright@microsoft.com');
  ```

  ***

  #### Parameters

  * ##### externaltext: string | RegExp

    Text to locate the element for.

  * ##### externaloptionaloptions: { exact?<!-- -->: boolean }
    * ##### externaloptionalexact: boolean

      Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

  #### Returns Locator

### [**](#getByRole)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L2934)externalinheritedgetByRole

* ****getByRole**(role, options): Locator

- Inherited from Page.getByRole

  Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles), [ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

  **Usage**

  Consider the following DOM structure.

  ```
  <h3>Sign up</h3>
  <label>
    <input type="checkbox" /> Subscribe
  </label>
  <br/>
  <button>Submit</button>
  ```

  You can locate each element by it's implicit role:

  ```
  await expect(page.getByRole('heading', { name: 'Sign up' })).toBeVisible();

  await page.getByRole('checkbox', { name: 'Subscribe' }).check();

  await page.getByRole('button', { name: /submit/i }).click();
  ```

  **Details**

  Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback about the ARIA guidelines.

  Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings) that is recognized by the role selector. You can find all the [supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend** duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

  ***

  #### Parameters

  * ##### externalrole: form | search | link | log | none | document | menubar | status | toolbar | alert | article | blockquote | button | caption | code | dialog | figure | img | main | menu | meter | option | strong | table | time | alertdialog | application | banner | cell | checkbox | columnheader | combobox | complementary | contentinfo | definition | deletion | directory | emphasis | feed | generic | grid | gridcell | group | heading | insertion | list | listbox | listitem | marquee | math | menuitem | menuitemcheckbox | menuitemradio | navigation | note | paragraph | presentation | progressbar | radio | radiogroup | region | row | rowgroup | rowheader | scrollbar | searchbox | separator | slider | spinbutton | subscript | superscript | switch | tab | tablist | tabpanel | term | textbox | timer | tooltip | tree | treegrid | treeitem

    Required aria role.

  * ##### externaloptionaloptions: { checked?<!-- -->: boolean; disabled?<!-- -->: boolean; exact?<!-- -->: boolean; expanded?<!-- -->: boolean; includeHidden?<!-- -->: boolean; level?<!-- -->: number; name?<!-- -->: string | RegExp; pressed?<!-- -->: boolean; selected?<!-- -->: boolean }
    * ##### externaloptionalchecked: boolean

      An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.

      Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked).

    * ##### externaloptionaldisabled: boolean

      An attribute that is usually set by `aria-disabled` or `disabled`.

      **NOTE** Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled).

    * ##### externaloptionalexact: boolean

      Whether [`name`](https://playwright.dev/docs/api/class-page#page-get-by-role-option-name) is matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when [`name`](https://playwright.dev/docs/api/class-page#page-get-by-role-option-name) is a regular expression. Note that exact match still trims whitespace.

    * ##### externaloptionalexpanded: boolean

      An attribute that is usually set by `aria-expanded`.

      Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded).

    * ##### externaloptionalincludeHidden: boolean

      Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.

      Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden).

    * ##### externaloptionallevel: number

      A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.

      Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level).

    * ##### externaloptionalname: string | RegExp

      Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use [`exact`](https://playwright.dev/docs/api/class-page#page-get-by-role-option-exact) to control this behavior.

      Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

    * ##### externaloptionalpressed: boolean

      An attribute that is usually set by `aria-pressed`.

      Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed).

    * ##### externaloptionalselected: boolean

      An attribute that is usually set by `aria-selected`.

      Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected).

  #### Returns Locator

### [**](#getByTestId)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3042)externalinheritedgetByTestId

* ****getByTestId**(testId): Locator

- Inherited from Page.getByTestId

  Locate element by the test id.

  **Usage**

  Consider the following DOM structure.

  ```
  <button data-testid="directions">Itinéraire</button>
  ```

  You can locate the element by it's test id:

  ```
  await page.getByTestId('directions').click();
  ```

  **Details**

  By default, the `data-testid` attribute is used as a test id. Use [selectors.setTestIdAttribute(attributeName)](https://playwright.dev/docs/api/class-selectors#selectors-set-test-id-attribute) to configure a different test id attribute if necessary.

  ```
  // Set custom test id attribute from @playwright/test config:
  import { defineConfig } from '@playwright/test';

  export default defineConfig({
    use: {
      testIdAttribute: 'data-pw'
    },
  });
  ```

  ***

  #### Parameters

  * ##### externaltestId: string | RegExp

    Id to locate the element by.

  #### Returns Locator

### [**](#getByText)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3088)externalinheritedgetByText

* ****getByText**(text, options): Locator

- Inherited from Page.getByText

  Allows locating elements that contain given text.

  See also [locator.filter(\[options\])](https://playwright.dev/docs/api/class-locator#locator-filter) that allows to match by another criteria, like an accessible role, and then filter by the text content.

  **Usage**

  Consider the following DOM structure:

  ```
  <div>Hello <span>world</span></div>
  <div>Hello</div>
  ```

  You can locate by text substring, exact string, or a regular expression:

  ```
  // Matches <span>
  page.getByText('world');

  // Matches first <div>
  page.getByText('Hello world');

  // Matches second <div>
  page.getByText('Hello', { exact: true });

  // Matches both <div>s
  page.getByText(/Hello/);

  // Matches second <div>
  page.getByText(/^hello$/i);
  ```

  **Details**

  Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into one, turns line breaks into spaces and ignores leading and trailing whitespace.

  Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

  ***

  #### Parameters

  * ##### externaltext: string | RegExp

    Text to locate the element for.

  * ##### externaloptionaloptions: { exact?<!-- -->: boolean }
    * ##### externaloptionalexact: boolean

      Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

  #### Returns Locator

### [**](#getByTitle)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3116)externalinheritedgetByTitle

* ****getByTitle**(text, options): Locator

- Inherited from Page.getByTitle

  Allows locating elements by their title attribute.

  **Usage**

  Consider the following DOM structure.

  ```
  <span title='Issues count'>25 issues</span>
  ```

  You can check the issues count after locating it by the title text:

  ```
  await expect(page.getByTitle('Issues count')).toHaveText('25 issues');
  ```

  ***

  #### Parameters

  * ##### externaltext: string | RegExp

    Text to locate the element for.

  * ##### externaloptionaloptions: { exact?<!-- -->: boolean }
    * ##### externaloptionalexact: boolean

      Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace.

  #### Returns Locator

### [**](#goBack)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3131)externalinheritedgoBack

* ****goBack**(options): Promise\<null | Response>

- Inherited from Page.goBack

  Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. If cannot go back, returns `null`.

  Navigate to the previous page in history.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<null | Response>

### [**](#goForward)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3161)externalinheritedgoForward

* ****goForward**(options): Promise\<null | Response>

- Inherited from Page.goForward

  Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. If cannot go forward, returns `null`.

  Navigate to the next page in history.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<null | Response>

### [**](#goto)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3212)externalinheritedgoto

* ****goto**(url, options): Promise\<null | Response>

- Inherited from Page.goto

  Returns the main resource response. In case of multiple redirects, the navigation will resolve with the first non-redirect response.

  The method will throw an error if:

  * there's an SSL error (e.g. in case of self-signed certificates).
  * target URL is invalid.
  * the [`timeout`](https://playwright.dev/docs/api/class-page#page-goto-option-timeout) is exceeded during navigation.
  * the remote server does not respond or is unreachable.
  * the main resource failed to load.

  The method will not throw an error when any valid HTTP status code is returned by the remote server, including 404 "Not Found" and 500 "Internal Server Error". The status code for such responses can be retrieved by calling [response.status()](https://playwright.dev/docs/api/class-response#response-status).

  **NOTE** The method either throws an error or returns a main resource response. The only exceptions are navigation to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.

  **NOTE** Headless mode doesn't support navigation to a PDF document. See the [upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

  ***

  #### Parameters

  * ##### externalurl: string

    URL to navigate page to. The url should include scheme, e.g. `https://`. When a [`baseURL`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url) via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.

  * ##### externaloptionaloptions: { referer?<!-- -->: string; timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionalreferer: string

      Referer header value. If provided it will take preference over the referer header value set by [page.setExtraHTTPHeaders(headers)](https://playwright.dev/docs/api/class-page#page-set-extra-http-headers).

    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<null | Response>

### [**](#hover)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3265)externalinheritedhover

* ****hover**(selector, options): Promise\<void>

- Inherited from Page.hover

  **NOTE** Use locator-based [locator.hover(\[options\])](https://playwright.dev/docs/api/class-locator#locator-hover) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method hovers over an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-hover-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-hover-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-hover-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  3. Scroll the element into view if needed.
  4. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to hover over the center of the element, or the specified [`position`](https://playwright.dev/docs/api/class-page#page-hover-option-position).

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-hover-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; modifiers?<!-- -->: (Alt | Control | ControlOrMeta | Meta | Shift)\[]; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalmodifiers: (Alt | Control | ControlOrMeta | Meta | Shift)\[]

      Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

  #### Returns Promise\<void>

### [**](#innerHTML)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3326)externalinheritedinnerHTML

* ****innerHTML**(selector, options): Promise\<string>

- Inherited from Page.innerHTML

  **NOTE** Use locator-based [locator.innerHTML(\[options\])](https://playwright.dev/docs/api/class-locator#locator-inner-html) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns `element.innerHTML`.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<string>

### [**](#innerText)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3351)externalinheritedinnerText

* ****innerText**(selector, options): Promise\<string>

- Inherited from Page.innerText

  **NOTE** Use locator-based [locator.innerText(\[options\])](https://playwright.dev/docs/api/class-locator#locator-inner-text) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns `element.innerText`.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<string>

### [**](#inputValue)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3381)externalinheritedinputValue

* ****inputValue**(selector, options): Promise\<string>

- Inherited from Page.inputValue

  **NOTE** Use locator-based [locator.inputValue(\[options\])](https://playwright.dev/docs/api/class-locator#locator-input-value) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

  Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the control.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<string>

### [**](#isChecked)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3406)externalinheritedisChecked

* ****isChecked**(selector, options): Promise\<boolean>

- Inherited from Page.isChecked

  **NOTE** Use locator-based [locator.isChecked(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-checked) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<boolean>

### [**](#isClosed)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3425)externalinheritedisClosed

* ****isClosed**(): boolean

- Inherited from Page.isClosed

  Indicates that the page has been closed.

  ***

  #### Returns boolean

### [**](#isDisabled)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3437)externalinheritedisDisabled

* ****isDisabled**(selector, options): Promise\<boolean>

- Inherited from Page.isDisabled

  **NOTE** Use locator-based [locator.isDisabled(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-disabled) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/docs/actionability#enabled).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<boolean>

### [**](#isEditable)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3463)externalinheritedisEditable

* ****isEditable**(selector, options): Promise\<boolean>

- Inherited from Page.isEditable

  **NOTE** Use locator-based [locator.isEditable(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-editable) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is [editable](https://playwright.dev/docs/actionability#editable).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<boolean>

### [**](#isEnabled)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3488)externalinheritedisEnabled

* ****isEnabled**(selector, options): Promise\<boolean>

- Inherited from Page.isEnabled

  **NOTE** Use locator-based [locator.isEnabled(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-enabled) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is [enabled](https://playwright.dev/docs/actionability#enabled).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<boolean>

### [**](#isHidden)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3515)externalinheritedisHidden

* ****isHidden**(selector, options): Promise\<boolean>

- Inherited from Page.isHidden

  **NOTE** Use locator-based [locator.isHidden(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-hidden) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/docs/actionability#visible). [`selector`](https://playwright.dev/docs/api/class-page#page-is-hidden-option-selector) that does not match any elements is considered hidden.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      * **@deprecated**

        This option is ignored. [page.isHidden(selector\[, options\])](https://playwright.dev/docs/api/class-page#page-is-hidden) does not wait for the element to become hidden and returns immediately.

  #### Returns Promise\<boolean>

### [**](#isVisible)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3541)externalinheritedisVisible

* ****isVisible**(selector, options): Promise\<boolean>

- Inherited from Page.isVisible

  **NOTE** Use locator-based [locator.isVisible(\[options\])](https://playwright.dev/docs/api/class-locator#locator-is-visible) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns whether the element is [visible](https://playwright.dev/docs/actionability#visible). [`selector`](https://playwright.dev/docs/api/class-page#page-is-visible-option-selector) that does not match any elements is considered not visible.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      * **@deprecated**

        This option is ignored. [page.isVisible(selector\[, options\])](https://playwright.dev/docs/api/class-page#page-is-visible) does not wait for the element to become visible and returns immediately.

  #### Returns Promise\<boolean>

### [**](#locator)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3565)externalinheritedlocator

* ****locator**(selector, options): Locator

- Inherited from Page.locator

  The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved to the element immediately before performing an action, so a series of actions on the same locator can in fact be performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

  [Learn more about locators](https://playwright.dev/docs/locators).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to use when resolving DOM element.

  * ##### externaloptionaloptions: { has?<!-- -->: Locator; hasNot?<!-- -->: Locator; hasNotText?<!-- -->: string | RegExp; hasText?<!-- -->: string | RegExp }
    * ##### externaloptionalhas: Locator

      Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.

      Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has

      ```
      article
      div
      ```

      will fail, because the inner locator must be relative and should not use any elements outside the `content`.

      Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](https://playwright.dev/docs/api/class-framelocator)s.

    * ##### externaloptionalhasNot: Locator

      Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.

      Note that outer and inner locators must belong to the same frame. Inner locator must not contain [FrameLocator](https://playwright.dev/docs/api/class-framelocator)s.

    * ##### externaloptionalhasNotText: string | RegExp

      Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a \[string], matching is case-insensitive and searches for a substring.

    * ##### externaloptionalhasText: string | RegExp

      Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a \[string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`.

  #### Returns Locator

### [**](#mainFrame)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3606)externalinheritedmainFrame

* ****mainFrame**(): Frame

- Inherited from Page.mainFrame

  The page's main frame. Page is guaranteed to have a main frame which persists during navigations.

  ***

  #### Returns Frame

### [**](#observe)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L186)observe

* ****observe**(options): Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>

- Observe the page and get AI-suggested actions.

  * **@example**

    ```
    const suggestions = await page.observe();
    console.log('Available actions:', suggestions);
    ```

  ***

  #### Parameters

  * ##### optionaloptions: Omit<[ObserveOptions](https://crawlee.dev/js/api/stagehand-crawler/interface/ObserveOptions.md), page>

    Optional configuration for the observation

  #### Returns Promise<[Action](https://crawlee.dev/js/api/stagehand-crawler/interface/Action.md)\[]>

  Promise that resolves with available actions on the page

### [**](#off)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1623)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1628)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1633)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1638)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1643)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1648)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1653)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1658)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1663)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1668)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1673)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1678)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1683)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1688)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1693)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1698)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1703)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1708)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1713)externalinheritedoff

* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this
* ****off**(event, listener): this

- Inherited from Page.off

  Removes an event listener added by `on` or `addListener`.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1019)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1040)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1060)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1080)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1086)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1092)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1107)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1112)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1117)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1122)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1127)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1143)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1172)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1179)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1198)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1204)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1210)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1215)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1221)externalinheritedon

* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this
* ****on**(event, listener): this

- Inherited from Page.on

  Emitted when the page closes.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1226)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1231)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1236)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1241)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1246)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1251)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1256)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1261)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1266)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1271)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1276)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1281)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1286)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1291)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1296)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1301)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1306)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1311)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1316)externalinheritedonce

* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this
* ****once**(event, listener): this

- Inherited from Page.once

  Adds an event listener that will be automatically removed after it is triggered once. See `addListener` for more information about this event.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#opener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3611)externalinheritedopener

* ****opener**(): Promise\<null | Page>

- Inherited from Page.opener

  Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

  ***

  #### Returns Promise\<null | Page>

### [**](#pageErrors)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3617)externalinheritedpageErrors

* ****pageErrors**(): Promise\<Error\[]>

- Inherited from Page.pageErrors

  Returns up to (currently) 200 last page errors from this page. See [page.on('pageerror')](https://playwright.dev/docs/api/class-page#page-event-page-error) for more details.

  ***

  #### Returns Promise\<Error\[]>

### [**](#pause)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3630)externalinheritedpause

* ****pause**(): Promise\<void>

- Inherited from Page.pause

  Pauses script execution. Playwright will stop executing the script and wait for the user to either press the 'Resume' button in the page overlay or to call `playwright.resume()` in the DevTools console.

  User can inspect selectors or perform manual steps while paused. Resume will continue running the original script from the place it was paused.

  **NOTE** This method requires Playwright to be started in a headed mode, with a falsy [`headless`](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-option-headless) option.

  ***

  #### Returns Promise\<void>

### [**](#pdf)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3687)externalinheritedpdf

* ****pdf**(options): Promise\<Buffer\<ArrayBufferLike>>

- Inherited from Page.pdf

  Returns the PDF buffer.

  `page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call [page.emulateMedia(\[options\])](https://playwright.dev/docs/api/class-page#page-emulate-media) before calling `page.pdf()`:

  **NOTE** By default, `page.pdf()` generates a pdf with modified colors for printing. Use the [`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust) property to force rendering of exact colors.

  **Usage**

  ```
  // Generates a PDF with 'screen' media type.
  await page.emulateMedia({ media: 'screen' });
  await page.pdf({ path: 'page.pdf' });
  ```

  The [`width`](https://playwright.dev/docs/api/class-page#page-pdf-option-width), [`height`](https://playwright.dev/docs/api/class-page#page-pdf-option-height), and [`margin`](https://playwright.dev/docs/api/class-page#page-pdf-option-margin) options accept values labeled with units. Unlabeled values are treated as pixels.

  A few examples:

  * `page.pdf({width: 100})` - prints with width set to 100 pixels
  * `page.pdf({width: '100px'})` - prints with width set to 100 pixels
  * `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

  All possible units are:

  * `px` - pixel
  * `in` - inch
  * `cm` - centimeter
  * `mm` - millimeter

  The [`format`](https://playwright.dev/docs/api/class-page#page-pdf-option-format) options are:

  * `Letter`: 8.5in x 11in
  * `Legal`: 8.5in x 14in
  * `Tabloid`: 11in x 17in
  * `Ledger`: 17in x 11in
  * `A0`: 33.1in x 46.8in
  * `A1`: 23.4in x 33.1in
  * `A2`: 16.54in x 23.4in
  * `A3`: 11.7in x 16.54in
  * `A4`: 8.27in x 11.7in
  * `A5`: 5.83in x 8.27in
  * `A6`: 4.13in x 5.83in

  **NOTE** [`headerTemplate`](https://playwright.dev/docs/api/class-page#page-pdf-option-header-template) and [`footerTemplate`](https://playwright.dev/docs/api/class-page#page-pdf-option-footer-template) markup have the following limitations: > 1. Script tags inside templates are not evaluated. > 2. Page styles are not visible inside templates.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { displayHeaderFooter?<!-- -->: boolean; footerTemplate?<!-- -->: string; format?<!-- -->: string; headerTemplate?<!-- -->: string; height?<!-- -->: string | number; landscape?<!-- -->: boolean; margin?<!-- -->: { bottom?<!-- -->: string | number; left?<!-- -->: string | number; right?<!-- -->: string | number; top?<!-- -->: string | number }; outline?<!-- -->: boolean; pageRanges?<!-- -->: string; path?<!-- -->: string; preferCSSPageSize?<!-- -->: boolean; printBackground?<!-- -->: boolean; scale?<!-- -->: number; tagged?<!-- -->: boolean; width?<!-- -->: string | number }
    * ##### externaloptionaldisplayHeaderFooter: boolean

      Display header and footer. Defaults to `false`.

    * ##### externaloptionalfooterTemplate: string

      HTML template for the print footer. Should use the same format as the [`headerTemplate`](https://playwright.dev/docs/api/class-page#page-pdf-option-header-template).

    * ##### externaloptionalformat: string

      Paper format. If set, takes priority over [`width`](https://playwright.dev/docs/api/class-page#page-pdf-option-width) or [`height`](https://playwright.dev/docs/api/class-page#page-pdf-option-height) options. Defaults to 'Letter'.

    * ##### externaloptionalheaderTemplate: string

      HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them:

      * `'date'` formatted print date
      * `'title'` document title
      * `'url'` document location
      * `'pageNumber'` current page number
      * `'totalPages'` total pages in the document

    * ##### externaloptionalheight: string | number

      Paper height, accepts values labeled with units.

    * ##### externaloptionallandscape: boolean

      Paper orientation. Defaults to `false`.

    * ##### externaloptionalmargin: { bottom?<!-- -->: string | number; left?<!-- -->: string | number; right?<!-- -->: string | number; top?<!-- -->: string | number }

      Paper margins, defaults to none.

    * ##### externaloptionaloutline: boolean

      Whether or not to embed the document outline into the PDF. Defaults to `false`.

    * ##### externaloptionalpageRanges: string

      Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.

    * ##### externaloptionalpath: string

      The file path to save the PDF to. If [`path`](https://playwright.dev/docs/api/class-page#page-pdf-option-path) is a relative path, then it is resolved relative to the current working directory. If no path is provided, the PDF won't be saved to the disk.

    * ##### externaloptionalpreferCSSPageSize: boolean

      Give any CSS `@page` size declared in the page priority over what is declared in [`width`](https://playwright.dev/docs/api/class-page#page-pdf-option-width) and [`height`](https://playwright.dev/docs/api/class-page#page-pdf-option-height) or [`format`](https://playwright.dev/docs/api/class-page#page-pdf-option-format) options. Defaults to `false`, which will scale the content to fit the paper size.

    * ##### externaloptionalprintBackground: boolean

      Print background graphics. Defaults to `false`.

    * ##### externaloptionalscale: number

      Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.

    * ##### externaloptionaltagged: boolean

      Whether or not to generate tagged (accessible) PDF. Defaults to `false`.

    * ##### externaloptionalwidth: string | number

      Paper width, accepts values labeled with units.

  #### Returns Promise\<Buffer\<ArrayBufferLike>>

### [**](#prependListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1718)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1739)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1759)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1779)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1785)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1791)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1806)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1811)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1816)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1821)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1826)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1842)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1871)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1878)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1897)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1903)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1909)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1914)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1920)externalinheritedprependListener

* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this
* ****prependListener**(event, listener): this

- Inherited from Page.prependListener

  Emitted when the page closes.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#press)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3848)externalinheritedpress

* ****press**(selector, key, options): Promise\<void>

- Inherited from Page.press

  **NOTE** Use locator-based [locator.press(key\[, options\])](https://playwright.dev/docs/api/class-locator#locator-press) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Focuses the element, and then uses [keyboard.down(key)](https://playwright.dev/docs/api/class-keyboard#keyboard-down) and [keyboard.up(key)](https://playwright.dev/docs/api/class-keyboard#keyboard-up).

  [`key`](https://playwright.dev/docs/api/class-page#page-press-option-key) can specify the intended [keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character to generate the text for. A superset of the [`key`](https://playwright.dev/docs/api/class-page#page-press-option-key) values can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

  `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`, `Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.

  Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`, `ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

  Holding down `Shift` will type the text that corresponds to the [`key`](https://playwright.dev/docs/api/class-page#page-press-option-key) in the upper case.

  If [`key`](https://playwright.dev/docs/api/class-page#page-press-option-key) is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective texts.

  Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

  **Usage**

  ```
  const page = await browser.newPage();
  await page.goto('https://keycode.info');
  await page.press('body', 'A');
  await page.screenshot({ path: 'A.png' });
  await page.press('body', 'ArrowLeft');
  await page.screenshot({ path: 'ArrowLeft.png' });
  await page.press('body', 'Shift+O');
  await page.screenshot({ path: 'O.png' });
  await browser.close();
  ```

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalkey: string

    Name of the key to press or a character to generate, such as `ArrowLeft` or `a`.

  * ##### externaloptionaloptions: { delay?<!-- -->: number; noWaitAfter?<!-- -->: boolean; strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionaldelay: number

      Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0.

    * ##### externaloptionalnoWaitAfter: boolean

      Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.

      * **@deprecated**

        This option will default to `true` in the future.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#reload)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3883)externalinheritedreload

* ****reload**(options): Promise\<null | Response>

- Inherited from Page.reload

  This method reloads the current page, in the same way as if the user had triggered a browser refresh. Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<null | Response>

### [**](#removeAllListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L986)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1007)externalinheritedremoveAllListeners

* ****removeAllListeners**(type): this
* ****removeAllListeners**(type, options): Promise\<void>

- Inherited from Page.removeAllListeners

  Removes all the listeners of the given type (or all registered listeners if no type given). Allows to wait for async listeners to complete or to ignore subsequent errors from these listeners.

  **Usage**

  ```
  page.on('request', async request => {
    const response = await request.response();
    const body = await response.body();
    console.log(body.byteLength);
  });
  await page.goto('https://playwright.dev', { waitUntil: 'domcontentloaded' });
  // Waits for all the reported 'request' events to resolve.
  await page.removeAllListeners('request', { behavior: 'wait' });
  ```

  ***

  #### Parameters

  * ##### externaloptionaltype: string

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1528)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1533)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1538)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1543)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1548)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1553)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1558)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1563)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1568)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1573)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1578)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1583)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1588)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1593)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1598)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1603)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1608)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1613)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L1618)externalinheritedremoveListener

* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this
* ****removeListener**(event, listener): this

- Inherited from Page.removeListener

  Removes an event listener added by `on` or `addListener`.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externallistener: (page) => any


  #### Returns this

### [**](#removeLocatorHandler)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3913)externalinheritedremoveLocatorHandler

* ****removeLocatorHandler**(locator): Promise\<void>

- Inherited from Page.removeLocatorHandler

  Removes all locator handlers added by [page.addLocatorHandler(locator, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-add-locator-handler) for a specific locator.

  ***

  #### Parameters

  * ##### externallocator: Locator

    Locator passed to [page.addLocatorHandler(locator, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-add-locator-handler).

  #### Returns Promise\<void>

### [**](#requestGC)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3933)externalinheritedrequestGC

* ****requestGC**(): Promise\<void>

- Inherited from Page.requestGC

  Request the page to perform garbage collection. Note that there is no guarantee that all unreachable objects will be collected.

  This is useful to help detect memory leaks. For example, if your page has a large object `'suspect'` that might be leaked, you can check that it does not leak by using a [`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef).

  ```
  // 1. In your page, save a WeakRef for the "suspect".
  await page.evaluate(() => globalThis.suspectWeakRef = new WeakRef(suspect));
  // 2. Request garbage collection.
  await page.requestGC();
  // 3. Check that weak ref does not deref to the original object.
  expect(await page.evaluate(() => !globalThis.suspectWeakRef.deref())).toBe(true);
  ```

  ***

  #### Returns Promise\<void>

### [**](#requests)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L3948)externalinheritedrequests

* ****requests**(): Promise\<Request\[]>

- Inherited from Page.requests

  Returns up to (currently) 100 last network request from this page. See [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request) for more details.

  Returned requests should be accessed immediately, otherwise they might be collected to prevent unbounded memory growth as new requests come in. Once collected, retrieving most information about the request is impossible.

  Note that requests reported through the [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request) request are not collected, so there is a trade off between efficient memory usage with [page.requests()](https://playwright.dev/docs/api/class-page#page-requests) and the amount of available information reported through [page.on('request')](https://playwright.dev/docs/api/class-page#page-event-request).

  ***

  #### Returns Promise\<Request\[]>

### [**](#route)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4017)externalinheritedroute

* ****route**(url, handler, options): Promise\<void>

- Inherited from Page.route

  Routing provides the capability to modify network requests that are made by a page.

  Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

  **NOTE** The handler will only be called for the first url if the response is a redirect.

  **NOTE** [page.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-route) will not intercept requests intercepted by Service Worker. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [`serviceWorkers`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-service-workers) to `'block'`.

  **NOTE** [page.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-route) will not intercept the first request of a popup page. Use [browserContext.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-browsercontext#browser-context-route) instead.

  **Usage**

  An example of a naive handler that aborts all image requests:

  ```
  const page = await browser.newPage();
  await page.route('**/*.{png,jpg,jpeg}', route => route.abort());
  await page.goto('https://example.com');
  await browser.close();
  ```

  or the same snippet using a regex pattern instead:

  ```
  const page = await browser.newPage();
  await page.route(/(\.png$)|(\.jpg$)/, route => route.abort());
  await page.goto('https://example.com');
  await browser.close();
  ```

  It is possible to examine the request to decide the route action. For example, mocking all requests that contain some post data, and leaving all other requests as is:

  ```
  await page.route('/api/**', async route => {
    if (route.request().postData().includes('my-string'))
      await route.fulfill({ body: 'mocked-data' });
    else
      await route.continue();
  });
  ```

  Page routes take precedence over browser context routes (set up with [browserContext.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-browsercontext#browser-context-route)) when request matches both handlers.

  To remove a route with its handler you can use [page.unroute(url\[, handler\])](https://playwright.dev/docs/api/class-page#page-unroute).

  **NOTE** Enabling routing disables http cache.

  ***

  #### Parameters

  * ##### externalurl: string | RegExp | (url) => boolean

    A glob pattern, regex pattern, or predicate that receives a \[URL] to match during routing. If [`baseURL`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url) is set in the context options and the provided URL is a string that does not start with `*`, it is resolved using the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.

  *

    ##### externalhandler: (route, request) => any

    handler function to route the request.

  *
    ##### externaloptionaloptions: { times?<!-- -->: number }
    * ##### externaloptionaltimes: number

      How often a route should be used. By default it will be used every time.

  #### Returns Promise\<void>

### [**](#routeFromHAR)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4037)externalinheritedrouteFromHAR

* ****routeFromHAR**(har, options): Promise\<void>

- Inherited from Page.routeFromHAR

  If specified the network requests that are made in the page will be served from the HAR file. Read more about [Replaying from HAR](https://playwright.dev/docs/mock#replaying-from-har).

  Playwright will not serve requests intercepted by Service Worker from the HAR file. See [this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when using request interception by setting [`serviceWorkers`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-service-workers) to `'block'`.

  ***

  #### Parameters

  * ##### externalhar: string

    Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory.

  * ##### externaloptionaloptions: { notFound?<!-- -->: abort | fallback; update?<!-- -->: boolean; updateContent?<!-- -->: embed | attach; updateMode?<!-- -->: full | minimal; url?<!-- -->: string | RegExp }
    * ##### externaloptionalnotFound: abort | fallback

      * If set to 'abort' any request not found in the HAR file will be aborted.
      * If set to 'fallback' missing requests will be sent to the network.

      Defaults to abort.

    * ##### externaloptionalupdate: boolean

      If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when [browserContext.close(\[options\])](https://playwright.dev/docs/api/class-browsercontext#browser-context-close) is called.

    * ##### externaloptionalupdateContent: embed | attach

      Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file.

    * ##### externaloptionalupdateMode: full | minimal

      When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`.

    * ##### externaloptionalurl: string | RegExp

      A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file.

  #### Returns Promise\<void>

### [**](#routeWebSocket)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4098)externalinheritedrouteWebSocket

* ****routeWebSocket**(url, handler): Promise\<void>

- Inherited from Page.routeWebSocket

  This method allows to modify websocket connections that are made by the page.

  Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this method before navigating the page.

  **Usage**

  Below is an example of a simple mock that responds to a single message. See [WebSocketRoute](https://playwright.dev/docs/api/class-websocketroute) for more details and examples.

  ```
  await page.routeWebSocket('/ws', ws => {
    ws.onMessage(message => {
      if (message === 'request')
        ws.send('response');
    });
  });
  ```

  ***

  #### Parameters

  * ##### externalurl: string | RegExp | (url) => boolean

    Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the [`baseURL`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url) context option.

  *

    ##### externalhandler: (websocketroute) => any

    Handler function to route the WebSocket.



  #### Returns Promise\<void>

### [**](#screenshot)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4104)externalinheritedscreenshot

* ****screenshot**(options): Promise\<Buffer\<ArrayBufferLike>>

- Inherited from Page.screenshot

  Returns the buffer with the captured screenshot.

  ***

  #### Parameters

  * ##### externaloptionaloptions: PageScreenshotOptions

  #### Returns Promise\<Buffer\<ArrayBufferLike>>

### [**](#selectOption)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4146)externalinheritedselectOption

* ****selectOption**(selector, values, options): Promise\<string\[]>

- Inherited from Page.selectOption

  **NOTE** Use locator-based [locator.selectOption(values\[, options\])](https://playwright.dev/docs/api/class-locator#locator-select-option) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method waits for an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-select-option-option-selector), waits for [actionability](https://playwright.dev/docs/actionability) checks, waits until all specified options are present in the `<select>` element and selects these options.

  If the target element is not a `<select>` element, this method throws an error. However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used instead.

  Returns the array of option values that have been successfully selected.

  Triggers a `change` and `input` event once all the provided options have been selected.

  **Usage**

  ```
  // Single selection matching the value or label
  page.selectOption('select#colors', 'blue');

  // single selection matching the label
  page.selectOption('select#colors', { label: 'Blue' });

  // multiple selection
  page.selectOption('select#colors', ['red', 'green', 'blue']);
  ```

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalvalues: null | string | readonly<!-- --> string\[] | ElementHandle\<Node> | { index?<!-- -->: number; label?<!-- -->: string; value?<!-- -->: string } | readonly<!-- --> ElementHandle\<Node>\[] | readonly<!-- --> { index?<!-- -->: number; label?<!-- -->: string; value?<!-- -->: string }\[]

    Options to select. If the `<select>` has the `multiple` attribute, all matching options are selected, otherwise only the first option matching one of the passed options is selected. String values are matching both values and labels. Option is considered matching if all specified properties match.

  * * ##### externaloptionalindex: number

      Matches by the index. Optional.

    * ##### externaloptionallabel: string

      Matches by `option.label`. Optional.

    * ##### externaloptionalvalue: string

      Matches by `option.value`. Optional.
    ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<string\[]>

### [**](#setChecked)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4232)externalinheritedsetChecked

* ****setChecked**(selector, checked, options): Promise\<void>

- Inherited from Page.setChecked

  **NOTE** Use locator-based [locator.setChecked(checked\[, options\])](https://playwright.dev/docs/api/class-locator#locator-set-checked) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method checks or unchecks an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-set-checked-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-set-checked-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Ensure that matched element is a checkbox or a radio input. If not, this method throws.
  3. If the element already has the right checked state, this method returns immediately.
  4. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-set-checked-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  5. Scroll the element into view if needed.
  6. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to click in the center of the element.
  7. Ensure that the element is now checked or unchecked. If not, this method throws.

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-set-checked-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalchecked: boolean

    Whether to check or uncheck the checkbox.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

  #### Returns Promise\<void>

### [**](#setContent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4281)externalinheritedsetContent

* ****setContent**(html, options): Promise\<void>

- Inherited from Page.setContent

  This method internally calls [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write), inheriting all its specific characteristics and behaviors.

  ***

  #### Parameters

  * ##### externalhtml: string

    HTML markup to assign to the page.

  * ##### externaloptionaloptions: { timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<void>

### [**](#setDefaultNavigationTimeout)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4324)externalinheritedsetDefaultNavigationTimeout

* ****setDefaultNavigationTimeout**(timeout): void

- Inherited from Page.setDefaultNavigationTimeout

  This setting will change the default maximum navigation time for the following methods and related shortcuts:

  * [page.goBack(\[options\])](https://playwright.dev/docs/api/class-page#page-go-back)
  * [page.goForward(\[options\])](https://playwright.dev/docs/api/class-page#page-go-forward)
  * [page.goto(url\[, options\])](https://playwright.dev/docs/api/class-page#page-goto)
  * [page.reload(\[options\])](https://playwright.dev/docs/api/class-page#page-reload)
  * [page.setContent(html\[, options\])](https://playwright.dev/docs/api/class-page#page-set-content)
  * [page.waitForNavigation(\[options\])](https://playwright.dev/docs/api/class-page#page-wait-for-navigation)
  * [page.waitForURL(url\[, options\])](https://playwright.dev/docs/api/class-page#page-wait-for-url)

  **NOTE** [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) takes priority over [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) and [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout).

  ***

  #### Parameters

  * ##### externaltimeout: number

    Maximum navigation time in milliseconds

  #### Returns void

### [**](#setDefaultTimeout)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4337)externalinheritedsetDefaultTimeout

* ****setDefaultTimeout**(timeout): void

- Inherited from Page.setDefaultTimeout

  This setting will change the default maximum time for all the methods accepting [`timeout`](https://playwright.dev/docs/api/class-page#page-set-default-timeout-option-timeout) option.

  **NOTE** [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) takes priority over [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout).

  ***

  #### Parameters

  * ##### externaltimeout: number

    Maximum time in milliseconds. Pass `0` to disable timeout.

  #### Returns void

### [**](#setExtraHTTPHeaders)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4348)externalinheritedsetExtraHTTPHeaders

* ****setExtraHTTPHeaders**(headers): Promise\<void>

- Inherited from Page.setExtraHTTPHeaders

  The extra HTTP headers will be sent with every request the page initiates.

  **NOTE** [page.setExtraHTTPHeaders(headers)](https://playwright.dev/docs/api/class-page#page-set-extra-http-headers) does not guarantee the order of headers in the outgoing requests.

  ***

  #### Parameters

  * ##### externalheaders: <!-- -->{}

    An object containing additional HTTP headers to be sent with every request. All header values must be strings.



  #### Returns Promise\<void>

### [**](#setInputFiles)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4368)externalinheritedsetInputFiles

* ****setInputFiles**(selector, files, options): Promise\<void>

- Inherited from Page.setInputFiles

  **NOTE** Use locator-based [locator.setInputFiles(files\[, options\])](https://playwright.dev/docs/api/class-locator#locator-set-input-files) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs with a `[webkitdirectory]` attribute, only a single directory path is supported.

  This method expects [`selector`](https://playwright.dev/docs/api/class-page#page-set-input-files-option-selector) to point to an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside the `<label>` element that has an associated [control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externalfiles: string | readonly<!-- --> string\[] | { buffer: Buffer\<ArrayBufferLike>; mimeType: string; name: string } | readonly<!-- --> { buffer: Buffer\<ArrayBufferLike>; mimeType: string; name: string }\[]

  * * ##### externalbuffer: Buffer\<ArrayBufferLike>

      File content

    * ##### externalmimeType: string

      File type

    * ##### externalname: string

      File name
    ##### externaloptionaloptions: { noWaitAfter?<!-- -->: boolean; strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#setViewportSize)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4446)externalinheritedsetViewportSize

* ****setViewportSize**(viewportSize): Promise\<void>

- Inherited from Page.setViewportSize

  In the case of multiple pages in a single browser, each page can have its own viewport size. However, [browser.newContext(\[options\])](https://playwright.dev/docs/api/class-browser#browser-new-context) allows to set viewport size (and more) for all pages in the context at once.

  [page.setViewportSize(viewportSize)](https://playwright.dev/docs/api/class-page#page-set-viewport-size) will resize the page. A lot of websites don't expect phones to change size, so you should set the viewport size before navigating to the page. [page.setViewportSize(viewportSize)](https://playwright.dev/docs/api/class-page#page-set-viewport-size) will also reset `screen` size, use [browser.newContext(\[options\])](https://playwright.dev/docs/api/class-browser#browser-new-context) with `screen` and `viewport` parameters if you need better control of these properties.

  **Usage**

  ```
  const page = await browser.newPage();
  await page.setViewportSize({
    width: 640,
    height: 480,
  });
  await page.goto('https://example.com');
  ```

  ***

  #### Parameters

  * ##### externalviewportSize: { height: number; width: number }
    * ##### externalheight: number

      page height in pixels.

    * ##### externalwidth: number

      page width in pixels.

  #### Returns Promise\<void>

### [**](#tap)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4486)externalinheritedtap

* ****tap**(selector, options): Promise\<void>

- Inherited from Page.tap

  **NOTE** Use locator-based [locator.tap(\[options\])](https://playwright.dev/docs/api/class-locator#locator-tap) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method taps an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-tap-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-tap-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-tap-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  3. Scroll the element into view if needed.
  4. Use [page.touchscreen](https://playwright.dev/docs/api/class-page#page-touchscreen) to tap the center of the element, or the specified [`position`](https://playwright.dev/docs/api/class-page#page-tap-option-position).

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-tap-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  **NOTE** [page.tap(selector\[, options\])](https://playwright.dev/docs/api/class-page#page-tap) the method will throw if [`hasTouch`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-has-touch) option of the browser context is false.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; modifiers?<!-- -->: (Alt | Control | ControlOrMeta | Meta | Shift)\[]; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalmodifiers: (Alt | Control | ControlOrMeta | Meta | Shift)\[]

      Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

  #### Returns Promise\<void>

### [**](#textContent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4548)externalinheritedtextContent

* ****textContent**(selector, options): Promise\<null | string>

- Inherited from Page.textContent

  **NOTE** Use locator-based [locator.textContent(\[options\])](https://playwright.dev/docs/api/class-locator#locator-text-content) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns `element.textContent`.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<null | string>

### [**](#title)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4567)externalinheritedtitle

* ****title**(): Promise\<string>

- Inherited from Page.title

  Returns the page's title.

  ***

  #### Returns Promise\<string>

### [**](#type)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4587)externalinheritedtype

* ****type**(selector, text, options): Promise\<void>

- Inherited from Page.type

  Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to send fine-grained keyboard events. To fill values in form fields, use [page.fill(selector, value\[, options\])](https://playwright.dev/docs/api/class-page#page-fill).

  To press a special key, like `Control` or `ArrowDown`, use [keyboard.press(key\[, options\])](https://playwright.dev/docs/api/class-keyboard#keyboard-press).

  **Usage**

  * **@deprecated**

    In most cases, you should use [locator.fill(value\[, options\])](https://playwright.dev/docs/api/class-locator#locator-fill) instead. You only need to press keys one by one if there is special keyboard handling on the page - in this case use [locator.pressSequentially(text\[, options\])](https://playwright.dev/docs/api/class-locator#locator-press-sequentially).

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaltext: string

    A text to type into a focused element.

  * ##### externaloptionaloptions: { delay?<!-- -->: number; noWaitAfter?<!-- -->: boolean; strict?<!-- -->: boolean; timeout?<!-- -->: number }
    * ##### externaloptionaldelay: number

      Time to wait between key presses in milliseconds. Defaults to 0.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#uncheck)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4641)externalinheriteduncheck

* ****uncheck**(selector, options): Promise\<void>

- Inherited from Page.uncheck

  **NOTE** Use locator-based [locator.uncheck(\[options\])](https://playwright.dev/docs/api/class-locator#locator-uncheck) instead. Read more about [locators](https://playwright.dev/docs/locators).

  This method unchecks an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-uncheck-option-selector) by performing the following steps:

  1. Find an element matching [`selector`](https://playwright.dev/docs/api/class-page#page-uncheck-option-selector). If there is none, wait until a matching element is attached to the DOM.
  2. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is already unchecked, this method returns immediately.
  3. Wait for [actionability](https://playwright.dev/docs/actionability) checks on the matched element, unless [`force`](https://playwright.dev/docs/api/class-page#page-uncheck-option-force) option is set. If the element is detached during the checks, the whole action is retried.
  4. Scroll the element into view if needed.
  5. Use [page.mouse](https://playwright.dev/docs/api/class-page#page-mouse) to click in the center of the element.
  6. Ensure that the element is now unchecked. If not, this method throws.

  When all steps combined have not finished during the specified [`timeout`](https://playwright.dev/docs/api/class-page#page-uncheck-option-timeout), this method throws a [TimeoutError](https://playwright.dev/docs/api/class-timeouterror). Passing zero timeout disables this.

  ***

  #### Parameters

  * ##### externalselector: string

    A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used.

  * ##### externaloptionaloptions: { force?<!-- -->: boolean; noWaitAfter?<!-- -->: boolean; position?<!-- -->: { x: number; y: number }; strict?<!-- -->: boolean; timeout?<!-- -->: number; trial?<!-- -->: boolean }
    * ##### externaloptionalforce: boolean

      Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

    * ##### externaloptionalnoWaitAfter: boolean

      This option has no effect.

      * **@deprecated**

        This option has no effect.

    * ##### externaloptionalposition: { x: number; y: number }

      A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

    * ##### externaloptionalstrict: boolean

      When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

    * ##### externaloptionaltimeout: number

      Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionaltrial: boolean

      When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it.

  #### Returns Promise\<void>

### [**](#unroute)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4692)externalinheritedunroute

* ****unroute**(url, handler): Promise\<void>

- Inherited from Page.unroute

  Removes a route created with [page.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-route). When [`handler`](https://playwright.dev/docs/api/class-page#page-unroute-option-handler) is not specified, removes all routes for the [`url`](https://playwright.dev/docs/api/class-page#page-unroute-option-url).

  ***

  #### Parameters

  * ##### externalurl: string | RegExp | (url) => boolean

    A glob pattern, regex pattern or predicate receiving \[URL] to match while routing.

  *

    ##### externaloptionalhandler: (route, request) => any

    Optional handler function to route the request.



  #### Returns Promise\<void>

### [**](#unrouteAll)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4700)externalinheritedunrouteAll

* ****unrouteAll**(options): Promise\<void>

- Inherited from Page.unrouteAll

  Removes all routes created with [page.route(url, handler\[, options\])](https://playwright.dev/docs/api/class-page#page-route) and [page.routeFromHAR(har\[, options\])](https://playwright.dev/docs/api/class-page#page-route-from-har).

  ***

  #### Parameters

  * ##### externaloptionaloptions: { behavior?<!-- -->: default | wait | ignoreErrors }
    * ##### externaloptionalbehavior: default | wait | ignoreErrors

      Specifies whether to wait for already running handlers and what to do if they throw errors:

      * `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error
      * `'wait'` - wait for current handler calls (if any) to finish
      * `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught

  #### Returns Promise\<void>

### [**](#url)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4712)externalinheritedurl

* ****url**(): string

- Inherited from Page.url

  #### Returns string

### [**](#video)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4717)externalinheritedvideo

* ****video**(): null | Video

- Inherited from Page.video

  Video object associated with this page.

  ***

  #### Returns null | Video

### [**](#viewportSize)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4719)externalinheritedviewportSize

* ****viewportSize**(): null | { height: number; width: number }

- Inherited from Page.viewportSize

  #### Returns null | { height: number; width: number }

### [**](#waitForEvent)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4734)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4755)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4775)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4795)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4801)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4807)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4822)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4827)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4832)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4837)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4842)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4858)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4887)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4894)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4913)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4919)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4925)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4930)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4936)externalinheritedwaitForEvent

* ****waitForEvent**(event, optionsOrPredicate): Promise\<Page>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<ConsoleMessage>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Page>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Dialog>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Page>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Download>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<FileChooser>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Frame>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Frame>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Frame>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Page>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Error>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Page>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Request>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Request>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Request>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Response>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<WebSocket>
* ****waitForEvent**(event, optionsOrPredicate): Promise\<Worker>

- Inherited from Page.waitForEvent

  Emitted when the page closes.

  ***

  #### Parameters

  * ##### externalevent: close
  * ##### externaloptionaloptionsOrPredicate: { predicate?<!-- -->: (page) => boolean | Promise\<boolean>; timeout?<!-- -->: number } | (page) => boolean | Promise\<boolean>
    * ##### externaloptionalpredicate: (page) => boolean | Promise\<boolean>
    * ##### externaloptionaltimeout: number


  #### Returns Promise\<Page>

### [**](#waitForFunction)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L643)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L682)externalinheritedwaitForFunction

* ****waitForFunction**\<R, Arg>(pageFunction, arg, options): Promise\<SmartHandle\<R>>
* ****waitForFunction**\<R>(pageFunction, arg, options): Promise\<SmartHandle\<R>>

- Inherited from Page.waitForFunction

  Returns when the [`pageFunction`](https://playwright.dev/docs/api/class-page#page-wait-for-function-option-expression) returns a truthy value. It resolves to a JSHandle of the truthy value.

  **Usage**

  The [page.waitForFunction(pageFunction\[, arg, options\])](https://playwright.dev/docs/api/class-page#page-wait-for-function) can be used to observe viewport size change:

  ```
  const { webkit } = require('playwright');  // Or 'chromium' or 'firefox'.

  (async () => {
    const browser = await webkit.launch();
    const page = await browser.newPage();
    const watchDog = page.waitForFunction(() => window.innerWidth < 100);
    await page.setViewportSize({ width: 50, height: 50 });
    await watchDog;
    await browser.close();
  })();
  ```

  To pass an argument to the predicate of [page.waitForFunction(pageFunction\[, arg, options\])](https://playwright.dev/docs/api/class-page#page-wait-for-function) function:

  ```
  const selector = '.foo';
  await page.waitForFunction(selector => !!document.querySelector(selector), selector);
  ```

  ***

  #### Parameters

  * ##### externalpageFunction: PageFunction\<Arg, R>

    Function to be evaluated in the page context.

  * ##### externalarg: Arg

    Optional argument to pass to [`pageFunction`](https://playwright.dev/docs/api/class-page#page-wait-for-function-option-expression).

  * ##### externaloptionaloptions: PageWaitForFunctionOptions

  #### Returns Promise\<SmartHandle\<R>>

### [**](#waitForLoadState)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L4972)externalinheritedwaitForLoadState

* ****waitForLoadState**(state, options): Promise\<void>

- Inherited from Page.waitForLoadState

  Returns when the required load state has been reached.

  This resolves when the page reaches a required load state, `load` by default. The navigation must have been committed when this method is called. If current document has already reached the required state, resolves immediately.

  **NOTE** Most of the time, this method is not needed because Playwright [auto-waits before every action](https://playwright.dev/docs/actionability).

  **Usage**

  ```
  await page.getByRole('button').click(); // Click triggers navigation.
  await page.waitForLoadState(); // The promise resolves after 'load' event.
  ```

  ```
  const popupPromise = page.waitForEvent('popup');
  await page.getByRole('button').click(); // Click triggers a popup.
  const popup = await popupPromise;
  await popup.waitForLoadState('domcontentloaded'); // Wait for the 'DOMContentLoaded' event.
  console.log(await popup.title()); // Popup is ready to use.
  ```

  ***

  #### Parameters

  * ##### externaloptionalstate: domcontentloaded | load | networkidle

    Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current document, the method resolves immediately. Can be one of:

    * `'load'` - wait for the `load` event to be fired.
    * `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired.
    * `'networkidle'` - **DISCOURAGED** wait until there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.

  * ##### externaloptionaloptions: { timeout?<!-- -->: number }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<void>

### [**](#waitForNavigation)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5009)externalinheritedwaitForNavigation

* ****waitForNavigation**(options): Promise\<null | Response>

- Inherited from Page.waitForNavigation

  Waits for the main frame navigation and returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or navigation due to History API usage, the navigation will resolve with `null`.

  **Usage**

  This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will indirectly cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from a `setTimeout`. Consider this example:

  ```
  // Start waiting for navigation before clicking. Note no await.
  const navigationPromise = page.waitForNavigation();
  await page.getByText('Navigate after timeout').click();
  await navigationPromise;
  ```

  **NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL is considered a navigation.

  * **@deprecated**

    This method is inherently racy, please use [page.waitForURL(url\[, options\])](https://playwright.dev/docs/api/class-page#page-wait-for-url) instead.

  ***

  #### Parameters

  * ##### externaloptionaloptions: { timeout?<!-- -->: number; url?<!-- -->: string | RegExp | (url) => boolean; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalurl: string | RegExp | (url) => boolean

      A glob pattern, regex pattern or predicate receiving \[URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<null | Response>

### [**](#waitForRequest)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5062)externalinheritedwaitForRequest

* ****waitForRequest**(urlOrPredicate, options): Promise\<Request>

- Inherited from Page.waitForRequest

  Waits for the matching request and returns it. See [waiting for event](https://playwright.dev/docs/events#waiting-for-event) for more details about events.

  **Usage**

  ```
  // Start waiting for request before clicking. Note no await.
  const requestPromise = page.waitForRequest('https://example.com/resource');
  await page.getByText('trigger request').click();
  const request = await requestPromise;

  // Alternative way with a predicate. Note no await.
  const requestPromise = page.waitForRequest(request =>
    request.url() === 'https://example.com' && request.method() === 'GET',
  );
  await page.getByText('trigger request').click();
  const request = await requestPromise;
  ```

  ***

  #### Parameters

  * ##### externalurlOrPredicate: string | RegExp | (request) => boolean | Promise\<boolean>

    Request URL string, regex or predicate receiving [Request](https://playwright.dev/docs/api/class-request) object.

  *
    ##### externaloptionaloptions: { timeout?<!-- -->: number }
    * ##### externaloptionaltimeout: number

      Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) method.

  #### Returns Promise\<Request>

### [**](#waitForResponse)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5098)externalinheritedwaitForResponse

* ****waitForResponse**(urlOrPredicate, options): Promise\<Response>

- Inherited from Page.waitForResponse

  Returns the matched response. See [waiting for event](https://playwright.dev/docs/events#waiting-for-event) for more details about events.

  **Usage**

  ```
  // Start waiting for response before clicking. Note no await.
  const responsePromise = page.waitForResponse('https://example.com/resource');
  await page.getByText('trigger response').click();
  const response = await responsePromise;

  // Alternative way with a predicate. Note no await.
  const responsePromise = page.waitForResponse(response =>
    response.url() === 'https://example.com' && response.status() === 200
        && response.request().method() === 'GET'
  );
  await page.getByText('trigger response').click();
  const response = await responsePromise;
  ```

  ***

  #### Parameters

  * ##### externalurlOrPredicate: string | RegExp | (response) => boolean | Promise\<boolean>

    Request URL string, regex or predicate receiving [Response](https://playwright.dev/docs/api/class-response) object. When a [`baseURL`](https://playwright.dev/docs/api/class-browser#browser-new-context-option-base-url) via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor.

  *
    ##### externaloptionaloptions: { timeout?<!-- -->: number }
    * ##### externaloptionaltimeout: number

      Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

  #### Returns Promise\<Response>

### [**](#waitForSelector)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L727)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L771)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L815)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L859)externalinheritedwaitForSelector

* ****waitForSelector**\<K>(selector, options): Promise\<ElementHandleForTag\<K>>
* ****waitForSelector**(selector, options): Promise\<ElementHandle\<HTMLElement | SVGElement>>
* ****waitForSelector**\<K>(selector, options): Promise\<null | ElementHandleForTag\<K>>
* ****waitForSelector**(selector, options): Promise\<null | ElementHandle\<HTMLElement | SVGElement>>

- Inherited from Page.waitForSelector

  **NOTE** Use web assertions that assert visibility or a locator-based [locator.waitFor(\[options\])](https://playwright.dev/docs/api/class-locator#locator-wait-for) instead. Read more about [locators](https://playwright.dev/docs/locators).

  Returns when element specified by selector satisfies [`state`](https://playwright.dev/docs/api/class-page#page-wait-for-selector-option-state) option. Returns `null` if waiting for `hidden` or `detached`.

  **NOTE** Playwright automatically waits for element to be ready before performing an action. Using [Locator](https://playwright.dev/docs/api/class-locator) objects and web-first assertions makes the code wait-for-selector-free.

  Wait for the [`selector`](https://playwright.dev/docs/api/class-page#page-wait-for-selector-option-selector) to satisfy [`state`](https://playwright.dev/docs/api/class-page#page-wait-for-selector-option-state) option (either appear/disappear from dom, or become visible/hidden). If at the moment of calling the method [`selector`](https://playwright.dev/docs/api/class-page#page-wait-for-selector-option-selector) already satisfies the condition, the method will return immediately. If the selector doesn't satisfy the condition for the [`timeout`](https://playwright.dev/docs/api/class-page#page-wait-for-selector-option-timeout) milliseconds, the function will throw.

  **Usage**

  This method works across navigations:

  ```
  const { chromium } = require('playwright');  // Or 'firefox' or 'webkit'.

  (async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    for (const currentURL of ['https://google.com', 'https://bbc.com']) {
      await page.goto(currentURL);
      const element = await page.waitForSelector('img');
      console.log('Loaded image: ' + await element.getAttribute('src'));
    }
    await browser.close();
  })();
  ```

  ***

  #### Parameters

  * ##### externalselector: K

    A selector to query for.

  * ##### externaloptionaloptions: PageWaitForSelectorOptionsNotHidden

  #### Returns Promise\<ElementHandleForTag\<K>>

### [**](#waitForTimeout)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5127)externalinheritedwaitForTimeout

* ****waitForTimeout**(timeout): Promise\<void>

- Inherited from Page.waitForTimeout

  **NOTE** Never wait for timeout in production. Tests that wait for time are inherently flaky. Use [Locator](https://playwright.dev/docs/api/class-locator) actions and web assertions that wait automatically.

  Waits for the given [`timeout`](https://playwright.dev/docs/api/class-page#page-wait-for-timeout-option-timeout) in milliseconds.

  Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going to be flaky. Use signals such as network events, selectors becoming visible and others instead.

  **Usage**

  ```
  // wait for 1 second
  await page.waitForTimeout(1000);
  ```

  ***

  #### Parameters

  * ##### externaltimeout: number

    A timeout to wait for

  #### Returns Promise\<void>

### [**](#waitForURL)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5144)externalinheritedwaitForURL

* ****waitForURL**(url, options): Promise\<void>

- Inherited from Page.waitForURL

  Waits for the main frame to navigate to the given URL.

  **Usage**

  ```
  await page.click('a.delayed-navigation'); // Clicking the link will indirectly cause a navigation
  await page.waitForURL('**/target.html');
  ```

  ***

  #### Parameters

  * ##### externalurl: string | RegExp | (url) => boolean

    A glob pattern, regex pattern or predicate receiving \[URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string.

  *
    ##### externaloptionaloptions: { timeout?<!-- -->: number; waitUntil?<!-- -->: domcontentloaded | load | networkidle | commit }
    * ##### externaloptionaltimeout: number

      Maximum operation time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `navigationTimeout` option in the config, or by using the [browserContext.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-navigation-timeout), [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout), [page.setDefaultNavigationTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-navigation-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

    * ##### externaloptionalwaitUntil: domcontentloaded | load | networkidle | commit

      When to consider operation succeeded, defaults to `load`. Events can be either:

      * `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
      * `'load'` - consider operation to be finished when the `load` event is fired.
      * `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead.
      * `'commit'` - consider operation to be finished when network response is received and the document started loading.

  #### Returns Promise\<void>

### [**](#workers)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/playwright-core/types/types.d.ts#L5174)externalinheritedworkers

* ****workers**(): Worker\[]

- Inherited from Page.workers

  This method returns all of the dedicated [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) associated with the page.

  **NOTE** This does not contain ServiceWorkers

  ***

  #### Returns Worker\[]
