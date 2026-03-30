# Source: https://docs.kedro.org/en/stable/tutorials/tutorial_template/index.md

# Set up the spaceflights project

This section shows how to create a new project with `kedro new` using the [Kedro spaceflights starter](https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas) and install project dependencies (with `pip install -r requirements.txt`).

## Create a new project

Navigate to the folder you want to store the project. Type the following to generate the project from the [Kedro spaceflights starter](https://github.com/kedro-org/kedro-starters/tree/main/spaceflights-pandas). The project will be populated with a complete set of working example code:

```
uvx kedro new --starter spaceflights-pandas --name spaceflights
```

Note

Using `uvx` lets you run Kedro without installing it into your system or virtual environment. It downloads and runs Kedro in a clean temporary environment each time. If you prefer a standard installation (for example pip + virtual environment), see the [installation guide](https://docs.kedro.org/en/stable/getting-started/install/#alternative-methods).

After Kedro has created the project, navigate to the [project root directory](https://docs.kedro.org/en/stable/tutorials/spaceflights_tutorial/#project-root-directory):

```
cd spaceflights
```

Next, to create a virtual environment and install the dependencies, run

```
uv sync
```

Then verify that your installation is correct:

```
uv run kedro info
```

See the documentation for more information and alternative methods to [set up Kedro](https://docs.kedro.org/en/stable/getting-started/install/index.md).

Tip

We recommend using the Kedro version tested with this tutorial (1.0.0). To check the version installed, type `kedro -V` in your terminal window.

## Optional: logging and configuration

You might want to [set up logging](https://docs.kedro.org/en/stable/develop/logging/index.md) at this stage of the workflow, but we do not use it in this tutorial.

You may also want to store credentials such as usernames and passwords if they are needed for specific data sources used by the project.

To do this, add them to `conf/local/credentials.yml` (some examples are included in that file for illustration).

### Configuration best practice to avoid leaking confidential data

- Do not commit data to version control.
- Do not commit notebook output cells (data can sneak into notebooks when you do not delete output cells).
- Do not commit credentials in `conf/`. Keep the sensitive information in the `conf/local/` folder.

You can find additional information in the [documentation on configuration](https://docs.kedro.org/en/stable/configure/configuration_basics/index.md).
