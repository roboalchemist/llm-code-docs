# Source: https://docs.wandb.ai/models/ref/python/functions/setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# setup()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/sdk/wandb_setup.py" />

### <kbd>function</kbd> `setup`

```python  theme={null}
setup(settings: 'Settings | None' = None) → _WandbSetup
```

Prepares W\&B for use in the current process and its children.

You can usually ignore this as it is implicitly called by `wandb.init()`.

When using wandb in multiple processes, calling `wandb.setup()` in the parent process before starting child processes may improve performance and resource utilization.

Note that `wandb.setup()` modifies `os.environ`, and it is important that child processes inherit the modified environment variables.

See also `wandb.teardown()`.

**Args:**

* `settings`:  Configuration settings to apply globally. These can be  overridden by subsequent `wandb.init()` calls.

**Example:**

```python  theme={null}
import multiprocessing

import wandb


def run_experiment(params):
   with wandb.init(config=params):
        # Run experiment
        pass


if __name__ == "__main__":
   # Start backend and set global config
   wandb.setup(settings={"project": "my_project"})

   # Define experiment parameters
   experiment_params = [
        {"learning_rate": 0.01, "epochs": 10},
        {"learning_rate": 0.001, "epochs": 20},
   ]

   # Start multiple processes, each running a separate experiment
   processes = []
   for params in experiment_params:
        p = multiprocessing.Process(target=run_experiment, args=(params,))
        p.start()
        processes.append(p)

   # Wait for all processes to complete
   for p in processes:
        p.join()

   # Optional: Explicitly shut down the backend
   wandb.teardown()
```
