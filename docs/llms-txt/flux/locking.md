# Source: https://docs.flux.ai/reference/locking.md

# Locking


Lock objects to prevent unwanted changes.

{% image url="https://uploads.developerhub.io/prod/86Yw/p1flz6dy7njfdwp5bj4w2823otmrpg7hzwwyirpx0zdov83mweg6h5y3v75g3ab6.png" mode="responsive" height="1208" width="2147" %}
{% /image %}

## Overview

Locking prevents users from accidentally interacting with an object. This is particularly helpful for larger projects, or where the position of an object is critical.

**On the PCB editor, every element can be locked, except for the root object. On the Schematic editor, any component (part or module) can be locked.**

## Locking an Object

There are three ways of locking an object:

- **Object tree:** go the "Objects" tab on the left, find the target component and click on the lock icon
- **Context menu:** right-click on the target object and select "Lock"
- **Hotkey:** Use `Shift+L`

{% image url="https://uploads.developerhub.io/prod/86Yw/waap2s1ofy12e4aiwdxph3m9n58tnu1z6h4o25vou17yovhql6uc8yktsncuoyp7.gif" mode="600" height="480" width="852" %}
{% /image %}

### What is Disabled?

Locking disables the following interactions on the PCB editor:

- Drag
- Context menu and hotkeys for:
    - Add
    - Delete
    - Disable
    - Rotate
    - Flip layer
    - Align
    - Space Evenly
    - Trace Width
    - Replace

### What is Enabled?

Some interactions will still be possible on locked elements:

- Selection
- Wiring and routing to and from locked objects.
- Context menu and hotkeys for...
    - Flux
    - Copy and copy special
    - Paste
    - Cut (results in a copy action)
    - Start Routing a Trace
    - Open
    - Measure Distance

### Locking and Inheritance

When locking an element, every children of  said element will also become locked using a special state called lock from inheritance. This is shown with a dot.

Any child can also be manually locked. Manually locked children remain locked even when the parent becomes unlocked.

{% image url="https://uploads.developerhub.io/prod/86Yw/htr27tzsx6me9ip08rctxobma9wjilb2ua78lxi56sxn0y8lruw3lpuh5plu6flr.gif" mode="600" height="480" width="852" %}
{% /image %}

### Locking and Collaboration

Lock is a document state, meaning it applies to every user that has access to the project. Only users with edit permissions can lock or unlock objects.

### Locking and Version History

Locking doesn’t make a visible action record in the change history, but it can be undone with the undo menu item or hotkey (`Ctrl/Cmd + Z`).

## Unlocking an Object

To unlock an element, find it in the object list and click on the lock symbol.

{% image url="https://uploads.developerhub.io/prod/86Yw/0zzeenb2zid7r3h5fhg1yolwivoubdy6sr37uyusv5vkf5103ip7joiqzkxp1zm8.gif" mode="600" height="480" width="852" %}
{% /image %}
