# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-guidelines-efr32/06-conclusions-and-summary.md

# Conclusions and Summary

As you can see from the descriptions of each test phase within this document, the recommended tests and test flow are different when comparing characterization testing with manufacturing testing.

The following table lists the test recommendations by phase and [Table : Comparison of Test Phases](#conclusions-and-summary) on page [16](06-conclusions-and-summary) compares the test phases.

> **Note**: In the following table, C denotes tests recommended for characterization testing, L denotes tests recommended for low-volume manufacturing testing, and H denotes tests recommended for high-volume manufacturing.

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
            <td>CLH</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Supply Current</td>
            <td>CLH</td>
            <td>CLH</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit/Receive Verify</td>
            <td>CLH</td>
            <td>CLH</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Power</td>
            <td>CL</td>
            <td>L</td>
            <td>C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Frequency Offset</td>
            <td>CL</td>
            <td>L</td>
            <td>C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit EVM</td>
            <td>C</td>
            <td></td>
            <td>C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Transmit Sweep</td>
            <td>CL</td>
            <td></td>
            <td></td>
            <td>L</td>
            <td>C</td>
        </tr>
        <tr>
            <td>Spurious Emissions</td>
            <td>CL</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Sweep</td>
            <td>CL</td>
            <td></td>
            <td></td>
            <td>L</td>
            <td>C</td>
        </tr>
        <tr>
            <td>Receive Sensitivity</td>
            <td>CLH</td>
            <td>LH</td>
            <td>C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Receive Waterfall</td>
            <td>C</td>
            <td></td>
            <td>C</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>RSSI</td>
            <td>CL</td>
            <td>CL</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>External 32kHz Crystal</td>
            <td>CLH</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Peripherals</td>
            <td>CLH</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

**Comparison of Test Phases**

|**Step**|**Characterization**|**Manufacturing Low-Volume**|**Manufacturing High-Volume**|
|---|---|---|---|
|Program bootloader (if applicable)|Functional Test|Functional Test or Preconfigured|Preconfigured|
|Program/load test application|Functional Test|Functional Test or Preconfigured|Standalone/Test Mode within application|
|Load stack information|Functional Test|Functional Test or Preconfigured|Preconfigured|
|Load manufacturing Information|Functional Test|Functional Test|Golden Node application|
|Load application information|Functional Test|Functional Test|Preconfigured|
|Verify DUT operation|Functional Test|Functional Test|Golden Node application|
|Program/load production application|Functional Test|Functional Test|Preconfigured|

In the characterization phase of testing, all programming and configuration steps can be automated to occur within the test itself. In the low-volume manufacturing phase, some of these steps can be done before actual manufacturing. For example, the device can be preconfigured with the appropriate bootloader and/or test application. In the case of high-volume manufacturing, the test functions can be included in the production application as a test mode or a standalone test application can be used. The Golden Node application can be developed by the customer to configure the appropriate unique manufacturing information for each DUT.