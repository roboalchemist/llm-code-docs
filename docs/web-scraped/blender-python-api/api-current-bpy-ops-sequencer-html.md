# Source: https://docs.blender.org/api/current/bpy.ops.sequencer.html

Title: Sequencer Operators - Blender Python API

URL Source: https://docs.blender.org/api/current/bpy.ops.sequencer.html

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
Sequencer Operators
bpy.ops.sequencer.add_scene_strip_from_scene_asset(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, asset_library_type='LOCAL', asset_library_identifier='', relative_asset_identifier='')

Add a strip using a duplicate of this scene asset as the source

PARAMETERS:

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

asset_library_type (enum in Asset Library Type Items, (optional)) – Asset Library Type

asset_library_identifier (string, (optional, never None)) – Asset Library Identifier

relative_asset_identifier (string, (optional, never None)) – Relative Asset Identifier

bpy.ops.sequencer.change_effect_type(*, type='CROSS')

Replace effect strip with another that takes the same number of inputs

PARAMETERS:

type (enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)) –

Type, Strip effect type

CROSS Crossfade – Fade out of one video, fading into another.

ADD Add – Add together color channels from two videos.

SUBTRACT Subtract – Subtract one strip’s color from another.

ALPHA_OVER Alpha Over – Blend alpha on top of another video.

ALPHA_UNDER Alpha Under – Blend alpha below another video.

GAMMA_CROSS Gamma Crossfade – Crossfade with color correction.

MULTIPLY Multiply – Multiply color channels from two videos.

WIPE Wipe – Sweep a transition line across the frame.

GLOW Glow – Add blur and brightness to light areas.

COLOR Color – Add a simple color strip.

SPEED Speed – Timewarp video strips, modifying playback speed.

MULTICAM Multicam Selector – Control active camera angles.

ADJUSTMENT Adjustment Layer – Apply nondestructive effects.

GAUSSIAN_BLUR Gaussian Blur – Soften details along axes.

TEXT Text – Add a simple text strip.

COLORMIX Color Mix – Combine two strips using blend modes.

bpy.ops.sequencer.change_path(*, filepath='', directory='', files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_placeholders=False)

Undocumented, consider contributing.

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

display_type (enum in ['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL'], (optional)) –

Display Type

DEFAULT Default – Automatically determine display type for files.

LIST_VERTICAL Short List – Display files as short list.

LIST_HORIZONTAL Long List – Display files as a detailed list.

THUMBNAIL Thumbnails – Display files as thumbnails.

sort_method (enum in [], (optional)) – File sorting mode

use_placeholders (boolean, (optional)) – Use Placeholders, Use placeholders for missing frames of the strip

bpy.ops.sequencer.change_scene(*, scene='')

Change Scene assigned to Strip

PARAMETERS:

scene (enum in [], (optional)) – Scene

bpy.ops.sequencer.connect(*, toggle=True)

Link selected strips together for simplified group selection

PARAMETERS:

toggle (boolean, (optional)) – Toggle, Toggle strip connections

bpy.ops.sequencer.copy()

Copy the selected strips to the internal clipboard

bpy.ops.sequencer.crossfade_sounds()

Do cross-fading volume animation of two selected sound strips

FILE:

startup/bl_operators/sequencer.py:43

bpy.ops.sequencer.cursor_set(*, location=(0.0, 0.0))

Set 2D cursor location

PARAMETERS:

location (mathutils.Vector of 2 items in [-inf, inf], (optional)) – Location, Cursor location in normalized preview coordinates

bpy.ops.sequencer.deinterlace_selected_movies()

Deinterlace all selected movie sources

FILE:

startup/bl_operators/sequencer.py:134

bpy.ops.sequencer.delete(*, delete_data=False)

Delete selected strips from the sequencer

PARAMETERS:

delete_data (boolean, (optional)) – Delete Data, After removing the Strip, delete the associated data also

bpy.ops.sequencer.disconnect()

Unlink selected strips so that they can be selected individually

bpy.ops.sequencer.duplicate(*, linked=False)

Duplicate the selected strips

PARAMETERS:

linked (boolean, (optional)) – Linked, Duplicate strip but not strip data, linking to the original data

bpy.ops.sequencer.duplicate_move(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None)

Duplicate selected strips and move them

PARAMETERS:

SEQUENCER_OT_duplicate (SEQUENCER_OT_duplicate, (optional)) – Duplicate Strips, Duplicate the selected strips

