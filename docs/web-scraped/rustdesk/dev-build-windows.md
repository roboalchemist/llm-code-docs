# Source: https://rustdesk.com/docs/en/dev/build/windows/

# Windows

Note

The command line commands here must be run in Git Bash not command prompt or you will get syntax errors.

## Dependencies

### C++ build environment

Download MSVC and install.
Select `Windows` as Developer machine OS and check `C++`, then download Visual Studio Community version and install. The installation may take a while.

### Rust develop environment

Download rustup-init.exe and run it as administrator to install `rust`.

### vcpkg

Go to the folder you want to clone vcpkg and use Git Bash to run the following commands, download `vcpkg`, install 64-bit version of `libvpx`, `libyuv` and `opus`.
If you don&rsquo;t have `Git` installed, get `Git` here.

```
git clone https://github.com/microsoft/vcpkg
vcpkg/bootstrap-vcpkg.bat
export VCPKG_ROOT=$PWD/vcpkg
vcpkg/vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
```

Add System environment variable `VCPKG_ROOT`=`<path>\vcpkg`. The `<path>` should be the location you choose above to clone `vcpkg`.

### Sciter

Desktop versions use Sciter for GUI, please download sciter.dll.

### LLVM

`rust-bindgen` depends on `clang`, download LLVM and install, add System environment variable `LIBCLANG_PATH`=`<llvm_install_dir>/bin`.

You can download version 15.0.2 of the LLVM binaries here: 64 bit / 32 bit.

## Build

### Default

```
git clone --recurse-submodules https://github.com/rustdesk/rustdesk
cd rustdesk
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll
mv sciter.dll target/debug
cargo run
```