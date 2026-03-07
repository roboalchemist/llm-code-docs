# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-border-routing-counters.md

Represents the counters of packets forwarded via Border Routing. 

## Public Attributes

### mInboundUnicast

```
otPacketsAndBytes otBorderRoutingCounters::mInboundUnicast
```

**Description:** The counters for inbound unicast.

### mInboundMulticast

```
otPacketsAndBytes otBorderRoutingCounters::mInboundMulticast
```

**Description:** The counters for inbound multicast.

### mOutboundUnicast

```
otPacketsAndBytes otBorderRoutingCounters::mOutboundUnicast
```

**Description:** The counters for outbound unicast.

### mOutboundMulticast

```
otPacketsAndBytes otBorderRoutingCounters::mOutboundMulticast
```

**Description:** The counters for outbound multicast.

### mInboundInternet

```
otPacketsAndBytes otBorderRoutingCounters::mInboundInternet
```

**Description:** The counters for inbound Internet when DHCPv6 PD enabled.

### mOutboundInternet

```
otPacketsAndBytes otBorderRoutingCounters::mOutboundInternet
```

**Description:** The counters for outbound Internet when DHCPv6 PD enabled.

### mRaRx

```
uint32_t otBorderRoutingCounters::mRaRx
```

**Description:** The number of received RA packets.

### mRaTxSuccess

```
uint32_t otBorderRoutingCounters::mRaTxSuccess
```

**Description:** The number of RA packets successfully transmitted.

### mRaTxFailure

```
uint32_t otBorderRoutingCounters::mRaTxFailure
```

**Description:** The number of RA packets failed to transmit.

### mRsRx

```
uint32_t otBorderRoutingCounters::mRsRx
```

**Description:** The number of received RS packets.

### mRsTxSuccess

```
uint32_t otBorderRoutingCounters::mRsTxSuccess
```

**Description:** The number of RS packets successfully transmitted.

### mRsTxFailure

```
uint32_t otBorderRoutingCounters::mRsTxFailure
```

**Description:** The number of RS packets failed to transmit.