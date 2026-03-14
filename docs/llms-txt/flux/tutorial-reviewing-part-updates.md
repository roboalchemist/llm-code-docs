# Source: https://docs.flux.ai/tutorials/tutorial-reviewing-part-updates.md

# Reviewing Component Updates in Flux

The community-focused nature of Flux means that you'll probably be using components that another Flux user owns. When that other user updates a component and publishes the update, that update can then be applied to your project. How can you get a notification of these updates, review them, and determine whether you want to take more ownership of your components?

It's important to note that this same mechanism applies when you're the owner of the component that's being modified. But in those cases, you're more likely to know what those changes are.

## How to Work With Component Updates

Whenever any component in your project has been updated, you'll notice a notification at the bottom of your screen like the one below:

![When you open a project, you may see a message box that flags an update is available for one of your components.](https://uploads.developerhub.io/prod/86Yw/9rm1ektfyviewq0a5rcrpnvo6kw8ypfufpqn31a8863pep4s3o5gcyn176fq48rv.png)

You can click the "Dismiss" button if you don't want to deal with component updates at that moment. You can access the Component updates [menu](#alternative-menu-item-access) anytime by clicking on the main Flux menu and locating the "Component Updates" option.

If you click the Review button, you will see the following dialog where you can review changes to components. From here, you can accept the component changes, and the updates will be applied to the components in your design. If you want to reject any component changes, just ignore them and continue using your project.

![](https://uploads.developerhub.io/prod/86Yw/d0jjejvu5ozpvbz6jeippusuoq8ab5iv2gzhpz23a6ztbrrmlveeybqtf92reiii.png)

Once Update is clicked, the newest available changes will be applied to the components in your design. You can also use the "Update All" option to update all components in the design automatically.

### Alternative Menu Item Access

You can also access the Component Updates dialog shown above from the main menu in the Flux platform. This option is accessible inside the schematic editor or the PCB editor.

![The list of Component Updates can be accessed from the main menu.](https://uploads.developerhub.io/prod/86Yw/e72bkdearo6bk8bri8wvivo6euz0hkyciz3r6aomv89x84gltzruwljy1npuuzsl.png)

### Receive Latest Drafts

**In Flux, you have absolute control over the components you use in your projects. For this reason, the platform does not automatically update components; instead, users can review and apply updates when available**. This prevents another user from inadvertently breaking your board and allows you to control how your project changes over time.

However, there are certain instances where you want to receive every change done to a component. A good example is when you're creating a new component or module. You might make many small changes and check how they look in the final project. **That's where the "Receive latest drafts" option comes in handy.**

**When you have "Receive latest drafts" enabled, changes will be automatically applied to your project without you having to accept them manually.**

> Keep in mind that you still need to [Publish changes to the library](https://docs.flux.ai/flux/tutorials/publishing-a-part-to-the-library#publish-changes-to-the-library) from the component.

## What Happens When Component Updates Are Applied?

When updates are applied, only the data that was changed in the schematic symbol and the footprint/layout for the components will be updated. If updates are applied to a footprint or module, the changes could require you to restore some connections or modify the connections in the PCB layout. In some cases, no changes will be needed to the schematics or PCB layout.

Make sure to take note of which component updates need to be applied, and check that the updates do not require additional major design changes. This involves comparing the pinout in the schematics and adjusting any connections. After reviewing the schematics, make sure to review the PCB layout and make any necessary modifications.

## Component Changes Are Not Required

When working with components in the public library, it is always possible that the owner makes changes to the component. If you open your project and you see component updates, you are not required to accept these into your project.

If you are designing something in Flux and you do not want to worry about component changes, you are also free to only use your own components. This will give you total control over your own library. Flux offers several options to create components:

1. Create all of your own components from scratch
2. Create your components by importing your KiCAD libraries
3. Create your own components by forking them from publicly available components

Option #3 is the easiest way to get up and running with a library of components that you control. When you fork or clone these components, they will be accessible in your own workspace and you will not have to worry about someone else modifying your components. To access your own projects and components inside the schematic editor or in the PCB editor, make sure you turn on the "Your items" filter option below the search bar. This will show all the components you have created in your own library.

If you are working as part of a group, then you will also want to make sure that any components you own have appropriate sharing privileges to prevent editing. If you give anyone in your group editing permissions for a component, and they make a change to that component, then you will also have to review those changes if you have used that component in a project.