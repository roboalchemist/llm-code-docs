# Source: https://docs.silabs.com/openthread/3.0.0/zigbee-openthread-coexistence-wifi/index.md

# Zigbee and OpenThread Coexistence with Wi-Fi

> **Note: This section replaces _AN1017: Zigbee and OpenThread Coexistence with Wi-Fi_. Further updates to this application note will be provided here**.

This application note describes methods to improve coexistence of 2.4 GHz IEEE 802.11b/g/n Wi-Fi and IEEE 802.15.4-based radios such as Zigbee® and OpenThread. This section assumes you have a basic understanding of the concepts and principles of Wi-Fi coexistence with 802.15.4 radios and how Wi-Fi coexistence is implemented on EFR32 devices. For more information, see [Wi-Fi Coexistence Fundamentals](https://docs.silabs.com/multiprotocol/latest/multiprotocol-wifi-coexistence-fundamentals/).

This application note describes EFR32 Zigbee and OpenThread coexistence support for EmberZNet PRO 6.9.0.0 and OpenThread 1.1.0.0 versions and above.

Additional details about the implementation of managed coexistence are included in _AN1243: Timing and Test Data for EFR32 Coexistence with Wi-Fi_, available under non-disclosure from Silicon Labs Sales.