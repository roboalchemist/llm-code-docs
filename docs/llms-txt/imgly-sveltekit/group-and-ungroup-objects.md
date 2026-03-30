# Group and Ungroup Objects

Group multiple blocks to move, scale, and transform them as a single unit; ungroup to edit them individually.

![Group and Ungroup Objects example showing grouped rectangles in CE.SDK](/docs/cesdk/_astro/browser.hero.BVZn_DGh_WiXiM.webp)

5 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-create-composition-grouping-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-create-composition-grouping-browser)

Groups let you treat multiple blocks as a cohesive unit. Grouped blocks move, scale, and rotate together while maintaining their relative positions. Groups can contain other groups, enabling hierarchical compositions.

Groups are not currently available when editing videos.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Group and Ungroup Objects Guide * * This example demonstrates: * - Creating multiple graphic blocks * - Checking if blocks can be grouped * - Grouping blocks together * - Navigating into and out of groups * - Ungrouping blocks * - Finding and inspecting groups */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    const engine = cesdk.engine;
    // Create a design scene and get the page    await cesdk.createDesignScene();    const pages = engine.block.findByType('page');    const page = pages[0];    if (!page) {      throw new Error('No page found');    }
    // Set page dimensions    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    // Create a graphic block with a colored rectangle shape    const block1 = engine.block.create('graphic');    const shape1 = engine.block.createShape('rect');    engine.block.setShape(block1, shape1);    engine.block.setWidth(block1, 120);    engine.block.setHeight(block1, 120);    engine.block.setPositionX(block1, 200);    engine.block.setPositionY(block1, 240);    const fill1 = engine.block.createFill('color');    engine.block.setColor(fill1, 'fill/color/value', {      r: 0.4,      g: 0.6,      b: 0.9,      a: 1.0    });    engine.block.setFill(block1, fill1);    engine.block.appendChild(page, block1);
    // Create two more blocks for grouping    const block2 = engine.block.create('graphic');    const shape2 = engine.block.createShape('rect');    engine.block.setShape(block2, shape2);    engine.block.setWidth(block2, 120);    engine.block.setHeight(block2, 120);    engine.block.setPositionX(block2, 340);    engine.block.setPositionY(block2, 240);    const fill2 = engine.block.createFill('color');    engine.block.setColor(fill2, 'fill/color/value', {      r: 0.9,      g: 0.5,      b: 0.4,      a: 1.0    });    engine.block.setFill(block2, fill2);    engine.block.appendChild(page, block2);
    const block3 = engine.block.create('graphic');    const shape3 = engine.block.createShape('rect');    engine.block.setShape(block3, shape3);    engine.block.setWidth(block3, 120);    engine.block.setHeight(block3, 120);    engine.block.setPositionX(block3, 480);    engine.block.setPositionY(block3, 240);    const fill3 = engine.block.createFill('color');    engine.block.setColor(fill3, 'fill/color/value', {      r: 0.5,      g: 0.8,      b: 0.5,      a: 1.0    });    engine.block.setFill(block3, fill3);    engine.block.appendChild(page, block3);
    // Check if the blocks can be grouped together    const canGroup = engine.block.isGroupable([block1, block2, block3]);    console.log('Blocks can be grouped:', canGroup);
    // Group the blocks together    if (canGroup) {      const groupId = engine.block.group([block1, block2, block3]);      console.log('Created group with ID:', groupId);
      // Select the group to show it in the UI      engine.block.setSelected(groupId, true);
      // Enter the group to select individual members      engine.block.enterGroup(groupId);
      // Select a specific member within the group      engine.block.setSelected(block2, true);      console.log('Selected member inside group');
      // Exit the group to return selection to the parent group      engine.block.exitGroup(block2);      console.log('Exited group, group is now selected');
      // Find all groups in the scene      const allGroups = engine.block.findByType('group');      console.log('Number of groups in scene:', allGroups.length);
      // Check the type of the group block      const groupType = engine.block.getType(groupId);      console.log('Group block type:', groupType);
      // Get the members of the group      const members = engine.block.getChildren(groupId);      console.log('Group has', members.length, 'members');
      // Ungroup the blocks to make them independent again      engine.block.ungroup(groupId);      console.log('Ungrouped blocks');
      // Verify blocks are no longer in a group      const groupsAfterUngroup = engine.block.findByType('group');      console.log('Groups after ungrouping:', groupsAfterUngroup.length);
      // Re-group for the final display      const finalGroup = engine.block.group([block1, block2, block3]);      engine.block.setSelected(finalGroup, true);    }
    // Enable auto-fit zoom to keep the page centered    engine.scene.enableZoomAutoFit(page, 'Both', 40, 40, 40, 40);  }}
