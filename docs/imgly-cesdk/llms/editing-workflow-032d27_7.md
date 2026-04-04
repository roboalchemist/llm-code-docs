# Source: https://img.ly/docs/cesdk/macos/concepts/editing-workflow-032d27/

---
title: "Editing Workflow"
description: "Control editing access with Creator and Adopter roles, each offering tailored permissions and UI constraints."
platform: macos
url: "https://img.ly/docs/cesdk/macos/concepts/editing-workflow-032d27/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/macos/concepts-c9ff51/) > [Editing Workflow](https://img.ly/docs/cesdk/macos/concepts/editing-workflow-032d27/)

---

## Roles

User roles allow the CE.SDK to change and adapt its UI layout and functionality to provide the optimal editing experience for a specific purpose.

### Creator

The `Creator` role is the most powerful and least restrictive role that is offered by the CE.SDK. Running the editor with this role means that there are no limits to what the user can do with the loaded scene.

Elements can be added, moved, deleted, and modified. All types of controls for modifying the selected elements are shown inside of the inspector.

### Adopter

The `Adopter` role allows new elements to be added and modified. Existing elements of a scene are only modifiable based on the set of constraints that the `Creator` has manually enabled.

This provides the `Adopter` with a simpler interface that is reduced to only the properties that they should be able to change and prevents them from accidentally changing or deleting parts of a design that should not be modified.

An example use case for how such a distinction between `Creator` and `Adopter` roles can provide a lot of value is the process of designing business cards.

A professional designer (using the `Creator` role) can create a template design of the business card with the company name, logo, colors, etc. They can then use the constraints to make only the name text editable for non-creators. Non-designers (either the employees themselves or the HR department) can then easily open the design in a CE.SDK instance with the `Adopter` role and are able to quickly change the name on the business card and export it for printing, without a designer having to get involved.

### Role customization

Roles in the CE.SDK are sets of global scopes and settings. When changing the
role via the `setRole` command in the EditorAPI, the internal defaults for that
role are applied as described in the previous sections.

The CE.SDK and Engine provide a `onRoleChanged` callback subscription on the
EditorAPI. Callbacks registered here are invoked whenever the role changes and
can be used to configure additional settings or adjust the default scopes and
settings.



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
