# 0G Data Availability (DA): Integration

To submit data to the 0G DA, you must run a DA Client node and the Encoder node. The DA client interfaces with the Encoder for data encoding and the Retriever for data access.

## Overview

### Maximum Blob Size
Users can submit data blobs up to 32,505,852 bytes in length, which are then processed, encoded, and distributed across a network of DA nodes. The system employs a sophisticated data processing flow that includes padding, matrix formation, redundant encoding, and signature aggregation.

### Fee Market
As the DA user, you pay a fee which is the (BLOB_PRICE) when submitting DA blob data.

### Submitting Data
See example here: https://github.com/0gfoundation/0g-da-example-rust/blob/main/src/disperser.proto

## Hardware Requirements

The following table outlines the hardware requirements for different types of DA Client nodes:

| Node Type | Memory | CPU | Disk | Bandwidth | Additional Notes |
|-----------|--------|-----|------|-----------|------------------|
| DA Client | 8 GB | 2 cores | - | 100 MBps | For Download / Upload |
| DA Encoder | - | - | - | - | NVIDIA Drivers: 12.04 on the RTX 4090* |
| DA Retriever | 8 GB | 2 cores | - | 100 MBps | For Download / Upload |

## Standing up DA Client, Encoder, Retriever

<Tabs>
<TabItem value="binary" label="DA Client" default>

## DA Client Node Installation

**1. Clone the DA Client Node Repo**

```bash
git clone https://github.com/0gfoundation/0g-da-client.git
```

**2. Build the Docker Image**

```bash
cd 0g-da-client
docker build -t 0g-da-client -f combined.Dockerfile .
```

**3. Set Environment Variables**

Create a file named `envfile.env` with the following content. Be sure you paste in your private key.

```bash