# Source: https://docs.silabs.com/openthread/3.0.0/multi-pan-rcp-performance-for-openthread-and-zigbee/04-test-methodology.md

# Test Methodology

OpenThread traffic is generated using the ping command, which uses Internet Control Message Protocol (ICMP) Echo Request and Echo Reply packets. The Echo Reply packets sent by the DuT have the same packet length as the received Echo Request packet.

The Zigbee throughput plugin sends APS messages one-way from the SoC to the DuT. 802.15.4 acks are sent in return, but not APS acks.

The following illustrates the test setup.

- Traffic flow is directed at the DuT.
- Many > One, where the One is the DuT.
- Current testing assumes all devices are within 1 hop.

![image](/multi-pan-rcp-performance-for-openthread-and-zigbee/0.2/images/sld805-image1.png)

Additional details on the traffic created follow.

## Open Thread

OT testing used ping (ICMP) with a variable IP payload of 16 bytes up to a maximum of 1232 bytes.

[https://github.com/openthread/openthread/blob/main/src/cli/README.md#ping--i-source-ipaddr-size-count-interval-hoplimit-timeout](https://github.com/openthread/openthread/blob/main/src/cli/README.md#ping--i-source-ipaddr-size-count-interval-hoplimit-timeout)

```C
ping [-I source] <ipaddr> [size] [count] [interval] [hoplimit] [timeout]
```

Example:

```C
> ping -I fd00:db8:0:0:76b:6a05:3ae9:a61a 8 3 1 1 1
> 16 bytes from fd00:db8:0:0:f605:fb4b:d429:d59a: icmp_seq=4 hlim=64 time=18ms
> 16 bytes from fd00:db8:0:0:f605:fb4b:d429:d59a: icmp_seq=5 hlim=64 time=20ms
> 16 bytes from fd00:db8:0:0:f605:fb4b:d429:d59a: icmp_seq=6 hlim=64 time=19ms
3 packets transmitted, 3 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 18/19.0/20 ms.
Done
```

For the 8-byte payload size specified in the first argument to ping above, ICMP adds 8 bytes of header, and the total packet size including 40 bytes of 802.15.4 and IP headers comes to 56 bytes.

The maximum 802.15.4 packet is 127 bytes. Subtracting the 48 bytes of headers, the maximum IP payload for a single packet is 79 bytes. Larger payload sizes cause OT packets to be fragmented.

## Zigbee

Zigbee testing uses the Zigbee throughput component.

As before, the maximum 802.15.4 packet size is 127 bytes. Subtracting 45 bytes of 802.15.4 and Zigbee headers, the maximum Zigbee payload size is 82 bytes. This component cannot send fragmented packets.