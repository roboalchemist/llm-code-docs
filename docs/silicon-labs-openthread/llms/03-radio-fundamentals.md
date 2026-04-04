# Source: https://docs.silabs.com/openthread/3.0.0/wireless-networking-application-development-fundamentals/03-radio-fundamentals.md

# Radio Fundamentals

Radio is the wireless transmission of signals by modulation of electromagnetic waves with frequencies below those of visible light. Electromagnetic waves are, in the case of radio, a form of non-ionizing radiation, which travels by means of oscillating electromagnetic fields that pass through electrical conductors, the air, and the vacuum of space. Electromagnetic radiation does not require a medium of transport like a sound wave. Information can be imposed on electromagnetic waves by systematically changing (modulating) some property of the radiated waves, such as their amplitude or their frequency. When radio waves pass an electrical conductor, the oscillating fields induce an alternating current in the conductor. This can be detected and transformed into sound or other signals that reproduce the imposed information.

The word 'radio' is used to describe this phenomenon, and radio transmission signals are classed as _radio frequency emissions_. The range or spectrum of radio waves used for communication has been divided into arbitrary units for identification. The Federal Communications Commission (FCC) and National Telecommunications and Information Association (NTIA) arbitrarily define the radio spectrum in the United States as that part of the natural spectrum of electromagnetic radiation lying between the frequency limits of 9 kilohertz and 300 gigahertz, divided into various sub-spectrums for convenience.

The following names are commonly used to identify the various sub-spectrums:

|Name|Sub-Spectrum|
|---|---|
|Very Low Frequencies (VLF)|3 kHz to 30 kHz|
|Low Frequencies (LF)|30 kHz to 300 kHz|
|Medium Frequencies (MF)|300 kHz to 3,000 kHz|
|High Frequencies (HF)|3,000 kHz to 30,000 kHz|
|Very High Frequencies (VHF)|30,000 kHz to 300,000 kHz|
|Ultra High Frequencies (UHF)|300,000 kHz to 3,000,000 kHz|
|Super High Frequencies (SHF)|3,000,000 kHz to 30,000,000 kHz|
|Extremely High Frequencies (EHF)|30,000,000 kHz to 300,000,000 kHz|

Each of the sub-spectrums listed above are further subdivided into many other sub-portions or ‘bands.’ For example, the American AM Broadcast Band extends from 535 kHz to 1705 kHz, which is within the portion of the spectrum classified as _Medium Frequencies_.

## Frequency Bands

The radio spectrum is regulated by government agencies and by international treaties. Most transmitting stations, including commercial broadcasters, military, scientific, industrial, and amateur radio stations, require a license to operate. Each license typically defines the limits of the type of operation, power levels, modulation types, and whether the assigned frequency bands are reserved for exclusive or shared use. Three frequency bands can be used for transmitting radio signals without requiring licensing from the United States Government:

|Band|Description|
|---|---|
|900 MHz|The 900 MHz band was used extensively in different countries for different products including pagers and cellular devices. This band was considered to have good range characteristics. However, it can be less popular for products because it is not a worldwide unlicensed band, and products therefore need to be modified depending on where they are being used.|
|2400 MHz|The 2400 MHz band is a very commonly-used frequency band. This band was one of the first worldwide unlicensed bands and therefore became popular for wireless consumer products. Typical wireless technologies that use this band are 802.11b (1-11 Mbps), 802.11g (1-50 Mbps) and 802.15.4, as well as numerous proprietary radio types.|
|5200-5800 MHz|The 5200 MHz band has three sub-bands, the lowest being for indoor home use only, while the 5800 MHz frequencies can be used for long distance wireless links at very fast speeds (30 – 100 Mbps).|

A common strategy is to use 2400 MHz in residential and home environments. The Connectivity Standards Alliance and Thread Group endorse the use of this band, and both are looking at other SubGHz bands to expand their capabilities

## Signal Modulation

Modulation is the process of changing the behavior of a signal so that it transfers information. Modulation can also be thought of as a way to encode information to be transmitted to a receiver that decodes, or demodulates, the information into a useful form.

The basic radio frequency (RF) signal has a fundamental frequency that can be visualized as an alternating current whose frequency is referred to as the _carrier wave frequency_. The earliest method used for encoding information onto the carrier wave involved switching the carrier wave on and off in a specific time duration pattern. This was known as continuous wave (CW) mode. The carrier frequency can also be varied in its amplitude (that is, signal strength) or its frequency. These two modulation methods are called amplitude modulation (AM) and frequency modulation (FM), respectively. It is possible to impose a signal onto the carrier wave using these three basic modulation techniques and creative variations of these techniques.

The Silicon Labs EFR32 integrated circuit family uses a form of _offset quadrature phase-shift keying_ (OQPSK) to modulate the carrier wave. _Phase-shift keying_ (PSK) is a digital modulation scheme that conveys data by changing, or modulating, the phase of a reference signal such as the carrier wave. PSK is a derivative of FM techniques.

