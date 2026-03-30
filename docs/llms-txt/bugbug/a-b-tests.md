# Source: https://docs.bugbug.io/troubleshooting/a-b-tests.md

# A/B tests

Running some A/B tests on your website under tests could make tests flaky because your website renders differently depending on the browser session and the A/B test drawn.  This is especially problematic for smoke tests in production environments.

There are a few solutions to prevent this situation:

1. Disable A/B tests for specific IP addresses. This is probably the easiest solution, but it depends on the A/B testing tool that you use. Some of them have the option to disable A/B tests for specific IPs. In this case, you should disable A/B tests for our cloud runners [IP list of cloud runners](https://docs.bugbug.io/troubleshooting/ips-list-of-cloud-runners) but also your local IP address.
2. Exclude A/B testing script based on query string parameter. Using Google Tag Manager and loading custom JavaScript code from an external A/B tool is popular. You can exclude the loading of this script based on the query string parameter. To do this, add `?bugbug=1` to your Goto URL step in tests and exclude loading of the A/B test script based on this parameter.
3. Manually mark your browser session as A or B version. This requires some development knowledge. A/B testing tools use cookies or local storage to store information about the test version. If you are familiar with DevTools, you can check what kind of cookies or localStorage item has been added and set this manually in your tests using [Custom JavaScript](https://docs.bugbug.io/editing-tests/custom-javascript-actions#javascript-steps) to bind the same website version with tests.
