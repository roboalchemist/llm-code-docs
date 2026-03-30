# Reference

> Choose from a constrained list of component types.

## Features

*   ✅ Ideal for modular sections and programatic pages
    

*   ✅ Displays an combobox with options
    
*   ✅ Options are type safe in the SDK
    
*   ✅ Gives you the option choose between different component structures within a single block
    
*   ✅ It can have nested blocks
    

## Constraints

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Contraint

Description

Is required

Validates the input is filled.

Multiple

Allow a single or multiple selected options.

Can link existing

Allow to reference existing instances or components.

Can create new

Allow to create new instances of allowed components inside the reference block.

Reference types

List of allowed options to choose from.

## Use cases

Apart from the obvious single reference uses, the Reference type is a powerful block that enables you to create a space for a singular or multiple instances of the selected types. Think of it as an “OR” between the allowed types selected. For example, if you have a Reference with allowed types “Code Group” and “Code Snippet”, the union child can be a “Code Group” instance OR a “Code Snippet” instance.

This makes it ideal for a bunch of use cases, including:

1.  Creating a “Sections” union block for your modular, programmatic pages ([see example](https://basehub.com/basehub/marketing-website/explore/main/vtx_SP9e9HHLM-AE17BsA#94706f2563a70962531c4))
    
2.  Creating a conditional structure, such as “Section with Media“ in which the media part is a union of “either an image or a video”