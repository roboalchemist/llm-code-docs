# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/join-mainnet-verifier-nodes/operating-a-verifier-node/running-in-cli/using-docker.md

# Using Docker

{% hint style="info" %}
Note that the configuration may change while testing. Please check this page consistently for operation info.
{% endhint %}

One of the quickest ways to run verifier is by using Docker:

## Use Private Key (mode = 0)

**Update config\_docker.yaml**

Update your private\_key and run :

```
wallet:
  # wallet mode, by which way to pass the private key
  # 0: through startup parameters
  # 1: through plain text private key in config file
  # 2: through path and password of the keystore in config file
  mode: 0
  # plain text private key, needed when mode is 1
  private_key: "99a038e9d345d0b12130b3b1fb003bf8f2d3a5c27ce2a800bbb1608efff6c591"
  # path of the keystore, needed when mode is 2
  keystore_path: ""
  # password of the keystore, needed when mode is 2
  keystore_password: ""
```

```
docker run -d --name verifier -v /<Path To This Repository>/verifier/configs:/data/conf -v /<Path To Keystore direction>:/data/keystore carvprotocol/verifier:mainnet
```

## **Use Keystore (mode = 2)**

> If you want to use keystore, you need to generate a keystore file first. You can use the following command to generate a keystore file.

```
./verifier -generate-keystore -keystore-path <path to generate your keystore file>
```

After running the command, you can run verifier by following the steps below.

**update config\_docker.yaml**

Update your keystore\_path and keystore\_password and run :

```
wallet:
  # wallet mode, by which way to pass the private key
  # 0: through startup parameters
  # 1: through plain text private key in config file
  # 2: through path and password of the keystore in config file
  mode: 2
  # plain text private key, needed when mode is 1
  private_key: ""
  # path of the keystore, needed when mode is 2
  keystore_path: "/data/conf/xxxx/UTC--2021-09-29T07-00-00.000000000Z--xxxx"
  # password of the keystore, needed when mode is 2
  keystore_password: "123456"
```

```
docker run -d --name verifier -v /<Path To This Repository>/verifier/configs:/data/conf -v /<Path To Keystore direction>:/data/keystore carvprotocol/verifier:mainnet
```

#### Example Config

````
```yaml
chain:
  chain_id: 42161
  chain_name: "arbitrum"
  rpc_url: "https://arb1.arbitrum.io/rpc"
  start_block: 0
  offset_block: 14400 # arbitrum block time: 0.25 sec. An offset of 14400 starts fetching blocks from 1 hours ago.
  max_block_per_query: 500
  query_ticker: 5 # second
  report_delay: 30 # second
  enable_gas_mode: false # default: false
contract:
  addr: "0xa91fF8b606BA57D8c6638Dd8CF3FC7eB15a9c634"
  tee_addr: "0x8A5614d82187BAa01FB004D5adAcC86992543e67"
  topic1: "0x89a3b784b99180438f3b2027aa89e97c3c3ed66e8dc78a555d7013b39caf1a89"
  topic2: "0x455929120054502ca2ea8194b26e7bb3acb631d30177f6881ffa70581abd4a13"
  topic3: "0x8a0859fa4a2e331800d512db6925d210facda82733207cb9fe49e7da954fc4aa"
#wallet:
  ## wallet mode, by which way to pass the private key
  ## 0: through startup parameters
  ## 1: through plain text private key in config file
  ## 2: through path and password of the keystore in config file
#  mode: 1
#  private_key: "99a038e9d345d0b12130b3b1fb003bf8f2d3a5c27ce2a800bbb1608efff6c591"
#  keystore_path: ""
#  keystore_password: ""
#  reward_claimer_addr: "0x689d0b32Da0480095b7AE7b604f1b1997736B3F9"
#  commission_rate: 100
wallet:
  mode: 2
  private_key: ""
  keystore_path: "./keystore/UTC--2024-06-25T12-01-01.663731000Z--031cff11b035aa5f5189f163c1fc937bf0be235c"
  keystore_password: "123456"
  reward_claimer_addr: "0x689d0b32Da0480095b7AE7b604f1b1997736B3F9"
  commission_rate: 100
signature:
  domain_name: "ProtocolService"
  domain_version: "1.0.0"
  expired_time: 3600
gasless_service:
  url: "https://interface.carv.io"
  version: "1.0.0"
````
