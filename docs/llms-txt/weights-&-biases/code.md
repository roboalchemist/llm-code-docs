# Source: https://docs.wandb.ai/models/app/features/panels/code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save and diff code

> Enable code saving, compare code across W&B runs with the code comparer, and capture Jupyter session history.

By default, W\&B only saves the latest git commit hash. You can turn on more code features to compare the code between your experiments dynamically in the UI.

Starting with `wandb` version 0.8.28, W\&B can save the code from your main training file where you call `wandb.init()`.

## Save library code

When you enable code saving, W\&B saves the code from the file that called `wandb.init()`. To save additional library code, you have three options:

### Call `wandb.Run.log_code(".")` after calling `wandb.init()`

```python  theme={null}
import wandb

with wandb.init() as run:
  run.log_code(".")
```

### Pass a settings object to `wandb.init()` with `code_dir` set

```python  theme={null}
import wandb

wandb.init(settings=wandb.Settings(code_dir="."))
```

This captures all python source code files in the current directory and all subdirectories as an [artifact](/models/ref/python/experiments/artifact). For more control over the types and locations of source code files that are saved, see the [reference docs](/models/ref/python/experiments/run#log_code).

### Set code saving in the UI

In addition to setting code saving programmatically, you can also toggle this feature in your W\&B account Settings. Note that this will enable code saving for all teams associated with your account.

> By default, W\&B disables code saving for all teams.

1. Log in to your W\&B account.
2. Navigate to **Settings** > **Privacy**.
3. Under **Project and content security**, toggle **Disable default code saving** on.

## Code comparer

Compare code used in different W\&B runs:

1. Select the **Add panels** button in the top right corner of the page.
2. Expand **TEXT AND CODE** dropdown and select **Code**.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/code_comparer.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=fcd0416ae8bdeaadd69f541104fe6d6d" alt="Code comparer panel" width="887" height="337" data-path="images/app_ui/code_comparer.png" />
</Frame>

## Jupyter session history

W\&B saves the history of code executed in your Jupyter notebook session. When you call **wandb.init()** inside of Jupyter, W\&B adds a hook to automatically save a Jupyter notebook containing the history of code executed in your current session.

1. Navigate to your project workspaces that contains your code.
2. Select the **Artifacts** tab in the project sidebar.
3. Expand the **code** artifact.
4. Select the **Files** tab.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/jupyter_session_history.gif?s=49da7b37f1224d224a013d6236f8b2bc" alt="Jupyter session history" width="3868" height="2574" data-path="images/app_ui/jupyter_session_history.gif" />
</Frame>

This displays the cells that were run in your session along with any outputs created by calling iPython’s display method. This enables you to see exactly what code was run within Jupyter in a given run. When possible W\&B also saves the most recent version of the notebook which you would find in the code directory as well.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/jupyter_session_history_display.png?fit=max&auto=format&n=ZDqxXQYvQVF43fU1&q=85&s=08c634b5d45cdac9d16a3c803879c6eb" alt="Jupyter session output" width="3826" height="1840" data-path="images/app_ui/jupyter_session_history_display.png" />
</Frame>
