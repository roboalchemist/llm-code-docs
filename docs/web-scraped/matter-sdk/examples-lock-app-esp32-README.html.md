# Source: https://project-chip.github.io/connectedhomeip-doc/examples/lock-app/esp32/README.html

# Matter ESP32 Lock Example

## Contents

# Matter ESP32 Lock Example

This example demonstrates the mapping of OnOff cluster to lock/unlock logic.

Please [setup ESP-IDF and CHIP Environment](../../../platforms/esp32/setup_idf_chip.html) and refer [building and commissioning](../../../platforms/esp32/build_app_and_commission.html) guides to get started.

* * *

* Cluster control

* Example Demo

* [RPC console and Device Tracing](../../../platforms/esp32/rpc_console.html)

* * *

## Cluster control

### onoff

To use the Client to send Matter commands, run the built executable and pass it the target cluster name, the target command name as well as an endpoint id.

    ./out/debug/chip-tool onoff on <NODE ID> 1
    

The client will send a single command packet and then exit.

## Example Demo

This demo app illustrates controlling OnOff cluster (Server) attributes of an endpoint and lock/unlock status of door using LED’s. For `ESP32-DevKitC`, a GPIO (configurable through `LOCK_STATE_LED` in `main/include/AppConfig.h`) is updated through the on/off/toggle commands from the `python-controller`. If you wish to see the actual effect of the commands on `ESP32-DevKitC`, you will have to connect an external LED to GPIO.