TRANSFORM_OT_seq_slide (TRANSFORM_OT_seq_slide, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.duplicate_move_linked(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None)

Duplicate selected strips, but not their data, and move them

PARAMETERS:

SEQUENCER_OT_duplicate (SEQUENCER_OT_duplicate, (optional)) – Duplicate Strips, Duplicate the selected strips

TRANSFORM_OT_seq_slide (TRANSFORM_OT_seq_slide, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.effect_strip_add(*, type='CROSS', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, color=(0.0, 0.0, 0.0))

Add an effect to the sequencer, most are applied on top of existing strips

PARAMETERS:

type (enum in ['CROSS', 'ADD', 'SUBTRACT', 'ALPHA_OVER', 'ALPHA_UNDER', 'GAMMA_CROSS', 'MULTIPLY', 'WIPE', 'GLOW', 'COLOR', 'SPEED', 'MULTICAM', 'ADJUSTMENT', 'GAUSSIAN_BLUR', 'TEXT', 'COLORMIX'], (optional)) –

Type, Sequencer effect type

CROSS Crossfade – Fade out of one video, fading into another.

ADD Add – Add together color channels from two videos.

SUBTRACT Subtract – Subtract one strip’s color from another.

ALPHA_OVER Alpha Over – Blend alpha on top of another video.

ALPHA_UNDER Alpha Under – Blend alpha below another video.

GAMMA_CROSS Gamma Crossfade – Crossfade with color correction.

MULTIPLY Multiply – Multiply color channels from two videos.

WIPE Wipe – Sweep a transition line across the frame.

GLOW Glow – Add blur and brightness to light areas.

COLOR Color – Add a simple color strip.

SPEED Speed – Timewarp video strips, modifying playback speed.

MULTICAM Multicam Selector – Control active camera angles.

ADJUSTMENT Adjustment Layer – Apply nondestructive effects.

GAUSSIAN_BLUR Gaussian Blur – Soften details along axes.

TEXT Text – Add a simple text strip.

COLORMIX Color Mix – Combine two strips using blend modes.

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

length (int in [-inf, inf], (optional)) – Length, Length of the strip in frames, or the length of each strip if multiple are added

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

color (mathutils.Color of 3 items in [0, 1], (optional)) – Color, Initialize the strip with this color

bpy.ops.sequencer.enable_proxies(*, proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=False)

Enable selected proxies on all selected Movie and Image strips

PARAMETERS:

proxy_25 (boolean, (optional)) – 25%

proxy_50 (boolean, (optional)) – 50%

proxy_75 (boolean, (optional)) – 75%

proxy_100 (boolean, (optional)) – 100%

overwrite (boolean, (optional)) – Overwrite

bpy.ops.sequencer.export_subtitles(*, filepath='', hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='')

Export .srt file containing text strips

PARAMETERS:

filepath (string, (optional, never None)) – File Path, Path to file

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

display_type (enum in ['DEFAULT', 'LIST_VERTICAL', 'LIST_HORIZONTAL', 'THUMBNAIL'], (optional)) –

Display Type

DEFAULT Default – Automatically determine display type for files.

LIST_VERTICAL Short List – Display files as short list.

LIST_HORIZONTAL Long List – Display files as a detailed list.

THUMBNAIL Thumbnails – Display files as thumbnails.

sort_method (enum in [], (optional)) – File sorting mode

bpy.ops.sequencer.fades_add(*, duration_seconds=1.0, type='IN_OUT')

Adds or updates a fade animation for either visual or audio strips

PARAMETERS:

duration_seconds (float in [0.01, inf], (optional)) – Fade Duration, Duration of the fade in seconds

type (enum in ['IN_OUT', 'IN', 'OUT', 'CURSOR_FROM', 'CURSOR_TO'], (optional)) –

Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out

IN_OUT Fade In and Out – Fade selected strips in and out.

IN Fade In – Fade in selected strips.

OUT Fade Out – Fade out selected strips.

CURSOR_FROM From Current Frame – Fade from the time cursor to the end of overlapping strips.

CURSOR_TO To Current Frame – Fade from the start of strips under the time cursor to the current frame.

FILE:

startup/bl_operators/sequencer.py:221

bpy.ops.sequencer.fades_clear()

Removes fade animation from selected strips

FILE:

startup/bl_operators/sequencer.py:157

bpy.ops.sequencer.gap_insert(*, frames=10)

Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

PARAMETERS:

frames (int in [0, inf], (optional)) – Frames, Frames to insert after current strip

bpy.ops.sequencer.gap_remove(*, all=False)

Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

PARAMETERS:

all (boolean, (optional)) – All Gaps, Do all gaps to right of current frame

bpy.ops.sequencer.image_strip_add(*, directory='', files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, length=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, image_import_type='DETECT', use_sequence_detection=True, use_placeholders=False)

Add an image or image sequence to the sequencer

PARAMETERS:

directory (string, (optional, never None)) – Directory, Directory of the file

files (bpy_prop_collection of OperatorFileListElement, (optional)) – Files

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

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

length (int in [-inf, inf], (optional)) – Length, Length of the strip in frames, or the length of each strip if multiple are added

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

fit_method (enum in Strip Scale Method Items, (optional)) – Fit Method, Mode for fitting the image to the canvas

set_view_transform (boolean, (optional)) – Set View Transform, Set appropriate view transform based on media color space

image_import_type (enum in ['DETECT', 'SEQUENCE', 'INDIVIDUAL'], (optional)) –

Import As, Mode for importing selected images

DETECT Auto Detect – Add images as individual strips, unless their filenames match Blender’s numbered sequence pattern, in which case they are grouped into a single image sequence.

SEQUENCE Image Sequence – Import all selected images as a single image sequence. The sequence of images does not have to match Blender’s numbered sequence pattern, so placeholders cannot be inferred.

INDIVIDUAL Individual Images – Add each selected image as an individual strip.

use_sequence_detection (boolean, (optional)) – Detect Sequences, Automatically detect animated sequences in selected images (based on file names)

use_placeholders (boolean, (optional)) – Use Placeholders, Reserve placeholder frames for missing frames of the image sequence

bpy.ops.sequencer.images_separate(*, length=1)

On image sequence strips, it returns a strip for each image

PARAMETERS:

length (int in [1, inf], (optional)) – Length, Length of each frame

bpy.ops.sequencer.lock()

Lock strips so they cannot be transformed

bpy.ops.sequencer.mask_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, mask='')

Add a mask strip to the sequencer

PARAMETERS:

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

mask (enum in [], (optional)) – Mask

bpy.ops.sequencer.meta_make()

Group selected strips into a meta-strip

bpy.ops.sequencer.meta_separate()

Put the contents of a meta-strip back in the sequencer

bpy.ops.sequencer.meta_toggle()

Toggle a meta-strip (to edit enclosed strips)

bpy.ops.sequencer.movie_strip_add(*, filepath='', directory='', files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, fit_method='FIT', set_view_transform=True, adjust_playback_rate=True, sound=True, use_framerate=True)

Add a movie strip to the sequencer

PARAMETERS:

filepath (string, (optional, never None)) – File Path, Path to file

directory (string, (optional, never None)) – Directory, Directory of the file

files (bpy_prop_collection of OperatorFileListElement, (optional)) – Files

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

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

fit_method (enum in Strip Scale Method Items, (optional)) – Fit Method, Mode for fitting the image to the canvas

set_view_transform (boolean, (optional)) – Set View Transform, Set appropriate view transform based on media color space

adjust_playback_rate (boolean, (optional)) – Adjust Playback Rate, Play at normal speed regardless of scene FPS

sound (boolean, (optional)) – Sound, Load sound with the movie

use_framerate (boolean, (optional)) – Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie

bpy.ops.sequencer.movieclip_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, clip='')

