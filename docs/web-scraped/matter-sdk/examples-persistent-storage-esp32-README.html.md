# Source: https://project-chip.github.io/connectedhomeip-doc/examples/persistent-storage/esp32/README.html

# CHIP ESP32 Persistent Storage Example

## Contents

# CHIP ESP32 Persistent Storage Example

An example testing and demonstrating the key value storage API.

Please [setup ESP-IDF and CHIP Environment](../../../platforms/esp32/setup_idf_chip.html) and refer [building and commissioning](../../../platforms/esp32/build_app_and_commission.html) guides to get started.

* * *

* Introduction

* * *

## Introduction

This example serves to both test the key value storage implementation and API as it is brought-up on different platforms, as well as provide an example for how to use the API.

In the future this example can be moved into a unit test when available on all platforms.

The ESP32 platform KVS is not yet fully implemented. In particular offset and partial reads are not yet supported.
