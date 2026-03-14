# Source: https://docs.neuron.world/neuron-concepts/sdk-purpose-and-responsibility.md

# Purpose and Responsibility of the SDK

## Overview

The Neuron SDK is responsible for maintaining the fundamental network connectivity and security of the Neuron network. Its primary purpose is to ensure that when two peers decide to connect, they stay connected, regardless of network conditions or application behavior. This is different from regular P2P libraries - the SDK doesn't just send packets; it guarantees persistent connections backed by Service License Agreements (SLAs). Moreover, there are minimal external dependencies between the two peers other than the backing DLT; thus, two peers talking to each other should assume that they don't talk to anyone else other than themselves and the DLT. This is unless they agree to be relayed or use an external service to facilitate IP discovery, relaying, etc.

## Core SDK Responsibilities

### 1. Connection Persistence

* Maintain persistent connections between peers at all costs
* Automatically handle reconnection when connections fail
* Use the public ledger (DLT) for signaling and coordination
* Implement the exact reconnection logic specified in the SLA
* Handle NAT traversal and connection establishment
* Persist and maintain connection state
* Connect to peers even in the event of non reachable DLT servers if persistent state allows for connection re-establishemnt.

### 2. Security and Privacy

* Encrypt all sensitive data, especially IP addresses
* Use public key encryption for peer-to-peer communication
* Never expose private information on the public ledger
* Handle secure key management and storage
* Implement identity verification

### 3. Service Discovery

* Make peers discoverable on the network
* Handle service registration and availability
* Manage peer discovery through the network
* Support service advertisement on explorers
* Implement the standardized discovery protocol

## What the SDK Does NOT Do

* Handle application-specific business logic
* Manage application data formats or protocols
* Process application-level messages
* Make decisions about when to connect/disconnect
* Override the standardized connection behavior

## Key Distinctions

### SDK Responsibility

* Maintaining the connection itself using the DLT as a signalling layer
* Handling reconnection automatically
* Managing security and encryption
* Implementing the standardized protocol
* Making peers discoverable

### Application Responsibility

* Deciding which peers to connect to
* Managing application-specific data
* Implementing business logic
* Handling application-level protocols
* Managing application state

## Critical Requirements

### Must Do

1. Maintain persistent connections as specified in the SLA in a way that can be monitored buy outside validators
2. Implement exact reconnection logic without modification
3. Use public ledger only for essential signaling
4. Encrypt all sensitive data
5. Make peers discoverable on the network

### Must Not Do

1. Allow applications to override core connection behavior
2. Expose private information on the public ledger
3. Bypass the standardized protocol
4. Ignore connection failures
5. Modify the deterministic behavior

## Why This Matters

The SDK's behavior is deterministic and verifiable. Any peer on the network can observe the SDK's actions through the public ledger and verify that it's following the correct protocol. This is crucial for:

* Maintaining network reliability
* Ensuring fair service delivery
* Supporting SLA enforcement
* Enabling network validation
* Building trust in the system

## Technologies That Don't Meet Requirements

### 1. Distributed Hash Tables (DHTs)

DHTs like Kademlia or Chord fail to meet the SDK's requirements because:

* They expose IP addresses publicly in their routing tables
* They rely on a network of untrusted nodes for routing
* They don't guarantee persistent connections
* They can't be monitored for SLA compliance
* They don't support deterministic behavior verification

### 2. Unauthorized Relay Services

Relay services that aren't explicitly agreed upon by both peers are problematic because:

* They introduce unauthorized third parties into the communication
* They can't be monitored for SLA compliance
* They may compromise privacy and security
* They create unpredictable connection behavior
* They can't be verified through the public ledger

### 3. Centralized Signaling Servers

Traditional signaling servers (like those used in WebRTC) don't meet requirements because:

* They create a single point of failure
* They can't be monitored for SLA compliance
* They don't provide verifiable connection guarantees
* They may compromise privacy
* They don't support deterministic behavior

### 4. Peer Discovery Protocols (like mDNS)

Protocols that broadcast service availability locally fail because:

* They expose service information without encryption
* They don't guarantee persistent connections
* They can't be monitored for SLA compliance
* They don't support cross-network discovery
* They lack verifiable behavior
