# Source: https://docs.statsig.com/experiments/statistical-methods/methodologies/one-sample-test.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# One-Sample Test

## One-Sample Tests (aka Fixed-Value Test)

A one-sample test compares a single sample of data against a known or hypothesized value to determine if there is a statistically significant difference. Unlike A/B tests that compare two groups, one-sample tests evaluate whether a single group differs from a specific benchmark, target, or historical baseline.

## When to Use One-Sample Tests

One-sample tests are useful for comparing a single group against a known value:

* **Single Group Events**: When only one group can trigger certain events (e.g., feature usage, error types), compare against expected baseline
* **Algorithm Testing**: Test if an algorithm performs better than random (e.g., testing if success rate differs from 50%)

## Statistical Considerations

One-sample tests provide a way to make statistical inferences about whether your observed data differs significantly from a hypothesized value. The test helps determine if any observed difference is due to random variation or represents a true change in the underlying process.

## How to Enable the Feature

1. Go to the setup page of an experiment

<img width="1167" height="562" alt="Experiment setup screen highlighting metrics section" src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/statistical-methods/methodologies/one-sample-test/742634e0-0db9-44f9-b849-0a205f604a76.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=ced5225a381da357d3709883bbd97356" data-path="images/experiments/statistical-methods/methodologies/one-sample-test/742634e0-0db9-44f9-b849-0a205f604a76.png" />

2. Click the metric name

<img width="226" height="73" alt="Metric name dropdown showing configure options" src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/statistical-methods/methodologies/one-sample-test/3a645771-4771-480e-a263-15a6af951284.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=98df48c2879cfbce09282d72db1ca3db" data-path="images/experiments/statistical-methods/methodologies/one-sample-test/3a645771-4771-480e-a263-15a6af951284.png" />

3. Select Use Fixed Baseline as Control

<img width="507" height="503" alt="Fixed baseline control modal for one-sample test configuration" src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/statistical-methods/methodologies/one-sample-test/9c7e85d6-e0b0-40bb-a22c-a96d7084d3e7.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=fb02f62a41a4412dd0a64f7ecf63abec" data-path="images/experiments/statistical-methods/methodologies/one-sample-test/9c7e85d6-e0b0-40bb-a22c-a96d7084d3e7.png" />


Built with [Mintlify](https://mintlify.com).