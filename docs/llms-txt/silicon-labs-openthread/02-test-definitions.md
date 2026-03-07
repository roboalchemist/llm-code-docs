# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-guidelines-efr32/02-test-definitions.md

# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-overview/02-test-definitions.md

# Test Definitions

Automated test is defined as a test method where test equipment and DUT are controlled by a PC. A test program on the PC controls the test equipment and DUT. The DUT is loaded with embedded software that allows the radio to be configured for particular tests.

The tests can be divided into different types of tests— RF testing, DC testing, and peripheral testing.

- RF testing is any test specific to the operation and functionality of the radio (for example, transmitting and receiving Zigbee packets).
- DC testing is any test related to the voltage and current characteristics of the device or board (for example, active and sleep currents).
- Peripheral testing is any test not specific to RF or DC, like a sensor or an external crystal.

For more details on the specific recommended tests, refer to [Manufacturing Test Guidelines for the EFR32](https://docs.silabs.com/zigbee/latest/mfg-test-guidelines-efr32/).
