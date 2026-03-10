# Source: https://developers.webflow.com/flowkit/components/tabs.mdx

***

title: Tabs
slug: components/tabs
description: Tabs are navigation components that organize content into separate views.
hidden: null
'og:title': Flowkit - Tabs
'og:description': Tabs are navigation components that organize content into separate views.
-------------------------------------------------------------------------------------------

Each tab button uses a base class and can be styled to reflect different backgrounds or interface variants.

The base class is: <span class="sg-selector sg-class">tab\_menu-button</span>

## Surface Modifiers

Use these to adapt the tab appearance based on the background context.

Naming convention for combo classes is <span class="sg-selector sg-class">tab\_menu-button</span> <span class="sg-selector sg-class">on-`surface`</span>,
where `surface` can be `inverse`, `accent-primary`, `accent-tertiary`, or `accent-secondary`.

Example:
<span class="sg-selector sg-class">tab\_menu-button</span> <span class="sg-selector sg-class">on-inverse</span>

## Style Modifiers

Additional style options for tabs is <span class="sg-selector sg-class">tab\_menu-link</span>.  It removes tab background but keeps underline and label styling.