Add a movieclip strip to the sequencer

PARAMETERS:

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

clip (enum in [], (optional)) – Clip

bpy.ops.sequencer.mute(*, unselected=False)

Mute (un)selected strips

PARAMETERS:

unselected (boolean, (optional)) – Unselected, Mute unselected rather than selected strips

bpy.ops.sequencer.offset_clear()

Clear strip in/out offsets from the start and end of content

bpy.ops.sequencer.paste(*, keep_offset=False, x=0, y=0)

Paste strips from the internal clipboard

PARAMETERS:

keep_offset (boolean, (optional)) – Keep Offset, Keep strip offset relative to the current frame when pasting

x (int in [-inf, inf], (optional)) – X

y (int in [-inf, inf], (optional)) – Y

bpy.ops.sequencer.preview_duplicate_move(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_translate=None)

Duplicate selected strips and move them

PARAMETERS:

SEQUENCER_OT_duplicate (SEQUENCER_OT_duplicate, (optional)) – Duplicate Strips, Duplicate the selected strips

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

bpy.ops.sequencer.preview_duplicate_move_linked(*, SEQUENCER_OT_duplicate=None, TRANSFORM_OT_translate=None)

Duplicate selected strips, but not their data, and move them

PARAMETERS:

SEQUENCER_OT_duplicate (SEQUENCER_OT_duplicate, (optional)) – Duplicate Strips, Duplicate the selected strips

