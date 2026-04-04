# Source: https://docs.snowflake.com/en/developer-guide/declarative-sharing/add-packages.md

# Add Anaconda packages to a notebook

The notebook environment includes a set of pre-installed Anaconda packages, such as Python and Streamlit.

If your notebook uses additional Anaconda packages, you must add those packages to your application package so that your notebook can access them.

You can add them while editing the notebook in development mode. You can also add the packages by providing an `environment.yml` file.

> **Note:**
>
> If an `environment.yml` file is present in the same directory as a notebook, it overwrites the list of dependent packages, and any packages added through the Snowsight UI are ignored.
>
> Using an `environment.yml` file is recommended for production applications as it allows you to manage dependencies in source control.
>
> Using the UI is convenient for interactive development and testing.

## Adding Anaconda packages while editing the notebook in development mode

You can add Anaconda packages to your notebook while editing it in development mode. We recommend using this method rather than adding packages to the `environment.yml` file, because the process is considerably simpler.

To add packages while editing the notebook:

1. Install your application package locally from the live version.
2. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
3. In the navigation menu, select Projects » Notebooks.
4. Open your notebook file.
5. Make sure the notebook is in development mode. For information about development mode, see [Editing Notebooks in Declarative Shared Native Applications](live-editing.md).
6. Select the Packages button in the top center of the notebook editor.
7. Search for the package you want to add, and select it.

The notebook environment now automatically loads the selected dependencies when the notebook is run.

## Adding Anaconda packages to the `environment.yml` file

You can define your Python dependencies by creating an `environment.yml` file, and uploading it to the same stage directory as your notebook (.ipynb) file.

For information about creating an `environment.yml` file that includes your new packages, see
[Manage packages by using the environment.yml file](../streamlit/getting-started/create-streamlit-sql.md)

> **Note:**
>
> You can only install packages listed in the
> [Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/).
> Streamlit in Snowflake does not support external Anaconda channels.

Use the PUT command to upload your `environment.yml` file from your local machine to the application package stage. The `environment.yml` file must be in the same directory on the stage as the notebook file it configures.

Replace the placeholders in the following command with your own values. If your notebook is at the root of the live version, do not include a directory path after `live/`.

```bash
PUT <file:///path/to/your/environment.yml> snow://package/<PACKAGE_NAME>/versions/live/<path/to/your/notebook> OVERWRITE=TRUE AUTO_COMPRESS=FALSE;
```
