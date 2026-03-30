# Source: https://developers.webflow.com/designer/reference/variable-collections-overview.mdx

***

title: Variable collections
slug: designer/reference/variable-collections-overview
description: Learn how to create and manage variable collections with the Designer API.
hidden: false
'og:title': 'Webflow Designer API: Variable collections'
'og:description': Learn how to create and manage variable collections with the Designer API.
--------------------------------------------------------------------------------------------

Variable collections provide an organizational structure for managing related variables. Collections allow you to group variables logically - for example, you might create separate collections for brand colors, typography, or spacing variables. Collections help maintain a clean and organized variable system, making it easier to manage design tokens at scale across your projects.

## Creating a collection

Create a collection using the [create variable collection](/designer/reference/create-variable-collection) endpoint.

{/* <!-- vale off --> */}

```typescript
// Create a collection
const collection = await webflow.createVariableCollection('Brand Styles')
```

{/* <!-- vale on --> */}

## Selecting a collection

Select a collection in multiple ways. Either, get all collections or get a specific collection by name or ID.

{/* <!-- vale off --> */}

```typescript
// Get all collections
const collections = await webflow.getAllVariableCollections()

// Get a collection by ID
const collection = await webflow.getVariableCollectionById('collection-4a393cee-14d6-d927-f2af-44169031a25')
```

{/* <!-- vale on --> */}

## Working with variables

Once a collection is selected, you can use the collection methods to [create, retrieve, and manage variables](/designer/reference/variables-overview).

{/* <!-- vale off --> */}

```typescript
// Get collection
const collection = await webflow.getDefaultVariableCollection()

// Create a variable
const variable = await collection?.createColorVariable('primary', 'red')

// Get all variables
const variables = await collection?.getAllVariables()
```

{/* <!-- vale on --> */}
