# Check 0gchaind logs
tail -f /{your data path}/0g-home/log/0gchaind.log
```

:::success **Success Indicators**
- 0gchaind should show "Committed state" messages
- Geth should show archive mode synchronization
- No error messages in either log
:::

## Important Configuration Notes

### Variables to Replace

- `{your data path}`: Your chosen data directory path
- `{node name}`: Your chosen node name
- `{your node ip}`: Your server's public IP address
- `/your/snapshot/directory`: Path where you extracted the snapshot

### Directory Structure

After setup, your directory structure should look like:

```
{your data path}/
└── 0g-home/
    ├── geth-home/
    ├── 0gchaind-home/
    │   ├── config/
    │   │   ├── node_key.json
    │   │   └── priv_validator_key.json
    │   └── data/
    │       └── priv_validator_state.json
    └── log/
        ├── 0gchaind.log
        └── geth.log
```

### Network Ports

Ensure the following ports are open:

- **26657**: 0gchaind RPC
- **26656**: 0gchaind P2P
- **3500**: Node API
- **30303**: Geth network

## Archive Node Benefits

Archive nodes provide several key benefits to the 0G network:

- **Complete Historical Data**: Full access to all historical blockchain data and state
- **Enhanced Query Capabilities**: Support for complex historical queries and analytics
- **Network Resilience**: Backup and redundancy for the network's historical data
- **Developer Support**: Essential for applications requiring historical blockchain data

:::warning **Storage Requirements**
Archive nodes require significantly more storage space than regular nodes as they maintain the complete blockchain history. Ensure adequate disk space before setup.
:::

---

## Community Docker Repository

---

This section provides a list of Docker images 🐳 for 0G DA from the community. For instructions on running 0G nodes via binary installation, please visit the node pages directly.

For most users, Docker offers the simplest method to get 0G nodes up and running. Docker is a platform for containerization, allowing 0G nodes to operate in an isolated environment. This approach enables you to run 0G nodes on your system without needing to install and configure all the necessary dependencies manually.

Most of the officially endorsed 0G Docker implementations can be found under the documentation page for each 0G node type. 

Below is a list of community-maintained Docker images for 0G DA. Please note that these images are not officially endorsed by 0G, and users should proceed with caution.

### All Node Types
[Ember Stake](https://docs.emberstake.xyz/networks/zero-gravity/nodes-guide/getting-started)

### Validator Node
[CryptoWarden](https://medium.com/@CryptoWarden/guide-to-running-a-node-in-the-0g-labs-project-0g-ai-1bee56ea53ca)

---

## Data Availability Node

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';