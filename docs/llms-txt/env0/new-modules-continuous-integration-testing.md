# Source: https://docs.envzero.com/changelogs/2024/01/new-modules-continuous-integration-testing.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔭 New: Modules Continuous Integration Testing

> We're excited to announce our Beta release of continuous integration testing for modules. Built using OpenTofu testing feature, you will now be able to set up testing and integrate it seamlessly into your private module registry.

We're excited to announce our Beta release of continuous integration testing for modules. Built using OpenTofu testing feature, you will now be able to set up testing and integrate it seamlessly into your private module registry. /

## Streamline your module CI with OpenTofu tests

Start by creating your [tftest files](https://opentofu.org/docs/cli/commands/test/#testing-modules) and storing them within your module directory. You'll be able to run common tests on a real infrastructure that is created, tested and destroyed in a single flow.

```hcl  theme={null}
run "test" {
  assert {
    condition     = file(local_file.test.filename) == "Hello world!"
    error_message = "Incorrect content in ${local_file.test.filename}."
  }
}
```

You can write multiple runs in each file, and create multiple test files. env0 will execute all of the tests in all of the files.

## Trigger and manage module tests in your module registry

With your test files in place, enable Testing in your module settings and env0 will trigger test runs on every merge to your default branch (and optionally on every PR targeting the main branch). env0 will then present the test results and a full history of all test runs.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/01/e9633a6-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=34ea8ec6d0c369e241e1f6d7fbaa3ef4" alt="Feature demonstration screenshot showing new functionality" width="2938" height="1616" data-path="images/changelogs/2024/01/e9633a6-image.png" />
</Frame>

Status checks will be presented in your VCS to give you all the information directly in your flow.

Learn more about module testing in our [docs](/guides/admin-guide/private-registry/modules/modules-continuous-integration-testing), and read more about OpenTofu GA on our [blog](https://www.env0.com/blog/celebrating-opentofu-ga-with-our-new-ci-testing-feature).

Built with [Mintlify](https://mintlify.com).
