# Source: https://docs.infrahub.app/emma/getting-started/first-steps.md

# First Steps

Welcome to Emma! This guide will walk you through your first experience using Emma to interact with Infrahub.

## Opening Emma[​](#opening-emma "Direct link to Opening Emma")

1. **Navigate to Emma** at `http://localhost:8501` (or your configured port)
2. **Verify connection** - Emma should show a connection status to your Infrahub instance
3. **Select a branch** - Choose which Infrahub branch to work with (usually `main`)

![Emma Homepage](/assets/images/home_page-688ffc9365ffba7db2bec7b3ee5c6c4f.png)

## Understanding Emma's interface[​](#understanding-emmas-interface "Direct link to Understanding Emma's interface")

Emma is organized into several key areas accessible from the sidebar:

### Core features[​](#core-features "Direct link to Core features")

* **🏗️ Schema Builder** - AI-powered schema creation and editing
* **📁 Schema Library** - Browse and use pre-built schema templates
* **🔄 Schema Loader** - Load schemas into your Infrahub instance
* **👁️ Schema Visualizer** - Visual representation of your schemas
* **📥 Data Importer** - Import CSV data into Infrahub
* **📤 Data Exporter** - Export Infrahub data to CSV

### Experimental features[​](#experimental-features "Direct link to Experimental features")

* **🔍 Query Builder** - Build GraphQL queries (feature flag required)
* **📋 Template Builder** - Create templates (feature flag required)

## Your first task: explore the schema library[​](#your-first-task-explore-the-schema-library "Direct link to Your first task: explore the schema library")

Let's start by exploring Emma's schema library:

1. **Click "Schema Library"** in the sidebar
2. **Browse available schemas** - You'll see categories like Base, Extensions, and Experimental
3. **Select a schema** to view its details, such as the "Device" schema from Base/DCIM
4. **Review the schema structure** - Notice how it defines attributes, relationships, and inheritance

This gives you an understanding of how Infrahub schemas are structured.

## Load your first schema[​](#load-your-first-schema "Direct link to Load your first schema")

Next, let's load a schema into Infrahub:

1. **Navigate to "Schema Loader"**
2. **Select schemas** from the library (start with Base schemas like Organization and Location)
3. **Preview the schema** to understand what will be loaded
4. **Click "Load Schema"** to add it to your Infrahub instance

tip

Start with foundational schemas like Organization and Location before adding more complex schemas that depend on them.

## Visualize your schema[​](#visualize-your-schema "Direct link to Visualize your schema")

After loading schemas:

1. **Go to "Schema Visualizer"**
2. **View the graphical representation** of your schema relationships
3. **Explore connections** between different schema objects
4. **Use filters** to focus on specific schema types or relationships

## Import sample data[​](#import-sample-data "Direct link to Import sample data")

To see Emma in action with real data:

1. **Prepare a CSV file** with data matching your schema structure
2. **Navigate to "Data Importer"**
3. **Upload your CSV** and map columns to schema attributes
4. **Preview the import** to verify mappings are correct
5. **Execute the import** to add data to Infrahub

## Key concepts to understand[​](#key-concepts-to-understand "Direct link to Key concepts to understand")

### Schemas vs data[​](#schemas-vs-data "Direct link to Schemas vs data")

* **Schemas** define the structure and relationships of your infrastructure models
* **Data** is the actual instances that follow those schemas (specific devices, locations, etc.)

### Branches[​](#branches "Direct link to Branches")

* Emma works with Infrahub branches, similar to Git branches
* Changes can be made in development branches before merging to main
* Always be aware of which branch you're working in

### AI integration[​](#ai-integration "Direct link to AI integration")

* Emma's Schema Builder uses AI to help create schemas from natural language
* The AI understands infrastructure concepts and can suggest appropriate attributes and relationships
* Review AI-generated schemas carefully before using them in production

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you've completed your first steps:

1. **Explore Features** - Learn about each feature in detail in the [Features](/emma/features/schema-builder.md) section
2. **Follow Guides** - Try the step-by-step [guides](/emma/guides/building-your-first-schema.md) for common tasks
3. **Build Your Own** - Start creating schemas and importing data for your infrastructure

## Getting help[​](#getting-help "Direct link to Getting help")

If you encounter issues:

* Check the [Troubleshooting Guide](/emma/reference/troubleshooting.md)
* Review feature-specific documentation in the Features section
* Remember that Emma is experimental - some features may not work as expected

Emma is designed to make working with Infrahub more accessible and efficient. Take your time to explore each feature and don't hesitate to experiment!
