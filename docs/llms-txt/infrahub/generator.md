# Source: https://docs.infrahub.app/topics/generator.md

# Source: https://docs.infrahub.app/guides/generator.md

# How to create a Generator in Infrahub

Generators in Infrahub allow you to automatically create or modify data based on existing information in your database. They are defined in [external repositories](/topics/repository.md) and can be developed and tested locally using [infrahubctl generator](/infrahubctl/infrahubctl-generator.md).

In this guide, you'll learn how to develop a Generator and integrate it into Infrahub.

For conceptual information about Generators and their architecture, see [Generators](/topics/generator.md).

## What you'll build[​](#what-youll-build "Direct link to What you'll build")

You'll build a basic Generator that:

1. Reads information about Widget objects from the database
2. Creates a number of Resource objects based on each Widget's count property
3. Automatically runs when changes to Widget objects are proposed

## Steps overview[​](#steps-overview "Direct link to Steps overview")

1. Prepare the data model by creating a schema and objects
2. Create a GraphQL query to fetch data from Infrahub
3. Implement a Python Generator that creates the data
4. Tie everything together in an `.infrahub.yml` file
5. Test the Generator locally with infrahubctl
6. Deploy the Generator to Infrahub
7. Validate that the Generator works in Infrahub's CI pipeline

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, you'll need:

* Basic knowledge of Infrahub, Python, GraphQL, YAML, and Git
* Familiarity with Generators and how they work in Infrahub (see [Generators topic](/topics/generator.md))
* An Infrahub instance running locally or remotely
* A Git repository connected to Infrahub (see [Adding an External Repository guide](/guides/repository.md))
* [infrahubctl](/infrahubctl/infrahubctl.md) installed and configured locally
* The repository cloned locally where you'll develop the Generator

## Step 1: Setting up the data model[​](#step-1-setting-up-the-data-model "Direct link to Step 1: Setting up the data model")

In this step, you'll create the data structures needed for your Generator, including a schema, group, and sample objects that the Generator will process.

### Create a new branch[​](#create-a-new-branch "Direct link to Create a new branch")

Version Control & Branching

We recommend creating a new branch in your Git repository for your Generator development to avoid affecting the main branch. In this guide, we'll use a branch named `create-widget-generator`.

```
git checkout -b create-widget-generator
```

### Create group[​](#create-group "Direct link to Create group")

Object file or UI

If you prefer a "as code" approach, use the object file method. Otherwise, you can create the group directly in the Infrahub UI.

* Using Object File
* Using the UI

1. Create a file named `groups.yml` in the `objects` directory of your repository:

objects/groups.yml

```
---
apiVersion: infrahub.app/v1
kind: Object
spec:
  kind: CoreStandardGroup
  data:
    - name: "widgets"
```

2. Update the `.infrahub.yml` file to include the new object file:

.infrahub.yml

```
---
objects:
  - file_path: objects/groups.yml
```

3. Commit the changes to your repository:

```
git add objects/groups.yml .infrahub.yml
git commit -m "Add widgets group"
git push
```

1. Open the **Infrahub UI** in your browser
2. Select the branch `create-widget-generator`
3. Navigate to the **Groups** view (Object Management > Groups)
4. Create a **Standard group** named `widgets`

success

To verify the group was created successfully, navigate to the Groups view in the Infrahub UI and check that the `widgets` group appears in the list.

### Create and load schema[​](#create-and-load-schema "Direct link to Create and load schema")

Schema Creation

This step is only necessary if you don't already have the schemas affected by the Generator in your instance.

1. Create a `widgets.yml` file in the `schemas` directory of your repository:

schemas/widgets.yml

```
# yaml-language-server: $schema=https://schema.infrahub.app/infrahub/schema/latest.json
---
version: '1.0'

nodes:
  - name: Widget
    namespace: Test
    label: Widget
    human_friendly_id:
      - name__value
    display_label: "{{ name__value }}"
    attributes:
      - name: name
        kind: Text
        unique: true
      - name: count
        kind: Number

  - name: Resource
    namespace: Test
    label: Resource
    human_friendly_id:
      - name__value
    display_label: "{{ name__value }}"
    attributes:
      - name: name
        kind: Text
        unique: true
```

Schema Loading

Choose the method you already use to manage schema changes in your Infrahub deployment.

* Using Git Integration
* Using infrahubctl

2. Update the `.infrahub.yml` file to include the new schema file:

.infrahub.yml

```
---
schemas:
  - schemas/widgets.yml
```

3. Commit and push the changes to your repository

2) Load the following schema using the [infrahubctl schema](/infrahubctl/infrahubctl-schema.md) command.

```
infrahubctl schema load schemas/widgets.yml --branch=create-widget-generator
```

```
schema 'widgets.yml' loaded successfully
1 schema processed in 8.453 seconds.
```

success

You should see new entries for `Widget` and `Resource` in the left-hand side menu of the Infrahub UI.

### Create widget objects[​](#create-widget-objects "Direct link to Create widget objects")

Now that you have the schema loaded, you need to create objects that will be used by the Generator:

Object Creation

This step is only necessary if you don't already have the objects affected by the Generator in your instance.

Object Creation Method

You can also use an object file to create the widgets, though it's less relevant here than for the group creation.

1. Open the **Infrahub UI** in your browser

2. Select the branch `create-widget-generator`

3. Navigate to the **Widget** view

4. Create a new widget:

   <!-- -->

   * Name: `widget1`
   * Count: `1`
   * Member of groups: `widgets`

5. Create a second widget:

   <!-- -->

   * Name: `widget2`
   * Count: `2`
   * Member of groups: `widgets`

## Step 2: Create the GraphQL query[​](#step-2-create-the-graphql-query "Direct link to Step 2: Create the GraphQL query")

Next, create a GraphQL query that fetches the data your Generator needs to process.

### Create a query file[​](#create-a-query-file "Direct link to Create a query file")

Create a `widget_query.gql` file in the `queries` directory of your repository:

queries/widget\_query.gql

```
query Widgets($name: String!) {
  TestWidget(name__value: $name) {
    edges {
      node {
        __typename
        id
        name {
          value
        }
        count {
          value
        }
      }
    }
  }
}
```

### Test the query[​](#test-the-query "Direct link to Test the query")

To test the query you can use **Infrahub's GraphQL Sandbox**.

GraphQL Sandbox

Access the sandbox by clicking your user icon in the bottom left corner and selecting **GraphQL Sandbox**. This tool allows you to run GraphQL queries and provides an interactive way to explore the schema.

1. Copy the above GraphQL query in the main section

2. In the **variables** section, add:

```
{
  "name": "widget1"
}
```

3. Click the **Execute** button, this should return a response like:

```
{
  "data": {
    "TestWidget": {
      "edges": [
        {
          "node": {
            "__typename": "TestWidget",
            "id": "185526eb-2114-ce20-390a-c51aac78460a",
            "name": {
              "value": "widget1"
            },
            "count": {
              "value": 1
            }
          }
        }
      ]
    }
  }
}
```

success

You now have a working GraphQL query that retrieves the necessary data from Infrahub. You might want to keep the result of the query for later reference, as it will be useful when implementing the Generator.

## Step 3: Implement the Generator[​](#step-3-implement-the-generator "Direct link to Step 3: Implement the Generator")

Now create a Python class that implements your Generator logic. The Generator creates `TestResource` objects equal to the widget's count value.

The class must:

* Inherit from `InfrahubGenerator`
* Implement an async `generate()` method that processes data from your GraphQL query

info

If you aren't using `convert_query_response`, you can access the widget data directly from the `data` parameter passed to the `generate()` method. If you're working with `protocols`, you can create `TestResource` objects using strict typing.

1. Create a file named `widget_generator.py` in your `generators` directory:

generators/widget\_generator.py

```
from infrahub_sdk.generator import InfrahubGenerator

class WidgetGenerator(InfrahubGenerator):
    async def generate(self, data: dict) -> None:
        # Access the widget as an SDK object
        widget = self.nodes[0]  # or self.store.get(data["TestWidget"]["edges"][0]["node"]["id"])
        widget_name: str = widget.name.value
        widget_count: int = widget.count.value

        # Create resources based on widget count
        for count in range(1, widget_count + 1):
            payload = {
              "name": f"{widget_name.lower()}-{count}",
            }
            obj = await self.client.create(kind="TestResource", data=payload)
            await obj.save(allow_upsert=True)
```

## Step 4: Tie everything together in the .infrahub.yml file[​](#step-4-tie-everything-together-in-the-infrahubyml-file "Direct link to Step 4: Tie everything together in the .infrahub.yml file")

Now that you have your GraphQL query and Python Generator, edit your [.infrahub.yml](/topics/infrahub-yml.md) file to tie everything together.

1. Add the following configuration to the file `.infrahub.yml`:

.infrahub.yml

```
---
generator_definitions:
  - name: widget_generator
    file_path: "generators/widget_generator.py"
    targets: widgets
    query: widget_query
    convert_query_response: true
    class_name: WidgetGenerator
    parameters:
      name: "name__value"

queries:
  - name: widget_query
    file_path: "queries/widget_query.gql"
```

For a complete explanation of the `.infrahub.yml` file format, see the [infrahub.yml topic](/topics/infrahub-yml.md).

2. Verify the configuration

Check that your `.infrahub.yml` file is correctly formatted by listing available Generators:

```
infrahubctl generator --list
```

success

If successful, you'll see output like:

```
Generators defined in repository: 1
widget_generator (generators/widget_generator.py::WidgetGenerator) Target: widgets
```

