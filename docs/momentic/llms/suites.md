# Source: https://momentic.ai/docs/suites.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Suites

<Info>Suites are only available on Momentic Cloud.</Info>

You can use suites to group and run tests together. You can configure shared
schedules, notifications, and environments for all tests in a suite.

Select **Suites** on the left sidebar to view all your suites. Click on the
**Create suite** button in the top-right corner to create a new suite.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/suites.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=1f91f09f28536c05fe281a8b589b809e" width="3620" height="2432" data-path="images/suites.png" />
</Frame>

## Setup & teardown

The setup test will always run first before any other tests in the suite. If it
fails, the rest of the suite will be skipped and the entire suite will be marked
as failed.

If the setup test succeeds, Momentic will continue running the tests in the
suite. **All tests in the suite will run in parallel**.

Whenever the suite's final result is determined, Momentic will start running the
teardown test. The teardown test's result does not affect the overall suite
result.

### Persistent variables

To allow passing data between tests in a suite, Momentic exposes the
`setPersistentVariable` JavaScript function. This function allows users to set a
[variable](/variables) that is accessible by later tests.

```javascript  theme={null}
setPersistentVariable("CREATED_USERNAME", "randomusername");
```


Built with [Mintlify](https://mintlify.com).