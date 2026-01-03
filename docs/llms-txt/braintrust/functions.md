# Source: https://braintrust.dev/docs/reference/functions.md

# Functions

Many of the advanced capabilities of Braintrust involve defining and calling custom code functions. Currently,
Braintrust supports defining functions in JavaScript/TypeScript and Python, which you can use as custom scorers
or callable tools.

This guide serves as a reference for functions, how they work, and some security considerations when working with them.

## Access functions

Several places in the UI, for example the custom scorer menu in the playground, allow you to define functions. You can also
bundle them in your code and push them to Braintrust with `braintrust push` and `braintrust eval --push`. Technically speaking,
functions are a generalization of prompts and code functions, so when you define a custom prompt, you are technically defining
a "prompt function".

### Organizing functions into projects

Functions are organized into projects using the `projects.create()` method:

<Tabs>
  <Tab title="TypeScript">
    ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import * as braintrust from "braintrust";

    // Get a handle to the project (creates if it doesn't exist)
    const project = braintrust.projects.create({ name: "my-project" });

    // Use the project to create functions
    project.tools.create({...});
    project.prompts.create({...});
    project.scorers.create({...});
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import braintrust

    # Get a handle to the project (creates if it doesn't exist)
    project = braintrust.projects.create(name="my-project")

    # Use the project to create functions
    project.tools.create(...)
    project.prompts.create(...)
    project.scorers.create(...)
    ```
  </Tab>
</Tabs>

<Note>
  If a project already exists, `projects.create()` returns a handle. There is no separate `.get()` method.
</Note>

Every function supports a number of common features:

* Well-defined parameters and return types
* Streaming and non-streaming invocation
* Automatic tracing and logging in Braintrust
* Prompts can be loaded into your code in the OpenAI argument format
* Prompts and code can be easily saved and uploaded from your codebase

See the [API docs](/api-reference) for more information on how to create and invoke functions.

## Sandbox

Functions are executed in a secure sandbox environment. If you are self-hosting Braintrust, refer to the [self-hosting guide](/guides/self-hosting) for information on configuring the sandbox environment for your deployment.

Custom code runs in quarantined environments that are sandboxed and isolated from your other infrastructure. For AWS deployments, this uses Lambda functions in a quarantined VPC.

For more information on the security architecture underlying code execution, please [reach out to us](mailto:support@braintrust.dev).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt