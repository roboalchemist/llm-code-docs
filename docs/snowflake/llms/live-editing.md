# Source: https://docs.snowflake.com/en/developer-guide/declarative-sharing/live-editing.md

# Editing Notebooks in Declarative Shared Native Applications

Declarative Native Apps can include [notebooks](../../user-guide/ui-snowsight/notebooks.md) to query, visualize, and explore the data. This topic describes how to use **Notebook Live Editing** to streamline the development and testing of notebooks within an application.

Using the **Notebook Live Editing** feature, you can speed up the development process by editing and testing notebooks directly within an application. This saves you from having to develop notebooks externally, or from having to rebuild the application package for every change.

**Notebook Live Editing** uses a **Development Mode** that lets you make changes to notebooks “live” inside an application instance. Your edits are saved to a dedicated live version of the application package, allowing for rapid, on-the-fly
testing and iteration.

## How It Works

The workflow uses a live version of your application package, which functions as a development sandbox. This tutorial describes how to set up
and use the Notebook Live Editing feature.

### Step 1: Set Up the Development Environment

To begin, you need a package that contains the following:

* A manifest file that defines the application and its components.
* A notebook that you can edit and test.

You then create an application instance from the live version of your package. The live version is created automatically when you create your application.

1. Build the package.

   ```sqlexample
   ALTER APPLICATION PACKAGE pkg_name BUILD;
   ```

2. Create an application instance from the live version. Notebooks in this new application will automatically be in **Development
   Mode**, allowing live editing. Prior to this step, notebooks in the application are in **Read-only mode**.

   ```sqlexample
   CREATE APPLICATION live_app_name
     FROM APPLICATION PACKAGE pkg_name
     USING VERSION LIVE;
   ```

### Step 2: Live Edit and Test Notebooks

With your `live_app_name` application running, in SnowSight, open your app from the list of apps in your account, and open one of its notebooks from its listing page. After creating the application from the application package in the previous step, the applications’ notebooks will be in **Developer mode**.You can now do the following:

* Edit notebook cells directly in the browser.
* Run and test your code immediately within the context of the application.

Any changes you make are instantly saved to the live version of the `pkg_name` application package. This allows you to iterate changes
to your application quickly, without needing to perform a full package build for each minor adjustment.

### Step 3: Finalize and Release Changes

Once you’re happy with the state of your notebooks, you can promote the live version to a stable release. This freezes the current state of
your notebooks and makes them part of a permanent application version. The app framework automatically creates a version number for your
release.

* Release the live version to finalize your work.

```sqlexample
ALTER APPLICATION PACKAGE pkg_name RELEASE LIVE VERSION;
```

This command creates a new, immutable version of your application package containing all the notebook changes you made. For more information
about the application package and the live version, see [Application Packages in Declarative Sharing in the Native Application Framework](package.md).
