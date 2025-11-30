# Source: https://www.electronjs.org/docs/latest/development/build-instructions-windows

On this page

# Build Instructions (Windows)

Follow the guidelines below for building **Electron itself** on Windows, for the purposes of creating custom Electron binaries. For bundling and distributing your app code with the prebuilt Electron binaries, see the [application distribution](/docs/latest/tutorial/application-distribution) guide.

## Prerequisites[â€‹](#prerequisites "Direct link to Prerequisites") 

- Windows 10 / Server 2012 R2 or higher
- Visual Studio 2019 (\>=16.0.0) to build, but Visual Studio 2022 (\>=17.0.0) is preferred - [download VS 2022 Community Edition for free](https://www.visualstudio.com/vs/)
  - See [the Chromium build documentation](https://chromium.googlesource.com/chromium/src/+/main/docs/windows_build_instructions.md#visual-studio) for more details on which Visual Studio components are required.
  - If your Visual Studio is installed in a directory other than the default, you\'ll need to set a few environment variables to point the toolchains to your installation path.
    - `vs2022_install = DRIVE:\path\to\Microsoft Visual Studio\2022\Community`, replacing `2022` and `Community` with your installed versions and replacing `DRIVE:` with the drive that Visual Studio is on. Often, this will be `C:`.
    - `WINDOWSSDKDIR = DRIVE:\path\to\Windows Kits\10`, replacing `DRIVE:` with the drive that Windows Kits is on. Often, this will be `C:`.
- [Node.js](https://nodejs.org/download/) \>= 22.12.0
- [Git](https://git-scm.com)
- Debugging Tools for Windows of Windows SDK 10.0.15063.468 if you plan on creating a full distribution since `symstore.exe` is used for creating a symbol store from `.pdb` files.
  - Different versions of the SDK can be installed side by side. To install the SDK, open Visual Studio Installer, select `Modify` â†' `Individual Components`, scroll down and select the appropriate Windows SDK to install. Another option would be to look at the [Windows SDK and emulator archive](https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/) and download the standalone version of the SDK respectively.
  - The SDK Debugging Tools must also be installed. If the Windows 10 SDK was installed via the Visual Studio installer, then they can be installed by going to: `Control Panel` â†' `Programs` â†' `Programs and Features` â†' Select the \"Windows Software Development Kit\" â†' `Change` â†' `Change` â†' Check \"Debugging Tools For Windows\" â†' `Change`. Or, you can download the standalone SDK installer and use it to install the Debugging Tools.

If you don\'t currently have a Windows installation, [developer.microsoft.com](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/) has timebombed versions of Windows that you can use to build Electron.

Building Electron is done entirely with command-line scripts and cannot be done with Visual Studio. You can develop Electron with any editor but support for building with Visual Studio will come in the future.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Even though Visual Studio is not used for building, it\'s still **required** because we need the build toolchains it provides.

## Exclude source tree from Windows Security[â€‹](#exclude-source-tree-from-windows-security "Direct link to Exclude source tree from Windows Security") 

Windows Security doesn\'t like one of the files in the Chromium source code (see [https://crbug.com/441184](https://crbug.com/441184)), so it will constantly delete it, causing `gclient sync` issues. You can exclude the source tree from being monitored by Windows Security by [following these instructions](https://support.microsoft.com/en-us/windows/add-an-exclusion-to-windows-security-811816c0-4dfd-af4a-47e4-c301afe13b26).

## Building[â€‹](#building "Direct link to Building") 

See [Build Instructions: GN](/docs/latest/development/build-instructions-gn)

## 32bit Build[â€‹](#32bit-build "Direct link to 32bit Build") 

To build for the 32bit target, you need to pass `target_cpu = "x86"` as a GN arg. You can build the 32bit target alongside the 64bit target by using a different output directory for GN, e.g. `out/Release-x86`, with different arguments.

``` 
$ gn gen out/Release-x86 --args="import(\"//electron/build/args/release.gn\") target_cpu=\"x86\""
```

The other building steps are exactly the same.

## Visual Studio project[â€‹](#visual-studio-project "Direct link to Visual Studio project") 

To generate a Visual Studio project, you can pass the `--ide=vs2017` parameter to `gn gen`:

``` 
$ gn gen out/Testing --ide=vs2017
```

## Troubleshooting[â€‹](#troubleshooting "Direct link to Troubleshooting") 

### Command xxxx not found[â€‹](#command-xxxx-not-found "Direct link to Command xxxx not found") 

If you encountered an error like `Command xxxx not found`, you may try to use the `VS2015 Command Prompt` console to execute the build scripts.

### Fatal internal compiler error: C1001[â€‹](#fatal-internal-compiler-error-c1001 "Direct link to Fatal internal compiler error: C1001") 

Make sure you have the latest Visual Studio update installed.

### LNK1181: cannot open input file \'kernel32.lib\'[â€‹](#lnk1181-cannot-open-input-file-kernel32lib "Direct link to LNK1181: cannot open input file 'kernel32.lib'") 

Try reinstalling 32bit Node.js.

### Error: ENOENT, stat \'C:\\Users\\USERNAME\\AppData\\Roaming\\npm\'[â€‹](#error-enoent-stat-cusersusernameappdataroamingnpm "Direct link to Error: ENOENT, stat 'C:\Users\USERNAME\AppData\Roaming\npm'") 

Creating that directory [should fix the problem](https://stackoverflow.com/a/25095327/102704):

``` 
$ mkdir ~\AppData\Roaming\npm
```

### node-gyp is not recognized as an internal or external command[â€‹](#node-gyp-is-not-recognized-as-an-internal-or-external-command "Direct link to node-gyp is not recognized as an internal or external command") 

You may get this error if you are using Git Bash for building, you should use PowerShell or VS2015 Command Prompt instead.

### cannot create directory at \'\...\': Filename too long[â€‹](#cannot-create-directory-at--filename-too-long "Direct link to cannot create directory at '...': Filename too long") 

node.js has some [extremely long pathnames](https://github.com/electron/node/tree/electron/deps/npm/node_modules/libnpx/node_modules/yargs/node_modules/read-pkg-up/node_modules/read-pkg/node_modules/load-json-file/node_modules/parse-json/node_modules/error-ex/node_modules/is-arrayish), and by default git on windows doesn\'t handle long pathnames correctly (even though windows supports them). This should fix it:

``` 
$ git config --system core.longpaths true
```

### error: use of undeclared identifier \'DefaultDelegateCheckMode\'[â€‹](#error-use-of-undeclared-identifier-defaultdelegatecheckmode "Direct link to error: use of undeclared identifier 'DefaultDelegateCheckMode'") 

This can happen during build, when Debugging Tools for Windows has been installed with Windows Driver Kit. Uninstall Windows Driver Kit and install Debugging Tools with steps described above.

### Build Scripts Hang Until Keypress[â€‹](#build-scripts-hang-until-keypress "Direct link to Build Scripts Hang Until Keypress") 

This bug is a \"feature\" of Windows\' command prompt. It happens when clicking inside the prompt window with `QuickEdit` enabled and is intended to allow selecting and copying output text easily. Since each accidental click will pause the build process, you might want to disable this feature in the command prompt properties.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/build-instructions-windows.md)