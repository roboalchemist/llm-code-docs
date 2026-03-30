:::::: {#header}

# GerbView

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}

::: {#toctitle}

Table of Contents
:::

- [Introduction to GerbView](#_introduction_to_gerbview)

- [Interface](#_interface)

  - [Main window](#_main_window)

  - [Top toolbar](#_top_toolbar)

  - [Left toolbar](#_left_toolbar)

  - [Layers Manager](#_layers_manager)

- [Commands in menu bar](#_commands_in_menu_bar)

  - [File menu](#_file_menu)

  - [Preferences menu](#_preferences_menu)

  - [Miscellaneous menu](#_miscellaneous_menu)

- [Display modes](#_display_modes)

  - [Raw mode](#_raw_mode)

  - [Stacked mode](#_stacked_mode)

  - [Transparency mode](#_transparency_mode)

  - [Layer occlusion](#_layer_occlusion)

- [Moving items](#_moving_items)

- [Printing](#_printing)
::::
::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::: {#preamble}

::::::::::::::: sectionbody
::: paragraph
*Reference manual*
:::

::: {#copyright .paragraph}

**Copyright**
:::

::: paragraph
This document is Copyright © 2010-2018 by it's contributors as listed
below. You may distribute it and/or modify it under the terms of either
the GNU General Public License
([https://www.gnu.org/licenses/gpl.html](https://www.gnu.org/licenses/gpl.html){.bare}),
version 3 or later, or the Creative Commons Attribution License
([https://creativecommons.org/licenses/by/3.0/](https://creativecommons.org/licenses/by/3.0/){.bare}),
version 3.0 or later.
:::

::: paragraph
All trademarks within this guide belong to their legitimate owners.
:::

::: {#contributors .paragraph}

**Contributors**
:::

::: paragraph
The KiCad Team.
:::

::: {#feedback .paragraph}

**Feedback**
:::

::: paragraph
Please direct any bug reports, suggestions or new versions to here:
:::

::: ulist

- About KiCad document:
  [https://github.com/KiCad/kicad-doc/issues](https://github.com/KiCad/kicad-doc/issues){.bare}

- About KiCad software:
  [https://bugs.launchpad.net/kicad](https://bugs.launchpad.net/kicad){.bare}

- About KiCad software i18n:
  [https://github.com/KiCad/kicad-i18n/issues](https://github.com/KiCad/kicad-i18n/issues){.bare}
:::

::: {#publication_date_and_software_version .paragraph}

**Publication date and software version**
:::

::: paragraph
Published on February 24, 2018.
:::

::: {style="page-break-after: always;"}
:::
:::::::::::::::
::::::::::::::::

:::::: sect1

## Introduction to GerbView {#_introduction_to_gerbview}

::::: sectionbody
::: paragraph
GerbView is a Gerber file (RS-274X format) and Excellon drill file
viewer. Up to 32 files can be displayed at once.
:::

::: paragraph
For more information about the Gerber file format please read [the
Gerber File Format
Specification](http://www.ucamco.com/files/downloads/file/81/the_gerber_file_format_specification.pdf).
Details about drill file format can be found at [the Excellon format
description](http://web.archive.org/web/20071030075236/http://www.excellon.com/manuals/program.htm).
:::
:::::
::::::

::::::::::::::::::::: sect1

## Interface {#_interface}

:::::::::::::::::::: sectionbody
:::::: sect2

### Main window {#_main_window}

:::: imageblock
::: content
![gerbview_main_screen_png](images/gerbview_main_screen.png)
:::
::::

::: {style="page-break-after: always;"}
:::
::::::

:::::: sect2

### Top toolbar {#_top_toolbar}

:::: imageblock
::: content
![gerbview_top_toolbar_png](images/gerbview_top_toolbar.png)
:::
::::

+----------------------------------------------------------------------------+-----------------------------------------+
| [![delete_gerber_png](images/icons/delete_gerber.png)]{.image}             | Clear all layers                        |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![load_gerber_png](images/icons/load_gerber.png)]{.image}                 | Load Gerber files                       |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_drill_file_png](images/icons/gerbview_drill_file.png)]{.image} | Load Excellon drill files               |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![sheetset_png](images/icons/sheetset.png)]{.image}                       | Set page size                           |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![print_button_png](images/icons/print_button.png)]{.image}               | Print                                   |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![zoom_redraw_png](images/icons/zoom_redraw.png)]{.image}                 | Redraw view                             |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![zoom_in_png](images/icons/zoom_in.png)]{.image}                         | Zoom in or out                          |
| [![zoom_out_png](images/icons/zoom_out.png)]{.image}                       |                                         |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![zoom_fit_in_page_png](images/icons/zoom_fit_in_page.png)]{.image}       | Zoom auto (zoom fit)                    |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![zoom_area_png](images/icons/zoom_area.png)]{.image}                     | Zoom to selection                       |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_top_layer_png](images/gerbview_top_layer.png)]{.image}         | Select active layer                     |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_top_info_png](images/gerbview_top_info.png)]{.image}           | Display info about active layer         |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_x2_component_png](images/gerbview_x2_component.png)]{.image}   | Highlight items belonging to selected   |
|                                                                            | component (Gerber X2)                   |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_x2_net_png](images/gerbview_x2_net.png)]{.image}               | Highlight items belonging to selected   |
|                                                                            | net (Gerber X2)                         |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_x2_attributeo_png](images/gerbview_x2_attribute.png)]{.image}  | Highlight items with the selected       |
|                                                                            | attribute (Gerber X2)                   |
+----------------------------------------------------------------------------+-----------------------------------------+
| [![gerbview_top_dcode_png](images/gerbview_top_dcode.png)]{.image}         | Highlight items of selected D Code on   |
|                                                                            | the active layer                        |
+----------------------------------------------------------------------------+-----------------------------------------+

::: {style="page-break-after: always;"}
:::
::::::

:::: sect2

### Left toolbar {#_left_toolbar}

+--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| [![gerbview_left_toolbar_png](images/gerbview_left_toolbar.png)]{.image} | [![cursor_png](images/icons/cursor.png)]{.image}                                                 | Select items                                               |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![measurement_png](images/icons/measurement.png)]{.image}                                       | Measure between two points                                 |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![grid_png](images/icons/grid.png)]{.image}                                                     | Toggle grid visibility                                     |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![polar_coord_png](images/icons/polar_coord.png)]{.image}                                       | Toggle polar coordinates display                           |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![unit_inch_png](images/icons/unit_inch.png)]{.image}                                           | Select inch or millimeter units                            |
|                                                                          | [![unit_mm_png](images/icons/unit_mm.png)]{.image}                                               |                                                            |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![cursor_shape_png](images/icons/cursor_shape.png)]{.image}                                     | Toggle full-screen cursor                                  |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![pad_sketch_png](images/icons/pad_sketch.png)]{.image}                                         | Display flashed items in sketch (outline) mode             |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![track_sketch_png](images/icons/track_sketch.png)]{.image}                                     | Display lines in sketch (outline) mode                     |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![opt_show_polygon_png](images/icons/opt_show_polygon.png)]{.image}                             | Display polygons in sketch (outline) mode                  |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![gerbview_show_negative_objects_png](images/icons/gerbview_show_negative_objects.png)]{.image} | Show negative objects in ghost color                       |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![show_dcodenumber_png](images/icons/show_dcodenumber.png)]{.image}                             | Show/hide D Codes                                          |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![gbr_select_mode2_png](images/icons/gbr_select_mode2.png)]{.image}                             | Display layers in diff(compare) mode                       |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![contrast_mode_png](images/icons/contrast_mode.png)]{.image}                                   | Display current layer in high-contrast mode                |
|                                                                          +--------------------------------------------------------------------------------------------------+------------------------------------------------------------+
|                                                                          | [![layers_manager_png](images/icons/layers_manager.png)]{.image}                                 | Show/hide layer manager                                    |
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------------------------------------------------+

::: {style="page-break-after: always;"}
:::
::::

::::::::: sect2

### Layers Manager {#_layers_manager}

:::: imageblock
::: content
![gerbview_layer_manager_png](images/gerbview_layer_manager.png)
:::
::::

::: paragraph
The Layers Manager controls and displays visibility of all layers. An
arrow indicates the active layer, and each layer can be shown or hidden
with the checkboxes.
:::

::: paragraph
Mouse button assignments:
:::

::: ulist

- Left click: select the active layer

- Right click: show/hide/sort layers options

- Middle click or double click (on color swatch): select the layer color
:::

::: paragraph
The Layers tab allows you to control the visibility and color of all
loaded Gerber and drill layers. The Items tab allows you to control the
color and display of the grid, D Codes, and negative objects.
:::
:::::::::
::::::::::::::::::::
:::::::::::::::::::::

::::::::::::::::::: sect1

## Commands in menu bar {#_commands_in_menu_bar}

:::::::::::::::::: sectionbody
:::::: sect2

### File menu {#_file_menu}

:::: imageblock
::: content
![gerbview_file_menu_png](images/gerbview_file_menu.png)
:::
::::

::: ulist

- **Export to Pcbnew** is a limited capability to export Gerber files
  into Pcbnew. The final result depends on what features of the RS-274X
  format are used in the original Gerber files: rasterized items cannot
  be converted (typically negative objects), flashed items are converted
  to vias, lines are converted to track segments (or graphic lines for
  non-copper layers).
:::
::::::

::::::::: sect2

### Preferences menu {#_preferences_menu}

:::: imageblock
::: content
![gerbview_preferences_menu_png](images/gerbview_preferences_menu.png)
:::
::::

:::::: sect3

#### Toolsets {#_toolsets}

::: paragraph
GerbView now supports the modern graphics toolset that is available in
PcbNew. Enabling the modern toolset brings new features and better
performance. You can select which toolset to use in the preferences
menu. Using the Modern (Accelerated) toolset is recommended if your
graphics card supports it (requires OpenGL 2.0). If your graphics card
does not support the Accelerated toolset, you can still use the new
features by selecting the Modern (Fallback) toolset.
:::

::: paragraph
Using the Legacy toolset is only recommended if you notice that the
Modern toolset does not support a feature you need or if it does not
render a Gerber file correctly. If you notice such a problem, please
notify the KiCad developers so that it can be fixed in a future release.
:::

::: paragraph
The Legacy toolset will be removed in a future version of GerbView.
:::
::::::
:::::::::

:::::: sect2

### Miscellaneous menu {#_miscellaneous_menu}

:::: imageblock
::: content
![gerbview_misc_menu_png](images/gerbview_misc_menu.png)
:::
::::

::: ulist

- **List DCodes** shows the D Code information for all layers.

- **Show Source** displays the Gerber file contents of the active layer
  in a text editor.

- **Clear Current Layer** erases the contents of the active layer.

- **Set Text Editor...​** allows you to choose which program to show
  source with.
:::
::::::
::::::::::::::::::
:::::::::::::::::::

:::::::::::::::::::::::::::: sect1

## Display modes {#_display_modes}

::::::::::::::::::::::::::: sectionbody
::: paragraph
GerbView has three display modes which are useful for different
situations or requirements.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | Stacked mode and Transparency     |
| Note                              | mode provide a better graphical   |
| :::                               | experience, but may be slower     |
|                                   | then Raw mode on some computers.  |
+-----------------------------------+-----------------------------------+
:::

::::::: sect2

### Raw mode {#_raw_mode}

::: paragraph
This mode is selected by
[![gbr_select_mode0_png](images/icons/gbr_select_mode0.png)]{.image}.
Each file and each item in the file are drawn in the order files are
loaded. However, the active layer is drawn last.
:::

::: paragraph
When Gerber files have negative items (drawn in black), artifacts may be
visible on already-drawn layers.
:::

:::: imageblock
::: content
![gerbview_mode_raw_stack_png](images/gerbview_mode_raw_stack.png)
:::
::::
:::::::

::::::: sect2

### Stacked mode {#_stacked_mode}

::: paragraph
Invoked by
[![gbr_select_mode1_png](images/icons/gbr_select_mode1.png)]{.image},
each file is drawn in the order files are loaded. Again, the active
layer is drawn last.
:::

::: paragraph
When Gerber files have negative items (drawn in black) there are no
artifacts on already-drawn layers because this mode draws each file in a
local buffer before it is shown on screen.
:::

:::: imageblock
::: content
![gerbview_mode_raw_stack_png](images/gerbview_mode_raw_stack.png)
:::
::::
:::::::

:::::: sect2

### Transparency mode {#_transparency_mode}

::: paragraph
Use [![gbr_select_mode2_png](images/icons/gbr_select_mode2.png)]{.image}
to display in this mode, where no artifacts are present and layers are
blended together with the active layer on top.
:::

:::: imageblock
::: content
![gerbview_mode_transparency_png](images/gerbview_mode_transparency.png)
:::
::::
::::::

:::::::::: sect2

### Layer occlusion {#_layer_occlusion}

::: paragraph
In raw or stacked mode, the active layer will be on top of other layers
and hide items below it.
:::

::: paragraph
Here, layer 1 (green) is the active layer (note the triangle next to it)
and so it is drawn on top of layer 2 (blue):
:::

:::: imageblock
::: content
![gerbview_layer_select_1_png](images/gerbview_layer_select_1.png)
:::
::::

::: paragraph
Making layer 2 (blue) the active layer brings it to the top:
:::

:::: imageblock
::: content
![gerbview_layer_select_2_png](images/gerbview_layer_select_2.png)
:::
::::
::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

:::::: sect1

## Moving items {#_moving_items}

::::: sectionbody
::: paragraph
When using the legacy toolset, items may be selected by holding down the
left mouse button and drawing a rectangle. Releasing the button picks up
the items. A click of the left mouse button places the items.
:::

::: paragraph
This behavior is deprecated and not available in the modern toolsets.
:::
:::::
::::::

:::::: sect1

## Printing {#_printing}

::::: sectionbody
::: paragraph
To print layers, use the
[![print_button_png](images/icons/print_button.png)]{.image} icon or the
**File → Print** menu.
:::

::: {.admonitionblock .caution}

+-----------------------------------+------------------------------------------------------+
| ::: title                         | ::: paragraph                                        |
| Caution                           | Be sure items are inside the printable area. Use     |
| :::                               | [![sheetset_png](images/icons/sheetset.png)]{.image} |
|                                   | to select a suitable page format.                    |
|                                   | :::                                                  |
|                                   |                                                      |
|                                   | ::: paragraph                                        |
|                                   | Note that many photoplotters support a large         |
|                                   | plottable area, much bigger than the page sizes used |
|                                   | by most printers. Moving the entire layer set may be |
|                                   | required.                                            |
|                                   | :::                                                  |
+-----------------------------------+------------------------------------------------------+
:::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::
