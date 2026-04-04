# Source: https://docs.nomad.xyz/operational-security/contracts.md

# Contracts

## Contract Addresses

Contracts are deployed and verified.

All details can be found in [the config repo](https://github.com/nomad-xyz/config).

* [Ethereum](#ethereum)
* [Moonbeam](#moonbeam)
* [Evmos](#evmos)
* [Milkomeda C1](#milkomeda-c1)
* [Gnosis Chain](#gnosis-chain)
* [Avalanche](#avalanche)

### Ethereum

#### Core Contracts

```
"ethereum": {
      "deployHeight": 13983724,
      "governanceRouter": {
        "beacon": "0x67833a48b3f509d4252ac2c19cd604556ed6c981",
        "implementation": "0x569d80f7fc17316b4c83f072b92ef37b72819de0",
        "proxy": "0x3009c99d370b780304d2098196f1ebf779a4777a"
      },
      "home": {
        "beacon": "0x063e871f8db991cead34b557a00b157b360084cc",
        "implementation": "0x8f184d6aa1977fd2f9d9024317d0ea5cf5815b6f",
        "proxy": "0x92d3404a7e6c91455bbd81475cd9fad96acff4c8"
      },
      "replicas": {
        "avalanche": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x5d94309e5a0090b165fa4181519701637b6daeba"
        },
        "evmos": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x5bae47bf29f4e9b1e275c0b427b84c4daa30033a"
        },
        "milkomedaC1": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0xef989866b66a491e7b6c7473d73b589450d0f766"
        },
        "moonbeam": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x049b51e531fd8f90da6d92ea83dc4125002f20ef"
        },
        "xdai": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x0a627a6398f429b62969cd475fb5ba8e04a4eb70"
        }
      },
      "updaterManager": "0x9272c9d5fa902ef3804ec81e0333ae420d57f715",
      "upgradeBeaconController": "0xdb378579c2af11817eea21474a39f95b5b9dfd7e",
      "xAppConnectionManager": "0xfe8874778f946ac2990a29eba3cfd50760593b2f"
    },
```

#### Token Bridge Contracts

```
"ethereum": {
  "bridgeRouter": {
    "beacon": "0xb70588b1a51f847d13158ff18e9cac861df5fb00",
    "implementation": "0xd3dfd3ede74e0dcebc1aa685e151332857efce2d",
    "proxy": "0x88a69b4e698a4b090df6cf5bd7b2d47325ad30a3"
  },
  "bridgeToken": {
    "beacon": "0x8ca56e6235d83ff2f4e779f0b35a6c856d5a2fb2",
    "implementation": "0x4ad6444b55729f657a71a82a5448f85ac8aa47ba",
    "proxy": "0x9f7ea856ba1fb88d35e000c45e75f134a756ac4f"
  },
  "customs": [],
  "deployHeight": 13983724,
  "ethHelper": "0x2d6775c1673d4ce55e1f827a0d53e62c43d1f304",
  "tokenRegistry": {
    "beacon": "0x4d5ff8a01ed833e11aba43821d2881a5f2911f98",
    "implementation": "0xa7e4fea3c1468d6c1a3a77e21e6e43daed855c1b",
    "proxy": "0x0a6f564c5c9bebd66f1595f1b51d1f3de6ef3b79"
  }
```

### Moonbeam

### Evmos

### Milkomeda C1

### Gnosis Chain

### Avalanche
