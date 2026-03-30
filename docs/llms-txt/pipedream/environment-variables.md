# Source: https://pipedream.com/docs/workflows/environment-variables.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Variables

Environment variables (env vars) enable you to separate secrets and other static configuration data from your code.

You shouldn’t include API keys or other sensitive data directly in your workflow’s code. By referencing the value of an environment variable instead, your workflow includes a reference to that variable — for example, `process.env.API_KEY` instead of the API key itself.

You can reference env vars and secrets in [workflow code](/workflows/building-workflows/code/) or in the object explorer when passing data to steps, and you can define them either globally for the entire workspace, or scope them to individual projects.

| Scope         | Description                                                                                                                                                                                                                |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Workspace** | All environment variables are available to all workflows within the workspace. All workspace members can manage workspace-wide variables [in the UI](https://pipedream.com/settings/env-vars).                             |
| **Project**   | Environment variables defined within a project are only accessible to the workflows within that project. Only workspace members who have [access to the project](/projects/access-controls/) can manage project variables. |

## Creating and updating environment variables

* To manage **global** environment variables for the workspace, navigate to **Settings**, then click **Environment Variables**: [https://pipedream.com/settings/env-vars](https://pipedream.com/settings/env-vars)
* To manage environment variables within a project, open the project, then click **Variables** from the project nav on the left

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/82742810-project-vars_ilxq7x.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=3cd3652724146c636d97d2dd47ca6a02" width="431" height="499" data-path="images/82742810-project-vars_ilxq7x.png" />
</Frame>

Click **New Variable** to add a new environment variable or secret:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/b96b62c1-add-new-var-v2_ocvfoi.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=2fff06d9c4387da7648f19f28a27ec64" width="1170" height="502" data-path="images/b96b62c1-add-new-var-v2_ocvfoi.png" />
</Frame>

**Configure the required fields**:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/3a26bef5-add-var-modal-v2_nvu2eq.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=fcec43f613b784bb8ac939fd22bbec57" width="1299" height="1054" data-path="images/3a26bef5-add-var-modal-v2_nvu2eq.png" />
</Frame>

| Input field     | Description                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Key**         | Name of the variable — for example, `CLIENT_ID`                                                                              |
| **Value**       | The value, which can contain any string with a max limit of 64KB                                                             |
| **Description** | Optionally add a description of the variable. This is only visible in the UI, and is not accessible within a workflow.       |
| **Secret**      | New variables default to **secret**. If configured as a secret, the value is never exposed in the UI and cannot be modified. |

To edit an environment variable, click the **Edit** button from the three dots to the right of a specific variable.

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/915495c6-edit-env-var_bno34z.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=88bbcfe3ac7ee565f27197d5cc0c520f" width="1596" height="958" data-path="images/915495c6-edit-env-var_bno34z.png" />
</Frame>

* Updates to environment variables will be made available to your workflows as soon as the save operation is complete — typically a few seconds after you click **Save**.
* If you update the value of an environment variable in the UI, your workflow should automatically use that new value where it’s referenced.
* If you delete a variable in the UI, any deployed workflows that reference it will return `undefined`.

## Referencing environment variables in code

You can reference the value of any environment variable using the object [`process.env`](https://nodejs.org/dist/latest-v10.x/api/process.html#process_process_env). This object contains environment variables as key-value pairs.

For example, let’s say you have an environment variable named `API_KEY`. You can reference its value in Node.js using `process.env.API_KEY`:

```javascript  theme={null}
const url = `http://yourapi.com/endpoint/?api_key=${process.env.API_KEY}`;
```

Reference the same environment variable in Python:

```python  theme={null}
import os
print(os.environ["API_KEY"])
```

Variable names are case-sensitive. Use the key name you defined when referencing your variable in `process.env`.

Referencing an environment variable that doesn’t exist returns the value `undefined` in Node.js. For example, if you try to reference `process.env.API_KEY` without first defining the `API_KEY` environment variable in the UI, it will return the value `undefined`.

### Using autocomplete to reference env vars

When referencing env vars directly in code within your Pipedream workflow, you can also take advantage of autocomplete:

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f8998b18-autocomplete-env-vars_yoeaxy.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=2e993c751a70b2e4f21ebf9bffbb2f96" width="1414" height="632" data-path="images/f8998b18-autocomplete-env-vars_yoeaxy.png" />
</Frame>

<Warning>
  Logging the value of any environment variables — for example, using `console.log` — will include that value in the logs associated with the cell. Please keep this in mind and take care not to print the values of sensitive secrets.
</Warning>

<Note>
  `process.env` will always return `undefined` when used outside of the `defineComponent` export.
</Note>

## Referencing environment variables in actions

[Actions](/components/contributing/#actions) are pre-built code steps that let you provide input in a form, selecting the correct params to send to the action.

You can reference the value of environment variables using `{{process.env.YOUR_ENV_VAR}}`. You’ll see a list of your environment variables in the object explorer when selecting a variable to pass to a step.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/14bf2f5d-env-vars-object-explorer-v2_x9afzl.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=db4c137ab2c510f6ee09dd82d88e6800" width="890" height="524" data-path="images/14bf2f5d-env-vars-object-explorer-v2_x9afzl.png" />
</Frame>

<Note>
  [Private components](/components/contributing/#using-components) (actions or triggers) do not have direct access to workspace or project variables as public components or code steps. Add a prop specifically for the variable you need. For sensitive data like API keys, [configure the prop as a secret](/components/contributing/api/#props). In your prop configuration, set the value to `{{process.env.YOUR_ENV_VAR}}` to securely reference the environment variable.
</Note>

## FAQ

### What if I define the same variable key in my workspace env vars and project env vars?

The project-scoped variable will take priority if the same variable key exists at both the workspace and project level. If a workflow *outside* of the relevant project references that variable, it’ll use the value of the environment variable defined for the workspace.

### What happens if I share a workflow that references an environment variable?

If you [share a workflow](/workflows/building-workflows/sharing/) that references an environment variable, **only the reference is included, and not the actual value**.

## Limits

* Currently, environment variables are only exposed in Pipedream workflows, [not event sources](https://github.com/PipedreamHQ/pipedream/issues/583).
* The value of any environment variable may be no longer than `64KB`.
* The names of environment variables must start with a letter or underscore.
* Pipedream reserves environment variables that start with `PIPEDREAM_` for internal use. You cannot create an environment variable that begins with that prefix.

Built with [Mintlify](https://mintlify.com).
