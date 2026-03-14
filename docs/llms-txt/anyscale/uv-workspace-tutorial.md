# Source: https://docs.anyscale.com/dependency-management/uv-workspace-tutorial.md

# Tutorial: Use uv to iterate in an Anyscale workspace

[View Markdown](/dependency-management/uv-workspace-tutorial.md)

# Tutorial: Use uv to iterate in an Anyscale workspace

This page provides an overview of using uv in an Anyscale workspace for iteratively developing Ray workloads, iteratively developing linked code dependencies, and managing your project environment.

warning

Support for uv on Anyscale is in beta. If you run into any issues, contact [Anyscale support](mailto:support@anyscale.com).

See [Use uv to manage Python dependencies](/dependency-management/uv.md).

## Step 0: Build an image with uv[​](#step0 "Direct link to Step 0: Build an image with uv")

Anyscale includes uv in all base images that use Ray 2.47.1 or later.

If you need to use an earlier version of Ray, use the following Dockerfile definition to create a custom image in the console. See [Build a custom image on Anyscale](/container-image/build-image.md).

```
# Start with an Anyscale base image.
FROM anyscale/ray:2.47.1-slim-py312-cu128

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set the uv runtime hook so "uv run" propagates 
# uv environments from Ray drivers to Ray workers.
RUN echo "export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook" >> /home/ray/.bashrc
```

## Step 1: Launch a workspace image that supports uv[​](#step1 "Direct link to Step 1: Launch a workspace image that supports uv")

If you built your own image, use it to configure your workspace. See [Use a container image in a workspace](/container-image.md#use-image).

All Anyscale base images that use Ray 2.47.1 or later have uv installed and the entrypoint hook defined by default.

## Step 2: Initialize your project[​](#step2 "Direct link to Step 2: Initialize your project")

Run the following command in a terminal in your Anyscale workspace to initialize your project:

```
uv init
```

This creates the following files in your workspace directory:

* `.gitignore`
* `.python-version`
* `main.py`
* `pyproject.toml`
* `README.md`

Open the `pyproject.toml` file to see the state of your project. Note that the `dependencies` list is empty.

## Step 3: Add Ray to your project[​](#step3 "Direct link to Step 3: Add Ray to your project")

Run the following command in the web terminal to add Ray to your project:

```
uv add ray==2.47.1 # Use the Ray version of your image here
```

uv adds the specified version of Ray to the `dependencies` list in your `pyproject.toml` file.

uv also creates a `uv.lock` file that lists all the additional packages installed to support the version of Ray.

## Step 4: Clone and add an editable dependency[​](#step-4-clone-and-add-an-editable-dependency "Direct link to Step 4: Clone and add an editable dependency")

uv supports adding editable dependencies and automatically symlinks local modules to official package names.

note

This step demonstrates a pattern for modifying Python dependencies alongside your Ray code.

This works as long as you include the local module in the working directory broadcast to your cluster. Anyscale workspaces do this automatically. See [Local files, code, and directories in workspaces](/development/workspace-defaults.md#files).

Run the following command in the web terminal to clone a public GitHub repo and add it as an editable package to your uv project:

```
git clone https://github.com/carpedm20/emoji/ my_emoji
uv add --editable ./my_emoji
```

The code example uses `my_emoji` as the directory name for the clone target to avoid a conflict with the package name. uv extracts the module name from the repository and accurately links the official module name to your directory. Your `pyproject.toml` file now includes `emoji` in the dependencies list and the following section to link this package to your editable local module:

```
[tool.uv.sources]
emoji = { path = "my_emoji", editable = true }
```

## Step 5: Write a Ray application[​](#step-5-write-a-ray-application "Direct link to Step 5: Write a Ray application")

Write a simple Ray application that uses the code you cloned into the `my_emoji` directory.

Replace the contents of the `main.py` file with the following code:

```
import ray

@ray.remote
def main():
    import emoji
    return emoji.emojize("Hello world :thumbs_up:")


if __name__ == "__main__":
    print(ray.get(main.remote()))
```

## Step 6: Run your Ray application with uv[​](#step-6-run-your-ray-application-with-uv "Direct link to Step 6: Run your Ray application with uv")

To see the output of your Ray application, run the following command in the web terminal:

```
uv run main.py
```

The terminal displays a series of messages reflecting the state of connecting to your Ray cluster, adding nodes, and managing the environment and dependencies. After a few seconds, the following output of your Python script should display:

```
Hello world 👍
```

## Step 7: Edit code in your dependency[​](#step-7-edit-code-in-your-dependency "Direct link to Step 7: Edit code in your dependency")

Make an arbitrary edit to the editable dependency to confirm that uv is tracking changes.

Start by locating following line of code, which is the `return` statement for the `emojize` method:

```
    return pattern.sub(replace, string)
```

Above the return statement, add a new line with a print statement, as in the following example:

```
    print("Hello, editable dependency!")
    return pattern.sub(replace, string)
```

Save your file.

## Step 8: Re-run your Ray application to see changes[​](#step-8-re-run-your-ray-application-to-see-changes "Direct link to Step 8: Re-run your Ray application to see changes")

To see the updated output for your application, run the following command in the web terminal:

```
uv run main.py
```

In addition to the `Hello world 👍` line, you should see a print statement such as the following:

```
(main pid=2288, ip=10.0.234.70) Hello, editable dependency!
```
