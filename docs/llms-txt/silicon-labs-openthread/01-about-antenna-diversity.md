# Source: https://docs.silabs.com/openthread/3.0.0/configuring-antenna-diversity-for-openthread/01-about-antenna-diversity.md

# About Antenna Diversity

Antenna diversity is a technique used to improve radio performance by using two different antennas to transmit and/or receive messages. For a more detailed explanation of the problems with signal transmission and reception in indoor environments and how antenna diversity can mitigate those problems, see [Using Antenna Diversity to Create Highly Robust Radio Links](https://www.silabs.com/documents/public/white-papers/using-antenna-diversity-to-create-highly-robust-radio-links.pdf).

Antenna diversity may be applied to transmission (Tx) and/or reception (Rx). Diversity is achieved using an external RF switch, either standalone or as part of a FEM (Front End Module) / LNA (Low Noise Amplifier).

The Tx algorithm uses reception of the packet acknowledgement (ACK) to determine if it should change antennas. If the device does not receive an ACK after packet transmission it toggles the RF switch to the other antenna and tries again. It retries two more times, for a total of four attempts, before the MAC (Media Access Layer) fails the transmit up to the network layer. Specifically, the worst-case scenario is as follows:

- New MAC packet transmitted on antenna 1.
- No ACK received so antenna is switched to antenna 2.
- MAC retransmit #1 sent on antenna 2.
- No ACK received, so antenna is switched to antenna 1.
- MAC retransmit #2 sent on antenna 1.
- No ACK received, so antenna is switched to antenna 2.
- MAC retransmit #3 sent on antenna 2.
- No ACK received, so antenna is switched to antenna 1.
- (MAC retries have exhausted, so MAC fails transmit to network layer).
- The next transmit will start on antenna 1.

If transmission is successful, at the beginning of the next transmission the device starts on the last successfully-used antenna.

In Rx antenna diversity with RSSI (Received Signal Strength Indicator), the receiver alternates between antenna 1 and antenna 2 during the timing search looking for a valid timing pattern on the incoming signal. When a valid timing pattern is found, antenna diversity tries to select the best antenna for receiving the rest of the frame. To achieve this, the signal quality for the currently active antenna is saved/updated at every subsequent antenna switch. Therefore, at the first timing detect event the algorithm already has a fresh quality metric for one antenna.

To perform a valid comparison between antenna 1 and antenna 2, the radio switches simultaneously with the timing detect event to the other antenna to perform a signal quality evaluation/update there. Finally, antenna quality results get compared, and the algorithm selects the better antenna for packet reception. If the better antenna is the current antenna, then the Rx operation carries on with packet reception without further antenna switching. If the better antenna is the other antenna, then the radio switches to that one, reacquires timing and carries on with packet reception on that antenna.

In antenna diversity, longer preambles are often used to provide the antenna diversity algorithm time to detect and evaluate the signal on each antenna to ensure that a true preamble is found. However, shorter preambles are preferred as they reduce MCU on-time and in turn reduce MCU current consumption. The RSSI measurement technique for evaluating signal quality requires less preamble time than other methods such as timing correlation.

> **Note**: Antenna Rx diversity is available for testing and evaluation purposes on the Gecko SDK suite. Due to the short preambles on the 802.15.4 packets, customers will need to make their own assessment on the performance and production readiness of this feature.

Rx and Tx antenna diversity are independent operations. In practice this means that, for example, Tx antenna diversity will begin the next transmission on the last successfully used antenna for Tx (for example antenna 1), even though in the intervening receive Rx antenna diversity found better signal quality on antenna 2.