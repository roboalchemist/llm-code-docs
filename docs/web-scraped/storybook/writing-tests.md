# Storybook Documentation
# Source: https://storybook.js.org/docs/writing-tests
# Page: /docs/writing-tests

# How to test UIs with Storybook

Storybook [stories](./writing-stories) are test cases for your UI components in their various states and configurations. With Storybook, you can develop and test your components at the same time, in multiple ways, with instant feedback.

Storybook tackles UI component testing from a holistic perspective, ensuring that you can not only execute component tests quickly and reliably, but that you also have well established patterns to develop, debug, maintain, and even collaborate on these tests across the development lifecycle.

## 

Get started

If your project is using Vite, you can likely use the [Vitest addon](./writing-tests/integrations/vitest-addon) to run your component tests in Storybook. This addon is built on top of [Vitest](https://vitest.dev/), a fast and lightweight test runner that works seamlessly with Vite.

Run this command, which will install and configure the Vitest addon and Vitest:

npm
    
    
    npx storybook add @storybook/addon-vitest

The full installation instructions, including project requirements, are available in the [Vitest addon documentation](./writing-tests/integrations/vitest-addon/index#install-and-set-up).

Once your project is set up, you will see a testing widget in the bottom of your sidebar. After running tests, you will also see test status indicators on sidebar items. Additionally, many tests can be debugged with an addon panel.

![Storybook app with story status indicators, testing widget, and interactions panel annotated](/docs-assets/10.1/writing-tests/testing-ui-overview.png)

If you cannot use the Vitest addon in your project, you can still run tests using the [test-runner](./writing-tests/integrations/test-runner).

Next, we’ll cover some key concepts of testing in Storybook.

## 

Key concepts

Testing in Storybook is similar to other testing environments. Most of the knowledge and techniques you’ve been using apply here, too. But there are also some significant improvements.

### 

Component tests

A component test is a test which:

  * Renders a component in the browser for high fidelity
  * Simulates a user interacting with actual UI, like an end-to-end (E2E) test
  * Only tests a unit (e.g. a single component) of UI, **and** can reach into the implementation to mock things or manipulate data, like a unit test



This combination of using a real browser, simulating behavior, and mocking provides a powerful means of testing the functional aspects of your UI.

In Storybook, the entire testing experience is built around component tests. This means that you can run your tests in the same environment as your stories, with the same tools and techniques.

### 

Storybook Test

Storybook Test enables real time testing of your stories, through the [Vitest addon](./writing-tests/integrations/vitest-addon). It uses a Vitest plugin to automatically transform your stories into real Vitest tests, which are then run with Vitest’s browser mode.

### 

Watch mode

Get instant test feedback as you develop with watch mode. It will watch your code—either the component source or the tests—for changes and automatically re-run only the relevant tests. It’s perfect for test-driven development, where you write your tests first and then the component.

To activate watch mode, press the watch mode button (the eye icon) in the testing widget:

![Testing widget with watch mode enabled](/docs-assets/10.1/writing-tests/test-widget-watch-mode-enabled.png)

### 

CI

If you’re not running Storybook Test as part of your CI, you’re missing out on the biggest benefit it provides: catching bugs on PRs before you merge them.

If you are already running `vitest` as part of your CI then your stories should automatically run as tests “for free” when you commit your changes to Git.

If you’re not yet running Vitest in CI, you should set that up. First by adding a new script to your `package.json`:

package.json
    
    
    { 
      "scripts": {
        "test-storybook": "vitest --project=storybook"
      }
    }  

Note that this assumes you have a Vitest project called “storybook” for your stories, which is the default configuration when you install Storybook Test. If you’ve renamed it, adjust the script accordingly.

Next, add a new CI workflow.

If you use Github Actions that would look like:.github/workflows/test-storybook.yml
    
    
    name: Storybook Tests
     
    on: [push]
     
    jobs:
      test:
        runs-on: ubuntu-latest
        container:
          # Make sure to grab the latest version of the Playwright image
          # https://playwright.dev/docs/docker#pull-the-image
          image: mcr.microsoft.com/playwright:v1.52.0-noble
        steps:
          - uses: actions/checkout@v4
          
          - name: Setup Node
            uses: actions/setup-node@v4
            with:
              node-version: 22.12.0
          
          - name: Install dependencies
            run: npm ci
          
          - name: Run tests
            run: npm run test-storybook

If you are using a different CI provider, please consult our full [CI guide](./writing-tests/in-ci) for more information.

Storybook Test uses Playwright to render your stories by default. For the fastest experience, you should use [a machine image that has Playwright already installed](https://playwright.dev/docs/docker#pull-the-image) (as in the snippet above).

### 

Coverage

Code coverage provides insight into which code is tested or not. It functions as a guardrail as you develop, to help be sure your work is covered by the proper tests.

In Storybook Test, you can see the coverage provided by your stories in two ways. First, a summary is displayed in the testing widget. Second, clicking that coverage summary will open a full, interactive report.

![Two browser windows. The frontmost one shows the interactive coverage report generated by the Vitest addon. The background one shows the Storybook sidebar with the coverage summary visible in the testing widget.](/docs-assets/10.1/writing-tests/coverage-summary-and-report.png)

In the report, clicking through to a specific component shows the exact branches of code that are covered or not covered:

![Interactive coverage report generated by the Vitest addon, showing the Page component's reported source](/docs-assets/10.1/writing-tests/coverage-report-html-component.png)

Each project’s coverage report will look different, but the important things to note are:

  1. **The overall line/branch coverage** , which serves as a high-level health check.
  2. **Specific lines/branches** that are not covered, which are potential test gaps.



In our point of view, the goal is not to get 100% coverage and fill every gap, but rather to have a barometer to help you judge code/test changes, and for the gaps to inform you of key states or interactions that are untested. For example, if you’re building a prototype you might skip testing altogether, whereas in a critical app you might want to dot every i and cross every t.

Running coverage analysis can slow down your test runs, so it is turned off by default. To activate coverage, check the coverage checkbox in the testing widget.

![Testing widget with coverage activated](/docs-assets/10.1/writing-tests/test-widget-coverage-enabled.png)

#### 

Coverage in CI

And while we’re looking at coverage, update your CI workflow to include it:
    
    
    - yarn test
    + yarn test --coverage

💡

Why are we running all tests (`yarn test`) instead of just the Storybook tests (`yarn test-storybook`)? Because a coverage report is most accurate when accounting for all tests in your project, not just the stories you've written.

Seeing [Storybook-specific coverage](./writing-tests/test-coverage#storybook-ui) can be helpful, but in CI output, you want to see the comprehensive coverage of your project.

This way we can track the coverage change in every PR.

Those are the key concepts you’ll need to test in Storybook. Now, let’s look at the different types of tests you can perform.

## 

Types of tests

Storybook Test supports a variety of testing types to help you validate your work in multiple dimensions.

### 

Render tests

The most important tool for testing your components in Storybook is stories that render your components in various states.

However, you might not be aware that a basic story is also a [smoke test](https://en.wikipedia.org/wiki/Smoke_testing_\(software\)), which we call a **render test**. The test passes when the story renders successfully and fails when it errors.

Depending on the complexity of your components, you might be able to capture many of your key UI states this way.

### 

[Interaction tests](./writing-tests/interaction-testing)

Render tests are a very basic kind of interaction test. To test stateful components or verify interactive behavior, you define a play function for your story:

CSF 3CSF Next 🧪

Dialog.stories.ts

Typescript
    
    
    // Replace your-framework with the name of your framework (e.g. react-vite, vue3-vite, etc.)
    import type { Meta, StoryObj } from '@storybook/your-framework';
    import { expect } from 'storybook/test';
     
    import { Dialog } from './Dialog';
     
    const meta = {
      component: Dialog,
    } satisfies Meta<typeof Dialog>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    export const Opens: Story = {
      play: async ({ canvas, userEvent }) => {
        // Click on a button and assert that a dialog appears
        const button = canvas.getByRole('button', { text: 'Open Modal' });
        await userEvent.click(button);
        await expect(canvas.getByRole('dialog')).toBeInTheDocument();
      },
    };

But `play` functions can also be used for setting up state, creating spies, mocking out the network, simulating user interactions with your components, asserting output, and more. They are the meat and potatoes of testing and are the foundation for the rest of your testing journey in Storybook.

Here’s a more complex example, which includes [spying and mocking](./writing-tests/interaction-testing#spying-on-functions-with-fn) via the `fn` utility.

CSF 3CSF Next 🧪

EventForm.stories.ts

Typescript
    
    
    // Replace your-framework with the name of your framework (e.g. react-vite, vue3-vite, etc.)
    import type { Meta, StoryObj } from '@storybook/your-framework';
    import { fn, expect } from 'storybook/test';
     
    import { users } from '../mocks/users';
    import { EventForm } from './EventForm';
     
    const meta = {
      component: EventForm,
    } satisfies Meta<typeof EventForm>;
    export default meta;
     
    type Story = StoryObj<typeof meta>;
     
    export const Submits: Story = {
      // Mock functions so we can manipulate and spy on them
      args: {
        getUsers: fn(),
        onSubmit: fn(),
      },
      beforeEach: async ({ args }) => {
        // Manipulate `getUsers` mock to return mocked value
        args.getUsers.mockResolvedValue(users);
      },
      play: async ({ args, canvas, userEvent }) => {
        const usersList = canvas.getAllByRole('listitem');
        await expect(usersList).toHaveLength(4);
        await expect(canvas.getAllByText('VIP')).toHaveLength(2);
     
        const titleInput = await canvas.findByLabelText('Enter a title for your event');
        await userEvent.type(titleInput, 'Holiday party');
     
        const submitButton = canvas.getByRole('button', { text: 'Plan event' });
        await userEvent.click(submitButton);
     
        // Spy on `onSubmit` to verify that it is called correctly
        await expect(args.onSubmit).toHaveBeenCalledWith({
          name: 'Holiday party',
          userCount: 4,
          data: expect.anything(),
        });
      },
    };

For more information on how to write interaction tests and mocks using the `play` function, please see the [interaction testing guide](./writing-tests/interaction-testing#writing-interaction-tests).

### 

[Accessibility tests](./writing-tests/accessibility-testing)

Storybook’s [Accessibility (A11y) addon](https://storybook.js.org/addons/@storybook/addon-a11y) runs a set of automated checks on your stories to help ensure your components can be used by all users, regardless of ability or technology they're using. That means supporting requirements such as: keyboard navigation, screen reader support, usable color contrast, etc.

Accessibility is not only the right thing to do, but it is increasingly mandated. For example, the [European accessibility act](https://ec.europa.eu/social/main.jsp?catId=1202) is scheduled to go into law in June 2025. Similarly in the US, laws like the [Americans with Disabilities Act (ADA)](https://www.ada.gov/) and [Section 508 of the Rehabilitation Act](https://www.section508.gov/) apply to many public-facing services.

To activate accessibility checks alongside your component tests, check the Accessibility checkbox in the testing widget.

![Testing widget with accessibility activated](/docs-assets/10.1/writing-tests/test-widget-a11y-enabled.png)

Once activated, you will see accessibility failures in the sidebar.

![Storybook showing a failing accessibility test in both the sidebar story menu and the Accessibility panel](/docs-assets/10.1/writing-tests/test-a11y-overview.png)

Any failures can be debugged in the Accessibility addon panel.

![Storybook app with accessibility panel open, showing violations and an interactive popover on the violating elements in the preview](/docs-assets/10.1/writing-tests/addon-a11y-debug-violations.png)

### 

[Visual tests](./writing-tests/visual-testing)

Visual tests are the most efficient way to test your components. With the click of a button you can take snapshots of every story in your Storybook and compare those snapshots to baselines — last known “good” snapshots. Not only does this allow you to check the appearance of your components, but they are also able to check a large subset of component functionality [without having to write or maintain any test code](https://storybook.js.org/blog/visual-testing-is-the-greatest-trick-in-ui-development/)!

Storybook supports cross-browser visual testing natively using [Chromatic](https://www.chromatic.com/storybook/?ref=storybook_site), a cloud service made by the Storybook team. When you enable visual testing, every story is automatically turned into a test. This gives you instant feedback on UI bugs directly in Storybook.

![Visual test panel with diff](/docs-assets/10.1/writing-tests/vta-changes-found.png)

### 

[Snapshot tests](./writing-tests/snapshot-testing)

In most cases, the other testing types will provide more coverage with less effort. But there are scenarios where it can be helpful to compare the rendered markup of a story against a known baseline. For example, it can help identify markup changes that trigger rendering errors.

## 

Reusing stories in other testing tools

Stories are made to be reusable, so you can use them as test cases in popular testing tools.

### 

[End-to-end](./writing-tests/integrations/stories-in-end-to-end-tests)

Sometimes you need to test a full workflow, with the full running stack. In those cases, you can still use your stories by importing them within your Playwright or Cypress end-to-end (E2E) tests.

### 

[Unit](./writing-tests/integrations/stories-in-unit-tests)

If you prefer, you can reuse your Storybook stories in a traditional testing environment, like Vitest or Jest.

**More testing resources**

  * [Vitest addon](./writing-tests/integrations/vitest-addon) for running tests in Storybook
  * [Interaction testing](./writing-tests/interaction-testing) for user behavior simulation
  * [Accessibility testing](./writing-tests/accessibility-testing) for accessibility
  * [Visual testing](./writing-tests/visual-testing) for appearance
  * [Snapshot testing](./writing-tests/snapshot-testing) for rendering errors and warnings
  * [Test coverage](./writing-tests/test-coverage) for measuring code coverage
  * [CI](./writing-tests/in-ci) for running tests in your CI/CD pipeline
  * [End-to-end testing](./writing-tests/integrations/stories-in-end-to-end-tests) for simulating real user scenarios
  * [Unit testing](./writing-tests/integrations/stories-in-unit-tests) for functionality
  * [Test runner](./writing-tests/integrations/test-runner) to automate test execution



Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/writing-tests/index.mdx)