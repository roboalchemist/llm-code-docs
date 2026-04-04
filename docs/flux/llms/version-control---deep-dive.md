# Source: https://docs.flux.ai/tutorials/version-control---deep-dive.md

# Version Control in PCB Design: Flux's Integrated Approach

No change is ever lost. Flux automatically saves every change into its integrated version control system.



## Overview

The software industry has found great benefits in tight version-controlled workflow, but this is something that does not get enough attention in the hardware world. **Automated version control is built into Flux**, **ensuring that no change is ever lost.** If someone makes a mistake on a design, you can always roll back to an earlier version.

In this tutorial, we'll show how version control works in Flux and how it's accessed in your projects.

## Accessing the Change History

The Change History is a mode where you can see all earlier versions of the project. A new version is created for every change a user makes to a project. A change could be **anything**, from adding a part, changing a wire, or deleting a trace.

To access the Change History:

1. Click on the Flux menu in the top left.
2. Click on the "Change History" menu to access a list of previous versions of your project.
3. The left-side menu will show a list with every version (change) in the project. Select one to see how the project looked at that point in time.

![](https://uploads.developerhub.io/prod/86Yw/wn7zxkougbsu62xsuiasi0qmlddoa4o5pgimgs0svi35omakkk25ggiadghkb5i1.png)

## Restoring a Previous Version

If the current project is not to your liking, you can roll it back to an earlier version.

To restore a previous version:

- Click on the Flux menu in the top left.
- Click on the "Change History" menu to access a list of previous versions of your project.
- The left-side menu will show a list with every version (change) in the project. Select the version you want to restore.
- Once you've found the version you want to roll back to, click on "Restore Version"

![](https://uploads.developerhub.io/prod/86Yw/d1z6j72k7sms979dvg11h9dzj3c1n8psvu7j00oi1pqzxqnot5gvavohhs00l4eo.gif)

**Pro tip:** If you decide to roll back to a previous version, that's also considered a change. This means that the roll back can also be reverted by restoring the version previous to the roll back.

## Part Updates in Version Control

In some cases, when you open a project in Flux, components in your design may have been [updated](https://docs.flux.ai/flux/tutorials/tutorial-reviewing-part-updates) by the owner. When this happens, you'll see a notification at the bottom of the screen stating that component updates are available. You must choose whether to accept or decline these updates - they won't be applied automatically. But how will those changes impact your design?

One way to find out is to accept the updates and see the impact on your project for yourself. Then, if you don't like what you see, you can easily undo it.

Accepting the update was a change to your project, so it was saved to the Change History. Use Undo or visit the Change History to restore a previous version.

## Forking and Cloning in Version Control

You can duplicate a project using either Fork or Clone. Both actions result in a duplicated project but impact the Change History differently:

- **Forking creates a copy of the project** _**and**_ **its change history.** When you open the forked project, you'll be able to see all earlier changes that were applied to the project. You could also roll back a forked project to a point before you applied the fork.
- **Cloning** **only creates** **a copy of the design data.** None of the revision history is copied to the cloned project. When cloning a project, you will not be able to revert to a version that existed before the cloning event. Only future revisions, where changes are applied to the project after cloning, can be accessed and reverted.

## Benefits of Version Control in PCB Design

Version control in PCB design offers several key advantages:

1. **Design Confidence**: Make changes without fear of losing previous work
2. **Collaboration**: Multiple team members can work on a design with clear accountability
3. **Design Review**: Compare different iterations to evaluate design decisions
4. **Troubleshooting**: Identify when and where issues were introduced
5. **Documentation**: Maintain a complete history of design evolution

## Best Practices for Version Control

To make the most of Flux's version control system:

- **Make incremental changes**: Smaller, focused changes make it easier to track and revert if needed
- **Use descriptive comments**: When making significant changes, add comments to help identify important versions
- **Review history periodically**: Familiarize yourself with the project's evolution
- **Consider forking for major experiments**: When trying significant design changes, fork the project to preserve the original

## Troubleshooting Common Issues

### Missing Previous Versions

If you can't find previous versions of your project:

- Verify you're looking at the correct project (not a clone)
- Check if you have the necessary permissions to view the project history
- Ensure you're using the Change History feature correctly

### Reverting Changes

If you're having trouble reverting to a previous version:

- Make sure you've selected the correct version in the Change History
- Check that you have edit permissions for the project
- Remember that reverting is itself a change that will be recorded in the history

### Collaboration Conflicts

When multiple people are working on a project:

- Communicate clearly about who is making what changes
- Consider using forks for major changes to avoid conflicts
- Review the Change History before making significant modifications

## What's Next

Now that you understand how version control works in Flux, you might want to explore:

- [Collaboration Deep Dive](https://docs.flux.ai/flux/tutorials/tutorial-collaboration-deep-dive) - Learn how to work with others on PCB designs
- [Reviewing Component Updates](https://docs.flux.ai/flux/tutorials/tutorial-reviewing-part-updates) - Understand how to manage component changes
- [Reusing Projects](https://docs.flux.ai/flux/tutorials/reusing-community-projects) - Discover how to leverage existing projects
- [Embedding Flux Projects](https://docs.flux.ai/flux/tutorials/tutorial-embed-a-flux-project) - Learn how to share your projects with others