TRANSFORM_OT_translate (TRANSFORM_OT_translate, (optional)) – Move, Move selected items

bpy.ops.sequencer.reassign_inputs()

Reassign the inputs for the effect strip

bpy.ops.sequencer.rebuild_proxy()

Rebuild all selected proxies and timecode indices

bpy.ops.sequencer.refresh_all()

Refresh the sequencer editor

bpy.ops.sequencer.reload(*, adjust_length=False)

Reload strips in the sequencer

PARAMETERS:

adjust_length (boolean, (optional)) – Adjust Length, Adjust length of strips to their data length

bpy.ops.sequencer.rename_channel()

Undocumented, consider contributing.

bpy.ops.sequencer.rendersize()

Set render size and aspect from active strip

bpy.ops.sequencer.retiming_add_freeze_frame_slide(*, SEQUENCER_OT_retiming_freeze_frame_add=None, TRANSFORM_OT_seq_slide=None)

Add freeze frame and move it

PARAMETERS:

SEQUENCER_OT_retiming_freeze_frame_add (SEQUENCER_OT_retiming_freeze_frame_add, (optional)) – Add Freeze Frame, Add freeze frame

TRANSFORM_OT_seq_slide (TRANSFORM_OT_seq_slide, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.retiming_add_transition_slide(*, SEQUENCER_OT_retiming_transition_add=None, TRANSFORM_OT_seq_slide=None)

Add smooth transition between 2 retimed segments and change its duration

PARAMETERS:

SEQUENCER_OT_retiming_transition_add (SEQUENCER_OT_retiming_transition_add, (optional)) – Add Speed Transition, Add smooth transition between 2 retimed segments

TRANSFORM_OT_seq_slide (TRANSFORM_OT_seq_slide, (optional)) – Sequence Slide, Slide a sequence strip in time

bpy.ops.sequencer.retiming_freeze_frame_add(*, duration=0)

Add freeze frame

PARAMETERS:

duration (int in [0, inf], (optional)) – Duration, Duration of freeze frame segment

bpy.ops.sequencer.retiming_key_add(*, timeline_frame=0)

Add retiming Key

PARAMETERS:

timeline_frame (int in [0, inf], (optional)) – Timeline Frame, Frame where key will be added

bpy.ops.sequencer.retiming_key_delete()

Delete selected retiming keys from the sequencer

bpy.ops.sequencer.retiming_reset()

Reset strip retiming

bpy.ops.sequencer.retiming_segment_speed_set(*, speed=100.0, keep_retiming=True)

Set speed of retimed segment

PARAMETERS:

speed (float in [0.001, inf], (optional)) – Speed, New speed of retimed segment

keep_retiming (boolean, (optional)) – Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead

bpy.ops.sequencer.retiming_show()

Show retiming keys in selected strips

bpy.ops.sequencer.retiming_transition_add(*, duration=0)

Add smooth transition between 2 retimed segments

PARAMETERS:

duration (int in [0, inf], (optional)) – Duration, Duration of freeze frame segment

bpy.ops.sequencer.sample(*, size=1)

Use mouse to sample color in current frame

PARAMETERS:

size (int in [1, 128], (optional)) – Sample Size

bpy.ops.sequencer.scene_frame_range_update()

Update frame range of scene strip

bpy.ops.sequencer.scene_strip_add(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, scene='')

Add a strip re-using this scene as the source

PARAMETERS:

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

scene (enum in [], (optional)) – Scene

bpy.ops.sequencer.scene_strip_add_new(*, move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, type='NEW')

Add a strip using a new scene as the source

PARAMETERS:

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

type (enum in ['NEW', 'EMPTY', 'LINK_COPY', 'FULL_COPY'], (optional)) –

Type

NEW New – Add new Strip with a new empty Scene with default settings.

EMPTY Copy Settings – Add a new Strip, with an empty scene, and copy settings from the current scene.

LINK_COPY Linked Copy – Add a Strip and link in the collections from the current scene (shallow copy).

FULL_COPY Full Copy – Add a Strip and make a full copy of the current scene.

bpy.ops.sequencer.select(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False, ignore_connections=False)

Select a strip (last selected becomes the “active strip”)

PARAMETERS:

wait_to_deselect_others (boolean, (optional)) – Wait to Deselect Others

use_select_on_click (boolean, (optional)) – Act on Click, Instead of selecting on mouse press, wait to see if there’s drag event. Otherwise select on mouse release

mouse_x (int in [-inf, inf], (optional)) – Mouse X

mouse_y (int in [-inf, inf], (optional)) – Mouse Y

extend (boolean, (optional)) – Extend, Extend selection instead of deselecting everything first

deselect (boolean, (optional)) – Deselect, Remove from selection

toggle (boolean, (optional)) – Toggle Selection, Toggle the selection

deselect_all (boolean, (optional)) – Deselect On Nothing, Deselect all when nothing under the cursor

select_passthrough (boolean, (optional)) – Only Select Unselected, Ignore the select action when the element is already selected

center (boolean, (optional)) – Center, Use the object center when selecting, in edit mode used to extend object selection

linked_handle (boolean, (optional)) – Linked Handle, Select handles next to the active strip

linked_time (boolean, (optional)) – Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode

side_of_frame (boolean, (optional)) – Side of Frame, Select all strips on same side of the current frame as the mouse cursor

ignore_connections (boolean, (optional)) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_all(*, action='TOGGLE')

Select or deselect all strips

PARAMETERS:

action (enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)) –

