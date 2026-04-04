# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-overview/06-range-test.md

# Range Test

A crucial aspect of designing an RF wireless product is maximizing its operational range when communicating with another device. To achieve this, perform a range test, which could be the final but important step for characterizing the product. The test setup consists of a transmitter and a receiver with their known RF parameters (transmit power, receiver sensitivity) and their spatial arrangement. Wireless communication is then initiated (frequency, data rate, and modulation parameters chosen according to the desired operation), and the receiver performance is measured.

The accounting of the measurable parameters and environmental effects is called the link budget, according to the following equation:

![link budget](/mfg-test-overview/0.1/images/sld869-image2.png)

where:

- PRX: received power (dBm)
- PTX: transmitter output power (dBm)
- GTX: transmitter antenna gain (dBi)
- LTX: transmitter losses (cables, connectors) (dB)
- LFS: path loss (free space and multipath propagation) (dB)
- LM: miscellaneous losses (fading, polarization, mismatch, interference, absorption, weather) (dB)
- GRX: receiver antenna gain (dBi)
- LRX: receiver losses (cables, connectors) (dB)

However, other variables play a crucial role in the quality of the RF link, such as:

- Antenna radiation pattern: Silicon Labs recommends placing the transmitter and receiver devices facing each another with their maximas of radiation.
- Frequency offset: Any occurrent frequency offset between the transmitter and receiver can degrade the range.
- Distance from the ground: The proximity of ground degrades performance.

See KBA [RF range factors](https://community.silabs.com/s/article/rf-range-factors?language=en_US) for a list of the most prominent effecting variables.

Prior to the range test, ensure that the product is finalized in terms of overall RF performance (TX power, harmonics, RX sensitivity, antenna matching) and that the test procedure best represents a use case scenario with the inclusion of the plastic case or having a human hand in the proximity of the device (if there is going to be one).

Sensitivity is the minimum received power at the antenna port of the device at which the data transfer is still adequately successful. A common way of determining sensitivity is by counting the number of sent, and successfully received packets, and calculating the Packet Error Rate percentage (PER%). A similar method is calculating the Bit Error Rate percentage (BER%). Refer to the datasheet of the Silicon Labs device for the ideal sensitivity values depending on data rate, frequency, and modulation.

Silicon Labs recommends first choosing an open field with as few environmental factors as possible to determine the maximum range. Then, measure the BER or PER and modify the range accordingly, so that the measured value is equal to or less than the predefined value in the datasheet of the device. If equal, the received signal strength at the antenna port equals the sensitivity of the device by definition.

It is good practice to choose an operating range that is smaller than the determined maximum range so that there is some margin (link margin) between the received signal and the sensitivity of the device to allow for the detrimental effects of the degrading variables.

After the range of the communication has been determined, any introduced additional link budget to the system (e.g., by increasing the transmitter power) also yields an improvement in the range of the RF link, which can be approximated by the following formula:

![RF link](/mfg-test-overview/0.1/images/sld869-image3.png)

where:

- ΔLB is the extra link budget introduced to the RF link
- n is the propagation factor, which is usually between 2.8 and 4 (3 for line of sight) outdoors
- Roriginal is the range prior to the introduced link budget
- Rnew is the improved range after the introduced link budget
- ΔR is the ratio of the new range to the original range

As an example, this means that if the link budget introduced to the RF link is e.g., 3 dB and n = 3 is assumed, the calculated range increase is ΔR = 1.25 (25% improvement).

Follow [Flex SDK v3.x Range Test Demo User's Guide](https://docs.silabs.com/rail/latest/flex-v3x-range-test-demo/) for the range test evaluation of the Gecko EFR32 devices.