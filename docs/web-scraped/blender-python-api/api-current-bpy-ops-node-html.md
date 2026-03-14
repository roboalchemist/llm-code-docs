# Source: https://docs.blender.org/api/current/bpy.ops.node.html

Title: Node Operators - Blender Python API

URL Source: https://docs.blender.org/api/current/bpy.ops.node.html

Markdown Content:
Hide navigation sidebar
Hide table of contents sidebar
Skip to content
Blender Python API

DOCUMENTATION

Quickstart
API Overview
API Reference Usage
Best Practice
Tips and Tricks
Gotchas
Toggle navigation of Gotchas
Advanced
Toggle navigation of Advanced
Change Log

APPLICATION MODULES

Context Access (bpy.context)
Data Access (bpy.data)
Message Bus (bpy.msgbus)
Operators (bpy.ops)
Toggle navigation of Operators (bpy.ops)
Action Operators
Anim Operators
Armature Operators
Asset Operators
Boid Operators
Brush Operators
Buttons Operators
Cachefile Operators
Camera Operators
Clip Operators
Cloth Operators
Collection Operators
Console Operators
Constraint Operators
Curve Operators
Curves Operators
Cycles Operators
Dpaint Operators
Ed Operators
Export Anim Operators
Export Scene Operators
Extensions Operators
File Operators
Fluid Operators
Font Operators
Geometry Operators
Gizmogroup Operators
Gpencil Operators
Graph Operators
Grease Pencil Operators
Image Operators
Import Anim Operators
Import Curve Operators
Import Scene Operators
Info Operators
Lattice Operators
Marker Operators
Mask Operators
Material Operators
Mball Operators
Mesh Operators
Nla Operators
Node Operators
Object Operators
Outliner Operators
Paint Operators
Paintcurve Operators
Palette Operators
Particle Operators
Pointcloud Operators
Pose Operators
Poselib Operators
Preferences Operators
Ptcache Operators
Render Operators
Rigidbody Operators
Scene Operators
Screen Operators
Script Operators
Sculpt Operators
Sculpt Curves Operators
Sequencer Operators
Sound Operators
Spreadsheet Operators
Surface Operators
Text Operators
Text Editor Operators
Texture Operators
Transform Operators
Ui Operators
Uilist Operators
Uv Operators
View2D Operators
View3D Operators
Wm Operators
Workspace Operators
World Operators
Types (bpy.types)
Toggle navigation of Types (bpy.types)
Utilities (bpy.utils)
Toggle navigation of Utilities (bpy.utils)
Path Utilities (bpy.path)
Application Data (bpy.app)
Toggle navigation of Application Data (bpy.app)
Property Definitions (bpy.props)

STANDALONE MODULES

Audio System (aud)
Additional Math Functions (bl_math)
Font Drawing (blf)
BMesh Module (bmesh)
Toggle navigation of BMesh Module (bmesh)
Extra Utilities (bpy_extras)
Toggle navigation of Extra Utilities (bpy_extras)
Freestyle Module (freestyle)
Toggle navigation of Freestyle Module (freestyle)
GPU Module (gpu)
Toggle navigation of GPU Module (gpu)
GPU Utilities (gpu_extras)
Toggle navigation of GPU Utilities (gpu_extras)
ID Property Access (idprop.types)
Image Buffer (imbuf)
Toggle navigation of Image Buffer (imbuf)
Math Types & Utilities (mathutils)
Toggle navigation of Math Types & Utilities (mathutils)
5.0
Toggle table of contents sidebar
Node Operators
bpy.ops.node.activate_viewer()

Activate selected viewer node in compositor and geometry nodes

bpy.ops.node.add_closure_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

Add a Closure zone

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

FILE:

startup/bl_operators/node.py:633

bpy.ops.node.add_collection(*, name='', session_uid=0)

Add a collection info node to the current node editor

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_color(*, color=(0.0, 0.0, 0.0, 0.0), gamma=False, has_alpha=False)

Add a color node to the current node editor

PARAMETERS:

color (float array of 4 items in [0, inf], (optional)) – Color, Source color

gamma (boolean, (optional)) – Gamma Corrected, The source color is gamma corrected

has_alpha (boolean, (optional)) – Has Alpha, The source color contains an Alpha component

bpy.ops.node.add_empty_group(*, settings=None, use_transform=False)

Add a group node with an empty group

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

FILE:

startup/bl_operators/node.py:534

bpy.ops.node.add_foreach_geometry_element_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

FILE:

