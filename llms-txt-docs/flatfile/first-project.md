# Source: https://flatfile.com/docs/getting-started/quickstart/first-project.md

# Creating Your First Project

> Running through the import flow with your Flatfile App

<Note>
  If you haven't created an app yet, start with the [Building Your First App
  with AutoBuild guide](/getting-started/quickstart/autobuild).
</Note>

## Understanding Projects

With your app created, it's time to create your first data import project!

A project is an instance of your app - think of your app as a template for onboarding customers,
and you'll create a project for each customer you onboard.
Each project gives you an isolated workspace with its own database, permissions, and workflow.

## Creating a New Project

To create a project, click the create button in the upper right corner of the
app page in your dashboard. The text in this button will depend on how you've named
your app's entity.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/getting-started/quickstart/assets/create_project.png" width="1259" />
</Frame>

The AutoBuild agent will create a new space based on your app's template.

You'll be taken to your new space, ready to receive data.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/getting-started/quickstart/assets/new_space.png" width="1258" />
</Frame>

If you'd like, you can manually import data using Flatfile's intuitive spreadsheet interface.

## Uploading and Mapping Data

Most users will start by uploading a data file.

You can drag and drop a file from your computer directly onto the sheet interface. The file will
automatically be extracted and you'll be taken to the mapping interface.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/getting-started/quickstart/assets/mapping.png" width="539" />
</Frame>

Here you can map columns from your uploaded file to fields in your source sheet. With your
mappings in place, click "Continue."

The data from your file will be mapped into your sheet.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/getting-started/quickstart/assets/mapped_sheet.png" width="1053" />
</Frame>

## Learn More

Now that you've created your first project, explore these helpful resources:

* [Core Concepts](/core-concepts/overview) - Understand Flatfile's fundamental building blocks
* [Handling Data](/guides/using-record-hooks) - Advanced data transformation and validation techniques
* [Using Actions](/guides/using-actions) - Create custom workflows and automations
* [API Reference](/api-reference) - Complete technical documentation

## Working with Your Data

From here, any transformations and validations you've defined will run automatically. You can resolve
any data issues in your sheet using AI transforms, find and replace, custom
actions, or by simply editing the data manually. You can collaborate with others on
data issues using comments and data clips.

## Exporting Your Data

When you're ready to move your perfected data out of Flatfile, you've got options!

You can download your data directly from the sheets interface. You can retrieve the sheet data
via API. Or, you can create a custom action to ship the data directly into your system.
