# Source: https://docs.flux.ai/tutorials/tutorial-add-part-library.md

# Adding Components to the Flux Library: A Complete Guide

Add parts to the library. Create them from scratch or import them from other tools.



## Overview

Flux's library contains tens of thousands of parts created by the community that are ready to be used. You can add new parts if you haven't found the part you're looking for in the library. At the end of the process, you can choose to share it so other designers can use your part in their projects.

## Getting Started

When adding a part to the library in Flux, you have several options to fit your needs and workflow:

### Use an Existing Part

Start by [searching](https://docs.flux.ai/flux/reference/reference-library#searching) the library. With tens of thousands of community-created parts, there's a good chance you'll find what you need or something close to it.

### Clone or Fork for Customization

Found a similar part? [Clone](https://docs.flux.ai/flux/reference/reference-forking-cloning#cloning) it to make quick adjustments, or [fork](https://docs.flux.ai/flux/reference/reference-forking-cloning#forking) it to add missing details and contribute improvements back to the library.

### Import Parts from Other Tools

If you're migrating from other software or have parts stored elsewhere, you can import them into Flux. Currently, KiCAD v6 libraries are supported, with more formats to come. [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-import-part)

### Create from Scratch

For new, unique, or niche parts, create a component from the ground up using Flux's part editor. [Learn more.](https://docs.flux.ai/flux/tutorials/tutorial-creating-a-part-from-scratch)

> If you're having trouble importing or creating a new part, you can ask our [community on Slack](https://www.flux.ai/p/slack-community) for assistance.

## Share Your Parts

Flux's library is created and maintained by the community. When creating new parts, please consider [sharing them](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions#share-menu) with the community so others can benefit from them.

### Benefits of Sharing Parts

- **Help other designers**: Save time for others who need the same components
- **Get feedback**: Community members may suggest improvements to your parts
- **Build reputation**: Become known for creating high-quality, reliable parts
- **Improve the ecosystem**: Contribute to making Flux a more comprehensive platform

## Best Practices for Component Creation

To ensure your components are useful and accurate:

1. **Include comprehensive metadata**: Add manufacturer part numbers, descriptions, and tags
2. **Create accurate footprints**: Double-check dimensions against datasheets
3. **Add pin labels**: Clearly label all pins with their functions
4. **Include 3D models**: When possible, add 3D models for better visualization
5. **Test in a real design**: Verify the component works as expected in an actual project

## Troubleshooting Common Issues

### Import Problems

If you're having trouble importing parts:

- Ensure your source library files are in a supported format (currently KiCAD v6)
- Check that the file structure matches what Flux expects
- Try importing individual parts rather than entire libraries if you encounter errors

### Creation Challenges

When creating parts from scratch:

- Reference the manufacturer's datasheet for accurate dimensions
- Start with a similar existing part when possible
- Use the grid and snap features for precise placement
- Verify pin numbering matches the datasheet

### Sharing Issues

If you can't share your parts:

- Verify you have the correct permissions for your account
- Ensure you're not trying to share parts that contain proprietary information
- Check that you've completed all required fields for the part

## What's Next

Now that you understand how to add components to the Flux library, you might want to explore:

- [Creating a Generic Part](https://docs.flux.ai/flux/tutorials/tutorial-generic-part) - Learn how to create versatile, reusable components
- [Custom Pad Shapes](https://docs.flux.ai/flux/tutorials/custom-pad-shapes) - Discover how to create specialized pad geometries
- [Component Placement](https://docs.flux.ai/flux/tutorials/component-placement) - Learn best practices for placing components in your design
- [Working with the Library](https://docs.flux.ai/flux/reference/reference-library) - Explore advanced library features and management techniques