startup/bl_operators/node.py:633

bpy.ops.node.add_group(*, name='', session_uid=0, show_datablock_in_node=True)

Add an existing node group to the current node editor

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

show_datablock_in_node (boolean, (optional)) – Show the data-block selector in the node

bpy.ops.node.add_group_asset(*, asset_library_type='LOCAL', asset_library_identifier='', relative_asset_identifier='')

Add a node group asset to the active node tree

PARAMETERS:

asset_library_type (enum in Asset Library Type Items, (optional)) – Asset Library Type

asset_library_identifier (string, (optional, never None)) – Asset Library Identifier

relative_asset_identifier (string, (optional, never None)) – Relative Asset Identifier

bpy.ops.node.add_group_input_node(*, socket_identifier='', panel_identifier=0)

Add a Group Input node with selected sockets to the current node editor

PARAMETERS:

socket_identifier (string, (optional, never None)) – Socket Identifier, Socket to include in the added group input/output node

panel_identifier (int in [-inf, inf], (optional)) – Panel Identifier, Panel from which to add sockets to the added group input/output node

bpy.ops.node.add_image(*, filepath='', directory='', files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name='', session_uid=0)

Add a image/movie file as node to the current node editor

PARAMETERS:

filepath (string, (optional, never None)) – File Path, Path to file

directory (string, (optional, never None)) – Directory, Directory of the file

files (bpy_prop_collection of OperatorFileListElement, (optional)) – Files

hide_props_region (boolean, (optional)) – Hide Operator Properties, Collapse the region displaying the operator settings

check_existing (boolean, (optional)) – Check Existing, Check and warn on overwriting existing files

filter_blender (boolean, (optional)) – Filter .blend files

filter_backup (boolean, (optional)) – Filter .blend files

filter_image (boolean, (optional)) – Filter image files

filter_movie (boolean, (optional)) – Filter movie files

filter_python (boolean, (optional)) – Filter Python files

filter_font (boolean, (optional)) – Filter font files

filter_sound (boolean, (optional)) – Filter sound files

filter_text (boolean, (optional)) – Filter text files

filter_archive (boolean, (optional)) – Filter archive files

filter_btx (boolean, (optional)) – Filter btx files

filter_alembic (boolean, (optional)) – Filter Alembic files

filter_usd (boolean, (optional)) – Filter USD files

filter_obj (boolean, (optional)) – Filter OBJ files

filter_volume (boolean, (optional)) – Filter OpenVDB volume files

filter_folder (boolean, (optional)) – Filter folders

filter_blenlib (boolean, (optional)) – Filter Blender IDs

filemode (int in [1, 9], (optional)) – File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file

relative_path (boolean, (optional)) – Relative Path, Select the file relative to the blend file

show_multiview (boolean, (optional)) – Enable Multi-View

use_multiview (boolean, (optional)) – Use Multi-View

display_type (enum in ['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL'], (optional)) –

Display Type

DEFAULT Default – Automatically determine display type for files.

LIST_VERTICAL Short List – Display files as short list.

LIST_HORIZONTAL Long List – Display files as a detailed list.

THUMBNAIL Thumbnails – Display files as thumbnails.

sort_method (enum in ['DEFAULT', 'FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE', 'ASSET_CATALOG'], (optional)) –

File sorting mode

DEFAULT Default – Automatically determine sort method for files.

FILE_SORT_ALPHA Name – Sort the file list alphabetically.

FILE_SORT_EXTENSION Extension – Sort the file list by extension/type.

FILE_SORT_TIME Modified Date – Sort files by modification time.

FILE_SORT_SIZE Size – Sort files by size.

ASSET_CATALOG Asset Catalog – Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_import_node(*, directory='', files=None)

Add an import node to the node tree

PARAMETERS:

directory (string, (optional, never None)) – Directory, Directory of the file

files (bpy_prop_collection of OperatorFileListElement, (optional)) – Files

bpy.ops.node.add_mask(*, name='', session_uid=0)

Add a mask node to the current node editor

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_material(*, name='', session_uid=0)

Add a material node to the current node editor

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_node(*, settings=None, use_transform=False, type='', visible_output='')

Add a node to the active tree

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

type (string, (optional, never None)) – Node Type, Node type

visible_output (string, (optional, never None)) – Output Name, If provided, all outputs that are named differently will be hidden

FILE:

startup/bl_operators/node.py:419

bpy.ops.node.add_object(*, name='', session_uid=0)

Add an object info node to the current node editor

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the data-block to use by the operator

