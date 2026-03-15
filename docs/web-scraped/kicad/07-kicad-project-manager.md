# KiCad 9.0 Project Manager Documentation

## Introduction

KiCad is an open-source suite for designing electronic schematics and PCBs. It operates on multiple platforms and supports designs with up to 32 copper layers. The latest documentation can be found at https://docs.kicad.org.

### System Requirements

KiCad runs on various hardware configurations, though a dedicated graphics card and 1920x1080+ display are recommended for optimal performance. Specific system requirements are available at https://kicad.org/help/system-requirements/.

## Installation and Settings

### Initial Configuration

Upon launching a new KiCad version, users receive a settings initialization prompt. The system can automatically detect and import configurations from previous versions, though symbol and footprint library tables require manual migration.

Configuration folders are version-specific:
- **Windows**: `%APPDATA%\kicad\9.0`
- **Linux**: `~/.config/kicad/9.0`
- **macOS**: `/Users/<username>/Library/Preferences/kicad/9.0`

### File Migration

Modern KiCad versions maintain backward compatibility for opening legacy files. Files created or modified by one version of KiCad cannot be opened by older versions. Users should maintain backup copies when testing new releases.

Hotkey configurations require manual transfer between versions by copying `.hotkeys` files from the old configuration directory.

## Project Manager Overview

The KiCad Project Manager serves as the central hub for creating projects and launching all KiCad tools:

- Schematic Editor
- Symbol Editor
- PCB Editor
- Footprint Editor
- Gerber Viewer
- Image Converter
- Calculator Tools
- Drawing Sheet Editor
- Plugin and Content Manager

The interface features a left-side tree view displaying project files and a right-side launcher with tool shortcuts.

### Project Structure

A complete KiCad project requires:
- Project file (`.kicad_pro`)
- Schematic root sheet (`.kicad_sch`)
- Board file (`.kicad_pcb`)

Schematics may contain multiple sheets, but a project contains only one board design.

## Creating Projects

### New Project Workflow

Use **File** → **New Project** (or `Ctrl+N`) to create a new project. The system generates a dedicated project directory containing:

| File | Purpose |
|------|---------|
| `example.kicad_pro` | Project configuration |
| `example.kicad_sch` | Main schematic |
| `example.kicad_pcb` | PCB design |

### Importing from Other Tools

KiCad supports importing complete projects from:
- Eagle 6.x+ (`.sch`, `.brd`)
- CADSTAR (`.csa`, `.cpa`)
- EasyEDA Standard/Pro (`.zip`)

Standalone schematics and boards can be imported from Altium Designer, P-Cad, and Fabmaster formats. KiCad does not support schematics with multiple top-level sheets.

## Project Archives

### Creating Backups