Action, Selection action to execute

TOGGLE Toggle – Toggle selection for all elements.

SELECT Select – Select all elements.

DESELECT Deselect – Deselect all elements.

INVERT Invert – Invert selection of all elements.

bpy.ops.sequencer.select_box(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False, ignore_connections=False)

Select strips using box selection

PARAMETERS:

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

tweak (boolean, (optional)) – Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip

include_handles (boolean, (optional)) – Select Handles, Select the strips and their handles

ignore_connections (boolean, (optional)) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_circle(*, x=0, y=0, radius=25, wait_for_input=True, mode='SET', ignore_connections=False)

Select strips using circle selection

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

ignore_connections (boolean, (optional)) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_grouped(*, type='TYPE', extend=False, use_active_channel=False)

Select all strips grouped by various properties

PARAMETERS:

type (enum in ['TYPE', 'TYPE_BASIC', 'TYPE_EFFECT', 'DATA', 'EFFECT', 'EFFECT_LINK', 'OVERLAP'], (optional)) –

Type

TYPE Type – Shared strip type.

TYPE_BASIC Global Type – All strips of same basic type (graphical or sound).

TYPE_EFFECT Effect Type – Shared strip effect type (if active strip is not an effect one, select all non-effect strips).

DATA Data – Shared data (scene, image, sound, etc.).

EFFECT Effect – Shared effects.

EFFECT_LINK Effect/Linked – Other strips affected by the active one (sharing some time, and below or effect-assigned).

OVERLAP Overlap – Overlapping time.

extend (boolean, (optional)) – Extend, Extend selection instead of deselecting everything first

use_active_channel (boolean, (optional)) – Same Channel, Only consider strips on the same channel as the active one

bpy.ops.sequencer.select_handle(*, wait_to_deselect_others=False, use_select_on_click=False, mouse_x=0, mouse_y=0, ignore_connections=False)

Select strip handle

PARAMETERS:

wait_to_deselect_others (boolean, (optional)) – Wait to Deselect Others

use_select_on_click (boolean, (optional)) – Act on Click, Instead of selecting on mouse press, wait to see if there’s drag event. Otherwise select on mouse release

mouse_x (int in [-inf, inf], (optional)) – Mouse X

mouse_y (int in [-inf, inf], (optional)) – Mouse Y

ignore_connections (boolean, (optional)) – Ignore Connections, Select strips individually whether or not they are connected

bpy.ops.sequencer.select_handles(*, side='BOTH')

Select gizmo handles on the sides of the selected strip

PARAMETERS:

side (enum in ['LEFT', 'RIGHT', 'BOTH', 'LEFT_NEIGHBOR', 'RIGHT_NEIGHBOR', 'BOTH_NEIGHBORS'], (optional)) – Side, The side of the handle that is selected

bpy.ops.sequencer.select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

Select strips using lasso selection

PARAMETERS:

path (bpy_prop_collection of OperatorMousePath, (optional)) – Path

use_smooth_stroke (boolean, (optional)) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path

smooth_stroke_factor (float in [0.5, 0.99], (optional)) – Smooth Stroke Factor, Higher values gives a smoother stroke

smooth_stroke_radius (int in [10, 200], (optional)) – Smooth Stroke Radius, Minimum distance from last point before selection continues

mode (enum in ['SET', 'ADD', 'SUB'], (optional)) –

Mode

SET Set – Set a new selection.

ADD Extend – Extend existing selection.

