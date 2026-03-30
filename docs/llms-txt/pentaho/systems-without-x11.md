# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/prepare-your-linux-environment-for-a-manual-installation/advanced-linux-considerations/systems-without-x11.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/advanced-linux-considerations/systems-without-x11.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install/advanced-linux-considerations/systems-without-x11.md

# Systems without X11

To generate charts, the Pentaho Reporting engine requires functions found in X11. This topic is for Linux users who have a headless node and a video card, but do not have an X server installed.

If you are unwilling or unable to install an X server, you can install the Xvfb package instead. Xvfb provides the X11 framebuffer emulation, which performs all graphical operations in the memory rather than sending them to the screen.

Use your operating system's package manager to properly install Xvfb.