## Step 5: Test the Generator locally[​](#step-5-test-the-generator-locally "Direct link to Step 5: Test the Generator locally")

Before deploying your Generator to Infrahub, test it locally using the `infrahubctl` command-line tool.

### Run the Generator[​](#run-the-generator "Direct link to Run the Generator")

Run the Generator on both of your widget objects:

```
infrahubctl generator widget_generator --branch=create-widget-generator name=widget1
infrahubctl generator widget_generator --branch=create-widget-generator name=widget2
```

### Verify the results[​](#verify-the-results "Direct link to Verify the results")

1. Select the branch `create-widget-generator` from the branch selector

2. Navigate to **Resource** objects

3. You should see:

   <!-- -->

   * One resource object for `widget1` (named `widget1-1`)
   * Two resource objects for `widget2` (named `widget2-1` and `widget2-2`)

![Generated resource objects](/assets/images/generator_pc_3-cdfaa19101c8ed4238c45fec7213a7a4.png)

warning

You might want to cleanup this development data before merging your changes into the main branch.

success

Your Generator worked as expected, it's now time to deploy it to Infrahub.

## Step 6: Deploy to Infrahub[​](#step-6-deploy-to-infrahub "Direct link to Step 6: Deploy to Infrahub")

Now that you've tested your Generator, deploy it to Infrahub.

### Verify repository structure[​](#verify-repository-structure "Direct link to Verify repository structure")

Ensure your repository has the following structure:

Schemas & Objects

Depending on your organization, you might also have `schemas` and `objects` directories in your repository.

```
your-repository/
├── .infrahub.yml
├── generators/
│   └── widget_generator.py
└── queries/
    └── widget_query.gql
```

### Commit and push your code[​](#commit-and-push-your-code "Direct link to Commit and push your code")

Upload your Generator code to the repository:

```
git add .
git commit -m "Add widget generator"
git push
```

### Confirm the Generator is imported[​](#confirm-the-generator-is-imported "Direct link to Confirm the Generator is imported")

After pushing your changes, confirm that the Generator is imported correctly by checking the Infrahub UI.

1. Open the **Infrahub UI** in your browser
2. Select the `create-widget-generator` branch
3. Navigate to the **Generators Definition view** (Actions > Generator Definitions)
4. You should see your `widget_generator` listed there

If you don't see it verify the status of the repository in the **Repository view** and ensure the sync status is `synced`.

### Proposed changes and merge[​](#proposed-changes-and-merge "Direct link to Proposed changes and merge")

Now merge your development branch `create-widget-generator` into `main`.

Merging Options

We recommend using Infrahub's **Proposed Changes** feature to merge your changes. This allows you to review both data and code changes before merging.

1. Create a **Proposed Change**

   * Source branch: `create-widget-generator`
   * Destination branch: `main`
   * Name: `Add widget generator`

2. Navigate to the **Data** and **Files** tabs to review the changes

3. Back to the **Overview** tab, click the **Merge** button

success

Your Generator is now deployed to Infrahub in the `main` branch and ready to be used.

## Step 7: Run the Generator in Infrahub's CI pipeline[​](#step-7-run-the-generator-in-infrahubs-ci-pipeline "Direct link to Step 7: Run the Generator in Infrahub's CI pipeline")

Now let's verify that your Generator automatically runs when new widgets are created:

1. Create a new branch named `add-widget-3`

2. Navigate to the **Widget** objects in the Infrahub UI

3. Create a new widget:

   <!-- -->

   * Name: `widget3`
   * Count: `3`
   * Member of groups: `widgets`

4. Create a **Proposed Change**

   * Source branch: `add-widget-3`
   * Destination branch: `main`
   * Name: `Add widget3`

### Check Generator results[​](#check-generator-results "Direct link to Check Generator results")

1. Navigate to the **Checks** tab of your proposed change
2. Wait for the **Generator** CI check to complete ![Generator CI Check](/assets/images/generator_pc_1-806e4bf23f6b989bd1dffb62ee863b2b.png)
3. Navigate to the **Data** tab
4. Click the **Refresh diff** button to see the resources created by your Generator ![Data Refresh showing generated resources](/assets/images/generator_pc_2-029c5257939535f8409cb76669efcc2b.png)

success

You should see three new resources (`widget3-1`, `widget3-2`, and `widget3-3`) automatically created by your Generator.

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've created a basic Generator, you can:

* Create Generators that handle a full object lifecycle, including creation, updates, and deletions
* Build idempotent Generators that can be run multiple times without creating duplicate data
* Add unit tests to your Generator to ensure it behaves as expected
* Harden your Generator by adding error handling and logging

Real-World Example

Want to see how Generators can be used in production? Read our blog post on [How to Turn Your Source of Truth into a Service Factory](https://www.opsmill.com/how-to-turn-your-source-of-truth-into-a-service-factory/).
