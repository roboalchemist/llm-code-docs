# Source: https://docs.helix-editor.com/install.html

# Installing Helix

The typical way to install Helix is viayour operating system's package manager.
Note that:
- To get the latest nightly version of Helix, you need tobuild from source.
- To take full advantage of Helix, install the language servers for your
preferred programming languages. See thewikifor instructions.

## Pre-built binaries

Download pre-built binaries from theGitHub Releases page.
The tarball contents include anhxbinary and aruntimedirectory.
To set up Helix:
- Add thehxbinary to your system's$PATHto allow it to be used from the command line.
- Copy theruntimedirectory to a location thathxsearches for runtime files. A typical location on Linux/macOS is~/.config/helix/runtime.
To see the runtime directories thathxsearches, runhx --health. If necessary, you can override the default runtime location by setting theHELIX_RUNTIMEenvironment variable.