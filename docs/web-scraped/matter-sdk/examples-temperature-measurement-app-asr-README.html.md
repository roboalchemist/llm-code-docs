# Source: https://project-chip.github.io/connectedhomeip-doc/examples/temperature-measurement-app/asr/README.html

# Matter ASR Temperature Measurement Example

## Contents

# Matter ASR Temperature Measurement Example

The ASR Temperature Measurement Example demonstrates getting simulated data from temperature sensor.

* * *

* Matter ASR Temperature Measurement Example

  * Building and Commissioning

  * Cluster Control

* * *

## Building and Commissioning

Please refer [Building and Commissioning](../../../platforms/asr/asr_getting_started_guide.html#building-the-example-application) guides to get started

    ./scripts/build/build_examples.py --target asr-$ASR_BOARD-temperature-measurement build
    

## Cluster Control

After successful commissioning, use `chip-tool` to control the board

For example,read temperature sensor measured value:

    ./chip-tool temperaturemeasurement read measured-value <NODE ID> 1
