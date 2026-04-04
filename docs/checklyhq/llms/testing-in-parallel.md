# Source: https://checklyhq.com/docs/learn/playwright/testing-in-parallel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to run Playwright tests in parallel

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

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright offers robust capabilities for automating browser tests. However, a common question among developers revolves around the best practices for structuring Playwright projects, especially when tests involve significant environment changes, resource creation, or database updates.

This post describes strategies for running Playwright tests in parallel, sequence, or both while optimizing your testing workflow for efficiency and reliability.

## Understanding Test Types: stateful vs stateless

Before getting into the technicalities of test execution, you must categorize your tests into two main types: stateless and stateful.

* **Stateless Tests** do not rely on a specific state of the environment and do not alter any global configuration. Since they are isolated in their operations, running them in parallel is generally safe and efficient. Stateless tests won't interfere with each other.
* **Stateful Tests** modify the environment by creating or deleting resources, or changing global configuration. Such tests can easily conflict if run in parallel, as one test's actions might disrupt another's expected environment state.

<Note>
  Tests that start and rely on a state created by a previous test are typically considered antipatterns. Tests should create and clean up their own state to avoid cluttering test environments and enable parallelization.
</Note>

## Playwright's Default Test Execution

Before you start wondering how to parallelize all your Playwright tests, be aware that you probably run some of your tests in parallel already.

By default, **Playwright runs your test files in parallel, and all tests in a single file are run in order and with the same worker process**.

<img src="https://mintcdn.com/checkly-422f444a/qO288JasnPmYv-Y5/images/learn/images/default-execution@2x.jpg?fit=max&auto=format&n=qO288JasnPmYv-Y5&q=85&s=96168c2dcfdb456a9c5ef12d0c179fb9" alt="Playwright default execution mode" width="2110" height="1092" data-path="images/learn/images/default-execution@2x.jpg" />

This default execution model is a sane default. It safely runs tests in a single file in order while still trying to parallelize all the `spec` files.

The execution model can be changed in multiple ways if you want to parallelize more tests or have specific requirements:

* set `fullyParallel: true` in your `playwright.config`
* change a test file's execution model using `test.describe.configure`
* limit the numbers of `workers` in your `playwright.config` or via the command line

Let's look at common execution scenarios and their required configuration.

## Running Tests Sequentially

While parallel execution is efficient, specific scenarios require running tests sequentially. This is especially true for destructive and stateful tests, where ensuring a predictable and unaltered environment state is crucial for test accuracy.

If you want to run all project tests sequentially, you can turn off Playwright's parallelism entirely. Limit the number of worker processes to one process, and all tests from all files will run after another.

<Note>
  But remember that you usually want to parallelize as many tests as possible to keep the test execution times low.
</Note>

You can limit the workers via the command line:

```sh  theme={null}
npx playwright test --workers=1
```

Or set the `workers` property to `1` in your `playwright.config`.

```ts playwright.config.ts theme={null}
export default defineConfig({
  workers: 1,
});
```

There are multiple options if you want to run only a subset of your tests sequentially in one worker.

```sh  theme={null}
# Run all test files in `./tests/sequential` sequentially
npx playwright test --workers=1 ./tests/sequential

# Run all tests with the test tag `@sequential` sequentially
npx playwright test --workers=1 --grep @sequential

# Run all tests in the `sequential` project sequentially
npx playwright test --workers=1 --project=sequential
```

You can run a subset of test files, grep for specific test tags, or define a separate project to run tests sequentially. None of these approaches is better; you must decide what fits your project best.

## Running Tests in Parallel

Thanks to Playwright's automatic encapsulation and easy-to-use worker functionality, the test runner naturally excels at executing tests in parallel, significantly reducing the time it takes to execute your entire test suite.

By default, running multiple workers is limited to test files. Still, you can configure Playwright to parallelize running all your non-destructive and stateless tests, each running in its isolated environment.

To explicitly configure all your tests to run in parallel, you can utilize the `fullyParallel` option in your Playwright configuration file or project settings. This option instructs Playwright to maximize parallelism by launching separate workers for each test file.

Playwright will now try to run as many tests in parallel regardless of where they're defined.

```ts playwright.config.ts theme={null}
export default defineConfig({
  fullyParallel: true,
});
```

However, there are even more configuration options, and the test execution order in test files and groups can still be tweaked another way.

## Playwright's different execution modes

While you can control test execution order and parallelism via the `workers` and `fullyParallel` option, Playwright also allows you to configure each test file or group with predefined execution modes.

### The `serial` mode (sequential)

If you want to run all your project tests using `fullyParallel`, but one file's test should run sequentially, use the `serial` mode.

```ts serial.spec.ts theme={null}
import { test, type Page } from '@playwright/test';

/**
 * Run tests in this file sequentially and stop after a failure.
 *
 * -> If `One` fails `Two` won't be run.
 */
test.describe.configure({ mode: 'serial' });

test('One', async () => { /* ... */ });
test('Two', async () => { /* ... */ });
```

<Note>
  Note that by using the `serial` mode, a test failure will stop all the subsequent tests from running.
</Note>

### The `default` mode (sequential)

If you want to run all your tests using `fullyParallel`, but one file's test should run sequentially while ignoring all the test results, use the `default` mode.

```ts default.spec.ts theme={null}
import { test, type Page } from '@playwright/test';

/**
 * Run tests in this file sequentially regardless of their results
 *
 * -> If `One` fails `Two` is still run.
 */
test.describe.configure({ mode: 'default' });

test('One', async () => { /* ... */ });
test('Two', async () => { /* ... */ });
```

The `default` mode will run all defined tests and ignore if tests fail on the way.

### The `parallel` mode

If you don't want to parallelize all your tests with `fullyParallel` but still have one file with stateless tests that you want to run in parallel, use the `parallel` mode.

```ts default.spec.ts theme={null}
import { test, type Page } from '@playwright/test';

/**
 * Run tests in this file in parallel.
 */
test.describe.configure({ mode: 'parallel' });

test('One', async () => { /* ... */ });
test('Two', async () => { /* ... */ });
```

## Leveraging Playwright's Flexibility

Playwright's design accommodates various testing strategies, allowing developers to tailor test execution to their project's needs. Whether running tests in parallel to save time or sequentially to ensure environment stability, Playwright provides the tools necessary to configure your testing environment effectively.

### Tips for Organizing Tests

* Use directories, tags or projects to separate stateful and stateless tests and apply appropriate parallel or sequential execution modes.
* Name your test files strategically if relying on alphabetical execution order for sequencing.
* Consider leveraging Playwright's capabilities for test sharding and annotations for more complex test suite organization.

## Conclusion

Choosing between parallel and sequential execution in Playwright tests hinges on understanding your tests' nature and their impact on the application environment. By categorizing tests into stateful and stateless, developers can apply the appropriate execution strategy, ensuring efficiency and reliability in their E2E testing processes.

Over on [the Checkly YouTube channel](https://www.youtube.com/checklyhq), Stefan gets hands-on with Playwright test Parallelism and execution modes.

<YoutubeEmbed id="8NIm1QCUXE0" title="How to Run Playwright Test in &#x22;Parallel,&#x22; &#x22;Serial,&#x22; or &#x22;Default&#x22; Mode" />

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).