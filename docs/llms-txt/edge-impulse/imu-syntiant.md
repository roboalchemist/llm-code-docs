# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/imu-syntiant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IMU Syntiant

The **IMU Syntiant** block rescales raw data to 8 bits values to match the NDP101/120 chip input requirements.

## Parameters

**Scaling**

* Scale 16 bits to 8 bits: Scale data to 8-bits values in the \[-1, 1] range, raw data is divided by 2G (2 \* 9.80665). Using Edge Impulse official firmwares, this parameter should be enabled as raw data is not rescaled. If this parameter is disabled the data samples will not be rescaled, you should disable this parameter if your raw data samples are already normalized to the \[-1, 1] range.

## How does the IMU Syntiant block work?

The **IMU Syntiant** block retrieves raw samples and applies the *Scale 16 bits to 8 bits* parameter.


Built with [Mintlify](https://mintlify.com).