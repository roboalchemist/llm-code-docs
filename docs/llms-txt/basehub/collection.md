# Collection

> A powerful list of blocks that can be fully customizable.

## Features

*   ✅ Ideal for repeatable content, such as a list of “Posts“, “Authors“
    
*   ✅ It can be searched through (using [BaseHub Search](https://docs.basehub.com/extras/search))
    
*   ✅ Updates can be tracked by [Workflow](https://docs.basehub.com/blocks/primitives/workflow) blocks.
    

## Constraints

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Contraint

Description

Template

The component that will give structure to the collection

Max rows

A maximum amount of rows required for commit validation to pass

Min rows

A minimum amount of rows required for commit validation to pass

As its name implies, you can make a Collection out of anything in BaseHub. Each new collection starts with an empty "Template" Component, which can be customized or replaced with an existing Component from your schema to serve as its template. When a new row is added to the collection, an empty instance of this template component is automatically appended to the collection’s children list.

Also, you can customize the visibility of collection columns according to the specific needs of different collection types. For instance, if you require a simple image carousel without titles, you have the option to hide the title column, resulting in a cleaner and more streamlined user interface.

## Advanced: recursive collections

If you have a structure in mind in which you have recursion, that is, a block that has nested blocks, that can have more nested blocks (infinitely), you can achieve this via collections.

Let’s take this documentation as an example. As you can see in the sidebar, some articles have nested articles within. This is fully defined by the content editor, as they’re free to nest and nest virtually infinitely. The key here is to have a component that has a child collection that targets the parent component itself ([src](https://basehub.com/basehub/docs/explore/main/GOSCkL1oxXpFlktOiuZY_)).

Something like this.