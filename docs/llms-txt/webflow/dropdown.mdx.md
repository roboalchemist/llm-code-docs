# Source: https://developers.webflow.com/flowkit/components/dropdown.mdx

***

title: Dropdown
slug: components/dropdown
description: Dropdowns are menus that display a list of options when triggered.
hidden: null
'og:title': Flowkit - Dropdown
'og:description': Dropdowns are menus that display a list of options when triggered.
------------------------------------------------------------------------------------

## Class Naming

The dropdown component is used to display a list of options that appear on interaction. It uses a base wrapper class and internal toggle/list elements to manage behavior and style.

The base class is <span class="sg-selector sg-class">dropdown</span>. This class wraps the entire dropdown structure and controls visibility of the dropdown list.

## Elements

| Class                                                      | Purpose                                      |
| ---------------------------------------------------------- | -------------------------------------------- |
| <span class="sg-selector sg-class">dropdown\_toggle</span> | Interactive button that reveals the dropdown |
| <span class="sg-selector sg-class">dropdown\_list</span>   | Container for the list of options            |

## Direction Modifiers

Dropdowns support directional modifiers that control where the dropdown list appears in relation to the toggle button.

Combine these with <span class="sg-selector sg-class">dropdown\_list</span> to control layout.

| Modifier Class                                                                                                      | Description                      |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| <span class="sg-selector sg-class">dropdown\_list</span> <span class="sg-selector sg-class">is-open\_left</span>    | Opens list to the left           |
| <span class="sg-selector sg-class">dropdown\_list</span> <span class="sg-selector sg-class">is-open\_up</span>      | Opens list above the toggle      |
| <span class="sg-selector sg-class">dropdown\_list</span> <span class="sg-selector sg-class">is-open\_up-left</span> | Opens list above and to the left |

Example: <span class="sg-selector sg-class">dropdown\_list</span> <span class="sg-selector sg-class">is-open\_left</span>
