## Quick-start your own project

NOTE: The following instructions are terse, and Linux-based only. For detailed steps, instructions for other platforms, and just in general, we recommend you see the https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf[Getting started with Raspberry Pi Pico] and https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf[Raspberry Pi Pico C/{cpp} SDK] books.

Install CMake (at least version 3.13), and GCC cross compiler

```console
$ sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib
```

Set up your project to point to use the Raspberry Pi Pico SDK by cloning the SDK locally:

```console
$ git clone https://github.com/raspberrypi/pico-sdk.git
```

Copy `external/pico*sdk*import.cmake` from the SDK into your project directory

Set `PICO*SDK*PATH` to the SDK location in your environment, or pass it (`-DPICO*SDK*PATH=`) to `cmake` later.

Setup a `CMakeLists.txt` like:

```
cmake*minimum*required(VERSION 3.13)

# initialize the SDK based on PICO*SDK*PATH
# note: this must happen before project()
include(pico*sdk*import.cmake)

project(my*project)

# initialize the Raspberry Pi Pico SDK
pico*sdk*init()

# rest of your project
```

Go ahead and write your code, see https://github.com/raspberrypi/pico-examples[pico-examples] or the https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf[Raspberry Pi Pico C/{cpp} SDK] book for more information on how to go about that.

About the simplest you can do is a single source file (e.g. `hello*world.c`)

```c
#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    setup*default*uart();
    printf("Hello, world!\n");
    return 0;
}
```

and add the following to your CMakeLists.txt:

```
add*executable(hello*world
    hello*world.c
)

# Add pico*stdlib library which aggregates commonly used features
target*link*libraries(hello*world pico*stdlib)

# create map/bin/hex/uf2 file in addition to ELF.
pico*add*extra*outputs(hello*world)
```

NOTE: This example uses the default UART for stdout; if you want to use the default USB see the hello-usb example.

Setup a CMake build directory. For example, if not using an IDE:

```console
$ mkdir build
$ cd build
$ cmake ..
```

When building for a board other than the Raspberry Pi Pico, you should pass `-DPICO*BOARD=board*name` to the cmake command above, e.g. cmake `-DPICO*BOARD=pico*w ..` to configure the SDK and build options accordingly for that particular board.

Doing so sets up various compiler defines (e.g. default pin numbers for UART and other hardware) and in certain cases also enables the use of additional libraries (e.g. wireless support when building for `PICO*BOARD=pico*w`) which cannot be built without a board which provides the requisite functionality.

For a list of boards defined in the SDK itself, look in https://github.com/raspberrypi/pico-sdk/blob/master/src/boards/include/boards[this directory] which has a header for each named board.

Make your target from the build directory you created.

```console
$ make hello*world
```

You now have `hello*world.elf` to load via a debugger, or `hello_world.uf2` that can be installed and run on your Raspberry Pi Pico via drag and drop.