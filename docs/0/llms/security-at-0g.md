# Security at 0G

At 0G, we prioritize the security and integrity of our platform. Our commitment to security is reflected in our rigorous audit processes and our active bug bounty program.

## Audits

We regularly conduct thorough security audits of our smart contracts, protocols, and infrastructure to ensure the highest level of security for our users.

### Recent Audits 

| Date | Auditor | Scope | Report |
|------|---------|-------|--------|
| Aug 2024 - Sept 2024 | Halborn | 0G Storage | [Report](https://github.com/0gfoundation/0g-doc/blob/main/audit/Halborn%200G%20Storage%20Node%20Audit.pdf) |
| Aug 2024 | Zellic | 0G Storage and 0G DA | [Report](https://github.com/0gfoundation/0g-doc/blob/main/audit/Zellic%200G%20Storage%20and%200G%20DA%20Audit.pdf) |
| Aug 2025 | Octane | 0G Chain | [Report](https://drive.google.com/file/d/1SgL-PDL_8jzDTUMQ9pO28OQVCP2IeqHR/view) |

For a complete list of our audits and their detailed reports, please visit our [GitHub repository](https://github.com/0gfoundation/0g-doc/tree/main/audit).

## [0G Labs Bug Bounty Program with Hackenproof](https://hackenproof.com/programs/0g-labs-smart-contracts)

At 0G, we believe in the power of **community-driven security**. Our bug bounty program invites security researchers and developers to help us identify and resolve potential vulnerabilities, ensuring the robustness of our systems. 

### Scope of the Bug Bounty Program
Our bug bounty program covers:
- Smart Contracts
- Infrastructure
- Protocol
  
## Focus Area

### In-Scope Vulnerabilities: 
We are interested in vulnerabilities that result in incorrect behavior of the smart contract and could lead to unintended functionality, including:

- Stealing or loss of funds
- Unauthorized transactions
- Transaction manipulation
- Attacks on logic (behavior that deviates from the intended business logic)
- Reentrancy attacks
- Reordering transactions
- Overflows and underflows

### Out-of-Scope Vulnerabilities: 
The following are out of scope for the bug bounty program:

- Theoretical vulnerabilities without proof or demonstration
- Old compiler versions
- Unlocked compiler version
- Vulnerabilities in imported contracts
- Code style guide violations
- Redundant code
- Gas optimizations
- Best practice issues
- Vulnerabilities exploitable through front-run attacks only

Additionally, the following contracts are out of scope for 0g-storage-contract:
- `cashier`
- `token`
- `reward/OnePoolReward`
- `reward/ChunkDecayReward`
- `uploadMarket`
- `utils/Exponent.sol`

### Rewards

Rewards are based on the severity of the discovered vulnerability:

| Severity | Reward Range |
|----------|--------------|
| Critical | $35,000 |
| High     | $8000 |
| Medium   | $2000 |
| Low      | $500 |

### Program Rules

- Avoid using web application scanners for automatic vulnerability searching which generates massive traffic
- Make every effort not to damage or restrict the availability of products, services, or infrastructure
- Avoid compromising any personal data, interruption, or degradation of any service
- Don’t access or modify other user data, localize all tests to your accounts
- Perform testing only within the scope
- Don’t exploit any DoS/DDoS vulnerabilities, social engineering attacks, or spam
- Don’t spam forms or account creation flows using automated scanners
- In case you find chain vulnerabilities we’ll pay only for vulnerability with the highest severity.
- Don’t break any law and stay in the defined scope
- Any details of found vulnerabilities must not be communicated to anyone who is not a HackenProof Team or an authorized employee of this Company without appropriate permission

### Disclosure Guidelines
:::important
- Do not discuss this program or any vulnerabilities (even resolved ones) outside of the program without express consent from the organization
- No vulnerability disclosure, including partial is allowed for the moment.
- Please do NOT publish/discuss bugs
:::

### Eligibility and Coordinated Disclosure

We are happy to thank everyone who submits valid reports which help us improve the security. However, only those that meet the following eligibility requirements may receive a monetary reward:

- You must be the first reporter of a vulnerability.
- The vulnerability must be a qualifying vulnerability
- Any vulnerability found must be reported no later than 24 hours after discovery and exclusively through hackenproof.com
- You must send a clear textual description of the report along with steps to reproduce the issue, include attachments such as screenshots or proof of concept code as necessary.
- You must not be a former or current employee of us or one of its contractors.
- ONLY USE the EMAIL under which you registered your HackenProof account (in case of violation, no bounty can be awarded)
- Provide detailed but to-the point reproduction steps

We look forward to working with the community to enhance 0G's security!

---

## 0G Whitepaper

<iframe 
      src="/whitepaper.pdf" 
      className="whitepaper-iframe"
      title="0G Whitepaper"
    >
      If you're unable to view the PDF, please click here to download it.
    </iframe>
  
  
    
      Download PDF

---

## Archival Node

---

Running an Archival node for the **0G-Galileo-Testnet** means providing complete historical data storage and access for the network, maintaining the full blockchain history and state.

:::info **What You'll Need**
- Linux system with sufficient disk space for archive data
- `lz4` compression tool installed
- Public IP address for node connectivity
- Stable internet connection
:::

## Hardware Requirements

| Component  | Requirement |
|------------|-------------|
| Memory     | 64 GB       |
| CPU        | 8 cores     |
| Disk       | Large NVME SSD (for full archive data) |
| Bandwidth  | 100 MBps for Download / Upload |

## Prerequisites

### Required Files

1. **Node Package**: [galileo-archive.tar.gz](/binaries/galileo-archive.tar.gz)
2. **Archive Snapshot**: Download from https://chain-snapshot.oss-cn-hongkong.aliyuncs.com/snapshot/galileo/archive/20250717.tar.lz4

### System Requirements

- Linux system with sufficient disk space for archive data
- `lz4` compression tool installed
- Public IP address for node connectivity

## Setup Guide

### 1. Download Node Package

Download the node package: [galileo-archive.tar.gz](/binaries/galileo-archive.tar.gz)

### 2. Extract Node Package

Unzip the file to your home directory

### 3. Download Archive Snapshot

Download the archive node snapshot from:

```
https://chain-snapshot.oss-cn-hongkong.aliyuncs.com/snapshot/galileo/archive/20250717.tar.lz4
```

### 4. Extract Snapshot

```bash
lz4 -d 20250717.tar.lz4 | tar -xvf - -C /your/snapshot/directory
```

## Deployment Steps

### 1. Copy Files and Set Permissions

```bash
cd galileo-v1.2.0
cp -r 0g-home {your data path}
sudo chmod 777 ./bin/geth
sudo chmod 777 ./bin/0gchaind
```

### 2. Initialize Geth

```bash
./bin/geth init --state.scheme=hash --db.engine=pebble --datadir /{your data path}/0g-home/geth-home ./genesis.json
```

### 3. Initialize 0gchaind with Temporary Directory

```bash
./bin/0gchaind init {node name} --home /{your data path}/tmp
```

### 4. Copy Node Files to 0gchaind Home

```bash
cp /{your data path}/tmp/data/priv_validator_state.json /{your data path}/0g-home/0gchaind-home/data/
cp /{your data path}/tmp/config/node_key.json /{your data path}/0g-home/0gchaind-home/config/
cp /{your data path}/tmp/config/priv_validator_key.json /{your data path}/0g-home/0gchaind-home/config/
```

### 5. Copy Data from Snapshot

```bash
cp -r /your/snapshot/directory/0g-home/geth-home/geth/chaindata /{your data path}/0g-home/geth-home/geth/
cp -r /your/snapshot/directory/0g-home/0gchaind-home/data /{your data path}/0g-home/0gchaind-home/
```

### 6. Start 0gchaind

```bash
cd galileo-v1.2.0
nohup ./bin/0gchaind start \
    --rpc.laddr tcp://0.0.0.0:26657 \
    --chaincfg.chain-spec devnet \
    --chaincfg.kzg.trusted-setup-path=kzg-trusted-setup.json \
    --chaincfg.engine.jwt-secret-path=jwt-secret.hex \
    --chaincfg.kzg.implementation=crate-crypto/go-kzg-4844 \
    --chaincfg.block-store-service.enabled \
    --chaincfg.node-api.enabled \
    --chaincfg.node-api.logging \
    --chaincfg.node-api.address 0.0.0.0:3500 \
    --pruning=nothing \
    --home /{your data path}/0g-home/0gchaind-home \
    --p2p.seeds 85a9b9a1b7fa0969704db2bc37f7c100855a75d9@8.218.88.60:26656 \
    --p2p.external_address {your node ip}:26656 > /{your data path}/0g-home/log/0gchaind.log 2>&1 &
```

### 7. Start Geth

```bash
cd galileo-v1.2.0
nohup ./bin/geth \
    --config geth-archive-config.toml \
    --nat extip:{your node ip} \
    --bootnodes enode://de7b86d8ac452b1413983049c20eafa2ea0851a3219c2cc12649b971c1677bd83fe24c5331e078471e52a94d95e8cde84cb9d866574fec957124e57ac6056699@8.218.88.60:30303 \
    --datadir /{your data path}/0g-home/geth-home \
    --state.scheme=hash \
    --gcmode archive \
    --networkid 16601 > /{your data path}/0g-home/log/geth.log 2>&1 &
```

### 8. Verify Setup

Check the logs to ensure the node is running properly:

```bash