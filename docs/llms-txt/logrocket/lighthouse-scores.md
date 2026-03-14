# Source: https://docs.logrocket.com/docs/lighthouse-scores.md

# Lighthouse Scores

LogRocket should not impact your Lighthouse scores. To confirm this, we recommend creating a Lighthouse test with and without LogRocket installed, to see if there is an impact to your application.

## Third Party Script Explainer

Lighthouse will currently attribute execution and blocking time from other scripts to the LogRocket SDK. The SDK wraps other functions in order to capture unhandled exceptions (effectively wrapping other code in a try/catch). This can lead Lighthouse to attribute execution time to that wrapper, rather than the inner functions doing the actual work. This appears in Lighthouse reports in the following ways:

1. `LogRocket.min.js` can be falsely attributed with Third Party Main-Thread Blocking Time
2. `LogRocket.min.js` can be falsely attributed with JavaScript Execution Time

In order to prevent true sources of execution and blocking time from being masked, we recommend using the LogRocket NPM package as opposed to the `<script>` tag. See [Quickstart](https://docs.logrocket.com/docs/quickstart) for installation details.