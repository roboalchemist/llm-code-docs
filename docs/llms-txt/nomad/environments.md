# Source: https://docs.nomad.xyz/developers/environments.md

# Environments

Nomad is currently deployed on both mainnet and testnets of various networks, across three environments:

* Development
* Staging
* Production

### Contract Addresses

The addresses of Nomad contracts deployed on-chain can be found in our [configuration](https://github.com/nomad-xyz/config) package.&#x20;

Our [development](https://github.com/nomad-xyz/config/blob/main/development.json) environment is deployed on testnets and intended for Nomad core team to test new features and debug. It is unstable!

Our [staging](https://github.com/nomad-xyz/config/blob/main/staging.json) environment is deployed on testnets so that developers can test their cross-chain applications.

Our [production](https://github.com/nomad-xyz/config/blob/main/production.json) environment is deployed on mainnets for real-world application usage.

### Bridge App

The Nomad bridge app is available in both environments.

Production: [https://app.nomad.xyz/](https://staging.app.nomad.xyz/)

Staging: <https://staging.app.nomad.xyz/>

Development: <https://development.app.nomad.xyz/>
