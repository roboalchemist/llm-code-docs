# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-guidelines-efr32/04-test-recommendations.md

# Test Recommendations

This section outlines the various tests that can be run on the hardware product, which of those tests Silicon Labs recommends running, and the channel selection for each test in each phase.

## SoC Test Recommendations

### Characterization Testing

Characterization testing is recommended for early production stages. In this phase of testing, the hardware is characterized on all 16 Zigbee channels or a subset of these channels, as well as at various transmit output power levels or receiver input power levels. This phase fully characterizes the hardware that is being developed, determines the tests to be executed in manufacturing test, determines the test limits of these tests, and flushes out any manufacturing or process issues that might be present.

Silicon Labs recommends that the tests outlined in the following table be conducted in the characterization phase of testing. This table, and the similar tables that follow in subsequent sections of this document, list the various tests that could be run on these devices, which of those tests Silicon Labs recommends running, and the channel selection for each test in each phase.

> **Note**: An X in these tables represents a test that is recommended for this phase of testing.

<table>
    <thead>
        <tr>
            <th rowspan="2"><strong>Test</strong></th>
            <th rowspan="2"><strong>Run?</strong></th>
            <th colspan="4"><strong>Channel</strong></th>
        </tr>
        <tr>
            <th><strong>Mid</strong></th>
            <th><strong>Low<br>Mid<br>High</strong></th>
            <th><strong>Subset</strong></th>
            <th><strong>All</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Serial Communication</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Supply Current</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit/Receive Verify</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td>X</td>
            <td></td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Frequency Offset</td>
            <td>X</td>
            <td></td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit EVM</td>
            <td>X</td>
            <td></td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Sweep</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td>X</td>
        </tr>
        <tr>
            <td>Spurious Emissions</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sweep</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td>X</td>
        </tr>
        <tr>
            <td>Receive Sensitivity</td>
            <td>X</td>
            <td></td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Waterfall</td>
            <td>X</td>
            <td></td>
            <td>X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>RSSI</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>External 32 kHz Crystal</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Peripherals</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

### Low-Volume Manufacturing Test

Low-volume manufacturing test is usually a subset of the characterization testing. A subset of the 16 Zigbee channels or transmit output power levels can be tested to reduce the test time without compromising test coverage. For example, one channel/power level combination (likely mid-band at max power) can be measured for transmit power and frequency. Also, receive waterfall can be omitted and receive sensitivity can be run in its place, where a certain packet-success rate is expected at mid-band for a given input power level.

The results from the characterization phase of testing help determine not only what should be tested in the manufacturing phase but also the test limits to be applied to certain tests. For example, if a particular test does not fail at all during the characterization phase, it can be omitted from the manufacturing phase altogether. Also, if it is determined that a particular test will fail all channels if it fails at all, testing can be reduced from all channels to a single channel, most likely mid-band.

#### Test Recommendations

The following table lists the tests Silicon Labs recommends be conducted in the low-volume manufacturing phase of testing.

<table>
    <thead>
        <tr>
            <th rowspan="2"><strong>Test</strong></th>
            <th rowspan="2"><strong>Run?</strong></th>
            <th colspan="4"><strong>Channel</strong></th>
        </tr>
        <tr>
            <th><strong>Mid</strong></th>
            <th><strong>Low<br>Mid<br>High</strong></th>
            <th><strong>Subset</strong></th>
            <th><strong>All</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Serial Communication</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Supply Current</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit/Receive Verify</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Frequency Offset</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit EVM</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Sweep</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td>X</td>
            <td></td>
        </tr>
        <tr>
            <td>Spurious Emissions</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sweep</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td>X</td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sensitivity</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Waterfall</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>RSSI</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>External 32kHz Crystal</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Peripherals</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

#### Test Times

The typical test time that can be achieved in the low-volume manufacturing test phase is three minutes per board. If the devices are preprogrammed, the overall test time can be reduced to less than three minutes. Program times vary depending on the flash memory size of the microprocessor. Note that programming may be included at both the front end (test application) and back end (final application) of the process.

#### Setting Test Limits

The results of the characterization phase of testing help determine how the limits are set for low-volume manufacturing test. Other factors in setting limits are customer application and manufacturing variation. For example, if an application specifies only a certain amount of dynamic range, perhaps limits will be relaxed to allow for this. Manufacturing variation can also be a factor in setting limits. For example, if the performance of the board is sensitive to particular components, it is important to account for any performance variation that may be seen with these particular components.

#### Full Characterization Sampling

It is important to continue to fully characterize samples from each production run to ensure that nothing in the process has shifted, causing a difference in the overall performance of a production run compared to a previous run. The size of this sample can be determined by the manufacturer, but Silicon Labs recommends this full characterization sampling for additional test coverage and process control at volume testing.

### High-Volume Manufacturing Test

High-volume manufacturing testing is much simpler than characterization testing or low volume manufacturing testing. The hardware design and manufacturing process have already been proven, so the product now just requires a quick “go/no go” functional test to verify operation.

#### Test Recommendations

Silicon Labs recommends that the tests in the following table be conducted in the high-volume phase of testing.

<table>
    <thead>
        <tr>
            <th rowspan="2"><strong>Test</strong></th>
            <th rowspan="2"><strong>Run?</strong></th>
            <th colspan="4"><strong>Channel</strong></th>
        </tr>
        <tr>
            <th><strong>Mid</strong></th>
            <th><strong>Low<br>Mid<br>High</strong></th>
            <th><strong>Subset</strong></th>
            <th><strong>All</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Serial Communication</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Supply Current</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit/Receive Verify</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Frequency Offset</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit EVM</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Sweep</td>
            <td></td>
            <td></td>
            <td></td>
            <td>X</td>
            <td></td>
        </tr>
        <tr>
            <td>Spurious Emissions</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sweep</td>
            <td></td>
            <td></td>
            <td></td>
            <td>X</td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sensitivity</td>
            <td>X</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Waterfall</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>RSSI</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>External 32 kHz Crystal</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Peripherals</td>
            <td>X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

#### Test Times

The typical test time that can be achieved in the high-volume manufacturing test phase is less than one minute per board. This assumes that devices are preprogrammed with the customer application and that the customer application uses the appropriate test tool for invoking test modes.

#### Setting Test Limits

Since the test environment in the high-volume manufacturing phase is different from the test environment in the low-volume phase, setting the limits is also done differently. The test limits for the basic transmit and receive tests are dependent on the fixed attenuation between the Golden Node and the DUT, as well as the variation in over-the-air results. Silicon Labs recommends that customers run a sample size of boards through testing to determine these test limits.

#### Full Characterization Sampling

Even in high-volume testing, it makes sense to fully characterize samples from each production run to ensure that the process has not shifted in any way. The size of this sample can be determined by the manufacturer, but this full characterization sampling is recommended for additional test coverage at high volumes.

## PCB and SiP Module Testing

Silicon Labs offers EFR-based modules that are pre-certified or fully certified. When customers use PCB or SiP modules, the end product will require only limited RF testing depending on the module variant, market region and its compliance to the regulatory standards. Therefore, modules need only a subset of the tests described in Section [Test Definitions](02-test-definitions). For example, modules with an integrated antenna may only need a quick go/no-go test to verify functionality and modules with an external antenna path will need to be evaluated for its radiated RF performance. Refer to _AN1048: Regulatory RF Module Certifications_ for more information on module certifications and the required testing.