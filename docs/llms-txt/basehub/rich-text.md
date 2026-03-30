# Rich Text

> A powerful text input that not only supports markdown syntax but also it has the possibility to have many custom components made in BaseHub.

## Introduction

The Rich Text block is the most flexible primitive in BaseHub. Playing with its constraints, you can go from a simple text input with bold, italic and underline formatting to a complex text editor with many custom components present in the repository and integrated in your codebase. It supports Markdown, image copy and pasting, image and video captions, code snippets and more. This tool is particularly effective for those looking to compose articles, blog posts, or any extensive text work that benefits from added visual components and structured formatting.

## Features

*   ✅ Ideal for articles, blog posts or long texts
    
*   ✅ It can be search indexed
    
*   ✅ Supports AI Chat
    
*   🔄 It can be converted into a [Text block](https://docs.basehub.com/blocks/primitives/text), but be ware that it will remove all rich capabilities in the process.
    

## Constraints

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Contraint

Description

Is required

Validates the input is filled.

Formatting

This describes the formatting options available in the editor, such as bold, italic, or underline. If a particular format is turned off, it won't appear in the command menu, and using it will cause a validation error on commit if it's already present in the content.

Component types

Allows the inclusion of specific custom components from the repository into the text content, enabling enhanced customization and functionality in your content.