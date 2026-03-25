# Source: https://blog.nomic.foundation/secure-deployments-with-hardhat-ignition-and-ledger-hardware-wallets-028080159e77/

Title: Secure deployments with Hardhat Ignition and Ledger hardware wallets

URL Source: https://blog.nomic.foundation/secure-deployments-with-hardhat-ignition-and-ledger-hardware-wallets-028080159e77/

Published Time: 2024-05-14T12:47:59.000Z

Markdown Content:
As you may know, we recently introduced Hardhat Ignition, a declarative system for deploying smart contracts on Ethereum, which aims to…

*   [![Image 1: Zoey](https://blog.nomic.foundation/content/images/size/w100/v2/da:true/resize:fill:144:144/0-5dusj5smzo3iqkwa.png)](https://blog.nomic.foundation/author/zoeytm/)

#### [Zoey](https://blog.nomic.foundation/author/zoeytm/)

14 May 2024• 2 min read

![Image 2: Secure deployments with Hardhat Ignition and Ledger hardware wallets](https://blog.nomic.foundation/content/images/size/w2000/max/1200/1-jtudwgpzwc8p9xpfrnya3a.jpg)

As you may know, we recently [introduced Hardhat Ignition](https://blog.nomic.foundation/introducing-hardhat-ignition-a-refreshed-deployments-experience-9580d2946e10), a declarative system for deploying smart contracts on Ethereum, which aims to pick up the torch from`hardhat-deploy`and expand Hardhat's deployment capabilities.

Among many other features, Hardhat Ignition supports deploying contracts using a Ledger hardware wallet via the `hardhat-ledger` plugin. This guide will show you how to deploy your contracts using a Ledger device.

The first step is to install the `hardhat-ledger` plugin:

`npm install --save-dev @nomicfoundation/hardhat-ledger`
### Configuring the Ledger plugin

We are going to use the [Sepolia testnet](https://ethereum.org/en/developers/docs/networks/?ref=blog.nomic.foundation#sepolia) to deploy our Hardhat Ignition module, so you need to add this network in your Hardhat config. Here we are using [Alchemy](https://alchemy.com/?ref=blog.nomic.foundation) to connect to the network.

You’ll also need to add the `@nomicfoundation/hardhat-ledger` plugin to your Hardhat config file, configure it for Sepolia, and add the accounts on your Ledger that you’ll use to deploy:

```
// ...rest of your imports... 
import("@nomicfoundation/hardhat-ledger"); 
 
// Go to <https://alchemy.com>, sign up, create a new App in 
// its dashboard, and set the Hardhat configuration variable 
// ALCHEMY_API_KEY to the key 
const ALCHEMY_API_KEY = vars.get("ALCHEMY_API_KEY"); 
export default { 
  // ...rest of your config... 
  networks: { 
    sepolia: { 
      url: `https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}`, 
      ledgerAccounts: [ 
        // This is an example address 
        // Be sure to replace it with an address from your own Ledger device 
        "0xa809931e3b38059adae9bc5455bc567d0509ab92", 
      ], 
    }, 
  }, 
};
```

To deploy on Sepolia you need to send some Sepolia ETH to the address that’s going to be making the deployment. You can get testnet ETH from a faucet, a service that distributes testing-ETH for free. Here is [Alchemy’s Sepolia Faucet](https://sepoliafaucet.com/?ref=blog.nomic.foundation).

For more information on how to configure the `hardhat-ledger` plugin for things like derivation path, or learning how to use it for signatures, check out the [plugin’s documentation](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-ledger?ref=blog.nomic.foundation).

### Deploying with Ledger

After configuring the plugin, you can now deploy your module as you normally would, and Hardhat Ignition will use your Ledger device to sign the transactions. For this example, we’ll be deploying the `Apollo` module from the Hardhat Ignition [quick start guide](https://hardhat.org/ignition/docs/getting-started?ref=blog.nomic.foundation#quick-start). Ensure that your Ledger device is plugged in, unlocked, connected to the Ethereum app, and with [Blind Signing enabled](https://www.ledger.com/academy/enable-blind-signing-why-when-and-how-to-stay-safe?ref=blog.nomic.foundation), then run the deploy command:

`npx hardhat ignition deploy ignition/modules/Apollo.ts --network sepolia`
This will deploy as usual, however, you will now be prompted on your Ledger device to confirm each transaction before it’s sent to the network. You should see a message like the following in your terminal:

```
Hardhat Ignition 🚀

Deploying [ Apollo ]

Batch #1
  Executing Apollo#Rocket...
  
  Ledger: Waiting for confirmation on device
```

At this point, you should see a prompt on your Ledger device to confirm the transaction. Once you confirm, the message will update to show that the transaction was sent to the network, and you’ll see the deployment progress in your terminal.

To learn more, check out the [Hardhat Ignition](https://hardhat.org/ignition/docs/getting-started?ref=blog.nomic.foundation#overview) and the [hardhat-ledger plugin](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-ledger?ref=blog.nomic.foundation) documentation.

### Feedback welcome

We would love your feedback if you run into any issues or have any feature requests! Please [open an issue on Github](https://github.com/NomicFoundation/hardhat-ignition/issues/new?ref=blog.nomic.foundation).
