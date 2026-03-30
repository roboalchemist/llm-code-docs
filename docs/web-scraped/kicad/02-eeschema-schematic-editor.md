:::::: {#header}
# Eeschema

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}
::: {#toctitle}
Table of Contents
:::

- [Introduction to Eeschema](#_introduction_to_eeschema)
  - [Description](#_description)
  - [Technical overview](#_technical_overview)
- [Generic Eeschema commands](#_generic_eeschema_commands)
  - [Mouse commands](#_mouse_commands)
  - [Hotkeys](#_hotkeys)
  - [Grid](#_grid)
  - [Zoom selection](#_zoom_selection)
  - [Displaying cursor coordinates](#_displaying_cursor_coordinates)
  - [Top menu bar](#_top_menu_bar)
  - [Upper toolbar](#_upper_toolbar)
  - [Right toolbar icons](#_right_toolbar_icons)
  - [Left toolbar icons](#_left_toolbar_icons)
  - [Pop-up menus and quick editing](#pop-up-menus-and-quick-editing)
- [Main top menu](#main-top-menu)
  - [File menu](#file-menu)
  - [Preferences menu](#preferences-menu)
  - [Help menu](#help-menu)
- [General Top Toolbar](#general-top-toolbar)
  - [Sheet management](#sheet-management)
  - [Search tool](#search-tool)
  - [Netlist tool](#netlist-tool)
  - [Annotation tool](#annotation-tool)
  - [Electrical Rules Check tool](#electrical-rules-check-tool)
  - [Bill of Material tool](#bill-of-material-tool)
  - [Edit Fields tool](#edit-fields-tool)
  - [Import tool for footprint
    assignment](#import-tool-for-footprint-assignment)
- [Manage Symbol Libraries](#_manage_symbol_libraries)
  - [Symbol Library Table](#_symbol_library_table)
- [Schematic Creation and Editing](#schematic-creation-and-editing)
  - [Introduction](#_introduction)
  - [General considerations](#general-considerations)
  - [The development chain](#the-development-chain)
  - [Symbol placement and editing](#component-placement-and-editing)
  - [Wires, Buses, Labels, Power ports](#wires-buses-labels-power-ports)
  - [Drawing Complements](#drawing-complements)
  - [Rescuing cached symbols](#rescuing-cached-components)
- [Hierarchical schematics](#hierarchical-schematics)
  - [Introduction](#introduction-2)
  - [Navigation in the Hierarchy](#navigation-in-the-hierarchy)
  - [Local, hierarchical and global
    labels](#local-hierarchical-and-global-labels)
  - [Summary of hierarchy creation](#summary-of-hierarchy-creation)
  - [Sheet symbol](#sheet-symbol)
  - [Connections - hierarchical pins](#connections-hierarchical-pins)
  - [Connections - hierarchical
    labels](#connections---hierarchical-labels)
  - [Complex Hierarchy](#complex-hierarchy)
  - [Flat hierarchy](#flat-hierarchy)
- [Symbol Annotation Tool](#automatic-classification-annotation)
  - [Introduction](#_introduction_2)
  - [Some examples](#some-examples)
- [Design verification with Electrical Rules Check](#erc)
  - [Introduction](#_introduction_3)
  - [How to use ERC](#how-to-use-erc)
  - [Example of ERC](#example-of-erc)
  - [Displaying diagnostics](#displaying-diagnostics)
  - [Power pins and Power flags](#power-pins-and-power-flags)
  - [Configuration](#configuration)
  - [ERC report file](#erc-report-file)
- [Create a Netlist](#create-a-netlist)
  - [Overview](#_overview)
  - [Netlist formats](#netlist-formats)
  - [Netlist examples](#netlist-examples)
  - [Notes on Netlists](#notes-on-netlists)
  - [Other formats](#other-formats)
- [Plot and Print](#plot-and-print)
  - [Introduction](#_introduction_4)
  - [Common printing commands](#common-printing-commands)
  - [Plot in Postscript](#plot-in-postscript)
  - [Plot in PDF](#plot-in-pdf)
  - [Plot in SVG](#plot-in-svg)
  - [Plot in DXF](#plot-in-dxf)
  - [Plot in HPGL](#plot-in-hpgl)
  - [Print on paper](#print-on-paper)
- [Symbol Library Editor](#symbol-library-editor)
  - [General Information About Symbol
    Libraries](#general-information-about-symbol-libraries)
  - [Symbol Library Overview](#symbol-library-overview)
  - [Symbol Library Editor Overview](#symbol-library-editor-overview)
  - [Library Selection and
    Maintenance](#library-selection-and-maintenance)
  - [Creating Library Symbols](#creating-library-symbols)
  - [Graphical Elements](#graphical-elements)
  - [Multiple Units per Symbol and Alternate Body
    Styles](#multiple-units-per-symbol-and-alternate-body-styles)
  - [Pin Creation and Editing](#pin-creation-and-editing)
  - [Symbol Fields](#symbol-fields)
  - [Power Symbols](#power-symbols)
- [LibEdit - Symbols](#libedit-symbols)
  - [Overview](#_overview_2)
  - [Position a symbol anchor](#position-a-symbol-anchor)
  - [Symbol aliases](#symbol-aliases)
  - [Symbol fields](#symbol-fields-1)
  - [Symbol documentation](#symbol-documentation)
  - [Symbol library](#symbol-library)
- [Symbol Library Browser](#viewlib)
  - [Introduction](#_introduction_5)
  - [Viewlib - main screen](#viewlib---main-screen)
  - [Symbol Library Browser Top Toolbar](#viewlib-top-toolbar)
- [Creating Customized Netlists and BOM
  Files](#creating-customized-netlists-and-bom-files)
  - [Intermediate Netlist File](#intermediate-netlist-file)
  - [Conversion to a new netlist
    format](#conversion-to-a-new-netlist-format)
  - [XSLT approach](#xslt-approach)
  - [Command line format: example for python
    scripts](#command-line-format-example-for-python-scripts)
  - [Intermediate Netlist structure](#intermediate-netlist-structure)
  - [More about xsltproc](#more-about-xsltproc)
- [Simulator](#simulator)
  - [Assigning models](#_assigning_models)
  - [Spice directives](#sim-directives)
  - [Simulation](#_simulation)
::::
::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}
::::::::::::::: {#preamble}
:::::::::::::: sectionbody
::: paragraph
*Reference manual*
:::

::: {#copyright .paragraph}
**Copyright**
:::

::: paragraph
This document is Copyright © 2010-2018 by its contributors as listed
below. You may distribute it and/or modify it under the terms of either
the GNU General Public License
([http://www.gnu.org/licenses/gpl.html](http://www.gnu.org/licenses/gpl.html){.bare}),
version 3 or later, or the Creative Commons Attribution License
([http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/){.bare}),
version 3.0 or later.
:::

::: paragraph
All trademarks within this guide belong to their legitimate owners.
:::

::: {#contributors .paragraph}
**Contributors**
:::

::: paragraph
Jean-Pierre Charras, Fabrizio Tappero.
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

- About KiCad translation:
  [https://github.com/KiCad/kicad-i18n/issues](https://github.com/KiCad/kicad-i18n/issues){.bare}
:::

::: {#publication_date_and_software_version .paragraph}
**Publication date and software version**
:::

::: paragraph
Published on May 30, 2015.
:::
::::::::::::::
:::::::::::::::

:::::::::::::::: sect1
## Introduction to Eeschema {#_introduction_to_eeschema}

::::::::::::::: sectionbody
:::::::::: sect2
### Description {#_description}

::: paragraph
Eeschema is a schematic capture software distributed as a part of KiCad
and available under the following operating systems:
:::

::: ulist
- Linux

- Apple macOS

- Windows
:::

::: paragraph
Regardless of the OS, all Eeschema files are 100% compatible from one OS
to another.
:::

::: paragraph
Eeschema is an integrated application where all functions of drawing,
control, layout, library management and access to the PCB design
software are carried out within Eeschema itself.
:::

::: paragraph
Eeschema is intended to cooperate with PcbNew, which is KiCad's printed
circuit design software. It can also export netlist files, which lists
all the electrical connections, for other packages.
:::

::: paragraph
Eeschema includes a symbol library editor, which can create and edit
symbols and manage libraries. It also integrates the following
additional but essential functions needed for modern schematic capture
software:
:::

::: ulist
- Electrical rules check (ERC) for the automatic control of incorrect
  and missing connections

- Export of plot files in many formats (Postscript, PDF, HPGL, and SVG)

- Bill of Materials generation (via Python or XSLT scripts, which allow
  many flexible formats).
:::
::::::::::

:::::: sect2
### Technical overview {#_technical_overview}

::: paragraph
Eeschema is limited only by the available memory. There is thus no real
limitation to the number of components, component pins, connections or
sheets. In the case of multi-sheet diagrams, the representation is
hierarchical.
:::

::: paragraph
Eeschema can use multi-sheet diagrams in a few ways:
:::

::: ulist
- Simple hierarchies (each schematic is used only once).

- Complex hierarchies (some schematics are used more than once with
  multiple instances).

- Flat hierarchies (schematics are not explicitly connected in a master
  diagram).
:::
::::::
:::::::::::::::
::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Generic Eeschema commands {#_generic_eeschema_commands}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Commands can be executed by:
:::

::: ulist
- Clicking on the menu bar (top of screen).

- Clicking on the icons on top of the screen (general commands).

- Clicking on the icons on the right side of the screen (particular
  commands or \"tools\").

- Clicking on the icons on the left side of the screen (display
  options).

- Pressing the mouse buttons (important complementary commands). In
  particular a right click opens a contextual menu for the element under
  the cursor (Zoom, grid and editing of the elements).

- Function keys (F1, F2, F3, F4, Insert and Space keys). Specifically:
  Escape key cancels the command in progress. Insert key allows the
  duplication of the last element created.

- Pressing hot keys which typically perform a select tool command and
  begin tool action at the current cursor location. For a list of hot
  keys, see the \"Help→List Hotkeys\" menu entry or press \'?\' key.
:::

:::: imageblock
::: content
![Commands overview](images/en/commands_overview.png)
:::
::::

::::::::::::::::: sect2
### Mouse commands {#_mouse_commands}

::::::: sect3
#### Basic commands {#_basic_commands}

::: paragraph
**Left button**
:::

::: ulist
- Single click: displays the characteristics of the symbol or text under
  the cursor in the status bar.

- Double click: edit (if the element is editable) the symbol or text.
:::

::: paragraph
**Right button**
:::

::: ulist
- Opens a pop-up menu.
:::
:::::::

::::::::::: sect3
#### Block operations {#_block_operations}

::: paragraph
You can move, drag, copy and delete selected areas in all Eeschema
menus.
:::

::: paragraph
Areas are selected by drawing a box around items using the left mouse
button.
:::

::: paragraph
Holding `Shift`, `Ctrl`, or `Shift + Ctrl` during selection
respectively performs copying, dragging and deletion:
:::

+----------------------------------------------+-----------------------+
| left mouse button                            | Move selection.       |
+----------------------------------------------+-----------------------+
| Shift + left mouse button                    | Copy selection.       |
+----------------------------------------------+-----------------------+
| Ctrl + left mouse button                     | Drag selection.       |
+----------------------------------------------+-----------------------+
| Ctrl + Shift + left mouse button             | Delete selection.     |
+----------------------------------------------+-----------------------+

::: paragraph
When dragging or copying, you can:
:::

::: ulist
- Click again to place the elements.

- Click the right button or press Escape key to cancel.
:::

::: paragraph
If a block move command has started, another command can be selected
using the right-click pop-up menu.
:::

:::: imageblock
::: content
![main window popup](images/en/main_window_popup.png)
:::
::::
:::::::::::
:::::::::::::::::

::::::: sect2
### Hotkeys {#_hotkeys}

::: ulist
- The \"?\" key displays the current hotkey list.

- Hotkeys might be redefined in Controls tab of Schematic Editor Options
  dialog (menu Preferences → General Options).
:::

::: paragraph
Here is the default hotkey list:
:::

+-----------------------------------+-----------------------------------+
| Help (this window)                | ?                                 |
+-----------------------------------+-----------------------------------+
| Zoom In                           | F1                                |
+-----------------------------------+-----------------------------------+
| Zoom Out                          | F2                                |
+-----------------------------------+-----------------------------------+
| Zoom Redraw                       | F3                                |
+-----------------------------------+-----------------------------------+
| Zoom Center                       | F4                                |
+-----------------------------------+-----------------------------------+
| Fit on Screen                     | Home                              |
+-----------------------------------+-----------------------------------+
| Zoom to Selection                 | @                                 |
+-----------------------------------+-----------------------------------+
| Reset Local Coordinates           | Space                             |
+-----------------------------------+-----------------------------------+
| Edit Item                         | E                                 |
+-----------------------------------+-----------------------------------+
| Delete Item                       | Del                               |
+-----------------------------------+-----------------------------------+
| Rotate Item                       | R                                 |
+-----------------------------------+-----------------------------------+
| Drag Item                         | G                                 |
+-----------------------------------+-----------------------------------+
| Undo                              | Ctrl+Z                            |
+-----------------------------------+-----------------------------------+
| Redo                              | Ctrl+Y                            |
+-----------------------------------+-----------------------------------+
| Mouse Left Click                  | Return                            |
+-----------------------------------+-----------------------------------+
| Mouse Left Double Click           | End                               |
+-----------------------------------+-----------------------------------+
| Save Schematic                    | Ctrl+S                            |
+-----------------------------------+-----------------------------------+
| Load Schematic                    | Ctrl+O                            |
+-----------------------------------+-----------------------------------+
| Find Item                         | Ctrl+F                            |
+-----------------------------------+-----------------------------------+
| Find Next Item                    | F5                                |
+-----------------------------------+-----------------------------------+
| Find Next DRC Marker              | Shift+F5                          |
+-----------------------------------+-----------------------------------+
| Find and Replace                  | Ctrl+Alt+F                        |
+-----------------------------------+-----------------------------------+
| Repeat Last Item                  | Ins                               |
+-----------------------------------+-----------------------------------+
| Move Block → Drag Block           | Tab                               |
+-----------------------------------+-----------------------------------+
| Copy Block                        | Ctrl+C                            |
+-----------------------------------+-----------------------------------+
| Paste Block                       | Ctrl+V                            |
+-----------------------------------+-----------------------------------+
| Cut Block                         | Ctrl+X                            |
+-----------------------------------+-----------------------------------+
| Move Schematic Item               | M                                 |
+-----------------------------------+-----------------------------------+
| Duplicate Symbol or Label         | C                                 |
+-----------------------------------+-----------------------------------+
| Add Symbol                        | A                                 |
+-----------------------------------+-----------------------------------+
| Add Power                         | P                                 |
+-----------------------------------+-----------------------------------+
| Mirror X                          | X                                 |
+-----------------------------------+-----------------------------------+
| Mirror Y                          | Y                                 |
+-----------------------------------+-----------------------------------+
| Orient Normal Symbol              | N                                 |
+-----------------------------------+-----------------------------------+
| Edit Symbol Value                 | V                                 |
+-----------------------------------+-----------------------------------+
| Edit Symbol Reference             | U                                 |
+-----------------------------------+-----------------------------------+
| Edit Symbol Footprint             | F                                 |
+-----------------------------------+-----------------------------------+
| Edit with Symbol Editor           | Ctrl+E                            |
+-----------------------------------+-----------------------------------+
| Begin Wire                        | W                                 |
+-----------------------------------+-----------------------------------+
| Begin Bus                         | B                                 |
+-----------------------------------+-----------------------------------+
| End Line Wire Bus                 | K                                 |
+-----------------------------------+-----------------------------------+
| Add Label                         | L                                 |
+-----------------------------------+-----------------------------------+
| Add Hierarchical Label            | H                                 |
+-----------------------------------+-----------------------------------+
| Add Global Label                  | Ctrl+L                            |
+-----------------------------------+-----------------------------------+
| Add Junction                      | J                                 |
+-----------------------------------+-----------------------------------+
| Add No Connect Flag               | Q                                 |
+-----------------------------------+-----------------------------------+
| Add Sheet                         | S                                 |
+-----------------------------------+-----------------------------------+
| Add Wire Entry                    | Z                                 |
+-----------------------------------+-----------------------------------+
| Add Bus Entry                     | /                                 |
+-----------------------------------+-----------------------------------+
| Add Graphic PolyLine              | I                                 |
+-----------------------------------+-----------------------------------+
| Add Graphic Text                  | T                                 |
+-----------------------------------+-----------------------------------+
| Update PCB from Schematic         | F8                                |
+-----------------------------------+-----------------------------------+
| Autoplace Fields                  | O                                 |
+-----------------------------------+-----------------------------------+
| Leave Sheet                       | Alt+BkSp                          |
+-----------------------------------+-----------------------------------+
| Delete Node                       | BkSp                              |
+-----------------------------------+-----------------------------------+
| Highlight Connection              | Ctrl+X                            |
+-----------------------------------+-----------------------------------+

::: paragraph
All hotkeys can be redefined using the hotkey editor (menu
Preferences→General Options→[Controls](#preferences-controls)).
:::

::: paragraph
It is possible to import/export hotkey settings using menu
Preferences→Import and Export→Import/Export Hotkeys.
:::
:::::::

:::::::: sect2
### Grid {#_grid}

::: paragraph
In Eeschema the cursor always moves over a grid. The grid can be
customized:
:::

::: ulist
- Size might be changed using the pop-up menu or using the
  Preferences/Options menu.

- Color might be changed in Colors tab of the Schematic Editor Options
  dialog (menu Preferences → General Options).

- Visibility might be switched using the left-hand toolbar button.
:::

::: paragraph
The default grid size is 50 mil (0.050\") or 1,27 millimeters.
:::

::: paragraph
This is the preferred grid to place symbols and wires in a schematic,
and to place pins when designing a symbol in the Symbol Editor.
:::

::: paragraph
One can also work with a smaller grid from 25 mil to 10 mil. This is
only intended for designing the symbol body or placing text and comments
and not recommended for placing pins and wires.
:::
::::::::

::::: sect2
### Zoom selection {#_zoom_selection}

::: paragraph
To change the zoom level:
:::

::: ulist
- Right click to open the Pop-up menu and select the desired zoom.

- Or use the function keys:

  ::: ulist
  - F1: Zoom in

  - F2: Zoom out

  - F4 or simply click on the middle mouse button (without moving the
    mouse): Center the view around the cursor pointer position
  :::

- Window Zoom:

  ::: ulist
  - Mouse wheel: Zoom in/out

  - Shift+Mouse wheel: Pan up/down

  - Ctrl+Mouse wheel: Pan left/right
  :::
:::
:::::

::::::::: sect2
### Displaying cursor coordinates {#_displaying_cursor_coordinates}

::: paragraph
The display units are in inches or millimeters. However, Eeschema always
uses 0.001 inch (mil/thou) as its internal unit.
:::

::: paragraph
The following information is displayed at the bottom right hand side of
the window:
:::

::: ulist
- The zoom factor

- The absolute position of the cursor

- The relative position of the cursor
:::

::: paragraph
The relative coordinates can be reset to zero by pressing Space. This is
useful for measuring distance between two points or aligning objects.
:::

:::: imageblock
::: content
![status_bar](images/en/status_bar.png)
:::
::::
:::::::::

:::::: sect2
### Top menu bar {#_top_menu_bar}

::: paragraph
The top menu bar allows the opening and saving of schematics, program
configuration and viewing the documentation.
:::

:::: imageblock
::: content
![menubar](images/en/menu_bar.png)
:::
::::
::::::

::::::::: sect2
### Upper toolbar {#_upper_toolbar}

::: paragraph
This toolbar gives access to the main functions of Eeschema.
:::

::: paragraph
If Eeschema is run in standalone mode, this is the available tool set:
:::

:::: imageblock
::: content
![](images/toolbar_schedit_standalone.png)
:::
::::

::: paragraph
Note that when KiCad runs in project mode, the first two icons are not
available as they work with individual files.
:::

+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![New schematic icon](images/icons/new_document.png)]{.image}             | Create a new schematic (only in standalone mode).             |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Open schematic icon](images/icons/open_document.png)]{.image}           | Open a schematic (only in standalone mode).                   |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Save schematic icon](images/icons/save.png)]{.image}                    | Save complete schematic project.                              |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Page Settings icon](images/icons/sheetset.png)]{.image}                 | Select the sheet size and edit the title block.               |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Print icon](images/icons/print_button.png)]{.image}                     | Open print dialog.                                            |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/paste_png](images/icons/paste.png)]{.image}                       | Paste a copied/cut item or block to the current sheet.        |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/undo_png](images/icons/undo.png)]{.image}                         | Undo: Revert the last change.                                 |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/redo_png](images/icons/redo.png)]{.image}                         | Redo: Revert the last undo operation.                         |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![search icon](images/icons/find.png)]{.image}                            | Show the dialog to search symbols and texts in the schematic. |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![search replace icon](images/icons/find_replace.png)]{.image}            | Show the dialog to search and replace texts in the schematic. |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/zoom_redraw](images/icons/zoom_redraw.png)]{.image}               | Refresh screen; zoom to fit.                                  |
| [![icons/zoom_fit_in_page_png](images/icons/zoom_fit_in_page.png)]{.image} |                                                               |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/zoom_in](images/icons/zoom_in.png)]{.image}                       | Zoom in and out.                                              |
| [![icons/zoom_out](images/icons/zoom_out.png)]{.image}                     |                                                               |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![hierarchy navigator icon](images/icons/hierarchy_nav.png)]{.image}      | View and navigate the hierarchy tree.                         |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/leave_sheet](images/icons/leave_sheet.png)]{.image}               | Leave the current sheet and go up in the hierarchy.           |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/libedit_png](images/icons/libedit.png)]{.image}                   | Call the symbol library editor to view and modify libraries   |
|                                                                            | and symbols.                                                  |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/library_browse_png](images/icons/library_browse.png)]{.image}     | Browse symbol libraries.                                      |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons_annotate_png](images/icons/annotate.png)]{.image}                 | Annotate symbols.                                             |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![ERC icon](images/icons/erc.png)]{.image}                                | Electrical Rules Checker (ERC), automatically validate        |
|                                                                            | electrical connections.                                       |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![run cvpcb icon](images/icons/cvpcb.png)]{.image}                        | Call CvPcb to assign footprints to symbols.                   |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Netlist icon](images/icons/netlist.png)]{.image}                        | Export a netlist (Pcbnew, SPICE and other formats).           |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Symbol fields editor icon](images/icons/spreadsheet.png)]{.image}       | Edit symbol fields.                                           |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![BOM icon](images/icons/bom.png)]{.image}                                | Generate the Bill of Materials (BOM).                         |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/pcbnew_png](images/icons/pcbnew.png)]{.image}                     | Call Pcbnew to perform a PCB layout.                          |
+----------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Import Footprint Names                                                  | Back-import footprint assignment (selected using CvPcb or     |
| icon](images/icons/import_footprint_names.png)]{.image}                    | Pcbnew) into the \"footprint\" fields.                        |
+----------------------------------------------------------------------------+---------------------------------------------------------------+

::: {style="page-break-after: always;"}
:::
:::::::::

::::: sect2
### Right toolbar icons {#_right_toolbar_icons}

::: paragraph
This toolbar contains tools to:
:::

::: ulist
- Place symbols, wires, buses, junctions, labels, text, etc.

- Create hierarchical subsheets and connection symbols.
:::

+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Cancel tool icon](images/icons/cursor.png)]{.image}                                       | Cancel the active command or tool.                            |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Highlight net icon](images/icons/net_highlight_schematic.png)]{.image}                    | Highlight a net by marking its wires and net labels with a    |
|                                                                                              | different color. If KiCad runs in project mode then copper    |
|                                                                                              | corresponding to the selected net will be highlighted in      |
|                                                                                              | Pcbnew as well.                                               |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![New Symbol icon](images/icons/new_symbol.png)]{.image}                                    | Display the symbol selector dialog to select a new symbol to  |
|                                                                                              | be placed.                                                    |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Add Power icon](images/icons/add_power.png)]{.image}                                      | Display the power symbol selector dialog to select a power    |
|                                                                                              | symbol to be placed.                                          |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_line_png](images/icons/add_line.png)]{.image}                                   | Draw a wire.                                                  |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_bus_png](images/icons/add_bus.png)]{.image}                                     | Draw a bus.                                                   |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_line2bus_png](images/icons/add_line2bus.png)]{.image}                           | Draw wire-to-bus entry points. These elements are only        |
|                                                                                              | graphical and do not create a connection, thus they should    |
|                                                                                              | not be used to connect wires together.                        |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_bus2bus_png](images/icons/add_bus2bus.png)]{.image}                             | Draw bus-to-bus entry points.                                 |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/noconn_png](images/icons/noconn.png)]{.image}                                       | Place a \"No Connect\" flag. These flags should be placed on  |
|                                                                                              | symbol pins which are meant to be left unconnected. It is     |
|                                                                                              | done to notify the Electrical Rules Checker that lack of      |
|                                                                                              | connection for a particular pin is intentional and should not |
|                                                                                              | be reported.                                                  |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_junction_png](images/icons/add_junction.png)]{.image}                           | Place a junction. This connects two crossing wires or a wire  |
|                                                                                              | and a pin, when it can be ambiguous (i.e. if a wire end or a  |
|                                                                                              | pin is not directly connected to another wire end).           |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_line_label_png](images/icons/add_line_label.png)]{.image}                       | Place a local label. Local label connects items located **in  |
|                                                                                              | the same sheet**. For connections between two different       |
|                                                                                              | sheets, you have to use global or hierarchical labels.        |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![Global label icon](images/icons/add_glabel.png)]{.image}                                  | Place a global label. All global labels with the same name    |
|                                                                                              | are connected, even when located on different sheets.         |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_hierarchical_label_png](images/icons/add_hierarchical_label.png)]{.image}       | Place a hierarchical label. Hierarchical labels are used to   |
|                                                                                              | create a connection between a subsheet and the parent sheet   |
|                                                                                              | that contains it.                                             |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_hierarchical_subsheet_png](images/icons/add_hierarchical_subsheet.png)]{.image} | Place a hierarchical subsheet. You must specify the file name |
|                                                                                              | for this subsheet.                                            |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/import_hierarchical_label_png](images/icons/import_hierarchical_label.png)]{.image} | Import a hierarchical pin from a subsheet. This command can   |
|                                                                                              | be executed only on hierarchical subsheets. It will create    |
|                                                                                              | hierarchical pins corresponding to hierarchical labels placed |
|                                                                                              | in the target subsheet.                                       |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_hierar_pin_png](images/icons/add_hierar_pin.png)]{.image}                       | Place a hierarchical pin in a subsheet. This command can be   |
|                                                                                              | executed only on hierarchical subsheets. It will create       |
|                                                                                              | arbitrary hierarchical pins, even if they do not exist in the |
|                                                                                              | target subsheet.                                              |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_dashed_line_png](images/icons/add_dashed_line.png)]{.image}                     | Draw a line. These are only graphical and do not connect      |
|                                                                                              | anything.                                                     |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/text.png](images/icons/text.png)]{.image}                                           | Place a text comment.                                         |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/image_png](images/icons/image.png)]{.image}                                         | Place a bitmap image.                                         |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/cancel_png](images/icons/delete.png)]{.image}                                       | Delete selected element.                                      |
+----------------------------------------------------------------------------------------------+---------------------------------------------------------------+
:::::

:::: sect2
### Left toolbar icons {#_left_toolbar_icons}

::: paragraph
This toolbar manages the display options:
:::

+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/grid](images/icons/grid.png)]{.image}                 | Toggle grid visibility.                                       |
+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/unit_inch](images/icons/unit_inch.png)]{.image}       | Switch units to inches.                                       |
+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/unit_mm](images/icons/unit_mm.png)]{.image}           | Switch units to millimeters.                                  |
+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/cursor_shape](images/icons/cursor_shape.png)]{.image} | Choose the cursor shape (full screen/small).                  |
+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/hidden_pin](images/icons/hidden_pin.png)]{.image}     | Toggle visibility of \"invisible\" pins.                      |
+----------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/lines90](images/icons/lines90.png)]{.image}           | Toggle free angle/90 degrees wires and buses placement.       |
+----------------------------------------------------------------+---------------------------------------------------------------+
::::

:::::::::::::: sect2
### Pop-up menus and quick editing

::: paragraph
A right-click opens a contextual menu for the selected element. This
contains:
:::

::: ulist
- Zoom factor.

- Grid adjustment.

- Commonly edited parameters of the selected element.
:::

::: paragraph
Pop-up without selected element.
:::

:::: imageblock
::: content
![eeschema_popup_without_element_png](images/eeschema_popup_without_element.png)
:::
::::

::: paragraph
Editing a label.
:::

:::: imageblock
::: content
![eeschema_popup_edit_label_png](images/eeschema_popup_edit_label.png)
:::
::::

::: paragraph
Editing a symbol.
:::

:::: imageblock
::: content
![eeschema_popup_edit_component_png](images/eeschema_popup_edit_component.png)
:::
::::
::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Main top menu

:::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2
### File menu

:::: imageblock
::: content
![File menu](images/en/menu_file.png)
:::
::::

+---------------------+------------------------------------------------+
| New                 | Close current schematic and start a new one    |
|                     | (only in standalone mode).                     |
+=====================+================================================+
| Open                | Load a schematic project (only in standalone   |
|                     | mode).                                         |
+---------------------+------------------------------------------------+
| Open Recent         | Open a schematic project from the list of      |
|                     | recently opened files (only in standalone      |
|                     | mode).                                         |
+---------------------+------------------------------------------------+
| Append Schematic    | Insert the contents of another sheet into the  |
| Sheet               | current one.                                   |
+---------------------+------------------------------------------------+
| Import Non-Kicad    | Imports a schematic project saved in another   |
| Schematic File      | file format.                                   |
+---------------------+------------------------------------------------+
| Save                | Save current sheet and all its subsheets.      |
+---------------------+------------------------------------------------+
| Save Current Sheet  | Save only the current sheet, but not others in |
|                     | the project.                                   |
+---------------------+------------------------------------------------+
| Save Current Sheet  | Save the current sheet under a new name.       |
| As...​               |                                                |
+---------------------+------------------------------------------------+
| Page Settings       | Configure page dimensions and title block.     |
+---------------------+------------------------------------------------+
| Print               | Print schematic project (See also chapter      |
|                     | [Plot and Print](#plot-and-print)).            |
+---------------------+------------------------------------------------+
| Plot                | Export to PDF, PostScript, HPGL or SVG format  |
|                     | (See chapter [Plot and                         |
|                     | Print](#plot-and-print)).                      |
+---------------------+------------------------------------------------+
| Close               | Terminate the application.                     |
+---------------------+------------------------------------------------+
:::::

::::::::::::::::::::::::::::::::::::::::: sect2
### Preferences menu

:::: imageblock
::: content
![Preferences menu](images/en/menu_preferences.png)
:::
::::

+--------------------+-------------------------------------------------+
| Manage Symbol      | Add/remove symbol libraries.                    |
| Library Tables     |                                                 |
+--------------------+-------------------------------------------------+
| Configure Paths    | Set the default search paths.                   |
+--------------------+-------------------------------------------------+
| General Options    | Preferences (units, grid size, field names,     |
|                    | etc.).                                          |
+--------------------+-------------------------------------------------+
| Set Language       | Select interface language.                      |
+--------------------+-------------------------------------------------+
| Icons Options      | Icons visibility settings.                      |
+--------------------+-------------------------------------------------+
| Import and Export  | Transfer preferences to/from file.              |
+--------------------+-------------------------------------------------+

::::::::::::::::: sect3
#### Manage Symbol Library Tables {#manage-sym-lib-table}

:::: imageblock
::: content
![Symbol Library Tables](images/en/options_symbol_lib.png)
:::
::::

::: paragraph
Eeschema uses two library tables to store the list of available symbol
libraries, which differ by the scope:
:::

::: ulist
- Global Libraries
:::

::: paragraph
Libraries listed in the Global Libraries table are available to every
project. They are saved in **sym-lib-table** in your home directory
(exact path is dependent on the operating system; check the path above
the table).
:::

::: ulist
- Project Specific Libraries
:::

::: paragraph
Libraries listed in Project Specific Libraries table are available to
the currently opened project. They are saved in **sym-lib-table** file
in the project directory (check the path above the table).
:::

::: paragraph
You can view either list by clicking on \"Global Libraries\" or
\"Project Specific Libraries\" tab below the library table.
:::

:::: sect4
##### Add a new library {#_add_a_new_library}

::: paragraph
Add a library either by clicking **Browse Libraries...​** button and
selecting a file or clicking \"Append Library\" and typing a path to a
library file. The selected library will be added to the currently opened
library table (Global/Project Specific).
:::
::::

:::: sect4
##### Remove a library {#_remove_a_library}

::: paragraph
Remove a library by selecting one or more libraries and clicking
**Remove Library** button.
:::
::::

:::: sect4
##### Library properties {#_library_properties}

::: paragraph
Each row in the table stores several fields describing a library:
:::

+--------------------+-------------------------------------------------+
| Active             | Enables/disables the library. It is useful to   |
|                    | temporarily reduce the loaded library set.      |
+--------------------+-------------------------------------------------+
| Nickname           | Nickname is a short, unique identifier used for |
|                    | assigning symbols to components. Symbols are    |
|                    | represented by \'\<Library Nickname\>:\<Symbol  |
|                    | Name\>\' strings.                               |
+--------------------+-------------------------------------------------+
| Library Path       | Path points to the library location.            |
+--------------------+-------------------------------------------------+
| Plugin Type        | Determines the library file format.             |
+--------------------+-------------------------------------------------+
| Options            | Stores library specific options, if used by     |
|                    | plugin.                                         |
+--------------------+-------------------------------------------------+
| Description        | Briefly characterizes the library contents.     |
+--------------------+-------------------------------------------------+
::::
:::::::::::::::::

::::::::::::::::::::::: sect3
#### General Options {#preferences-general-options}

::::: sect4
##### Display {#preferences-display}

:::: imageblock
::: content
![Display settings](images/en/options_display.png)
:::
::::

+---------------------------+------------------------------------------+
| Grid Size                 | Grid size selection.                     |
|                           |                                          |
|                           | It is **recommended** to work with       |
|                           | normal grid (0.050 inches or 1,27 mm).   |
|                           | Smaller grids are used for component     |
|                           | building.                                |
+---------------------------+------------------------------------------+
| Bus thickness             | Pen size used to draw buses.             |
+---------------------------+------------------------------------------+
| Line thickness            | Pen size used to draw objects that do    |
|                           | not have a specified pen size.           |
+---------------------------+------------------------------------------+
| Part ID notation          | Style of suffix that is used to denote   |
|                           | symbol units (U1A, U1.A, U1-1, etc.)     |
+---------------------------+------------------------------------------+
| Icon scale                | Adjust toolbar icons size.               |
+---------------------------+------------------------------------------+
| Show Grid                 | Grid visibility setting.                 |
+---------------------------+------------------------------------------+
| Restrict buses and wires  | If checked, buses and wires are drawn    |
| to H and V orientation    | only with vertical or horizontal lines.  |
|                           | Otherwise buses and wires can be placed  |
|                           | at any orientation.                      |
+---------------------------+------------------------------------------+
| Show hidden pins:         | Display invisible (or *hidden*) pins,    |
|                           | typically power pins.                    |
+---------------------------+------------------------------------------+
| Show page limits          | If checked, shows the page boundaries on |
|                           | screen.                                  |
+---------------------------+------------------------------------------+
| Footprint previews in     | Displays a footprint preview frame and   |
| symbol chooser            | footprint selector when placing a new    |
|                           | symbol.                                  |
|                           |                                          |
|                           | **Note:** it may cause problems or       |
|                           | delays, use at your own risk.            |
+---------------------------+------------------------------------------+
:::::

::::: sect4
##### Editing {#preferences-editing}

:::: imageblock
::: content
![Editing settings](images/en/options_editing.png)
:::
::::

+---------------------------+------------------------------------------+
| Measurement units         | Select the display and the cursor        |
|                           | coordinate units (inches or              |
|                           | millimeters).                            |
+---------------------------+------------------------------------------+
| Horizontal pitch of       | Increment on X axis during element       |
| repeated items            | duplication (default: 0) (after placing  |
|                           | an item like a symbol, label or wire, a  |
|                           | duplication is made by the *Insert* key) |
+---------------------------+------------------------------------------+
| Vertical pitch of         | Increment on Y axis during element       |
| repeated items            | duplication (default: 0.100 inches or    |
|                           | 2,54 mm).                                |
+---------------------------+------------------------------------------+
| Increment of repeated     | Increment of label value during          |
| labels                    | duplication of texts ending in a number, |
|                           | such as bus members (usual value 1 or    |
|                           | -1).                                     |
+---------------------------+------------------------------------------+
| Default text size         | Text size used when creating new text    |
|                           | items or labels.                         |
+---------------------------+------------------------------------------+
| Auto-save time interval   | Time in minutes between saving backups.  |
+---------------------------+------------------------------------------+
| Automatically place       | If checked, symbol fields (e.g. value    |
| symbol fields             | and reference) in newly placed symbols   |
|                           | might be moved to avoid collisions with  |
|                           | other items.                             |
+---------------------------+------------------------------------------+
| Allow field autoplace to  | Extension of \'Automatically place       |
| change justification      | symbol fields\' option. Enable text      |
|                           | justification adjustment for symbol      |
|                           | fields when placing a new part.          |
+---------------------------+------------------------------------------+
| Always align autoplaced   | Extension of \'Automatically place       |
| fields to the 50 mil grid | symbol fields\' option. If checked,      |
|                           | fields are autoplaced using 50 mils      |
|                           | grid, otherwise they are placed freely.  |
+---------------------------+------------------------------------------+
:::::

:::::::: sect4
##### Controls {#preferences-controls}

::: paragraph
Redefine hotkeys and set up the user interface behavior.
:::

:::: imageblock
::: content
![Controls settings](images/en/options_controls.png)
:::
::::

::: paragraph
Select a new hotkey by double clicking an action or right click on an
action to show a popup menu:
:::

+---------------------------+------------------------------------------+
| Edit                      | Define a new hotkey for the action (same |
|                           | as double click).                        |
+---------------------------+------------------------------------------+
| Undo Changes              | Reverts the recent hotkey changes for    |
|                           | the action.                              |
+---------------------------+------------------------------------------+
| Restore Default           | Sets the action hotkey to its default    |
|                           | value.                                   |
+---------------------------+------------------------------------------+
| Undo All Changes          | Reverts all recent hotkey changes for    |
|                           | the action.                              |
+---------------------------+------------------------------------------+
| Restore All to Default    | Sets all action hotkeys to their default |
|                           | values.                                  |
+---------------------------+------------------------------------------+

::: paragraph
Options description:
:::

+---------------------------+------------------------------------------+
| Center and warp cursor on | If checked, the pointed location is      |
| zoom                      | warped to the screen center when zooming |
|                           | in/out.                                  |
+---------------------------+------------------------------------------+
| Use touchpad to pan       | When enabled, view is panned using       |
|                           | scroll wheels (or touchpad gestures) and |
|                           | to zoom one needs to hold Ctrl.          |
|                           | Otherwise scroll wheels zoom in/out and  |
|                           | Ctrl/Shift are the panning modifiers.    |
+---------------------------+------------------------------------------+
| Pan while moving object   | If checked, automatically pans the       |
|                           | window if the cursor leaves the window   |
|                           | during drawing or moving.                |
+---------------------------+------------------------------------------+
::::::::

:::::: sect4
##### Colors {#preferences-colors}

::: paragraph
Color scheme for various graphic elements. Click on any of the color
swatches to select a new color for a particular element.
:::

:::: imageblock
::: content
![Color settings](images/en/options_color.png)
:::
::::
::::::

:::::: sect4
##### Default Fields {#preferences-default-fields}

::: paragraph
Define additional custom fields and corresponding values that will
appear in newly placed symbols.
:::

:::: imageblock
::: content
![Default Fields settings](images/en/options_default_fields.png)
:::
::::
::::::
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::

::::: sect2
### Help menu

::: paragraph
Access to on-line help (this document) for an extensive tutorial about
KiCad.
:::

::: paragraph
Use \`\`Copy Version Information\'\' when submitting bug reports to
identify your build and system.
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## General Top Toolbar

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::: sect2
### Sheet management

::: paragraph
The Sheet Settings icon ([![Sheet Settings
icon](images/icons/sheetset.png)]{.image}) allows you to define the
sheet size and the contents of the title block.
:::

:::: imageblock
::: content
![Page Settings](images/en/page_settings.png)
:::
::::

::: paragraph
Sheet numbering is automatically updated. You can set the date to today
by pressing the left arrow button by \"Issue Date\", but it will not be
automatically changed.
:::
:::::::

::::::: sect2
### Search tool

::: paragraph
The Find icon ([![Find icon](images/icons/find.png)]{.image}) can be
used to access the search tool.
:::

:::: imageblock
::: content
![Find dialog](images/en/find_dialog.png)
:::
::::

::: paragraph
You can search for a reference, a value or a text string in the current
sheet or in the whole hierarchy. Once found, the cursor will be
positioned on the found element in the relevant sub-sheet.
:::
:::::::

::::::::::::::: sect2
### Netlist tool

::: paragraph
The Netlist icon ([![Netlist icon](images/icons/netlist.png)]{.image})
opens the netlist generation tool.
:::

::: paragraph
The tool creates a file which describe all connections in the entire
hierarchy.
:::

::: paragraph
In a multisheet hierarchy, any local label is visible only inside the
sheet to which it belongs. For example: the label LABEL1 of sheet 3 is
different from the label LABEL1 of sheet 5 (if no connection has been
intentionally introduced to connect them). This is due to the fact that
the sheet name path is internally associated with the local label.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | Even though there is no text      |
| Note                              | length limit for labels in        |
| :::                               | Eeschema, please take into        |
|                                   | account that other programs       |
|                                   | reading the generated netlist may |
|                                   | have such constraints.            |
+-----------------------------------+-----------------------------------+
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | Avoid spaces in labels, because   |
| Note                              | they will appear as separated     |
| :::                               | words in the generated file. It   |
|                                   | is not a limitation of Eeschema,  |
|                                   | but of many netlist formats,      |
|                                   | which often assume that a label   |
|                                   | has no spaces.                    |
+-----------------------------------+-----------------------------------+
:::

:::: imageblock
::: content
![Netlist dialog](images/en/netlist_dialog.png)
:::
::::

::: paragraph
Option:
:::

+---------------------------+------------------------------------------+
| Default Format            | Check to select Pcbnew as the default    |
|                           | format.                                  |
+---------------------------+------------------------------------------+

::: paragraph
Other formats can also be generated:
:::

::: ulist
- Orcad PCB2

- CadStar

- Spice (simulators)
:::

::: paragraph
External plugins can be added to extend the netlist formats list
(PadsPcb Plugin was added in the picture above).
:::

::: paragraph
There is more information about creating netlists in [Create a
Netlist](#create-a-netlist) chapter.
:::
:::::::::::::::

::::::::::::: sect2
### Annotation tool

::: paragraph
The icon [![icons_annotate_png](images/icons/annotate.png)]{.image}
launches the annotation tool. This tool assigns references to
components.
:::

::: paragraph
For multi-part components (such as 7400 TTL which contains 4 gates), a
multi-part suffix is also allocated (thus a 7400 TTL designated U3 will
be divided into U3A, U3B, U3C and U3D).
:::

::: paragraph
You can unconditionally annotate all the components or only the new
components, i.e. those which were not previously annotated.
:::

:::: imageblock
::: content
![annotate-dialog_img](images/en/annotate-dialog.png)
:::
::::

::: paragraph
**Scope**
:::

+---------------------------+------------------------------------------+
| Use the entire schematic  | All sheets are re-annotated (default).   |
+===========================+==========================================+
| Use the current page only | Only the current sheet is re-annotated   |
|                           | (this option is to be used only in       |
|                           | special cases, for example to evaluate   |
|                           | the amount of resistors in the current   |
|                           | sheet.).                                 |
+---------------------------+------------------------------------------+
| Keep existing annotation  | Conditional annotation, only the new     |
|                           | components will be re-annotated          |
|                           | (default).                               |
+---------------------------+------------------------------------------+
| Reset existing annotation | Unconditional annotation, all the        |
|                           | components will be re-annotated (this    |
|                           | option is to be used when there are      |
|                           | duplicated references).                  |
+---------------------------+------------------------------------------+
| Reset, but do not swap    | Keeps all groups of multiple units (e.g. |
| any annotated multi-unit  | U2A, U2B) together when reannotating.    |
| parts                     |                                          |
+---------------------------+------------------------------------------+

::: paragraph
**Annotation Order**
:::

::: paragraph
Selects the order in which components will be numbered (either
horizontally or vertically).
:::

::: paragraph
**Annotation Choice**
:::

::: paragraph
Selects the assigned reference format.
:::
:::::::::::::

:::::::::::::::::::::: sect2
### Electrical Rules Check tool

::: paragraph
The icon [![ERC icon](images/icons/erc.png)]{.image} launches the
electrical rules check (ERC) tool.
:::

::: paragraph
This tool performs a design verification and is able to detect forgotten
connections, and inconsistencies.
:::

::: paragraph
Once you have run the ERC, Eeschema places markers to highlight
problems. The error description is displayed after left clicking on the
marker. An error report file can also be generated.
:::

:::::::::: sect3
#### Main ERC dialog

:::: imageblock
::: content
![ERC dialog](images/en/dialog_erc.png)
:::
::::

::: paragraph
Errors are displayed in the Electrical Rules Checker dialog:
:::

::: ulist
- Total count of errors and warnings.

- Errors count.

- Warnings count.
:::

::: paragraph
Option:
:::

+---------------------------+------------------------------------------+
| Create ERC file report    | Check this option to generate an ERC     |
|                           | report file.                             |
+---------------------------+------------------------------------------+

::: paragraph
Commands:
:::

+---------------------------+------------------------------------------+
| Delete Markers            | Remove all ERC error/warnings markers.   |
+---------------------------+------------------------------------------+
| Run                       | Start an Electrical Rules Check.         |
+---------------------------+------------------------------------------+
| Close                     | Close the dialog.                        |
+---------------------------+------------------------------------------+

::: {.ulist .NOTE}
- Clicking on an error message jumps to the corresponding marker in the
  schematic.
:::
::::::::::

:::::::::: sect3
#### ERC options dialog

:::: imageblock
::: content
![ERC Options dialog](images/en/dialog_erc_opts.png)
:::
::::

::: paragraph
This tab allows you to define the connectivity rules between pins; you
can choose between 3 options for each case:
:::

::: ulist
- No error

- Warning

- Error
:::

::: paragraph
Each square of the matrix can be modified by clicking on it.
:::

::: paragraph
Option:
:::

+---------------------------+------------------------------------------+
| Test similar labels       | Report labels that differ only by letter |
|                           | case (e.g. label/Label/LaBeL). Net names |
|                           | are case-sensitive therefore such labels |
|                           | are treated as separate nets.            |
+---------------------------+------------------------------------------+
| Test unique global labels | Report global lables that occur only     |
|                           | once for a particular net. Normally it   |
|                           | is required to have at least two make a  |
|                           | connection.                              |
+---------------------------+------------------------------------------+

::: paragraph
Commands:
:::

+---------------------------+------------------------------------------+
| Initialize to Default     | Restores the original settings.          |
+---------------------------+------------------------------------------+
::::::::::
::::::::::::::::::::::

::::::::::::::: sect2
### Bill of Material tool

::: paragraph
The icon [![BOM icon](images/icons/bom.png)]{.image} launches the bill
of materials (BOM) generator. This tool generates a file listing the
components and/or hierarchical connections (global labels).
:::

:::: imageblock
::: content
![BOM dialog](images/en/dialog_bom.png)
:::
::::

::: paragraph
Eeschema's BOM generator makes use of external plugins, either as XSLT
or Python scripts. There are a few examples installed inside the KiCad
program files directory.
:::

::: paragraph
A useful set of component properties to use for a BOM are:
:::

::: ulist
- Value - unique name for each part used.

- Footprint - either manually entered or back-annotated (see below).

- Field1 - Manufacturer's name.

- Field2 - Manufacturer's Part Number.

- Field3 - Distributor's Part Number.
:::

::: paragraph
For example:
:::

:::: imageblock
::: content
![Component Properties
dialog](images/en/dialog_component_properties.png)
:::
::::

::: paragraph
On **MS Windows**, BOM generator dialog has a special option (pointed by
red arrow) that controls visibility of external plugin window.\
By default, BOM generator command is executed console window hidden and
output is redirected to *Plugin info* field. Set this option to show the
window of the running command. It may be necessary if plugin has
provides a graphical user interface.
:::

:::: imageblock
::: content
![BOM dialog extra option on MS
Windows](images/bom_extra_option_windows.png)
:::
::::
:::::::::::::::

:::::::::: sect2
### Edit Fields tool

::: paragraph
The icon [![Edit Fields icon](images/icons/spreadsheet.png)]{.image}
opens a spreadsheet to view and modify field values for all symbols.
:::

::: paragraph
[![Symbol Dialog](images/en/dialog_edit_fields.png)]{.image}
:::

::: paragraph
Once you modify field values, you need to either accept changes by
clicking on \'Apply\' button or undo them by clicking on \'Revert\'
button.
:::

:::::: sect3
#### Tricks to simplify fields filling

::: paragraph
There are several special copy/paste methods in spreadsheet. They may be
useful when entering field values that are repeated in a few components.
:::

::: paragraph
These methods are illustrated below.
:::

+--------------------------------------------+-------------------------------------------------+---------------------------------------------+
| Copy (Ctrl+C)                              | Selection                                       | Paste (Ctrl+V)                              |
+============================================+=================================================+=============================================+
| [![1copy](images/copypaste11.png)]{.image} | [![1selection](images/copypaste12.png)]{.image} | [![1paste](images/copypaste13.png)]{.image} |
+--------------------------------------------+-------------------------------------------------+---------------------------------------------+
| [![2copy](images/copypaste21.png)]{.image} | [![2selection](images/copypaste22.png)]{.image} | [![2paste](images/copypaste23.png)]{.image} |
+--------------------------------------------+-------------------------------------------------+---------------------------------------------+
| [![3copy](images/copypaste31.png)]{.image} | [![3selection](images/copypaste32.png)]{.image} | [![3paste](images/copypaste33.png)]{.image} |
+--------------------------------------------+-------------------------------------------------+---------------------------------------------+
| [![4copy](images/copypaste41.png)]{.image} | [![4selection](images/copypaste42.png)]{.image} | [![4paste](images/copypaste43.png)]{.image} |
+--------------------------------------------+-------------------------------------------------+---------------------------------------------+
| [![5copy](images/copypaste51.png)]{.image} | [![5selection](images/copypaste52.png)]{.image} | [![5paste](images/copypaste53.png)]{.image} |
+--------------------------------------------+-------------------------------------------------+---------------------------------------------+

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | These techniques are also         |
| Note                              | available in other dialogs with a |
| :::                               | grid control element.             |
+-----------------------------------+-----------------------------------+
:::
::::::
::::::::::

:::::: sect2
### Import tool for footprint assignment

::::: sect3
#### Access:

::: paragraph
The icon [![Import Footprint Names
icon](images/icons/import_footprint_names.png)]{.image} launches the
back-annotate tool.
:::

::: paragraph
This tool allows footprint changes made in PcbNew to be imported back
into the footprint fields in Eeschema.
:::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::: sect1
## Manage Symbol Libraries {#_manage_symbol_libraries}

::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Symbol libraries hold collections of symbols used when creating
schematics. Each symbol in a schematic is uniquely identified by a full
name that is composed of a library nickname and a symbol name. An
example is `Audio:AD1853`.
:::

::::::::::::::::::::::::::::::::::::::: sect2
### Symbol Library Table {#_symbol_library_table}

::: paragraph
The symbol library table holds a list of all library files KiCad knows
about. The symbol library table is constructed from the global symbol
library table file and the project specific symbol library table file.
:::

::: paragraph
When a symbol is loaded, Eeschema uses the library nickname, `Audio` in
our example, to lookup the library location in the symbol library table.
:::

::: paragraph
The image below shows the symbol library table editing dialog which can
be opened by invoking the
`Manage Symbol Library Tables` entry in the `Preferences` menu.
:::

:::: imageblock
::: content
![sym lib table dlg](images/en/options_symbol_lib.png)
:::
::::

:::: sect3
#### Global Symbol Library Table {#_global_symbol_library_table}

::: paragraph
The global symbol library table contains the list of libraries that are
always available regardless of the currently loaded project file. The
table is saved in the file sym-lib-table in the user's home folder. The
location of this folder is dependent upon the operating system being
used.
:::
::::

:::: sect3
#### Project Specific Symbol Library Table {#_project_specific_symbol_library_table}

::: paragraph
The project specific symbol library table contains the list of libraries
that are available specifically for the currently loaded project file.
The project specific symbol library table can only be edited when it is
loaded along with the project file. If no project file is loaded or
there is no symbol library table file in the current project path, an
empty table is created which can be edited and later saved along with
the project file.
:::
::::

::::: sect3
#### Initial Configuration {#_initial_configuration}

::: paragraph
The first time Eeschema is run and the global symbol table file
**sym-lib-table** is not found in the user's home folder, Eeschema will
attempt to copy the default symbol table file sym-lib-table stored in
the system's KiCad template folder to the file sym-lib-table in the
user's home folder. If the default template sym-lib-table file cannot be
found, a dialog will prompt for an alternate location for the
sym-lib-table file. If no sym-lib-table is found or the dialog is
dismissed, an empty symbol library table will be created in the user's
home folder. If this happens, the user can either copy sym-lib-table
manually or configure the table by hand.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | The default symbol library table  |
| :::                               | includes all of the symbol        |
|                                   | libraries that are installed as   |
|                                   | part of KiCad. This may or may    |
|                                   | not be desirable depending on     |
|                                   | usages and the speed of the       |
|                                   | system. The amount of time        |
|                                   | required to load the symbol       |
|                                   | libraries is proportional to the  |
|                                   | number of libraries in the symbol |
|                                   | library table. If symbol library  |
|                                   | load times are excessive, remove  |
|                                   | rarely and/or never used          |
|                                   | libraries from the global library |
|                                   | table and add them to the project |
|                                   | library table as required.        |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::::

::::::::: sect3
#### Adding Table Entries {#_adding_table_entries}

::: paragraph
In order to use a symbol library, it must first be added to either the
global table or the project specific table. The project specific table
is only applicable when you have a project file open.
:::

::: paragraph
**Each library entry must have a unique nickname.**
:::

::: paragraph
This does not have to be related in any way to the actual library file
name or path. The colon \':\' and \'/\' characters cannot be used
anywhere in the library nickname. Each library entry must have a valid
path and/or file name depending on the type of library. Paths can be
defined as absolute, relative, or by environment variable substitution
(see section below).
:::

::: paragraph
The appropriate plug in type must be selected in order for the library
to be properly read. KiCad currently supports only legacy symbol library
files plug-in.
:::

::: paragraph
There is also a description field to add a description of the library
entry. The option field is not used at this time so adding options will
have no effect when loading libraries.
:::

::: ulist
- Please note that you cannot have duplicate library nicknames in the
  same table. However, you can have duplicate library nicknames in both
  the global and project specific symbol library table.

- The project specific table entry will take precedence over the global
  table entry when duplicate nicknames occur.

- When entries are defined in the project specific table, a
  sym-lib-table file containing the entries will be written into the
  folder of the currently open project file.
:::
:::::::::

:::::::: sect3
#### Environment Variable Substitution {#_environment_variable_substitution}

::: paragraph
One of the most powerful features of the symbol library table is
environment variable substitution. This allows for definition of custom
paths to where symbol libraries are stored in environment variables.
Environment variable substitution is supported by using the syntax
\$\\{ENV_VAR_NAME\\} in the library path.
:::

::: paragraph
By default, at run time KiCad defines **two environment variables**:
:::

::: ulist
- the **KIPRJMOD** environment variable that always points to the
  currently open project directory. **KIPRJMOD** cannot be modified.

- the **KICAD_SYMBOL_DIR** environment variable. This points to the path
  where the default symbol libraries that were installed with KiCad.
:::

::: paragraph
You can override KICAD_SYMBOL_DIR by defining it yourself in
preferences/ Configure Path which allows you to substitute your own
libraries in place of the default KiCad symbol libraries.
:::

::: paragraph
**KIPRJMOD** allows you to store libraries in the project path without
having to define the absolute path (which is not always known) to the
library in the project specific symbol library table.
:::
::::::::

::::::: sect3
#### Usage Patterns {#_usage_patterns}

::: paragraph
Symbol libraries can be defined either globally or specifically to the
currently loaded project. Symbol libraries defined in the user's global
table are always available and are stored in the sym-lib-table file in
the user's home folder. The project specific symbol library table is
active only for the currently open project file.
:::

::: paragraph
There are advantages and disadvantages to each method. Defining all
libraries in the global table means they will always be available when
needed. The disadvantage of this is that load time will increase.
:::

::: paragraph
Defining all symbol libraries on a project specific basis means that you
only have the libraries required for the project which decreases symbol
library load times. The disadvantage is that you always have to remember
to add each symbol library that you need for every project.
:::

::: paragraph
One usage pattern would be to define commonly used libraries globally
and the libraries only required for the project in the project specific
library table. There is no restriction on how to define libraries.
:::
:::::::

:::::::: sect3
#### Legacy Project Remapping {#_legacy_project_remapping}

::: paragraph
When loading a schematic created prior to the symbol library table
implementation, Eeschema will attempt to remap the symbol library links
in the schematic to the appropriate library table symbols. The success
of this process is dependent on several factors:
:::

::: ulist
- the original libraries used in the schematic are still available and
  unchanged from when the symbol was added to the schematic.

- all rescue operations were performed when detected to create a rescue
  library or keep the existing rescue library up to date.

- the integrity of the project symbol cache library has not been
  corrupted.
:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Warning                           | The remapping will make a back up |
| :::                               | of all the files that are changed |
|                                   | during remapping in the           |
|                                   | rescue-backup folder in the       |
|                                   | project folder. Always make a     |
|                                   | back up of your project before    |
|                                   | remapping just in case something  |
|                                   | goes wrong.                       |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Warning                           | The rescue operation is performed |
| :::                               | even if it has been disabled to   |
|                                   | ensure the correct symbols are    |
|                                   | available for remapping. Do not   |
|                                   | cancel this operation or the      |
|                                   | remapping will fail to correctly  |
|                                   | remap schematics symbols. Any     |
|                                   | broken symbol links will have to  |
|                                   | be fixed manually.                |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | If the original libraries have    |
| :::                               | been removed and the rescue was   |
|                                   | not performed, the cache library  |
|                                   | can be used as a recovery library |
|                                   | as a last resort. Copy the cache  |
|                                   | library to a new file name and    |
|                                   | add the new library file to the   |
|                                   | top of the library list using a   |
|                                   | version of Eeschema prior to the  |
|                                   | symbol library table              |
|                                   | implementation.                   |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
::::::::
:::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Schematic Creation and Editing

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2
### Introduction {#_introduction}

::: paragraph
A schematic can be represented by a single sheet, but, if big enough, it
will require several sheets.
:::

::: paragraph
A schematic represented by several sheets is hierarchical, and all its
sheets (each one represented by its own file) constitute an Eeschema
project. The manipulation of hierarchical schematics will be described
in the [Hierarchical Schematics](#hierarchical-schematics) chapter.
:::
:::::

:::::: sect2
### General considerations

::: paragraph
A schematic designed with Eeschema is more than a simple graphic
representation of an electronic device. It is normally the entry point
of a development chain that allows for:
:::

::: ulist
- Validating against a set of rules ([Electrical Rules Check](#erc)) to
  detect errors and omissions.

- Automatically generating a bill of materials
  ([BOM](#creating-customized-netlists-and-bom-files)).

- [Generating a netlist](#creating-customized-netlists-and-bom-files)
  for simulation software such as SPICE.

- [Generating a netlist](#creating-customized-netlists-and-bom-files)
  for transferring to PCB layout.
:::

::: paragraph
A schematic mainly consists of symbols, wires, labels, junctions, buses
and power ports. For clarity in the schematic, you can place purely
graphical elements like bus entries, comments, and polylines.
:::
::::::

:::::: sect2
### The development chain

:::: imageblock
::: content
![dev-chain_png](images/en/dev-chain.png)
:::
::::

::: paragraph
Symbols are added to the schematic from symbol libraries. After the
schematic is made, a netlist is generated, which is later used to import
the set of connections and footprints into PcbNew.
:::
::::::

:::::::::::::::::::::::::::::: sect2
### Symbol placement and editing {#component-placement-and-editing}

:::::::::::: sect3
#### Find and place a symbol {#find-and-place-a-component}

::: paragraph
To load a symbol into your schematic you can use the icon [![New Symbol
icon](images/icons/new_symbol.png)]{.image}. A dialog box allows you to
type the name of the symbol to load.
:::

:::: imageblock
::: content
![Choose Component dialog](images/en/dialog_choose_component.png)
:::
::::

::: paragraph
The Choose Symbols dialog will filter symbols by name, keywords, and
description according to what you type into the search field. Advanced
filters can be used just by typing them:
:::

::: ulist
- **Wildcards:** use the characters `?` and `*` respectively to mean
  \"any character\" and \"any number of characters\".

- **Relational:** if a library part's description or keywords contain a
  tag of the format \"Key:123\", you can match relative to that by
  typing \"Key\>123\" (greater than), \"Key\<123\" (less than), etc.
  Numbers may include one of the following case-insensitive suffixes:

  +---------+--------+--------+--------+--------+--------+--------+--------+
  | p       | n      | u      | m      | k      | meg    | g      | t      |
  +---------+--------+--------+--------+--------+--------+--------+--------+
  | 10^-12^ | 10^-9^ | 10^-6^ | 10^-3^ | 10^3^  | 10^6^  | 10^9^  | 10^12^ |
  +---------+--------+--------+--------+--------+--------+--------+--------+

  +-----------------+-----------------+-----------------+-----------------+
  | ki              | mi              | gi              | ti              |
  +-----------------+-----------------+-----------------+-----------------+
  | 2^10^           | 2^20^           | 2^30^           | 2^40^           |
  +-----------------+-----------------+-----------------+-----------------+

- **Regular expression:** if you're familiar with regular expressions,
  these can be used too. The regular expression flavor used is the
  [wxWidgets Advanced Regular Expression
  style](http://docs.wxwidgets.org/3.0/overview_resyntax.html), which is
  similar to Perl regular expressions.
:::

::: paragraph
Before placing the symbol in the schematic, you can rotate it, mirror
it, and edit its fields, by either using the hotkeys or the right-click
context menu. This can be done the same way after placement.
:::

::: paragraph
Here is a symbol during placement:
:::

:::: imageblock
::: content
![component during placement](images/en/component_during_placement.png)
:::
::::
::::::::::::

:::: sect3
#### Power ports

::: paragraph
A power port symbol is a symbol (the symbols are grouped in the "power"
library), so they can be placed using the symbol chooser. However, as
power placements are frequent, the [![Add Power
icon](images/icons/add_power.png)]{.image} tool is available. This tool
is similar, except that the search is done directly in the \`\`power\'\'
library.
:::
::::

::::::::::::::::: sect3
#### Symbol Editing and Modification (already placed component) {#component-editing-and-modification-already-placed-component}

::: paragraph
There are two ways to edit a symbol:
:::

::: ulist
- Modification of the symbol itself: position, orientation, unit
  selection on a multi-unit symbol.

- Modification of one of the fields of the symbol: reference, value,
  footprint, etc.
:::

::: paragraph
When a symbol has just been placed, you may have to modify its value
(particularly for resistors, capacitors, etc.), but it is useless to
assign to it a reference number right away, or to select the unit
(except for components with locked units, which you have to assign
manually). This can be done automatically by the annotation function.
:::

::::: sect4
##### Symbol modification {#component-modification}

::: paragraph
To modify some feature of a symbol, position the cursor on the symbol,
and then either:
:::

::: ulist
- Double-click on the symbol to open the full editing dialog.

- Right-click to open the context menu and use one of the commands:
  Move, Orientation, Edit, Delete, etc.
:::
:::::

:::::::::: sect4
##### Text fields modification

::: paragraph
You can modify the reference, value, position, orientation, text size
and visibility of the fields:
:::

::: ulist
- Double-click on the text field to modify it.

- Right-click to open the context menu and use one of the commands:
  Move, Rotate, Edit, Delete, etc.
:::

::: paragraph
For more options, or in order to create fields, double-click on the
symbol to open the Symbol Properties dialog.
:::

:::: imageblock
::: content
![Component Properties
dialog](images/en/dialog_component_properties.png)
:::
::::

::: paragraph
Each field can be visible or hidden, and displayed horizontally or
vertically. The displayed position is always indicated for a normally
displayed symbol (no rotation or mirroring) and is relative to the
anchor point of the symbol.
:::

::: paragraph
The option "Reset to Library Defaults" sets the symbol to the original
orientation, and resets the options, size and position of each field.
However, texts fields are not modified because this could break the
schematic.
:::
::::::::::
:::::::::::::::::
::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2
### Wires, Buses, Labels, Power ports

:::::: sect3
#### Overview

::: paragraph
All these drawing elements can also be placed with the tools on the
vertical right toolbar.
:::

::: paragraph
These elements are:
:::

::: ulist
- **Wires:** most connections between symbols.

- **Buses:** to graphically join bus labels

- **Polylines:** for graphic presentation.

- **Junctions:** to create connections between crossing wires or buses.

- **Bus entries:** to show connections between wires and buses.

- **Labels:** for labeling or creating connections.

- **Global labels:** for connections between sheets.

- **Texts:** for comments and annotations.

- **\"No Connect\" flags:** to terminate a pin that does not need any
  connection.

- **Hierarchical sheets**, and their connection pins.
:::
::::::

::::::::::::::::::: sect3
#### Connections (Wires and Labels)

::: paragraph
There are two ways to establish connection:
:::

::: ulist
- Pin to pin wires.

- Labels.
:::

::: paragraph
The following figure shows the two methods:
:::

:::: imageblock
::: content
![Wires labels](images/wires_labels.png)
:::
::::

::: paragraph
**Note 1:**
:::

::: paragraph
The point of "contact" of a label is the lower left corner of the first
letter of the label. This point is displayed with a small square when
not connected.
:::

::: paragraph
This point must thus be in contact with the wire, or be superimposed at
the end of a pin so that the label is seen as connected.
:::

::: paragraph
**Note 2:**
:::

::: paragraph
To establish a connection, a segment of wire must be connected by its
ends to an another segment or to a pin.
:::

::: paragraph
If there is overlapping (if a wire passes over a pin, but without being
connected to the pin end) there is no connection.
:::

::: paragraph
**Note 3:**
:::

::: paragraph
Wires that cross are not implicitly connected. It is necessary to join
them with a junction dot if a connection is desired.
:::

::: paragraph
The previous figure (wires connected to DB25FEMALE pins 22, 21, 20, 19)
shows such a case of connection using a junction symbol.
:::

::: paragraph
**Note 4:**
:::

::: paragraph
A signal can only have one name. If two different labels are placed on
the same wire (or connected wires), an ERC error will be generated.
:::
:::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: sect3
#### Connections (Buses)

::: paragraph
In the following schematic, many pins are connected to buses.
:::

:::: imageblock
::: content
![Example schematic with buses](images/sch_with_buses.png)
:::
::::

::::::::::: sect4
##### Bus members

::: paragraph
Buses are a way to group related signals in the schematic in order to
simplify complicated designs. Buses can be drawn like wires using the
bus tool, and are named using labels the same way signal wires are.
There are two types of bus in KiCad 6.0 and later: vector buses and
group buses.
:::

::: paragraph
A **vector bus** is a collection of signals that start with a common
prefix and end with a number. Vector buses are named `<PREFIX>[M..N]`
where `PREFIX` is any valid signal name, `M` is the first suffix number,
and `N` is the last suffix number. For example, the bus `DATA[0..7]`
contains the signals `DATA0`, `DATA1`, and so on up to `DATA7`. It
doesn't matter which order `M` and `N` are specified in, but both must
be non-negative.
:::

::: paragraph
A **group bus** is a collection of one or more signals and/or vector
buses. Group buses can be used to bundle together related signals even
when they have different names. Group buses use a special label syntax:
:::

::: paragraph
`<OPTIONAL_NAME>{SIGNAL1 SIGNAL2 SIGNAL3}`
:::

::: paragraph
The members of the group are listed inside curly braces (`{}`) separated
by space characters. An optional name for the group goes before the
opening curly brace. If the group bus is unnamed, the resulting nets on
the PCB will just be the signal names inside the group. If the group bus
has a name, the resulting nets will have the name as a prefix, with a
period (`.`) separating the prefix from the signal name.
:::

::: paragraph
For example, the bus `{SCL SDA}` has two signal members, and in the
netlist these signals will be `SCL` and `SDA`. The bus `USB1{DP DM}`
will generate nets called `USB1.DP` and `USB1.DM`. For designs with
larger buses that are repeated across several similar circuits, using
this technique can save time.
:::

::: paragraph
Group buses can also contain vector buses. For example, the bus
`MEMORY{A[7..0] D[7..0] OE WE}` contains both vector buses and plain
signals, and will result in nets such as `MEMORY.A7` and `MEMORY.OE` on
the PCB.
:::

::: paragraph
Bus wires can be drawn and connected in the same manner as signal wires,
including using junctions to create connections between crossing wires.
Like signals, buses cannot have more than one name --- if two
conflicting labels are attached to the same bus, an ERC error will be
generated.
:::
:::::::::::

:::::::: sect4
##### Connections between bus members

::: paragraph
Pins connected between the same members of a bus must be connected by
labels. It is not possible to connect a pin directly to a bus; this type
of connection will be ignored by Eeschema.
:::

::: paragraph
In the example above, connections are made by the labels placed on wires
connected to the pins. Bus entries (wire segments at 45 degrees) to
buses are graphical only, and are not necessary to form logical
connections.
:::

::: paragraph
In fact, using the repetition command (*Insert* key), connections can be
very quickly made in the following way, if component pins are aligned in
increasing order (a common case in practice on components such as
memories, microprocessors...​):
:::

::: ulist
- Place the first label (for example PCA0)

- Use the repetition command as much as needed to place members.
  Eeschema will automatically create the next labels (PCA1, PCA2...​)
  vertically aligned, theoretically on the position of the other pins.

- Draw the wire under the first label. Then use the repetition command
  to place the other wires under the labels.

- If needed, place the bus entries by the same way (Place the first
  entry, then use the repetition command).
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | In the Preferences/Options menu,  |
| :::                               | you can set the repetition        |
|                                   | parameters:                       |
|                                   | :::                               |
|                                   |                                   |
|                                   | ::: ulist                         |
|                                   | - Vertical step.                  |
|                                   |                                   |
|                                   | - Horizontal step.                |
|                                   |                                   |
|                                   | - Label increment (which can thus |
|                                   |   be incremented by 2, 3. or      |
|                                   |   decremented).                   |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
::::::::

::::: sect4
##### Bus unfolding

::: paragraph
The unfold tool allows you to quickly break out signals from a bus. To
unfold a signal, right-click on a bus object (a bus wire, etc) and
choose `Unfold Bus`. Alternatively, use the `Unfold Bus` hotkey
(default: `D`) when the cursor is over a bus object. The menu allows you
to select which bus member to unfold.
:::

::: paragraph
After selecting the bus member, the next click will place the bus member
label at the desired location. The tool automatically generates a bus
entry and wire leading up to the label location. After placing the
label, you can continue placing additional wire segments (for example,
to connect to a component pin) and complete the wire in any of the
normal ways.
:::
:::::

:::::::::: sect4
##### Bus aliases

::: paragraph
Bus aliases are shortcuts that allow you to work with large group buses
more efficiently. They allow you to define a group bus and give it a
short name that can then be used instead of the full group name across
the schematic.
:::

::: paragraph
To create bus aliases, open the `Bus Definitions` dialog in the `Tools`
menu.
:::

:::: imageblock
::: content
![Bus Definitions Dialog](images/en/dialog_bus_definitions.png)
:::
::::

::: paragraph
An alias may be named any valid signal name. Using the dialog, you can
add signals or vector buses to the alias. As a shortcut, you can type or
paste in a list of signals and/or buses separated by spaces, and they
will all be added to the alias definition. In this example, we define an
alias called `USB` with members `DP`, `DM`, and `VBUS`.
:::

::: paragraph
After defining an alias, it can be used in a group bus label by putting
the alias name inside the curly braces of the group bus: `{USB}`. This
has the same effect as labeling the bus `{DP DM VBUS}`. You can also add
a prefix name to the group, such as `USB1{USB}`, which results in nets
such as `USB1.DP` as described above. For complicated buses, using
aliases can make the labels on your schematic much shorter. Keep in mind
that the aliases are just a shortcut, and the name of the alias is not
included in the netlist.
:::

::: paragraph
Bus aliases are saved in the schematic file. Any aliases created in a
given schematic sheet are available to use in any other schematic sheet
that is in the same hierarchical design.
:::
::::::::::

:::::::: sect4
##### Buses with more than one label {#bus-migration}

::: paragraph
KiCad 5.0 and earlier allowed the connection of bus wires with different
labels together, and would join the members of these buses during
netlisting. This behavior has been removed in KiCad 6.0 because it is
incompatible with group buses, and also leads to confusing netlists
because the name that a given signal will receive is not easily
predicted.
:::

::: paragraph
If you open a design that made use of this feature in a modern version
of KiCad, you will see the Migrate Buses dialog which guides you through
updating the schematic so that only one label exists on any given set of
bus wires.
:::

:::: imageblock
::: content
![Bus Migration Dialog](images/en/dialog_migrate_buses.png)
:::
::::

::: paragraph
For each set of bus wires that has more than one label, you must choose
the label to keep. The drop-down name box lets you choose between the
labels that exist in the design, or you can choose a different name by
manually entering it into the new name field.
:::
::::::::
::::::::::::::::::::::::::::::::::::::

:::::::::::::::: sect3
#### Power ports connection

::: paragraph
When the power pins of the symbols are visible, they must be connected,
as for any other signal.
:::

::: paragraph
Symbols such as gates and flip-flops may have invisible power pins. Care
must be taken with these because:
:::

::: ulist
- You cannot connect wires, because of their invisibility.

- You do not know their names.
:::

::: paragraph
And moreover, it would be a bad idea to make them visible and to connect
them like the other pins, because the schematic would become unreadable
and not in accordance with usual conventions.
:::

::: {.admonitionblock .note}
+-----------------------------------+--------------------------------------------+
| ::: title                         | If you want to enforce the display of      |
| Note                              | these invisible power pins, you must check |
| :::                               | the option \`\`Show invisible power        |
|                                   | pins\'\' in the Preferences/Options dialog |
|                                   | box of the main menu, or the icon          |
|                                   | [![hidden                                  |
|                                   | pin](images/icons/hidden_pin.png)]{.image} |
|                                   | on the left (options) toolbar.             |
+-----------------------------------+--------------------------------------------+
:::

::: paragraph
Eeschema automatically connects invisible power pins of the same name to
the power net of that name. It may be necessary to join power nets of
different names (for example, \"GND\" in TTL components and \"VSS\" in
MOS components); use power ports for this.
:::

::: paragraph
It is not recommended to use labels for power connection. These only
have a "local" connection scope, and would not connect the invisible
power pins.
:::

::: paragraph
The figure below shows an example of power port connections.
:::

:::: imageblock
::: content
![Power ports example](images/en/power_ports_example.png)
:::
::::

::: paragraph
In this example, ground (GND) is connected to power port VSS, and power
port VCC is connected to VDD.
:::

::: paragraph
Two PWR_FLAG symbols are visible. They indicate that the two power ports
VCC and GND are really connected to a power source. Without these two
flags, the ERC tool would diagnose: *Warning: power port not powered*.
:::

::: paragraph
All these symbols can be found in the \`\`power\'\' symbol library.
:::
::::::::::::::::

::::: sect3
#### \`\`No Connect\'\' flag {#no-connection-symbols}

::: paragraph
These symbols are very useful to avoid undesired ERC warnings. The
electrical rules check ensures that no connection has been accidentally
left unconnected.
:::

::: paragraph
If pins must really remain unconnected, it is necessary to place a \"No
Connect\" flag (tool [![No connection
icon](images/icons/noconn.png)]{.image}) on these pins. These symbols do
not have any influence on the generated netlists.
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::: sect2
### Drawing Complements

::::::: sect3
#### Text Comments

::: paragraph
It can be useful (to aid in understanding the schematic) to place
annotations such as text fields and frames. Text fields (tool
[![text](images/icons/text.png)]{.image}) and Polyline (tool [![add
dashed line](images/icons/add_dashed_line.png)]{.image}) are intended
for this use, contrary to labels and wires, which are connection
elements.
:::

::: paragraph
Here you can find an example of a frame with a textual comment.
:::

:::: imageblock
::: content
![Frame with comment example](images/en/frame_example.png)
:::
::::
:::::::

::::::::: sect3
#### Sheet title block

::: paragraph
The title block is edited with the tool [![Page Settings
tool](images/icons/sheetset.png)]{.image}.
:::

:::: imageblock
::: content
![Page settings dialog](images/en/page_settings.png)
:::
::::

:::: imageblock
::: content
![Title block](images/en/title_block.png)
:::
::::

::: paragraph
The sheet number (Sheet X/Y) is automatically updated.
:::
:::::::::
:::::::::::::::

:::::::::: sect2
### Rescuing cached symbols {#rescuing-cached-components}

::: paragraph
By default, Eeschema loads symbols from the project libraries according
to the set paths and library order. This can cause a problem when
loading a very old project: if the symbols in the library have changed
or have been removed or the library no longer exists since they were
used in the project, the ones in the project would be automatically
replaced with the new versions. The new versions might not line up
correctly or might be oriented differently leading to a broken
schematic.
:::

::: paragraph
When a project is saved, a cache library with the contents of the
current library symbols is saved along with the schematic. This allows
the project to be distributed without the full libraries. If you load a
project where symbols are present both in its cache and in the system
libraries, Eeschema will scan the libraries for conflicts. Any conflicts
found will be listed in the following dialog:
:::

:::: imageblock
::: content
![Rescue conflicts dialog](images/en/rescue-conflicts.png)
:::
::::

::: paragraph
You can see in this example that the project originally used a diode
with the cathode facing up, but the library now contains one with the
cathode facing down. This change would break the schematic! Pressing OK
here will cause the symbol cache library to be saved into a special
\`\`rescue\'\' library and all the symbols are renamed to avoid naming
conflicts.
:::

::: paragraph
If you press Cancel, no rescues will be made, so Eeschema will load all
the new components by default. If you save the schematic at this point,
your cache will be overwritten and the old symbols will not be
recoverable. If you have saved the schematic, you can still go back and
run the rescue function again by selecting \"Rescue Cached Components\"
in the \"Tools\" menu to call up the rescue dialog again.
:::

::: paragraph
If you would prefer not to see this dialog, you can press \"Never Show
Again\". The default will be to do nothing and allow the new components
to be loaded. This option can be changed back in the Libraries
preferences.
:::
::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Hierarchical schematics

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::::::: sect2
### About Hierarchies

::: paragraph
A hierarchical representation is generally a good solution for projects
bigger than a few sheets. If you want to manage this kind of project, it
will be necessary to:
:::

::: ulist
- Use large sheets, which results in printing and handling problems.

- Use several sheets, which leads you to a hierarchy structure.
:::

::: paragraph
The complete schematic then consists in a main schematic sheet, called
root sheet, and sub-sheets constituting the hierarchy. Moreover, a
skillful subdividing of the design into separate sheets often improves
on its readability.
:::

::: paragraph
From the root sheet, you must be able to find all sub-sheets.
Hierarchical schematics management is very easy with Eeschema, thanks to
an integrated \"hierarchy navigator\" accessible via the icon
[![icons/hierarchy_nav_png](images/icons/hierarchy_nav.png)]{.image} of
the top toolbar.
:::

::: paragraph
There are two types of hierarchy that can exist simultaneously: the
first one has just been evoked and is of general use. The second
consists in creating symbols in the library that appear like traditional
symbols in the schematic, but which actually correspond to a schematic
which describes their internal structure.
:::

::: paragraph
This second type is used to develop integrated circuits, because in this
case you have to use function libraries in the schematic you are
drawing.
:::

::: paragraph
Eeschema currently doesn't treat this second case.
:::

::: paragraph
A hierarchy can be:
:::

::: ulist
- simple: a given sheet is used only once

- complex: a given sheet is used more than once (multiples instances)

- flat: which is a simple hierarchy, but connections between sheets are
  not drawn.
:::

::: paragraph
Eeschema can deal with all these hierarchies.
:::

::: paragraph
The creation of a hierarchical schematic is easy, the whole hierarchy is
handled starting from the root schematic, as if you had only one
schematic.
:::

::: paragraph
The two important steps to understand are:
:::

::: ulist
- How to create a sub-sheet.

- How to build electrical connections between sub-sheets.
:::
::::::::::::::::

:::::::: sect2
### Navigation in the Hierarchy

::: paragraph
Navigation among sub-sheets is acheived by using the navigator tool
accessible via the button
[![icons/hierarchy_nav_png](images/icons/hierarchy_nav.png)]{.image} on
the top toolbar.
:::

:::: imageblock
::: content
![hierarchy_navigator_dialog_png](images/hierarchy_navigator_dialog.png)
:::
::::

::: paragraph
Each sheet is reachable by clicking on its name. For quick access, right
click on a sheet name, and choose to Enter Sheet or double click within
the bounds of the sheet.
:::

::: paragraph
In order to exit the current sheet to the parent sheet, right click
anywhere in the schematic where there is no object and select \"Leave
Sheet\" in the context menu or press Alt+Backspace.
:::
::::::::

::::::: sect2
### Local, hierarchical and global labels

:::::: sect3
#### Properties

::: paragraph
Local labels, tool
[![icons/add_line_label_png](images/icons/add_line_label.png)]{.image},
are connecting signals only within a sheet. Hierarchical labels (tool
[![icons/add_hierarchical_label_png](images/icons/add_hierarchical_label.png)]{.image})
are connecting signals only within a sheet and to a hierarchical pin
placed in the parent sheet.
:::

::: paragraph
Global labels (tool [![Global label
icon](images/icons/add_glabel.png)]{.image}) are connecting signals
across all the hierarchy. Power pins (type *power in* and *power out*)
invisible are like global labels because they are seen as connected
between them across all the hierarchy.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | Within a hierarchy (simple or     |
| Note                              | complex) one can use both         |
| :::                               | hierarchical labels and/or global |
|                                   | labels.                           |
+-----------------------------------+-----------------------------------+
:::
::::::
:::::::

::::: sect2
### Summary of hierarchy creation

::: paragraph
You have to:
:::

::: ulist
- Place in the root sheet a hierarchy symbol called \"sheet symbol\".

- Enter into the new schematic (sub-sheet) with the navigator and draw
  it, like any other schematic.

- Draw the electric connections between the two schematics by placing
  Global Labels (HLabels) in the new schematic (sub-sheet), and labels
  having the same name in the root sheet, known as SheetLabels. These
  SheetLabels will be connected to the sheet symbol of the root sheet to
  the other elements of the schematic like standard symbol pins.
:::
:::::

::::::::::: sect2
### Sheet symbol

::: paragraph
Draw a rectangle defined by two diagonal points symbolizing the
sub-sheet.
:::

::: paragraph
The size of this rectangle must allow you to place later particular
labels, hierarchy pins, corresponding to the global labels (HLabels) in
the sub-sheet.
:::

::: paragraph
These labels are similar to usual symbol pins. Select the tool
[![icons/add_hierarchical_subsheet_png](images/icons/add_hierarchical_subsheet.png)]{.image}.
:::

::: paragraph
Click to place the upper left corner of the rectangle. Click again to
place the lower right corner, having a large enough rectangle.
:::

::: paragraph
You will then be prompted to type a file name and a sheet name for this
sub-sheet (in order to reach the corresponding schematic, using the
hierarchy navigator).
:::

:::: imageblock
::: content
![hsheet_properties_1_png](images/hsheet_properties_1.png)
:::
::::

::: paragraph
You must give at least a file name. If there is no sheet name, the file
name will be used as sheet name (usual way to do that).
:::
:::::::::::

:::::::::::::::::: sect2
### Connections - hierarchical pins {#connections-hierarchical-pins}

::: paragraph
You will create here points of connection (hierarchy pins) for the
symbol which has been just created.
:::

::: paragraph
These points of connection are similar to normal symbol pins, with
however the possibility to connect a complete bus with only one point of
connection.
:::

::: paragraph
There are two ways to do this:
:::

::: ulist
- Place the different pins before drawing the sub-sheet (manual
  placement).

- Place the different pins after drawing the sub-sheet, and the global
  labels (semi-automatic placement).
:::

::: paragraph
The second solution is quite preferable.
:::

::: paragraph
**Manual placement:**
:::

::: ulist
- Select the tool
  [![icons/add_hierar_pin_png](images/icons/add_hierar_pin.png)]{.image}.

- Click on the hierarchy symbol where you want to place the pin.
:::

::: paragraph
See below for an example of creating a hierarchical pin named
\"CONNECTION\":
:::

:::: imageblock
::: content
![eeschema_hierarchical_pin_png](images/eeschema_hierarchical_pin.png)
:::
::::

::: paragraph
You can define the name, size and direction of the pin during creation
or later, by right clicking the pin and selecting Edit Sheet Pin in the
popup menu.
:::

::: paragraph
Inside the sheet a Hierarchical Label must be preset with the same name
as the Hierarchical Pin. Taking care to correctly match these names must
be done manually, which is why the second method, below, is preferred.
:::

::: paragraph
**Automatic placement:**
:::

::: ulist
- Select the tool
  [![icons/import_hierarchical_label_png](images/icons/import_hierarchical_label.png)]{.image}.

- Click on the hierarchy symbol from where you want to import the pins
  corresponding to global labels placed in the corresponding schematic.
  A hierarchical pin appears, if a new global label exists, i.e. not
  corresponding to an already placed pin.

- Click where you want to place this pin.
:::

::: paragraph
All necessary pins can thus be placed quickly and without error. Their
aspect is in accordance with corresponding global labels.
:::
::::::::::::::::::

:::::::::::::::::::::::::::::: sect2
### Connections - hierarchical labels

::: paragraph
Each pin of the sheet symbol just created, must correspond to a label
called hierarchical Label in the sub-sheet. Hierarchical labels are
similar to labels, but they provide connections between sub-sheet and
root sheet. The graphical representation of the two complementary labels
(pin and HLabel) is similar. Hierarchical labels creation is made with
the tool
[![icons/add_hierarchical_label_png](images/icons/add_hierarchical_label.png)]{.image}.
:::

::: paragraph
See below a root sheet example:
:::

:::: imageblock
::: content
![hierarchical_label_root_png](images/hierarchical_label_root.png)
:::
::::

::: paragraph
Notice pin VCC_PIC, connected to connector JP1.
:::

::: paragraph
Here are the corresponding connections in the sub-sheet :
:::

:::: imageblock
::: content
![hierarchical_label_sub_png](images/hierarchical_label_sub.png)
:::
::::

::: paragraph
You find again, the two corresponding hierarchical labels, providing
connection between the two hierarchical sheets.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | You can use hierarchical labels   |
| Note                              | and hierarchy pins to connect two |
| :::                               | buses, according to the syntax    |
|                                   | (Bus \[N. .m\]) previously        |
|                                   | described.                        |
+-----------------------------------+-----------------------------------+
:::

:::::::::::::::: sect3
#### Labels, hierarchical labels, global labels and invisible power pins

::: paragraph
Here are some comments on various ways to provide connections, other
than wire connections.
:::

:::::: sect4
##### Simple labels

::: paragraph
Simple labels have a local capacity of connection, i.e. limited to the
schematic sheet where they are placed. This is due to the fact that :
:::

::: ulist
- Each sheet has a sheet number.

- This sheet number is associated to a label.
:::

::: paragraph
Thus, if you place the label \"TOTO\" in sheet n° 3, in fact the true
label is \"TOTO_3\". If you also place a label \"TOTO\" in sheet n° 1
(root sheet) you place in fact a label called \"TOTO_1\", different from
\"TOTO_3\". This is always true, even if there is only one sheet.
:::
::::::

:::::: sect4
##### Hierarchical labels

::: paragraph
What is said for the simple labels is also true for hierarchical labels.
:::

::: paragraph
Thus in the same sheet, a hierarchical label \"TOTO\" is considered to
be connected to a local label \"TOTO\", but not connected to a
hierarchical label or label called \"TOTO\" in another sheet.
:::

::: paragraph
A hierarchical label is considered to be connected to the corresponding
sheet pin symbol in the hierarchical symbol placed in the parent sheet.
:::
::::::

:::::: sect4
##### Invisible power pins

::: paragraph
It was seen that invisible power pins were connected together if they
have the same name. Thus all the power pins declared \"Invisible Power
Pins\" and named VCC are connected all symbol invisible power pins named
VCC only within the sheet they are placed.
:::

::: paragraph
This means that if you place a VCC label in a sub-sheet, it will not be
connected to VCC pins, because this label is actually VCC_n, where n is
the sheet number.
:::

::: paragraph
If you want this label VCC to be really connected to the VCC for the
entire schematic, it will have to be explicitly connected to an
invisible power pin via a VCC power symbol.
:::
::::::
::::::::::::::::

::::: sect3
#### Global labels

::: paragraph
Global labels that have an identical name are connected across the whole
hierarchy.
:::

::: paragraph
(power labels like vcc ...​ are global labels)
:::
:::::
::::::::::::::::::::::::::::::

:::::: sect2
### Complex Hierarchy

::: paragraph
Here is an example. The same schematic is used twice (two instances).
The two sheets share the same schematic because the file name is the
same for the two sheets (\`\`other_sheet.sch\'\'). The sheet names must
be unique.
:::

:::: imageblock
::: content
![eeschema_complex_hierarchy_png](images/eeschema_complex_hierarchy.png)
:::
::::
::::::

:::::::::::::::::: sect2
### Flat hierarchy

::: paragraph
You can create a project using many sheets without creating connections
between these sheets (flat hierarchy) if the following rules are
observed:
:::

::: ulist
- Create a root sheet containing the other sheets which acts as a link
  between others sheets.

- No explicit connections are needed.

- Use global labels instead of hierarchical labels in all sheets.
:::

::: paragraph
Here is an example of a root sheet.
:::

:::: imageblock
::: content
![eeschema_flat_hierarchy_png](images/eeschema_flat_hierarchy.png)
:::
::::

::: paragraph
Here is the two pages, connected by global labels.
:::

::: paragraph
Here is the pic_programmer.sch.
:::

:::: imageblock
::: content
![eeschema_flat_hierarchy_1_png](images/eeschema_flat_hierarchy_1.png)
:::
::::

::: paragraph
Here is the pic_sockets.sch.
:::

:::: imageblock
::: content
![eeschema_flat_hierarchy_2_png](images/eeschema_flat_hierarchy_2.png)
:::
::::

::: paragraph
Look at global labels.
:::

:::: imageblock
::: content
![eeschema_flat_hierarchy_3_png](images/eeschema_flat_hierarchy_3.png)
:::
::::
::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: sect1
## Symbol Annotation Tool {#automatic-classification-annotation}

::::::::::::::::::::::::::::::::::::: sectionbody
::::::::::::: sect2
### Introduction {#_introduction_2}

::: paragraph
The annotation tool allows you to automatically assign a designator to
symbols in your schematic. Annotation of symbols with multiple units
will assign a unique suffix to minimize the number of these symbols. The
annotation tool is accessible via the icon
[![icons_annotate_png](images/icons/annotate.png)]{.image}. Here you
find its main window.
:::

:::: imageblock
::: content
![annotate-dialog_img](images/en/annotate-dialog.png)
:::
::::

::: paragraph
Available annotation schemes:
:::

::: ulist
- Annotate all the symbols (reset existing annotation option)

- Annotate all the symbols, but do not swap any previously annotated
  multi-unit parts.

- Annotate only symbols that are currently not annotated. Symbols that
  are not annotated will have a designator which ends with a \'?\'
  character.

- Annotate the whole hierarchy (use the entire schematic option).

- Annotate the current sheet only (use current page only option).
:::

::: paragraph
The \`\`Reset, but do not swap any annotated multi-unit parts\'\' option
keeps all existing associations between symbols with multilple units.
For example, U2A and U2B may be reannotated to U1A and U1B respectively
but they will never be reannotated to U1A and U2A, nor to U2B and U2A.
This is useful if you want to ensure that pin groupings are maintained.
:::

::: paragraph
The annotation order choice gives the method used to set the reference
number inside each sheet of the hierarchy.
:::

::: paragraph
Except for particular cases, an automatic annotation applies to the
whole project (all sheets) and to the new components, if you don't want
to modify previous annotations.
:::

::: paragraph
The Annotation Choice gives the method used to calculate reference:
:::

::: ulist
- Use first free number in schematic: components are annotated from 1
  (for each reference prefix). If a previous annotation exists, only
  unused numbers will be used.

- Start to sheet number\*100 and use first free number: annotation start
  from 101 for the sheet 1, from 201 for the sheet 2, etc. If there are
  more than 99 items having the same reference prefix (U, R) inside the
  sheet 1, the annotation tool uses the number 200 and more, and
  annotation for sheet 2 will start from the next free number.

- Start to sheet number\*1000 and use first free number. Annotation
  start from 1001 for the sheet 1, from 2001 for the sheet 2.
:::
:::::::::::::

::::::::::::::::::::::::: sect2
### Some examples

:::::::::::::: sect3
#### Annotation order

::: paragraph
This example shows 5 elements placed, but not annotated.
:::

:::: imageblock
::: content
![eeschema_annotation_order_none_png](images/eeschema_annotation_order_none.png)
:::
::::

::: paragraph
After the annotation tool Is executed, the following result is obtained.
:::

::: paragraph
Sort by X position.
:::

:::: imageblock
::: content
![eeschema_annotation_order_x_png](images/eeschema_annotation_order_x.png)
:::
::::

::: paragraph
Sort by Y position.
:::

:::: imageblock
::: content
![eeschema_annotation_order_y_png](images/eeschema_annotation_order_y.png)
:::
::::

::: paragraph
You can see that four 74LS00 gates were distributed in U1 package, and
that the fifth 74LS00 has been assigned to the next, U2.
:::
::::::::::::::

:::::::::::: sect3
#### Annotation Choice

::: paragraph
Here is an annotation in sheet 2 where the option use first free number
in schematic was set.
:::

:::: imageblock
::: content
![eeschema_annotation_choice_free_png](images/eeschema_annotation_choice_free.png)
:::
::::

::: paragraph
Option start to sheet number\*100 and use first free number give the
following result.
:::

:::: imageblock
::: content
![eeschema_annotation_choice_x100_png](images/eeschema_annotation_choice_x100.png)
:::
::::

::: paragraph
The option start to sheet number\*1000 and use first free number gives
the following result.
:::

:::: imageblock
::: content
![eeschema_annotation_choice_x1000_png](images/eeschema_annotation_choice_x1000.png)
:::
::::
::::::::::::
:::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::: sect1
## Design verification with Electrical Rules Check {#erc}

:::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::: sect2
### Introduction {#_introduction_3}

::: paragraph
The Electrical Rules Check (ERC) tool performs an automatic check of
your schematic. The ERC checks for any errors in your sheet, such as
unconnected pins, unconnected hierarchical symbols, shorted outputs,
etc. Naturally, an automatic check is not infallible, and the software
that makes it possible to detect all design errors is not yet 100%
complete. Such a check is very useful, because it allows you to detect
many oversights and small errors.
:::

::: paragraph
In fact all detected errors must be checked and then corrected before
proceeding as normal. The quality of the ERC is directly related to the
care taken in declaring electrical pin properties during symbol library
creation. ERC output is reported as `errors` or `warnings`.
:::

:::: imageblock
::: content
![ERC dialog](images/en/dialog_erc.png)
:::
::::
:::::::

::::::: sect2
### How to use ERC

::: paragraph
ERC can be started by clicking on the icon [![ERC
icon](images/icons/erc.png)]{.image}.
:::

::: paragraph
Warnings are placed on the schematic elements raising an ERC error (pins
or labels).
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - In this dialog window, when     |
| :::                               |   clicking on an error message    |
|                                   |   you can jump to the             |
|                                   |   corresponding marker in the     |
|                                   |   schematic.                      |
|                                   |                                   |
|                                   | - In the schematic right-click on |
|                                   |   a marker to access the          |
|                                   |   corresponding diagnostic        |
|                                   |   message.                        |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
You can also delete error markers from the dialog.
:::
:::::::

::::::: sect2
### Example of ERC

:::: imageblock
::: content
![ERC pointers](images/erc_pointers.png)
:::
::::

::: paragraph
Here you can see four errors:
:::

::: ulist
- Two outputs have been erroneously connected together (red arrow).

- Two inputs have been left unconnected (green arrow).

- There is an error on an invisible power port, power flag is missing
  (green arrow on the top).
:::
:::::::

::::::::: sect2
### Displaying diagnostics

::: paragraph
By right-clicking on a marker the pop-up menu allows you to access the
ERC marker diagnostic window.
:::

:::: imageblock
::: content
![ERC pointers info](images/en/erc_pointers_info.png)
:::
::::

::: paragraph
and when clicking on Marker Error Info you can get a description of the
error.
:::

:::: imageblock
::: content
![erc_pointers_message_png](images/erc_pointers_message.png)
:::
::::
:::::::::

:::::::::: sect2
### Power pins and Power flags

::: paragraph
It is common to have an error or a warning on power pins, even though
all seems normal. See example above. This happens because, in most
designs, the power is provided by connectors that are not power sources
(like regulator output, which is declared as Power out).
:::

::: paragraph
The ERC thus won't detect any Power out pin to control this wire and
will declare them not driven by a power source.
:::

::: paragraph
To avoid this warning you have to place a \"PWR_FLAG\" on such a power
port. Take a look at the following example:
:::

:::: imageblock
::: content
![eeschema_power_pins_and_flags_png](images/eeschema_power_pins_and_flags.png)
:::
::::

::: paragraph
The error marker will then disappear.
:::

::: paragraph
Most of the time, a PWR_FLAG must be connected to GND, because
regulators have outputs declared as power out, but ground pins are never
power out (the normal attribute is power in), so grounds never appear
connected to a power source without a power flag symbol.
:::
::::::::::

::::::: sect2
### Configuration

::: paragraph
*The Options* panel allows you to configure connectivity rules to define
electrical conditions for errors and warnings check.
:::

:::: imageblock
::: content
![eeschema_erc_options_png](images/eeschema_erc_options.png)
:::
::::

::: paragraph
Rules can be changed by clicking on the desired square of the matrix,
causing it to cycle through the choices: normal, warning, error.
:::
:::::::

:::::: sect2
### ERC report file

::: paragraph
An ERC report file can be generated and saved by checking the option
Write ERC report. The file extension for ERC report files is .erc. Here
is an example ERC report file.
:::

:::: listingblock
::: content
    ERC control (4/1/1997-14:16:4)

    ***** Sheet 1 (INTERFACE UNIVERSAL)
    ERC: Warning Pin input Unconnected @ 8.450, 2.350
    ERC: Warning passive Pin Unconnected @ 8.450, 1.950
    ERC: Warning: BiDir Pin connected to power Pin (Net 6) @ 10.100, 3.300
    ERC: Warning: Power Pin connected to BiDir Pin (Net 6) @ 4.950, 1.400

    >> Errors ERC: 4
:::
::::
::::::
::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Create a Netlist

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::::: sect2
### Overview {#_overview}

::: paragraph
A netlist is a file which describes electrical connections between
symbols. These connections are referred to as nets. In the netlist file
you can find:
:::

::: ulist
- The list of the symbols

- The list of connections (nets) between symbols.
:::

::: paragraph
Many different netlist formats exist. Sometimes the symbols list and the
list of nets are two separate files. This netlist is fundamental in the
use of schematic capture software, because the netlist is the link with
other electronic CAD software such as:
:::

::: ulist
- PCB layout software.

- Schematic and electrical signal simulators.

- CPLD (and other programmable IC's) compilers.
:::

::: paragraph
Eeschema supports several netlist formats.
:::

::: ulist
- PCBNEW format (printed circuits).

- ORCAD PCB2 format (printed circuits).

- CADSTAR format (printed circuits).

- Spice format, for various simulators (the Spice format is also used by
  other simulators).
:::
:::::::::

:::::::::::: sect2
### Netlist formats

::: paragraph
Select the tool [![Netlist icon](images/icons/netlist.png)]{.image} to
open the netlist creation dialog.
:::

::: paragraph
Pcbnew selected
:::

:::: imageblock
::: content
![eeschema_netlist_dialog_pcbnew_png](images/eeschema_netlist_dialog_pcbnew.png)
:::
::::

::: paragraph
Spice selected
:::

:::: imageblock
::: content
![eeschema_netlist_dialog_spice_png](images/eeschema_netlist_dialog_spice.png)
:::
::::

::: paragraph
Using the different tabs you can select the desired format. In Spice
format you can generate netlists with either net names which makes the
SPICE file more human readable or net numbers which are used by older
Spice. By clicking the Netlist button, you will be asked for a netlist
file name.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | The netlist generation can take   |
| Note                              | up to several minutes for large   |
| :::                               | schematics.                       |
+-----------------------------------+-----------------------------------+
:::
::::::::::::

:::::::::::: sect2
### Netlist examples

::: paragraph
You can see below a schematic design using the PSPICE library:
:::

:::: imageblock
::: content
![eeschema_netlist_schematic_png](images/eeschema_netlist_schematic.png)
:::
::::

::: paragraph
Example of a PCBNEW netlist file:
:::

:::: listingblock
::: content
    # Eeschema Netlist Version 1.0 generee le 21/1/1997-16:51:15
    (
    (32E35B76 $noname C2 1NF {Lib=C}
    (1 0)
    (2 VOUT_1)
    )
    (32CFC454 $noname V2 AC_0.1 {Lib=VSOURCE}
    (1 N-000003)
    (2 0)
    )
    (32CFC413 $noname C1 1UF {Lib=C}
    (1 INPUT_1)
    (2 N-000003)
    )
    (32CFC337 $noname V1 DC_12V {Lib=VSOURCE}
    (1 +12V)
    (2 0)
    )
    (32CFC293 $noname R2 10K {Lib=R}
    (1 INPUT_1)
    (2 0)
    )
    (32CFC288 $noname R6 22K {Lib=R}
    (1 +12V)
    (2 INPUT_1)
    )
    (32CFC27F $noname R5 22K {Lib=R}
    (1 +12V)
    (2 N-000008)
    )
    (32CFC277 $noname R1 10K {Lib=R}
    (1 N-000008)
    (2 0)
    )
    (32CFC25A $noname R7 470 {Lib=R}
    (1 EMET_1)
    (2 0)
    )
    (32CFC254 $noname R4 1K {Lib=R}
    (1 +12V)
    (2 VOUT_1)
    )
    (32CFC24C $noname R3 1K {Lib=R}
    (1 +12V)
    (2 N-000006)
    )
    (32CFC230 $noname Q2 Q2N2222 {Lib=NPN}
    (1 VOUT_1)
    (2 N-000008)
    (3 EMET_1)
    )
    (32CFC227 $noname Q1 Q2N2222 {Lib=NPN}
    (1 N-000006)
    (2 INPUT_1)
    (3 EMET_1)
    )
    )
    # End
:::
::::

::: paragraph
In PSPICE format, the netlist is as follows:
:::

:::: listingblock
::: content
    * Eeschema Netlist Version 1.1 (Spice format) creation date: 18/6/2008-08:38:03

    .model Q2N2222 npn (bf=200)
    .AC 10 1Meg \*1.2
    .DC V1 10 12 0.5


    R12   /VOUT N-000003 22K
    R11   +12V N-000003 100
    L1   N-000003 /VOUT 100mH
    R10   N-000005 N-000004 220
    C3   N-000005 0 10uF
    C2   N-000009 0 1nF
    R8   N-000004 0 2.2K
    Q3   /VOUT N-000009 N-000004 N-000004 Q2N2222
    V2   N-000008 0 AC 0.1
    C1   /VIN N-000008 1UF
    V1   +12V 0 DC 12V
    R2   /VIN 0 10K
    R6   +12V /VIN 22K
    R5   +12V N-000012 22K
    R1   N-000012 0 10K
    R7   N-000007 0 470
    R4   +12V N-000009 1K
    R3   +12V N-000010 1K
    Q2   N-000009 N-000012 N-000007 N-000007 Q2N2222
    Q1   N-000010 /VIN N-000007 N-000007 Q2N2222

    .print ac v(vout)
    .plot ac v(nodes) (-1,5)

    .end
:::
::::
::::::::::::

::::::::::::::::::::::::: sect2
### Notes on Netlists

::::: sect3
#### Netlist name precautions

::: paragraph
Many software tools that use netlists do not accept spaces in the
component names, pins, nets or other informations. Avoid using spaces in
labels, or names and value fields of components or their pins to ensure
maximum compatibility.
:::

::: paragraph
In the same way, special characters other than letters and numbers can
cause problems. Note that this limitation is not related to Eeschema,
but to the netlist formats that can then become untranslatable to
software that uses netlist files.
:::
:::::

::::::::::::::::::::: sect3
#### PSPICE netlists

::: paragraph
For the Pspice simulator, you have to include some command lines in the
netlist itself (.PROBE, .AC, etc.).
:::

::: paragraph
Any text line included in the schematic diagram starting with the
keyword **-pspice** or **-gnucap** will be inserted (without the
keyword) at the top of the netlist.
:::

::: paragraph
Any text line included in the schematic diagram starting with the
keyword **+pspice** or **+gnucap** will be inserted (without the
keyword) at the end of the netlist.
:::

::: paragraph
Here is a sample using many one-line texts and one multi-line text:
:::

:::: imageblock
::: content
![eeschema_pspice_netlist_png](images/eeschema_pspice_netlist.png)
:::
::::

::: paragraph
For example, if you type the following text (do not use a label!):
:::

:::: literalblock
::: content
    -PSPICE .PROBE
:::
::::

::: paragraph
a line .PROBE will be inserted in the netlist.
:::

::: paragraph
In the previous example three lines were inserted at the beginning of
the netlist and two at the end with this technique.
:::

::: paragraph
If you are using multiline texts, **+pspice** or **+gnucap** keywords
are needed only once:
:::

:::: literalblock
::: content
    +PSPICE .model NPN NPN
    .model PNP PNP
    .lib C:\Program Files\LTC\LTspiceIV\lib\cmp\standard.bjt
    .backanno
:::
::::

::: paragraph
creates the four lines:
:::

:::: literalblock
::: content
    .model NPN NPN
    .model PNP PNP
    .lib C:\Program Files\LTC\LTspiceIV\lib\cmp\standard.bjt
    .backanno
:::
::::

::: paragraph
Also note that the GND net must be named 0 (zero) for Pspice.
:::
:::::::::::::::::::::
:::::::::::::::::::::::::

::::::::::::::::::::::::::: sect2
### Other formats

::: paragraph
For other netlist formats you can add netlist converters in the form of
plugins. These converters are automatically launched by Eeschema.
Chapter 14 gives some explanations and examples of converters.
:::

::: paragraph
A converter is a text file (xsl format) but one can use other languages
like Python. When using the xsl format, a tool (xsltproc.exe or
xsltproc) read the intermediate file created by Eeschema, and the
converter file to create the output file. In this case, the converter
file (a sheet style) is very small and very easy to write.
:::

::::::::::::: sect3
#### Init the dialog window

::: paragraph
You can add a new netlist plug-in via the Add Plugin button.
:::

:::: imageblock
::: content
![eeschema_netlist_dialog_add_plugin_png](images/eeschema_netlist_dialog_add_plugin.png)
:::
::::

::: paragraph
Here is the plug-in PadsPcb setup window:
:::

:::: imageblock
::: content
![eeschema_netlist_dialog_padspcb_png](images/eeschema_netlist_dialog_padspcb.png)
:::
::::

::: paragraph
The setup will require:
:::

::: ulist
- A title (for example, the name of the netlist format).

- The plug-in to launch.
:::

::: paragraph
When the netlist is generated:
:::

::: {.olist .arabic}
1.  Eeschema creates an intermediate file \*.tmp, for example test.tmp.

2.  Eeschema runs the plug-in, which reads test.tmp and creates
    test.net.
:::
:::::::::::::

:::::::: sect3
#### Command line format

::: paragraph
Here is an example, using xsltproc.exe as a tool to convert .xsl files,
and a file netlist_form_pads-pcb.xsl as converter sheet style:
:::

::: paragraph
**f:/kicad/bin/xsltproc.exe -o %O.net
f:/kicad/bin/plugins/netlist_form_pads-pcb.xsl %I**
:::

::: paragraph
With:
:::

+------------------------------------------------+-----------------------------+
| f:/kicad/bin/xsltproc.exe                      | A tool to read and convert  |
|                                                | xsl file                    |
+================================================+=============================+
| -o %O.net                                      | Output file: %O will define |
|                                                | the output file.            |
+------------------------------------------------+-----------------------------+
| f:/kicad/bin/plugins/netlist_form_pads-pcb.xsl | File name converter (a      |
|                                                | sheet style, xsl format).   |
+------------------------------------------------+-----------------------------+
| %I                                             | Will be replaced by the     |
|                                                | intermediate file created   |
|                                                | by Eeschema (\*.tmp).       |
+------------------------------------------------+-----------------------------+

::: paragraph
For a schematic named test.sch, the actual command line is:
:::

::: paragraph
f:/kicad/bin/xsltproc.exe -o test.net
f:/kicad/bin/plugins/netlist_form_pads-pcb.xsl test.tmp.
:::
::::::::

::::: sect3
#### Converter and sheet style (plug-in)

::: paragraph
This is a very simple piece of software, because its purpose is only to
convert an input text file (the intermediate text file) to another text
file. Moreover, from the intermediate text file, you can create a BOM
list.
:::

::: paragraph
When using xsltproc as the converter tool only the sheet style will be
generated.
:::
:::::

:::: sect3
#### Intermediate netlist file format

::: paragraph
See Chapter 14 for more explanations about xslproc, descriptions of the
intermediate file format, and some examples of sheet style for
converters.
:::
::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Plot and Print

:::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::: sect2
### Introduction {#_introduction_4}

::: paragraph
You can access both print and plot commands via the file menu.
:::

:::: imageblock
::: content
![eeschema_file_menu_plot_png](images/eeschema_file_menu_plot.png)
:::
::::

::: paragraph
The suported output formats are Postscript, PDF, SVG, DXF and HPGL. You
can also directly print to your printer.
:::
:::::::

:::: sect2
### Common printing commands

::: dlist

Plot Current Page

:   prints one file for the current sheet only.

Plot All Pages

:   allows you to plot the whole hierarchy (one print file is generated
    for each sheet).
:::
::::

::::::: sect2
### Plot in Postscript

::: paragraph
This command allows you to create PostScript files.
:::

:::: imageblock
::: content
![eeschema_plot_postscript_png](images/eeschema_plot_postscript.png)
:::
::::

::: paragraph
The file name is the sheet name with an extension .ps. You can disable
the option \"Plot border and title block\". This is useful if you want
to create a postscript file for encapsulation (format .eps) often used
to insert a diagram in a word processing software. The message window
displays the file names created.
:::
:::::::

:::::: sect2
### Plot in PDF

:::: imageblock
::: content
![eeschema_plot_pdf.png](images/eeschema_plot_pdf.png)
:::
::::

::: paragraph
Allows you to create plot files using the format PDF. The file name is
the sheet name with an extension .pdf.
:::
::::::

:::::: sect2
### Plot in SVG

:::: imageblock
::: content
![eeschema_plot_svg_png](images/eeschema_plot_svg.png)
:::
::::

::: paragraph
Allows you to create plot files using the vectored format SVG. The file
name is the sheet name with an extension .svg.
:::
::::::

:::::: sect2
### Plot in DXF

:::: imageblock
::: content
![eeschema_plot_dxf_png](images/eeschema_plot_dxf.png)
:::
::::

::: paragraph
Allows you to create plot files using the format DXF. The file name is
the sheet name with an extension .dxf.
:::
::::::

::::::::::::::::: sect2
### Plot in HPGL

::: paragraph
This command allows you to create an HPGL file. In this format you can
define:
:::

::: ulist
- Page size.

- Origin.

- Pen width (in mm).
:::

::: paragraph
The plotter setup dialog window looks like the following:
:::

:::: imageblock
::: content
![eeschema_plot_hpgl_png](images/eeschema_plot_hpgl.png)
:::
::::

::: paragraph
The output file name will be the sheet name plus the extension .plt.
:::

:::: sect3
#### Sheet size selection

::: paragraph
Sheet size is normally checked. In this case, the sheet size defined in
the title block menu will be used and the chosen scale will be 1. If a
different sheet size is selected (A4 with A0, or A with E), the scale is
automatically adjusted to fill the page.
:::
::::

:::::::: sect3
#### Offset adjustments

::: paragraph
For all standard dimensions, you can adjust the offsets to center the
drawing as accurately as possible. Because plotters have an origin point
at the center or at the lower left corner of the sheet, it is necessary
to be able to introduce an offset in order to plot properly.
:::

::: paragraph
Generally speaking:
:::

::: ulist
- For plotters having their origin point at the center of the sheet the
  offset must be negative and set at half of the sheet dimension.

- For plotters having their origin point at the lower left corner of the
  sheet the offset must be set to 0.
:::

::: paragraph
To set an offset:
:::

::: ulist
- Select sheet size.

- Set offset X and offset Y.

- Click on accept offset.
:::
::::::::
:::::::::::::::::

:::::::: sect2
### Print on paper

::: paragraph
This command, available via the icon
[![icons/print_button_png](images/icons/print_button.png)]{.image},
allows you to visualize and generate design files for the standard
printer.
:::

:::: imageblock
::: content
![print_dialog_png](images/print_dialog.png)
:::
::::

::: paragraph
The \"Print sheet reference and title block\" option enables or disables
sheet references and title block.
:::

::: paragraph
The \"Print in black and white\" option sets printing in monochrome.
This option is generally necessary if you use a black and white laser
printer, because colors are printed into half-tones that are often not
so readable.
:::
::::::::
::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Symbol Library Editor

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2
### General Information About Symbol Libraries

::: paragraph
A symbol is a schematic element which contains a graphical
representation, electrical connections, and fields defining the symbol.
Symbols used in a schematic are stored in symbol libraries. Eeschema
provides a symbol library editing tool that allows you to create
libraries, add, delete or transfer symbols between libraries, export
symbols to files, and import symbols from files. The library editing
tool provides a simple way to manage symbol library files.
:::
::::

:::::::: sect2
### Symbol Library Overview

::: paragraph
A symbol library is composed of one or more symbols. Generally the
symbols are logically grouped by function, type, and/or manufacturer.
:::

::: paragraph
A symbol is composed of:
:::

::: ulist
- Graphical items (lines, circles, arcs, text, etc ) that provide the
  symbolic definition.

- Pins which have both graphic properties (line, clock, inverted, low
  level active, etc ) and electrical properties (input, output,
  bidirectional, etc.) used by the Electrical Rules Check (ERC) tool.

- Fields such as references, values, corresponding footprint names for
  PCB design, etc.

- Aliases used to associate a common symbol such as a 7400 with all of
  its derivatives such as 74LS00, 74HC00, and 7437. All of these aliases
  share the same library symbol.
:::

::: paragraph
Proper symbol designing requires:
:::

::: ulist
- Defining if the symbol is made up of one or more units.

- Defining if the symbol has an alternate body style also known as a De
  Morgan representation.

- Designing its symbolic representation using lines, rectangles,
  circles, polygons and text.

- Adding pins by carefully defining each pin's graphical elements, name,
  number, and electrical property (input, output, tri-state, power port,
  etc.).

- Adding an alias if other symbols have the same design and pin out or
  removing one if the symbol has been created from another symbol.

- Adding optional fields such as the name of the footprint used by the
  PCB design software and/or defining their visibility.

- Documenting the symbol by adding a description string and links to
  data sheets, etc.

- Saving it in the desired library.
:::
::::::::

:::::::::::::: sect2
### Symbol Library Editor Overview

::: paragraph
The symbol library editor main window is shown below. It consists of
three tool bars for quick access to common features and a symbol
viewing/editing area. Not all commands are available on the tool bars
but can be accessed using the menus.
:::

:::: imageblock
::: content
![libedit_main_window_png](images/libedit_main_window.png)
:::
::::

:::::: sect3
#### Main Toolbar

::: paragraph
The main tool bar typically located at the top of the main window shown
below consists of the library management tools, undo/redo commands, zoom
commands, and symbol properties dialogs.
:::

:::: imageblock
::: content
![](images/toolbar_libedit.png)
:::
::::

+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/save_library_png](images/icons/save_library.png)]{.image}                          | Save the currently selected library. The button will   |
|                                                                                             | be disabled if no library is currently selected or no  |
|                                                                                             | changes to the currently selected library have been    |
|                                                                                             | made.                                                  |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/library_png](images/icons/library.png)]{.image}                                    | Select the library to edit.                            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/delete_png](images/icons/delete.png)]{.image}                                      | Delete a symbol from the currently selected library or |
|                                                                                             | any library defined by the project if no library is    |
|                                                                                             | currently selected.                                    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/library_browse_png](images/icons/library_browse.png)]{.image}                      | Open the symbol library browser to select the library  |
|                                                                                             | and symbol to edit.                                    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/new_symbol_png](images/icons/new_symbol.png)]{.image}                              | Create a new symbol.                                   |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/import_cmp_from_lib_png](images/icons/import_cmp_from_lib.png)]{.image}            | Load symbol from currently selected library for        |
|                                                                                             | editing.                                               |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/copy_symbol_png](images/icons/copy_symbol.png)]{.image}                            | Create a new symbol from the currently loaded symbol.  |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/save_part_in_mem_png](images/icons/save_part_in_mem.png)]{.image}                  | Save the current symbol changes in memory. The library |
|                                                                                             | file is not changed.                                   |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/import_png](images/icons/import.png)]{.image}                                      | Import one symbol from a file.                         |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/export_png](images/icons/export.png)]{.image}                                      | Export the current symbol to a file.                   |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/new_library_png](images/icons/new_library.png)]{.image}                            | Create a new library file containing the current       |
|                                                                                             | symbol. Note: new libraries are not automatically      |
|                                                                                             | added to the project.                                  |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/undo_png](images/icons/undo.png)]{.image}                                          | Undo last edit.                                        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/redo_png](images/icons/redo.png)]{.image}                                          | Redo last undo.                                        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/part_properties_png](images/icons/part_properties.png)]{.image}                    | Edit the current symbol properties.                    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/text.png](images/icons/text.png)]{.image}                                          | Edit the fields of current symbol.                     |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/erc_png](images/icons/erc.png)]{.image}                                            | Test the current symbol for design errors.             |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image}                                              | Zoom in.                                               |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![zoom out](images/icons/zoom_out.png)]{.image}                                            | Zoom out.                                              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![zoom redraw](images/icons/zoom_redraw.png)]{.image}                                      | Refresh display.                                       |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![zoom fit in page](images/icons/zoom_fit_in_page.png)]{.image}                            | Zoom to fit symbol in display.                         |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/morgan1_png](images/icons/morgan1.png)]{.image}                                    | Select the normal body style. The button is disabled   |
|                                                                                             | if the current symbol does not have an alternate body  |
|                                                                                             | style.                                                 |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/morgan2_png](images/icons/morgan2.png)]{.image}                                    | Select the alternate body style. The button is         |
|                                                                                             | disabled if the current symbol does not have an        |
|                                                                                             | alternate body style.                                  |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/datasheet_png](images/icons/datasheet.png)]{.image}                                | Show the associated documentation. The button will be  |
|                                                                                             | disabled if no documentation is defined for the        |
|                                                                                             | current symbol.                                        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![](images/toolbar_libedit_part.png){width="80%"}]{.image}                                 | Select the unit to display. The drop down control will |
|                                                                                             | be disabled if the current symbol is not derived from  |
|                                                                                             | multiple units.                                        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![images/toolbar_libedit_part.png](images/toolbar_libedit_alias.png){width="80%"}]{.image} | Select the alias. The drop down control will be        |
|                                                                                             | disabled if the current symbol does not have any       |
|                                                                                             | aliases.                                               |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/pin2pin_png](images/icons/pin2pin.png)]{.image}                                    | Pin editing: independent editing for pin shape and     |
|                                                                                             | position for symbols with multiple units and alternate |
|                                                                                             | symbols.                                               |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/pin_table_png](images/icons/pin_table.png)]{.image}                                | Show pin table.                                        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
::::::

:::: sect3
#### Element Toolbar

::: paragraph
The vertical toolbar typically located on the right hand side of the
main window allows you to place all of the elements required to design a
symbol. The table below defines each toolbar button.
:::

+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/cursor_png](images/icons/cursor.png)]{.image}               | Select tool. Right-clicking with the select tool opens the    |
|                                                                      | context menu for the object under the cursor. Left-clicking   |
|                                                                      | with the select tool displays the attributes of the object    |
|                                                                      | under the cursor in the message panel at the bottom of the    |
|                                                                      | main window. Double-left-clicking with the select tool will   |
|                                                                      | open the properties dialog for the object under the cursor.   |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/pin_png](images/icons/pin.png)]{.image}                     | Pin tool. Left-click to add a new pin.                        |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/text.png](images/icons/text.png)]{.image}                   | Graphical text tool. Left-click to add a new graphical text   |
|                                                                      | item.                                                         |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_rectangle_png](images/icons/add_rectangle.png)]{.image} | Rectangle tool. Left-click to begin drawing the first corner  |
|                                                                      | of a graphical rectangle. Left-click again to place the       |
|                                                                      | opposite corner of the rectangle.                             |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_circle_png](images/icons/add_circle.png)]{.image}       | Circle tool. Left-click to begin drawing a new graphical      |
|                                                                      | circle from the center. Left-click again to define the radius |
|                                                                      | of the circle.                                                |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_arc_png](images/icons/add_arc.png)]{.image}             | Arc tool. Left-click to begin drawing a new graphical arc     |
|                                                                      | item from the center. Left-click again to define the first    |
|                                                                      | arc end point. Left-click again to define the second arc end  |
|                                                                      | point.                                                        |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/add_polygon_png](images/icons/add_polygon.png)]{.image}     | Polygon tool. Left-click to begin drawing a new graphical     |
|                                                                      | polygon item in the current symbol. Left-click for each       |
|                                                                      | addition polygon line. Double-left-click to complete the      |
|                                                                      | polygon.                                                      |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/anchor_png](images/icons/anchor.png)]{.image}               | Anchor tool. Left-click to set the anchor position of the     |
|                                                                      | symbol.                                                       |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/import_png](images/icons/import.png)]{.image}               | Import a symbol from a file.                                  |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/export_png](images/icons/export.png)]{.image}               | Export the current symbol to a file.                          |
+----------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/delete_png](images/icons/delete.png)]{.image}               | Delete tool. Left-click to delete an object from the current  |
|                                                                      | symbol.                                                       |
+----------------------------------------------------------------------+---------------------------------------------------------------+
::::

:::: sect3
#### Options Toolbar

::: paragraph
The vertical tool bar typically located on the left hand side of the
main window allows you to set some of the editor drawing options. The
table below defines each tool bar button.
:::

+--------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/grid_png](images/icons/grid.png)]{.image}                 | Toggle grid visibility on and off.                            |
+--------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/unit_inch_png](images/icons/unit_inch.png)]{.image}       | Set units to inches.                                          |
+--------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/unit_mm_png](images/icons/unit_mm.png)]{.image}           | Set units to millimeters.                                     |
+--------------------------------------------------------------------+---------------------------------------------------------------+
| [![icons/cursor_shape_png](images/icons/cursor_shape.png)]{.image} | Toggle full screen cursor on and off.                         |
+--------------------------------------------------------------------+---------------------------------------------------------------+
::::
::::::::::::::

::::::::::::::::::::::: sect2
### Library Selection and Maintenance

::: paragraph
The selection of the current library is possible via the
[![icons/library_png](images/icons/library.png)]{.image} which shows you
all available libraries and allows you to select one. When a symbol is
loaded or saved, it will be put in this library. The library name of
symbol is the contents of its value field.
:::

::: {.admonitionblock .note}
+-----------------------------------+----------------------------------------------------------------------+
| ::: title                         | ::: ulist                                                            |
| Note                              | - You must load a library into Eeschema, in order to access its      |
| :::                               |   contents.                                                          |
|                                   |                                                                      |
|                                   | - The content of the current library can be saved after              |
|                                   |   modification, by clicking on the                                   |
|                                   |   [![icons/save_library_png](images/icons/save_library.png)]{.image} |
|                                   |   on the main tool bar.                                              |
|                                   |                                                                      |
|                                   | - A symbol can be removed from any library by clicking on the        |
|                                   |   [![icons/delete_png](images/icons/delete.png)]{.image}.            |
|                                   | :::                                                                  |
+-----------------------------------+----------------------------------------------------------------------+
:::

:::::::::::::::::::: sect3
#### Select and Save a Symbol

::: paragraph
When you edit a symbol you are not really working on the symbol in its
library but on a copy of it in the computer's memory. Any edit action
can be undone easily. A symbol may be loaded from a local library or
from an existing symbol.
:::

:::::: sect4
##### Symbol Selection

::: paragraph
Clicking the
[![icons/import_cmp_from_lib_png](images/icons/import_cmp_from_lib.png)]{.image}
on the main tool bar displays the list of the available symbols that you
can select and load from the currently selected library.
:::

::: {.admonitionblock .note}
+-----------------------------------+--------------------------------------------------+
| ::: title                         | If a symbol is selected by its alias, the name   |
| Note                              | of the loaded symbol is displayed on the window  |
| :::                               | title bar instead of the selected alias. The     |
|                                   | list of symbol aliases is always loaded with     |
|                                   | each symbol and can be edited. You can create a  |
|                                   | new symbol by selecting an alias of the current  |
|                                   | symbol from the                                  |
|                                   | [![](images/toolbar_libedit_alias.png)]{.image}. |
|                                   | The first item in the alias list is the root     |
|                                   | name of the symbol.                              |
+-----------------------------------+--------------------------------------------------+
:::

::: {.admonitionblock .note}
+-----------------------------------+---------------------------------------------------------+
| ::: title                         | Alternatively, clicking the                             |
| Note                              | [![icons/import_png](images/icons/import.png)]{.image}  |
| :::                               | allows you to load a symbol which has been previously   |
|                                   | saved by the                                            |
|                                   | [![icons/export_png](images/icons/export.png)]{.image}. |
+-----------------------------------+---------------------------------------------------------+
:::
::::::

::::::::: sect4
##### Save a Symbol

::: paragraph
After modification, a symbol can be saved in the current library, in a
new library, or exported to a backup file.
:::

::: paragraph
To save the modified symbol in the current library, click the
[![icons/save_part_in_mem_png](images/icons/save_part_in_mem.png)]{.image}.
Please note that the update command only saves the symbol changes in the
local memory. This way, you can make up your mind before you save the
library.
:::

::: paragraph
To permanently save the symbol changes to the library file, click the
[![icons/save_library_png](images/icons/save_library.png)]{.image} which
will overwrite the existing library file with the symbol changes.
:::

::: paragraph
If you want to create a new library containing the current symbol, click
the [![icons/new_library_png](images/icons/new_library.png)]{.image}.
You will be asked to enter a new library name.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | New libraries are not             |
| :::                               | automatically added to the        |
|                                   | current project.                  |
|                                   | :::                               |
|                                   |                                   |
|                                   | ::: paragraph                     |
|                                   | You must add any new library you  |
|                                   | wish to use in a schematic to the |
|                                   | list of project libraries in      |
|                                   | Eeschema using the [Symbol        |
|                                   | Library Table                     |
|                                   | dialog](#manage-sym-lib-table).   |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
Click the [![icons/export_png](images/icons/export.png)]{.image} to
create a file containing only the current symbol. This file will be a
standard library file which will contain only one symbol. This file can
be used to import the symbol into another library. In fact, the create
new library command and the export command are basically identical.
:::
:::::::::

::::: sect4
##### Transfer Symbols to Another Library

::: paragraph
You can very easily copy a symbol from a source library into a
destination library using the following commands:
:::

::: ulist
- Select the source library by clicking the
  [![icons/library_png](images/icons/library.png)]{.image}.

- Load the symbol to be transferred by clicking the
  [![icons/import_cmp_from_lib_png](images/icons/import_cmp_from_lib.png)]{.image}.
  The symbol will be displayed in the editing area.

- Select the destination library by clicking the
  [![icons/library_png](images/icons/library.png)]{.image}.

- Save the current symbol to the new library in the local memory by
  clicking the
  [![icons/save_part_in_mem_png](images/icons/save_part_in_mem.png)]{.image}.

- Save the symbol in the current local library file by clicking the
  [![icons/save_library_png](images/icons/save_library.png)]{.image}.
:::
:::::

:::: sect4
##### Discarding Symbol Changes

::: paragraph
When you are working on a symbol, the edited symbol is only a working
copy of the actual symbol in its library. This means that as long as you
have not saved it, you can just reload it to discard all changes made.
If you have already updated it in the local memory and you have not
saved it to the library file, you can always quit and start again.
Eeschema will undo all the changes.
:::
::::
::::::::::::::::::::
:::::::::::::::::::::::

::::::::::::::::::::::::::: sect2
### Creating Library Symbols

::::::::: sect3
#### Create a New Symbol

::: paragraph
A new symbol can be created by clicking the
[![icons/new_symbol_png](images/icons/new_symbol.png)]{.image}. You will
be asked for a symbol name (this name is used as default value for the
value field in the schematic editor), the reference designator (U, IC,
R...​), the number of units per package (for example a 7400 is made of 4
units per package) and if an alternate body style (sometimes referred to
as DeMorgan) is desired. If the reference designator field is left
empty, it will default to \"U\". These properties can be changed later,
but it is preferable to set them correctly at the creation of the
symbol.
:::

:::: imageblock
::: content
![eeschema_symbol_properties_png](images/eeschema_symbol_properties.png)
:::
::::

::: paragraph
A new symbol will be created using the properties above and will appear
in the editor as shown below.
:::

:::: imageblock
::: content
![eeschema_libedit_new_png](images/eeschema_libedit_new.png)
:::
::::
:::::::::

::::: sect3
#### Create a Symbol from Another Symbol

::: paragraph
Often, the symbol that you want to make is similar to one already in a
symbol library. In this case it is easy to load and modify an existing
symbol.
:::

::: ulist
- Load the symbol which will be used as a starting point.

- Click on the
  [![icons/copy_symbol_png](images/icons/copy_symbol.png)]{.image} or
  modify its name by right-clicking on the value field and editing the
  text. If you chose to duplicate the current symbol, you will be
  prompted for a new symbol name.

- If the model symbol has aliases, you will be prompted to remove
  aliases from the new symbol which conflict with the current library.
  If the answer is no the new symbol creation will be aborted. Symbol
  libraries cannot have any duplicate names or aliases.

- Edit the new symbol as required.

- Update the new symbol in the current library by clicking the
  [![icons/save_part_in_mem_png](images/icons/save_part_in_mem.png)]{.image}
  or save to a new library by clicking the
  [![icons/new_library_png](images/icons/new_library.png)]{.image} or if
  you want to save this new symbol in an other existing library select
  the other library by clicking on the
  [![icons/library_png](images/icons/library.png)]{.image} and save the
  new symbol.

- Save the current library file to disk by clicking the
  [![icons/save_library_png](images/icons/save_library.png)]{.image}.
:::
:::::

::::::::::: sect3
#### Symbol Properties

::: paragraph
Symbol properties should be carefully set during the symbol creation or
alternatively they are inherited from the copied symbol. To change the
symbol properties, click on the
[![icons/part_properties_png](images/icons/part_properties.png)]{.image}
to show the dialog below.
:::

:::: imageblock
::: content
![eeschema_properties_for_symbol_png](images/eeschema_properties_for_symbol.png)
:::
::::

::: paragraph
It is very important to correctly set the number of units per package
and the alternate symbolic representation, if enabled, because when pins
are edited or created the corresponding pins for each unit will be
affected. If you change the number of units per package after pin
creation and editing, there will be additional work to add the new unit
pins and symbols. Nevertheless, it is possible to modify these
properties at any time.
:::

::: paragraph
The graphic options \"Show pin number\" and \"Show pin name\" define the
visibility of the pin number and pin name text. This text will be
visible if the corresponding options are checked. The option \"Place pin
names inside\" defines the pin name position relative to the pin body.
This text will be displayed inside the symbol outline if the option is
checked. In this case the \"Pin Name Position Offset\" property defines
the shift of the text away from the body end of the pin. A value from 30
to 40 (in 1/1000 inch) is reasonable.
:::

::: paragraph
The example below shows a symbol with the \"Place pin name inside\"
option unchecked. Notice the position of the names and pin numbers.
:::

:::: imageblock
::: content
![eeschema_uncheck_pin_name_inside_png](images/eeschema_uncheck_pin_name_inside.png)
:::
::::
:::::::::::

::::::: sect3
#### Symbols with Alternate Symbolic Representation

::: paragraph
If the symbol has more than one symbolic repersentation, you will have
to select one representation to edit them. To edit the normal
representation, click the
[![icons/morgan1_png](images/icons/morgan1.png)]{.image}.
:::

::: paragraph
To edit the alternate representation, click on the
[![icons/morgan2_png](images/icons/morgan2.png)]{.image}. Use the
[![images/toolbar_libedit_part.png](images/toolbar_libedit_alias.png)]{.image}
shown below to select the unit you wish to edit.
:::

:::: imageblock
::: content
![eeschema_libedit_select_unit_png](images/eeschema_libedit_select_unit.png)
:::
::::
:::::::
:::::::::::::::::::::::::::

::::::::::::::::: sect2
### Graphical Elements

::: paragraph
Graphical elements create the representation of a symbol and contain no
electrical connection information. Their design is possible using the
following tools:
:::

::: ulist
- Lines and polygons defined by start and end points.

- Rectangles defined by two diagonal corners.

- Circles defined by the center and radius.

- Arcs defined by the starting and ending point of the arc and its
  center. An arc goes from 0° to 180°.
:::

::: paragraph
The vertical toolbar on the right hand side of the main window allows
you to place all of the graphical elements required to design the
representation of a symbol.
:::

::::::::::: sect3
#### Graphical Element Membership

::: paragraph
Each graphic element (line, arc, circle, etc.) can be defined as common
to all units and/or body styles or specific to a given unit and/or body
style. Element options can be quickly accessed by right-clicking on the
element to display the context menu for the selected element. Below is
the context menu for a line element.
:::

:::: imageblock
::: content
![eeschema_libedit_context_menu_png](images/eeschema_libedit_context_menu.png)
:::
::::

::: paragraph
You can also double-left-click on an element to modify its properties.
Below is the properties dialog for a polygon element.
:::

:::: imageblock
::: content
![eeschema_libedit_polyline_properties_png](images/eeschema_libedit_polyline_properties.png)
:::
::::

::: paragraph
The properties of a graphic element are:
:::

::: ulist
- Line width which defines the width of the element's line in the
  current drawing units.

- The \"Common to all units in symbol\" setting defines if the graphical
  element is drawn for each unit in symbol with more than one unit per
  package or if the graphical element is only drawn for the current
  unit.

- The \"Common by all body styles (DeMorgan)\" setting defines if the
  graphical element is drawn for each symbolic representation in symbols
  with an alternate body style or if the graphical element is only drawn
  for the current body style.

- The fill style setting determines if the symbol defined by the
  graphical element is to be drawn unfilled, background filled, or
  foreground filled.
:::
:::::::::::

:::: sect3
#### Graphical Text Elements

::: paragraph
The [![icons/text.png](images/icons/text.png)]{.image} allows for the
creation of graphical text. Graphical text is always readable, even when
the symbol is mirrored. Please note that graphical text items are not
fields.
:::
::::
:::::::::::::::::

:::::::::::::::::::::::::::: sect2
### Multiple Units per Symbol and Alternate Body Styles

::: paragraph
Symbols can have two symbolic representations (a standard symbol and an
alternate symbol often referred to as \"DeMorgan\") and/or have more
than one unit per package (logic gates for example). Some symbols can
have more than one unit per package each with different symbols and pin
configurations.
:::

::: paragraph
Consider for instance a relay with two switches which can be designed as
a symbol with three different units: a coil, switch 1, and switch 2.
Designing a symbol with multiple units per package and/or alternate body
styles is very flexible. A pin or a body symbol item can be common to
all units or specific to a given unit or they can be common to both
symbolic representation so are specific to a given symbol
representation.
:::

::: paragraph
By default, pins are specific to each symbolic representation of each
unit, because the pin number is specific to a unit, and the shape
depends on the symbolic representation. When a pin is common to each
unit or each symbolic representation, you need to create it only once
for all units and all symbolic representations (this is usually the case
for power pins). This is also the case for the body style graphic shapes
and text, which may be common to each unit (but typically are specific
to each symbolic representation).
:::

:::::::::::::::::::::::: sect3
#### Example of a Symbol Having Multiple Units with Different Symbols:

::: paragraph
This is an example of a relay defined with three units per package,
switch 1, switch 2, and the coil:
:::

::: paragraph
Option: pins are not linked. One can add or edit pins for each unit
without any coupling with pins of other units.
:::

:::: imageblock
::: content
![eeschema_libedit_pins_per_part_png](images/eeschema_libedit_pins_per_part.png)
:::
::::

::: paragraph
All units are not interchangeable must be selected.
:::

:::: imageblock
::: content
![eeschema_libedit_not_interchangeable_png](images/eeschema_libedit_not_interchangeable.png)
:::
::::

::: paragraph
Unit 1
:::

:::: imageblock
::: content
![eeschema_libedit_unit1_png](images/eeschema_libedit_unit1.png)
:::
::::

::: paragraph
Unit 2
:::

:::: imageblock
::: content
![eeschema_libedit_unit2_png](images/eeschema_libedit_unit2.png)
:::
::::

::: paragraph
Unit 3
:::

:::: imageblock
::: content
![eeschema_libedit_unit3_png](images/eeschema_libedit_unit3.png)
:::
::::

::: paragraph
It does not have the same symbol and pin layout and therefore is not
interchangeable with units 1 and 2.
:::

:::::: sect4
##### Graphical Symbolic Elements

::: paragraph
Shown below are properties for a graphic body element. From the relay
example above, the three units have different symbolic representations.
Therefore, each unit was created separately and the graphical body
elements must have the \"Common to all units in symbol\" disabled.
:::

:::: imageblock
::: content
![eeschema_libedit_disable_common_png](images/eeschema_libedit_disable_common.png)
:::
::::
::::::
::::::::::::::::::::::::
::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::: sect2
### Pin Creation and Editing

::: paragraph
You can click on the [![icons/pin_png](images/icons/pin.png)]{.image} to
create and insert a pin. The editing of all pin properties is done by
double-clicking on the pin or right-clicking on the pin to open the pin
context menu. Pins must be created carefully, because any error will
have consequences on the PCB design. Any pin already placed can be
edited, deleted, and/or moved.
:::

:::::: sect3
#### Pin Overview

::: paragraph
A pin is defined by its graphical representation, its name and its
\"number\". The pin's \"number\" is defined by a set of 4 letters and /
or numbers. For the Electrical Rules Check (ERC) tool to be useful, the
pin's \"electrical\" type (input, output, tri-state...​) must also be
defined correctly. If this type is not defined properly, the schematic
ERC check results may be invalid.
:::

::: paragraph
Important notes:
:::

::: ulist
- Do not use spaces in pin names and numbers.

- To define a pin name with an inverted signal (overline) use the `~`
  (tilde) character. The next `~` character will turn off the overline.
  For example `~FO~O` would display [FO]{.overline} O.

- If the pin name is reduced to a single symbol, the pin is regarded as
  unnamed.

- Pin names starting with `#`, are reserved for power port symbols.

- A pin \"number\" consists of 1 to 4 letters and/ or numbers.
  1,2,..9999 are valid numbers. A1, B3, Anod, Gnd, Wire, etc. are also
  valid.

- Duplicate pin \"numbers\" cannot exist in a symbol.
:::
::::::

::::::: sect3
#### Pin Properties

:::: imageblock
::: content
![eeschema_libedit_pin_properties_png](images/eeschema_libedit_pin_properties.png)
:::
::::

::: paragraph
The pin properties dialog allows you to edit all of the characteristics
of a pin. This dialog pops up automatically when you create a pin or
when double-clicking on an existing pin. This dialog allows you to
modify:
:::

::: ulist
- Name and name's text size.

- Number and number's text size.

- Length.

- Electrical and graphical types.

- Unit and alternate representation membership.

- Visibility.
:::
:::::::

:::::: sect3
#### Pins Graphical Styles

::: paragraph
Shown in the figure below are the different pin graphical styles. The
choice of graphic styles does not have any influence on the pin's
electrical type.
:::

:::: imageblock
::: content
![eeschema_libedit_pin_properties_style_png](images/eeschema_libedit_pin_properties_style.png)
:::
::::
::::::

::::: sect3
#### Pin Electrical Types

::: paragraph
Choosing the correct electrical type is important for the schematic ERC
tool. The electrical types defined are:
:::

::: ulist
- Bidirectional which indicates bidirectional pins commutable between
  input and output (microprocessor data bus for example).

- Tri-state is the usual 3 states output.

- Passive is used for passive symbol pins, resistors, connectors, etc.

- Unspecified can be used when the ERC check doesn't matter.

- Power input is used for the symbol's power pins. Power pins are
  automatically connected to the other power input pins with the same
  name.

- Power output is used for regulator outputs.

- Open emitter and open collector types can be used for logic outputs
  defined as such.

- Not connected is used when a symbol has a pin that has no internal
  connection.
:::
:::::

:::::: sect3
#### Pin Global Properties

::: paragraph
You can modify the length or text size of the name and/or number of all
the pins using the Global command entry of the pin context menu. Click
on the parameter you want to modify and type the new value which will
then be applied to all of the current symbol's pins.
:::

:::: imageblock
::: content
![eeschema_libedit_pin_context_menu_png](images/eeschema_libedit_pin_context_menu.png)
:::
::::
::::::

::::::::: sect3
#### Defining Pins for Multiple Units and Alternate Symbolic Representations

::: paragraph
Symbols with multiple units and/or graphical representations are
particularly problematic when creating and editing pins. The majority of
pins are specific to each unit (because their pin number is specific to
each unit) and to each symbolic representation (because their form and
position is specific to each symbolic representation). The creation and
the editing of pins can be problematic for symbols with multiple units
per package and alternate symbolic representations. The symbol library
editor allows the simultaneous creation of pins. By default, changes
made to a pin are made for all units of a multiple unit symbol and both
representations for symbols with an alternate symbolic representation.
:::

::: paragraph
The only exception to this is the pin's graphical type and name. This
dependency was established to allow for easier pin creation and editing
in most of the cases. This dependency can be disabled by toggling the
[![icons/pin2pin_png](images/icons/pin2pin.png)]{.image} on the main
tool bar. This will allow you to create pins for each unit and
representation completely independently.
:::

::: paragraph
A symbol can have two symbolic representations (representation known
as\`\`DeMorgan\'\') and can be made up of more than one unit as in the
case of symbols with logic gates. For certain symbols, you may want
several different graphic elements and pins. Like the relay sample shown
in the [previous
section](#example-of-a-symbol-having-multiple-units-with-different-symbols),
a relay can be represented by three distinct units: a coil, switch
contact 1, and switch contact 2.
:::

::: paragraph
The management of the symbols with multiple units and symbols with
alternate symbolic representations is flexible. A pin can be common or
specific to different units. A pin can also be common to both symbolic
representations or specific to each symbolic representation.
:::

::: paragraph
By default, pins are specific to each representation of each unit,
because their number differs for each unit, and their design is
different for each symbolic representation. When a pin is common to all
units, it only has to drawn once such as in the case of power pins.
:::

::: paragraph
An example is the output pin 7400 quad dual input NAND gate. Since there
are four units and two symbolic representations, there are eight
separate output pins defined in the symbol definition. When creating a
new 7400 symbol, unit A of the normal symbolic representation will be
shown in the library editor. To edit the pin style in alternate symbolic
representation, it must first be enabled by clicking the
[![icons/morgan2_png](images/icons/morgan2.png)]{.image} button on the
tool bar. To edit the pin number for each unit, select the appropriate
unit using the [![](images/toolbar_libedit_alias.png)]{.image} drop down
control.
:::
:::::::::
:::::::::::::::::::::::::::::::

:::::::::::::: sect2
### Symbol Fields

::: paragraph
All library symbols are defined with four default fields. The reference
designator, value, footprint assignment, and documentation file link
fields are created whenever a symbol is created or copied. Only the
reference designator and value fields are required. For existing fields,
you can use the context menu commands by right-clicking on the pin.
Symbols defined in libraries are typically defined with these four
default fields. Additional fields such as vendor, part number, unit
cost, etc. can be added to library symbols but generally this is done in
the schematic editor so the additional fields can be applied to all of
the symbols in the schematic.
:::

:::::::::::: sect3
#### Editing Symbol Fields

::: paragraph
To edit an existing symbol field, right-click on the field text to show
the field context menu shown below.
:::

:::: imageblock
::: content
![eeschema_libedit_field_context_menu_png](images/eeschema_libedit_field_context_menu.png)
:::
::::

::: paragraph
To edit undefined fields, add new fields, or delete optional fields
[![icons/text.png](images/icons/text.png)]{.image} on the main tool bar
to open the field properties dialog shown below.
:::

:::: imageblock
::: content
![eeschema_libedit_field_properties_png](images/eeschema_libedit_field_properties.png)
:::
::::

::: paragraph
Fields are text sections associated with the symbol. Do not confuse them
with the text belonging to the graphic representation of this symbol.
:::

::: paragraph
Important notes:
:::

::: ulist
- Modifying value fields effectively creates a new symbol using the
  current symbol as the starting point for the new symbol. This new
  symbol has the name contained in the value field when you save it to
  the currently selected library.

- The field edit dialog above must be used to edit a field that is empty
  or has the invisible attribute enabled.

- The footprint is defined as an absolute footprint using the
  LIBNAME:FPNAME format where LIBNAME is the name of the footprint
  library defined in the footprint library table (see the \"Footprint
  Library Table\" section in the Pcbnew \"Reference Manual\") and FPNAME
  is the name of the footprint in the library LIBNAME.
:::
::::::::::::
::::::::::::::

:::::::::: sect2
### Power Symbols

::: paragraph
Power symbols are created the same way as normal symbols. It may be
useful to place them in a dedicated library such as power.lib. Power
symbols consist of a graphical symbol and a pin of the type \"Power
Invisible\". Power port symbols are handled like any other symbol by the
schematic capture software. Some precautions are essential. Below is an
example of a power +5V symbol.
:::

:::: imageblock
::: content
![eeschema_libedit_power_symbol_png](images/eeschema_libedit_power_symbol.png)
:::
::::

::: paragraph
To create a power symbol, use the following steps:
:::

::: ulist
- Add a pin of type \"Power input\" named +5V (important because this
  name will establish connection to the net +5V), with a pin number of 1
  (number of no importance), a length of 0, and a \"Line\" \"Graphic
  Style\".

- Place a small circle and a segment from the pin to the circle as
  shown.

- The anchor of the symbol is on the pin.

- The symbol value is `+5V`.

- The symbol reference is `#+5V`. The reference text is not important
  except the first character which must be `#` to indicate that the
  symbol is a power symbol. By convention, every symbol in which the
  reference field starts with a `#` will not appear in the symbol list
  or in the netlist and the reference is declared as invisible.
:::

::: paragraph
An easier method to create a new power port symbol is to use another
symbol as a model:
:::

::: ulist
- Load an existing power symbol.

- Edit the pin name with name of the new power symbol.

- Edit the value field to the same name as the pin, if you want to
  display the power port value.

- Save the new symbol.
:::
::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## LibEdit - Symbols {#libedit-symbols}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::: sect2
### Overview {#_overview_2}

::: paragraph
A symbol consist of the following elements
:::

::: ulist
- A graphical representation (geometrical shapes, texts).

- Pins.

- Fields or associated text used by the post processors: netlist,
  symbols list.
:::

::: paragraph
Two fields are to be initialized: reference and value. The name of the
design associated with the symbol, and the name of the associated
footprint, the other fields are the free fields, they can generally
remain empty, and could be filled during schematic capture.
:::

::: paragraph
However, managing the documentation associated with any symbol
facilitates the research, use and maintenance of libraries. The
associated documentation consists of
:::

::: ulist
- A line of comment.

- A line of key words such as TTL CMOS NAND2, separated by spaces.

- An attached file name (for example an application note or a pdf file).

  ::: paragraph
  The default directory for attached files:
  :::

  ::: paragraph
  kicad/share/library/doc
  :::

  ::: paragraph
  If not found:
  :::

  ::: paragraph
  kicad/library/doc
  :::

  ::: paragraph
  Under linux:
  :::

  ::: paragraph
  /usr/local/kicad/share/library/doc
  :::

  ::: paragraph
  /usr/share/kicad/library/doc
  :::

  ::: paragraph
  /usr/local/share/kicad/library/doc
  :::
:::

::: paragraph
Key words allow you to selectively search for a symbol according to
various selection criteria. Comments and key words are displayed in
various menus, and particularly when you select a symbol from the
library.
:::

::: paragraph
The symbol also has an anchoring point. A rotation or a mirror is made
relative to this anchor point and during a placement this point is used
as a reference position. It is thus useful to position this anchor
accurately.
:::

::: paragraph
A symbol can have aliases, i.e. equivalent names. This allows you to
considerably reduce the number of symbols that need to be created (for
example, a 74LS00 can have aliases such as 74000, 74HC00, 74HCT00...​).
:::

::: paragraph
Finally, the symbols are distributed in libraries (classified by topics,
or manufacturer) in order to facilitate their management.
:::
::::::::::::

::::::: sect2
### Position a symbol anchor

::: paragraph
The anchor is at the coordinates (0,0) and it is shown by the blue axes
displayed on your screen.
:::

:::: imageblock
::: content
![eeschema_libedit_anchor_png](images/eeschema_libedit_anchor.png)
:::
::::

::: paragraph
The anchor can be repositioned by selecting the icon
[![icons/anchor_png](images/icons/anchor.png)]{.image} and clicking on
the new desired anchor position. The drawing will be automatically
re-centered on the new anchor point.
:::
:::::::

:::::::::: sect2
### Symbol aliases

::: paragraph
An alias is another name corresponding to the same symbol in the
library. Symbols with similar pin-out and representation can then be
represented by only one symbol, having several aliases (e.g. 7400 with
alias 74LS00, 74HC00, 74LS37 ).
:::

::: paragraph
The use of aliases allows you to build complete libraries quickly. In
addition these libraries, being much more compact, are easily loaded by
KiCad.
:::

::: paragraph
To modify the list of aliases, you have to select the main editing
window via the icon
[![icons/part_properties_png](images/icons/part_properties.png)]{.image}
and select the alias folder.
:::

:::: imageblock
::: content
![eeschema_libedit_alias_png](images/eeschema_libedit_alias.png)
:::
::::

::: paragraph
You can thus add or remove the desired alias. The current alias cannot
obviously be removed since it is edited.
:::

::: paragraph
To remove all aliases, you have firstly to select the root symbol. The
first symbol in the alias list in the window of selection of the main
toolbar.
:::
::::::::::

::::::::: sect2
### Symbol fields

::: paragraph
The field editor is called via the icon
[![icons/text.png](images/icons/text.png)]{.image}.
:::

::: paragraph
There are four special fields (texts attached to the symbol), and
configurable user fields
:::

:::: imageblock
::: content
![eeschema_libedit_field_properties_png](images/eeschema_libedit_field_properties.png)
:::
::::

::: paragraph
Special fields
:::

::: ulist
- Reference.

- Value. It is the symbol name in the library and the default value
  field in schematic.

- Footprint. It is the footprint name used for the board. Not very
  useful when using CvPcb to setup the footprint list, but mandatory if
  CvPcb is not used.

- Sheet. It is a reserved field, not used at the time of writing.
:::
:::::::::

:::::::::::::::::::::::::::::: sect2
### Symbol documentation

::: paragraph
To edit documentation information, it is necessary to call the main
editing window of the symbol via the icon
[![icons/part_properties_png](images/icons/part_properties.png)]{.image}
and to select the document folder.
:::

:::: imageblock
::: content
![eeschema_libedit_description_png](images/eeschema_libedit_description.png)
:::
::::

::: paragraph
Be sure to select the right alias, or the root symbol, because this
documentation is the only characteristic which differs between aliases.
The \"Copy Doc\" button allows you to copy the documentation information
from the root symbol towards the currently edited alias.
:::

:::::: sect3
#### Symbol keywords

::: paragraph
Keywords allow you to search in a selective way for a symbol according
to specific selection criteria (function, technological family, etc.)
:::

::: paragraph
The Eeschema research tool is not case sensitive. The most current key
words used in the libraries are
:::

::: ulist
- CMOS TTL for the logic families

- AND2 NOR3 XOR2 INV...​ for the gates (AND2 = 2 inputs AND gate, NOR3 =
  3 inputs NOR gate).

- JKFF DFF...​ for JK or D flip-flop.

- ADC, DAC, MUX...​

- OpenCol for the gates with open collector output. Thus if in the
  schematic capture software, you search the symbol: by keywords NAND2
  OpenCol Eeschema will display the list of symbols having these 2 key
  words.
:::
::::::

::::: sect3
#### Symbol documentation (Doc)

::: paragraph
The line of comment (and keywords) is displayed in various menus,
particularly when you select a symbol in the displayed symbols list of a
library and in the ViewLib menu.
:::

::: paragraph
If this Doc. file exists, it is also accessible in the schematic capture
software, in the pop-up menu displayed by right-clicking on the symbol.
:::
:::::

:::: sect3
#### Associated documentation file (DocFileName)

::: paragraph
Indicates an attached file (documentation, application schematic)
available ( pdf file, schematic diagram, etc.).
:::
::::

:::::::::::::::: sect3
#### Footprint filtering for CvPcb

::: paragraph
You can enter a list of allowed footprints for the symbol. This list
acts as a filter used by CvPcb to display only the allowed footprints. A
void list does not filter anything.
:::

:::: imageblock
::: content
![eeschema_libedit_footprint_png](images/eeschema_libedit_footprint.png)
:::
::::

::: paragraph
Wild-card characters are allowed.
:::

::: paragraph
S014\* allows CvPcb to show all the footprints with a name starting by
SO14.
:::

::: paragraph
For a resistor, R? shows all the footprints with a 2 letters name
starting by R.
:::

::: paragraph
Here are samples: with and without filtering
:::

::: paragraph
With filtering
:::

:::: imageblock
::: content
![eeschema_cvpcb_with_filtering_png](images/eeschema_cvpcb_with_filtering.png)
:::
::::

::: paragraph
Without filtering
:::

:::: imageblock
::: content
![eeschema_cvpcb_without_filtering_png](images/eeschema_cvpcb_without_filtering.png)
:::
::::
::::::::::::::::
::::::::::::::::::::::::::::::

::::::::: sect2
### Symbol library

::: paragraph
You can easily compile a graphic symbols library file containing
frequently used symbols. This can be used for the creation of symbols
(triangles, the shape of AND, OR, Exclusive OR gates, etc.) for saving
and subsequent re-use.
:::

::: paragraph
These files are stored by default in the library directory and have a
\'.sym\' extension. These symbols are not gathered in libraries like the
normal symbols because they are generally not so many.
:::

:::: sect3
#### Export or create a symbol

::: paragraph
A symbol can be exported with the button
[![icons/export_png](images/icons/export.png)]{.image}. You can
generally create only one graphic, also it will be a good idea to delete
all pins, if they exist.
:::
::::

:::: sect3
#### Import a symbol

::: paragraph
Importing allows you to add graphics to a symbol you are editing. A
symbol is imported with the button [![Import graphic
icon](images/icons/import.png)]{.image}. Imported graphics are added as
they were created in existing graphics.
:::
::::
:::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::: sect1
## Symbol Library Browser {#viewlib}

:::::::::::::::::: sectionbody
:::::: sect2
### Introduction {#_introduction_5}

::: paragraph
The Symbol Library Browser allows you to quickly examine the content of
symbol libraries. The Symbol Library Viewer can be accessed by clicking
[![icons/library_browse_png](images/icons/library_browse.png)]{.image}
icon on the main toolbar, selecting \"Library Browser\" entry in the
\"View\" menu or double clicking symbol image on \"Choose Symbol\"
window.
:::

:::: imageblock
::: content
![eeschema_viewlib_choose_png](images/eeschema_viewlib_choose.png)
:::
::::
::::::

:::::::: sect2
### Viewlib - main screen

:::: imageblock
::: content
![eeschema_viewlib_select_library_png](images/eeschema_viewlib_select_library.png)
:::
::::

::: paragraph
To examine the contents of a library, select a library from the list on
the left hand pane. All symbols in the selected library will appear in
the second pane. Select a symbol name to view the symbol.
:::

:::: imageblock
::: content
![eeschema_viewlib_select_component_png](images/eeschema_viewlib_select_component.png)
:::
::::
::::::::

::::::: sect2
### Symbol Library Browser Top Toolbar {#viewlib-top-toolbar}

::: paragraph
The top tool bar in Symbol Library Brower is shown below.
:::

:::: imageblock
::: content
![](images/toolbar_viewlib.png)
:::
::::

::: paragraph
The available commands are:
:::

+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/library_png](images/icons/library.png)]{.image}             | Selection of the desired library which can be also     |
|                                                                      | selected in the displayed list.                        |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/add_component_png](images/icons/add_component.png)]{.image} | Selection of the symbol which can be also selected in  |
|                                                                      | the displayed list.                                    |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/lib_previous_png](images/icons/lib_previous.png)]{.image}   | Display previous symbol.                               |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/lib_next_png](images/icons/lib_next.png)]{.image}           | Display next symbol.                                   |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image} [![zoom               | Zoom tools.                                            |
| out](images/icons/zoom_out.png)]{.image} [![zoom                     |                                                        |
| redraw](images/icons/zoom_redraw.png)]{.image} [![zoom fit in        |                                                        |
| page](images/icons/zoom_fit_in_page.png)]{.image}                    |                                                        |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![morgan1](images/icons/morgan1.png)]{.image}                       | Selection of the representation (normal or converted)  |
| [![morgan2](images/icons/morgan2.png)]{.image}                       | if exist.                                              |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![](images/toolbar_viewlib_part.png){width="70%"}]{.image}          | Selection of the unit for symbols that contain         |
|                                                                      | multiple units.                                        |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/datasheet_png](images/icons/datasheet.png)]{.image}         | If it exist, display the associated documents. Exists  |
|                                                                      | only when called by the place symbol dialog frame from |
|                                                                      | Eeschema.                                              |
+----------------------------------------------------------------------+--------------------------------------------------------+
| [![icons/export_png](images/icons/export.png)]{.image}               | Close the browser and place the selected symbol in     |
|                                                                      | Eeschema. This icon is only displayed when browser has |
|                                                                      | been called from Eeschema (double click on a symbol in |
|                                                                      | the component chooser).                                |
+----------------------------------------------------------------------+--------------------------------------------------------+
:::::::
::::::::::::::::::
:::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Creating Customized Netlists and BOM Files

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::::::::::: sect2
### Intermediate Netlist File

::: paragraph
BOM files and netlist files can be converted from an Intermediate
netlist file created by Eeschema.
:::

::: paragraph
This file uses XML syntax and is called the intermediate netlist. The
intermediate netlist includes a large amount of data about your board
and because of this, it can be used with post-processing to create a BOM
or other reports.
:::

::: paragraph
Depending on the output (BOM or netlist), different subsets of the
complete Intermediate Netlist file will be used in the post-processing.
:::

::::: sect3
#### Schematic sample

:::: imageblock
::: content
![Schematic sample](images/schematic-sample.png)
:::
::::
:::::

:::::: sect3
#### The Intermediate Netlist file sample

::: paragraph
The corresponding intermediate netlist (using XML syntax) of the circuit
above is shown below.
:::

:::: listingblock
::: content
    <?xml version="1.0" encoding="utf-8"?>
    <export version="D">
      <design>
        <source>F:\kicad_aux\netlist_test\netlist_test.sch</source>
        <date>29/08/2010 20:35:21</date>
        <tool>eeschema (2010-08-28 BZR 2458)-unstable</tool>
      </design>
      <components>
        <comp ref="P1">
          <value>CONN_4</value>
          <libsource lib="conn" part="CONN_4"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E2141</tstamp>
        </comp>
        <comp ref="U2">
          <value>74LS74</value>
          <libsource lib="74xx" part="74LS74"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E20BA</tstamp>
        </comp>
        <comp ref="U1">
          <value>74LS04</value>
          <libsource lib="74xx" part="74LS04"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E20A6</tstamp>
        </comp>
        <comp ref="C1">
          <value>CP</value>
          <libsource lib="device" part="CP"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E2094</tstamp>
        </comp>
        <comp ref="R1">
          <value>R</value>
          <libsource lib="device" part="R"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E208A</tstamp>
        </comp>
      </components>
      <libparts>
        <libpart lib="device" part="C">
          <description>Condensateur non polarise</description>
          <footprints>
            <fp>SM*</fp>
            <fp>C?</fp>
            <fp>C1-1</fp>
          </footprints>
          <fields>
            <field name="Reference">C</field>
            <field name="Value">C</field>
          </fields>
          <pins>
            <pin num="1" name="~" type="passive"/>
            <pin num="2" name="~" type="passive"/>
          </pins>
        </libpart>
        <libpart lib="device" part="R">
          <description>Resistance</description>
          <footprints>
            <fp>R?</fp>
            <fp>SM0603</fp>
            <fp>SM0805</fp>
            <fp>R?-*</fp>
            <fp>SM1206</fp>
          </footprints>
          <fields>
            <field name="Reference">R</field>
            <field name="Value">R</field>
          </fields>
          <pins>
            <pin num="1" name="~" type="passive"/>
            <pin num="2" name="~" type="passive"/>
          </pins>
        </libpart>
        <libpart lib="conn" part="CONN_4">
          <description>Symbole general de connecteur</description>
          <fields>
            <field name="Reference">P</field>
            <field name="Value">CONN_4</field>
          </fields>
          <pins>
            <pin num="1" name="P1" type="passive"/>
            <pin num="2" name="P2" type="passive"/>
            <pin num="3" name="P3" type="passive"/>
            <pin num="4" name="P4" type="passive"/>
          </pins>
        </libpart>
        <libpart lib="74xx" part="74LS04">
          <description>Hex Inverseur</description>
          <fields>
            <field name="Reference">U</field>
            <field name="Value">74LS04</field>
          </fields>
          <pins>
            <pin num="1" name="~" type="input"/>
            <pin num="2" name="~" type="output"/>
            <pin num="3" name="~" type="input"/>
            <pin num="4" name="~" type="output"/>
            <pin num="5" name="~" type="input"/>
            <pin num="6" name="~" type="output"/>
            <pin num="7" name="GND" type="power_in"/>
            <pin num="8" name="~" type="output"/>
            <pin num="9" name="~" type="input"/>
            <pin num="10" name="~" type="output"/>
            <pin num="11" name="~" type="input"/>
            <pin num="12" name="~" type="output"/>
            <pin num="13" name="~" type="input"/>
            <pin num="14" name="VCC" type="power_in"/>
          </pins>
        </libpart>
        <libpart lib="74xx" part="74LS74">
          <description>Dual D FlipFlop, Set &amp; Reset</description>
          <docs>74xx/74hc_hct74.pdf</docs>
          <fields>
            <field name="Reference">U</field>
            <field name="Value">74LS74</field>
          </fields>
          <pins>
            <pin num="1" name="Cd" type="input"/>
            <pin num="2" name="D" type="input"/>
            <pin num="3" name="Cp" type="input"/>
            <pin num="4" name="Sd" type="input"/>
            <pin num="5" name="Q" type="output"/>
            <pin num="6" name="~Q" type="output"/>
            <pin num="7" name="GND" type="power_in"/>
            <pin num="8" name="~Q" type="output"/>
            <pin num="9" name="Q" type="output"/>
            <pin num="10" name="Sd" type="input"/>
            <pin num="11" name="Cp" type="input"/>
            <pin num="12" name="D" type="input"/>
            <pin num="13" name="Cd" type="input"/>
            <pin num="14" name="VCC" type="power_in"/>
          </pins>
        </libpart>
      </libparts>
      <libraries>
        <library logical="device">
          <uri>F:\kicad\share\library\device.lib</uri>
        </library>
        <library logical="conn">
          <uri>F:\kicad\share\library\conn.lib</uri>
        </library>
        <library logical="74xx">
          <uri>F:\kicad\share\library\74xx.lib</uri>
        </library>
      </libraries>
      <nets>
        <net code="1" name="GND">
          <node ref="U1" pin="7"/>
          <node ref="C1" pin="2"/>
          <node ref="U2" pin="7"/>
          <node ref="P1" pin="4"/>
        </net>
        <net code="2" name="VCC">
          <node ref="R1" pin="1"/>
          <node ref="U1" pin="14"/>
          <node ref="U2" pin="4"/>
          <node ref="U2" pin="1"/>
          <node ref="U2" pin="14"/>
          <node ref="P1" pin="1"/>
        </net>
        <net code="3" name="">
          <node ref="U2" pin="6"/>
        </net>
        <net code="4" name="">
          <node ref="U1" pin="2"/>
          <node ref="U2" pin="3"/>
        </net>
        <net code="5" name="/SIG_OUT">
          <node ref="P1" pin="2"/>
          <node ref="U2" pin="5"/>
          <node ref="U2" pin="2"/>
        </net>
        <net code="6" name="/CLOCK_IN">
          <node ref="R1" pin="2"/>
          <node ref="C1" pin="1"/>
          <node ref="U1" pin="1"/>
          <node ref="P1" pin="3"/>
        </net>
      </nets>
    </export>
:::
::::
::::::
:::::::::::::

::::: sect2
### Conversion to a new netlist format

::: paragraph
By applying a post-processing filter to the Intermediate netlist file
you can generate foreign netlist files as well as BOM files. Because
this conversion is a text to text transformation, this post-processing
filter can be written using Python, XSLT, or any other tool capable of
taking XML as input.
:::

::: paragraph
XSLT itself is an XML language very suitable for XML transformations.
There is a free program called *xsltproc* that you can download and
install. The xsltproc program can be used to read the Intermediate XML
netlist input file, apply a style-sheet to transform the input, and save
the results in an output file. Use of xsltproc requires a style-sheet
file using XSLT conventions. The full conversion process is handled by
Eeschema, after it is configured once to run xsltproc in a specific way.
:::
:::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2
### XSLT approach

::: paragraph
The document that describes XSL Transformations (XSLT) is available
here:
:::

::: paragraph
**[http://www.w3.org/TR/xslt](http://www.w3.org/TR/xslt){.bare}**
:::

:::::::::::::: sect3
#### Create a Pads-Pcb netlist file

::: paragraph
The pads-pcb format is comprised of two sections.
:::

::: ulist
- The footprint list.

- The Nets list: grouping pads references by nets.
:::

::: paragraph
Immediately below is a style-sheet which converts the Intermediate
Netlist file to a pads-pcb netlist format:
:::

:::: listingblock
::: content
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!--XSL style sheet to Eeschema Generic Netlist Format to PADS netlist format
        Copyright (C) 2010, SoftPLC Corporation.
        GPL v2.

        How to use:
            https://lists.launchpad.net/kicad-developers/msg05157.html
    -->

    <!DOCTYPE xsl:stylesheet [
      <!ENTITY nl  "&#xd;&#xa;"> <!--new line CR, LF -->
    ]>

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>

    <xsl:template match="/export">
        <xsl:text>*PADS-PCB*&nl;*PART*&nl;</xsl:text>
        <xsl:apply-templates select="components/comp"/>
        <xsl:text>&nl;*NET*&nl;</xsl:text>
        <xsl:apply-templates select="nets/net"/>
        <xsl:text>*END*&nl;</xsl:text>
    </xsl:template>

    <!-- for each component -->
    <xsl:template match="comp">
        <xsl:text> </xsl:text>
        <xsl:value-of select="@ref"/>
        <xsl:text> </xsl:text>
        <xsl:choose>
            <xsl:when test = "footprint != '' ">
                <xsl:apply-templates select="footprint"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>unknown</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>&nl;</xsl:text>
    </xsl:template>

    <!-- for each net -->
    <xsl:template match="net">
        <!-- nets are output only if there is more than one pin in net -->
        <xsl:if test="count(node)>1">
            <xsl:text>*SIGNAL* </xsl:text>
            <xsl:choose>
                <xsl:when test = "@name != '' ">
                    <xsl:value-of select="@name"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>N-</xsl:text>
                    <xsl:value-of select="@code"/>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:text>&nl;</xsl:text>
            <xsl:apply-templates select="node"/>
        </xsl:if>
    </xsl:template>

    <!-- for each node -->
    <xsl:template match="node">
        <xsl:text> </xsl:text>
        <xsl:value-of select="@ref"/>
        <xsl:text>.</xsl:text>
        <xsl:value-of select="@pin"/>
        <xsl:text>&nl;</xsl:text>
    </xsl:template>

    </xsl:stylesheet>
:::
::::

::: paragraph
And here is the pads-pcb output file after running xsltproc:
:::

:::: listingblock
::: content
    *PADS-PCB*
    *PART*
    P1 unknown
    U2 unknown
    U1 unknown
    C1 unknown
    R1 unknown
    *NET*
    *SIGNAL* GND
    U1.7
    C1.2
    U2.7
    P1.4
    *SIGNAL* VCC
    R1.1
    U1.14
    U2.4
    U2.1
    U2.14
    P1.1
    *SIGNAL* N-4
    U1.2
    U2.3
    *SIGNAL* /SIG_OUT
    P1.2
    U2.5
    U2.2
    *SIGNAL* /CLOCK_IN
    R1.2
    C1.1
    U1.1
    P1.3

    *END*
:::
::::

::: paragraph
The command line to make this conversion is:
:::

:::: listingblock
::: content
    kicad\\bin\\xsltproc.exe -o test.net kicad\\bin\\plugins\\netlist_form_pads-pcb.xsl test.tmp
:::
::::
::::::::::::::

::::::::::: sect3
#### Create a Cadstar netlist file

::: paragraph
The Cadstar format is comprised of two sections.
:::

::: ulist
- The footprint list.

- The Nets list: grouping pads references by nets.
:::

::: paragraph
Here is the style-sheet file to make this specific conversion:
:::

:::: listingblock
::: content
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!--XSL style sheet to Eeschema Generic Netlist Format to CADSTAR netlist format
        Copyright (C) 2010, Jean-Pierre Charras.
        Copyright (C) 2010, SoftPLC Corporation.
        GPL v2.

    <!DOCTYPE xsl:stylesheet [
      <!ENTITY nl  "&#xd;&#xa;"> <!--new line CR, LF -->
    ]>

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>

    <!-- Netlist header -->
    <xsl:template match="/export">
        <xsl:text>.HEA&nl;</xsl:text>
        <xsl:apply-templates select="design/date"/>  <!-- Generate line .TIM <time> -->
        <xsl:apply-templates select="design/tool"/>  <!-- Generate line .APP <eeschema version> -->
        <xsl:apply-templates select="components/comp"/>  <!-- Generate list of components -->
        <xsl:text>&nl;&nl;</xsl:text>
        <xsl:apply-templates select="nets/net"/>          <!-- Generate list of nets and connections -->
        <xsl:text>&nl;.END&nl;</xsl:text>
    </xsl:template>

     <!-- Generate line .TIM 20/08/2010 10:45:33 -->
    <xsl:template match="tool">
        <xsl:text>.APP "</xsl:text>
        <xsl:apply-templates/>
        <xsl:text>"&nl;</xsl:text>
    </xsl:template>

     <!-- Generate line .APP "eeschema (2010-08-17 BZR 2450)-unstable" -->
    <xsl:template match="date">
        <xsl:text>.TIM </xsl:text>
        <xsl:apply-templates/>
        <xsl:text>&nl;</xsl:text>
    </xsl:template>

    <!-- for each component -->
    <xsl:template match="comp">
        <xsl:text>.ADD_COM </xsl:text>
        <xsl:value-of select="@ref"/>
        <xsl:text> </xsl:text>
        <xsl:choose>
            <xsl:when test = "value != '' ">
                <xsl:text>"</xsl:text> <xsl:apply-templates select="value"/> <xsl:text>"</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>""</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>&nl;</xsl:text>
    </xsl:template>

    <!-- for each net -->
    <xsl:template match="net">
        <!-- nets are output only if there is more than one pin in net -->
        <xsl:if test="count(node)>1">
        <xsl:variable name="netname">
            <xsl:text>"</xsl:text>
            <xsl:choose>
                <xsl:when test = "@name != '' ">
                    <xsl:value-of select="@name"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:text>N-</xsl:text>
                    <xsl:value-of select="@code"/>
            </xsl:otherwise>
            </xsl:choose>
            <xsl:text>"&nl;</xsl:text>
            </xsl:variable>
            <xsl:apply-templates select="node" mode="first"/>
            <xsl:value-of select="$netname"/>
            <xsl:apply-templates select="node" mode="others"/>
        </xsl:if>
    </xsl:template>

    <!-- for each node -->
    <xsl:template match="node" mode="first">
        <xsl:if test="position()=1">
           <xsl:text>.ADD_TER </xsl:text>
        <xsl:value-of select="@ref"/>
        <xsl:text>.</xsl:text>
        <xsl:value-of select="@pin"/>
        <xsl:text> </xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="node" mode="others">
        <xsl:choose>
            <xsl:when test='position()=1'>
            </xsl:when>
            <xsl:when test='position()=2'>
               <xsl:text>.TER     </xsl:text>
            </xsl:when>
            <xsl:otherwise>
               <xsl:text>         </xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:if test="position()>1">
            <xsl:value-of select="@ref"/>
            <xsl:text>.</xsl:text>
            <xsl:value-of select="@pin"/>
            <xsl:text>&nl;</xsl:text>
        </xsl:if>
    </xsl:template>

    </xsl:stylesheet>
:::
::::

::: paragraph
Here is the Cadstar output file.
:::

:::: listingblock
::: content
    .HEA
    .TIM 21/08/2010 08:12:08
    .APP "eeschema (2010-08-09 BZR 2439)-unstable"
    .ADD_COM P1 "CONN_4"
    .ADD_COM U2 "74LS74"
    .ADD_COM U1 "74LS04"
    .ADD_COM C1 "CP"
    .ADD_COM R1 "R"

    .ADD_TER U1.7 "GND"
    .TER     C1.2
             U2.7
             P1.4
    .ADD_TER R1.1 "VCC"
    .TER     U1.14
             U2.4
             U2.1
             U2.14
             P1.1
    .ADD_TER U1.2 "N-4"
    .TER     U2.3
    .ADD_TER P1.2 "/SIG_OUT"
    .TER     U2.5
             U2.2
    .ADD_TER R1.2 "/CLOCK_IN"
    .TER     C1.1
             U1.1
             P1.3

    .END
:::
::::
:::::::::::

:::::::::: sect3
#### Create an OrcadPCB2 netlist file {#create-a-orcadpcb2-netlist-file}

::: paragraph
This format has only one section which is the footprint list. Each
footprint includes its list of pads with reference to a net.
:::

::: paragraph
Here is the style-sheet for this specific conversion:
:::

:::: listingblock
::: content
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <!--XSL style sheet to Eeschema Generic Netlist Format to CADSTAR netlist format
        Copyright (C) 2010, SoftPLC Corporation.
        GPL v2.

        How to use:
            https://lists.launchpad.net/kicad-developers/msg05157.html
    -->

    <!DOCTYPE xsl:stylesheet [
      <!ENTITY nl  "&#xd;&#xa;"> <!--new line CR, LF -->
    ]>

    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text" omit-xml-declaration="yes" indent="no"/>

    <!--
        Netlist header
        Creates the entire netlist
        (can be seen as equivalent to main function in C
    -->
    <xsl:template match="/export">
        <xsl:text>( { Eeschema Netlist Version 1.1  </xsl:text>
        <!-- Generate line .TIM <time> -->
    <xsl:apply-templates select="design/date"/>
    <!-- Generate line eeschema version ... -->
    <xsl:apply-templates select="design/tool"/>
    <xsl:text>}&nl;</xsl:text>

    <!-- Generate the list of components -->
    <xsl:apply-templates select="components/comp"/>  <!-- Generate list of components -->

    <!-- end of file -->
    <xsl:text>)&nl;*&nl;</xsl:text>
    </xsl:template>

    <!--
        Generate id in header like "eeschema (2010-08-17 BZR 2450)-unstable"
    -->
    <xsl:template match="tool">
        <xsl:apply-templates/>
    </xsl:template>

    <!--
        Generate date in header like "20/08/2010 10:45:33"
    -->
    <xsl:template match="date">
        <xsl:apply-templates/>
        <xsl:text>&nl;</xsl:text>
    </xsl:template>

    <!--
        This template read each component
        (path = /export/components/comp)
        creates lines:
         ( 3EBF7DBD $noname U1 74LS125
          ... pin list ...
          )
        and calls "create_pin_list" template to build the pin list
    -->
    <xsl:template match="comp">
        <xsl:text> ( </xsl:text>
        <xsl:choose>
            <xsl:when test = "tstamp != '' ">
                <xsl:apply-templates select="tstamp"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>00000000</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text> </xsl:text>
        <xsl:choose>
            <xsl:when test = "footprint != '' ">
                <xsl:apply-templates select="footprint"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>$noname</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text> </xsl:text>
        <xsl:value-of select="@ref"/>
        <xsl:text> </xsl:text>
        <xsl:choose>
            <xsl:when test = "value != '' ">
                <xsl:apply-templates select="value"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:text>"~"</xsl:text>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>&nl;</xsl:text>
        <xsl:call-template name="Search_pin_list" >
            <xsl:with-param name="cmplib_id" select="libsource/@part"/>
            <xsl:with-param name="cmp_ref" select="@ref"/>
        </xsl:call-template>
        <xsl:text> )&nl;</xsl:text>
    </xsl:template>

    <!--
        This template search for a given lib component description in list
        lib component descriptions are in /export/libparts,
        and each description start at ./libpart
        We search here for the list of pins of the given component
        This template has 2 parameters:
            "cmplib_id" (reference in libparts)
            "cmp_ref"   (schematic reference of the given component)
    -->
    <xsl:template name="Search_pin_list" >
        <xsl:param name="cmplib_id" select="0" />
        <xsl:param name="cmp_ref" select="0" />
            <xsl:for-each select="/export/libparts/libpart">
                <xsl:if test = "@part = $cmplib_id ">
                    <xsl:apply-templates name="build_pin_list" select="pins/pin">
                        <xsl:with-param name="cmp_ref" select="$cmp_ref"/>
                    </xsl:apply-templates>
                </xsl:if>
            </xsl:for-each>
    </xsl:template>


    <!--
        This template writes the pin list of a component
        from the pin list of the library description
        The pin list from library description is something like
              <pins>
                <pin num="1" type="passive"/>
                <pin num="2" type="passive"/>
              </pins>
        Output pin list is ( <pin num> <net name> )
        something like
                ( 1 VCC )
                ( 2 GND )
    -->
    <xsl:template name="build_pin_list" match="pin">
        <xsl:param name="cmp_ref" select="0" />

        <!-- write pin numner and separator -->
        <xsl:text>  ( </xsl:text>
        <xsl:value-of select="@num"/>
        <xsl:text> </xsl:text>

        <!-- search net name in nets section and write it: -->
        <xsl:variable name="pinNum" select="@num" />
        <xsl:for-each select="/export/nets/net">
            <!-- net name is output only if there is more than one pin in net
                 else use "?" as net name, so count items in this net
            -->
            <xsl:variable name="pinCnt" select="count(node)" />
            <xsl:apply-templates name="Search_pin_netname" select="node">
                <xsl:with-param name="cmp_ref" select="$cmp_ref"/>
                <xsl:with-param name="pin_cnt_in_net" select="$pinCnt"/>
                <xsl:with-param name="pin_num"> <xsl:value-of select="$pinNum"/>
                </xsl:with-param>
            </xsl:apply-templates>
        </xsl:for-each>

        <!-- close line -->
        <xsl:text> )&nl;</xsl:text>
    </xsl:template>

    <!--
        This template writes the pin netname of a given pin of a given component
        from the nets list
        The nets list description is something like
          <nets>
            <net code="1" name="GND">
              <node ref="J1" pin="20"/>
                  <node ref="C2" pin="2"/>
            </net>
            <net code="2" name="">
              <node ref="U2" pin="11"/>
            </net>
        </nets>
        This template has 2 parameters:
            "cmp_ref"   (schematic reference of the given component)
            "pin_num"   (pin number)
    -->

    <xsl:template name="Search_pin_netname" match="node">
        <xsl:param name="cmp_ref" select="0" />
        <xsl:param name="pin_num" select="0" />
        <xsl:param name="pin_cnt_in_net" select="0" />

        <xsl:if test = "@ref = $cmp_ref ">
            <xsl:if test = "@pin = $pin_num">
            <!-- net name is output only if there is more than one pin in net
                 else use "?" as net name
            -->
                <xsl:if test = "$pin_cnt_in_net>1">
                    <xsl:choose>
                        <!-- if a net has a name, use it,
                            else build a name from its net code
                        -->
                        <xsl:when test = "../@name != '' ">
                            <xsl:value-of select="../@name"/>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:text>$N-0</xsl:text><xsl:value-of select="../@code"/>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:if>
                <xsl:if test = "$pin_cnt_in_net &lt;2">
                    <xsl:text>?</xsl:text>
                </xsl:if>
            </xsl:if>
        </xsl:if>

    </xsl:template>

    </xsl:stylesheet>
:::
::::

::: paragraph
Here is the OrcadPCB2 output file.
:::

:::: listingblock
::: content
    ( { Eeschema Netlist Version 1.1  29/08/2010 21:07:51
    eeschema (2010-08-28 BZR 2458)-unstable}
     ( 4C6E2141 $noname P1 CONN_4
      (  1 VCC )
      (  2 /SIG_OUT )
      (  3 /CLOCK_IN )
      (  4 GND )
     )
     ( 4C6E20BA $noname U2 74LS74
      (  1 VCC )
      (  2 /SIG_OUT )
      (  3 N-04 )
      (  4 VCC )
      (  5 /SIG_OUT )
      (  6 ? )
      (  7 GND )
      (  14 VCC )
     )
     ( 4C6E20A6 $noname U1 74LS04
      (  1 /CLOCK_IN )
      (  2 N-04 )
      (  7 GND )
      (  14 VCC )
     )
     ( 4C6E2094 $noname C1 CP
      (  1 /CLOCK_IN )
      (  2 GND )
     )
     ( 4C6E208A $noname R1 R
      (  1 VCC )
      (  2 /CLOCK_IN )
     )
    )
    *
:::
::::
::::::::::

::::::::::::::::::::::::::::::::::::: sect3
#### Eeschema plugins interface

::: paragraph
Intermediate Netlist converters can be automatically launched within
Eeschema.
:::

::::::::: sect4
##### Init the Dialog window

::: paragraph
One can add a new netlist plug-in user interface tab by clicking on the
Add Plugin button.
:::

:::: imageblock
::: content
![eeschema_plugin_add_plugin_png](images/eeschema_plugin_add_plugin.png)
:::
::::

::: paragraph
Here is what the configuration data for the PadsPcb tab looks like:
:::

:::: imageblock
::: content
![eeschema_plugin_padspcb_png](images/eeschema_plugin_padspcb.png)
:::
::::
:::::::::

::::::: sect4
##### Plugin Configuration Parameters

::: paragraph
The Eeschema plug-in configuration dialog requires the following
information:
:::

::: ulist
- The title: for instance, the name of the netlist format.

- The command line to launch the converter.
:::

::: paragraph
Once you click on the netlist button the following will happen:
:::

::: {.olist .arabic}
1.  Eeschema creates an intermediate netlist file \*.xml, for instance
    test.xml.

2.  Eeschema runs the plug-in by reading test.xml and creates test.net.
:::
:::::::

::::::::::::::: sect4
##### Generate netlist files with the command line

::: paragraph
Assuming we are using the program *xsltproc.exe* to apply the sheet
style to the intermediate file, *xsltproc.exe* is executed with the
following command:
:::

::: paragraph
*xsltproc.exe -o \<output filename\> \< style-sheet filename\> \<input
XML file to convert\>*
:::

::: paragraph
In KiCad under Windows the command line is the following:
:::

::: paragraph
*f:/kicad/bin/xsltproc.exe -o \"%O\"
f:/kicad/bin/plugins/netlist_form_pads-pcb.xsl \"%I\"*
:::

::: paragraph
Under Linux the command becomes as follows:
:::

::: paragraph
*xsltproc -o \"%O\"
/usr/local/kicad/bin/plugins/netlist_form_pads-pcb.xsl \"%I\"*
:::

::: paragraph
Where *netlist_form_pads-pcb.xsl* is the style-sheet that you are
applying. Do not forget the double quotes around the file names, this
allows them to have spaces after the substitution by Eeschema.
:::

::: paragraph
The command line format accepts parameters for filenames:
:::

::: paragraph
The supported formatting parameters are.
:::

::: ulist
- %B ⇒ base filename and path of selected output file, minus path and
  extension.

- %I ⇒ complete filename and path of the temporary input file (the
  intermediate net file).

- %O ⇒ complete filename and path of the user chosen output file.
:::

::: paragraph
*%I* will be replaced by the actual intermediate file name
:::

::: paragraph
*%O* will be replaced by the actual output file name.
:::
:::::::::::::::

:::::::::: sect4
##### Command line format: example for xsltproc

::: paragraph
The command line format for xsltproc is the following:
:::

::: paragraph
\<path of xsltproc\> xsltproc \<xsltproc parameters\>
:::

::: paragraph
under Windows:
:::

::: paragraph
**f:/kicad/bin/xsltproc.exe -o \"%O\"
f:/kicad/bin/plugins/netlist_form_pads-pcb.xsl \"%I\"**
:::

::: paragraph
under Linux:
:::

::: paragraph
**xsltproc -o \"%O\"
/usr/local/kicad/bin/plugins/netlist_form_pads-pcb.xsl \"%I\"**
:::

::: paragraph
The above examples assume xsltproc is installed on your PC under Windows
and all files located in kicad/bin.
:::
::::::::::
:::::::::::::::::::::::::::::::::::::

::::::: sect3
#### Bill of Materials Generation

::: paragraph
Because the intermediate netlist file contains all information about
used components, a BOM can be extracted from it. Here is the plug-in
setup window (on Linux) to create a customized Bill Of Materials (BOM)
file:
:::

:::: imageblock
::: content
![bom-netlist-tab_png](images/en/bom-netlist-tab.png)
:::
::::

::: paragraph
The path to the style sheet bom2csv.xsl is system dependent. The
currently best XSLT style-sheet for BOM generation at this time is
called *bom2csv.xsl*. You are free to modify it according to your needs,
and if you develop something generally useful, ask that it become part
of the KiCad project.
:::
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::: sect2
### Command line format: example for python scripts

::: paragraph
The command line format for python is something like:
:::

::: paragraph
python \<script file name\> \<input filename\> \<output filename\>
:::

::: paragraph
under Windows:
:::

::: paragraph
**python \*.exe f:/kicad/python/my_python_script.py \"%I\" \"%O\"**
:::

::: paragraph
under Linux:
:::

::: paragraph
**python /usr/local/kicad/python/my_python_script.py \"%I\" \"%O\"**
:::

::: paragraph
Assuming python is installed on your PC.
:::
::::::::::

:::::::::::::::::::::::::::::::::::::::::::::: sect2
### Intermediate Netlist structure

::: paragraph
This sample gives an idea of the netlist file format.
:::

:::: listingblock
::: content
    <?xml version="1.0" encoding="utf-8"?>
    <export version="D">
      <design>
        <source>F:\kicad_aux\netlist_test\netlist_test.sch</source>
        <date>29/08/2010 21:07:51</date>
        <tool>eeschema (2010-08-28 BZR 2458)-unstable</tool>
      </design>
      <components>
        <comp ref="P1">
          <value>CONN_4</value>
          <libsource lib="conn" part="CONN_4"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E2141</tstamp>
        </comp>
        <comp ref="U2">
          <value>74LS74</value>
          <libsource lib="74xx" part="74LS74"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E20BA</tstamp>
        </comp>
        <comp ref="U1">
          <value>74LS04</value>
          <libsource lib="74xx" part="74LS04"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E20A6</tstamp>
        </comp>
        <comp ref="C1">
          <value>CP</value>
          <libsource lib="device" part="CP"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E2094</tstamp>
        <comp ref="R1">
          <value>R</value>
          <libsource lib="device" part="R"/>
          <sheetpath names="/" tstamps="/"/>
          <tstamp>4C6E208A</tstamp>
        </comp>
      </components>
      <libparts/>
      <libraries/>
      <nets>
        <net code="1" name="GND">
          <node ref="U1" pin="7"/>
          <node ref="C1" pin="2"/>
          <node ref="U2" pin="7"/>
          <node ref="P1" pin="4"/>
        </net>
        <net code="2" name="VCC">
          <node ref="R1" pin="1"/>
          <node ref="U1" pin="14"/>
          <node ref="U2" pin="4"/>
          <node ref="U2" pin="1"/>
          <node ref="U2" pin="14"/>
          <node ref="P1" pin="1"/>
        </net>
        <net code="3" name="">
          <node ref="U2" pin="6"/>
        </net>
        <net code="4" name="">
          <node ref="U1" pin="2"/>
          <node ref="U2" pin="3"/>
        </net>
        <net code="5" name="/SIG_OUT">
          <node ref="P1" pin="2"/>
          <node ref="U2" pin="5"/>
          <node ref="U2" pin="2"/>
        </net>
        <net code="6" name="/CLOCK_IN">
          <node ref="R1" pin="2"/>
          <node ref="C1" pin="1"/>
          <node ref="U1" pin="1"/>
          <node ref="P1" pin="3"/>
        </net>
      </nets>
    </export>
:::
::::

:::::::: sect3
#### General netlist file structure

::: paragraph
The intermediate Netlist accounts for five sections.
:::

::: ulist
- The header section.

- The components section.

- The lib parts section.

- The libraries section.

- The nets section.
:::

::: paragraph
The file content has the delimiter \<export\>
:::

:::: listingblock
::: content
    <export version="D">
    ...
    </export>
:::
::::
::::::::

::::::: sect3
#### The header section

::: paragraph
The header has the delimiter \<design\>
:::

:::: listingblock
::: content
    <design>
    <source>F:\kicad_aux\netlist_test\netlist_test.sch</source>
    <date>21/08/2010 08:12:08</date>
    <tool>eeschema (2010-08-09 BZR 2439)-unstable</tool>
    </design>
:::
::::

::: paragraph
This section can be considered a comment section.
:::
:::::::

::::::::::::: sect3
#### The components section

::: paragraph
The component section has the delimiter \<components\>
:::

:::: listingblock
::: content
    <components>
    <comp ref="P1">
    <value>CONN_4</value>
    <libsource lib="conn" part="CONN_4"/>
    <sheetpath names="/" tstamps="/"/>
    <tstamp>4C6E2141</tstamp>
    </comp>
    </components>
:::
::::

::: paragraph
This section contains the list of components in your schematic. Each
component is described like this:
:::

:::: listingblock
::: content
    <comp ref="P1">
    <value>CONN_4</value>
    <libsource lib="conn" part="CONN_4"/>
    <sheetpath names="/" tstamps="/"/>
    <tstamp>4C6E2141</tstamp>
    </comp>
:::
::::

+-------------------------+--------------------------------------------+
| **libsource**           | name of the lib where this component was   |
|                         | found.                                     |
+=========================+============================================+
| **part**                | component name inside this library.        |
+-------------------------+--------------------------------------------+
| **sheetpath**           | path of the sheet inside the hierarchy:    |
|                         | identify the sheet within the full         |
|                         | schematic hierarchy.                       |
+-------------------------+--------------------------------------------+
| **tstamps (time         | time stamp of the schematic file.          |
| stamps)**               |                                            |
+-------------------------+--------------------------------------------+
| **tstamp (time stamp)** | time stamp of the component.               |
+-------------------------+--------------------------------------------+

:::::: sect4
##### Note about time stamps for components

::: paragraph
To identify a component in a netlist and therefore on a board, the
timestamp reference is used as unique for each component. However KiCad
provides an auxiliary way to identify a component which is the
corresponding footprint on the board. This allows the re-annotation of
components in a schematic project and does not loose the link between
the component and its footprint.
:::

::: paragraph
A time stamp is an unique identifier for each component or sheet in a
schematic project. However, in complex hierarchies, the same sheet is
used more than once, so this sheet contains components having the same
time stamp.
:::

::: paragraph
A given sheet inside a complex hierarchy has an unique identifier: its
sheetpath. A given component (inside a complex hierarchy) has an unique
identifier: the sheetpath + its tstamp
:::
::::::
:::::::::::::

:::::::: sect3
#### The libparts section

::: paragraph
The libparts section has the delimiter \<libparts\>, and the content of
this section is defined in the schematic libraries. The libparts section
contains
:::

::: ulist
- The allowed footprints names (names use wildcards) delimiter \<fp\>.

- The fields defined in the library delimiter \<fields\>.

- The list of pins delimiter \<pins\>.
:::

:::: listingblock
::: content
    <libparts>
    <libpart lib="device" part="CP">
      <description>Condensateur polarise</description>
      <footprints>
        <fp>CP*</fp>
        <fp>SM*</fp>
      </footprints>
      <fields>
        <field name="Reference">C</field>
        <field name="Valeur">CP</field>
      </fields>
      <pins>
        <pin num="1" name="1" type="passive"/>
        <pin num="2" name="2" type="passive"/>
      </pins>
    </libpart>
    </libparts>
:::
::::

::: paragraph
Lines like \<pin num=\"1\" type=\"passive\"/\> give also the electrical
pin type. Possible electrical pin types are
:::

+-----------------+-----------------------------------------------------+
| Input           | Usual input pin                                     |
+-----------------+-----------------------------------------------------+
| Output          | Usual output                                        |
+-----------------+-----------------------------------------------------+
| Bidirectional   | Input or Output                                     |
+-----------------+-----------------------------------------------------+
| Tri-state       | Bus input/output                                    |
+-----------------+-----------------------------------------------------+
| Passive         | Usual ends of passive components                    |
+-----------------+-----------------------------------------------------+
| Unspecified     | Unknown electrical type                             |
+-----------------+-----------------------------------------------------+
| Power input     | Power input of a component                          |
+-----------------+-----------------------------------------------------+
| Power output    | Power output like a regulator output                |
+-----------------+-----------------------------------------------------+
| Open collector  | Open collector often found in analog comparators    |
+-----------------+-----------------------------------------------------+
| Open emitter    | Open emitter sometimes found in logic               |
+-----------------+-----------------------------------------------------+
| Not connected   | Must be left open in schematic                      |
+-----------------+-----------------------------------------------------+
::::::::

:::::: sect3
#### The libraries section

::: paragraph
The libraries section has the delimiter \<libraries\>. This section
contains the list of schematic libraries used in the project.
:::

:::: listingblock
::: content
    <libraries>
      <library logical="device">
        <uri>F:\kicad\share\library\device.lib</uri>
      </library>
      <library logical="conn">
        <uri>F:\kicad\share\library\conn.lib</uri>
      </library>
    </libraries>
:::
::::
::::::

:::::::::: sect3
#### The nets section

::: paragraph
The nets section has the delimiter \<nets\>. This section contains the
\"connectivity\" of the schematic.
:::

:::: listingblock
::: content
    <nets>
      <net code="1" name="GND">
        <node ref="U1" pin="7"/>
        <node ref="C1" pin="2"/>
        <node ref="U2" pin="7"/>
        <node ref="P1" pin="4"/>
      </net>
      <net code="2" name="VCC">
        <node ref="R1" pin="1"/>
        <node ref="U1" pin="14"/>
        <node ref="U2" pin="4"/>
        <node ref="U2" pin="1"/>
        <node ref="U2" pin="14"/>
        <node ref="P1" pin="1"/>
      </net>
    </nets>
:::
::::

::: paragraph
This section lists all nets in the schematic.
:::

::: paragraph
A possible net contains the following.
:::

:::: listingblock
::: content
    <net code="1" name="GND">
      <node ref="U1" pin="7"/>
      <node ref="C1" pin="2"/>
      <node ref="U2" pin="7"/>
      <node ref="P1" pin="4"/>
    </net>
:::
::::

+-------------+--------------------------------------------------------+
| net code    | is an internal identifier for this net                 |
+-------------+--------------------------------------------------------+
| name        | is a name for this net                                 |
+-------------+--------------------------------------------------------+
| node        | give a pin reference connected to this net             |
+-------------+--------------------------------------------------------+
::::::::::
::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2
### More about xsltproc

::: paragraph
Refer to the page:
*[http://xmlsoft.org/XSLT/xsltproc.html](http://xmlsoft.org/XSLT/xsltproc.html){.bare}*
:::

:::::: sect3
#### Introduction

::: paragraph
xsltproc is a command line tool for applying XSLT style-sheets to XML
documents. While it was developed as part of the GNOME project, it can
operate independently of the GNOME desktop.
:::

::: paragraph
xsltproc is invoked from the command line with the name of the
style-sheet to be used followed by the name of the file or files to
which the style-sheet is to be applied. It will use the standard input
if a filename provided is - .
:::

::: paragraph
If a style-sheet is included in an XML document with a Style-sheet
Processing Instruction, no style-sheet needs to be named in the command
line. xsltproc will automatically detect the included style-sheet and
use it. By default, the output is to *stdout*. You can specify a file
for output using the -o option.
:::
::::::

::::: sect3
#### Synopsis

:::: listingblock
::: content
    xsltproc [[-V] | [-v] | [-o *file* ] | [--timing] | [--repeat] |
    [--debug] | [--novalid] | [--noout] | [--maxdepth *val* ] | [--html] |
    [--param *name* *value* ] | [--stringparam *name* *value* ] | [--nonet] |
    [--path *paths* ] | [--load-trace] | [--catalogs] | [--xinclude] |
    [--profile] | [--dumpextensions] | [--nowrite] | [--nomkdir] |
    [--writesubtree] | [--nodtdattr]] [ *stylesheet* ] [ *file1* ] [ *file2* ]
    [ *....* ]
:::
::::
:::::

::::::::::::::::::::::::::::::::::::::::::::::::: sect3
#### Command line options

::: paragraph
*-V* or *\--version*
:::

::: paragraph
Show the version of libxml and libxslt used.
:::

::: paragraph
*-v* or *\--verbose*
:::

::: paragraph
Output each step taken by xsltproc in processing the stylesheet and the
document.
:::

::: paragraph
*-o* or *\--output file*
:::

::: paragraph
Direct output to the file named *file*. For multiple outputs, also known
as \`\`chunking\'\', -o directory/ directs the output files to a
specified directory. The directory must already exist.
:::

::: paragraph
*\--timing*
:::

::: paragraph
Display the time used for parsing the stylesheet, parsing the document
and applying the stylesheet and saving the result. Displayed in
milliseconds.
:::

::: paragraph
*\--repeat*
:::

::: paragraph
Run the transformation 20 times. Used for timing tests.
:::

::: paragraph
*\--debug*
:::

::: paragraph
Output an XML tree of the transformed document for debugging purposes.
:::

::: paragraph
*\--novalid*
:::

::: paragraph
Skip loading the document's DTD.
:::

::: paragraph
*\--noout*
:::

::: paragraph
Do not output the result.
:::

::: paragraph
*\--maxdepth value*
:::

::: paragraph
Adjust the maximum depth of the template stack before libxslt concludes
it is in an infinite loop. The default is 500.
:::

::: paragraph
*\--html*
:::

::: paragraph
The input document is an HTML file.
:::

::: paragraph
*\--param name value*
:::

::: paragraph
Pass a parameter of name *name* and value *value* to the stylesheet. You
may pass multiple name/value pairs up to a maximum of 32. If the value
being passed is a string rather than a node identifier, use
\--stringparam instead.
:::

::: paragraph
*\--stringparam name value*
:::

::: paragraph
Pass a paramenter of name *name* and value *value* where *value* is a
string rather than a node identifier. (Note: The string must be utf-8.)
:::

::: paragraph
*\--nonet*
:::

::: paragraph
Do not use the Internet to fetch DTD's, entities or documents.
:::

::: paragraph
*\--path paths*
:::

::: paragraph
Use the list (separated by space or column) of filesystem paths
specified by *paths* to load DTDs, entities or documents.
:::

::: paragraph
*\--load-trace*
:::

::: paragraph
Display to stderr all the documents loaded during the processing.
:::

::: paragraph
*\--catalogs*
:::

::: paragraph
Use the SGML catalog specified in SGML_CATALOG_FILES to resolve the
location of external entities. By default, xsltproc looks for the
catalog specified in XML_CATALOG_FILES. If that is not specified, it
uses /etc/xml/catalog.
:::

::: paragraph
*\--xinclude*
:::

::: paragraph
Process the input document using the Xinclude specification. More
details on this can be found in the Xinclude specification:
<http://www.w3.org/TR/xinclude/>
:::

::: paragraph
*\--profile \--norman*
:::

::: paragraph
Output profiling information detailing the amount of time spent in each
part of the stylesheet. This is useful in optimizing stylesheet
performance.
:::

::: paragraph
*\--dumpextensions*
:::

::: paragraph
Dumps the list of all registered extensions to stdout.
:::

::: paragraph
*\--nowrite*
:::

::: paragraph
Refuses to write to any file or resource.
:::

::: paragraph
*\--nomkdir*
:::

::: paragraph
Refuses to create directories.
:::

::: paragraph
*\--writesubtree path*
:::

::: paragraph
Allow file write only within the *path* subtree.
:::

::: paragraph
*\--nodtdattr*
:::

::: paragraph
Do not apply default attributes from the document's DTD.
:::
:::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::: sect3
#### Xsltproc return values

::: paragraph
xsltproc returns a status number that can be quite useful when calling
it within a script.
:::

::: paragraph
0: normal
:::

::: paragraph
1: no argument
:::

::: paragraph
2: too many parameters
:::

::: paragraph
3: unknown option
:::

::: paragraph
4: failed to parse the stylesheet
:::

::: paragraph
5: error in the stylesheet
:::

::: paragraph
6: error in one of the documents
:::

::: paragraph
7: unsupported xsl:output method
:::

::: paragraph
8: string parameter contains both quote and double-quotes
:::

::: paragraph
9: internal processing error
:::

::: paragraph
10: processing was stopped by a terminating message
:::

::: paragraph
11: could not write the result to the output file
:::
::::::::::::::::

::::: sect3
#### More Information about xsltproc

::: paragraph
libxml web page: <http://www.xmlsoft.org/>
:::

::: paragraph
W3C XSLT page: <http://www.w3.org/TR/xslt>
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1
## Simulator

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Eeschema provides an embedded electrical circuit simulator using
[ngspice](http://ngspice.sourceforge.net) as the simulation engine.
:::

::: paragraph
When working with the simulator, you may find the official *pspice*
library useful. It contains common symbols used for simulation like
voltage/current sources or transistors with pins numbered to match the
ngspice node order specification.
:::

::: paragraph
There are also a few demo projects to illustrate the simulator
capabilities. You will find them in *demos/simulation* directory.
:::

::::::::::::::::::::::::: sect2
### Assigning models {#_assigning_models}

::: paragraph
Before a simulation is launched, components need to have Spice model
assigned.
:::

::: paragraph
Each component can have only one model assigned, even if component
consists of multiple units. In such case, the first unit should have the
model specified.
:::

::: paragraph
[]{#sim-passive-models} Passive components with reference matching a
device type in Spice notation (*R\** for resistors, *C\** for
capacitors, *L\** for inductors) will have models assigned implicitly
and use the value field to determine their properties.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | Keep in mind that in Spice        |
| Note                              | notation \'M\' stands for milli   |
| :::                               | and \'Meg\' corresponds to mega.  |
|                                   | If you prefer to use \'M\' to     |
|                                   | indicate mega prefix, you may     |
|                                   | request doing so in the           |
|                                   | [simulation settings              |
|                                   | dialog](#sim-settings).           |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
Spice model information is stored as text in symbol fields, therefore
you may either define it in symbol editor or schematics editor. Open
symbol properties dialog and click on *Edit Spice Model* button to open
Spice Model Editor dialog.
:::

::: paragraph
Spice Model Editor dialog has three tabs corresponding to different
model types. There are two options common to all model types:
:::

+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| Disable symbol for | When checked the component is excluded from     |
| simulation         | simulation.                                     |
| :::                | :::                                             |
| ::::               | ::::                                            |
+--------------------+-------------------------------------------------+
| :::: content       | ::::::::: content                               |
| ::: paragraph      | ::: paragraph                                   |
| Alternate node     | Allows one to override symbol pin to model node |
| sequence           | mapping. To define a different mapping, specify |
| :::                | pin numbers in order expected by the model.     |
| ::::               | :::                                             |
|                    |                                                 |
|                    | ::: paragraph                                   |
|                    | \'Example:\'\                                   |
|                    | :::                                             |
|                    |                                                 |
|                    | ::: quoteblock                                  |
|                    | > ::: paragraph                                 |
|                    | > `* connections:`\                             |
|                    | > `* 1: non-inverting input`\                   |
|                    | > `* 2: inverting input`\                       |
|                    | > `* 3: positive power supply`\                 |
|                    | > `* 4: negative power supply`\                 |
|                    | > `* 5: output`\                                |
|                    | > `.subckt tl071 1 2 3 4 5`                     |
|                    | > :::                                           |
|                    | :::                                             |
|                    |                                                 |
|                    | :::: imageblock                                 |
|                    | ::: content                                     |
|                    | ![Generic operational amplifier                 |
|                    | symbol](images/opamp_symbol.png)                |
|                    | :::                                             |
|                    | ::::                                            |
|                    |                                                 |
|                    | ::: paragraph                                   |
|                    | To match the symbol pins to the Spice model     |
|                    | nodes shown above, one needs to use an          |
|                    | alternate node sequence option with value:      |
|                    | \"1 3 5 2 4\". It is a list of pin numbers      |
|                    | corresponding to the Spice model nodes order.   |
|                    | :::                                             |
|                    | :::::::::                                       |
+--------------------+-------------------------------------------------+

::::::: sect3
#### Passive {#_passive}

::: paragraph
*Passive* tab allows the user to assign a passive device model
(resistor, capacitor or inductor) to a component. It is a rarely used
option, as normally passive components have models assigned
[implicitly](#sim-passive-models), unless component reference does not
match the actual device type.
:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | Explicitly defined passive device |
| Note                              | models have priority over the     |
| :::                               | ones assigned implicitly. It      |
|                                   | means that once a passive device  |
|                                   | model is assigned, the reference  |
|                                   | and value fields are not taken    |
|                                   | into account during simulation.   |
|                                   | It may lead to a confusing        |
|                                   | situation when assigned model     |
|                                   | value does not match the one      |
|                                   | displayed on a schematic sheet.   |
+-----------------------------------+-----------------------------------+
:::

:::: imageblock
::: content
![Passive device model editor tab](images/sim_model_passive.png)
:::
::::

+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| Type               | Selects the device type (resistor, capacitor or |
| :::                | inductor).                                      |
| ::::               | :::                                             |
|                    | ::::                                            |
+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| Value              | Defines the device property (resistance,        |
| :::                | capacitance or inductance). The value may use   |
| ::::               | common Spice unit prefixes (as listed below the |
|                    | text input field) and should use point as the   |
|                    | decimal separator. Note that Spice does not     |
|                    | correctly interpret prefixes intertwined in the |
|                    | value (e.g. 1k5).                               |
|                    | :::                                             |
|                    | ::::                                            |
+--------------------+-------------------------------------------------+
:::::::

::::::: sect3
#### Model {#_model}

::: paragraph
*Model* tab is used to assign a semiconductor or a complex model defined
in an external library file. Spice model libraries are often offered by
device manufacturers.
:::

::: paragraph
The main text widget displays the selected library file contents. It is
a common practice to put models description inside library files,
including the node order.
:::

:::: imageblock
::: content
![Semiconductor device model editor tab](images/sim_model_subckt.png)
:::
::::

+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| File               | Path to a Spice library file. This file is      |
| :::                | going to be used by the simulator, as it is     |
| ::::               | added using *.include* directive.               |
|                    | :::                                             |
|                    | ::::                                            |
+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| Model              | Selected device model. When a file is selected, |
| :::                | the list is filled with available models to     |
| ::::               | choose from.                                    |
|                    | :::                                             |
|                    | ::::                                            |
+--------------------+-------------------------------------------------+
| :::: content       | :::: content                                    |
| ::: paragraph      | ::: paragraph                                   |
| Type               | Selects model type (subcircuit, BJT, MOSFET or  |
| :::                | diode). Normally it is set automatically when a |
| ::::               | model is selected.                              |
|                    | :::                                             |
|                    | ::::                                            |
+--------------------+-------------------------------------------------+
:::::::

:::::::: sect3
#### Source {#_source}

::: paragraph
*Source* tab is used to assign a power or signal source model. There are
two sections: *DC/AC analysis* and *Transient analysis*. Each defines
source parameters for the corresponding simulation type.
:::

::: paragraph
*Source type* option applies to all simulation types.
:::

:::: imageblock
::: content
![Source model editor tab](images/sim_model_source.png)
:::
::::

::: paragraph
Refer to the [ngspice
documentation](http://ngspice.sourceforge.net/docs/ngspice-27-manual.pdf),
chapter 4 (Voltage and Current Sources) for more details about sources.
:::
::::::::
:::::::::::::::::::::::::

:::: sect2
### Spice directives {#sim-directives}

::: paragraph
It is possible to add Spice directives by placing them in text fields on
a schematic sheet. This approach is convenient for defining the default
simulation type. This functionality is limited to Spice directives
starting with a dot (e.g. \".tran 10n 1m\"), it is not possible to place
additional components using text fields.
:::
::::

:::::::::::::::::::::::::::::::::::::::::::::::: sect2
### Simulation {#_simulation}

::: paragraph
To launch a simulation, open *Spice Simulator* dialog by selecting menu
*Tools→Simulator* in the schematics editor window.
:::

:::: imageblock
::: content
![Main simulation dialog](images/sim_main_dialog.png)
:::
::::

::: paragraph
The dialog is divided into several sections:
:::

::: ulist
- [Toolbar](#sim-toolbar)

- [Plot panel](#sim-plot-panel)

- [Output console](#sim-output-console)

- [Signals list](#sim-signals-list)

- [Cursors list](#sim-cursors-list)

- [Tune panel](#sim-tune-panel)
:::

:::::: sect3
#### Menu {#_menu}

::: sect4
##### File {#sim-menu-file}

+--------------------+-------------------------------------------------+
| New Plot           | Create a new tab in the plot panel.             |
+--------------------+-------------------------------------------------+
| Open Workbook      | Open a list of plotted signals.                 |
+--------------------+-------------------------------------------------+
| Save Workbook      | Save a list of plotted signals.                 |
+--------------------+-------------------------------------------------+
| Save as image      | Export the active plot to a .png file.          |
+--------------------+-------------------------------------------------+
| Save as .csv file  | Export the active plot raw data points to a     |
|                    | .csv file.                                      |
+--------------------+-------------------------------------------------+
| Exit Simulation    | Close the dialog.                               |
+--------------------+-------------------------------------------------+
:::

::: sect4
##### Simulation {#sim-menu-simulation}

+--------------------+-------------------------------------------------+
| Run Simulation     | Perform a simulation using the current          |
|                    | settings.                                       |
+--------------------+-------------------------------------------------+
| Add signals...​     | Open a dialog to select signals to be plotted.  |
+--------------------+-------------------------------------------------+
| Probe from         | Start the schematics [Probe](#sim-probe-tool)   |
| schematics         | tool.                                           |
+--------------------+-------------------------------------------------+
| Tune component     | Start the [Tuner](#sim-tuner-tool) tool.        |
| value              |                                                 |
+--------------------+-------------------------------------------------+
| Show SPICE         | Open a dialog showing the generated netlist for |
| Netlist...​         | the simulated circuit.                          |
+--------------------+-------------------------------------------------+
| Settings...​        | Open the [simulation settings                   |
|                    | dialog](#sim-settings).                         |
+--------------------+-------------------------------------------------+
:::

::: sect4
##### View {#sim-menu-view}

+--------------------+-------------------------------------------------+
| Zoom In            | Zoom in the active plot.                        |
+--------------------+-------------------------------------------------+
| Zoom Out           | Zoom out the active plot.                       |
+--------------------+-------------------------------------------------+
| Fit on Screen      | Adjust the zoom setting to display all plots.   |
+--------------------+-------------------------------------------------+
| Show grid          | Toggle grid visibility.                         |
+--------------------+-------------------------------------------------+
| Show legend        | Toggle plot legend visibility.                  |
+--------------------+-------------------------------------------------+
:::
::::::

:::::: sect3
#### Toolbar {#sim-toolbar}

:::: imageblock
::: content
![Simulation dialog top toolbar](images/sim_main_toolbar.png)
:::
::::

::: paragraph
The top toolbar provides access to the most frequently performed
actions.
:::

+--------------------+-------------------------------------------------+
| Run/Stop           | Start or stop the simulation.                   |
| Simulation         |                                                 |
+--------------------+-------------------------------------------------+
| Add Signals        | Open a dialog to select signals to be plotted.  |
+--------------------+-------------------------------------------------+
| Probe              | Start the schematics [Probe](#sim-probe-tool)   |
|                    | tool.                                           |
+--------------------+-------------------------------------------------+
| Tune               | Start the [Tuner](#sim-tuner-tool) tool.        |
+--------------------+-------------------------------------------------+
| Settings           | Open the [simulation settings                   |
|                    | dialog](#sim-settings).                         |
+--------------------+-------------------------------------------------+
::::::

::::::: sect3
#### Plot panel {#sim-plot-panel}

::: paragraph
Visualizes the simulation results as plots. One can have multiple plots
opened in separate tabs, but only the active one is updated when a
simulation is executed. This way it is possible to compare simulation
results for different runs.
:::

::: paragraph
Plots might be customized by toggling grid and legend visibility using
[View](#sim-menu-view) menu. When a legend is visible, it can be dragged
to change its position.
:::

::: paragraph
Plot panel interaction:
:::

::: ulist
- scroll mouse wheel to zoom in/out

- right click to open a context menu to adjust the view

- draw a selection rectangle to zoom in the selected area

- drag a cursor to change its coordinates
:::
:::::::

:::: sect3
#### Output console {#sim-output-console}

::: paragraph
Output console displays messages from the simulator. It is advised to
check the console output to verify there are no errors or warnings.
:::
::::

:::::: sect3
#### Signals list {#sim-signals-list}

::: paragraph
Shows the list of signals displayed in the active plot.
:::

::: paragraph
Signals list interaction:
:::

::: ulist
- right click to open a context menu to hide signal or toggle cursor

- double click to hide signal
:::
::::::

:::: sect3
#### Cursors list {#sim-cursors-list}

::: paragraph
Shows the list of cursors and their coordinates. Each signal may have
one cursor displayed. Cursors visibility is set using the
[Signals](#sim-signals-list) list.
:::
::::

::::::: sect3
#### Tune panel {#sim-tune-panel}

::: paragraph
Displays components picked with the [Tuner](#sim-tuner-tool) tool. Tune
panel allows the user to quickly modify component values and observe
their influence on the simulation results - every time a component value
is changed, the simulation is rerun and plots are updated.
:::

::: paragraph
For each component there a few controls associated:
:::

::: ulist
- The top text field sets the maximum component value.

- The middle text field sets the actual component value.

- The bottom text field sets the minimum component value.

- Slider allows the user to modify the component value in a smooth way.

- *Save* button modifies component value on the schematics to the one
  selected with the slider.

- *X* button removes component from the Tune panel and restores its
  original value.
:::

::: paragraph
The three text fields recognize Spice unit prefixes.
:::
:::::::

::::: sect3
#### Tuner tool {#sim-tuner-tool}

::: paragraph
Tuner tool lets the user pick components for tuning.
:::

::: paragraph
To select a component for tuning, click on one in the schematics editor
when the tool is active. Selected components will appear in the
[Tune](#sim-tune-panel) panel. Only passive components might be tuned.
:::
:::::

::::: sect3
#### Probe tool {#sim-probe-tool}

::: paragraph
Probe tool provides an user-friendly way of selecting signals for
plotting.
:::

::: paragraph
To add a signal to plot, click on a corresponding wire in the schematics
editor when the tool is active.
:::
:::::

:::::::::: sect3
#### Simulation settings {#sim-settings}

:::: imageblock
::: content
![Simulation settings dialog](images/sim_settings.png)
:::
::::

::: paragraph
Simulation settings dialog lets the user set the simulation type and
parameters. There are four tabs:
:::

::: ulist
- AC

- DC Transfer

- Transient

- Custom
:::

::: paragraph
The first three tabs provide forms where simulation parameters might be
specified. The last tab allows the user to type in custom Spice
directives to set up a simulation. You can find more information about
simulation types and parameters in the [ngspice
documentation](http://ngspice.sourceforge.net/docs/ngspice-27-manual.pdf),
chapter 1.2.
:::

::: paragraph
An alternative way to configure a simulation is to type [Spice
directives](#sim-directives) into text fields on schematics. Any text
field directives related to simulation type are overridden by the
settings selected in the dialog. It means that once you start using the
simulation dialog, the dialog overriddes the schematics directives until
the simulator is reopened.
:::

::: paragraph
There are two options common to all simulation types:
:::

+--------------------+-------------------------------------------------+
| Adjust passive     | Replace passive symbol values to convert common |
| symbol values      | component values notation to Spice notation.    |
+--------------------+-------------------------------------------------+
| Add full path for  | Prepend Spice model library file names with     |
| .include library   | full path. Normally full path is required by    |
| directives         | ngspice to access a library file.               |
+--------------------+-------------------------------------------------+
::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}
::: {#footer-text}
Last updated 2026-03-15 16:35:47 -0700
:::
::::
