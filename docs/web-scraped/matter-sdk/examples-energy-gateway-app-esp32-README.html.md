# Source: https://project-chip.github.io/connectedhomeip-doc/examples/energy-gateway-app/esp32/README.html

# Matter ESP32 Energy Gateway Example

## Contents

# Matter ESP32 Energy Gateway Example

This example demonstrates the Matter `Commodity Price` and `Electrical Grid Conditions` clusters on ESP platforms.

Please [setup ESP-IDF and CHIP Environment](../../../platforms/esp32/setup_idf_chip.html) and refer [building and commissioning](../../../platforms/esp32/build_app_and_commission.html) guides to get started.

## Enabling ESP-Insights

* Before building the app, enable the option: `ESP_INSIGHTS_ENABLED` through menuconfig.

* Create a file named `insights_auth_key.txt` in the main directory of the example.

* Follow the steps present [here](https://github.com/espressif/esp-insights/blob/main/examples/README.md#set-up-esp-insights-account) to set up an insights_account and the auth key created while setting it up will be used in the example.

* Download the auth key and copy Auth Key to the example

    cp /path/to/auth/key.txt path/to/connectedhomeip/examples/energy-gateway-app/esp32/main/insights_auth_key.txt

* * *

* Cluster Control

* [Matter OTA guide](../../../platforms/esp32/ota.html)

* * *

## Build time configuration

* Test Event Trigger support: By default the `CommodityPrice` and `ElectricalGridConditions` test event triggers are enabled in the build. To turn these off run `idf.py menuconfig` and search for the following config entries:

        ENABLE_COMMODITY_PRICE_TRIGGER
        ENABLE_ELECTRICAL_GRID_CONDITIONS_TRIGGER
        

## Cluster Control

* More examples using matter-repl are demonstrated in [Energy Gateway Linux](../linux/README.html)