session_uid (int in [-inf, inf], (optional)) – Session UID, Session UID of the data-block to use by the operator

bpy.ops.node.add_repeat_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

Add a repeat zone that allows executing nodes a dynamic number of times

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

FILE:

startup/bl_operators/node.py:633

bpy.ops.node.add_reroute(*, path=None, cursor=11)

Add a reroute node

PARAMETERS:

path (bpy_prop_collection of OperatorMousePath, (optional)) – Path

cursor (int in [0, inf], (optional)) – Cursor

bpy.ops.node.add_simulation_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0))

Add simulation zone input and output nodes to the active tree

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

FILE:

startup/bl_operators/node.py:633

bpy.ops.node.add_zone(*, settings=None, use_transform=False, offset=(150.0, 0.0), input_node_type='', output_node_type='', add_default_geometry_link=False)

Undocumented, consider contributing.

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

use_transform (boolean, (optional)) – Use Transform, Start transform operator after inserting the node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

input_node_type (string, (optional, never None)) – Input Node, Specifies the input node used by the created zone

output_node_type (string, (optional, never None)) – Output Node, Specifies the output node used by the created zone

add_default_geometry_link (boolean, (optional)) – Add Geometry Link, When enabled, create a link between geometry sockets in this zone

FILE:

startup/bl_operators/node.py:633

bpy.ops.node.attach()

Attach active node to a frame

bpy.ops.node.backimage_fit()

Fit the background image to the view

bpy.ops.node.backimage_move()

Move node backdrop

bpy.ops.node.backimage_sample()

Use mouse to sample background image

bpy.ops.node.backimage_zoom(*, factor=1.2)

Zoom in/out the background image

PARAMETERS:

factor (float in [0, 10], (optional)) – Factor

bpy.ops.node.bake_node_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.bake_node_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.bake_node_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.capture_attribute_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.capture_attribute_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.capture_attribute_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.clear_viewer_border()

Clear the boundaries for viewer operations

bpy.ops.node.clipboard_copy()

Copy the selected nodes to the internal clipboard

bpy.ops.node.clipboard_paste(*, offset=(0.0, 0.0))

Paste nodes from the internal clipboard to the active node tree

PARAMETERS:

offset (float array of 2 items in [-inf, inf], (optional)) – Location, The 2D view location for the center of the new nodes, or unchanged if not set

bpy.ops.node.closure_input_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.closure_input_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.closure_input_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.closure_output_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.closure_output_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.closure_output_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.collapse_hide_unused_toggle()

Toggle collapsed nodes and hide unused sockets

FILE:

startup/bl_operators/node.py:856

bpy.ops.node.combine_bundle_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.combine_bundle_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.combine_bundle_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.connect_to_output(*, run_in_geometry_nodes=True)

Connect active node to the active output node of the node tree

PARAMETERS:

run_in_geometry_nodes (boolean, (optional)) – Run in Geometry Nodes Editor

FILE:

startup/bl_operators/connect_to_output.py:251

bpy.ops.node.cryptomatte_layer_add()

Add a new input layer to a Cryptomatte node

bpy.ops.node.cryptomatte_layer_remove()

Remove layer from a Cryptomatte node

bpy.ops.node.deactivate_viewer()

Deactivate selected viewer node in geometry nodes

bpy.ops.node.default_group_width_set()

Set the width based on the parent group node in the current context

bpy.ops.node.delete()

Remove selected nodes

bpy.ops.node.delete_reconnect()

Remove nodes and reconnect nodes as if deletion was muted

bpy.ops.node.detach()

Detach selected nodes from parents

