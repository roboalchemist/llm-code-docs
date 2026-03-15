traceview 2.1.0 - Docs.rs
        
    

    

    
        
            

                
                
                    
                    Docs.rs
                

    
- 
            
                
                traceview-2.1.0
            
        
    

                
                

                    
- 
                        docs.rs
                        

  -  About docs.rs
  -  Badges
  -  Builds
  -  Metadata
  -  Shorthand URLs
  -  Download
  -  Rustdoc JSON
  -  Build queue
  -  Privacy policy
                        

                    
                

                

- 
                        Rust
                        

                            
  - Rust website
                            
  - The Book

                            
  - Standard Library API Reference

                            
  - Rust by Example

                            
  - The Cargo Guide

                            
  - Clippy Documentation
                        

                    
                

                
                
                    
                        
                    

                    
                    
                    
                
            
        
    

    
    
        
            
                

                
                
# 
                    traceview 2.1.0
                    
                

                
                Tracing and viewing your files and resource landscape

                
                    

                        
                        
- 
                                
                                 Crate
                            
                        

                        
                        
- 
                            
                                
                                 Source
                            
                        

                        
                        
- 
                            
                                
                                 Builds
                            
                        

                        
                        
- 
                            
                                
                                Feature flags
                            
                        
                    

                
            
    

        
            
                
                    

- Size
                            
- 
                                Source code size: 433.67 kB
                                    This is the summed size of all the files inside the crates.io package for this release.
                                    
                                
                            
- Links
                        
- 
                                
                                    
                                    
                                        
                                            javaLux/traceview
                                        
                                        

                                         7
                                         1
                                         0

                                    
                            
                        
- 
                            
                                 crates.io
                            
                        

                        
- Dependencies
                        
- 
                            
                                

                                    
                                    
  - 
                anyhow ^1.0.102
                
                    *normal*
                    
                
            
        
  - 
                async-trait ^0.1.89
                
                    *normal*
                    
                
            
        
  - 
                chrono ^0.4.44
                
                    *normal*
                    
                
            
        
  - 
                clap ^4.5.60
                
                    *normal*
                    
                
            
        
  - 
                confy ^2.0.0
                
                    *normal*
                    
                
            
        
  - 
                console ^0.16.2
                
                    *normal*
                    
                
            
        
  - 
                copypasta ^0.10.2
                
                    *normal*
                    
                
            
        
  - 
                crossterm ^0.29.0
                
                    *normal*
                    
                
            
        
  - 
                dirs ^6.0.0
                
                    *normal*
                    
                
            
        
  - 
                file-format ^0.28.0
                
                    *normal*
                    
                
            
        
  - 
                futures ^0.3.32
                
                    *normal*
                    
                
            
        
  - 
                human_bytes ^0.4.3
                
                    *normal*
                    
                
            
        
  - 
                log ^0.4.29
                
                    *normal*
                    
                
            
        
  - 
                os_info ^3.14.0
                
                    *normal*
                    
                
            
        
  - 
                path-absolutize ^3.1.1
                
                    *normal*
                    
                
            
        
  - 
                ratatui ^0.30.0
                
                    *normal*
                    
                
            
        
  - 
                serde ^1.0.228
                
                    *normal*
                    
                
            
        
  - 
                serde_json ^1.0.149
                
                    *normal*
                    
                
            
        
  - 
                simplelog ^0.12.2
                
                    *normal*
                    
                
            
        
  - 
                sysinfo ^0.38.2
                
                    *normal*
                    
                
            
        
  - 
                tokio ^1.49.0
                
                    *normal*
                    
                
            
        
  - 
                tokio-util ^0.7.18
                
                    *normal*
                    
                
            
        
  - 
                walkdir ^2.5.0
                
                    *normal*
                    
                
            
        
                                

                            
                        

                        
- Versions
                        
- 
                            
                                

                                    
                                    
        
         
        
  - 
            **2.1.0** (2026-02-25)
        
        
         
        
  - 
            **2.0.0** (2026-02-24)
        
        
         
        
  - 
            **1.0.3** (2025-04-11)
        
        
         
        
  - 
            **1.0.2** (2025-03-23)
        
        
         
        
  - 
            **1.0.1** (2025-02-21)
        
        
         
        
  - 
            **1.0.0** (2025-02-20)
        
                                

                            
                        

                        
                        
- Owners
                        
- 
                                    
                                
                    

                
            

            
                
                        traceview-2.1.0 is not a library.
                    

                

# TraceView

A fast and feature-rich TUI (Text-based User Interface) application written in Rust. It enables users to navigate the local filesystem, monitor system resources, search for files and directories, retrieve metadata, and export search results to JSON.

---

---

## Features

- **Filesystem Explorer**: Quickly browse and navigate local directories.

- **System Overview**: Monitor CPU, Swap, memory, and disk usage in real-time.

- **File & Directory Search**: Search files and folders by name with instant results.

