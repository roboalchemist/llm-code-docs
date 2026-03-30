# Source: https://developers.webflow.com/flowkit/v1.0.0/components/forms.mdx

***

title: Forms
slug: components/forms
description: Forms consist of modular components with consistent styling patterns.
hidden: null
'og:title': Flowkit - Forms
'og:description': Forms consist of modular components with consistent styling patterns.
---------------------------------------------------------------------------------------

## Class Naming

Forms consist of modular components with consistent styling patterns. Each element (labels, fields, toggles, and messages) is styled using reusable classes and combo modifiers to adapt to different contexts (inverse, accents, etc.).

**Form Components**

| Element Class                                                                                       | Purpose                  |
| --------------------------------------------------------------------------------------------------- | ------------------------ |
| <span class="sg-selector sg-class">Input</span>                                                     | For basic text fields    |
| <span class="sg-selector sg-class">Input</span> <span class="sg-selector sg-class">Select</span>    | For select fields        |
| <span class="sg-selector sg-class">Input</span> <span class="sg-selector sg-class">Text Area</span> | For multiline input      |
| <span class="sg-selector sg-class">Checkbox</span>                                                  | Custom-styled checkbox   |
| <span class="sg-selector sg-class">Radio</span>                                                     | Custom-styled radio      |
| <span class="sg-selector sg-class">Button</span>                                                    | For submitting the form  |
| <span class="sg-selector sg-class">Form Success Message</span>                                      | Visible after submission |
| <span class="sg-selector sg-class">Form Error Message</span>                                        | Shows validation errors  |

## Elements

**Input elements**

* <span class="sg-selector sg-class">
    Input Label
  </span>
* <span class="sg-selector sg-class">Input Block</span> - wrapper of the label and input field

**Checkbox elements:**

* <span class="sg-selector sg-class">
    Checkbox Toggle
  </span>
* <span class="sg-selector sg-class">
    Checkbox Label
  </span>

**Radio elements:**

* <span class="sg-selector sg-class">
    Radio Toggle
  </span>
* <span class="sg-selector sg-class">
    Radio Label
  </span>

## Surface Modifiers

To ensure proper contrast and accessibility, surface modifiers are applied as combo classes to individual form elements and following naming convention <span class="sg-selector sg-class">`Element`</span> <span class="sg-selector sg-class">`Element` `Surface`</span>

| Element                                                                             | Surface             |
| ----------------------------------------------------------------------------------- | ------------------- |
| Input                                                                               | On Inverse          |
| Radio (Main class is  <span class="sg-selector sg-class">Radio Toggle</span>)       | On Accent Primary   |
| Checkbox (Main class is  <span class="sg-selector sg-class">Checkbox Toggle</span>) | On Accent Secondary |
|                                                                                     | On Accent Tertiary  |

Example: <span class="sg-selector sg-class">Checkbox Toggle</span> <span class="sg-selector sg-class">Checkbox On inverse</span>
