# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/smart-contract-upgradeability.md

# Smart Contract Upgradeability

The following smart contracts are upgradeable:

* [LightClient](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/light-client)
* [FeeContract](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/fee-token)

These contracts use the *universally upgradeable proxy pattern (UUPS)* to make it possible to upgrade functionality in the contract, e.g., adding a new method for a future launch.

## How it works

A proxy contract directs calls to the implementation contract, which contains the logic of the system.

When an upgrade is needed, a new implementation contract is deployed and the proxy contract's storage is updated so that it will now route requests to the new implementation. This allows for modifications to be made without affecting the state stored in the contract. Espresso users can continue interacting with the same contract address (the address of the proxy) to access the updated functionalities of the implementation contract. Careful consideration will be made to ensure backward compatibility and data consistency during the upgrade process.
