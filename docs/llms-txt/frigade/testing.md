# Source: https://docs.frigade.com/sdk/advanced/testing.md

# Automated Testing

> Learn how to run unit and integration tests with your Frigade Flows

***

Unlike no-code tools, Frigade allows you to easily write automated tests for your Flows. In this guide, we will show you how to write and run tests for your Flows using Playwright and Jest. The same principles can be applied to any testing framework.

<Steps>
  <Step title="Using a test user">
    When writing tests for your Flows, you should use a test user. This user should have the same permissions and properties as the users who will use your Flow.

    Before running your tests, you will likely want to reset this user in Frigade. This can be done by making the following API request using your private API key in the Developer environment (see [API docs](/api-reference/users/users-delete) for more information):

    ```javascript
    function resetTestUser() {
      fetch('https://api.frigade.com/v1/users?foreignId=my-test-user-id', {
        method: 'DELETE',
        headers: {
          'Authorization
          : `Bearer ${process.env.FRIGADE_PRIVATE_DEV_API_KEY}`,
        },
      });
    }
    ```

    With this in hand, you can add a `beforeAll` to reset the test user before and after running your tests.

    ```javascript
    beforeAll(() => {
      resetTestUser();
    });
    ```
  </Step>

  <Step title="Writing tests">
    To write tests for your Flows, you can use Playwright, Puppeteer, or any other testing framework.

    In this example, we will use Playwright. This test presses the primary button with the text "Got it" in a `Frigade.Announcement` and ensures that the modal is closed.

    ```javascript
    const { test, expect } = require('@playwright/test');

    test('close announcement', async ({ page }) => {
      await page.goto('http://localhost:3000/');
      await page.click('text=Got it');
      await page.waitForSelector('text=Got it', { state: 'detached' });
    });
    ```
  </Step>

  <Step title="Going further">
    For testing more complex scenarios (for instance, the chaining of Flows), you can leverage the underlying Vanilla JS SDK to simulate completing the first Flow and then starting the second Flow.

    Methods such as `flow.complete()` or `step.complete()` support an optional `createdAt` parameter that can simulate the time of completion, too.

    ```javascript
    import { Frigade } from '@frigade/js'

    test('Flow is visible after completing other Flow', async () => {
        const frigade = new Frigade(process.env.FRIGADE_PRIVATE_DEV_API_KEY, {
          userId: "my-test-user-id"
        })
        const flow = await frigade.getFlow("flow_abc")
        expect(flow.isVisible).toBeFalsy() // The Flow is not yet visible because `flow_def` has not been completed
        await frigade.getFlow("flow_def").complete({
            // Overrides the date of completion
            createdAt: "2022-01-01T00:00:00Z",
          })
        expect(flow.isVisible).toBeTruthy() // The Flow is now visible
      })
    ```
  </Step>
</Steps>
