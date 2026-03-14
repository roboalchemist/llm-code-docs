# Source: https://docs.nomad.xyz/resources/faq.md

# Source: https://docs.nomad.xyz/token-bridge/faq.md

# FAQ

### Bridge Features <a href="#nomad-bridge-features" id="nomad-bridge-features"></a>

#### What assets are available to bridge? <a href="#what-assets-are-available-to-bridge-updated-01-13-2022" id="what-assets-are-available-to-bridge-updated-01-13-2022"></a>

You can bridge any ERC-20 permissionlessly using the Nomad token bridge. The Nomad core team doesn't control or deploy tokens manually. [Nomad token bridge smart contracts](https://docs.nomad.xyz/token-bridge/smart-contracts) automatically deploy bridged token contracts when assets are bridged for the first time.

For a complete list of tokens and their addresses see the [Deployed Tokens List](https://docs.nomad.xyz/token-bridge/deployed-tokens/mainnet).

#### Why can't I see `<a specific token>` in the Nomad bridge application?

The Nomad core team adds tokens on a case-by-case basis in the web application.

We are actively adding more assets. If you would like an asset listed, make your voice heard in the Nomad [Discord](https://discord.gg/RurtmJApqm)!

You can also [use Etherscan](https://docs.nomad.xyz/token-bridge/how-to-bridge/using-etherscan) to bridge tokens that we have not listed in the web app.

#### Do you have `<blank>` feature? <a href="#do-you-have-blank-feature" id="do-you-have-blank-feature"></a>

We are adding new features and making updates on a daily basis. Some things we have in the works:

* Transaction History View
* Adding Custom Tokens
* General UI Improvements

If you'd like to see a specific feature added, please reach out in the Nomad [Discord](https://discord.gg/RurtmJApqm).

### Bridging 101 <a href="#bridging-101" id="bridging-101"></a>

#### I bridged over my assets with `someOtherBridgeNotNomad`, why can’t I see them?[#](https://docs.nomad.xyz/bridge/faq.html#i-bridged-over-my-assets-with-someotherbridgenotnomad-why-can%E2%80%99t-i-see-them) <a href="#i-bridged-over-my-assets-with-someotherbridgenotnomad-why-cant-i-see-them" id="i-bridged-over-my-assets-with-someotherbridgenotnomad-why-cant-i-see-them"></a>

Each bridge deploys their own token contracts, so assets bridged using one Bridge A are not compatible with assets bridged using Bridge B, even though they started out with the same original asset.

If you want to bridge over with Nomad but you've already used another bridge, you'll need to bridge *back* to the origin chain, and then bridge again with Nomad. This will get you back on track.

#### How long does it take to bridge? <a href="#how-long-does-it-take-to-bridge" id="how-long-does-it-take-to-bridge"></a>

Bridging using Nomad usually takes around 35 mins, but can be up to +60 mins depending on on- and off- chain activity (see our [docs on the Nomad architecture](https://docs.nomad.xyz/) for more information).

However, we've partnered with Connext to give users an option to have a faster cross-chain experience! For a small fee, you can use Connext to enable faster transfers--around 7-15 mins!

#### It's been longer than the estimated time--where are my tokens? <a href="#it-s-been-longer-than-the-estimated-time-where-are-my-tokens" id="it-s-been-longer-than-the-estimated-time-where-are-my-tokens"></a>

Ocassionally there are times where it takes longer to process a transaction. This could be due to on-chain activity, or a delay in agent processing.

This could also be due to missing a step in the process, such as when sending assets back to Ethereum. You'll need to manually process the transaction. See [this answer](https://docs.nomad.xyz/bridge/faq.html#why-is-gas-estimate-so-high-to-get-my-funds-on-ethereum).

#### Do I get WETH or ETH? <a href="#do-i-get-weth-or-eth" id="do-i-get-weth-or-eth"></a>

You can bridge over WETH or ETH from Ethereum, but you will always receive WETH on the destination. If you bridge over ETH, the contract will automatically call a helper function to wrap your ETH for you.

If you use Connext to bridge your WETH back to Ethereum, you will receive ETH automatically through the Connext process.

If you use Nomad to bridge your WETH back to Ethereum, you will receive WETH and will need to unwrap it manually if you want ETH again.

#### Do you have a development/testnet site? <a href="#do-you-have-a-development-testnet-site" id="do-you-have-a-development-testnet-site"></a>

Yes! It is available at [development.app.nomad.xyz](https://development.app.nomad.xyz/)

### Connext + Nomad <a href="#connext-nomad" id="connext-nomad"></a>

#### What is your relationship with Connext? <a href="#what-is-your-relationship-with-connext" id="what-is-your-relationship-with-connext"></a>

Nomad and Connext are complementary pieces that work together to provide a better cross-chain experience for users. Connext is an interoperability protocol that allows users to swap/transact over liquidity that already exists on the chain. Nomad is at its core protocol for passing generalized data between arbitrary chains, and the Nomad Bridge is an application built to pass specific kinds of messages that allow you to bridge tokens.

Connext routers set up cross-chain liquidity pools for Nomad assets. For a small fee, these liquidity pools allow users to make faster swaps, since the assets have already been bridged over.

#### I bridged using Connext, where are my tokens? <a href="#i-bridged-using-connext-where-are-my-tokens" id="i-bridged-using-connext-where-are-my-tokens"></a>

When you bridge with Connext, you'll need to manually claim your tokens after the transaction has processed. You can claim your transaction using the [Nomad bridge](https://app.nomad.xyz/), or you can also use the Connext UI at `https://connextscan.io/tx/<txId>`

### Bridging to Ethereum <a href="#bridging-to-ethereum" id="bridging-to-ethereum"></a>

#### I'm trying to bridge my assets back to Ethereum and it's taking a long time. <a href="#i-m-trying-to-bridge-my-assets-back-to-ethereum-and-it-s-taking-a-long-time" id="i-m-trying-to-bridge-my-assets-back-to-ethereum-and-it-s-taking-a-long-time"></a>

When you bridge back to Ethereum, you'll need to process the transaction manually to disperse your funds at the end. You can do this by going to: `https://app.nomad.xyz/tx/nomad/<origin-chain>/<tx-id>`

### General <a href="#general" id="general"></a>

#### What is madWETH? <a href="#what-is-madweth" id="what-is-madweth"></a>

These are the same assets! Often times applications will prefix assets depending on the bridge that was used. Nomad assets are listed with either no prefix (WETH), or the mad- prefix (madWETH). We prefer to use no prefix or the mad- prefix and will kindly ask applications to change this for us, but sometimes there may be a delay in this change.

#### Why does my recently-bridged token have a funny name like `0006648936.eb48`? <a href="#why-does-my-recently-bridged-token-have-a-funny-name-like-0006648936-eb48" id="why-does-my-recently-bridged-token-have-a-funny-name-like-0006648936-eb48"></a>

In order to avoid sending redundant data like the token name and symbol with every message, the first time a bridged ERC-20 Token representation is deployed, metadata is pulled from the originating chain after initial deployment. This involves a round-trip between the replica and originating chain wherein data about name/symbol/decimals is synced.

This is expected behavior, and the explorer will update after a day or two.

#### Why is the ERC-20 token placeholder name like that? <a href="#why-is-the-erc-20-token-placeholder-name-like-that" id="why-is-the-erc-20-token-placeholder-name-like-that"></a>

`0006648936.eb48` is the Nomad domain ID for Ethereum and the last 4 letters of the token address on Ethereum

`6648936 == 0x657468` -- the utf8 encoding of 'eth'

USDC's address is `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`

Note the `eb48` at the end.