bpy.ops.node.detach_translate_attach(*, NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

Detach nodes, move and attach to frame

PARAMETERS:

NODE_OT_detach (NODE_OT_detach, (optional)) – Detach Nodes, Detach selected nodes from parents

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

NODE_OT_attach (NODE_OT_attach, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.duplicate(*, keep_inputs=False, linked=True)

Duplicate selected nodes

PARAMETERS:

keep_inputs (boolean, (optional)) – Keep Inputs, Keep the input links to duplicated nodes

linked (boolean, (optional)) – Linked, Duplicate node but not node trees, linking to the original data

bpy.ops.node.duplicate_compositing_node_group()

Duplicate the currently assigned compositing node group.

bpy.ops.node.duplicate_move(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

Duplicate selected nodes and move them

PARAMETERS:

NODE_OT_duplicate (NODE_OT_duplicate, (optional)) – Duplicate Nodes, Duplicate selected nodes

NODE_OT_translate_attach (NODE_OT_translate_attach, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.duplicate_move_keep_inputs(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

Duplicate selected nodes keeping input links and move them

PARAMETERS:

NODE_OT_duplicate (NODE_OT_duplicate, (optional)) – Duplicate Nodes, Duplicate selected nodes

NODE_OT_translate_attach (NODE_OT_translate_attach, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.duplicate_move_linked(*, NODE_OT_duplicate=None, NODE_OT_translate_attach=None)

Duplicate selected nodes, but not their node trees, and move them

PARAMETERS:

NODE_OT_duplicate (NODE_OT_duplicate, (optional)) – Duplicate Nodes, Duplicate selected nodes

NODE_OT_translate_attach (NODE_OT_translate_attach, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.enum_definition_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.enum_definition_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.enum_definition_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_input_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_input_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_input_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_output_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_output_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.evaluate_closure_output_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.field_to_grid_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.field_to_grid_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.field_to_grid_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.file_output_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.file_output_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.file_output_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.find_node()

Search for a node by name and focus and select it

bpy.ops.node.foreach_geometry_element_zone_generation_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_generation_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_generation_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_input_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_input_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_input_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_main_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_main_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.foreach_geometry_element_zone_main_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.format_string_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.format_string_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.format_string_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.geometry_nodes_viewer_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.geometry_nodes_viewer_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.geometry_nodes_viewer_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.gltf_settings_node_operator()

Add a node to the active tree for glTF export

FILE:

addons_core/io_scene_gltf2/blender/com/gltf2_blender_ui.py:34

bpy.ops.node.group_edit(*, exit=False)

Edit node group

PARAMETERS:

exit (boolean, (optional)) – Exit

bpy.ops.node.group_enter_exit()

Enter or exit node group based on cursor location

bpy.ops.node.group_insert()

Insert selected nodes into a node group

bpy.ops.node.group_make()

Make group from selected nodes

bpy.ops.node.group_separate(*, type='COPY')

Separate selected nodes from the node group

PARAMETERS:

type (enum in ['COPY', 'MOVE'], (optional)) –

Type

COPY Copy – Copy to parent node tree, keep group intact.

MOVE Move – Move to parent node tree, remove from group.

bpy.ops.node.group_ungroup()

Ungroup selected nodes

bpy.ops.node.hide_socket_toggle()

Toggle unused node socket display

bpy.ops.node.hide_toggle()

Toggle collapsing of selected nodes

bpy.ops.node.index_switch_item_add(*, node_identifier=0)

Add an item to the index switch

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.index_switch_item_remove(*, index=0)

Remove an item from the index switch

PARAMETERS:

index (int in [0, inf], (optional)) – Index, Index to remove

bpy.ops.node.insert_offset()

Automatically offset nodes on insertion

bpy.ops.node.interface_item_duplicate()

Add a copy of the active item to the interface

FILE:

startup/bl_operators/node.py:1042

bpy.ops.node.interface_item_make_panel_toggle()

Make the active boolean socket a toggle for its parent panel

FILE:

startup/bl_operators/node.py:1118

bpy.ops.node.interface_item_new(*, item_type='INPUT')

Add a new item to the interface

PARAMETERS:

item_type (enum in ['INPUT', 'OUTPUT', 'PANEL'], (optional)) – Item Type, Type of the item to create

FILE:

startup/bl_operators/node.py:948

bpy.ops.node.interface_item_new_panel_toggle()

Add a checkbox to the currently selected panel

FILE:

startup/bl_operators/node.py:1013

bpy.ops.node.interface_item_remove()

Remove active item from the interface

FILE:

startup/bl_operators/node.py:1061

bpy.ops.node.interface_item_unlink_panel_toggle()

Make the panel toggle a stand-alone socket

FILE:

startup/bl_operators/node.py:1166

bpy.ops.node.join()

Attach selected nodes to a new common frame

bpy.ops.node.join_named(*, NODE_OT_join=None, WM_OT_call_panel=None)

Create a new frame node around the selected nodes and name it immediately

PARAMETERS:

NODE_OT_join (NODE_OT_join, (optional)) – Join Nodes in Frame, Attach selected nodes to a new common frame

WM_OT_call_panel (WM_OT_call_panel, (optional)) – Call Panel, Open a predefined panel

bpy.ops.node.join_nodes()

Merge selected group input nodes into one if possible

bpy.ops.node.link(*, detach=False, drag_start=(0.0, 0.0), inside_padding=2.0, outside_padding=0.0, speed_ramp=1.0, max_speed=26.0, delay=0.5, zoom_influence=0.5)

Use the mouse to create a link between two nodes

PARAMETERS:

detach (boolean, (optional)) – Detach, Detach and redirect existing links

drag_start (float array of 2 items in [-6, 6], (optional)) – Drag Start, The position of the mouse cursor at the start of the operation

inside_padding (float in [0, 100], (optional)) – Inside Padding, Inside distance in UI units from the edge of the region within which to start panning

outside_padding (float in [0, 100], (optional)) – Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning

speed_ramp (float in [0, 100], (optional)) – Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge

max_speed (float in [0, 10000], (optional)) – Max Speed, Maximum speed in UI units per second

delay (float in [0, 10], (optional)) – Delay, Delay in seconds before maximum speed is reached

zoom_influence (float in [0, 1], (optional)) – Zoom Influence, Influence of the zoom factor on scroll speed

bpy.ops.node.link_make(*, replace=False)

Make a link between selected output and input sockets

PARAMETERS:

replace (boolean, (optional)) – Replace, Replace socket connections with the new links

bpy.ops.node.link_viewer()

Link to viewer node

bpy.ops.node.links_cut(*, path=None, cursor=15)

Use the mouse to cut (remove) some links

PARAMETERS:

path (bpy_prop_collection of OperatorMousePath, (optional)) – Path

cursor (int in [0, inf], (optional)) – Cursor

bpy.ops.node.links_detach()

Remove all links to selected nodes, and try to connect neighbor nodes together

bpy.ops.node.links_mute(*, path=None, cursor=39)

Use the mouse to mute links

PARAMETERS:

path (bpy_prop_collection of OperatorMousePath, (optional)) – Path

cursor (int in [0, inf], (optional)) – Cursor

bpy.ops.node.move_detach_links(*, NODE_OT_links_detach=None, TRANSFORM_OT_translate=None)

Move a node to detach links

PARAMETERS:

NODE_OT_links_detach (NODE_OT_links_detach, (optional)) – Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

bpy.ops.node.move_detach_links_release(*, NODE_OT_links_detach=None, NODE_OT_translate_attach=None)

Move a node to detach links

PARAMETERS:

NODE_OT_links_detach (NODE_OT_links_detach, (optional)) – Detach Links, Remove all links to selected nodes, and try to connect neighbor nodes together

NODE_OT_translate_attach (NODE_OT_translate_attach, (optional)) – Move and Attach, Move nodes and attach to frame

bpy.ops.node.mute_toggle()

Toggle muting of selected nodes

bpy.ops.node.new_compositing_node_group(*, name='')

Create a new compositing node group and initialize it with default nodes

PARAMETERS:

name (string, (optional, never None)) – Name

bpy.ops.node.new_compositor_sequencer_node_group(*, name='Sequencer Compositor Nodes')

Create a new compositor node group for sequencer

PARAMETERS:

name (string, (optional, never None)) – Name

bpy.ops.node.new_geometry_node_group_assign()

Create a new geometry node group and assign it to the active modifier

FILE:

startup/bl_operators/geometry_nodes.py:340

bpy.ops.node.new_geometry_node_group_tool()

Create a new geometry node group for a tool

FILE:

startup/bl_operators/geometry_nodes.py:361

bpy.ops.node.new_geometry_nodes_modifier()

Create a new modifier with a new geometry node group

FILE:

startup/bl_operators/geometry_nodes.py:317

bpy.ops.node.new_node_tree(*, type='', name='NodeTree')

Create a new node tree

PARAMETERS:

type (enum in [], (optional)) – Tree Type

name (string, (optional, never None)) – Name

bpy.ops.node.node_color_preset_add(*, name='', remove_name=False, remove_active=False)

Add or remove a Node Color Preset

PARAMETERS:

name (string, (optional, never None)) – Name, Name of the preset, used to make the path name

remove_name (boolean, (optional)) – remove_name

remove_active (boolean, (optional)) – remove_active

FILE:

startup/bl_operators/presets.py:119

bpy.ops.node.node_copy_color()

Copy color to all selected nodes

bpy.ops.node.options_toggle()

Toggle option buttons display for selected nodes

bpy.ops.node.parent_set()

Attach selected nodes

bpy.ops.node.preview_toggle()

Toggle preview display for selected nodes

bpy.ops.node.read_viewlayers()

Read all render layers of all used scenes

bpy.ops.node.render_changed()

Render current scene, when input node’s layer has been changed

bpy.ops.node.repeat_zone_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.repeat_zone_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.repeat_zone_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.resize()

Resize a node

bpy.ops.node.select(*, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0, 0), socket_select=False, clear_viewer=False)

Select the node under the cursor

PARAMETERS:

extend (boolean, (optional)) – Extend, Extend selection instead of deselecting everything first

deselect (boolean, (optional)) – Deselect, Remove from selection

toggle (boolean, (optional)) – Toggle Selection, Toggle the selection

deselect_all (boolean, (optional)) – Deselect On Nothing, Deselect all when nothing under the cursor

select_passthrough (boolean, (optional)) – Only Select Unselected, Ignore the select action when the element is already selected

location (int array of 2 items in [-inf, inf], (optional)) – Location, Mouse location

socket_select (boolean, (optional)) – Socket Select

clear_viewer (boolean, (optional)) – Clear Viewer, Deactivate geometry nodes viewer when clicking in empty space

bpy.ops.node.select_all(*, action='TOGGLE')

(De)select all nodes

PARAMETERS:

action (enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)) –

Action, Selection action to execute

TOGGLE Toggle – Toggle selection for all elements.

SELECT Select – Select all elements.

DESELECT Deselect – Deselect all elements.

INVERT Invert – Invert selection of all elements.

bpy.ops.node.select_box(*, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET')

Use box selection to select nodes

PARAMETERS:

tweak (boolean, (optional)) – Tweak, Only activate when mouse is not over a node (useful for tweak gesture)

xmin (int in [-inf, inf], (optional)) – X Min

xmax (int in [-inf, inf], (optional)) – X Max

ymin (int in [-inf, inf], (optional)) – Y Min

ymax (int in [-inf, inf], (optional)) – Y Max

wait_for_input (boolean, (optional)) – Wait for Input

mode (enum in ['SET', 'ADD', 'SUB'], (optional)) –

Mode

SET Set – Set a new selection.

ADD Extend – Extend existing selection.

SUB Subtract – Subtract existing selection.

bpy.ops.node.select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET')

Use circle selection to select nodes

PARAMETERS:

x (int in [-inf, inf], (optional)) – X

y (int in [-inf, inf], (optional)) – Y

radius (int in [1, inf], (optional)) – Radius

wait_for_input (boolean, (optional)) – Wait for Input

mode (enum in ['SET', 'ADD', 'SUB'], (optional)) –

Mode

SET Set – Set a new selection.

ADD Extend – Extend existing selection.

SUB Subtract – Subtract existing selection.

bpy.ops.node.select_grouped(*, extend=False, type='TYPE')

Select nodes with similar properties

PARAMETERS:

extend (boolean, (optional)) – Extend, Extend selection instead of deselecting everything first

type (enum in ['TYPE', 'COLOR', 'PREFIX', 'SUFFIX'], (optional)) – Type

bpy.ops.node.select_lasso(*, tweak=False, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

Select nodes using lasso selection

PARAMETERS:

tweak (boolean, (optional)) – Tweak, Only activate when mouse is not over a node (useful for tweak gesture)

path (bpy_prop_collection of OperatorMousePath, (optional)) – Path

use_smooth_stroke (boolean, (optional)) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

smooth_stroke_factor (float in [0.5, 0.99], (optional)) – Smooth Stroke Factor, Higher values gives a smoother stroke

smooth_stroke_radius (int in [10, 200], (optional)) – Smooth Stroke Radius, Minimum distance from last point before selection continues

mode (enum in ['SET', 'ADD', 'SUB'], (optional)) –

Mode

SET Set – Set a new selection.

ADD Extend – Extend existing selection.

SUB Subtract – Subtract existing selection.

bpy.ops.node.select_link_viewer(*, NODE_OT_select=None, NODE_OT_link_viewer=None)

Select node and link it to a viewer node

PARAMETERS:

NODE_OT_select (NODE_OT_select, (optional)) – Select, Select the node under the cursor

NODE_OT_link_viewer (NODE_OT_link_viewer, (optional)) – Link to Viewer Node, Link to viewer node

bpy.ops.node.select_linked_from()

Select nodes linked from the selected ones

bpy.ops.node.select_linked_to()

Select nodes linked to the selected ones

bpy.ops.node.select_same_type_step(*, prev=False)

Activate and view same node type, step by step

PARAMETERS:

prev (boolean, (optional)) – Previous

bpy.ops.node.separate_bundle_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.separate_bundle_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.separate_bundle_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.shader_script_update()

Update shader script node with new sockets and options from the script

bpy.ops.node.simulation_zone_item_add(*, node_identifier=0)

Add item below active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.simulation_zone_item_move(*, direction='UP', node_identifier=0)

Move active item

PARAMETERS:

direction (enum in ['UP', 'DOWN'], (optional)) – Direction, Move direction

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.simulation_zone_item_remove(*, node_identifier=0)

Remove active item

PARAMETERS:

node_identifier (int in [0, inf], (optional)) – Node Identifier, Optional identifier of the node to operate on

bpy.ops.node.sockets_sync(*, node_name='')

Update sockets to match what is actually used

PARAMETERS:

node_name (string, (optional, never None)) – Node Name

bpy.ops.node.swap_empty_group(*, settings=None)

Replace active node with an empty group

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

FILE:

startup/bl_operators/node.py:570

bpy.ops.node.swap_group_asset(*, asset_library_type='LOCAL', asset_library_identifier='', relative_asset_identifier='')

Swap selected nodes with the specified node group asset

PARAMETERS:

asset_library_type (enum in Asset Library Type Items, (optional)) – Asset Library Type

asset_library_identifier (string, (optional, never None)) – Asset Library Identifier

relative_asset_identifier (string, (optional, never None)) – Relative Asset Identifier

bpy.ops.node.swap_node(*, settings=None, type='', visible_output='')

Replace the selected nodes with the specified type

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

type (string, (optional, never None)) – Node Type, Node type

visible_output (string, (optional, never None)) – Output Name, If provided, all outputs that are named differently will be hidden

FILE:

startup/bl_operators/node.py:464

bpy.ops.node.swap_zone(*, settings=None, offset=(150.0, 0.0), input_node_type='', output_node_type='', add_default_geometry_link=False)

Undocumented, consider contributing.

PARAMETERS:

settings (bpy_prop_collection of NodeSetting, (optional)) – Settings, Settings to be applied on the newly created node

offset (float array of 2 items in [-inf, inf], (optional)) – Offset, Offset of nodes from the cursor when added

input_node_type (string, (optional, never None)) – Input Node, Specifies the input node used by the created zone

output_node_type (string, (optional, never None)) – Output Node, Specifies the output node used by the created zone

add_default_geometry_link (boolean, (optional)) – Add Geometry Link, When enabled, create a link between geometry sockets in this zone

FILE:

startup/bl_operators/node.py:720

bpy.ops.node.test_inlining_shader_nodes()

Create a new inlined shader node tree as is consumed by renderers

bpy.ops.node.toggle_viewer()

Toggle selected viewer node in compositor and geometry nodes

bpy.ops.node.translate_attach(*, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

Move nodes and attach to frame

PARAMETERS:

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

NODE_OT_attach (NODE_OT_attach, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.translate_attach_remove_on_cancel(*, TRANSFORM_OT_translate=None, NODE_OT_attach=None)

Move nodes and attach to frame

PARAMETERS:

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

NODE_OT_attach (NODE_OT_attach, (optional)) – Attach Nodes, Attach active node to a frame

bpy.ops.node.tree_path_parent(*, parent_tree_index=0)

Go to parent node tree

PARAMETERS:

parent_tree_index (int in [-inf, inf], (optional)) – Parent Index, Parent index in context path

FILE:

startup/bl_operators/node.py:892

bpy.ops.node.view_all()

Resize view so you can see all nodes

bpy.ops.node.view_selected()

Resize view so you can see selected nodes

bpy.ops.node.viewer_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

Set the boundaries for viewer operations

PARAMETERS:

xmin (int in [-inf, inf], (optional)) – X Min

xmax (int in [-inf, inf], (optional)) – X Max

ymin (int in [-inf, inf], (optional)) – Y Min

ymax (int in [-inf, inf], (optional)) – Y Max

wait_for_input (boolean, (optional)) – Wait for Input

bpy.ops.node.viewer_shortcut_get(*, viewer_index=0)

Toggle a specific viewer node using 1,2,..,9 keys

PARAMETERS:

viewer_index (int in [-inf, inf], (optional)) – Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..

FILE:

startup/bl_operators/node.py:1280

bpy.ops.node.viewer_shortcut_set(*, viewer_index=0)

Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9

PARAMETERS:

viewer_index (int in [-inf, inf], (optional)) – Viewer Index, Index corresponding to the shortcut, e.g. number key 1 corresponds to index 1 etc..

FILE:

startup/bl_operators/node.py:1220

Next
Object Operators
Previous
Nla Operators
Copyright © Blender Authors
Made with Furo
Report issue on this page
ON THIS PAGE
activate_viewer()
add_closure_zone()
add_collection()
add_color()
add_empty_group()
add_foreach_geometry_element_zone()
add_group()
add_group_asset()
add_group_input_node()
add_image()
add_import_node()
add_mask()
add_material()
add_node()
add_object()
add_repeat_zone()
add_reroute()
add_simulation_zone()
add_zone()
attach()
backimage_fit()
backimage_move()
backimage_sample()
backimage_zoom()
bake_node_item_add()
bake_node_item_move()
bake_node_item_remove()
capture_attribute_item_add()
capture_attribute_item_move()
capture_attribute_item_remove()
clear_viewer_border()
clipboard_copy()
clipboard_paste()
closure_input_item_add()
closure_input_item_move()
closure_input_item_remove()
closure_output_item_add()
closure_output_item_move()
closure_output_item_remove()
collapse_hide_unused_toggle()
combine_bundle_item_add()
combine_bundle_item_move()
combine_bundle_item_remove()
connect_to_output()
cryptomatte_layer_add()
cryptomatte_layer_remove()
deactivate_viewer()
default_group_width_set()
delete()
delete_reconnect()
detach()
detach_translate_attach()
duplicate()
duplicate_compositing_node_group()
duplicate_move()
duplicate_move_keep_inputs()
duplicate_move_linked()
enum_definition_item_add()
enum_definition_item_move()
enum_definition_item_remove()
evaluate_closure_input_item_add()
evaluate_closure_input_item_move()
evaluate_closure_input_item_remove()
evaluate_closure_output_item_add()
evaluate_closure_output_item_move()
evaluate_closure_output_item_remove()
field_to_grid_item_add()
field_to_grid_item_move()
field_to_grid_item_remove()
file_output_item_add()
file_output_item_move()
file_output_item_remove()
find_node()
foreach_geometry_element_zone_generation_item_add()
foreach_geometry_element_zone_generation_item_move()
foreach_geometry_element_zone_generation_item_remove()
foreach_geometry_element_zone_input_item_add()
foreach_geometry_element_zone_input_item_move()
foreach_geometry_element_zone_input_item_remove()
foreach_geometry_element_zone_main_item_add()
foreach_geometry_element_zone_main_item_move()
foreach_geometry_element_zone_main_item_remove()
format_string_item_add()
format_string_item_move()
format_string_item_remove()
geometry_nodes_viewer_item_add()
geometry_nodes_viewer_item_move()
geometry_nodes_viewer_item_remove()
gltf_settings_node_operator()
group_edit()
group_enter_exit()
group_insert()
group_make()
group_separate()
group_ungroup()
hide_socket_toggle()
hide_toggle()
index_switch_item_add()
index_switch_item_remove()
insert_offset()
interface_item_duplicate()
interface_item_make_panel_toggle()
interface_item_new()
interface_item_new_panel_toggle()
interface_item_remove()
interface_item_unlink_panel_toggle()
join()
join_named()
join_nodes()
link()
link_make()
link_viewer()
links_cut()
links_detach()
links_mute()
move_detach_links()
move_detach_links_release()
mute_toggle()
new_compositing_node_group()
new_compositor_sequencer_node_group()
new_geometry_node_group_assign()
new_geometry_node_group_tool()
new_geometry_nodes_modifier()
new_node_tree()
node_color_preset_add()
node_copy_color()
options_toggle()
parent_set()
preview_toggle()
read_viewlayers()
render_changed()
repeat_zone_item_add()
repeat_zone_item_move()
repeat_zone_item_remove()
resize()
select()
select_all()
select_box()
select_circle()
select_grouped()
select_lasso()
select_link_viewer()
select_linked_from()
select_linked_to()
select_same_type_step()
separate_bundle_item_add()
separate_bundle_item_move()
separate_bundle_item_remove()
shader_script_update()
simulation_zone_item_add()
simulation_zone_item_move()
simulation_zone_item_remove()
sockets_sync()
swap_empty_group()
swap_group_asset()
swap_node()
swap_zone()
test_inlining_shader_nodes()
toggle_viewer()
translate_attach()
translate_attach_remove_on_cancel()
tree_path_parent()
view_all()
view_selected()
viewer_border()
viewer_shortcut_get()
viewer_shortcut_set()
