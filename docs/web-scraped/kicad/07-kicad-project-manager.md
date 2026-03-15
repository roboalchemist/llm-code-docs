:::::: {#header}

# KiCad

::: details
[The KiCad Team]{#author .author}\
:::

:::: {#toc .toc}
::: {#toctitle}
Table of Contents
:::

- [Introduction](#_introduction)
  - [KiCad](#_kicad)
  - [KiCad files and folders](#_kicad_files_and_folders)
- [Installation and configuration](#_installation_and_configuration)
  - [Display options](#_display_options)
  - [Initialization of the default
    configuration](#_initialization_of_the_default_configuration)
  - [Modifying the default
    configuration](#_modifying_the_default_configuration)
  - [Paths configuration](#_paths_configuration)
  - [Initialization of external
    utilities](#_initialization_of_external_utilities)
  - [Creating a new project](#_creating_a_new_project)
  - [Importing a foreign project](#_importing_a_foreign_project)
- [Using KiCad project manager](#_using_kicad_project_manager)
  - [Project manager window](#_project_manager_window)
  - [Utility launch pane](#_utility_launch_pane)
  - [Project tree view](#_project_tree_view)
  - [Top toolbar](#_top_toolbar)
- [Project templates](#_project_templates)
  - [Using templates](#_using_templates)
  - [Template Locations:](#_template_locations)
  - [Creating templates](#_creating_templates)
- [Upgrading from Version 4 to Version
  5](#_upgrading_from_version_4_to_version_5)
  - [Schematic Symbol Libraries](#_schematic_symbol_libraries)
    - [Global Symbol Library Table.](#_global_symbol_library_table)
    - [Symbol Library Table Mapping](#_symbol_library_table_mapping)
    - [Remapping Search Order](#_remapping_search_order)
    - [Symbol Names and Symbol Library Nickname
      Limitations](#_symbol_names_and_symbol_library_nickname_limitations)
  - [Symbol Cache Library
    Availability](#_symbol_cache_library_availability)
  - [Board File Format Changes](#_board_file_format_changes)
    - [Global Footprint Library
      Table.](#_global_footprint_library_table)

::::
::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#content}
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
2015, May 21.
:::
::::::::::::::
:::::::::::::::

:::::::::::::::::::::::: sect1

## Introduction {#_introduction}

::::::::::::::::::::::: sectionbody
::::::::::::: sect2

### KiCad {#_kicad}

::: paragraph
KiCad is an open-source software tool for the creation of electronic
schematic diagrams and PCB artwork. Beneath its singular surface, KiCad
incorporates an elegant ensemble of the following software tools:
:::

::: ulist

- **KiCad**: Project manager

- **Eeschema**: Schematic editor and component editor

- **Pcbnew**: Circuit board layout editor and footprint editor

- **GerbView**: Gerber viewer

:::

::: paragraph
3 utility tools are also included:
:::

::: ulist

- **Bitmap2Component**: Component maker for logos. It creates a
  schematic component or a footprint from a bitmap picture.

- **PcbCalculator**: A calculator that is helpful to calculate
  components for regulators, track width versus current, transmission
  lines, etc.

- **Pl Editor**: Page layout editor.

:::

::: paragraph
These tools are usually run from the project manager, but can be also
run as stand-alone tools.
:::

::: paragraph
KiCad does not present any board-size limitation and it can handle up to
32 copper layers, 14 technical layers and 4 auxiliary layers.
:::

::: paragraph
KiCad can create all the files necessary for building printed circuit
boards, including:
:::

::: ulist

- Gerber files for photo-plotters

- drilling files

- component location files

:::

::: paragraph
Being open source (GPL licensed), KiCad represents the ideal tool for
projects oriented towards the creation of electronic hardware with an
open-source flavour.
:::

::: paragraph
KiCad is available for Linux, Windows and Apple macOS.
:::
:::::::::::::

::::::::::: sect2

### KiCad files and folders {#_kicad_files_and_folders}

::: paragraph
KiCad creates and uses files with the following specific file extensions
(and folders) for schematic and board editing.
:::

::: paragraph
**Project manager file:**
:::

+-------------+--------------------------------------------------------+
| \*.pro      | Small file containing a few parameters for the current |
|             | project, including the component library list.         |
+-------------+--------------------------------------------------------+

::: paragraph
**Schematic editor files:**
:::

+---------------+--------------------------------------------------------+
| \*.sch        | Schematic files, which do not contain the components   |
|               | themselves.                                            |
+---------------+--------------------------------------------------------+
| \*.lib        | Schematic component library files, containing the      |
|               | component descriptions: graphic shape, pins, fields.   |
+---------------+--------------------------------------------------------+
| \*.dcm        | Schematic component library documentation, containing  |
|               | some component descriptions: comments, keywords,       |
|               | reference to data sheets.                              |
+---------------+--------------------------------------------------------+
| \*\_cache.lib | Schematic component library cache file, containing a   |
|               | copy of the components used in the schematic project.  |
+---------------+--------------------------------------------------------+
| sym-lib-table | Symbol library list (*symbol library table*): list of  |
|               | symbol libraries available in the schematic editor.    |
+---------------+--------------------------------------------------------+

::: paragraph
**Board editor files and folders:**
:::

+--------------+--------------------------------------------------------+
| \*.kicad_pcb | Board file containing all info but the page layout.    |
+--------------+--------------------------------------------------------+
| \*.pretty    | Footprint library folders. The folder itself is the    |
|              | library.                                               |
+--------------+--------------------------------------------------------+
| \*.kicad_mod | Footprint files, containing one footprint description  |
|              | each.                                                  |
+--------------+--------------------------------------------------------+
| \*.brd       | Board file in the legacy format. Can be read, but not  |
|              | written, by the current board editor.                  |
+--------------+--------------------------------------------------------+
| \*.mod       | Footprint library in the legacy format. Can be read by |
|              | the footprint or the board editor, but not written.    |
+--------------+--------------------------------------------------------+
| fp-lib-table | Footprint library list (*footprint library table*):    |
|              | list of footprint libraries (various formats) which    |
|              | are loaded by the board or the footprint editor or     |
|              | CvPcb.                                                 |
+--------------+--------------------------------------------------------+

::: paragraph
**Common files:**
:::

+--------------+--------------------------------------------------------+
| \*.kicad_wks | Page layout description files, for people who want a   |
|              | worksheet with a custom look.                          |
+--------------+--------------------------------------------------------+
| \*.net       | Netlist file created by the schematic, and read by the |
|              | board editor. This file is associated to the .cmp      |
|              | file, for users who prefer a separate file for the     |
|              | component/footprint association.                       |
+--------------+--------------------------------------------------------+

::: paragraph
**Special file:**
:::

+-------------+--------------------------------------------------------+
| \*.cmp      | Association between components used in the schematic   |
|             | and their footprints. It can be created by Pcbnew and  |
|             | imported by Eeschema. Its purpose is to import changes |
|             | from Pcbnew to Eeschema, for users who change          |
|             | footprints inside Pcbnew (for instance using *Exchange |
|             | Footprints* command) and want to import these changes  |
|             | in schematic.                                          |
+-------------+--------------------------------------------------------+

::: paragraph
**Other files:**
:::

::: paragraph
They are generated by KiCad for fabrication or documentation.
:::

+-------------+--------------------------------------------------------+
| \*.gbr      | Gerber files, for fabrication.                         |
+-------------+--------------------------------------------------------+
| \*.drl      | Drill files (Excellon format), for fabrication.        |
+-------------+--------------------------------------------------------+
| \*.pos      | Position files (ASCII format), for automatic insertion |
|             | machines.                                              |
+-------------+--------------------------------------------------------+
| \*.rpt      | Report files (ASCII format), for documentation.        |
+-------------+--------------------------------------------------------+
| \*.ps       | Plot files (Postscript), for documentation.            |
+-------------+--------------------------------------------------------+
| \*.pdf      | Plot files (PDF format), for documentation.            |
+-------------+--------------------------------------------------------+
| \*.svg      | Plot files (SVG format), for documentation.            |
+-------------+--------------------------------------------------------+
| \*.dxf      | Plot files (DXF format), for documentation.            |
+-------------+--------------------------------------------------------+
| \*.plt      | Plot files (HPGL format), for documentation.           |
+-------------+--------------------------------------------------------+
:::::::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::: sect1

## Installation and configuration {#_installation_and_configuration}

:::::::::::::::::::::::::::::::::::::::::::::: sectionbody
:::: sect2

### Display options {#_display_options}

::: paragraph
Hardware accelerated renderer in Pcbnew and Gerbview requires video card
with support of OpenGL v2.1 or higher.
:::
::::

::::: sect2

### Initialization of the default configuration {#_initialization_of_the_default_configuration}

::: paragraph
The default configuration file named **kicad.pro** is supplied in
kicad/template. It serves as a template for any new project and is used
to set the list of library files loaded by Eeschema. A few other
parameters for Pcbnew (default text size, default line thickness, etc.)
are also stored here.
:::

::: paragraph
Another default configuration file named **fp-lib-table** may exist. It
will be used only once to create a footprint library list; otherwise the
list will be created from scratch.
:::
:::::

:::::::: sect2

### Modifying the default configuration {#_modifying_the_default_configuration}

::: paragraph
The default **kicad.pro** file can be freely modified, if desired.
:::

::: paragraph
Verify that you have write access to kicad/template/kicad.pro
:::

::: paragraph
Run KiCad and load **kicad.pro** project.
:::

::: paragraph
Run Eeschema via KiCad manager. Modify and update the Eeschema
configuration, to set the list of libraries you want to use each time
you create new projects.
:::

::: paragraph
Run Pcbnew via KiCad manager. Modify and update the Pcbnew
configuration, especially the footprint library list. Pcbnew will create
or update a library list file called **footprint library table**. There
are 2 library list files (named fp-lib-table): The first (located in the
user home directory) is global for all projects and the second (located
in the project directory) is optional and specific to the project.
:::
::::::::

:::::::::::::: sect2

### Paths configuration {#_paths_configuration}

::: paragraph
In KiCad, one can define paths using an *environment variable*. A few
environment variables are internally defined by KiCad, and can be used
to define paths for libraries, 3D shapes, etc.
:::

::: paragraph
This is useful when absolute paths are not known or are subject to
change (e.g. when you transfer a project to a different computer), and
also when one base path is shared by many similar items. Consider the
following which may be installed in varying locations:
:::

::: ulist

- Eeschema component libraries

- Pcbnew footprint libraries

- 3D shape files used in footprint definitions

:::

::: paragraph
For instance, the path to the ***connect.pretty*** footprint library,
when using the **KISYSMOD** environment variable, would be defined as
***\${KISYSMOD}/connect.pretty***
:::

::: paragraph
This option allows you to define a path using an environment variable,
and add your own environment variables to define personal paths, if
needed.
:::

::: paragraph
**KiCad environment variables:**
:::

+-------------------------+--------------------------------------------------------+
| KICAD_PTEMPLATES        | Templates used during project creation (DEPRECATED as  |
|                         | of version 5.0.0-rc2, use KICAD_TEMPLATE_DIR instead). |
|                         | If you are using this variable, it must be defined.    |
+-------------------------+--------------------------------------------------------+
| KICAD_SYMBOL_DIR        | Base path of symbol library files.                     |
+-------------------------+--------------------------------------------------------+
| KIGITHUB                | Frequently used in example footprint lib tables. If    |
|                         | you are using this variable, it must be defined.       |
+-------------------------+--------------------------------------------------------+
| KISYS3DMOD              | Base path of 3D shapes files, and must be defined      |
|                         | because an absolute path is not usually used.          |
+-------------------------+--------------------------------------------------------+
| KISYSMOD                | Base path of footprint library folders, and must be    |
|                         | defined if an absolute path is not used in footprint   |
|                         | library names.                                         |
+-------------------------+--------------------------------------------------------+
| KICAD_TEMPLATE_DIR      | Location of templates installed with KiCad.            |
+-------------------------+--------------------------------------------------------+
| KICAD_USER_TEMPLATE_DIR | Location of personal templates.                        |
+-------------------------+--------------------------------------------------------+

:::: imageblock
::: content
![configure path dlg](images/configure_path_dlg.png)
:::
::::

::: paragraph
Note also the environment variable **KIPRJMOD** is **always** internally
defined by KiCad, and is the **current project absolute path**.
:::

::: paragraph
For instance, ***\${KIPRJMOD}/connect.pretty*** is always the
***connect.pretty*** folder (the pretty footprint library) found inside
**the current project folder**.
:::

::: paragraph
**If you modify the configuration of paths, please quit and restart
KiCad to avoid any issues in path handling.**
:::
::::::::::::::

:::::::::::::: sect2

### Initialization of external utilities {#_initialization_of_external_utilities}

::: paragraph
You may define your favorite text editor and PDF viewer. These settings
are used whenever you want to open a text or PDF file.
:::

::: paragraph
These settings are accessible from the Preference menu:
:::

:::: imageblock
::: content
![preferences menu](images/preferences_menu.png)
:::
::::

::::: sect3

#### Selection of text editor {#_selection_of_text_editor}

::: paragraph
Before using a text editor to browse/edit files in the current project,
you must choose the text editor you want to use.
:::

::: paragraph
Select ***Preferences → Set Text Editor*** to set the text editor you
want to use.
:::
:::::

:::::: sect3

#### Selection of PDF viewer {#_selection_of_pdf_viewer}

::: paragraph
You may use the default PDF viewer or choose your own.
:::

::: paragraph
To change from the default PDF viewer use ***Preferences → PDF Viewer →
Set PDF Viewer*** to choose the PDF viewer program, then select
***Preferences → PDF Viewer → Favourite PDF Viewer***.
:::

::: paragraph
On Linux the default PDF viewer is known to be fragile, so selecting
your own PDF viewer is recommended.
:::
::::::
::::::::::::::

::::::: sect2

### Creating a new project {#_creating_a_new_project}

::: paragraph
In order to manage a KiCad project consisting of schematic files,
printed circuit board files, supplementary libraries, manufacturing
files for photo-tracing, drilling and automatic component placement
files, it is recommended to create a project as follows:
:::

::: ulist

- **Create a working directory for the project** (using KiCad or by
  other means).

- **In this directory, use KiCad to create a project file** (file with
  extension .pro) via the \"Create a new project\" or \"Create a new
  project from template\" icon.

:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | Use a unique directory for each   |
| Warning                           | KiCad project. Do not combine     |
| :::                               | multiple projects into a single   |
|                                   | directory.                        |
+-----------------------------------+-----------------------------------+
:::

::: paragraph
KiCad creates a file with a .pro extension that maintains a number of
parameters for project management (such as the list of libraries used in
the schematic). Default names of both main schematic file and printed
circuit board file are derived from the name of the project. Thus, if a
project called **example.pro** was created in a directory called
**example**, the default files will be created:
:::

+-------------------+---------------------------------------------------+
| example.pro       | Project management file.                          |
+-------------------+---------------------------------------------------+
| example.sch       | Main schematic file.                              |
+-------------------+---------------------------------------------------+
| example.kicad_pcb | Printed circuit board file.                       |
+-------------------+---------------------------------------------------+
| example.net       | Netlist file.                                     |
+-------------------+---------------------------------------------------+
| example.\*        | Various files created by the other utility        |
|                   | programs.                                         |
+-------------------+---------------------------------------------------+
| example-cache.lib | Library file automatically created and used by    |
|                   | the schematic editor containing a backup of the   |
|                   | components used in the schematic.                 |
+-------------------+---------------------------------------------------+
:::::::

::::: sect2

### Importing a foreign project {#_importing_a_foreign_project}

::: paragraph
KiCad is able to import files created using other software packages.
Currently only Eagle 6.x or newer (XML format) is supported.
:::

::: paragraph
To import a foreign project, you need to select either a schematic or a
board file in the import file browser dialog. Imported schematic and
board files should have the same base file name (e.g. project.sch and
project.brd). Once the requested files are selected, you will be asked
to select a directory to store the imported files, which are going to be
saved as a KiCad project.
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::: sect1

## Using KiCad project manager {#_using_kicad_project_manager}

:::::::::::::::::::::::::: sectionbody
::: paragraph
KiCad project manager (kicad or kicad.exe) is a tool which can easily
run the other tools (schematic and PCB editors, Gerber viewer and
utility tools) when creating a design.
:::

::: paragraph
Running the other tools from KiCad manager has some advantages:
:::

::: ulist

- cross probing between schematic editor and board editor.

- cross probing between schematic editor and footprint selector (CvPcb).

:::

::: paragraph
However, you can only edit the current project files. When these tools
are run in *stand alone* mode, you can open any file in any project but
cross probing between tools can give strange results.
:::

:::::: sect2

### Project manager window {#_project_manager_window}

:::: imageblock
::: content
![main window](images/main_window.png)
:::
::::

::: paragraph
The main KiCad window is composed of a project tree view, a launch pane
containing buttons used to run the various software tools, and a message
window. The menu and the toolbar can be used to create, read and save
project files.
:::
::::::

::::::: sect2

### Utility launch pane {#_utility_launch_pane}

::: paragraph
KiCad allows you to run all standalone software tools that come with it.
:::

::: paragraph
The launch pane is made of the 8 buttons below that correspond to the
following commands (1 to 8, from left to right):
:::

:::: imageblock
::: content
![launch pane](images/launch_pane.png)
:::
::::

+---+----------------------+-----------------------------------------------------+
| 1 | **Eeschema**         | Schematic editor.                                   |
+---+----------------------+-----------------------------------------------------+
| 2 | **LibEdit**          | Component editor and component library manager.     |
+---+----------------------+-----------------------------------------------------+
| 3 | **Pcbnew**           | Board layout editor.                                |
+---+----------------------+-----------------------------------------------------+
| 4 | **FootprintEditor**  | Footprint editor and footprint library manager.     |
+---+----------------------+-----------------------------------------------------+
| 5 | **Gerbview**         | Gerber file viewer. It can also display drill       |
|   |                      | files.                                              |
+---+----------------------+-----------------------------------------------------+
| 6 | **Bitmap2component** | Tool to build a footprint or a component from a B&W |
|   |                      | bitmap image to create logos.                       |
+---+----------------------+-----------------------------------------------------+
| 7 | **Pcb Calculator**   | Tool to calculate track widths, and many other      |
|   |                      | things.                                             |
+---+----------------------+-----------------------------------------------------+
| 8 | **Pl Editor**        | Page layout editor, to create/customize frame       |
|   |                      | references.                                         |
+---+----------------------+-----------------------------------------------------+
:::::::

:::::::: sect2

### Project tree view {#_project_tree_view}

:::: imageblock
::: content
![project tree](images/project_tree.png)
:::
::::

::: paragraph
Double-clicking on the schematic file runs the schematic editor, in this
case opening the file **pic_programmer.sch**.
:::

::: paragraph
Double-clicking on the board file runs the layout editor, in this case
opening the file **pic_programmer.kicad_pcb**.
:::

::: paragraph
Right clicking on any of the files in the project tree allows generic
file manipulation.
:::
::::::::

:::::: sect2

### Top toolbar {#_top_toolbar}

:::: imageblock
::: content
![main toolbar](images/main_toolbar.png)
:::
::::

::: paragraph
KiCad top toolbar allows for some basic file operations:
:::

+----------------------------------------------------------------+----------------------------------------------------+
| [![new project](images/icons/new_project.png)]{.image}         | Create a new project. If the default template file |
|                                                                | (kicad.pro) is found in **kicad/template**, it is  |
|                                                                | copied into the working directory.                 |
+----------------------------------------------------------------+----------------------------------------------------+
| [![new project with                                            | Create a new project from an existing template.    |
| template](images/icons/new_project_with_template.png)]{.image} |                                                    |
+----------------------------------------------------------------+----------------------------------------------------+
| [![open project](images/icons/open_project.png)]{.image}       | Open an existing project.                          |
+----------------------------------------------------------------+----------------------------------------------------+
| [![save project](images/icons/save_project.png)]{.image}       | Update and save the current project tree.          |
+----------------------------------------------------------------+----------------------------------------------------+
| [![zip](images/icons/zip.png)]{.image}                         | Create a zip archive of the whole project. This    |
|                                                                | includes schematic files, libraries, PCB, etc.     |
+----------------------------------------------------------------+----------------------------------------------------+
| [![reload](images/icons/reload.png)]{.image}                   | Refresh the tree view, sometimes needed after a    |
|                                                                | tree change.                                       |
+----------------------------------------------------------------+----------------------------------------------------+
::::::
::::::::::::::::::::::::::
:::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::: sect1

## Project templates {#_project_templates}

:::::::::::::::::::::::::::::::::: sectionbody
::: paragraph
Using a project template facilitates setting up a new project with
predefined settings. Templates may contain pre-defined board outlines,
connector positions, schematic elements, design rules, etc. Complete
schematics and/or PCBs used as seed files for the new project may even
be included.
:::

:::::::::: sect2

### Using templates {#_using_templates}

::: paragraph
The ***File → New Project → New Project from Template*** menu will open
the Project Template Selector dialog:
:::

:::: imageblock
::: content
![template selector](images/template_selector.png)
:::
::::

::: paragraph
A single click on a template's icon will display the template
information, and a further click on the OK button creates the new
project. The template files will be copied to the new project location
and renamed to reflect the new project's name.
:::

::: paragraph
After selection of a template:
:::

:::: imageblock
::: content
![template selected](images/template_selected.png)
:::
::::
::::::::::

::::: sect2

### Template Locations: {#_template_locations}

::: paragraph
KiCad looks for template files in the following paths:
:::

::: ulist

- path defined in the environment variable KICAD_USER_TEMPLATE_DIR

- path defined in the environment variable KICAD_TEMPLATE_DIR

- System templates: \<kicad bin dir\>/../share/kicad/template/

- User templates:

  ::: ulist
  - Unix: \~/kicad/templates/

  - Windows: C:\\Documents and Settings\\username\\My
    Documents\\kicad\\templates

  - Mac: \~/Documents/kicad/templates/
  :::

- When the environment variable KICAD_PTEMPLATES is defined there is a
  third tab, Portable Templates, which lists templates found at the
  KICAD_PTEMPLATES path (DEPRECATED).

:::
:::::

::::::::::::::::::::: sect2

### Creating templates {#_creating_templates}

::: paragraph
The template name is the directory name where the template files are
stored. The metadata directory is a subdirectory named **meta**
containing files describing the template.
:::

::: paragraph
All files and directories in a template are copied to the new project
path when a project is created using a template, except **meta**.
:::

::: paragraph
When a new project is created from a template, all files and directories
starting with the template name will be renamed with the new project
file name, excluding the file extension.
:::

::: paragraph
The metadata consists of one required file, and may contain optional
files. All files must be created by the user using a text editor or
previous KiCad project files, and placed into the required directory
structure.
:::

::: paragraph
Here is an example showing project files for **raspberrypi-gpio**
template:
:::

:::: imageblock
::: content
![template tree](images/template_tree.png)
:::
::::

::: paragraph
And the metadata files:
:::

:::: imageblock
::: content
![template tree meta](images/template_tree_meta.png)
:::
::::

:::::::: sect3

#### Required File: {#_required_file}

+----------------+--------------------------------------------------------+
| meta/info.html | HTML-formatted information describing the template.    |
+----------------+--------------------------------------------------------+

::: paragraph
The \<title\> tag determines the actual name of the template that is
exposed to the user for template selection. Note that the project
template name will be cut off if it's too long. Due to font kerning,
typically 7 or 8 characters can be displayed.
:::

::: paragraph
Using HTML means that images can be easily in-lined without having to
invent a new scheme. Only basic HTML tags can be used in this document.
:::

::: paragraph
Here is a sample **info.html** file:
:::

:::: listingblock
::: content

``` highlight
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML>
<HEAD>
<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html;
charset=windows-1252">
<TITLE>Raspberry Pi - Expansion Board</TITLE>
</HEAD>
<BODY LANG="fr-FR" DIR="LTR">
<P>This project template is the basis of an expansion board for the
<A HREF="http://www.raspberrypi.org/" TARGET="blank">Raspberry Pi $25
ARM board.</A> <BR><BR>This base project includes a PCB edge defined
as the same size as the Raspberry-Pi PCB with the connectors placed
correctly to align the two boards. All IO present on the Raspberry-Pi
board is connected to the project through the 0.1&quot; expansion
headers. <BR><BR>The board outline looks like the following:
</P>
<P><IMG SRC="brd.png" NAME="brd" ALIGN=BOTTOM WIDTH=680 HEIGHT=378
BORDER=0><BR><BR><BR><BR>
</P>
<P>(c)2012 Brian Sidebotham<BR>(c)2012 KiCad Developers</P>
</BODY>
</HTML>
```

:::
::::
::::::::

:::: sect3

#### Optional Files: {#_optional_files}

+---------------+--------------------------------------------------------+
| meta/icon.png | A 64 x 64 pixel PNG icon file which is used as a       |
|               | clickable icon in the template selection dialog.       |
+---------------+--------------------------------------------------------+

::: paragraph
Any other image files used by **meta/info.html**, such as the image of
the board file in the dialog above, are placed in this folder as well.
:::
::::
:::::::::::::::::::::
::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::

# Upgrading from Version 4 to Version 5 {#_upgrading_from_version_4_to_version_5 .sect0}

::::: {.openblock .partintro}
:::: content
::: paragraph
Changes were made to the behavior to KiCad during the version 5
development that can impact projects created with older versions of
KiCad. This section serves as a guide to ensure the smoothest possible
path when upgrading to version 5 of KiCad.
:::
::::
:::::

:::::::::::::::::::::::: sect1

## Schematic Symbol Libraries {#_schematic_symbol_libraries}

::::::::::::::::::::::: sectionbody
::: paragraph
Schematic symbol libraries are no longer accessed using a symbol
(referred to as components in version 4) look up list. Symbol libraries
are now managed by a symbol library table that behaves similarly to the
footprint library table. This change is a significant improvement, but
some schematics may need manual intervention when being converted to
version 5.
:::

::: paragraph
In previous versions, KiCad used a list of library files to search when
locating symbols in the Eeschema file. When locating a symbol, each path
would be searched and the first library that held the symbol name would
be used.
:::

::: paragraph
From v5, KiCad symbol names are prefixed with a nickname, and a [lookup
table matching nicknames to library
paths](https://github.com/KiCad/kicad-doc/blob/master/src/kicad/kicad_upgrading_from_v4_to_v5.adoc)
is used to locate the library which holds the symbol. The table is
called the \'symbol library table\' and built from configuration files
stored in the user's KiCad configuration directory and the currently
loaded project directory.
:::

::: paragraph
To upgrade a KiCad project from v4 to v5, nicknames for all of the
library files need to be created and then schematic symbol names need to
be prefixed with the correct nickname.
:::

::::: sect2

### Global Symbol Library Table. {#_global_symbol_library_table}

::: paragraph
Eeschema v5 will automatically create a global symbol table when first
started. You will be given a chance to skip this and create your own
global symbol table by hand. You only need to do this if don't use KiCad
symbol libraries at all. Otherwise it is easier to modify the
automatically generated global symbol table.
:::

::: {.admonitionblock .note}
+-----------------------------------+------------------------------------------------------+
| ::: title                         | If you track the [symbol library                     |
| Note                              | repository](https://github.com/KiCad/kicad-symbols), |
| :::                               | changes made to the default global symbol library    |
|                                   | table are not tracked by KiCad. You will have to     |
|                                   | manually keep the global symbol library table up to  |
|                                   | date.                                                |
+-----------------------------------+------------------------------------------------------+
:::
:::::

:::::::: sect2

### Symbol Library Table Mapping {#_symbol_library_table_mapping}

::: paragraph
Automatic remapping of symbols will be executed whenever a schematic is
opened that has not been remapped. There are a few steps you should take
ahead of time in order for the remapping to be the most effective.
:::

::: {.admonitionblock .note}
+-----------------------------------+----------------------------------------------------------------------------------+
| ::: title                         | If you have been using a development build of KiCad, copy the full default       |
| Note                              | global symbol library table file (sym-lib-table) from the template folder        |
| :::                               | installed with the KiCad libraries or from the [KiCad library                    |
|                                   | repo](https://github.com/KiCad/kicad-library/blob/master/template/sym-lib-table) |
|                                   | to your KiCad user configuration folder. This will replace the empty one (most   |
|                                   | likely) created by Eeschema. If you do not do this, you will most likely end up  |
|                                   | with a bunch of broken symbol links.                                             |
+-----------------------------------+----------------------------------------------------------------------------------+
:::

::: {.admonitionblock .warning}
+-----------------------------------+-----------------------------------+
| ::: title                         | Remapped schematics will not be   |
| Warning                           | compatible with older versions of |
| :::                               | KiCad. The Remap Symbols dialog   |
|                                   | will make a backup of your        |
|                                   | schematic files and you should do |
|                                   | the same if you remap manually.\  |
+-----------------------------------+-----------------------------------+
:::

::: {.olist .arabic}

1. If possible, keep version 4 of KiCad installed on your system unless
    you have never used any of the symbol libraries distributed with
    KiCad.

2. If you get warning about missing libraries when you start version 4
    of Eeschema, make sure to fix the missing libraries if they contain
    symbols that are in the schematic before you attempt to remap your
    schematic. Otherwise, the correct symbol will not be found and you
    will end up with broken symbol links in your schematic. You can test
    this by left clicking on a symbol in the schematic and verifying
    that the symbol is not being loaded from the cache library. If a
    symbol is being loaded from the cache library, Eeschema cannot find
    your part in the system or project symbol libraries. If you need a
    cached part to be available to other projects on your system, you
    will need to integrate it into a system or project library manually.

3. If symbol recovery is required during the remapping process, do not
    dismiss it. Failure to recover symbols will result in broken symbol
    links or the wrong symbol being linked in the schematic.

4. During the remapping process, symbol libraries not found in the
    global symbol library table will be used to create a project
    specific symbol library table. You can move them manually to the
    global symbol library table if that is your preference.

5. For the most accurate remapping, create a project library by copying
    the project cache file (project-name-cache.lib) to a different file
    and add it to the top of the symbol library list. You must use a
    version of KiCad prior to the symbol library table implementation in
    order to do this.

:::

::: {.admonitionblock .note}
+-----------------------------------+-----------------------------------+
| ::: title                         | ::: title                         |
| Note                              | **Fixing broken remapping:**      |
| :::                               | :::                               |
|                                   |                                   |
|                                   | A tool has been provided to       |
|                                   | attempt to fix remapping issues.  |
|                                   | If there are missing symbol       |
|                                   | library links in a schematic,     |
|                                   | they can be fixed by opening the  |
|                                   | \"Tools→Edit Symbol Library       |
|                                   | References...​\" menu entry and    |
|                                   | clicking on the \"Map Orphans\"   |
|                                   | button.                           |
+-----------------------------------+-----------------------------------+
:::
::::::::

::::: sect2

### Remapping Search Order {#_remapping_search_order}

::: paragraph
When remapping symbols, KiCad proceeds in the following order to assign
the library to a symbol:
:::

::: {.olist .arabic}

1. Global Symbol Library Table: Symbols are preferentially mapped to
    the global symbol library table, if one exists.

2. Project specific libraries: Libraries listed in the project library
    list that are not in the global symbol library table are searched
    next.

3. Project cache file: If a symbol doesn't exist in the listed
    libraries above, it is first rescued --- a copy is made from the
    cache and placed in the *proj*-rescue.lib --- before the symbol is
    mapped to this new, rescue library.

:::
:::::

:::::: sect2

### Symbol Names and Symbol Library Nickname Limitations {#_symbol_names_and_symbol_library_nickname_limitations}

::: paragraph
Symbol names may not contain `<SPACE>, ':', '/'`.
:::

::: paragraph
Library nicknames may not contain `<SPACE>, ':'`.
:::

::: paragraph
Existing symbol names with these characters must be renamed by manually
editing the relevant schematic and library files.
:::
::::::
:::::::::::::::::::::::
::::::::::::::::::::::::

::::: sect1

## Symbol Cache Library Availability {#_symbol_cache_library_availability}

:::: sectionbody
::: paragraph
The cache library is no longer shown in either the symbol library viewer
or the symbol library editor. The cache should never be edited because
any changes are overwritten by the next schematic save.
:::
::::
:::::

:::::::: sect1

## Board File Format Changes {#_board_file_format_changes}

::::::: sectionbody
::: paragraph
Several new features have been added to Pcbnew which impact the board
file format. Using these new features in board designs will prevent them
from being opened with previous versions of Pcbnew.
:::

::: ulist

- Rounded rectangle footprint pads.

- Custom shape footprint pads.

- Footprint pad names longer than four characters.

- Keep out zones on more than a single layer.

- 3D models offset saved as millimeters instead of inches.

- Footprint text locking.

:::

:::: sect2

### Global Footprint Library Table. {#_global_footprint_library_table}

::: paragraph
If you track the [footprint library
repository](https://github.com/KiCad/kicad-footprints), changes made to
the default global footprint library table are not tracked by KiCad. You
will have to manually keep the global footprint library table up to
date.
:::
::::
:::::::
::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::: {#footer}
::: {#footer-text}
Last updated 2026-03-15 16:35:47 -0700
:::
::::
