# Source: https://developers.webflow.com/flowkit/components/forms.mdx

***

title: Forms
slug: components/forms
description: Forms consist of modular components with consistent styling patterns.
hidden: null
'og:title': Flowkit - Forms
'og:description': Forms consist of modular components with consistent styling patterns.
---------------------------------------------------------------------------------------

## Class Naming

Forms consist of modular components with consistent styling patterns. Each element within a form, like labels, fields, toggles, and messages, is styled using reusable classes and combo modifiers to adapt to different contexts (inverse, accents, etc.).

**Form Components**

| Element Class                                                                                                 | Purpose                  |
| ------------------------------------------------------------------------------------------------------------- | ------------------------ |
| <span class="sg-selector sg-class">input\_field</span>                                                        | For basic text fields    |
| <span class="sg-selector sg-class">input\_field</span> <span class="sg-selector sg-class">is-select</span>    | For select fields        |
| <span class="sg-selector sg-class">input\_field</span> <span class="sg-selector sg-class">is-text-area</span> | For multiline input      |
| <span class="sg-selector sg-class">checkbox</span>                                                            | Custom-styled checkbox   |
| <span class="sg-selector sg-class">radio</span>                                                               | Custom-styled radio      |
| <span class="sg-selector sg-class">button</span>                                                              | For submitting the form  |
| <span class="sg-selector sg-class">form\_success-message</span>                                               | Visible after submission |
| <span class="sg-selector sg-class">form\_error-message</span>                                                 | Shows validation errors  |

## Elements

**Input elements**

* <span class="sg-selector sg-class">
    input_label
  </span>
* <span class="sg-selector sg-class">input</span> - wrapper of the label and input field

**Checkbox elements:**

* <span class="sg-selector sg-class">
    checkbox_toggle
  </span>
* <span class="sg-selector sg-class">
    checkbox_label
  </span>

**Radio elements:**

* <span class="sg-selector sg-class">
    radio_toggle
  </span>
* <span class="sg-selector sg-class">
    radio_label
  </span>

## Surface Modifiers

To ensure proper contrast and accessibility, surface modifiers are applied as combo classes to individual form elements and following naming convention <span class="sg-selector sg-class">`element`</span> <span class="sg-selector sg-class">on-`surface`</span>

Surface options: `on-inverse`, `on-accent-primary`, `on-accent-secondary`, `on-accent-tertiary`

Example: <span class="sg-selector sg-class">checkbox\_toggle</span> <span class="sg-selector sg-class">on-inverse</span>
