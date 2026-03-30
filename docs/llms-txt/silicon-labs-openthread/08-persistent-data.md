# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/08-persistent-data.md

# Persistent Data

Devices operating in the field may be reset accidentally or on purpose for a variety of reasons. Devices that have been reset need to restart network operations without user intervention. For this to be done successfully, non-volatile storage must store the following information:

- Network information (such as PAN ID)
- Security material
- Addressing information from the network to form the IPv6 addresses for the devices