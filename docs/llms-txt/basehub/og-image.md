# OG Image

> A lightweight OG Image editor used for social cards. Accepts variables and is fully customizable.

## Features

*   ✅ Uses [@vercel/og](https://www.npmjs.com/package/@vercel/og) under the hood
    
*   ✅ Renders a lightweight editor
    
*   ✅ Can use block variables (like the [preview button does](https://docs.basehub.com/nextjs-integration/environments-and-caching#preview-environment)) to build the design
    

## Component/Instance Workflow

When you design an OG Image Block within a Component, you’re defining sort of the “template” that will be used by all of the Instance Blocks targeting it. You won’t be able to edit the OG Image within an Instance. That’s why, you’ll probably want to leverage variablesx, such as the ones the [preview button has](https://docs.basehub.com/nextjs-integration/environments-and-caching#preview-environment).

## Constraints

It doesn’t have any.