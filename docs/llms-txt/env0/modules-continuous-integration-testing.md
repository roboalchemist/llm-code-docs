# Source: https://docs.envzero.com/guides/admin-guide/private-registry/modules/modules-continuous-integration-testing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Modules in CI

> Run automated CI tests on private registry modules using OpenTofu tftest files in env zero

env zero's module testing feature allows you to stay on top of your modules' health at any point, running tests with any change done to your modules. All information will be visible within env zero and your VCS, providing a quick and clear view of your module's status and allowing you to identify and remediate issues quickly for your modules' consumers.

# Writing tests with OpenTofu tftest files

Module testing in env zero uses [Opentofu test command](https://opentofu.org/docs/cli/commands/test/). Start by writing your tests as [tftest files](https://opentofu.org/docs/cli/commands/test/#the-tftesthcl-file-structure). All of your module test files have to be saved within the VCS folder of your module in order to be executed by env zero.

# Set Testing Credentials and Self Hosted Agent

As your tests are executed by env zero, you can select which credentials are used for execution. Go to Registry Settings and select credentials to be used in the tests execution.\
If you're using Self Hosted Agents, you can also set up which Self Hosted Agent will be used to execute the tests.\
The credentials and agent will apply to tests executed on all modules in the registry.

# Enable & Run tests

## Configure module testing

When creating or editing a module, go to the Testing step and check Enable Testing.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/modules/e0b832b0229be5448a7fd2b2b161b3d2acff1bc92c7f89fc72f0dc108f15559c-screenshot_2024-09-12_at_10.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=43a368b160ee499c6b11910f7d5a3add" alt="Interface screenshot showing configuration options" width="1442" height="559" data-path="images/guides/admin-guide/private-registry/modules/e0b832b0229be5448a7fd2b2b161b3d2acff1bc92c7f89fc72f0dc108f15559c-screenshot_2024-09-12_at_10.png" />
</Frame>

When testing is enabled, `test` will be executed on each commit to the repository default branch. You can enable "Run tests on every PR" to make sure tests are also executed on each commit to a pull request targeting the default branch.

Select OpenTofu version or default to the latest version, then set up any variables required for your test execution.

<Info>
  **Organization Variable Inheritance**

  Organization Variables will be inherited by your module registry and applied to each test execution. You can override the organization variables in the Module level.
</Info>

## Manually trigger tests

You can also manually trigger a module run by clicking "Run Tests" on the module details page. A run will be immediately queued and you can see its details in the Tests tab.

<Info>
  **Version support**

  Module tests will always run on the latest version of the module.
</Info>

# Tracking test results your VCS and in env zero

When tests run is triggered by a commit, you'll be able to see status checks in your VCS indicating the test results triggered by the commit.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/modules/284ee36-image.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=c4e81aa09864d1eeb22c170b500d8801" alt="" width="914" height="154" data-path="images/guides/admin-guide/private-registry/modules/284ee36-image.png" />

In env zero, within each module, the Tests tab will show all historical testing runs executed on this module.

An overview recap of success, skipped, failed, and errored tests is given for each run. You can also see the type of run and which commit triggered the test execution.

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/01/e9633a6-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=34ea8ec6d0c369e241e1f6d7fbaa3ef4" alt="" width="2938" height="1616" data-path="images/changelogs/2024/01/e9633a6-image.png" />

Click any record in order to drill down into the logs of the specific run.

Within the Test Logs you'll be able to see the full details of the test execution. Each test file will have its own step with a success or failed status, and clicking the step will show the full breakdown of all test runs included in this file.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/modules/f1f6c48-image.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=134e976beabae3fdc23a9466072ea1c6" alt="" width="2934" height="1836" data-path="images/guides/admin-guide/private-registry/modules/f1f6c48-image.png" />

Built with [Mintlify](https://mintlify.com).
