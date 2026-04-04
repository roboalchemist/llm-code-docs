# Source: https://developers.webflow.com/flowkit/v1.0.0/components/dropdown.mdx

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

The base class is <span class="sg-selector sg-class">Dropdown</span>. This class wraps the entire dropdown structure and controls visibility of the dropdown list.

## Elements

| Class                                                     | Purpose                                      |
| --------------------------------------------------------- | -------------------------------------------- |
| <span class="sg-selector sg-class">Dropdown Toggle</span> | Interactive button that reveals the dropdown |
| <span class="sg-selector sg-class">Dropdown List</span>   | Container for the list of options            |

## Direction Modifiers

Dropdowns support directional modifiers that control where the dropdown list appears in relation to the toggle button.

Combine these with <span class="sg-selector sg-class">Dropdown List</span> to control layout.

| Modifier Class                                                  | Description                      |
| --------------------------------------------------------------- | -------------------------------- |
| <span class="sg-selector sg-class">Open Left Dropdown</span>    | Opens list to the left           |
| <span class="sg-selector sg-class">Open Up Dropdown</span>      | Opens list above the toggle      |
| <span class="sg-selector sg-class">Open Up Left Dropdown</span> | Opens list above and to the left |

Example: <span class="sg-selector sg-class">Dropdown List</span> <span class="sg-selector sg-class">Open Left Dropdown</span>
