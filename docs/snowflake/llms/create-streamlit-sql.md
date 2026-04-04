# Source: https://docs.snowflake.com/en/developer-guide/streamlit/getting-started/create-streamlit-sql.md

# Create and deploy Streamlit apps using SQL

This topic describes how to deploy a Streamlit app in Snowflake by using SQL
commands. Starting from a local development environment, you can copy your
Streamlit app files to a named stage in Snowflake and create a Streamlit object
from those files.

## Create a Streamlit app by using SQL

Before creating a Streamlit app by using SQL, ensure that you meet the required [prerequisites](overview.md).

To create a Streamlit app in Snowflake by using SQL commands, perform each of the following tasks:

* Optional: Create the Streamlit files on your local file system
* Upload your Streamlit files to a named stage
* Create a STREAMLIT object
* View a Streamlit app

### Optional: Create the Streamlit files on your local file system

This section describes how to create a local set of app source files and stage them in Snowflake. In the next section, if you don’t have
staged source files when you create your STREAMLIT object, a default set of source files is copied into your STREAMLIT object instead.

1. On your local file system, [create your main Streamlit app](https://docs.streamlit.io/library/get-started/create-an-app).
2. Optional: To configure your deployment environment and specify dependencies, create an `environment.yml` file.

   If you don’t include this file, your app will run on the latest supported versions of Python and Streamlit in Streamlit in Snowflake. For
   information about app dependencies, see Manage packages by using the environment.yml file.

After you create the Streamlit app, your directory structure should look similar to this:

```none
project_directory/
├── .streamlit/
│   └── config.toml
├── environment.yml
└── streamlit_app.py
```

> **Note:**
>
> Streamlit in Snowflake supports multipage Streamlit apps. This example only shows a single-page app, but you can add a `pages/` directory or use
> `st.navigation` to create a multipage app. To learn about multipage apps, see the
> [Overview of multipage apps](https://docs.streamlit.io/develop/concepts/multipage-apps/overview) in the Streamlit open-source
> documentation.

### Upload your Streamlit files to a named stage

To create a Streamlit app in Streamlit in Snowflake, you must upload your application files to a named stage.

* To upload application files, do one of the following:

  * Upload the application files by using Snowsight, as described in
    [Staging files using Snowsight](../../../user-guide/data-load-local-file-system-stage-ui.md).
  * Upload the application files by using SnowSQL, as shown in the following example:

    ```sqlexample
    PUT file:///<path_to_your_project_directory>/streamlit/streamlit_app.py @streamlit_db.streamlit_schema.streamlit_stage overwrite=true auto_compress=false;
    PUT file:///<path_to_your_project_directory>/streamlit/environment.yml @streamlit_db.streamlit_schema.streamlit_stage overwrite=true auto_compress=false;
    PUT file:///<path_to_your_project_directory>/streamlit/.streamlit/config.toml @streamlit_db.streamlit_schema.streamlit_stage/.streamlit/ overwrite=true auto_compress=false;
    ```

### Create a STREAMLIT object

A STREAMLIT object is a database object in Snowflake that encapsulates the files required by your Streamlit app.

1. To create a STREAMLIT object, run the [CREATE STREAMLIT](../../../sql-reference/sql/create-streamlit.md) command, as shown in the following example:

   ```sqlexample
   CREATE STREAMLIT hello_streamlit
   FROM '@streamlit_db.streamlit_schema.streamlit_stage'
   MAIN_FILE = 'streamlit_app.py'
   QUERY_WAREHOUSE = my_warehouse;
   ```

   This command creates a STREAMLIT object named `hello_streamlit` based on the path and file specified
   in FROM and MAIN_FILE.

   > **Note:**
   >
   > Although the QUERY_WAREHOUSE clause is optional, you must specify a query warehouse to be able to run the Streamlit app in Snowflake.
2. Optional: To verify that the Streamlit object was created, run the [SHOW STREAMLITS](../../../sql-reference/sql/show-streamlits.md) command:

   ```sqlexample
   SHOW STREAMLITS;
   ```

3. To complete initializing the app, the owner role must either view the app in Snowsight, or run the following command:

   ```sqlexample
   ALTER STREAMLIT hello_streamlit ADD LIVE VERSION FROM LAST;
   ```

## Manage packages by using the `environment.yml` file

To install additional Python packages in your Streamlit app:

1. Create an `environment.yml` file on your local file system.
2. To upload the file to the stage location specified by
   the `ROOT_LOCATION` parameter of the STREAMLIT object, run the [PUT](../../../sql-reference/sql/put.md) command.

   Packages listed in the `environment.yml` are installed from the
   [Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/).

The following sample `environment.yml` shows how to install `scikit-learn` within the Streamlit environment:

```yaml
name: sf_env
channels:
- snowflake
dependencies:
- scikit-learn
```

The `name` and `channels` properties are required. Also, the `- snowflake` key is required under the
`channels` property.

> **Note:**
>
> You can only install packages listed in the
> [Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/).
> Streamlit in Snowflake does not support external Anaconda channels.

### Pin the Streamlit version in the `environment.yml` file

* To pin the Streamlit version in the `environment.yml` file, include a `streamlit` dependency as shown in the following example:

  > ```yaml
  > name: sf_env
  > channels:
  > - snowflake
  > dependencies:
  > - scikit-learn
  > - streamlit=1.31.1
  > ```

## View a Streamlit app

* To view information about the STREAMLIT object, run the [DESCRIBE STREAMLIT](../../../sql-reference/sql/desc-streamlit.md) command, as shown in the following example:

  > ```sqlexample
  > DESC STREAMLIT hello_streamlit;
  > ```
>
* To view your Streamlit app in Snowsight, see [View a Streamlit app](create-streamlit-ui.md).

## Manage STREAMLIT objects

After creating a STREAMLIT object, use the [ALTER STREAMLIT](../../../sql-reference/sql/alter-streamlit.md) command to modify
different properties as described in the following sections.

### Rename a STREAMLIT object

* To rename a STREAMLIT object, use the RENAME TO clause of the [ALTER STREAMLIT](../../../sql-reference/sql/alter-streamlit.md) command, as shown in the following example:

  > ```sqlexample
  > ALTER STREAMLIT hello_streamlit RENAME TO hello_snowflake;
  > ```

### Change the stage or main file in a STREAMLIT object

* To change the path to the stage for a STREAMLIT object, use the [ALTER STREAMLIT](../../../sql-reference/sql/alter-streamlit.md) command to set the ROOT_LOCATION property of the object, as shown in the following example:

  > ```sqlexample
  > ALTER STREAMLIT hello_streamlit SET ROOT_LOCATION = '@snowflake_db.snowflake_schema.snowflake_stage'
  > ```
>
* To change the main Streamlit file in a STREAMLIT object, use the [ALTER STREAMLIT](../../../sql-reference/sql/alter-streamlit.md) command to set the MAIN_FILE property of the object, as shown in the following example:

  > ```sqlexample
  > ALTER STREAMLIT hello_streamlit SET MAIN_FILE = 'snowflake_main.py'
  > ```

### Change the query warehouse assigned to a STREAMLIT object

* To add a query warehouse or change the current query warehouse for a STREAMLIT object, use the [ALTER STREAMLIT](../../../sql-reference/sql/alter-streamlit.md) command to set the QUERY_WAREHOUSE property of the object, as shown in the following example:

  > ```sqlexample
  > ALTER STREAMLIT hello_streamlit SET QUERY_WAREHOUSE = my_new_warehouse;
  > ```

### List available STREAMLIT objects

* To list the Streamlit apps that are available to your current role, run the [SHOW STREAMLITS](../../../sql-reference/sql/show-streamlits.md) command, as shown in the following example:

  > ```sqlexample
  > SHOW STREAMLITS;
  > ```

### Delete a STREAMLIT object

* To delete a STREAMLIT object, run the [DROP STREAMLIT](../../../sql-reference/sql/drop-streamlit.md) command, as shown in the following example:

  > ```sqlexample
  > DROP STREAMLIT hello_streamlit;
  > ```