SUB Subtract – Subtract existing selection.

bpy.ops.sequencer.select_less()

Shrink the current selection of adjacent selected strips

bpy.ops.sequencer.select_linked()

Select all strips adjacent to the current selection

bpy.ops.sequencer.select_linked_pick(*, extend=False)

Select a chain of linked strips nearest to the mouse pointer

PARAMETERS:

extend (boolean, (optional)) – Extend, Extend the selection

bpy.ops.sequencer.select_more()

Select more strips adjacent to the current selection

bpy.ops.sequencer.select_side(*, side='BOTH')

Select strips on the nominated side of the selected strips

PARAMETERS:

side (enum in ['MOUSE', 'LEFT', 'RIGHT', 'BOTH', 'NO_CHANGE'], (optional)) – Side, The side to which the selection is applied

bpy.ops.sequencer.select_side_of_frame(*, extend=False, side='LEFT')

Select strips relative to the current frame

PARAMETERS:

extend (boolean, (optional)) – Extend, Extend the selection

side (enum in ['LEFT', 'RIGHT', 'CURRENT'], (optional)) –

Side

LEFT Left – Select to the left of the current frame.

RIGHT Right – Select to the right of the current frame.

CURRENT Current Frame – Select intersecting with the current frame.

bpy.ops.sequencer.set_range_to_strips(*, preview=False)

Set the frame range to the selected strips start and end

PARAMETERS:

preview (boolean, (optional)) – Preview, Set the preview range instead

bpy.ops.sequencer.slip(*, offset=0.0, slip_keyframes=False, use_cursor_position=False, ignore_connections=False)

Slip the contents of selected strips

PARAMETERS:

offset (float in [-inf, inf], (optional)) – Offset, Offset to the data of the strip

slip_keyframes (boolean, (optional)) – Slip Keyframes, Move the keyframes alongside the media

use_cursor_position (boolean, (optional)) – Use Cursor Position, Slip strips under mouse cursor instead of all selected strips

ignore_connections (boolean, (optional)) – Ignore Connections, Do not slip connected strips if using cursor position

bpy.ops.sequencer.snap(*, frame=0)

Frame where selected strips will be snapped

PARAMETERS:

frame (int in [-inf, inf], (optional)) – Frame, Frame where selected strips will be snapped

