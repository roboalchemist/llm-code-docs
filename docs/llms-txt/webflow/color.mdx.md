# Source: https://developers.webflow.com/flowkit/variables/color.mdx

***

title: Color
slug: variables/color
description: Color variables and how they are used in the Flowkit Framework.
hidden: null
'og:title': Flowkit - Color
'og:description': Color variables and how they are used in the Flowkit Framework.
---------------------------------------------------------------------------------

The framework uses a system of structured color variables that power the entire site. These variables are applied consistently across text, backgrounds, borders, and component variations.

All colors are managed through variables and that are grouped by the following roles:

* [**Core Colors**](#core-colors)<br /> The foundational palette used across the system
* [**Tints**](#tints)<br /> Create depth and hierarchy without introducing additional colors
* [**Contextual Usage**](#contextual-usage)<br /> Semantic variables that reference core colors behind the scenes

***

## Core Colors

Core colors represent the main color tokens for UI elements like buttons, cards, and links. These include both accent and neutral palettes. These are the foundational variables used for background fills, button states, and links.

| Accent Colors                                                  | Neutral Colors                                            |
| -------------------------------------------------------------- | --------------------------------------------------------- |
| <span class="sg-selector sg-var">Accent Primary</span>         | <span class="sg-selector sg-var">Neutral Primary</span>   |
| <span class="sg-selector sg-var">Accent Secondary</span>       | <span class="sg-selector sg-var">Neutral Secondary</span> |
| <span class="sg-selector sg-var">Accent Tertiary</span>        | <span class="sg-selector sg-var">Neutral Inverse</span>   |
| <span class="sg-selector sg-var">Accent Primary Hover</span>   |                                                           |
| <span class="sg-selector sg-var">Accent Secondary Hover</span> |                                                           |
| <span class="sg-selector sg-var">Accent Tertiary Hover</span>  |                                                           |

***

## Tints

Each core color includes a tint scale ranging from `A10` (lightest) to `A90` (strongest). These are used for opacity layering, accessible text, or background overlays. Tints allow you to create depth and hierarchy without introducing additional colors.

| Group            | Tint Range |
| ---------------- | ---------- |
| Accent Primary   | A10 – A90  |
| Accent Secondary | A10 – A90  |
| Accent Tertiary  | A10 – A90  |
| Neutral Primary  | A10 – A90  |
| Neutral Inverse  | A10 – A90  |

Examples:

* <span class="sg-selector sg-var">Text Secondary</span> uses <span class="sg-selector sg-var">Neutral Inverse A60</span>
* <span class="sg-selector sg-var">Border Primary</span> uses <span class="sg-selector sg-var">Neutral Inverse A50</span>
* <span class="sg-selector sg-var">BG Overlay</span> uses <span class="sg-selector sg-var">Neutral Inverse A90</span>

***

## Contextual Usage

Many design variables reference core colors behind the scenes. These are more semantic and mapped to actual UI roles. Update any of the base colors, and these will automatically reflect those changes in the UI.

| Usage Context | Variable Example                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Background    | <span class="sg-selector sg-var">BG Primary</span>, <span class="sg-selector sg-var">BG Accent Secondary</span>, <span class="sg-selector sg-var">BG Inverse</span>             |
| Text          | <span class="sg-selector sg-var">Text Primary</span>, <span class="sg-selector sg-var">Text On Accent Primary</span>, <span class="sg-selector sg-var">Text On Overlay</span>   |
| Border        | <span class="sg-selector sg-var">Border Primary</span>, <span class="sg-selector sg-var">Border Accent</span>, <span class="sg-selector sg-var">Border Inverse Secondary</span> |
