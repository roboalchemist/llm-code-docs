:::::: {#header}

# Pcbnew

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}

::: {#toctitle}

Table of Contents
:::

- [Introduction to Pcbnew](#_introduction_to_pcbnew)

  - [Description](#_description)

  - [Principal design features](#_principal_design_features)

  - [General remarks](#_general_remarks)

- [Installation](#_installation)

  - [Installation of the software](#_installation_of_the_software)

  - [Modifying the default
    configuration](#_modifying_the_default_configuration)

  - [Managing Footprint Libraries](#_managing_footprint_libraries)

- [General operations](#_general_operations)

  - [Toolbars and commands](#_toolbars_and_commands)

  - [Mouse commands](#_mouse_commands)

  - [Selection of grid size](#_selection_of_grid_size)

  - [Adjustment of the zoom level](#_adjustment_of_the_zoom_level)

  - [Displaying cursor coordinates](#_displaying_cursor_coordinates)

  - [Keyboard commands - hotkeys](#_keyboard_commands_hotkeys)

  - [Operation on blocks](#_operation_on_blocks)

  - [Units used in dialogs](#_units_used_in_dialogs)

  - [Top menu bar](#_top_menu_bar)

  - [Using icons on the top toolbar](#_using_icons_on_the_top_toolbar)

  - [Right-hand side toolbar](#_right_hand_side_toolbar)

  - [Left-hand side toolbar](#_left_hand_side_toolbar)

  - [Pop-up windows and fast editing](#_pop_up_windows_and_fast_editing)

  - [Available modes](#_available_modes)

- [Schematic Implementation](#_schematic_implementation)

  - [Linking a schematic to a printed circuit
    board](#_linking_a_schematic_to_a_printed_circuit_board)

  - [Procedure for creating a printed circuit
    board](#_procedure_for_creating_a_printed_circuit_board)

  - [Procedure for updating a printed circuit
    board](#_procedure_for_updating_a_printed_circuit_board)

  - [Reading netlist file - loading
    footprints](#_reading_netlist_file_loading_footprints)

- [Layers](#_layers)

  - [Introduction](#_introduction)

  - [Setting up layers](#_setting_up_layers)

  - [Layer Description](#_layer_description)

  - [Selection of the active layer](#_selection_of_the_active_layer)

  - [Selection of the Layers for
    Vias](#_selection_of_the_layers_for_vias)

  - [Using the high-contrast mode](#_using_the_high_contrast_mode)

- [Create and modify a board](#_create_and_modify_a_board)

  - [Creating a board](#_creating_a_board)

  - [Correcting a board](#_correcting_a_board)

  - [Direct exchange for footprints already placed on
    board](#_direct_exchange_for_footprints_already_placed_on_board)

- [Footprint placement](#_footprint_placement)

  - [Assisted placement](#_assisted_placement)

  - [Manual placement](#_manual_placement)

  - [Automatic Footprint
    Distribution](#_automatic_footprint_distribution)

  - [Automatic placement of
    footprints](#_automatic_placement_of_footprints)

- [Setting routing parameters](#_setting_routing_parameters)

  - [Current settings](#_current_settings)

  - [General options](#_general_options)

  - [Netclasses](#_netclasses)

  - [Examples and typical dimensions](#_examples_and_typical_dimensions)

  - [Examples](#_examples)

  - [Manual routing](#_manual_routing)

  - [Help when creating tracks](#_help_when_creating_tracks)

  - [Select/edit the track width and via
    size](#_selectedit_the_track_width_and_via_size)

  - [Editing and changing tracks](#_editing_and_changing_tracks)

- [Interactive Router](#_interactive_router)

  - [Setting up](#_setting_up)

  - [Laying out tracks](#_laying_out_tracks)

  - [Setting track widths and via
    sizes](#_setting_track_widths_and_via_sizes)

  - [Dragging](#_dragging)

  - [Options](#_options)

- [Creating copper zones](#_creating_copper_zones)

  - [Creating zones on copper layers](#_creating_zones_on_copper_layers)

  - [Creating a zone](#_creating_a_zone)

  - [Filling options](#_filling_options)

  - [Adding a cutout area inside a
    zone](#_adding_a_cutout_area_inside_a_zone)

  - [Outlines editing](#_outlines_editing)

  - [Editing zone parameters](#_editing_zone_parameters)

  - [Final zone filling](#_final_zone_filling)

  - [Change zones net names](#_change_zones_net_names)

  - [Creating zones on technical
    layers](#_creating_zones_on_technical_layers)

  - [Creating a Keepout area](#_creating_a_keepout_area)

- [Files for circuit fabrication](#_files_for_circuit_fabrication)

  - [Final preparations](#_final_preparations)

  - [Final DRC test](#_final_drc_test)

  - [Setting coordinates origin](#_setting_coordinates_origin)

  - [Generating files for
    photo-tracing](#_generating_files_for_photo_tracing)

  - [Global clearance settings for the solder stop and the solder paste
    mask](#_global_clearance_settings_for_the_solder_stop_and_the_solder_paste_mask)

  - [Generating drill files](#_generating_drill_files)

  - [Generating wiring documentation](#_generating_wiring_documentation)

  - [Generation of files for automatic component
    insertion](#_generation_of_files_for_automatic_component_insertion)

  - [Advanced tracing options](#_advanced_tracing_options)

- [Footprint Editor - Managing
  Libraries](#_footprint_editor_managing_libraries)

  - [Overview of Footprint Editor](#_overview_of_footprint_editor)

  - [Accessing Footprint Editor](#_accessing_footprint_editor)

  - [Footprint Editor user interface](#_footprint_editor_user_interface)

  - [Top toolbar in Footprint Editor](#_top_toolbar_in_footprint_editor)

  - [Creating a new library](#_creating_a_new_library)

  - [Saving a footprint in the active
    library](#_saving_a_footprint_in_the_active_library)

  - [Transferring a footprint from one library to
    another](#_transferring_a_footprint_from_one_library_to_another)

  - [Saving all footprints of your board in the active
    library](#_saving_all_footprints_of_your_board_in_the_active_library)

  - [Documentation for library
    footprints](#_documentation_for_library_footprints)

  - [Documenting libraries - recommended
    practice](#_documenting_libraries_recommended_practice)

  - [Footprint Libraries Management](#_footprint_libraries_management)

  - [3D Shapes Libraries Management](#_3d_shapes_libraries_management)

- [Footprint Editor - Creating and Editing
  Footprints](#_footprint_editor_creating_and_editing_footprints)

  - [Footprint Editor Overview](#_footprint_editor_overview)

  - [Footprint Elements](#_footprint_elements)

  - [Starting Footprint Editor and Selecting a Footprint to
    Edit](#_starting_footprint_editor_and_selecting_a_footprint_to_edit)

  - [Footprint Editor Toolbars](#_footprint_editor_toolbars)

  - [Context Menus](#_context_menus)

  - [Footprint Properties Dialog](#_footprint_properties_dialog)

  - [Creating a New Footprint](#_creating_a_new_footprint)

  - [Adding and Editing Pads](#_adding_and_editing_pads)

  - [Fields Properties](#_fields_properties)

  - [Automatic Placement of a
    Footprint](#_automatic_placement_of_a_footprint)

  - [Attributes](#_attributes)

  - [Documenting Footprints in a
    Library](#_documenting_footprints_in_a_library)

  - [3-Dimensional Visualization](#_3_dimensional_visualization)

  - [Saving a Footprint into the Active
    Library](#_saving_a_footprint_into_the_active_library)

  - [Saving a footprint to the board](#_saving_a_footprint_to_the_board)

- [Advanced PCB editing tools](#_advanced_pcb_editing_tools)

  - [Duplicating items](#_duplicating_items)

  - [Moving items exactly](#_moving_items_exactly)

  - [Array tools](#_array_tools)

  - [Measurement (ruler) tool](#_measurement_ruler_tool)

- [KiCad Scripting Reference](#_kicad_scripting_reference)

  - [KiCad Objects](#_kicad_objects)

  - [Basic API Reference](#_basic_api_reference)

  - [Loading and Saving a Board](#_loading_and_saving_a_board)

  - [Listing and Loading Libraries](#_listing_and_loading_libraries)

  - [BOARD](#_board)

  - [Examples](#_examples_2)

  - [Footprint Wizards](#Footprint_Wizards)

  - [Action Plugins](#action_menu)
::::
::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::: {#preamble}

:::::::::::::: sectionbody
::: paragraph
*Reference manual*
:::

::: {#copyright .paragraph}

**Copyright**
:::

::: paragraph
This document is Copyright © 2010-2015 by its contributors as listed
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

- About KiCad software i18n:
  [https://github.com/KiCad/kicad-i18n/issues](https://github.com/KiCad/kicad-i18n/issues){.bare}
:::

::: {#publication_date_and_software_version .paragraph}

**Publication date and software version**
:::

::: paragraph
2014, march 17.
:::
::::::::::::::
:::::::::::::::

::::::::::::::::::::::::::: sect1

## Introduction to Pcbnew {#_introduction_to_pcbnew}

:::::::::::::::::::::::::: sectionbody
::::::::: sect2

### Description {#_description}

::: paragraph
Pcbnew is a powerful printed circuit board software tool available for
the Linux, Microsoft Windows and Apple OS X operating systems. Pcbnew is
used in association with the schematic capture program Eeschema to
create printed circuit boards.
:::

::: paragraph
Pcbnew manages libraries of footprints. Each footprint is a drawing of
the physical component including its land pattern (the layout of pads on
the circuit board). The required footprints are automatically loaded
during the reading of the Netlist. Any changes to footprint selection or
annotation can be changed in the schematic and updated in pcbnew by
regenerating the netlist and reading it in pcbnew again.
:::

::: paragraph
Pcbnew provides a design rules check (DRC) tool which prevents track and
pad clearance issues as well as preventing nets from being connected
that aren't connected in the netlist/schematic. When using the
interactive router it continuously runs the design rules check and will
help automatically route individual traces.
:::

::: paragraph
Pcbnew provides a rats nest display, a hairline connecting the pads of
footprints which are connected on the schematic. These connections move
dynamically as track and footprint movements are made.
:::

::: paragraph
Pcbnew has a simple but effective autorouter to assist in the production
of the circuit board. An Export/Import in SPECCTRA dsn format allows the
use of more advanced auto-routers.
:::

::: paragraph
Pcbnew provides options specifically provided for the production of
ultra high frequency microwave circuits (such as pads of trapezoidal and
complex form, automatic layout of coils on the printed circuit, etc).
:::
:::::::::

::::::::::::::: sect2

### Principal design features {#_principal_design_features}

::: paragraph
The smallest unit in pcbnew is 1 nanometer. All dimensions are stored as
integer nanometers.
:::

::: paragraph
Pcbnew can generate up to 32 layers of copper, 14 technical layers (silk
screen, solder mask, component adhesive, solder paste and edge cuts)
plus 4 auxiliary layers (drawings and comments) and manages in real time
the hairline indication (rats nest) of missing tracks.
:::

::: paragraph
The display of the PCB elements (tracks, pads, text, drawings...​) is
customizable:
:::

::: ulist

- In full or outline.

- With or without track clearance.
:::

::: paragraph
For complex circuits, the display of layers, zones, and components can
be hidden in a selective way for clarity on screen. Nets of traces can
be highlighted to provide high contrast as well.
:::

::: paragraph
Footprints can be rotated to any angle, with a resolution of 0.1 degree.
:::

::: paragraph
Pcbnew includes a Footprint Editor that allows editing of individual
footprints that have been on a pcb or editing a footprint in a library.
:::

::: paragraph
The Footprint Editor provides many time saving tools such as:
:::

::: ulist

- Fast pad numbering by simply dragging the mouse over pads in the order
  you want them numbered.

- Easy generation of rectangular and circular arrays of pads for LGA/BGA
  or circular footprints.

- Semi-automatic aligning of rows or columns of pads.
:::

::: paragraph
Footprint pads have a variety of properties that can be adjusted. The
pads can be round, rectangular, oval or trapezoidal. For through-hole
parts drills can be offset inside the pad and be round or a slot.
Individual pads can also be rotated and have unique soldermask, net, or
paste clearance. Pads can also have a solid connection or a thermal
relief connection for easier manufacturing. Any combination of unique
pads can be placed within a footprint.
:::

::: paragraph
Pcbnew easily generates all the documents necessary for production:
:::

::: ulist

- Fabrication outputs:

  ::: ulist

  - Files for Photoplotters in GERBER RS274X format.

  - Files for drilling in EXCELLON format.
  :::

- Plot files in HPGL, SVG and DXF format.

- Plot and drilling maps in POSTSCRIPT format.

- Local Printout.
:::
:::::::::::::::

::::: sect2

### General remarks {#_general_remarks}

::: paragraph
Due to the degree of control necessary it is highly suggested to use a
3-button mouse with pcbnew. Many features such as panning and zooming
require a 3-button mouse.
:::

::: paragraph
In the new release of KiCad, pcbnew has seen wide sweeping changes from
developers at CERN. This includes features such as a new renderer
(OpenGL and Cairo view modes), an interative push and shove router,
differential and meander trace routing and tuning, a reworked Footprint
Editor, and many other features. Please note that most of these new
features **only** exist in the new OpenGL and Cairo view modes.
:::
:::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Installation {#_installation}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2

### Installation of the software {#_installation_of_the_software}

::: paragraph
The installation procedure is described in the KiCad documentation.
:::
::::

::::::: sect2

### Modifying the default configuration {#_modifying_the_default_configuration}

::: paragraph
A default configuration file `kicad.pro` is provided in
`kicad/share/template`. This file is used as the initial configuration
for all new projects.
:::

::: paragraph
This configuration file can be modified to change the libraries to be
loaded.
:::

::: paragraph
To do this:
:::

::: ulist

- Launch Pcbnew using kicad or directly. On Windows it is in
  `C:\kicad\bin\pcbnew.exe` and on Linux you can run
  `/usr/local/kicad/bin/kicad` or `/usr/local/kicad/bin/pcbnew` if the
  binaries are located in `/usr/local/kicad/bin`.

- Select Preferences - Libs and Dir.

- Edit as required.

- Save the modified configuration (Save Cfg) to
  `kicad/share/template/kicad.pro`.
:::
:::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Managing Footprint Libraries {#_managing_footprint_libraries}

::: paragraph
As of release 4.0, Pcbnew organises the footprint libraries using files
called \"footprint library tables\". A footprint library table contains
descriptions of some number of individual footprint libraries, along
with a \"nickname\" for each library, which is used to refer to that
library when referencing a footprint.
:::

::: paragraph
There are several kinds of library supported by Pcbnew, each of which is
supported by a \"plugin\":
:::

::: ulist

- KiCad - native KiCad footprint libraries stored on a local filesystem
  in the *.pretty* format (folders containing *.kicad_mod* files)

- Github - native KiCad footprint libraries in the *.pretty* format,
  stored online as a Github repository

- Legacy - old-style KiCad footprint libraries (*.mod* files)

- Eagle - Eagle footprint libraries (folders containing *.fp* files)

- Geda-PCB - Geda PCB libraries
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - You can write only KiCad        |
| :::                               |   *.pretty* footprint library     |
|                                   |   folders on your local disk (and |
|                                   |   the .kicad_mod files inside     |
|                                   |   these folders).                 |
|                                   |                                   |
|                                   | - All other formats are read      |
|                                   |   only.                           |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
It is allowed to have footprints with the same name in different
libraries. The footprint will be stored as a combination of library
*and* footprint name, ensuring that the correct footprint is loaded from
the appropriate library.
:::

::: paragraph
There are two footprint library tables: the global one and the project
one.
:::

:::: sect3

#### Global Footprint Library Table {#_global_footprint_library_table}

::: paragraph
The global footprint library table contains the list of libraries that
are always available regardless of the currently loaded project file.
The table is saved in the file `fp-lib-table` in the user's home folder.
The location of this folder is dependent on the operating system.
:::
::::

::::: sect3

#### Project Specific Footprint Library Table {#_project_specific_footprint_library_table}

::: paragraph
The project specific footprint library table contains the list of
libraries that are available specifically for the currently loaded
project file. The project specific footprint library table can only be
edited when it is loaded along with the project board file. If no
project file is loaded or there is no footprint library table file in
the project path, an empty table is created which can be edited and
later saved along with the board file.
:::

::: paragraph
When entries are defined in the project specific table, an
\`fp-lib-table file \`containing the entries will be written into the
folder of the currently open PCB.
:::
:::::

:::::::: sect3

#### Initial Configuration {#_initial_configuration}

::: paragraph
The first time CvPcb or Pcbnew is run and the global footprint table
file `fp-lib-table` is not found in the user's home folder, Pcbnew will
attempt to copy the default footprint table file `fp_global_table`
stored in the system's KiCad template folder to the file `fp-lib-table`
in the user's home folder. If `fp_global_table` cannot be found, an
empty footprint library table will be created in the user's home folder.
If this happens, the user can either copy `fp_global_table` manually or
configure the table by hand.
:::

::: paragraph
The default footprint library table includes all of the standard
footprint libraries that are installed as part of KiCad.
:::

::: {.admonitionblock .tip}

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ::: title                         | ::: paragraph                                                                                                              |
| Tip                               | There are also sample `fp-lib-table` files in the official [KiCad library                                                  |
| :::                               | repository](https://github.com/KiCad/kicad-library) that you can use as your own starting point:                           |
|                                   | :::                                                                                                                        |
|                                   |                                                                                                                            |
|                                   | ::: ulist                                                                                                                  |
|                                   | - All KiCad libraries via Github:                                                                                          |
|                                   |   [fp-lib-table.for-github](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-github)           |
|                                   |                                                                                                                            |
|                                   | - All KiCad libraries, assuming they are on your disk already (you will need to download them if you do not already have   |
|                                   |   them): [fp-lib-table.for-pretty](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-pretty)    |
|                                   |                                                                                                                            |
|                                   | - Standard Eagle libraries (for Eagle 6.4.0)                                                                               |
|                                   |   [fp-lib-table.for-eagle-6.4.0](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-eagle-6.4.0) |
|                                   | :::                                                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
:::

::: paragraph
The **first thing** to do when configuring KiCad do is to modify this
table (add/remove entries) according to your work and the libraries you
need for your projects.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | It can be time consuming to have  |
| Tip                               | many libraries, especially if     |
| :::                               | they are only found online (such  |
|                                   | as the Github libraries). If you  |
|                                   | find libraries slow to load, try  |
|                                   | removing ones you don't need.     |
+-----------------------------------+-----------------------------------+
:::
::::::::

::::::::::::::: sect3

#### Adding Table Entries using the Libraries Manager {#_adding_table_entries_using_the_libraries_manager}

::: paragraph
The library table manager is accessible by:
:::

:::: imageblock
::: content
![Library tables menu item](images/Library_tables_menu_item.png)
:::
::::

::: paragraph
The image below shows the footprint library table editing dialog which
can be opened by invoking the \"Footprint Libraries Manager\" entry from
the \"Preferences\" menu.
:::

:::: imageblock
::: content
![Footprint tables list](images/Footprint_tables_list.png)
:::
::::

::: paragraph
In order to use a footprint library, it must first be added to either
the global table or the project specific table. The project specific
table is only applicable when a board file is open.
:::

::: paragraph
Each library table entry has a nickname. This *must* be unique within
that table. The nickname does not have to be related in any way to the
actual library file name or path.
:::

::: paragraph
There are some rules for valid library table entries:
:::

::: ulist

- The colon `:` character cannot be used anywhere in the nickname.

- Each library entry must have a valid path and/or file name depending
  on the type of library. Paths can be defined as absolute, relative, or
  by environment variable substitution (see below)

- The appropriate plug in type must be selected in order for the library
  to be properly read.
:::

::: paragraph
There is also a description field to add a description of the library
entry. The option field contains special options that are
plugin-specific and is generally blank.
:::

::: paragraph
Although you cannot have duplicate library nicknames in the same table,
you can have duplicate library nicknames in both the global and project
specific footprint library table. The project specific table entry will
take precedence over the global table entry when duplicated names occur.
:::
:::::::::::::::

::::::: sect3

#### Environment Variable Substitution {#_environment_variable_substitution}

::: paragraph
One of the most powerful features of the footprint library table is
environment variable substitution. This allows you to define custom
paths to where your libraries are stored in environment variables.
:::

::: paragraph
Environment variable substitution is supported by using the syntax
`${ENV_VAR_NAME}` in the footprint library path.
:::

::: paragraph
There are some default variables that KiCad defines:
:::

::: ulist

- `$KISYSMOD`: This points to where the default footprint libraries that
  were installed along with KiCad are located. You can override
  `$KISYSMOD` by defining it yourself which allows you to substitute
  your own libraries in place of the default KiCad footprint libraries.

- When a board file is loaded, `$KPRJMOD` is defined using that board's
  path. This allows you to refer to libraries in the project path
  without having to repeat the absolute path to the library in the
  project specific footprint library table.
:::
:::::::

:::::::::::::::::::::::::::::::::::::: sect3

#### Adding Table Entries using the Library Wizard {#_adding_table_entries_using_the_library_wizard}

::: paragraph
There is an interactive wizard that can assist you adding libraries to
your library tables. It is accessible from the menu:
:::

:::: imageblock
::: content
![Library tables menu item](images/Library_tables_menu_item.png)
:::
::::

::: paragraph
It can also be launched from the library manager, using the \"Append
With Wizard\" button.
:::

::: paragraph
Here, the local libraries option is selected.
:::

:::: imageblock
::: content
![Footprint library wizard local
libstartpage](images/en/fplib_wizard_locallibstartpage.png)
:::
::::

::: paragraph
Here, the remote libraries option is selected.
:::

:::: imageblock
::: content
![Footprint library wizard startpage
GitHub](images/en/fplib_wizard_startpage_github.png)
:::
::::

::: paragraph
The wizard will then lead you though the steps to adding a library,
which will depend on the type of library you are adding. The process for
each type will be explained below.
:::

::: paragraph
After a set of libraries is selected, the next page validates the
choice:
:::

:::: imageblock
::: content
![Footprint libary wizard validate](images/en/fplib_wizard_validate.png)
:::
::::

::: paragraph
If some selected libraries are incorrect (not supported, not a footprint
library ...​) they will be flagged as \`\`INVALID\'\'.
:::

::: paragraph
The last choice is the footprint library table to populate either:
:::

::: ulist

- the global table, or

- the project specific table
:::

:::: imageblock
::: content
![Footprint library wizard choose local
folder](images/en/fplib_wizard_chooseflt.png)
:::
::::

::::::::: sect4

##### Adding Existing Local Libraries {#_adding_existing_local_libraries}

::: paragraph
You might have local libraries already on your computer. For example:
:::

::: ulist

- Previously downloaded KiCad pretty directories

- Legacy KiCad *.mod* files from older installations

- Geda or Eagle libraries
:::

::: paragraph
These can be added with the \"Files on my computer\" option. You will be
asked for the directory of the library to add and the format:
:::

:::: imageblock
::: content
![Footprint library wizard local lib
selection](images/en/fplib_wizard_locallibselection.png)
:::
::::

::: paragraph
If you don't select the format, the wizard will try to guess the right
format.
:::
:::::::::

::::::::::: sect4

##### Adding Libraries from Github {#_adding_libraries_from_github}

::: paragraph
The wizard can also add libraries from Github with the \"Github
repository\" option.
:::

::: paragraph
You need to specify the Github account that contains the repositories
you want to add.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-------------------------------------------------------------+
| ::: title                         | The offical KiCad library Github account is                 |
| Tip                               | [https://github.com/KiCad](https://github.com/KiCad){.bare} |
| :::                               |                                                             |
+-----------------------------------+-------------------------------------------------------------+
:::

::: paragraph
You may choose to save a local copy. If you do *not* save a local copy,
the library will be a *Github* library, and will resync on every library
reload. If you *do* save a local copy, the library will be a *KiCad*
(pretty) library and will not automatically update in future.
:::

::: paragraph
The next page will load a list of *.pretty* repositories found on that
Github account. You can choose any number to add to the library.
:::

:::: imageblock
::: content
![Footprint library wizard GitHub
selection](images/en/fplib_wizard_githubselection.png)
:::
::::

::: paragraph
After confirmation,if you opted to save a copy, the footprints will be
downloaded to the specified local location now. If you are using the
Github plugin (no local copy), the footprints are loaded from Github
when needed.
:::
:::::::::::
::::::::::::::::::::::::::::::::::::::

:::::::::::: sect3

#### Using the KiCad plugin {#_using_the_kicad_plugin}

::: paragraph
The KiCad plugin deals with native KiCad libraries that exist on your
computer (or some accessible filesystem).
:::

::: paragraph
It is used for pre-installed libraries that are installed along with
KiCad, as well as other KiCad libraries, either from the official KiCad
library collection, 3rd party libraries or your own curated libraries.
:::

::::::::: sect4

##### Installing KiCad plugin libraries {#_installing_kicad_plugin_libraries}

::: paragraph
The Footprint Library Wizard can help you install libraries already on
disk or on Github. However, for libraries on disk, you need to put them
there yourself in the first place.
:::

::: paragraph
A KiCad library is a directory that contains some number of *.kicad_mod*
files.
:::

::: paragraph
This is often done by unpacking an archive file, copying a directory
from another location, or cloning a version-controlled repository.
:::

::: paragraph
The KiCad plugin does not specify any kind of version control, but Git
is very commonly used to track changes to libraries, which can be
critical to ensuring library data is safely recorded and backed up.
:::

::: paragraph
It is easy to track changes and contribute with the offical KiCad Github
libraries. This is done using the Git version control software. If you
want to contribute back, you'll have to fork the repos on Github so you
can send pull requests. If you just want to update libraries when
needed, you don't need to do that, you can clone the offical KiCad
libraries directly and pull as needed.
:::

::: {.admonitionblock .note}

+-----------------------------------+------------------------------------------------------------------------------------+
| ::: title                         | Sending pull requests via Github will allow the automatic library standards        |
| Note                              | checker to verify your proposed changes. See [KiCad Library                        |
| :::                               | Conventions](https://github.com/KiCad/kicad-library/wiki/Kicad-Library-Convention) |
|                                   | for details of the library conventions.                                            |
+-----------------------------------+------------------------------------------------------------------------------------+
:::
:::::::::
::::::::::::

:::::::::::::::::::::::::: sect3

#### Using the GitHub Plugin {#_using_the_github_plugin}

::: paragraph
The GitHub plugin is a special plugin that provides an interface for
read-only access to a remote GitHub repository consisting of *.pretty*
footprints and optionally provides \"Copy-On-Write\" (COW) support for
editing footprints read from the GitHub repo and saving them locally.
:::

::: {.admonitionblock .important}

+-----------------------------------+----------------------------------------------------+
| ::: title                         | ::: ulist                                          |
| Important                         | - The \"GitHub\" plugin is for **read-only access  |
| :::                               |   of remote pretty footprint libraries** at        |
|                                   |   [https://github.com](https://github.com){.bare}. |
|                                   |                                                    |
|                                   | - You will not be told if a remote repository      |
|                                   |   changed since your last use of it. Be cautious   |
|                                   |   when using footprint directly from Github.       |
|                                   | :::                                                |
+-----------------------------------+----------------------------------------------------+
:::

::: paragraph
To add a GitHub entry to the footprint library table the \"Library
Path\" in the footprint library table entry must be set to a valid
GitHub URL.
:::

::: paragraph
For example:
:::

:::: literalblock
::: content
    https://github.com/liftoff-sr/pretty_footprints
:::
::::

::: paragraph
Typically GitHub URLs take the form:
:::

:::: literalblock
::: content
    https://github.com/user_name/repo_name
:::
::::

::: paragraph
The \"Plugin Type\" must be set to \"Github\".
:::

::: paragraph
The table below shows a footprint library table entry with the default
options (no COW support):
:::

+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-------------+-------------+
| Nickname    | Library Path                                                                                              | Plugin Type | Options     | Description |
+=============+===========================================================================================================+=============+=============+=============+
| github      | [https://github.com/liftoff-sr/pretty_footprints](https://github.com/liftoff-sr/pretty_footprints){.bare} | Github      |             | Liftoff's   |
|             |                                                                                                           |             |             | GH          |
|             |                                                                                                           |             |             | footprints  |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-------------+-------------+

:::::::: sect4

##### Copy-On-Write {#_copy_on_write}

::: paragraph
To enable the \"Copy-On-Write\" feature the option
`allow_pretty_writing_to_this_dir` must be added to the \"Options\"
setting of the footprint library table entry. This option is the
\"Library Path\" for local storage of modified copies of footprints read
from the GitHub repo. The footprints saved to this path are combined
with the read-only part of the GitHub repository to create the footprint
library. If this option is missing, then the GitHub library is
read-only. If the option is present for a GitHub library, then any
writes to this hybrid library will go to the local `*.pretty` directory.
:::

::: paragraph
The github.com resident portion of this hybrid COW library is always
read-only, meaning you cannot delete anything or modify any footprint in
the specified GitHub repository directly. The aggregate library type
remains \"Github\" in all further discussions, but it consists of both
the local read/write portion and the remote read-only portion.
:::

::: paragraph
The table below shows a footprint library table entry with the COW
option given. Note the use of the environment variable `${HOME}` as an
example only. The github.pretty directory is located in
`${HOME}/pretty/path`. Anytime you use the option
`allow_pretty_writing_to_this_dir`, you will need to create that
directory manually in advance and it must end with the extension
`.pretty`.
:::

+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------+-------------+
| Nickname    | Library Path                                                                                              | Plugin Type | Options                                                         | Description |
+=============+===========================================================================================================+=============+=================================================================+=============+
| github      | [https://github.com/liftoff-sr/pretty_footprints](https://github.com/liftoff-sr/pretty_footprints){.bare} | Github      | `allow_pretty_writing_to_this_dir=${HOME}/pretty/github.pretty` | Liftoff's   |
|             |                                                                                                           |             |                                                                 | GH          |
|             |                                                                                                           |             |                                                                 | footprints  |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------+-------------+

::: paragraph
Footprint loads will always give precedence to the local footprints
found in the path given by the option
`allow_pretty_writing_to_this_dir`. Once you have saved a footprint to
the COW library's local directory by doing a footprint save in the
Footprint Editor, no GitHub updates will be seen when loading a
footprint with the same name as one for which you've saved locally.
:::

::: paragraph
Always keep a separate local

.pretty directory for each GitHub library, never combine them by
referring to the same directory more than once. Also, do not use the
same COW (`.pretty`) directory in a footprint library table entry. This
would likely create a mess. The value of the option
`allow_pretty_writing_to_this_dir` will expand any environment variable
using the `${}` notation to create the path in the same way as the
\"Library Path\" setting.
:::
::::::::

::::: sect4

##### Using Copy-On-Write to share footprints {#_using_copy_on_write_to_share_footprints}

::: paragraph
What's the point of COW? If you periodically email your COW pretty
footprint modifications to the GitHub repository maintainer, you can
help update the GitHub copy. Simply email the individual `*.kicad_mod`
files you find in your COW directories to the maintainer of the GitHub
repository. After you've received confirmation that your changes have
been committed, you can safely delete your COW file(s) and the updated
footprint from the read-only part of GitHub library will flow down. Your
goal should be to keep the COW file set as small as possible by
contributing frequently to the shared master copies at
[https://github.com](https://github.com){.bare}.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | You can also contribute to        |
| Tip                               | library developement using local  |
| :::                               | Git clones of the relevant        |
|                                   | libraries using the *KiCad*       |
|                                   | plugin and submitting pull        |
|                                   | requests to the library           |
|                                   | maintainers.                      |
+-----------------------------------+-----------------------------------+
:::
:::::

::::: sect4

##### Caching Github requests {#_caching_github_requests}

::: paragraph
The Github plugin can be slow, as it must download all the libraries
from the Internet before they can be used.
:::

::: paragraph
Nginx can be used as a cache to the github server to speed up the
loading of footprints. It can be installed locally or on a network
server. There is an example configuration in KiCad sources at
`pcbnew/github/nginx.conf`. The most straightforward way to get this
working is to overwrite the default nginx.conf with this one and
`export KIGITHUB=http://my_server:54321/KiCad`, where `my_server` is the
IP or domain name of the machine running nginx.
:::
:::::
::::::::::::::::::::::::::

:::::::::::: sect3

#### Usage Patterns {#_usage_patterns}

::: paragraph
Footprint libraries can be defined either globally or specifically to
the currently loaded project. Footprint libraries defined in the user's
global table are always available and are stored in the `fp-lib-table`
file in the user's home folder. Global footprint libraries can always be
accessed even when there is no project net list file opened. The project
specific footprint table is active only for the currently open net list
file. The project specific footprint library table is saved in the file
`fp-lib-table` in the path of the currently open board file. You are
free to define libraries in either table.
:::

::: paragraph
There are advantages and disadvantages to each method:
:::

::: ulist

- You can define all of your libraries in the global table which means
  they will always be available when you need them.

  ::: ulist

  - The disadvantage of this is that you may have to search through a
    lot of libraries to find the footprint you are looking for.
  :::

- You can define all your libraries on a project specific basis.

  ::: ulist

  - The advantage of this is that you only need to define the libraries
    you actually need for the project which cuts down on searching.

  - The disadvantage is that you always have to remember to add each
    footprint library that you need for every project.
  :::

- You can also define footprint libraries both globally and project
  specifically.
:::

::: paragraph
One usage pattern would be to define your most commonly used libraries
globally and the library only required for the project in the project
specific library table. There is no restriction on how you define your
libraries.
:::

::::::: sect4

##### Modifying footprints in a PCB project {#_modifying_footprints_in_a_pcb_project}

::: paragraph
When a footprint is added to a PCB, the entire footprint is copied into
the PCB file (*.kicad_pcb*). This means changes to the footprint in the
library do not automatically affect the PCB.
:::

::: paragraph
This also means that you can individually edit footprints on the PCB
without affecting other instances of the same footprint (either on the
same PCB or on other PCBs).
:::

::: paragraph
However, if you modify the library footprint, the next time you place an
instance, it will not match existing footprints of the same name.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | A common practice is to copy all  |
| Tip                               | the footprints you use to a       |
| :::                               | separate version-controlled       |
|                                   | location, so that this project is |
|                                   | not unexpectedly affected by      |
|                                   | changes to system or user         |
|                                   | libraries. Also, it ensures all   |
|                                   | the footprint resources used for  |
|                                   | the PCB can be easily distributed |
|                                   | with the PCB file.                |
+-----------------------------------+-----------------------------------+
:::
:::::::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## General operations {#_general_operations}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::: sect2

### Toolbars and commands {#_toolbars_and_commands}

::: paragraph
In Pcbnew it is possible to execute commands using various means:
:::

::: ulist

- Text-based menu at the top of the main window.

- Top toolbar menu.

- Right toolbar menu.

- Left toolbar menu.

- Mouse buttons (menu options). Specifically:

  ::: ulist

  - The right mouse button reveals a pop-up menu the content of which
    depends on the element under the mouse arrow.
  :::

- Keyboard (Function keys `F1`, `F2`, `F3`, `F4`, `Shift`, `Delete`,
  `+`, `-`, `Page Up`, `Page Down` and `Space bar`). The `Escape` key
  generally cancels an operation in progress.
:::

::: paragraph
The screenshot below illustrates some of the possible accesses to these
operations:
:::

:::: imageblock
::: content
![Right click legacy menu](images/Right-click_legacy_menu.png)
:::
::::
::::::::

::::::::::::: sect2

### Mouse commands {#_mouse_commands}

:::: sect3

#### Basic commands {#_basic_commands}

::: ulist

- Left button

  ::: ulist

  - Single-click displays the characteristics of the footprint or text
    under the cursor in the lower status bar.

  - Double-click displays the editor (if the element is editable) of the
    element under the cursor.
  :::

- Centre button/wheel

  ::: ulist

  - Rapid zoom and some commands in layer manager.

  - Hold down the centre button and draw a rectangle to zoom to the
    described area. Rotation of the mouse wheel will allow you to zoom
    in and zoom out.
  :::

- Right button

  ::: ulist

  - Displays a pop-up menu
  :::
:::
::::

:::::::::: sect3

#### Operations on blocks {#_operations_on_blocks}

::: paragraph
Operations to move, invert (mirror), copy, rotate and delete a block are
all available via the pop-up menu. In addition, the view can zoom to the
area described by the block.
:::

::: paragraph
The framework of the block is traced by moving the mouse while holding
down the left mouse button. The operation is executed when the button is
released.
:::

::: paragraph
By holding down one of the hotkeys `Shift` or `Ctrl`, or both keys
`Shift` and `Ctrl` together, while the block is drawn the operation
invert, rotate or delete is automatically selected as shown in the table
below:
:::

+-----------------------------------+-----------------------------------+
| Action                            | Effect                            |
+===================================+===================================+
| Left mouse button held down       | Trace framework to move block     |
+-----------------------------------+-----------------------------------+
| `Shift` + Left mouse button held  | Trace framework for invert block  |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Ctrl` + Left mouse button held   | Trace framework for rotating      |
| down                              | block 90°                         |
+-----------------------------------+-----------------------------------+
| `Shift` + `Ctrl` + Left mouse     | Trace framework to delete the     |
| button held down                  | block                             |
+-----------------------------------+-----------------------------------+
| Centre mouse button held down     | Trace framework to zoom to block  |
+-----------------------------------+-----------------------------------+

::: paragraph
When moving a block:
:::

::: ulist

- Move block to new position and operate left mouse button to place the
  elements.

- To cancel the operation use the right mouse button and select Cancel
  Block from the menu (or press the `Esc` key).
:::

::: paragraph
Alternatively if no key is pressed when drawing the block use the right
mouse button to display the pop-up menu and select the required
operation.
:::

::: paragraph
For each block operation a selection window enables the action to be
limited to only some elements.
:::
::::::::::
:::::::::::::

::::: sect2

### Selection of grid size {#_selection_of_grid_size}

::: paragraph
During element layout the cursor moves on a grid. The grid can be turned
on or off using the icon on the left toolbar.
:::

::: paragraph
Any of the pre-defined grid sizes, or a User Defined grid, can be chosen
using the pop-up window, or the drop-down selector on the toolbar at the
top of the screen. The size of the User Defined grid is set using the
menu bar option Dimensions → User Grid Size.
:::
:::::

::::: sect2

### Adjustment of the zoom level {#_adjustment_of_the_zoom_level}

::: paragraph
The zoom level can be changed using any of the following methods:
:::

::: ulist

- Open the pop-up window (using the right mouse button) and then select
  the desired zoom.

- Use the following function keys:

  ::: ulist

  - `F1`: Enlarge (zoom in)

  - `F2`: Reduce (zoom out)

  - `F3`: Redraw the display

  - `F4`: Centre view at the current cursor position
  :::

- Rotate the mouse wheel.

- Hold down the middle mouse button and draw a rectangle to zoom to the
  described area.
:::
:::::

:::::::::: sect2

### Displaying cursor coordinates {#_displaying_cursor_coordinates}

::: paragraph
The cursor coordinates are displayed in inches or millimetres as
selected using the \'In\' or \'mm\' icons on the left hand side toolbar.
:::

::: paragraph
Whichever unit is selected Pcbnew always works to a precision of
1/10,000 of inch.
:::

::: paragraph
The status bar at the bottom of the screen gives:
:::

::: ulist

- The current zoom setting.

- The absolute position of the cursor.

- The relative position of the cursor. Note the relative coordinates
  (x,y) can be set to (0,0) at any position by pressing the space bar.
  The cursor position is then displayed relative to this new datum.
:::

::: paragraph
In addition the relative position of the cursor can be displayed using
its polar co-ordinates (ray + angle). This can be turned on and off
using the icon in the left hand side toolbar.
:::

:::: imageblock
::: content
![Pcbnew coordinate status
display](images/Pcbnew_coordinate_status_display.png)
:::
::::
::::::::::

::::: sect2

### Keyboard commands - hotkeys {#_keyboard_commands_hotkeys}

::: paragraph
Many commands are accessible directly with the keyboard. Selection can
be either upper or lower case. Most hot keys are shown in menus. Some
hot keys that do not appear are:
:::

::: ulist

- `Delete`: deletes a footprint or a track. (*Available only if the
  Footprint mode or the Track mode is active*)

- `V`: if the track tool is active switches working layer or place via,
  if a track is in progress.

- `+` and `-`: select next or previous layer.

- `?`: display the list of all hot keys.

- `Space`: reset relative coordinates.
:::
:::::

:::::::::: sect2

### Operation on blocks {#_operation_on_blocks}

::: paragraph
Operations to move, invert (mirror), copy, rotate and delete a block are
all available from the pop-up menu. In addition, the view can zoom to
that described by the block.
:::

::: paragraph
The framework of the block is traced by moving the mouse while holding
down the left mouse button. The operation is executed when the button is
released.
:::

::: paragraph
By holding down one of the keys `Shift` or `Ctrl`, both `Shift` and
`Ctrl` together, or `Alt`, while the block is drawn the operation
invert, rotate, delete or copy is automatically selected as shown in the
table below:
:::

+-----------------------------------+-----------------------------------+
| Action                            | Effect                            |
+===================================+===================================+
| Left mouse button held down       | Move block                        |
+-----------------------------------+-----------------------------------+
| `Shift` + Left mouse button held  | Invert (mirror) block             |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Ctrl` + Left mouse button held   | Rotate block 90°                  |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Shift` + `Ctrl` + Left mouse     | Delete the block                  |
| button held down                  |                                   |
+-----------------------------------+-----------------------------------+
| `Alt` + Left mouse button held    | Copy the block                    |
| down                              |                                   |
+-----------------------------------+-----------------------------------+

::: paragraph
When a block command is made, a dialog window is displayed, and items
involved in this command can be chosen.
:::

::: paragraph
Any of the commands above can be cancelled via the same pop-up menu or
by pressing the Escape key (`Esc`).
:::

:::: imageblock
::: content
![Pcbnew legacy block selection
dialog](images/Pcbnew_legacy_block_selection_dialog.png)
:::
::::
::::::::::

::::::: sect2

### Units used in dialogs {#_units_used_in_dialogs}

::: paragraph
Units used to display dimensions values are inch and mm. The desired
unit can be selected by pressing the icon located in left toolbar:
[![unit inch](images/icons/unit_inch.png)]{.image} [![unit
mm](images/icons/unit_mm.png)]{.image} However one can enter the unit
used to define a value, when entering a new value.
:::

::: paragraph
Accepted units are:
:::

+-----------------------------------+-----------------------------------+
| 1 **in**                          | 1 inch                            |
+-----------------------------------+-----------------------------------+
| 1 **\"**                          | 1 inch                            |
+-----------------------------------+-----------------------------------+
| 25 **th**                         | 25 thou                           |
+-----------------------------------+-----------------------------------+
| 25 **mi**                         | 25 mils, same as thou             |
+-----------------------------------+-----------------------------------+
| 6 **mm**                          | 6 mm                              |
+-----------------------------------+-----------------------------------+

::: paragraph
The rules are:
:::

::: ulist

- Spaces between the number and the unit are accepted.

- Only the first two letters are significant.

- In countries using an alternative decimal separator than the period,
  the period (`.`) can be used as well. Therefore `1,5` and `1.5` are
  the same in French.
:::
:::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Top menu bar {#_top_menu_bar}

::: paragraph
The top menu bar provides access to the files (loading and saving),
configuration options, printing, plotting and the help files.
:::

:::: imageblock
::: content
![Pcbnew top menu bar](images/Pcbnew_top_menu_bar.png)
:::
::::

:::::: sect3

#### The File menu {#_the_file_menu}

:::: imageblock
::: content
![Pcbnew file menu](images/Pcbnew_file_menu.png)
:::
::::

::: paragraph
The File menu allows the loading and saving of printed circuits files,
as well as printing and plotting the circuit board. It enables the
export (with the format GenCAD 1.4) of the circuit for use with
automatic testers.
:::
::::::

:::::: sect3

#### Edit menu {#_edit_menu}

::: paragraph
Allows some global edit actions:
:::

:::: imageblock
::: content
![Pcbnew edit menu](images/Pcbnew_edit_menu.png)
:::
::::
::::::

:::::::::::: sect3

#### View menu {#_view_menu}

::: paragraph
Allows:
:::

::: ulist

- Hide/Show the Layers manager (colors selection for displaying layers
  and other elements. Also enables the display of elements to be turned
  on and off).

- Hide/Show the Microwave toolbar.

- Display Library browser and 3D viewer.

- Zoom functions

- Setting grid and units

- Select Drawing mode and Contrast mode
:::

:::: imageblock
::: content
![Pcbnew view menu](images/Pcbnew_view_menu.png)
:::
::::

::: paragraph
Zoom functions and 3D board display.
:::

:::::: sect4

##### 3D Viewer {#_3d_viewer}

::: paragraph
Opens the 3D Viewer. Here is a sample:
:::

:::: imageblock
::: content
![Sample 3D board](images/Sample_3D_board.png)
:::
::::
::::::
::::::::::::

::::::::: sect3

#### Setup menu {#_setup_menu}

::: paragraph
Provides access to 2 dialogs:
:::

::: ulist

- Setting Layers (number, enabled and layers names)

- Setting Design Rules (tracks and vias sizes, clearances).
:::

::: paragraph
An important menu. Allows adjustment of:
:::

::: ulist

- Size of texts and the line width for drawings.

- Dimensions and characteristic of pads.

- Setting the global values for solder mask and solder paste layers
:::

:::: imageblock
::: content
![Pcbnew setup menu](images/Pcbnew_setup_menu.png)
:::
::::
:::::::::

:::::: sect3

#### Place menu {#_place_menu}

::: paragraph
Same function as the right-hand toolbar.
:::

:::: imageblock
::: content
![Pcbnew place menu](images/Pcbnew_place_menu.png)
:::
::::
::::::

:::::: sect3

#### Route menu {#_route_menu}

::: paragraph
Routing function.
:::

:::: imageblock
::: content
![Pcbnew route menu](images/Pcbnew_route_menu.png)
:::
::::
::::::

::::::: sect3

#### Inspect menu {#_inspect_menu}

::: paragraph
Allows:
:::

::: ulist

- List nets

- Measure function

- Design Rules Checker
:::

:::: imageblock
::: content
![Pcbnew inspect menu](images/Pcbnew_inspect_menu.png)
:::
::::
:::::::

::::::: sect3

#### Tools menu {#_tools_menu}

::: paragraph
Allows:
:::

::: ulist

- Display load netlist dialog

- Update PCB from schematic

- Update Footprints from library

- FreeRoute collaboration

- Python scripting console

- External plugins
:::

:::: imageblock
::: content
![Pcbnew tools menu](images/Pcbnew_tools_menu.png)
:::
::::
:::::::

::::::: sect3

#### The Preferences menu {#_the_preferences_menu}

:::: imageblock
::: content
![Pcbnew preferences menu](images/Pcbnew_preferences_menu.png)
:::
::::

::: paragraph
Allows:
:::

::: ulist

- Selection of the footprint libraries.

- Management of general options (units, etc.).

- The management of other display options.

- Creation, editing (and re-read) of the hot keys file.
:::
:::::::

:::: sect3

#### The Help menu {#_the_help_menu}

::: paragraph
Provides access to the user manuals and to the version information menu
(Pcbnew About).
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::: sect2

### Using icons on the top toolbar {#_using_icons_on_the_top_toolbar}

::: paragraph
This toolbar gives access to the principal functions of Pcbnew.
:::

:::: imageblock
::: content
![Pcbnew top toolbar](images/Pcbnew_top_toolbar.png)
:::
::::

+---------------------------------------------------------------------+--------------------------------------------------+
| [![new board](images/icons/new_board.png)]{.image}                  | Creation of a new printed circuit.               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![open brd file](images/icons/open_brd_file.png)]{.image}          | Opening of an old printed circuit.               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![save](images/icons/save.png)]{.image}                            | Save printed circuit.                            |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![sheetset](images/icons/sheetset.png)]{.image}                    | Selection of the page size and modification of   |
|                                                                     | the file properties.                             |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![module editor](images/icons/module_editor.png)]{.image}          | Opens Footprint Editor to edit library or pcb    |
|                                                                     | footprint.                                       |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![modview icon](images/icons/modview_icon.png)]{.image}            | Opens Footprint Viewer to display library or pcb |
|                                                                     | footprint.                                       |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![undo](images/icons/undo.png)]{.image}                            | Undo/Redo last commands (10 levels)              |
| [![redo](images/icons/redo.png)]{.image}                            |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![print button](images/icons/print_button.png)]{.image}            | Display print menu.                              |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![plot](images/icons/plot.png)]{.image}                            | Display plot menu.                               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image} [![zoom              | Zoom in and Zoom out (relative to the centre of  |
| out](images/icons/zoom_out.png)]{.image}                            | screen).                                         |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom redraw](images/icons/zoom_redraw.png)]{.image}              | Redraw the screen                                |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom fit in page](images/icons/zoom_fit_in_page.png)]{.image}    | Fit to page                                      |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![find](images/icons/find.png)]{.image}                            | Find footprint or text.                          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![netlist](images/icons/netlist.png)]{.image}                      | Netlist operations (selection, reading, testing  |
|                                                                     | and compiling).                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![drc](images/icons/drc.png)]{.image}                              | DRC (Design Rule Check): Automatic check of the  |
|                                                                     | tracks.                                          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew toolbar layer select                                      | Selection of the working layer.                  |
| dropdown](images/Pcbnew_toolbar_layer_select_dropdown.png)]{.image} |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew layer pair                                                | Selection of layer pair (for vias)               |
| indicator](images/Pcbnew_layer_pair_indicator.png)]{.image}         |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![mode module](images/icons/mode_module.png)]{.image}              | Footprint mode: when active this enables         |
|                                                                     | footprint options in the pop-up window.          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![mode track](images/icons/mode_track.png)]{.image}                | Routing mode: when active this enables routing   |
|                                                                     | options in the pop-up window                     |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![web support](images/icons/web_support.png)]{.image}              | Direct access to the router Freerouter           |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![py script](images/icons/py_script.png)]{.image}                  | Show / Hide the Python scripting console         |
+---------------------------------------------------------------------+--------------------------------------------------+

:::: sect3

#### Auxiliary toolbar {#_auxiliary_toolbar}

+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew track thickness                                      | Selection of thickness of track already in use.  |
| dropdown](images/Pcbnew_track_thickness_dropdown.png)]{.image} |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew via size                                             | Selection of a dimension of via already in use.  |
| dropdown](images/Pcbnew_via_size_dropdown.png)]{.image}        |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![auto track                                                  | Automatic track width: if enabled when creating  |
| width](images/icons/auto_track_width.png)]{.image}             | a new track, when starting on an existing track, |
|                                                                | the width of the new track is set to the width   |
|                                                                | of the existing track.                           |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew grid size                                            | Selection of the grid size.                      |
| dropdown](images/Pcbnew_grid_size_dropdown.png)]{.image}       |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew zoom factor                                          | Selection of the zoom.                           |
| dropdown](images/Pcbnew_zoom_factor_dropdown.png)]{.image}     |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+

::: {style="page-break-after: always;"}
:::
::::
::::::::

:::::: sect2

### Right-hand side toolbar {#_right_hand_side_toolbar}

::: paragraph
This toolbar gives access to the editing tool to change the PCB shown in
Pcbnew.
:::

+-----------------------------------------------------------------+-----------------------------------------------------+------------------------------------------------------------+
| [![Pcbnew right                                                 | [![cursor](images/icons/cursor.png)]{.image}        | Select the standard mouse mode.                            |
| toolbar](images/Pcbnew_right_toolbar.png){width="80%"}]{.image} |                                                     |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![net                                              | Highlight net selected by clicking on a track or pad.      |
|                                                                 | highlight](images/icons/net_highlight.png)]{.image} |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![tool                                             | Display local ratsnest (Pad or Footprint).                 |
|                                                                 | ratsnest](images/icons/tool_ratsnest.png)]{.image}  |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![module](images/icons/module.png)]{.image}        | Add a footprint from a library.                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Placement of tracks and vias.                              |
|                                                                 | tracks](images/icons/add_tracks.png)]{.image}       |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add zone](images/icons/add_zone.png)]{.image}    | Placement of zones (copper planes).                        |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add keepout                                      | Placement of keepout areas ( on copper layers ).           |
|                                                                 | area](images/icons/add_keepout_area.png)]{.image}   |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add dashed                                       | Draw Lines on technical layers (i.e. not a copper layer).  |
|                                                                 | line](images/icons/add_dashed_line.png)]{.image}    |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Draw Circles on technical layers (i.e. not a copper        |
|                                                                 | circle](images/icons/add_circle.png)]{.image}       | layer).                                                    |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add arc](images/icons/add_arc.png)]{.image}      | Draw Arcs on technical layers (i.e. not a copper layer).   |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![text](images/icons/text.png)]{.image}            | Placement of text.                                         |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Draw Dimensions on technical layers (i.e. not the copper   |
|                                                                 | dimension](images/icons/add_dimension.png)]{.image} | layer).                                                    |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add pcb                                          | Draw Alignment Marks (appearing on all layers).            |
|                                                                 | target](images/icons/add_pcb_target.png)]{.image}   |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![delete](images/icons/delete.png)]{.image}        | Delete element pointed to by the cursor                    |
|                                                                 |                                                     |                                                            |
|                                                                 |                                                     | **Note:** When Deleting, if several superimposed elements  |
|                                                                 |                                                     | are pointed to, priority is given to the smallest (in the  |
|                                                                 |                                                     | decreasing set of priorities tracks, text, footprint). The |
|                                                                 |                                                     | function \"Undelete\" of the upper toolbar allows the      |
|                                                                 |                                                     | cancellation of the last item deleted.                     |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![pcb                                              | Offset adjust for drilling and place files.                |
|                                                                 | offset](images/icons/pcb_offset.png)]{.image}       |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![grid select                                      | Grid origin. (grid offset). Useful mainly for editing and  |
|                                                                 | axis](images/icons/grid_select_axis.png)]{.image}   | placement of footprints. Can also be set in                |
|                                                                 |                                                     | Dimensions/Grid menu.                                      |
+-----------------------------------------------------------------+-----------------------------------------------------+------------------------------------------------------------+

::: ulist

- Placement of footprints, tracks, zones of copper, texts, etc.

- Net Highlighting.

- Creating notes, graphic elements, etc.

- Deleting elements.
:::

::: {style="page-break-after: always;"}
:::
::::::

:::: sect2

### Left-hand side toolbar {#_left_hand_side_toolbar}

::: paragraph
The left hand-side toolbar provides display and control options that
affect Pcbnew's interface.
:::

+----------------------------------------------------------------+---------------------------------------------------------+------------------------------------------------------------+
| [![Pcbnew left                                                 | [![drc off](images/icons/drc_off.png)]{.image}          | Turns DRC (Design Rule Checking) on/off. **Caution:** when |
| toolbar](images/Pcbnew_left_toolbar.png){width="80%"}]{.image} |                                                         | DRC is off incorrect connections can be made.              |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![grid](images/icons/grid.png)]{.image}                | Turn grid display on/off **Note:** a small grid may not be |
|                                                                |                                                         | displayed unless zoomed in far enough                      |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![polar coord](images/icons/polar_coord.png)]{.image}  | Polar display of the relative co-ordinates on the status   |
|                                                                |                                                         | bar on/off.                                                |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![unit inch](images/icons/unit_inch.png)]{.image}      | Display/entry of coordinates or dimensions in inches or    |
|                                                                | [![unit mm](images/icons/unit_mm.png)]{.image}          | millimeters.                                               |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![cursor                                               | Change cursor display shape.                               |
|                                                                | shape](images/icons/cursor_shape.png)]{.image}          |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![general                                              | Display general rats nest (incomplete connections between  |
|                                                                | ratsnest](images/icons/general_ratsnest.png)]{.image}   | footprints).                                               |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![local                                                | Display footprint rats nest dynamically as it is moved.    |
|                                                                | ratsnest](images/icons/local_ratsnest.png)]{.image}     |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![auto delete                                          | Enable/Disable automatic deletion of a track when it is    |
|                                                                | track](images/icons/auto_delete_track.png)]{.image}     | redrawn.                                                   |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone](images/icons/show_zone.png)]{.image}      | Show filled areas in zones                                 |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone                                            | Do not show filled areas in zones                          |
|                                                                | disable](images/icons/show_zone_disable.png)]{.image}   |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone outline                                    | Show only outlines of filled areas in zones                |
|                                                                | only](images/icons/show_zone_outline_only.png)]{.image} |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![pad sketch](images/icons/pad_sketch.png)]{.image}    | Display of pads in outline mode on/off.                    |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![via sketch](images/icons/via_sketch.png)]{.image}    | Display of vias in outline mode on/off.                    |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![showtrack](images/icons/showtrack.png)]{.image}      | Display of tracks in outline mode on/off.                  |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![contrast                                             | High contrast display mode on/off. In this mode the active |
|                                                                | mode](images/icons/contrast_mode.png)]{.image}          | layer is displayed normally, all the other layers are      |
|                                                                |                                                         | displayed in gray. Useful for working on multi-layer       |
|                                                                |                                                         | circuits.                                                  |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![layers                                               | Hide/Show the Layers manager                               |
|                                                                | manager](images/icons/layers_manager.png)]{.image}      |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![mw toolbar](images/icons/mw_toolbar.png)]{.image}    | Access to microwaves tools. Under development              |
+----------------------------------------------------------------+---------------------------------------------------------+------------------------------------------------------------+
::::

::::::: sect2

### Pop-up windows and fast editing {#_pop_up_windows_and_fast_editing}

::: paragraph
A right-click of the mouse opens a pop-up window. Its contents depends
on the element pointed at by the cursor.
:::

::: paragraph
This gives immediate access to:
:::

::: ulist

- Changing the display (centre display on cursor, zoom in or out or
  selecting the zoom).

- Setting the grid size.

- Additionally a right-click on an element enables editing of the most
  commonly modified element parameters.
:::

::: paragraph
The screenshots below show what the pop-up windows looks like.
:::
:::::::

:::::::::::::::::::::::::::::::::::: sect2

### Available modes {#_available_modes}

::: paragraph
There are 3 modes when using pop-up menus. In the pop-up menus, these
modes add or remove some specific commands.
:::

+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Normal mode                                      |
| module](images/icons/mode_module.png)]{.image} |                                                  |
| and [![mode                                    |                                                  |
| track](images/icons/mode_track.png)]{.image}   |                                                  |
| disabled                                       |                                                  |
+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Footprint mode                                   |
| module](images/icons/mode_module.png)]{.image} |                                                  |
| enabled                                        |                                                  |
+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Tracks mode                                      |
| track](images/icons/mode_track.png)]{.image}   |                                                  |
| enabled                                        |                                                  |
+------------------------------------------------+--------------------------------------------------+

:::::::::::: sect3

#### Normal mode {#_normal_mode}

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode](images/Pcbnew_popup_normal_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode
track](images/Pcbnew_popup_normal_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode
footprint](images/Pcbnew_popup_normal_mode_footprint.png)
:::
::::
::::::::::::

::::::::::::: sect3

#### Footprint mode {#_footprint_mode}

::: paragraph
Same cases in Footprint Mode ([![mode
module](images/icons/mode_module.png)]{.image} enabled)
:::

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode](images/Pcbnew_popup_footprint_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode
track](images/Pcbnew_popup_footprint_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode
footprint](images/Pcbnew_popup_footprint_mode_footprint.png)
:::
::::
:::::::::::::

::::::::::::: sect3

#### Tracks mode {#_tracks_mode}

::: paragraph
Same cases in Track Mode ([![mode
track](images/icons/mode_track.png)]{.image} enabled)
:::

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup track mode](images/Pcbnew_popup_track_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup track mode
track](images/Pcbnew_popup_track_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup track mode
footprint](images/Pcbnew_popup_track_mode_footprint.png)
:::
::::
:::::::::::::
::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::: sect1

## Schematic Implementation {#_schematic_implementation}

:::::::::::::::::::::::::::::::::::::: sectionbody
::::::: sect2

### Linking a schematic to a printed circuit board {#_linking_a_schematic_to_a_printed_circuit_board}

::: paragraph
Generally speaking, a schematic sheet is linked to its printed circuit
board by means of the netlist file, which is normally generated by the
schematic editor used to make the schematic. Pcbnew accepts netlist
files made with Eeschema or Orcad PCB 2. The netlist file, generated
from the schematic is usually missing the footprints that correspond to
the various components. Consequently an intermediate stage is necessary.
During this intermediate process the association of components with
footprints is performed. In KiCad, CvPcb is used to create this
association and a file named `*.cmp` is produced. CvPcb also updates the
netlist file using this information.
:::

::: paragraph
CvPcb can also output a \"stuff file\" `*.stf` which can be back
annotated into the schematic file as the F2 field for each component,
saving the task of re-assigning footprints in each schematic edit pass.
In Eeschema copying a component will also copy the footprint assignment
and set the reference designator as unassigned for later
auto-incremental annotation.
:::

::: paragraph
Pcbnew reads the modified netlist file `.net` and, if it exists, the
`.cmp` file. In the event of a footprint being changed directly in
Pcbnew the `.cmp` file is automatically updated avoiding the requirement
to run CvPcb again.
:::

::: paragraph
Refer to the figure of \"Getting Started in KiCad\" manual in the
section *KiCad Workflow* that illustrates the work-flow of KiCad and how
intermediate files are obtained and used by the different software tools
that comprise KiCad.
:::
:::::::

:::::: sect2

### Procedure for creating a printed circuit board {#_procedure_for_creating_a_printed_circuit_board}

::: paragraph
After having created your schematic in Eeschema:
:::

::: ulist

- Generate the netlist using Eeschema.

- Assign each component in your netlist file to the corresponding land
  pattern (often called footprint) used on the printed circuit using
  Cvpcb.

- Launch Pcbnew and read the modified Netlist. This will also read the
  file with the footprint selections.
:::

::: paragraph
Pcbnew will then load automatically all the necessary footprints.
Footprints can now be placed manually or automatically on the board and
tracks can be routed.
:::
::::::

:::::: sect2

### Procedure for updating a printed circuit board {#_procedure_for_updating_a_printed_circuit_board}

::: paragraph
If the schematic is modified (after a printed circuit board has been
generated), the following steps must be repeated:
:::

::: ulist

- Generate a new netlist file using Eeschema.

- If the changes to the schematic involve new components, the
  corresponding footprints must be assigned using Cvpcb.

- Launch Pcbnew and re-read the modified netlist (this will also re-read
  the file with the footprint selections).
:::

::: paragraph
Pcbnew will then load automatically any new footprints, add the new
connections and remove redundant connections. This process is called
forward annotation and is a very common procedure when a PCB is made and
updated.
:::
::::::

:::::::::::::::::::::::: sect2

### Reading netlist file - loading footprints {#_reading_netlist_file_loading_footprints}

:::::: sect3

#### Dialog box {#_dialog_box}

::: paragraph
Accessible from the icon [![netlist](images/icons/netlist.png)]{.image}
:::

:::: imageblock
::: content
![Pcbnew netlist dialog](images/en/Pcbnew_netlist_dialog.png)
:::
::::
::::::

::: sect3

#### Available options {#_available_options}

+-----------------------------------+-----------------------------------+
| Footprint Selection               | Components and corresponding      |
|                                   | footprints on board link: normal  |
|                                   | link is Reference (normal option  |
|                                   | Timestamp can be used after       |
|                                   | reannotation of schematic, if the |
|                                   | previous annotation was destroyed |
|                                   | (special option)                  |
+-----------------------------------+-----------------------------------+
| Exchange Footprint:               | If a footprint has changed in the |
|                                   | netlist: keep old footprint or    |
|                                   | change to the new one.            |
+-----------------------------------+-----------------------------------+
| Unconnected Tracks                | Keep all existing tracks, or      |
|                                   | delete erroneous tracks           |
+-----------------------------------+-----------------------------------+
| Extra Footprints                  | Remove footprints which are on    |
|                                   | board but not in the netlist.     |
|                                   | Footprint with attribute          |
|                                   | \"Locked\" will not be removed.   |
+-----------------------------------+-----------------------------------+
| Single Pad Nets                   | Remove single pad nets.           |
+-----------------------------------+-----------------------------------+
:::

:::::::::::::::::: sect3

#### Loading new footprints {#_loading_new_footprints}

::: paragraph
With the GAL backend when new footprints are found in the netlist file,
they will be loaded, spread out, and be ready for you to place as a
group where you would like.
:::

:::: imageblock
::: content
![Pcbnew import spread
footprints](images/Pcbnew_import_spread_footprints.png){height="300"}
:::
::::

::: paragraph
With the legacy backend when new footprints are found in the netlist
file, they will be automatically loaded and placed at coordinate (0,0).
:::

:::: imageblock
::: content
![Pcbnew stacked footprints](images/Pcbnew_stacked_footprints.png)
:::
::::

::: paragraph
New footprints can be moved and arranged one by one. A better way is to
automatically move (unstack) them:
:::

::: paragraph
Activate footprint mode ([![mode
module](images/icons/mode_module.png)]{.image})
:::

::: paragraph
Move the mouse cursor to a suitable (free of component) area, and click
on the right button:
:::

:::: imageblock
::: content
![Pcbnew move all modules](images/Pcbnew_move_all_modules.png)
:::
::::

::: ulist

- Automatically Place New Footprints, if there is already a board with
  existing footprints.

- Automatically Place All Footprints, for the first time (when creating
  a board).
:::

::: paragraph
The following screenshot shows the results.
:::

:::: imageblock
::: content
![Pcbnew unstacked footprints](images/Pcbnew_unstacked_footprints.png)
:::
::::
::::::::::::::::::
::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Layers {#_layers}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2

### Introduction {#_introduction}

::: paragraph
Pcbnew can work with 50 different layers:
:::

::: ulist

- Between 1 and 32 copper layers for routing tracks.

- 14 fixed-purpose technical layers:

  ::: ulist

  - 12 paired layers (Front/Back): **Adhesive**, **Solder Paste**,
    **Silk Screen**, **Solder Mask**, **Courtyard**, **Fabrication**

  - 2 standalone layers: **Edge Cuts**, **Margin**
  :::

- 4 auxiliary layers that you can use any way you want: **Comments**,
  **E.C.O. 1**, **E.C.O. 2**, **Drawings**
:::
:::::

::::::: sect2

### Setting up layers {#_setting_up_layers}

::: paragraph
To open the **Layers Setup** from the menu bar, select **Setup** →
**Layers Setup**.
:::

::: paragraph
The board thickness, number of copper layers, their names, and their
function are configured there. Unused technical layers can be disabled.
:::

:::: imageblock
::: content
![Pcbnew layer setup dialog](images/Pcbnew_layer_setup_dialog.png)
:::
::::
:::::::

::::::::::::::::: sect2

### Layer Description {#_layer_description}

::::::: sect3

#### Copper Layers {#_copper_layers}

::: paragraph
Copper layers are the usual working layers used to place and re-arrange
tracks. Layer numbers start from 0 (the first copper layer, on Front)
and end at 31 (Back). Since components cannot be placed in **inner
layers** (number 1 to 30), only layers number 0 and 31 are **component
layer**.
:::

::: paragraph
The name of any copper layer is editable. Copper layers have a function
attribute that is useful when using the external router *Freerouter*.
Example of default layer names are **F.Cu** and **In0** for layer number
0.
:::

:::: imageblock
::: content
![Pcbnew layer setup dialog layer
properties](images/Pcbnew_layer_setup_dialog_layer_properties.png)
:::
::::
:::::::

:::::: sect3

#### Paired Technical Layers {#_paired_technical_layers}

::: paragraph
12 technical layers come in pairs: one for the front, one for the back.
You can recognize them with the \"F.\" or \"B.\" prefix in their names.
The elements making up a footprint (pad, drawing, text) of one of these
layers are automatically mirrored and moved to the complementary layer
when the footprint is flipped.
:::

::: paragraph
The paired technical layers are:
:::

::: dlist

**Adhesive** (F.Adhes and B.Adhes)

:   These are used in the application of adhesive to stick SMD
    components to the circuit board, generally before wave soldering.

**Solder Paste** (F.Paste and B.Paste)

:   Used to produce a mask to allow solder paste to be placed on the
    pads of surface mount components, generally before reflow soldering.
    Usually only surface mount pads occupy these layers.

**Silk Screen** (F.SilkS and B.SilkS)

:   They are the layers where the drawings of the components appear.
    That's where you draw things like component polarity, first pin
    indicator, reference for mounting, ...​

**Solder Mask** (F.Mask and B.Mask)

:   These define the solder masks. All pads should appear on one of
    these layers (SMT) or both (for through hole) to prevent the varnish
    from covering the pads.

**Courtyard** (F.CrtYd and B.CrtYd)

:   Used to show how much space a component physically takes on the PCB.

**Fabrication** (F.Fab and B.Fab)

:   The fabrication layers are primarily used for documentation purposes
    to convey information to, for example, the PCB maker or the assembly
    house.
:::
::::::

:::: sect3

#### Independant Technical Layers {#_independant_technical_layers}

::: dlist

**Edge.Cuts**

:   This layer is reserved for the drawing of circuit board outline. Any
    element (graphic, texts...​) placed on this layer appears on all the
    other layers. Use this layer only to draw board outlines.

**Margin**

:   Board's edge setback outline (?).
:::
::::

::::: sect3

#### Layers for general use {#_layers_for_general_use}

::: paragraph
These layers are for any use. They can be used for text such as
instructions for assembly or wiring, or construction drawings, to be
used to create a file for assembly or machining. Their names are:
:::

::: ulist

- Comments

- E.C.O. 1

- E.C.O. 2

- Drawings
:::
:::::
:::::::::::::::::

::::::::::::::::::: sect2

### Selection of the active layer {#_selection_of_the_active_layer}

::: paragraph
The selection of the active working layer can be done in several ways:
:::

::: ulist

- Using the right toolbar (Layer manager).

- Using the upper toolbar.

- With the pop-up window (activated with the right mouse button).

- Using the + and - keys (works on copper layers only).

- By hot keys.
:::

::::: sect3

#### Selection using the layer manager {#_selection_using_the_layer_manager}

:::: imageblock
::: content
![Pcbnew layer manager pane](images/Pcbnew_layer_manager_pane.png)
:::
::::
:::::

::::::: sect3

#### Selection using the upper toolbar {#_selection_using_the_upper_toolbar}

:::: imageblock
::: content
![Pcbnew layer selection
dropdown](images/Pcbnew_layer_selection_dropdown.png)
:::
::::

::: paragraph
This directly selects the working layer.
:::

::: paragraph
Hot keys to select the working layer are displayed.
:::
:::::::

:::::::: sect3

#### Selection using the pop-up window {#_selection_using_the_pop_up_window}

:::: imageblock
::: content
![Pcbnew layer selection popup](images/Pcbnew_layer_selection_popup.png)
:::
::::

::: paragraph
The Pop-up window opens a menu window which provides a choice for the
working layer.
:::

:::: imageblock
::: content
![Pcbnew layer selection
dialog](images/Pcbnew_layer_selection_dialog.png)
:::
::::
::::::::
:::::::::::::::::::

::::::::::: sect2

### Selection of the Layers for Vias {#_selection_of_the_layers_for_vias}

::: paragraph
If the **Add Tracks and Vias** icon is selected on the right hand
toolbar, the Pop-Up window provides the option to change the layer pair
used for vias:
:::

:::: imageblock
::: content
![Pcbnew via layer pair popup](images/Pcbnew_via_layer_pair_popup.png)
:::
::::

::: paragraph
This selection opens a menu window which provides choice of the layers
used for vias.
:::

:::: imageblock
::: content
![Pcbnew via layer pair dialog](images/Pcbnew_via_layer_pair_dialog.png)
:::
::::

::: paragraph
When a via is placed the working (active) layer is automatically
switched to the alternate layer of the layer pair used for the vias
(unless \'Shift\' is held when adding the via).
:::

::: paragraph
One can also switch to another active layer by hot keys, and if a track
is in progress, a via will be inserted.
:::
:::::::::::

::::::::::::::::::::::: sect2

### Using the high-contrast mode {#_using_the_high_contrast_mode}

::: paragraph
This mode is entered when the tool (in the left toolbar) is activated:
[![contrast mode](images/icons/contrast_mode.png)]{.image}
:::

::: paragraph
When using this mode, the active layer is displayed like in the normal
mode, but all others layers are displayed in gray color.
:::

::: paragraph
There are two useful cases:
:::

:::::::::: sect3

#### Copper layers in high-contrast mode {#_copper_layers_in_high_contrast_mode}

::: paragraph
When a board uses more than four layers, this option allows the active
copper layer to be seen more easily:
:::

::: paragraph
**Normal mode** (back side copper layer active):
:::

:::: imageblock
::: content
![Pcbnew copper layers contrast
normal](images/Pcbnew_copper_layers_contrast_normal.png)
:::
::::

::: paragraph
**High-contrast mode** (back side copper layer active):
:::

:::: imageblock
::: content
![Pcbnew copper layers contrast
high](images/Pcbnew_copper_layers_contrast_high.png)
:::
::::
::::::::::

::::::::::: sect3

#### Technical layers {#_technical_layers}

::: paragraph
The other case is when it is necessary to examine solder paste layers
and solder mask layers which are usually not displayed.
:::

::: paragraph
Masks on pads are displayed if this mode is active.
:::

::: paragraph
**Normal mode** (front side solder mask layer active):
:::

:::: imageblock
::: content
![Pcbnew technical layers contrast
normal](images/Pcbnew_technical_layers_contrast_normal.png)
:::
::::

::: paragraph
**High-contrast mode** (front side solder mask layer active):
:::

:::: imageblock
::: content
![Pcbnew technical layers contrast
high](images/Pcbnew_technical_layers_contrast_high.png)
:::
::::
:::::::::::
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Create and modify a board {#_create_and_modify_a_board}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::::::::::::::::::::::::::::::::::: sect2

### Creating a board {#_creating_a_board}

::::::::: sect3

#### Drawing the board outline {#_drawing_the_board_outline}

::: paragraph
It is usually a good idea to define the outline of the board first. The
outline is drawn as a sequence of line segments. Select \'Edge.Cuts\' as
the active layer and use the \'Add graphic line or polygon\' tool to
trace the edge, clicking at the position of each vertex and
double-clicking to finish the outline. Boards usually have very precise
dimensions, so it may be necessary to use the displayed cursor
coordinates while tracing the outline. Remember that the relative
coordinates can be zeroed at any time using the space bar, and that the
display units can also be toggled using \'Ctrl-U\'. Relative coordinates
enable very precise dimensions to be drawn. It is possible to draw a
circular (or arc) outline:
:::

::: {.olist .arabic}

1.  Select the \'Add graphic circle\' or \'Add graphic arc\' tool

2.  Click to fix the circle centre

3.  Adjust the radius by moving the mouse

4.  Finish by clicking again.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | The width of the outline can be   |
| Note                              | adjusted in the Parameters menu   |
| :::                               | (recommended width = 150 in 1/10  |
|                                   | mils) or via the Options, but     |
|                                   | this will not be visible unless   |
|                                   | the graphics are displayed in     |
|                                   | other than outline mode.          |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
The resulting outline might look something like this:
:::

:::: imageblock
::: content
![Pcbnew simple board outline](images/Pcbnew_simple_board_outline.png)
:::
::::
:::::::::

::::::::::::::::::::::::: sect3

#### Using a DXF drawing for the board outline {#_using_a_dxf_drawing_for_the_board_outline}

::: paragraph
As an alternative to drawing the board outline in Pcbnew directly, an
outline can also be imported from a DXF drawing.
:::

::: paragraph
Using this feature allows for much more complex board shapes than is
possible with the Pcbnew drawing capabilities.
:::

::: paragraph
For example a mechanical CAD package can be used to define a board shape
that fits a particular enclosure.
:::

::::::::::: sect4

##### Preparing the DXF drawing for import into KiCad {#_preparing_the_dxf_drawing_for_import_into_kicad}

::: paragraph
The **DXF** import capability in KiCad does not support DXF features
like **POLYLINES** and **ELLIPSIS** and DXF files that use these
features require a few conversion steps to prepare them for import.
:::

::: paragraph
A software package like LibreCAD can be used for this conversion.
:::

::: paragraph
As a first step, any **POLYLINES** need to be split (Exploded) into
their original simpler shapes. In LibreCAD use the following steps:
:::

::: {.olist .arabic}

1.  Open a copy of the DXF file.

2.  Select the board shape (selected shapes are shown with dashed
    lines).

3.  In the **Modify** menu, select **Explode**.

4.  Press ENTER.
:::

::: paragraph
As a next step, complex curves like **ELLIPSIS** need to be broken up in
small line segments that \'approximate\' the required shape. This
happens automatically when the DXF file is exported or saved in the
older **DXF R12** file format (as the R12 format does not support
complex curve shapes, CAD applications convert these shapes to line
segments. Some CAD applications allow configuration of the number or the
length of the line segments used). In LibreCAD the segment length it
generally small enough for use in board shapes.
:::

::: paragraph
In LibreCAD, use the following steps to export to the **DXF R12** file
format:
:::

::: {.olist .arabic}

1.  In the **File** menu, use **Save As...​**

2.  In the **Save Drawing As** dialog, there is a **Save as type:**
    selection near the bottom of the dialog. Select the option **Drawing
    Exchange DXF R12**.

3.  Optionally enter a file name in the **File name:** field.

4.  Click **Save**
:::

::: paragraph
Your DXF file is now ready for import into KiCad.
:::
:::::::::::

:::::::: sect4

##### Importing the DXF file into KiCad {#_importing_the_dxf_file_into_kicad}

::: paragraph
The following steps describe the import of the prepared DXF file as a
board shape into KiCad. Note that the import bahaviour is slightly
different depending on which \'canvas\' is used.
:::

::: paragraph
Using the \"default\" canvas mode:
:::

::: {.olist .arabic}

1.  In the **File** menu, select **Import** and then the **DXF File**
    option.

2.  In the **Import DXF File** dialog use \'Browse\' to select the
    prepared DXF file to be imported.

3.  In the \'Place DXF origin (0,0) point:\' option, select the
    placement of DXF origin relative to the board coordinates (the KiCad
    board has (0,0) in the top left corner). For the \'User defined
    position\' enter the coordinates in the \'X Position\' and \'Y
    Position\' fields.

4.  In the \'Layer\' selection, select the board layer for the import.
    **Edge.Cuts** is needed for the board outline.

5.  Click \'OK\'.
:::

::: paragraph
Using the \"OpenGL\" or \"Cairo\" canvas modes:
:::

::: {.olist .arabic}

1.  In the **File** menu, select **Import** and then the **DXF File**
    option.

2.  In the **Import DXF File** dialog use \'Browse\' to select the
    prepared DXF file to be imported.

3.  The \'Place DXF origin (0,0) point:\' option setting is ignored in
    this mode.

4.  In the \'Layer\' selection, select the board layer for the import.
    **Edge.Cuts** is needed for the board outline.

5.  Click \'OK\'.

6.  The shape is now attached to your cursor and it can be moved around
    the board area.

7.  Click to \'drop\' the shape on the board.
:::
::::::::

:::::: sect4

##### Example imported DXF shape {#_example_imported_dxf_shape}

::: paragraph
Here is an example of a DXF import with a board that had several
elliptical segments approximated by a number of short line segments:
:::

:::: imageblock
::: content
![Pcbnew board outline imported from a
DXF](images/Pcbnew_board_outline_imported_from_a_DXF.png)
:::
::::
::::::
:::::::::::::::::::::::::

::::::::::::: sect3

#### Reading the netlist generated from the schematic {#_reading_the_netlist_generated_from_the_schematic}

::: paragraph
Activate the [![netlist](images/icons/netlist.png)]{.image} icon to
display the netlist dialog window:
:::

:::: imageblock
::: content
![Pcbnew netlist dialog](images/en/Pcbnew_netlist_dialog.png)
:::
::::

::: paragraph
If the name (path) of the netlist in the window title is incorrect, use
the \'Select\' button to browse to the desired netlist. Then \'Read\'
the netlist. Any footprints not already loaded will appear, superimposed
one upon another (we shall see below how to move them automatically).
:::

:::: imageblock
::: content
![Pcbnew board outline with
dogpile](images/Pcbnew_board_outline_with_dogpile.png)
:::
::::

::: paragraph
If none of the footprints have been placed, all of the footprints will
appear on the board in the same place, making them difficult to
recognize. It is possible to arrange them automatically (using the
command \'Global Spread and Place\' accessed via the right mouse
button). Here is the result of such automatic arrangement:
:::

:::: imageblock
::: content
![Pcbnew board outline with globally placed
modules](images/Pcbnew_board_outline_with_globally_placed_modules.png)
:::
::::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | If a board is modified by         |
| Note                              | replacing an existing footprint   |
| :::                               | with a new one (for example       |
|                                   | changing a 1/8 W resistor to 1/2  |
|                                   | W) in CvPcb, it will be necessary |
|                                   | to delete the existing component  |
|                                   | before Pcbnew will load the       |
|                                   | replacement footprint. However,   |
|                                   | if a footprint is to be replaced  |
|                                   | by an existing footprint, this is |
|                                   | easier to do using the footprint  |
|                                   | dialog accessed by clicking the   |
|                                   | right mouse button over the       |
|                                   | footprint in question.            |
+-----------------------------------+-----------------------------------+
:::
:::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::: sect2

### Correcting a board {#_correcting_a_board}

::: paragraph
It is very often necessary to correct a board following a corresponding
change in the schematic.
:::

:::: sect3

#### Steps to follow {#_steps_to_follow}

::: {.olist .arabic}

1.  Create a new netlist from the modified schematic.

2.  If new components have been added, link these to their corresponding
    footprint in CvPcb.

3.  Read the new netlist in Pcbnew.
:::
::::

::::::: sect3

#### Deleting incorrect tracks {#_deleting_incorrect_tracks}

::: paragraph
Pcbnew is able to automatically delete tracks that have become incorrect
as a result of modifications. To do this, check the \'Delete\' option in
the \'Unconnected Tracks\' box of the netlist dialog:
:::

:::: imageblock
::: content
![Pcbnew bad tracks deletion
option](images/Pcbnew_bad_tracks_deletion_option.png)
:::
::::

::: paragraph
However, it is often quicker to modify such tracks by hand (the DRC
function allows their identification).
:::
:::::::

:::::::::: sect3

#### Deleted components {#_deleted_components}

::: paragraph
Pcbnew can delete footprint corresponding to components that have been
removed from the schematic. This is optional.
:::

::: paragraph
This is necessary because there are often footprints (holes for fixation
screws, for instance) that are added to the PCB that never appear in the
schematic.
:::

:::: imageblock
::: content
![Pcbnew extra footprints deletion
option](images/Pcbnew_extra_footprints_deletion_option.png)
:::
::::

::: paragraph
If the \"Extra Footprints\" option is checked, a footprint corresponding
to a component not found in the netlist will be deleted, unless they
have the option \"Locked\" active. It is a good idea to activate this
option for \"mechanical\" footprints:
:::

:::: imageblock
::: content
![Pcbnew unlock footprint
option](images/Pcbnew_unlock_footprint_option.png)
:::
::::
::::::::::

::::::: sect3

#### Modified footprints {#_modified_footprints}

::: paragraph
If a footprint is modified in the netlist (using CvPcb), but the
footprint has already been placed, it will not be modified by Pcbnew,
unless the corresponding option of the \'Exchange Footprint\' box of the
netlist dialog is checked:
:::

:::: imageblock
::: content
![Pcbnew exchange module
option](images/Pcbnew_exchange_module_option.png)
:::
::::

::: paragraph
Changing a footprint (replacing a resistor with one of a different size,
for instance) can be effected directly by editing the footprint.
:::
:::::::

:::::::: sect3

#### Advanced options - selection using time stamps {#_advanced_options_selection_using_time_stamps}

::: paragraph
Sometimes the notation of the schematic is changed, without any material
changes in the circuit (this would concern the references - like R5,
U4...​).The PCB is therefore unchanged (except possibly for the
silkscreen markings). Nevertheless, internally, components and
footprints are represented by their reference. In this situation, the
\'Timestamp\' option of the netlist dialog may be selected before
re-reading the netlist:
:::

:::: imageblock
::: content
![Pcbnew module selection
option](images/Pcbnew_module_selection_option.png)
:::
::::

::: paragraph
With this option, Pcbnew no longer identifies footprints by their
reference, but by their time stamp instead. The time stamp is
automatically generated by Eeschema (it is the time and date when the
component was placed in the schematic).
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | Great care should be exercised    |
| Warning                           | when using this option (save the  |
| :::                               | file first!). This is because the |
|                                   | technique is complicated in the   |
|                                   | case of components containing     |
|                                   | multiple parts (e.g. a 7400 has 4 |
|                                   | parts and one case). In this      |
|                                   | situation, the time stamp is not  |
|                                   | uniquely defined (for the 7400    |
|                                   | there would be up to four - one   |
|                                   | for each part). Nevertheless, the |
|                                   | time stamp option usually         |
|                                   | resolves re-annotation problems.  |
+-----------------------------------+-----------------------------------+
:::
::::::::
::::::::::::::::::::::::::::::

:::::::::::: sect2

### Direct exchange for footprints already placed on board {#_direct_exchange_for_footprints_already_placed_on_board}

::: paragraph
Changing a footprint ( or some identical footprints) to another
footprint is very useful, and is very easy:
:::

::: {.olist .arabic}

1.  Click on a footprint to open the Edit dialog box.

2.  Activate Change Footprints.
:::

:::: imageblock
::: content
![Pcbnew change modules button](images/Pcbnew_change_modules_button.png)
:::
::::

::: paragraph
Options for Change Footprint(s):
:::

:::: imageblock
::: content
![Pcbnew footprint exchange
options](images/Pcbnew_footprint_exchange_options.png)
:::
::::

::: paragraph
One must choose a new footprint name and use:
:::

::: ulist

- **Change footprint of \'xx\'** for the current footprint

- **Change footprints \'yy\'** for all footprints like the current
  footprint.

- **Change footprints having same value** for all footprints like the
  current footprint, restricted to components which have the same value.

- **Update all footprints of the board** for reloading of all footprints
  on board.
:::
::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint placement {#_footprint_placement}

::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2

### Assisted placement {#_assisted_placement}

::: paragraph
Whilst moving footprints the footprint ratsnest (the net connections)
can be displayed to assist the placement. To enable this the icon
[![modratsnest](images/icons/modratsnest.png)]{.image} of the left
toolbar must be activated.
:::
::::

:::::::::: sect2

### Manual placement {#_manual_placement}

::: paragraph
Select the footprint with the right mouse button then choose the Move
command from the menu. Move the footprint to the required position and
place it with the left mouse button. If required the selected footprint
can also be rotated, inverted or edited. Select Cancel from the menu (or
press the Esc key) to abort.
:::

::: paragraph
Here you can see the display of the footprint ratsnest during a move:
:::

:::: imageblock
::: content
![Pcbnew ratsnest during move](images/Pcbnew_ratsnest_during_move.png)
:::
::::

::: paragraph
The circuit once all the footprints are placed may be as shown:
:::

:::: imageblock
::: content
![Pcbnew circuit after
placement](images/Pcbnew_circuit_after_placement.png)
:::
::::
::::::::::

:::::::::::::: sect2

### Automatic Footprint Distribution {#_automatic_footprint_distribution}

::: paragraph
Generally speaking, footprints can only be moved if they have not been
\"Fixed\". This attribute can be turned on and off from the pop-up
window (click right mouse button over footprint) whilst in Footprint
Mode, or through the Edit Footprint Menu.
:::

::: paragraph
As stated in the last chapter, new footprints loaded during the reading
of the netlist appear piled up at a single location on the board. Pcbnew
allows an automatic distribution of the footprints to make manual
selection and placement easier.
:::

::: ulist

- Select the option \"Footprint Mode\" (Icon [![mode
  module](images/icons/mode_module.png)]{.image} on the upper toolbar).

- The pop-up window activated by the right mouse button becomes:
:::

::: paragraph
If there is a footprint under the cursor:
:::

:::: imageblock
::: content
![Pcbnew context module mode module under
cursor](images/Pcbnew_context_module_mode_module_under_cursor.png)
:::
::::

::: paragraph
If there is nothing under the cursor:
:::

:::: imageblock
::: content
![Pcbnew context module mode no module under
cursor](images/Pcbnew_context_module_mode_no_module_under_cursor.png)
:::
::::

::: paragraph
In both cases the following commands are available:
:::

::: ulist

- **Spread out All Footprints** allows the automatic distribution of all
  the footprints not Fixed. This is generally used after the first
  reading of a netlist.

- **Spread out Footprints not Already on Board** allows the automatic
  distribution of the footprints which have not been placed already
  within the PCB outline. This command requires that an outline of the
  board has been drawn to determine which footprints can be
  automatically distributed.
:::
::::::::::::::

:::::::::::::::::::::: sect2

### Automatic placement of footprints {#_automatic_placement_of_footprints}

::::: sect3

#### Characteristics of the automatic placer {#_characteristics_of_the_automatic_placer}

::: paragraph
The automatic placement feature allows the placement of footprints onto
the 2 faces of the circuit board (however switching a footprint onto the
copper layer is not automatic).
:::

::: paragraph
It also seeks the best orientation (0, 90, -90, 180 degrees) of the
footprint. The placement is made according to an optimization algorithm,
which seeks to minimize the length of the ratsnest, and which seeks to
create space between the larger footprints with many pads. The order of
placement is optimized to initially place these larger footprints with
many pads.
:::
:::::

:::::::::: sect3

#### Preparation {#_preparation}

::: paragraph
Pcbnew can thus place the footprints automatically, however it is
necessary to guide this placement, because no software can guess what
the user wants to achieve.
:::

::: paragraph
Before an automatic placement is carried out one must:
:::

::: ulist

- Create the outline of the board (It can be complex, but it must be
  closed if the form is not rectangular).

- Manually place the components whose positions are imposed (Connectors,
  clamp holes, etc).

- Similarly, certain SMD footprints and critical components (large
  footprints for example) must be on a specific side or position on the
  board and this must be done manually.

- Having completed any manual placement these footprints must be
  \"Fixed\" to prevent them being moved. With the Footprint Mode icon
  [![mode module](images/icons/mode_module.png)]{.image} selected right
  click on the footprint and pick \"Fix Footprint\" on the Pop-up menu.
  This can also be done through the Edit/Footprint Pop-up menu.

- Automatic placement can then be carried out. With the Footprint Mode
  icon selected, right click and select Glob(al) Move and Place - then
  Autoplace All Footprints.
:::

::: paragraph
During automatic placement, if required, Pcbnew can optimize the
orientation of the footprints. However rotation will only be attempted
if this has been authorized for the footprint (see Edit Footprint
Options).
:::

::: paragraph
Usually resistors and non-polarized capacitors are authorized for 180
degrees rotation. Some footprints (small transistors for example) can be
authorized for +/- 90 and 180 degrees rotation.
:::

::: paragraph
For each footprint one slider authorizes 90 degree Rot(ation) and a
second slider authorizes 180 degree Rot(ation). A setting of 0 prevents
rotation, a setting of 10 authorizes it, and an intermediate value
indicates a preference for/against rotation.
:::

::: paragraph
The rotation authorization can be done by editing the footprint once it
is placed on the board. However it is preferable to set the required
options to the footprint in the library as these settings will then be
inherited each time the footprint is used.
:::
::::::::::

:::::: sect3

#### Interactive auto-placement {#_interactive_auto_placement}

::: paragraph
It may be necessary during automatic placement to stop (press Esc key)
and manually re-position a footprint. Using the command Autoplace Next
Footprint will restart the autoplacement from the point at which it was
stopped.
:::

::: paragraph
The command Autoplace new footprints allows the automatic placement of
the footprints which have not been placed already within the PCB
outline. It will not move those within the PCB outline even if they are
not \"fixed\".
:::

::: paragraph
The command Autoplace Footprint makes it possible to execute an
autoplacement on the footprint pointed to by the mouse, even if its
\'fixed\' attribute is active.
:::
::::::

:::::: sect3

#### Additional note {#_additional_note}

::: paragraph
Pcbnew automatically determines the possible zone of placement of the
footprints by respecting the shape of the board outline, which is not
necessarily rectangular (It can be round, or have cutouts, etc).
:::

::: paragraph
If the board is not rectangular, the outline must be closed, so that
Pcbnew can determine what is inside and what is outside the outline. In
the same way, if there are internal cutouts, their outline will have to
be closed.
:::

::: paragraph
Pcbnew calculates the possible zone of placement of the footprints using
the outline of the board, then passes each footprint in turn over this
area in order to determine the optimum position at which to place it.
:::
::::::
::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Setting routing parameters {#_setting_routing_parameters}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::: sect2

### Current settings {#_current_settings}

::::::: sect3

#### Accessing the main dialog {#_accessing_the_main_dialog}

::: paragraph
The most important parameters are accessed from the following drop-down
menu:
:::

:::: imageblock
::: content
![Pcbnew design rules dropdown](images/Pcbnew_design_rules_dropdown.png)
:::
::::

::: paragraph
and are set in the Design Rules dialog.
:::
:::::::

:::::: sect3

#### Current settings {#_current_settings_2}

::: paragraph
Current settings are displayed in the top toolbar.
:::

:::: imageblock
::: content
![Pcbnew design rules top
toolbar](images/Pcbnew_design_rules_top_toolbar.png)
:::
::::
::::::
::::::::::::

::::::::::: sect2

### General options {#_general_options}

::: paragraph
The General options menu is available via the top toolbar link
Preferences → General dialog.
:::

:::: imageblock
::: content
![Pcbnew preferences menu](images/Pcbnew_preferences_menu.png)
:::
::::

::: paragraph
The dialog looks like the following:
:::

:::: imageblock
::: content
![Pcbnew general options
dialog](images/Pcbnew_general_options_dialog.png)
:::
::::

::: paragraph
For the creation of tracks the necessary parameters are:
:::

::: ulist

- **Tracks 45 Only**: Directions allowed for track segments are 0, 45 or
  90 degrees.

- **Double Segm Track**: When creating tracks, 2 segments will be
  displayed.

- **Tracks Auto Del**: When recreating tracks, the old one will be
  automatically deleted if considered redundant.

- **Magnetic Pads**: The graphic cursor becomes a pad, centered in the
  pad area.

- **Magnetic Tracks**: The graphic cursor becomes the track axis.
:::
:::::::::::

:::::::::::::::::::::::::::::::::: sect2

### Netclasses {#_netclasses}

::: paragraph
Pcbnew allows you to define different routing parameters for each net.
Parameters are defined by a group of nets.
:::

::: ulist

- A group of nets is called a Netclass.

- There is always a netclass called \"default\".

- Users can add other Netclasses.
:::

::: paragraph
A netclass specifies:
:::

::: ulist

- The width of tracks, via diameters and drills.

- The clearance between pads and tracks (or vias).

- When routing, Pcbnew automatically selects the netclass corresponding
  to the net of the track to create or edit, and therefore the routing
  parameters.
:::

:::: sect3

#### Setting routing parameters {#_setting_routing_parameters_2}

::: paragraph
The choice is made in the menu: Design Rules → Design Rules.
:::
::::

::::::: sect3

#### Netclass editor {#_netclass_editor}

::: paragraph
The Netclass editor allows you to:
:::

::: ulist

- Add or delete Netclasses.

- Set routing parameters values: clearance, track width, via sizes.

- Group nets in netclasses.
:::

:::: imageblock
::: content
![Pcbnew design rules editor netclass
tab](images/Pcbnew_design_rules_editor_netclass_tab.png)
:::
::::
:::::::

::::::::::: sect3

#### Global Design Rules {#_global_design_rules}

::: paragraph
The global design rules are:
:::

::: ulist

- Enabling/disabling Blind/buried Vias use.

- Enabling/disabling Micro Vias use.

- Minimum Allowed Values for tracks and vias.
:::

::: paragraph
A DRC error is raised when a value smaller than the minimum value
specified is encountered. The second dialog panel is:
:::

:::: imageblock
::: content
![Pcbnew design rules editor global
tab](images/Pcbnew_design_rules_editor_global_tab.png)
:::
::::

::: paragraph
This dialog also allows to enter a \"stock\" of tracks and via sizes.
:::

::: paragraph
When routing, one can select one of these values to create a track or
via, instead of using the netclass's default value.
:::

::: paragraph
Useful in critical cases when a small track segment must have a specific
size.
:::
:::::::::::

::::::: sect3

#### Via parameters {#_via_parameters}

::: paragraph
Pcbnew handles 3 types of vias:
:::

::: ulist

- Through vias (usual vias).

- Blind or buried vias.

- Micro Vias, like buried vias but restricted to an external layer to
  its nearest neighbor. They are intended to connect BGA pins to the
  nearest inner layer. Their diameter is usually very small and they are
  drilled by laser.
:::

::: paragraph
By default, all vias have the same drill value.
:::

::: paragraph
This dialog specifies the smallest acceptable values for via parameters.
On a board, a via smaller than specified here generates a DRC error.
:::
:::::::

:::: sect3

#### Track parameters {#_track_parameters}

::: paragraph
Specify the minimum acceptable track width. On a board, a track width
smaller than specified here generates a DRC error.
:::
::::

:::::: sect3

#### Specific sizes {#_specific_sizes}

:::: imageblock
::: content
![Pcbnew specific size options](images/Pcbnew_specific_size_options.png)
:::
::::

::: paragraph
One can enter a set of extra tracks and/or via sizes. While routing a
track, these values can be used on demand instead of the values from the
current netclass values.
:::
::::::
::::::::::::::::::::::::::::::::::

::::::: sect2

### Examples and typical dimensions {#_examples_and_typical_dimensions}

:::: sect3

#### Track width {#_track_width}

::: paragraph
Use the largest possible value and conform to the minimum sizes given
here.
:::

+----------+----------+----------+----------+----------+-----------+
| Units    | CLASS 1  | CLASS 2  | CLASS 3  | CLASS 4  | CLASS 5   |
+==========+==========+==========+==========+==========+===========+
| mm       | 0.8      | 0.5      | 0.4      | 0.25     | 0.15      |
+----------+----------+----------+----------+----------+-----------+
| mils     | 31       | 20       | 16       | 10       | 6         |
+----------+----------+----------+----------+----------+-----------+
::::

:::: sect3

#### Insulation (clearance) {#_insulation_clearance}

+----------+----------+----------+----------+----------+-----------+
| Units    | CLASS 1  | CLASS 2  | CLASS 3  | CLASS 4  | CLASS 5   |
+==========+==========+==========+==========+==========+===========+
| mm       | 0.7      | 0.5      | 0.35     | 0.23     | 0.15      |
+----------+----------+----------+----------+----------+-----------+
| mils     | 27       | 20       | 14       | 9        | 6         |
+----------+----------+----------+----------+----------+-----------+

::: paragraph
Usually, the minimum clearance is very similar to the minimum track
width.
:::
::::
:::::::

::::::::::: sect2

### Examples {#_examples}

:::::: sect3

#### Rustic {#_rustic}

::: ulist

- Clearance: 0.35 mm (0.0138 inches).

- Track width: 0.8 mm (0.0315 inches).

- Pad diameter for ICs and vias: 1.91 mm (0.0750 inches).

- Pad diameter for discrete components: 2.54 mm (0.1 inches).

- Ground track width: 2.54 mm (0.1 inches).
:::

:::: imageblock
::: content
![Pcbnew dr example rustic](images/Pcbnew_dr_example_rustic.png)
:::
::::
::::::

:::::: sect3

#### Standard {#_standard}

::: ulist

- Clearance: 0.35 mm (0.0138 inches).

- Track width: 0.5 mm (0.0127 inches).

- Pad diameter for ICs: make them elongated in order to allow tracks to
  pass between IC pads and yet have the pads offer a sufficient adhesive
  surface (1.27 x 2.54 mm -→ 0.05 x 0.1 inches).

- Vias: 1.27 mm (0.0500 inches).
:::

:::: imageblock
::: content
![Pcbnew dr example standard](images/Pcbnew_dr_example_standard.png)
:::
::::
::::::
:::::::::::

:::: sect2

### Manual routing {#_manual_routing}

::: paragraph
Manual routing is often recommended, because it is the only method
offering control over routing priorities. For example, it is preferable
to start by routing power tracks, making them wide and short and keeping
analog and digital supplies well separated. Later, sensitive signal
tracks should be routed. Amongst other problems, automatic routing often
requires many vias. However, automatic routing can offer a useful
insight into the positioning of footprints. With experience, you will
probably find that the automatic router is useful for quickly routing
the \'obvious\' tracks, but the remaining tracks will best be routed by
hand.
:::
::::

:::::::::::::::::::::::: sect2

### Help when creating tracks {#_help_when_creating_tracks}

::: paragraph
Pcbnew can display the full ratsnest, if the button
[![modratsnest](images/icons/modratsnest.png)]{.image} is activated.
:::

::: paragraph
The button [![net highlight](images/icons/net_highlight.png)]{.image}
allows one to highlight a net (click to a pad or an existing track to
highlight the corresponding net).
:::

::: paragraph
The DRC checks tracks in real time while creating them. One cannot
create a track which does not match the DRC rules. It is possible to
disable the DRC by clicking on the button. This is, however, not
recommended, use it only in specific cases.
:::

:::::::::::::: sect3

#### Creating tracks {#_creating_tracks}

::: paragraph
A track can be created by clicking on the button [![add
tracks](images/icons/add_tracks.png)]{.image}. A new track must start on
a pad or on another track, because Pcbnew must know the net used for the
new track (in order to match the DRC rules).
:::

:::: imageblock
::: content
![Pcbnew creating new track](images/Pcbnew_creating_new_track.png)
:::
::::

::: paragraph
As you move the mouse, a track is drawn connecting the origin of the
track with the current mouse position. The track will be drawn with at
most two segments (for example, rightwards, then a switch to
diagonally). Clicking while routing locks in the corner node.
:::

::: paragraph
The direction that the track is drawn in first (e.g. right first, then
diagonally, or diagonally first then right) is called the \"Track
Posture\" and can be switched with the hotkey \'/\' or the button
[![change entry orient](images/icons/change_entry_orient.png)]{.image}.
:::

::: paragraph
[![Pcbnew routing posture](images/Pcbnew_routing_posture.png)]{.image}
:::

::: paragraph
Holding \'Ctrl\' while routing in the non-legacy canvases constrains the
routing to a single horizontal or vertical segment. Switching posture
changes to a single diagonal segment. Holding \'Shift\' while routing
removes the \'snap to object\' gravity.
:::

::: paragraph
When creating a new track, Pcbnew shows links to nearest unconnected
pads.
:::

::: paragraph
End the track by double-clicking, by the pop-up menu or by the hotkey
\'End\'.
:::

:::: imageblock
::: content
![Pcbnew track in progres
context](images/Pcbnew_track_in_progres_context.png)
:::
::::
::::::::::::::

:::: sect3

#### Moving and dragging tracks {#_moving_and_dragging_tracks}

::: paragraph
When the button [![add tracks](images/icons/add_tracks.png)]{.image} is
active, the track where the cursor is positioned can be moved with the
hotkey \'M\'. If you want to drag the track you can use the hotkey
\'G\'.
:::
::::

:::::: sect3

#### Via Insertion {#_via_insertion}

::: paragraph
A via can be inserted only when a track is in progress:
:::

::: ulist

- By the pop-up menu.

- By the hotkey \'V\'.

- By switching to a new copper layer using the appropriate hotkey.
:::

::: paragraph
Holding \'Shift\' while adding a via ends routing as soon as the via is
placed. This is useful when adding a connection to a plane, so the
active layer doesn't change and no extra key need be pressed to exit
routing.
:::
::::::
::::::::::::::::::::::::

:::::::::::::: sect2

### Select/edit the track width and via size {#_selectedit_the_track_width_and_via_size}

::: paragraph
When clicking on a track or a pad, Pcbnew automatically selects the
corresponding Netclass, and the track size and via dimensions are
derived from this netclass.
:::

::: paragraph
As previously seen, the Global Design Rules editor has a tool to insert
extra tracks and via sizes.
:::

::: ulist

- The horizontal toolbar can be used to select a size.

- When the button [![add tracks](images/icons/add_tracks.png)]{.image}
  is active, the current track width can be selected from the pop-up
  menu (accessible as well when creating a track).

- The user can utilize the default Netclasses values or a specified
  value.
:::

::::: sect3

#### Using the horizontal toolbar {#_using_the_horizontal_toolbar}

:::: imageblock
::: content
![Pcbnew track toolbar](images/Pcbnew_track_toolbar.png)
:::
::::

+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar track width                                                      | Track width selection. The symbol \* is  |
| selection](images/Pcbnew_track_toolbar_track_width_selection.png){width="70%"}]{.image}  | a mark for default Netclass value        |
|                                                                                          | selection.                               |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar track width selection in                                         | Selecting a specific track width value.  |
| use](images/Pcbnew_track_toolbar_track_width_selection_in_use.png){width="70%"}]{.image} | The first value in the list is always    |
|                                                                                          | the netclass value. Other values are     |
|                                                                                          | tracks widths entered from the Global    |
|                                                                                          | Design Rules editor.                     |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar via size                                                         | Via size selection. The symbol \* is a   |
| selection](images/Pcbnew_track_toolbar_via_size_selection.png){width="70%"}]{.image}     | mark for default Netclass value          |
|                                                                                          | selection.                               |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar via size selection in                                            | Selecting a specific via dimension       |
| use](images/Pcbnew_track_toolbar_via_size_selection_in_use.png){width="70%"}]{.image}    | value. The first value in the list is    |
|                                                                                          | always the netclass value. Other values  |
|                                                                                          | are via dimensions entered from the      |
|                                                                                          | Global Design Rules editor.              |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![auto track width](images/icons/auto_track_width.png)]{.image}                         | When enabled: Automatic track width      |
|                                                                                          | selection. When starting a track on an   |
|                                                                                          | existing track, the new track has the    |
|                                                                                          | same width as the existing track.        |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar grid size                                                        | Grid size selection.                     |
| selection](images/Pcbnew_track_toolbar_grid_size_selection.png){width="70%"}]{.image}    |                                          |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar zoom                                                             | Zoom selection.                          |
| selection](images/Pcbnew_track_toolbar_zoom_selection.png){width="70%"}]{.image}         |                                          |
+------------------------------------------------------------------------------------------+------------------------------------------+
:::::

::::::: sect3

#### Using the pop-up menu {#_using_the_pop_up_menu}

::: paragraph
One can select a new size for routing, or change to a previously created
via or track segment:
:::

:::: imageblock
::: content
![Pcbnew track context menu](images/Pcbnew_track_context_menu.png)
:::
::::

::: paragraph
If you want to change many via (or track) sizes, the best way is to use
a specific Netclass for the net(s) that must be edited (see global
changes).
:::
:::::::
::::::::::::::

:::::::::::::::::::: sect2

### Editing and changing tracks {#_editing_and_changing_tracks}

::::::::::: sect3

#### Change a track {#_change_a_track}

::: paragraph
In many cases redrawing a track is required.
:::

::: paragraph
New track (in progress):
:::

:::: imageblock
::: content
![Pcbnew new track in progress](images/Pcbnew_new_track_in_progress.png)
:::
::::

::: paragraph
When finished:
:::

:::: imageblock
::: content
![Pcbnew new track completed](images/Pcbnew_new_track_completed.png)
:::
::::

::: paragraph
Pcbnew will automatically remove the old track if it is redundant.
:::
:::::::::::

:::::::::: sect3

#### Global changes {#_global_changes}

::: paragraph
Global tracks and via sizes dialog editor is accessible via the pop-up
window by right clicking on a track:
:::

:::: imageblock
::: content
![Pcbnew track global edit context
menu](images/Pcbnew_track_global_edit_context_menu.png)
:::
::::

::: paragraph
The dialog editor allows global changes of tracks and/or vias for:
:::

::: ulist

- The current net.

- The whole board.
:::

:::: imageblock
::: content
![Pcbnew track global edit
dialog](images/Pcbnew_track_global_edit_dialog.png)
:::
::::
::::::::::
::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::: sect1

## Interactive Router {#_interactive_router}

:::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
The Interactive Router lets you quickly and efficiently route your PCBs
by shoving off or walking around items on the PCB that collide with the
trace you are currently drawing.
:::

::: paragraph
Following modes are supported:
:::

::: ulist

- **Highlight collisions**, which highlights all violating objects with
  a nice, shiny green color and shows violating clearance regions.

- **Shove**, attempting to push and shove all items colliding with the
  currently routed track.

- **Walk around**, trying to avoid obstacles by hugging/walking around
  them.
:::

:::::::::: sect2

### Setting up {#_setting_up}

::: paragraph
Before using the Interactive Router, please set up these two things:
:::

::: ulist

- **Clearance settings** To set the clearances, open the *Design Rules*
  dialog and make sure at least the default clearance value looks
  sensible.
:::

:::: imageblock
::: content
![Rules editor](images/en/rules_editor.png)
:::
::::

::: ulist

- **Enable OpenGL mode** By selecting *View→Switch canvas to OpenGL*
  menu option or pressing **F11**.
:::

:::: imageblock
::: content
![OpenGL mode](images/en/opengl_menu.png)
:::
::::
::::::::::

::::::::::: sect2

### Laying out tracks {#_laying_out_tracks}

::: paragraph
To activate the router tool press the *Interactive Router* button
[![Interactive Router Button](images/route_icon.png)]{.image} or the
**X** key. The cursor will turn into a cross and the tool name, will
appear in the status bar.
:::

::: paragraph
To start a track, click on any item (a pad, track or a via) or press the
**X** key again hovering the mouse over that item. The new track will
use the net of the starting item. Clicking or pressing **X** on empty
PCB space starts a track with no net assigned.
:::

::: paragraph
Move the mouse to define shape of the track. The router will try to
follow the mouse trail, hugging unmovable obstacles (such as pads) and
shoving colliding traces/vias, depending on the mode. Retreating the
mouse cursor will cause the shoved items to spring back to their former
locations.
:::

::: paragraph
Clicking on a pad/track/via in the same net finishes routing. Clicking
in empty space fixes the segments routed so far and continues routing
the trace.
:::

::: paragraph
In order to stop routing and undo all changes (shoved items, etc.),
simply press **Esc**.
:::

::: paragraph
Pressing **V** or selecting *Place Through Via* from the context menu
while routing a track attaches a via at the end of the trace being
routed. Pressing **V** again disables via placement. Clicking in any
spot establishes the via and continues routing (unless \'Shift\' is
held).
:::

::: paragraph
Pressing **/** or selecting *Switch Track Posture* from the context menu
toggles the direction of the initial track segment between straight or
diagonal.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | By default, the router snaps to   |
| Note                              | centers/axes of the items.        |
| :::                               | Snapping can be disabled by       |
|                                   | holding **Shift** while routing   |
|                                   | or selecting items.               |
+-----------------------------------+-----------------------------------+
:::
:::::::::::

::::: sect2

### Setting track widths and via sizes {#_setting_track_widths_and_via_sizes}

::: paragraph
There are several ways to pre-select a track width/via size or to change
it during routing:
:::

::: ulist

- Use standard KiCad shortcuts.

- Press **W** or select *Custom Track Width* from the context menu to
  type in a custom track width/via size.

- Pick a predefined width from the *Select Track Width* sub-menu of the
  context menu.

- Select *Use the starting track width* in the *Select Track Width* menu
  to pick the width from the start item (or the traces already connected
  to it).
:::
:::::

:::: sect2

### Dragging {#_dragging}

::: paragraph
The router can drag track segments, corners and vias. To drag an item,
click on it with **Ctrl** key pressed, hover the mouse and press **G**
or select *Drag Track/Via* from the context menu. Finish dragging by
clicking again or abort by pressing *Esc*.
:::
::::

:::::::: sect2

### Options {#_options}

::: paragraph
The router behavior can be configured by pressing *E* or selecting
*Routing Options* from the context menu while in the Track mode. It
opens a window like the one below:
:::

::: paragraph
The options are:
:::

:::: imageblock
::: content
![Router options window screenshot](images/en/router_options.png)
:::
::::

::: ulist

- **Mode** - select how the router handles DRC violation (shoving,
  walking around, etc.)

- **Shove vias** - when disabled, vias are treated as un-movable objects
  and hugged instead of shoved.

- **Jump over obstacles** - when enabled, the router tries to move
  colliding traces behind solid obstacles (e.g. pads) instead of
  \"reflecting\" back the collision

- **Remove redundant tracks** - removes loops while routing (e.g. if the
  new track ensures same connectivity as an already existing one, the
  old track is removed). Loop removal works locally (only between the
  start and end of the currently routed trace).

- **Automatic neckdown** - when enabled, the router tries to break out
  pads/vias in a clean way, avoiding acute angles and jagged breakout
  traces.

- **Smooth dragged segments** - when enabled, the router attempts to
  merge several jagged segments into a single straight one (dragging
  mode).

- **Allow DRC violations** (*Highlight collisions* mode only) - allows
  to establish a track even if is violating the DRC rules.

- **Optimizer effort** - defines how much time the router shall spend
  optimizing the routed/shoved traces. More effort means cleaner routing
  (but slower), less effort means faster routing but somewhat jagged
  traces.
:::
::::::::
::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Creating copper zones {#_creating_copper_zones}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Copper zones are defined by an outline (closed polygon), and can include
holes (closed polygons inside the outline). A zone can be drawn on a
copper layer or alternatively on a technical layer.
:::

::::::::::: sect2

### Creating zones on copper layers {#_creating_zones_on_copper_layers}

::: paragraph
Pad (and track) connections to filled copper areas are checked by the
DRC engine. A zone must be filled (not just created) to connect pads.
Pcbnew currently uses track segments or polygons to fill copper areas.
:::

::: paragraph
Each option has its advantages and its disadvantages, the main
disadvantage being increased screen redraw time on slower machines. The
final result is however the same.
:::

::: paragraph
For calculation time reasons, the zone filling is not recreated after
each change, but only:
:::

::: ulist

- If a filling zone command is executed.

- When a DRC test is performed.
:::

::: paragraph
Copper zones must be filled or refilled after changes in tracks or pads
are made. Copper zones (usually ground and power planes) are usually
attached to a net.
:::

::: paragraph
In order to create a copper zone you should:
:::

::: ulist

- Select parameters (net name, layer...​). Turning on the layer and
  highlighting this net is not mandatory but it is good practice.

- Create the zone limit (If not, the entire board will be filled.).

- Fill the zone.
:::

::: paragraph
Pcbnew tries to fill all zones in one piece, and usually, there will be
no unconnected copper blocks. It can happen that some areas remain
unfilled. Zones having no net are not cleaned and can have insulated
areas.
:::
:::::::::::

:::::::::::::::::::::::::::::::::::::: sect2

### Creating a zone {#_creating_a_zone}

::::::::::::: sect3

#### Creating the limits of a zone {#_creating_the_limits_of_a_zone}

::: paragraph
Use the tool [![add zone](images/icons/add_zone.png)]{.image}. The
active layer must be a copper layer. When clicking to start the zone
outline, the following dialog box will be opened.
:::

:::: imageblock
::: content
![Pcbnew zone properties
dialog](images/Pcbnew_zone_properties_dialog.png)
:::
::::

::: paragraph
You can specify all parameters for this zone:
:::

::: ulist

- Net

- Layer

- Filling options

- Pad options

- Priority level
:::

::: paragraph
Draw the zone limit on this layer. This zone limit is a polygon, created
by left-clicking at each corner. A double-click will end and close the
polygon. If the starting point and ending point are not at the same
coordinate, Pcbnew will add a segment from the end point to the start
point.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - The DRC is active when creating |
| :::                               |   zone outlines.                  |
|                                   |                                   |
|                                   | - A corner which creates a DRC    |
|                                   |   error will not be accepted by   |
|                                   |   Pcbnew.                         |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
In the following image you can see an example of a zone limit (polygon
in thin hatched line):
:::

:::: imageblock
::: content
![Pcbnew zone limit example](images/Pcbnew_zone_limit_example.png)
:::
::::
:::::::::::::

:::::::::::::: sect3

#### Priority level {#_priority_level}

::: paragraph
Sometimes a small zone must be created inside a large zone.
:::

::: paragraph
This is possible if the small zone has a higher priority level than the
large zone.
:::

::: paragraph
Level setting:
:::

:::: imageblock
::: content
![Pcbnew zone priority level
setting](images/Pcbnew_zone_priority_level_setting.png)
:::
::::

::: paragraph
Here is an example:
:::

:::: imageblock
::: content
![Pcbnew zone priority example](images/Pcbnew_zone_priority_example.png)
:::
::::

::: paragraph
After filling:
:::

:::: imageblock
::: content
![Pcbnew zone priority example after
filling](images/Pcbnew_zone_priority_example_after_filling.png)
:::
::::
::::::::::::::

:::::::::::::: sect3

#### Filling the zone {#_filling_the_zone}

::: paragraph
When filling a zone, Pcbnew removes all unconnected copper islands. To
access the zone filling command, right-click on the edge zone.
:::

:::: imageblock
::: content
![Pcbnew zone context menu](images/Pcbnew_zone_context_menu.png)
:::
::::

::: paragraph
Activate the \"Fill Zone\" command. Below is the filling result for a
starting point inside the polygon:
:::

:::: imageblock
::: content
![Pcbnew zone filling result](images/Pcbnew_zone_filling_result.png)
:::
::::

::: paragraph
The polygon is the border of the filling area. You can see a non-filled
area inside the zone, because this area is not accessible:
:::

::: ulist

- A track creates a border, and

- There is no starting point for filling in this area.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | You can use many polygons to      |
| Note                              | create cutout areas. Here you can |
| :::                               | see an example:                   |
+-----------------------------------+-----------------------------------+
:::

:::: imageblock
::: content
![Pcbnew zone filled with
cutout](images/Pcbnew_zone_filled_with_cutout.png)
:::
::::
::::::::::::::
::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::: sect2

### Filling options {#_filling_options}

:::: imageblock
::: content
![Pcbnew zone filling options](images/Pcbnew_zone_filling_options.png)
:::
::::

::: paragraph
When you fill an area, you must choose:
:::

::: ulist

- The mode for filling.

- The clearance and minimum copper thickness.

- How pads are drawn inside the zone (or connected to this zone).

- Thermal relief parameters.
:::

:::: sect3

#### Filling mode {#_filling_mode}

::: paragraph
Zones can be filled using polygons or segments. The result is the same.
If you have problems with polygon mode (slow screen refresh) you should
use segments.
:::
::::

::::: sect3

#### Clearance and minimum copper thickness {#_clearance_and_minimum_copper_thickness}

::: paragraph
A good choice for clearance is a grid that is a bit bigger than the
routing grid. Minimum copper thickness value ensures that there are no
too small copper areas.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | if this value is too large, small |
| Warning                           | shapes like thermal stubs in      |
| :::                               | thermal reliefs cannot be drawn.  |
+-----------------------------------+-----------------------------------+
:::
:::::

::::::::::::: sect3

#### Pad options {#_pad_options}

::: paragraph
Pads of the net can either be included or excluded from the zone, or
connected by thermal reliefs.
:::

::: ulist

- If included, soldering and un-soldering can be very difficult due to
  the high thermal mass of the large copper area.
:::

:::: imageblock
::: content
![Pcbnew zone include pads](images/Pcbnew_zone_include_pads.png)
:::
::::

::: ulist

- If excluded, the connection to the zone will not be very good.

  ::: ulist

  - The zone can be filled only if tracks exists to connect zone areas.

  - Pads must be connected by tracks.
  :::
:::

:::: imageblock
::: content
![Pcbnew zone exclude pads](images/Pcbnew_zone_exclude_pads.png)
:::
::::

::: ulist

- A thermal relief is a good compromise.

  ::: ulist

  - Pad is connected by 4 track segments.

  - The segment width is the current value used for the track width.
  :::
:::

:::: imageblock
::: content
![Pcbnew zone thermal relief](images/Pcbnew_zone_thermal_relief.png)
:::
::::
:::::::::::::

:::::::: sect3

#### Thermal relief parameters {#_thermal_relief_parameters}

:::: imageblock
::: content
![Pcbnew thermal relief
settings](images/Pcbnew_thermal_relief_settings.png)
:::
::::

::: paragraph
You can set two parameters for thermal reliefs:
:::

:::: imageblock
::: content
![Pcbnew thermal relief
parameters](images/Pcbnew_thermal_relief_parameters.png)
:::
::::
::::::::

::::: sect3

#### Choice of parameters {#_choice_of_parameters}

::: paragraph
The copper width value for thermal reliefs must be bigger than the
minimum thickness value for the copper zone. If not, they cannot be
drawn.
:::

::: paragraph
Additionally, a too large value for this parameter or for antipad size
does not allow one to create a thermal relief for small pads (like pad
sizes used for SMD components).
:::
:::::
::::::::::::::::::::::::::::::::

:::::::::: sect2

### Adding a cutout area inside a zone {#_adding_a_cutout_area_inside_a_zone}

::: paragraph
A zone must already exist. To add a cutout area (a non-filled area
inside the zone):
:::

::: ulist

- Right-click on an existing edge outline.

- Select Add Cutout Area.
:::

:::: imageblock
::: content
![Pcbnew add cutout menu item](images/Pcbnew_add_cutout_menu_item.png)
:::
::::

::: ulist

- Create the new outline.
:::

:::: imageblock
::: content
![Pcbnew zone unfilled cutout
outline](images/Pcbnew_zone_unfilled_cutout_outline.png)
:::
::::
::::::::::

::::::::::::::::::::::: sect2

### Outlines editing {#_outlines_editing}

::: paragraph
An outline can be modified by:
:::

::: ulist

- Moving a corner or an edge.

- Deleting or adding a corner.

- Adding a similar zone, or a cutout area.
:::

::: paragraph
If polygons are overlapping they will be combined.
:::

:::: imageblock
::: content
![Pcbnew zone modification menu
items](images/Pcbnew_zone_modification_menu_items.png)
:::
::::

::: paragraph
To do that, right-click on a corner or on an edge, then select the
proper command.
:::

::: paragraph
Here is a corner (from a cutout) that has been moved:
:::

:::: imageblock
::: content
![Pcbnew zone corner move
during](images/Pcbnew_zone_corner_move_during.png)
:::
::::

::: paragraph
Here is the final result:
:::

:::: imageblock
::: content
![Pcbnew zone corner move
after](images/Pcbnew_zone_corner_move_after.png)
:::
::::

::: paragraph
Polygons are combined.
:::

::::::::: sect3

#### Adding a similar zone {#_adding_a_similar_zone}

::: paragraph
Adding the similar zone:
:::

:::: imageblock
::: content
![Pcbnew zone add similar
during](images/Pcbnew_zone_add_similar_during.png)
:::
::::

::: paragraph
Final result:
:::

:::: imageblock
::: content
![Pcbnew zone add similar
after](images/Pcbnew_zone_add_similar_after.png)
:::
::::
:::::::::
:::::::::::::::::::::::

:::: sect2

### Editing zone parameters {#_editing_zone_parameters}

::: paragraph
When right-clicking on an outline, and using \'Edit Zone Params\' the
Zone params Dialog box will open. Initial parameters can be inputted .
If the zone is already filled, refilling it will be necessary.
:::
::::

:::::: sect2

### Final zone filling {#_final_zone_filling}

::: paragraph
When the board is finished, one must fill or refill all zones. To do
this:
:::

::: ulist

- Activate the tool zones via the button [![add
  zone](images/icons/add_zone.png)]{.image}.

- Right-click to display the pop-up menu.

- Use Fill or Refill All Zones: [![Pcbnew fill refill all
  zones](images/Pcbnew_fill_refill_all_zones.png)]{.image}
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | Calculation can take some time if |
| Warning                           | the filling grid is small.        |
| :::                               |                                   |
+-----------------------------------+-----------------------------------+
:::
::::::

:::::: sect2

### Change zones net names {#_change_zones_net_names}

::: paragraph
After editing a schematic, you can change the name of any net. For
instance VCC can be changed to +5V.
:::

::: paragraph
When a global DRC is made Pcbnew checks if the zone net name exists, and
displays an error if not.
:::

::: paragraph
Manually editing the zone parameters will be necessary to change the old
name to the new one.
:::
::::::

:::::::::: sect2

### Creating zones on technical layers {#_creating_zones_on_technical_layers}

::::::::: sect3

#### Creating zone limits {#_creating_zone_limits}

::: paragraph
This is done using the button [![add
zone](images/icons/add_zone.png)]{.image}. The active layer must be a
technical layer.
:::

::: paragraph
When clicking to start the zone outline, this dialog box is opened:
:::

:::: imageblock
::: content
![Pcbnew technical layer zone
dialog](images/Pcbnew_technical_layer_zone_dialog.png)
:::
::::

::: paragraph
Select the technical layer to place the zone and draw the zone outline
like explained previously for copper layers.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - For editing outlines use the    |
| :::                               |   same method as for copper       |
|                                   |   zones.                          |
|                                   |                                   |
|                                   | - If necessary, cutout areas can  |
|                                   |   be added.                       |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::::::::
::::::::::

:::::::::::: sect2

### Creating a Keepout area {#_creating_a_keepout_area}

::: paragraph
Select the tool [![add keepout
area](images/icons/add_keepout_area.png)]{.image}
:::

::: paragraph
The active layer should be a copper layer.
:::

::: paragraph
After clicking on the starting point of a new keepout area, the dialog
box is opened:
:::

:::: imageblock
::: content
![Pcbnew keepout area
properties](images/Pcbnew_keepout_area_properties.png)
:::
::::

::: paragraph
One can select disallowed items:
:::

::: ulist

- Tracks.

- Vias.

- Copper pours.
:::

::: paragraph
When a track or a via is inside a keepout which does not allow it, a DRC
error will be raised.
:::

::: paragraph
For copper zones, the area inside a keepout with no copper pour will not
be filled. A keep-out area is a like a zone, so editing its outline is
analogous to copper zone editing.
:::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Files for circuit fabrication {#_files_for_circuit_fabrication}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Let us see now what the steps are for the creation of the necessary
files for the production of your printed circuit board.
:::

::: paragraph
All files generated by KiCad are placed in the working directory which
is the same directory that contains the xxxx.brd file for the printed
circuit board.
:::

::::::::: sect2

### Final preparations {#_final_preparations}

::: paragraph
The generation of the necessary files for the production of your printed
circuit board includes the following preparatory steps.
:::

::: ulist

- Mark any layer (e.g., \'top or front\' and \'bottom or back\') with
  the project name by placing appropriate text upon each of the layers.

- All text on copper layers (sometimes called \'solder\' or \'bottom\')
  must be mirrored.

- Create any ground planes, modifying traces as required to ensure they
  are contiguous.

- Place alignment crosshairs and possibly the dimensions of the board
  outline (these are usually placed on one of the general purpose
  layers).
:::

::: paragraph
Here is an example showing all of these elements, except ground planes,
which have been omitted for better visibility:
:::

:::: imageblock
::: content
![Pcbnew final preparation example
board](images/Pcbnew_final_preparation_example_board.png)
:::
::::

::: paragraph
A color key for the 4 copper layers has also been included: [![Pcbnew
layer colour key](images/Pcbnew_layer_colour_key.png)]{.image}
:::
:::::::::

::::::::: sect2

### Final DRC test {#_final_drc_test}

::: paragraph
Before generating the output files, a global DRC test is very strongly
recommended.
:::

::: paragraph
Zones are filled or refilled when starting a DRC. Press the button
[![drc](images/icons/drc.png)]{.image} to launch the following DRC
dialog:
:::

:::: imageblock
::: content
![Pcbnew DRC dialog](images/Pcbnew_DRC_dialog.png)
:::
::::

::: paragraph
Adjust the parameters accordingly and then press the \"Start DRC\"
button.
:::

::: paragraph
This final check will prevent any unpleasant surprises.
:::
:::::::::

:::::: sect2

### Setting coordinates origin {#_setting_coordinates_origin}

::: paragraph
Set the coordinates origin for the photo plot and drill files, one must
place the auxiliary axis on this origin. Activate the icon [![pcb
offset](images/icons/pcb_offset.png)]{.image}. Move the auxiliary axis
by left-clicking on the chosen location.
:::

:::: imageblock
::: content
![Pcbnew setting pcb origin](images/Pcbnew_setting_pcb_origin.png)
:::
::::
::::::

:::::::::::::::::::::::::::::::::::: sect2

### Generating files for photo-tracing {#_generating_files_for_photo_tracing}

::: paragraph
This is done via the Files/Plot menu option and invokes the following
dialog:
:::

:::: imageblock
::: content
![Pcbnew plot dialog](images/Pcbnew_plot_dialog.png)
:::
::::

::: paragraph
Usually, the files are in the GERBER format. Nevertheless, it is
possible to produce output in both HPGL and POSTSCRIPT formats. When
Postscript format is selected, this dialog will appear.
:::

:::: imageblock
::: content
![Pcbnew plot postscript
dialog](images/Pcbnew_plot_postscript_dialog.png)
:::
::::

::: paragraph
In these formats, a fine scale adjust can be used to compensate for the
plotter accuracy and to have a true scale of 1 for the output:
:::

:::: imageblock
::: content
![Pcbnew plot fine scale
setting](images/Pcbnew_plot_fine_scale_setting.png)
:::
::::

::::::::: sect3

#### GERBER format {#_gerber_format}

::: paragraph
For each layer, Pcbnew generates a separate file following the GERBER
274X standard, by default in 4.6 format (each coordinate in the file is
represented by 10 digits, of which 4 are before the decimal point and 6
follow it), units in inches, and a scale of 1.
:::

::: paragraph
It is normally necessary to create files for all of the copper layers
and, depending on the circuit, for the silkscreen, solder mask, and
solder paste layers. All of these files can be produced in one step, by
selecting the appropriate check boxes.
:::

::: paragraph
For example, for a double-sided circuit with silkscreen, solder mask and
solder paste (for SMD components), 8 files should be generated (\'xxxx\'
represents the name of the .brd file).
:::

::: ulist

- xxxx-F_Cu.gbr for the component side.

- xxxx-B_Cu.gbr for the copper side.

- xxxx-F_SilkS.gbr for the component-side silkscreen markings.

- xxxx-B_SilkS.gbr for the copper-side silkscreen markings.

- xxxx-F_Paste.gbr for the component-side solder paste.

- xxxx-B_Paste.gbr for the copper-side solder paste.

- xxxx-F_Mask.gbr for the component-side solder mask.

- xxxx-B_Mask.gbr for the copper-side solder mask.
:::

::: paragraph
GERBER file format:
:::

::: paragraph
The format used by Pcbnew is RS274X format 4.6, Imperial, Leading zero
omitted, Abs format. These are very usual settings.
:::
:::::::::

::::: sect3

#### POSTSCRIPT format {#_postscript_format}

::: paragraph
The standard extension for the output files is .ps in the case of
postscript output. As for HPGL output, the tracing can be at
user-selected scales and can be mirrored. If the Org = Centre option is
active, the origin for the coordinates of the tracing table is assumed
to be in the centre of the drawing.
:::

::: paragraph
If the Print Sheet Ref option is active, the sheet cartridge is traced.
:::
:::::

:::::::::: sect3

#### Plot options {#_plot_options}

::: paragraph
Gerber format:
:::

:::: imageblock
::: content
![Pcbnew plot options gerber](images/Pcbnew_plot_options_gerber.png)
:::
::::

::: paragraph
Other formats:
:::

:::: imageblock
::: content
![Pcbnew plot options other
formats](images/Pcbnew_plot_options_other_formats.png)
:::
::::

::: paragraph
GERBER format specific options:
:::

+-----------------------------------+-----------------------------------+
| Use Protel filename extensions    | Use .gbl .gtl .gbs .gts .gbp .gtp |
|                                   | .gbo .gto instead of .gbr for     |
|                                   | file name extensions.             |
+-----------------------------------+-----------------------------------+
| Include extended attributes       | Output extended attributes to     |
|                                   | file.                             |
+-----------------------------------+-----------------------------------+
| Subtract soldermask from          | Remove all Silk from solder paste |
| silkscreen                        | areas.                            |
+-----------------------------------+-----------------------------------+
::::::::::

:::::::: sect3

#### Other formats {#_other_formats}

::: paragraph
The standard extension depends on the output file type.
:::

::: paragraph
Some options are not available for some formats.
:::

::: paragraph
The plot can be done at user-selected scales and can be mirrored.
:::

::: paragraph
The Print Drill Opt list offers the option of pads that are filled,
drilled to the correct diameter or drilled with a small hole (to guide
hand drilling).
:::

::: paragraph
If the Print Sheet Ref option is active, the sheet cartridge is traced.
:::
::::::::
::::::::::::::::::::::::::::::::::::

::::::::::::::::::::: sect2

### Global clearance settings for the solder stop and the solder paste mask {#_global_clearance_settings_for_the_solder_stop_and_the_solder_paste_mask}

::: paragraph
Mask clearance values can be set globally for the solder mask layers and
the solder paste layers. These clearances can be set at the following
levels.
:::

::: ulist

- At pads level.

- At footprint level.

- Globally.
:::

::: paragraph
And Pcbnew uses by priority order.
:::

::: ulist

- Pad values. If null:

- Footprint values. If null:

- Global values.
:::

::::::::: sect3

#### Access {#_access}

::: paragraph
The menu option for this is available via the Dimensions menu:
:::

:::: imageblock
::: content
![Pcbnew pad mask clearance menu
item](images/Pcbnew_pad_mask_clearance_menu_item.png)
:::
::::

::: paragraph
The dialog box is the following:
:::

:::: imageblock
::: content
![Pcbnew pad mask settings
dialog](images/Pcbnew_pad_mask_settings_dialog.png)
:::
::::
:::::::::

:::::: sect3

#### Solder mask clearance {#_solder_mask_clearance}

::: paragraph
A value near to 0.2 mm is usually good. This value is positive because
the mask is usually bigger than the pad.
:::

::: paragraph
One can set a minimum value for the solder mask width, between 2 pads.
:::

::: paragraph
If the actual value is smaller than the minimum value, the 2 solder mask
shapes will be merged.
:::
::::::

::::: sect3

#### Solder paste clearance {#_solder_paste_clearance}

::: paragraph
The final clearance is the sum of the solder paste clearance and a
percentage of the pad size.
:::

::: paragraph
This value is negative because the mask is usually smaller than the pad.
:::
:::::
:::::::::::::::::::::

::::::::::::::: sect2

### Generating drill files {#_generating_drill_files}

::: paragraph
The creation of a drill file xxxx.drl following the EXCELLON standard is
always necessary.
:::

::: paragraph
One can also produce an optional drill report, and an optional drill
map.
:::

::: ulist

- The drill map can be plotted using several formats.

- The drill report is a plain text file.
:::

::: paragraph
The generation of these files is controlled via:
:::

::: ulist

- \"Create Drill File\" button, or

- Files/Fabrication Outputs/Drill file menu selection.
:::

::: paragraph
The Drill tools dialog box will be the following:
:::

:::: imageblock
::: content
![Pcbnew drill file dialog](images/Pcbnew_drill_file_dialog.png)
:::
::::

::: paragraph
For setting the coordinate origin, the following dialog box is used:
:::

:::: imageblock
::: content
![Pcbnew drill origin setting](images/Pcbnew_drill_origin_setting.png)
:::
::::

::: ulist

- Absolute: absolute coordinate system is used.

- Auxiliary axis: coordinates are relative to the auxiliary axis, use
  the icon (right toolbar) to set it.
:::
:::::::::::::::

:::: sect2

### Generating wiring documentation {#_generating_wiring_documentation}

::: paragraph
To produce wiring documentation files, the component and copper
silkscreen layers can be traced. Usually, just the component-side
silkscreen markings are sufficient for wiring a PCB. If the copper-side
silkscreen is used, the text it contains should be mirrored in order to
be readable.
:::
::::

:::: sect2

### Generation of files for automatic component insertion {#_generation_of_files_for_automatic_component_insertion}

::: paragraph
This option is accessed via the Postprocess/Create Cmp file menu option.
However, no file will be generated unless at least one footprint has the
Normal+Insert attribute activated (see Editing Footprints). One or two
files will be produced, depending upon whether insertable components are
present on one or both sides of the PCB. A dialogue box will display the
names of the file(s) created.
:::
::::

::::::: sect2

### Advanced tracing options {#_advanced_tracing_options}

::: paragraph
The options described below (part of the Files/Plot dialogue) allow for
fine-grained control of the tracing process. They are particularly
useful when printing the silkscreen markings for wiring documentation.
:::

:::: imageblock
::: content
![Pcbnew advanced tracing
options](images/Pcbnew_advanced_tracing_options.png)
:::
::::

::: paragraph
The available options are:
:::

+----------------------+-----------------------------------------------+
| Plot sheet reference | Trace sheet outline and the cartridge.        |
| on all layers        |                                               |
+----------------------+-----------------------------------------------+
| Plot pads on         | Enables/disables printing of pad outlines on  |
| silkscreen           | the silkscreen layers (if the pads have       |
|                      | already been declared to appear on these      |
|                      | layers). Prevents any pads from being printed |
|                      | in the disabled mode.                         |
+----------------------+-----------------------------------------------+
| Plot footprint       | Enables printing of VALUE text on the         |
| values               | silkscreen.                                   |
+----------------------+-----------------------------------------------+
| Plot footprint       | Enables printing of the REFERENCE text on the |
| references           | silkscreen.                                   |
+----------------------+-----------------------------------------------+
| Force plotting of    | Forces printing of fields (reference, value)  |
| invisible            | declared as invisible. In combination with    |
| values/references    | \'Plot footprint values\' and \'Plot          |
|                      | footprint references\', this option enables   |
|                      | production of documents for guiding wiring    |
|                      | and repair. These options have proven         |
|                      | necessary for circuits using components that  |
|                      | are too small (SMD) to allow readable         |
|                      | placement of two separate text fields.        |
+----------------------+-----------------------------------------------+
| Do not tent vias     | Delete the mask over the vias.                |
+----------------------+-----------------------------------------------+
| Exclude PCB edge     | GERBER format specific. Do not plot graphic   |
| layer from other     | items on edge layer.                          |
| layers               |                                               |
+----------------------+-----------------------------------------------+
| Use Protel filename  | GERBER format specific. When creating files,  |
| extensions           | use specific extensions for each file. If     |
|                      | disabled the Gerber file extension is .gbr.   |
+----------------------+-----------------------------------------------+
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint Editor - Managing Libraries {#_footprint_editor_managing_libraries}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::: sect2

### Overview of Footprint Editor {#_overview_of_footprint_editor}

::: paragraph
Pcbnew can simultaneously maintain several libraries. Thus, when a
footprint is loaded, all libraries that appear in the library list are
searched until the first instance of the footprint is found. In what
follows, note that the active library is the library selected within the
Footprint Editor, the program will now be described
:::

::: paragraph
Footprint Editor enables the creation and the editing of footprints:
:::

::: ulist

- Adding and removing pads.

- Changing pad properties (shape, layer) for individual pads or globally
  for all pads of a footprint.

- Editing graphic elements (lines, text).

- Editing information fields (value, reference, etc.).

- Editing the associated documentation (description, keywords).
:::

::: paragraph
Footprint Editor allows the maintenance of the active library as well
by:
:::

::: ulist

- Listing the footprints in the active library.

- Deletion of a footprint from the active library.

- Saving a footprint to the active library.

- Saving all of the footprints contained by a printed circuit.
:::

::: paragraph
It is also possible to create new libraries.
:::

::: paragraph
The library extension is `.mod`.
:::
::::::::::

:::::::: sect2

### Accessing Footprint Editor {#_accessing_footprint_editor}

::: paragraph
The Footprint Editor can be accessed in two different ways:
:::

::: ulist

- Directly, via the icon [![module
  editor](images/icons/module_editor.png)]{.image} in the main toolbar
  of Pcbnew.

- In the edit dialog for the active footprint (see figure below:
  accessed via the context menu), there is the button Footprint Editor.
:::

:::: imageblock
::: content
![Pcbnew module properties](images/Pcbnew_module_properties.png)
:::
::::

::: paragraph
In this case, the active footprint of the board will be loaded
automatically in Footprint Editor, enabling immediate editing or
archiving.
:::
::::::::

:::::: sect2

### Footprint Editor user interface {#_footprint_editor_user_interface}

::: paragraph
By calling Footprint Editor the following window will appear:
:::

:::: imageblock
::: content
![Modedit main window](images/Modedit_main_window.png)
:::
::::
::::::

:::::: sect2

### Top toolbar in Footprint Editor {#_top_toolbar_in_footprint_editor}

:::: imageblock
::: content
![Modedit top toolbar](images/Modedit_top_toolbar.png)
:::
::::

::: paragraph
From this toolbar, the following functions are available:
:::

+-------------------------------------------------------+--------------------------------------------------------+
| [![library](images/icons/library.png)]{.image}        | Select the active library.                             |
+-------------------------------------------------------+--------------------------------------------------------+
| [![save                                               | Save the current footprint to the active library, and  |
| library](images/icons/save_library.png)]{.image}      | write it to disk.                                      |
+-------------------------------------------------------+--------------------------------------------------------+
| [![new                                                | Create a new library and save the current footprint in |
| library](images/icons/new_library.png)]{.image}       | it.                                                    |
+-------------------------------------------------------+--------------------------------------------------------+
| [![modview                                            | Open the Footprint Viewer                              |
| icon](images/icons/modview_icon.png)]{.image}         |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![delete](images/icons/delete.png)]{.image}          | Access a dialog for deleting a footprint from the      |
|                                                       | active library.                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![new                                                | Create a new footprint.                                |
| footprint](images/icons/new_footprint.png)]{.image}   |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Create a footprint using a wizard                      |
| wizard](images/icons/module_wizard.png)]{.image}      |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![load module                                        | Load a footprint from the active library.              |
| lib](images/icons/load_module_lib.png)]{.image}       |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![load module                                        | Load (import) a footprint from the printed circuit     |
| board](images/icons/load_module_board.png)]{.image}   | board.                                                 |
+-------------------------------------------------------+--------------------------------------------------------+
| [![update module                                      | Export the current footprint to the printed circuit    |
| board](images/icons/update_module_board.png)]{.image} | board. when the footprint was previously imported from |
|                                                       | the current board. It will replace the corresponding   |
|                                                       | footprint on the board (i.e., respecting position and  |
|                                                       | orientation).                                          |
+-------------------------------------------------------+--------------------------------------------------------+
| [![insert module                                      | Export the current footprint to the printed circuit    |
| board](images/icons/insert_module_board.png)]{.image} | board. It will be copied on to the printed circuit     |
|                                                       | board at position 0.                                   |
+-------------------------------------------------------+--------------------------------------------------------+
| [![import                                             | Import a footprint from a file created by the Export   |
| module](images/icons/import_module.png)]{.image}      | command.                                               |
+-------------------------------------------------------+--------------------------------------------------------+
| [![export                                             | Export a footprint. This command is essentially        |
| module](images/icons/export_module.png)]{.image}      | identical to that for creating a library, the only     |
|                                                       | difference being that it creates a library in the user |
|                                                       | directory, while creating a library in the standard    |
|                                                       | library directory (usually kicad/modules).             |
+-------------------------------------------------------+--------------------------------------------------------+
| [![undo](images/icons/undo.png)]{.image}              | Undo and Redo                                          |
| [![redo](images/icons/redo.png)]{.image}              |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Invokes the footprint properties dialog.               |
| options](images/icons/module_options.png)]{.image}    |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![print                                              | Call the print dialog.                                 |
| button](images/icons/print_button.png)]{.image}       |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image}        | Standard zoom commands.                                |
| [![zoom out](images/icons/zoom_out.png)]{.image}      |                                                        |
| [![zoom                                               |                                                        |
| redraw](images/icons/zoom_redraw.png)]{.image}        |                                                        |
| [![zoom fit in                                        |                                                        |
| page](images/icons/zoom_fit_in_page.png)]{.image}     |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![options                                            | Call the pad editor.                                   |
| pad](images/icons/options_pad.png)]{.image}           |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Perform a check of footprint correctness               |
| check](images/icons/module_check.png)]{.image}        |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
::::::

:::::: sect2

### Creating a new library {#_creating_a_new_library}

::: paragraph
The creation of a new library is done via the button [![new
library](images/icons/new_library.png)]{.image}, in this case the file
is created by default in the library directory or via the button
[![export module](images/icons/export_module.png)]{.image}, in which
case the file is created by default in your working directory.
:::

::: paragraph
A file-choosing dialog allows the name of the library to be specified
and its directory to be changed. In both cases, the library will contain
the footprint being edited.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | If an old library of the same     |
| Warning                           | name exists, it will be           |
| :::                               | overwritten without warning.      |
+-----------------------------------+-----------------------------------+
:::
::::::

::::: sect2

### Saving a footprint in the active library {#_saving_a_footprint_in_the_active_library}

::: paragraph
The action of saving a footprint (thereby modifying the file of the
active library) is performed using this button [![save
library](images/icons/save_library.png)]{.image}. If a footprint of the
same name already exists, it will be replaced. Since you will depend
upon the accuracy of the library footprints, it is worth double-checking
the footprint before saving.
:::

::: paragraph
It is recommended to edit either the reference or value field text to
the name of the footprint as identified in the library.
:::
:::::

:::::: sect2

### Transferring a footprint from one library to another {#_transferring_a_footprint_from_one_library_to_another}

::: ulist

- Select the source library via the button
  [![library](images/icons/library.png)]{.image}.

- Load the footprint via the button [![load module
  lib](images/icons/load_module_lib.png)]{.image}.

- Select the destination library via the button
  [![library](images/icons/library.png)]{.image}.

- Save the footprint via the button [![save
  library](images/icons/save_library.png)]{.image}
:::

::: paragraph
You may also wish to delete the source footprint.
:::

::: ulist

- Reselect the source library with
  [![library](images/icons/library.png)]{.image}

- Delete the old footprint via the button
  [![delete](images/icons/delete.png)]{.image}
:::
::::::

::::: sect2

### Saving all footprints of your board in the active library {#_saving_all_footprints_of_your_board_in_the_active_library}

::: paragraph
It is possible to copy all of the footprints of a given board design to
the active library. These footprints will keep their current library
names. This command has two uses:
:::

::: ulist

- To create an archive or complete a library with the footprints from a
  board, in the event of the loss of a library.

- More importantly, it facilitates library maintenance by enabling the
  production of documentation for the library, as below.
:::
:::::

:::::::::::: sect2

### Documentation for library footprints {#_documentation_for_library_footprints}

::: paragraph
It is strongly recommended to document the footprints you create, in
order to enable rapid and error-free searching.
:::

::: paragraph
For example, who is able to remember all of the multiple pin-out
variants of a TO92 package? The Footprint Properties dialog offers a
simple solution to this problem.
:::

:::: imageblock
::: content
![Modedit module properties](images/Modedit_module_properties.png)
:::
::::

::: paragraph
This dialog accepts:
:::

::: ulist

- A one-line comment/description.

- Multiple keywords.
:::

::: paragraph
The description is displayed with the component list in Cvpcb and, in
Pcbnew, it is used in the footprint selection dialogs.
:::

::: paragraph
The keywords enable searches to be restricted to those footprints
corresponding to particular keywords.
:::

::: paragraph
When directly loading a footprint (the icon
[![module](images/icons/module.png)]{.image} of the right-hand Pcbnew
toolbar), keywords may be entered in the dialog box. Thus, entering the
text `=CONN` will cause the display of the list of footprints whose
keyword lists contain the word `CONN`.
:::
::::::::::::

:::::::::::::: sect2

### Documenting libraries - recommended practice {#_documenting_libraries_recommended_practice}

::: paragraph
It is recommended to create libraries indirectly, by creating one or
more auxiliary circuit boards that constitute the source of (part of)
the library, as follows: Create a circuit board in A4 format, in order
to be able to print easily to scale (scale = 1).
:::

::: paragraph
Create the footprints that the library will contain on this circuit
board. The library itself will be created with the File/Archive
footprints/Create footprint archive command.
:::

:::: imageblock
::: content
![Pcbnew archive footprints
menu](images/Pcbnew_archive_footprints_menu.png)
:::
::::

::: paragraph
The \"true source\" of the library will thus be the auxiliary circuit
board, and it is on this circuit that any subsequent alterations of
footprints will be made. Naturally, several circuit boards can be saved
in the same library.
:::

::: paragraph
It is generally a good idea to make different libraries for different
kinds of components (connectors, discretes,...​), since Pcbnew is able to
search many libraries when loading footprints.
:::

::: paragraph
Here is an example of such a library source:
:::

:::: imageblock
::: content
![Pcbnew example library](images/Pcbnew_example_library.png)
:::
::::

::: paragraph
This technique has several advantages:
:::

::: ulist

- The circuit can be printed to scale and serve as documentation for the
  library with no further effort.

- Future changes of Pcbnew may require regeneration of the libraries,
  something that can be done very quickly if circuit-board sources of
  this type have been used. This is important, because the circuit board
  file formats are guaranteed to remain compatible during future
  development, but this is not the case for the library file format.
:::
::::::::::::::

:::::: sect2

### Footprint Libraries Management {#_footprint_libraries_management}

::: paragraph
The list of footprint libraries in Pcbnew can be edited using the
Footprint Libraries Manager. This allows you to add and remove footprint
libraries by hand, and also allows you to invoke the Footprint Libraries
Wizard by pressing the \"Append With Wizard\" button.
:::

::: paragraph
The Footprint Libraries Wizard can also be invoked through the
Preferences menu, and can automatically add a library (detecting its
type) from a file or from a Github URL. The URL for the official
libraries is:
[https://github.com/KiCad](https://github.com/KiCad){.bare}
:::

::: paragraph
More details about footprint library tables and the Manager and Wizard
can be found in the CvPcb Reference Manual in the section *Footprint
Library Tables*.
:::
::::::

:::: sect2

### 3D Shapes Libraries Management {#_3d_shapes_libraries_management}

::: paragraph
The 3D shape libraries can be downloaded by 3D Shape Libraries Wizard.
It can be invoked from the menu Preferences → 3D Shapes Libraries
Downloader.
:::
::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint Editor - Creating and Editing Footprints {#_footprint_editor_creating_and_editing_footprints}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2

### Footprint Editor Overview {#_footprint_editor_overview}

::: paragraph
The footprint editor is used for editing and creating PCB footprints.
This includes:
:::

::: ulist

- Adding and removing pads.

- Changing pad properties (shape, layer), for individual pads or for all
  the pads in a footprint.

- Adding and editing graphic elements (contours, text).

- Editing fields (value, reference, etc.).

- Editing the associated documentation (description, keywords).
:::
:::::

::::::::::::: sect2

### Footprint Elements {#_footprint_elements}

::: paragraph
A footprint is the physical representation (footprint) of the part to be
inserted in the PCB and it must be linked to the relative component in
your schematic. Each footprint includes three different elements:
:::

::: ulist

- The pads.

- Graphical contours and text.

- Fields.
:::

::: paragraph
In addition, a number of other parameters must be correctly defined if
the auto-placement function will be used. The same holds for the
generation of auto-insertion files.
:::

::::: sect3

#### Pads {#_pads}

::: paragraph
Two pad properties are important:
:::

::: ulist

- Geometry (shape, layers, drill holes).

- The pad number, which is constituted by up to four alphanumeric
  characters. Thus, the following are all valid pad numbers: 1, 45 and
  9999, but also AA56 and ANOD. The pad number must be identical to that
  of the corresponding pin number in the schematic, because it defines
  the matching pin and pad numbers that Pcbnew links pins and pads with.
:::
:::::

:::: sect3

#### Contours {#_contours}

::: paragraph
Graphical contours are used to draw the physical shape of the footprint.
Several different types of contour are available: lines, circles, arcs,
and text. Contours have no electrical significance, they are simply
graphical aids.
:::
::::

:::: sect3

#### Fields {#_fields}

::: paragraph
These are text elements associated with a footprint. Two are obligatory
and always present: the reference field and the value field. These are
automatically read and updated by Pcbnew when a netlist is read during
the loading of footprints into your board. The reference is replaced by
the appropriate schematic reference (U1, IC3, etc.). The value is
replaced by the value of the corresponding part in the schematic (47K,
74LS02, etc.). Other fields can be added and these will behave like
graphical text.
:::
::::
:::::::::::::

::::: sect2

### Starting Footprint Editor and Selecting a Footprint to Edit {#_starting_footprint_editor_and_selecting_a_footprint_to_edit}

::: paragraph
Footprint Editor can be started in two ways:
:::

::: ulist

- Directly via the [![module
  editor](images/icons/module_editor.png)]{.image} icon from the main
  toolbar of Pcbnew. This allows the creation or modification of a
  footprint in the library.

- Double-clicking a footprint will launch the \'Footprint Properties\'
  menu, which offers a \'Go to Footprint Editor\' button. If this option
  is used, the footprint from the board will be loaded into the editor,
  for modification or for saving.
:::
:::::

:::::::::::: sect2

### Footprint Editor Toolbars {#_footprint_editor_toolbars}

::: paragraph
Calling Footprint Editor will launch a new window that looks like this:
:::

:::: imageblock
::: content
![Modedit main window](images/Modedit_main_window.png)
:::
::::

:::::: sect3

#### Edit Toolbar (right-hand side) {#_edit_toolbar_right_hand_side}

::: paragraph
This toolbar contains tools for:
:::

::: ulist

- Placing pads.

- Adding graphic elements (contours, text).

- Positioning the anchor.

- Deleting elements.
:::

::: paragraph
The specific functions are the following:
:::

+---------------------------------------------------+--------------------------------------------------------+
| [![cursor](images/icons/cursor.png)]{.image}      | No tool.                                               |
+---------------------------------------------------+--------------------------------------------------------+
| [![pad](images/icons/pad.png)]{.image}            | Add pads.                                              |
+---------------------------------------------------+--------------------------------------------------------+
| [![add                                            | Draw line segments and polygons.                       |
| polygon](images/icons/add_polygon.png)]{.image}   |                                                        |
+---------------------------------------------------+--------------------------------------------------------+
| [![add                                            | Draw circles.                                          |
| circle](images/icons/add_circle.png)]{.image}     |                                                        |
+---------------------------------------------------+--------------------------------------------------------+
| [![add arc](images/icons/add_arc.png)]{.image}    | Draw circular arcs.                                    |
+---------------------------------------------------+--------------------------------------------------------+
| [![text](images/icons/text.png)]{.image}          | Add graphical text (fields are not managed by this     |
|                                                   | tool).                                                 |
+---------------------------------------------------+--------------------------------------------------------+
| [![anchor](images/icons/anchor.png)]{.image}      | Position the footprint anchor.                         |
+---------------------------------------------------+--------------------------------------------------------+
| [![delete](images/icons/delete.png)]{.image}      | Delete elements.                                       |
+---------------------------------------------------+--------------------------------------------------------+
| [![grid select                                    | Grid origin. (grid offset). Useful for placement of    |
| axis](images/icons/grid_select_axis.png)]{.image} | pads. The grid origin can be put on a given location   |
|                                                   | (the first pad to place), and after the grid size can  |
|                                                   | be set to the pad pitch. Placing pads is therefore     |
|                                                   | very easy                                              |
+---------------------------------------------------+--------------------------------------------------------+
::::::

:::: sect3

#### Display Toolbar (left-hand side) {#_display_toolbar_left_hand_side}

::: paragraph
These tools manage the display options in Footprint Editor:
:::

+------------------------------------------------+--------------------------------------------------------+
| [![grid](images/icons/grid.png)]{.image}       | Display the grid.                                      |
+------------------------------------------------+--------------------------------------------------------+
| [![polar                                       | Display polar coordinates.                             |
| coord](images/icons/polar_coord.png)]{.image}  |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![unit mm](images/icons/unit_mm.png)]{.image} | Use units of mm or inch                                |
| [![unit                                        |                                                        |
| inch](images/icons/unit_inch.png)]{.image}     |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![cursor                                      | Toggle cursor crosshair shape                          |
| shape](images/icons/cursor_shape.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![pad                                         | Display pad in outline mode.                           |
| sketch](images/icons/pad_sketch.png)]{.image}  |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![text                                        | Display text in outline mode.                          |
| sketch](images/icons/text_sketch.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![show mod                                    | Display contours in outline mode.                      |
| edge](images/icons/show_mod_edge.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![contrast                                    | Toggle high-contrast mode                              |
| mode](images/icons/contrast_mode.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
::::
::::::::::::

::::::::::::: sect2

### Context Menus {#_context_menus}

::: paragraph
The right mouse button calls up menus that depend upon the element
beneath the cursor.
:::

::: paragraph
The context menu for editing footprint parameters:
:::

:::: imageblock
::: content
![Modedit context menu module
parameters](images/Modedit_context_menu_module_parameters.png)
:::
::::

::: paragraph
The context menu for editing pads:
:::

:::: imageblock
::: content
![Modedit context menu pads](images/Modedit_context_menu_pads.png)
:::
::::

::: paragraph
The context menu for editing graphic elements:
:::

:::: imageblock
::: content
![Modedit context menu
graphics](images/Modedit_context_menu_graphics.png)
:::
::::
:::::::::::::

::::::: sect2

### Footprint Properties Dialog {#_footprint_properties_dialog}

::: paragraph
This dialog can be launched when the cursor is over a footprint by
clicking on the right mouse button and then selecting \'Edit
Footprint\'.
:::

:::: imageblock
::: content
![Modedit module properties
dialog](images/Modedit_module_properties_dialog.png)
:::
::::

::: paragraph
The dialog can be used to define the main footprint parameters.
:::
:::::::

:::::::::: sect2

### Creating a New Footprint {#_creating_a_new_footprint}

::: paragraph
A new footprint can be created via the button [![new
footprint](images/icons/new_footprint.png)]{.image}. The name of the new
footprint will be requested. This will be the name by which the
footprint will be identified in the library.
:::

::: paragraph
This text also serves as the footprint value, which is ultimately
replaced by the real value (100 µF_16 V, 100 Ω_0.5 W, ...​).
:::

::: paragraph
The new footprint will require:
:::

::: ulist

- Contours (and possibly graphic text).

- Pads.

- A value (hidden text that is replaced by the true value when used).
:::

::: paragraph
Alternative method:
:::

::: paragraph
When a new footprint is similar to an existing footprint in a library or
a circuit board, an alternative and quicker method of creating the new
footprint is as follows:
:::

::: ulist

- Load the similar footprint ([![load module
  lib](images/icons/load_module_lib.png)]{.image}, [![load module
  board](images/icons/load_module_board.png)]{.image} or [![import
  module](images/icons/import_module.png)]{.image}).

- Modify the \"Footprint Name in Library\" field in order to generate a
  new identifier (name).

- Edit and save the new footprint.
:::
::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Adding and Editing Pads {#_adding_and_editing_pads}

::: paragraph
Once a footprint has been created, pads can be added, deleted or
modified. Modification of pads can be local, affecting only the pad
under the cursor, or global, affecting all pads of the footprint.
:::

::::: sect3

#### Adding Pads {#_adding_pads}

::: paragraph
Select the [![pad](images/icons/pad.png)]{.image} icon from the right
hand toolbar. Pads can be added by clicking in the desired position with
the left mouse button. Pad properties are predefined in the pad
properties menu.
:::

::: paragraph
Do not forget to enter the pad number.
:::
:::::

:::::::::::::::::::::::::::: sect3

#### Setting Pad Properties {#_setting_pad_properties}

::: paragraph
This can be done in three different ways:
:::

::: ulist

- Selecting the [![options pad](images/icons/options_pad.png)]{.image}
  icon from the horizontal toolbar.

- Clicking on an existing pad and selecting \'Edit Pad\'. The pad's
  settings can then be edited.

- Clicking on an existing pad and selecting \'Export Pad Settings\'. In
  this case, the geometrical properties of the selected pad will become
  the default pad properties.
:::

::: paragraph
In the first two cases, the following dialog window will be displayed:
:::

:::: imageblock
::: content
![Modedit pad properties
dialog](images/Modedit_pad_properties_dialog.png)
:::
::::

::: paragraph
Care should be taken to define correctly the layers to which the pad
will belong. In particular, although copper layers are easy to define,
the management of non-copper layers (solder mask, solder pads...​) is
equally important for circuit manufacture and documentation.
:::

::: paragraph
The Pad Type selector triggers an automatic selection of layers that is
generally sufficient.
:::

:::: sect4

##### Rectangular Pads {#_rectangular_pads}

::: paragraph
For SMD footprints of the VQFP/PQFP type which have rectangular pads on
all four sides (both horizontal and vertical) it is recommended to use
just one shape (for example, a horizontal rectangle) and to place it
with different orientations (0 for horizontal and 90 degrees for
vertical). Global resizing of pads can then be done in a single
operation.
:::
::::

:::: sect4

##### Rotate Pads {#_rotate_pads}

::: paragraph
Rotations of -90 or -180 are only required for trapezoidal pads used in
microwave footprints.
:::
::::

:::::::: sect4

##### Non-plated Through Hole Pads {#_non_plated_through_hole_pads}

::: paragraph
Pads can be defined as Non-Plated Through Hole pads (NPTH pads).
:::

::: paragraph
These pads must be defined on one or all copper layers (obviously, the
hole exists on all copper layers).
:::

::: paragraph
This requirement allows you to define specific clearance parameters (
for instance clearance for a screw).
:::

::: paragraph
When the pad hole size is the same as the pad size, for a round or oval
pad, this pad is NOT plotted on copper layers in GERBER files.
:::

::: paragraph
These pads are used for mechanical purposes, therefore no pad name or
net name is allowed. A connection to a net is not possible.
:::
::::::::

:::::: sect4

##### Offset Parameter {#_offset_parameter}

::: paragraph
Pad 3 has an offset Y = 15 mils:
:::

:::: imageblock
::: content
![Modedit pad offset example](images/Modedit_pad_offset_example.png)
:::
::::
::::::

:::::: sect4

##### Delta Parameter (trapezoidal pads) {#_delta_parameter_trapezoidal_pads}

::: paragraph
Pad 1 has its parameter Delta X = 10 mils
:::

:::: imageblock
::: content
![Modedit pad delta example](images/Modedit_pad_delta_example.png)
:::
::::
::::::
::::::::::::::::::::::::::::

:::::::::: sect3

#### Setting Clearances for Solder Mask and Solder Paste Layers {#_setting_clearances_for_solder_mask_and_solder_paste_layers}

::: paragraph
When defining pads containing copper layers, KiCad creates solder mask
and solder paste layers based on a fixed clearance and/or a ratio of the
pad geometry. The non-zero settings used to calculate the final pad size
is based on the following order of precedence:
:::

::: ulist

- Pad setting

- Footprint setting

- Global setting
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | The solder mask pad shape is      |
| :::                               | usually bigger than the pad       |
|                                   | itself. So the clearance value is |
|                                   | positive. The solder paste mask   |
|                                   | pad shape is usually smaller than |
|                                   | the pad itself. So the clearance  |
|                                   | value is negative.                |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

:::::: sect4

##### Solder Paste Settings {#_solder_paste_settings}

::: paragraph
Two settings are used to calculate the solder paste aperture:
:::

::: ulist

- A fixed clearance setting.

- A percentage of the pad size.
:::

::: paragraph
The the final value is the product of the ratio setting and the
clearance setting.
:::
::::::
::::::::::

::::::::::: sect3

#### Pads Not on Copper Layers {#_pads_not_on_copper_layers}

::: paragraph
There is second method for creating pads that do not have any copper
layers defined. These pads are commonly referred to as aperture pads and
can be use to create custom apertures not based on the outline of a
copper pad geometry. This method was introduced in version 5.0.0-rc2.
Pads defined without any copper layers ignore the global and footprint
level settings and only use the pad level settings.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Warning                           | Pads without copper layers        |
| :::                               | defined prior to version          |
|                                   | 5.0.0-rc2 were plotted using      |
|                                   | precedence defined above with the |
|                                   | global and footprint settings.    |
|                                   | Adjustments will have to be made  |
|                                   | for any boards designed prior to  |
|                                   | this version in order to achieve  |
|                                   | the same output plots.            |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
Footprint level settings:
:::

:::: imageblock
::: content
![Modedit footprint level pad
settings](images/Modedit_footprint_level_pad_settings.png)
:::
::::

::: paragraph
Pad level settings:
:::

:::: imageblock
::: content
![Modedit pad level pad
settings](images/Modedit_pad_level_pad_settings.png)
:::
::::
:::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

::::::: sect2

### Fields Properties {#_fields_properties}

::: paragraph
There are at least two fields: reference and value.
:::

::: paragraph
Their parameters (attribute, size, width) must be updated. You can
access the dialog box from the pop-up menu, by double clicking on the
field, or by the footprint properties dialog box:
:::

:::: imageblock
::: content
![Modedit footprint text
properties](images/Modedit_footprint_text_properties.png)
:::
::::
:::::::

::::::::: sect2

### Automatic Placement of a Footprint {#_automatic_placement_of_a_footprint}

::: paragraph
If the user wishes to exploit the full capabilities of the
auto-placement functions, it is necessary to define the allowed
orientations of the footprint (Footprint Properties dialog).
:::

:::: imageblock
::: content
![Modedit module autoplace
settings](images/Modedit_module_autoplace_settings.png)
:::
::::

::: paragraph
Usually, rotation of 180 degrees is permitted for resistors,
non-polarized capacitors and other symmetrical elements.
:::

::: paragraph
Some footprints (small transistors, for example) are often permitted to
rotate by +/- 90 or 180 degrees. By default, a new footprint will have
its rotation permissions set to zero. This can be adjusted according to
the following rule:
:::

::: paragraph
A value of 0 makes rotation impossible, 10 allows it completely, and any
intermediate value represents a limited rotation. For example, a
resistor might have a permission of 10 to rotate 180 degrees
(unrestrained) and a permission of 5 for a +/- 90 degree rotation
(allowed, but discouraged).
:::
:::::::::

::::::: sect2

### Attributes {#_attributes}

::: paragraph
The attributes window is the following:
:::

:::: imageblock
::: content
![Modedit module attributes](images/Modedit_module_attributes.png)
:::
::::

::: ulist

- Normal is the standard attribute.

- Normal+Insert indicates that the footprint must appear in the
  automatic insertion file (for automatic insertion machines). This
  attribute is most useful for surface mount components (SMDs).

- Virtual indicates that a component is directly formed by the circuit
  board. Examples would be edge connectors or inductors created by a
  particular track shape (as sometimes seen in microwave footprints).
:::
:::::::

::::::::::: sect2

### Documenting Footprints in a Library {#_documenting_footprints_in_a_library}

::: paragraph
It is strongly recommended to document newly created footprints, in
order to facilitate their rapid and accurate retrieval. Who is able to
recall the multiple pin-out variants of a TO92 footprint?
:::

::: paragraph
The Footprint Properties dialog offers a simple and yet powerful means
for documentation generation.
:::

:::: imageblock
::: content
![Modedit module properties documentation
fields](images/Modedit_module_properties_documentation_fields.png)
:::
::::

::: paragraph
This menu allows:
:::

::: ulist

- The entry of a comment line (description).

- Multiple keywords.
:::

::: paragraph
The comment line is displayed with the component list in CvPcb and in
the footprint selection menus in Pcbnew. The keywords can be used to
restrict searches to those parts possessing the given keywords.
:::

::: paragraph
Thus, while using the load footprint command (icon in the right-hand
toolbar in Pcbnew), it is possible to type the text `=TO220` into the
dialog box to have Pcbnew display a list of the footprints possessing
the keyword `TO220`
:::
:::::::::::

:::::::::::::::::::::::::::: sect2

### 3-Dimensional Visualization {#_3_dimensional_visualization}

::: paragraph
A footprint may be associated with a file containing a three-dimensional
representation of the component. In order to associate a footprint with
a model file, select the *3D Settings* tab as shown below.
:::

::::: {#img-Modedit_module_3d_options .imageblock}

::: content
![Modedit module 3d options](images/Modedit_module_3d_options.png)
:::

::: title
Figure 1. 3D Model selection interface
:::
:::::

::: paragraph
The buttons on the right have the following functions:
:::

::: ulist

- **Add 3D Shape** shows a 3D file selection dialog and creates a new
  model entry for the component.

- **Remove 3D Shape** deletes the selected model entry.

- **Edit Filename** shows a text editor for manual entry of the model
  file name.

- **Configure Paths** shows a configuration dialog which allows the user
  to edit the list of path aliases and alias values.
:::

::: paragraph
The *3D Settings* tab contains a panel with a preview of the selected
model and the scale, offset, and rotation data for the model.
:::

::: paragraph
Scale values are useful for visualization formats such as VRML1, VRML2,
and X3D. Since the model may have been produced by any number of
VRML/X3D editors or exporters and VRML does not enforce a unit of length
for the models, users can enter an appropriate scale value to ensure
that the model appears as it should within the 3DViewer. Some users
employ a simple VRML box as a generic model for components and select
scale values so that the box has the correct size to represent the
component. For Mechanical CAD (MCAD) models the scale values should be
left at unity. MCAD formats always specify a unit length and any
exporters which make use of MCAD data formats will ignore the scale
values. However the 3DViewer will always apply the scale values; if
scale values other than unity are used with MCAD models, the output of
the 3DViewer will differ from any exported MCAD models such as IDF.
:::

::: paragraph
Offset and Rotation values are typically required to align a 3D model
with a footprint. Due to differences in 3D modeling software as well as
differences in how users construct a model, in the vast majority of
cases it is necessary for users to enter Offset and Rotation values to
achieve the desired positioning of a 3D model. The Rotation values are
given in degrees and are applied successively in the order ZYX; the
convention used is that a positive angle results in a clockwise rotation
of the part when viewing from the positive position of the axis towards
the origin.
:::

::: paragraph
KiCad supports 3D model formats via a plugin system and support is
provided for the visual model formats VRML1, VRML2, and X3D as well as
the MCAD format IDF. The MCAD formats IGES and STEP are supported via
the OCE Plugin which requires a suitable version of the OpenCascade or
OpenCascade Community Edition (OCE) software.
:::

::::::::::::::::: sect3

#### 3D Model Paths {#_3d_model_paths}

::: paragraph
In the past KiCad used a fixed path to a directory of 3D models and
later relied on the *KISYS3DMOD* environment variable to specify the
location of the model directory. Other base directories for models could
be specified by using additional environment variables. The current
version of KiCad has a specialized *alias* system for handling 3D model
names. The aim of the new file name management system (filename
resolution system) is to provide a scheme which is compatible with
earlier versions of KiCad while offering a more flexible mechanism for
specifying 3D model file names and improving the ability to share
project files.
:::

::: paragraph
Due to the requirement to support previous schemes while offering a
flexible new scheme for finding 3D models, there are two distinct
methods for specifying base search paths for 3D models.
:::

::: paragraph
In order to maintain the legibility of the *kicad_pcb* and *pretty* data
files, KiCad prefers to use filenames which have been shortened via the
use of environment variables (old method) or aliases (new method). Since
setting environment variables can be cumbersome especially on GUI-based
operating systems, the environment variable scheme for supporting model
search paths has been extended to make use of KiCad's existing
internally defined *Path Configuration* dialog. This dialog is available
via the *Preferences→Configure Paths* menu and is shown below. Setting
additional paths within this dialog will extend the search paths used to
find 3D model files. The dialog does not actually set environment
variables but the filename resolution system acts as if it does; in
cases where an actual environment variable with the same name is
defined, the environment variable's value overrides any internally
defined values. File names relative to these defined variables begin
with *\${MY_ENV_VAR}* where *MY_ENV_VAR* is a variable defined via the
*Path Configuration* dialog or an actual environment variable.
:::

::::: {#img-Modedit_internal_path_config .imageblock}

::: content
![Modedit internal path config](images/Modedit_internal_path_config.png)
:::

::: title
Figure 2. KiCad Path Configuration dialog
:::
:::::

::: paragraph
The newer scheme to support shortened file names is the *alias* system.
In this system a path begins with the string *:my alias:* where *my
alias* is a text string which is preferably chosen to be short while
also being significant to the user; for example an alias to a directory
containing the official KiCad models may have an alias *Official Models*
while your personal model collection may have an alias *My Models*. The
aliases may be set up by clicking on the **Configure Paths** button
within the **3D Settings** tab shown previously. The alias configuration
dialog is shown below.
:::

::::: {#img-Modedit_alias_path_config .imageblock}

::: content
![Modedit alias path config](images/Modedit_alias_path_config.png)
:::

::: title
Figure 3. KiCad Alias Configuration dialog
:::
:::::

::: paragraph
3D model files can be selected by clicking **Add 3D Shape** to display
the 3D Model Browser shown below. The model browser provides a 3D
preview, file filter, and a drop-down path selector which contains the
current list of search paths defined via environment variables or
aliases. Depending on the model size and complexity it may take a few
seconds for a model to be displayed when it is selected. In an extreme
case a BGA package model which was used during testing took around 12
seconds to display.
:::

::::: {#img-Modedit_3D_file_browser .imageblock}

::: content
![Modedit 3D file browser](images/Modedit_3D_file_browser.png)
:::

::: title
Figure 4. KiCad 3D File Browser
:::
:::::
:::::::::::::::::
::::::::::::::::::::::::::::

:::::: sect2

### Saving a Footprint into the Active Library {#_saving_a_footprint_into_the_active_library}

::: paragraph
The save command (modification of the file of the active library) is
activated by the [![save
library](images/icons/save_library.png)]{.image} button.
:::

::: paragraph
If a footprint of the same name exists (an older version), it will be
overwritten. Because it is important to be able to have confidence in
the library footprints, it is worth double-checking the footprint for
errors before saving.
:::

::: paragraph
Before saving, it is also recommended to change the reference or value
of the footprint to be equal to the library name of the footprint.
:::
::::::

:::: sect2

### Saving a footprint to the board {#_saving_a_footprint_to_the_board}

::: paragraph
If the edited footprint comes from the current board, the button
[![update module board](images/icons/update_module_board.png)]{.image}
will update this footprint on the board.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Advanced PCB editing tools {#_advanced_pcb_editing_tools}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
There are some more advanced editing tools available in Pcbnew and
Footprint Editor, which can help you to efficiently lay out components
on the canvas.
:::

::::: sect2

### Duplicating items {#_duplicating_items}

::: paragraph
Duplication is a method to clone an item and pick it up in the same
action. It is broadly similar to copy-and-pasting, but it allows you to
\"sprinkle\" components over the PCB and it allows you to manually lay
out components using the \"Move Exact\" tool (see below) more easily.
:::

::: paragraph
Duplication is done by using the hotkey (which defaults to Ctrl-D) or
the duplicate item option in the context menu, icon
[![duplicate](images/icons/duplicate.png)]{.image}.
:::
:::::

:::::::::::::: sect2

### Moving items exactly {#_moving_items_exactly}

::: paragraph
The \"Move Exact\" tool allows you to move an item (or group of items)
by a certain amount, which can be entered in Cartesian or polar formats
and which can be entered in any supported units. This is useful when it
would otherwise be cumbersome to switch to a different grid, or when a
feature is not spaced according to any existing grids.
:::

::: paragraph
To use this tool, select the items you wish to move and then use either
the hotkey (defaults to Ctrl-M) or the context menu items to invoke the
dialog. You can also invoke the dialog with the hotkey when moving or
duplicating items, which can make it easy to repeatedly apply an offset
to multiple components.
:::

::: paragraph
Move exact with Cartesian move vector entry
:::

:::: imageblock
::: content
![Pcbnew move exact cartesian](images/Pcbnew_move_exact_cartesian.png)
:::
::::

::: paragraph
Move exact with polar move vector entry
:::

:::: imageblock
::: content
![Pcbnew move exact polar](images/Pcbnew_move_exact_polar.png)
:::
::::

::: paragraph
The checkbox allows you to switch between Cartesian and polar
co-ordinate systems. Whatever is currently in the form will be converted
automatically to the other system.
:::

::: paragraph
Then you enter the desired move vector. You can use the units indicated
by the labels (\"mm\" in the images above) or you can specify the units
yourself (e.g. \"1 in\" for an inch, or \"2 rad\" for 2 radians).
:::

::: paragraph
Pressing OK will apply the translation to the selection, and cancel will
close the dialog and the items will not be moved. If OK is pressed, the
move vector will be saved and pre-filled next time the dialog is opened,
which allows repeated application of the same vector to multiple
objects.
:::
::::::::::::::

:::::::::::::::::::::::::::::::::::: sect2

### Array tools {#_array_tools}

::: paragraph
Pcbnew and the Footprint Editor both have assistants for creating arrays
of features and components, which can be used to easily and accurately
lay out repetitive elements on PCBs and in footprints.
:::

:::::: sect3

#### Activating the array tool {#_activating_the_array_tool}

::: paragraph
The array tool acts on the component under the cursor, or, in GAL mode,
on a selection. It can be accessed either via the context menu, icon
[![array](images/icons/array.png)]{.image} for the selection or by a
keyboard shortcut (defaults to Ctrl-N).
:::

::: paragraph
The array tool is presented as a dialog window, with a pane for the
types of arrays. There are two types of arrays supported so far: grid,
and circular.
:::

::: paragraph
Each type of array can be fully specified on the respective panes.
Geometric options (how the grid is laid out) go on the left; numbering
options (including how the numbers progress across the grid) on the
right.
:::
::::::

:::::::::::::::::::::: sect3

#### Grid arrays {#_grid_arrays}

::: paragraph
Grid arrays are arrays that lay components out according to a
2-dimensional square grid. This kind of array can also produce a linear
array by only laying out a single row or column.
:::

::: paragraph
The settings dialog for grid arrays look like this:
:::

:::: imageblock
::: content
![Pcbnew array dialog grid](images/Pcbnew_array_dialog_grid.png)
:::
::::

::::::::::::::: sect4

##### Geometric options {#_geometric_options}

::: paragraph
The geometric options are as follow:
:::

::: ulist

- **Horizontal count**: the number of \"columns\" in the grid.

- **Vertical count**: the number of \"rows\" in the grid.

- **Horizontal spacing**: the horizontal distance from item to the item
  in the same row and next column. If this is negative, the grid
  progresses from right to left.

- **Vertical spacing**: the vertical distance from one item to the item
  in the same column and the next row. If this is negative, the grid
  progress bottom to top.

- **Horizontal offset**: start each row this distance to the right of
  the previous one

- **Vertical offset**: start each column this distance below the
  previous one
:::

::::: imageblock
::: content
![Pcbnew array grid offsets](images/Pcbnew_array_grid_offsets.png)
:::

::: title
Figure 5. 3x3 grid with x and y offsets
:::
:::::

::: ulist

- **Stagger**: add an offset to every set of \"n\" rows/columns, with
  each row progressing by 1/n'th of the relevant spacing dimension:
:::

::::: imageblock
::: content
![Pcbnew array grid stagger rows
2](images/Pcbnew_array_grid_stagger_rows_2.png)
:::

::: title
Figure 6. 3x3 grid with a row stagger of 2
:::
:::::

::::: imageblock
::: content
![Pcbnew array grid stagger cols
3](images/Pcbnew_array_grid_stagger_cols_3.png)
:::

::: title
Figure 7. 4x3 grid with a column stagger of 3
:::
:::::
:::::::::::::::

:::: sect4

##### Numbering options {#_numbering_options}

::: ulist

- **Numbering Direction**: Determines whether numbers proceed along rows
  and then moves to the next row, or down columns and then to the next
  column. Note that the direction on numbering is defined by the sign of
  the spacing: a negative spacing will result in right-to-left or
  bottom-to-top numbering.

- **Reverse numbering on alternate rows or columns**: If selected, the
  numbering order (left-to-right or right-to-left, for example) on
  alternate rows or columns. Whether rows or columns alternate depends
  on the numbering direction. This option is useful for packages like
  DIPs where the numbering proceeds up one side and down the other.

- **Restart numbering**: if laying out using items that already have
  numbers, reset to the start, otherwise continue if possible from this
  item's number

- **Numbering Scheme**

  ::: ulist

  - **Continuous**: the numbering just continues across a row/column
    break - if the last item in the first row is numbered \"7\", the
    first item in the second row will be \"8\".

  - **Coordinate**: the numbering uses a two-axis scheme where the
    number is made up of the row and column index. Which one comes first
    (row or column) is determined by the numbering direction.
  :::

- **Axis numberings**: what \"alphabet\" to use to number the axes.
  Choices are

  ::: ulist

  - **Numerals** for normal integer indices

  - **Hexadecimal** for base-16 indexing

  - **Alphabetic, minus IOSQXZ**, a common scheme for electronic
    components, recommended by ASME Y14.35M-1997 sec. 5.2 (previously
    MIL-STD-100 sec. 406.5) to avoid confusion with numerals.

  - **Full alphabet** from A-Z.
  :::
:::
::::
::::::::::::::::::::::

:::::::::: sect3

#### Circular arrays {#_circular_arrays}

::: paragraph
Circular arrays lay out items around a circle or a circular arc. The
circle is defined by the location of the selection (or the centre of a
selected group) and a centre point that is specified. Below is the
circular array configuration dialog:
:::

:::: imageblock
::: content
![Pcbnew array dialog circular](images/Pcbnew_array_dialog_circular.png)
:::
::::

:::: sect4

##### Geometric options {#_geometric_options_2}

::: ulist

- **Horizontal center**, **Vertical center**: The centre of the circle.
  The radius field below will update automatically when you adjust
  these.

- **Angle**: The angular difference between two adjacent items in the
  array. Set this to zero to evenly divide the circle with \"count\"
  elements.

- **Count**: Number of items in the array (including the original item)

- **Rotate**: Rotate each item around its own location. Otherwise, the
  item will be translated but not rotated (for example, a square pad
  will always remain upright if this option is not set).
:::
::::

:::: sect4

##### Numbering options {#_numbering_options_2}

::: paragraph
Circular arrays have only one dimension and a simpler geometry than
grids. The meanings of the available options are the same as for grids.
Items are numbered clockwise - for an anticlockwise array, specify a
negative angle.
:::
::::
::::::::::
::::::::::::::::::::::::::::::::::::

::::::: sect2

### Measurement (ruler) tool {#_measurement_ruler_tool}

::: paragraph
The measurement tool is a linear ruler that can be used to visually
check sizes and spacings on a PCB.
:::

::: paragraph
It is accessible via the calipers icon
[![measurement](images/icons/measurement.png)]{.image} in the right hand
toolbar, in the \"Dimension\" menu and with the hotkey (Ctrl-Shift-M by
default).
:::

::: paragraph
When active, you can draw a temporary ruler over the canvas, which will
be marked with the current units. You can snap to 45-degree angles by
holding the Ctrl key. Units can be changed without leaving the tool
using the ususal hotkey (Ctrl-U by default).
:::

::: paragraph
[![Pcbnew measurement tool](images/Pcbnew_measurement_tool.png)]{.image}
:::
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## KiCad Scripting Reference {#_kicad_scripting_reference}

::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Scripting allows you to automate tasks within KiCad using the
[Python](https://www.python.org/) language.
:::

::: paragraph
Also see the doxygen documentation on [Python Scripting
Reference](http://docs.kicad-pcb.org/doxygen-python/namespaces.html).
:::

::: paragraph
You can see python module help by typing `pydoc pcbnew` on your
terminal.
:::

::: paragraph
Using scripting you can create:
:::

::: ulist

- **Plugins**: this type of script is loaded when KiCad starts.
  Examples:

  ::: ulist

  - **Footprint Wizards**: To help you build footprints easily filling
    in parameters. See the dedicated section [Footprint
    Wizards](#Footprint_Wizards) below.

  - **File I/O** \'(planned)\': To let you write plugins to
    export/import other filetypes

  - **Actions** \'(experimental)\': Associate events to scripting
    actions or register new menus or toolbar icons.
  :::

- **Command Line Scripts**: scripts that can be used from the command
  line, load boards or libraries, modify them, and render outputs or new
  boards.
:::

::: paragraph
It shall be noted that the only KiCad application that supports
scripting is Pcbnew. It is also planned for Eeschema in the future.
:::

::::: sect2

### KiCad Objects {#_kicad_objects}

::: paragraph
The scripting API reflects the internal object structure inside
KiCad/pcbnew. BOARD is the main object, that has a set of properties and
a set of MODULEs, and TRACKs/VIAs, TEXTE_PCB, DIMENSION, DRAWSEGMENT.
Then MODULEs have D_PADs, EDGEs, etc.
:::

::: ulist

- See the BOARD section below.
:::
:::::

:::: sect2

### Basic API Reference {#_basic_api_reference}

::: paragraph
All the pcbnew API is provided from the \"pcbnew\" module in Python.
GetBoard() method will return the current pcb open at editor, useful for
commands written from the integrated scripting shell inside pcbnew or
action plugins.
:::
::::

::::::: sect2

### Loading and Saving a Board {#_loading_and_saving_a_board}

::: ulist

- **LoadBoard(filename):** loads a board from file returning a BOARD
  object, using the file format that matches the filename extension.

- **SaveBoard(filename,board):** saves a BOARD object to file, using the
  file format that matches the filename extension.

- **board.Save(filename):** same as above, but it's a method of BOARD
  object.
:::

::::: listingblock
::: title
Example that loads a board, hides all values, shows all references
:::

::: content

```python

#!/usr/bin/env python2.7
import sys
from pcbnew import *

filename=sys.argv[1]

pcb = LoadBoard(filename)
for module in pcb.GetModules():
    print "* Module: %s"%module.GetReference()
    module.Value().SetVisible(False)      # set Value as Hidden
    module.Reference().SetVisible(True)   # set Reference as Visible

pcb.Save("mod_"+filename)

```

:::
:::::
:::::::

:::::: sect2

### Listing and Loading Libraries {#_listing_and_loading_libraries}

::::: listingblock
::: title
Enumerate library, enumerate modules, enumerate pads
:::

::: content

```python

#!/usr/bin/python

from pcbnew import *

libpath = "/usr/share/kicad/modules/Sockets.pretty"
print ">> enumerate footprints, pads of",libpath

# Load the suitable plugin to read/write the .pretty library

# (containing the .kicad_mod footprint files)
src_type = IO_MGR.GuessPluginTypeFromLibPath( libpath );

# Rem: we can force the plugin type by using IO_MGR.PluginFind( IO_MGR.KICAD )
plugin = IO_MGR.PluginFind( src_type )

# Print plugin type name: (Expecting "KiCad" for a .pretty library)
print( "Selected plugin type: %s" % plugin.PluginName() )

list_of_footprints = plugin.FootprintEnumerate(libpath)

for name in list_of_footprints:
    fp = plugin.FootprintLoad(libpath,name)
    # print the short name of the footprint
    print name  # this is the name inside the loaded library
    # followed by ref field, value field, and decription string:
    # Remember ref and value texts are dummy texts, replaced by the schematic values
    # when reading a netlist.
    print "  ->", fp.GetReference(), fp.GetValue(), fp.GetDescription()

    # print pad info: GetPos0() is the pad position relative to the footrint position
    for pad in fp.Pads():
        print "    pad [%s]" % pad.GetPadName(), "at",\
        "pos0", ToMM(pad.GetPos0().x), ToMM(pad.GetPos0().y),"mm",\
        "shape offset", ToMM(pad.GetOffset().x), ToMM(pad.GetOffset().y), "mm"
    print ""

```

:::
:::::
::::::

::::::::: sect2

### BOARD {#_board}

::: paragraph
Board is the basic object in KiCad pcbnew, it's the document.
:::

::: paragraph
BOARD contains a set of object lists that can be accessed using the
following methods, they will return iterable lists that can be iterated
using \"for obj in list:\"
:::

::: ulist

- **board.GetModules():** This method returns a list of MODULE objects,
  all the modules available in the board will be exposed here.

- **board.GetDrawings():** Returns the list of BOARD_ITEMS that belong
  to the board drawings

- **board.GetTracks():** This method returns a list of TRACKs and VIAs
  inside a BOARD

- **board.GetFullRatsnest():** Returns the list of ratsnest (connections
  still not routed)

- **board.GetNetClasses():** Returns the list of net classes

- **board.GetCurrentNetClassName():** Returns the current net class

- **board.GetViasDimensionsList():** Returns the list of Via dimensions
  available to the board.

- **board.GetTrackWidthList():** Returns the list of Track Widths
  available to the board.
:::

::::: listingblock
::: title
Board Inspection Example
:::

::: content

```python

#!/usr/bin/env python
import sys
from pcbnew import *

filename=sys.argv[1]

pcb = LoadBoard(filename)

ToUnits = ToMM
FromUnits = FromMM

#ToUnits=ToMils

#FromUnits=FromMils

print "LISTING VIAS:"

for item in pcb.GetTracks():
    if type(item) is VIA:

        pos = item.GetPosition()
        drill = item.GetDrillValue()
        width = item.GetWidth()
        print " * Via:   %s - %f/%f "%(ToUnits(pos),ToUnits(drill),ToUnits(width))

    elif type(item) is TRACK:

        start = item.GetStart()
        end = item.GetEnd()
        width = item.GetWidth()

        print " * Track: %s to %s, width %f" % (ToUnits(start),ToUnits(end),ToUnits(width))

    else:
        print "Unknown type    %s" % type(item)

print ""
print "LIST DRAWINGS:"

for item in pcb.GetDrawings():
    if type(item) is TEXTE_PCB:
        print "* Text:    '%s' at %s"%(item.GetText(), item.GetPosition())
    elif type(item) is DRAWSEGMENT:
        print "* Drawing: %s"%item.GetShapeStr() # dir(item)
    else:
        print type(item)

print ""
print "LIST MODULES:"

for module in pcb.GetModules():
    print "* Module: %s at %s"%(module.GetReference(),ToUnits(module.GetPosition()))

print ""
print "Ratsnest cnt:",len(pcb.GetFullRatsnest())
print "track w cnt:",len(pcb.GetTrackWidthList())
print "via s cnt:",len(pcb.GetViasDimensionsList())

print ""
print "LIST ZONES:", pcb.GetAreaCount()

for idx in range(0, pcb.GetAreaCount()):
    zone=pcb.GetArea(idx)
    print "zone:", idx, "priority:", zone.GetPriority(), "netname", zone.GetNetname()

print ""
print "NetClasses:", pcb.GetNetClasses().GetCount(),

```

:::
:::::
:::::::::

::::::: sect2

### Examples {#_examples_2}

:::::: sect3

#### Change a component pin's paste mask margin {#_change_a_component_pins_paste_mask_margin}

::::: listingblock
::: title
We only want to change pins from 1 to 14, 15 is a thermal pad that must
be kept as it is.
:::

::: content

```python

#!/usr/bin/env python2.7
import sys
from pcbnew import *

filename=sys.argv[1]
pcb = LoadBoard(filename)

# Find module U304
u304 = pcb.FindModuleByReference('U304')
pads = u304.Pads()

#  Iterate over pads, printing solder paste margin
for p in pads:
    print p.GetPadName(), ToMM(p.GetLocalSolderPasteMargin())
    id = int(p.GetPadName())
    # Set margin to 0 for all but pad (pin) 15
    if id<15: p.SetLocalSolderPasteMargin(0)

pcb.Save("mod_"+filename)

```

:::
:::::
::::::
:::::::

:::::::::: sect2

### Footprint Wizards {#Footprint_Wizards}

::: paragraph
The footprint wizards are a collection of python scripts that can be
accessed from the Footprint Editor. If you invoke the footprint dialog
you select a given wizard that allows you to see the footprint rendered,
and you have some parameters you can edit.
:::

::: paragraph
If the plugins are not properly distributed to your system package, you
can find the latest versions in the KiCad source tree at
[launchpad](https://git.launchpad.net/kicad/tree/pcbnew/python/plugins).
:::

::: paragraph
They should be located in for example
`C:\Program Files\KiCad\share\kicad\scripting\plugins`.
:::

::: paragraph
On linux you can also keep your user plugins in `$HOME/.kicad_plugins`.
:::

::::: listingblock
::: title
Build footprints easily filling in parameters.
:::

::: content

```python
from __future__ import division
import pcbnew

import HelpfulFootprintWizardPlugin as HFPW


class FPC_FootprintWizard(HFPW.HelpfulFootprintWizardPlugin):

    def GetName(self):
        return "FPC (SMT connector)"

    def GetDescription(self):
        return "FPC (SMT connector) Footprint Wizard"

    def GetValue(self):
        pins = self.parameters["Pads"]["*n"]
        return "FPC_%d" % pins

    def GenerateParameterList(self):
        self.AddParam( "Pads", "n", self.uNatural, 40 )
        self.AddParam( "Pads", "pitch", self.uMM, 0.5 )
        self.AddParam( "Pads", "width", self.uMM, 0.25 )
        self.AddParam( "Pads", "height", self.uMM, 1.6)
        self.AddParam( "Shield", "shield_to_pad", self.uMM, 1.6 )
        self.AddParam( "Shield", "from_top", self.uMM, 1.3 )
        self.AddParam( "Shield", "width", self.uMM, 1.5 )
        self.AddParam( "Shield", "height", self.uMM, 2 )


    # build a rectangular pad
    def smdRectPad(self,module,size,pos,name):
        pad = pcbnew.D_PAD(module)
        pad.SetSize(size)
        pad.SetShape(pcbnew.PAD_SHAPE_RECT)
        pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        pad.SetLayerSet( pad.SMDMask() )
        pad.SetPos0(pos)
        pad.SetPosition(pos)
        pad.SetPadName(name)
        return pad

    def CheckParameters(self):
        p = self.parameters
        self.CheckParamInt( "Pads", "*n" )  # not internal units preceded by "*"


    def BuildThisFootprint(self):
        p = self.parameters
        pad_count       = int(p["Pads"]["*n"])
        pad_width       = p["Pads"]["width"]
        pad_height      = p["Pads"]["height"]
        pad_pitch       = p["Pads"]["pitch"]
        shl_width       = p["Shield"]["width"]
        shl_height      = p["Shield"]["height"]
        shl_to_pad      = p["Shield"]["shield_to_pad"]
        shl_from_top    = p["Shield"]["from_top"]

        offsetX         = pad_pitch * ( pad_count-1 ) / 2
        size_pad = pcbnew.wxSize( pad_width, pad_height )
        size_shld = pcbnew.wxSize(shl_width, shl_height)
        size_text = self.GetTextSize()  # IPC nominal

        # Gives a position and size to ref and value texts:
        textposy = pad_height/2 + pcbnew.FromMM(1) + self.GetTextThickness()
        self.draw.Reference( 0, textposy, size_text )

        textposy = textposy + size_text + self.GetTextThickness()
        self.draw.Value( 0, textposy, size_text )

        # create a pad array and add it to the module
        for n in range ( 0, pad_count ):
            xpos = pad_pitch*n - offsetX
            pad = self.smdRectPad(self.module,size_pad, pcbnew.wxPoint(xpos,0),str(n+1))
            self.module.Add(pad)


        # Mechanical shield pads: left pad and right pad
        xpos = -shl_to_pad-offsetX
        pad_s0_pos = pcbnew.wxPoint(xpos,shl_from_top)
        pad_s0 = self.smdRectPad(self.module, size_shld, pad_s0_pos, "0")
        xpos = (pad_count-1) * pad_pitch+shl_to_pad - offsetX
        pad_s1_pos = pcbnew.wxPoint(xpos,shl_from_top)
        pad_s1 = self.smdRectPad(self.module, size_shld, pad_s1_pos, "0")

        self.module.Add(pad_s0)
        self.module.Add(pad_s1)

        # add footprint outline
        linewidth = self.draw.GetLineThickness()
        margin = linewidth

        # upper line
        posy = -pad_height/2 - linewidth/2 - margin
        xstart = - pad_pitch*0.5-offsetX
        xend = pad_pitch * pad_count + xstart;
        self.draw.Line( xstart, posy, xend, posy )

        # lower line
        posy = pad_height/2 + linewidth/2 + margin
        self.draw.Line(xstart, posy, xend, posy)

        # around left mechanical pad (the outline around right pad is mirrored/y axix)
        yend = pad_s0_pos.y + shl_height/2 + margin
        self.draw.Line(xstart, posy, xstart, yend)
        self.draw.Line(-xstart, posy, -xstart, yend)

        posy = yend
        xend = pad_s0_pos.x - (shl_width/2 + linewidth + margin*2)
        self.draw.Line(xstart, posy, xend, posy)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)

        # set SMD attribute
        self.module.SetAttributes(pcbnew.MOD_CMS)

        # vertical segment at left of the pad
        xstart = xend
        yend = posy - (shl_height + linewidth + margin*2)
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)

        # horizontal segment above the pad
        xstart = xend
        xend = - pad_pitch*0.5-offsetX
        posy = yend
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy,-xend, yend)

        # vertical segment above the pad
        xstart = xend
        yend = -pad_height/2 - linewidth/2 - margin
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)


# register into pcbnew
FPC_FootprintWizard().register()

```

:::
:::::
::::::::::

:::::::::::: sect2

### Action Plugins {#action_menu}

::: paragraph
Action plugin associate events to scripting actions. Currently only
register a new menu is implemented.
:::

::: paragraph
New menu are available inside menu **Tools** ⇒ **External plugins**.
:::

:::: imageblock
::: content
![Pcbnew action menu](images/Pcbnew_action_menu.png)
:::
::::

::: ulist

- **Refresh**: reload plugins (create new menu if needed)

- **Add date on PCB**: An example plugin.
:::

::: paragraph
**Warning**: As all other python scripts, undo/redo function not work
(yet !).
:::

::::: listingblock
::: title
Action plugin example: Add date to any text item with content
\'\$date\$\'
:::

::: content

```python
import pcbnew
import re
import datetime

class text_by_date(pcbnew.ActionPlugin):
    """
    test_by_date: A sample plugin as an example of ActionPlugin
    Add the date to any text field of the board where the content is '$date$'
    How to use:

    - Add a text on your board with the content '$date$'

    - Call the plugin

    - Automaticaly the date will be added to the text (format YYYY-MM-DD)
    """

    def defaults(self):
        """
        Method defaults must be redefined
        self.name should be the menu label to use
        self.category should be the category (not yet used)
        self.description should be a comprehensive description
          of the plugin
        """
        self.name = "Add date on PCB"
        self.category = "Modify PCB"
        self.description = "Automaticaly add date on an existing PCB"

    def Run(self):
        pcb = pcbnew.GetBoard()
        for draw in pcb.GetDrawings():
            if draw.GetClass() == 'PTEXT':
                txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                                 "$date$", draw.GetText())
                if txt == "$date$":
                    draw.SetText("$date$ %s"%datetime.date.today())


text_by_date().register()

```

:::
:::::
::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::: sect1

## Introduction to Pcbnew {#_introduction_to_pcbnew}

:::::::::::::::::::::::::: sectionbody
::::::::: sect2

### Description {#_description}

::: paragraph
Pcbnew is a powerful printed circuit board software tool available for
the Linux, Microsoft Windows and Apple OS X operating systems. Pcbnew is
used in association with the schematic capture program Eeschema to
create printed circuit boards.
:::

::: paragraph
Pcbnew manages libraries of footprints. Each footprint is a drawing of
the physical component including its land pattern (the layout of pads on
the circuit board). The required footprints are automatically loaded
during the reading of the Netlist. Any changes to footprint selection or
annotation can be changed in the schematic and updated in pcbnew by
regenerating the netlist and reading it in pcbnew again.
:::

::: paragraph
Pcbnew provides a design rules check (DRC) tool which prevents track and
pad clearance issues as well as preventing nets from being connected
that aren't connected in the netlist/schematic. When using the
interactive router it continuously runs the design rules check and will
help automatically route individual traces.
:::

::: paragraph
Pcbnew provides a rats nest display, a hairline connecting the pads of
footprints which are connected on the schematic. These connections move
dynamically as track and footprint movements are made.
:::

::: paragraph
Pcbnew has a simple but effective autorouter to assist in the production
of the circuit board. An Export/Import in SPECCTRA dsn format allows the
use of more advanced auto-routers.
:::

::: paragraph
Pcbnew provides options specifically provided for the production of
ultra high frequency microwave circuits (such as pads of trapezoidal and
complex form, automatic layout of coils on the printed circuit, etc).
:::
:::::::::

::::::::::::::: sect2

### Principal design features {#_principal_design_features}

::: paragraph
The smallest unit in pcbnew is 1 nanometer. All dimensions are stored as
integer nanometers.
:::

::: paragraph
Pcbnew can generate up to 32 layers of copper, 14 technical layers (silk
screen, solder mask, component adhesive, solder paste and edge cuts)
plus 4 auxiliary layers (drawings and comments) and manages in real time
the hairline indication (rats nest) of missing tracks.
:::

::: paragraph
The display of the PCB elements (tracks, pads, text, drawings...​) is
customizable:
:::

::: ulist

- In full or outline.

- With or without track clearance.
:::

::: paragraph
For complex circuits, the display of layers, zones, and components can
be hidden in a selective way for clarity on screen. Nets of traces can
be highlighted to provide high contrast as well.
:::

::: paragraph
Footprints can be rotated to any angle, with a resolution of 0.1 degree.
:::

::: paragraph
Pcbnew includes a Footprint Editor that allows editing of individual
footprints that have been on a pcb or editing a footprint in a library.
:::

::: paragraph
The Footprint Editor provides many time saving tools such as:
:::

::: ulist

- Fast pad numbering by simply dragging the mouse over pads in the order
  you want them numbered.

- Easy generation of rectangular and circular arrays of pads for LGA/BGA
  or circular footprints.

- Semi-automatic aligning of rows or columns of pads.
:::

::: paragraph
Footprint pads have a variety of properties that can be adjusted. The
pads can be round, rectangular, oval or trapezoidal. For through-hole
parts drills can be offset inside the pad and be round or a slot.
Individual pads can also be rotated and have unique soldermask, net, or
paste clearance. Pads can also have a solid connection or a thermal
relief connection for easier manufacturing. Any combination of unique
pads can be placed within a footprint.
:::

::: paragraph
Pcbnew easily generates all the documents necessary for production:
:::

::: ulist

- Fabrication outputs:

  ::: ulist

  - Files for Photoplotters in GERBER RS274X format.

  - Files for drilling in EXCELLON format.
  :::

- Plot files in HPGL, SVG and DXF format.

- Plot and drilling maps in POSTSCRIPT format.

- Local Printout.
:::
:::::::::::::::

::::: sect2

### General remarks {#_general_remarks}

::: paragraph
Due to the degree of control necessary it is highly suggested to use a
3-button mouse with pcbnew. Many features such as panning and zooming
require a 3-button mouse.
:::

::: paragraph
In the new release of KiCad, pcbnew has seen wide sweeping changes from
developers at CERN. This includes features such as a new renderer
(OpenGL and Cairo view modes), an interative push and shove router,
differential and meander trace routing and tuning, a reworked Footprint
Editor, and many other features. Please note that most of these new
features **only** exist in the new OpenGL and Cairo view modes.
:::
:::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::
::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Installation {#_installation}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2

### Installation of the software {#_installation_of_the_software}

::: paragraph
The installation procedure is described in the KiCad documentation.
:::
::::

::::::: sect2

### Modifying the default configuration {#_modifying_the_default_configuration}

::: paragraph
A default configuration file `kicad.pro` is provided in
`kicad/share/template`. This file is used as the initial configuration
for all new projects.
:::

::: paragraph
This configuration file can be modified to change the libraries to be
loaded.
:::

::: paragraph
To do this:
:::

::: ulist

- Launch Pcbnew using kicad or directly. On Windows it is in
  `C:\kicad\bin\pcbnew.exe` and on Linux you can run
  `/usr/local/kicad/bin/kicad` or `/usr/local/kicad/bin/pcbnew` if the
  binaries are located in `/usr/local/kicad/bin`.

- Select Preferences - Libs and Dir.

- Edit as required.

- Save the modified configuration (Save Cfg) to
  `kicad/share/template/kicad.pro`.
:::
:::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Managing Footprint Libraries {#_managing_footprint_libraries}

::: paragraph
As of release 4.0, Pcbnew organises the footprint libraries using files
called \"footprint library tables\". A footprint library table contains
descriptions of some number of individual footprint libraries, along
with a \"nickname\" for each library, which is used to refer to that
library when referencing a footprint.
:::

::: paragraph
There are several kinds of library supported by Pcbnew, each of which is
supported by a \"plugin\":
:::

::: ulist

- KiCad - native KiCad footprint libraries stored on a local filesystem
  in the *.pretty* format (folders containing *.kicad_mod* files)

- Github - native KiCad footprint libraries in the *.pretty* format,
  stored online as a Github repository

- Legacy - old-style KiCad footprint libraries (*.mod* files)

- Eagle - Eagle footprint libraries (folders containing *.fp* files)

- Geda-PCB - Geda PCB libraries
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - You can write only KiCad        |
| :::                               |   *.pretty* footprint library     |
|                                   |   folders on your local disk (and |
|                                   |   the .kicad_mod files inside     |
|                                   |   these folders).                 |
|                                   |                                   |
|                                   | - All other formats are read      |
|                                   |   only.                           |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
It is allowed to have footprints with the same name in different
libraries. The footprint will be stored as a combination of library
*and* footprint name, ensuring that the correct footprint is loaded from
the appropriate library.
:::

::: paragraph
There are two footprint library tables: the global one and the project
one.
:::

:::: sect3

#### Global Footprint Library Table {#_global_footprint_library_table}

::: paragraph
The global footprint library table contains the list of libraries that
are always available regardless of the currently loaded project file.
The table is saved in the file `fp-lib-table` in the user's home folder.
The location of this folder is dependent on the operating system.
:::
::::

::::: sect3

#### Project Specific Footprint Library Table {#_project_specific_footprint_library_table}

::: paragraph
The project specific footprint library table contains the list of
libraries that are available specifically for the currently loaded
project file. The project specific footprint library table can only be
edited when it is loaded along with the project board file. If no
project file is loaded or there is no footprint library table file in
the project path, an empty table is created which can be edited and
later saved along with the board file.
:::

::: paragraph
When entries are defined in the project specific table, an
\`fp-lib-table file \`containing the entries will be written into the
folder of the currently open PCB.
:::
:::::

:::::::: sect3

#### Initial Configuration {#_initial_configuration}

::: paragraph
The first time CvPcb or Pcbnew is run and the global footprint table
file `fp-lib-table` is not found in the user's home folder, Pcbnew will
attempt to copy the default footprint table file `fp_global_table`
stored in the system's KiCad template folder to the file `fp-lib-table`
in the user's home folder. If `fp_global_table` cannot be found, an
empty footprint library table will be created in the user's home folder.
If this happens, the user can either copy `fp_global_table` manually or
configure the table by hand.
:::

::: paragraph
The default footprint library table includes all of the standard
footprint libraries that are installed as part of KiCad.
:::

::: {.admonitionblock .tip}

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ::: title                         | ::: paragraph                                                                                                              |
| Tip                               | There are also sample `fp-lib-table` files in the official [KiCad library                                                  |
| :::                               | repository](https://github.com/KiCad/kicad-library) that you can use as your own starting point:                           |
|                                   | :::                                                                                                                        |
|                                   |                                                                                                                            |
|                                   | ::: ulist                                                                                                                  |
|                                   | - All KiCad libraries via Github:                                                                                          |
|                                   |   [fp-lib-table.for-github](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-github)           |
|                                   |                                                                                                                            |
|                                   | - All KiCad libraries, assuming they are on your disk already (you will need to download them if you do not already have   |
|                                   |   them): [fp-lib-table.for-pretty](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-pretty)    |
|                                   |                                                                                                                            |
|                                   | - Standard Eagle libraries (for Eagle 6.4.0)                                                                               |
|                                   |   [fp-lib-table.for-eagle-6.4.0](https://github.com/KiCad/kicad-library/blob/master/template/fp-lib-table.for-eagle-6.4.0) |
|                                   | :::                                                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
:::

::: paragraph
The **first thing** to do when configuring KiCad do is to modify this
table (add/remove entries) according to your work and the libraries you
need for your projects.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | It can be time consuming to have  |
| Tip                               | many libraries, especially if     |
| :::                               | they are only found online (such  |
|                                   | as the Github libraries). If you  |
|                                   | find libraries slow to load, try  |
|                                   | removing ones you don't need.     |
+-----------------------------------+-----------------------------------+
:::
::::::::

::::::::::::::: sect3

#### Adding Table Entries using the Libraries Manager {#_adding_table_entries_using_the_libraries_manager}

::: paragraph
The library table manager is accessible by:
:::

:::: imageblock
::: content
![Library tables menu item](images/Library_tables_menu_item.png)
:::
::::

::: paragraph
The image below shows the footprint library table editing dialog which
can be opened by invoking the \"Footprint Libraries Manager\" entry from
the \"Preferences\" menu.
:::

:::: imageblock
::: content
![Footprint tables list](images/Footprint_tables_list.png)
:::
::::

::: paragraph
In order to use a footprint library, it must first be added to either
the global table or the project specific table. The project specific
table is only applicable when a board file is open.
:::

::: paragraph
Each library table entry has a nickname. This *must* be unique within
that table. The nickname does not have to be related in any way to the
actual library file name or path.
:::

::: paragraph
There are some rules for valid library table entries:
:::

::: ulist

- The colon `:` character cannot be used anywhere in the nickname.

- Each library entry must have a valid path and/or file name depending
  on the type of library. Paths can be defined as absolute, relative, or
  by environment variable substitution (see below)

- The appropriate plug in type must be selected in order for the library
  to be properly read.
:::

::: paragraph
There is also a description field to add a description of the library
entry. The option field contains special options that are
plugin-specific and is generally blank.
:::

::: paragraph
Although you cannot have duplicate library nicknames in the same table,
you can have duplicate library nicknames in both the global and project
specific footprint library table. The project specific table entry will
take precedence over the global table entry when duplicated names occur.
:::
:::::::::::::::

::::::: sect3

#### Environment Variable Substitution {#_environment_variable_substitution}

::: paragraph
One of the most powerful features of the footprint library table is
environment variable substitution. This allows you to define custom
paths to where your libraries are stored in environment variables.
:::

::: paragraph
Environment variable substitution is supported by using the syntax
`${ENV_VAR_NAME}` in the footprint library path.
:::

::: paragraph
There are some default variables that KiCad defines:
:::

::: ulist

- `$KISYSMOD`: This points to where the default footprint libraries that
  were installed along with KiCad are located. You can override
  `$KISYSMOD` by defining it yourself which allows you to substitute
  your own libraries in place of the default KiCad footprint libraries.

- When a board file is loaded, `$KPRJMOD` is defined using that board's
  path. This allows you to refer to libraries in the project path
  without having to repeat the absolute path to the library in the
  project specific footprint library table.
:::
:::::::

:::::::::::::::::::::::::::::::::::::: sect3

#### Adding Table Entries using the Library Wizard {#_adding_table_entries_using_the_library_wizard}

::: paragraph
There is an interactive wizard that can assist you adding libraries to
your library tables. It is accessible from the menu:
:::

:::: imageblock
::: content
![Library tables menu item](images/Library_tables_menu_item.png)
:::
::::

::: paragraph
It can also be launched from the library manager, using the \"Append
With Wizard\" button.
:::

::: paragraph
Here, the local libraries option is selected.
:::

:::: imageblock
::: content
![Footprint library wizard local
libstartpage](images/en/fplib_wizard_locallibstartpage.png)
:::
::::

::: paragraph
Here, the remote libraries option is selected.
:::

:::: imageblock
::: content
![Footprint library wizard startpage
GitHub](images/en/fplib_wizard_startpage_github.png)
:::
::::

::: paragraph
The wizard will then lead you though the steps to adding a library,
which will depend on the type of library you are adding. The process for
each type will be explained below.
:::

::: paragraph
After a set of libraries is selected, the next page validates the
choice:
:::

:::: imageblock
::: content
![Footprint libary wizard validate](images/en/fplib_wizard_validate.png)
:::
::::

::: paragraph
If some selected libraries are incorrect (not supported, not a footprint
library ...​) they will be flagged as \`\`INVALID\'\'.
:::

::: paragraph
The last choice is the footprint library table to populate either:
:::

::: ulist

- the global table, or

- the project specific table
:::

:::: imageblock
::: content
![Footprint library wizard choose local
folder](images/en/fplib_wizard_chooseflt.png)
:::
::::

::::::::: sect4

##### Adding Existing Local Libraries {#_adding_existing_local_libraries}

::: paragraph
You might have local libraries already on your computer. For example:
:::

::: ulist

- Previously downloaded KiCad pretty directories

- Legacy KiCad *.mod* files from older installations

- Geda or Eagle libraries
:::

::: paragraph
These can be added with the \"Files on my computer\" option. You will be
asked for the directory of the library to add and the format:
:::

:::: imageblock
::: content
![Footprint library wizard local lib
selection](images/en/fplib_wizard_locallibselection.png)
:::
::::

::: paragraph
If you don't select the format, the wizard will try to guess the right
format.
:::
:::::::::

::::::::::: sect4

##### Adding Libraries from Github {#_adding_libraries_from_github}

::: paragraph
The wizard can also add libraries from Github with the \"Github
repository\" option.
:::

::: paragraph
You need to specify the Github account that contains the repositories
you want to add.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-------------------------------------------------------------+
| ::: title                         | The offical KiCad library Github account is                 |
| Tip                               | [https://github.com/KiCad](https://github.com/KiCad){.bare} |
| :::                               |                                                             |
+-----------------------------------+-------------------------------------------------------------+
:::

::: paragraph
You may choose to save a local copy. If you do *not* save a local copy,
the library will be a *Github* library, and will resync on every library
reload. If you *do* save a local copy, the library will be a *KiCad*
(pretty) library and will not automatically update in future.
:::

::: paragraph
The next page will load a list of *.pretty* repositories found on that
Github account. You can choose any number to add to the library.
:::

:::: imageblock
::: content
![Footprint library wizard GitHub
selection](images/en/fplib_wizard_githubselection.png)
:::
::::

::: paragraph
After confirmation,if you opted to save a copy, the footprints will be
downloaded to the specified local location now. If you are using the
Github plugin (no local copy), the footprints are loaded from Github
when needed.
:::
:::::::::::
::::::::::::::::::::::::::::::::::::::

:::::::::::: sect3

#### Using the KiCad plugin {#_using_the_kicad_plugin}

::: paragraph
The KiCad plugin deals with native KiCad libraries that exist on your
computer (or some accessible filesystem).
:::

::: paragraph
It is used for pre-installed libraries that are installed along with
KiCad, as well as other KiCad libraries, either from the official KiCad
library collection, 3rd party libraries or your own curated libraries.
:::

::::::::: sect4

##### Installing KiCad plugin libraries {#_installing_kicad_plugin_libraries}

::: paragraph
The Footprint Library Wizard can help you install libraries already on
disk or on Github. However, for libraries on disk, you need to put them
there yourself in the first place.
:::

::: paragraph
A KiCad library is a directory that contains some number of *.kicad_mod*
files.
:::

::: paragraph
This is often done by unpacking an archive file, copying a directory
from another location, or cloning a version-controlled repository.
:::

::: paragraph
The KiCad plugin does not specify any kind of version control, but Git
is very commonly used to track changes to libraries, which can be
critical to ensuring library data is safely recorded and backed up.
:::

::: paragraph
It is easy to track changes and contribute with the offical KiCad Github
libraries. This is done using the Git version control software. If you
want to contribute back, you'll have to fork the repos on Github so you
can send pull requests. If you just want to update libraries when
needed, you don't need to do that, you can clone the offical KiCad
libraries directly and pull as needed.
:::

::: {.admonitionblock .note}

+-----------------------------------+------------------------------------------------------------------------------------+
| ::: title                         | Sending pull requests via Github will allow the automatic library standards        |
| Note                              | checker to verify your proposed changes. See [KiCad Library                        |
| :::                               | Conventions](https://github.com/KiCad/kicad-library/wiki/Kicad-Library-Convention) |
|                                   | for details of the library conventions.                                            |
+-----------------------------------+------------------------------------------------------------------------------------+
:::
:::::::::
::::::::::::

:::::::::::::::::::::::::: sect3

#### Using the GitHub Plugin {#_using_the_github_plugin}

::: paragraph
The GitHub plugin is a special plugin that provides an interface for
read-only access to a remote GitHub repository consisting of *.pretty*
footprints and optionally provides \"Copy-On-Write\" (COW) support for
editing footprints read from the GitHub repo and saving them locally.
:::

::: {.admonitionblock .important}

+-----------------------------------+----------------------------------------------------+
| ::: title                         | ::: ulist                                          |
| Important                         | - The \"GitHub\" plugin is for **read-only access  |
| :::                               |   of remote pretty footprint libraries** at        |
|                                   |   [https://github.com](https://github.com){.bare}. |
|                                   |                                                    |
|                                   | - You will not be told if a remote repository      |
|                                   |   changed since your last use of it. Be cautious   |
|                                   |   when using footprint directly from Github.       |
|                                   | :::                                                |
+-----------------------------------+----------------------------------------------------+
:::

::: paragraph
To add a GitHub entry to the footprint library table the \"Library
Path\" in the footprint library table entry must be set to a valid
GitHub URL.
:::

::: paragraph
For example:
:::

:::: literalblock
::: content
    https://github.com/liftoff-sr/pretty_footprints
:::
::::

::: paragraph
Typically GitHub URLs take the form:
:::

:::: literalblock
::: content
    https://github.com/user_name/repo_name
:::
::::

::: paragraph
The \"Plugin Type\" must be set to \"Github\".
:::

::: paragraph
The table below shows a footprint library table entry with the default
options (no COW support):
:::

+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-------------+-------------+
| Nickname    | Library Path                                                                                              | Plugin Type | Options     | Description |
+=============+===========================================================================================================+=============+=============+=============+
| github      | [https://github.com/liftoff-sr/pretty_footprints](https://github.com/liftoff-sr/pretty_footprints){.bare} | Github      |             | Liftoff's   |
|             |                                                                                                           |             |             | GH          |
|             |                                                                                                           |             |             | footprints  |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-------------+-------------+

:::::::: sect4

##### Copy-On-Write {#_copy_on_write}

::: paragraph
To enable the \"Copy-On-Write\" feature the option
`allow_pretty_writing_to_this_dir` must be added to the \"Options\"
setting of the footprint library table entry. This option is the
\"Library Path\" for local storage of modified copies of footprints read
from the GitHub repo. The footprints saved to this path are combined
with the read-only part of the GitHub repository to create the footprint
library. If this option is missing, then the GitHub library is
read-only. If the option is present for a GitHub library, then any
writes to this hybrid library will go to the local `*.pretty` directory.
:::

::: paragraph
The github.com resident portion of this hybrid COW library is always
read-only, meaning you cannot delete anything or modify any footprint in
the specified GitHub repository directly. The aggregate library type
remains \"Github\" in all further discussions, but it consists of both
the local read/write portion and the remote read-only portion.
:::

::: paragraph
The table below shows a footprint library table entry with the COW
option given. Note the use of the environment variable `${HOME}` as an
example only. The github.pretty directory is located in
`${HOME}/pretty/path`. Anytime you use the option
`allow_pretty_writing_to_this_dir`, you will need to create that
directory manually in advance and it must end with the extension
`.pretty`.
:::

+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------+-------------+
| Nickname    | Library Path                                                                                              | Plugin Type | Options                                                         | Description |
+=============+===========================================================================================================+=============+=================================================================+=============+
| github      | [https://github.com/liftoff-sr/pretty_footprints](https://github.com/liftoff-sr/pretty_footprints){.bare} | Github      | `allow_pretty_writing_to_this_dir=${HOME}/pretty/github.pretty` | Liftoff's   |
|             |                                                                                                           |             |                                                                 | GH          |
|             |                                                                                                           |             |                                                                 | footprints  |
+-------------+-----------------------------------------------------------------------------------------------------------+-------------+-----------------------------------------------------------------+-------------+

::: paragraph
Footprint loads will always give precedence to the local footprints
found in the path given by the option
`allow_pretty_writing_to_this_dir`. Once you have saved a footprint to
the COW library's local directory by doing a footprint save in the
Footprint Editor, no GitHub updates will be seen when loading a
footprint with the same name as one for which you've saved locally.
:::

::: paragraph
Always keep a separate local

.pretty directory for each GitHub library, never combine them by
referring to the same directory more than once. Also, do not use the
same COW (`.pretty`) directory in a footprint library table entry. This
would likely create a mess. The value of the option
`allow_pretty_writing_to_this_dir` will expand any environment variable
using the `${}` notation to create the path in the same way as the
\"Library Path\" setting.
:::
::::::::

::::: sect4

##### Using Copy-On-Write to share footprints {#_using_copy_on_write_to_share_footprints}

::: paragraph
What's the point of COW? If you periodically email your COW pretty
footprint modifications to the GitHub repository maintainer, you can
help update the GitHub copy. Simply email the individual `*.kicad_mod`
files you find in your COW directories to the maintainer of the GitHub
repository. After you've received confirmation that your changes have
been committed, you can safely delete your COW file(s) and the updated
footprint from the read-only part of GitHub library will flow down. Your
goal should be to keep the COW file set as small as possible by
contributing frequently to the shared master copies at
[https://github.com](https://github.com){.bare}.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | You can also contribute to        |
| Tip                               | library developement using local  |
| :::                               | Git clones of the relevant        |
|                                   | libraries using the *KiCad*       |
|                                   | plugin and submitting pull        |
|                                   | requests to the library           |
|                                   | maintainers.                      |
+-----------------------------------+-----------------------------------+
:::
:::::

::::: sect4

##### Caching Github requests {#_caching_github_requests}

::: paragraph
The Github plugin can be slow, as it must download all the libraries
from the Internet before they can be used.
:::

::: paragraph
Nginx can be used as a cache to the github server to speed up the
loading of footprints. It can be installed locally or on a network
server. There is an example configuration in KiCad sources at
`pcbnew/github/nginx.conf`. The most straightforward way to get this
working is to overwrite the default nginx.conf with this one and
`export KIGITHUB=http://my_server:54321/KiCad`, where `my_server` is the
IP or domain name of the machine running nginx.
:::
:::::
::::::::::::::::::::::::::

:::::::::::: sect3

#### Usage Patterns {#_usage_patterns}

::: paragraph
Footprint libraries can be defined either globally or specifically to
the currently loaded project. Footprint libraries defined in the user's
global table are always available and are stored in the `fp-lib-table`
file in the user's home folder. Global footprint libraries can always be
accessed even when there is no project net list file opened. The project
specific footprint table is active only for the currently open net list
file. The project specific footprint library table is saved in the file
`fp-lib-table` in the path of the currently open board file. You are
free to define libraries in either table.
:::

::: paragraph
There are advantages and disadvantages to each method:
:::

::: ulist

- You can define all of your libraries in the global table which means
  they will always be available when you need them.

  ::: ulist

  - The disadvantage of this is that you may have to search through a
    lot of libraries to find the footprint you are looking for.
  :::

- You can define all your libraries on a project specific basis.

  ::: ulist

  - The advantage of this is that you only need to define the libraries
    you actually need for the project which cuts down on searching.

  - The disadvantage is that you always have to remember to add each
    footprint library that you need for every project.
  :::

- You can also define footprint libraries both globally and project
  specifically.
:::

::: paragraph
One usage pattern would be to define your most commonly used libraries
globally and the library only required for the project in the project
specific library table. There is no restriction on how you define your
libraries.
:::

::::::: sect4

##### Modifying footprints in a PCB project {#_modifying_footprints_in_a_pcb_project}

::: paragraph
When a footprint is added to a PCB, the entire footprint is copied into
the PCB file (*.kicad_pcb*). This means changes to the footprint in the
library do not automatically affect the PCB.
:::

::: paragraph
This also means that you can individually edit footprints on the PCB
without affecting other instances of the same footprint (either on the
same PCB or on other PCBs).
:::

::: paragraph
However, if you modify the library footprint, the next time you place an
instance, it will not match existing footprints of the same name.
:::

::: {.admonitionblock .tip}

+-----------------------------------+-----------------------------------+
| ::: title                         | A common practice is to copy all  |
| Tip                               | the footprints you use to a       |
| :::                               | separate version-controlled       |
|                                   | location, so that this project is |
|                                   | not unexpectedly affected by      |
|                                   | changes to system or user         |
|                                   | libraries. Also, it ensures all   |
|                                   | the footprint resources used for  |
|                                   | the PCB can be easily distributed |
|                                   | with the PCB file.                |
+-----------------------------------+-----------------------------------+
:::
:::::::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## General operations {#_general_operations}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::: sect2

### Toolbars and commands {#_toolbars_and_commands}

::: paragraph
In Pcbnew it is possible to execute commands using various means:
:::

::: ulist

- Text-based menu at the top of the main window.

- Top toolbar menu.

- Right toolbar menu.

- Left toolbar menu.

- Mouse buttons (menu options). Specifically:

  ::: ulist

  - The right mouse button reveals a pop-up menu the content of which
    depends on the element under the mouse arrow.
  :::

- Keyboard (Function keys `F1`, `F2`, `F3`, `F4`, `Shift`, `Delete`,
  `+`, `-`, `Page Up`, `Page Down` and `Space bar`). The `Escape` key
  generally cancels an operation in progress.
:::

::: paragraph
The screenshot below illustrates some of the possible accesses to these
operations:
:::

:::: imageblock
::: content
![Right click legacy menu](images/Right-click_legacy_menu.png)
:::
::::
::::::::

::::::::::::: sect2

### Mouse commands {#_mouse_commands}

:::: sect3

#### Basic commands {#_basic_commands}

::: ulist

- Left button

  ::: ulist

  - Single-click displays the characteristics of the footprint or text
    under the cursor in the lower status bar.

  - Double-click displays the editor (if the element is editable) of the
    element under the cursor.
  :::

- Centre button/wheel

  ::: ulist

  - Rapid zoom and some commands in layer manager.

  - Hold down the centre button and draw a rectangle to zoom to the
    described area. Rotation of the mouse wheel will allow you to zoom
    in and zoom out.
  :::

- Right button

  ::: ulist

  - Displays a pop-up menu
  :::
:::
::::

:::::::::: sect3

#### Operations on blocks {#_operations_on_blocks}

::: paragraph
Operations to move, invert (mirror), copy, rotate and delete a block are
all available via the pop-up menu. In addition, the view can zoom to the
area described by the block.
:::

::: paragraph
The framework of the block is traced by moving the mouse while holding
down the left mouse button. The operation is executed when the button is
released.
:::

::: paragraph
By holding down one of the hotkeys `Shift` or `Ctrl`, or both keys
`Shift` and `Ctrl` together, while the block is drawn the operation
invert, rotate or delete is automatically selected as shown in the table
below:
:::

+-----------------------------------+-----------------------------------+
| Action                            | Effect                            |
+===================================+===================================+
| Left mouse button held down       | Trace framework to move block     |
+-----------------------------------+-----------------------------------+
| `Shift` + Left mouse button held  | Trace framework for invert block  |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Ctrl` + Left mouse button held   | Trace framework for rotating      |
| down                              | block 90°                         |
+-----------------------------------+-----------------------------------+
| `Shift` + `Ctrl` + Left mouse     | Trace framework to delete the     |
| button held down                  | block                             |
+-----------------------------------+-----------------------------------+
| Centre mouse button held down     | Trace framework to zoom to block  |
+-----------------------------------+-----------------------------------+

::: paragraph
When moving a block:
:::

::: ulist

- Move block to new position and operate left mouse button to place the
  elements.

- To cancel the operation use the right mouse button and select Cancel
  Block from the menu (or press the `Esc` key).
:::

::: paragraph
Alternatively if no key is pressed when drawing the block use the right
mouse button to display the pop-up menu and select the required
operation.
:::

::: paragraph
For each block operation a selection window enables the action to be
limited to only some elements.
:::
::::::::::
:::::::::::::

::::: sect2

### Selection of grid size {#_selection_of_grid_size}

::: paragraph
During element layout the cursor moves on a grid. The grid can be turned
on or off using the icon on the left toolbar.
:::

::: paragraph
Any of the pre-defined grid sizes, or a User Defined grid, can be chosen
using the pop-up window, or the drop-down selector on the toolbar at the
top of the screen. The size of the User Defined grid is set using the
menu bar option Dimensions → User Grid Size.
:::
:::::

::::: sect2

### Adjustment of the zoom level {#_adjustment_of_the_zoom_level}

::: paragraph
The zoom level can be changed using any of the following methods:
:::

::: ulist

- Open the pop-up window (using the right mouse button) and then select
  the desired zoom.

- Use the following function keys:

  ::: ulist

  - `F1`: Enlarge (zoom in)

  - `F2`: Reduce (zoom out)

  - `F3`: Redraw the display

  - `F4`: Centre view at the current cursor position
  :::

- Rotate the mouse wheel.

- Hold down the middle mouse button and draw a rectangle to zoom to the
  described area.
:::
:::::

:::::::::: sect2

### Displaying cursor coordinates {#_displaying_cursor_coordinates}

::: paragraph
The cursor coordinates are displayed in inches or millimetres as
selected using the \'In\' or \'mm\' icons on the left hand side toolbar.
:::

::: paragraph
Whichever unit is selected Pcbnew always works to a precision of
1/10,000 of inch.
:::

::: paragraph
The status bar at the bottom of the screen gives:
:::

::: ulist

- The current zoom setting.

- The absolute position of the cursor.

- The relative position of the cursor. Note the relative coordinates
  (x,y) can be set to (0,0) at any position by pressing the space bar.
  The cursor position is then displayed relative to this new datum.
:::

::: paragraph
In addition the relative position of the cursor can be displayed using
its polar co-ordinates (ray + angle). This can be turned on and off
using the icon in the left hand side toolbar.
:::

:::: imageblock
::: content
![Pcbnew coordinate status
display](images/Pcbnew_coordinate_status_display.png)
:::
::::
::::::::::

::::: sect2

### Keyboard commands - hotkeys {#_keyboard_commands_hotkeys}

::: paragraph
Many commands are accessible directly with the keyboard. Selection can
be either upper or lower case. Most hot keys are shown in menus. Some
hot keys that do not appear are:
:::

::: ulist

- `Delete`: deletes a footprint or a track. (*Available only if the
  Footprint mode or the Track mode is active*)

- `V`: if the track tool is active switches working layer or place via,
  if a track is in progress.

- `+` and `-`: select next or previous layer.

- `?`: display the list of all hot keys.

- `Space`: reset relative coordinates.
:::
:::::

:::::::::: sect2

### Operation on blocks {#_operation_on_blocks}

::: paragraph
Operations to move, invert (mirror), copy, rotate and delete a block are
all available from the pop-up menu. In addition, the view can zoom to
that described by the block.
:::

::: paragraph
The framework of the block is traced by moving the mouse while holding
down the left mouse button. The operation is executed when the button is
released.
:::

::: paragraph
By holding down one of the keys `Shift` or `Ctrl`, both `Shift` and
`Ctrl` together, or `Alt`, while the block is drawn the operation
invert, rotate, delete or copy is automatically selected as shown in the
table below:
:::

+-----------------------------------+-----------------------------------+
| Action                            | Effect                            |
+===================================+===================================+
| Left mouse button held down       | Move block                        |
+-----------------------------------+-----------------------------------+
| `Shift` + Left mouse button held  | Invert (mirror) block             |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Ctrl` + Left mouse button held   | Rotate block 90°                  |
| down                              |                                   |
+-----------------------------------+-----------------------------------+
| `Shift` + `Ctrl` + Left mouse     | Delete the block                  |
| button held down                  |                                   |
+-----------------------------------+-----------------------------------+
| `Alt` + Left mouse button held    | Copy the block                    |
| down                              |                                   |
+-----------------------------------+-----------------------------------+

::: paragraph
When a block command is made, a dialog window is displayed, and items
involved in this command can be chosen.
:::

::: paragraph
Any of the commands above can be cancelled via the same pop-up menu or
by pressing the Escape key (`Esc`).
:::

:::: imageblock
::: content
![Pcbnew legacy block selection
dialog](images/Pcbnew_legacy_block_selection_dialog.png)
:::
::::
::::::::::

::::::: sect2

### Units used in dialogs {#_units_used_in_dialogs}

::: paragraph
Units used to display dimensions values are inch and mm. The desired
unit can be selected by pressing the icon located in left toolbar:
[![unit inch](images/icons/unit_inch.png)]{.image} [![unit
mm](images/icons/unit_mm.png)]{.image} However one can enter the unit
used to define a value, when entering a new value.
:::

::: paragraph
Accepted units are:
:::

+-----------------------------------+-----------------------------------+
| 1 **in**                          | 1 inch                            |
+-----------------------------------+-----------------------------------+
| 1 **\"**                          | 1 inch                            |
+-----------------------------------+-----------------------------------+
| 25 **th**                         | 25 thou                           |
+-----------------------------------+-----------------------------------+
| 25 **mi**                         | 25 mils, same as thou             |
+-----------------------------------+-----------------------------------+
| 6 **mm**                          | 6 mm                              |
+-----------------------------------+-----------------------------------+

::: paragraph
The rules are:
:::

::: ulist

- Spaces between the number and the unit are accepted.

- Only the first two letters are significant.

- In countries using an alternative decimal separator than the period,
  the period (`.`) can be used as well. Therefore `1,5` and `1.5` are
  the same in French.
:::
:::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Top menu bar {#_top_menu_bar}

::: paragraph
The top menu bar provides access to the files (loading and saving),
configuration options, printing, plotting and the help files.
:::

:::: imageblock
::: content
![Pcbnew top menu bar](images/Pcbnew_top_menu_bar.png)
:::
::::

:::::: sect3

#### The File menu {#_the_file_menu}

:::: imageblock
::: content
![Pcbnew file menu](images/Pcbnew_file_menu.png)
:::
::::

::: paragraph
The File menu allows the loading and saving of printed circuits files,
as well as printing and plotting the circuit board. It enables the
export (with the format GenCAD 1.4) of the circuit for use with
automatic testers.
:::
::::::

:::::: sect3

#### Edit menu {#_edit_menu}

::: paragraph
Allows some global edit actions:
:::

:::: imageblock
::: content
![Pcbnew edit menu](images/Pcbnew_edit_menu.png)
:::
::::
::::::

:::::::::::: sect3

#### View menu {#_view_menu}

::: paragraph
Allows:
:::

::: ulist

- Hide/Show the Layers manager (colors selection for displaying layers
  and other elements. Also enables the display of elements to be turned
  on and off).

- Hide/Show the Microwave toolbar.

- Display Library browser and 3D viewer.

- Zoom functions

- Setting grid and units

- Select Drawing mode and Contrast mode
:::

:::: imageblock
::: content
![Pcbnew view menu](images/Pcbnew_view_menu.png)
:::
::::

::: paragraph
Zoom functions and 3D board display.
:::

:::::: sect4

##### 3D Viewer {#_3d_viewer}

::: paragraph
Opens the 3D Viewer. Here is a sample:
:::

:::: imageblock
::: content
![Sample 3D board](images/Sample_3D_board.png)
:::
::::
::::::
::::::::::::

::::::::: sect3

#### Setup menu {#_setup_menu}

::: paragraph
Provides access to 2 dialogs:
:::

::: ulist

- Setting Layers (number, enabled and layers names)

- Setting Design Rules (tracks and vias sizes, clearances).
:::

::: paragraph
An important menu. Allows adjustment of:
:::

::: ulist

- Size of texts and the line width for drawings.

- Dimensions and characteristic of pads.

- Setting the global values for solder mask and solder paste layers
:::

:::: imageblock
::: content
![Pcbnew setup menu](images/Pcbnew_setup_menu.png)
:::
::::
:::::::::

:::::: sect3

#### Place menu {#_place_menu}

::: paragraph
Same function as the right-hand toolbar.
:::

:::: imageblock
::: content
![Pcbnew place menu](images/Pcbnew_place_menu.png)
:::
::::
::::::

:::::: sect3

#### Route menu {#_route_menu}

::: paragraph
Routing function.
:::

:::: imageblock
::: content
![Pcbnew route menu](images/Pcbnew_route_menu.png)
:::
::::
::::::

::::::: sect3

#### Inspect menu {#_inspect_menu}

::: paragraph
Allows:
:::

::: ulist

- List nets

- Measure function

- Design Rules Checker
:::

:::: imageblock
::: content
![Pcbnew inspect menu](images/Pcbnew_inspect_menu.png)
:::
::::
:::::::

::::::: sect3

#### Tools menu {#_tools_menu}

::: paragraph
Allows:
:::

::: ulist

- Display load netlist dialog

- Update PCB from schematic

- Update Footprints from library

- FreeRoute collaboration

- Python scripting console

- External plugins
:::

:::: imageblock
::: content
![Pcbnew tools menu](images/Pcbnew_tools_menu.png)
:::
::::
:::::::

::::::: sect3

#### The Preferences menu {#_the_preferences_menu}

:::: imageblock
::: content
![Pcbnew preferences menu](images/Pcbnew_preferences_menu.png)
:::
::::

::: paragraph
Allows:
:::

::: ulist

- Selection of the footprint libraries.

- Management of general options (units, etc.).

- The management of other display options.

- Creation, editing (and re-read) of the hot keys file.
:::
:::::::

:::: sect3

#### The Help menu {#_the_help_menu}

::: paragraph
Provides access to the user manuals and to the version information menu
(Pcbnew About).
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::: sect2

### Using icons on the top toolbar {#_using_icons_on_the_top_toolbar}

::: paragraph
This toolbar gives access to the principal functions of Pcbnew.
:::

:::: imageblock
::: content
![Pcbnew top toolbar](images/Pcbnew_top_toolbar.png)
:::
::::

+---------------------------------------------------------------------+--------------------------------------------------+
| [![new board](images/icons/new_board.png)]{.image}                  | Creation of a new printed circuit.               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![open brd file](images/icons/open_brd_file.png)]{.image}          | Opening of an old printed circuit.               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![save](images/icons/save.png)]{.image}                            | Save printed circuit.                            |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![sheetset](images/icons/sheetset.png)]{.image}                    | Selection of the page size and modification of   |
|                                                                     | the file properties.                             |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![module editor](images/icons/module_editor.png)]{.image}          | Opens Footprint Editor to edit library or pcb    |
|                                                                     | footprint.                                       |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![modview icon](images/icons/modview_icon.png)]{.image}            | Opens Footprint Viewer to display library or pcb |
|                                                                     | footprint.                                       |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![undo](images/icons/undo.png)]{.image}                            | Undo/Redo last commands (10 levels)              |
| [![redo](images/icons/redo.png)]{.image}                            |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![print button](images/icons/print_button.png)]{.image}            | Display print menu.                              |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![plot](images/icons/plot.png)]{.image}                            | Display plot menu.                               |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image} [![zoom              | Zoom in and Zoom out (relative to the centre of  |
| out](images/icons/zoom_out.png)]{.image}                            | screen).                                         |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom redraw](images/icons/zoom_redraw.png)]{.image}              | Redraw the screen                                |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![zoom fit in page](images/icons/zoom_fit_in_page.png)]{.image}    | Fit to page                                      |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![find](images/icons/find.png)]{.image}                            | Find footprint or text.                          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![netlist](images/icons/netlist.png)]{.image}                      | Netlist operations (selection, reading, testing  |
|                                                                     | and compiling).                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![drc](images/icons/drc.png)]{.image}                              | DRC (Design Rule Check): Automatic check of the  |
|                                                                     | tracks.                                          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew toolbar layer select                                      | Selection of the working layer.                  |
| dropdown](images/Pcbnew_toolbar_layer_select_dropdown.png)]{.image} |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew layer pair                                                | Selection of layer pair (for vias)               |
| indicator](images/Pcbnew_layer_pair_indicator.png)]{.image}         |                                                  |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![mode module](images/icons/mode_module.png)]{.image}              | Footprint mode: when active this enables         |
|                                                                     | footprint options in the pop-up window.          |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![mode track](images/icons/mode_track.png)]{.image}                | Routing mode: when active this enables routing   |
|                                                                     | options in the pop-up window                     |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![web support](images/icons/web_support.png)]{.image}              | Direct access to the router Freerouter           |
+---------------------------------------------------------------------+--------------------------------------------------+
| [![py script](images/icons/py_script.png)]{.image}                  | Show / Hide the Python scripting console         |
+---------------------------------------------------------------------+--------------------------------------------------+

:::: sect3

#### Auxiliary toolbar {#_auxiliary_toolbar}

+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew track thickness                                      | Selection of thickness of track already in use.  |
| dropdown](images/Pcbnew_track_thickness_dropdown.png)]{.image} |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew via size                                             | Selection of a dimension of via already in use.  |
| dropdown](images/Pcbnew_via_size_dropdown.png)]{.image}        |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![auto track                                                  | Automatic track width: if enabled when creating  |
| width](images/icons/auto_track_width.png)]{.image}             | a new track, when starting on an existing track, |
|                                                                | the width of the new track is set to the width   |
|                                                                | of the existing track.                           |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew grid size                                            | Selection of the grid size.                      |
| dropdown](images/Pcbnew_grid_size_dropdown.png)]{.image}       |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+
| [![Pcbnew zoom factor                                          | Selection of the zoom.                           |
| dropdown](images/Pcbnew_zoom_factor_dropdown.png)]{.image}     |                                                  |
+----------------------------------------------------------------+--------------------------------------------------+

::: {style="page-break-after: always;"}
:::
::::
::::::::

:::::: sect2

### Right-hand side toolbar {#_right_hand_side_toolbar}

::: paragraph
This toolbar gives access to the editing tool to change the PCB shown in
Pcbnew.
:::

+-----------------------------------------------------------------+-----------------------------------------------------+------------------------------------------------------------+
| [![Pcbnew right                                                 | [![cursor](images/icons/cursor.png)]{.image}        | Select the standard mouse mode.                            |
| toolbar](images/Pcbnew_right_toolbar.png){width="80%"}]{.image} |                                                     |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![net                                              | Highlight net selected by clicking on a track or pad.      |
|                                                                 | highlight](images/icons/net_highlight.png)]{.image} |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![tool                                             | Display local ratsnest (Pad or Footprint).                 |
|                                                                 | ratsnest](images/icons/tool_ratsnest.png)]{.image}  |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![module](images/icons/module.png)]{.image}        | Add a footprint from a library.                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Placement of tracks and vias.                              |
|                                                                 | tracks](images/icons/add_tracks.png)]{.image}       |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add zone](images/icons/add_zone.png)]{.image}    | Placement of zones (copper planes).                        |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add keepout                                      | Placement of keepout areas ( on copper layers ).           |
|                                                                 | area](images/icons/add_keepout_area.png)]{.image}   |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add dashed                                       | Draw Lines on technical layers (i.e. not a copper layer).  |
|                                                                 | line](images/icons/add_dashed_line.png)]{.image}    |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Draw Circles on technical layers (i.e. not a copper        |
|                                                                 | circle](images/icons/add_circle.png)]{.image}       | layer).                                                    |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add arc](images/icons/add_arc.png)]{.image}      | Draw Arcs on technical layers (i.e. not a copper layer).   |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![text](images/icons/text.png)]{.image}            | Placement of text.                                         |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add                                              | Draw Dimensions on technical layers (i.e. not the copper   |
|                                                                 | dimension](images/icons/add_dimension.png)]{.image} | layer).                                                    |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![add pcb                                          | Draw Alignment Marks (appearing on all layers).            |
|                                                                 | target](images/icons/add_pcb_target.png)]{.image}   |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![delete](images/icons/delete.png)]{.image}        | Delete element pointed to by the cursor                    |
|                                                                 |                                                     |                                                            |
|                                                                 |                                                     | **Note:** When Deleting, if several superimposed elements  |
|                                                                 |                                                     | are pointed to, priority is given to the smallest (in the  |
|                                                                 |                                                     | decreasing set of priorities tracks, text, footprint). The |
|                                                                 |                                                     | function \"Undelete\" of the upper toolbar allows the      |
|                                                                 |                                                     | cancellation of the last item deleted.                     |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![pcb                                              | Offset adjust for drilling and place files.                |
|                                                                 | offset](images/icons/pcb_offset.png)]{.image}       |                                                            |
|                                                                 +-----------------------------------------------------+------------------------------------------------------------+
|                                                                 | [![grid select                                      | Grid origin. (grid offset). Useful mainly for editing and  |
|                                                                 | axis](images/icons/grid_select_axis.png)]{.image}   | placement of footprints. Can also be set in                |
|                                                                 |                                                     | Dimensions/Grid menu.                                      |
+-----------------------------------------------------------------+-----------------------------------------------------+------------------------------------------------------------+

::: ulist

- Placement of footprints, tracks, zones of copper, texts, etc.

- Net Highlighting.

- Creating notes, graphic elements, etc.

- Deleting elements.
:::

::: {style="page-break-after: always;"}
:::
::::::

:::: sect2

### Left-hand side toolbar {#_left_hand_side_toolbar}

::: paragraph
The left hand-side toolbar provides display and control options that
affect Pcbnew's interface.
:::

+----------------------------------------------------------------+---------------------------------------------------------+------------------------------------------------------------+
| [![Pcbnew left                                                 | [![drc off](images/icons/drc_off.png)]{.image}          | Turns DRC (Design Rule Checking) on/off. **Caution:** when |
| toolbar](images/Pcbnew_left_toolbar.png){width="80%"}]{.image} |                                                         | DRC is off incorrect connections can be made.              |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![grid](images/icons/grid.png)]{.image}                | Turn grid display on/off **Note:** a small grid may not be |
|                                                                |                                                         | displayed unless zoomed in far enough                      |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![polar coord](images/icons/polar_coord.png)]{.image}  | Polar display of the relative co-ordinates on the status   |
|                                                                |                                                         | bar on/off.                                                |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![unit inch](images/icons/unit_inch.png)]{.image}      | Display/entry of coordinates or dimensions in inches or    |
|                                                                | [![unit mm](images/icons/unit_mm.png)]{.image}          | millimeters.                                               |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![cursor                                               | Change cursor display shape.                               |
|                                                                | shape](images/icons/cursor_shape.png)]{.image}          |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![general                                              | Display general rats nest (incomplete connections between  |
|                                                                | ratsnest](images/icons/general_ratsnest.png)]{.image}   | footprints).                                               |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![local                                                | Display footprint rats nest dynamically as it is moved.    |
|                                                                | ratsnest](images/icons/local_ratsnest.png)]{.image}     |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![auto delete                                          | Enable/Disable automatic deletion of a track when it is    |
|                                                                | track](images/icons/auto_delete_track.png)]{.image}     | redrawn.                                                   |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone](images/icons/show_zone.png)]{.image}      | Show filled areas in zones                                 |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone                                            | Do not show filled areas in zones                          |
|                                                                | disable](images/icons/show_zone_disable.png)]{.image}   |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![show zone outline                                    | Show only outlines of filled areas in zones                |
|                                                                | only](images/icons/show_zone_outline_only.png)]{.image} |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![pad sketch](images/icons/pad_sketch.png)]{.image}    | Display of pads in outline mode on/off.                    |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![via sketch](images/icons/via_sketch.png)]{.image}    | Display of vias in outline mode on/off.                    |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![showtrack](images/icons/showtrack.png)]{.image}      | Display of tracks in outline mode on/off.                  |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![contrast                                             | High contrast display mode on/off. In this mode the active |
|                                                                | mode](images/icons/contrast_mode.png)]{.image}          | layer is displayed normally, all the other layers are      |
|                                                                |                                                         | displayed in gray. Useful for working on multi-layer       |
|                                                                |                                                         | circuits.                                                  |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![layers                                               | Hide/Show the Layers manager                               |
|                                                                | manager](images/icons/layers_manager.png)]{.image}      |                                                            |
|                                                                +---------------------------------------------------------+------------------------------------------------------------+
|                                                                | [![mw toolbar](images/icons/mw_toolbar.png)]{.image}    | Access to microwaves tools. Under development              |
+----------------------------------------------------------------+---------------------------------------------------------+------------------------------------------------------------+
::::

::::::: sect2

### Pop-up windows and fast editing {#_pop_up_windows_and_fast_editing}

::: paragraph
A right-click of the mouse opens a pop-up window. Its contents depends
on the element pointed at by the cursor.
:::

::: paragraph
This gives immediate access to:
:::

::: ulist

- Changing the display (centre display on cursor, zoom in or out or
  selecting the zoom).

- Setting the grid size.

- Additionally a right-click on an element enables editing of the most
  commonly modified element parameters.
:::

::: paragraph
The screenshots below show what the pop-up windows looks like.
:::
:::::::

:::::::::::::::::::::::::::::::::::: sect2

### Available modes {#_available_modes}

::: paragraph
There are 3 modes when using pop-up menus. In the pop-up menus, these
modes add or remove some specific commands.
:::

+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Normal mode                                      |
| module](images/icons/mode_module.png)]{.image} |                                                  |
| and [![mode                                    |                                                  |
| track](images/icons/mode_track.png)]{.image}   |                                                  |
| disabled                                       |                                                  |
+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Footprint mode                                   |
| module](images/icons/mode_module.png)]{.image} |                                                  |
| enabled                                        |                                                  |
+------------------------------------------------+--------------------------------------------------+
| [![mode                                        | Tracks mode                                      |
| track](images/icons/mode_track.png)]{.image}   |                                                  |
| enabled                                        |                                                  |
+------------------------------------------------+--------------------------------------------------+

:::::::::::: sect3

#### Normal mode {#_normal_mode}

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode](images/Pcbnew_popup_normal_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode
track](images/Pcbnew_popup_normal_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup normal mode
footprint](images/Pcbnew_popup_normal_mode_footprint.png)
:::
::::
::::::::::::

::::::::::::: sect3

#### Footprint mode {#_footprint_mode}

::: paragraph
Same cases in Footprint Mode ([![mode
module](images/icons/mode_module.png)]{.image} enabled)
:::

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode](images/Pcbnew_popup_footprint_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode
track](images/Pcbnew_popup_footprint_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup footprint mode
footprint](images/Pcbnew_popup_footprint_mode_footprint.png)
:::
::::
:::::::::::::

::::::::::::: sect3

#### Tracks mode {#_tracks_mode}

::: paragraph
Same cases in Track Mode ([![mode
track](images/icons/mode_track.png)]{.image} enabled)
:::

::: ulist

- Pop-up menu with no selection:
:::

:::: imageblock
::: content
![Pcbnew popup track mode](images/Pcbnew_popup_track_mode.png)
:::
::::

::: ulist

- Pop-up menu with track selected:
:::

:::: imageblock
::: content
![Pcbnew popup track mode
track](images/Pcbnew_popup_track_mode_track.png)
:::
::::

::: ulist

- Pop-up menu with footprint selected:
:::

:::: imageblock
::: content
![Pcbnew popup track mode
footprint](images/Pcbnew_popup_track_mode_footprint.png)
:::
::::
:::::::::::::
::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Create and modify a board {#_create_and_modify_a_board}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::::::::::::::::::::::::::::::::::: sect2

### Creating a board {#_creating_a_board}

::::::::: sect3

#### Drawing the board outline {#_drawing_the_board_outline}

::: paragraph
It is usually a good idea to define the outline of the board first. The
outline is drawn as a sequence of line segments. Select \'Edge.Cuts\' as
the active layer and use the \'Add graphic line or polygon\' tool to
trace the edge, clicking at the position of each vertex and
double-clicking to finish the outline. Boards usually have very precise
dimensions, so it may be necessary to use the displayed cursor
coordinates while tracing the outline. Remember that the relative
coordinates can be zeroed at any time using the space bar, and that the
display units can also be toggled using \'Ctrl-U\'. Relative coordinates
enable very precise dimensions to be drawn. It is possible to draw a
circular (or arc) outline:
:::

::: {.olist .arabic}

1.  Select the \'Add graphic circle\' or \'Add graphic arc\' tool

2.  Click to fix the circle centre

3.  Adjust the radius by moving the mouse

4.  Finish by clicking again.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | The width of the outline can be   |
| Note                              | adjusted in the Parameters menu   |
| :::                               | (recommended width = 150 in 1/10  |
|                                   | mils) or via the Options, but     |
|                                   | this will not be visible unless   |
|                                   | the graphics are displayed in     |
|                                   | other than outline mode.          |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
The resulting outline might look something like this:
:::

:::: imageblock
::: content
![Pcbnew simple board outline](images/Pcbnew_simple_board_outline.png)
:::
::::
:::::::::

::::::::::::::::::::::::: sect3

#### Using a DXF drawing for the board outline {#_using_a_dxf_drawing_for_the_board_outline}

::: paragraph
As an alternative to drawing the board outline in Pcbnew directly, an
outline can also be imported from a DXF drawing.
:::

::: paragraph
Using this feature allows for much more complex board shapes than is
possible with the Pcbnew drawing capabilities.
:::

::: paragraph
For example a mechanical CAD package can be used to define a board shape
that fits a particular enclosure.
:::

::::::::::: sect4

##### Preparing the DXF drawing for import into KiCad {#_preparing_the_dxf_drawing_for_import_into_kicad}

::: paragraph
The **DXF** import capability in KiCad does not support DXF features
like **POLYLINES** and **ELLIPSIS** and DXF files that use these
features require a few conversion steps to prepare them for import.
:::

::: paragraph
A software package like LibreCAD can be used for this conversion.
:::

::: paragraph
As a first step, any **POLYLINES** need to be split (Exploded) into
their original simpler shapes. In LibreCAD use the following steps:
:::

::: {.olist .arabic}

1.  Open a copy of the DXF file.

2.  Select the board shape (selected shapes are shown with dashed
    lines).

3.  In the **Modify** menu, select **Explode**.

4.  Press ENTER.
:::

::: paragraph
As a next step, complex curves like **ELLIPSIS** need to be broken up in
small line segments that \'approximate\' the required shape. This
happens automatically when the DXF file is exported or saved in the
older **DXF R12** file format (as the R12 format does not support
complex curve shapes, CAD applications convert these shapes to line
segments. Some CAD applications allow configuration of the number or the
length of the line segments used). In LibreCAD the segment length it
generally small enough for use in board shapes.
:::

::: paragraph
In LibreCAD, use the following steps to export to the **DXF R12** file
format:
:::

::: {.olist .arabic}

1.  In the **File** menu, use **Save As...​**

2.  In the **Save Drawing As** dialog, there is a **Save as type:**
    selection near the bottom of the dialog. Select the option **Drawing
    Exchange DXF R12**.

3.  Optionally enter a file name in the **File name:** field.

4.  Click **Save**
:::

::: paragraph
Your DXF file is now ready for import into KiCad.
:::
:::::::::::

:::::::: sect4

##### Importing the DXF file into KiCad {#_importing_the_dxf_file_into_kicad}

::: paragraph
The following steps describe the import of the prepared DXF file as a
board shape into KiCad. Note that the import bahaviour is slightly
different depending on which \'canvas\' is used.
:::

::: paragraph
Using the \"default\" canvas mode:
:::

::: {.olist .arabic}

1.  In the **File** menu, select **Import** and then the **DXF File**
    option.

2.  In the **Import DXF File** dialog use \'Browse\' to select the
    prepared DXF file to be imported.

3.  In the \'Place DXF origin (0,0) point:\' option, select the
    placement of DXF origin relative to the board coordinates (the KiCad
    board has (0,0) in the top left corner). For the \'User defined
    position\' enter the coordinates in the \'X Position\' and \'Y
    Position\' fields.

4.  In the \'Layer\' selection, select the board layer for the import.
    **Edge.Cuts** is needed for the board outline.

5.  Click \'OK\'.
:::

::: paragraph
Using the \"OpenGL\" or \"Cairo\" canvas modes:
:::

::: {.olist .arabic}

1.  In the **File** menu, select **Import** and then the **DXF File**
    option.

2.  In the **Import DXF File** dialog use \'Browse\' to select the
    prepared DXF file to be imported.

3.  The \'Place DXF origin (0,0) point:\' option setting is ignored in
    this mode.

4.  In the \'Layer\' selection, select the board layer for the import.
    **Edge.Cuts** is needed for the board outline.

5.  Click \'OK\'.

6.  The shape is now attached to your cursor and it can be moved around
    the board area.

7.  Click to \'drop\' the shape on the board.
:::
::::::::

:::::: sect4

##### Example imported DXF shape {#_example_imported_dxf_shape}

::: paragraph
Here is an example of a DXF import with a board that had several
elliptical segments approximated by a number of short line segments:
:::

:::: imageblock
::: content
![Pcbnew board outline imported from a
DXF](images/Pcbnew_board_outline_imported_from_a_DXF.png)
:::
::::
::::::
:::::::::::::::::::::::::

::::::::::::: sect3

#### Reading the netlist generated from the schematic {#_reading_the_netlist_generated_from_the_schematic}

::: paragraph
Activate the [![netlist](images/icons/netlist.png)]{.image} icon to
display the netlist dialog window:
:::

:::: imageblock
::: content
![Pcbnew netlist dialog](images/en/Pcbnew_netlist_dialog.png)
:::
::::

::: paragraph
If the name (path) of the netlist in the window title is incorrect, use
the \'Select\' button to browse to the desired netlist. Then \'Read\'
the netlist. Any footprints not already loaded will appear, superimposed
one upon another (we shall see below how to move them automatically).
:::

:::: imageblock
::: content
![Pcbnew board outline with
dogpile](images/Pcbnew_board_outline_with_dogpile.png)
:::
::::

::: paragraph
If none of the footprints have been placed, all of the footprints will
appear on the board in the same place, making them difficult to
recognize. It is possible to arrange them automatically (using the
command \'Global Spread and Place\' accessed via the right mouse
button). Here is the result of such automatic arrangement:
:::

:::: imageblock
::: content
![Pcbnew board outline with globally placed
modules](images/Pcbnew_board_outline_with_globally_placed_modules.png)
:::
::::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | If a board is modified by         |
| Note                              | replacing an existing footprint   |
| :::                               | with a new one (for example       |
|                                   | changing a 1/8 W resistor to 1/2  |
|                                   | W) in CvPcb, it will be necessary |
|                                   | to delete the existing component  |
|                                   | before Pcbnew will load the       |
|                                   | replacement footprint. However,   |
|                                   | if a footprint is to be replaced  |
|                                   | by an existing footprint, this is |
|                                   | easier to do using the footprint  |
|                                   | dialog accessed by clicking the   |
|                                   | right mouse button over the       |
|                                   | footprint in question.            |
+-----------------------------------+-----------------------------------+
:::
:::::::::::::
::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::: sect2

### Correcting a board {#_correcting_a_board}

::: paragraph
It is very often necessary to correct a board following a corresponding
change in the schematic.
:::

:::: sect3

#### Steps to follow {#_steps_to_follow}

::: {.olist .arabic}

1.  Create a new netlist from the modified schematic.

2.  If new components have been added, link these to their corresponding
    footprint in CvPcb.

3.  Read the new netlist in Pcbnew.
:::
::::

::::::: sect3

#### Deleting incorrect tracks {#_deleting_incorrect_tracks}

::: paragraph
Pcbnew is able to automatically delete tracks that have become incorrect
as a result of modifications. To do this, check the \'Delete\' option in
the \'Unconnected Tracks\' box of the netlist dialog:
:::

:::: imageblock
::: content
![Pcbnew bad tracks deletion
option](images/Pcbnew_bad_tracks_deletion_option.png)
:::
::::

::: paragraph
However, it is often quicker to modify such tracks by hand (the DRC
function allows their identification).
:::
:::::::

:::::::::: sect3

#### Deleted components {#_deleted_components}

::: paragraph
Pcbnew can delete footprint corresponding to components that have been
removed from the schematic. This is optional.
:::

::: paragraph
This is necessary because there are often footprints (holes for fixation
screws, for instance) that are added to the PCB that never appear in the
schematic.
:::

:::: imageblock
::: content
![Pcbnew extra footprints deletion
option](images/Pcbnew_extra_footprints_deletion_option.png)
:::
::::

::: paragraph
If the \"Extra Footprints\" option is checked, a footprint corresponding
to a component not found in the netlist will be deleted, unless they
have the option \"Locked\" active. It is a good idea to activate this
option for \"mechanical\" footprints:
:::

:::: imageblock
::: content
![Pcbnew unlock footprint
option](images/Pcbnew_unlock_footprint_option.png)
:::
::::
::::::::::

::::::: sect3

#### Modified footprints {#_modified_footprints}

::: paragraph
If a footprint is modified in the netlist (using CvPcb), but the
footprint has already been placed, it will not be modified by Pcbnew,
unless the corresponding option of the \'Exchange Footprint\' box of the
netlist dialog is checked:
:::

:::: imageblock
::: content
![Pcbnew exchange module
option](images/Pcbnew_exchange_module_option.png)
:::
::::

::: paragraph
Changing a footprint (replacing a resistor with one of a different size,
for instance) can be effected directly by editing the footprint.
:::
:::::::

:::::::: sect3

#### Advanced options - selection using time stamps {#_advanced_options_selection_using_time_stamps}

::: paragraph
Sometimes the notation of the schematic is changed, without any material
changes in the circuit (this would concern the references - like R5,
U4...​).The PCB is therefore unchanged (except possibly for the
silkscreen markings). Nevertheless, internally, components and
footprints are represented by their reference. In this situation, the
\'Timestamp\' option of the netlist dialog may be selected before
re-reading the netlist:
:::

:::: imageblock
::: content
![Pcbnew module selection
option](images/Pcbnew_module_selection_option.png)
:::
::::

::: paragraph
With this option, Pcbnew no longer identifies footprints by their
reference, but by their time stamp instead. The time stamp is
automatically generated by Eeschema (it is the time and date when the
component was placed in the schematic).
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | Great care should be exercised    |
| Warning                           | when using this option (save the  |
| :::                               | file first!). This is because the |
|                                   | technique is complicated in the   |
|                                   | case of components containing     |
|                                   | multiple parts (e.g. a 7400 has 4 |
|                                   | parts and one case). In this      |
|                                   | situation, the time stamp is not  |
|                                   | uniquely defined (for the 7400    |
|                                   | there would be up to four - one   |
|                                   | for each part). Nevertheless, the |
|                                   | time stamp option usually         |
|                                   | resolves re-annotation problems.  |
+-----------------------------------+-----------------------------------+
:::
::::::::
::::::::::::::::::::::::::::::

:::::::::::: sect2

### Direct exchange for footprints already placed on board {#_direct_exchange_for_footprints_already_placed_on_board}

::: paragraph
Changing a footprint ( or some identical footprints) to another
footprint is very useful, and is very easy:
:::

::: {.olist .arabic}

1.  Click on a footprint to open the Edit dialog box.

2.  Activate Change Footprints.
:::

:::: imageblock
::: content
![Pcbnew change modules button](images/Pcbnew_change_modules_button.png)
:::
::::

::: paragraph
Options for Change Footprint(s):
:::

:::: imageblock
::: content
![Pcbnew footprint exchange
options](images/Pcbnew_footprint_exchange_options.png)
:::
::::

::: paragraph
One must choose a new footprint name and use:
:::

::: ulist

- **Change footprint of \'xx\'** for the current footprint

- **Change footprints \'yy\'** for all footprints like the current
  footprint.

- **Change footprints having same value** for all footprints like the
  current footprint, restricted to components which have the same value.

- **Update all footprints of the board** for reloading of all footprints
  on board.
:::
::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Layers {#_layers}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2

### Introduction {#_introduction}

::: paragraph
Pcbnew can work with 50 different layers:
:::

::: ulist

- Between 1 and 32 copper layers for routing tracks.

- 14 fixed-purpose technical layers:

  ::: ulist

  - 12 paired layers (Front/Back): **Adhesive**, **Solder Paste**,
    **Silk Screen**, **Solder Mask**, **Courtyard**, **Fabrication**

  - 2 standalone layers: **Edge Cuts**, **Margin**
  :::

- 4 auxiliary layers that you can use any way you want: **Comments**,
  **E.C.O. 1**, **E.C.O. 2**, **Drawings**
:::
:::::

::::::: sect2

### Setting up layers {#_setting_up_layers}

::: paragraph
To open the **Layers Setup** from the menu bar, select **Setup** →
**Layers Setup**.
:::

::: paragraph
The board thickness, number of copper layers, their names, and their
function are configured there. Unused technical layers can be disabled.
:::

:::: imageblock
::: content
![Pcbnew layer setup dialog](images/Pcbnew_layer_setup_dialog.png)
:::
::::
:::::::

::::::::::::::::: sect2

### Layer Description {#_layer_description}

::::::: sect3

#### Copper Layers {#_copper_layers}

::: paragraph
Copper layers are the usual working layers used to place and re-arrange
tracks. Layer numbers start from 0 (the first copper layer, on Front)
and end at 31 (Back). Since components cannot be placed in **inner
layers** (number 1 to 30), only layers number 0 and 31 are **component
layer**.
:::

::: paragraph
The name of any copper layer is editable. Copper layers have a function
attribute that is useful when using the external router *Freerouter*.
Example of default layer names are **F.Cu** and **In0** for layer number
0.
:::

:::: imageblock
::: content
![Pcbnew layer setup dialog layer
properties](images/Pcbnew_layer_setup_dialog_layer_properties.png)
:::
::::
:::::::

:::::: sect3

#### Paired Technical Layers {#_paired_technical_layers}

::: paragraph
12 technical layers come in pairs: one for the front, one for the back.
You can recognize them with the \"F.\" or \"B.\" prefix in their names.
The elements making up a footprint (pad, drawing, text) of one of these
layers are automatically mirrored and moved to the complementary layer
when the footprint is flipped.
:::

::: paragraph
The paired technical layers are:
:::

::: dlist

**Adhesive** (F.Adhes and B.Adhes)

:   These are used in the application of adhesive to stick SMD
    components to the circuit board, generally before wave soldering.

**Solder Paste** (F.Paste and B.Paste)

:   Used to produce a mask to allow solder paste to be placed on the
    pads of surface mount components, generally before reflow soldering.
    Usually only surface mount pads occupy these layers.

**Silk Screen** (F.SilkS and B.SilkS)

:   They are the layers where the drawings of the components appear.
    That's where you draw things like component polarity, first pin
    indicator, reference for mounting, ...​

**Solder Mask** (F.Mask and B.Mask)

:   These define the solder masks. All pads should appear on one of
    these layers (SMT) or both (for through hole) to prevent the varnish
    from covering the pads.

**Courtyard** (F.CrtYd and B.CrtYd)

:   Used to show how much space a component physically takes on the PCB.

**Fabrication** (F.Fab and B.Fab)

:   The fabrication layers are primarily used for documentation purposes
    to convey information to, for example, the PCB maker or the assembly
    house.
:::
::::::

:::: sect3

#### Independant Technical Layers {#_independant_technical_layers}

::: dlist

**Edge.Cuts**

:   This layer is reserved for the drawing of circuit board outline. Any
    element (graphic, texts...​) placed on this layer appears on all the
    other layers. Use this layer only to draw board outlines.

**Margin**

:   Board's edge setback outline (?).
:::
::::

::::: sect3

#### Layers for general use {#_layers_for_general_use}

::: paragraph
These layers are for any use. They can be used for text such as
instructions for assembly or wiring, or construction drawings, to be
used to create a file for assembly or machining. Their names are:
:::

::: ulist

- Comments

- E.C.O. 1

- E.C.O. 2

- Drawings
:::
:::::
:::::::::::::::::

::::::::::::::::::: sect2

### Selection of the active layer {#_selection_of_the_active_layer}

::: paragraph
The selection of the active working layer can be done in several ways:
:::

::: ulist

- Using the right toolbar (Layer manager).

- Using the upper toolbar.

- With the pop-up window (activated with the right mouse button).

- Using the + and - keys (works on copper layers only).

- By hot keys.
:::

::::: sect3

#### Selection using the layer manager {#_selection_using_the_layer_manager}

:::: imageblock
::: content
![Pcbnew layer manager pane](images/Pcbnew_layer_manager_pane.png)
:::
::::
:::::

::::::: sect3

#### Selection using the upper toolbar {#_selection_using_the_upper_toolbar}

:::: imageblock
::: content
![Pcbnew layer selection
dropdown](images/Pcbnew_layer_selection_dropdown.png)
:::
::::

::: paragraph
This directly selects the working layer.
:::

::: paragraph
Hot keys to select the working layer are displayed.
:::
:::::::

:::::::: sect3

#### Selection using the pop-up window {#_selection_using_the_pop_up_window}

:::: imageblock
::: content
![Pcbnew layer selection popup](images/Pcbnew_layer_selection_popup.png)
:::
::::

::: paragraph
The Pop-up window opens a menu window which provides a choice for the
working layer.
:::

:::: imageblock
::: content
![Pcbnew layer selection
dialog](images/Pcbnew_layer_selection_dialog.png)
:::
::::
::::::::
:::::::::::::::::::

::::::::::: sect2

### Selection of the Layers for Vias {#_selection_of_the_layers_for_vias}

::: paragraph
If the **Add Tracks and Vias** icon is selected on the right hand
toolbar, the Pop-Up window provides the option to change the layer pair
used for vias:
:::

:::: imageblock
::: content
![Pcbnew via layer pair popup](images/Pcbnew_via_layer_pair_popup.png)
:::
::::

::: paragraph
This selection opens a menu window which provides choice of the layers
used for vias.
:::

:::: imageblock
::: content
![Pcbnew via layer pair dialog](images/Pcbnew_via_layer_pair_dialog.png)
:::
::::

::: paragraph
When a via is placed the working (active) layer is automatically
switched to the alternate layer of the layer pair used for the vias
(unless \'Shift\' is held when adding the via).
:::

::: paragraph
One can also switch to another active layer by hot keys, and if a track
is in progress, a via will be inserted.
:::
:::::::::::

::::::::::::::::::::::: sect2

### Using the high-contrast mode {#_using_the_high_contrast_mode}

::: paragraph
This mode is entered when the tool (in the left toolbar) is activated:
[![contrast mode](images/icons/contrast_mode.png)]{.image}
:::

::: paragraph
When using this mode, the active layer is displayed like in the normal
mode, but all others layers are displayed in gray color.
:::

::: paragraph
There are two useful cases:
:::

:::::::::: sect3

#### Copper layers in high-contrast mode {#_copper_layers_in_high_contrast_mode}

::: paragraph
When a board uses more than four layers, this option allows the active
copper layer to be seen more easily:
:::

::: paragraph
**Normal mode** (back side copper layer active):
:::

:::: imageblock
::: content
![Pcbnew copper layers contrast
normal](images/Pcbnew_copper_layers_contrast_normal.png)
:::
::::

::: paragraph
**High-contrast mode** (back side copper layer active):
:::

:::: imageblock
::: content
![Pcbnew copper layers contrast
high](images/Pcbnew_copper_layers_contrast_high.png)
:::
::::
::::::::::

::::::::::: sect3

#### Technical layers {#_technical_layers}

::: paragraph
The other case is when it is necessary to examine solder paste layers
and solder mask layers which are usually not displayed.
:::

::: paragraph
Masks on pads are displayed if this mode is active.
:::

::: paragraph
**Normal mode** (front side solder mask layer active):
:::

:::: imageblock
::: content
![Pcbnew technical layers contrast
normal](images/Pcbnew_technical_layers_contrast_normal.png)
:::
::::

::: paragraph
**High-contrast mode** (front side solder mask layer active):
:::

:::: imageblock
::: content
![Pcbnew technical layers contrast
high](images/Pcbnew_technical_layers_contrast_high.png)
:::
::::
:::::::::::
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint placement {#_footprint_placement}

::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2

### Assisted placement {#_assisted_placement}

::: paragraph
Whilst moving footprints the footprint ratsnest (the net connections)
can be displayed to assist the placement. To enable this the icon
[![modratsnest](images/icons/modratsnest.png)]{.image} of the left
toolbar must be activated.
:::
::::

:::::::::: sect2

### Manual placement {#_manual_placement}

::: paragraph
Select the footprint with the right mouse button then choose the Move
command from the menu. Move the footprint to the required position and
place it with the left mouse button. If required the selected footprint
can also be rotated, inverted or edited. Select Cancel from the menu (or
press the Esc key) to abort.
:::

::: paragraph
Here you can see the display of the footprint ratsnest during a move:
:::

:::: imageblock
::: content
![Pcbnew ratsnest during move](images/Pcbnew_ratsnest_during_move.png)
:::
::::

::: paragraph
The circuit once all the footprints are placed may be as shown:
:::

:::: imageblock
::: content
![Pcbnew circuit after
placement](images/Pcbnew_circuit_after_placement.png)
:::
::::
::::::::::

:::::::::::::: sect2

### Automatic Footprint Distribution {#_automatic_footprint_distribution}

::: paragraph
Generally speaking, footprints can only be moved if they have not been
\"Fixed\". This attribute can be turned on and off from the pop-up
window (click right mouse button over footprint) whilst in Footprint
Mode, or through the Edit Footprint Menu.
:::

::: paragraph
As stated in the last chapter, new footprints loaded during the reading
of the netlist appear piled up at a single location on the board. Pcbnew
allows an automatic distribution of the footprints to make manual
selection and placement easier.
:::

::: ulist

- Select the option \"Footprint Mode\" (Icon [![mode
  module](images/icons/mode_module.png)]{.image} on the upper toolbar).

- The pop-up window activated by the right mouse button becomes:
:::

::: paragraph
If there is a footprint under the cursor:
:::

:::: imageblock
::: content
![Pcbnew context module mode module under
cursor](images/Pcbnew_context_module_mode_module_under_cursor.png)
:::
::::

::: paragraph
If there is nothing under the cursor:
:::

:::: imageblock
::: content
![Pcbnew context module mode no module under
cursor](images/Pcbnew_context_module_mode_no_module_under_cursor.png)
:::
::::

::: paragraph
In both cases the following commands are available:
:::

::: ulist

- **Spread out All Footprints** allows the automatic distribution of all
  the footprints not Fixed. This is generally used after the first
  reading of a netlist.

- **Spread out Footprints not Already on Board** allows the automatic
  distribution of the footprints which have not been placed already
  within the PCB outline. This command requires that an outline of the
  board has been drawn to determine which footprints can be
  automatically distributed.
:::
::::::::::::::

:::::::::::::::::::::: sect2

### Automatic placement of footprints {#_automatic_placement_of_footprints}

::::: sect3

#### Characteristics of the automatic placer {#_characteristics_of_the_automatic_placer}

::: paragraph
The automatic placement feature allows the placement of footprints onto
the 2 faces of the circuit board (however switching a footprint onto the
copper layer is not automatic).
:::

::: paragraph
It also seeks the best orientation (0, 90, -90, 180 degrees) of the
footprint. The placement is made according to an optimization algorithm,
which seeks to minimize the length of the ratsnest, and which seeks to
create space between the larger footprints with many pads. The order of
placement is optimized to initially place these larger footprints with
many pads.
:::
:::::

:::::::::: sect3

#### Preparation {#_preparation}

::: paragraph
Pcbnew can thus place the footprints automatically, however it is
necessary to guide this placement, because no software can guess what
the user wants to achieve.
:::

::: paragraph
Before an automatic placement is carried out one must:
:::

::: ulist

- Create the outline of the board (It can be complex, but it must be
  closed if the form is not rectangular).

- Manually place the components whose positions are imposed (Connectors,
  clamp holes, etc).

- Similarly, certain SMD footprints and critical components (large
  footprints for example) must be on a specific side or position on the
  board and this must be done manually.

- Having completed any manual placement these footprints must be
  \"Fixed\" to prevent them being moved. With the Footprint Mode icon
  [![mode module](images/icons/mode_module.png)]{.image} selected right
  click on the footprint and pick \"Fix Footprint\" on the Pop-up menu.
  This can also be done through the Edit/Footprint Pop-up menu.

- Automatic placement can then be carried out. With the Footprint Mode
  icon selected, right click and select Glob(al) Move and Place - then
  Autoplace All Footprints.
:::

::: paragraph
During automatic placement, if required, Pcbnew can optimize the
orientation of the footprints. However rotation will only be attempted
if this has been authorized for the footprint (see Edit Footprint
Options).
:::

::: paragraph
Usually resistors and non-polarized capacitors are authorized for 180
degrees rotation. Some footprints (small transistors for example) can be
authorized for +/- 90 and 180 degrees rotation.
:::

::: paragraph
For each footprint one slider authorizes 90 degree Rot(ation) and a
second slider authorizes 180 degree Rot(ation). A setting of 0 prevents
rotation, a setting of 10 authorizes it, and an intermediate value
indicates a preference for/against rotation.
:::

::: paragraph
The rotation authorization can be done by editing the footprint once it
is placed on the board. However it is preferable to set the required
options to the footprint in the library as these settings will then be
inherited each time the footprint is used.
:::
::::::::::

:::::: sect3

#### Interactive auto-placement {#_interactive_auto_placement}

::: paragraph
It may be necessary during automatic placement to stop (press Esc key)
and manually re-position a footprint. Using the command Autoplace Next
Footprint will restart the autoplacement from the point at which it was
stopped.
:::

::: paragraph
The command Autoplace new footprints allows the automatic placement of
the footprints which have not been placed already within the PCB
outline. It will not move those within the PCB outline even if they are
not \"fixed\".
:::

::: paragraph
The command Autoplace Footprint makes it possible to execute an
autoplacement on the footprint pointed to by the mouse, even if its
\'fixed\' attribute is active.
:::
::::::

:::::: sect3

#### Additional note {#_additional_note}

::: paragraph
Pcbnew automatically determines the possible zone of placement of the
footprints by respecting the shape of the board outline, which is not
necessarily rectangular (It can be round, or have cutouts, etc).
:::

::: paragraph
If the board is not rectangular, the outline must be closed, so that
Pcbnew can determine what is inside and what is outside the outline. In
the same way, if there are internal cutouts, their outline will have to
be closed.
:::

::: paragraph
Pcbnew calculates the possible zone of placement of the footprints using
the outline of the board, then passes each footprint in turn over this
area in order to determine the optimum position at which to place it.
:::
::::::
::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint Editor - Creating and Editing Footprints {#_footprint_editor_creating_and_editing_footprints}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::::: sect2

### Footprint Editor Overview {#_footprint_editor_overview}

::: paragraph
The footprint editor is used for editing and creating PCB footprints.
This includes:
:::

::: ulist

- Adding and removing pads.

- Changing pad properties (shape, layer), for individual pads or for all
  the pads in a footprint.

- Adding and editing graphic elements (contours, text).

- Editing fields (value, reference, etc.).

- Editing the associated documentation (description, keywords).
:::
:::::

::::::::::::: sect2

### Footprint Elements {#_footprint_elements}

::: paragraph
A footprint is the physical representation (footprint) of the part to be
inserted in the PCB and it must be linked to the relative component in
your schematic. Each footprint includes three different elements:
:::

::: ulist

- The pads.

- Graphical contours and text.

- Fields.
:::

::: paragraph
In addition, a number of other parameters must be correctly defined if
the auto-placement function will be used. The same holds for the
generation of auto-insertion files.
:::

::::: sect3

#### Pads {#_pads}

::: paragraph
Two pad properties are important:
:::

::: ulist

- Geometry (shape, layers, drill holes).

- The pad number, which is constituted by up to four alphanumeric
  characters. Thus, the following are all valid pad numbers: 1, 45 and
  9999, but also AA56 and ANOD. The pad number must be identical to that
  of the corresponding pin number in the schematic, because it defines
  the matching pin and pad numbers that Pcbnew links pins and pads with.
:::
:::::

:::: sect3

#### Contours {#_contours}

::: paragraph
Graphical contours are used to draw the physical shape of the footprint.
Several different types of contour are available: lines, circles, arcs,
and text. Contours have no electrical significance, they are simply
graphical aids.
:::
::::

:::: sect3

#### Fields {#_fields}

::: paragraph
These are text elements associated with a footprint. Two are obligatory
and always present: the reference field and the value field. These are
automatically read and updated by Pcbnew when a netlist is read during
the loading of footprints into your board. The reference is replaced by
the appropriate schematic reference (U1, IC3, etc.). The value is
replaced by the value of the corresponding part in the schematic (47K,
74LS02, etc.). Other fields can be added and these will behave like
graphical text.
:::
::::
:::::::::::::

::::: sect2

### Starting Footprint Editor and Selecting a Footprint to Edit {#_starting_footprint_editor_and_selecting_a_footprint_to_edit}

::: paragraph
Footprint Editor can be started in two ways:
:::

::: ulist

- Directly via the [![module
  editor](images/icons/module_editor.png)]{.image} icon from the main
  toolbar of Pcbnew. This allows the creation or modification of a
  footprint in the library.

- Double-clicking a footprint will launch the \'Footprint Properties\'
  menu, which offers a \'Go to Footprint Editor\' button. If this option
  is used, the footprint from the board will be loaded into the editor,
  for modification or for saving.
:::
:::::

:::::::::::: sect2

### Footprint Editor Toolbars {#_footprint_editor_toolbars}

::: paragraph
Calling Footprint Editor will launch a new window that looks like this:
:::

:::: imageblock
::: content
![Modedit main window](images/Modedit_main_window.png)
:::
::::

:::::: sect3

#### Edit Toolbar (right-hand side) {#_edit_toolbar_right_hand_side}

::: paragraph
This toolbar contains tools for:
:::

::: ulist

- Placing pads.

- Adding graphic elements (contours, text).

- Positioning the anchor.

- Deleting elements.
:::

::: paragraph
The specific functions are the following:
:::

+---------------------------------------------------+--------------------------------------------------------+
| [![cursor](images/icons/cursor.png)]{.image}      | No tool.                                               |
+---------------------------------------------------+--------------------------------------------------------+
| [![pad](images/icons/pad.png)]{.image}            | Add pads.                                              |
+---------------------------------------------------+--------------------------------------------------------+
| [![add                                            | Draw line segments and polygons.                       |
| polygon](images/icons/add_polygon.png)]{.image}   |                                                        |
+---------------------------------------------------+--------------------------------------------------------+
| [![add                                            | Draw circles.                                          |
| circle](images/icons/add_circle.png)]{.image}     |                                                        |
+---------------------------------------------------+--------------------------------------------------------+
| [![add arc](images/icons/add_arc.png)]{.image}    | Draw circular arcs.                                    |
+---------------------------------------------------+--------------------------------------------------------+
| [![text](images/icons/text.png)]{.image}          | Add graphical text (fields are not managed by this     |
|                                                   | tool).                                                 |
+---------------------------------------------------+--------------------------------------------------------+
| [![anchor](images/icons/anchor.png)]{.image}      | Position the footprint anchor.                         |
+---------------------------------------------------+--------------------------------------------------------+
| [![delete](images/icons/delete.png)]{.image}      | Delete elements.                                       |
+---------------------------------------------------+--------------------------------------------------------+
| [![grid select                                    | Grid origin. (grid offset). Useful for placement of    |
| axis](images/icons/grid_select_axis.png)]{.image} | pads. The grid origin can be put on a given location   |
|                                                   | (the first pad to place), and after the grid size can  |
|                                                   | be set to the pad pitch. Placing pads is therefore     |
|                                                   | very easy                                              |
+---------------------------------------------------+--------------------------------------------------------+
::::::

:::: sect3

#### Display Toolbar (left-hand side) {#_display_toolbar_left_hand_side}

::: paragraph
These tools manage the display options in Footprint Editor:
:::

+------------------------------------------------+--------------------------------------------------------+
| [![grid](images/icons/grid.png)]{.image}       | Display the grid.                                      |
+------------------------------------------------+--------------------------------------------------------+
| [![polar                                       | Display polar coordinates.                             |
| coord](images/icons/polar_coord.png)]{.image}  |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![unit mm](images/icons/unit_mm.png)]{.image} | Use units of mm or inch                                |
| [![unit                                        |                                                        |
| inch](images/icons/unit_inch.png)]{.image}     |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![cursor                                      | Toggle cursor crosshair shape                          |
| shape](images/icons/cursor_shape.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![pad                                         | Display pad in outline mode.                           |
| sketch](images/icons/pad_sketch.png)]{.image}  |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![text                                        | Display text in outline mode.                          |
| sketch](images/icons/text_sketch.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![show mod                                    | Display contours in outline mode.                      |
| edge](images/icons/show_mod_edge.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
| [![contrast                                    | Toggle high-contrast mode                              |
| mode](images/icons/contrast_mode.png)]{.image} |                                                        |
+------------------------------------------------+--------------------------------------------------------+
::::
::::::::::::

::::::::::::: sect2

### Context Menus {#_context_menus}

::: paragraph
The right mouse button calls up menus that depend upon the element
beneath the cursor.
:::

::: paragraph
The context menu for editing footprint parameters:
:::

:::: imageblock
::: content
![Modedit context menu module
parameters](images/Modedit_context_menu_module_parameters.png)
:::
::::

::: paragraph
The context menu for editing pads:
:::

:::: imageblock
::: content
![Modedit context menu pads](images/Modedit_context_menu_pads.png)
:::
::::

::: paragraph
The context menu for editing graphic elements:
:::

:::: imageblock
::: content
![Modedit context menu
graphics](images/Modedit_context_menu_graphics.png)
:::
::::
:::::::::::::

::::::: sect2

### Footprint Properties Dialog {#_footprint_properties_dialog}

::: paragraph
This dialog can be launched when the cursor is over a footprint by
clicking on the right mouse button and then selecting \'Edit
Footprint\'.
:::

:::: imageblock
::: content
![Modedit module properties
dialog](images/Modedit_module_properties_dialog.png)
:::
::::

::: paragraph
The dialog can be used to define the main footprint parameters.
:::
:::::::

:::::::::: sect2

### Creating a New Footprint {#_creating_a_new_footprint}

::: paragraph
A new footprint can be created via the button [![new
footprint](images/icons/new_footprint.png)]{.image}. The name of the new
footprint will be requested. This will be the name by which the
footprint will be identified in the library.
:::

::: paragraph
This text also serves as the footprint value, which is ultimately
replaced by the real value (100 µF_16 V, 100 Ω_0.5 W, ...​).
:::

::: paragraph
The new footprint will require:
:::

::: ulist

- Contours (and possibly graphic text).

- Pads.

- A value (hidden text that is replaced by the true value when used).
:::

::: paragraph
Alternative method:
:::

::: paragraph
When a new footprint is similar to an existing footprint in a library or
a circuit board, an alternative and quicker method of creating the new
footprint is as follows:
:::

::: ulist

- Load the similar footprint ([![load module
  lib](images/icons/load_module_lib.png)]{.image}, [![load module
  board](images/icons/load_module_board.png)]{.image} or [![import
  module](images/icons/import_module.png)]{.image}).

- Modify the \"Footprint Name in Library\" field in order to generate a
  new identifier (name).

- Edit and save the new footprint.
:::
::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: sect2

### Adding and Editing Pads {#_adding_and_editing_pads}

::: paragraph
Once a footprint has been created, pads can be added, deleted or
modified. Modification of pads can be local, affecting only the pad
under the cursor, or global, affecting all pads of the footprint.
:::

::::: sect3

#### Adding Pads {#_adding_pads}

::: paragraph
Select the [![pad](images/icons/pad.png)]{.image} icon from the right
hand toolbar. Pads can be added by clicking in the desired position with
the left mouse button. Pad properties are predefined in the pad
properties menu.
:::

::: paragraph
Do not forget to enter the pad number.
:::
:::::

:::::::::::::::::::::::::::: sect3

#### Setting Pad Properties {#_setting_pad_properties}

::: paragraph
This can be done in three different ways:
:::

::: ulist

- Selecting the [![options pad](images/icons/options_pad.png)]{.image}
  icon from the horizontal toolbar.

- Clicking on an existing pad and selecting \'Edit Pad\'. The pad's
  settings can then be edited.

- Clicking on an existing pad and selecting \'Export Pad Settings\'. In
  this case, the geometrical properties of the selected pad will become
  the default pad properties.
:::

::: paragraph
In the first two cases, the following dialog window will be displayed:
:::

:::: imageblock
::: content
![Modedit pad properties
dialog](images/Modedit_pad_properties_dialog.png)
:::
::::

::: paragraph
Care should be taken to define correctly the layers to which the pad
will belong. In particular, although copper layers are easy to define,
the management of non-copper layers (solder mask, solder pads...​) is
equally important for circuit manufacture and documentation.
:::

::: paragraph
The Pad Type selector triggers an automatic selection of layers that is
generally sufficient.
:::

:::: sect4

##### Rectangular Pads {#_rectangular_pads}

::: paragraph
For SMD footprints of the VQFP/PQFP type which have rectangular pads on
all four sides (both horizontal and vertical) it is recommended to use
just one shape (for example, a horizontal rectangle) and to place it
with different orientations (0 for horizontal and 90 degrees for
vertical). Global resizing of pads can then be done in a single
operation.
:::
::::

:::: sect4

##### Rotate Pads {#_rotate_pads}

::: paragraph
Rotations of -90 or -180 are only required for trapezoidal pads used in
microwave footprints.
:::
::::

:::::::: sect4

##### Non-plated Through Hole Pads {#_non_plated_through_hole_pads}

::: paragraph
Pads can be defined as Non-Plated Through Hole pads (NPTH pads).
:::

::: paragraph
These pads must be defined on one or all copper layers (obviously, the
hole exists on all copper layers).
:::

::: paragraph
This requirement allows you to define specific clearance parameters (
for instance clearance for a screw).
:::

::: paragraph
When the pad hole size is the same as the pad size, for a round or oval
pad, this pad is NOT plotted on copper layers in GERBER files.
:::

::: paragraph
These pads are used for mechanical purposes, therefore no pad name or
net name is allowed. A connection to a net is not possible.
:::
::::::::

:::::: sect4

##### Offset Parameter {#_offset_parameter}

::: paragraph
Pad 3 has an offset Y = 15 mils:
:::

:::: imageblock
::: content
![Modedit pad offset example](images/Modedit_pad_offset_example.png)
:::
::::
::::::

:::::: sect4

##### Delta Parameter (trapezoidal pads) {#_delta_parameter_trapezoidal_pads}

::: paragraph
Pad 1 has its parameter Delta X = 10 mils
:::

:::: imageblock
::: content
![Modedit pad delta example](images/Modedit_pad_delta_example.png)
:::
::::
::::::
::::::::::::::::::::::::::::

:::::::::: sect3

#### Setting Clearances for Solder Mask and Solder Paste Layers {#_setting_clearances_for_solder_mask_and_solder_paste_layers}

::: paragraph
When defining pads containing copper layers, KiCad creates solder mask
and solder paste layers based on a fixed clearance and/or a ratio of the
pad geometry. The non-zero settings used to calculate the final pad size
is based on the following order of precedence:
:::

::: ulist

- Pad setting

- Footprint setting

- Global setting
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Note                              | The solder mask pad shape is      |
| :::                               | usually bigger than the pad       |
|                                   | itself. So the clearance value is |
|                                   | positive. The solder paste mask   |
|                                   | pad shape is usually smaller than |
|                                   | the pad itself. So the clearance  |
|                                   | value is negative.                |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

:::::: sect4

##### Solder Paste Settings {#_solder_paste_settings}

::: paragraph
Two settings are used to calculate the solder paste aperture:
:::

::: ulist

- A fixed clearance setting.

- A percentage of the pad size.
:::

::: paragraph
The the final value is the product of the ratio setting and the
clearance setting.
:::
::::::
::::::::::

::::::::::: sect3

#### Pads Not on Copper Layers {#_pads_not_on_copper_layers}

::: paragraph
There is second method for creating pads that do not have any copper
layers defined. These pads are commonly referred to as aperture pads and
can be use to create custom apertures not based on the outline of a
copper pad geometry. This method was introduced in version 5.0.0-rc2.
Pads defined without any copper layers ignore the global and footprint
level settings and only use the pad level settings.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: paragraph                     |
| Warning                           | Pads without copper layers        |
| :::                               | defined prior to version          |
|                                   | 5.0.0-rc2 were plotted using      |
|                                   | precedence defined above with the |
|                                   | global and footprint settings.    |
|                                   | Adjustments will have to be made  |
|                                   | for any boards designed prior to  |
|                                   | this version in order to achieve  |
|                                   | the same output plots.            |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
Footprint level settings:
:::

:::: imageblock
::: content
![Modedit footprint level pad
settings](images/Modedit_footprint_level_pad_settings.png)
:::
::::

::: paragraph
Pad level settings:
:::

:::: imageblock
::: content
![Modedit pad level pad
settings](images/Modedit_pad_level_pad_settings.png)
:::
::::
:::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

::::::: sect2

### Fields Properties {#_fields_properties}

::: paragraph
There are at least two fields: reference and value.
:::

::: paragraph
Their parameters (attribute, size, width) must be updated. You can
access the dialog box from the pop-up menu, by double clicking on the
field, or by the footprint properties dialog box:
:::

:::: imageblock
::: content
![Modedit footprint text
properties](images/Modedit_footprint_text_properties.png)
:::
::::
:::::::

::::::::: sect2

### Automatic Placement of a Footprint {#_automatic_placement_of_a_footprint}

::: paragraph
If the user wishes to exploit the full capabilities of the
auto-placement functions, it is necessary to define the allowed
orientations of the footprint (Footprint Properties dialog).
:::

:::: imageblock
::: content
![Modedit module autoplace
settings](images/Modedit_module_autoplace_settings.png)
:::
::::

::: paragraph
Usually, rotation of 180 degrees is permitted for resistors,
non-polarized capacitors and other symmetrical elements.
:::

::: paragraph
Some footprints (small transistors, for example) are often permitted to
rotate by +/- 90 or 180 degrees. By default, a new footprint will have
its rotation permissions set to zero. This can be adjusted according to
the following rule:
:::

::: paragraph
A value of 0 makes rotation impossible, 10 allows it completely, and any
intermediate value represents a limited rotation. For example, a
resistor might have a permission of 10 to rotate 180 degrees
(unrestrained) and a permission of 5 for a +/- 90 degree rotation
(allowed, but discouraged).
:::
:::::::::

::::::: sect2

### Attributes {#_attributes}

::: paragraph
The attributes window is the following:
:::

:::: imageblock
::: content
![Modedit module attributes](images/Modedit_module_attributes.png)
:::
::::

::: ulist

- Normal is the standard attribute.

- Normal+Insert indicates that the footprint must appear in the
  automatic insertion file (for automatic insertion machines). This
  attribute is most useful for surface mount components (SMDs).

- Virtual indicates that a component is directly formed by the circuit
  board. Examples would be edge connectors or inductors created by a
  particular track shape (as sometimes seen in microwave footprints).
:::
:::::::

::::::::::: sect2

### Documenting Footprints in a Library {#_documenting_footprints_in_a_library}

::: paragraph
It is strongly recommended to document newly created footprints, in
order to facilitate their rapid and accurate retrieval. Who is able to
recall the multiple pin-out variants of a TO92 footprint?
:::

::: paragraph
The Footprint Properties dialog offers a simple and yet powerful means
for documentation generation.
:::

:::: imageblock
::: content
![Modedit module properties documentation
fields](images/Modedit_module_properties_documentation_fields.png)
:::
::::

::: paragraph
This menu allows:
:::

::: ulist

- The entry of a comment line (description).

- Multiple keywords.
:::

::: paragraph
The comment line is displayed with the component list in CvPcb and in
the footprint selection menus in Pcbnew. The keywords can be used to
restrict searches to those parts possessing the given keywords.
:::

::: paragraph
Thus, while using the load footprint command (icon in the right-hand
toolbar in Pcbnew), it is possible to type the text `=TO220` into the
dialog box to have Pcbnew display a list of the footprints possessing
the keyword `TO220`
:::
:::::::::::

:::::::::::::::::::::::::::: sect2

### 3-Dimensional Visualization {#_3_dimensional_visualization}

::: paragraph
A footprint may be associated with a file containing a three-dimensional
representation of the component. In order to associate a footprint with
a model file, select the *3D Settings* tab as shown below.
:::

::::: {#img-Modedit_module_3d_options .imageblock}

::: content
![Modedit module 3d options](images/Modedit_module_3d_options.png)
:::

::: title
Figure 1. 3D Model selection interface
:::
:::::

::: paragraph
The buttons on the right have the following functions:
:::

::: ulist

- **Add 3D Shape** shows a 3D file selection dialog and creates a new
  model entry for the component.

- **Remove 3D Shape** deletes the selected model entry.

- **Edit Filename** shows a text editor for manual entry of the model
  file name.

- **Configure Paths** shows a configuration dialog which allows the user
  to edit the list of path aliases and alias values.
:::

::: paragraph
The *3D Settings* tab contains a panel with a preview of the selected
model and the scale, offset, and rotation data for the model.
:::

::: paragraph
Scale values are useful for visualization formats such as VRML1, VRML2,
and X3D. Since the model may have been produced by any number of
VRML/X3D editors or exporters and VRML does not enforce a unit of length
for the models, users can enter an appropriate scale value to ensure
that the model appears as it should within the 3DViewer. Some users
employ a simple VRML box as a generic model for components and select
scale values so that the box has the correct size to represent the
component. For Mechanical CAD (MCAD) models the scale values should be
left at unity. MCAD formats always specify a unit length and any
exporters which make use of MCAD data formats will ignore the scale
values. However the 3DViewer will always apply the scale values; if
scale values other than unity are used with MCAD models, the output of
the 3DViewer will differ from any exported MCAD models such as IDF.
:::

::: paragraph
Offset and Rotation values are typically required to align a 3D model
with a footprint. Due to differences in 3D modeling software as well as
differences in how users construct a model, in the vast majority of
cases it is necessary for users to enter Offset and Rotation values to
achieve the desired positioning of a 3D model. The Rotation values are
given in degrees and are applied successively in the order ZYX; the
convention used is that a positive angle results in a clockwise rotation
of the part when viewing from the positive position of the axis towards
the origin.
:::

::: paragraph
KiCad supports 3D model formats via a plugin system and support is
provided for the visual model formats VRML1, VRML2, and X3D as well as
the MCAD format IDF. The MCAD formats IGES and STEP are supported via
the OCE Plugin which requires a suitable version of the OpenCascade or
OpenCascade Community Edition (OCE) software.
:::

::::::::::::::::: sect3

#### 3D Model Paths {#_3d_model_paths}

::: paragraph
In the past KiCad used a fixed path to a directory of 3D models and
later relied on the *KISYS3DMOD* environment variable to specify the
location of the model directory. Other base directories for models could
be specified by using additional environment variables. The current
version of KiCad has a specialized *alias* system for handling 3D model
names. The aim of the new file name management system (filename
resolution system) is to provide a scheme which is compatible with
earlier versions of KiCad while offering a more flexible mechanism for
specifying 3D model file names and improving the ability to share
project files.
:::

::: paragraph
Due to the requirement to support previous schemes while offering a
flexible new scheme for finding 3D models, there are two distinct
methods for specifying base search paths for 3D models.
:::

::: paragraph
In order to maintain the legibility of the *kicad_pcb* and *pretty* data
files, KiCad prefers to use filenames which have been shortened via the
use of environment variables (old method) or aliases (new method). Since
setting environment variables can be cumbersome especially on GUI-based
operating systems, the environment variable scheme for supporting model
search paths has been extended to make use of KiCad's existing
internally defined *Path Configuration* dialog. This dialog is available
via the *Preferences→Configure Paths* menu and is shown below. Setting
additional paths within this dialog will extend the search paths used to
find 3D model files. The dialog does not actually set environment
variables but the filename resolution system acts as if it does; in
cases where an actual environment variable with the same name is
defined, the environment variable's value overrides any internally
defined values. File names relative to these defined variables begin
with *\${MY_ENV_VAR}* where *MY_ENV_VAR* is a variable defined via the
*Path Configuration* dialog or an actual environment variable.
:::

::::: {#img-Modedit_internal_path_config .imageblock}

::: content
![Modedit internal path config](images/Modedit_internal_path_config.png)
:::

::: title
Figure 2. KiCad Path Configuration dialog
:::
:::::

::: paragraph
The newer scheme to support shortened file names is the *alias* system.
In this system a path begins with the string *:my alias:* where *my
alias* is a text string which is preferably chosen to be short while
also being significant to the user; for example an alias to a directory
containing the official KiCad models may have an alias *Official Models*
while your personal model collection may have an alias *My Models*. The
aliases may be set up by clicking on the **Configure Paths** button
within the **3D Settings** tab shown previously. The alias configuration
dialog is shown below.
:::

::::: {#img-Modedit_alias_path_config .imageblock}

::: content
![Modedit alias path config](images/Modedit_alias_path_config.png)
:::

::: title
Figure 3. KiCad Alias Configuration dialog
:::
:::::

::: paragraph
3D model files can be selected by clicking **Add 3D Shape** to display
the 3D Model Browser shown below. The model browser provides a 3D
preview, file filter, and a drop-down path selector which contains the
current list of search paths defined via environment variables or
aliases. Depending on the model size and complexity it may take a few
seconds for a model to be displayed when it is selected. In an extreme
case a BGA package model which was used during testing took around 12
seconds to display.
:::

::::: {#img-Modedit_3D_file_browser .imageblock}

::: content
![Modedit 3D file browser](images/Modedit_3D_file_browser.png)
:::

::: title
Figure 4. KiCad 3D File Browser
:::
:::::
:::::::::::::::::
::::::::::::::::::::::::::::

:::::: sect2

### Saving a Footprint into the Active Library {#_saving_a_footprint_into_the_active_library}

::: paragraph
The save command (modification of the file of the active library) is
activated by the [![save
library](images/icons/save_library.png)]{.image} button.
:::

::: paragraph
If a footprint of the same name exists (an older version), it will be
overwritten. Because it is important to be able to have confidence in
the library footprints, it is worth double-checking the footprint for
errors before saving.
:::

::: paragraph
Before saving, it is also recommended to change the reference or value
of the footprint to be equal to the library name of the footprint.
:::
::::::

:::: sect2

### Saving a footprint to the board {#_saving_a_footprint_to_the_board}

::: paragraph
If the edited footprint comes from the current board, the button
[![update module board](images/icons/update_module_board.png)]{.image}
will update this footprint on the board.
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Advanced PCB editing tools {#_advanced_pcb_editing_tools}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
There are some more advanced editing tools available in Pcbnew and
Footprint Editor, which can help you to efficiently lay out components
on the canvas.
:::

::::: sect2

### Duplicating items {#_duplicating_items}

::: paragraph
Duplication is a method to clone an item and pick it up in the same
action. It is broadly similar to copy-and-pasting, but it allows you to
\"sprinkle\" components over the PCB and it allows you to manually lay
out components using the \"Move Exact\" tool (see below) more easily.
:::

::: paragraph
Duplication is done by using the hotkey (which defaults to Ctrl-D) or
the duplicate item option in the context menu, icon
[![duplicate](images/icons/duplicate.png)]{.image}.
:::
:::::

:::::::::::::: sect2

### Moving items exactly {#_moving_items_exactly}

::: paragraph
The \"Move Exact\" tool allows you to move an item (or group of items)
by a certain amount, which can be entered in Cartesian or polar formats
and which can be entered in any supported units. This is useful when it
would otherwise be cumbersome to switch to a different grid, or when a
feature is not spaced according to any existing grids.
:::

::: paragraph
To use this tool, select the items you wish to move and then use either
the hotkey (defaults to Ctrl-M) or the context menu items to invoke the
dialog. You can also invoke the dialog with the hotkey when moving or
duplicating items, which can make it easy to repeatedly apply an offset
to multiple components.
:::

::: paragraph
Move exact with Cartesian move vector entry
:::

:::: imageblock
::: content
![Pcbnew move exact cartesian](images/Pcbnew_move_exact_cartesian.png)
:::
::::

::: paragraph
Move exact with polar move vector entry
:::

:::: imageblock
::: content
![Pcbnew move exact polar](images/Pcbnew_move_exact_polar.png)
:::
::::

::: paragraph
The checkbox allows you to switch between Cartesian and polar
co-ordinate systems. Whatever is currently in the form will be converted
automatically to the other system.
:::

::: paragraph
Then you enter the desired move vector. You can use the units indicated
by the labels (\"mm\" in the images above) or you can specify the units
yourself (e.g. \"1 in\" for an inch, or \"2 rad\" for 2 radians).
:::

::: paragraph
Pressing OK will apply the translation to the selection, and cancel will
close the dialog and the items will not be moved. If OK is pressed, the
move vector will be saved and pre-filled next time the dialog is opened,
which allows repeated application of the same vector to multiple
objects.
:::
::::::::::::::

:::::::::::::::::::::::::::::::::::: sect2

### Array tools {#_array_tools}

::: paragraph
Pcbnew and the Footprint Editor both have assistants for creating arrays
of features and components, which can be used to easily and accurately
lay out repetitive elements on PCBs and in footprints.
:::

:::::: sect3

#### Activating the array tool {#_activating_the_array_tool}

::: paragraph
The array tool acts on the component under the cursor, or, in GAL mode,
on a selection. It can be accessed either via the context menu, icon
[![array](images/icons/array.png)]{.image} for the selection or by a
keyboard shortcut (defaults to Ctrl-N).
:::

::: paragraph
The array tool is presented as a dialog window, with a pane for the
types of arrays. There are two types of arrays supported so far: grid,
and circular.
:::

::: paragraph
Each type of array can be fully specified on the respective panes.
Geometric options (how the grid is laid out) go on the left; numbering
options (including how the numbers progress across the grid) on the
right.
:::
::::::

:::::::::::::::::::::: sect3

#### Grid arrays {#_grid_arrays}

::: paragraph
Grid arrays are arrays that lay components out according to a
2-dimensional square grid. This kind of array can also produce a linear
array by only laying out a single row or column.
:::

::: paragraph
The settings dialog for grid arrays look like this:
:::

:::: imageblock
::: content
![Pcbnew array dialog grid](images/Pcbnew_array_dialog_grid.png)
:::
::::

::::::::::::::: sect4

##### Geometric options {#_geometric_options}

::: paragraph
The geometric options are as follow:
:::

::: ulist

- **Horizontal count**: the number of \"columns\" in the grid.

- **Vertical count**: the number of \"rows\" in the grid.

- **Horizontal spacing**: the horizontal distance from item to the item
  in the same row and next column. If this is negative, the grid
  progresses from right to left.

- **Vertical spacing**: the vertical distance from one item to the item
  in the same column and the next row. If this is negative, the grid
  progress bottom to top.

- **Horizontal offset**: start each row this distance to the right of
  the previous one

- **Vertical offset**: start each column this distance below the
  previous one
:::

::::: imageblock
::: content
![Pcbnew array grid offsets](images/Pcbnew_array_grid_offsets.png)
:::

::: title
Figure 1. 3x3 grid with x and y offsets
:::
:::::

::: ulist

- **Stagger**: add an offset to every set of \"n\" rows/columns, with
  each row progressing by 1/n'th of the relevant spacing dimension:
:::

::::: imageblock
::: content
![Pcbnew array grid stagger rows
2](images/Pcbnew_array_grid_stagger_rows_2.png)
:::

::: title
Figure 2. 3x3 grid with a row stagger of 2
:::
:::::

::::: imageblock
::: content
![Pcbnew array grid stagger cols
3](images/Pcbnew_array_grid_stagger_cols_3.png)
:::

::: title
Figure 3. 4x3 grid with a column stagger of 3
:::
:::::
:::::::::::::::

:::: sect4

##### Numbering options {#_numbering_options}

::: ulist

- **Numbering Direction**: Determines whether numbers proceed along rows
  and then moves to the next row, or down columns and then to the next
  column. Note that the direction on numbering is defined by the sign of
  the spacing: a negative spacing will result in right-to-left or
  bottom-to-top numbering.

- **Reverse numbering on alternate rows or columns**: If selected, the
  numbering order (left-to-right or right-to-left, for example) on
  alternate rows or columns. Whether rows or columns alternate depends
  on the numbering direction. This option is useful for packages like
  DIPs where the numbering proceeds up one side and down the other.

- **Restart numbering**: if laying out using items that already have
  numbers, reset to the start, otherwise continue if possible from this
  item's number

- **Numbering Scheme**

  ::: ulist

  - **Continuous**: the numbering just continues across a row/column
    break - if the last item in the first row is numbered \"7\", the
    first item in the second row will be \"8\".

  - **Coordinate**: the numbering uses a two-axis scheme where the
    number is made up of the row and column index. Which one comes first
    (row or column) is determined by the numbering direction.
  :::

- **Axis numberings**: what \"alphabet\" to use to number the axes.
  Choices are

  ::: ulist

  - **Numerals** for normal integer indices

  - **Hexadecimal** for base-16 indexing

  - **Alphabetic, minus IOSQXZ**, a common scheme for electronic
    components, recommended by ASME Y14.35M-1997 sec. 5.2 (previously
    MIL-STD-100 sec. 406.5) to avoid confusion with numerals.

  - **Full alphabet** from A-Z.
  :::
:::
::::
::::::::::::::::::::::

:::::::::: sect3

#### Circular arrays {#_circular_arrays}

::: paragraph
Circular arrays lay out items around a circle or a circular arc. The
circle is defined by the location of the selection (or the centre of a
selected group) and a centre point that is specified. Below is the
circular array configuration dialog:
:::

:::: imageblock
::: content
![Pcbnew array dialog circular](images/Pcbnew_array_dialog_circular.png)
:::
::::

:::: sect4

##### Geometric options {#_geometric_options_2}

::: ulist

- **Horizontal center**, **Vertical center**: The centre of the circle.
  The radius field below will update automatically when you adjust
  these.

- **Angle**: The angular difference between two adjacent items in the
  array. Set this to zero to evenly divide the circle with \"count\"
  elements.

- **Count**: Number of items in the array (including the original item)

- **Rotate**: Rotate each item around its own location. Otherwise, the
  item will be translated but not rotated (for example, a square pad
  will always remain upright if this option is not set).
:::
::::

:::: sect4

##### Numbering options {#_numbering_options_2}

::: paragraph
Circular arrays have only one dimension and a simpler geometry than
grids. The meanings of the available options are the same as for grids.
Items are numbered clockwise - for an anticlockwise array, specify a
negative angle.
:::
::::
::::::::::
::::::::::::::::::::::::::::::::::::

::::::: sect2

### Measurement (ruler) tool {#_measurement_ruler_tool}

::: paragraph
The measurement tool is a linear ruler that can be used to visually
check sizes and spacings on a PCB.
:::

::: paragraph
It is accessible via the calipers icon
[![measurement](images/icons/measurement.png)]{.image} in the right hand
toolbar, in the \"Dimension\" menu and with the hotkey (Ctrl-Shift-M by
default).
:::

::: paragraph
When active, you can draw a temporary ruler over the canvas, which will
be marked with the current units. You can snap to 45-degree angles by
holding the Ctrl key. Units can be changed without leaving the tool
using the ususal hotkey (Ctrl-U by default).
:::

::: paragraph
[![Pcbnew measurement tool](images/Pcbnew_measurement_tool.png)]{.image}
:::
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Creating copper zones {#_creating_copper_zones}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Copper zones are defined by an outline (closed polygon), and can include
holes (closed polygons inside the outline). A zone can be drawn on a
copper layer or alternatively on a technical layer.
:::

::::::::::: sect2

### Creating zones on copper layers {#_creating_zones_on_copper_layers}

::: paragraph
Pad (and track) connections to filled copper areas are checked by the
DRC engine. A zone must be filled (not just created) to connect pads.
Pcbnew currently uses track segments or polygons to fill copper areas.
:::

::: paragraph
Each option has its advantages and its disadvantages, the main
disadvantage being increased screen redraw time on slower machines. The
final result is however the same.
:::

::: paragraph
For calculation time reasons, the zone filling is not recreated after
each change, but only:
:::

::: ulist

- If a filling zone command is executed.

- When a DRC test is performed.
:::

::: paragraph
Copper zones must be filled or refilled after changes in tracks or pads
are made. Copper zones (usually ground and power planes) are usually
attached to a net.
:::

::: paragraph
In order to create a copper zone you should:
:::

::: ulist

- Select parameters (net name, layer...​). Turning on the layer and
  highlighting this net is not mandatory but it is good practice.

- Create the zone limit (If not, the entire board will be filled.).

- Fill the zone.
:::

::: paragraph
Pcbnew tries to fill all zones in one piece, and usually, there will be
no unconnected copper blocks. It can happen that some areas remain
unfilled. Zones having no net are not cleaned and can have insulated
areas.
:::
:::::::::::

:::::::::::::::::::::::::::::::::::::: sect2

### Creating a zone {#_creating_a_zone}

::::::::::::: sect3

#### Creating the limits of a zone {#_creating_the_limits_of_a_zone}

::: paragraph
Use the tool [![add zone](images/icons/add_zone.png)]{.image}. The
active layer must be a copper layer. When clicking to start the zone
outline, the following dialog box will be opened.
:::

:::: imageblock
::: content
![Pcbnew zone properties
dialog](images/Pcbnew_zone_properties_dialog.png)
:::
::::

::: paragraph
You can specify all parameters for this zone:
:::

::: ulist

- Net

- Layer

- Filling options

- Pad options

- Priority level
:::

::: paragraph
Draw the zone limit on this layer. This zone limit is a polygon, created
by left-clicking at each corner. A double-click will end and close the
polygon. If the starting point and ending point are not at the same
coordinate, Pcbnew will add a segment from the end point to the start
point.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - The DRC is active when creating |
| :::                               |   zone outlines.                  |
|                                   |                                   |
|                                   | - A corner which creates a DRC    |
|                                   |   error will not be accepted by   |
|                                   |   Pcbnew.                         |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
In the following image you can see an example of a zone limit (polygon
in thin hatched line):
:::

:::: imageblock
::: content
![Pcbnew zone limit example](images/Pcbnew_zone_limit_example.png)
:::
::::
:::::::::::::

:::::::::::::: sect3

#### Priority level {#_priority_level}

::: paragraph
Sometimes a small zone must be created inside a large zone.
:::

::: paragraph
This is possible if the small zone has a higher priority level than the
large zone.
:::

::: paragraph
Level setting:
:::

:::: imageblock
::: content
![Pcbnew zone priority level
setting](images/Pcbnew_zone_priority_level_setting.png)
:::
::::

::: paragraph
Here is an example:
:::

:::: imageblock
::: content
![Pcbnew zone priority example](images/Pcbnew_zone_priority_example.png)
:::
::::

::: paragraph
After filling:
:::

:::: imageblock
::: content
![Pcbnew zone priority example after
filling](images/Pcbnew_zone_priority_example_after_filling.png)
:::
::::
::::::::::::::

:::::::::::::: sect3

#### Filling the zone {#_filling_the_zone}

::: paragraph
When filling a zone, Pcbnew removes all unconnected copper islands. To
access the zone filling command, right-click on the edge zone.
:::

:::: imageblock
::: content
![Pcbnew zone context menu](images/Pcbnew_zone_context_menu.png)
:::
::::

::: paragraph
Activate the \"Fill Zone\" command. Below is the filling result for a
starting point inside the polygon:
:::

:::: imageblock
::: content
![Pcbnew zone filling result](images/Pcbnew_zone_filling_result.png)
:::
::::

::: paragraph
The polygon is the border of the filling area. You can see a non-filled
area inside the zone, because this area is not accessible:
:::

::: ulist

- A track creates a border, and

- There is no starting point for filling in this area.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | You can use many polygons to      |
| Note                              | create cutout areas. Here you can |
| :::                               | see an example:                   |
+-----------------------------------+-----------------------------------+
:::

:::: imageblock
::: content
![Pcbnew zone filled with
cutout](images/Pcbnew_zone_filled_with_cutout.png)
:::
::::
::::::::::::::
::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::: sect2

### Filling options {#_filling_options}

:::: imageblock
::: content
![Pcbnew zone filling options](images/Pcbnew_zone_filling_options.png)
:::
::::

::: paragraph
When you fill an area, you must choose:
:::

::: ulist

- The mode for filling.

- The clearance and minimum copper thickness.

- How pads are drawn inside the zone (or connected to this zone).

- Thermal relief parameters.
:::

:::: sect3

#### Filling mode {#_filling_mode}

::: paragraph
Zones can be filled using polygons or segments. The result is the same.
If you have problems with polygon mode (slow screen refresh) you should
use segments.
:::
::::

::::: sect3

#### Clearance and minimum copper thickness {#_clearance_and_minimum_copper_thickness}

::: paragraph
A good choice for clearance is a grid that is a bit bigger than the
routing grid. Minimum copper thickness value ensures that there are no
too small copper areas.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | if this value is too large, small |
| Warning                           | shapes like thermal stubs in      |
| :::                               | thermal reliefs cannot be drawn.  |
+-----------------------------------+-----------------------------------+
:::
:::::

::::::::::::: sect3

#### Pad options {#_pad_options}

::: paragraph
Pads of the net can either be included or excluded from the zone, or
connected by thermal reliefs.
:::

::: ulist

- If included, soldering and un-soldering can be very difficult due to
  the high thermal mass of the large copper area.
:::

:::: imageblock
::: content
![Pcbnew zone include pads](images/Pcbnew_zone_include_pads.png)
:::
::::

::: ulist

- If excluded, the connection to the zone will not be very good.

  ::: ulist

  - The zone can be filled only if tracks exists to connect zone areas.

  - Pads must be connected by tracks.
  :::
:::

:::: imageblock
::: content
![Pcbnew zone exclude pads](images/Pcbnew_zone_exclude_pads.png)
:::
::::

::: ulist

- A thermal relief is a good compromise.

  ::: ulist

  - Pad is connected by 4 track segments.

  - The segment width is the current value used for the track width.
  :::
:::

:::: imageblock
::: content
![Pcbnew zone thermal relief](images/Pcbnew_zone_thermal_relief.png)
:::
::::
:::::::::::::

:::::::: sect3

#### Thermal relief parameters {#_thermal_relief_parameters}

:::: imageblock
::: content
![Pcbnew thermal relief
settings](images/Pcbnew_thermal_relief_settings.png)
:::
::::

::: paragraph
You can set two parameters for thermal reliefs:
:::

:::: imageblock
::: content
![Pcbnew thermal relief
parameters](images/Pcbnew_thermal_relief_parameters.png)
:::
::::
::::::::

::::: sect3

#### Choice of parameters {#_choice_of_parameters}

::: paragraph
The copper width value for thermal reliefs must be bigger than the
minimum thickness value for the copper zone. If not, they cannot be
drawn.
:::

::: paragraph
Additionally, a too large value for this parameter or for antipad size
does not allow one to create a thermal relief for small pads (like pad
sizes used for SMD components).
:::
:::::
::::::::::::::::::::::::::::::::

:::::::::: sect2

### Adding a cutout area inside a zone {#_adding_a_cutout_area_inside_a_zone}

::: paragraph
A zone must already exist. To add a cutout area (a non-filled area
inside the zone):
:::

::: ulist

- Right-click on an existing edge outline.

- Select Add Cutout Area.
:::

:::: imageblock
::: content
![Pcbnew add cutout menu item](images/Pcbnew_add_cutout_menu_item.png)
:::
::::

::: ulist

- Create the new outline.
:::

:::: imageblock
::: content
![Pcbnew zone unfilled cutout
outline](images/Pcbnew_zone_unfilled_cutout_outline.png)
:::
::::
::::::::::

::::::::::::::::::::::: sect2

### Outlines editing {#_outlines_editing}

::: paragraph
An outline can be modified by:
:::

::: ulist

- Moving a corner or an edge.

- Deleting or adding a corner.

- Adding a similar zone, or a cutout area.
:::

::: paragraph
If polygons are overlapping they will be combined.
:::

:::: imageblock
::: content
![Pcbnew zone modification menu
items](images/Pcbnew_zone_modification_menu_items.png)
:::
::::

::: paragraph
To do that, right-click on a corner or on an edge, then select the
proper command.
:::

::: paragraph
Here is a corner (from a cutout) that has been moved:
:::

:::: imageblock
::: content
![Pcbnew zone corner move
during](images/Pcbnew_zone_corner_move_during.png)
:::
::::

::: paragraph
Here is the final result:
:::

:::: imageblock
::: content
![Pcbnew zone corner move
after](images/Pcbnew_zone_corner_move_after.png)
:::
::::

::: paragraph
Polygons are combined.
:::

::::::::: sect3

#### Adding a similar zone {#_adding_a_similar_zone}

::: paragraph
Adding the similar zone:
:::

:::: imageblock
::: content
![Pcbnew zone add similar
during](images/Pcbnew_zone_add_similar_during.png)
:::
::::

::: paragraph
Final result:
:::

:::: imageblock
::: content
![Pcbnew zone add similar
after](images/Pcbnew_zone_add_similar_after.png)
:::
::::
:::::::::
:::::::::::::::::::::::

:::: sect2

### Editing zone parameters {#_editing_zone_parameters}

::: paragraph
When right-clicking on an outline, and using \'Edit Zone Params\' the
Zone params Dialog box will open. Initial parameters can be inputted .
If the zone is already filled, refilling it will be necessary.
:::
::::

:::::: sect2

### Final zone filling {#_final_zone_filling}

::: paragraph
When the board is finished, one must fill or refill all zones. To do
this:
:::

::: ulist

- Activate the tool zones via the button [![add
  zone](images/icons/add_zone.png)]{.image}.

- Right-click to display the pop-up menu.

- Use Fill or Refill All Zones: [![Pcbnew fill refill all
  zones](images/Pcbnew_fill_refill_all_zones.png)]{.image}
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | Calculation can take some time if |
| Warning                           | the filling grid is small.        |
| :::                               |                                   |
+-----------------------------------+-----------------------------------+
:::
::::::

:::::: sect2

### Change zones net names {#_change_zones_net_names}

::: paragraph
After editing a schematic, you can change the name of any net. For
instance VCC can be changed to +5V.
:::

::: paragraph
When a global DRC is made Pcbnew checks if the zone net name exists, and
displays an error if not.
:::

::: paragraph
Manually editing the zone parameters will be necessary to change the old
name to the new one.
:::
::::::

:::::::::: sect2

### Creating zones on technical layers {#_creating_zones_on_technical_layers}

::::::::: sect3

#### Creating zone limits {#_creating_zone_limits}

::: paragraph
This is done using the button [![add
zone](images/icons/add_zone.png)]{.image}. The active layer must be a
technical layer.
:::

::: paragraph
When clicking to start the zone outline, this dialog box is opened:
:::

:::: imageblock
::: content
![Pcbnew technical layer zone
dialog](images/Pcbnew_technical_layer_zone_dialog.png)
:::
::::

::: paragraph
Select the technical layer to place the zone and draw the zone outline
like explained previously for copper layers.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | ::: ulist                         |
| Note                              | - For editing outlines use the    |
| :::                               |   same method as for copper       |
|                                   |   zones.                          |
|                                   |                                   |
|                                   | - If necessary, cutout areas can  |
|                                   |   be added.                       |
|                                   | :::                               |
+-----------------------------------+-----------------------------------+
:::
:::::::::
::::::::::

:::::::::::: sect2

### Creating a Keepout area {#_creating_a_keepout_area}

::: paragraph
Select the tool [![add keepout
area](images/icons/add_keepout_area.png)]{.image}
:::

::: paragraph
The active layer should be a copper layer.
:::

::: paragraph
After clicking on the starting point of a new keepout area, the dialog
box is opened:
:::

:::: imageblock
::: content
![Pcbnew keepout area
properties](images/Pcbnew_keepout_area_properties.png)
:::
::::

::: paragraph
One can select disallowed items:
:::

::: ulist

- Tracks.

- Vias.

- Copper pours.
:::

::: paragraph
When a track or a via is inside a keepout which does not allow it, a DRC
error will be raised.
:::

::: paragraph
For copper zones, the area inside a keepout with no copper pour will not
be filled. A keep-out area is a like a zone, so editing its outline is
analogous to copper zone editing.
:::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Setting routing parameters {#_setting_routing_parameters}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::::: sect2

### Current settings {#_current_settings}

::::::: sect3

#### Accessing the main dialog {#_accessing_the_main_dialog}

::: paragraph
The most important parameters are accessed from the following drop-down
menu:
:::

:::: imageblock
::: content
![Pcbnew design rules dropdown](images/Pcbnew_design_rules_dropdown.png)
:::
::::

::: paragraph
and are set in the Design Rules dialog.
:::
:::::::

:::::: sect3

#### Current settings {#_current_settings_2}

::: paragraph
Current settings are displayed in the top toolbar.
:::

:::: imageblock
::: content
![Pcbnew design rules top
toolbar](images/Pcbnew_design_rules_top_toolbar.png)
:::
::::
::::::
::::::::::::

::::::::::: sect2

### General options {#_general_options}

::: paragraph
The General options menu is available via the top toolbar link
Preferences → General dialog.
:::

:::: imageblock
::: content
![Pcbnew preferences menu](images/Pcbnew_preferences_menu.png)
:::
::::

::: paragraph
The dialog looks like the following:
:::

:::: imageblock
::: content
![Pcbnew general options
dialog](images/Pcbnew_general_options_dialog.png)
:::
::::

::: paragraph
For the creation of tracks the necessary parameters are:
:::

::: ulist

- **Tracks 45 Only**: Directions allowed for track segments are 0, 45 or
  90 degrees.

- **Double Segm Track**: When creating tracks, 2 segments will be
  displayed.

- **Tracks Auto Del**: When recreating tracks, the old one will be
  automatically deleted if considered redundant.

- **Magnetic Pads**: The graphic cursor becomes a pad, centered in the
  pad area.

- **Magnetic Tracks**: The graphic cursor becomes the track axis.
:::
:::::::::::

:::::::::::::::::::::::::::::::::: sect2

### Netclasses {#_netclasses}

::: paragraph
Pcbnew allows you to define different routing parameters for each net.
Parameters are defined by a group of nets.
:::

::: ulist

- A group of nets is called a Netclass.

- There is always a netclass called \"default\".

- Users can add other Netclasses.
:::

::: paragraph
A netclass specifies:
:::

::: ulist

- The width of tracks, via diameters and drills.

- The clearance between pads and tracks (or vias).

- When routing, Pcbnew automatically selects the netclass corresponding
  to the net of the track to create or edit, and therefore the routing
  parameters.
:::

:::: sect3

#### Setting routing parameters {#_setting_routing_parameters_2}

::: paragraph
The choice is made in the menu: Design Rules → Design Rules.
:::
::::

::::::: sect3

#### Netclass editor {#_netclass_editor}

::: paragraph
The Netclass editor allows you to:
:::

::: ulist

- Add or delete Netclasses.

- Set routing parameters values: clearance, track width, via sizes.

- Group nets in netclasses.
:::

:::: imageblock
::: content
![Pcbnew design rules editor netclass
tab](images/Pcbnew_design_rules_editor_netclass_tab.png)
:::
::::
:::::::

::::::::::: sect3

#### Global Design Rules {#_global_design_rules}

::: paragraph
The global design rules are:
:::

::: ulist

- Enabling/disabling Blind/buried Vias use.

- Enabling/disabling Micro Vias use.

- Minimum Allowed Values for tracks and vias.
:::

::: paragraph
A DRC error is raised when a value smaller than the minimum value
specified is encountered. The second dialog panel is:
:::

:::: imageblock
::: content
![Pcbnew design rules editor global
tab](images/Pcbnew_design_rules_editor_global_tab.png)
:::
::::

::: paragraph
This dialog also allows to enter a \"stock\" of tracks and via sizes.
:::

::: paragraph
When routing, one can select one of these values to create a track or
via, instead of using the netclass's default value.
:::

::: paragraph
Useful in critical cases when a small track segment must have a specific
size.
:::
:::::::::::

::::::: sect3

#### Via parameters {#_via_parameters}

::: paragraph
Pcbnew handles 3 types of vias:
:::

::: ulist

- Through vias (usual vias).

- Blind or buried vias.

- Micro Vias, like buried vias but restricted to an external layer to
  its nearest neighbor. They are intended to connect BGA pins to the
  nearest inner layer. Their diameter is usually very small and they are
  drilled by laser.
:::

::: paragraph
By default, all vias have the same drill value.
:::

::: paragraph
This dialog specifies the smallest acceptable values for via parameters.
On a board, a via smaller than specified here generates a DRC error.
:::
:::::::

:::: sect3

#### Track parameters {#_track_parameters}

::: paragraph
Specify the minimum acceptable track width. On a board, a track width
smaller than specified here generates a DRC error.
:::
::::

:::::: sect3

#### Specific sizes {#_specific_sizes}

:::: imageblock
::: content
![Pcbnew specific size options](images/Pcbnew_specific_size_options.png)
:::
::::

::: paragraph
One can enter a set of extra tracks and/or via sizes. While routing a
track, these values can be used on demand instead of the values from the
current netclass values.
:::
::::::
::::::::::::::::::::::::::::::::::

::::::: sect2

### Examples and typical dimensions {#_examples_and_typical_dimensions}

:::: sect3

#### Track width {#_track_width}

::: paragraph
Use the largest possible value and conform to the minimum sizes given
here.
:::

+----------+----------+----------+----------+----------+-----------+
| Units    | CLASS 1  | CLASS 2  | CLASS 3  | CLASS 4  | CLASS 5   |
+==========+==========+==========+==========+==========+===========+
| mm       | 0.8      | 0.5      | 0.4      | 0.25     | 0.15      |
+----------+----------+----------+----------+----------+-----------+
| mils     | 31       | 20       | 16       | 10       | 6         |
+----------+----------+----------+----------+----------+-----------+
::::

:::: sect3

#### Insulation (clearance) {#_insulation_clearance}

+----------+----------+----------+----------+----------+-----------+
| Units    | CLASS 1  | CLASS 2  | CLASS 3  | CLASS 4  | CLASS 5   |
+==========+==========+==========+==========+==========+===========+
| mm       | 0.7      | 0.5      | 0.35     | 0.23     | 0.15      |
+----------+----------+----------+----------+----------+-----------+
| mils     | 27       | 20       | 14       | 9        | 6         |
+----------+----------+----------+----------+----------+-----------+

::: paragraph
Usually, the minimum clearance is very similar to the minimum track
width.
:::
::::
:::::::

::::::::::: sect2

### Examples {#_examples}

:::::: sect3

#### Rustic {#_rustic}

::: ulist

- Clearance: 0.35 mm (0.0138 inches).

- Track width: 0.8 mm (0.0315 inches).

- Pad diameter for ICs and vias: 1.91 mm (0.0750 inches).

- Pad diameter for discrete components: 2.54 mm (0.1 inches).

- Ground track width: 2.54 mm (0.1 inches).
:::

:::: imageblock
::: content
![Pcbnew dr example rustic](images/Pcbnew_dr_example_rustic.png)
:::
::::
::::::

:::::: sect3

#### Standard {#_standard}

::: ulist

- Clearance: 0.35 mm (0.0138 inches).

- Track width: 0.5 mm (0.0127 inches).

- Pad diameter for ICs: make them elongated in order to allow tracks to
  pass between IC pads and yet have the pads offer a sufficient adhesive
  surface (1.27 x 2.54 mm -→ 0.05 x 0.1 inches).

- Vias: 1.27 mm (0.0500 inches).
:::

:::: imageblock
::: content
![Pcbnew dr example standard](images/Pcbnew_dr_example_standard.png)
:::
::::
::::::
:::::::::::

:::: sect2

### Manual routing {#_manual_routing}

::: paragraph
Manual routing is often recommended, because it is the only method
offering control over routing priorities. For example, it is preferable
to start by routing power tracks, making them wide and short and keeping
analog and digital supplies well separated. Later, sensitive signal
tracks should be routed. Amongst other problems, automatic routing often
requires many vias. However, automatic routing can offer a useful
insight into the positioning of footprints. With experience, you will
probably find that the automatic router is useful for quickly routing
the \'obvious\' tracks, but the remaining tracks will best be routed by
hand.
:::
::::

:::::::::::::::::::::::: sect2

### Help when creating tracks {#_help_when_creating_tracks}

::: paragraph
Pcbnew can display the full ratsnest, if the button
[![modratsnest](images/icons/modratsnest.png)]{.image} is activated.
:::

::: paragraph
The button [![net highlight](images/icons/net_highlight.png)]{.image}
allows one to highlight a net (click to a pad or an existing track to
highlight the corresponding net).
:::

::: paragraph
The DRC checks tracks in real time while creating them. One cannot
create a track which does not match the DRC rules. It is possible to
disable the DRC by clicking on the button. This is, however, not
recommended, use it only in specific cases.
:::

:::::::::::::: sect3

#### Creating tracks {#_creating_tracks}

::: paragraph
A track can be created by clicking on the button [![add
tracks](images/icons/add_tracks.png)]{.image}. A new track must start on
a pad or on another track, because Pcbnew must know the net used for the
new track (in order to match the DRC rules).
:::

:::: imageblock
::: content
![Pcbnew creating new track](images/Pcbnew_creating_new_track.png)
:::
::::

::: paragraph
As you move the mouse, a track is drawn connecting the origin of the
track with the current mouse position. The track will be drawn with at
most two segments (for example, rightwards, then a switch to
diagonally). Clicking while routing locks in the corner node.
:::

::: paragraph
The direction that the track is drawn in first (e.g. right first, then
diagonally, or diagonally first then right) is called the \"Track
Posture\" and can be switched with the hotkey \'/\' or the button
[![change entry orient](images/icons/change_entry_orient.png)]{.image}.
:::

::: paragraph
[![Pcbnew routing posture](images/Pcbnew_routing_posture.png)]{.image}
:::

::: paragraph
Holding \'Ctrl\' while routing in the non-legacy canvases constrains the
routing to a single horizontal or vertical segment. Switching posture
changes to a single diagonal segment. Holding \'Shift\' while routing
removes the \'snap to object\' gravity.
:::

::: paragraph
When creating a new track, Pcbnew shows links to nearest unconnected
pads.
:::

::: paragraph
End the track by double-clicking, by the pop-up menu or by the hotkey
\'End\'.
:::

:::: imageblock
::: content
![Pcbnew track in progres
context](images/Pcbnew_track_in_progres_context.png)
:::
::::
::::::::::::::

:::: sect3

#### Moving and dragging tracks {#_moving_and_dragging_tracks}

::: paragraph
When the button [![add tracks](images/icons/add_tracks.png)]{.image} is
active, the track where the cursor is positioned can be moved with the
hotkey \'M\'. If you want to drag the track you can use the hotkey
\'G\'.
:::
::::

:::::: sect3

#### Via Insertion {#_via_insertion}

::: paragraph
A via can be inserted only when a track is in progress:
:::

::: ulist

- By the pop-up menu.

- By the hotkey \'V\'.

- By switching to a new copper layer using the appropriate hotkey.
:::

::: paragraph
Holding \'Shift\' while adding a via ends routing as soon as the via is
placed. This is useful when adding a connection to a plane, so the
active layer doesn't change and no extra key need be pressed to exit
routing.
:::
::::::
::::::::::::::::::::::::

:::::::::::::: sect2

### Select/edit the track width and via size {#_selectedit_the_track_width_and_via_size}

::: paragraph
When clicking on a track or a pad, Pcbnew automatically selects the
corresponding Netclass, and the track size and via dimensions are
derived from this netclass.
:::

::: paragraph
As previously seen, the Global Design Rules editor has a tool to insert
extra tracks and via sizes.
:::

::: ulist

- The horizontal toolbar can be used to select a size.

- When the button [![add tracks](images/icons/add_tracks.png)]{.image}
  is active, the current track width can be selected from the pop-up
  menu (accessible as well when creating a track).

- The user can utilize the default Netclasses values or a specified
  value.
:::

::::: sect3

#### Using the horizontal toolbar {#_using_the_horizontal_toolbar}

:::: imageblock
::: content
![Pcbnew track toolbar](images/Pcbnew_track_toolbar.png)
:::
::::

+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar track width                                                      | Track width selection. The symbol \* is  |
| selection](images/Pcbnew_track_toolbar_track_width_selection.png){width="70%"}]{.image}  | a mark for default Netclass value        |
|                                                                                          | selection.                               |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar track width selection in                                         | Selecting a specific track width value.  |
| use](images/Pcbnew_track_toolbar_track_width_selection_in_use.png){width="70%"}]{.image} | The first value in the list is always    |
|                                                                                          | the netclass value. Other values are     |
|                                                                                          | tracks widths entered from the Global    |
|                                                                                          | Design Rules editor.                     |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar via size                                                         | Via size selection. The symbol \* is a   |
| selection](images/Pcbnew_track_toolbar_via_size_selection.png){width="70%"}]{.image}     | mark for default Netclass value          |
|                                                                                          | selection.                               |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar via size selection in                                            | Selecting a specific via dimension       |
| use](images/Pcbnew_track_toolbar_via_size_selection_in_use.png){width="70%"}]{.image}    | value. The first value in the list is    |
|                                                                                          | always the netclass value. Other values  |
|                                                                                          | are via dimensions entered from the      |
|                                                                                          | Global Design Rules editor.              |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![auto track width](images/icons/auto_track_width.png)]{.image}                         | When enabled: Automatic track width      |
|                                                                                          | selection. When starting a track on an   |
|                                                                                          | existing track, the new track has the    |
|                                                                                          | same width as the existing track.        |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar grid size                                                        | Grid size selection.                     |
| selection](images/Pcbnew_track_toolbar_grid_size_selection.png){width="70%"}]{.image}    |                                          |
+------------------------------------------------------------------------------------------+------------------------------------------+
| [![Pcbnew track toolbar zoom                                                             | Zoom selection.                          |
| selection](images/Pcbnew_track_toolbar_zoom_selection.png){width="70%"}]{.image}         |                                          |
+------------------------------------------------------------------------------------------+------------------------------------------+
:::::

::::::: sect3

#### Using the pop-up menu {#_using_the_pop_up_menu}

::: paragraph
One can select a new size for routing, or change to a previously created
via or track segment:
:::

:::: imageblock
::: content
![Pcbnew track context menu](images/Pcbnew_track_context_menu.png)
:::
::::

::: paragraph
If you want to change many via (or track) sizes, the best way is to use
a specific Netclass for the net(s) that must be edited (see global
changes).
:::
:::::::
::::::::::::::

:::::::::::::::::::: sect2

### Editing and changing tracks {#_editing_and_changing_tracks}

::::::::::: sect3

#### Change a track {#_change_a_track}

::: paragraph
In many cases redrawing a track is required.
:::

::: paragraph
New track (in progress):
:::

:::: imageblock
::: content
![Pcbnew new track in progress](images/Pcbnew_new_track_in_progress.png)
:::
::::

::: paragraph
When finished:
:::

:::: imageblock
::: content
![Pcbnew new track completed](images/Pcbnew_new_track_completed.png)
:::
::::

::: paragraph
Pcbnew will automatically remove the old track if it is redundant.
:::
:::::::::::

:::::::::: sect3

#### Global changes {#_global_changes}

::: paragraph
Global tracks and via sizes dialog editor is accessible via the pop-up
window by right clicking on a track:
:::

:::: imageblock
::: content
![Pcbnew track global edit context
menu](images/Pcbnew_track_global_edit_context_menu.png)
:::
::::

::: paragraph
The dialog editor allows global changes of tracks and/or vias for:
:::

::: ulist

- The current net.

- The whole board.
:::

:::: imageblock
::: content
![Pcbnew track global edit
dialog](images/Pcbnew_track_global_edit_dialog.png)
:::
::::
::::::::::
::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::: sect1

## Interactive Router {#_interactive_router}

:::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
The Interactive Router lets you quickly and efficiently route your PCBs
by shoving off or walking around items on the PCB that collide with the
trace you are currently drawing.
:::

::: paragraph
Following modes are supported:
:::

::: ulist

- **Highlight collisions**, which highlights all violating objects with
  a nice, shiny green color and shows violating clearance regions.

- **Shove**, attempting to push and shove all items colliding with the
  currently routed track.

- **Walk around**, trying to avoid obstacles by hugging/walking around
  them.
:::

:::::::::: sect2

### Setting up {#_setting_up}

::: paragraph
Before using the Interactive Router, please set up these two things:
:::

::: ulist

- **Clearance settings** To set the clearances, open the *Design Rules*
  dialog and make sure at least the default clearance value looks
  sensible.
:::

:::: imageblock
::: content
![Rules editor](images/en/rules_editor.png)
:::
::::

::: ulist

- **Enable OpenGL mode** By selecting *View→Switch canvas to OpenGL*
  menu option or pressing **F11**.
:::

:::: imageblock
::: content
![OpenGL mode](images/en/opengl_menu.png)
:::
::::
::::::::::

::::::::::: sect2

### Laying out tracks {#_laying_out_tracks}

::: paragraph
To activate the router tool press the *Interactive Router* button
[![Interactive Router Button](images/route_icon.png)]{.image} or the
**X** key. The cursor will turn into a cross and the tool name, will
appear in the status bar.
:::

::: paragraph
To start a track, click on any item (a pad, track or a via) or press the
**X** key again hovering the mouse over that item. The new track will
use the net of the starting item. Clicking or pressing **X** on empty
PCB space starts a track with no net assigned.
:::

::: paragraph
Move the mouse to define shape of the track. The router will try to
follow the mouse trail, hugging unmovable obstacles (such as pads) and
shoving colliding traces/vias, depending on the mode. Retreating the
mouse cursor will cause the shoved items to spring back to their former
locations.
:::

::: paragraph
Clicking on a pad/track/via in the same net finishes routing. Clicking
in empty space fixes the segments routed so far and continues routing
the trace.
:::

::: paragraph
In order to stop routing and undo all changes (shoved items, etc.),
simply press **Esc**.
:::

::: paragraph
Pressing **V** or selecting *Place Through Via* from the context menu
while routing a track attaches a via at the end of the trace being
routed. Pressing **V** again disables via placement. Clicking in any
spot establishes the via and continues routing (unless \'Shift\' is
held).
:::

::: paragraph
Pressing **/** or selecting *Switch Track Posture* from the context menu
toggles the direction of the initial track segment between straight or
diagonal.
:::

::: {.admonitionblock .note}

+-----------------------------------+-----------------------------------+
| ::: title                         | By default, the router snaps to   |
| Note                              | centers/axes of the items.        |
| :::                               | Snapping can be disabled by       |
|                                   | holding **Shift** while routing   |
|                                   | or selecting items.               |
+-----------------------------------+-----------------------------------+
:::
:::::::::::

::::: sect2

### Setting track widths and via sizes {#_setting_track_widths_and_via_sizes}

::: paragraph
There are several ways to pre-select a track width/via size or to change
it during routing:
:::

::: ulist

- Use standard KiCad shortcuts.

- Press **W** or select *Custom Track Width* from the context menu to
  type in a custom track width/via size.

- Pick a predefined width from the *Select Track Width* sub-menu of the
  context menu.

- Select *Use the starting track width* in the *Select Track Width* menu
  to pick the width from the start item (or the traces already connected
  to it).
:::
:::::

:::: sect2

### Dragging {#_dragging}

::: paragraph
The router can drag track segments, corners and vias. To drag an item,
click on it with **Ctrl** key pressed, hover the mouse and press **G**
or select *Drag Track/Via* from the context menu. Finish dragging by
clicking again or abort by pressing *Esc*.
:::
::::

:::::::: sect2

### Options {#_options}

::: paragraph
The router behavior can be configured by pressing *E* or selecting
*Routing Options* from the context menu while in the Track mode. It
opens a window like the one below:
:::

::: paragraph
The options are:
:::

:::: imageblock
::: content
![Router options window screenshot](images/en/router_options.png)
:::
::::

::: ulist

- **Mode** - select how the router handles DRC violation (shoving,
  walking around, etc.)

- **Shove vias** - when disabled, vias are treated as un-movable objects
  and hugged instead of shoved.

- **Jump over obstacles** - when enabled, the router tries to move
  colliding traces behind solid obstacles (e.g. pads) instead of
  \"reflecting\" back the collision

- **Remove redundant tracks** - removes loops while routing (e.g. if the
  new track ensures same connectivity as an already existing one, the
  old track is removed). Loop removal works locally (only between the
  start and end of the currently routed trace).

- **Automatic neckdown** - when enabled, the router tries to break out
  pads/vias in a clean way, avoiding acute angles and jagged breakout
  traces.

- **Smooth dragged segments** - when enabled, the router attempts to
  merge several jagged segments into a single straight one (dragging
  mode).

- **Allow DRC violations** (*Highlight collisions* mode only) - allows
  to establish a track even if is violating the DRC rules.

- **Optimizer effort** - defines how much time the router shall spend
  optimizing the routed/shoved traces. More effort means cleaner routing
  (but slower), less effort means faster routing but somewhat jagged
  traces.
:::
::::::::
::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::: sect1

## Schematic Implementation {#_schematic_implementation}

:::::::::::::::::::::::::::::::::::::: sectionbody
::::::: sect2

### Linking a schematic to a printed circuit board {#_linking_a_schematic_to_a_printed_circuit_board}

::: paragraph
Generally speaking, a schematic sheet is linked to its printed circuit
board by means of the netlist file, which is normally generated by the
schematic editor used to make the schematic. Pcbnew accepts netlist
files made with Eeschema or Orcad PCB 2. The netlist file, generated
from the schematic is usually missing the footprints that correspond to
the various components. Consequently an intermediate stage is necessary.
During this intermediate process the association of components with
footprints is performed. In KiCad, CvPcb is used to create this
association and a file named `*.cmp` is produced. CvPcb also updates the
netlist file using this information.
:::

::: paragraph
CvPcb can also output a \"stuff file\" `*.stf` which can be back
annotated into the schematic file as the F2 field for each component,
saving the task of re-assigning footprints in each schematic edit pass.
In Eeschema copying a component will also copy the footprint assignment
and set the reference designator as unassigned for later
auto-incremental annotation.
:::

::: paragraph
Pcbnew reads the modified netlist file `.net` and, if it exists, the
`.cmp` file. In the event of a footprint being changed directly in
Pcbnew the `.cmp` file is automatically updated avoiding the requirement
to run CvPcb again.
:::

::: paragraph
Refer to the figure of \"Getting Started in KiCad\" manual in the
section *KiCad Workflow* that illustrates the work-flow of KiCad and how
intermediate files are obtained and used by the different software tools
that comprise KiCad.
:::
:::::::

:::::: sect2

### Procedure for creating a printed circuit board {#_procedure_for_creating_a_printed_circuit_board}

::: paragraph
After having created your schematic in Eeschema:
:::

::: ulist

- Generate the netlist using Eeschema.

- Assign each component in your netlist file to the corresponding land
  pattern (often called footprint) used on the printed circuit using
  Cvpcb.

- Launch Pcbnew and read the modified Netlist. This will also read the
  file with the footprint selections.
:::

::: paragraph
Pcbnew will then load automatically all the necessary footprints.
Footprints can now be placed manually or automatically on the board and
tracks can be routed.
:::
::::::

:::::: sect2

### Procedure for updating a printed circuit board {#_procedure_for_updating_a_printed_circuit_board}

::: paragraph
If the schematic is modified (after a printed circuit board has been
generated), the following steps must be repeated:
:::

::: ulist

- Generate a new netlist file using Eeschema.

- If the changes to the schematic involve new components, the
  corresponding footprints must be assigned using Cvpcb.

- Launch Pcbnew and re-read the modified netlist (this will also re-read
  the file with the footprint selections).
:::

::: paragraph
Pcbnew will then load automatically any new footprints, add the new
connections and remove redundant connections. This process is called
forward annotation and is a very common procedure when a PCB is made and
updated.
:::
::::::

:::::::::::::::::::::::: sect2

### Reading netlist file - loading footprints {#_reading_netlist_file_loading_footprints}

:::::: sect3

#### Dialog box {#_dialog_box}

::: paragraph
Accessible from the icon [![netlist](images/icons/netlist.png)]{.image}
:::

:::: imageblock
::: content
![Pcbnew netlist dialog](images/en/Pcbnew_netlist_dialog.png)
:::
::::
::::::

::: sect3

#### Available options {#_available_options}

+-----------------------------------+-----------------------------------+
| Footprint Selection               | Components and corresponding      |
|                                   | footprints on board link: normal  |
|                                   | link is Reference (normal option  |
|                                   | Timestamp can be used after       |
|                                   | reannotation of schematic, if the |
|                                   | previous annotation was destroyed |
|                                   | (special option)                  |
+-----------------------------------+-----------------------------------+
| Exchange Footprint:               | If a footprint has changed in the |
|                                   | netlist: keep old footprint or    |
|                                   | change to the new one.            |
+-----------------------------------+-----------------------------------+
| Unconnected Tracks                | Keep all existing tracks, or      |
|                                   | delete erroneous tracks           |
+-----------------------------------+-----------------------------------+
| Extra Footprints                  | Remove footprints which are on    |
|                                   | board but not in the netlist.     |
|                                   | Footprint with attribute          |
|                                   | \"Locked\" will not be removed.   |
+-----------------------------------+-----------------------------------+
| Single Pad Nets                   | Remove single pad nets.           |
+-----------------------------------+-----------------------------------+
:::

:::::::::::::::::: sect3

#### Loading new footprints {#_loading_new_footprints}

::: paragraph
With the GAL backend when new footprints are found in the netlist file,
they will be loaded, spread out, and be ready for you to place as a
group where you would like.
:::

:::: imageblock
::: content
![Pcbnew import spread
footprints](images/Pcbnew_import_spread_footprints.png){height="300"}
:::
::::

::: paragraph
With the legacy backend when new footprints are found in the netlist
file, they will be automatically loaded and placed at coordinate (0,0).
:::

:::: imageblock
::: content
![Pcbnew stacked footprints](images/Pcbnew_stacked_footprints.png)
:::
::::

::: paragraph
New footprints can be moved and arranged one by one. A better way is to
automatically move (unstack) them:
:::

::: paragraph
Activate footprint mode ([![mode
module](images/icons/mode_module.png)]{.image})
:::

::: paragraph
Move the mouse cursor to a suitable (free of component) area, and click
on the right button:
:::

:::: imageblock
::: content
![Pcbnew move all modules](images/Pcbnew_move_all_modules.png)
:::
::::

::: ulist

- Automatically Place New Footprints, if there is already a board with
  existing footprints.

- Automatically Place All Footprints, for the first time (when creating
  a board).
:::

::: paragraph
The following screenshot shows the results.
:::

:::: imageblock
::: content
![Pcbnew unstacked footprints](images/Pcbnew_unstacked_footprints.png)
:::
::::
::::::::::::::::::
::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Files for circuit fabrication {#_files_for_circuit_fabrication}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Let us see now what the steps are for the creation of the necessary
files for the production of your printed circuit board.
:::

::: paragraph
All files generated by KiCad are placed in the working directory which
is the same directory that contains the xxxx.brd file for the printed
circuit board.
:::

::::::::: sect2

### Final preparations {#_final_preparations}

::: paragraph
The generation of the necessary files for the production of your printed
circuit board includes the following preparatory steps.
:::

::: ulist

- Mark any layer (e.g., \'top or front\' and \'bottom or back\') with
  the project name by placing appropriate text upon each of the layers.

- All text on copper layers (sometimes called \'solder\' or \'bottom\')
  must be mirrored.

- Create any ground planes, modifying traces as required to ensure they
  are contiguous.

- Place alignment crosshairs and possibly the dimensions of the board
  outline (these are usually placed on one of the general purpose
  layers).
:::

::: paragraph
Here is an example showing all of these elements, except ground planes,
which have been omitted for better visibility:
:::

:::: imageblock
::: content
![Pcbnew final preparation example
board](images/Pcbnew_final_preparation_example_board.png)
:::
::::

::: paragraph
A color key for the 4 copper layers has also been included: [![Pcbnew
layer colour key](images/Pcbnew_layer_colour_key.png)]{.image}
:::
:::::::::

::::::::: sect2

### Final DRC test {#_final_drc_test}

::: paragraph
Before generating the output files, a global DRC test is very strongly
recommended.
:::

::: paragraph
Zones are filled or refilled when starting a DRC. Press the button
[![drc](images/icons/drc.png)]{.image} to launch the following DRC
dialog:
:::

:::: imageblock
::: content
![Pcbnew DRC dialog](images/Pcbnew_DRC_dialog.png)
:::
::::

::: paragraph
Adjust the parameters accordingly and then press the \"Start DRC\"
button.
:::

::: paragraph
This final check will prevent any unpleasant surprises.
:::
:::::::::

:::::: sect2

### Setting coordinates origin {#_setting_coordinates_origin}

::: paragraph
Set the coordinates origin for the photo plot and drill files, one must
place the auxiliary axis on this origin. Activate the icon [![pcb
offset](images/icons/pcb_offset.png)]{.image}. Move the auxiliary axis
by left-clicking on the chosen location.
:::

:::: imageblock
::: content
![Pcbnew setting pcb origin](images/Pcbnew_setting_pcb_origin.png)
:::
::::
::::::

:::::::::::::::::::::::::::::::::::: sect2

### Generating files for photo-tracing {#_generating_files_for_photo_tracing}

::: paragraph
This is done via the Files/Plot menu option and invokes the following
dialog:
:::

:::: imageblock
::: content
![Pcbnew plot dialog](images/Pcbnew_plot_dialog.png)
:::
::::

::: paragraph
Usually, the files are in the GERBER format. Nevertheless, it is
possible to produce output in both HPGL and POSTSCRIPT formats. When
Postscript format is selected, this dialog will appear.
:::

:::: imageblock
::: content
![Pcbnew plot postscript
dialog](images/Pcbnew_plot_postscript_dialog.png)
:::
::::

::: paragraph
In these formats, a fine scale adjust can be used to compensate for the
plotter accuracy and to have a true scale of 1 for the output:
:::

:::: imageblock
::: content
![Pcbnew plot fine scale
setting](images/Pcbnew_plot_fine_scale_setting.png)
:::
::::

::::::::: sect3

#### GERBER format {#_gerber_format}

::: paragraph
For each layer, Pcbnew generates a separate file following the GERBER
274X standard, by default in 4.6 format (each coordinate in the file is
represented by 10 digits, of which 4 are before the decimal point and 6
follow it), units in inches, and a scale of 1.
:::

::: paragraph
It is normally necessary to create files for all of the copper layers
and, depending on the circuit, for the silkscreen, solder mask, and
solder paste layers. All of these files can be produced in one step, by
selecting the appropriate check boxes.
:::

::: paragraph
For example, for a double-sided circuit with silkscreen, solder mask and
solder paste (for SMD components), 8 files should be generated (\'xxxx\'
represents the name of the .brd file).
:::

::: ulist

- xxxx-F_Cu.gbr for the component side.

- xxxx-B_Cu.gbr for the copper side.

- xxxx-F_SilkS.gbr for the component-side silkscreen markings.

- xxxx-B_SilkS.gbr for the copper-side silkscreen markings.

- xxxx-F_Paste.gbr for the component-side solder paste.

- xxxx-B_Paste.gbr for the copper-side solder paste.

- xxxx-F_Mask.gbr for the component-side solder mask.

- xxxx-B_Mask.gbr for the copper-side solder mask.
:::

::: paragraph
GERBER file format:
:::

::: paragraph
The format used by Pcbnew is RS274X format 4.6, Imperial, Leading zero
omitted, Abs format. These are very usual settings.
:::
:::::::::

::::: sect3

#### POSTSCRIPT format {#_postscript_format}

::: paragraph
The standard extension for the output files is .ps in the case of
postscript output. As for HPGL output, the tracing can be at
user-selected scales and can be mirrored. If the Org = Centre option is
active, the origin for the coordinates of the tracing table is assumed
to be in the centre of the drawing.
:::

::: paragraph
If the Print Sheet Ref option is active, the sheet cartridge is traced.
:::
:::::

:::::::::: sect3

#### Plot options {#_plot_options}

::: paragraph
Gerber format:
:::

:::: imageblock
::: content
![Pcbnew plot options gerber](images/Pcbnew_plot_options_gerber.png)
:::
::::

::: paragraph
Other formats:
:::

:::: imageblock
::: content
![Pcbnew plot options other
formats](images/Pcbnew_plot_options_other_formats.png)
:::
::::

::: paragraph
GERBER format specific options:
:::

+-----------------------------------+-----------------------------------+
| Use Protel filename extensions    | Use .gbl .gtl .gbs .gts .gbp .gtp |
|                                   | .gbo .gto instead of .gbr for     |
|                                   | file name extensions.             |
+-----------------------------------+-----------------------------------+
| Include extended attributes       | Output extended attributes to     |
|                                   | file.                             |
+-----------------------------------+-----------------------------------+
| Subtract soldermask from          | Remove all Silk from solder paste |
| silkscreen                        | areas.                            |
+-----------------------------------+-----------------------------------+
::::::::::

:::::::: sect3

#### Other formats {#_other_formats}

::: paragraph
The standard extension depends on the output file type.
:::

::: paragraph
Some options are not available for some formats.
:::

::: paragraph
The plot can be done at user-selected scales and can be mirrored.
:::

::: paragraph
The Print Drill Opt list offers the option of pads that are filled,
drilled to the correct diameter or drilled with a small hole (to guide
hand drilling).
:::

::: paragraph
If the Print Sheet Ref option is active, the sheet cartridge is traced.
:::
::::::::
::::::::::::::::::::::::::::::::::::

::::::::::::::::::::: sect2

### Global clearance settings for the solder stop and the solder paste mask {#_global_clearance_settings_for_the_solder_stop_and_the_solder_paste_mask}

::: paragraph
Mask clearance values can be set globally for the solder mask layers and
the solder paste layers. These clearances can be set at the following
levels.
:::

::: ulist

- At pads level.

- At footprint level.

- Globally.
:::

::: paragraph
And Pcbnew uses by priority order.
:::

::: ulist

- Pad values. If null:

- Footprint values. If null:

- Global values.
:::

::::::::: sect3

#### Access {#_access}

::: paragraph
The menu option for this is available via the Dimensions menu:
:::

:::: imageblock
::: content
![Pcbnew pad mask clearance menu
item](images/Pcbnew_pad_mask_clearance_menu_item.png)
:::
::::

::: paragraph
The dialog box is the following:
:::

:::: imageblock
::: content
![Pcbnew pad mask settings
dialog](images/Pcbnew_pad_mask_settings_dialog.png)
:::
::::
:::::::::

:::::: sect3

#### Solder mask clearance {#_solder_mask_clearance}

::: paragraph
A value near to 0.2 mm is usually good. This value is positive because
the mask is usually bigger than the pad.
:::

::: paragraph
One can set a minimum value for the solder mask width, between 2 pads.
:::

::: paragraph
If the actual value is smaller than the minimum value, the 2 solder mask
shapes will be merged.
:::
::::::

::::: sect3

#### Solder paste clearance {#_solder_paste_clearance}

::: paragraph
The final clearance is the sum of the solder paste clearance and a
percentage of the pad size.
:::

::: paragraph
This value is negative because the mask is usually smaller than the pad.
:::
:::::
:::::::::::::::::::::

::::::::::::::: sect2

### Generating drill files {#_generating_drill_files}

::: paragraph
The creation of a drill file xxxx.drl following the EXCELLON standard is
always necessary.
:::

::: paragraph
One can also produce an optional drill report, and an optional drill
map.
:::

::: ulist

- The drill map can be plotted using several formats.

- The drill report is a plain text file.
:::

::: paragraph
The generation of these files is controlled via:
:::

::: ulist

- \"Create Drill File\" button, or

- Files/Fabrication Outputs/Drill file menu selection.
:::

::: paragraph
The Drill tools dialog box will be the following:
:::

:::: imageblock
::: content
![Pcbnew drill file dialog](images/Pcbnew_drill_file_dialog.png)
:::
::::

::: paragraph
For setting the coordinate origin, the following dialog box is used:
:::

:::: imageblock
::: content
![Pcbnew drill origin setting](images/Pcbnew_drill_origin_setting.png)
:::
::::

::: ulist

- Absolute: absolute coordinate system is used.

- Auxiliary axis: coordinates are relative to the auxiliary axis, use
  the icon (right toolbar) to set it.
:::
:::::::::::::::

:::: sect2

### Generating wiring documentation {#_generating_wiring_documentation}

::: paragraph
To produce wiring documentation files, the component and copper
silkscreen layers can be traced. Usually, just the component-side
silkscreen markings are sufficient for wiring a PCB. If the copper-side
silkscreen is used, the text it contains should be mirrored in order to
be readable.
:::
::::

:::: sect2

### Generation of files for automatic component insertion {#_generation_of_files_for_automatic_component_insertion}

::: paragraph
This option is accessed via the Postprocess/Create Cmp file menu option.
However, no file will be generated unless at least one footprint has the
Normal+Insert attribute activated (see Editing Footprints). One or two
files will be produced, depending upon whether insertable components are
present on one or both sides of the PCB. A dialogue box will display the
names of the file(s) created.
:::
::::

::::::: sect2

### Advanced tracing options {#_advanced_tracing_options}

::: paragraph
The options described below (part of the Files/Plot dialogue) allow for
fine-grained control of the tracing process. They are particularly
useful when printing the silkscreen markings for wiring documentation.
:::

:::: imageblock
::: content
![Pcbnew advanced tracing
options](images/Pcbnew_advanced_tracing_options.png)
:::
::::

::: paragraph
The available options are:
:::

+----------------------+-----------------------------------------------+
| Plot sheet reference | Trace sheet outline and the cartridge.        |
| on all layers        |                                               |
+----------------------+-----------------------------------------------+
| Plot pads on         | Enables/disables printing of pad outlines on  |
| silkscreen           | the silkscreen layers (if the pads have       |
|                      | already been declared to appear on these      |
|                      | layers). Prevents any pads from being printed |
|                      | in the disabled mode.                         |
+----------------------+-----------------------------------------------+
| Plot footprint       | Enables printing of VALUE text on the         |
| values               | silkscreen.                                   |
+----------------------+-----------------------------------------------+
| Plot footprint       | Enables printing of the REFERENCE text on the |
| references           | silkscreen.                                   |
+----------------------+-----------------------------------------------+
| Force plotting of    | Forces printing of fields (reference, value)  |
| invisible            | declared as invisible. In combination with    |
| values/references    | \'Plot footprint values\' and \'Plot          |
|                      | footprint references\', this option enables   |
|                      | production of documents for guiding wiring    |
|                      | and repair. These options have proven         |
|                      | necessary for circuits using components that  |
|                      | are too small (SMD) to allow readable         |
|                      | placement of two separate text fields.        |
+----------------------+-----------------------------------------------+
| Do not tent vias     | Delete the mask over the vias.                |
+----------------------+-----------------------------------------------+
| Exclude PCB edge     | GERBER format specific. Do not plot graphic   |
| layer from other     | items on edge layer.                          |
| layers               |                                               |
+----------------------+-----------------------------------------------+
| Use Protel filename  | GERBER format specific. When creating files,  |
| extensions           | use specific extensions for each file. If     |
|                      | disabled the Gerber file extension is .gbr.   |
+----------------------+-----------------------------------------------+
:::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Footprint Editor - Managing Libraries {#_footprint_editor_managing_libraries}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::::::::: sect2

### Overview of Footprint Editor {#_overview_of_footprint_editor}

::: paragraph
Pcbnew can simultaneously maintain several libraries. Thus, when a
footprint is loaded, all libraries that appear in the library list are
searched until the first instance of the footprint is found. In what
follows, note that the active library is the library selected within the
Footprint Editor, the program will now be described
:::

::: paragraph
Footprint Editor enables the creation and the editing of footprints:
:::

::: ulist

- Adding and removing pads.

- Changing pad properties (shape, layer) for individual pads or globally
  for all pads of a footprint.

- Editing graphic elements (lines, text).

- Editing information fields (value, reference, etc.).

- Editing the associated documentation (description, keywords).
:::

::: paragraph
Footprint Editor allows the maintenance of the active library as well
by:
:::

::: ulist

- Listing the footprints in the active library.

- Deletion of a footprint from the active library.

- Saving a footprint to the active library.

- Saving all of the footprints contained by a printed circuit.
:::

::: paragraph
It is also possible to create new libraries.
:::

::: paragraph
The library extension is `.mod`.
:::
::::::::::

:::::::: sect2

### Accessing Footprint Editor {#_accessing_footprint_editor}

::: paragraph
The Footprint Editor can be accessed in two different ways:
:::

::: ulist

- Directly, via the icon [![module
  editor](images/icons/module_editor.png)]{.image} in the main toolbar
  of Pcbnew.

- In the edit dialog for the active footprint (see figure below:
  accessed via the context menu), there is the button Footprint Editor.
:::

:::: imageblock
::: content
![Pcbnew module properties](images/Pcbnew_module_properties.png)
:::
::::

::: paragraph
In this case, the active footprint of the board will be loaded
automatically in Footprint Editor, enabling immediate editing or
archiving.
:::
::::::::

:::::: sect2

### Footprint Editor user interface {#_footprint_editor_user_interface}

::: paragraph
By calling Footprint Editor the following window will appear:
:::

:::: imageblock
::: content
![Modedit main window](images/Modedit_main_window.png)
:::
::::
::::::

:::::: sect2

### Top toolbar in Footprint Editor {#_top_toolbar_in_footprint_editor}

:::: imageblock
::: content
![Modedit top toolbar](images/Modedit_top_toolbar.png)
:::
::::

::: paragraph
From this toolbar, the following functions are available:
:::

+-------------------------------------------------------+--------------------------------------------------------+
| [![library](images/icons/library.png)]{.image}        | Select the active library.                             |
+-------------------------------------------------------+--------------------------------------------------------+
| [![save                                               | Save the current footprint to the active library, and  |
| library](images/icons/save_library.png)]{.image}      | write it to disk.                                      |
+-------------------------------------------------------+--------------------------------------------------------+
| [![new                                                | Create a new library and save the current footprint in |
| library](images/icons/new_library.png)]{.image}       | it.                                                    |
+-------------------------------------------------------+--------------------------------------------------------+
| [![modview                                            | Open the Footprint Viewer                              |
| icon](images/icons/modview_icon.png)]{.image}         |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![delete](images/icons/delete.png)]{.image}          | Access a dialog for deleting a footprint from the      |
|                                                       | active library.                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![new                                                | Create a new footprint.                                |
| footprint](images/icons/new_footprint.png)]{.image}   |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Create a footprint using a wizard                      |
| wizard](images/icons/module_wizard.png)]{.image}      |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![load module                                        | Load a footprint from the active library.              |
| lib](images/icons/load_module_lib.png)]{.image}       |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![load module                                        | Load (import) a footprint from the printed circuit     |
| board](images/icons/load_module_board.png)]{.image}   | board.                                                 |
+-------------------------------------------------------+--------------------------------------------------------+
| [![update module                                      | Export the current footprint to the printed circuit    |
| board](images/icons/update_module_board.png)]{.image} | board. when the footprint was previously imported from |
|                                                       | the current board. It will replace the corresponding   |
|                                                       | footprint on the board (i.e., respecting position and  |
|                                                       | orientation).                                          |
+-------------------------------------------------------+--------------------------------------------------------+
| [![insert module                                      | Export the current footprint to the printed circuit    |
| board](images/icons/insert_module_board.png)]{.image} | board. It will be copied on to the printed circuit     |
|                                                       | board at position 0.                                   |
+-------------------------------------------------------+--------------------------------------------------------+
| [![import                                             | Import a footprint from a file created by the Export   |
| module](images/icons/import_module.png)]{.image}      | command.                                               |
+-------------------------------------------------------+--------------------------------------------------------+
| [![export                                             | Export a footprint. This command is essentially        |
| module](images/icons/export_module.png)]{.image}      | identical to that for creating a library, the only     |
|                                                       | difference being that it creates a library in the user |
|                                                       | directory, while creating a library in the standard    |
|                                                       | library directory (usually kicad/modules).             |
+-------------------------------------------------------+--------------------------------------------------------+
| [![undo](images/icons/undo.png)]{.image}              | Undo and Redo                                          |
| [![redo](images/icons/redo.png)]{.image}              |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Invokes the footprint properties dialog.               |
| options](images/icons/module_options.png)]{.image}    |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![print                                              | Call the print dialog.                                 |
| button](images/icons/print_button.png)]{.image}       |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![zoom in](images/icons/zoom_in.png)]{.image}        | Standard zoom commands.                                |
| [![zoom out](images/icons/zoom_out.png)]{.image}      |                                                        |
| [![zoom                                               |                                                        |
| redraw](images/icons/zoom_redraw.png)]{.image}        |                                                        |
| [![zoom fit in                                        |                                                        |
| page](images/icons/zoom_fit_in_page.png)]{.image}     |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![options                                            | Call the pad editor.                                   |
| pad](images/icons/options_pad.png)]{.image}           |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
| [![module                                             | Perform a check of footprint correctness               |
| check](images/icons/module_check.png)]{.image}        |                                                        |
+-------------------------------------------------------+--------------------------------------------------------+
::::::

:::::: sect2

### Creating a new library {#_creating_a_new_library}

::: paragraph
The creation of a new library is done via the button [![new
library](images/icons/new_library.png)]{.image}, in this case the file
is created by default in the library directory or via the button
[![export module](images/icons/export_module.png)]{.image}, in which
case the file is created by default in your working directory.
:::

::: paragraph
A file-choosing dialog allows the name of the library to be specified
and its directory to be changed. In both cases, the library will contain
the footprint being edited.
:::

::: {.admonitionblock .warning}

+-----------------------------------+-----------------------------------+
| ::: title                         | If an old library of the same     |
| Warning                           | name exists, it will be           |
| :::                               | overwritten without warning.      |
+-----------------------------------+-----------------------------------+
:::
::::::

::::: sect2

### Saving a footprint in the active library {#_saving_a_footprint_in_the_active_library}

::: paragraph
The action of saving a footprint (thereby modifying the file of the
active library) is performed using this button [![save
library](images/icons/save_library.png)]{.image}. If a footprint of the
same name already exists, it will be replaced. Since you will depend
upon the accuracy of the library footprints, it is worth double-checking
the footprint before saving.
:::

::: paragraph
It is recommended to edit either the reference or value field text to
the name of the footprint as identified in the library.
:::
:::::

:::::: sect2

### Transferring a footprint from one library to another {#_transferring_a_footprint_from_one_library_to_another}

::: ulist

- Select the source library via the button
  [![library](images/icons/library.png)]{.image}.

- Load the footprint via the button [![load module
  lib](images/icons/load_module_lib.png)]{.image}.

- Select the destination library via the button
  [![library](images/icons/library.png)]{.image}.

- Save the footprint via the button [![save
  library](images/icons/save_library.png)]{.image}
:::

::: paragraph
You may also wish to delete the source footprint.
:::

::: ulist

- Reselect the source library with
  [![library](images/icons/library.png)]{.image}

- Delete the old footprint via the button
  [![delete](images/icons/delete.png)]{.image}
:::
::::::

::::: sect2

### Saving all footprints of your board in the active library {#_saving_all_footprints_of_your_board_in_the_active_library}

::: paragraph
It is possible to copy all of the footprints of a given board design to
the active library. These footprints will keep their current library
names. This command has two uses:
:::

::: ulist

- To create an archive or complete a library with the footprints from a
  board, in the event of the loss of a library.

- More importantly, it facilitates library maintenance by enabling the
  production of documentation for the library, as below.
:::
:::::

:::::::::::: sect2

### Documentation for library footprints {#_documentation_for_library_footprints}

::: paragraph
It is strongly recommended to document the footprints you create, in
order to enable rapid and error-free searching.
:::

::: paragraph
For example, who is able to remember all of the multiple pin-out
variants of a TO92 package? The Footprint Properties dialog offers a
simple solution to this problem.
:::

:::: imageblock
::: content
![Modedit module properties](images/Modedit_module_properties.png)
:::
::::

::: paragraph
This dialog accepts:
:::

::: ulist

- A one-line comment/description.

- Multiple keywords.
:::

::: paragraph
The description is displayed with the component list in Cvpcb and, in
Pcbnew, it is used in the footprint selection dialogs.
:::

::: paragraph
The keywords enable searches to be restricted to those footprints
corresponding to particular keywords.
:::

::: paragraph
When directly loading a footprint (the icon
[![module](images/icons/module.png)]{.image} of the right-hand Pcbnew
toolbar), keywords may be entered in the dialog box. Thus, entering the
text `=CONN` will cause the display of the list of footprints whose
keyword lists contain the word `CONN`.
:::
::::::::::::

:::::::::::::: sect2

### Documenting libraries - recommended practice {#_documenting_libraries_recommended_practice}

::: paragraph
It is recommended to create libraries indirectly, by creating one or
more auxiliary circuit boards that constitute the source of (part of)
the library, as follows: Create a circuit board in A4 format, in order
to be able to print easily to scale (scale = 1).
:::

::: paragraph
Create the footprints that the library will contain on this circuit
board. The library itself will be created with the File/Archive
footprints/Create footprint archive command.
:::

:::: imageblock
::: content
![Pcbnew archive footprints
menu](images/Pcbnew_archive_footprints_menu.png)
:::
::::

::: paragraph
The \"true source\" of the library will thus be the auxiliary circuit
board, and it is on this circuit that any subsequent alterations of
footprints will be made. Naturally, several circuit boards can be saved
in the same library.
:::

::: paragraph
It is generally a good idea to make different libraries for different
kinds of components (connectors, discretes,...​), since Pcbnew is able to
search many libraries when loading footprints.
:::

::: paragraph
Here is an example of such a library source:
:::

:::: imageblock
::: content
![Pcbnew example library](images/Pcbnew_example_library.png)
:::
::::

::: paragraph
This technique has several advantages:
:::

::: ulist

- The circuit can be printed to scale and serve as documentation for the
  library with no further effort.

- Future changes of Pcbnew may require regeneration of the libraries,
  something that can be done very quickly if circuit-board sources of
  this type have been used. This is important, because the circuit board
  file formats are guaranteed to remain compatible during future
  development, but this is not the case for the library file format.
:::
::::::::::::::

:::::: sect2

### Footprint Libraries Management {#_footprint_libraries_management}

::: paragraph
The list of footprint libraries in Pcbnew can be edited using the
Footprint Libraries Manager. This allows you to add and remove footprint
libraries by hand, and also allows you to invoke the Footprint Libraries
Wizard by pressing the \"Append With Wizard\" button.
:::

::: paragraph
The Footprint Libraries Wizard can also be invoked through the
Preferences menu, and can automatically add a library (detecting its
type) from a file or from a Github URL. The URL for the official
libraries is:
[https://github.com/KiCad](https://github.com/KiCad){.bare}
:::

::: paragraph
More details about footprint library tables and the Manager and Wizard
can be found in the CvPcb Reference Manual in the section *Footprint
Library Tables*.
:::
::::::

:::: sect2

### 3D Shapes Libraries Management {#_3d_shapes_libraries_management}

::: paragraph
The 3D shape libraries can be downloaded by 3D Shape Libraries Wizard.
It can be invoked from the menu Preferences → 3D Shapes Libraries
Downloader.
:::
::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::


---

::: {#header}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}

:::::::::::::::::::::::::::::::::::::::::::::::::::::: sect1

## KiCad Scripting Reference {#_kicad_scripting_reference}

::::::::::::::::::::::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Scripting allows you to automate tasks within KiCad using the
[Python](https://www.python.org/) language.
:::

::: paragraph
Also see the doxygen documentation on [Python Scripting
Reference](http://docs.kicad-pcb.org/doxygen-python/namespaces.html).
:::

::: paragraph
You can see python module help by typing `pydoc pcbnew` on your
terminal.
:::

::: paragraph
Using scripting you can create:
:::

::: ulist

- **Plugins**: this type of script is loaded when KiCad starts.
  Examples:

  ::: ulist

  - **Footprint Wizards**: To help you build footprints easily filling
    in parameters. See the dedicated section [Footprint
    Wizards](#Footprint_Wizards) below.

  - **File I/O** \'(planned)\': To let you write plugins to
    export/import other filetypes

  - **Actions** \'(experimental)\': Associate events to scripting
    actions or register new menus or toolbar icons.
  :::

- **Command Line Scripts**: scripts that can be used from the command
  line, load boards or libraries, modify them, and render outputs or new
  boards.
:::

::: paragraph
It shall be noted that the only KiCad application that supports
scripting is Pcbnew. It is also planned for Eeschema in the future.
:::

::::: sect2

### KiCad Objects {#_kicad_objects}

::: paragraph
The scripting API reflects the internal object structure inside
KiCad/pcbnew. BOARD is the main object, that has a set of properties and
a set of MODULEs, and TRACKs/VIAs, TEXTE_PCB, DIMENSION, DRAWSEGMENT.
Then MODULEs have D_PADs, EDGEs, etc.
:::

::: ulist

- See the BOARD section below.
:::
:::::

:::: sect2

### Basic API Reference {#_basic_api_reference}

::: paragraph
All the pcbnew API is provided from the \"pcbnew\" module in Python.
GetBoard() method will return the current pcb open at editor, useful for
commands written from the integrated scripting shell inside pcbnew or
action plugins.
:::
::::

::::::: sect2

### Loading and Saving a Board {#_loading_and_saving_a_board}

::: ulist

- **LoadBoard(filename):** loads a board from file returning a BOARD
  object, using the file format that matches the filename extension.

- **SaveBoard(filename,board):** saves a BOARD object to file, using the
  file format that matches the filename extension.

- **board.Save(filename):** same as above, but it's a method of BOARD
  object.
:::

::::: listingblock
::: title
Example that loads a board, hides all values, shows all references
:::

::: content

```python

#!/usr/bin/env python2.7
import sys
from pcbnew import *

filename=sys.argv[1]

pcb = LoadBoard(filename)
for module in pcb.GetModules():
    print "* Module: %s"%module.GetReference()
    module.Value().SetVisible(False)      # set Value as Hidden
    module.Reference().SetVisible(True)   # set Reference as Visible

pcb.Save("mod_"+filename)

```

:::
:::::
:::::::

:::::: sect2

### Listing and Loading Libraries {#_listing_and_loading_libraries}

::::: listingblock
::: title
Enumerate library, enumerate modules, enumerate pads
:::

::: content

```python

#!/usr/bin/python

from pcbnew import *

libpath = "/usr/share/kicad/modules/Sockets.pretty"
print ">> enumerate footprints, pads of",libpath

# Load the suitable plugin to read/write the .pretty library

# (containing the .kicad_mod footprint files)
src_type = IO_MGR.GuessPluginTypeFromLibPath( libpath );

# Rem: we can force the plugin type by using IO_MGR.PluginFind( IO_MGR.KICAD )
plugin = IO_MGR.PluginFind( src_type )

# Print plugin type name: (Expecting "KiCad" for a .pretty library)
print( "Selected plugin type: %s" % plugin.PluginName() )

list_of_footprints = plugin.FootprintEnumerate(libpath)

for name in list_of_footprints:
    fp = plugin.FootprintLoad(libpath,name)
    # print the short name of the footprint
    print name  # this is the name inside the loaded library
    # followed by ref field, value field, and decription string:
    # Remember ref and value texts are dummy texts, replaced by the schematic values
    # when reading a netlist.
    print "  ->", fp.GetReference(), fp.GetValue(), fp.GetDescription()

    # print pad info: GetPos0() is the pad position relative to the footrint position
    for pad in fp.Pads():
        print "    pad [%s]" % pad.GetPadName(), "at",\
        "pos0", ToMM(pad.GetPos0().x), ToMM(pad.GetPos0().y),"mm",\
        "shape offset", ToMM(pad.GetOffset().x), ToMM(pad.GetOffset().y), "mm"
    print ""

```

:::
:::::
::::::

::::::::: sect2

### BOARD {#_board}

::: paragraph
Board is the basic object in KiCad pcbnew, it's the document.
:::

::: paragraph
BOARD contains a set of object lists that can be accessed using the
following methods, they will return iterable lists that can be iterated
using \"for obj in list:\"
:::

::: ulist

- **board.GetModules():** This method returns a list of MODULE objects,
  all the modules available in the board will be exposed here.

- **board.GetDrawings():** Returns the list of BOARD_ITEMS that belong
  to the board drawings

- **board.GetTracks():** This method returns a list of TRACKs and VIAs
  inside a BOARD

- **board.GetFullRatsnest():** Returns the list of ratsnest (connections
  still not routed)

- **board.GetNetClasses():** Returns the list of net classes

- **board.GetCurrentNetClassName():** Returns the current net class

- **board.GetViasDimensionsList():** Returns the list of Via dimensions
  available to the board.

- **board.GetTrackWidthList():** Returns the list of Track Widths
  available to the board.
:::

::::: listingblock
::: title
Board Inspection Example
:::

::: content

```python

#!/usr/bin/env python
import sys
from pcbnew import *

filename=sys.argv[1]

pcb = LoadBoard(filename)

ToUnits = ToMM
FromUnits = FromMM

#ToUnits=ToMils

#FromUnits=FromMils

print "LISTING VIAS:"

for item in pcb.GetTracks():
    if type(item) is VIA:

        pos = item.GetPosition()
        drill = item.GetDrillValue()
        width = item.GetWidth()
        print " * Via:   %s - %f/%f "%(ToUnits(pos),ToUnits(drill),ToUnits(width))

    elif type(item) is TRACK:

        start = item.GetStart()
        end = item.GetEnd()
        width = item.GetWidth()

        print " * Track: %s to %s, width %f" % (ToUnits(start),ToUnits(end),ToUnits(width))

    else:
        print "Unknown type    %s" % type(item)

print ""
print "LIST DRAWINGS:"

for item in pcb.GetDrawings():
    if type(item) is TEXTE_PCB:
        print "* Text:    '%s' at %s"%(item.GetText(), item.GetPosition())
    elif type(item) is DRAWSEGMENT:
        print "* Drawing: %s"%item.GetShapeStr() # dir(item)
    else:
        print type(item)

print ""
print "LIST MODULES:"

for module in pcb.GetModules():
    print "* Module: %s at %s"%(module.GetReference(),ToUnits(module.GetPosition()))

print ""
print "Ratsnest cnt:",len(pcb.GetFullRatsnest())
print "track w cnt:",len(pcb.GetTrackWidthList())
print "via s cnt:",len(pcb.GetViasDimensionsList())

print ""
print "LIST ZONES:", pcb.GetAreaCount()

for idx in range(0, pcb.GetAreaCount()):
    zone=pcb.GetArea(idx)
    print "zone:", idx, "priority:", zone.GetPriority(), "netname", zone.GetNetname()

print ""
print "NetClasses:", pcb.GetNetClasses().GetCount(),

```

:::
:::::
:::::::::

::::::: sect2

### Examples {#_examples}

:::::: sect3

#### Change a component pin's paste mask margin {#_change_a_component_pins_paste_mask_margin}

::::: listingblock
::: title
We only want to change pins from 1 to 14, 15 is a thermal pad that must
be kept as it is.
:::

::: content

```python

#!/usr/bin/env python2.7
import sys
from pcbnew import *

filename=sys.argv[1]
pcb = LoadBoard(filename)

# Find module U304
u304 = pcb.FindModuleByReference('U304')
pads = u304.Pads()

#  Iterate over pads, printing solder paste margin
for p in pads:
    print p.GetPadName(), ToMM(p.GetLocalSolderPasteMargin())
    id = int(p.GetPadName())
    # Set margin to 0 for all but pad (pin) 15
    if id<15: p.SetLocalSolderPasteMargin(0)

pcb.Save("mod_"+filename)

```

:::
:::::
::::::
:::::::

:::::::::: sect2

### Footprint Wizards {#Footprint_Wizards}

::: paragraph
The footprint wizards are a collection of python scripts that can be
accessed from the Footprint Editor. If you invoke the footprint dialog
you select a given wizard that allows you to see the footprint rendered,
and you have some parameters you can edit.
:::

::: paragraph
If the plugins are not properly distributed to your system package, you
can find the latest versions in the KiCad source tree at
[launchpad](https://git.launchpad.net/kicad/tree/pcbnew/python/plugins).
:::

::: paragraph
They should be located in for example
`C:\Program Files\KiCad\share\kicad\scripting\plugins`.
:::

::: paragraph
On linux you can also keep your user plugins in `$HOME/.kicad_plugins`.
:::

::::: listingblock
::: title
Build footprints easily filling in parameters.
:::

::: content

```python
from __future__ import division
import pcbnew

import HelpfulFootprintWizardPlugin as HFPW


class FPC_FootprintWizard(HFPW.HelpfulFootprintWizardPlugin):

    def GetName(self):
        return "FPC (SMT connector)"

    def GetDescription(self):
        return "FPC (SMT connector) Footprint Wizard"

    def GetValue(self):
        pins = self.parameters["Pads"]["*n"]
        return "FPC_%d" % pins

    def GenerateParameterList(self):
        self.AddParam( "Pads", "n", self.uNatural, 40 )
        self.AddParam( "Pads", "pitch", self.uMM, 0.5 )
        self.AddParam( "Pads", "width", self.uMM, 0.25 )
        self.AddParam( "Pads", "height", self.uMM, 1.6)
        self.AddParam( "Shield", "shield_to_pad", self.uMM, 1.6 )
        self.AddParam( "Shield", "from_top", self.uMM, 1.3 )
        self.AddParam( "Shield", "width", self.uMM, 1.5 )
        self.AddParam( "Shield", "height", self.uMM, 2 )


    # build a rectangular pad
    def smdRectPad(self,module,size,pos,name):
        pad = pcbnew.D_PAD(module)
        pad.SetSize(size)
        pad.SetShape(pcbnew.PAD_SHAPE_RECT)
        pad.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        pad.SetLayerSet( pad.SMDMask() )
        pad.SetPos0(pos)
        pad.SetPosition(pos)
        pad.SetPadName(name)
        return pad

    def CheckParameters(self):
        p = self.parameters
        self.CheckParamInt( "Pads", "*n" )  # not internal units preceded by "*"


    def BuildThisFootprint(self):
        p = self.parameters
        pad_count       = int(p["Pads"]["*n"])
        pad_width       = p["Pads"]["width"]
        pad_height      = p["Pads"]["height"]
        pad_pitch       = p["Pads"]["pitch"]
        shl_width       = p["Shield"]["width"]
        shl_height      = p["Shield"]["height"]
        shl_to_pad      = p["Shield"]["shield_to_pad"]
        shl_from_top    = p["Shield"]["from_top"]

        offsetX         = pad_pitch * ( pad_count-1 ) / 2
        size_pad = pcbnew.wxSize( pad_width, pad_height )
        size_shld = pcbnew.wxSize(shl_width, shl_height)
        size_text = self.GetTextSize()  # IPC nominal

        # Gives a position and size to ref and value texts:
        textposy = pad_height/2 + pcbnew.FromMM(1) + self.GetTextThickness()
        self.draw.Reference( 0, textposy, size_text )

        textposy = textposy + size_text + self.GetTextThickness()
        self.draw.Value( 0, textposy, size_text )

        # create a pad array and add it to the module
        for n in range ( 0, pad_count ):
            xpos = pad_pitch*n - offsetX
            pad = self.smdRectPad(self.module,size_pad, pcbnew.wxPoint(xpos,0),str(n+1))
            self.module.Add(pad)


        # Mechanical shield pads: left pad and right pad
        xpos = -shl_to_pad-offsetX
        pad_s0_pos = pcbnew.wxPoint(xpos,shl_from_top)
        pad_s0 = self.smdRectPad(self.module, size_shld, pad_s0_pos, "0")
        xpos = (pad_count-1) * pad_pitch+shl_to_pad - offsetX
        pad_s1_pos = pcbnew.wxPoint(xpos,shl_from_top)
        pad_s1 = self.smdRectPad(self.module, size_shld, pad_s1_pos, "0")

        self.module.Add(pad_s0)
        self.module.Add(pad_s1)

        # add footprint outline
        linewidth = self.draw.GetLineThickness()
        margin = linewidth

        # upper line
        posy = -pad_height/2 - linewidth/2 - margin
        xstart = - pad_pitch*0.5-offsetX
        xend = pad_pitch * pad_count + xstart;
        self.draw.Line( xstart, posy, xend, posy )

        # lower line
        posy = pad_height/2 + linewidth/2 + margin
        self.draw.Line(xstart, posy, xend, posy)

        # around left mechanical pad (the outline around right pad is mirrored/y axix)
        yend = pad_s0_pos.y + shl_height/2 + margin
        self.draw.Line(xstart, posy, xstart, yend)
        self.draw.Line(-xstart, posy, -xstart, yend)

        posy = yend
        xend = pad_s0_pos.x - (shl_width/2 + linewidth + margin*2)
        self.draw.Line(xstart, posy, xend, posy)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)

        # set SMD attribute
        self.module.SetAttributes(pcbnew.MOD_CMS)

        # vertical segment at left of the pad
        xstart = xend
        yend = posy - (shl_height + linewidth + margin*2)
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)

        # horizontal segment above the pad
        xstart = xend
        xend = - pad_pitch*0.5-offsetX
        posy = yend
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy,-xend, yend)

        # vertical segment above the pad
        xstart = xend
        yend = -pad_height/2 - linewidth/2 - margin
        self.draw.Line(xstart, posy, xend, yend)

        # right pad side
        self.draw.Line(-xstart, posy, -xend, yend)


# register into pcbnew
FPC_FootprintWizard().register()

```

:::
:::::
::::::::::

:::::::::::: sect2

### Action Plugins {#action_menu}

::: paragraph
Action plugin associate events to scripting actions. Currently only
register a new menu is implemented.
:::

::: paragraph
New menu are available inside menu **Tools** ⇒ **External plugins**.
:::

:::: imageblock
::: content
![Pcbnew action menu](images/Pcbnew_action_menu.png)
:::
::::

::: ulist

- **Refresh**: reload plugins (create new menu if needed)

- **Add date on PCB**: An example plugin.
:::

::: paragraph
**Warning**: As all other python scripts, undo/redo function not work
(yet !).
:::

::::: listingblock
::: title
Action plugin example: Add date to any text item with content
\'\$date\$\'
:::

::: content

```python
import pcbnew
import re
import datetime

class text_by_date(pcbnew.ActionPlugin):
    """
    test_by_date: A sample plugin as an example of ActionPlugin
    Add the date to any text field of the board where the content is '$date$'
    How to use:

    - Add a text on your board with the content '$date$'

    - Call the plugin

    - Automaticaly the date will be added to the text (format YYYY-MM-DD)
    """

    def defaults(self):
        """
        Method defaults must be redefined
        self.name should be the menu label to use
        self.category should be the category (not yet used)
        self.description should be a comprehensive description
          of the plugin
        """
        self.name = "Add date on PCB"
        self.category = "Modify PCB"
        self.description = "Automaticaly add date on an existing PCB"

    def Run(self):
        pcb = pcbnew.GetBoard()
        for draw in pcb.GetDrawings():
            if draw.GetClass() == 'PTEXT':
                txt = re.sub("\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                                 "$date$", draw.GetText())
                if txt == "$date$":
                    draw.SetText("$date$ %s"%datetime.date.today())


text_by_date().register()

```

:::
:::::
::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}

::: {#footer-text}

Last updated 2026-03-15 16:35:47 -0700
:::
::::
