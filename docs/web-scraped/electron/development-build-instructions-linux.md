# Source: https://www.electronjs.org/docs/latest/development/build-instructions-linux

On this page

# Build Instructions (Linux)

Follow the guidelines below for building **Electron itself** on Linux, for the purposes of creating custom Electron binaries. For bundling and distributing your app code with the prebuilt Electron binaries, see the [application distribution](/docs/latest/tutorial/application-distribution) guide.

## Prerequisites[â€‹](#prerequisites "Direct link to Prerequisites") 

Due to Electron\'s dependency on Chromium, prerequisites and dependencies for Electron change over time. [Chromium\'s documentation on building on Linux](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/linux/build_instructions.md) has up to date information for building Chromium on Linux. This documentation can generally be followed for building Electron on Linux as well.

Additionally, Electron\'s [Linux dependency installer](https://github.com/electron/build-images/blob/main/tools/install-deps.sh) can be referenced to get the current dependencies that Electron requires in addition to what Chromium installs via [build/install-deps.sh](https://chromium.googlesource.com/chromium/src/+/HEAD/build/install-build-deps.sh).

### Cross compilation[â€‹](#cross-compilation "Direct link to Cross compilation") 

If you want to build for an `arm` target, you can use Electron\'s [Linux dependency installer](https://github.com/electron/build-images/blob/main/tools/install-deps.sh) to install the additional dependencies by passing the `--arm argument`:

``` 
$ sudo install-deps.sh --arm
```

And to cross-compile for `arm` or targets, you should pass the `target_cpu` parameter to `gn gen`:

``` 
$ gn gen out/Testing --args='import(...) target_cpu="arm"'
```

## Building[â€‹](#building "Direct link to Building") 

See [Build Instructions: GN](/docs/latest/development/build-instructions-gn)

## Troubleshooting[â€‹](#troubleshooting "Direct link to Troubleshooting") 

### Error While Loading Shared Libraries: libtinfo.so.5[â€‹](#error-while-loading-shared-libraries-libtinfoso5 "Direct link to Error While Loading Shared Libraries: libtinfo.so.5") 

Prebuilt `clang` will try to link to `libtinfo.so.5`. Depending on the host architecture, symlink to appropriate `libncurses`:

``` 
$ sudo ln -s /usr/lib/libncurses.so.5 /usr/lib/libtinfo.so.5
```

## Advanced topics[â€‹](#advanced-topics "Direct link to Advanced topics") 

The default building configuration is targeted for major desktop Linux distributions. To build for a specific distribution or device, the following information may help you.

### Using system `clang` instead of downloaded `clang` binaries[â€‹](#using-system-clang-instead-of-downloaded-clang-binaries "Direct link to using-system-clang-instead-of-downloaded-clang-binaries") 

By default Electron is built with prebuilt [`clang`](https://clang.llvm.org/get_started.html) binaries provided by the Chromium project. If for some reason you want to build with the `clang` installed in your system, you can specify the `clang_base_path` argument in the GN args.

For example if you installed `clang` under `/usr/local/bin/clang`:

``` 
$ gn gen out/Testing --args='import("//electron/build/args/testing.gn") clang_base_path = "/usr/local/bin"'
```

### Using compilers other than `clang`[â€‹](#using-compilers-other-than-clang "Direct link to using-compilers-other-than-clang") 

Building Electron with compilers other than `clang` is not supported.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/development/build-instructions-linux.md)