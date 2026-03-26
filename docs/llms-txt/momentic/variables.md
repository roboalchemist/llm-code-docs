# Source: https://momentic.ai/docs/variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Variables

Variables are a powerful feature in Momentic that allow you to store and reuse
data across your tests. They can be used to store values like user credentials,
URLs, or any other data that you want to reference multiple times in your tests.

## Environment variables

All variables are stored on a global object `env` that is accessible from any
step in your test. You can access these variables using the templating syntax
`{{ env.VARIABLE_NAME }}`.

Reserved variables:

* `BASE_URL`: The base URL of the environment. This is automatically set when
  you create a new environment and can be used to construct URLs for your tests.
* `CURRENT_URL`: The current URL of the page being tested. This is updated
  automatically as you navigate through your test.
* `ENV_NAME`: The name of the environment. This is also automatically set when
  you create a new environment and can be used to identify the environment in
  your tests.
* `TEST_NAME`: The name of the test. This is automatically set when you create a
  new test and can be used to identify the test in your tests.

You can add any number of key-value pairs as environment variables when you
create a new environment in Momentic. Any tests that you create using that
environment will have access to these variables.

If you're using the [Momentic CLI](/quickstart/cli), you can also load
environment variables from a `.env` or JSON file.

## Setting variables

### `setVariable`

You can use [JavaScript](/steps/javascript) steps to set variables using the
`setVariable` function.

```javascript  theme={null}
setVariable("USERNAME", "testuser");
setVariable("PASSWORD", Math.random().toString(36).substring(2, 15));
```

This will set the `USERNAME` variable to `testuser` and the `PASSWORD` variable
to a random string. You can then access these variables in other steps using the
templating syntax `{{ env.USERNAME }}` or `{{ env.PASSWORD }}`.

### Save to environment variable

For steps that can have a return value such as [AI extract](/steps/ai-extract)
or [JavaScript](/steps/javascript), there's an option on the step that allows
you to input a string key to set on the environment. After this step is executed
you will be able to access the variable using `{{ env.NUM_BUTTONS }}`.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/save-to-environment-variable.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=38a36b4a69376c69cced8ed395ddb9ca" width="1272" height="1432" data-path="images/save-to-environment-variable.png" />
</Frame>

## Accessing variables

Variables can be accessed using JavaScript. You can use it directly inside
[JavaScript](/steps/javascript) steps or by using the templating syntax `{{ }}`.
All input fields support the templating syntax.

For example, if you have set a variable named `USERNAME`, you can access it like
this:

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/accessing-variable.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=816563be013702996a2c3c8b48cd108f" width="1248" height="1590" data-path="images/accessing-variable.png" />
</Frame>

### Module parameters

Module parameters are also variables. If you have a module parameter named
`API_KEY`, you can access it using `{{ env.API_KEY }}`.

## Variable scope

Variables in Momentic tests all live on the global test scope, which means they
are accessible from any step in the test. This allows you to set a variable in
one step and use it in another step later in the test.


Built with [Mintlify](https://mintlify.com).