# Source: https://docs.silabs.com/openthread/3.0.0/multi-pan-rcp-performance-for-openthread-and-zigbee/02-test-plan-strategy.md

# Test Plan Strategy

This test plan is focused on the performance of the Multiprotocol RCP using mixed protocol traffic streams. The tests are run with both protocols on the same channel, and with both protocols on different channels to test Concurrent Listening.

<table>
    <thead>
        <tr>
            <th>Scenario</th>
            <th>Devices</th>
            <th>Notes</th>
            <th>Illustrated Topology</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>9x9 single channel</td>
            <td>
                <p>9 SoC Devices OT</p>
                <p>9 Soc Devices Zigbee</p>
            </td>
            <td>Zigbee and OpenThread networks on the same channel.</td>
            <td><img src="/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image1.png" alt="image"></td>
        </tr>
        <tr>
            <td>9x9 dual channel</td>
            <td>
                <p>9 SoC Devices OT</p>
                <p>9 Soc Devices Zigbee</p>
            </td>
            <td>Zigbee and OpenThread on different channels to test Concurrent Listening on the RCP.</td>
            <td><img src="/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image1.png" alt="image"></td>
        </tr>
        <tr>
            <td>
                <p>Greater sizes</p>
                <p>(y)x(z)</p>
            </td>
            <td>
                <p>(y) SoC Devices OT</p>
                <p>(z) Soc Devices Zigbee</p>
            </td>
            <td></td>
            <td>The same setup as above but with more devices.</td>
        </tr>
    </tbody>
</table>

The SOC devices send periodic unicast traffic to the DuT (Device under Test) with staggered start times. We measure the reliability and latency for various packet sizes.