All digital modulation schemes use a finite number of distinct signals to represent digital data. In the case of PSK, a finite number of phases are used. Each of these phases is assigned a unique pattern of binary bits. Usually, each phase encodes an equal number of bits. Each pattern of bits forms the symbol that is represented by the particular phase. The demodulator, which is designed specifically for the symbol set used by the modulator, determines the phase of the received signal and maps it back to the symbol it represents, thus recovering the original data. To do so, the receiver must compare the phase of the received signal to a reference signal. Such a system is termed _coherent_.

## Antennas

An antenna (or aerial) is an arrangement of electrical conductors designed to emit or capture electromagnetic waves. The ability of an antenna to emit a signal that can be detected by another antenna is referred to as _radio propagation_. Antennas are made to a certain size based on the operating frequencies. An antenna from a 2400 MHz radio cannot be used effectively on a 5800 MHz radio, or vice versa. However, an antenna from one type of 2400 MHz technology, such as Wi-Fi or Bluetooth, can be used in another 2400 MHz technology, such as Zigbee or Thread.

Two fundamental types of antennas are described with reference to a specific three-dimensional space:

- Omni-directional: radiates equally in all directions
- Uni-directional (also known as directional): radiates more in one direction than in the other. All antennas radiate some energy in all directions in free space, but careful construction results in substantial transmission of energy in certain directions and negligible energy radiated in other directions.

In general, because of the nature of mesh networking, an omni-directional antenna is desired to provide as many communication paths as possible.

## How Far Signals Travel

The distance a radio signal will travel and the amount of information that can be transmitted is based on:

- The amount of power the antenna is transmitting into the air.
- The distance between the transmitting and receiving stations.
- How much radio signal strength the receiving radio needs.
- What types of physical/electrical obstructions are in the way.

### Radio Transmit Power

Radio transmit power is measured in watts, and typically discussed in terms of dBm, decibels referenced to 1 milliwatt. Converting wattage to dBm allows radio link calculations using simple addition and subtraction (dBm= 10*log10(P/ 0.001)).

For example, a typical power amplified wireless radio card transmits at 100 milliwatts (or mW), which translates to a power output of 20dBm.

If 1 mW, or 0 dBm, is the baseline for power in decibels, then +3 dBm is some power level above 1 mW (2 mW to be specific). The EFR32 platforms include some variants that go to +13 dBm and others that go up to +20 dBm, both without the aid of an external power amplifier.

### Signal Degradation

The radio also needs to be able to hear a radio signal at a certain level. The minimum signal strength required for a receiver to understand the data is called the _receive sensitivity_.

As the radio signal travels through the air, it weakens. When a radio signal leaves the transmitting antenna, the dBm is a high number (for example, 20dBm). As it travels through the air, it loses strength and drops to a negative number. At some point, a minimum value for dBm is reached, below which the radio will no longer successfully receive the transmission. This value represents the "receive sensitivity" or "Rx sensitivity." This value will vary with the type of radio used but is typically between -90dBm and -100dBm. (Refer to the datasheet for your radio chip for specific receive sensitivity figures.)

If you can achieve a signal level of -75dBm and your radio has an Rx sensitivity of -95dBm, you have 20dBm of extra signal to accommodate interference and other issues. This is called _margin_.

### How Far Can the Radio Signal Go

If you know the power out and the receiver sensitivity, you can determine whether you can broadcast over a given distance. In the following example, you want to know if you can receive a signal over five miles. To do so, you need to know the free space loss between the radio transmitter and the receiver.

For example, free space loss of a 2.4 GHz signal at 5 miles is 118.36 dB. So, you can estimate signal strength over the range of the network as:

|What|Add or subtract it|The value|
|---|---|---|
|Transmitter power|+|15 dBm|
|Transmitter antenna gain|+|14 dBi|
|Receiver antenna gain|+|14 dBi|
|Transmitter's coaxial cable loss|-|2 dB|
|Receiver's coaxial cable loss|-|2 dB|
|Free Space Loss @ 5 miles|-|118.36 dB|
| |Total|-79.36 dBm|

In other words, a 15 dBm radio hooked into a 14 dBi antenna, transmitting 5 miles through free space to another radio hooked up to a 14 dBi antenna, yields approximately -79 dBm of signal. Note that antennas with gain are necessarily directional, and would need to be aimed at each other. However, physical obstructions such as buildings or trees would have a substantial impact on these calculations. Typical Zigbee and Thread networks use smaller, lower-cost antennas without the gain increase and only use power amplifiers if extended range is required. Occasionally, external low-noise amplifiers (LNAs) may also be employed to boost RX sensitivity of incoming signals just before they reach the radio.

This calculation is provided as an example. See _Embedded Software Tools_ in [Manufacturing Test Overview](https://docs.silabs.com/zigbee/latest/mfg-test-overview/04-embedded-software-tools/) for a summary of the tools that can be used for performing range tests with different protocols.

The Flex SDK comes with the RangeTest application. It has a version that can be used to measure Bluetooth and IEEE 802.15.4 ranges, called "RangeTest BLE and IEEE 802.15.4". For more information, see [Range Test Demo User's Guide in Flex SDK v3.x](https://docs.silabs.com/rail/latest/flex-v3x-range-test-demo/) or _UG147: Range Test Demo User's Guide in Flex SDK v2.x_. Silicon Labs recommends that basic range testing be conducted in the expected environment to evaluate whether extended range is required.