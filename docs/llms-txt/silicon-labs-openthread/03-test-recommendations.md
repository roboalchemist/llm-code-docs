# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-overview/03-test-recommendations.md

# Test Recommendations

This section summarizes the functionality that should be tested on the hardware product, depending on the phase. These recommendations are for SoC (System-on-Chip) products. Silicon Labs also offers EFR-based modules that are pre-certified or fully certified. In such cases, the customer’s end product will require limited RF testing depending on the region and its compliance to the regulatory standards. See _AN1048: Regulatory RF Module Certifications_ for more information on module certifications and the required testing.

## Prototype Testing

Prototype testing is necessary for all product designs. In this phase of testing, the design is verified across the full environmental product requirements, including temperature range and voltage supply range, as well as humidity range in some cases. This level of environmental testing may occur over several months, depending on the qualification requirements of the product. Certification and compliance testing may also be necessary in this phase of testing. External test houses are likely to be involved to support this testing. This phase fully verifies the design of the hardware and product that is being developed, and helps identify any design issues that need to be corrected before proceeding to the characterization testing phase.

## Characterization Testing

Characterization testing is recommended for early production stages. In this phase of testing, the RF functionality (transmit and receive) should be characterized on all applicable channels or a subset of these channels, as well as at various transmit output power levels or receiver input power levels. This phase fully characterizes the hardware that is being developed, determines the tests to be executed in manufacturing test, determines the test limits of these tests, and flushes out any manufacturing or process issues that might be present.

## Low-Volume Manufacturing Testing

Low-volume manufacturing testing is usually a subset of the characterization testing. A subset of the applicable channels or transmit output power levels can be tested to reduce the test time without compromising test coverage. For example, one channel/power level combination (likely mid-band at max power) can be measured for transmit and receive functionality.

The results from the characterization phase of testing help determine not only what should be tested in the manufacturing phase but also the test limits to be applied to certain tests. For example, if a particular test does not fail at all during the characterization phase, it can be omitted from the manufacturing phase altogether. Also, if it is determined that a particular test will fail all channels if it fails at all, testing can be reduced from all channels to a single channel, most likely mid-band.

## High-Volume Manufacturing Testing

High-volume manufacturing testing is much simpler than characterization testing or low-volume manufacturing testing. The hardware design and manufacturing process have already been proven, so the product now just requires a quick “go/no go” transmit and receive functional test to verify operation.