Use **File** → **Archive Project** to create zip archives containing:
- Design files (`.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, etc.)
- Legacy files (`.sch`, `.lib`, `.brd`)
- 3D models (`.stp`, `.step`)
- Manufacturing files (Gerber, drill, position data)
- Documentation and scripts

### Extracting Archives

The Unarchive tool (**File** → **Unarchive Project**) automatically reloads projects when extracted into the current directory.

## Git Integration

### Enabling Version Control

KiCad provides integrated Git support for tracking project changes. Projects already under version control display:
- Active branch name next to project title
- File status icons indicating changes, additions, or tracked status

Disable Git features via **Preferences** → **Version Control**.

### Adding Version Control to Existing Projects

Right-click project files and select **Version Control** → **Add Project to Version Control**. Configuration requires:
- Remote location (HTTPS, SSH, or local path)
- Authentication credentials
- SSH key information (if applicable)

### Workflow Operations

**Committing changes**: Right-click → **Version Control** → **Commit Project** (or specific file)

**Synchronizing**: Use **Push** and **Pull** options from the Version Control menu

**Branch management**: Select desired branch from **Version Control** → **Switch to Branch**

## File Organization

### Core Design Files

| Extension | Purpose |
|-----------|---------|
| `.kicad_pro` | Project settings shared between schematic and PCB |
| `.kicad_sch` | Schematic with symbols and connections |
| `.kicad_sym` | Symbol library definitions |
| `.kicad_pcb` | Board design data |
| `.kicad_mod` | Individual footprint definitions |
| `.pretty` | Footprint library folders |

### Supporting Files

| Extension | Purpose |
|-----------|---------|
| `.kicad_prl` | Local project settings (not required for distribution) |
| `.kicad_dru` | Custom design rules |
| `.kicad_wks` | Page layout definitions |
| `fp-lib-table` | Footprint library registry |
| `sym-lib-table` | Symbol library registry |

### Manufacturing Outputs

| Extension | Purpose |
|-----------|---------|
| `.gbr` | Gerber fabrication files |
| `.drl` | Drill files (Excellon format) |
| `.pos` | Component placement data |
| `.net` | Netlist from schematic |

### Legacy Formats

KiCad reads but doesn't write files from earlier versions:
- `.sch` and `.lib` (KiCad 5.x)
- `.brd` and `.mod` (KiCad 4.x)
- `-cache.lib` (legacy component library cache)

## Configuration and Preferences

Access preferences via **Preferences** menu or `Ctrl+,`. Settings are shared across KiCad tools.

### Common Settings

**Graphics rendering**: Choose antialiasing methods (accelerated or fallback)

**Interface**: Configure text editors, PDF viewers, icon display, and scrollbar visibility

**Mouse behavior**: Control cursor warping and focus behavior between editors

**Autosave**: Enable periodic saves; set interval to 0 to disable

**Backup options**: Configure automatic project archiving with customizable retention limits and maximum backup sizes

**File history**: Set recently-opened file list length

**3D cache**: Configure duration before deleting cached 3D models

### Mouse and Touchpad

**Zoom behavior**: Enable acceleration, configure speed, center cursor on zoom

**Pan control**: Set middle/right mouse button functions; enable horizontal scrolling

**Object movement**: Auto-pan near canvas edges with configurable speed

**Drag operations**: Define left-button behavior based on object selection status

### Hotkey Configuration

Access via **Preferences** → **Hotkeys**. Features include:

- Customize any available command hotkey
- View common hotkeys (shared across all KiCad tools)
- Tool-specific hotkeys displayed when each tool is running
- Conflict detection when reassigning keys
- Undo individual changes or reset all hotkeys

**Importing hotkeys**: Copy `.hotkeys` files to the new version's settings directory

## Path Variables and Environment

### KiCad Path Variables

Configure via **Preferences** → **Configure Paths**:

| Variable | Purpose |
|----------|---------|
| `KICAD9_3DMODEL_DIR` | Standard 3D model library path |
| `KICAD9_FOOTPRINT_DIR` | Standard footprint library path |
| `KICAD9_SYMBOL_DIR` | Standard symbol library path |
| `KICAD9_TEMPLATE_DIR` | Project template library path |
| `KICAD9_3RD_PARTY` | Plugin and content manager installation location |
| `KICAD_USER_TEMPLATE_DIR` | Custom project template storage |
| `KIPRJMOD` | Current project directory (auto-set, non-editable) |

### Advanced Environment Variables

Set externally (not in Preferences):
- `KICAD_CONFIG_HOME`: Configuration file base path
- `KICAD_DOCUMENTS_HOME`: User documents base path
- `KICAD_STOCK_DATA_HOME`: Default library and data location

Versioned path variables from older KiCad versions automatically resolve to current equivalents if not explicitly defined.

## Library Management

### Symbol Libraries

Access via **Preferences** → **Manage Symbol Libraries**

Maintains two tables:
- **Global**: Available to all projects
- **Project-specific**: Optional, located in project directory

### Footprint Libraries

Access via **Preferences** → **Manage Footprint Libraries**

Implements same global/project-specific dual-table structure

## Project Templates

### Using Templates

**File** → **New Project from Template** opens the Template Selector. Single-click displays template information; confirm with OK to create the project.

Template files are copied to the new project location with renamed filenames reflecting the new project name.

### Template Locations

- **System templates**: `KICAD9_TEMPLATE_DIR` path variable
- **User templates**: `KICAD_USER_TEMPLATE_DIR` path variable
- **Custom locations**: Browse arbitrary directories using the Folder control

### Creating Templates

A template is a directory containing project files plus a `meta` subfolder with:
- `info.html`: Template description displayed in selector (required)
- `icon.png`: 64×64 pixel template icon (optional)

**Metadata file**: The `<title>` tag in `info.html` determines the displayed template name

**File copying**: All files are copied except dotfiles (files starting with `.`), with exceptions for `.gitignore` and `.gitattributes`

**File renaming**: Files containing the template directory name are renamed to match the new project name

**Partial templates**: Missing project files are created using default project generation behavior

## Jobsets

Jobsets define output configurations allowing multiple jobs to be generated with a single command. Each jobset contains jobs (individual output types) and destinations (job groupings with defined output locations).

### Creating and Opening Jobsets

**File** → **New Jobset File** creates new jobset (`.kicad_jobset`)

**File** → **Open Jobset File** loads existing jobset

Project-stored jobsets appear in the project file tree and can be opened by double-clicking.

### Jobs

Jobs represent individual output types. Right-click to:
- **Edit Job Description**: Modify display name
- **Edit Job Settings**: Reconfigure output parameters
- **Remove**: Delete from jobset

Output filenames support text variables: `${PROJECTNAME}`, `${CURRENT_DATE}`, and project-defined variables.

### Jobset Destinations

Destinations define how outputs are stored:
- **Archive**: Compress outputs in zip file
- **Folder**: Save outputs uncompressed

Features:
- Select which jobs run for this destination
- Set absolute or relative output paths
- Use path and text variables in output locations
- Configure folder/archive naming

All outputs are generated in temporary folders, then moved to the final destination after all jobs complete successfully.

### Available Job Types

**PCB exports**: 3D models, drill data, DXF, Gerber, IPC-2581, ODB++, PDF, position data, SVG

**PCB operations**: Design Rule Check, 3D rendering

**Schematic exports**: DXF, HPGL, netlist, PDF, PostScript, SVG

**Schematic operations**: Bill of Materials generation, Electrical Rule Check

**Utilities**: File copying, command execution

## Plugin and Content Manager

The PCM provides access to community-developed packages including plugins, libraries, and color themes.

### Repository Management

**Default**: KiCad official repository (enabled by default)

**Adding repositories**: **Manage** → ![plus icon] → enter repository URL

**Removing repositories**: Select repository → ![trash icon]

**Reinstating default**: **Add Default Repository** option in dropdown menu

### Package Categories

**Plugins**: Tools launching from PCB Editor; includes footprint wizards

**Fabrication plugins**: Sub-category for manufacturer-specific ordering tools

**Libraries**: Symbol, footprint, and 3D model collections with auto-configuration of library tables

**Color themes**: Schematics, symbol, board, and footprint editor themes

### Package Installation

1. Select package → **Install** button
2. Choose version if multiple available
3. Package queued in **Pending** tab
4. Click **Apply Pending Changes** to install all queued packages

### Managing Installed Packages

**Updates**: Click **Update** for specific package or **Update All** for all

**Uninstall**: Click **Uninstall** button (queued until changes applied)

**Pin Package**: Prevents automatic updates via dropdown menu

**Download only**: **Download** button saves package without installation; use **Install from file** to install later

## Project Manager Actions Reference

| Action | Default Hotkey | Function |
|--------|---|----------|
| New Project | Ctrl+N | Create blank project |
| New Project from Template | Ctrl+T | Create from template |
| Open Project | Ctrl+O | Open existing project |
| Clone Project from Repository | — | Clone remote repository |
| Close Project | — | Close current project |
| Schematic Editor | Ctrl+E | Edit schematic |
| Symbol Editor | Ctrl+L | Edit symbols |
| PCB Editor | Ctrl+P | Edit board |
| Footprint Editor | Ctrl+F | Edit footprints |
| Gerber Viewer | Ctrl+G | Preview Gerber files |
| Drawing Sheet Editor | Ctrl+Y | Edit borders/title blocks |
| Image Converter | Ctrl+B | Convert images |
| Plugin and Content Manager | Ctrl+M | Browse/install packages |
| Calculator Tools | — | Component calculations |
| Open Demo Project | — | Load example project |
| Open Text Editor | — | Launch text editor |

## Important Notes

- Symbol and footprint library tables from the previous version of KiCad will not be imported
- When sharing projects, include `.kicad_pro` file for complete design information
- Files like `.kicad_prl` and `fp-info-cache` are not required for distribution
- Design information is embedded within schematic and board files; external libraries are automatically included

---

**Documentation Version**: Based on KiCad 9.0.8
**License**: GNU General Public License v3+ or Creative Commons Attribution License 3.0+