- **Metadata Retrieval**: View file and directory metadata (size, permissions, last modified, and more).

- **Export Functionality**: Save search results as JSON files.

- **Configurable Settings**: Customize behavior and appearance via the Built-in Settings-Page

- **Themes**: Choose from **Dark**, **Light**, **Dracula**, and **Indigo** themes.

- **Help Page**: Built-in Help-Page with keybindings and descriptions.

- **Status Bar**: Displays current context, active theme, last keystroke, and error messages in real-time.

---

## Getting Started

### Installation

There are three ways to get started with TraceView:

#### Option 1: Build from Source

- **Clone the repository**:

```
git clone https://github.com/javaLux/traceview
cd traceview

```

- **Build the project**:

```
cargo build --release

```

- **Run the application**:

```
cd target/release
./traceview

```

#### Option 2: Download Pre-Compiled Binaries *(Recommended for quick setup)*

If you don't want to build the project yourself or don't want to install Rust, you can download pre-compiled binaries from the Releases section on GitHub:

##### **How to Run the Downloaded Binary:**

- Download the appropriate file for your operating system.

- Extract the archive if necessary.

- Make the binary executable (Linux/macOS):

```
chmod +x traceview

```

- Run the application:

```
./traceview

```

#### Option 3: Install via crates.io *(Quick and direct installation)*

TraceView is available on crates.io, allowing users to install and run it directly without cloning the repository.

- 

**Install using Cargo:**

```
cargo install traceview

```

- 

**Run the application:**

```
traceview

```

**Advantages of this method:**

- The installed binary is placed in Cargo's bin directory (usually `~/.cargo/bin`), which is typically included in the system's `$PATH` environment variable.

- You can run `traceview` directly from any terminal without specifying the path.

- Easily update to the latest version with:

```
cargo install traceview --force

```

---

## Configuration

TraceView is configurable via the built-in Settings-Page. To open it, press `F3`. The App-Settings are stored in a file named `config.toml`.
This file is located in the App Config-Directory.

### Configuration Options

- **Default-Theme**: Describes the default theme on startup. Default is the `Dark-Theme`.

- **Start-Directory**: Describes the directory in which the file explorer should start. Default is the `User-Home-Directory`.

- **Export-Directory**: Describes the destination directory where the JSON export results will be saved. Default is the `Application data directory`.

- **Follow symbolic links**: Influences the file explorer, file/directory name search, and the recording of metadata for directories. Default is `false`.

  - **What are symbolic links?** Symbolic links (or symlinks) are pointers to other files or directories. When this option is set to `true`, TraceView follows these links during navigation and searches, potentially traversing linked paths.

- **Frames per second**: Frames per second to be rendered on screen. Default is `45`

- **Update rate (System-Resources)**: Update rate of the system resources per second. Default is `1`

### ⚠️ Invalid Configuration Handling

If any settings in `config.toml` are incorrect or cannot be interpreted:

- The application will log a warning in the **log file** located in the app's `data` directory.

- Default settings will be applied automatically to ensure stability.

- Users should consult the log file for details on which settings failed to load and why.

### Command-Line Interface (CLI) Options

Option
Description

`-h`, `--help`
Print help

`-V`, `--version`
Print version

`-c`, `--config <FILE>`
Set a custom config file [default: ~/.config/traceview/config.toml]

---

## Themes

Supported themes:

- **Dark** – High contrast for low-light environments (default)

- **Light** – Bright theme for well-lit spaces

- **Dracula** – Vibrant dark theme with colorful highlights

- **Indigo** – Calming theme with indigo tones

To change the theme you can press `Ctrl + T` within the app. Furthermore, the default theme can be set at startup via the Settings-Page.

---

## App Contexts

TraceView operates in three primary contexts, each with context-specific controls and keybindings:

- **Explorer Context** – Navigate and browse the filesystem.

- **Search Context** – Input and execute file/directory searches.

- **Result Context** – View and export search results.

- Please use the provided help page by pressing `F1` to view all keyboard shortcuts and their context.

## Status Bar Features

The status bar, located at the bottom of the interface, provides:

- **Current Context**: Shows whether you are in Explorer, Search, or Result context.

- **Active Theme**: Displays the currently applied theme.

- **Last Keystroke**: Shows the last pressed key.

- **Error Messages**: Displays any application errors or warnings.

---

## Searching by File or Directory Name

TraceView provides a powerful search feature that allows users to search specifically for **file and directory names**. The search functionality focuses only on names, making it possible to:

- Search for specific filenames.

- Search by partial matches (e.g., typing "log" to find "app_log.txt").

- Search by file extensions (e.g., ".txt" to find all text files).

### Search Options

TraceView offers two search modes:

- **Flat Search:** Searches only within the currently selected directory (non-recursive). Ideal for quick local searches.

- **Deep Search:** Recursively searches through all subdirectories within the selected path. Useful for locating files or directories in nested structures.

### Search Input History

