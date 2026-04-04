# Component

> The Component block functions as a modular structure within your repository, that can be reused across your schema.

## Features

*   ✅ Ideal for reusable types, such as a “CTA” or “Article”
    
*   ✅ It can have nested blocks
    
*   ✅ It can be converted into a [Document](https://docs.basehub.com/blocks/layout/document)
    
*   ✅ It can be hidden
    

Each Component outlines a schema, and the content for each instance is then defined within those parameters. The main difference here with other CMSs is that the Component is a source of content at the same time that defines the schema.

## Component creation

To create a Component, you can start from scratch or transform an existing Document into a Component. To do this, simply click the "Make Component" button found in the Document properties panel. This action changes the block type, enabling its reuse as an instance throughout your project.

## Detaching

If you need to transform a Component back into a Document, or if you wish to convert an instance into a standalone Component, you will need to detach the main Component first. By selecting the “Detach Component” button, you’ll convert that block back into a [Document](https://docs.basehub.com/blocks/layout/document). An Instance will be then converted into a Component with that same structure, thus preserving all of the existing instances as they are. No data will be lost during this transition; however, existing instances will now target this new “promoted” instance.

## Nesting components

Unlike other structures, Components cannot embed Documents within them. If your design calls for a more layered structure with nested layout blocks, you can achieve this by nesting multiple components or instances. To nest components, simply access the slash command within your main component; it will display the option to insert another component right inside it.

## Display Info

You can define some helpful display information for each Component, so that content editors can understand more about how to use it.

You’ll be able to edit Display Info in the Properties Panel (right hand side) of a Component.

This is how it shows in the slash command.