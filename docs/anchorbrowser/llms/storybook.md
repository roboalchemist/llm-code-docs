# Source: https://docs.anchorbrowser.io/integrations/open-source/playwright/e2e-testing/storybook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Storybook

> Test Storybook components with Playwright's component testing framework.

# How to Test Storybook with Playwright

Test your Storybook components directly with Playwright's component testing framework. You'll catch UI bugs early by testing components in a real browser environment. Use Storybook's experimental Playwright integration to mount and interact with your stories.

[View the complete example](https://github.com/storybookjs/storybook/blob/795e05c3e6a72d7de10fbb2f4cb309e4dd333f46/docs/_snippets/portable-stories-playwright-ct.md) from the Storybook project.

## Setup

Install the required packages:

```bash  theme={null}
npm install @storybook/react/experimental-playwright @playwright/experimental-ct-react
```

## Write Tests

Create tests that mount your stories:

```JavaScript  theme={null}
import { createTest } from '@storybook/react/experimental-playwright';
import { test as base } from '@playwright/experimental-ct-react';
import stories from './Button.stories.portable';

const test = createTest(base);

test('renders primary button', async ({ mount }) => {
  await mount(<stories.Primary />);
});

test('renders with custom props', async ({ mount }) => {
  const component = await mount(<stories.Primary label="custom label" />);
  await expect(component).toContainText('custom label');
});

```

The `mount` function executes your story's loaders, render, and play functions automatically. You can override props and test different component states.

## Scale your Storybook testing with Anchor Browser

Run your Playwright component tests on cloud browsers with enterprise-grade reliability and performance. Learn more and get started for free: [https://anchorbrowser.io](https://anchorbrowser.io)
