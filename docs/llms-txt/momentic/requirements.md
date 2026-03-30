# Source: https://momentic.ai/docs/environment/requirements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Requirements

In order to automate hundreds or thousands of end-to-end tests, and run them
concurrently, we need a testing environment that meets certain requirements.

## Resource class

For the best performance, we recommend using a resource class with **at least 2
vCPUs and 4 GB of RAM per browser instance** (these are the minimum
specifications needed for Chromium).

## Stability

Applications on the environment do not have frequent restarts or resource
consumption issues; and there is some form of change control to prevent
unexpected deployments.

## Concurrent user capacity

We run each of your tests in a separate worker, each of which acts as an
individual user. The test environment (and dependent databases, email servers,
etc.) must have the resources to support as many concurrent users as you have
tests.

## Configured for automated testing

Applications in the environment need to be configured so that the tests can
pass. For example:

* If the application has feature flags, the flags are set so that tests can
  pass.
* There is at least one user account created for Momentic, and the ability to
  programmatically add more as needed to run tests concurrently.
* Sub-one minute email and SMS delivery.


Built with [Mintlify](https://mintlify.com).