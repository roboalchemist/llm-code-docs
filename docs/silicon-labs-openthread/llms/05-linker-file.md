# Source: https://docs.silabs.com/openthread/3.0.0/bootloader-transitioning-guide-gsdk-v40-and-higher/05-linker-file.md

# Linker File

The linker files for GCC and IAR are now generated during the project generation step. The linker files for the bootloader are generated from template files using the Jinja template engine. The template files are included with theGecko SDK Suite (GSDK), which is installed through Simplicity Studio. The jinja template files are located at **<path-to-simplicity-studio-installation>|v5|developer|sdks|gecko_sdk_suite|<gecko_sdk_version>|platform|common|toolchain|**.This path contains folders for both **gcc** and **iar**.