export default Example;
```

This guide covers how to check if blocks can be grouped, create and dissolve groups, navigate into groups to select individual members, and find existing groups in a scene.

## Understanding Groups[#](#understanding-groups)

Groups are blocks with type `'group'` that contain child blocks as members. Transformations applied to a group affect all members proportionally—position, scale, and rotation cascade to all children.

Groups can be nested, meaning a group can contain other groups. This enables complex hierarchical structures where multiple logical units can be combined and manipulated together.

**What cannot be grouped**

*   Scene blocks cannot be grouped
*   Blocks already part of a group cannot be grouped again until ungrouped

## Create the Blocks[#](#create-the-blocks)

We first create several graphic blocks that we’ll group together. Each block has a different color fill to make them visually distinct.

```
// Create a graphic block with a colored rectangle shapeconst block1 = engine.block.create('graphic');const shape1 = engine.block.createShape('rect');engine.block.setShape(block1, shape1);engine.block.setWidth(block1, 120);engine.block.setHeight(block1, 120);engine.block.setPositionX(block1, 200);engine.block.setPositionY(block1, 240);const fill1 = engine.block.createFill('color');engine.block.setColor(fill1, 'fill/color/value', {  r: 0.4,  g: 0.6,  b: 0.9,  a: 1.0});engine.block.setFill(block1, fill1);engine.block.appendChild(page, block1);
```

## Check If Blocks Can Be Grouped[#](#check-if-blocks-can-be-grouped)

Before grouping, verify that the selected blocks can be grouped using `engine.block.isGroupable()`. This method returns `true` if all blocks can be grouped together, or `false` if any block is a scene or already belongs to a group.

```
// Check if the blocks can be grouped togetherconst canGroup = engine.block.isGroupable([block1, block2, block3]);console.log('Blocks can be grouped:', canGroup);
```

## Create a Group[#](#create-a-group)

Use `engine.block.group()` to combine multiple blocks into a new group. The method returns the ID of the newly created group block. The group inherits the combined bounding box of its members.

```
// Group the blocks togetherif (canGroup) {  const groupId = engine.block.group([block1, block2, block3]);  console.log('Created group with ID:', groupId);
  // Select the group to show it in the UI  engine.block.setSelected(groupId, true);
```

## Navigate Group Selection[#](#navigate-group-selection)

CE.SDK provides methods to navigate into and out of groups while editing.

### Enter a Group[#](#enter-a-group)

When a group is selected, use `engine.block.enterGroup()` to enter editing mode for that group. This allows you to select and modify individual members within the group.

```
// Enter the group to select individual membersengine.block.enterGroup(groupId);
// Select a specific member within the groupengine.block.setSelected(block2, true);console.log('Selected member inside group');
```

### Exit a Group[#](#exit-a-group)

When editing a member inside a group, use `engine.block.exitGroup()` to return selection to the parent group. This method takes a member block ID and selects its parent group.

```
// Exit the group to return selection to the parent groupengine.block.exitGroup(block2);console.log('Exited group, group is now selected');
```

## Find and Inspect Groups[#](#find-and-inspect-groups)

Discover groups in a scene and inspect their contents using `engine.block.findByType()`, `engine.block.getType()`, and `engine.block.getChildren()`.

```
// Find all groups in the sceneconst allGroups = engine.block.findByType('group');console.log('Number of groups in scene:', allGroups.length);
// Check the type of the group blockconst groupType = engine.block.getType(groupId);console.log('Group block type:', groupType);
// Get the members of the groupconst members = engine.block.getChildren(groupId);console.log('Group has', members.length, 'members');
```

Use `engine.block.findByType('group')` to get all group blocks in the current scene. Use `engine.block.getType()` to check if a specific block is a group (returns `'//ly.img.ubq/group'`). Use `engine.block.getChildren()` to get the member blocks of a group.

## Ungroup Blocks[#](#ungroup-blocks)

Use `engine.block.ungroup()` to dissolve a group and release its children back to the parent container. The children maintain their current positions in the scene.

```
// Ungroup the blocks to make them independent againengine.block.ungroup(groupId);console.log('Ungrouped blocks');
// Verify blocks are no longer in a groupconst groupsAfterUngroup = engine.block.findByType('group');console.log('Groups after ungrouping:', groupsAfterUngroup.length);
```

## Troubleshooting[#](#troubleshooting)

### Blocks Cannot Be Grouped[#](#blocks-cannot-be-grouped)

If `engine.block.isGroupable()` returns `false`:

*   Check if any of the blocks is a scene block (scenes cannot be grouped)
*   Check if any block is already part of a group (use `engine.block.getParent()` to verify)
*   Ensure all block IDs are valid

### Enter Group Has No Effect[#](#enter-group-has-no-effect)

If `engine.block.enterGroup()` doesn’t change selection:

*   Verify the block is a group using `engine.block.getType()`
*   Ensure the `'editor/select'` scope is enabled

### Group Not Visible After Creation[#](#group-not-visible-after-creation)

If a newly created group is not visible:

*   Check that the member blocks were visible before grouping
*   Verify the group’s opacity using `engine.block.getOpacity()`

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.isGroupable(ids)` | Check if blocks can be grouped together |
| `engine.block.group(ids)` | Create a group from multiple blocks |
| `engine.block.ungroup(id)` | Dissolve a group and release its children |
| `engine.block.enterGroup(id)` | Enter group editing mode (select member) |
| `engine.block.exitGroup(id)` | Exit group editing mode (select parent group) |
| `engine.block.findByType(type)` | Find all blocks of a specific type |
| `engine.block.getType(id)` | Get the type string of a block |
| `engine.block.getParent(id)` | Get the parent block |
| `engine.block.getChildren(id)` | Get child blocks of a container |

## Next Steps[#](#next-steps)

Explore related topics:

*   [Layer Management](sveltekit/create-composition/layer-management-18f07a/) \- Control z-order and visibility of blocks
*   [Position and Align](sveltekit/insert-media/position-and-align-cc6b6a/) \- Arrange blocks precisely on the canvas
*   [Lock Design](sveltekit/create-composition/lock-design-0a81de/) \- Prevent modifications to specific elements

---



[Source](https:/img.ly/docs/cesdk/sveltekit/create-composition/collage-f7d28d)