- The input field for typing search queries maintains a **history of previous searches** during the current session.

- Navigate through past queries using the **Up (↑)** and **Down (↓)** arrow keys to quickly reuse or modify previous searches.

- This feature enhances efficiency, especially when refining searches or repeating common queries.

**Usage Notes:**

- Initiate a search by pressing `Ctrl + F` in the Explorer Context.

- Enter your search query and choose between Flat or Deep mode.

- Search results are displayed instantly based on the selected mode.

⚠️ **Performance Considerations:**

- **Deep Search** in large directory structures may take longer, especially if the `follow_sym_links` configuration option is enabled.

- **Flat Search** provides faster results for localized searches.

---

## Capturing File and Directory Metadata

TraceView allows users to capture metadata (press `Ctrl + A` in Explorer Context), for both files and directories with the following considerations:

### File Metadata

- File metadata is available immediately after invoking the metadata view.

- Displayed information includes file size, permissions, last modified date, and ownership.

### Directory Metadata

- Directory metadata collection may take longer, especially for large directories.

- This is because TraceView recursively scans all contained files and subdirectories to determine:

  - Total size

  - Number of contained files

  - Number of contained subdirectories

- **Note:** The depth and complexity of the directory structure will affect the processing time.

- If `follow_sym_links` is enabled in the configuration, symbolic links within directories are also traversed, potentially increasing processing time.

---

## If Things Take a Long Time

Some operations in TraceView, such as searching for files/directories or exporting search results, may take longer to complete depending on the size and complexity of the filesystem.

**Cancel Ongoing Processes:**

- You can quit the app at any time by pressing `Ctrl + Q`.

- This is especially useful during deep searches or large directory exports that require extensive processing time.

---

## 🚫 Limitations

While TraceView offers a variety of features for browsing, searching, and viewing metadata, it is important to note that **it is not a full-fledged file explorer**. As such:

- **File or directory manipulation (copying, moving, deleting, or renaming) is not supported.**

- TraceView is currently designed to provide safe, read-only access to filesystem information without risking unintended file modifications.

---

## License

This project is licensed under the MIT License.

---

## Built With ❤️ in Rust and these awesome crates

Thanks to the developers of these crates, without whom `TraceView` would not exist

- **Ratatui** – Rust-based library for building rich terminal user interfaces.

- **Walkdir** – Efficient directory traversal for Rust projects.

- **Crossterm** – Cross-platform Terminal Manipulation Library

---

## Tested Platforms

TraceView has been tested on the following operating systems and environments:

Operating System
Version
Terminal/Shell
CPU-Arch

Windows
10/11
Windows Terminal, PowerShell
x86_64

Ubuntu Linux
25.04
GNOME-Terminal / bash, zsh
x86_64

Linux Mint
22.3
GNOME-Terminal / bash, zsh
x86_64

EndeavourOS
Ganymede Neo
KDE-Terminal / bash, zsh
x86_64

macOS
Monterey (12.x)
iTerm2 / zsh
x86_64

### Notice

When testing under MacOs, I noticed that the standard terminal does not fully support true RGB (24-bit) colors. For this reason, the test was also carried out with the third-party terminal `iTerm2'`. There all colors are displayed as expected. So if you notice an incorrect display of colors under MacOs, please use the iTerm2 terminal.

---

## Troubleshooting

### Pasting content from the clipboard does not work

If `Ctrl+V` does not work to paste content from the clipboard, please try `Ctrl+Shift+V` as an alternative.

**Note:**
Pasting content from the clipboard via `Ctrl+V` may not work in all terminal environments. Depending on your terminal emulator, you might need to use `Ctrl+Shift+V` instead (e.g., GNOME, KDE, or other Linux-based terminal emulators).

### Windows Terminal Freeze Issue

If you experience the app freezing when clicking inside the terminal window with the **left mouse button** on Windows, this is due to the terminal's default behavior of entering "selection mode." In this mode, terminal input is paused while text is being selected. To avoid this issue:

- Use keyboard navigation instead of mouse clicks.

- Right-click outside the terminal to regain control.

- Change terminal settings to disable selection mode if supported.

### Error Messages and Logs

If an error appears in the status bar:

- A brief error description is displayed in the status bar.

- For detailed information, consult the **log file** located in the app's `data` directory.

  - The log file includes timestamps, error descriptions, and debugging information.

  - Check the logs if you encounter unexpected behavior or crashes.

---

## **Collaboration, Feedback & Bug Reports**

I welcome feedback, suggestions, and bug reports! Your input helps make TraceView better.

### How to Contribute

- **Fork** this repository.

- **Create a new branch** for your changes.

- Make your changes, ensuring they are clean and well-documented.

- **Commit** your changes with a meaningful message.

- **Push** your branch to your fork.

- Open a pull request from your branch to the main repository.

### Found a Bug?

- Report issues or suggestions via GitHub Issues.

## Thank you for using TraceView! 🙌