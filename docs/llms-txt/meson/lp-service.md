# Source: https://docs.meson.fi/protocol/system-design/lp-service.md

# LP Service

In Meson's swap process, users and LPs need to conduct multiple rounds of information exchange and verification. This process happens off-chain and requires LP to run a service, complete the necessary verification, signature, call Meson contract and other operations. We will provide an open source service that any LP can run to complete the redemption process. The LP needs to run this service on its own server, actively monitor the swap initiated by the user, lock funds for the swap, and finally complete the swap on the two chains. We will release an open source LP service that can complete the above process for most LPs to use. For LPs with independent trading strategies, they can modify and design specific workflow in the swap process according to the Meson protocol and the open-sourced LP services to meet their specific trading preferences.