bpy.ops.sequencer.sound_strip_add(*, filepath='', directory='', files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', move_strips=True, frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, skip_locked_or_muted_channels=True, cache=False, mono=False)

Add a sound strip to the sequencer

PARAMETERS:

filepath (string, (optional, never None)) – File Path, Path to file

directory (string, (optional, never None)) – Directory, Directory of the file

files (bpy_prop_collection of OperatorFileListElement, (optional)) – Files

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

move_strips (boolean, (optional)) – Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline

frame_start (int in [-inf, inf], (optional)) – Start Frame, Start frame of the strip

channel (int in [1, 128], (optional)) – Channel, Channel to place this strip into

replace_sel (boolean, (optional)) – Replace Selection, Deselect previously selected strips after add operation completes

overlap (boolean, (optional)) – Allow Overlap, Don’t correct overlap on new strips

overlap_shuffle_override (boolean, (optional)) – Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips

skip_locked_or_muted_channels (boolean, (optional)) – Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips

cache (boolean, (optional)) – Cache, Cache the sound in memory

mono (boolean, (optional)) – Mono, Merge all the sound’s channels into one

bpy.ops.sequencer.split(*, frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False, ignore_connections=False)

Split the selected strips in two

PARAMETERS:

frame (int in [-inf, inf], (optional)) – Frame, Frame where selected strips will be split

channel (int in [-inf, inf], (optional)) – Channel, Channel in which strip will be cut

type (enum in ['SOFT', 'HARD'], (optional)) – Type, The type of split operation to perform on strips

use_cursor_position (boolean, (optional)) – Use Cursor Position, Split at position of the cursor instead of current frame

side (enum in ['MOUSE', 'LEFT', 'RIGHT', 'BOTH', 'NO_CHANGE'], (optional)) – Side, The side that remains selected after splitting

ignore_selection (boolean, (optional)) – Ignore Selection, Make cut even if strip is not selected preserving selection state after cut

ignore_connections (boolean, (optional)) – Ignore Connections, Don’t propagate split to connected strips

bpy.ops.sequencer.split_multicam(*, camera=1)

Split multicam strip and select camera

PARAMETERS:

camera (int in [1, 32], (optional)) – Camera

FILE:

startup/bl_operators/sequencer.py:101

bpy.ops.sequencer.strip_color_tag_set(*, color='NONE')

Set a color tag for the selected strips

PARAMETERS:

color (enum in Strip Color Items, (optional)) – Color Tag

bpy.ops.sequencer.strip_jump(*, next=True, center=True)

Move frame to previous edit point

PARAMETERS:

next (boolean, (optional)) – Next Strip

center (boolean, (optional)) – Use Strip Center

bpy.ops.sequencer.strip_modifier_add(*, type='')

Add a modifier to the strip

PARAMETERS:

type (enum in [], (optional)) – Type

bpy.ops.sequencer.strip_modifier_copy(*, type='REPLACE')

Copy modifiers of the active strip to all selected strips

PARAMETERS:

type (enum in ['REPLACE', 'APPEND'], (optional)) –

Type

REPLACE Replace – Replace modifiers in destination.

APPEND Append – Append active modifiers to selected strips.

bpy.ops.sequencer.strip_modifier_equalizer_redefine(*, graphs='SIMPLE', name='Name')

Redefine equalizer graphs

PARAMETERS:

graphs (enum in ['SIMPLE', 'DOUBLE', 'TRIPLE'], (optional)) –

Graphs, Number of graphs

SIMPLE Unique – One unique graphical definition.

DOUBLE Double – Graphical definition in 2 sections.

TRIPLE Triplet – Graphical definition in 3 sections.

name (string, (optional, never None)) – Name, Name of modifier to redefine

bpy.ops.sequencer.strip_modifier_move(*, name='Name', direction='UP')

Move modifier up and down in the stack

PARAMETERS:

name (string, (optional, never None)) – Name, Name of modifier to remove

direction (enum in ['UP', 'DOWN'], (optional)) –

Type

UP Up – Move modifier up in the stack.

DOWN Down – Move modifier down in the stack.

bpy.ops.sequencer.strip_modifier_move_to_index(*, modifier='', index=0)

Change the strip modifier’s index in the stack so it evaluates after the set number of others

PARAMETERS:

modifier (string, (optional, never None)) – Modifier, Name of the modifier to edit

index (int in [0, inf], (optional)) – Index, The index to move the modifier to

bpy.ops.sequencer.strip_modifier_remove(*, name='Name')

Remove a modifier from the strip

PARAMETERS:

name (string, (optional, never None)) – Name, Name of modifier to remove

bpy.ops.sequencer.strip_modifier_set_active(*, modifier='')

Activate the strip modifier to use as the context

PARAMETERS:

modifier (string, (optional, never None)) – Modifier, Name of the strip modifier to edit

bpy.ops.sequencer.strip_transform_clear(*, property='ALL')

Reset image transformation to default value

PARAMETERS:

property (enum in ['POSITION', 'SCALE', 'ROTATION', 'ALL'], (optional)) –

Property, Strip transform property to be reset

POSITION Position – Reset strip transform location.

SCALE Scale – Reset strip transform scale.

ROTATION Rotation – Reset strip transform rotation.

ALL All – Reset strip transform location, scale and rotation.

bpy.ops.sequencer.strip_transform_fit(*, fit_method='FIT')

Undocumented, consider contributing.

PARAMETERS:

fit_method (enum in Strip Scale Method Items, (optional)) – Fit Method, Mode for fitting the image to the canvas

bpy.ops.sequencer.swap(*, side='RIGHT')

Swap active strip with strip to the right or left

PARAMETERS:

side (enum in ['LEFT', 'RIGHT'], (optional)) – Side, Side of the strip to swap

bpy.ops.sequencer.swap_data()

Swap 2 sequencer strips

bpy.ops.sequencer.swap_inputs()

Swap the two inputs of the effect strip

bpy.ops.sequencer.text_cursor_move(*, type='LINE_BEGIN', select_text=False)

Move cursor in text

PARAMETERS:

type (enum in ['LINE_BEGIN', 'LINE_END', 'TEXT_BEGIN', 'TEXT_END', 'PREVIOUS_CHARACTER', 'NEXT_CHARACTER', 'PREVIOUS_WORD', 'NEXT_WORD', 'PREVIOUS_LINE', 'NEXT_LINE'], (optional)) – Type, Where to move cursor to, to make a selection

select_text (boolean, (optional)) – Select Text, Select text while moving cursor

bpy.ops.sequencer.text_cursor_set(*, select_text=False)

Set cursor position in text

PARAMETERS:

select_text (boolean, (optional)) – Select Text, Select text while moving cursor

bpy.ops.sequencer.text_delete(*, type='NEXT_OR_SELECTION')

Delete text at cursor position

PARAMETERS:

type (enum in ['NEXT_OR_SELECTION', 'PREVIOUS_OR_SELECTION'], (optional)) – Type, Which part of the text to delete

bpy.ops.sequencer.text_deselect_all()

Deselect all characters

bpy.ops.sequencer.text_edit_copy()

Copy text to clipboard

bpy.ops.sequencer.text_edit_cut()

Cut text to clipboard

bpy.ops.sequencer.text_edit_mode_toggle()

Toggle text editing

bpy.ops.sequencer.text_edit_paste()

Paste text from clipboard

bpy.ops.sequencer.text_insert(*, string='')

Insert text at cursor position

PARAMETERS:

string (string, (optional, never None)) – String, String to be inserted at cursor position

bpy.ops.sequencer.text_line_break()

Insert line break at cursor position

bpy.ops.sequencer.text_select_all()

Select all characters

bpy.ops.sequencer.unlock()

Unlock strips so they can be transformed

bpy.ops.sequencer.unmute(*, unselected=False)

Unmute (un)selected strips

PARAMETERS:

unselected (boolean, (optional)) – Unselected, Unmute unselected rather than selected strips

bpy.ops.sequencer.view_all()

View all the strips in the sequencer

bpy.ops.sequencer.view_all_preview()

Zoom preview to fit in the area

bpy.ops.sequencer.view_frame()

Move the view to the current frame

bpy.ops.sequencer.view_ghost_border(*, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True)

Set the boundaries of the border used for offset view

PARAMETERS:

xmin (int in [-inf, inf], (optional)) – X Min

xmax (int in [-inf, inf], (optional)) – X Max

ymin (int in [-inf, inf], (optional)) – Y Min

ymax (int in [-inf, inf], (optional)) – Y Max

wait_for_input (boolean, (optional)) – Wait for Input

bpy.ops.sequencer.view_selected()

Zoom the sequencer on the selected strips

bpy.ops.sequencer.view_zoom_ratio(*, ratio=1.0)

Change zoom ratio of sequencer preview

PARAMETERS:

ratio (float in [-inf, inf], (optional)) – Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out

Next
Sound Operators
Previous
Sculpt Curves Operators
Copyright © Blender Authors
Made with Furo
Report issue on this page
ON THIS PAGE
add_scene_strip_from_scene_asset()
change_effect_type()
change_path()
change_scene()
connect()
copy()
crossfade_sounds()
cursor_set()
deinterlace_selected_movies()
delete()
disconnect()
duplicate()
duplicate_move()
duplicate_move_linked()
effect_strip_add()
enable_proxies()
export_subtitles()
fades_add()
fades_clear()
gap_insert()
gap_remove()
image_strip_add()
images_separate()
lock()
mask_strip_add()
meta_make()
meta_separate()
meta_toggle()
movie_strip_add()
movieclip_strip_add()
mute()
offset_clear()
paste()
preview_duplicate_move()
preview_duplicate_move_linked()
reassign_inputs()
rebuild_proxy()
refresh_all()
reload()
rename_channel()
rendersize()
retiming_add_freeze_frame_slide()
retiming_add_transition_slide()
retiming_freeze_frame_add()
retiming_key_add()
retiming_key_delete()
retiming_reset()
retiming_segment_speed_set()
retiming_show()
retiming_transition_add()
sample()
scene_frame_range_update()
scene_strip_add()
scene_strip_add_new()
select()
select_all()
select_box()
select_circle()
select_grouped()
select_handle()
select_handles()
select_lasso()
select_less()
select_linked()
select_linked_pick()
select_more()
select_side()
select_side_of_frame()
set_range_to_strips()
slip()
snap()
sound_strip_add()
split()
split_multicam()
strip_color_tag_set()
strip_jump()
strip_modifier_add()
strip_modifier_copy()
strip_modifier_equalizer_redefine()
strip_modifier_move()
strip_modifier_move_to_index()
strip_modifier_remove()
strip_modifier_set_active()
strip_transform_clear()
strip_transform_fit()
swap()
swap_data()
swap_inputs()
text_cursor_move()
text_cursor_set()
text_delete()
text_deselect_all()
text_edit_copy()
text_edit_cut()
text_edit_mode_toggle()
text_edit_paste()
text_insert()
text_line_break()
text_select_all()
unlock()
unmute()
view_all()
view_all_preview()
view_frame()
view_ghost_border()
view_selected()
view_zoom_ratio()
