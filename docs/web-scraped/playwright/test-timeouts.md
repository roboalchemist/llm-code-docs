# Source: https://playwright.dev/docs/test-timeouts

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Playwright Test]
-   [Timeouts]

On this page

<div>

# Timeouts

</div>

Playwright Test has multiple configurable timeouts for various tasks.

Timeout

Default

Description

Test timeout

30_000 ms

Timeout for each test\
[Set in config]\
``\
[Override in test]\
`test.setTimeout(120_000)`

Expect timeout

5_000 ms

Timeout for each assertion\
[Set in config]\
` }`\
[Override in test]\
`expect(locator).toBeVisible()`

## Test timeout[​](#test-timeout "Direct link to Test timeout") 

Playwright Test enforces a timeout for each test, 30 seconds by default. Time spent by the test function, fixture setups, and `beforeEach` hooks is included in the test timeout.

Timed out test produces the following error:

``` 
example.spec.ts:3:1 › basic test ===========================

Timeout of 30000ms exceeded.
```

Additional separate timeout, of the same value, is shared between fixture teardowns and `afterEach` hooks, after the test function has finished.

The same timeout value also applies to `beforeAll` and `afterAll` hooks, but they do not share time with any test.

### Set test timeout in the config[​](#set-test-timeout-in-the-config "Direct link to Set test timeout in the config") 

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

API reference: [testConfig.timeout](/docs/api/class-testconfig#test-config-timeout).

### Set timeout for a single test[​](#set-timeout-for-a-single-test "Direct link to Set timeout for a single test") 

example.spec.ts

``` 
import  from '@playwright/test';

test('slow test', async () => );

test('very slow test', async () => );
```

API reference: [test.setTimeout()](/docs/api/class-test#test-set-timeout) and [test.slow()](/docs/api/class-test#test-slow).

### Change timeout from a `beforeEach` hook[​](#change-timeout-from-a-beforeeach-hook "Direct link to change-timeout-from-a-beforeeach-hook") 

example.spec.ts

``` 
import  from '@playwright/test';

test.beforeEach(async (, testInfo) => );
```

API reference: [testInfo.setTimeout()](/docs/api/class-testinfo#test-info-set-timeout).

### Change timeout for `beforeAll`/`afterAll` hook[​](#change-timeout-for-beforeallafterall-hook "Direct link to change-timeout-for-beforeallafterall-hook") 

`beforeAll` and `afterAll` hooks have a separate timeout, by default equal to test timeout. You can change it separately for each hook by calling [testInfo.setTimeout()](/docs/api/class-testinfo#test-info-set-timeout) inside the hook.

example.spec.ts

``` 
import  from '@playwright/test';

test.beforeAll(async () => );
```

API reference: [testInfo.setTimeout()](/docs/api/class-testinfo#test-info-set-timeout).

## Expect timeout[​](#expect-timeout "Direct link to Expect timeout") 

Auto-retrying assertions like [expect(locator).toHaveText()](/docs/api/class-locatorassertions#locator-assertions-to-have-text) have a separate timeout, 5 seconds by default. Assertion timeout is unrelated to the test timeout. It produces the following error:

``` 
example.spec.ts:3:1 › basic test ===========================

Error: expect(received).toHaveText(expected)

Expected string: "my text"
Received string: ""
Call log:
  - expect.toHaveText with timeout 5000ms
  - waiting for "locator('button')"
```

### Set expect timeout in the config[​](#set-expect-timeout-in-the-config "Direct link to Set expect timeout in the config") 

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

API reference: [testConfig.expect](/docs/api/class-testconfig#test-config-expect).

### Specify expect timeout for a single assertion[​](#specify-expect-timeout-for-a-single-assertion "Direct link to Specify expect timeout for a single assertion") 

example.spec.ts

``` 
import  from '@playwright/test';

test('example', async () => );
});
```

## Global timeout[​](#global-timeout "Direct link to Global timeout") 

Playwright Test supports a timeout for the whole test run. This prevents excess resource usage when everything went wrong. There is no default global timeout, but you can set a reasonable one in the config, for example one hour. Global timeout produces the following error:

``` 
Running 1000 tests using 10 workers

  514 skipped
  486 passed
  Timed out waiting 3600s for the entire test run
```

You can set global timeout in the config.

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig();
```

API reference: [testConfig.globalTimeout](/docs/api/class-testconfig#test-config-global-timeout).

## Advanced: low level timeouts[​](#advanced-low-level-timeouts "Direct link to Advanced: low level timeouts") 

These are the low-level timeouts that are pre-configured by the test runner, you should not need to change these. If you happen to be in this section because your test are flaky, it is very likely that you should be looking for the solution elsewhere.

Timeout

Default

Description

Action timeout

no timeout

Timeout for each action\
[Set in config]\
` }`\
[Override in test]\
`locator.click()`

Navigation timeout

no timeout

Timeout for each navigation action\
[Set in config]\
` }`\
[Override in test]\
`page.goto('/', )`

Global timeout

no timeout

Global timeout for the whole test run\
[Set in config]\
``\

`beforeAll`/`afterAll` timeout

30_000 ms

Timeout for the hook\
[Set in hook]\
`test.setTimeout(60_000)`\

Fixture timeout

no timeout

Timeout for an individual fixture\
[Set in fixture]\
``\

### Set action and navigation timeouts in the config[​](#set-action-and-navigation-timeouts-in-the-config "Direct link to Set action and navigation timeouts in the config") 

playwright.config.ts

``` 
import  from '@playwright/test';

export default defineConfig(,
});
```

API reference: [testOptions.actionTimeout](/docs/api/class-testoptions#test-options-action-timeout) and [testOptions.navigationTimeout](/docs/api/class-testoptions#test-options-navigation-timeout).

### Set timeout for a single action[​](#set-timeout-for-a-single-action "Direct link to Set timeout for a single action") 

example.spec.ts

``` 
import  from '@playwright/test';

test('basic test', async () => );
  await page.getByText('Get Started').click();
});
```

## Fixture timeout[​](#fixture-timeout "Direct link to Fixture timeout") 

By default, [fixture](/docs/test-fixtures) shares timeout with the test. However, for slow fixtures, especially [worker-scoped](/docs/test-fixtures#worker-scoped-fixtures) ones, it is convenient to have a separate timeout. This way you can keep the overall test timeout small, and give the slow fixture more time.

example.spec.ts

``` 
import  from '@playwright/test';

const test = base.extend<>(, use) => , ]
});

test('example test', async () => );
```

API reference: [test.extend()](/docs/api/class-test#test-extend).