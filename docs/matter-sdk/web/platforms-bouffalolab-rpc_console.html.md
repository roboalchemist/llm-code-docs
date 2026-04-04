# Source: https://project-chip.github.io/connectedhomeip-doc/platforms/bouffalolab/rpc_console.html

# Bouffalo Lab with RPC console

## Contents

# `Bouffalo Lab` with RPC console

## Build image

* `BL602DK`

        ./scripts/build/build_examples.py --target bouffalolab-bl602dk-light-wifi-littlefs-rpc build
        

* `BL704LDK`

        ./scripts/build/build_examples.py --target bouffalolab-bl704ldk-light-thread-littlefs-rpc build
        

* `BL706DK`

        ./scripts/build/build_examples.py --target bouffalolab-bl706dk-light-thread-littlefs-rpc build
        

## Run RPC Console

* Build chip-console following this [guide](../../examples/common/pigweed/rpc_console/README.html)

* Start the console

        chip-console -d /dev/ttyACM0 -b 115200
        

* Get or Set the light state

`rpcs.chip.rpc.Lighting.Get()`

`rpcs.chip.rpc.Lighting.Set(on=True, level=128)`
