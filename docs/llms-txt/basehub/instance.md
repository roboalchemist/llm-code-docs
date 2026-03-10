# Instance

> A modular block that reuses the structure from your Components.

## Features

*   ✅ Ideal for reusable types, such as a “CTA” or “Article”
    
*   ✅ It can have nested blocks—although it follows the structure of its target component
    
*   ✅ It can be hidden
    

Instances are created from components stored in your repository and can be used in all sorts of ways, fitting into many different scenarios. For example, a component and its instances can be listed in a Document block to structure sections of a landing page. Alternatively, you could create a component in a union block with multiple fields, and create various instances from it.

## What you can do in Instances

Instances have their own values, so you can update its title and fill every child input. That includes rows in a collection, references and any other input.

## What you cannot do in Instances

You cannot modify the schema in any way, you cannot modify constraints or collection columns, allowed types, children titles, etc.

## Special cases

### OG Image

The OG Image block can only be modified in the main component. That’s the case because every change in the OG Image block is a properties change. But that doesn’t mean that every instance will have the exact same OG image, since you can use variables for text and images, so they will automatically update those based on the current instance they’re set in. [Learn more about the OG Image](https://docs.basehub.com/blocks/primitives/og-image).