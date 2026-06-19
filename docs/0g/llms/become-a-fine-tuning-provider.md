# Become a Fine-tuning Provider

This guide provides a comprehensive walkthrough for setting up and offering computing power as a fine-tuning provider on the 0G Compute Network.

## Prerequisites

- Docker and Docker Compose
- TDX-enabled Intel CPU
- Compatible NVIDIA GPU (H100/H200 with TEE support)
- Wallet with 0G tokens for gas fees
- Publicly accessible server

## Preparation

### Download the Installation Package

- **Visit the Releases Page:** [0G Serving Broker Releases](https://github.com/0gfoundation/0g-serving-broker/releases)
- **Download and Extract:** Get the latest version of the fine-tuning installation package.

### Configuration Setup

**Copy the Config File:** Duplicate `config.example.yaml` to create `config.local.yaml`.

```bash
cp config.example.yaml config.local.yaml
```

**Modify Settings:**
- Set `servingUrl` to your publicly accessible URL.
- Set `privateKeys` using your wallet's private key for the 0G blockchain.

**Edit `docker-compose.yml`:** Replace `#PORT#` with the desired port, matching the port in `config.local.yaml`.

```bash