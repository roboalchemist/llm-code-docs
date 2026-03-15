:::::: {#header}
# Pl_Editor

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}
::: {#toctitle}
Table of Contents
:::

- [Introduction to **Pl_Editor**](#introduction-to-pl_editor)
- [Pl_Editor files](#pl_editor-files)
  - [Input file and default title
    block](#input-file-and-default-title-block)
  - [Output file](#output-file)
- [Theory of operations](#theory-of-operations)
  - [Basic page layout items
    properties:](#basic-page-layout-items-properties)
  - [Coordinates definition](#coordinates-definition)
  - [Reference corners and
    coordinates:](#reference-corners-and-coordinates)
  - [Rotation](#rotation)
  - [Repeat option](#repeat-option)
- [Texts and formats](#texts-and-formats)
  - [Format symbols:](#format-symbols)
  - [Multi-line texts:](#multi-line-texts)
  - [Multi-line texts in Page Setup
    dialog:](#multi-line-texts-in-page-setup-dialog)
- [Constraints](#constraints)
  - [Page 1 constraint](#page-1-constraint)
  - [Text full size constraint](#text-full-size-constraint)
- [Invoking Pl_Editor](#invoking-pl_editor)
- [Pl_Editor Commands](#pl_editor-commands)
  - [Main Screen](#main-screen)
  - [Main Window Toolbar](#main-window-toolbar)
  - [Commands in drawing area (draw
    panel)](#commands-in-drawing-area-draw-panel)
  - [Status Bar Information](#status-bar-information)
- [Left window](#left-window)
- [Right window](#right-window)
- [Interactive edition](#interactive-edition)
  - [Item selection](#item-selection)
  - [Item creation](#item-creation)
  - [Adding lines, rectangles and
    texts](#adding-lines-rectangles-and-texts)
  - [Adding logos](#adding-logos)
  - [Adding image bitmaps](#adding-image-bitmaps)
::::
::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}
::::::::::::::: {#preamble}
:::::::::::::: sectionbody
::: paragraph
*Reference manual*
:::

::: {#copyright .paragraph}
**Copyright**
:::

::: paragraph
This document is Copyright © 2015 by it's contributors as listed below.
You may distribute it and/or modify it under the terms of either the GNU
General Public License
([http://www.gnu.org/licenses/gpl.html](http://www.gnu.org/licenses/gpl.html){.bare}),
version 3 or later, or the Creative Commons Attribution License
([http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/){.bare}),
version 3.0 or later.
:::

::: {#contributors .paragraph}
**Contributors**
:::

::: paragraph
Jean-Pierre Charras.
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
may 23, 2015.
:::

::: {style="page-break-after: always;"}
:::
::::::::::::::
:::::::::::::::

:::::::::: sect1
## Introduction to **Pl_Editor**

::::::::: sectionbody
::: paragraph
Pl_Editor is a page layout editor tool to create custom title blocks,
and frame references.
:::

::: paragraph
The title block, associated to frame references, and other graphic items
(logos) is called here a page layout.
:::

::: paragraph
Basic page layout items are:
:::

::: ulist
- **Lines**

- **Rectangles**

- **Texts** (with format symbols, that will be replaced by the actual
  text, like the date, page number...​) in Eeschema or Pcbnew.

- **Poly-polygons** (mainly to place logos and special graphic shapes)

- **Bitmaps**.
:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | Bitmaps can be plotted only by    |
| Warning                           | few plotters (PDF and PS only)    |
| :::                               | Therefore, for other plotters,    |
|                                   | only a bounding box will be       |
|                                   | plotted.                          |
+-----------------------------------+-----------------------------------+
:::

::: ulist
- Items can be repeated, and texts and poly_polygons can be rotated.
:::
:::::::::
::::::::::

::::::::::: sect1
## Pl_Editor files

:::::::::: sectionbody
::::: sect2
### Input file and default title block

::: paragraph
Pl_Editor reads or writes page layout description files \*.kicad_wks
(KiCad worksheet).
:::

::: paragraph
An internal default page layout description to display the default KiCad
title block is used until a file is read.
:::
:::::

:::::: sect2
### Output file

::: paragraph
The current page layout description can be written in a **\*.kicad_wks**
file, using the S-expression format, which is widely used in KiCad.
:::

::: paragraph
This file can be used to show the custom page layout in Eeschema and/or
Pcbnew.
:::

::: {style="page-break-after: always;"}
:::
::::::
::::::::::
:::::::::::

::::::::::::::::::::::::::::::::::: sect1
## Theory of operations

:::::::::::::::::::::::::::::::::: sectionbody
:::::::::: sect2
### Basic page layout items properties:

::: paragraph
Basic page layout items are:
:::

::: ulist
- **Lines**

- **Rectangles**

- **Texts** (with format symbols, with will be replaced by the actual
  text, like the date, page number...​) in Eeschema or Pcbnew.

- **Poly-polygons** (mainly to place logos and special graphic shapes).
  These poly polygons are created by **Bitmap2component**, and cannot be
  built inside pl_editor, because it is not possible to create such
  shapes by hand.

- **Bitmaps** to place logos.
:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | Bitmaps can be plotted only by    |
| Warning                           | few plotters: PDF and PS only.    |
| :::                               |                                   |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
Therefore:
:::

::: ulist
- **Texts, poly-polygons** and **bitmaps** are defined by a position,
  and can be rotated.

- **Lines** (in fact segments) and **rectangles** are defined by two
  points: a start point and a end point. They cannot be rotated (this is
  useless for segments).
:::

::: paragraph
These basic items can be repeated.
:::

::: paragraph
Texts which are repeated accept also an increment value for labels (has
meaning only if the text is one letter or one digit).
:::
::::::::::

::::: sect2
### Coordinates definition

::: paragraph
Each position, start point and end point of items is always relative to
a page corner.
:::

::: paragraph
**This feature ensure you can define a page layout which is not
dependent on the paper size**.
:::
:::::

::::::: sect2
### Reference corners and coordinates:

::: paragraph
[![page property 1](images/en/page_property_1.png)]{.image}
:::

::: ulist
- When the page size is changed, the position of the item, relative to
  its reference corner does not change.

- Usually, title blocks are attached to the right bottom corner, and
  therefore this corner is the default corner, when creating an item.
:::

::: paragraph
For rectangles and segments, which have two defined points, each point
has its reference corner.
:::

::: {style="page-break-after: always;"}
:::
:::::::

::::::::::: sect2
### Rotation

::: paragraph
Items which have a position defined by just one point (texts and
poly-polygons) can be rotated:
:::

::: paragraph
Normal: Rotation = 0
:::

:::: imageblock
::: content
![text noriented](images/en/text_noriented.png)
:::
::::

::: paragraph
Rotated: Rotation = 20 and 10 degrees.
:::

:::: imageblock
::: content
![text rotated](images/en/text_rotated.png)
:::
::::

::: {style="page-break-after: always;"}
:::
:::::::::::

:::::::: sect2
### Repeat option

::: paragraph
Items can be repeated:
:::

::: paragraph
This is useful to create grid and grid labels.
:::

:::: imageblock
::: content
![page property 2](images/en/page_property_2.png){width="]"}
:::
::::

::: {style="page-break-after: always;"}
:::
::::::::
::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Texts and formats

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::::::::::::::::::::::::::: sect2
### Format symbols:

::: paragraph
Texts can be simple strings or can include format symbols.
:::

::: paragraph
Format symbols are replaced by the actual values in Eeschema or Pcbnew.
:::

::: paragraph
They are like format symbols in printf function.
:::

::: paragraph
A format symbol is **%** followed by 1 letter.
:::

::: paragraph
The **%C** format has one digit (comment identifier).
:::

::: paragraph
Formats symbols are:
:::

::: paragraph
**%% = replaced by %**
:::

::: paragraph
**%K = KiCad version**
:::

::: paragraph
**%Z = paper format name (A4, USLetter ...​)**
:::

::: paragraph
**%Y = company name**
:::

::: paragraph
**%D = date**
:::

::: paragraph
**%R = revision**
:::

::: paragraph
**%S = sheet number**
:::

::: paragraph
**%N = number of sheets**
:::

::: paragraph
**%Cx = comment (x = 0 to 9 to identify the comment)**
:::

::: paragraph
**%F = filename**
:::

::: paragraph
**%P = sheet path (sheet full name, for Eeschema)**
:::

::: paragraph
**%T = title**
:::

::: paragraph
Example:
:::

::: paragraph
\"Size: %Z\" displays \"Size: A4\" or \"Size: USLetter\"
:::

::: {style="page-break-after: always;"}
:::

::: paragraph
User display mode: [![pagelayout normal view
mode](images/icons/pagelayout_normal_view_mode.png)]{.image} activated.
Title block displayed like in Eeschema and Pcbnew
:::

:::: imageblock
::: content
![show fields data](images/en/show_fields_data.png)
:::
::::

::: paragraph
\"Native\" display mode: [![pagelayout special view
mode](images/icons/pagelayout_special_view_mode.png)]{.image} activated.
The native texts entered in Pl_Editor, with their format symbols.
:::

:::: imageblock
::: content
![show fields codes](images/en/show_fields_codes.png)
:::
::::

::: {style="page-break-after: always;"}
:::
:::::::::::::::::::::::::::::::

:::::::::::::: sect2
### Multi-line texts:

::: paragraph
Texts can be multi-line.
:::

::: paragraph
There are 2 ways to insert a new line in texts:
:::

::: {.olist .arabic}
1.  Insert the \"\\n\" 2 chars sequence (mainly in Page setup dialog in
    KiCad).

2.  Insert a new line in Pl_Editor Design window.
:::

::: paragraph
Here is an example:
:::

::: paragraph
Setup
:::

:::: imageblock
::: content
![options multi line](images/en/options_multi_line.png)
:::
::::

::: paragraph
Output
:::

:::: imageblock
::: content
![multi line](images/en/multi_line.png)
:::
::::

::: {style="page-break-after: always;"}
:::
::::::::::::::

:::::::::::::: sect2
### Multi-line texts in Page Setup dialog:

::: paragraph
In the page setup dialog, text controls do not accept a multi-line text.
:::

::: paragraph
The **\"\\n\"** 2 chars sequence should be inserted to force a new line
inside a text.
:::

::: paragraph
Here is a two lines text, in *comment 2* field:
:::

::: paragraph
[![insert newline code](images/en/insert_newline_code.png)]{.image}
:::

::: paragraph
Here is the actual text:
:::

::: paragraph
[![multi line 2](images/en/multi_line_2.png)]{.image}
:::

::: paragraph
However, if you really want the **\"\\n\"** inside the text, enter
**\"\\\\n\"**.
:::

::: paragraph
[![insert slashnewline
code](images/en/insert_slashnewline_code.png)]{.image}
:::

::: paragraph
And the displayed text:
:::

::: paragraph
[![multi line 3](images/en/multi_line_3.png)]{.image}
:::

::: {style="page-break-after: always;"}
:::
::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::: sect1
## Constraints

::::::::::::::::::::::::::::: sectionbody
:::::::::: sect2
### Page 1 constraint

::: paragraph
When using Eeschema, the full schematic often uses more than one page.
:::

::: paragraph
Usually page layout items are displayed on all pages.
:::

::: paragraph
But if a user want some items to be displayed only on page 1, or not on
page 1, the \"page 1 option\" this is possible by setting this option:
:::

::: paragraph
[![display options](images/en/display_options.png)]{.image}
:::

::: paragraph
Page 1 option:
:::

::: ulist
- None: no constraint.

- Page 1 only: the items is visible only on page 1.

- Not on page 1: the items is visible on all pages but the page 1.
:::

::: {style="page-break-after: always;"}
:::
::::::::::

:::::::::::::::::::: sect2
### Text full size constraint

::: paragraph
[![constraint options](images/en/constraint_options.png)]{.image}
:::

::: paragraph
Only for texts, one can set 2 parameters :
:::

::: ulist
- the max size X

- the max size Y
:::

::: paragraph
which define a bounding box.
:::

::: paragraph
When these parameters are not 0, when displaying the text, the actual
text height and the actual text width are dynamically modified if the
full text size is bigger than the max size X and/or the max size Y, to
fit the full text size with this bounding box.
:::

::: paragraph
When the actual full text size is smaller than the max size X and/or the
max size Y, the text height and/or the text width is not modified.
:::

::: paragraph
The text with no bounding box. Max size X = 0,0 Max size Y = 0,0
:::

::: paragraph
[![constraints none](images/en/constraints_none.png)]{.image}
:::

::: paragraph
The **same** text with constraint. Max size X = 40,0 Max size Y = 0,0
:::

::: paragraph
[![constraints defined](images/en/constraints_defined.png)]{.image}
:::

::: {style="page-break-after: always;"}
:::

::: paragraph
A multi line text, constrained:
:::

::: paragraph
Setup
:::

::: paragraph
[![constraint options](images/en/constraint_options.png)]{.image}
:::

::: paragraph
Output
:::

::: paragraph
[![block constraints](images/en/block_constraints.png)]{.image}
:::

::: {style="page-break-after: always;"}
:::
::::::::::::::::::::
:::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::

:::::: sect1
## Invoking Pl_Editor

::::: sectionbody
::: paragraph
Pl_Editor is typically invoked from a command line, or from the KiCad
manager.
:::

::: paragraph
From a command line, the syntax is pl_editor \<\*.kicad_wks file to
open\>.
:::
:::::
::::::

::::::::::::::::::::::::::::: sect1
## Pl_Editor Commands

:::::::::::::::::::::::::::: sectionbody
::::::::: sect2
### Main Screen

::: paragraph
The image below shows the main window of Pl_Editor.
:::

:::: imageblock
::: content
![main window](images/en/main_window.png)
:::
::::

::: paragraph
The left pane contains the list of basic items.
:::

::: paragraph
The right pane is the item settings editor.
:::

::: {style="page-break-after: always;"}
:::
:::::::::

::::: sect2
### Main Window Toolbar

::: paragraph
[![main toolbar](images/en/main_toolbar.png)]{.image}
:::

::: paragraph
The top toolbar allows for easy access to the following commands:
:::

+---------------------------------------------------------------+--------------------------------------------------+
| [![new page                                                   | Select the net list file to be processed.        |
| layout](images/icons/new_page_layout.png)]{.image}            |                                                  |
+---------------------------------------------------------------+--------------------------------------------------+
| [![open page                                                  | Load a page layout description file.             |
| layout](images/icons/open_page_layout.png)]{.image}           |                                                  |
+---------------------------------------------------------------+--------------------------------------------------+
| [![save](images/icons/save.png)]{.image}                      | Save the current page layout description in a    |
|                                                               | .kicad_wks file.                                 |
+---------------------------------------------------------------+--------------------------------------------------+
| [![sheetset](images/icons/sheetset.png)]{.image}              | Display the page size selector and the title     |
|                                                               | block user data editor.                          |
+---------------------------------------------------------------+--------------------------------------------------+
| [![print button](images/icons/print_button.png)]{.image}      | Prints the current page.                         |
+---------------------------------------------------------------+--------------------------------------------------+
| [![delete](images/icons/delete.png)]{.image}                  | Delete the currently selected item.              |
+---------------------------------------------------------------+--------------------------------------------------+
| [![undo](images/icons/undo.png)]{.image}                      | Undo/redo tools.                                 |
| [![redo](images/icons/redo.png)]{.image}                      |                                                  |
+---------------------------------------------------------------+--------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image} [![zoom        | Zoom in, out, redraw and auto, respectively.     |
| out](images/icons/zoom_out.png)]{.image} [![zoom              |                                                  |
| redraw](images/icons/zoom_redraw.png)]{.image} [![zoom fit in |                                                  |
| page](images/icons/zoom_fit_in_page.png)]{.image}             |                                                  |
+---------------------------------------------------------------+--------------------------------------------------+
| [![pagelayout normal view                                     | Show the page layout in user mode: texts are     |
| mode](images/icons/pagelayout_normal_view_mode.png)]{.image}  | shown like in Eeschema or Pcbnew: text format    |
|                                                               | symbols are replaced by the user texts.          |
+---------------------------------------------------------------+--------------------------------------------------+
| [![pagelayout special view                                    | Show the page layout in native mode: texts are   |
| mode](images/icons/pagelayout_special_view_mode.png)]{.image} | displayed \"as is\", with the contained formats, |
|                                                               | without any replacement.                         |
+---------------------------------------------------------------+--------------------------------------------------+
| [![set base                                                   | Reference corner selection, for coordinates      |
| corner](images/en/set_base_corner.png){width="70%"}]{.image}  | displayed to the status bar.                     |
+---------------------------------------------------------------+--------------------------------------------------+
| [![set current                                                | Selection of the page number (page & or other    |
| page](images/en/set_current_page.png){width="85%"}]{.image}   | pages).                                          |
|                                                               |                                                  |
|                                                               | This selection has meaning only if some items    |
|                                                               | than have a page option, are not shown on all    |
|                                                               | pages (in a schematic for instance, which        |
|                                                               | contains more than one page).                    |
+---------------------------------------------------------------+--------------------------------------------------+
:::::

::::::::::: sect2
### Commands in drawing area (draw panel)

::: sect3
#### Keyboard Commands

+-------------+--------------------------------------------------------+
| F1          | Zoom In                                                |
+-------------+--------------------------------------------------------+
| F2          | Zoom Out                                               |
+-------------+--------------------------------------------------------+
| F3          | Refresh Display                                        |
+-------------+--------------------------------------------------------+
| F4          | Move cursor to center of display window                |
+-------------+--------------------------------------------------------+
| Home        | Fit footprint into display window                      |
+-------------+--------------------------------------------------------+
| Space Bar   | Set relative coordinates to the current cursor         |
|             | position                                               |
+-------------+--------------------------------------------------------+
| Right Arrow | Move cursor right one grid position                    |
+-------------+--------------------------------------------------------+
| Left Arrow  | Move cursor left one grid position                     |
+-------------+--------------------------------------------------------+
| Up Arrow    | Move cursor up one grid position                       |
+-------------+--------------------------------------------------------+
| Down Arrow  | Move cursor down one grid position                     |
+-------------+--------------------------------------------------------+
:::

::: sect3
#### Mouse Commands

+----------------------+-----------------------------------------------+
| Scroll Wheel         | Zoom in and out at the current cursor         |
|                      | position                                      |
+----------------------+-----------------------------------------------+
| Ctrl + Scroll Wheel  | Pan right and left                            |
+----------------------+-----------------------------------------------+
| Shift + Scroll Wheel | Pan up and down                               |
+----------------------+-----------------------------------------------+
| Right Button Click   | Open context menu                             |
+----------------------+-----------------------------------------------+
:::

:::::::: sect3
#### Context Menu

::: paragraph
Displayed by right-clicking the mouse:
:::

::: ulist
- Add Line

- Add Rectangle

- Add Text

- Append Page Layout Descr File
:::

::: paragraph
Are commands to add a basic layout item to the current page layout
description.
:::

::: ulist
- Zoom selection: direct selection of the display zoom.

- Grid selection: direct selection of the grid.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | *Append Page Layout Descr File*   |
| :::                               | is intended to add poly polygons  |
|                                   | to make logos.                    |
|                                   | :::                               |
|                                   |                                   |
|                                   | ::: paragraph                     |
|                                   | Because usually a logo it needs   |
|                                   | hundred of vertices, you cannot   |
|                                   | create a polygon by hand. But you |
|                                   | can append a description file,    |
|                                   | created by Bitmap2Component.      |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
::::::::
:::::::::::

:::::::: sect2
### Status Bar Information

::: paragraph
The status bar is located at the bottom of the Pl_Editor and provides
useful information to the user.
:::

:::: imageblock
::: content
![pl status bar](images/en/pl_status_bar.png)
:::
::::

::: paragraph
Coordinates are **always relative to the corner** selected as
**reference**.
:::

::: {style="page-break-after: always;"}
:::
::::::::
::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::

:::::::::::: sect1
## Left window

::::::::::: sectionbody
::: paragraph
The left windows shows the list of layout items.
:::

::: paragraph
One can select a given item (left clicking on the line) or, when right
clicking on the line, display a pop up menu.
:::

::: paragraph
This menu allows basic operations: add a new item, or delete the
selected item.
:::

::: paragraph
**→ A selected item is also drawn in a different color on draw panel**.
:::

::: paragraph
Design tree: the item 19 is selected, and shown in highlighted on the
draw panel.
:::

:::: imageblock
::: content
![project tree](images/en/project_tree.png)
:::
::::

::: {style="page-break-after: always;"}
:::
:::::::::::
::::::::::::

::::::::: sect1
## Right window

:::::::: sectionbody
::: paragraph
The right window is the edit window.
:::

+----------------------------------------------------------+----------------------------------------------------------+
| [![property                                              | [![property                                              |
| none](images/en/property_none.png){width="50%"}]{.image} | main](images/en/property_main.png){width="50%"}]{.image} |
+----------------------------------------------------------+----------------------------------------------------------+

::: paragraph
On this dialog you can set the page property and the item property of
the current item.
:::

::: {style="page-break-after: always;"}
:::

::: paragraph
Displayed settings depend on the selected item:
:::

+------------------------------------------------------------------+--------------------------------------------------------------+
| Settings for lines and rectangles                                | Settings for texts                                           |
+------------------------------------------------------------------+--------------------------------------------------------------+
| [![property                                                      | [![property                                                  |
| line](images/en/property_line.png){width="50%"}]{.image}         | text](images/en/property_text.png){width="50%"}]{.image}     |
+------------------------------------------------------------------+--------------------------------------------------------------+
| Settings for poly-polygons                                       | Setting for bitmaps                                          |
+------------------------------------------------------------------+--------------------------------------------------------------+
| [![property                                                      | [![property                                                  |
| polyline](images/en/property_polyline.png){width="50%"}]{.image} | bitmap](images/en/property_bitmap.png){width="50%"}]{.image} |
+------------------------------------------------------------------+--------------------------------------------------------------+

::: {style="page-break-after: always;"}
:::
::::::::
:::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Interactive edition

:::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::::::::: sect2
### Item selection

::: paragraph
An item can be selected:
:::

::: ulist
- From the Design tree.

- By Left clicking on it.

- By Right clicking on it (and a pop up menu will be displayed).
:::

::: paragraph
When selected, this item is drawn in yellow.
:::

+---------------------------------------------------+----------------------------------------------+
| [![edit                                           | The starting point ([![edit line             |
| line](images/edit_line.png){width="70%"}]{.image} | start](images/edit_line_start.png)]{.image}) |
|                                                   | and the ending point ([![edit line           |
|                                                   | end](images/edit_line_end.png)]{.image}) are |
|                                                   | highlighted.                                 |
+---------------------------------------------------+----------------------------------------------+

::: paragraph
When right clicking on the item, a pop-up menu is displayed.
:::

::: paragraph
The pop menu options slightly depend on the selection:
:::

+---------------------------------------------------------------------+-----------------------------------------------------------------+--------------------------------------------------------------+
| [![context line move                                                | [![context line move                                            | [![context line                                              |
| start](images/en/context_line_move_start.png){width="50%"}]{.image} | end](images/en/context_line_move_end.png){width="50%"}]{.image} | move](images/en/context_line_move.png){width="50%"}]{.image} |
+---------------------------------------------------------------------+-----------------------------------------------------------------+--------------------------------------------------------------+

::: {style="page-break-after: always;"}
:::

::: paragraph
If more than one item is found, a menu clarification will be shown, to
select the item:
:::

:::: imageblock
::: content
![dialog select element](images/en/dialog_select_element.png)
:::
::::

+---------------------------------------------------------+-----------------------------------+
| [![drag                                                 | Once selected, the item, or one   |
| element](images/drag_element.png){width="70%"}]{.image} | of its end points, can be moved   |
|                                                         | by moving the mouse and placed    |
|                                                         | (right clicking on the mouse).    |
+---------------------------------------------------------+-----------------------------------+

::: {style="page-break-after: always;"}
:::
:::::::::::::

::::::::::::::: sect2
### Item creation

::: paragraph
To add a new item, right click the mouse button when the cursor is on
the left window or the draw area.
:::

::: paragraph
A popup menu is displayed:
:::

::: paragraph
Pop up menu in left window
:::

:::: imageblock
::: content
![context createnew](images/en/context_createnew.png)
:::
::::

::: paragraph
Pop up menu in draw area.
:::

:::: imageblock
::: content
![context createnew2](images/en/context_createnew2.png)
:::
::::

::: paragraph
Lines, rectangles and texts are added just by clicking on the
corresponding menu item.
:::

::: paragraph
Logos must first be created by Bitmap2component, which creates a page
layout description file.
:::

::: paragraph
The Append Page Layout Descr File option append this file, to insert the
logo (a poly polygon).
:::

::: {style="page-break-after: always;"}
:::
:::::::::::::::

::::::::::::::: sect2
### Adding lines, rectangles and texts

::: paragraph
When clicking on the option, a dialog is opened:
:::

::: paragraph
Adding line or rectangle
:::

:::: imageblock
::: content
![dialog newline](images/en/dialog_newline.png)
:::
::::

::: paragraph
Adding text
:::

:::: imageblock
::: content
![dialog newtext](images/en/dialog_newtext.png)
:::
::::

::: paragraph
Position of end points, and corner reference can be defined here.
:::

::: paragraph
However they can be defined later, from the right window, or by moving
the item, or one of its end points.
:::

::: paragraph
Most of time the corner reference is the same for both points.
:::

::: paragraph
If this is not the case, define the corner reference at creation is
better, because if a corner reference is changed later, the geometry of
the item will be a bit strange.
:::

::: paragraph
When an item is created, if is put in move mode, and you can refine its
position (this is very useful for texts and small lines or rectangles)
:::
:::::::::::::::

:::::::: sect2
### Adding logos

::: paragraph
To add a logo, a poly polygon (the vectored image of the logo) must be
first created using Bitmap2component.
:::

::: paragraph
Bitmap2component creates a page layout description file which is append
to the current design, using the **Append Page Layout Descr File**
option.
:::

::: paragraph
Bitmap2component creates a page layout description file which contains
only one item: a poly polygon.
:::

::: paragraph
*However, this command can be used to append any page layout description
file, which is merged with the current design.*
:::

::: paragraph
Once a poly polygon is inserted, it can be moved and its parameters
edited.
:::
::::::::

:::::: sect2
### Adding image bitmaps

::: paragraph
You can add an image bitmap using most of bitmap formats (PNG, JPEG, BMP
...​).
:::

::: ulist
- When a bitmap is imported, its PPI (pixel per inch) definition is set
  to 300PPI.

- This value can be modified in panel Properties (right panel).

- The actual size depend on this parameter.

- Be aware that using higher definition values brings larger output
  files, and can have a noticeable draw or plot time.
:::

::: paragraph
A bitmap can be repeated, **but not rotated**.
:::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}
::: {#footer-text}
Last updated 2026-03-15 16:35:47 -0700
:::
::::
