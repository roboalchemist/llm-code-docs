# Tempo Documentation

Source: https://docs.tempo.xyz/llms-full.txt

---

# Tempo

Documentation for the Tempo network and protocol specifications

<!--
Sitemap:
- [Tempo](/index): Explore Tempo's blockchain documentation, integration guides, and protocol specs. Build low-cost, high-throughput payment applications.
- [Changelog](/changelog)
- [Learn](/learn/): Explore stablecoin use cases and Tempo's payments-optimized blockchain architecture for remittances, payouts, and embedded finance.
- [Tempo Protocol](/protocol/): Technical specifications and reference documentation for the Tempo blockchain protocol, purpose-built for global payments at scale.
- [SDKs](/sdk/): Integrate Tempo into your applications with SDKs for TypeScript, Go, Rust, and Foundry. Build blockchain apps in your preferred language.
- [!Replace Me!](/guide/_template)
- [Building with AI](/guide/building-with-ai): Tempo documentation is built with AI-first principles, providing llms.txt files, Markdown rendering, and MCP server access for AI assistants.
- [Stablecoin Issuance](/guide/issuance/): Create and manage your own stablecoin on Tempo. Issue tokens, manage supply, and integrate with Tempo's payment infrastructure.
- [Tempo Node](/guide/node/): Run your own Tempo node for direct network access. Set up RPC nodes for API access or validator nodes to participate in consensus.
- [Stablecoin Payments](/guide/payments/): Send and receive stablecoin payments on Tempo. Integrate payments with flexible fee options, sponsorship capabilities, and parallel transactions.
- [Exchange Stablecoins](/guide/stablecoin-dex/): Trade between stablecoins on Tempo's enshrined DEX. Execute swaps, provide liquidity, and query the onchain orderbook for optimal pricing.
- [Use Tempo Transactions](/guide/tempo-transaction/): Learn how to use Tempo Transactions for configurable fee tokens, fee sponsorship, batch calls, access keys, and concurrent execution.
- [Create & Use Accounts](/guide/use-accounts/): Create and integrate Tempo accounts with domain-bound passkeys or connect to EVM-compatible wallets. Choose embedded or universal account experiences.
- [Partners](/learn/partners): Discover Tempo's ecosystem of stablecoin issuers, wallets, custody providers, compliance tools, and ramps ready for mainnet launch.
- [What are stablecoins?](/learn/stablecoins): Learn what stablecoins are, how they maintain value through reserves, and the payment use cases they enable for businesses globally.
- [Tempo](/learn/tempo/): Discover Tempo, the payments-first blockchain with instant settlement, predictably low fees, and native stablecoin support.
- [Exchanging Stablecoins](/protocol/exchange/): Tempo's enshrined decentralized exchange for trading between stablecoins with optimal pricing, limit orders, and flip orders for liquidity provision.
- [Transaction Fees](/protocol/fees/): Pay transaction fees in any USD stablecoin on Tempo. No native token required—fees are paid directly in TIP-20 stablecoins with automatic conversion.
- [Tempo Improvement Proposals (TIPs)](/protocol/tips/)
- [Tempo Transactions](/protocol/transactions/): Learn about Tempo Transactions, a new EIP-2718 transaction type with passkey support, fee sponsorship, batching, and concurrent execution.
- [Connect to the Network](/quickstart/connection-details): Connect to Tempo Testnet using browser wallets, CLI tools, or direct RPC endpoints. Get chain ID, URLs, and configuration details.
- [Developer Tools](/quickstart/developer-tools): Explore Tempo's developer ecosystem with indexers, embedded wallets, node infrastructure, and analytics partners for building payment apps.
- [EVM Differences](/quickstart/evm-compatibility): Learn how Tempo differs from Ethereum. Understand wallet behavior, fee token selection, VM layer changes, and fast finality consensus.
- [Faucet](/quickstart/faucet): Get free test stablecoins on Tempo Testnet. Connect your wallet or enter any address to receive pathUSD, AlphaUSD, BetaUSD, and ThetaUSD.
- [Integrate Tempo Testnet](/quickstart/integrate-tempo): Start building on Tempo Testnet. Connect to the network, explore SDKs, and follow guides for accounts, payments, and stablecoin issuance.
- [Predeployed Contracts](/quickstart/predeployed-contracts): Discover Tempo's predeployed system contracts including TIP-20 Factory, Fee Manager, Stablecoin DEX, and standard utilities like Multicall3.
- [Tempo Token List Registry](/quickstart/tokenlist)
- [Contract Verification](/quickstart/verify-contracts): Verify your smart contracts on Tempo using contracts.tempo.xyz. Sourcify-compatible verification with Foundry integration.
- [Wallet Integration Guide](/quickstart/wallet-developers): Integrate Tempo into your wallet. Handle fee tokens, configure gas display, and deliver enhanced stablecoin payment experiences for users.
- [Foundry for Tempo](/sdk/foundry/): Build, test, and deploy smart contracts on Tempo using the Foundry fork. Access protocol-level features with forge and cast tools.
- [Go](/sdk/go/): Build blockchain apps with the Tempo Go SDK. Send transactions, batch calls, and handle fee sponsorship with idiomatic Go code.
- [Rust](/sdk/rust/): Build blockchain apps with the Tempo Rust SDK using Alloy. Query chains, send transactions, and manage tokens with type-safe Rust code.
- [TypeScript SDKs](/sdk/typescript/): Build blockchain apps with Tempo using Viem and Wagmi. Send transactions, manage tokens, and integrate AMM pools with TypeScript.
- [Create a Stablecoin](/guide/issuance/create-a-stablecoin): Create your own stablecoin on Tempo using the TIP-20 token standard. Deploy tokens with built-in compliance features and role-based permissions.
- [Distribute Rewards](/guide/issuance/distribute-rewards): Distribute rewards to token holders using TIP-20's built-in reward mechanism. Allocate tokens proportionally based on holder balances.
- [Manage Your Stablecoin](/guide/issuance/manage-stablecoin): Configure stablecoin permissions, supply limits, and compliance policies. Grant roles, set transfer policies, and control pause/unpause functionality.
- [Mint Stablecoins](/guide/issuance/mint-stablecoins): Mint new tokens to increase your stablecoin's total supply. Grant the issuer role and create tokens with optional memos for tracking.
- [Use Your Stablecoin for Fees](/guide/issuance/use-for-fees): Enable users to pay transaction fees using your stablecoin. Add fee pool liquidity and integrate with Tempo's flexible fee payment system.
- [Installation](/guide/node/installation): Install Tempo node using pre-built binaries, build from source with Rust, or run with Docker. Get started in minutes with tempoup.
- [Network Upgrades and Releases](/guide/node/network-upgrades): Timeline and details for Tempo network upgrades and important releases for node operators.
- [Operate your validator node](/guide/node/operate-validator): Day-to-day operations for Tempo validators. Node lifecycle, upgrades, key rotation, monitoring, and troubleshooting.
- [Running an RPC Node](/guide/node/rpc): Set up and run a Tempo RPC node for API access. Download snapshots, configure systemd services, and monitor node health and sync status.
- [System Requirements](/guide/node/system-requirements): Minimum and recommended hardware specs for running Tempo RPC and validator nodes. CPU, RAM, storage, network, and port requirements.
- [Running a validator node](/guide/node/validator): Configure and run a Tempo validator node. Generate signing keys, participate in DKG ceremonies, and troubleshoot consensus issues.
- [Accept a Payment](/guide/payments/accept-a-payment): Accept stablecoin payments in your application. Verify transactions, listen for transfer events, and reconcile payments using memos.
- [Pay Fees in Any Stablecoin](/guide/payments/pay-fees-in-any-stablecoin): Configure users to pay transaction fees in any supported stablecoin. Eliminate the need for a separate gas token with Tempo's flexible fee system.
- [Send a Payment](/guide/payments/send-a-payment): Send stablecoin payments between accounts on Tempo. Include optional memos for reconciliation and tracking with TypeScript, Rust, or Solidity.
- [Send Parallel Transactions](/guide/payments/send-parallel-transactions): Submit multiple transactions concurrently using Tempo's expiring nonce system under-the-hood.
- [Sponsor User Fees](/guide/payments/sponsor-user-fees): Enable gasless transactions by sponsoring fees for your users. Set up a fee payer service and improve UX by removing friction from payment flows.
- [Attach a Transfer Memo](/guide/payments/transfer-memos)
- [Executing Swaps](/guide/stablecoin-dex/executing-swaps): Learn to execute instant stablecoin swaps on Tempo's DEX. Get price quotes, set slippage protection, and batch approvals with swaps.
- [Managing Fee Liquidity](/guide/stablecoin-dex/managing-fee-liquidity): Add and remove liquidity in the Fee AMM to enable stablecoin fee conversions. Monitor pools, check LP balances, and rebalance reserves.
- [Providing Liquidity](/guide/stablecoin-dex/providing-liquidity): Place limit and flip orders to provide liquidity on the Stablecoin DEX orderbook. Learn to manage orders and set prices using ticks.
- [View the Orderbook](/guide/stablecoin-dex/view-the-orderbook): Inspect Tempo's onchain orderbook using SQL queries. View spreads, order depth, individual orders, and recent trade prices with indexed data.
- [Add Funds to Your Balance](/guide/use-accounts/add-funds): Get test stablecoins on Tempo testnet using the faucet. Request pathUSD, AlphaUSD, BetaUSD, and ThetaUSD tokens for development and testing.
- [Batch Transactions](/guide/use-accounts/batch-transactions)
- [Connect to Wallets](/guide/use-accounts/connect-to-wallets): Connect your application to EVM-compatible wallets like MetaMask on Tempo. Set up Wagmi connectors and add the Tempo network to user wallets.
- [Embed Passkey Accounts](/guide/use-accounts/embed-passkeys): Create domain-bound passkey accounts on Tempo using WebAuthn for secure, passwordless authentication with biometrics like Face ID and Touch ID.
- [Scheduled Transactions](/guide/use-accounts/scheduled-transactions)
- [WebAuthn & P256 Signatures](/guide/use-accounts/webauthn-p256-signatures)
- [Onchain FX](/learn/tempo/fx): Access foreign exchange liquidity directly onchain with regulated non-USD stablecoin issuers and multi-currency fee payments on Tempo.
- [Tempo Transactions](/learn/tempo/modern-transactions): Native support for gas sponsorship, batch transactions, scheduled payments, and passkey authentication built into Tempo's protocol.
- [TIP-20 Tokens](/learn/tempo/native-stablecoins): Tempo's stablecoin token standard with payment lanes, stable fees, reconciliation memos, and built-in compliance for regulated issuers.
- [Performance](/learn/tempo/performance): High throughput and sub-second finality built on Reth SDK and Simplex Consensus for payment applications requiring instant settlement.
- [Privacy](/learn/tempo/privacy): Explore Tempo's opt-in privacy features enabling private balances and confidential transfers while maintaining issuer compliance.
- [Power AI agents with programmable money](/learn/use-cases/agentic-commerce): Power autonomous AI agents with programmable stablecoin payments for goods, services, and digital resources in real time.
- [Bring embedded finance to life with stablecoins](/learn/use-cases/embedded-finance): Enable platforms and marketplaces to streamline partner payouts, lower payment costs, and launch rewarding loyalty programs.
- [Send global payouts instantly](/learn/use-cases/global-payouts): Deliver instant, low-cost payouts to contractors, merchants, and partners worldwide with stablecoins, bypassing slow banking rails.
- [Enable true pay-per-use pricing](/learn/use-cases/microtransactions): Enable true pay-per-use pricing with sub-cent payments for APIs, content, IoT services, and machine-to-machine commerce.
- [Stablecoins for Payroll](/learn/use-cases/payroll): Faster payroll funding, cheaper cross-border payouts, and new revenue streams for payroll providers using stablecoins.
- [Send money home faster and cheaper](/learn/use-cases/remittances): Send cross-border payments faster and cheaper with stablecoins, eliminating correspondent banks and reducing transfer costs.
- [Move treasury liquidity instantly across borders](/learn/use-cases/tokenized-deposits): Move treasury liquidity instantly across borders with real-time visibility into global cash positions using tokenized deposits.
- [Consensus and Finality](/protocol/blockspace/consensus): Tempo uses Simplex BFT via Commonware for deterministic sub-second finality with Byzantine fault tolerance.
- [Blockspace Overview](/protocol/blockspace/overview): Technical specification for Tempo block structure including header fields, payment lanes, subblocks, and system transaction ordering.
- [Payment Lane Specification](/protocol/blockspace/payment-lane-specification): Technical specification for Tempo payment lanes ensuring dedicated blockspace for payment transactions with predictable fees during congestion.
- [Sub-block Specification](/protocol/blockspace/sub-block-specification): Technical specification for subblocks enabling non-proposing validators to include transactions in every block with guaranteed blockspace access.
- [DEX Balance](/protocol/exchange/exchange-balance): Hold token balances directly on the Stablecoin DEX to save gas costs on trades, receive maker proceeds automatically, and trade more efficiently.
- [Executing Swaps](/protocol/exchange/executing-swaps): Learn how to execute swaps and quote prices on Tempo's Stablecoin DEX with exact-in and exact-out swap functions and slippage protection.
- [Providing Liquidity](/protocol/exchange/providing-liquidity): Provide liquidity on Tempo's DEX using limit orders and flip orders. Earn spreads while facilitating stablecoin trades with price-time priority.
- [Quote Tokens](/protocol/exchange/quote-tokens): Quote tokens determine trading pairs on Tempo's DEX. Each TIP-20 specifies a quote token, with pathUSD available as an optional neutral choice.
- [Stablecoin DEX](/protocol/exchange/spec): Technical specification for Tempo's enshrined DEX with price-time priority orderbook, flip orders, and multi-hop routing for stablecoin trading.
- [Fee AMM Overview](/protocol/fees/fee-amm/): Understand how the Fee AMM automatically converts transaction fees between stablecoins, enabling users to pay in any supported token.
- [Fee Specification](/protocol/fees/spec-fee): Technical specification for Tempo's fee system covering multi-token fee payment, fee sponsorship, token preferences, and validator payouts.
- [Fee AMM Specification](/protocol/fees/spec-fee-amm): Technical specification for the Fee AMM enabling automatic stablecoin conversion for transaction fees with fixed-rate swaps and MEV protection.
- [TIP-20 Rewards](/protocol/tip20-rewards/overview): Built-in reward distribution mechanism for TIP-20 tokens enabling efficient, opt-in proportional rewards to token holders at scale.
- [TIP-20 Rewards Distribution](/protocol/tip20-rewards/spec): Technical specification for the TIP-20 reward distribution system using reward-per-token accumulator pattern for scalable pro-rata rewards.
- [TIP-20 Token Standard](/protocol/tip20/overview): TIP-20 is Tempo's native token standard for stablecoins with built-in fee payment, payment lanes, transfer memos, and compliance policies.
- [TIP20](/protocol/tip20/spec): Technical specification for TIP-20, the optimized token standard extending ERC-20 with memos, rewards distribution, and policy integration.
- [TIP-403 Policy Registry](/protocol/tip403/overview): Learn how TIP-403 enables TIP-20 tokens to enforce access control through a shared policy registry with whitelist and blacklist support.
- [Overview](/protocol/tip403/spec): Technical specification for TIP-403, the policy registry system enabling whitelist and blacklist access control for TIP-20 tokens on Tempo.
- [TIP Title](/protocol/tips/_tip_template): Short description for SEO
- [State Creation Cost Increase](/protocol/tips/tip-1000): Increased gas costs for state creation operations to protect Tempo from adversarial state growth attacks.
- [Place-only mode for next quote token](/protocol/tips/tip-1001): A new DEX function for creating trading pairs against a token's staged next quote token, to allow orders to be placed on it.
- [Prevent crossed orders and allow same-tick flip orders](/protocol/tips/tip-1002): Changes to the Stablecoin DEX that prevent placing orders that would cross existing orders on the opposite side of the book, and allow flip orders to flip to the same tick.
- [Client order IDs](/protocol/tips/tip-1003): Addition of client order IDs to the Stablecoin DEX, allowing users to specify their own order identifiers for idempotency and easier order tracking.
- [Permit for TIP-20](/protocol/tips/tip-1004): Addition of EIP-2612 permit functionality to TIP-20 tokens, enabling gasless approvals via off-chain signatures.
- [Fix ask swap rounding loss](/protocol/tips/tip-1005): A fix for a rounding bug in the Stablecoin DEX where partial fills on ask orders can cause small amounts of quote tokens to be lost.
- [Burn At for TIP-20 Tokens](/protocol/tips/tip-1006): The burnAt function for TIP-20 tokens, enabling authorized administrators to burn tokens from any address.
- [Fee Token Introspection](/protocol/tips/tip-1007): Addition of fee token introspection functionality to the FeeManager precompile, enabling smart contracts to query the fee token being used for the current transaction.
- [Expiring Nonces](/protocol/tips/tip-1009): Time-bounded replay protection using transaction hashes instead of sequential nonce management.
- [Mainnet Gas Parameters](/protocol/tips/tip-1010): Initial gas parameters for Tempo mainnet launch including base fee pricing, payment lane capacity, and transaction gas limits.
- [Enhanced Access Key Permissions](/protocol/tips/tip-1011): Extends Access Keys with periodic spending limits and destination address scoping for subscription-based and restricted access patterns.
- [Compound Transfer Policies](/protocol/tips/tip-1015): Extends TIP-403 with compound policies that specify different authorization rules for senders and recipients.
- [Exempt Storage Creation from Gas Limits](/protocol/tips/tip-1016): Storage creation gas costs are charged but don't count against transaction or block gas limits, enabling higher contract code pricing and better throughput for new account operations.
- [ValidatorConfig V2](/protocol/tips/tip-1017): Second-generation validator configuration precompile with append-only semantics for historical validator set reconstruction.
- [Account Keychain Precompile](/protocol/transactions/AccountKeychain): Technical specification for the Account Keychain precompile managing access keys with expiry timestamps and per-token spending limits.
- [EIP-4337 Comparison](/protocol/transactions/eip-4337): How Tempo Transactions achieve EIP-4337 goals without bundlers, paymasters, or EntryPoint contracts.
- [EIP-7702 Comparison](/protocol/transactions/eip-7702): How Tempo Transactions extend EIP-7702 delegation with additional signature schemes and native features.
- [Tempo Transaction](/protocol/transactions/spec-tempo-transaction): Technical specification for the Tempo transaction type (EIP-2718) with WebAuthn signatures, parallelizable nonces, gas sponsorship, and batching.
- [Setup](/sdk/typescript/prool/setup): Set up infinite pooled Tempo node instances in TypeScript with Prool for testing and local development of blockchain applications.
- [Handler.compose](/sdk/typescript/server/handler.compose): Combine multiple Tempo server handlers into a single endpoint. Run fee payer and key manager services together from one server.
- [Handler.feePayer](/sdk/typescript/server/handler.feePayer): Create a server handler to subsidize gas costs for users. Sign transactions with a dedicated fee payer account on your backend.
- [Handler.keyManager](/sdk/typescript/server/handler.keyManager): Create a server handler to manage WebAuthn credential public keys. Enable passkey authentication for users across multiple devices.
- [Overview](/sdk/typescript/server/handlers): Framework-agnostic server handlers for Tempo protocol operations. Works with Node.js, Bun, Deno, Express, Hono, and Next.js.
-->

# Tempo \[Documentation, integration guides, and protocol specifications]

## Welcome to Tempo

Tempo is a general-purpose blockchain optimized for payments. Tempo is designed to be a low-cost, high-throughput blockchain with user and developer features that we believe should be core to a modern payment system.

Tempo was designed in close collaboration with an exceptional group of [design partners](https://tempo.xyz/ecosystem) who are helping to validate the system against real payment workloads.

Whether you're new to stablecoins, ready to start building, or looking for partners to help you integrate, these docs will help you get started with Tempo.

<Cards>
  <Card description="Start here to understand what they are, why they matter, and the real-world payment use cases they enable." to="/learn" icon="lucide:book-open" title="Learn About Stablecoins" />

  <Card description="Connect to the testnet, get faucet funds, and start building with our SDKs and guides." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Integrate Tempo Testnet" />

  <Card description="Work with our ecosystem partners for stablecoin issuance, custody, compliance, orchestration, and infrastructure." to="/learn/partners" icon="lucide:users" title="Build With Partners" />

  <Card description="Connect with the Tempo team to discuss partnerships, integration opportunities, or opportunities to collaborate." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get In Touch" />
</Cards>

# Changelog

::changelog

# Learn \[Notes on stablecoin use cases and Tempo's architecture]

Tempo is a general-purpose blockchain optimized for payments. Tempo is designed to be a low-cost, high-throughput blockchain with user and developer features that we believe should be core to a modern payment system.

Tempo was designed in close collaboration with an exceptional group of [design partners](https://tempo.xyz/ecosystem) who are helping to validate the system against real payment workloads. Here, we have written about what stablecoins are and how Tempo is designed from the ground up for the use cases they enable.

<Cards>
  <Card description="Learn what stablecoins are, how they work, and the real-world use cases they enable" to="/learn/stablecoins" icon="lucide:dollar-sign" title="How Stablecoins Work" />

  <Card description="Learn about what makes Tempo optimized for stablecoin payments at scale" to="/learn/tempo" icon="lucide:info" title="Tempo Overview" />
</Cards>

## Stablecoin use cases

Stablecoins enable a wide range of payment and financial use cases across industries:

<Cards>
  <Card description="Enable fast, cheap, and predictable cross-border money transfers for individuals and businesses" to="/learn/use-cases/remittances" icon="lucide:send" title="Remittances" />

  <Card description="Deliver instant, low-cost payouts to employees and contractors anywhere in the world" to="/learn/use-cases/global-payouts" icon="lucide:globe" title="Global Payouts" />

  <Card description="Let platforms and marketplaces embed seamless payment flows directly into their applications" to="/learn/use-cases/embedded-finance" icon="lucide:wallet" title="Embedded Finance" />

  <Card description="Move treasury liquidity instantly across borders with real-time visibility into global cash positions" to="/learn/use-cases/tokenized-deposits" icon="lucide:landmark" title="Tokenized Deposits" />

  <Card description="Enable true pay-per-use pricing with sub-cent payments for APIs, content, and IoT services" to="/learn/use-cases/microtransactions" icon="lucide:activity" title="Microtransactions" />

  <Card description="Power autonomous agents with programmable payments for goods, services, and digital resources" to="/learn/use-cases/agentic-commerce" icon="lucide:bot" title="Agentic Commerce" />
</Cards>

# Tempo Protocol

Tempo is a blockchain protocol purpose-built for global payments. Rather than being a general-purpose platform, Tempo makes deliberate technical choices optimized for payments at scale.

This section provides details on the Tempo Protocol specifications, and serves as a technical reference for protocol implementers, auditors, and core contributors building on Tempo.

## Protocol Components

<Cards>
  <Card description="Core token standard with native stablecoin features and policy registry integration" to="/protocol/tip20/overview" icon="lucide:coins" title="TIP-20 Tokens" />

  <Card description="Reward distribution system for token holders with automated yield mechanisms" to="/protocol/tip20-rewards/overview" icon="lucide:gift" title="TIP-20 Rewards" />

  <Card description="Policy registry system for compliance, access control, and token governance" to="/protocol/tip403/overview" icon="lucide:shield" title="TIP-403 Policies" />

  <Card description="Multi-token fee payment system with AMM for stablecoin conversion" to="/protocol/fees" icon="lucide:wallet" title="Fees" />

  <Card description="EIP-2718 transaction type with native passkeys, batching, scheduling, and fee sponsorship" to="/protocol/transactions" icon="lucide:layers" title="Tempo Transactions" />

  <Card description="Block format, payment lanes, and sub-blocks for optimized throughput" to="/protocol/blockspace/overview" icon="lucide:layout" title="Blockspace" />

  <Card description="Enshrined stablecoin DEX for stablecoin interoperability" to="/protocol/exchange" icon="lucide:arrow-left-right" title="Stablecoin DEX" />

  <Card description="View the full Tempo protocol source code and implementation" to="https://github.com/tempoxyz/tempo" icon="lucide:github" title="GitHub Repository" />
</Cards>

# SDKs

Tempo is building clients in multiple languages to make integration as easy as possible.

<Cards>
  <Card description="Build on Tempo using TypeScript" to="/sdk/typescript" icon="lucide:code" title="TypeScript" />

  <Card description="Build on Tempo using Go" to="/sdk/go" icon="lucide:box" title="Go" />

  <Card description="Build on Tempo using Foundry" to="/sdk/foundry" icon="lucide:hammer" title="Foundry" />

  <Card description="Build on Tempo using Rust" to="/sdk/rust" icon="lucide:cog" title="Rust" />
</Cards>

# !Replace Me

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam elementum odio ante, sit amet tincidunt leo scelerisque vitae.

<Demo.Container name="!Replace Me!" footerVariant="source" src="tempoxyz/examples/tree/main/examples/replace-me">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateToken stepNumber={3} last />
</Demo.Container>

## Steps

### Lorem

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::code-group

```tsx twoslash [Component.tsx]
// @noErrors
export function Component() {
  return (
    <div>
      {/* Component code here */}
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempoModerato.id]: http(),
  },
})
```

:::

### Ipsum

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

:::code-group

```tsx twoslash [Component.tsx]
// @noErrors
export function Component() {
  // Component code here
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempoModerato.id]: http(),
  },
})
```

:::

::::

## Recipes

### Foo

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Bar

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Best Practices

### Foo

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### Bar

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

## Learning Resources

<Cards>
  <Card description="Learn more about the Tempo transaction type that enables passkey signatures" to="/guide/use-accounts/webauthn-p256-signatures" icon="lucide:file" title="Tempo Transaction type" />

  <Card description="Learn more about how (passkey) signatures are structured in the protocol" to="/guide/use-accounts/webauthn-p256-signatures" icon="lucide:signature" title="Signatures" />
</Cards>

# Building with AI

Tempo documentation is built with AI-first principles, providing multiple features to make documentation accessible to LLMs and AI assistants.

## llms.txt

The docs automatically generate [`llms.txt`](https://llmstxt.org/) files for LLM consumption:

* `/llms.txt` – A concise index of all pages with titles and descriptions
* `/llms-full.txt` – Complete documentation content in a single file

These files are generated at build time and served at the root of the site.

## Markdown Rendering for AI Agents

AI user agents are automatically detected and served raw Markdown instead of rendered HTML. This provides better token efficiency and easier parsing for LLMs.

### Supported AI Agents

Popular user agents that are automatically detected:

* **OpenAI**: `GPTBot`, `ChatGPT-User`
* **Anthropic**: `ClaudeBot`, `claude-web`
* **Google**: `Googlebot`

See the [full list of supported agents](https://github.com/wevm/vocs/blob/next/src/waku/internal/middleware/md-router.ts#L3) for the most up-to-date list.

### Manual Markdown Access

Any page can be accessed as Markdown by appending `.md` to the URL:

```
https://docs.tempo.xyz/quickstart/integrate-tempo.md
```

This is useful for copying documentation into AI conversations or for custom integrations.

## Ask AI Menu

The docs include a built-in "Ask AI" menu (<kbd>⌘I</kbd> / <kbd>Ctrl+I</kbd>) that provides:

* **Open in ChatGPT/Claude**: Opens the current page context in popular AI assistants
* **Copy page for AI**: Copies the page content as Markdown to your clipboard
* **View as Markdown**: Opens the raw Markdown version of the current page
* **Copy MCP URL**: Copies the MCP server URL for AI assistant configuration

## MCP Server

The docs include a built-in [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that allows AI assistants to navigate documentation and source code programmatically.

:::code-group

```bash [Claude Code]
claude mcp add --transport http tempo https://docs.tempo.xyz/api/mcp
```

```bash [Codex CLI]
codex mcp add vercel --url https://docs.tempo.xyz/api/mcp
```

```bash [Amp]
amp mcp add tempo https://docs.tempo.xyz/api/mcp
```

:::

### Connecting AI Assistants

Configure your AI assistant to connect to the MCP server:

```json
{
  "mcpServers": {
    "tempo-docs": {
      "url": "https://docs.tempo.xyz/api/mcp"
    }
  }
}
```

### Available Tools

The MCP server exposes these tools to AI assistants:

| Tool | Description |
| --- | --- |
| `list_pages` | List all documentation pages with their paths |
| `read_page` | Read the content of a specific documentation page |
| `search_docs` | Search documentation for a query string |

### Source Code Navigation

The MCP server also provides access to source code repositories:

| Tool | Description |
| --- | --- |
| `list_sources` | List available source code repositories |
| `list_source_files` | List files in a directory |
| `read_source_file` | Read a source code file |
| `get_file_tree` | Get a recursive file tree |
| `search_source` | Search source code for a pattern |

Available source repositories:

* [`tempoxyz/tempo`](https://github.com/tempoxyz/tempo) – Tempo node implementation
* [`tempoxyz/tempo-ts`](https://github.com/tempoxyz/tempo-ts) – TypeScript SDK
* [`paradigmxyz/reth`](https://github.com/paradigmxyz/reth) – Reth Ethereum client
* [`foundry-rs/foundry`](https://github.com/foundry-rs/foundry) – Foundry development toolkit
* [`wevm/viem`](https://github.com/wevm/viem) – TypeScript interface for Ethereum
* [`wevm/wagmi`](https://github.com/wevm/wagmi) – React hooks for Ethereum

## Agent Skills

Install the [Tempo Agent Skills](https://github.com/tempoxyz/agent-skills) to give AI coding agents (Amp, Claude Code, etc.) access to Tempo documentation, source code via MCP, and examples. Check out [`tempoxyz/agent-skills`](https://github.com/tempoxyz/agent-skills) for more info on available skills.

### Installation

```bash
npx skills add tempoxyz/agent-skills
```

Or manually:

```bash
git clone https://github.com/tempoxyz/agent-skills.git
cp -r agent-skills/skills/tempo ~/.config/agents/skills/
```

Or add to your project's [`.agents/skills/`](https://github.com/tempoxyz/agent-skills/tree/main/skills) directory for project-specific access.

### Usage

Once installed, the skill is automatically available. The agent will use it when relevant tasks are detected.

**Examples:**

```
How do I create a TIP-20 stablecoin?
```

```
Show me how fee sponsorship works in Viem
```

```
Search the Tempo source for transaction validation
```

# Stablecoin Issuance

Create and manage your own stablecoin on Tempo. Learn how to issue tokens, manage supply, and integrate with Tempo's payment infrastructure.

<Cards>
  <Card description="Create your own stablecoin using the TIP-20 token standard with built-in compliance features" to="/guide/issuance/create-a-stablecoin" icon="lucide:coins" title="Create a Stablecoin" />

  <Card description="Mint new tokens to increase supply and distribute your stablecoin" to="/guide/issuance/mint-stablecoins" icon="lucide:plus" title="Mint Stablecoins" />

  <Card description="Enable users to pay transaction fees using your stablecoin" to="/guide/issuance/use-for-fees" icon="lucide:circle-dollar-sign" title="Use Your Stablecoin for Fees" />

  <Card description="Manage roles, permissions, supply caps, and transfer policies for your stablecoin" to="/guide/issuance/manage-stablecoin" icon="lucide:settings" title="Manage Your Stablecoin" />
</Cards>

# Tempo Node

Running a Tempo node allows you to interact with the network directly, providing your own RPC access or contributing to network infrastructure. Nodes provide JSON-RPC API access for applications, explorers, and wallets but do not participate in consensus.

## Supported Platforms

Prebuilt binaries are available for:

* **Linux** (x86\_64 and ARM64) - requires glibc ≥ 2.38
* **macOS** (ARM64)

## Getting Started

<Cards>
  <Card description="Hardware and software requirements for running a node" to="/guide/node/system-requirements" icon="lucide:hard-drive" title="System Requirements" />

  <Card description="Download and install the Tempo node software" to="/guide/node/installation" icon="lucide:download" title="Installation" />

  <Card description="Configure and run a full RPC node" to="/guide/node/rpc" icon="lucide:play" title="Running an RPC Node" />

  <Card description="Upcoming and past network upgrades and important releases" to="/guide/node/network-upgrades" icon="lucide:arrow-up-circle" title="Network Upgrades and Releases" />
</Cards>

:::info
Validator onboarding requires coordination with the Tempo team. Reach out to us if you are interested.
:::

# Stablecoin Payments

Send and receive payments using stablecoins on Tempo. Learn how to integrate payments into your application with flexible fee options and sponsorship capabilities.

<Cards>
  <Card description="Send stablecoin payments between accounts with optional memos for reconciliation" to="/guide/payments/send-a-payment" icon="lucide:send" title="Send a Payment" />

  <Card description="Accept payments from users and integrate payment flows into your application" to="/guide/payments/accept-a-payment" icon="lucide:handshake" title="Accept a Payment" />

  <Card description="Attach 32-byte references to TIP-20 transfers for payment reconciliation" to="/guide/payments/transfer-memos" icon="lucide:file-text" title="Attach a Transfer Memo" />

  <Card description="Configure users to pay transaction fees in any supported stablecoin" to="/guide/payments/pay-fees-in-any-stablecoin" icon="lucide:circle-dollar-sign" title="Pay Fees in Any Stablecoin" />

  <Card description="Sponsor transaction fees for your users to enable gasless transactions" to="/guide/payments/sponsor-user-fees" icon="lucide:heart-handshake" title="Sponsor User Fees" />

  <Card description="Submit multiple transactions in parallel using nonce keys" to="/guide/payments/send-parallel-transactions" icon="lucide:git-branch" title="Send Parallel Transactions" />
</Cards>

# Exchange Stablecoins

Trade between stablecoins on Tempo's enshrined decentralized exchange (DEX). The DEX enables optimal pricing for cross-stablecoin payments while minimizing chain load.

<Cards>
  <Card description="Learn about pathUSD, the root quote token that powers stablecoin interoperability" to="/protocol/exchange/quote-tokens#pathusd" icon="lucide:coins" title="pathUSD" />

  <Card description="Execute swaps between stablecoins" to="/guide/stablecoin-dex/executing-swaps" icon="lucide:arrow-left-right" title="Executing Swaps" />

  <Card description="Query price levels, individual orders, and liquidity on the onchain orderbook" to="/guide/stablecoin-dex/view-the-orderbook" icon="lucide:book-open" title="View the Onchain Orderbook" />

  <Card description="Provide liquidity by placing limit orders or flip orders in the orderbook" to="/guide/stablecoin-dex/providing-liquidity" icon="lucide:droplet" title="Providing Liquidity" />
</Cards>

## Use Tempo Transactions

Tempo Transactions are a new [EIP-2718](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2718.md) transaction type, exclusively available on Tempo.

:::note\[SDKs Support]
Transaction [SDKs](#integration-guides) are available for TypeScript, Rust, Go, and Foundry.
:::

If you're integrating with Tempo, we **strongly recommend** using Tempo Transactions, and not regular Ethereum transactions. Learn more about the benefits below, or follow the guide on issuance [here](/guide/issuance).

<Cards>
  <Card description="Pay transaction fees with any USD-denominated TIP-20 token via automatic Fee AMM conversion." to="#configurable-fee-tokens" icon="lucide:coins" title="Configurable Fee Tokens" />

  <Card description="Sponsor gas fees for users, enabling feeless transaction experiences in your application." to="#fee-sponsorship" icon="lucide:shield-check" title="Fee Sponsorship" />

  <Card description="Batch multiple transactions together for higher throughput and simpler wallet management." to="#batch-calls" icon="lucide:layers" title="Batch Calls" />

  <Card description="Delegate transaction signing capabilities to specific keys with customizable permissions." to="#access-keys" icon="lucide:key" title="Access Keys" />

  <Card description="Execute transactions in parallel using independent nonces for improved throughput." to="#concurrent-transactions" icon="lucide:zap" title="Concurrent Transactions" />

  <Card description="Create nonces that automatically expire after a set time window." to="#expiring-nonces" icon="lucide:timer" title="Expiring Nonces" />

  <Card description="Use two-dimensional nonces for flexible transaction ordering." to="#2d-nonces" icon="lucide:grid-2x2" title="2D Nonces" />

  <Card description="Schedule transactions to execute within a specific time window for automated payments." to="#scheduled-transactions" icon="lucide:clock" title="Scheduled Transactions" />
</Cards>

## Integration Guides

Integrating Tempo Transactions is easy and can be done quickly by a developer in multiple languages. See below for quick links to some of our guides.

|Language|Source|Integration Time|
|--------|--------|--------|
| **TypeScript**   | [tempoxyz/tempo-ts](/sdk/typescript)                            | \< 1 hour         |
| **Rust**         | [tempo-alloy](/sdk/rust)              | \< 1 hour         |
| **Golang**       | [tempo-go](https://github.com/tempoxyz/tempo-go)                                | \< 1 hour         |
| **Python**       | [pytempo](https://github.com/tempoxyz/pytempo)                                | \< 1 hour         |
| **Other Languages** | Reach out to us! The specification is [here](/protocol/transactions/spec-tempo-transaction) and easy to build against.                                                                  | 1-3 days         |

If you are an EVM smart contract developer, see the [Tempo extension for Foundry](/sdk/foundry).

## Properties

<TempoTxProperties />

# Create & Use Accounts

Create and integrate Tempo accounts into your product with domain-bound passkeys or connecting your app to EVM-compatible wallets.

:::tip
**Should I use a Passkey account or a wallet?**

* If you need a **domain-bound account** experience, you can embed a Passkey account.
* If you need a **universal account** experience, you can integrate your app with wallets.

You can even use both if you would like to offer both experiences.
:::

<Cards>
  <Card description="Use domain-bound passkey accounts for an Embedded Account experience" to="/guide/use-accounts/embed-passkeys" icon="lucide:fingerprint" title="Embed Passkey Accounts" />

  <Card description="Connect your app to wallets using MetaMask and others for a Universal Account experience" to="/guide/use-accounts/connect-to-wallets" icon="lucide:wallet" title="Connect to Wallets" />

  <Card description="Add test stablecoins to your account balance using the testnet faucet" to="/quickstart/faucet" icon="lucide:coins" title="Add Test Funds to Your Account" />
</Cards>

# Partners

Tempo is currently in development, with the mainnet launch coming in early 2026. Over the coming weeks, we're bringing online all the core infrastructure needed for stablecoin use cases like [remittances](/learn/use-cases/remittances), [global payouts](/learn/use-cases/global-payouts), [embedded finance](/learn/use-cases/embedded-finance), [tokenized deposits](/learn/use-cases/tokenized-deposits), [microtransactions](/learn/use-cases/microtransactions), and [agentic commerce](/learn/use-cases/agentic-commerce) so that they're available on Day 1 of the mainnet launch.

The Tempo ecosystem is being built with a diverse range of best-in-class partners across stablecoin issuance, wallets & custody, compliance tooling, fraud monitoring, interoperability protocols, analytics & monitoring, orchestration and ramps, and more. We're designing the ecosystem to be global from day one, with issuers across the globe and broad local currency support.

If you're interested in becoming an ecosystem partner, get in touch with us today to ensure you're fully set up for the Tempo mainnet launch coming soon.

If you're looking for local partners to work with on your stablecoin deployment and want to work with one of our ecosystem partners, visit our [ecosystem page](https://tempo.xyz/ecosystem) to see the full list or [get in touch](mailto:partners@tempo.xyz) with us to discuss how you can best integrate with Tempo.

<Cards>
  <Card description="See the full list of all partners including issuers, wallets, orchestration & ramps, compliance tooling, custodians, and more." to="https://tempo.xyz/ecosystem" icon="lucide:external-link" title="Explore Tempo Ecosystem" />

  <Card description="Get in touch with the Tempo team if you'd like to be connected with an ecosystem partner or become one yourself!" to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get In Touch" />
</Cards>

# Stablecoins

Stablecoins let businesses move value globally with faster settlement and more predictable fees than legacy payment rails. Treasury and payments teams use them for cross-border payouts, vendor settlement, and automated liquidity operations that run 24/7.

## What are stablecoins?

Stablecoins are blockchain-based digital assets designed to maintain a stable value. Unlike volatile cryptocurrencies such as Bitcoin or Ether, stablecoins are pegged to established currencies like the US dollar or Euro. Examples of USD-pegged stablecoins include USDC and USDT.

This page focuses on fully reserved, fiat-backed stablecoins. Other models (crypto-collateralized or algorithmic) have different risk profiles.

Real-world utility, increasing regulatory clarity, and growing institutional adoption are driving rapid growth in stablecoin usage. The circulating supply of stablecoins has grown more than tenfold over the past five years, reaching roughly $300 billion today. The US Treasury projects this figure could rise to $3 trillion by 2030.

## How stablecoins work

Fully reserved fiat-backed stablecoins are issued by regulated entities and backed 1:1 with reserves such as cash and short-term government securities held at licensed financial institutions. Stablecoin issuers use a mint-and-burn process to keep the supply aligned with underlying reserves and ensure holders can always redeem stablecoins at face value.

When a user deposits fiat currency with an issuer, the issuer mints the corresponding amount of stablecoins onchain and sends them to the user. When the user redeems stablecoins for fiat, the issuer burns the tokens and sends the equivalent fiat from reserves.

<ZoomableImage src="/learn/stablecoin-mint-burn-process.svg" alt="Mint and burn process for stablecoins" />

Regulatory frameworks such as the EU's MiCA and the US GENIUS Act are establishing disclosure and reserve requirements for issuers. Requirements and enforcement still vary by jurisdiction, so businesses should evaluate each stablecoin and issuer on its own terms.

## Why stablecoins matter for businesses

For financial institutions, corporations, and payment providers, fully reserved fiat-backed stablecoins enable near-instant payments that operate 24/7, work across borders, and bypass friction found in legacy payment rails.

They support established use cases such as [remittances](/learn/use-cases/remittances), [global payouts](/learn/use-cases/global-payouts), and [embedded finance](/learn/use-cases/embedded-finance), while enabling newer applications like [microtransactions](/learn/use-cases/microtransactions) and [agentic commerce](/learn/use-cases/agentic-commerce).

<ZoomableImage src="/learn/stablecoin-use-cases.svg" alt="Stablecoin use cases" />

## Programmable money

Stablecoins open the door to programmable money. Smart contracts can execute payments automatically based on predefined rules, improving efficiency and transparency in payment processing, liquidity management, and reconciliation.

For example, a global enterprise can use a smart contract to automatically top up or sweep subsidiary wallets based on balance thresholds. Routine treasury actions run automatically onchain, replacing custom integrations with multiple banking partners.

On Tempo, stablecoins follow the [TIP-20 token standard](/protocol/tip20/overview), which adds transfer memos, compliance controls, and reward distribution to standard token functionality.

## Stablecoins on Tempo

Tempo is purpose-built for stablecoin payments and issuance. Key resources:

* [TIP-20 token standard](/protocol/tip20/overview): How stablecoins and other tokens behave on Tempo, including transfer memos and compliance policies
* [Native stablecoins](/learn/tempo/native-stablecoins): How Tempo approaches stablecoin design, settlement, and fee payment
* [Stablecoin DEX](/guide/stablecoin-dex): On-chain exchange for stablecoin-to-stablecoin swaps
* [Mint stablecoins](/guide/issuance/mint-stablecoins): Create custom stablecoins with built-in compliance features

## History of stablecoins

Stablecoins emerged as a solution to cryptocurrency's volatility. Tether (USDT), launched in 2014 on the Bitcoin blockchain via the Omni Layer protocol, pioneered the concept of a dollar-pegged digital asset. MakerDAO introduced DAI in 2017, creating the first decentralized, crypto-collateralized stablecoin. Circle and Coinbase followed in 2018 with USD Coin (USDC), emphasizing regulatory compliance and transparent reserves.

The 2020 "DeFi Summer" marked an inflection point. Total stablecoin market capitalization surged from under $10 billion to over $100 billion by 2021, as stablecoins became essential infrastructure for lending protocols, decentralized exchanges, and yield farming.

Regulatory frameworks are now taking shape globally. The EU's Markets in Crypto-Assets (MiCA) regulation established comprehensive stablecoin requirements including reserve mandates and issuer licensing. In the US, the GENIUS Act represents ongoing legislative efforts to create a federal framework for stablecoin issuance and oversight.

## Stablecoin use cases

Stablecoins enable a wide range of payment and financial use cases:

<Cards>
  <Card description="Enable fast, cheap, and predictable cross-border money transfers for individuals and businesses" to="/learn/use-cases/remittances" icon="lucide:send" title="Remittances" />

  <Card description="Deliver instant, low-cost payouts to employees and contractors anywhere in the world" to="/learn/use-cases/global-payouts" icon="lucide:globe" title="Global Payouts" />

  <Card description="Let platforms and marketplaces embed seamless payment flows directly into their applications" to="/learn/use-cases/embedded-finance" icon="lucide:wallet" title="Embedded Finance" />

  <Card description="Move treasury liquidity instantly across borders with real-time visibility into global cash positions" to="/learn/use-cases/tokenized-deposits" icon="lucide:landmark" title="Tokenized Deposits" />

  <Card description="Enable true pay-per-use pricing with sub-cent payments for APIs, content, and IoT services" to="/learn/use-cases/microtransactions" icon="lucide:activity" title="Microtransactions" />

  <Card description="Power autonomous agents with programmable payments for goods, services, and digital resources" to="/learn/use-cases/agentic-commerce" icon="lucide:bot" title="Agentic Commerce" />
</Cards>

## Frequently asked questions

### What is a stablecoin?

A stablecoin is a blockchain-based digital asset designed to maintain a stable value, often pegged 1:1 to a fiat currency such as the US dollar. Stablecoins combine blockchain settlement (24/7 transfers, programmability) with price stability useful for payments and treasury operations.

### Are stablecoins safe?

Safety depends on the stablecoin's backing, redemption model, and issuer disclosures. Widely used USD-pegged stablecoins including USDC and USDT publish reserve reports or attestations. The frequency, detail, and regulatory regime vary by issuer and jurisdiction. Review reserve composition, redemption terms, and disclosure history before use.

### How are stablecoins different from other cryptocurrencies?

Stablecoins target a fixed value (such as 1 USD), while cryptocurrencies like Bitcoin and Ether fluctuate based on market demand. This makes stablecoins practical for payments, settlement, and treasury workflows that require predictable amounts.

### What are stablecoins used for?

Businesses use stablecoins for cross-border payments, vendor settlement, global payouts, and treasury liquidity. Stablecoins settle in minutes and operate 24/7, often with more predictable fees than traditional international wires.

### How do I get stablecoins?

Businesses typically acquire stablecoins through regulated exchanges, direct onboarding with issuers like Circle or Tether, or payment providers that support stablecoin on-ramps. Enterprise teams often use licensed custodians for custody and settlement.

### Are stablecoins regulated?

Regulation varies by jurisdiction and continues to evolve. Some regions have introduced issuer requirements for reserves, disclosures, and licensing (for example, the EU's MiCA framework). Confirm the rules that apply to your entity, counterparties, and operating geographies.

### What is counterparty risk in stablecoins?

Counterparty risk is the risk that a stablecoin issuer cannot redeem tokens 1:1 due to insufficient or illiquid reserves, operational failures, or insolvency. Major issuers such as Circle (USDC) and Tether (USDT) publish reserve disclosures, but these are not real-time views of reserves. Businesses prefer reserves held in cash and short-term government securities.

### What regulatory risks should I consider?

A stablecoin compliant in one jurisdiction may face restrictions elsewhere, and rules can change. Verify issuer licensing and compliance status where you operate, and confirm how custody, reporting, and redemption requirements apply to your use case.

<FAQSchema
  items={[
  {
    question: "What is a stablecoin?",
    answer: "A stablecoin is a blockchain-based digital asset designed to maintain a stable value, often pegged 1:1 to a fiat currency such as the US dollar. Stablecoins combine blockchain settlement (24/7 transfers, programmability) with price stability useful for payments and treasury operations."
  },
  {
    question: "Are stablecoins safe?",
    answer: "Safety depends on the stablecoin's backing, redemption model, and issuer disclosures. Widely used USD-pegged stablecoins including USDC and USDT publish reserve reports or attestations. The frequency, detail, and regulatory regime vary by issuer and jurisdiction."
  },
  {
    question: "How are stablecoins different from other cryptocurrencies?",
    answer: "Stablecoins target a fixed value (such as 1 USD), while cryptocurrencies like Bitcoin and Ether fluctuate based on market demand. This makes stablecoins practical for payments, settlement, and treasury workflows that require predictable amounts."
  },
  {
    question: "What are stablecoins used for?",
    answer: "Businesses use stablecoins for cross-border payments, vendor settlement, global payouts, and treasury liquidity. Stablecoins settle in minutes and operate 24/7, often with more predictable fees than traditional international wires."
  },
  {
    question: "How do I get stablecoins?",
    answer: "Businesses typically acquire stablecoins through regulated exchanges, direct onboarding with issuers like Circle or Tether, or payment providers that support stablecoin on-ramps. Enterprise teams often use licensed custodians for custody and settlement."
  },
  {
    question: "Are stablecoins regulated?",
    answer: "Regulation varies by jurisdiction and continues to evolve. Some regions have introduced issuer requirements for reserves, disclosures, and licensing (for example, the EU's MiCA framework). Confirm the rules that apply to your entity, counterparties, and operating geographies."
  },
  {
    question: "What is counterparty risk in stablecoins?",
    answer: "Counterparty risk is the risk that a stablecoin issuer cannot redeem tokens 1:1 due to insufficient or illiquid reserves, operational failures, or insolvency. Major issuers such as Circle (USDC) and Tether (USDT) publish reserve disclosures, but these are not real-time views of reserves."
  },
  {
    question: "What regulatory risks should I consider?",
    answer: "A stablecoin compliant in one jurisdiction may face restrictions elsewhere, and rules can change. Verify issuer licensing and compliance status where you operate, and confirm how custody, reporting, and redemption requirements apply to your use case."
  }
]}
/>

# Tempo \[The payments-first blockchain]

Tempo is a general-purpose blockchain optimized for payments, built to deliver instant, deterministic settlement, predictably low fees, and a stablecoin-native experience. Tempo's public testnet launched on December 9, 2025, and is now available for anyone to start building on.

Tempo was designed in close collaboration with an exceptional group of [design partners](https://tempo.xyz/ecosystem) who are helping to validate the system against real payment workloads.

The general-purpose programmability of the blockchain provides functionality directly in support of our global payments mission: stablecoin interoperability, onchain FX, compliant privacy, and more. Tempo will be a permissionless, decentralized chain. The Tempo client is open source under the Apache license, and anyone can run a node or sync the chain.

## Core Features

Explore the key features that make Tempo purpose-built for payments:

<Cards>
  <Card description="TIP-20 tokens with payment lanes, stable fees, reconciliation memos, and built-in compliance" to="/learn/tempo/native-stablecoins" icon="lucide:coins" title="Native Stablecoins" />

  <Card description="Batch transactions, fee sponsorship, scheduled payments, and passkey authentication" to="/learn/tempo/modern-transactions" icon="lucide:repeat" title="Modern Transactions" />

  <Card description="High throughput and sub-second finality built on cutting-edge consensus algorithms" to="/learn/tempo/performance" icon="lucide:trending-up" title="Performance Optimizations" />

  <Card description="Access FX liquidity directly onchain with regulated non-USD stablecoin issuers" to="/learn/tempo/fx" icon="lucide:zap" title="Onchain FX" />

  <Card description="Private balances and transfers that maintain compliance requirements for regulated issuers" to="/learn/tempo/privacy" icon="lucide:eye-off" title="Privacy" />
</Cards>

# Exchanging Stablecoins

Tempo features an enshrined decentralized exchange (DEX) designed specifically for trading between stablecoins of the same underlying asset (e.g., USDC to USDT). The exchange provides optimal pricing for cross-stablecoin payments while minimizing chain load from excessive market activity.

The exchange operates as a singleton precompiled contract at address `0xdec0000000000000000000000000000000000000`. It maintains an orderbook with separate queues for each price tick, using price-time priority for order matching.

Trading pairs are determined by each token's quote token. All TIP-20 tokens specify a quote token for trading on the exchange. See [Quote Tokens](/protocol/exchange/quote-tokens) for more information on quote token selection and the optional [pathUSD](/protocol/exchange/quote-tokens#pathusd) stablecoin. See the [Stablecoin DEX Specification](/protocol/exchange/spec) for detailed information on the exchange structure.

The exchange supports three types of orders, each with different execution behavior:

| Order Type | Description |
|------------|-------------|
| [**Limit Orders**](/protocol/exchange/providing-liquidity#limit-orders) | Place orders at specific price levels that wait in the book until matched or cancelled. Orders are added to the book immediately when placed. |
| [**Flip Orders**](/protocol/exchange/providing-liquidity#flip-orders) | Special orders that automatically reverse to the opposite side when completely filled, acting like a perpetual liquidity pool. When a flip order is fully filled, a new order is immediately created on the opposite side. |
| [**Market Orders**](/protocol/exchange/executing-swaps#swap-functions) | Execute immediately against the best available orders in the book (via swap functions). Swaps and cancellations execute immediately within the transaction. |

For the complete execution mechanics, see the [Stablecoin DEX Specification](/protocol/exchange/spec).

To get started with the exchange, explore these guides:

<Cards>
  <Card description="Quote prices and swap between stablecoins" to="/protocol/exchange/executing-swaps" icon="lucide:arrow-left-right" title="Executing Swaps" />

  <Card description="Place orders and flip orders to earn spreads" to="/protocol/exchange/providing-liquidity" icon="lucide:droplet" title="Providing Liquidity" />

  <Card description="Manage token balances on the DEX to save gas costs" to="/protocol/exchange/exchange-balance" icon="lucide:wallet" title="DEX Balance" />
</Cards>

:::info
For a more complete technical specification including design decisions and details of execution semantics, see the [Stablecoin DEX Specification](/protocol/exchange/spec).
:::

# Transaction Fees

Tempo has no native token. Instead, transaction fees—including both gas fees and priority fees—can be paid directly in stablecoins. When you send a transaction, you can choose which supported stablecoin to use for fees.

For a stablecoin to be accepted, it must be USD-denominated, issued as a native TIP-20 contract, and have sufficient liquidity on the native Fee AMM.

Tempo uses a fixed base fee (rather than a variable base fee as in EIP-1559), set so that a TIP-20 transfer costs less than $0.001. All fees accrue to the validator who proposes the block.

## Learn More

<Cards>
  <Card description="Provide liquidity to enable fee token conversions" to="/guide/stablecoin-dex/managing-fee-liquidity" icon="lucide:droplet" title="Managing Fee Liquidity" />

  <Card description="Complete fee system specification" to="/protocol/fees/spec-fee" icon="lucide:file-text" title="Fee Specification" />

  <Card description="Fee AMM protocol specification" to="/protocol/fees/spec-fee-amm" icon="lucide:file-text" title="Fee AMM Specification" />

  <Card description="Sponsor transaction fees" to="/guide/payments/sponsor-user-fees" icon="lucide:shield-check" title="Guide: Sponsor Transaction Fees" />

  <Card description="Pay fees in any supported stablecoin" to="/guide/payments/pay-fees-in-any-stablecoin" icon="lucide:wallet" title="Guide: Pay Fees in Any Supported Stablecoin" />
</Cards>

# Tempo Improvement Proposals (TIPs)

TIPs are design documents that describe changes to the Tempo protocol. Each TIP provides a complete specification that serves as the source of truth for implementation.

***

<TipsList />

# Tempo Transactions

Tempo Transactions are a new [EIP-2718](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2718.md) transaction type, exclusively available on Tempo.

If you're integrating with Tempo, we **strongly recommend** using Tempo Transactions, and not regular Ethereum transactions. Learn more about the benefits below, or follow the guide on issuance [here](/guide/issuance).

<Cards>
  <Card description="Pay transaction fees with any USD-denominated TIP-20 token via automatic Fee AMM conversion." to="#configurable-fee-tokens" icon="lucide:coins" title="Configurable Fee Tokens" />

  <Card description="Sponsor gas fees for users, enabling feeless transaction experiences in your application." to="#fee-sponsorship" icon="lucide:shield-check" title="Fee Sponsorship" />

  <Card description="Batch multiple transactions together for higher throughput and simpler wallet management." to="#batch-calls" icon="lucide:layers" title="Batch Calls" />

  <Card description="Delegate transaction signing capabilities to specific keys with customizable permissions." to="#access-keys" icon="lucide:key" title="Access Keys" />

  <Card description="Execute transactions in parallel using independent nonces for improved throughput." to="#concurrent-transactions" icon="lucide:zap" title="Concurrent Transactions" />

  <Card description="Schedule transactions to execute within a specific time window for automated payments." to="#scheduled-transactions" icon="lucide:clock" title="Scheduled Transactions" />
</Cards>

## Integration Guides

Integrating Tempo Transactions is easy and can be done quickly by a developer in multiple languages. See below for quick links to some of our guides.

|Language|Source|Integration Time|
|--------|--------|--------|
| **TypeScript**   | [tempoxyz/tempo-ts](/sdk/typescript)                            | \< 1 hour         |
| **Rust**         | [tempo-alloy](/sdk/rust)              | \< 1 hour         |
| **Golang**       | [tempo-go](https://github.com/tempoxyz/tempo-go)                                | \< 1 hour         |
| **Python**       | [pytempo](https://github.com/tempoxyz/pytempo)                                | \< 1 hour         |
| **Other Languages** | Reach out to us! The specification is [here](/protocol/transactions/spec-tempo-transaction) and easy to build against.                                                                  | 1-3 days         |

If you are an EVM smart contract developer, see the [Tempo extension for Foundry](/sdk/foundry).

## Properties

<TempoTxProperties />

## Learn more

<Cards>
  <Card description="Native protocol support for new transaction features including WebAuthn/P256 signatures, parallelizable nonces, gas sponsorship, call batching, and scheduled transactions" to="/protocol/transactions/spec-tempo-transaction" icon="lucide:file-code" title="Specification" />

  <Card description="Configure users to pay transaction fees in any supported stablecoin" to="/guide/payments/pay-fees-in-any-stablecoin" icon="lucide:coins" title="Guide: Pay Fees in Any Stablecoin" />

  <Card description="Execute multiple operations atomically" to="/guide/use-accounts/batch-transactions" icon="lucide:layers" title="Guide: Send Batch Transactions" />

  <Card description="Enable gasless transactions with fee payers" to="/guide/payments/sponsor-user-fees" icon="lucide:shield-check" title="Guide: Sponsor Transaction Fees" />

  <Card description="Sign transactions with WebAuthn, P256, or secp256k1 signatures" to="/guide/use-accounts/webauthn-p256-signatures" icon="lucide:fingerprint" title="Guide: Sign Using Passkeys & P256 Keys" />
</Cards>

# Connect to the Network

You can connect with the Tempo Testnet like you would with any other EVM chain.

## Connect using a Browser Wallet

Click on your browser wallet below to automatically connect it to the Tempo Testnet.

<ConnectWallet />

:::warning
Note that on some wallets, you might see an unusually high "balance". This is because, historically, blockchain wallets have always assumed that a blockchain has a "native gas token". On Tempo, there is no native gas token, and so the value shown is a placeholder. See [EVM Differences](/quickstart/evm-compatibility#handling-eth-balance-checks) for more information on this quirk.
:::

## Connect via CLI

To connect via CLI, we recommend using [`cast`](https://getfoundry.sh/cast/overview/), which is a command-line tool for interacting with Ethereum networks. To install cast, you can read more in the [Foundry SDK docs](/sdk/foundry#get-started-with-foundry).

```bash /dev/null/monitor.sh#L1-11
# Check block height (should be steadily increasing)
cast block-number --rpc-url https://rpc.moderato.tempo.xyz
```

## Direct Connection Details

If you're manually connecting to Tempo Testnet, you can use the following details:

| **Property** | **Value** |
|-------------------|-------|
| **Network Name** | Tempo Testnet (Moderato) |
| **Currency** | `USD` |
| **Chain ID** | `42431` |
| **HTTP URL** | `https://rpc.moderato.tempo.xyz` |
| **WebSocket URL** | `wss://rpc.moderato.tempo.xyz` |
| **Block Explorer** | [`https://explore.tempo.xyz`](https://explore.tempo.xyz) |

# Developer Tools

Integrating with Tempo is easy by leveraging services provided by our infrastructure partners. These partners take advantage of Tempo transactions, TIP-20 tokens, and more. Visit their documentation for more information on how to get started.

<Cards>
  <Card description="Query blockchain data with indexers, analytics platforms, and monitoring tools" to="#data--analytics" icon="lucide:bar-chart" title="Data & Analytics" />

  <Card description="View transactions, blocks, accounts, and token activity on Tempo" to="#block-explorers" icon="lucide:search" title="Block Explorers" />

  <Card description="Integrate user-friendly wallet experiences directly into your application" to="#embedded-wallets" icon="lucide:wallet" title="Embedded Wallets" />

  <Card description="Build with account abstraction and programmable smart contract wallets" to="#smart-contract-libraries" icon="lucide:wallet" title="Smart Contract Libraries" />

  <Card description="Connect to Tempo with reliable RPC endpoints and managed node services" to="#node-infrastructure" icon="lucide:server" title="Node Infrastructure" />

  <Card description="Build on Tempo with official SDKs for TypeScript, Go, Foundry, and Rust" to="/sdk" icon="lucide:package" title="Tempo SDKs" />
</Cards>

## Data & Analytics

### Allium

[Allium](https://www.allium.so) is an enterprise blockchain data platform that delivers real-time, analytics-ready datasets through a unified schema across chains. Developers can fetch wallet, token, and price data in milliseconds without managing infrastructure, decoding raw data, or inferring transactions—making it easy to focus on building Tempo applications.

Get access to Tempo data through the [Allium App](https://app.allium.so/join), explore the full API in the [Allium docs](https://docs.allium.so/), and browse real examples of production apps built on Allium [here](https://docs.allium.so/api/developer/overview).

:::tip
Allium has a [ready-to-use recipe](https://github.com/Allium-Science/allium-recipes/tree/main/tempo) for querying Tempo data with SQL.
:::

### Artemis

[Artemis](https://www.artemisanalytics.com/products/terminal) provides a unified analytics terminal for monitoring onchain activity across stablecoins, assets, and networks. Developers use Artemis to analyze flows, liquidity, token performance, and ecosystem-level trends through a clean, queryable interface.

Tempo is already supported within Artemis, with a dedicated analytics page for [Tempo Testnet](https://app.artemisanalytics.com/asset/tempo_moderato).

Artemis also maintains a cross-chain stablecoin dashboard covering major USD-pegged assets across numerous networks. Stablecoins launched on Tempo will appear in the [Stablecoins dashboard](https://app.artemisanalytics.com/stablecoins).

### Chainlink

[Chainlink](https://chain.link) is the industry-standard oracle platform powering the majority of DeFi and bringing capital markets onchain. The Chainlink stack provides the data, interoperability, and security needed for tokenized assets, stablecoins, payments, lending, and other advanced onchain use cases.

Chainlink supports Tempo through:

* **Cross-Chain Interoperability Protocol (CCIP):** A secure interoperability layer for sending messages and value across chains, enabling cross-chain user flows and multi-chain architectures.\
  Explore CCIP in the [Chainlink CCIP docs](https://docs.chain.link/ccip).
* **Data Streams:** Chainlink Data Streams delivers low-latency market data offchain, which can be verified onchain. This pull-based design gives dApps on-demand access to high-frequency market data backed by decentralized, fault-tolerant, and transparent infrastructure—an improvement over traditional push-based oracles that update only at fixed intervals or price thresholds.\
  View the Chainlink Data Stream deployed on Tempo [here](https://explore.tempo.xyz/address/0x72790f9eB82db492a7DDb6d2af22A270Dcc3Db64?tab=contract).

Developers can explore CCIP, Data Streams, and the full Chainlink platform through the [Chainlink Developer Docs](https://docs.chain.link/).

### Goldsky

[Goldsky](https://goldsky.com) makes it easy to access real-time Tempo data with minimal maintenance. Goldsky offers two core products for indexing and streaming onchain data:

* **[Subgraphs](https://docs.goldsky.com/subgraphs/):** A fully backwards-compatible subgraph indexing solution that handles reorgs, RPC failures, and scaling automatically, with improved reliability and performance over traditional subgraph hosts.
* **[Mirror](https://docs.goldsky.com/mirror/):** A simple way to replicate subgraph or chain-level streams directly into your own databases or message queues, powering flexible front-end and back-end data pipelines.

Start indexing Tempo [here](https://goldsky.com/chains/tempo).

### Range

[Range](https://www.range.org) powers the Stablecoin Explorer, which provides a unified view of major stablecoins across 100+ chains. Tempo is fully supported, allowing developers and users to trace stablecoin flows in a way traditional explorers cannot.

Range stands out through:

* **Complete cross-chain visibility**, showing the entire lifecycle of a transfer in one place
* **Enriched context**, including bridge routes, verified entities, and risk signals
* **Built-in compliance checks** via global sanctions lists

Explore Tempo activity in the [Stablecoin Explorer](https://explorer.money/transactions?dn=tempo-testnet\&sc=INTRACHAIN\&sn=tempo-testnet).

## Block Explorers

### Tempo Explorer

Tempo's official block explorer is available at [explore.tempo.xyz](https://explore.tempo.xyz). View transactions, blocks, accounts, and token activity on the Tempo network.

### Tenderly

[Tenderly](https://tenderly.co) delivers full-stack observability, debugging, and simulation tools for Tempo smart contract development and monitoring. With Tenderly you get real-time error tracking, EVM-level tracing, and off-chain transaction simulation — enabling you to catch bugs, analyze reverts, and inspect gas usage before transactions go live.

You can enable Tempo in the [Tenderly Dashboard](https://dashboard.tenderly.co/) to use its tracing, alerts, and debugging tools with no infrastructure to manage.

## Embedded Wallets

### Blockradar

[Blockradar](https://blockradar.co) provides non-custodial wallet infrastructure purpose-built for fintechs running stablecoin payments. The platform focuses on real financial use cases, from merchant settlement to cross-border payouts, with tools designed for payments, compliance, treasury operations, and multi-chain liquidity. Explore the full platform in the [Blockradar Docs](https://docs.blockradar.co/).

**Wallet and Payment Operations:** Through one unified API, teams can issue wallets for users, merchants, or treasury; accept fiat inflows through virtual accounts; enable gasless stablecoin transactions; apply AML checks automatically; consolidate balances through configurable sweeps; and handle cross-chain movement using swap and bridge. Fintechs can start building immediately from our API or [Blockradar Dashboard](https://dashboard.blockradar.co/). For advanced flows or high-volume programs, fintechs can [book a demo](https://www.blockradar.co/contact) to walk through production architectures.

### Crossmint

[Crossmint](https://www.crossmint.com) is an all-in-one platform, with unified APIs for [wallets](https://docs.crossmint.com/wallets/), [stablecoin orchestration](https://docs.crossmint.com/stablecoin-orchestration/), [checkout flows](https://docs.crossmint.com/payments), and [tokenization](https://docs.crossmint.com/minting), giving developers a single interface for everything from payments to asset management on Tempo.

Crossmint delivers a gasless, seed-phrase-free UX backed by bank-grade security and compliance, along with no-code dashboards for managing programs across your team.

Set up a project in the [Crossmint console](https://crossmint.com/console) and explore the [Solution Guide](https://docs.crossmint.com/solutions/overview#fintech) tailored for payment use-cases.

### Dynamic

[Dynamic](https://dynamic.xyz) combines authentication, smart wallets, and key management into a flexible SDK for Tempo developers. Teams can onboard users with familiar login methods and provision Tempo-compatible wallets through Dynamic's secure infrastructure.

Enable Tempo testnet in the [Dynamic dashboard](https://app.dynamic.xyz/dashboard/chains-and-networks), and create an account [here](https://www.dynamic.xyz/get-started) to start integrating Dynamic into your app.

### Para

[Para](https://getpara.com) is a comprehensive wallet and authentication suite for fintech and crypto applications. It provides flexible login methods, secure MPC-backed wallets, fast authentication, and infrastructure for automating onchain activity. Para is adding Tempo chain support so developers can easily build Tempo-enabled wallets and payment flows.

Get started by signing up through the [Para Dev Portal](https://developer.getpara.com/) and following the quickstart in the [Para docs](https://docs.getpara.com/v2/introduction/welcome).

### Privy

[Privy](https://www.privy.io/) builds secure key management and embedded wallets so any developer can easily build secure, scalable wallets into their app. Easily spin up self-custodial wallets for users, manage your treasury wallets and more.

Privy takes advantage of Tempo-native experiences to enable better stablecoin and payments experiences. Easily enable gas sponsorship, leverage webhooks for onchain events, delegated signatures, simple wallet funding, etc.

You can get started now. Simply [create](https://docs.privy.io/wallets/wallets/create/create-a-wallet#param-chain-type-1) an ethereum wallet with Privy and pass in `"caip2": "eip155:42431"` when [making transactions](https://docs.privy.io/wallets/using-wallets/ethereum/send-a-transaction#usage-9).

:::tip
Check out Privy's [example](https://github.com/privy-io/examples/tree/main/examples/privy-next-tempo) peer-to-peer payments app that uses Tempo transaction memos.
:::

### thirdweb

[thirdweb](https://thirdweb.com) provides a full-stack developer platform for building modern onchain applications. Developers can create wallets, deploy tokens, use blockchain-native AI tools, and integrate native internet payments—all with built-in support for Tempo. Access the Tempo Testnet via the [thirdweb dashboard](https://thirdweb.com/tempo-testnet) and explore tooling in the [Thirdweb developer docs](https://portal.thirdweb.com).

Try features live in the [thirdweb Playground](https://playground.thirdweb.com) and create an account by signing up [here](https://thirdweb.com/login).

### Turnkey

[Turnkey](https://www.turnkey.com) provides programmable key management and non-custodial wallet infrastructure for applications that need granular signing policies and automated transaction flows. With Turnkey, developers can securely sign Tempo transactions, automate wallet operations, and build custom logic around how keys are used.

Turnkey also supports sponsor-style workflows, enabling gasless or subsidized transaction flows through configurable signing policies.

[Create your Turnkey account](https://app.turnkey.com/dashboard) and follow the [Turnkey Embedded Wallet Kit guide](https://docs.turnkey.com/sdks/react/getting-started) to integrate embedded wallets into your Tempo app.

:::tip
Turnkey has a [`with-tempo` example](https://github.com/tkhq/sdk/tree/main/examples/with-tempo) in their SDK to get you started quickly.
:::

### Utila

[Utila](https://utila.io) provides secure MPC wallet infrastructure and asset-management tooling for teams building with stablecoins and digital assets. Developers can use Utila to manage Tempo-based payments and treasury operations across multiple wallets and blockchains, all within a single policy-driven platform. Utila's MPC technology reduces counterparty risk, while its configurable approval engine gives teams granular control over how funds are moved.

[Learn more](https://utila.io/product/payments/) about how Utila supports stablecoin operations on Tempo, and [request a demo](https://utila.io/request-a-demo/) if you're interested in secure MPC infrastructure.

## Smart Contract Libraries

### Safe *(coming soon)*

[Safe](https://safe.global) provides a modular smart account framework used across leading Web3 applications and institutions. With Safe, developers can build Tempo applications that take advantage of multi-sig controls, programmable permissions, session keys, and automated transaction policies.

Safe integration for Tempo is coming soon. Stay tuned for updates as support becomes available.

### ZeroDev

[ZeroDev](https://zerodev.app) provides a powerful smart account platform for Tempo, supporting both ERC-4337 and EIP-7702. Developers can onboard users with social logins, enable gas sponsorship, and automate transactions while taking advantage of ZeroDev's chain-abstracted workflows. Its modular wallet stack also allows teams to build customized features such as custom transaction policies and tailored approval logic.

Create a project in the [ZeroDev dashboard](https://dashboard.zerodev.app) and follow the [SDK quickstart](https://docs.zerodev.app/sdk/getting-started/quickstart) to integrate smart accounts into your Tempo application.

## Node Infrastructure

### Alchemy

With [Alchemy](https://alchemy.com), build the fastest and most reliable Tempo applications, powered by industry-leading latency, uptime, and elastic throughput. Alchemy's global RPC infrastructure supports everything from stablecoins to tokenization and large-scale consumer apps.

Sign up through the [Alchemy dashboard](https://dashboard.alchemy.com) and visit the [Alchemy docs](https://www.alchemy.com/docs/node#tldr) to start building.

### Blockdaemon

[Blockdaemon](https://app.blockdaemon.com/) provides institutional-grade node and API infrastructure, along with staking and MPC wallet services. Their globally distributed platform supports enterprise-scale, production workloads with strong reliability and compliance guarantees.

Sign up through the [Blockdaemon Developer Dashboard](https://app.blockdaemon.com/) and deploy a Tempo node by navigating to **Nodes & RPC → Deploy a Node**.

### Chainstack

[Chainstack](https://chainstack.com) provides managed blockchain infrastructure with high-performance, secure RPC nodes. The platform offers reliable Tempo endpoints with built-in monitoring and analytics.

Create an account through the [Chainstack console](https://console.chainstack.com) to deploy Tempo nodes and access RPC endpoints.

### Conduit

[Conduit](https://conduit.xyz) provides high-performance RPC infrastructure for Tempo Testnet. Developers can create API keys and access Tempo Testnet endpoints through the [Conduit app](https://app.conduit.xyz).

View the Tempo Testnet RPC endpoint in the [Conduit Hub](https://hub.conduit.xyz/tempo-testnet) and get started with the [Tempo RPC Quickstart](https://docs.conduit.xyz/rpc-nodes/getting-started/tempo-rpc-quickstart).

### dRPC

[dRPC](https://drpc.org) provides managed Tempo RPC endpoints through NodeCloud, with smart routing, analytics, key control, and front-end protection across 180+ networks. The platform runs on 40 providers in 8 geoclusters, with a free tier and flat-rate plans starting at $10.

Get started by visiting the [Tempo chain page](https://drpc.org/chainlist/tempo-testnet-rpc), and learn more about NodeCloud on the [dRPC NodeCloud page](https://drpc.org/nodecloud-multichain-rpc-management).

### Quicknode

[Quicknode](https://quicknode.com) is the enterprise-grade development platform for building, scaling, and launching onchain applications with speed and reliability. Their globally optimized RPC network makes it easy to run high-performance Tempo workloads from day one.

Get started on the [Tempo Chain Page](https://www.quicknode.com/chains/tempo) and follow the [QuickStart guide](https://www.quicknode.com/docs/tempo) to create your Tempo RPC endpoint.

## Security & Compliance

### Blockaid

[Blockaid](https://blockaid.io) provides real-time security infrastructure for Web3 applications. Its transaction scanning and threat detection systems identify malicious activity before users sign transactions, improving safety across wallets and interfaces.

Learn how Blockaid's transaction scanning improves security by visiting their [overview page](https://www.blockaid.io/transaction-security), and reach out to their team [here](https://www.blockaid.io/contact) to get started.

### Chainalysis

[Chainalysis](https://www.chainalysis.com) delivers industry-leading onchain intelligence, compliance, and security infrastructure. Through Hexagate, Chainalysis supports Tempo with real-time monitoring, anomaly detection, and threat insights to help developers and platforms better understand and manage onchain risk as the ecosystem grows.

Discover how Hexagate supports Tempo [here](https://www.hexagate.com), or request a dedicated walkthrough from the Chainalysis team through their [demo form](https://www.hexagate.com/request-demo).

## Issuance

### Brale

[Brale](https://brale.xyz) provides infrastructure for issuing, transferring, and managing stablecoins across chains. Developers can create new stablecoins or work with existing issued assets using Brale's APIs to support on- and off-ramps, payouts, and cross-ecosystem stablecoin movement.

Brale exposes two complementary APIs:

* **[Stablecoin Movement & Account Management](https://docs.brale.xyz/#stablecoin-movement--account-management-apibralexyz):**\
  An authenticated API for orchestrating stablecoin workflows, including issuance, transfers across accounts or chains, custody management, and integration with financial institutions.

* **[Stablecoin Market Data](https://docs.brale.xyz/#stablecoin-market-data-databralexyz):**\
  A public, read-only API that provides token metadata, stablecoin definitions, and price feeds.

These APIs support common stablecoin workflows such as minting, redemption, swaps, payouts, and treasury operations, making Brale suitable for fintechs, exchanges, and payment platforms building on Tempo.

Get started by creating an account [here](https://app.brale.xyz/buy/signup/).

# EVM Differences

Tempo is fully compatible with the Ethereum Virtual Machine (EVM), targeting the **Osaka** EVM hard fork. Developers can deploy and interact with smart contracts using the same tools, languages, and frameworks they use on Ethereum, such as Solidity, Foundry, and Hardhat. All Ethereum JSON-RPC methods work out of the box.

While the execution environment mirrors Ethereum's, Tempo introduces some differences optimized for payments, described below.

<Cards>
  <Card description="How Tempo handles wallet compatibility and native token representation." to="#wallet-differences" icon="lucide:wallet" title="Wallet Differences" />

  <Card description="Key differences when sending transactions, including fee tokens and default preferences." to="#transaction-differences" icon="lucide:send" title="Transaction Differences" />

  <Card description="VM-level differences including balance opcodes and Solidity compatibility." to="#vm-layer-differences" icon="lucide:code" title="VM Layer Differences" />

  <Card description="How Tempo's consensus and finality differ from Ethereum's approach." to="#consensus--finality" icon="lucide:check-circle" title="Consensus & Finality" />
</Cards>

## Wallet Differences

By default, all existing functionality will work for EVM-compatible wallets, with only a few quirks. For developers of wallets, we strongly encourage you to implement support for Tempo Transactions over regular EVM transactions. See the [transaction differences](#transaction-differences) for more.

:::tip
If you are building a wallet, read our [guide for wallet developers](/quickstart/wallet-developers).
:::

### Handling ETH (native token) Balance Checks

Remember that on Tempo, there is no native gas token.

Many wallets and applications check a user's "native account balance" before letting them complete some action. In this scenario, you might see an error message like "Insufficient balance".

This stems from the return value of the `eth_getBalance` RPC method. When a wallet calls this method, it expects a hex string representing the "native token balance", hard-coded to be represented as an 18-decimal place number.

On Tempo, the `eth_getBalance` method returns a hex string representing an extremely large number. Specifically it returns: `0x9612084f0316e0ebd5182f398e5195a51b5ca47667d4c9b26c9b26c9b26c9b2` which is represented in decimals as 4.242424242424242e+75.

Our recommendation to wallets and to applications using this method is to remove this balance check, and to not represent any "native balance" in your user's UI. This will allow users to complete actions without being blocked by balance checks.

We endorse [this proposed ERC](https://github.com/ethereum/ERCs/pull/1220) to standardize this behavior.

### Specifying a Native Token Currency Symbol

Sometimes wallets will need to specify the currency symbol for the native token. On Tempo, there is no native token, but fees are denominated in USD. So, we recommend using the currency symbol "USD".

## Transaction Differences

### Dealing with the fee token selection

Tempo does not have a native gas token. Instead, fees are denominated in USD and fees can be paid in an stablecoin. For Tempo Transactions, the `fee_token` field can be set to any TIP-20 token, and fees are paid in that token.

If your transactions are not using Tempo Transactions, there is a cascading fee token selection algorithm that determines the default fee token based on the user's preferences and the contract being called.

This preference system is specified [here](/protocol/fees/spec-fee#fee-token-preferences) in detail.

#### Consideration 1: Setting a user default fee token

As specified in the preference system above, the simplest way to specify the fee token for a user is to set the user default fee token. Read about how to do that [here](/protocol/fees/spec-fee#account-level) on behalf of an account.

#### Consideration 2: Paying fees in the TIP-20 contract being interacted with

If the user is calling a method on a TIP-20 token (e.g., `transfer`), the default fee token is that token itself. For example, if the user is calling the `transfer` method on a TIP-20 token with a symbol of "USDC", the default fee token would be "USDC".

Importantly, note that the `amount` field in this case is sent in full. So, if the user is calling the `transfer` method on a TIP-20 token with a symbol of "USDC" with the `amount` field set to 1000, the full amount of the token will be transferred **and** the sender's balance will be reduced by the amount spent in fees. So, the recipient will receive 1000 USDC.

#### Consideration 3: The fallback in the case of a non-TIP-20 contract

If the user is calling a contract that is not a TIP-20 token, the EVM transaction will default to the pathUSD token. Thus, in order to send transactions to non-TIP-20 contracts, the wallet must hold some balance of pathUSD.

On the Tempo Testnet, pathUSD is available from the [faucet](/quickstart/faucet).

If a wallet wants to submit a non-TIP20 transaction without having to submit the above transaction, we recommend investing in using [Tempo Transactions](/quickstart/integrate-tempo#tempo-transactions) instead.

## VM Layer Differences

At the VM layer, all opcodes are supported out of the box. Due to the lack of a native token, native token balance is always returning zero balances.

### State Creation Costs

Tempo uses higher gas costs for state-creating operations to prevent state growth attacks ([TIP-1000](/protocol/tips/tip-1000)):

| Operation | Tempo | Ethereum |
|-----------|-------|----------|
| New storage slot (SSTORE 0→non-zero) | 250,000 gas | 20,000 gas |
| Account creation | 250,000 gas | 0 gas |
| Contract creation per byte | 1,000 gas | 200 gas |
| Transaction gas cap | 30M gas | 30M gas |

This means transfers to new addresses cost ~300k gas, and contract deployments cost 5-10x more than on Ethereum. Update your `gas_limit` estimates accordingly.

### Balance Opcodes and RPC Methods

| Feature | Behavior on Tempo | Alternatives |
|---------|-------------------|--------------|
| **`BALANCE` and `SELFBALANCE`** | Will always return 0 | Use TIP-20 `balanceOf` instead |
| **`CALLVALUE`** | Will always return 0 | There is no alternative |

:::info
We are exploring transaction level introspection for Tempo Transactions, with an ability to declare things like `tx.fee_token` and `tx.fee_payer` in Solidity.
:::

## Consensus & Finality

Tempo uses **Simplex BFT consensus** with a permissioned validator set at launch, providing deterministic finality, unlike Ethereum's finality gadget which takes approximately 12 minutes.

Block times are targeted at ~0.5 seconds compared to Ethereum's ~12 second slots.

# Faucet

Get test stablecoins on Tempo testnet.

<Tabs>
  <Tab title="Fund your wallet">
    <div className="h-4" />

    Connect your wallet to receive test stablecoins directly.

    <div className="h-6" />

    <Demo.Container name="Connect and fund your wallet" footerVariant="balances" tokens={[Token.pathUsd, Token.alphaUsd, Token.betaUsd, Token.thetaUsd]} balanceSource="wallet">
      <Step.ConnectWallet stepNumber={1} />

      <Step.AddFundsToWallet stepNumber={2} />

      <Step.AddTokensToWallet stepNumber={3} />

      <Step.SetFeeToken stepNumber={4} last />
    </Demo.Container>
  </Tab>

  <Tab title="Fund an address">
    <div className="h-4" />

    Send test stablecoins to any address.

    <div className="h-6" />

    <Demo.Container name="Fund an address">
      <Step.AddFundsToOthers stepNumber={1} last />
    </Demo.Container>
  </Tab>

  <Tab title="cURL request">
    <div className="h-4" />

    Request tokens programmatically via the faucet API.

    <div className="h-4" />

    ```bash
    curl -X POST https://docs.tempo.xyz/api/faucet \
      -H "Content-Type: application/json" \
      -d '{"address": "<YOUR_ADDRESS>"}'
    ```

    <div className="h-4" />

    Replace `<YOUR_ADDRESS>` with a lowercase wallet address.
  </Tab>

  <Tab title="Cast RPC">
    <div className="h-4" />

    Request tokens using the `tempo_fundAddress` RPC method.

    <div className="h-4" />

    ```bash
    cast rpc tempo_fundAddress <YOUR_ADDRESS> \
      --rpc-url https://rpc.moderato.tempo.xyz
    ```

    <div className="h-4" />

    Replace `<YOUR_ADDRESS>` with your wallet address.
  </Tab>
</Tabs>

The faucet funds the following assets.

| Asset | Address |Amount|
|-------|---------|----:|
| [pathUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000000) | `0x20c0000000000000000000000000000000000000` | `1M` |
| [AlphaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000001) | `0x20c0000000000000000000000000000000000001` | `1M` |
| [BetaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000002) | `0x20c0000000000000000000000000000000000002` | `1M` |
| [ThetaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000003)   | `0x20c0000000000000000000000000000000000003` | `1M` |

# Integrate Tempo Testnet

Tempo is fully compatible with the Ethereum Virtual Machine (EVM), targeting the **Osaka** EVM hard fork. So, everything you'd expect to work with Ethereum works on Tempo, with only a few exceptions which we detail on the [EVM Differences](/quickstart/evm-compatibility) page.

<Cards>
  <Card icon="lucide:network" title="Connect to the Network" description="Learn how to connect to the Tempo Testnet with your wallet or programmatically." to="/quickstart/connection-details" />

  <Card icon="lucide:plug" title="Explore Testnet Integrations" description="Integrate right away with the developer products you're already familiar with." to="/quickstart/developer-tools" />

  <Card icon="lucide:wallet" title="Wallet Developers" description="Support Tempo in your wallet and deliver an enhanced experience for your users." to="/quickstart/wallet-developers" />
</Cards>

## Start Building

The guides below will help you get a sense for what is possible to do with Tempo. All of the guides below are fully-featured Tempo applications themselves, built with the [Tempo SDKs](/sdk).

<Cards>
  <Card icon="lucide:wallet" title="Create & Use Accounts" description="Create and integrate Tempo accounts with domain-bound passkeys or EVM-compatible wallets" to="/guide/use-accounts" />

  <Card icon="lucide:send" title="Make Payments" description="Send and receive stablecoin payments with flexible fee options and sponsorship capabilities" to="/guide/payments" />

  <Card icon="lucide:coins" title="Issue Stablecoins" description="Create and manage your own stablecoin with built-in compliance features" to="/guide/issuance" />

  <Card icon="lucide:arrow-left-right" title="Exchange Stablecoins" description="Trade between stablecoins on Tempo's enshrined decentralized exchange" to="/guide/stablecoin-dex" />
</Cards>

## Go Deeper

The Tempo source code is fully open-source and available on [GitHub](https://github.com/tempoxyz).

If you're interested in learning more about how Tempo works under the hood, feel free to explore the codebase directly, run a node for yourself, or refer to the protocol specifications for a deeper understanding.

<Cards>
  <Card icon="lucide:server" title="Run a Tempo Node" description="System requirements, installation and usage instructions for running a Tempo node." to="/guide/node" />

  <Card icon="lucide:book-open" title="Protocol Specifications" description="Technical specifications for tokens, fees, transactions, and protocol components." to="/protocol" />
</Cards>

We welcome contributions from the community to help improve and expand the project.

# Predeployed Contracts

## System Contracts

Core protocol contracts that power Tempo's features.

| Contract | Address | Description |
|----------|---------|-------------|
| [**TIP-20 Factory**](/protocol/tip20/overview) | `0x20fc000000000000000000000000000000000000` | Create new TIP-20 tokens |
| [**Fee Manager**](/protocol/fees/spec-fee-amm#2-feemanager-contract) | `0xfeec000000000000000000000000000000000000` | Handle fee payments and conversions |
| [**Stablecoin DEX**](/protocol/exchange) | `0xdec0000000000000000000000000000000000000` | Enshrined DEX for stablecoin swaps |
| [**TIP-403 Registry**](/protocol/tip403/spec) | `0x403c000000000000000000000000000000000000` | Transfer policy registry |
| [**pathUSD**](/protocol/exchange/quote-tokens#pathusd) | `0x20c0000000000000000000000000000000000000` | First stablecoin deployed |

## Standard Utilities

Popular Ethereum contracts deployed for convenience.

| Contract | Address | Description |
|----------|---------|-------------|
| [**Multicall3**](https://www.multicall3.com/) | `0xcA11bde05977b3631167028862bE2a173976CA11` | Batch multiple calls in one transaction |
| [**CreateX**](https://github.com/pcaversaccio/createx) | `0xba5Ed099633D3B313e4D5F7bdc1305d3c28ba5Ed` | Deterministic contract deployment |
| [**Permit2**](https://docs.uniswap.org/contracts/permit2/overview) | `0x000000000022d473030f116ddee9f6b43ac78ba3` | Token approvals and transfers |
| [**Arachnid Create2 Factory**](https://github.com/Arachnid/deterministic-deployment-proxy) | `0x4e59b44847b379578588920cA78FbF26c0B4956C` | CREATE2 deployment proxy |
| [**Safe Deployer**](https://github.com/safe-fndn/safe-singleton-factory) | `0x914d7Fec6aaC8cd542e72Bca78B30650d45643d7` | Safe deployer contract |

## Contract ABIs

ABIs for these contracts are available in the SDK:

```typescript
import { Abis } from 'viem/tempo'

const tip20Abi = Abis.tip20
const tip20FactoryAbi = Abis.tip20Factory
const stablecoinDexAbi = Abis.stablecoinDex
const feeManagerAbi = Abis.feeManager
const feeAmmAbi = Abis.feeAmm
// ...
```

import { TokenListDemo } from '../../components/TokenList.tsx'

# Tempo Token List Registry

A [Uniswap Token Lists](https://tokenlists.org)-compatible API for token metadata and icons on Tempo.

As an example, here's Tempo Testnet's tokenlist, fetched from [tokenlist.tempo.xyz/list/42431](https://tokenlist.tempo.xyz/list/42431):

<TokenListDemo />

## Endpoints

| Endpoint | Description |
|----------|-------------|
[`/list/{chain_id}`](https://tokenlist.tempo.xyz/list/42431) | Token list for a chain |
[`/asset/{chain_id}/{id}`](https://tokenlist.tempo.xyz/asset/42431/pathUSD) | Get a single token by symbol or address​
[`/icon/{chain_id}`](https://tokenlist.tempo.xyz/icon/42431) | Chain icon (SVG) |
[`/icon/{chain_id}/{address}`](https://tokenlist.tempo.xyz/icon/42431/0x20c0000000000000000000000000000000000000) | Token icon (SVG) |

## Adding a New Token

1. **Fork** [tempoxyz/tempo-apps](https://github.com/tempoxyz/tempo-apps)

2. **Add token** to `data/<chain_id>/tokenlist.json` in `apps/tokenlist`:

   ```json
   {
     "name": "piUSD",
     "symbol": "PiUSD",
     "decimals": 6,
     "chainId": 42431,
     "address": "0x..."
   }
   ```

3. **Add icon** to `data/<chain_id>/icons/<address>.svg` (lowercase address) in `apps/tokenlist`

4. **Submit PR** with as much information as you think is helpful for review.

### Icon Requirements

* Format: SVG
* Address filename must be lowercase (e.g., `0xabcd...1234.svg`)
* Recommended: square aspect ratio, minimal whitespace 1Code has comments. Press enter to view.

<Callout type="info">
  A token that gets added to the tokenlist will atuomatically reflect in the Explorer in the next deployment.
</Callout>

[Full OpenAPI Spec →](https://tokenlist.tempo.xyz/docs)

# Contract Verification

Verify your smart contracts on Tempo using [contracts.tempo.xyz](https://contracts.tempo.xyz), a Sourcify-compatible contract verification service. Verified contracts display source code and ABI in the [Tempo Explorer](https://explore.tempo.xyz), making it easier for users to interact with your contracts.

## Verify with Foundry

The easiest way to verify contracts is to include the `--verify` flag when deploying. You can specify Tempo's verifier by either setting the `VERIFIER_URL` environment variable:

```bash
export VERIFIER_URL=https://contracts.tempo.xyz
```

Or by passing `--verifier-url https://contracts.tempo.xyz` directly to the command.

The chain ID is auto-detected from the RPC URL, but you can specify it explicitly with `--chain <CHAIN_ID>` if needed.

### Verify during deployment

Deploy and verify in a single command:

```bash
# Deploy and verify with forge create
forge create src/Token.sol:Token \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --broadcast \
  --verify

# Deploy and verify with forge script
forge script script/Deploy.s.sol \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --sender <YOUR_WALLET_ADDRESS> \
  --broadcast \
  --verify
```

### Verify an existing contract

To verify a contract that's already deployed, use `forge verify-contract`:

```bash
forge verify-contract \
  --verifier-url https://contracts.tempo.xyz \
  <CONTRACT_ADDRESS> \
  src/MyContract.sol:MyContract
```

Replace `<CONTRACT_ADDRESS>` with your deployed contract address and `src/MyContract.sol:MyContract` with the path and name of your contract.

:::tip
Make sure you're using the same compiler settings (optimizer, EVM version) that you used when deploying the contract.
:::

### Retry options

If verification fails intermittently, use `--retries` and `--delay` to automatically retry:

```bash
forge create src/Token.sol:Token \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --broadcast \
  --verify \
  --retries 10 \
  --delay 10
```

This retries verification up to 10 times with a 10-second delay between attempts.

For more details on deployment and verification options, see the [Foundry documentation](https://getfoundry.sh/forge/deploying).

## Verify with Hardhat

If you deployed with Hardhat, add Sourcify verification to your `hardhat.config.ts` using [`@nomicfoundation/hardhat-verify`](https://hardhat.org/hardhat-runner/plugins/nomicfoundation-hardhat-verify):

```ts
import "@nomicfoundation/hardhat-verify";

const config: HardhatUserConfig = {
  // ... your existing config
  sourcify: {
    enabled: true,
    apiUrl: "https://contracts.tempo.xyz",
    browserUrl: "https://explore.tempo.xyz",
  },
};
```

Then verify:

```bash
npx hardhat verify --network tempo <CONTRACT_ADDRESS> [constructor args...]
```

### Verify from deployment artifacts

If you have Hardhat deployment JSON files (from `hardhat-deploy` or `hardhat-ignition`) but no longer have the project set up, you can still verify. These files contain embedded compiler metadata with full source code (when compiled with `useLiteralContent: true`, the default for `hardhat-deploy`).

Extract the `metadata` field, parse it as JSON, then construct a [verification API request](#verify-with-the-api) using:

* `metadata.sources` → `stdJsonInput.sources`
* `metadata.settings` (optimizer, evmVersion, remappings) → `stdJsonInput.settings`
* `metadata.compiler.version` → `compilerVersion`
* `metadata.settings.compilationTarget` → `contractIdentifier` (format: `path/to/File.sol:ContractName`)

## Proxy Contracts

OpenZeppelin proxy deployments (e.g., `TransparentUpgradeableProxy`) create multiple contracts — typically an implementation, a proxy, and a `ProxyAdmin`. Each must be verified **separately** and may use **different compiler versions** (e.g., your contract uses `solc 0.8.22` while the OZ proxy uses `solc 0.8.10`).

If you have the deployment artifact for each contract, the correct compiler version and settings are already embedded in each file's metadata.

## Verify with the API

You can also verify contracts directly using the REST API. Verification is asynchronous—you submit a request, then poll for the result.

### Submit for Verification

```bash
curl -X POST https://contracts.tempo.xyz/v2/verify/42431/<CONTRACT_ADDRESS> \
  -H 'Content-Type: application/json' \
  -d '{
    "stdJsonInput": {
      "language": "Solidity",
      "sources": {
        "src/MyContract.sol": {
          "content": "// SPDX-License-Identifier: MIT\npragma solidity ^0.8.20;\n\ncontract MyContract { }"
        }
      },
      "settings": {
        "optimizer": { "enabled": false, "runs": 200 },
        "evmVersion": "cancun"
      }
    },
    "compilerVersion": "0.8.20+commit.a1b79de6",
    "contractIdentifier": "src/MyContract.sol:MyContract"
  }'
```

The API returns `202 Accepted` with a verification ID:

```json
{
  "verificationId": "550e8400-e29b-41d4-a716-446655440000"
}
```

:::tip
If verification has trouble determining the creation bytecode, include `creationTransactionHash` in the request body.
:::

### Check Verification Status

Poll the status endpoint until verification completes:

```bash
curl https://contracts.tempo.xyz/v2/verify/<VERIFICATION_ID>
```

The endpoint returns `200` for completed jobs, but you must check the response body to determine success or failure:

```json
{
  "isJobCompleted": true,
  "contract": {
    "match": "exact_match",
    "chainId": "42431",
    "address": "0x1234567890abcdef1234567890abcdef12345678",
    "name": "MyContract"
  }
}
```

The `match` field can be `exact_match` (bytecode and metadata match), `match` (bytecode matches but metadata differs), or `null` (verification failed).

### Retrieve Verified Contract

Once verified, retrieve the contract details:

```bash
curl https://contracts.tempo.xyz/v2/contract/42431/<CONTRACT_ADDRESS>
```

Add `?fields=all` to get full compilation artifacts including ABI, source files, and bytecode.

## Vyper Support

The verification service supports Vyper contracts. Use `"language": "Vyper"` in the `stdJsonInput`:

```bash
curl -X POST https://contracts.tempo.xyz/v2/verify/42431/<CONTRACT_ADDRESS> \
  -H 'Content-Type: application/json' \
  -d '{
    "stdJsonInput": {
      "language": "Vyper",
      "sources": {
        "contracts/Token.vy": {
          "content": "# @version ^0.3.10\n..."
        }
      },
      "settings": {}
    },
    "compilerVersion": "0.3.10+commit.91361694",
    "contractIdentifier": "contracts/Token.vy:Token"
  }'
```

## API Reference

| Endpoint | Description |
|----------|-------------|
| `POST /v2/verify/{chainId}/{address}` | Submit contract for verification |
| `GET /v2/verify/{verificationId}` | Check verification status |
| `GET /v2/contract/{chainId}/{address}` | Get verified contract details |
| `GET /v2/contracts/{chainId}` | List all verified contracts |
| `GET /chains` | Get supported chains |

View the full API documentation at [contracts.tempo.xyz/docs](https://contracts.tempo.xyz/docs).

## Supported Chains

| Network | Chain ID |
|---------|----------|
| Tempo Mainnet | `4217` |
| Tempo Testnet (Moderato) | `42431` |
| Tempo Devnet | `31318` |

## Troubleshooting

:::tip
If you encounter unexpected failures, you might be running an older version of Foundry/Forge, or you might not be running Tempo's Foundry fork. See the [Foundry setup guide](/sdk/foundry/index.mdx) for installation instructions.
:::

### Verification Failed

If verification fails, check the following:

* **Compiler version**: Use the full version string with commit hash (e.g., `0.8.20+commit.a1b79de6`)
* **Optimizer settings**: Optimizer enabled/disabled and runs must match deployment settings
* **EVM version**: Must match the EVM version used during deployment
* **Source files**: All imported files must be included in the `sources` object
* **Contract identifier**: Must match the format `path/to/Contract.sol:ContractName`

### Common Errors

| Error | Cause |
|-------|-------|
| `contract_not_found` | No bytecode exists at the address |
| `compilation_error` | Source code has syntax errors |
| `compilation_failed` | Compilation service returned an error |
| `contract_not_found_in_output` | Contract identifier not found in compiled output |
| `no_match` | Compiled bytecode doesn't match on-chain code |

# Wallet Integration Guide

Because there is [no native token on Tempo](/quickstart/evm-compatibility#handling-eth-native-token-balance-checks) and transaction fees are paid directly in stablecoins, wallets need specific UI and logic adjustments to support the network. Follow this guide if your wallet logic and/or interfaces are dependent on the existence of a native token.

As part of supporting Tempo in your wallet, you can also deliver an enhanced experience for your users by integrating [Tempo Transactions](/guide/tempo-transaction). Common use cases include enabling a gasless transactions for your users, letting your users decide what token to use for fees, and more.

## Steps

::::steps

### Handle the absence of a native token

If you use `eth_getBalance` to validate a user's balance, you should instead check the user's account fee token balance on Tempo. Additionally, you should not display any "native balance" in your UI for Tempo users.

:::info
In testnet, `eth_getBalance` [returns a large placeholder value](/quickstart/evm-compatibility#handling-eth-native-token-balance-checks) for the native token balance to unblock existing assumptions wallets have about the native token balance.
:::

:::code-group

```ts twoslash [example.ts]
// @noErrors
import { client } from './viem.config'

const userFeeToken = await client.fee.getUserToken({ 
  account: '0x...' 
})

const balance = await client.token.getBalance({ 
  account: '0x...',
  token: userFeeToken.address 
})
```

```ts twoslash [viem.config.ts] filename="viem.config.ts"
// [!include ~/snippets/viem.config.ts:setup]
```

:::

### Configure native currency symbol

If you need to display a native token symbol, such as showing how much gas a transaction requires, you can set the currency symbol to `USD` for Tempo as fees are denominated in USD.

### Use fee token preferences to quote gas prices

On Tempo, users can pay fees in any supported stablecoin. You should quote gas/fee prices in your UI based on a transaction's fee token.

:::info
As a wallet developer, you can set the fee token for your user at the account level.

If you don't, Tempo uses a cascading fee token selection algorithm to determine the fee token for a transaction – learn more about [Fee Token Preferences](/protocol/fees/spec-fee#fee-token-preferences).
:::

### Display token and network assets

Tempo provides a public tokenlist service that hosts token and network assets. You can pull these assets from our public tokenlist service to display in your UI.

* **GitHub**: [tempoxyz/tempo-apps/apps/tokenlist](https://github.com/tempoxyz/tempo-apps/tree/main/apps/tokenlist)
* **Tokenlist JSON**: [tempoxyz.github.io/tempo-apps/42431/tokenlist.json](https://tempoxyz.github.io/tempo-apps/42431/tokenlist.json)

### Integrate Tempo Transactions

We strongly recommend using [Tempo Transactions](/guide/tempo-transaction) if you control transaction submission. We have [SDKs and guides](/guide/tempo-transaction#integration-guides) available to get you integrated in less than an hour!

:::tip
Use Tempo Transactions to

* Set the fee token used for your users' transactions ([guide](/guide/payments/pay-fees-in-any-stablecoin))
* Sponsor transaction fees for your users ([guide](/guide/payments/sponsor-user-fees))
* Send concurrent transactions with independent nonces ([guide](/guide/payments/send-parallel-transactions))

  :::
  ::::

## Recipes

### Get user's fee token

Retrieve the user's configured fee token preference:

```ts
import { getUserToken } from 'viem/tempo'

const feeToken = await client.fee.getUserToken({ 
  account: userAddress 
})
```

See [`getUserToken`](https://viem.sh/tempo/actions/fee.getUserToken) for full documentation.

### Get token balance

Check a user's balance for a specific token:

```ts
import { getBalance } from 'viem/tempo'

const balance = await client.token.getBalance({ 
  account: userAddress,
  token: tokenAddress 
})
```

See [`getBalance`](https://viem.sh/tempo/actions/token.getBalance) for full documentation.

### Set user fee token

Set the user's default fee token preference. This will be used for all transactions unless a different fee token is specified at the transaction level.

```ts
import { setUserToken } from 'viem/tempo'

await client.fee.setUserTokenSync({ 
  token: '0x20c0000000000000000000000000000000000001', 
})
```

See [`setUserToken`](https://viem.sh/tempo/actions/fee.setUserToken) for full documentation.

## Checklist

Before launching Tempo support, ensure your wallet:

* \[ ] Checks fee token balance instead of native balance
* \[ ] Hides or removes native balance display for Tempo
* \[ ] Displays `USD` as the currency symbol for gas
* \[ ] Quotes gas prices in the user's fee token
* \[ ] Pulls token/network assets from Tempo's tokenlist
* \[ ] (Recommended) Integrates Tempo Transactions for enhanced UX

## Learning Resources

<Cards>
  <Card description="Learn how fee token preferences work in the protocol" icon="lucide:file-text" title="Fee Token Preferences" to="/protocol/fees/spec-fee#fee-token-preferences" />

  <Card description="Integrate Tempo Transactions for full control over transaction parameters" icon="lucide:coins" title="Tempo Transactions" to="/guide/tempo-transaction" />

  <Card description="Sponsor user fees to enable feeless transaction experiences in your application" icon="lucide:shield-check" title="Sponsor User Fees" to="/guide/payments/sponsor-user-fees" />

  <Card description="Pay fees in any supported stablecoin" icon="lucide:wallet" title="Pay Fees in Any Stablecoin" to="/guide/payments/pay-fees-in-any-stablecoin" />
</Cards>

# Foundry for Tempo

Tempo builds on top of [Foundry](https://github.com/foundry-rs/foundry): the leading Ethereum development toolkit, through a custom fork that adds first-class support for Tempo.

This fork extends Foundry with Tempo's [protocol-level features](/protocol/), enabling developers to build, test, and deploy contracts that go [beyond the limits of standard EVM chains](/quickstart/evm-compatibility).

For general information about Foundry, see the [Foundry documentation](https://getfoundry.sh/).

## Get started with Foundry

### Install using `foundryup`

Tempo's Foundry fork is installed through the standard upstream `foundryup` using the `-n tempo` flag, no separate installer is required.

Getting started is very easy:

Install regular `foundryup`:

```bash
curl -L https://foundry.paradigm.xyz | bash
```

Or if you already have `foundryup` installed:

```bash
foundryup --update
```

Next, run:

```bash
foundryup -n tempo
```

It will automatically install the latest `nightly` release of all precompiled binaries: [`forge`](https://getfoundry.sh/forge/overview#forge), [`cast`](https://getfoundry.sh/cast/overview#cast), [`anvil`](https://getfoundry.sh/anvil/overview#anvil), and [`chisel`](https://getfoundry.sh/chisel/overview#chisel).

To install a specific version, replace `<TAG_NAME>` with the desired release tag:

```bash
foundryup -n tempo -i <TAG_NAME>
```

### Verify Installation

```bash
forge -V
```

You should see version information include `-tempo`, indicating you are using the Tempo fork.

```bash
# forge <version>-tempo (<commit> <timestamp>)
```

### Create a new Foundry project

Initialize a new project with Tempo support:

```bash
forge init -n tempo my-project && cd my-project
```

Each new project is configured for Tempo out of the box, with [`tempo-std`](https://github.com/tempoxyz/tempo-std), the Tempo standard library installed, containing helpers for Tempo's protocol-level features.

## Use Foundry for your workflows

All standard Foundry commands are supported out of the box.

### Test & deploy with `forge` locally

```bash
# Build your contracts
forge build

# Run all tests locally
forge test

# Run deployment scripts locally
forge script script/Mail.s.sol
```

### Test & deploy with `forge` on Tempo Testnet

```bash
# Set environment variables
export TEMPO_RPC_URL=https://rpc.moderato.tempo.xyz
export VERIFIER_URL=https://contracts.tempo.xyz

# Optional: create a new keypair and request some testnet tokens from the faucet.
cast wallet new
cast rpc tempo_fundAddress <YOUR_WALLET_ADDRESS> --rpc-url $TEMPO_RPC_URL

# Run all tests on Tempo's testnet
forge test

# Deploy and verify a simple contract
forge create src/Mail.sol:Mail \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --broadcast \
  --verify \
  --constructor-args 0x20c0000000000000000000000000000000000001

# Deploy a simple contract with custom fee token
forge create src/Mail.sol:Mail \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --broadcast \
  --verify \
  --constructor-args 0x20c0000000000000000000000000000000000001

# Set a salt for deterministic contract address derivation
# The salt is passed to TIP20_FACTORY.createToken() which uses it with the sender
# address to compute a deterministic deployment address via getTokenAddress(sender, salt)
export SALT="my-unique-salt"

# Run a deployment script and verify
forge script script/Mail.s.sol \
  --sig "run(string)" $SALT \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --sender <YOUR_WALLET_ADDRESS> \
  --broadcast \
  --verify

# Run a deployment script with custom fee token and verify
forge script script/Mail.s.sol \
  --sig "run(string)" $SALT \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL \
  --interactive \
  --sender <YOUR_WALLET_ADDRESS> \
  --broadcast \
  --verify

# Batch multiple calls into a single atomic transaction
forge script script/Deploy.s.sol \
  --broadcast --batch \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $PRIVATE_KEY
```

For more verification options including verifying existing contracts and API verification, see [Contract Verification](/quickstart/verify-contracts).

:::warning\[Batch Transaction Rules]

* **Atomic execution**: If any call reverts, the entire batch reverts
* **Single CREATE allowed**: At most one contract deployment per batch
* **CREATE must be first**: Deployment must be the first operation
* **Value must be zero**: Since Tempo has no native token, value must be 0
* **Silent failures**: Calling a non-existent function without a fallback succeeds silently
  :::

### Interact & debug with `cast`

```bash
# Check that your contract is deployed:
cast code <CONTRACT_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL

# Interact with the contract, retrieving the token address:
cast call <CONTRACT_ADDRESS> "token()" \
  --rpc-url $TEMPO_RPC_URL

# Get the name of an ERC20 token:
cast erc20 name <TOKEN_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL

# Check the ERC20 token balance of your address:
cast erc20 balance <TOKEN_ADDRESS> <YOUR_WALLET_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL

# Transfer some of your ERC20 tokens:
cast erc20 transfer <TOKEN_ADDRESS> <RECEIVER_ADDRESS> <AMOUNT> \
  --rpc-url $TEMPO_RPC_URL \
  --interactive

# Transfer some of your ERC20 tokens with custom fee token:
cast erc20 transfer <TOKEN_ADDRESS> <RECEIVER_ADDRESS> <AMOUNT> \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL \
  --interactive

# Send a transaction with custom fee token:
cast send <CONTRACT_ADDRESS> <FUNCTION_SIGNATURE> \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url $TEMPO_RPC_URL \
  --interactive

# Replay a transaction by hash:
cast run <TX_HASH> \
  --rpc-url $TEMPO_RPC_URL

# Send a batch transaction with multiple calls:
cast batch-send \
  --call "<CONTRACT_ADDRESS>::increment()" \
  --call "<CONTRACT_ADDRESS>::setNumber(uint256):500" \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $PRIVATE_KEY

# Batch with pre-encoded calldata:
ENCODED=$(cast calldata "setNumber(uint256)" 200)
cast batch-send \
  --call "<CONTRACT_ADDRESS>::$ENCODED" \
  --call "<CONTRACT_ADDRESS>::setNumber(uint256):101" \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $PRIVATE_KEY

# Sponsored transaction (gasless for sender):
# Step 1: Get the fee payer signature hash
FEE_PAYER_HASH=$(cast mktx <CONTRACT_ADDRESS> 'increment()' --rpc-url $TEMPO_RPC_URL --private-key $SENDER_KEY --tempo.print-sponsor-hash)
# Step 2: Sponsor signs the hash
SPONSOR_SIG=$(cast wallet sign --private-key $SPONSOR_KEY "$FEE_PAYER_HASH" --no-hash)
# Step 3: Send with sponsor signature
cast send <CONTRACT_ADDRESS> 'increment()' --rpc-url $TEMPO_RPC_URL --private-key $SENDER_KEY --tempo.sponsor-signature "$SPONSOR_SIG"

# Send with 2D nonce (parallel tx submission):
cast send <CONTRACT_ADDRESS> 'increment()' \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $PRIVATE_KEY \
  --nonce 0 --tempo.nonce-key 1

# Send with expiring nonce (time-bounded tx, max 30s):
VALID_BEFORE=$(($(date +%s) + 25))
cast send <CONTRACT_ADDRESS> 'increment()' \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $PRIVATE_KEY \
  --tempo.expiring-nonce --tempo.valid-before $VALID_BEFORE

# Send with access key (delegated signing):
# First authorize the key via Account Keychain precompile
cast send 0xAAAAAAAA00000000000000000000000000000000 \
  'authorizeKey(address,uint8,uint64,bool,(address,uint256)[])' \
  $ACCESS_KEY_ADDR 0 1893456000 false "[]" \
  --rpc-url $TEMPO_RPC_URL \
  --private-key $ROOT_PRIVATE_KEY
# Then send using the access key
cast send <CONTRACT_ADDRESS> 'increment()' \
  --rpc-url $TEMPO_RPC_URL \
  --access-key $ACCESS_KEY_PRIVATE_KEY \
  --root-account $ROOT_ADDRESS
```

### Local Development with Anvil

Anvil supports Tempo mode for local testing and forking Tempo networks:

```bash
# Start anvil in Tempo mode
anvil --tempo --hardfork t1

# Fork a live Tempo network for local testing
anvil --tempo --fork-url $TEMPO_RPC_URL

# Test transactions on local anvil fork
cast send <CONTRACT_ADDRESS> 'increment()' \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url http://127.0.0.1:8545 \
  --private-key $PRIVATE_KEY

# 2D nonce on anvil fork
cast send <CONTRACT_ADDRESS> 'increment()' \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url http://127.0.0.1:8545 \
  --private-key $PRIVATE_KEY \
  --nonce 0 --tempo.nonce-key 100

# Expiring nonce on anvil fork
cast send <CONTRACT_ADDRESS> 'increment()' \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url http://127.0.0.1:8545 \
  --private-key $PRIVATE_KEY \
  --tempo.expiring-nonce --tempo.valid-before $(($(date +%s) + 25))

# Batch transactions on anvil fork
cast batch-send \
  --tempo.fee-token <FEE_TOKEN_ADDRESS> \
  --rpc-url http://127.0.0.1:8545 \
  --call "<CONTRACT_ADDRESS>::increment()" \
  --call "<CONTRACT_ADDRESS>::increment()" \
  --private-key $PRIVATE_KEY
```

## Tempo-Specific CLI Flags

The following flags are available for `cast` and `forge script` for Tempo-specific features:

| Flag | Description | Example |
|------|-------------|---------|
| `--tempo.fee-token <ADDRESS>` | Specify the TIP-20 token to pay transaction fees | `--tempo.fee-token 0x20c0...0001` |
| `--tempo.nonce-key <KEY>` | 2D nonce key for parallel transaction submission | `--tempo.nonce-key 1` |
| `--tempo.expiring-nonce` | Enable expiring nonce for time-bounded transactions | `--tempo.expiring-nonce` |
| `--tempo.valid-before <TIMESTAMP>` | Unix timestamp before which tx must execute (max 30s from now) | `--tempo.valid-before 1704067200` |
| `--tempo.valid-after <TIMESTAMP>` | Unix timestamp after which tx can execute | `--tempo.valid-after 1704067100` |
| `--tempo.sponsor-signature <SIG>` | Pre-signed sponsor signature for gasless transactions | `--tempo.sponsor-signature 0x...` |
| `--tempo.print-sponsor-hash` | Print fee payer signature hash and exit (for sponsor to sign) | `--tempo.print-sponsor-hash` |

Ledger and Trezor wallets are not yet compatible with any `--tempo.*` option.

# Go

Tempo distributes a Go SDK for building application clients. The SDK provides packages for RPC communication, transaction signing, and key management.

The Tempo Go SDK can be used to perform common operations with the chain, such as: sending Tempo transactions, batching multiple calls, fee sponsorship, and more.

::::steps

## Install

To install the Tempo Go SDK:

```bash [go]
go get github.com/tempoxyz/tempo-go@v0.1.0
```

:::tip
The SDK requires Go 1.21 or higher.
:::

## Create an RPC Client

To interact with Tempo, first create an RPC client connected to a Tempo node:

```go [main.go]
package main

import (
    "context"
    "fmt"

    "github.com/tempoxyz/tempo-go/pkg/client"
)

func main() {
    c := client.New("https://rpc.testnet.tempo.xyz") 

    ctx := context.Background()
    blockNum, _ := c.GetBlockNumber(ctx)
    fmt.Printf("Connected to Tempo at block %d\n", blockNum)
}
```

For authenticated RPC endpoints:

```go [main.go]
c := client.New("https://rpc.testnet.tempo.xyz",
    client.WithAuth("username", "password"),
)
```

## Create a Signer

Create a signer to sign transactions. The signer manages your private key and generates signatures:

```go [main.go]
package main

import (
    "fmt"

    "github.com/tempoxyz/tempo-go/pkg/signer"
)

func main() {
    s, err := signer.NewSigner("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
    if err != nil {
        panic(err)
    }

    fmt.Printf("Address: %s\n", s.Address().Hex())
}
```

## Send a Transaction

Build and send a transaction using the builder pattern:

```go [main.go]
package main

import (
    "context"
    "log"
    "math/big"

    "github.com/ethereum/go-ethereum/common"
    "github.com/tempoxyz/tempo-go/pkg/client"
    "github.com/tempoxyz/tempo-go/pkg/signer"
    "github.com/tempoxyz/tempo-go/pkg/transaction"
)

func main() {
    c := client.New("https://rpc.testnet.tempo.xyz")
    s, _ := signer.NewSigner("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")

    ctx := context.Background()
    nonce, _ := c.GetTransactionCount(ctx, s.Address().Hex()) // [!code hl]

    recipient := common.HexToAddress("0x70997970C51812dc3A010C7d01b50e0d17dc79C8")

    // [!code hl:10]
    tx := transaction.NewBuilder(big.NewInt(42431)). // Tempo testnet
        SetNonce(nonce).
        SetGas(100000).
        SetMaxFeePerGas(big.NewInt(20000000000)). // 20 gwei base fee
        SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
        AddCall(recipient, big.NewInt(0), []byte{}).
        Build()

    transaction.SignTransaction(tx, s)
    serialized, _ := transaction.Serialize(tx, nil)
    hash, _ := c.SendRawTransaction(ctx, serialized) // [!code hl]
    log.Printf("Transaction hash: %s", hash)
}
```

::::

## Examples

### Read Chain Data

Query the blockchain for basic information:

```go [read.go]
ctx := context.Background()

blockNum, _ := c.GetBlockNumber(ctx)
chainID, _ := c.GetChainID(ctx)
nonce, _ := c.GetTransactionCount(ctx, "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb")

fmt.Printf("Block: %d, Chain: %d, Nonce: %d\n", blockNum, chainID, nonce)
```

### Token Transfer

Send a TIP-20 token transfer using go-ethereum's ABI encoding:

```go [transfer.go]
import "github.com/ethereum/go-ethereum/accounts/abi"

erc20ABI, _ := abi.JSON(strings.NewReader(`[{"name":"transfer","type":"function","inputs":[{"name":"to","type":"address"},{"name":"amount","type":"uint256"}]}]`))

recipient := common.HexToAddress("0x70997970C51812dc3A010C7d01b50e0d17dc79C8")
amount := big.NewInt(100_000_000) // 100 tokens (6 decimals)

transferData, _ := erc20ABI.Pack("transfer", recipient, amount)

tx := transaction.NewBuilder(big.NewInt(42429)).
    SetNonce(nonce).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    AddCall(transaction.AlphaUSDAddress, big.NewInt(0), transferData).
    Build()
```

### Transfer with Memo

Include a memo for payment reconciliation:

```go [memo.go]
tip20ABI, _ := abi.JSON(strings.NewReader(`[{"name":"transferWithMemo","type":"function","inputs":[{"name":"to","type":"address"},{"name":"amount","type":"uint256"},{"name":"memo","type":"bytes32"}]}]`))

recipient := common.HexToAddress("0x70997970C51812dc3A010C7d01b50e0d17dc79C8")
amount := big.NewInt(100_000_000)
memo := [32]byte{}
copy(memo[:], "INV-12345")

memoData, _ := tip20ABI.Pack("transferWithMemo", recipient, amount, memo)

tx := transaction.NewBuilder(big.NewInt(42429)).
    SetNonce(nonce).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    AddCall(transaction.AlphaUSDAddress, big.NewInt(0), memoData).
    Build()
```

### Batch Multiple Calls

Execute multiple operations atomically in a single transaction:

```go [batch.go]
tx := transaction.NewBuilder(big.NewInt(42429)).
    SetNonce(nonce).
    SetGas(200000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    AddCall(addr1, big.NewInt(0), transfer1Data). // [!code hl]
    AddCall(addr2, big.NewInt(0), transfer2Data). // [!code hl]
    AddCall(addr3, big.NewInt(0), contractCallData). // [!code hl]
    Build()

transaction.SignTransaction(tx, s)
```

### Parallel Transactions (2D Nonces)

Send multiple transactions concurrently using different nonce keys:

```go [parallel.go]
tx1 := transaction.NewBuilder(big.NewInt(42429)).
    SetNonceKey(big.NewInt(1)). // Sequence A // [!code hl]
    SetNonce(0).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    AddCall(recipient1, big.NewInt(0), data1).
    Build()

tx2 := transaction.NewBuilder(big.NewInt(42429)).
    SetNonceKey(big.NewInt(2)). // Sequence B (parallel) // [!code hl]
    SetNonce(0).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    AddCall(recipient2, big.NewInt(0), data2).
    Build()

transaction.SignTransaction(tx1, s)
transaction.SignTransaction(tx2, s)

// Send both in parallel
go func() { c.SendRawTransaction(ctx, serialize(tx1)) }()
go func() { c.SendRawTransaction(ctx, serialize(tx2)) }()
```

### Fee Sponsorship

Have another account pay for transaction fees:

```go [feepayer.go]
tx := transaction.NewBuilder(big.NewInt(42429)).
    SetNonce(nonce).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    SetSponsored(true). // Mark as awaiting fee payer // [!code hl]
    AddCall(recipient, big.NewInt(0), data).
    Build()

transaction.SignTransaction(tx, userSigner)
transaction.AddFeePayerSignature(tx, feePayerSigner)
```

### Transaction Validity Window

Set a time window during which the transaction is valid:

```go [validity.go]
now := time.Now()

tx := transaction.NewBuilder(big.NewInt(42429)).
    SetNonce(nonce).
    SetGas(100000).
    SetMaxFeePerGas(big.NewInt(10000000000)).
    SetMaxPriorityFeePerGas(big.NewInt(1000000000)).
    SetValidAfter(uint64(now.Unix())). // [!code hl]
    SetValidBefore(uint64(now.Add(1 * time.Hour).Unix())). // [!code hl]
    AddCall(recipient, big.NewInt(0), data).
    Build()
```

### Batch RPC Requests

Send multiple RPC calls efficiently in a single HTTP request:

```go [batch_rpc.go]
batch := client.NewBatchRequest()
batch.Add("eth_blockNumber").
    Add("eth_chainId").
    Add("eth_getBalance", "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb", "latest")

responses, _ := c.SendBatch(ctx, batch)
for _, resp := range responses {
    fmt.Printf("Result: %v\n", resp.Result)
}
```

## Packages

| Package | Description |
| --- | --- |
| `transaction` | TempoTransaction encoding, signing, and validation |
| `client` | RPC client for interacting with Tempo nodes |
| `signer` | Key management and signature generation |

## Next Steps

After setting up the Go SDK, you can:

* Follow a guide on how to [use accounts](/guide/use-accounts), [make payments](/guide/payments), [issue stablecoins](/guide/issuance), [exchange stablecoins](/guide/stablecoin-dex), and [more](/).
* View the [examples on GitHub](https://github.com/tempoxyz/tempo-go/tree/main/examples)

# Rust

Tempo distributes a Rust SDK in the form of an [Alloy](https://alloy.rs) crate. Alloy is a popular Rust crate for interacting with EVM-compatible blockchains.

The Tempo Alloy crate can be used to perform common operations with the chain, such as: querying the chain, sending Tempo transactions, managing tokens & their AMM pools, and more.

::::steps

## Install

To install the Tempo extension, you will need to install [Alloy](https://alloy.rs) and Tempo:

```bash [cargo]
cargo add alloy tokio
cargo add tempo-alloy --git https://github.com/tempoxyz/tempo
```

:::tip
We use [`tokio`](https://tokio.rs) in this example, but you can use any async runtime.
:::

## Configure A Provider

To use the Tempo extension crate, you will need to create a [`Provider`] using the [`TempoNetwork`](https://tempoxyz.github.io/tempo/tempo_alloy/struct.TempoNetwork.html). This will enable the usage of Tempo specific types on the [`Provider`] instance.

For more information about network types, see the Alloy [documentation](https://alloy.rs/guides/interacting-with-multiple-networks#interacting-with-multiple-networks).

```rs [main.rs]
use alloy::providers::ProviderBuilder; // [!code focus]
use tempo_alloy::TempoNetwork; // [!code focus]

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>() // [!code focus]
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set")) // [!code focus]
        .await?; // [!code focus]

    println!("Provider connected successfully"); // [!code focus]
    println!("Chain ID: {provider:?}"); // [!code focus]

    Ok(())
}
```

## Use Actions

Now we are ready to use the provider to interact with the network. We can use the provider to send transactions, read data, and more.

```rs [main.rs]
use alloy::providers::{Provider, ProviderBuilder};
use tempo_alloy::TempoNetwork;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    // [!code focus:2]
    println!("{}", provider.get_block_number().await?);
    // @log: 421045
    Ok(())
}
```

See the Alloy [documentation](https://alloy.rs) or the [`Provider`] docs for more examples.

[`Provider`]: https://docs.rs/alloy/latest/alloy/providers/trait.Provider.html

::::

# TypeScript SDKs

:::note
**Note:** `tempo.ts/chains` & `tempo.ts/viem` have been upstreamed into [Viem](https://viem.sh/tempo) as of `viem@2.43.0`. If you are using either entrypoint, please update to use `viem/chains` or `viem/tempo` instead.

[Migration Guide](https://github.com/tempoxyz/tempo-ts/releases/tag/tempo.ts%400.12.0)
:::

:::note
**Note:** `tempo.ts/wagmi` has been upstreamed into [Wagmi](https://wagmi.sh/tempo) as of `wagmi@3.2.0` and `@wagmi/core@3.1.0`. Please update to use `wagmi/tempo` or `@wagmi/core/tempo` instead.

[Migration Guide](https://github.com/tempoxyz/tempo-ts/releases/tag/tempo.ts%400.13.0)
:::

Tempo distributes TypeScript SDKs for:

* [Viem](https://viem.sh): TypeScript interface for EVM blockchains
* [Wagmi](https://wagmi.sh): React Hooks (and reactive primitives) for EVM blockchains

The Tempo extensions can be used to perform common operations with the chain, such as:
querying the chain, sending Tempo transactions, managing tokens & their AMM pools, and more.

<Cards>
  <Card description="Set up a Viem client to interact with Tempo" to="https://viem.sh/tempo" icon="lucide:workflow" title="Viem Setup" />

  <Card description="Set up a Wagmi configuration with Tempo" to="https://wagmi.sh/tempo" icon="lucide:workflow" title="Wagmi Setup" />
</Cards>

:::tip

**When should I use Wagmi vs. Viem?**

* **Viem** is best suited for **libraries, tooling, servers, scripting, etc** – a low-level and stateless interface for the EVM
* **Wagmi** is best suited for **applications & wallets** – a high-level and stateful interface for the EVM (React Hooks, Vanilla JS, etc)

:::

## Viem

<Cards>
  <Card description="Viem Actions for querying data, sending transactions, managing tokens & AMM pools, and more" to="https://viem.sh/tempo/actions" icon="lucide:workflow" title="Actions" />
</Cards>

## Wagmi

<Cards>
  <Card description="Wagmi React Hooks for building apps on Tempo" to="https://wagmi.sh/tempo/hooks" icon="lucide:network" title="Hooks" />

  <Card description="Wagmi Connectors for connecting between wallets, apps, and Tempo" to="https://wagmi.sh/tempo/connectors" icon="lucide:square-stack" title="Connectors" />

  <Card description="Wagmi Actions for querying data, sending transactions, managing tokens & AMM pools, and more" to="https://wagmi.sh/tempo/actions" icon="lucide:workflow" title="Actions" />
</Cards>

# Create a Stablecoin

Create your own stablecoin on Tempo using the [TIP-20 token standard](/protocol/tip20/overview).
TIP-20 tokens are designed specifically for payments with built-in compliance features, role-based permissions,
and integration with Tempo's payment infrastructure.

## Demo

By the end of this guide, you will be able to create a stablecoin on Tempo.

<Demo.Container name="Create a Stablecoin" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateToken stepNumber={3} last />
</Demo.Container>

## Steps

::::steps

### Set up Wagmi & integrate accounts

Ensure that you have set up your project with Wagmi and integrated accounts by following either of the guides:

* [Embed Passkey accounts](/guide/use-accounts/embed-passkeys)
* [Connect to wallets](/guide/use-accounts/connect-to-wallets)

### Add testnet funds¹

Before we send off a transaction to deploy our stablecoin to the Tempo testnet, we need to make sure our account is funded with a stablecoin to cover the transaction fee.

As we have configured our project to use `AlphaUSD` (`0x20c000…0001`)
as the [default fee token](/quickstart/integrate-tempo#default-fee-token), we will need to add some `AlphaUSD` to our account.

Luckily, the built-in Tempo testnet faucet supports funding accounts with `AlphaUSD`.

<Demo.Container name="Add Funds" footerVariant="balances" showBadge={false}>
  <Step.AddFunds stepNumber={1} last />
</Demo.Container>

:::code-group

```tsx twoslash [AddFunds.ts]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'

export function AddFunds() {
  const { address } = useConnection()
  const addFunds = Hooks.faucet.useFund()

  return (
    <button onClick={() => addFunds.mutate({ account: address })}>
      Add Funds
    </button>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

:::warning
¹ It is important to note that the `addFunds` Hook only works on testnets as a convenience feature to get
started quickly. For production, you will need to onramp & fund your account manually.
:::

### Add form fields

Now that we have some funds to cover the transaction fee in our account, we can create a stablecoin.

Let's create a new component and add some input fields for the **name** and **symbol** of our stablecoin, as shown in the demo.

<Demo.Container name="Create Form">
  <Step.AddFunds stepNumber={1} />

  <Step.CreateToken stepNumber={2} last />
</Demo.Container>

:::code-group

```tsx twoslash [CreateStablecoin.tsx]
// @noErrors
export function CreateStablecoin() {
  return (
    <div>
      <form
        onSubmit={(event) => {
          event.preventDefault()
          const formData = new FormData(event.target as HTMLFormElement)
          const name = formData.get('name') as string
          const symbol = formData.get('symbol') as string
        }}
      >
        <input type="text" name="name" placeholder="demoUSD" required />
        <input type="text" name="symbol" placeholder="DEMO" required />
        <button type="submit">
          Create
        </button>
      </form>
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Add submission logic

Now that we have some input fields, we need to add some logic to handle the submission of the form to create the stablecoin.

After this step, your users will be able to create a stablecoin by clicking the "Create" button!

:::warning
We **strongly** recommend that for stablecoins, the `currency` field be set to the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-letter code for the underlying fiat currency (e.g., `"USD"`, `"EUR"`, `"GBP"`) — **not** the token symbol. This value is **immutable** after token creation and affects fee payment eligibility, DEX routing, and quote token pairing. **Only `USD` stablecoins can be used to pay transaction fees on Tempo** — if your stablecoin is USD-denominated, the currency must be set to `"USD"` to be eligible for fee payment.
:::

<Demo.Container name="Create Form">
  <Step.CreateToken stepNumber={1} last />
</Demo.Container>

:::code-group

```tsx twoslash [CreateStablecoin.tsx]
import { Hooks } from 'wagmi/tempo' // [!code ++]

// @noErrors
export function CreateStablecoin() {
  const create = Hooks.token.useCreateSync() // [!code ++]

  return (
    <div>
      <form
        onSubmit={(event) => {
          event.preventDefault()
          const formData = new FormData(event.target as HTMLFormElement)
          const name = formData.get('name') as string
          const symbol = formData.get('symbol') as string
          create.mutate({ // [!code ++]
            name, // [!code ++]
            symbol, // [!code ++]
            currency: 'USD', // [!code ++]
          }) // [!code ++]
        }}
      >
        <input type="text" name="name" placeholder="demoUSD" required />
        <input type="text" name="symbol" placeholder="DEMO" required />
        <button type="submit">
          Create
        </button>
      </form>
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Add success state

Now that users can submit the form and create a stablecoin, let's add a basic success state to display
the name of the stablecoin and a link to the transaction receipt.

:::code-group

```tsx twoslash [CreateStablecoin.tsx]
import { Hooks } from 'wagmi/tempo' 

// @noErrors
export function CreateStablecoin() {
  const create = Hooks.token.useCreateSync() 

  return (
    <div>
      <form
        onSubmit={(event) => {
          event.preventDefault()
          const formData = new FormData(event.target as HTMLFormElement)
          const name = formData.get('name') as string
          const symbol = formData.get('symbol') as string
          create.mutate({ 
            name, 
            symbol, 
            currency: 'USD', 
          }) 
        }}
      >
        <input type="text" name="name" placeholder="demoUSD" required />
        <input type="text" name="symbol" placeholder="DEMO" required />
        <button type="submit">
          Create
        </button>
      </form>

      {create.data && ( // [!code ++]
        <div> {/* [!code ++] */}
          {create.data.name} created successfully! {/* [!code ++] */}
          <a href={`https://explore.tempo.xyz/tx/${create.data.receipt.transactionHash}`}> {/* [!code ++] */}
            View receipt {/* [!code ++] */}
          </a> {/* [!code ++] */}
        </div> {/* [!code ++] */}
      )} {/* [!code ++] */}
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Next steps

Now that you have created your first stablecoin, you can now:

* [Add your token to the Token List](/quickstart/tokenlist#adding-a-new-token) so it appears in wallets, explorers, and other apps on Tempo
* learn the [Best Practices](#best-practices) below
* follow a guide on how to [mint](/guide/issuance/mint-stablecoins) and [more](/guide/issuance/manage-stablecoin) with your stablecoin.

::::

## Best Practices

### Loading State

When the user is creating a stablecoin, we should show loading state to indicate that the process is happening.

We can use the `isPending` property from the `useCreateSync` hook to show pending state to the user on our "Create" button.

```tsx
<button 
  disabled={create.isPending} // [!code ++]
  type="submit"
>
  {create.isPending ? 'Creating...' : 'Create'} {/* [!code ++] */}
</button>
```

### Error Handling

If an error unexpectedly occurs, we should display an error message to the user.

We can use the `error` property from the `useCreateSync` hook to show error state to the user.

```tsx twoslash
// @noErrors
export function CreateStablecoin() {
  // ...

  if (create.error) // [!code ++]
    return <div>Error: {create.error.message}</div> {/* [!code ++] */}

  // ...
}
```

## Learning Resources

<Cards>
  <Card description="Learn more about TIP-20 tokens on Tempo" to="/protocol/tip20/overview" icon="lucide:coins" title="TIP20 Tokens" />
</Cards>

# Distribute Rewards

Distribute rewards to token holders using TIP-20's built-in reward distribution mechanism. Rewards allow parties to incentivize holders of a token by distributing tokens proportionally based on their balance.

Rewards can be distributed by anyone on any TIP-20 token, and claimed by any holder who has opted in. This guide covers both the reward distributor and token holder use cases. While the demo below uses a token you create, the same principles apply to any token.

## Demo

Try out the complete rewards flow: create a token, opt in to receive rewards on it, create a reward for yourself, and claim it.

<Demo.Container name="Distribute Rewards" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} />

  <Step.MintToken stepNumber={5} />

  <Step.OptInToRewards stepNumber={6} />

  <Step.StartReward stepNumber={7} />

  <Step.ClaimReward stepNumber={8} flowDependencies={['rewardId']} last />
</Demo.Container>

## Steps

::::steps

### \[Optional] Create a Stablecoin

If you would like to distribute rewards on a token you have created, follow the [Create a Stablecoin](/guide/issuance/create-a-stablecoin) guide to deploy your token.

### Tell Your Users to Opt In to Rewards

Token holders must opt in to receive rewards by setting their reward recipient address. This is typically set to their own address.

:::code-group

```tsx twoslash [OptInToRewards.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'

// @noErrors
export function OptInToRewards() {
  const { address } = useConnection()
  const tokenAddress = '0x...' // Your token address

  const setRecipient = Hooks.reward.useSetRecipientSync()

  const handleOptIn = () => { // [!code hl]
    if (!address) return // [!code hl]
    setRecipient.mutate({ // [!code hl]
      recipient: address, // [!code hl]
      token: tokenAddress, // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button 
      disabled={setRecipient.isPending}
      onClick={handleOptIn}
      type="button"
    >
      {setRecipient.isPending ? 'Opting in...' : 'Opt In to Rewards'}
    </button>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Make a Reward Distribution

Anyone can make a reward distribution that allocates tokens to all opted-in holders proportionally based on their balance.

:::code-group

```tsx twoslash [StartReward.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'

// @noErrors
export function StartReward() {
  const tokenAddress = '0x...' // Your token address

  const { data: metadata } = Hooks.token.useGetMetadata({
    token: tokenAddress,
  })

  const start = Hooks.reward.useStartSync()

  const handleStart = () => { // [!code hl]
    if (!metadata) return // [!code hl]
    start.mutate({ // [!code hl]
      amount: parseUnits('50', metadata.decimals), // [!code hl]
      token: tokenAddress, // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button
      disabled={start.isPending || !metadata}
      onClick={handleStart}
      type="button"
    >
      {start.isPending ? 'Starting...' : 'Start Reward'}
    </button>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Your Users Can Claim Rewards

Once a reward is distributed, opted-in holders can claim their share.

:::code-group

```tsx twoslash [ClaimReward.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'

// @noErrors
export function ClaimReward() {
  const tokenAddress = '0x...' // Your token address

  const claim = Hooks.reward.useClaimSync()

  const handleClaim = () => { // [!code hl]
    claim.mutate({ // [!code hl]
      token: tokenAddress, // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button
      disabled={claim.isPending}
      onClick={handleClaim}
      type="button"
    >
      {claim.isPending ? 'Claiming...' : 'Claim Rewards'}
    </button>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

::::

## Recipes

### Watch for new reward distributions

Use `useWatchRewardDistributed` to listen for new reward distributions on a token. This is useful for updating your UI when a reward is distributed.

```tsx twoslash
import { Hooks } from 'wagmi/tempo'

// @noErrors
function WatchRewards() {
  const tokenAddress = '0x...' // Your token address

  Hooks.reward.useWatchRewardDistributed({ // [!code hl]
    token: tokenAddress, // [!code hl]
    onRewardDistributed(args) { // [!code hl]
      console.log('New reward scheduled:', args) // [!code hl]
      // Update UI, refetch balances, show notification, etc. // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  return <div>Watching for reward distributions...</div>
}
```

### Watch for reward opt-ins

Use `useWatchRewardRecipientSet` to listen for when users opt in to rewards by setting their recipient address. This is useful for tracking opt-in activity.

```tsx twoslash
import { Hooks } from 'wagmi/tempo'

// @noErrors
function WatchOptIns() {
  const tokenAddress = '0x...' // Your token address

  Hooks.reward.useWatchRewardRecipientSet({ // [!code hl]
    token: tokenAddress, // [!code hl]
    onRewardRecipientSet(args) { // [!code hl]
      console.log('User opted in:', args) // [!code hl]
      // Update UI, track analytics, etc. // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  return <div>Watching for reward opt-ins...</div>
}
```

## Learning Resources

<Cards>
  <Card description="See the TIP-20 rewards spec" to="/protocol/tip20-rewards/spec" icon="lucide:file-text" title="TIP-20 Rewards Spec" />

  <Card description="Read an overview of TIP-20 rewards" to="/protocol/tip20-rewards/overview" icon="lucide:book-open" title="TIP-20 Rewards Overview" />
</Cards>

# Manage Your Stablecoin

Configure your stablecoin's permissions, supply limits, and compliance policies after deployment. This guide covers granting roles to manage token operations, setting supply caps, configuring transfer policies, and controlling token transfers through pause/unpause functionality.

TIP-20 tokens use a role-based access control system that allows you to delegate different administrative functions to different addresses. For detailed information about the role system, see the [TIP-20 specification](/protocol/tip20/spec#role-based-access-control).

## Steps

In this guide, we'll walk through how to assign and check the **`issuer`** role, but the process is identical for other roles like `pause`, `unpause`, `burnBlocked`, and `defaultAdmin`.

::::steps

### Setup

Before you can manage roles on your stablecoin, you need to create one. Follow the [Create a Stablecoin](/guide/issuance/create-a-stablecoin) guide to deploy your token.

Once you've created your token, you can proceed to grant roles to specific addresses.

### Grant Roles to an Address

Assign roles to specific addresses to delegate token management capabilities.

<Demo.Container name="Grant Roles to an Address" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} last />
</Demo.Container>

:::code-group

```tsx twoslash [GrantRoles.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function GrantRoles() {
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const treasuryAddress = '0x...' // Address to grant the issuer role

  const grant = Hooks.token.useGrantRolesSync({}) // [!code hl]

  const handleGrantIssuer = async () => { // [!code hl]
    await grant.mutate({ // [!code hl]
      token: tokenAddress, // [!code hl]
      roles: ['issuer'], // [!code hl]
      to: treasuryAddress, // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={grant.isPending} // [!code hl]
      onClick={handleGrantIssuer} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {grant.isPending ? 'Granting...' : 'Grant Issuer Role'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Check if an Address Has a Role

Use `hasRole` to verify whether an address has been granted a specific role.

:::code-group

```tsx twoslash [GrantRoles.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function GrantRoles() {
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const treasuryAddress = '0x...' // Address to grant the issuer role

  // Grant the issuer role
  const grant = Hooks.token.useGrantRolesSync({
    mutation: { // [!code ++]
      onSettled() { // [!code ++]
        queryClient.refetchQueries({ queryKey: ['hasRole'] }) // [!code ++]
      }, // [!code ++]
    }, // [!code ++]
  })

  const handleGrantIssuer = async () => {
    await grant.mutate({
      token: tokenAddress,
      roles: ['issuer'],
      to: treasuryAddress,
    })
  }

  const { data: hasIssuerRole } = Hooks.token.useHasRole({ // [!code ++]
    account: treasuryAddress, // [!code ++]
    token: tokenAddress, // [!code ++]
    role: 'issuer', // [!code ++]
  }) // [!code ++]

  return (
    <div>
      <button
        disabled={grant.isPending}
        onClick={handleGrantIssuer}
        type="button"
      >
        {grant.isPending ? 'Granting...' : 'Grant Issuer Role'}
      </button>

      {hasIssuerRole !== undefined && ( // [!code ++]
        <div> {/* [!code ++] */}
        Treasury {hasIssuerRole ? 'has' : 'does not have'} the issuer role // [!code ++]
        </div> {/* [!code ++] */}
        )} // [!code ++]
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Revoke the Issuer Role

Revoke roles from addresses when you need to remove their permissions.

<Demo.Container name="Revoke Issuer Role" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} />

  <Step.RevokeTokenRoles stepNumber={5} roles={['issuer']} last />
</Demo.Container>

:::code-group

```tsx twoslash [RevokeRoles.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function RevokeRoles() {
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const treasuryAddress = '0x...' // Address to grant/revoke the issuer role

  // Grant the issuer role
  const grant = Hooks.token.useGrantRolesSync({
    mutation: {
      onSettled() {
        queryClient.refetchQueries({ queryKey: ['hasRole'] })
      },
    },
  })

  const handleGrantIssuer = async () => {
    await grant.mutate({
      token: tokenAddress,
      roles: ['issuer'],
      to: treasuryAddress,
    })
  }

  // Check if the treasury has the issuer role
  const { data: hasIssuerRole } = Hooks.token.useHasRole({
    account: treasuryAddress,
    token: tokenAddress,
    role: 'issuer',
  })

  // Revoke the issuer role // [!code ++]
  const revoke = Hooks.token.useRevokeRolesSync({ // [!code ++]
    mutation: { // [!code ++]
      onSettled() { // [!code ++]
        queryClient.refetchQueries({ queryKey: ['hasRole'] }) // [!code ++]
      }, // [!code ++]
    }, // [!code ++]
  }) // [!code ++]

  const handleRevokeIssuer = async () => { // [!code ++]
    await revoke.mutate({ // [!code ++]
      token: tokenAddress, // [!code ++]
      roles: ['issuer'], // [!code ++]
      from: treasuryAddress, // [!code ++]
    }) // [!code ++]
  } // [!code ++]

  return (
    <div>
      <button
        disabled={grant.isPending}
        onClick={handleGrantIssuer}
        type="button"
      >
        {grant.isPending ? 'Granting...' : 'Grant Issuer Role'}
      </button>

      <button // [!code ++]
        disabled={revoke.isPending || !hasIssuerRole} // [!code ++]
        onClick={handleRevokeIssuer} // [!code ++]
        type="button" // [!code ++]
      > {/* [!code ++] */}
      {revoke.isPending ? 'Revoking...' : 'Revoke Issuer Role'} {/* [!code ++] */}
      </button> {/* [!code ++] */}

      {hasIssuerRole !== undefined && (
        <div>
          Treasury {hasIssuerRole ? 'has' : 'does not have'} the issuer role
        </div>
      )}
    </div>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

::::

## Recipes

### Set Supply Cap

Limit the maximum total supply of your token. Setting supply caps requires the **`DEFAULT_ADMIN_ROLE`**. The new cap cannot be less than the current total supply.

<Demo.Container name="Set Supply Cap" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.SetSupplyCap stepNumber={4} last />
</Demo.Container>

:::code-group

```tsx twoslash [SetSupplyCap.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'

// @noErrors
export function SetSupplyCap() {
  const tokenAddress = '0x...' // Your token address

  const { data: metadata, refetch: refetchMetadata } = // [!code hl]
    Hooks.token.useGetMetadata({ token: tokenAddress }) // [!code hl]

  const setSupplyCap = Hooks.token.useSetSupplyCapSync({ // [!code hl]
    mutation: { onSettled: () => refetchMetadata() }, // [!code hl]
  }) // [!code hl]

  const handleSetSupplyCap = () => { // [!code hl]
    setSupplyCap.mutate({ // [!code hl]
      token: tokenAddress, // [!code hl]
      supplyCap: parseUnits('1000', metadata?.decimals || 6), // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={setSupplyCap.isPending} // [!code hl]
      onClick={handleSetSupplyCap} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {setSupplyCap.isPending ? 'Setting...' : 'Set Cap'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Configure Transfer Policies

Control who can send and receive your stablecoin for compliance and regulatory requirements. Setting transfer policies requires the **`DEFAULT_ADMIN_ROLE`**.

Transfer policies can be:

* **Always allow**: Anyone can send/receive (default)
* **Always reject**: Nobody can send/receive
* **Whitelist**: Only authorized addresses can send/receive
* **Blacklist**: Blocked addresses cannot send/receive

Learn more about configuring transfer policies in the [TIP-403 specification](/protocol/tip403/spec).

<Demo.Container name="Create and Link Transfer Policy" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.CreateTokenPolicy stepNumber={4} />

  <Step.LinkTokenPolicy stepNumber={5} last />
</Demo.Container>

:::code-group

```tsx twoslash [CreateTokenPolicy.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'

// @noErrors
export function CreateTokenPolicy() {
  const tokenAddress = '0x...' // Your token address

  const createPolicy = Hooks.policy.useCreateSync({ // [!code hl]
    mutation: { // [!code hl]
      onSuccess(result) { // [!code hl]
        // Store policyId for the next step // [!code hl]
        console.log('Policy ID:', result.policyId) // [!code hl]
      }, // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  const handleCreatePolicy = async () => { // [!code hl]
    await createPolicy.mutateAsync({ // [!code hl]
      addresses: [ // [!code hl]
        '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb', // [!code hl]
      ], // [!code hl]
      type: 'blacklist', // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={createPolicy.isPending} // [!code hl]
      onClick={handleCreatePolicy} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {createPolicy.isPending ? 'Creating...' : 'Create Policy'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [LinkTokenPolicy.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'

// @noErrors
export function LinkTokenPolicy() {
  const tokenAddress = '0x...' // Your token address
  const policyId = 1n // Policy ID from previous step

  const linkPolicy = Hooks.token.useChangeTransferPolicySync() // [!code hl]

  const handleLinkPolicy = async () => { // [!code hl]
    await linkPolicy.mutateAsync({ // [!code hl]
      policyId, // [!code hl]
      token: tokenAddress, // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={linkPolicy.isPending} // [!code hl]
      onClick={handleLinkPolicy} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {linkPolicy.isPending ? 'Linking...' : 'Link Policy'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Pause and Unpause Token Transfers

Temporarily halt all token transfers during emergency situations or maintenance windows. Pausing transfers requires the **`PAUSE_ROLE`**. Unpausing transfers requires the **`UNPAUSE_ROLE`**.

<Demo.Container name="Pause and Unpause Your Token" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['pause', 'unpause']} />

  <Step.PauseUnpauseTransfers stepNumber={5} last />
</Demo.Container>

:::code-group

```tsx twoslash [PauseUnpauseTransfers.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'

// @noErrors
export function PauseUnpauseTransfers() {
  const tokenAddress = '0x...' // Your token address

  const { data: metadata, refetch: refetchMetadata } = // [!code hl]
    Hooks.token.useGetMetadata({ token: tokenAddress }) // [!code hl]

  const pause = Hooks.token.usePauseSync({ // [!code hl]
    mutation: { onSettled: () => refetchMetadata() }, // [!code hl]
  }) // [!code hl]

  const unpause = Hooks.token.useUnpauseSync({ // [!code hl]
    mutation: { onSettled: () => refetchMetadata() }, // [!code hl]
  }) // [!code hl]

  const paused = metadata?.paused || false // [!code hl]

  const handleToggle = () => { // [!code hl]
    if (paused) { // [!code hl]
      unpause.mutate({ // [!code hl]
        token: tokenAddress, // [!code hl]
      }) // [!code hl]
    } else { // [!code hl]
      pause.mutate({ // [!code hl]
        token: tokenAddress, // [!code hl]
      }) // [!code hl]
    } // [!code hl]
  } // [!code hl]

  const isProcessing = pause.isPending || unpause.isPending // [!code hl]

  return (
    <button // [!code hl]
      disabled={isProcessing} // [!code hl]
      onClick={handleToggle} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {isProcessing ? 'Processing...' : paused ? 'Unpause' : 'Pause'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Using the Burn Blocked Role

The Burn Blocked role allows your team to burn tokens from blocked or frozen addresses. This is useful for regulatory compliance when you need to remove tokens from addresses that violate terms of service or legal requirements.

<Demo.Container name="Create and Link Transfer Policy" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer', 'burnBlocked']} />

  <Step.MintToken stepNumber={5} recipient={Demo.FAKE_RECIPIENT} />

  <Step.CreateTokenPolicy stepNumber={6} flowDependencies={['transferId']} />

  <Step.LinkTokenPolicy stepNumber={7} />

  <Step.BurnTokenBlocked stepNumber={8} last />
</Demo.Container>

:::code-group

```tsx twoslash [BurnBlocked.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'

// @noErrors
export function BurnBlocked() {
  const tokenAddress = '0x...' // Your token address
  const blockedAddress = '0x...' // The blocked address to burn tokens from

  const { data: metadata } = Hooks.token.useGetMetadata({ // [!code hl]
    token: tokenAddress, // [!code hl]
  }) // [!code hl]

  const burnBlocked = Hooks.token.useBurnBlockedSync() // [!code hl]

  const handleBurnBlocked = async () => { // [!code hl]
    if (!metadata) return // [!code hl]

    await burnBlocked.mutateAsync({ // [!code hl]
      token: tokenAddress, // [!code hl]
      from: blockedAddress, // [!code hl]
      amount: parseUnits('100', metadata.decimals), // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={burnBlocked.isPending} // [!code hl]
      onClick={handleBurnBlocked} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {burnBlocked.isPending ? 'Burning...' : 'Burn Blocked Tokens'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

## Best Practices

### Role Separation

Use different addresses for different roles to enhance security. For example, assign the issuer role to your treasury address for minting, and the pause role to your security team for emergency controls.

### Event Monitoring

Monitor onchain events for role changes, mints, burns, and administrative actions to maintain visibility into token operations and detect unauthorized activities.

### Emergency Procedures

Ensure pause and unpause roles are assigned to trusted addresses and that your team has documented procedures for responding to security incidents requiring token transfers to be halted.

## Learning Resources

<Cards>
  <Card description="Learn about the role-based access control system and all available roles" to="/protocol/tip20/spec#role-based-access-control" icon="lucide:shield" title="Role-Based Access Control" />

  <Card description="Learn how to configure transfer policies for compliance requirements" to="/protocol/tip403/spec" icon="lucide:file-text" title="Transfer Policies (TIP-403)" />
</Cards>

# Mint Stablecoins

Create new tokens by minting them to a specified address. Minting increases the total supply of your stablecoin.

## Steps

::::steps

### Create a Stablecoin

Before you can mint tokens, you need to create a stablecoin. Follow the [Create a Stablecoin](/guide/issuance/create-a-stablecoin) guide to deploy your token.

Once you've created your token, you can proceed to grant the issuer role and mint tokens.

### Grant the Issuer Role

Assign the issuer role to the address that will mint tokens. Minting requires the **`ISSUER_ROLE`**.

<Demo.Container name="Grant Issuer Role" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} last />
</Demo.Container>

:::code-group

```tsx twoslash [GrantIssuerRole.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function GrantIssuerRole() {
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const issuerAddress = '0x...' // Address to grant the issuer role

  const grant = Hooks.token.useGrantRolesSync({ // [!code hl]
    mutation: { // [!code hl]
      onSettled() { // [!code hl]
        queryClient.refetchQueries({ queryKey: ['hasRole'] }) // [!code hl]
      }, // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  const handleGrantIssuer = async () => { // [!code hl]
    await grant.mutate({ // [!code hl]
      token: tokenAddress, // [!code hl]
      roles: ['issuer'], // [!code hl]
      to: issuerAddress, // [!code hl]
      feeToken: '0x20c0000000000000000000000000000000000001', // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <button // [!code hl]
      disabled={grant.isPending} // [!code hl]
      onClick={handleGrantIssuer} // [!code hl]
      type="button" // [!code hl]
    > {/* [!code hl] */}
    {grant.isPending ? 'Granting...' : 'Grant Issuer Role'} {/* [!code hl] */}
    </button> {/* [!code hl] */}
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Mint Tokens to a Recipient

Now that the issuer role is granted, you can mint tokens to any address.

<Demo.Container name="Mint Tokens" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} />

  <Step.MintToken stepNumber={5} last />
</Demo.Container>

:::code-group

```tsx twoslash [MintToken.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'
import { parseUnits, pad, stringToHex } from 'viem'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function MintToken() {
  const { address } = useConnection()
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const [recipient, setRecipient] = React.useState<string>('')
  const [memo, setMemo] = React.useState<string>('')

  const { data: metadata } = Hooks.token.useGetMetadata({ // [!code hl]
    token: tokenAddress, // [!code hl]
  }) // [!code hl]

  const mint = Hooks.token.useMintSync({ // [!code hl]
    mutation: { // [!code hl]
      onSettled() { // [!code hl]
        queryClient.refetchQueries({ queryKey: ['getBalance'] }) // [!code hl]
      }, // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  const handleMint = () => { // [!code hl]
    if (!tokenAddress || !recipient || !metadata) return // [!code hl]
    mint.mutate({ // [!code hl]
      amount: parseUnits('100', metadata.decimals), // [!code hl]
      to: recipient as `0x${string}`, // [!code hl]
      token: tokenAddress, // [!code hl]
      memo: memo ? pad(stringToHex(memo), { size: 32 }) : undefined, // [!code hl]
      feeToken: '0x20c0000000000000000000000000000000000001', // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <>
      <div>
        <label>Recipient address</label>
        <input
          type="text"
          value={recipient}
          onChange={(e) => setRecipient(e.target.value)}
          placeholder="0x..."
        />
      </div>
      <div>
        <label>Memo (optional)</label>
        <input
          type="text"
          value={memo}
          onChange={(e) => setMemo(e.target.value)}
          placeholder="INV-12345"
        />
      </div>
      <button // [!code hl]
        disabled={!address || mint.isPending} // [!code hl]
        onClick={handleMint} // [!code hl]
        type="button" // [!code hl]
      > {/* [!code hl] */}
      {mint.isPending ? 'Minting...' : 'Mint'} {/* [!code hl] */}
      </button> {/* [!code hl] */}
    </>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

```solidity [Solidity]
TIP20 token = TIP20(0x20c0000000000000000000000000000000000004);

// Mint 1,000 tokens to the treasury (USD has 6 decimals)
address treasuryAddress = 0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef;
token.mint(treasuryAddress, 1_000_000_000);

// Mint with a memo for tracking
token.mintWithMemo(
  treasuryAddress,
  1_000_000_000,
  keccak256("Q1_2024_TREASURY_ALLOCATION")
);
```

```rust [Rust]
use alloy::{
    primitives::{address, keccak256, U256},
    providers::ProviderBuilder,
};
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let token = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000004"), // [!code focus]
        &provider, // [!code focus]
    ); // [!code focus]

    let treasury_address = address!("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"); // [!code focus]

    // Mint 1,000 tokens to the treasury (USD has 6 decimals)
    token // [!code focus]
        .mint(treasury_address, U256::from(1_000_000_000)) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    // Mint with a memo for tracking
    token // [!code focus]
        .mintWithMemo( // [!code focus]
            treasury_address, // [!code focus]
            U256::from(1_000_000_000), // [!code focus]
            keccak256("Q1_2024_TREASURY_ALLOCATION"), // [!code focus]
        ) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    println!("Tokens minted successfully"); // [!code focus]

    Ok(())
}
```

:::

::::

## Recipes

### Burning Stablecoins

To decrease supply, you can burn tokens from your own balance. Burning requires the **`ISSUER_ROLE`** and sufficient balance in the caller's account.

<Demo.Container name="Burn Your Token" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} />

  <Step.MintToken stepNumber={5} />

  <Step.BurnToken stepNumber={6} last />
</Demo.Container>

:::code-group

```tsx twoslash [BurnToken.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'
import { parseUnits, pad, stringToHex } from 'viem'
import { useQueryClient } from '@tanstack/react-query'

// @noErrors
export function BurnToken() {
  const { address } = useConnection()
  const queryClient = useQueryClient()
  const tokenAddress = '0x...' // Your token address
  const [memo, setMemo] = React.useState<string>('')

  const { data: metadata } = Hooks.token.useGetMetadata({ // [!code hl]
    token: tokenAddress, // [!code hl]
  }) // [!code hl]

  const burn = Hooks.token.useBurnSync({ // [!code hl]
    mutation: { // [!code hl]
      onSettled() { // [!code hl]
        queryClient.refetchQueries({ queryKey: ['getBalance'] }) // [!code hl]
      }, // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  const handleBurn = () => { // [!code hl]
    if (!tokenAddress || !address || !metadata) return // [!code hl]
    burn.mutate({ // [!code hl]
      amount: parseUnits('100', metadata.decimals), // [!code hl]
      token: tokenAddress, // [!code hl]
      memo: memo ? pad(stringToHex(memo), { size: 32 }) : undefined, // [!code hl]
      feeToken: '0x20c0000000000000000000000000000000000001', // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <>
      <div>
        <label>Memo (optional)</label>
        <input
          type="text"
          value={memo}
          onChange={(e) => setMemo(e.target.value)}
          placeholder="INV-12345"
        />
      </div>
      <button // [!code hl]
        disabled={!address || burn.isPending} // [!code hl]
        onClick={handleBurn} // [!code hl]
        type="button" // [!code hl]
      > {/* [!code hl] */}
      {burn.isPending ? 'Burning...' : 'Burn'} {/* [!code hl] */}
      </button> {/* [!code hl] */}
    </>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

```solidity [Solidity]
TIP20 token = TIP20(0x20c0000000000000000000000000000000000004);

// Burn 100 tokens from your own balance
token.burn(100_000_000);

// Burn with a memo for tracking
token.burnWithMemo(100_000_000, keccak256("REDEMPTION_Q1_2024"));
```

```rust [Rust]
use alloy::{
    primitives::{address, keccak256, U256},
    providers::ProviderBuilder,
};
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let token = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000004"), // [!code focus]
        &provider, // [!code focus]
    ); // [!code focus]

    // Burn 100 tokens from your own balance
    token // [!code focus]
        .burn(U256::from(100_000_000)) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    // Burn with a memo for tracking
    token // [!code focus]
        .burnWithMemo( // [!code focus]
            U256::from(100_000_000), // [!code focus]
            keccak256("REDEMPTION_Q1_2024"), // [!code focus]
        ) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    println!("Tokens burned successfully"); // [!code focus]

    Ok(())
}
```

:::

## Best Practices

### Monitor Supply Caps

If your token has a supply cap set, any `mint()` or `mintWithMemo()` call that would exceed the cap will revert with `SupplyCapExceeded()`. You must either:

* Burn tokens to reduce total supply below the cap
* Increase the supply cap (requires `DEFAULT_ADMIN_ROLE`)
* Remove the cap entirely by setting it to `type(uint256).max`

Use [`getMetadata`](https://viem.sh/tempo/actions/token.getMetadata) to check your token's total supply before minting.

### Role Separation

Assign the issuer role to dedicated treasury or minting addresses separate from your admin address. This enhances security by limiting the privileges of any single address.

## Learning Resources

<Cards>
  <Card description="Learn more about TIP-20 tokens on Tempo" to="/protocol/tip20/overview" icon="lucide:coins" title="TIP-20 Tokens" />

  <Card description="Learn about role-based access control and token management" to="/guide/issuance/manage-stablecoin" icon="lucide:shield" title="Manage Your Stablecoin" />
</Cards>

# Use Your Stablecoin for Fees

Enable users to pay transaction fees using your stablecoin. Tempo supports flexible fee payment options, allowing users to pay fees in any stablecoin they hold.

## Demo

<Demo.Container name="Use Your Stablecoin for Fees" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.GrantTokenRoles stepNumber={4} roles={['issuer']} />

  <Step.MintToken stepNumber={5} />

  <Step.MintFeeAmmLiquidity stepNumber={6} />

  <Step.PayWithIssuedToken stepNumber={7} last />
</Demo.Container>

## Steps

::::steps

### Create your stablecoin

First, create and mint your stablecoin by following the [Create a Stablecoin](/guide/issuance/create-a-stablecoin) guide.

### Add fee pool liquidity

Before users can pay fees with your token, you need to provide liquidity in the Fee AMM between your token and each of the tokens accepted by validators.

To determine which validator tokens are needed, sample recent blocks and check the miner's preferred fee token using `getValidatorToken` on the FeeManager contract. For example, on Moderato testnet, validators accept fees in pathUSD and AlphaUSD. On mainnet, this token mix is different and subject to change.

Add liquidity to your token's fee pool for each validator token:

:::code-group

```tsx twoslash [TypeScript]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'
import { useConnection } from 'wagmi'

const { address } = useConnection()
const yourToken = '0x...' // Your issued token address
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD on testnet

const mintFeeLiquidity = Hooks.amm.useMintSync() // [!code hl]

// Add 100 AlphaUSD of liquidity to the fee pool // [!code hl]
mintFeeLiquidity.mutate({ // [!code hl]
  feeToken: validatorToken,
  to: address,
  userTokenAddress: yourToken,
  validatorTokenAddress: validatorToken,
  validatorTokenAmount: parseUnits('100', 6),
}) // [!code hl]
```

```solidity [Solidity]
IFeeAMM feeAmm = IFeeAMM(TIP_FEE_AMM_ADDRESS);
address yourToken = 0x20c0000000000000000000000000000000000004; // Your issued token
address validatorToken = 0x20c0000000000000000000000000000000000001; // AlphaUSD

// Add 100 AlphaUSD of liquidity to the fee pool
feeAmm.mint(
  yourToken,
  validatorToken,
  100_000_000, // 100 tokens (6 decimals)
  address(this)
);
```

:::

You can also check your token's fee pool liquidity at any time:

:::code-group

```tsx twoslash [TypeScript]
// @noErrors
import { Hooks } from 'wagmi/tempo'

const { data: pool } = Hooks.amm.usePool({
  userToken: yourToken,
  validatorToken: '0x20c0000000000000000000000000000000000001', // AlphaUSD on testnet
})

const hasLiquidity = pool && pool.reserveValidatorToken > 0n
```

```solidity [Solidity]
IFeeAMM feeAmm = IFeeAMM(TIP_FEE_AMM_ADDRESS);
address yourToken = 0x20c0000000000000000000000000000000000004; // Your issued token
address validatorToken = 0x20c0000000000000000000000000000000000001; // AlphaUSD

// Get pool reserves
(uint256 reserveValidator, uint256 reserveUser) = feeAmm.getReserves(yourToken, validatorToken);

// Check if there's sufficient liquidity
require(reserveValidator > 0, "No liquidity available for fee conversion");
```

:::

If the pool has no liquidity (`reserveValidatorToken == 0`), you'll need to add liquidity to the fee pool before users can pay fees with your token. See the [Create a Stablecoin](/guide/issuance/create-a-stablecoin) guide for instructions on minting fee AMM liquidity.

### Send payment with your token as fee

Your users can send payments using your issued stablecoin as the fee token:

:::code-group

```tsx twoslash [PayWithIssuedToken.tsx]
import React from 'react'
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'
import { parseUnits, pad, stringToHex, isAddress } from 'viem'

// @noErrors
export function PayWithIssuedToken() {
  const { address } = useConnection()
  const [recipient, setRecipient] = React.useState<string>('')
  const [memo, setMemo] = React.useState<string>('')

  const feeToken = '0x...' // Your issued token address
  const paymentToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

  const { data: paymentBalance, refetch: paymentBalanceRefetch } = // [!code hl]
    Hooks.token.useGetBalance({ // [!code hl]
      account: address, // [!code hl]
      token: paymentToken, // [!code hl]
    }) // [!code hl]

  const { data: feeTokenBalance, refetch: feeTokenBalanceRefetch } = // [!code hl]
    Hooks.token.useGetBalance({ // [!code hl]
      account: address, // [!code hl]
      token: feeToken, // [!code hl]
    }) // [!code hl]

  const sendPayment = Hooks.token.useTransferSync({ // [!code hl]
    mutation: { // [!code hl]
      onSettled() { // [!code hl]
        paymentBalanceRefetch() // [!code hl]
        feeTokenBalanceRefetch() // [!code hl]
      }, // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  const isValidRecipient = recipient && isAddress(recipient)

  const handleTransfer = () => { // [!code hl]
    if (!isValidRecipient) return // [!code hl]
    sendPayment.mutate({ // [!code hl]
      amount: parseUnits('100', 6), // [!code hl]
      to: recipient as `0x${string}`, // [!code hl]
      token: paymentToken, // [!code hl]
      memo: memo ? pad(stringToHex(memo), { size: 32 }) : undefined, // [!code hl]
      feeToken, // Pay fees with your issued token // [!code hl]
    }) // [!code hl]
  } // [!code hl]

  return (
    <>
      <div>
        <label>Recipient address</label>
        <input
          type="text"
          value={recipient}
          onChange={(e) => setRecipient(e.target.value)}
          placeholder="0x..."
        />
      </div>
      <div>
        <label>Memo (optional)</label>
        <input
          type="text"
          value={memo}
          onChange={(e) => setMemo(e.target.value)}
          placeholder="INV-12345"
        />
      </div>
      <button // [!code hl]
        disabled={!address || !isValidRecipient || sendPayment.isPending} // [!code hl]
        onClick={handleTransfer} // [!code hl]
        type="button" // [!code hl]
      > {/* [!code hl] */}
      {sendPayment.isPending ? 'Sending...' : 'Send'} {/* [!code hl] */}
      </button> {/* [!code hl] */}
    </>
  )
}
```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({
    keyManager: KeyManager.localStorage(),
  })],
  transports: {
    [tempo.id]: http(),
  },
})
```

```solidity [Solidity]
ITIP20 token = ITIP20(0x20c0000000000000000000000000000000000001); // AlphaUSD
address yourToken = 0x20c0000000000000000000000000000000000004; // Your issued stablecoin
address recipient = 0xbeefcafe54750903ac1c8909323af7beb21ea2cb;

// Send payment using your token for fees
IFeeManager feeManager = IFeeManager(TIP_FEE_MANAGER_ADDRESS);
feeManager.setTransactionFeeToken(yourToken);
token.transfer(recipient, 100_000_000);
```

```rust [Rust]
use alloy::{
    primitives::{address, U256},
    providers::ProviderBuilder,
};
use tempo_alloy::{
    TempoNetwork,
    contracts::precompiles::{ITIPFeeAMM, TIP_FEE_MANAGER_ADDRESS},
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    // Your issued token
    let your_token = address!("0x20c0000000000000000000000000000000000004"); // [!code focus]
    // AlphaUSD
    let validator_token = address!("0x20c0000000000000000000000000000000000001"); // [!code focus]

    let fee_amm = ITIPFeeAMM::new( // [!code focus]
        TIP_FEE_MANAGER_ADDRESS, // [!code focus]
        &provider, // [!code focus]
    ); // [!code focus]

    let recipient = address!("0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef"); // [!code focus]

    // Add 100 AlphaUSD of liquidity to the fee pool
    fee_amm // [!code focus]
        .mint( // [!code focus]
            your_token, // [!code focus]
            validator_token, // [!code focus]
            U256::from(100_000_000), // [!code focus]
            recipient, // [!code focus]
        ) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    println!("Fee liquidity added successfully"); // [!code focus]

    Ok(())
}
```

:::

Users can set your stablecoin as their default fee token at the account level, or specify it for individual transactions. Learn more about [how users pay fees in different stablecoins](/guide/payments/pay-fees-in-any-stablecoin).

::::

## How It Works

When users pay transaction fees with your stablecoin, Tempo's fee system automatically handles the conversion if validators prefer a different token. The [Fee AMM](/protocol/fees/spec-fee-amm) ensures seamless fee payments across all supported stablecoins.

Users can select your stablecoin as their fee token through:

* **Account-level preference**: Set as default for all transactions
* **Transaction-level preference**: Specify for individual transactions
* **Automatic selection**: When directly interacting with your token contract

Learn more about [how users pay fees in different stablecoins](/guide/payments/pay-fees-in-any-stablecoin) and the complete [fee token preference hierarchy](/protocol/fees/spec-fee#fee-token-preferences).

## Benefits

* **User convenience**: Users can pay fees with the same token they're using
* **Liquidity**: Encourages users to hold your stablecoin
* **Flexibility**: Works seamlessly with Tempo's fee system

## Best Practices

### Monitor pool liquidity

Regularly check your token's fee pool reserves to ensure users can consistently pay fees with your stablecoin. Low liquidity can prevent transactions from being processed.

### Maintain adequate reserves

Keep sufficient validator token reserves in your fee pool to handle expected transaction volume. Consider your user base size and typical transaction frequency when determining reserve levels.

As fees accrue in your token, the pool will run low on validator tokens and need to be rebalanced. Use [`rebalanceSwap`](/guide/stablecoin-dex/managing-fee-liquidity#rebalance-liquidity) to replenish validator token reserves when they become depleted.

### Test before launch

Before promoting fee payments with your token, thoroughly test the flow on testnet:

1. Add liquidity to the fee pool
2. Verify users can set your token as their fee preference
3. Execute test transactions with various gas costs
4. Monitor that fee conversions work correctly

## Next Steps

<Cards>
  <Card description="Manage roles, supply caps, and transfer policies" to="/guide/issuance/manage-stablecoin" icon="lucide:settings" title="Manage Your Stablecoin" />

  <Card description="Add and remove liquidity to enable fee conversions" to="/guide/stablecoin-dex/managing-fee-liquidity" icon="lucide:droplet" title="Managing Fee Liquidity" />

  <Card description="Complete fee token specification" to="/protocol/fees/spec-fee" icon="lucide:file-text" title="Fee Tokens" />
</Cards>

# Installation

We provide three different installation paths - installing a pre-built binary, building from source or using our provided Docker image.

## Versions

The versions across networks may not be compatible, as such, please consult the table below on what version for what network you should be running.

| Network  | Version |
|----------|---------|
| Mainnet | v1.1.0 |
| Moderato (Testnet) | v1.1.0 |

## Pre-built Binary

```bash /dev/null/download.sh#L1-4
curl -L https://tempo.xyz/install | bash
tempo --version
```

To update Tempo in the future, simply run `tempoup`.

## Build from Source

```bash /dev/null/build.sh#L1-10
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Build and install from source using cargo
cargo install --git https://github.com/tempoxyz/tempo.git tempo --root /usr/local
tempo --version
```

## Docker

You can find the latest tagged version of Tempo at [the Tempo GHCR package](https://github.com/tempoxyz/tempo/pkgs/container/tempo).

```bash /dev/null/docker.sh#L1-4
# Pull the latest Docker image
docker pull ghcr.io/tempoxyz/tempo:<version>

# Run the Docker container
docker run -d --name tempo ghcr.io/tempoxyz/tempo:<version> --version
docker logs tempo
```

## Verifying Releases

All release artifacts are cryptographically signed starting after **v1.1.1**. We recommend verifying signatures before running any binary.

### Binary Signatures (GPG)

Release binaries are signed with GPG. The `tempoup` installer verifies signatures automatically when `gpg` is available.

To verify manually:

```bash
# Import the Tempo release signing key
gpg --keyserver keyserver.ubuntu.com --recv-keys EE3C5D41EA963E896F310EC3CBBFA54B20D33446

# Verify a downloaded binary
gpg --verify tempo-v1.1.0-x86_64-unknown-linux-gnu.tar.gz.asc \
    tempo-v1.1.0-x86_64-unknown-linux-gnu.tar.gz
```

A successful verification will show `Good signature from "Tempo Release Signing Key"`.

**Fingerprint:** `EE3C 5D41 EA96 3E89 6F31 0EC3 CBBF A54B 20D3 3446`

<details>
  <summary>Public Key</summary>

  ```
  -----BEGIN PGP PUBLIC KEY BLOCK-----

  mDMEaYXmJhYJKwYBBAHaRw8BAQdAa+cO3zz4+YQuPgUCNXSW7ApNTCAIwx9wBfPc
  lXyZBw20Xlp5Z2ltYW50YXMgTWFnZWxpbnNrYXMgKFRlbXBvIHJlbGVhc2Ugc2ln
  bmluZyBrZXkgZm9yIDIwMjYgYW5kIG9ud2FyZHMpIDx6eWdpbWFudGFzQHRlbXBv
  Lnh5ej6IkwQTFgoAOxYhBO48XUHqlj6JbzEOw8u/pUsg0zRGBQJpheYmAhsDBQsJ
  CAcCAiICBhUKCQgLAgQWAgMBAh4HAheAAAoJEMu/pUsg0zRGjJABAP8dy+gWx/E8
  EqzkKEUkEfLiRZ6n8APsc0aI5gqwfVAuAP99147oAq9cWVkNMh5PQmvdSG8MIx7Z
  G4OIGIHqFwKSCA==
  =o2TA
  -----END PGP PUBLIC KEY BLOCK-----
  ```

</details>

### Docker Image Signatures (Cosign)

Docker images are signed with [Cosign](https://docs.sigstore.dev/cosign/signing/overview/) using keyless signing via GitHub Actions OIDC.

To verify a Docker image:

```bash
# Install cosign: https://docs.sigstore.dev/cosign/system_config/installation/
cosign verify ghcr.io/tempoxyz/tempo:latest \
  --certificate-identity-regexp="https://github.com/tempoxyz/tempo/" \
  --certificate-oidc-issuer="https://token.actions.githubusercontent.com"
```

This verifies that the image was built and signed by the official Tempo CI pipeline.

### SHA256 Checksums

Every release archive includes a `.sha256` checksum file:

```bash
# Download the checksum file
curl -sSfLO https://github.com/tempoxyz/tempo/releases/download/v1.1.0/tempo-v1.1.0-x86_64-unknown-linux-gnu.tar.gz.sha256

# Verify
shasum -a 256 -c tempo-v1.1.0-x86_64-unknown-linux-gnu.tar.gz.sha256
```

# Network Upgrades and Releases

Tempo uses scheduled network upgrades to introduce protocol changes. Each upgrade goes through testnet activation before mainnet. This page also tracks important releases that node operators should be aware of.

For detailed release notes and binaries, see the [Changelog](/changelog).

## Required Node Operator Updates

| Release | Date | Network | Description | Priority |
|---------|------|---------|-------------|----------|
| [v1.4.0](https://github.com/tempoxyz/tempo/releases/tag/v1.4.0) | Mar 5, 2026 | Moderato + Mainnet | Required for T1C; introduces keychain signature migration so only V2 signatures and hashes are accepted after activation | <Badge variant="red">Required</Badge> |
| [v1.3.1](https://github.com/tempoxyz/tempo/releases/tag/v1.3.1) | Feb 22, 2026 | Testnet + Mainnet | Fixes high-load issues and finalizes T1A/T1B hardening for expiring nonce replay protection and keychain precompile gas handling | <Badge variant="red">Required</Badge> |
| [v1.2.0](https://github.com/tempoxyz/tempo/releases/tag/v1.2.0) | Feb 13, 2026 | Mainnet only | Fixes validation bug rejecting transactions with gas limits above ~16.7M, blocking large contract deployments | <Badge variant="red">Required</Badge> |

***

## T1C

| | |
|---|---|
| **Scope** | Security hardening, includes breaking change on keychain signatures |
| **Release** | [v1.4.0](https://github.com/tempoxyz/tempo/releases/tag/v1.4.0) |
| **Testnet** | Moderato: Mar 9, 2026 15:00 UTC (unix: 1773068400) |
| **Mainnet** | Mar 12, 2026 15:00 UTC (unix: 1773327600) |
| **Priority** | <Badge variant="red">Required</Badge> |

***

## T1A / T1B

| | |
|---|---|
| **Scope** | T1A removes the 16.7M per-transaction gas limit in favor of Tempo's 30M cap; T1B adds keychain precompile gas metering and expiring nonce replay-protection hardening |
| **TIPs** | T1A: [TIP-1010: Mainnet Gas Parameters](https://docs.tempo.xyz/protocol/tips/tip-1010); T1B: upgrade hardening release |
| **Release** | [v1.3.1](https://github.com/tempoxyz/tempo/releases/tag/v1.3.1) |
| **Testnet** | T1A + T1B: Feb 23, 2026 15:00 UTC (unix: 1771858800) |
| **Mainnet** | T1A: Feb 12, 2026 15:00 UTC (unix: 1770908400); T1B: Feb 23, 2026 15:00 UTC (unix: 1771858800) |
| **Priority** | <Badge variant="red">Required</Badge> |

***

## T1 (Bach)

| | |
|---|---|
| **Scope** | Mainnet-ready gas economics, expiring nonces, and security hardening |
| **TIPs** | [TIP-1000: State Creation Cost Increase](https://docs.tempo.xyz/protocol/tips/tip-1000), [TIP-1009: Expiring Nonces](https://docs.tempo.xyz/protocol/tips/tip-1009), [TIP-1010: Mainnet Gas Parameters](https://docs.tempo.xyz/protocol/tips/tip-1010) |
| **Testnet** | Feb 5, 2026 15:00 UTC (unix: 1770303600) — Release: [v1.1.0](https://github.com/tempoxyz/tempo/releases/tag/v1.1.0) |
| **Mainnet** | Feb 12, 2026 15:00 UTC (unix: 1770908400) — Release: [v1.1.1](https://github.com/tempoxyz/tempo/releases/tag/v1.1.1) |
| **Priority** | <Badge variant="red">Required</Badge> |

***

## T0 (Genesis)

| | |
|---|---|
| **Scope** | Initial mainnet launch |
| **Mainnet** | Jan 16, 2026 (genesis) — Release: [v1.0.0](https://github.com/tempoxyz/tempo/releases/tag/v1.0.0) |
| **Priority** | <Badge variant="red">Required</Badge> |

# Operate your validator

This guide covers day-to-day operations for running a Tempo validator in production.

## Validator states

Your validator moves through different states during operation. The transitions will happen only once on your validator's creation. Every state transition will happen on epoch boundaries in the happy case.

```mermaid
flowchart TD
    A[Inactive] -->|epoch ends| B["Syncer<br/>The validator starts syncing"]
    B -->|+1 epoch| C["Syncer and Player"]
    C -->|"+1 epoch, receives share"| D["Syncer<br/>Player<br/>Dealer"]
    D -->|"once fully synced"| E["Voter ↔ Proposer"]

    click A "#not-a-participant-e"
    click B "#syncer-epoch-e1"
    click C "#player-epoch-e2"
    click D "#dealer-epoch-e3"
    click E "#dealer-epoch-e3"
```

Currently, on mainnet and testnet, the epoch length is around 3 hours, which means that your validator will transition through these states approximately every 3 hours. If the epoch length ever changes, the transition times will also change.

#### Not a participant (E)

Epoch E marks the addition of your validator to the on-chain validator configuration smart contract. Your validator isn't considered a peer by validators yet. This is because the validator hasn't been refreshed in the current epoch yet. It is normal that no height metrics progress during this period, your node has to be considered
a syncer to receive blocks.

#### Syncer (epoch E+1)

Your validator is now considered a peer by validators. It's syncing with the network and will be considered a player in the next epoch.

#### Player (epoch E+2)

Your validator is receiving consensus signing shares from dealers during the ceremony.

#### Dealer (epoch E+3)

Your validator is distributing consensus signing shares to other validators during the ceremony. Once your node is fully synced up, it will also
be able to propose blocks and vote for other validators' proposed blocks.

#### Checking your validator's state

Monitor these metrics to track your validator's state:

```bash
# Is your validator connected to other peers (i.e. is it considered a syncer)? This should be >0 in at most 3 hours after your validator's addition
curl -s localhost:8002/metrics | grep consensus_network_spawner_connections

# How many times YOUR node has been a dealer (distributing shares) - this metric should be >0 over 6 hours
curl -s localhost:8002/metrics | grep consensus_engine_dkg_manager_how_often_dealer

# How many times YOUR node has been a player (receiving shares) - this metric should be >0 over 6 hours
curl -s localhost:8002/metrics | grep consensus_engine_dkg_manager_how_often_player

# Successful ceremonies (should increase every ~3 hours)
curl -s localhost:8002/metrics | grep consensus_engine_dkg_manager_ceremony_successes_total

# Failed ceremonies (should stay at 0 or increase rarely)
curl -s localhost:8002/metrics | grep consensus_engine_dkg_manager_ceremony_failures_total
```

If `how_often_dealer` or `how_often_player` is increasing, your node is actively participating in DKG ceremonies. After your validator has been added to the network, you should alert on these metrics, as they indicate that your validator is actively participating in the network.

If your validator is not connected to other peers, but at least 3 epochs have passed, please check that your node is properly configured - e.g. firewall settings are open to other peers. If you have reset your validator's state,
your validator might've been blocked due to double-signing a block. In that case, please reach out to the Tempo team.

### Consensus

#### Proposer

Your validator is currently the leader and proposing blocks. Check proposal activity:

```bash
# Number of blocks your node has built and resolved
curl -s localhost:9000/metrics | grep reth_payloads_resolved_block
```

If this counter is increasing, your validator is actively proposing blocks.

#### Voter

Your validator is voting on blocks proposed by others (notarization and finalization). This is the most common state.

```bash
# Inbound voting messages (should increase steadily)
curl -s localhost:8002/metrics | grep consensus_engine_epoch_manager_simplex_batcher_inbound_messages_total | grep data_0
```

This counter should increase steadily when your node is participating in consensus.

### Execution

#### Catching up

Your node is syncing historical blocks.

```bash
# Check sync stage
curl -s localhost:6060/metrics | grep reth_sync_checkpoint
```

If `reth_sync_checkpoint` shows stages other than `Finish`, you're still syncing.

#### Up to sync

Your node is fully synced and processing new blocks in real-time.

```bash
# Processed height should match or be close to finalized height
curl -s localhost:8002/metrics | grep -E "marshal_finalized_height|marshal_processed_height"
```

Both values should be nearly equal and increasing together.

## Node Lifecycle

### Starting and Stopping

Use `SIGINT` (Ctrl+C) or `SIGTERM` to gracefully stop the node:

```bash
# If running directly
kill -INT <pid>

# If running via systemd
sudo systemctl stop tempo
```

The node will finish processing the current block before shutting down. Avoid using `SIGKILL` as it may corrupt the database.

### Resetting your validator's data

:::danger
**You cannot reset a validator's data and continue with the same identity.** Doing so risks inconsistent voting, which can cause irrecoverable network safety failures.
:::

If you need to reset your validator's data, you must rotate to a new validator identity. This requires coordinating with the Tempo team to deactivate your old identity and register a new one.

## Key Management

### Signing Key Rotation

To rotate your validator's signing key:

1. Generate a new keypair:

```bash
tempo consensus generate-private-key --output <new-key-path>
tempo consensus calculate-public-key --private-key <new-key-path>
```

1. Contact the Tempo team to update your validator's public key on-chain

2. Once confirmed, update your node configuration to use the new key and restart. Once the node is running, your validator will go through the [validator lifecycle](/guide/node/operate-validator#validator-states).

:::warning
The old validator identity must be deactivated before the new one is activated
:::

### Signing Share Recovery

:::danger
**You cannot reset a validator's data and continue with the same identity.** Doing so risks inconsistent voting, which can cause irrecoverable network safety failures.
:::

If you lose your signing share (stored on the database in `<datadir>/consensus/`), you will need to rotate to a new validator identity. This requires coordinating with the Tempo team to deactivate your old identity and register a new one.
We're planning to release a high-availability feature that allows storing consensus data in an external database, which will enable signing share recovery without the need for key rotation.

### Deleting Signing Shares

:::warning\[Breaking Change in v1.1.0]
`--delete-signing-share` now requires the `--force` flag to prevent accidental deletion of validator signing keys. **Update any automation scripts that manage validator key lifecycle.**
:::

```bash
tempo consensus --delete-signing-share --force
```

## Log Management

### Parsing Logs

Tempo logs include ANSI escape codes for colors. To strip them for grep/awk:

```bash
# Strip colors when searching
sudo journalctl -u tempo | sed 's/\x1b\[[0-9;]*m//g' | grep "error"

# Or disable colors at runtime
RUST_LOG_STYLE=never tempo node ...
```

If you're using Loki, you can also use the `decolorize` filter to strip colors:

```
{job="tempo-node"} | decolorize
```

### Log Levels

Control verbosity with `RUST_LOG`:

```bash
# Default (info)
RUST_LOG=info

# Debug consensus only
RUST_LOG=info,tempo_commonware_node::consensus=debug

# Quiet mode (warnings and errors only)
RUST_LOG=warn
```

## Metrics glossary

This is a table of the most important metrics to watch on your validator node:

| Metric Name | Description | When to alert? | Meaning |
| --- | --- | --- | --- |
| `consensus_engine_dkg_manager_ceremony_successes_total` | Number of successful DKG ceremonies | Critical when it hasn't increased in 12 hours | Your node has participated in a successful DKG ceremony |
| `consensus_engine_dkg_manager_ceremony_failures_total` | Number of failed DKG ceremonies | Warning when it increases | Your node has failed to participate in a DKG ceremony |
| `consensus_engine_marshal_finalized_height` | Latest finalized height your node is aware of | Warning when it hasn't increased in 1 hour, critical when it hasn't increased in 3 hours | Your node is aware of the latest finalized height |
| `consensus_engine_marshal_processed_height` | Latest height your node has processed | Critical when it hasn't increased in an hour, warning when it's behind finalized height | Your node is processing blocks |
| `consensus_network_spawner_connections` | Number of active peers on the consensus layer | Warning when it's below the expected validator count, critical when it's 0 | Your node is connected to the consensus layer |
| `consensus_engine_epoch_manager_simplex_batcher_inbound_messages_total` | Number of inbound messages related to voting on the consensus layer | Warning when it's not increasing and your node is synced | Your node is receiving voting messages from the consensus layer |
| `reth_sync_checkpoint` | Current sync progress | Warning on when there are no changes in the `Finish` stage | Your node is syncing with the network |
| `reth_payloads_resolved_block` | Number of built and resolved payloads | Warning when it hasn't increased in 12 hours | Your node has built and resolved blocks |

## Grafana Dashboard

We provide a pre-built Grafana dashboard for monitoring your validator. It visualizes key metrics including node status, sync progress, voting activity, consensus latency, and execution performance.

### Importing the dashboard

1. Download the dashboard JSON from the [Tempo repository](https://github.com/tempoxyz/tempo/blob/main/contrib/grafana/dashboards/validator-health.json)

2. In Grafana, go to **Dashboards → Import**

3. Either paste the JSON content or upload the file

4. Select your Prometheus and Loki datasources when prompted

5. Click **Import**

### Dashboard variables

The dashboard uses these template variables:

| Variable | Description |
| --- | --- |
| `datasource` | Prometheus datasource |
| `loki_ds` | Loki datasource (for log-based panels) |
| `network_name` | Filter by network/validator job name |

Make sure your Prometheus is scraping metrics from your validator's metrics endpoint (default: `localhost:8002/metrics`).

# Running an RPC Node

RPC nodes provide API access to the Tempo network without participating in consensus.

## Quick Start

```bash /dev/null/quickstart.sh#L1-15
# Download snapshot (this will help you sync much faster)
tempo download

# Run node
tempo node \
  --follow \
  --http --http.port 8545 \
  --http.api eth,net,web3,txpool,trace
```

<Callout type="info">
  For mainnet, you have to use the credentials in `--follow` that are issued to you by the Tempo team.
</Callout>

An RPC node running in follow mode is a **full node**. It fetches blocks from a trusted RPC endpoint, executes every transaction locally through the EVM, validates each block after execution, and stores complete block data with full state. The only trust assumption is block ordering: your node trusts the RPC endpoint to provide the correct sequence of blocks. All execution and validation happens locally on your machine.

By default, RPC nodes run in archive mode, meaning they do not prune historical state.

## Manually downloading snapshots

Daily snapshots for the persistent testnet can be found at [https://snapshots.tempoxyz.dev](https://snapshots.tempoxyz.dev). You can extract them either using
`tempo download --url <snapshot_url>` or downloading them manually and extracting them using `curl <snapshot_url> | lz4 -d | tar -xzf -`.

## Example Systemd Service

```bash /dev/null/systemd.sh#L1-55
sudo tee /etc/systemd/system/tempo.service > /dev/null <<EOF
[Unit]
Description=Tempo RPC Node
After=network.target
Wants=network.target

[Service]
Type=simple
User=$USER
Group=$USER
Environment=RUST_LOG=info
WorkingDirectory=$HOME/tempo
ExecStart=/usr/local/bin/tempo node \\
  --datadir <datadir> \\
  --follow \\
  --http \\
  --http.addr 0.0.0.0 \\
  --http.port 8545 \\
  --http.api eth,net,web3,txpool,trace \\
  --metrics 9000 \\

Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=tempo
LimitNOFILE=infinity

[Install]
WantedBy=multi-user.target
EOF

# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable tempo
sudo systemctl start tempo

# Check status
sudo systemctl status tempo

# View logs
sudo journalctl -u tempo -f
```

## Monitoring

Once you've set up your node (whether it's with Systemd or Docker), you can verify that it's running correctly using these commands (`cast` requires installation of [Foundry](/sdk/foundry)):

```bash /dev/null/monitor.sh#L1-11
# Check service status
sudo systemctl status tempo

# Check peer connections (should be non-zero)
cast rpc net_peerCount --rpc-url http://localhost:8545

# Check block height (should be steadily increasing)
cast block-number --rpc-url http://localhost:8545
cast block --rpc-url http://localhost:8545

# Search logs
sudo journalctl -u tempo -n 1000 | grep -i "error"
```

In a production setting, you should monitor the [Reth metrics port](https://reth.rs/run/monitoring) using a tool like Prometheus or Grafana.

# System Requirements

These are the minimum and recommended system requirements for running a validator/RPC node.
It is likely, that the nodes will not require as much resources at the beginning of the chain,
but we still highly recommend to follow the recommended specifications. This will allow for future growth and scalability.

Consensus state can live on a lower performance volume (for example, EBS), but execution state needs NVMe storage.
If you want to separate them, use `--datadir` for execution data and `--consensus.datadir` for consensus data.

## RPC Node

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 16 cores | 32+ cores |
| **RAM** | 32 GB | 64 GB |
| **Storage** | 1000 GB NVMe | 2000 GB NVMe |
| **Network** | 1 Gbps | 10 Gbps |

## Validator Node

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 8 cores | 16+ cores |
| **RAM** | 16 GB | 32 GB |
| **Storage** | 100 GB NVMe | 1 TB NVMe |
| **Network** | 1 Gbps | 1 Gbps |

## Cloud provider recommendations

These dedicated servers meet or exceed the recommended specs for both RPC and validator nodes:

| Provider | Server | CPU | RAM | Storage |
|----------|--------|-----|-----|---------|
| OVH | Advance-4 | Intel Xeon-E 2386G (6c/12t) | 32 GB | 2× 512 GB NVMe |
| Hetzner | AX42 | AMD Ryzen 5 3600 (6c/12t) | 64 GB | 2× 512 GB NVMe |
| AWS | `c6id.8xlarge` | 32 vCPUs | 64 GB | 1.9 TB NVMe |

:::warning
Cloud instances with network-attached storage (e.g., AWS EBS) do not provide sufficient I/O performance. Use dedicated servers or instances with local NVMe storage.
:::

## Security measures

We do not recommend using a cloud firewall / NAT gateway as it can introduce additional complexity and performance issues. Instead, we've implemented security measures in the networking layer of the node, including:

* only accepting connections from trusted IP addresses (active validators on-chain)
* ratelimiting connections and messages in consensus and execution to prevent abuse
* only accepting consensus connections from validators that can prove their identity

## Ports

| Port | Protocol | Purpose | Expose |
|------|----------|---------|--------|
| 30303 | TCP/UDP | Execution P2P | Public |
| 8000 | TCP | Consensus P2P | Validators only |
| 8545 | TCP | HTTP RPC | Optional (internal for validators) |
| 8546 | TCP | WebSocket RPC | Optional (internal for validators) |
| 9000 | TCP | Metrics | Internal |

# Running a validator node

:::info
The management of the active validator set is currently permissioned by the Tempo team. If you are interested in becoming a validator, please [get in touch](mailto:partners@tempo.xyz) with the Tempo team.
:::

Validator nodes secure Tempo by validating blocks and transactions, then using [Threshold Simplex](https://docs.rs/commonware-consensus/0.0.61/commonware_consensus/threshold_simplex/index.html) to reach consensus. They distribute signing shares among themselves to collectively sign block approvals and finalizations.

## Cryptographic key hierarchy

All validators have two kinds of keys:

* signing key - this is an ED25519 keypair used to identify your validator amongst others
* signing share - this is a share of a BLS12-381 keypair used to sign block notarizations and finalizations

The signing key is static and can only be rotated by removing and re-creating a validator on-chain. The signing share is dynamic and is updated periodically on each DKG ceremony. Once updated, it will be saved to disk. Currently, the DKG ceremony is scheduled to run on-chain every ~3 hours.

## Generating a signing key

You can generate an ED25519 keypair using the following command:

```bash
tempo consensus generate-private-key --output <path>
```

Once the private key is generated, you can calculate/verify the public key by running:

```bash
tempo consensus calculate-public-key --private-key <path>
```

The public key should match the output of the `generate-private-key` command.

## Running the validator

The process for running a validator node is very similar to [running a full node](/guide/node/rpc).

You should start by downloading the latest snapshot using `tempo download --chain <moderato|mainnet|devnet>`. Downloading the snapshot allows your validator to start participating in consensus much faster.
Once you've downloaded the snapshot and have been whitelisted on-chain, you can proceed to run the validator node as such:

```bash
tempo node --datadir <datadir> \
    --chain moderato \
    --consensus.signing-key <path> \
    --consensus.fee-recipient <validator_wallet_address> \
    --telemetry-url <TELEMETRY_URL>
```

### Optional flags

| Flag | Description |
|------|-------------|
| `--telemetry-url <URL>` | Unified metrics and logs export. See [Telemetry endpoint](#telemetry-endpoint) below for details. **We ask all validators to configure this so we can support troubleshooting.** |
| `--telemetry-metrics-interval <DURATION>` | Interval for pushing metrics (default: `10s`). |
| `--consensus.datadir <PATH>` | Store consensus data on a separate volume (e.g., AWS EBS) while keeping execution state on high-performance local disks. Migrate by copying `<datadir>/consensus` to the new location. |

### Telemetry endpoint

The `--telemetry-url` flag enables unified telemetry export. It pushes two types of data to a Tempo-operated metrics backend:

* **Prometheus metrics** — execution-layer (reth) and consensus-layer metrics in Prometheus text format, pushed at a configurable interval (default every 10 seconds).
* **Structured logs** — operational logs exported via OTLP at `debug` level, covering consensus events, block processing, and sync progress.

The URL must include credentials: `--telemetry-url https://user:pass@metrics.example.com`

#### What is collected

| Category | Examples |
|----------|---------|
| Execution metrics | Block processing times, transaction pool size, peer count, sync status, database stats |
| Consensus metrics | Epoch and view progress, DKG ceremony status, proposal and finalization counts |
| Operational logs | Consensus state transitions, block proposals, sync progress, error events |

All consensus metrics are namespaced under a `consensus` prefix.

#### What is **not** collected

The telemetry endpoint does **not** collect any ambient information about the host machine. Specifically:

* No hostname, IP address, or machine identifiers
* No operating system, CPU, memory, or disk information
* No information about other processes or services running on the machine
* No file paths or directory structures beyond the node's own data directory references in logs
* No network topology or firewall configuration

The data is strictly limited to the node's own operational metrics and logs.

The notable difference between RPC nodes and validator nodes is the omission of the `--follow` argument and the addition of the `--consensus.signing-key` and `--consensus.fee-recipient` arguments. The fee recipient is the address that will receive transaction fees in your validators' proposed blocks.

Once your node is up, it may not start syncing immediately. This is because your node might not be part of the active set. In most cases, your validator will enter the active set in under 6 hours after the on-chain addition of the validator identity.

## Troubleshooting

### Checking if your node is proposing blocks

Once your node is proposing blocks, it will start emitting logs like these:

```
INFO handle_propose{epoch=18 view=387213 parent.view=387212 parent.digest=0x43885416b4a7ae7550c615ad4dc702045cd26540b78fa2bd75abdcbfbef02d9d}: tempo_commonware_node::consensus::application::actor: constructed proposal proposal.digest=0x6baa8fa813beea491cf598024d8b31cb2927e7ba1b92a29899a795dbafd682c6 proposal.height=5733680
```

If you do not see logs like these:

* please check that your validator is part of the active set, and is both [a player and a dealer](https://docs.tempo.xyz/guide/node/operate-validator#validator-states)
* please check that your node is synced up to the [latest block height](https://explorer.tempo.xyz/).
* please check that your outgoing IP address matches the one whitelisted on the validator smart contract:

```bash
tempo consensus validators-info --rpc-url <YOUR_RPC_URL>
```

# Accept a Payment

Accept stablecoin payments in your application. Learn how to receive payments, verify transactions, and reconcile payments using memos.

## Receiving Payments

Payments are automatically credited to the recipient's address when a transfer is executed. You don't need to do anything special to "accept" a payment, it happens automatically onchain.

In this basic receiving demo you can see the balances update after you add funds to your account, using the `getBalance` and `watchEvent` calls documented below.

<Demo.Container name="Receive a Payment" footerVariant="balances" tokens={[Token.alphaUsd, Token.betaUsd, Token.thetaUsd]} src="tempoxyz/examples/tree/main/examples/payments">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} last />
</Demo.Container>

## Verifying Payments

Check if a payment has been received by querying the token balance or listening for transfer events:

### Check Balance

:::code-group

```ts [TypeScript]
import { client } from './viem.config'

const balance = await client.token.getBalance({
  token: '0x20c0000000000000000000000000000000000001', // AlphaUSD
  address: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
})

console.log('Balance:', balance)
```

```rust [Rust]
use alloy::{primitives::address, providers::ProviderBuilder};
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let balance = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000001"), // Alpha USD // [!code focus]
        &provider, // [!code focus]
    ) // [!code focus]
    .balanceOf(address!("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb")) // [!code focus]
    .call() // [!code focus]
    .await?; // [!code focus]

    println!("Balance: {balance:?}"); // [!code focus]

    Ok(())
}
```

:::

### Listen for Transfer Events

:::code-group

```ts [TypeScript]
import { watchEvent } from 'viem'

// Watch for incoming transfers
const unwatch = watchEvent(client, {
  address: '0x20c0000000000000000000000000000000000001',
  event: {
    type: 'event',
    name: 'Transfer',
    inputs: [
      { name: 'from', type: 'address', indexed: true },
      { name: 'to', type: 'address', indexed: true },
      { name: 'value', type: 'uint256' },
    ],
  },
  onLogs: (logs) => {
    logs.forEach((log) => {
      if (log.args.to === yourAddress) {
        console.log('Received payment:', {
          from: log.args.from,
          amount: log.args.value,
        })
      }
    })
  },
})
```

```rust [Rust]
use alloy::{primitives::address, providers::ProviderBuilder};
use futures::StreamExt;
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    // Watch for incoming transfers // [!code focus]
    let mut transfers = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000001"), // [!code focus]
        &provider, // [!code focus]
    ) // [!code focus]
    .Transfer_filter() // [!code focus]
    .watch() // [!code focus]
    .await? // [!code focus]
    .into_stream(); // [!code focus]

    while let Some(Ok((payment, _))) = transfers.next().await { // [!code focus]
        println!("Received payment: {payment:?}") // [!code focus]
    } // [!code focus]

    Ok(())
}
```

:::

## Payment Reconciliation with Memos

If payments include memos (invoice IDs, order numbers, etc.), you can reconcile them automatically:

:::code-group

```ts [TypeScript]
// Watch for TransferWithMemo events
const unwatch = watchEvent(client, {
  address: tokenAddress,
  event: {
    type: 'event',
    name: 'TransferWithMemo',
    inputs: [
      { name: 'from', type: 'address', indexed: true },
      { name: 'to', type: 'address', indexed: true },
      { name: 'value', type: 'uint256' },
      { name: 'memo', type: 'bytes32', indexed: true },
    ],
  },
  onLogs: (logs) => {
    logs.forEach((log) => {
      if (log.args.to === yourAddress) {
        const invoiceId = log.args.memo
        // Mark invoice as paid in your database
        markInvoiceAsPaid(invoiceId, log.args.value)
      }
    })
  },
})
```

```rust [Rust]
use alloy::{primitives::address, providers::ProviderBuilder};
use futures::StreamExt;
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let mut transfers = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000001"), // [!code focus]
        &provider, // [!code focus]
    ) // [!code focus]
    .TransferWithMemo_filter() // [!code focus]
    .watch() // [!code focus]
    .await? // [!code focus]
    .into_stream(); // [!code focus]

    while let Some(Ok((transfer, _))) = transfers.next().await { // [!code focus]
        let invoice_id = transfer.memo; // [!code focus]
        println!("Transfer received with memo: {invoice_id:?}"); // [!code focus]
    } // [!code focus]

    Ok(())
}
```

:::

## Smart Contract Integration

If you're building a smart contract that accepts payments:

```solidity
contract PaymentReceiver {
    ITIP20 public token;
    mapping(bytes32 => bool) public paidInvoices;
    
    event PaymentReceived(
        address indexed payer,
        uint256 amount,
        bytes32 indexed invoiceId
    );
    
    function receivePayment(
        address payer,
        uint256 amount,
        bytes32 invoiceId
    ) external {
        require(!paidInvoices[invoiceId], "Invoice already paid");
        
        // Transfer tokens from payer to this contract
        token.transferFrom(payer, address(this), amount);
        
        paidInvoices[invoiceId] = true;
        emit PaymentReceived(payer, amount, invoiceId);
    }
}
```

## Payment Verification Best Practices

1. **Verify onchain**: Always verify payments onchain before marking orders as paid
2. **Use memos**: Request memos from payers to link payments to invoices or orders
3. **Check confirmations**: Wait for transaction finality (~1 second on Tempo) before processing
4. **Handle edge cases**: Account for partial payments, refunds, and failed transactions

## Cross-Stablecoin Payments

If you need to accept payments in a specific stablecoin but receive a different one, use the exchange to swap:

```ts
// User sends USDC, but you need USDT
// Swap USDC to USDT using the exchange
const { receipt } = await client.dex.sellSync({
  tokenIn: usdcAddress,
  tokenOut: usdtAddress,
  amountIn: receivedAmount,
  minAmountOut: receivedAmount * 99n / 100n, // 1% slippage
})
```

## Next Steps

* **[Send a payment](/guide/payments/send-a-payment)** to learn how to send payments
* Learn more about [Exchange](/guide/stablecoin-dex) for cross-stablecoin payments

# Pay Fees in Any Stablecoin

Configure users to pay transaction fees in any supported stablecoin. Tempo's flexible fee system allows users to pay fees with the same token they're using, eliminating the need to hold a separate gas token.

## Demo

By the end of this guide you will be able to pay fees in any stablecoin on Tempo.

<Demo.Container name="Pay Fees in Any Stablecoin" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.PayWithFeeToken stepNumber={3} feeToken={betaUsd} last />
</Demo.Container>

## Quick Snippet

Using a custom fee token is as simple as passing a `feeToken` attribute to mutable actions like `useTransferSync`, `useSendTransactionSync`, and more.

<Tabs stateKey="library" className="-mt-2">
  <Tab title="Wagmi">
    <div className="h-6" />

    ```tsx twoslash
    // @noErrors
    import { Hooks } from 'wagmi/tempo'
    import { parseUnits } from 'viem'

    const alphaUsd = '0x20c0000000000000000000000000000000000001'
    const betaUsd = '0x20c0000000000000000000000000000000000002'

    const sendPayment = Hooks.token.useTransferSync()

    sendPayment.mutate({ 
      amount: parseUnits('100', 6), 
      feeToken: betaUsd, // [!code ++]
      to: '0x0000000000000000000000000000000000000000', 
      token: alphaUsd, 
    }) 
    ```
  </Tab>

  <Tab title="Viem">
    <div className="h-6" />

    ```tsx twoslash
    // @noErrors
    import { parseUnits } from 'viem'
    import { client } from './viem.config'

    const alphaUsd = '0x20c0000000000000000000000000000000000001'
    const betaUsd = '0x20c0000000000000000000000000000000000002'

    const receipt = await client.token.transferSync({ 
      amount: parseUnits('100', 6), 
      feeToken: betaUsd, // [!code ++]
      to: '0x0000000000000000000000000000000000000000', 
      token: alphaUsd, 
    }) 
    ```
  </Tab>
</Tabs>

## Steps

<Tabs stateKey="library">
  <Tab title="Wagmi">
    ::::steps

    ### Set up Wagmi & integrate accounts

    Ensure that you have set up your project with Wagmi and integrated accounts by following either of the guides:

    * [Embed Passkey accounts](/guide/use-accounts/embed-passkeys)
    * [Connect to wallets](/guide/use-accounts/connect-to-wallets)

    ### Add testnet funds¹

    Before you can pay fees in a token of your choice, you need to fund your account. In this guide you will be sending `AlphaUSD` (`0x20c000…0001`) and paying fees in `BetaUSD` (`0x20c000…0002`).

    The built-in Tempo testnet faucet includes `AlphaUSD` and `BetaUSD` when funding.

    <Demo.Container name="Add Funds" footerVariant="balances" showBadge={false} tokens={[Demo.alphaUsd, Demo.betaUsd, Demo.thetaUsd, Demo.pathUsd]}>
      <Step.AddFunds stepNumber={1} last />
    </Demo.Container>

    :::code-group

    ```tsx twoslash [AddFunds.ts]
    // @noErrors
    import { Hooks } from 'wagmi/tempo'
    import { useConnection } from 'wagmi'

    function AddFunds() {
      const { address } = useConnection()
      const { mutate, isPending } = Hooks.faucet.useFundSync()

      return (
        <button onClick={() => mutate({ account: address })} disabled={isPending}>
          Add Funds
        </button>
      )
    }
    ```

    ```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
    // @noErrors
    // [!include ~/snippets/wagmi.config.ts:setup]
    ```

    :::

    :::warning
    ¹ It is important to note that the `addFunds` Hook only works on testnets as a convenience feature to get
    started quickly. For production, you will need to onramp & fund your account manually.
    :::

    ### Add pay with fee token logic

    Now that you have `AlphaUSD` to send and `BetaUSD` to pay fees with, you can add a form that allows users to select a fee token and send a payment.

    After this step, your users can send payments with a specified fee token by clicking the "Send Payment" button!

    <Demo.Container name="Pay Fees in Any Stablecoin" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
      <Step.AddFunds stepNumber={1} />

      <Step.PayWithFeeToken stepNumber={2} last />
    </Demo.Container>

    :::code-group

    ```tsx twoslash [PayWithFeeToken.tsx]
    import { Hooks } from 'wagmi/tempo'
    import { parseUnits } from 'viem'

    const alphaUsd = '0x20c0000000000000000000000000000000000001'
    const betaUsd = '0x20c0000000000000000000000000000000000002'
    const thetaUsd = '0x20c0000000000000000000000000000000000003'
    const pathUsd = '0x20c0000000000000000000000000000000000000'

    // @noErrors
    function PayWithFeeToken() {
      const sendPayment = Hooks.token.useTransferSync()
      const metadata = Hooks.token.useGetMetadata({
        token: alphaUsd,
      })

      return (
        <form onSubmit={
          (event) => {
            event.preventDefault()
            const formData = new FormData(event.target as HTMLFormElement)

            const recipient = (formData.get('recipient') ||
              '0x0000000000000000000000000000000000000000') as `0x${string}`
            const feeToken = (formData.get('feeToken') ||
              alphaUsd) as `0x${string}`

            sendPayment.mutate({ // [!code hl]
              amount: parseUnits('100', metadata.data?.decimals ?? 6), // [!code hl]
              to: recipient, // [!code hl]
              token: alphaUsd, // [!code hl]
              feeToken: feeToken, // [!code hl]
            }) // [!code hl]
          }
        }>
          <div>
            <label htmlFor="recipient">Recipient address</label>
            <input type="text" name="recipient" placeholder="0x..." />
          </div>
          <div>
            <label htmlFor="feeToken">Fee token</label>
            <select name="feeToken">
              <option value={alphaUsd}>AlphaUSD</option>
              <option value={betaUsd}>BetaUSD</option>
              <option value={thetaUsd}>ThetaUSD</option>
              <option value={pathUsd}>pathUSD</option>
            </select>
          </div>
          <button type="submit" disabled={sendPayment.isPending}>
            Send Payment
          </button>
        </form>
      )
    }
    ```

    ```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
    // @noErrors
    // [!include ~/snippets/wagmi.config.ts:setup]
    ```

    :::

    ### Display a receipt

    Now that users can send payments with a specified fee token, you can link to the transaction receipt.

    :::code-group

    ```tsx twoslash [PayWithFeeToken.tsx]
    import { Hooks } from 'wagmi/tempo'
    import { parseUnits } from 'viem'

    const alphaUsd = '0x20c0000000000000000000000000000000000001'
    const betaUsd = '0x20c0000000000000000000000000000000000002'
    const thetaUsd = '0x20c0000000000000000000000000000000000003'
    const pathUsd = '0x20c0000000000000000000000000000000000000'

    // @noErrors
    function PayWithFeeToken() {
      const sendPayment = Hooks.token.useTransferSync()
      const metadata = Hooks.token.useGetMetadata({
        token: alphaUsd,
      })

      return (
        <>
          {/* ... your payment form ... */}
          {sendPayment.data && ( // [!code ++]
            <a href={`https://explore.tempo.xyz/tx/${sendPayment.data.receipt.transactionHash}`}> {/* [!code ++] */}
              View receipt {/* [!code ++] */}
            </a> {/* [!code ++] */}
          )} {/* [!code ++] */}
        </>
      )
    }
    ```

    ```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
    // @noErrors
    // [!include ~/snippets/wagmi.config.ts:setup]
    ```

    :::

    ### Next steps

    Now that you have made a payment using a desired fee token, you can:

    * Follow a guide on how to [sponsor user fees](/guide/payments/sponsor-user-fees) to enable gasless transactions
    * Learn more about [transaction fees](/protocol/fees)

    ::::
  </Tab>

  <Tab title="Viem">
    ::::steps

    ### Set up Viem Client

    First, we will set up a Viem client configured with Tempo.

    ```ts twoslash [viem.config.ts]
    // [!include ~/snippets/viem.config.ts:setup]
    ```

    :::info

    For simplicity of the guide, this example uses a Private Key (Secp256k1) account instead of Passkeys (WebAuthn).

    :::

    ### Add testnet funds¹

    Before you can pay fees in a token of your choice, you need to fund your account. In this guide you will be sending `AlphaUSD` (`0x20c000…0001`) and paying fees in `BetaUSD` (`0x20c000…0002`).

    The built-in Tempo testnet faucet includes `AlphaUSD` and `BetaUSD` when funding.

    <Demo.Container name="Add Funds" footerVariant="balances" showBadge={false} tokens={[Demo.alphaUsd, Demo.betaUsd, Demo.thetaUsd, Demo.pathUsd]}>
      <Step.AddFunds stepNumber={1} last />
    </Demo.Container>

    :::code-group

    ```tsx twoslash [example.ts]
    // @noErrors
    import { client } from './viem.config'

    await client.faucet.fundSync({
      account: client.account,
    })
    ```

    ```tsx twoslash [viem.config.ts] filename="viem.config.ts"
    // @noErrors
    // [!include ~/snippets/viem.config.ts:setup]
    ```

    :::

    ### Add pay with fee token logic

    Now that you have `AlphaUSD` to send and `BetaUSD` to pay fees with, you can now add logic to send a payment with a specified fee token.

    <Demo.Container name="Pay Fees in Any Stablecoin" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
      <Step.AddFunds stepNumber={1} />

      <Step.PayWithFeeToken stepNumber={2} last />
    </Demo.Container>

    :::code-group

    ```tsx twoslash [example.ts]
    // @noErrors
    import { client } from './viem.config'

    const receipt = await client.token.transferSync({
      amount: parseUnits('100', 6),
      feeToken: betaUsd, // [!code hl]
      to: '0x0000000000000000000000000000000000000000',
      token: alphaUsd,
    })
    ```

    ```tsx twoslash [viem.config.ts] filename="viem.config.ts"
    // @noErrors
    // [!include ~/snippets/viem.config.ts:setup]
    ```

    :::

    ::::
  </Tab>
</Tabs>

# Recipes

## Set user fee token

You can also set a persistent default fee token for an account, so users don't need to specify `feeToken` on every transaction. Learn more about fee token preferences [here](/protocol/fees/spec-fee#fee-token-preferences).

<Tabs stateKey="library" className="-mt-2">
  <Tab title="Wagmi">
    <div className="h-6" />

    ```tsx twoslash
    // @noErrors
    // [!include ~/snippets/unformatted/fee.setUserToken.ts:wagmi-hooks]
    ```
  </Tab>

  <Tab title="Viem">
    <div className="h-6" />

    ```ts twoslash
    // @noErrors
    // [!include ~/snippets/unformatted/fee.setUserToken.ts:viem]
    ```
  </Tab>
</Tabs>

## Learning Resources

<Cards>
  <Card description="Learn more about transaction fees on Tempo" to="/protocol/fees" icon="lucide:coins" title="Transaction Fees" />
</Cards>

# Send a Payment

Send stablecoin payments between accounts on Tempo. Payments can include optional memos for reconciliation and tracking.

## Demo

By the end of this guide you will be able to send payments on Tempo with an optional memo.

<Demo.Container name="Send a Payment" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.SendPayment stepNumber={3} last />
</Demo.Container>

## Steps

::::steps

### Set up Wagmi & integrate accounts

Ensure that you have set up your project with Wagmi and integrated accounts by following either of the guides:

* [Embed Passkey accounts](/guide/use-accounts/embed-passkeys)
* [Connect to wallets](/guide/use-accounts/connect-to-wallets)

### Add testnet funds¹

Before you can send a payment, you need to fund your account. In this guide you will be sending `AlphaUSD` (`0x20c000…0001`).

The built-in Tempo testnet faucet funds accounts with `AlphaUSD`.

<Demo.Container name="Add Funds" footerVariant="balances" showBadge={false} tokens={[Demo.alphaUsd]}>
  <Step.AddFunds stepNumber={1} last />
</Demo.Container>

:::code-group

```tsx twoslash [AddFunds.ts]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { useConnection } from 'wagmi'

function AddFunds() {
  const { address } = useConnection()
  const { mutate, isPending } = Hooks.faucet.useFundSync()

  return (
    <button onClick={() => mutate({ account: address })} disabled={isPending}>
      Add Funds
    </button>
  )
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

:::warning
¹ It is important to note that the `addFunds` Hook only works on testnets as a convenience feature to get
started quickly. For production, you will need to onramp & fund your account manually.
:::

### Add send payment logic

Now that you have `AlphaUSD` you are ready to add logic to send a payment with an optional memo.

<Demo.Container name="Send Payment" footerVariant="balances" showBadge={false} tokens={[Demo.alphaUsd]}>
  <Step.AddFunds stepNumber={1} />

  <Step.SendPayment stepNumber={2} last />
</Demo.Container>

:::code-group

```tsx twoslash [SendPaymentWithMemo.tsx]
import { Hooks } from 'wagmi/tempo'
import { parseUnits, stringToHex, pad } from 'viem'

// @noErrors
function SendPaymentWithMemo() {
  const sendPayment = Hooks.token.useTransferSync() // [!code hl]

  return (
    <form onSubmit={
      (event) => {
        event.preventDefault()
        const formData = new FormData(event.target as HTMLFormElement)

        const recipient = (formData.get('recipient') ||
          '0x0000000000000000000000000000000000000000') as `0x${string}`
        const memo = (formData.get('memo') || '') as string

        sendPayment.mutate({ // [!code hl]
          amount: parseUnits('100', 6), // [!code hl]
          to: recipient, // [!code hl]
          token: '0x20c0000000000000000000000000000000000001', // [!code hl]
          memo: memo ? pad(stringToHex(memo), { size: 32 }) : undefined, // [!code hl]
        }) // [!code hl]
      }
    }>
      <div>
        <label htmlFor="recipient">Recipient address</label>
        <input type="text" name="recipient" placeholder="0x..." />
      </div>
      <div>
        <label htmlFor="memo">Memo (optional)</label>
        <input type="text" name="memo" placeholder="Optional memo" />
      </div>
      <button // [!code hl]
        type="submit" // [!code hl]
        disabled={sendPayment.isPending} // [!code hl]
      > {/* [!code hl] */}
        Send Payment {/* [!code hl] */}
      </button> {/* [!code hl] */}
    </form>
  )
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Display receipt

Now that you can send a payment, you can display the transaction receipt on success.

:::code-group

```tsx twoslash [SendPaymentWithMemo.tsx]
import { Hooks } from 'wagmi/tempo'
import { parseUnits, stringToHex, pad } from 'viem'

// @noErrors
function SendPaymentWithMemo() {
  const sendPayment = Hooks.token.useTransferSync()

  return (
    <>
      {/* ... your payment form ... */}
      {sendPayment.data && ( // [!code ++]
        <a href={`https://explore.tempo.xyz/tx/${sendPayment.data.receipt.transactionHash}`}> {/* [!code ++] */}
          View receipt {/* [!code ++] */}
        </a> {/* [!code ++] */}
      )} {/* [!code ++] */}
    </>
  )
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Next steps

Now that you have made a payment you can

* **[Accept a payment](/guide/payments/accept-a-payment)** to receive payments in your application
* Learn about [Batch Transactions](/guide/use-accounts/batch-transactions)
* Send a payment [with a specific fee token](/guide/payments/pay-fees-in-any-stablecoin)

  ::::

## Recipes

### Basic transfer

Send a payment using the standard `transfer` function:

:::code-group

```ts [example.ts]
import { parseUnits } from 'viem'
import { client } from './viem.config'

const { receipt } = await client.token.transferSync({
  amount: parseUnits('100', 6), // 100 tokens (6 decimals)
  to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
  token: '0x20c0000000000000000000000000000000000001', // AlphaUSD
})
```

```ts [viem.config.ts] filename="viem.config.ts"
// [!include ~/snippets/viem.config.ts:setup]
```

```rs [Rust]
use alloy::{
    primitives::{address, U256},
    providers::ProviderBuilder,
};
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let token = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000001"), // AlphaUSD // [!code focus]
        &provider, // [!code focus]
    ); // [!code focus]

    let receipt = token // [!code focus]
        .transfer( // [!code focus]
            address!("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb"), // [!code focus]
            U256::from(100_000_000), // 100 tokens (6 decimals) // [!code focus]
        ) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    println!("Transfer successful: {:?}", receipt.transaction_hash); // [!code focus]

    Ok(())
}
```

:::

### Transfer with memo

Include a memo for payment reconciliation and tracking:

:::code-group

```ts [example.ts]
import { parseUnits } from 'viem'
import { client } from './viem.config'

const invoiceId = pad(stringToHex('INV-12345'), { size: 32 })

const { receipt } = await client.token.transferSync({
  amount: parseUnits('100', 6),
  to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
  token: '0x20c0000000000000000000000000000000000001',
  memo: invoiceId,
})
```

```ts [viem.config.ts] filename="viem.config.ts"
// [!include ~/snippets/viem.config.ts:setup]
```

```rs [Rust]
use alloy::{
    primitives::{address, B256, U256},
    providers::ProviderBuilder,
};
use tempo_alloy::{TempoNetwork, contracts::precompiles::ITIP20};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let token = ITIP20::new( // [!code focus]
        address!("0x20c0000000000000000000000000000000000001"), // AlphaUSD // [!code focus]
        &provider, // [!code focus]
    ); // [!code focus]

    let receipt = token // [!code focus]
        .transferWithMemo( // [!code focus]
            address!("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb"), // [!code focus]
            U256::from(100_000_000), // 100 tokens (6 decimals) // [!code focus]
            B256::left_padding_from("INV-12345".as_bytes()), // [!code focus]
        ) // [!code focus]
        .send() // [!code focus]
        .await? // [!code focus]
        .get_receipt() // [!code focus]
        .await?; // [!code focus]

    println!("Transfer successful: {:?}", receipt.transaction_hash); // [!code focus]

    Ok(())
}
```

:::

The memo is a 32-byte value that can store payment references, invoice IDs, order numbers, or any other metadata.

### Using Solidity

If you're building a smart contract that sends payments:

```solidity
interface ITIP20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferWithMemo(address to, uint256 amount, bytes32 memo) external;
}

contract PaymentSender {
    ITIP20 public token;
    
    function sendPayment(address recipient, uint256 amount) external {
        token.transfer(recipient, amount);
    }
    
    function sendPaymentWithMemo(
        address recipient, 
        uint256 amount, 
        bytes32 invoiceId
    ) external {
        token.transferWithMemo(recipient, amount, invoiceId);
    }
}
```

### Batch payment transactions

Send multiple payments in a single transaction using batch transactions:

:::code-group

```ts [example.ts]
import { encodeFunctionData, parseUnits } from 'viem'
import { Abis } from 'viem/tempo'
import { client } from './viem.config'

const tokenABI = Abis.tip20
const recipient1 = '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb'
const recipient2 = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'

const calls = [
  {
    to: '0x20c0000000000000000000000000000000000001', // AlphaUSD address
    data: encodeFunctionData({
      abi: tokenABI,
      functionName: 'transfer',
      args: [recipient1, parseUnits('100', 6)],
    }),
  },
  {
    to: '0x20c0000000000000000000000000000000000001',
    data: encodeFunctionData({
      abi: tokenABI,
      functionName: 'transfer',
      args: [recipient2, parseUnits('50', 6)],
    }),
  },
]

const hash = await client.sendTransaction({ calls })
```

```ts [viem.config.ts] filename="viem.config.ts"
// [!include ~/snippets/viem.config.ts:setup]
```

```rust [Rust]
use alloy::{
    primitives::{address, Address, U256},
    providers::{Provider, ProviderBuilder},
    sol_types::SolCall,
};
use tempo_alloy::{
    TempoNetwork, contracts::precompiles::ITIP20, primitives::transaction::Call,
    rpc::TempoTransactionRequest,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let provider = ProviderBuilder::new_with_network::<TempoNetwork>()
        .connect(&std::env::var("RPC_URL").expect("No RPC URL set"))
        .await?;

    let recipient1 = address!("0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb"); // [!code focus]
    let recipient2 = address!("0x70997970C51812dc3A010C7d01b50e0d17dc79C8"); // [!code focus]
    let token_address: Address = address!("0x20c0000000000000000000000000000000000001"); // [!code focus]

    let calls = vec![ // [!code focus]
        Call { // [!code focus]
            to: token_address.into(), // [!code focus]
            input: ITIP20::transferCall { // [!code focus]
                to: recipient1, // [!code focus]
                amount: U256::from(100_000_000), // [!code focus]
            } // [!code focus]
            .abi_encode() // [!code focus]
            .into(), // [!code focus]
            value: U256::ZERO, // [!code focus]
        }, // [!code focus]
        Call { // [!code focus]
            to: token_address.into(), // [!code focus]
            input: ITIP20::transferCall { // [!code focus]
                to: recipient2, // [!code focus]
                amount: U256::from(50_000_000), // [!code focus]
            } // [!code focus]
            .abi_encode() // [!code focus]
            .into(), // [!code focus]
            value: U256::ZERO, // [!code focus]
        }, // [!code focus]
    ]; // [!code focus]

    let pending = provider // [!code focus]
        .send_transaction(TempoTransactionRequest { // [!code focus]
            calls, // [!code focus]
            ..Default::default() // [!code focus]
        }) // [!code focus]
        .await?; // [!code focus]
    let tx_hash = pending.tx_hash(); // [!code focus]

    println!("Batch transaction sent: {tx_hash:?}"); // [!code focus]

    Ok(())
}
```

:::

### Payment events

When you send a payment, the token contract emits events:

* **Transfer**: Standard ERC-20 transfer event
* **TransferWithMemo**: Additional event with memo (if using `transferWithMemo`)

You can filter these events to track payments in your off-chain systems.

## Best practices

### Loading state

Users should see a loading state when the payment is being processed.

You can use the `isPending` property from the `useTransferSync` hook to show pending state to the user.

### Error handling

If an error unexpectedly occurs, you can display an error message to the user by using the `error` property from the `useTransferSync` hook.

```tsx
import { Hooks } from 'wagmi/tempo'

function SendPayment() {
  const sendPayment = Hooks.token.useTransferSync()

  return (
    <>
      {/* ... your paymentform ... */}
      {sendPayment.error && <div>Error: {sendPayment.error.message}</div>}
    </>
  )
}
```

## Learning resources

<Cards>
  <Card description="Learn more about the TypeScript SDK" to="/sdk/typescript" icon="lucide:code" title="TypeScript SDK" />

  <Card description="Learn more about transactions on Tempo" to="/protocol/transactions" icon="lucide:send" title="Transactions" />
</Cards>

# Send Parallel Transactions

Tempo enables concurrent transaction execution through its [expiring nonce](/guide/tempo-transaction#expiring-nonces) system. Unlike traditional sequential nonces that require transactions to be processed one at a time, expiring nonces allow multiple transactions to be submitted simultaneously without nonce conflicts. Each transaction uses an independent nonce that automatically expires after a set time window, enabling true parallel execution.

## Demo

By the end of this guide you will understand how to send parallel payments using expiring nonces under-the-hood.

<Demo.Container name="Send Parallel Payments" footerVariant="balances" tokens={[Token.alphaUsd]}>
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.SendParallelPayments stepNumber={3} />
</Demo.Container>

## Steps

::::steps

### Set up Wagmi & integrate accounts

Ensure that you have set up your project with Wagmi and integrated accounts by following either of the guides:

* [Embed Passkey accounts](/guide/use-accounts/embed-passkeys)
* [Connect to wallets](/guide/use-accounts/connect-to-wallets)

### Send concurrent transactions with nonce keys

To send multiple transactions in parallel, simply batch them together. [Expiring nonces](/guide/tempo-transaction#expiring-nonces) are attached to each transaction automatically.

:::code-group

```ts twoslash [example.ts]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'

const { mutate: transfer } = Hooks.token.useTransferSync()

// Send both transfers in parallel. // [!code focus]
const [receipt1, receipt2] = await Promise.all([ // [!code focus]
  transfer.mutate({ // [!code focus]
    amount: parseUnits('100', 6), // [!code focus]
    to: '0x70997970C51812dc3A010C7d01b50e0d17dc79C8', // [!code focus]
    token: alphaUsd, // [!code focus]
  }), // [!code focus]
  transfer.mutate({ // [!code focus]
    amount: parseUnits('50', 6), // [!code focus]
    to: '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC', // [!code focus]
    token: alphaUsd, // [!code focus]
  }), // [!code focus]
]) // [!code focus]

console.log('Transaction 1:', receipt1.transactionHash) // [!code focus]
console.log('Transaction 2:', receipt2.transactionHash) // [!code focus]
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

::::

## Learning Resources

<Cards>
  <Card description="Learn more about expiring nonces that power concurrent transactions." to="/guide/tempo-transaction#expiring-nonces" icon="lucide:timer" title="Expiring Nonces" />

  <Card description="Learn more about Tempo Transactions and their properties." to="/protocol/transactions" icon="lucide:send" title="Transactions" />
</Cards>

# Sponsor User Fees

Enable gasless transactions by sponsoring transaction fees for your users. Tempo's native fee sponsorship allows applications to pay fees on behalf of users, improving UX and removing friction from payment flows.

## Demo

<Demo.Container name="Sponsor User Fees" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.SendRelayerSponsoredPayment stepNumber={3} last />
</Demo.Container>

## Steps

::::steps

### Set up the fee payer service

:::tip
Tempo provides a public testnet fee payer service at `https://sponsor.moderato.tempo.xyz` that you can use for development and testing. If you want to run your own, follow the instructions below.
:::

You can stand up a minimal fee payer service using the `Handler.feePayer` handler provided by the Tempo TypeScript SDK ([link](/sdk/typescript/server/handler.feePayer)). To sponsor transactions, you need a funded account that will act as the fee payer.

```ts twoslash [server.ts]
// @noErrors
// [!include ~/snippets/unformatted/withFeePayer.ts:server]
```

### Configure your client to use the fee payer service

Use the `withFeePayer` transport provided by Viem ([link](https://viem.sh/tempo/transports/withFeePayer)). It routes transactions to the configured fee payer service for sponsorship when `feePayer: true` is requested on a transaction.

<PublicTestnetSponsorTip />

```ts twoslash [wagmi.config.ts]
// @noErrors
// [!include ~/snippets/wagmi.config.ts:withFeePayer]
```

### Sponsor your user's transactions

Now you can sponsor transactions by passing `feePayer: true` in the transaction parameters. For more details on how to send a transaction, see the [Send a payment](/guide/payments/send-a-payment) guide.

:::info
You can also sponsor transactions with a local account. See the [recipe below](/guide/payments/sponsor-user-fees#local-account-sponsorship) for more details.
:::

:::code-group

```tsx twoslash [SendSponsoredPayment.tsx] filename="SendSponsoredPayment.tsx"
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'

const alphaUsd = '0x20c0000000000000000000000000000000000001'

// @noErrors
function SendSponsoredPayment() {
  const sponsorAccount = privateKeyToAccount('0x...')
  const sendPayment = Hooks.token.useTransferSync() // [!code hl]
  const metadata = Hooks.token.useGetMetadata({
    token: alphaUsd,
  })

  return (
    <form onSubmit={
      (event) => {
        event.preventDefault()
        const formData = new FormData(event.target as HTMLFormElement)

        const recipient = (formData.get('recipient') ||
          '0x0000000000000000000000000000000000000000') as `0x${string}`

        sendPayment.mutate({ // [!code hl]
          amount: parseUnits('100', metadata.data.decimals), // [!code hl]
          feePayer: true, // [!code focus]
          to: recipient, // [!code hl]
          token: alphaUsd, // [!code hl]
        }) // [!code hl]
      }
    }>
      <div>
        <label htmlFor="recipient"> Recipient address </label>
        <input type="text" placeholder="0x..." />
      </div>
      <button type="submit" disabled={sendPayment.isPending}>
        Send Payment
      </button>
    </form>
  )
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:withFeePayer]
```

:::

## Next Steps

Now that you've implemented fee sponsorship, you can:

* Learn more about the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction#fee-payer-signature-details) type and fee payer signature details
* Explore [Batch Transactions](/guide/use-accounts/batch-transactions) to sponsor multiple operations at once
* Learn how to [Pay Fees in Any Stablecoin](/guide/payments/pay-fees-in-any-stablecoin)

::::

## Recipes

### Local account sponsorship

The example above uses a fee payer server to sign and sponsor transactions. If you want to sponsor transactions locally, you can easily do so by passing a local account to the `feePayer` parameter.

```ts twoslash [client.ts]
// @noErrors
import { createClient, http } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'
import { tempoModerato } from 'viem/chains'

const client = createClient({
  chain: tempoModerato,
  transport: http(),
})

const { receipt } = await client.token.transferSync({
  amount: parseUnits('10.5', 6),
  to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
  token: '0x20c0000000000000000000000000000000000000',
  feePayer: privateKeyToAccount('0x...'), // [!code hl]
})
```

## Best practices

1. **Set sponsorship limits**: Implement daily or per-user limits to control costs
2. **Monitor expenses**: Track sponsorship costs regularly to stay within budget
3. **Consider selective sponsorship**: Only sponsor fees for specific operations or user segments
4. **Educate users**: Clearly communicate when fees are being sponsored

### Security Considerations

* **Transaction-specific**: Fee payer signatures are tied to specific transactions
* **No delegation risk**: Fee payer can't execute arbitrary transactions
* **Balance checks**: Network verifies fee payer has sufficient balance
* **Signature validation**: Both signatures must be valid

### Signing Hash Behavior

When building fee-sponsored transactions, the sender must indicate sponsorship **before signing**. This is because the transaction's signing hash differs based on whether it will be sponsored:

* **Sponsored transactions**: The `fee_token` field is omitted from the sender's signing payload, and a `0x00` marker is used. This allows the fee payer to choose the fee token.
* **Non-sponsored transactions**: The `fee_token` is included in the sender's signing payload.

The `withFeePayer` transport and `feePayer: true` parameter handle this automatically. If you're building transactions manually with a local account as fee payer, the Viem SDK handles this for you:

```ts twoslash
// @noErrors
import { createClient, http, parseUnits } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'
import { tempoModerato } from 'viem/chains'

const client = createClient({
  chain: tempoModerato,
  transport: http(),
})

const senderAccount = privateKeyToAccount('0x...')
const feePayerAccount = privateKeyToAccount('0x...')

// When feePayer is an Account object, Viem:
// 1. Has the sender sign the transaction (with feeToken)
// 2. Recovers the sender address from their signature  
// 3. Has the fee payer sign a separate hash (includes sender + feeToken)
// 4. Serializes the dual-signed transaction
const { receipt } = await client.token.transferSync({
  account: senderAccount,
  amount: parseUnits('10.5', 6),
  to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
  token: '0x20c0000000000000000000000000000000000000',
  feePayer: feePayerAccount, // [!code hl]
})
```

:::info
When using `feePayer: true` with the `withFeePayer` transport, the SDK deletes the `feeToken` from the transaction before signing, then sends it to the fee payer service which adds their signature.
:::

## Learning Resources

<Cards>
  <Card description="Learn more about fees and how they work on Tempo" to="/protocol/fees/spec-fee" icon="lucide:book" title="Fee Specification" />

  <Card description="Technical specification for TempoTransactions and fee payer signature details" to="/protocol/transactions/spec-tempo-transaction" icon="lucide:file-code" title="TempoTransaction Spec" />

  <Card description="Learn how to sponsor fees for multiple operations at once" to="/guide/use-accounts/batch-transactions" icon="lucide:layers" title="Batch Transactions Guide" />

  <Card description="Understand fee token selection and how to pay with different stablecoins" to="/guide/payments/pay-fees-in-any-stablecoin" icon="lucide:coins" title="Pay Fees in Any Stablecoin" />
</Cards>

# Attach a Transfer Memo

Attach 32-byte references to [TIP-20](/protocol/tip20/overview) transfers for payment reconciliation. Use memos to link onchain transactions to your internal records—customer IDs, invoice numbers, or any identifier that helps you match payments to your database.

## Demo

<Demo.Container name="Transfer with Memo" footerVariant="source" src="tempoxyz/examples/tree/main/examples/payments">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.SendPaymentWithMemo stepNumber={3} last />
</Demo.Container>

## Steps

::::steps

### Set up your project

Ensure you have Wagmi configured with Tempo. Follow either guide to get started:

* [Embed Passkey accounts](/guide/use-accounts/embed-passkeys)
* [Connect to wallets](/guide/use-accounts/connect-to-wallets)

### Send a transfer with memo

Use `transferWithMemo` to attach a reference to your payment. The memo is a 32-byte value that gets emitted in the `TransferWithMemo` event.

:::code-group

```tsx twoslash [SendWithMemo.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { parseUnits, toHex } from 'viem'
import { useConnection } from 'wagmi'

export function SendWithMemo() {
  const { address } = useConnection()
  const transfer = Hooks.token.useTransferSync()

  const handleSend = () => {
    transfer.mutate({
      token: '0x20c0000000000000000000000000000000000001',
      to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
      amount: parseUnits('100', 6),
      memo: toHex('INV-12345', { size: 32 }),
    })
  }

  return (
    <button onClick={handleSend} disabled={transfer.isPending}>
      {transfer.isPending ? 'Sending...' : 'Send Payment'}
    </button>
  )
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Watch for transfers with memos

Listen for `TransferWithMemo` events to reconcile incoming payments. The memo is indexed, so you can filter by specific values.

:::code-group

```tsx twoslash [WatchMemos.tsx]
// @noErrors
import { useWatchContractEvent } from 'wagmi'
import { fromHex } from 'viem'
import { Abis } from 'viem/tempo'

export function WatchMemos({ depositAddress }: { depositAddress: `0x${string}` }) {
  useWatchContractEvent({
    address: '0x20c0000000000000000000000000000000000001',
    abi: Abis.TIP20,
    eventName: 'TransferWithMemo',
    onLogs: (logs) => {
      for (const log of logs) {
        if (log.args.to === depositAddress) {
          const memo = fromHex(log.args.memo, 'string').replace(/\0/g, '')
          console.log(`Received ${log.args.value} with memo: ${memo}`)
        }
      }
    },
  })

  return <div>Watching for deposits...</div>
}
```

```tsx twoslash [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

::::

## Recipes

### Exchange deposit reconciliation

As an exchange, use a single master hot wallet for all customer deposits. Customers include their customer ID as the memo, and you credit their account by parsing the event.

```ts
import { Actions } from 'viem/tempo'
import { parseUnits, stringToHex, pad } from 'viem'

// Customer deposits with their customer ID
await Actions.token.transferSync(walletClient, {
  token: tokenAddress,
  to: exchangeHotWallet,
  amount: parseUnits('500', 6),
  memo: pad(stringToHex('CUST-12345'), { size: 32 }),
})
```

### Payroll batch payments

Batch multiple payments in a single Tempo transaction with employee IDs in each memo for clear accounting records.

```ts
import { Abis } from 'viem/tempo'
import { encodeFunctionData, parseUnits, stringToHex, pad } from 'viem'

const calls = employees.map(emp => ({
  to: tokenAddress,
  data: encodeFunctionData({
    abi: Abis.TIP20,
    functionName: 'transferWithMemo',
    args: [emp.wallet, parseUnits(emp.salary, 6), pad(stringToHex(emp.id), { size: 32 })]
  })
}))

await walletClient.sendCalls({ calls })
```

### Refund address in memo

Include a refund address in the memo so the recipient knows where to send funds if a reversal is needed.

```ts
import { Actions } from 'viem/tempo'
import { parseUnits, stringToHex, pad } from 'viem'

const refundMemo = pad(stringToHex('REFUND 0x742d35Cc6634C0532925a3b8'), { size: 32 })

await Actions.token.transferSync(walletClient, {
  token: tokenAddress,
  to: merchantAddress,
  amount: parseUnits('100', 6),
  memo: refundMemo,
})
```

## Best Practices

### Use consistent memo formats

Establish a naming convention for your memos (e.g., `CUST-{id}`, `INV-{number}`, `REFUND-{id}`) to make parsing and filtering reliable across your system.

### Keep memos under 32 bytes

Memos are `bytes32` values. Use `toHex(string, { size: 32 })` to convert strings—if your string exceeds 32 bytes, it will be truncated. For longer references, store the full data offchain and use a hash or short ID as the memo.

### Index memos for efficient queries

The `TransferWithMemo` event has `memo` as an indexed parameter. Use `getLogs` with the `args` filter to query transactions by memo without scanning all events.

```ts
import { parseAbiItem, stringToHex, pad } from 'viem'

const logs = await client.getLogs({
  address: tokenAddress,
  event: parseAbiItem('event TransferWithMemo(address indexed from, address indexed to, uint256 value, bytes32 indexed memo)'),
  args: { memo: pad(stringToHex('INV-12345'), { size: 32 }) },
})
```

## Learning Resources

<Cards>
  <Card description="Complete guide to sending stablecoin payments with optional memos" to="/guide/payments/send-a-payment" icon="lucide:send" title="Send a Payment" />

  <Card description="Watch for incoming payments and integrate reconciliation flows" to="/guide/payments/accept-a-payment" icon="lucide:handshake" title="Accept a Payment" />

  <Card description="Full API reference for memo methods and events" to="/protocol/tip20/spec" icon="lucide:file-text" title="TIP-20 Specification" />
</Cards>

# Executing Swaps

Execute swaps between stablecoins on the exchange. Swaps execute immediately against existing orders in the orderbook, providing instant liquidity for cross-stablecoin payments.

By the end of this guide you will be able to execute swaps, get price quotes, and manage slippage protection.

<Demo.Container name="Execute a Swap" footerVariant="source" src="tempoxyz/examples/tree/main/examples/exchange">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.MakeSwaps stepNumber={3} last />
</Demo.Container>

## Steps

::::steps

### Set up your client

Ensure that you have set up your client by following the [guide](/sdk/typescript).

### Get a price quote

Before executing a swap, get a quote to see the expected price.

:::code-group

```tsx twoslash [Buy.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Buy() {
  const amount = parseUnits('10', 6)

  // How much AlphaUSD do I need to spend to receive 10 BetaUSD? // [!code hl]
  const { data: quote } = Hooks.dex.useBuyQuote({ // [!code hl]
    tokenIn: alphaUsd, // [!code hl]
    tokenOut: betaUsd, // [!code hl]
    amountOut: amount, // [!code hl]
  }) // [!code hl]

  return <div>Quote: {formatUnits(quote, 6)}</div>
}
```

```tsx twoslash [Sell.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Sell() {
  const amount = parseUnits('10', 6)

  // How much BetaUSD will I receive for 10 AlphaUSD? // [!code hl]
  const { data: quote } = Hooks.dex.useSellQuote({ // [!code hl]
    tokenIn: alphaUsd, // [!code hl]
    tokenOut: betaUsd, // [!code hl]
    amountIn: amount, // [!code hl]
  }) // [!code hl]

  return <div>Quote: {formatUnits(quote, 6)}</div>
}
```

:::

### Calculate slippage tolerance

Set appropriate slippage based on your quote to protect against unfavorable price movements.

:::code-group

```tsx twoslash [Buy.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Buy() {
  const amount = parseUnits('10', 6)

  // How much AlphaUSD do I need to spend to receive 10 BetaUSD?
  const { data: quote } = Hooks.dex.useBuyQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountOut: amount,
  })

  // [!code ++] Calculate 0.5% slippage tolerance 
  const slippageTolerance = 0.005 // [!code ++]
  const maxAmountIn = quote // [!code ++]
    ? quote * BigInt(Math.floor((1 + slippageTolerance) * 1000)) / 1000n // [!code ++]
    : 0n // [!code ++]

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Max input (0.5% slippage): {formatUnits(maxAmountIn, 6)}</div> {/* [!code ++] */}
    </div>
  )
}
```

```tsx twoslash [Sell.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Sell() {
  const amount = parseUnits('10', 6)

  // How much BetaUSD will I receive for 10 AlphaUSD?
  const { data: quote } = Hooks.dex.useSellQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountIn: amount,
  })

  // [!code ++] Calculate 0.5% slippage tolerance
  const slippageTolerance = 0.005 // [!code ++]
  const minAmountOut = quote // [!code ++]
    ? quote * BigInt(Math.floor((1 - slippageTolerance) * 1000)) / 1000n // [!code ++]
    : 0n // [!code ++]

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Min output (0.5% slippage): {formatUnits(minAmountOut, 6)}</div> {/* [!code ++] */}
    </div>
  )
}
```

:::

### Approve Spend

To execute a swap, you need to approve the Stablecoin DEX contract to spend the token you're using to fund the swap.

:::code-group

```tsx twoslash [Buy.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo' // [!code ++]
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi' // [!code ++]

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Buy() {
  const amount = parseUnits('10', 6)

  // How much AlphaUSD do I need to spend to receive 10 BetaUSD?
  const { data: quote } = Hooks.dex.useBuyQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountOut: amount,
  })

  // Calculate 0.5% slippage tolerance
  const slippageTolerance = 0.005
  const maxAmountIn = quote
    ? quote * BigInt(Math.floor((1 + slippageTolerance) * 1000)) / 1000n
    : 0n

  const sendCalls = useSendCallsSync() // [!code ++]

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Max input (0.5% slippage): {formatUnits(maxAmountIn, 6)}</div>
      <button type="button" onClick={() => { // [!code ++]
        const calls = [ // [!code ++]
          Actions.token.approve.call({ // [!code ++]
            amount: maxAmountIn, // Approve the max amount with slippage // [!code ++]
            spender: Addresses.stablecoinDex, // [!code ++]
            token: alphaUsd, // [!code ++]
          }), // [!code ++]
        ] // [!code ++]
        sendCalls.sendCallsSync({ calls }) // [!code ++]
      }}> {/* [!code ++] */}
        Approve Spend {/* [!code ++] */}
      </button> {/* [!code ++] */}
    </div>
  )
}
```

```tsx twoslash [Sell.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo' // [!code ++]
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi' // [!code ++]

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Sell() {
  const amount = parseUnits('10', 6)

  // How much BetaUSD will I receive for 10 AlphaUSD?
  const { data: quote } = Hooks.dex.useSellQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountIn: amount,
  })

  // Calculate 0.5% slippage tolerance
  const slippageTolerance = 0.005
  const minAmountOut = quote
    ? quote * BigInt(Math.floor((1 - slippageTolerance) * 1000)) / 1000n
    : 0n

  const sendCalls = useSendCallsSync() // [!code ++]

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Min output (0.5% slippage): {formatUnits(minAmountOut, 6)}</div>
      <button type="button" onClick={() => { // [!code ++]
        const calls = [ // [!code ++]
          Actions.token.approve.call({ // [!code ++]
            amount, // Approve the exact amount being sold // [!code ++]
            spender: Addresses.stablecoinDex, // [!code ++]
            token: alphaUsd, // [!code ++]
          }), // [!code ++]
        ] // [!code ++]
        sendCalls.sendCallsSync({ calls }) // [!code ++]
      }}> {/* [!code ++] */}
        Approve Spend {/* [!code ++] */}
      </button> {/* [!code ++] */}
    </div>
  )
}
```

:::

### Execute a swap

Batch the token approval with the swap in a single transaction for better UX.

:::code-group

```tsx twoslash [Buy.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo'
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Buy() {
  const amount = parseUnits('10', 6)

  // How much AlphaUSD do I need to spend to receive 10 BetaUSD?
  const { data: quote } = Hooks.dex.useBuyQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountOut: amount,
  })

  // Calculate 0.5% slippage tolerance
  const slippageTolerance = 0.005
  const maxAmountIn = quote
    ? quote * BigInt(Math.floor((1 + slippageTolerance) * 1000)) / 1000n
    : 0n

  const sendCalls = useSendCallsSync()

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Max input (0.5% slippage): {formatUnits(maxAmountIn, 6)}</div>
      <button type="button" onClick={() => {
        const calls = [
          Actions.token.approve.call({
            amount: maxAmountIn, // Approve the max amount with slippage
            spender: Addresses.stablecoinDex,
            token: alphaUsd,
          }),
          Actions.dex.buy.call({ // [!code ++]
            amountOut: amount, // [!code ++]
            maxAmountIn, // [!code ++]
            tokenIn: alphaUsd, // [!code ++]
            tokenOut: betaUsd, // [!code ++]
          }), // [!code ++]
        ]
        sendCalls.sendCallsSync({ calls })
      }}>
        Execute Swap
      </button>
    </div>
  )
}
```

```tsx twoslash [Sell.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo'
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Sell() {
  const amount = parseUnits('10', 6)

  // How much BetaUSD will I receive for 10 AlphaUSD?
  const { data: quote } = Hooks.dex.useSellQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountIn: amount,
  })

  // Calculate 0.5% slippage tolerance
  const slippageTolerance = 0.005
  const minAmountOut = quote
    ? quote * BigInt(Math.floor((1 - slippageTolerance) * 1000)) / 1000n
    : 0n

  const sendCalls = useSendCallsSync()

  return (
    <div>
      <div>Quote: {formatUnits(quote, 6)}</div>
      <div>Min output (0.5% slippage): {formatUnits(minAmountOut, 6)}</div>
      <button type="button" onClick={() => {
        const calls = [
          Actions.token.approve.call({
            amount, // Approve the exact amount being sold
            spender: Addresses.stablecoinDex,
            token: alphaUsd,
          }),
          Actions.dex.sell.call({ // [!code ++]
            amountIn: amount, // [!code ++]
            minAmountOut, // [!code ++]
            tokenIn: alphaUsd, // [!code ++]
            tokenOut: betaUsd, // [!code ++]
          }), // [!code ++]
        ]
        sendCalls.sendCallsSync({ calls })
      }}>
        Execute Swap
      </button>
    </div>
  )
}
```

:::

::::

## Recipes

### Handling insufficient liquidity

Quote requests will fail with an `InsufficientLiquidity` error if there isn't enough liquidity in the orderbook to satisfy the requested amount.

Handle this error when fetching quotes:

```tsx
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'
const betaUsd = '0x20c0000000000000000000000000000000000002'

function Swap() {
  const amount = parseUnits('10', 6)

  const { data: quote, error } = Hooks.dex.useSellQuote({
    tokenIn: alphaUsd,
    tokenOut: betaUsd,
    amountIn: amount,
  })

  if (error) {
    if (error.message.includes('InsufficientLiquidity')) {
      return <div>Not enough liquidity available. Try a smaller amount.</div>
    }
    return <div>Error: {error.message}</div>
  }

  if (!quote) {
    return <div>Loading quote...</div>
  }

  return <div>Quote: {quote.toString()}</div>
}
```

## Best Practices

### Always get quotes before swapping

Query the expected price before executing a swap to ensure you're getting a fair rate and to set appropriate slippage protection.

### Set appropriate slippage protection

Use `minAmountOut` or `maxAmountIn` to protect against unfavorable price movements between quoting and execution.

## Learning Resources

<Cards>
  <Card description="Learn about how the Stablecoin DEX interacts with your balances" to="/protocol/exchange/exchange-balance" icon="lucide:wallet" title="Exchange Balance" />

  <Card description="Learn about the technical details of swap execution" to="/protocol/exchange/executing-swaps" icon="lucide:arrow-left-right" title="Swap Execution Details" />
</Cards>

# Managing Fee Liquidity

The Fee AMM converts transaction fees between stablecoins when users pay in a different token than the validator prefers. This guide shows you how to add and remove liquidity to enable fee conversions.

<Demo.Container name="Manage Fee Liquidity" footerVariant="source" src="tempoxyz/examples/tree/main/examples/issuance">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.CreateOrLoadToken stepNumber={3} />

  <Step.MintFeeAmmLiquidity stepNumber={4} waitForBalance={false} />

  <Step.CheckFeeAmmPool stepNumber={5} />

  <Step.BurnFeeAmmLiquidity stepNumber={6} last />
</Demo.Container>

## Steps

::::steps

### Check pool reserves

Before adding liquidity, check the current pool reserves to understand the pool state.

:::code-group

```tsx twoslash [ManageFeeLiquidity.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits } from 'viem'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function ManageFeeLiquidity() {
  const { data: pool } = Hooks.amm.usePool({ // [!code hl]
    userToken, // [!code hl]
    validatorToken, // [!code hl]
  }) // [!code hl]

  return (
    <div>
      <div>User token reserves: {formatUnits(pool?.reserveUserToken ?? 0n, 6)}</div>
      <div>Validator token reserves: {formatUnits(pool?.reserveValidatorToken ?? 0n, 6)}</div>
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Add liquidity

Add validator token to the pool to receive LP tokens representing your share. The first liquidity provider to a new pool must burn 1,000 units of liquidity. This costs approximately 0.002 USD and prevents attacks on pool reserves. Learn more in the [Fee AMM specification](/protocol/fees/spec-fee-amm).

:::code-group

```tsx twoslash [ManageFeeLiquidity.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useConnection } from 'wagmi'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function ManageFeeLiquidity() {
  const { address } = useConnection()

  const { data: pool } = Hooks.amm.usePool({
    userToken,
    validatorToken,
  })

  const mintLiquidity = Hooks.amm.useMintSync() // [!code ++]

  return (
    <div>
      <div>User token reserves: {formatUnits(pool?.reserveUserToken ?? 0n, 6)}</div>
      <div>Validator token reserves: {formatUnits(pool?.reserveValidatorToken ?? 0n, 6)}</div>
      <button type="button" onClick={() => { // [!code ++]
        if (!address) return // [!code ++]
        mintLiquidity.mutate({ // [!code ++]
          userTokenAddress: userToken, // [!code ++]
          validatorTokenAddress: validatorToken, // [!code ++]
          validatorTokenAmount: parseUnits('100', 6), // [!code ++]
          to: address, // [!code ++]
          feeToken: validatorToken, // [!code ++]
        }) // [!code ++]
      }}> {/* [!code ++] */}
      Add Liquidity {/* [!code ++] */}
      </button> {/* [!code ++] */}
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Check your LP balance

View your LP token balance to see your share of the pool.

:::code-group

```tsx twoslash [ManageFeeLiquidity.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useConnection } from 'wagmi'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function ManageFeeLiquidity() {
  const { address } = useConnection()

  const { data: pool } = Hooks.amm.usePool({
    userToken,
    validatorToken,
  })

  const { data: balance } = Hooks.amm.useLiquidityBalance({ // [!code ++]
    address, // [!code ++]
    userToken, // [!code ++]
    validatorToken, // [!code ++]
  }) // [!code ++]

  const mintLiquidity = Hooks.amm.useMintSync()

  return (
    <div>
      <div>LP token balance: {formatUnits(balance ?? 0n, 6)}</div>  {/* [!code ++] */}
      <div>User token reserves: {formatUnits(pool?.reserveUserToken ?? 0n, 6)}</div>
      <div>Validator token reserves: {formatUnits(pool?.reserveValidatorToken ?? 0n, 6)}</div>
      <button type="button" onClick={() => {
        if (!address) return
        mintLiquidity.mutate({
          userTokenAddress: userToken,
          validatorTokenAddress: validatorToken,
          validatorTokenAmount: parseUnits('100', 6),
          to: address,
          feeToken: validatorToken,
        })
      }}>
        Add Liquidity
      </button>
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Remove liquidity

Burn LP tokens to withdraw your share of pool reserves plus accumulated fees.

:::code-group

```tsx twoslash [ManageFeeLiquidity.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useConnection } from 'wagmi'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function ManageFeeLiquidity() {
  const { address } = useConnection()

  const { data: pool } = Hooks.amm.usePool({
    userToken,
    validatorToken,
  })

  const { data: balance } = Hooks.amm.useLiquidityBalance({
    address,
    userToken,
    validatorToken,
  })

  const mintLiquidity = Hooks.amm.useMintSync()
  const burnLiquidity = Hooks.amm.useBurnSync() // [!code ++]

  return (
    <div>
      <div>LP token balance: {formatUnits(balance ?? 0n, 6)}</div>
      <div>User token reserves: {formatUnits(pool?.reserveUserToken ?? 0n, 6)}</div>
      <div>Validator token reserves: {formatUnits(pool?.reserveValidatorToken ?? 0n, 6)}</div>
      <button type="button" onClick={() => {
        if (!address) return
        mintLiquidity.mutate({
          userTokenAddress: userToken,
          validatorTokenAddress: validatorToken,
          validatorTokenAmount: parseUnits('100', 6),
          to: address,
          feeToken: validatorToken,
        })
      }}>
        Add Liquidity
      </button>
      <button type="button" onClick={() => { // [!code ++]
        if (!address) return // [!code ++]
        burnLiquidity.mutate({ // [!code ++]
          userToken, // [!code ++]
          validatorToken, // [!code ++]
          liquidity: parseUnits('10', 6), // Burn 10 LP tokens // [!code ++]
          to: address, // [!code ++]
        }) // [!code ++]
      }}> {/* [!code ++] */}
      Remove Liquidity {/* [!code ++] */}
      </button> {/* [!code ++] */}
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

::::

## Recipes

### Monitor pool utilization

Track fee swap activity to understand pool utilization and revenue.

:::code-group

```tsx twoslash [MonitorSwaps.tsx]
// @noErrors
import * as React from 'react'
import { Hooks } from 'wagmi/tempo'
import { formatUnits } from 'viem'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function MonitorSwaps() {
  const [swaps, setSwaps] = React.useState<any[]>([])

  Hooks.amm.useWatchFeeSwap({ // [!code hl]
    userToken, // [!code hl]
    validatorToken, // [!code hl]
    onLogs(logs) { // [!code hl]
      for (const log of logs) { // [!code hl]
        setSwaps((prev) => [...prev, { // [!code hl]
          amountIn: formatUnits(log.args.amountIn, 6), // [!code hl]
          amountOut: formatUnits(log.args.amountOut, 6), // [!code hl]
          revenue: formatUnits(log.args.amountIn * 30n / 10000n, 6), // [!code hl]
        }]) // [!code hl]
      } // [!code hl]
    }, // [!code hl]
  }) // [!code hl]

  return (
    <div>
      {swaps.map((swap, i) => (
        <div key={i}>
          Swap: {swap.amountIn} → {swap.amountOut} (LP revenue: {swap.revenue})
        </div>
      ))}
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Rebalance pools

You can rebalance pools by swapping validator tokens for accumulated user tokens at a fixed rate. Rebalancing restores validator token reserves and enables continued fee conversions. Learn more [here](/protocol/fees/spec-fee-amm#swap-mechanisms).

:::code-group

```tsx twoslash [RebalancePool.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'
import { formatUnits, parseUnits } from 'viem'
import { useConnection } from 'wagmi'

const userToken = '0x20c0000000000000000000000000000000000002' // BetaUSD
const validatorToken = '0x20c0000000000000000000000000000000000001' // AlphaUSD

function RebalancePool() {
  const { address } = useConnection()

  const { data: pool } = Hooks.amm.usePool({
    userToken,
    validatorToken,
  })

  const rebalance = Hooks.amm.useRebalanceSwapSync() // [!code hl]

  return (
    <div>
      <div>User token reserves: {formatUnits(pool?.reserveUserToken ?? 0n, 6)}</div>
      <div>Validator token reserves: {formatUnits(pool?.reserveValidatorToken ?? 0n, 6)}</div>
      <button type="button" onClick={() => { // [!code hl]
        if (!address || !pool) return // [!code hl]
        // Swap validator token for user token at 0.9985 rate // [!code hl]
        rebalance.mutate({ // [!code hl]
          userToken, // [!code hl]
          validatorToken, // [!code hl]
          amountOut: pool.reserveUserToken, // Amount of user token to receive // [!code hl]
          to: address, // [!code hl]
        }) // [!code hl]
      }}> { /* [!code hl] */ }
        Rebalance { /* [!code hl] */ }
      </button> { /* [!code hl] */ }
    </div>
  )
}
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.localStorage(),
    }),
  ],
  chains: [tempoModerato],
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

## Best Practices

### Monitor pool reserves

Regularly check pool reserves to ensure sufficient liquidity for fee conversions. Low reserves can prevent transactions from being processed.

Add liquidity when:

* Transaction rates increase for a given `userToken`
* Reserve levels drop below expected daily volume
* Multiple validators begin preferring the same token

### Maintain adequate reserves

As an issuer, keep sufficient validator token reserves to handle expected transaction volume. Consider your anticipated fee conversion volume when determining reserve levels.

For new token pairs, provide the entire initial amount in the validator token. The pool naturally accumulates user tokens as fees are paid.

### Deploy liquidity strategically

Focus liquidity on pools with:

* High transaction volume and frequent fee conversions
* New stablecoins that need initial bootstrapping
* Validator tokens preferred by multiple validators

## Learning Resources

<Cards>
  <Card description="Complete technical specification of the Fee AMM protocol" to="/protocol/fees/spec-fee-amm" icon="lucide:file-text" title="Fee AMM Specification" />

  <Card description="Learn how the Fee AMM enables flexible fee payments" to="/protocol/fees/fee-amm" icon="lucide:droplet" title="Fee AMM Overview" />

  <Card description="Enable users to pay fees using your stablecoin" to="/guide/issuance/use-for-fees" icon="lucide:coins" title="Use Your Stablecoin for Fees" />
</Cards>

# Providing Liquidity

Add liquidity for a token pair by placing orders on the Stablecoin DEX. You can provide liquidity on the `buy` or `sell` side of the orderbook, with `limit` or `flip` orders. To learn more about order types see the [documentation on order types](/protocol/exchange/providing-liquidity#order-types).

In this guide you will learn how to place buy and sell orders to provide liquidity on the Stablecoin DEX orderbook.

## Demo

<Demo.Container name="Place an Order" footerVariant="source" src="tempoxyz/examples/tree/main/examples/exchange">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.PlaceOrder stepNumber={3} />

  <Step.QueryOrder stepNumber={4} last />
</Demo.Container>

## Steps

::::steps

### Set up your client

Ensure that you have set up your client by following the [guide](/sdk/typescript).

### Approve spend

To place an order, you need to approve the Stablecoin DEX contract to spend the order's "spend" token.

:::info
The code samples in this guide will place orders on the `AlphaUSD` / `pathUSD` pair.

The "spend" token is the token that will be spent to place the order.

* buying `AlphaUSD` spends `pathUSD`
* selling `AlphaUSD` spends `AlphaUSD`

  :::

<Demo.Container name="Approve Spend">
  <Step.Connect stepNumber={1} />

  <Step.ApproveSpend stepNumber={2} last />
</Demo.Container>

:::code-group

```tsx twoslash [ApproveSpend.tsx]
// @noErrors
import { parseUnits } from 'viem'
import { Addresses } from 'viem/tempo'
import { Hooks } from 'wagmi/tempo'

const pathUsd = '0x20c0000000000000000000000000000000000000'
const alphaUsd = '0x20c0000000000000000000000000000000000001'

function ApproveSpend(props: { orderType: 'buy' | 'sell' }) {
  const { orderType } = props
  // buying AlphaUSD requires we spend pathUSD // [!code hl]
  const spendToken = orderType === 'buy' ? pathUsd : alphaUsd // [!code hl]
  // [!code hl]
  const { mutate: approve } = Hooks.token.useApproveSync() // [!code hl]

  return (
    <button type="button" onClick={() => {
      approve({ // [!code hl]
        amount: parseUnits('100', 6), // [!code hl]
        spender: Addresses.stablecoinDex, // [!code hl]
        token: spendToken, // [!code hl]
      }) // [!code hl]
  }}>
      Approve Spend
    </button>
  )
}
```

```ts [wagmi.config.ts]
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Place order

Once the spend is approved, you can place an order by calling the `place` action on the Stablecoin DEX.

:::info
In the code sample below, we use the `useSendCallsSync` hook to batch the approve and place order calls in a single transaction for efficiency.
:::

<Demo.Container name="Place Order">
  <Step.Connect stepNumber={1} />

  <Step.PlaceOrder stepNumber={2} last />
</Demo.Container>

:::code-group

```tsx twoslash [PlaceOrder.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo'
import { parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi' // [!code hl]

const pathUsd = '0x20c0000000000000000000000000000000000000'
const alphaUsd = '0x20c0000000000000000000000000000000000001'

function PlaceOrder(props: { orderType: 'buy' | 'sell' }) {
  const { orderType } = props
  // buying AlphaUSD requires we spend pathUSD
  const spendToken = orderType === 'buy' ? pathUsd : alphaUsd

  const sendCalls = useSendCallsSync() // [!code hl]

  return (
    <button type="button" onClick={() => {
      const calls = [ // [!code hl]
        Actions.token.approve.call({ // [!code hl]
          spender: Addresses.stablecoinDex, // [!code hl]
          amount: parseUnits('100', 6), // [!code hl]
          token: spendToken, // [!code hl]
        }), // [!code hl]
        Actions.dex.place.call({ // [!code hl]
          token: alphaUsd, // [!code hl]
          amount: parseUnits('100', 6), // [!code hl]
          type: orderType, // [!code hl]
          tick: 0, // [!code hl]
        }), // [!code hl]
      ] // [!code hl]
      sendCalls.sendCallsSync({ calls }) // [!code hl]
    }}>
      Place Order
    </button>
  )
}
```

```ts [wagmi.config.ts]
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### View order details

After placing an order, you can query its details to see the current state, including the amount filled and remaining using [`Hooks.dex.useOrder`](https://wagmi.sh/tempo/hooks/dex.useOrder).

<Demo.Container name="View Order">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.PlaceOrder stepNumber={3} />

  <Step.QueryOrder stepNumber={4} last />
</Demo.Container>

:::code-group

```tsx twoslash [QueryOrder.tsx]
// @noErrors
import { Hooks } from 'wagmi/tempo'

const orderId = 123n

const { data: order, refetch } = Hooks.dex.useOrder({
  orderId,
})

console.log('Type:', order?.isBid ? 'Buy' : 'Sell')
console.log('Amount:', order?.amount.toString())
console.log('Remaining:', order?.remaining.toString())
console.log('Tick:', order?.tick)
console.log('Is flip order:', order?.isFlip)
```

```ts [wagmi.config.ts]
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

For more details on querying orders, see the [`Hooks.dex.useOrder`](https://wagmi.sh/tempo/hooks/dex.useOrder) documentation.

::::

## Recipes

### Cancel order

Cancel an order using its order ID.

When you cancel an order, any remaining funds are credited to your exchange balance (not directly to your wallet). To move funds back to your wallet, you can [withdraw them to your wallet](/protocol/exchange/exchange-balance#withdrawing-funds).

<Demo.Container name="Place and Cancel an Order" footerVariant="source" src="tempoxyz/examples/tree/main/examples/exchange">
  <Step.Connect stepNumber={1} />

  <Step.AddFunds stepNumber={2} />

  <Step.PlaceOrder stepNumber={3} />

  <Step.CancelOrder stepNumber={4} last />
</Demo.Container>

:::code-group

```tsx twoslash [ManageOrder.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo'
import { Hooks } from 'wagmi/tempo'
import { parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi'

const pathUsd = '0x20c0000000000000000000000000000000000000'
const alphaUsd = '0x20c0000000000000000000000000000000000001'

function ManageOrder() {
  const sendCalls = useSendCallsSync()
  const cancelOrder = Hooks.dex.useCancelSync() // [!code hl]

  const placeOrder = () => {
    const calls = [
      Actions.token.approve.call({
        spender: Addresses.stablecoinDex,
        amount: parseUnits('100', 6),
        token: pathUsd,
      }),
      Actions.dex.place.call({
        token: alphaUsd,
        amount: parseUnits('100', 6),
        type: 'buy',
        tick: 0,
      }),
    ]
    sendCalls.sendCallsSync({ calls })
  }

  return (
    <>
      <button type="button" onClick={placeOrder}>
        Place Order
      </button>
      <form onSubmit={
        (event) => {
          event.preventDefault()
          const formData = new FormData(event.target as HTMLFormElement)
          const orderId = BigInt(formData.get('orderId') as string)

          cancelOrder.mutate({ orderId }) // [!code hl]
        }
      }>
        <input type="text" name="orderId" placeholder="Order ID" />
        <button // [!code hl]
          type="submit" // [!code hl]
          disabled={cancelOrder.isPending} // [!code hl]
        > {/* [!code hl] */}
        {cancelOrder.isPending ? 'Canceling...' : 'Cancel Order'} {/* [!code hl] */}
        </button> {/* [!code hl] */}
      </form>
    </>
  )
}
```

```ts [wagmi.config.ts]
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Determining quote token

Each token has a designated quote token that it trades against on the DEX. For most stablecoins, this will be `pathUSD`.

Use the `token.useGetMetadata` hook to retrieve a token's quote token.

:::code-group

```ts twoslash [example.ts]
// @errors: 2322
import { config } from './wagmi.config'
declare module 'wagmi' {
  interface Register {
    config: typeof config
  }
}
// ---cut---
import { Hooks } from 'wagmi/tempo'

const { data: metadata } = Hooks.token.useGetMetadata({ // [!code focus]
  token: '0x20c0000000000000000000000000000000000001', // AlphaUSD // [!code focus]
}) // [!code focus]

console.log('Token:', metadata?.symbol)
// @log: Token: AlphaUSD
console.log('Quote Token:', metadata?.quoteToken) // returns `pathUSD` address 
// @log: Quote Token: 0x20c0000000000000000000000000000000000000
```

```ts [wagmi.config.ts] filename="wagmi.config.ts"
// @noErrors
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Flip order

Flip orders automatically switch between buy and sell sides when filled, providing continuous liquidity. Use viem's [`dex.placeFlip`](https://viem.sh/tempo/actions/dex.placeFlip) to create a flip order call.

:::code-group

```tsx twoslash [PlaceFlipOrder.tsx]
// @noErrors
import { Actions, Addresses } from 'viem/tempo'
import { parseUnits } from 'viem'
import { useSendCallsSync } from 'wagmi'

const pathUsd = '0x20c0000000000000000000000000000000000000'
const alphaUsd = '0x20c0000000000000000000000000000000000001'

function PlaceFlipOrder(props: { orderType: 'buy' | 'sell' }) {
  const { orderType } = props
  // buying AlphaUSD requires we spend pathUSD
  const spendToken = orderType === 'buy' ? pathUsd : alphaUsd

  const sendCalls = useSendCallsSync()

  return (
    <button type="button" onClick={() => {
      const calls = [
        Actions.token.approve.call({
          spender: Addresses.stablecoinDex,
          amount: parseUnits('100', 6),
          token: spendToken,
        }),
        Actions.dex.placeFlip.call({ // [!code focus]
          token: alphaUsd,
          amount: parseUnits('100', 6),
          type: orderType,
          tick: 0,
        }),
      ]
      sendCalls.sendCallsSync({ calls })
    }}>
      Place Flip Order
    </button>
  )
}
```

```ts [wagmi.config.ts]
// [!include ~/snippets/wagmi.config.ts:setup]
```

:::

### Place order at specific price

Ticks represent prices relative to the quote token (usually pathUSD). The formula is:

```
tick = (price - 1) * 100_000
```

For example, price $1.0000 → tick = 0, price $0.9990 → tick = -10, and price $1.0010 → tick = 10.

Use the `Tick` utility to convert between prices and ticks:

```tsx
import { Actions, Tick } from 'viem/tempo' // [!code hl]
import { parseUnits } from 'viem'

const alphaUsd = '0x20c0000000000000000000000000000000000001'

// buy order at $0.9990 (tick: -10) // [!code hl]
const buyCall = Actions.dex.place.call({ // [!code hl]
  token: alphaUsd, // [!code hl]
  amount: parseUnits('100', 6), // [!code hl]
  type: 'buy', // [!code hl]
  tick: Tick.fromPrice('0.9990'), // -10 // [!code hl]
}) // [!code hl]

// sell order at $1.0010 (tick: 10) // [!code hl]
const sellCall = Actions.dex.place.call({ // [!code hl]
  token: alphaUsd, // [!code hl]
  amount: parseUnits('100', 6), // [!code hl]
  type: 'sell', // [!code hl]
  tick: Tick.fromPrice('1.0010'), // 10 // [!code hl]
}) // [!code hl]

```

For more details including tick precision, limits, and calculation examples, see [Understanding Ticks](/protocol/exchange/providing-liquidity#understanding-ticks).

## Best practices

### Batch calls

You can batch the calls to approve spend and place the order in a single transaction for efficiency. See the [guide on batch transactions](/guide/use-accounts/batch-transactions) for more details.

## Learning resources

<Cards>
  <Card description="Learn how to execute swaps and trade stablecoins on the DEX" to="/guide/stablecoin-dex/executing-swaps" icon="lucide:arrow-left-right" title="Executing Swaps" />

  <Card description="Deep dive into the Stablecoin DEX protocol specification" to="/protocol/exchange/spec" icon="lucide:book-open" title="Protocol Exchange Specification" />

  <Card description="Manage token balances on the exchange to optimize gas costs" to="/protocol/exchange/exchange-balance" icon="lucide:wallet" title="Exchange Balance" />
</Cards>

# View the Orderbook

Query and inspect the orderbook to see available liquidity, price levels, and individual orders on Tempo's Stablecoin DEX.

## Recommended Approach

We recommend using indexed data to query the orderbook for better performance and ease of use. While you can query logs and transactions directly from an RPC node, indexed data providers offer structured SQL interfaces that make complex queries simpler and more efficient.

In this guide, we use [Index Supply](https://www.indexsupply.net) as our indexing provider, but you're free to choose your own indexing solution or query the chain directly based on your needs.

## Recipes

### Get the current spread

Query the best bid and ask prices to calculate the current spread for a token pair.

Find the highest bid prices (buyers) for AlphaUSD. This query filters out fully filled and cancelled orders, groups by price level (tick), and shows the top 5 bid prices with their total liquidity.

<IndexSupplyQuery
  title={'Best Bid Prices for AlphaUSD'}
  query={`SELECT
  tick as price,
  SUM(amount) as total_liquidity
FROM orderplaced
WHERE token = '0x20c0000000000000000000000000000000000001'
  AND "isBid" = true
  AND NOT EXISTS (
    SELECT 1 FROM orderfilled
    WHERE orderfilled."orderId" = orderplaced."orderId"
      AND orderfilled."partialFill" = false
  )
  AND NOT EXISTS (
    SELECT 1 FROM ordercancelled
    WHERE ordercancelled."orderId" = orderplaced."orderId"
  )
GROUP BY price
ORDER BY price DESC
LIMIT 5`}
  signatures={["OrderPlaced", "OrderFilled", "OrderCancelled"]}
/>

Find the lowest ask prices (sellers) for AlphaUSD. The spread is the difference between the highest bid and lowest ask price.

<IndexSupplyQuery
  title={'Best Ask Prices for AlphaUSD'}
  query={`SELECT
  tick as price,
  SUM(amount) as total_liquidity
FROM orderplaced
WHERE token = '0x20c0000000000000000000000000000000000001'
  AND "isBid" = false
  AND NOT EXISTS (
    SELECT 1 FROM orderfilled
    WHERE orderfilled."orderId" = orderplaced."orderId"
      AND orderfilled."partialFill" = false
  )
  AND NOT EXISTS (
    SELECT 1 FROM ordercancelled
    WHERE ordercancelled."orderId" = orderplaced."orderId"
  )
GROUP BY price
ORDER BY price
LIMIT 5`}
  signatures={["OrderPlaced", "OrderFilled", "OrderCancelled"]}
/>

### Inspect order depth

View aggregated liquidity at each price level to understand the orderbook structure.

This query shows all active orders for BetaUSD, including both regular and flip orders.

<IndexSupplyQuery
  title={'BetaUSD Order Depth by Price Level'}
  query={`SELECT
  tick as price,
  "isBid" as is_bid,
  COUNT("orderId") as num_orders,
  SUM(amount) as total_amount
FROM orderplaced
WHERE token = '0x20c0000000000000000000000000000000000002'
  AND NOT EXISTS (
    SELECT 1 FROM orderfilled
    WHERE orderfilled."orderId" = orderplaced."orderId"
      AND orderfilled."partialFill" = false
  )
  AND NOT EXISTS (
    SELECT 1 FROM ordercancelled
    WHERE ordercancelled."orderId" = orderplaced."orderId"
  )
GROUP BY price, is_bid
ORDER BY is_bid DESC, price
LIMIT 50`}
  signatures={["OrderPlaced", "OrderFilled", "OrderCancelled"]}
/>

### Inspect an individual order

#### Order details

Get detailed information about a specific order including its placement details, fill history, and cancellation status.

This query inspects the details of the most recent order for AlphaUSD. It shows when the order was created, at what price (tick), the order size, whether it's a flip order, and who placed it.

<IndexSupplyQuery
  title={'Order Placement Details'}
  query={`SELECT
  "orderId",
  tick,
  "isBid",
  amount,
  "isFlipOrder",
  "flipTick",
  maker,
  token,
  block_num,
  tx_hash
FROM orderplaced
WHERE token = '0x20c0000000000000000000000000000000000001'
ORDER BY block_num DESC
LIMIT 1`}
  signatures={["OrderPlaced"]}
/>

#### Order fill status

Check if an order has been partially or fully filled. This query shows up to 5 fill events for order number `2`, including the amount filled in each transaction and whether it was a partial fill.

<IndexSupplyQuery
  title={'Order Fill History'}
  query={`SELECT
  "orderId",
  "amountFilled",
  "partialFill",
  block_num,
  tx_hash
FROM orderfilled
WHERE "orderId" = 2
ORDER BY block_num DESC
LIMIT 5`}
  signatures={["OrderFilled"]}
/>

#### Cancelled orders

Check if an order has been cancelled. This query returns an order for AlphaUSD that was explicitly cancelled by the maker before being fully filled.

<IndexSupplyQuery
  title={'Order Cancellation Status'}
  query={`SELECT
  oc."orderId",
  oc.block_num,
  oc.tx_hash
FROM ordercancelled oc
INNER JOIN orderplaced op ON oc."orderId" = op."orderId"
WHERE op.token = '0x20c0000000000000000000000000000000000001'
ORDER BY op.block_num DESC
LIMIT 1`}
  signatures={["OrderCancelled", "OrderPlaced"]}
/>

### Get recent trade prices

View the last prices a token traded at to understand recent market activity.

This query joins order fill events with their corresponding placement details to show the price tick and amount for recent trades.

<IndexSupplyQuery
  title={'Recent Trade Prices for AlphaUSD'}
  query={`SELECT
  ofl.block_num,
  ofl."orderId",
  o.tick as price,
  ofl."amountFilled",
  o."isBid"
FROM orderfilled ofl
INNER JOIN orderplaced o
  ON ofl."orderId" = o."orderId"
WHERE o.token = '0x20c0000000000000000000000000000000000001'
ORDER BY ofl.block_num DESC
LIMIT 10`}
  signatures={["OrderFilled", "OrderPlaced"]}
/>

# Add Funds to Your Balance

Get test tokens to start building on Tempo testnet.

<Tabs>
  <Tab title="Fund your wallet">
    <div className="h-4" />

    Connect your wallet to receive test stablecoins directly.

    <div className="h-6" />

    <Demo.Container name="Connect and fund your wallet" footerVariant="balances" tokens={[Token.pathUsd, Token.alphaUsd, Token.betaUsd, Token.thetaUsd]} balanceSource="wallet">
      <Step.ConnectWallet stepNumber={1} />

      <Step.AddFundsToWallet stepNumber={2} />

      <Step.AddTokensToWallet stepNumber={3} />

      <Step.SetFeeToken stepNumber={4} last />
    </Demo.Container>
  </Tab>

  <Tab title="Fund an address">
    <div className="h-4" />

    Send test stablecoins to any address.

    <div className="h-6" />

    <Demo.Container name="Fund an address">
      <Step.AddFundsToOthers stepNumber={1} last />
    </Demo.Container>
  </Tab>

  <Tab title="cURL request">
    <div className="h-4" />

    Request tokens programmatically via the faucet API.

    <div className="h-4" />

    ```bash
    curl -X POST https://docs.tempo.xyz/api/faucet \
      -H "Content-Type: application/json" \
      -d '{"address": "<YOUR_ADDRESS>"}'
    ```

    <div className="h-4" />

    Replace `<YOUR_ADDRESS>` with a lowercase wallet address.
  </Tab>

  <Tab title="Cast RPC">
    <div className="h-4" />

    Request tokens using the `tempo_fundAddress` RPC method.

    <div className="h-4" />

    ```bash
    cast rpc tempo_fundAddress <YOUR_ADDRESS> \
      --rpc-url https://rpc.moderato.tempo.xyz
    ```

    <div className="h-4" />

    Replace `<YOUR_ADDRESS>` with your wallet address.
  </Tab>
</Tabs>

The faucet funds the following assets.

| Asset | Address |Amount|
|-------|---------|----:|
| [pathUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000000) | `0x20c0000000000000000000000000000000000000` | `1M` |
| [AlphaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000001) | `0x20c0000000000000000000000000000000000001` | `1M` |
| [BetaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000002) | `0x20c0000000000000000000000000000000000002` | `1M` |
| [ThetaUSD](https://explore.tempo.xyz/address/0x20c0000000000000000000000000000000000003) | `0x20c0000000000000000000000000000000000003` | `1M` |

## Verify Your Balance

After requesting tokens, verify your balance:

```bash
cast erc20 balance 0x20c0000000000000000000000000000000000001 \
  <YOUR_ADDRESS> \
  --rpc-url https://rpc.moderato.tempo.xyz
```

# Batch Transactions

One of the most powerful features of the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction) type is batching multiple operations into a single transaction. This allows you to execute several actions atomically (i.e., they all succeed or all fail together). This helps reduce gas costs, prevents partial failures, and creates better user experiences by combining multiple steps into one transaction.

:::info
Batch transactions are a feature of Tempo's [TempoTransaction type](/protocol/transactions/spec-tempo-transaction). See the TempoTransaction spec for complete details on batching and other features.
:::

## Example: Sending a Batch of Transactions

:::code-group

```ts [batchTransactions.ts]
const { address, hash, id } = await client.sendTransaction({ // [!code focus]
  calls: [{ // [!code focus]
    to: tokenAddress, // [!code focus]
    data: transferCalldata // Transfer tokens // [!code focus]
  }, // [!code focus]
  { // [!code focus]
    to: anotherTokenAddress,  // [!code focus]
    data: approveCalldata // Approve spending // [!code focus]
  }, // [!code focus]
  { // [!code focus]
    to: dexAddress, // [!code focus]
    data: swapCalldata // Execute swap // [!code focus]
  }], // [!code focus]
}) // [!code focus]
```

```ts [viem.config.ts]
// [!include ~/snippets/setup.ts:setup] 
```

:::

## How It Works

Unlike traditional EVM transactions which only support a single call per transaction, the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction) type natively supports a `calls` vector—enabling multiple operations in a single atomic transaction.

### Native Protocol Support

Batching is built directly into the transaction type at the protocol level. This means:

* **Atomic execution**: All calls succeed or all calls revert together—no partial failures
* **Single signature**: Sign once for the entire batch, reducing UX friction
* **Lower gas costs**: Avoid the overhead of multiple transaction submissions
* **No smart contract required**: Works with any EOA, no need to deploy a separate batching contract

### Transaction Structure

The `TempoTransaction` includes a `calls` field that accepts a list of operations:

```rust
pub struct TempoTransaction {
    // ... other fields
    calls: Vec<Call>,  // Batch of calls to execute atomically
    // ...
}

pub struct Call {
    to: TxKind,      // Target address or Create for contract deployment
    value: U256,     // ETH value to send
    input: Bytes,    // Calldata for the call
}
```

# Connect to Wallets

It is possible to use Tempo with EVM-compatible wallets that support the Tempo network,
or support adding custom networks (like MetaMask).

You can use these wallets when building your application on Tempo.

This guide will walk you through how to set up your application to connect to wallets.

<Demo.Container name="Connect to Wallets" footerVariant="source" src="tempoxyz/examples/tree/main/examples/accounts">
  <Step.ConnectWallet stepNumber={1} last />
</Demo.Container>

## Wagmi Setup

::::steps

### Set up Wagmi

Ensure that you have set up your project with Wagmi by following the [guide](/sdk/typescript#wagmi-setup).

### Configure Wagmi

Next, let's ensure Wagmi is configured correctly to connect to wallets.

Ensure we have [`multiInjectedProviderDiscovery`](https://wagmi.sh/react/api/createConfig#multiinjectedproviderdiscovery) set to `true` to display injected browser wallets.

We can also utilize [wallet connectors](https://wagmi.sh/react/api/connectors) from Wagmi like `metaMask` to support mobile devices.

```tsx twoslash [config.ts]
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { metaMask } from 'wagmi/connectors' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [metaMask()], // [!code ++]
  multiInjectedProviderDiscovery: true, // [!code ++]
  transports: {
    [tempo.id]: http(),
  },
})
```

### Display Connect Buttons

After that, we will set up "Connect" buttons so that the user can connect to their wallet.

We will create a new `ConnectWallet.tsx` component to work in.

:::code-group

<div data-title="Preview">
  <ConnectWallet />
</div>

<div data-title="">
  <div />
</div>

:::

:::code-group

```tsx twoslash [Connect.tsx]
// @noErrors
import { useConnect, useConnectors } from 'wagmi'

export function Connect() {
  const connect = useConnect()
  const connectors = useConnectors()

  return (
    <div>
      {connectors.map((connector) => (
        <button
          key={connector.id}
          onClick={() => connect.connect({ connector })}
          type="button"
        >
          {connector.name}
        </button>
      ))}
    </div>
  )
}

```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { metaMask } from 'wagmi/connectors' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [metaMask()], // [!code ++]
  multiInjectedProviderDiscovery: true, // [!code ++]
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Display Account & Sign Out

After the user has connected to their wallet, we can display the account information and a sign out button.

We will create a new `Account.tsx` component to work in.

:::code-group

<div data-title="Preview">
  <ConnectWallet showAddChain={false} />
</div>

<div data-title="">
  <div />
</div>

:::

:::code-group

```tsx twoslash [Account.tsx]
// @noErrors
import { useConnection, useDisconnect } from 'wagmi'

export function Account() {
  const account = useConnection()
  const disconnect = useDisconnect()

  return (
    <div>
      <div>
        {account.address?.slice(0, 6)}...{account.address?.slice(-4)}
      </div>
      <button onClick={() => disconnect.disconnect()}>
        Sign out
      </button>
    </div>
  )
}

```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { metaMask } from 'wagmi/connectors' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [metaMask()], // [!code ++]
  multiInjectedProviderDiscovery: true, // [!code ++]
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Display "Add Tempo" Button

If the wallet is not on the Tempo network, we can display a "Add Tempo" button so that the user can add the network to their wallet.

:::code-group

<div data-title="Preview">
  <ConnectWallet />
</div>

<div data-title="">
  <div />
</div>

:::

:::code-group

```tsx twoslash [Account.tsx]
// @noErrors
import { useConnection, useDisconnect, useSwitchChain } from 'wagmi'
import { tempoModerato } from 'viem/chains' // [!code ++]

export function Account() {
  const account = useConnection()
  const disconnect = useDisconnect()
  const switchChain = useSwitchChain() // [!code ++]

  return (
    <div>
      <div>
        {account.address?.slice(0, 6)}...{account.address?.slice(-4)}
      </div>
      <button onClick={() => disconnect.disconnect()}>
        Sign out
      </button>

      <button // [!code ++]
        onClick={() => {/* [!code ++] */}
          switchChain.switchChain({ // [!code ++]
            chainId: tempo.id, // [!code ++]
            addEthereumChainParameter: { // [!code ++]
              nativeCurrency: { // [!code ++]
                name: 'USD', // [!code ++]
                decimals: 18, // [!code ++]
                symbol: 'USD', // [!code ++]
              }, // [!code ++]
            }, // [!code ++]
          }) // [!code ++]
        } // [!code ++]
      > {/* [!code ++] */}
        Add {chain.name} to wallet {/* [!code ++] */}
      </button> {/* [!code ++] */}
    </div>
  )
}

```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { metaMask } from 'wagmi/connectors' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [metaMask()], // [!code ++]
  multiInjectedProviderDiscovery: true, // [!code ++]
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

::::

## Third-Party Libraries

You can also use a third-party Wallet Connection library to handle the onboarding & connection of wallets.

Such libraries include: [Privy](https://privy.io), [ConnectKit](https://docs.family.co/connectkit), [AppKit](https://reown.com/appkit), [Dynamic](https://dynamic.xyz), and [RainbowKit](https://rainbowkit.com).

The above libraries are all built on top of Wagmi, handle all the edge cases around wallet connection.

:::warning
It is worth noting that some wallets that are included in the above libraries may not support Tempo yet. We are working on adding support for the majority of wallets.
:::

## Add to Wallet Manually

You can add Tempo testnet to a wallet that supports custom networks (e.g. MetaMask) manually.

For example, if you are using MetaMask:

1. Open MetaMask and click on the menu in the top right and select "Networks"
2. Click "Add a custom network"
3. Enter the network details:

| **Name** | `Tempo Testnet (Moderato)` |
|-------------------|-------|
| **Currency** | `USD` |
| **Chain ID** | `42431` |
| **HTTP URL** | `https://rpc.moderato.tempo.xyz` |
| **WebSocket URL** | `wss://rpc.moderato.tempo.xyz` |
| **Block Explorer** | [`https://explore.tempo.xyz`](https://explore.tempo.xyz) |

The official documentation from MetaMask on this process is also available [here](https://support.metamask.io/configure/networks/how-to-add-a-custom-network-rpc#adding-a-network-manually).

:::warning
Note that we recommend using the `symbol` "USD" for the currency symbol, despite there being no native gas token. Existing wallets like MetaMask don't natively support the Tempo network yet, so there are some quirks to the interface.
You might also need to set `nativeCurrency.decimals` to `18` instead of `6` in some wallets.
:::

# Embed Passkey Accounts

Create a domain-bound passkey account on Tempo using WebAuthn signatures for secure, passwordless authentication with [Tempo transactions](/protocol/transactions/spec-tempo-transaction).

Passkeys enable users to authenticate with biometrics (fingerprint, Face ID, Touch ID) they already use for other apps. Keys are stored in the device's secure enclave and sync across devices via iCloud Keychain or Google Password Manager.

:::info

**What does "domain-bound" mean?**

WebAuthn credentials are bound to a specific domain (the [Relying Party](https://en.wikipedia.org/wiki/Relying_party)).

This means that credentials created for one domain (e.g., `example.com`) will only work on that domain (and its subdomains) and cannot be used to authenticate on other domains.

This means your users won't be able to use the same passkey account on other applications. If this is not what you want, head to the [Connect to wallets](/guide/use-accounts/connect-to-wallets)
guide that walks you through on how to connect your application to a universal wallet like MetaMask.

:::

## Demo

By the end of this guide, you will be able to embed passkey accounts into your application.

<Demo.Container name="Passkey Accounts" footerVariant="source" src="tempoxyz/examples/tree/main/examples/accounts">
  <EmbedPasskeys />
</Demo.Container>

## Steps

::::steps

### Set up Wagmi

Ensure that you have set up your project with Wagmi by following the [guide](/sdk/typescript#wagmi-setup).

### Configure the WebAuthn Connector

Next, we will need to configure the `webAuthn` connector in our Wagmi config.

```tsx twoslash [config.ts]
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({ // [!code ++]
    keyManager: KeyManager.localStorage(), // [!code ++]
  })], // [!code ++]
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::warning

The `KeyManager.localStorage()` implementation is not recommended for production use as it stores public keys on the client device, meaning it cannot be re-extracted when the user's storage is cleared or if the user is on another device.

For production, you should opt for a remote key manager such as [`KeyManager.http`](https://wagmi.sh/tempo/keyManagers/http).

:::

:::tip

This Wagmi configuration sets `multiInjectedProviderDiscovery` to `false` to
prevent injected browser wallets from being detected, and to prefer the `webAuthn` connector.
If you would like to allow connection to other wallets, set this property to `true`.

:::

### Display Sign In Buttons

After that, we will set up "Sign in" and "Sign up" buttons so that the user can create
or use a passkey with the application.

We will create a new `Example.tsx` component to work in.

:::code-group

<div data-title="Preview">
  <SignInButtons />
</div>

:::

:::code-group

```tsx twoslash [Example.tsx]
// @noErrors
import { useConnect, useConnectors } from 'wagmi'

export function Example() {
  const connect = useConnect()
  const [connector] = useConnectors()

  return (
    <div>
      <button
        onClick={() =>
          connect.connect({
            connector,
            capabilities: { type: 'sign-up' },
          })
        }
      >
        Sign up
      </button>

      <button onClick={() => connect.connect({ connector })}>
        Sign in
      </button>
    </div>
  )
}

```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({ // [!code ++] 
    keyManager: KeyManager.localStorage(), // [!code ++]
  })], // [!code ++]
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Display Account & Sign Out

After the user has signed in, we can display the account information and a sign out button.

:::code-group

<div data-title="Preview">
  <EmbedPasskeys />
</div>

<div data-title="">
  <div />
</div>

:::

:::code-group

```tsx twoslash [Example.tsx]
// @noErrors
import { useConnection, useConnect, useConnectors, useDisconnect } from 'wagmi'

export function Example() {
  const account = useConnection() // [!code ++]
  const connect = useConnect()
  const [connector] = useConnectors()
  const disconnect = useDisconnect() // [!code ++]

  if (account.address) // [!code ++]
    return ( // [!code ++]
      <div> {/* [!code ++] */}
        <div>{account.address.slice(0, 6)}...{account.address.slice(-4)}</div> {/* [!code ++] */}
        <button onClick={() => disconnect.disconnect()}>Sign out</button> {/* [!code ++] */}
      </div> {/* [!code ++] */}
    ) // [!code ++]

  return (
    <div>
      <button
        onClick={() =>
          connect.connect({
            connector,
            capabilities: { type: 'sign-up' },
          })
        }
      >
        Sign up
      </button>

      <button onClick={() => connect.connect({ connector })}>
        Sign in
      </button>
    </div>
  )
}

```

```tsx twoslash [config.ts] filename="config.ts"
// @noErrors
import { createConfig, http } from 'wagmi'
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo' // [!code ++]

export const config = createConfig({
  chains: [tempoModerato],
  connectors: [webAuthn({ // [!code ++]
    keyManager: KeyManager.localStorage(), // [!code ++]
  })], // [!code ++]
  multiInjectedProviderDiscovery: false,
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

### Next Steps

Now that you have created your first passkey account, you can now:

* learn the [Best Practices](#best-practices) below
* follow a guide on how to [make a payment](#TODO), [create a stablecoin](#TODO), and [more](#TODO) with a passkey account.

::::

## Best Practices

### Loading State

When the user is logging in or signing out, we should show loading state to indicate that the process is happening.

We can use the `isPending` property from the `useConnect` hook to show pending state to the user.

```tsx twoslash [Example.tsx]
// @noErrors
import { useConnection, useConnect, useConnectors, useDisconnect } from 'wagmi'

export function Example() {
  const account = useConnection()
  const connect = useConnect()
  const [connector] = useConnectors()
  const disconnect = useDisconnect()

  if (connect.isPending) // [!code ++]
    return <div>Check prompt...</div> {/* [!code ++] */}
  return (/* ... */)
}
```

:::tip

Wagmi exposes [React Query's](https://tanstack.com/query/latest/docs/framework/react/overview) interfaces on all Hooks to extract asynchronous states such as loading (e.g. `isPending`) and error (e.g. `isError`, `error`) states.

:::

### Error Handling

If an error unexpectedly occurs, we should display an error message to the user.

We can use the `error` property from the `useConnect` hook to show error state to the user.

```tsx twoslash [Example.tsx]
// @noErrors
import { useConnection, useConnect, useConnectors, useDisconnect } from 'wagmi'

export function Example() {
  const account = useConnection()
  const connect = useConnect()
  const [connector] = useConnectors()
  const disconnect = useDisconnect()

  if (connect.error) // [!code ++]
    return <div>Error: {connect.error.message}</div> {/* [!code ++] */}
  return (/* ... */)
}
```

## Learning Resources

<Cards>
  <Card description="Learn more about the Tempo transaction type that enables passkey signatures" to="/guide/use-accounts/webauthn-p256-signatures" icon="lucide:file" title="Tempo Transaction type" />

  <Card description="Learn more about how (passkey) signatures are structured in the protocol" to="/guide/use-accounts/webauthn-p256-signatures" icon="lucide:signature" title="Signatures" />
</Cards>

# Scheduled Transactions

Execute transactions only within a specific time window using `validAfter` and `validBefore` timestamps.

Scheduled transactions are enabled by the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction) type, which includes optional timestamp fields. These fields are validated by the protocol when the transaction is submitted.

## Setting Time Bounds

You can add optional timestamp fields to your transaction to control when it can be executed. Both `validAfter` and `validBefore` accept Unix timestamps.

For example, to create a transaction that can only execute between Jan 1, 2025 and Jan 2, 2025, you would set `validAfter: 1735689600` and `validBefore: 1735776000` when signing the transaction.

## Time Window Validation

The protocol validates timestamps against the block timestamp:

* **`validAfter`**: Block timestamp must be greater than or equal to this value
* **`validBefore`**: Block timestamp must be less than or equal to this value
* **Both optional**: Omit either or both to not restrict that bound

You can use these fields individually or in combination:

* **Only `validAfter`**: Transaction can execute any time after the specified date (e.g., after Jan 1, 2025)
* **Only `validBefore`**: Transaction must execute by the specified date (e.g., before Jan 2, 2025)
* **Both**: Transaction has a specific time window for execution
* **Neither**: No time restrictions

## Examples

### Example: Vesting Schedule

Release tokens at a specific future time by pre-signing a transaction with a future `validAfter` timestamp.

You would sign a token transfer transaction that includes `validAfter: 1767225600` (Jan 1, 2026). The signed transaction can be stored off-chain or given to a third party. When Jan 1, 2026 arrives, anyone can submit the signed transaction to the network, and it will execute. If submitted before that date, validators will reject it.

This enables trustless vesting schedules where the beneficiary holds a pre-signed transaction that becomes valid at a specific future date.

### Example: Time-Limited Offer

You can create an offer that expires if not accepted by setting both `validAfter` and `validBefore` timestamps.

For example, to create an offer valid for 24 hours, you would set `validAfter` to the current timestamp and `validBefore` to 86400 seconds (24 hours) in the future. The signed transaction can only be executed within that 24-hour window. After the expiration time passes, the transaction becomes invalid and cannot be included in a block.

### Example: Delayed Execution

You can sign a transaction now that can only be executed at a future time by setting `validAfter` to a timestamp 7 days in the future.

The signed transaction is then stored (in a database, onchain via a contract, or held by a party). After the 7-day delay period passes, anyone with access to the signed transaction can submit it to the network for execution. The protocol enforces that the transaction cannot be included in a block before the specified time.

This is useful for governance proposals with timelock requirements or delayed contract upgrades.

## Storing Scheduled Transactions

:::info
**Important**: It is your responsibility to store and manage signed scheduled transactions until their execution time. The protocol validates the time constraints but does not store transactions for you.
:::

When you create a scheduled transaction, you have several options for storage:

* **Self-custody**: Store the signed transaction in your own database or secure storage until the execution time
* **Third-party services**: Work with a company that specializes in holding and submitting scheduled transactions at the appropriate time
* **Smart contracts**: Store the signed transaction onchain in a contract that can submit it when the time window is valid

The Tempo team is actively exploring the design of a protocol-level scheduled transaction feature that would eliminate the need for off-chain storage. If this capability is valuable to your use case, please contact us to share your requirements and help inform the design.

## Mempool Behavior

Validators will reject transactions that are outside their validity window:

* **Too early**: Transactions with `validAfter` in the future won't be included in blocks. The transaction will be rejected if you try to submit it before the specified time.
* **Too late**: Transactions with `validBefore` in the past will be rejected. Once the expiration time passes, the transaction can no longer be executed.

For example, if you submit a transaction with `validAfter` set to Jan 1, 2026, validators will return an error until that timestamp is reached.

## Combining with Other Features

**Fee sponsorship**: You can combine scheduled transactions with fee sponsorship, where a sponsor pays the fees for a time-locked transaction. The fee payer signs their portion, and the combined transaction becomes valid only within the specified time window.

**Batch transactions**: Multiple operations can be scheduled together to execute atomically within a specific time window. All operations in the batch must succeed or fail together, and the entire batch is subject to the time constraints.

:::warning
The block timestamp is set by validators and may vary slightly. For critical timing, account for small time variations (±15 seconds).
:::

## Technical Details

For complete specifications on timestamp validation, see the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction) type specification.

# WebAuthn & P256 Signatures

Tempo EOA addresses can be derived from multiple signature types. Allowing you to sign transactions with standard Ethereum wallets, hardware security keys, biometric authentication like Face ID and Touch ID, or even using [passkeys](https://passkeys.dev/).

## Supported signature types

### secp256k1

The standard Ethereum signature format. No type identifier needed, this is the default.

### P256

Raw P256 signatures that include the public key coordinates. Identified by type `0x01`.

The `preHash` flag indicates whether the digest should be hashed with SHA256 before verification. Set this to `true` if using Web Crypto API or similar implementations that require pre-hashing.

### WebAuthn

WebAuthn signatures include authenticator data from biometric devices. Identified by type `0x02`.

The verification data contains information from the authenticator (device metadata, user presence flags, etc.).

## Address derivation

### secp256k1

Standard Ethereum address derivation: `keccak256(uncompressed_public_key)[12:32]`.

### P256 and WebAuthn

Both P256 and WebAuthn derive addresses from the public key coordinates: `keccak256(pub_key_x || pub_key_y)[12:32]`.

:::info\[Shared address space]
P256 and WebAuthn use identical address derivation, so the same key pair produces the same address regardless of signature type. A passkey can authorize transactions via raw P256 signatures and vice versa.
:::

***

:::info
Additional signature types may be supported in the future. For complete technical specifications, see the [Tempo Transaction](/protocol/transactions/spec-tempo-transaction) protocol documentation.
:::

# Onchain FX

An overwhelming majority of cross-border payments facilitated by stablecoins use what is known as the stablecoin sandwich: the onchain leg is conducted in stablecoins, typically USD-denominated, with on- and off-ramps converting from/to a local currency.

## Accessing FX Liquidity Onchain

Tempo is exploring a design to enable stablecoin users to access FX liquidity directly onchain, including via a set of regulated non-USD stablecoin issuers. This removes the need for off-chain currency conversion and enables seamless multi-currency flows entirely onchain.

When available, users will be able to:

* Exchange between USD and non-USD stablecoins directly onchain
* Access competitive FX rates through decentralized liquidity pools
* Execute cross-border payments without relying on traditional FX providers
* Reduce settlement times and costs associated with currency conversion

## Multi-Currency Fee Payments

When available, Tempo will also allow users to pay for network fees in currencies beyond USD. This means users would be able to interact with Tempo in their preferred currency without needing to hold USD stablecoins specifically for transaction fees.

## Coming Soon

Onchain FX is currently in development and will be available in a future release. This feature is being designed in close collaboration with regulated stablecoin issuers to ensure it meets compliance requirements while providing the flexibility and efficiency that global payment flows demand.

If you're interested in multi-currency payment flows and want to explore how onchain FX can benefit your use case, reach out to our team.

## Help design this feature

<Cards>
  <Card description="Interested in multi-currency flows? Reach out to help design onchain FX capabilities." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Partner With Us" />
</Cards>

# Tempo Transactions \[Modern, optimized, and highly scalable blockchain transactions]

Tempo has built-in support for gas sponsorship, batch transactions, scheduled payments, and modern authentication through passkeys. These features are often grouped together as "smart accounts" or "account abstraction."

On other chains, even when available, these are generally add-on functionalities that require third-party providers to unlock. By natively enabling these features at the protocol level, developers on Tempo can deploy payment logic without managing additional middleware or custom contracts, and can build to enshrined standards.

Tempo Transactions are built into the protocol so developers don't need custom smart contracts or third-party middleware to get batching, sponsorship, scheduling, and modern auth. This reduces integration risk and operational overhead for payment applications.

## Batched Payments

Payment processors and platforms often need to send thousands of payments at once (e.g., payroll runs, merchant settlements, customer refunds). Tempo supports batch transactions where multiple operations execute atomically in a single transaction.

This unlocks high-volume use cases: orchestrators can submit thousands of payouts as a single operation, rather than submitting them one-by-one and tracking individual success or failure. If any operation in the batch fails, the entire batch reverts, ensuring atomic execution across all payments. This is critical for payment operators who need guaranteed settlement guarantees for their workflows.

## Fee Sponsorship

Applications often want to pay transaction fees on behalf of their users. For instance, to simplify onboarding, to improve the user experience, or to remove friction from their payment flows.

Tempo's protocol-level fee sponsorship allows an account to sign a transaction while a separate sponsor (typically the application) pays the gas fee. This means end users can interact with your application without holding any tokens for fees, dramatically lowering the barrier to entry.

## Configurable Fee Tokens

Tempo supports paying transaction fees in USD-denominated stablecoins. This removes the need for users to acquire a volatile gas token and simplifies accounting for payment applications operating in dollars. Users can pay fees in any supported USD stablecoin, and the protocol handles conversion automatically.

## Scheduled Payments

The Tempo transaction type includes scheduling as a protocol feature. Users can specify a time window for transaction execution, and validators will include the transaction when it becomes valid.

This enables "set and forget" payment operations directly at the protocol level, enabling recurring payments like subscriptions or scheduled disbursements. No need for external automation services or off-chain infrastructure to manage recurring transactions.

## Modern Authentication

Tempo supports passkey authentication through WebAuthn/P256 signature validation, built directly into the protocol. Users can authenticate with the same biometrics (fingerprint, Face ID) they already use for other apps.

Their keys are stored in their device's secure enclave, and passkeys sync across devices via services they already use such as iCloud Keychain or Google Password Manager. This way, users don't need to secure a 12 or 24-word seed phrase for traditional wallets. For payment applications, this means onboarding flows can be as simple as existing consumer apps, without sacrificing security.

Tempo uses an [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718) transaction type with native support for these features.

## Use Cases

Tempo Transactions provide the features necessary to bring a wide range of payment use cases onchain:

### Payroll and Merchant Payouts

Batch transactions allow large payout runs to be processed efficiently and securely. Payments execute in a single atomic batch: the entire batch succeeds as a single transaction, eliminating partial failures and manual reruns.

See: [Global payouts with stablecoins](/learn/use-cases/global-payouts)

### Wallets and Neobanks

Fee sponsorship removes gas from the user experience entirely. Combined with passkey authentication, users interact with a familiar fintech-grade interface with all of the blockchain complexity abstracted away.

### Commerce

As stablecoin adoption grows, platforms need flexibility in how fees are paid. Configurable fee tokens allow transaction fees to be paid in any USD stablecoin, while fee sponsorship enables merchants to offer seamless checkout experiences for users.

See: [TIP-20 Tokens](/learn/tempo/native-stablecoins) for stable fees and payment memos.

### Subscriptions

Scheduled transactions automate recurring payments and enable true subscription services onchain. No need for external automation services or custom smart contracts.

## Partner Ecosystem

Infrastructure partners including [Crossmint](https://www.crossmint.com/), [Fireblocks](https://www.fireblocks.com/), [Privy](https://www.privy.io/), and [Turnkey](https://www.turnkey.com/) support Tempo Transactions and can help accelerate your development. Visit the [Ecosystem](https://tempo.xyz/ecosystem) to explore Tempo's growing network of partners.

For partner testimonials and rollout context, see [Introducing Tempo Transactions](https://tempo.xyz/blog/tempo-transactions).

## Next steps

<Cards>
  <Card title="Protocol docs" description="Full spec and developer reference for Tempo Transactions." to="/protocol/transactions" icon="lucide:file-code" />

  <Card title="Global payouts use case" description="How batching and stable fees improve payout operations." to="/learn/use-cases/global-payouts" icon="lucide:send" />

  <Card title="Deep dive blog post" description="Announcement, context, and partner quotes." to="https://tempo.xyz/blog/tempo-transactions" icon="lucide:book-open" />
</Cards>

# TIP-20 Tokens \[Tempo's native stablecoin token standard]

Tempo extends the [ERC-20 standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) used on EVM chains (Ethereum, Base, Arbitrum) with additional features, and enshrines them in protocol as the TIP-20 contract suite. These features are purpose-built for payment use cases at scale.

## Predictable Payment Throughput

Tempo has dedicated payment lanes: reserved blockspace for payment transactions (specifically, TIP-20 token transfers) that other applications cannot consume. Payments have guaranteed blockspace reserved at the protocol level and don't compete with other traffic like NFT mints, liquidations, or high-frequency contract calls.

Even if there are extremely popular applications on the chain competing for blockspace, payroll runs or customer disbursements execute predictably. Fees stay low and stable even when other network activity spikes, with a target of one-tenth of a cent per payment transaction. For payment processors, that means no "downtime" from congestion, and predictable economics for high-volume flows.

There is no "noisy neighbor problem" like on traditional blockchains, where blockspace can fill up or cost orders of magnitude more during times of intense activity.

## Low, Predictable Fees, in Stables

Transaction fees can be paid directly in USD-denominated stablecoins. This removes the need for volatile gas tokens and lets payment applications operate entirely in the same currency as their underlying flows, ensuring predictable costs and simpler accounting.

For wallets and custodians, this removes the need to hold a balance of new cryptoassets just to facilitate stablecoin payments. Users can pay fees in any USD stablecoin, and validators can receive fees in any USD stablecoin, with the protocol automatically converting between them using onchain liquidity through Tempo's built-in DEX.

Costs are predictable and low: TIP-20 transfers target one-tenth of a cent per transaction. This removes a major barrier for mainstream adoption. Users can interact with Tempo using only the stablecoins they're already familiar with, without needing to understand or manage volatile crypto assets.

For how applications sponsor fees and batch payments, see [Tempo Transactions](/learn/tempo/modern-transactions).

## Native Reconciliation

Tempo's TIP-20 tokens can natively attach a short memo directly to each transfer. This mirrors traditional payment systems, where every transaction carries context (e.g., an invoice number, a customer ID, a cost center, or a simple reference note) for backend systems to automatically match payments to internal records.

For larger memos, Tempo supports flexible approaches where only a commitment (like a hash or locator) travels onchain while the full data (including PII) lives off-chain. This means finance teams can automatically match payments to invoices and payment processors can embed the structured data their systems need without custom solutions or integration with third-party reconciliation infrastructure.

See stablecoin reconciliation in practice: [Global payouts](/learn/use-cases/global-payouts) and [Tokenized deposits](/learn/use-cases/tokenized-deposits).

## Built-in Compliance

Stablecoin (and other regulated asset) issuers operate under regulatory requirements. They need to enforce whitelists (only approved addresses can transact) or blacklists (sanctioned addresses cannot transact).

Tempo provides a shared compliance infrastructure through the TIP-403 Policy Registry. An issuer can thus create a single policy with their compliance rules, and multiple tokens they issue can adopt that policy. When the compliance manager updates the policy, all tokens using it automatically enforce the new rules, unlike traditional blockchains where an issuer must update each contract one-by-one.

## Built-in Stable Asset DEX

Tempo includes a native decentralized exchange optimized for stablecoins and tokenized deposits. This means users can pay fees in any USD stablecoin, and validators can receive fees in any USD stablecoin, with the protocol automatically converting between them using onchain liquidity.

## When TIP-20 matters

Use TIP-20 when you need:

* **Predictable throughput** for large payment runs without congestion-driven fee spikes.
* **Stable-denominated fees** for simpler unit economics.
* **Reconciliation metadata** to tie onchain transfers to invoices and ERP records.
* **Shared compliance enforcement** across multiple regulated assets.

For basic token functionality without these requirements, standard ERC-20 contracts work on Tempo as they do on any EVM chain.

## Use Cases for Custom Stablecoins

Beyond peer-to-peer payments, custom stablecoins built on TIP-20 can be designed for specific treasury, settlement, and foreign exchange use cases:

### Corporate Treasury Management

Custom stablecoins can streamline global treasury operations, allowing funds to move instantly between subsidiaries. TIP-20's reward distribution enables reserve income to be shared across business units without complex off-chain accounting.

### Cross-border Payments

Stablecoins allow smaller banks and payment providers to participate in cross-border flows without correspondent banking networks. TIP-20's native transfer memos enable reconciliation between stablecoin transactions and existing payment engines that support SWIFT messaging.

### Wholesale Settlement and Deposit Tokens

Policy registries enable permissioned stablecoins and deposit tokens for bank-to-bank settlement. Issuers can enforce transfer rules directly at the token level, supporting regulated and wholesale payment systems.

### Interest-bearing Stablecoins

TIP-20 simplifies interest-bearing stablecoin issuance with native yield distribution. Issuers can programmatically share yield with users and intermediaries in real time, eliminating manual calculations and off-chain reconciliation.

### Non-USD Stablecoins and Onchain FX

A global stablecoin ecosystem requires currencies beyond USD. TIP-20 tokens include an optional currency identifier specifying the fiat currency they represent. Tempo's native DEX will enable onchain foreign exchange between stablecoins.

## FAQs

### Is TIP-20 compatible with ERC-20 tooling?

TIP-20 extends ERC-20 semantics for payment-scale features while remaining familiar to EVM developers. Most indexers and wallet patterns still apply, but advanced features (memos, policy registry) require TIP-20-aware integrations.

### How big can a reconciliation memo be?

TIP-20 supports short onchain memos for common references (invoice ID, customer ID). For larger data, store details offchain and put only a commitment or locator onchain to avoid leaking PII.

### How should issuers handle compliance updates?

Use the TIP-403 Policy Registry so multiple tokens can share a policy and inherit updates automatically, rather than updating each token contract individually.

## Infrastructure Partners

Work with infrastructure partners who are rolling out TIP-20 support to accelerate your development:

* [AllUnity](https://allunity.com/) - Regulated euro stablecoins for European corporates
* [Bridge](https://www.bridge.xyz/) - Custom regulated stablecoin issuance with off-the-shelf templates
* [LayerZero](https://layerzero.network/) - Cross-chain token extensions for Tempo's payment ecosystem

## Related reading

<Cards>
  <Card title="Deep dive: TIP-20" description="Full feature walkthrough and design rationale." to="https://tempo.xyz/blog/tip20" icon="lucide:book-open" />

  <Card title="Tempo Transactions" description="Batching, sponsorship, and scheduling primitives." to="/learn/tempo/modern-transactions" icon="lucide:layers" />

  <Card title="Tokenized deposits" description="Treasury and liquidity management use case." to="/learn/use-cases/tokenized-deposits" icon="lucide:building-2" />
</Cards>

# Performance \[Tempo's performant blockchain architecture]

All of Tempo's payments-first features are built on a foundation of a highly performant blockchain. Tempo delivers the throughput and finality characteristics that payment applications require.

## High Throughput

Tempo is built on the [Reth](https://reth.rs/) SDK, the most performant and flexible EVM (Ethereum Virtual Machine) execution client. Reth is also relied upon by several other blockchains including Ethereum, Base and Arc.

Tempo houses the team that built and maintains Reth, and several other pieces of core blockchain developer software such as [Foundry](https://getfoundry.sh/). We are already benchmarking 20,000 TPS on testnet with a clear line of sight to an order of magnitude higher by mainnet.

This throughput is critical for payment use cases. Whether processing payroll for thousands of employees, settling marketplace transactions, or handling microtransactions at scale, Tempo's performance ensures that your payment flows won't be bottlenecked by blockchain capacity.

## Fast Finality

Public blockchains that support financial activity need to balance two contradictory demands.

On the one hand, the blockchain needs fast finality: a payment made on the blockchain should be quickly confirmed as final, with no risk of being "re-orged" out as can happen on many blockchains today.

On the other hand, the blockchain also needs to degrade gracefully under suboptimal network conditions. Tempo uses Simplex Consensus (via [Commonware](https://www.commonware.xyz/)), which provides fast, sub-second finality in normal conditions while maintaining graceful degradation under adverse networks.

Tempo uses Byzantine-fault tolerant consensus with four validators on testnet. Blocks are finalized every ~0.5 seconds, and once a block is marked as final, transactions in that block are guaranteed to be included in the chain. This cutting-edge consensus algorithm optimally balances speed with resilience.

For payment applications, this gives payment operators the same settlement certainty they expect from existing financial systems, with speed that matches best-in-class blockchains. This is critical for use cases like point-of-sale systems, instant settlements, and cross-border transfers where users expect immediate, irreversible confirmation.

# Privacy

Tempo is also developing opt-in privacy features designed to coexist with issuer compliance requirements. This functionality will enable private balances and transfers while maintaining the auditability and reporting capabilities that regulated issuers need.

## Private Token Standard for Stablecoin Issuers

Traditional blockchains make all transaction data publicly visible, which creates challenges for businesses and consumers who need confidentiality. At the same time, regulated stablecoin issuers must maintain compliance and auditability.

We're currently working on multiple designs which provide:

* **Private balances**: Account balances that are hidden from public view while remaining auditable by authorized parties
* **Confidential transfers**: Transaction amounts and participants that can be shielded from the public ledger
* **Selective disclosure**: Issuers and regulators that can maintain the visibility they need for compliance without exposing sensitive business data publicly

## Use Cases for Privacy

When available, private tokens will enable:

**Sensitive business transactions**: Companies will be able to conduct payroll, vendor payments, and treasury operations without revealing confidential financial information to competitors or the public.

**Confidential consumer balances**: Users will be able to hold and transact with stablecoins without publicly broadcasting their account balances or spending patterns.

**Privacy-preserving payment flows**: Platforms will be able to process payments while protecting user privacy and maintaining confidentiality in sensitive transactions.

All of this is achieved while preserving the compliance features that make stablecoins viable in regulated markets. Issuers will be able to maintain the ability to monitor, report, and enforce policies as required by regulation.

## Coming Soon

The native private token standard is currently in development and will be available in a future release. This feature is being designed in close partnership with regulated stablecoin issuers to ensure it meets both privacy needs and regulatory requirements.

If you're interested in private payment flows and want to explore how privacy features can benefit your use case, reach out to our team.

## Help design this feature

<Cards>
  <Card description="Interested in privacy-preserving payments? Reach out to help design compliant privacy features." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Partner With Us" />
</Cards>

# Power AI agents with programmable money \[Enable autonomous agents to purchase goods, services, and digital resources with real-time, programmable stablecoin payments.]

## The rise of autonomous agents

Autonomous agents are increasingly able to purchase goods and services, negotiate discounts, and manage everyday tasks without human input. An agent might reorder groceries when supplies run low, find better deals on household items, pay for digital services, manage streaming or app subscriptions, or book travel based on preferences and schedules.

Further, the agentic commerce ecosystem is evolving quickly. New protocols are emerging that enable agents to interact directly with merchants: browsing offers, comparing terms, and purchasing goods or services autonomously. These protocols will allow businesses to sell directly to autonomous agents, whether they offer physical goods, digital items, compute, APIs, or data streams.

## The challenge with traditional payment rails

However, for autonomous agents to function reliably, they need real-time, digitally native money that matches the speed and autonomy of their decisions. This money must be available 24/7, settle instantly, and support frequent microtransactions without friction. It also needs to work seamlessly across borders and offer in-built programmability so agents can operate without human intervention.

Traditional payment rails were not designed to meet these requirements. Although card tokenization is being explored as a way for agents to pay, cards were never intended for machine-to-machine interactions. The entire card ecosystem is built around human cardholders and fraud models designed to stop bots, not support them.

## How stablecoins solve this

Stablecoins fill this gap. They provide a stable, programmable representation of money that agents can use autonomously. Stablecoins combine the familiarity of fiat value with the instant, global settlement of public blockchains. Agents can hold stablecoins, pay for goods or services, and transact with other agents without relying on intermediaries.

Agents also need an easy way to access payment credentials. Creating cards or card tokens requires coordination with issuers, and, in many cases, manual workflows. In contrast, onchain wallets can be provisioned instantly, at massive scale, and without relying on banking partners. Wallets give agents a ready-to-use financial instrument the moment they are created.

## Benefits beyond speed and cost

For developers building agentic platforms, stablecoins and wallets are far simpler and more flexible to work with than traditional payment instruments. Wallets can be created instantly and at scale, without issuer partnerships or card-provisioning workflows. Stablecoins also make it easy to top up agent balances instantly whenever additional funds are needed.

Developers can also set spending limits, enforce policy rules, and implement automatic top-ups directly in code, ensuring agents always have the funds they need without human intervention. Stablecoin balances can be monitored and rebalanced programmatically, enabling precise liquidity management and predictable spending across large fleets of autonomous agents.

As agentic commerce begins to scale, the need for a more native payment rail becomes unavoidable. Stablecoins provide exactly the properties agents require: real-time global settlement, programmable behavior, and the ability to operate without intermediaries or issuer dependencies. They offer payment infrastructure that aligns with how agents think, act, and transact.

## Building with Tempo

Autonomous agents require payment rails that are as programmable and tireless as they are. Tempo offers the throughput and sub-second settlement needed to support agent fleets at scale, without the friction of traditional card networks.

If you are architecting payment flows for autonomous systems, we can help you understand how to implement automated wallet provisioning and policy-based spending controls directly into your agent's code.

<Cards>
  <Card description="Want to explore this use case on Tempo? Email us to learn more about building agentic commerce solutions." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

# Bring embedded finance to life with stablecoins \[Enable platforms and marketplaces to streamline partner payouts, lower payment costs, and launch more rewarding loyalty programs.]

## The challenge with traditional embedded finance

Embedded finance was meant to help platforms and marketplaces offer smoother, more integrated user experiences. Yet its impact remains constrained by traditional payment rails, whose delays, fees, and operational complexity undermine much of the value embedded finance aims to provide.

For example, gig economy and creator work happens around the clock, while traditional payout rails do not. ACH transfers, while inexpensive, operate only during weekday banking windows and cannot support real-time payouts. Even when platforms offer instant payouts via card networks, these transfers carry higher fees, and the costs are often passed on to partners.

Merchant payouts on marketplaces face similar challenges. Settlement is often delayed by banking windows, regional cutoff times, and inconsistent payment rails across countries. Cross-border merchant payments frequently move through multiple intermediaries, adding cost and introducing unpredictability in when funds will arrive.

## How stablecoins solve this

By embedding blockchain wallets directly into their applications, these platforms can move onto modern, always-on payment rails. Partners, creators, and merchants can receive earnings in stablecoins far faster than through traditional methods, with settlement occurring onchain in seconds. Stablecoins also make these payouts inherently global, removing many of the barriers of regional banking systems.

Once partners, creators and merchants receive their earnings in the embedded wallet, they can manage those funds directly within the same application they use for work. The wallet can hold stablecoin balances, allow payouts to linked bank accounts, or support spending for goods and services through a stablecoin-linked payment card.

Stablecoins and embedded wallets can support far more than payouts. Marketplaces can also use stablecoins to collect consumer payments, deliver instant refunds, and issue loyalty rewards. Stablecoin payments do not have the settlement delays and interchange fees of card networks, making them a faster and cheaper payment option.

## Benefits beyond speed and cost

By significantly reducing the cost of collecting payments from consumers and paying out partners, creators, and merchants, marketplaces can redirect more value toward customer and merchant benefits. Lower payment costs give merchants more flexibility to reward loyal customers with better offers, reimagining their loyalty programs. After all, merchants ultimately fund card rewards through interchange fees.

For platforms, embedded wallets and stablecoin rails replace a patchwork of payment processors, banking partners, and regional settlement rules with a single, consistent infrastructure. Reconciliation relies on unified onchain records rather than scattered bank statements, and operational teams spend far less time managing exceptions or coordinating across time zones.

Faster payouts, lower-cost payment acceptance, and more dynamic loyalty programs are only the beginning of what stablecoins bring to embedded finance. As stablecoins become the foundation for agentic commerce, platforms will gain new opportunities to create value for customers and expand what embedded finance can offer.

## Building with Tempo

By providing a low-cost, high-speed settlement layer, Tempo enables platforms to offer financial products that were previously cost-prohibitive on legacy rails. Whether you are looking to embed wallets for gig workers or streamline complex marketplace settlements, our team can guide you through the wallet integration patterns that best fit your user experience.

We are available to help you evaluate the technical lift and commercial impact of moving your platform's payments onchain.

<Cards>
  <Card description="Want to explore this use case on Tempo? Email us to learn more about building embedded finance solutions." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

# Send global payouts instantly \[Deliver faster, cheaper, and more predictable cross-border payouts to contractors, merchants, and partners around the world with stablecoins.]

## The challenge with global payouts

Managing global payouts is both complex and expensive. Businesses must either rely on slow, expensive, unpredictable cross-border transfers to pay recipients directly, or first move liquidity to local subsidiaries to access domestic payment rails. Each domestic rail, in turn, comes with its own rules, banking holidays, cutoff times, formats, and fees.

This complexity results in a patchwork of manual workflows that is burdensome for finance teams and often frustrating for recipients waiting on delayed transfers. Stablecoins offer a way to simplify this process by reducing cost, improving predictability, and removing much of the operational overhead associated with traditional cross-border payments.

## The real cost of traditional payouts

Consider an example: when you send $1,000 to a contractor in Brazil using traditional rails, the costs add up quickly. Your payment processor may charge a $10–$40 fee per payment, while intermediary banks take anywhere from 0.1% to 4.0% on the FX spread. By the time the payment clears five days later, the recipient has lost $80 to fees. If local currency moved adversely in that window, they would lose again.

## Common pain points this removes

Traditional cross-border payouts fail in predictable ways:

* **High all-in cost:** Fees plus FX spread leakage compounds at scale.
* **Slow settlement:** 3-5 business days plus holidays and cutoffs.
* **Failures and reconciliation overhead:** Incorrect recipient details or intermediary issues create manual rework.
* **Currency volatility exposure:** Recipients can lose value between send and receive.

## How stablecoins solve this

Blockchains are global by design, allowing companies to send stablecoin payouts directly to recipients' wallets anywhere in the world without relying on local banks or intermediaries. These transfers typically cost less than a cent and arrive within seconds, offering far more consistency than traditional international payment rails.

When you send $1,000 to a contractor in Brazil using stablecoin rails, the process is far more straightforward: your stablecoin partner may charge a flat fee of 0.1–0.4% for the onramp and transfer, delivering a **60–80% cost reduction** compared to traditional rails. Recipients receive dollar-denominated stablecoins and can convert to local currency when and how they choose, typically paying a transparent offramp fee in the 0.1–2.0% range.

Cost reduction note: Traditional wire fees on a $1,000 payout typically range $10-$40 (1-4%) excluding FX spreads. Stablecoin onramp fees range from 0.1-0.4%. Comparing 0.4% vs 1.0% yields approximately 60% reduction; higher savings occur vs higher wire fees and FX spreads.

Companies can also choose to distribute funds through their subsidiaries. In this model, a business can convert funds into stablecoins at the headquarters level, such as in the United States, and distribute those funds to subsidiary wallets around the world. Liquidity moves to subsidiaries in seconds rather than days, removing the need to pre-fund subsidiary accounts in advance. Subsidiaries can then handle payouts to local recipients.

## Key benefits

<Cards>
  <Card title="Instant settlement" description="Stablecoins are powered by blockchains that operate 24/7/365, and payouts settle in seconds, not days. Workers and merchants get paid on time, every time." icon="lucide:zap" />

  <Card title="Lower costs" description="By eliminating intermediaries, stablecoins can reduce the cost of a cross-border payment by 60-80%, saving on operational costs or passing savings to users." icon="lucide:piggy-bank" />

  <Card title="Traceability" description="Every stablecoin transaction is recorded on the blockchain, creating an immutable audit trail that reduces disputes and simplifies reconciliation." icon="lucide:search" />
</Cards>

For structured payment references (invoice IDs, customer IDs), see [TIP-20 Tokens](/learn/tempo/native-stablecoins).

<Cards>
  <Card title="Dollar-based stability" description="Payouts in USD stablecoins protect recipients from local currency devaluation. They can convert to local currency on their own terms." icon="lucide:shield" />

  <Card title="Broader access" description="Stablecoins can be sent to any compatible digital wallet, anywhere in the world, opening access for individuals in countries underserved by traditional banking." icon="lucide:globe" />
</Cards>

## Benefits beyond speed and cost

Recipients receiving stablecoins can choose how they want to use their funds. They can hold stablecoins and spend them directly through stablecoin-linked payment cards, or convert them into fiat and withdraw the funds to a local bank account whenever they choose. This gives recipients flexibility and control over how they manage their income.

Stablecoins also reduce foreign exchange complexity. Instead of converting funds into multiple local currencies and dealing with unpredictable spreads and fees, companies can make payouts in a single currency, such as USD stablecoins. Recipients can then convert to their desired currency when it's most convenient for them. This simplifies treasury operations and provides more options for recipients.

Finally, reconciliation becomes significantly simpler. Because stablecoin payouts settle onchain, every transaction has a clear record. Companies no longer need to track separate reporting formats from multiple domestic banks or reconcile transactions that settle at different speeds. Instead, they rely on a single, unified ledger that provides immediate visibility into outgoing payments, balances, and settlement status.

Global payouts with stablecoins already deliver meaningful benefits for both senders and recipients. As familiarity grows and merchant acceptance expands, stablecoins are likely to become a preferred payment method for international disbursements of all kinds. With lower costs, real-time settlement, and programmability, stablecoins bring payout systems closer to the always-on, digital nature of today's global economy.

For native batching and scheduled payout execution, see [Tempo Transactions](/learn/tempo/modern-transactions).

## Evaluating stablecoins for global payouts

Stablecoin adoption starts with a clear business use case. Before evaluating vendors or integration paths, consider this framework:

* **Do you pay people internationally?** If you are paying contractors, merchants, or employees across borders, you are already managing multiple currencies, banks, and regulatory regimes.
* **Do those payments create friction today?** Delays, failed transfers, opaque fees, FX leakage, and reconciliation errors are signals that your current payout rails are not keeping up.
* **Are you forced to pre-fund payouts?** Long settlement times often require holding excess balances across banks and currencies, tying up working capital.
* **Would reducing that friction materially impact your business?** Faster payouts, lower costs, and happier recipients can improve retention, reduce operational overhead, and unlock new geographies.
* **Can instant payouts become a new revenue stream?** Many platforms offer real-time payouts as a premium feature, turning speed and reliability into a paid upgrade rather than a cost center.

If the answer to these questions is yes, you should be evaluating the stablecoin partner ecosystem. The infrastructure is ready, regulation is clearer, and the economics are hard to ignore.

## Getting started

Payouts are one of the cleanest entry points for stablecoins because you can pilot quickly and measure impact.

### Step 1: Clarify the business case

Pick your highest-friction corridor (e.g., U.S. to Brazil, Philippines, or Nigeria). Identify where fees, failed payments, or delays create real pain.

### Step 2: Choose an integration approach

Decide whether to **buy** (provider abstracts custody, liquidity, compliance) or **build** (you assemble wallets, custody, bank rails, and potentially licensing).

### Step 3: Run a pilot

Run stablecoin payouts alongside your existing system for approximately 60 days. Track delivery time, net recipient received, support tickets, and reconciliation effort.

### Step 4: Operationalize

Define SLAs, exception handling, reconciliation processes, and support playbooks, then expand corridors and automate what was manual.

## Building with Tempo

Designed for high-volume, global disbursement, Tempo allows organizations to bypass the fragmentation of local banking rails and reach recipients directly. We work closely with platforms, marketplaces, and payout operators to design stablecoin payout flows that are compliant, efficient, and user-friendly.

If you are interested in seeing how a unified onchain ledger can simplify your global payout operations and remove FX friction, let's discuss the integration requirements and coverage capabilities.

<Cards>
  <Card description="Want to explore this use case on Tempo? Email us to learn more about building global payout solutions." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

## FAQs

### Do I have to hold and manage stablecoins?

No. Many infrastructure providers, such as BVNK, Bridge, and ZeroHash, abstract the complexity of managing stablecoins, wallets, or licensing. You connect to their API to instruct a stablecoin payout, send funds from your bank account in fiat currency, and they handle on- and off-ramp, custody, and liquidity management.

### Will recipients understand stablecoins?

They don't have to. Historically, stablecoin payouts were used primarily by crypto-native developers and contractors. That is changing as new fintech apps hide the complexity. Modern stablecoin infrastructure, like embedded wallets, can be invisible. The recipient gets a notification that payment arrived and sees a balance in US dollars on a mobile app.

### What happens if a recipient wants local currency?

Recipients can convert stablecoins to local currency through supported off-ramps as soon as funds arrive. This is often a one-click experience inside a fintech app or exchange, with transparent fees that are typically far lower than traditional bank FX spreads. Stablecoin orchestration platforms can also automate this process end-to-end.

### Is this only useful for emerging markets?

No. While the benefits are most visible in emerging markets with high fees or volatile currencies, stablecoin payouts are increasingly used in developed markets as well, especially for instant payouts, weekend payments, or premium payout features.

### Is this regulated?

Yes, increasingly so. Since the passage of the GENIUS Act in the United States, the compliance landscape for stablecoins has become clearer. Any money transmitter, financial institution, or nonbank money mover is subject to travel rule requirements. In practice, regulatory requirements like KYC/KYB and screening of senders over $1,000 are lower risk in payout use cases because the payer is the corporation itself.

## Related reading

<Cards>
  <Card title="Stablecoins for Payroll" description="Payroll-specific use cases: account funding, embedded wallets, and revenue model opportunities." to="/learn/use-cases/payroll" icon="lucide:briefcase" />

  <Card title="Deep dive: Stablecoins for Global Payouts" description="Full guide with examples, rollout steps, and FAQs." to="https://tempo.xyz/blog/global-payouts" icon="lucide:book-open" />

  <Card title="Tempo Transactions" description="Native batching, scheduling, and fee sponsorship for payout operators." to="/learn/tempo/modern-transactions" icon="lucide:layers" />

  <Card title="TIP-20 Tokens" description="Reconciliation memos and stable fee mechanics." to="/learn/tempo/native-stablecoins" icon="lucide:tag" />
</Cards>

# Enable true pay-per-use pricing \[Build usage-based billing, pay-per-use APIs, and machine-to-machine services with real-time, sub-cent stablecoin payments.]

## The challenge with traditional payment rails

Digital services are increasingly shifting toward usage-based models, where users pay only for what they consume. This includes everything from API calls and AI inference requests to streaming content, and IoT services. Yet traditional payment rails were never designed for extremely small, frequent payments, making microtransactions impractical or impossible for most businesses today.

Card networks apply fixed fees to every transaction, making any payment under a dollar uneconomical. Even instant rails like FedNow, while cheaper than cards, cannot support usage-based billing where each action costs only a few cents. This forces many digital products into subscriptions or prepaid balances instead of offering the more user-friendly and transparent pay-as-you-go model.

## How stablecoins solve this

Stablecoins change this dynamic by enabling payments that cost a fraction of a cent and settle in seconds, making true microtransactions economically feasible at scale. They achieve this by removing the chain of intermediaries found in traditional payment rails, eliminating the delays, costs, and failure points that make small, frequent payments impractical today.

Programmability further expands what microtransactions can support. Smart contracts can meter usage, enforce payment rules, and top up wallet balances automatically. Developers can charge per API request, per compute cycle, or per any digital action, without building custom billing logic or relying on intermediaries.

Microtransactions also unlock machine-to-machine payments. Autonomous agents, bots, and IoT devices can pay for data, services, or compute in real time without human intervention. A device can pay another device for sensor data; an AI agent can pay for inference or model access; a drone can pay for map segments or airspace permissions.

Stablecoins also enable pay-as-you-go digital commerce for consumers. Instead of monthly subscriptions, consumers can pay per article, per minute of video, per chapter of a book, or per stream of a song. Creators and platforms can monetize content more flexibly, while users pay only for what they actually consume.

## Benefits beyond speed and cost

From a developer's perspective, building microtransaction-powered services is becoming increasingly straightforward. Stablecoins provide a simple, programmable payment primitive. At the same time, new protocols are emerging that standardize usage-based payments, authorization, and settlement, making it even easier to launch pay-per-use applications on top of stablecoin rails.

Finally, onchain microtransactions improve reconciliation. Instead of aggregating thousands of small events into batched invoices that must be reconciled manually, stablecoins provide a unified ledger of each individual payment. This reduces operational overhead and simplifies financial reporting for businesses handling large volumes of small-value transactions.

Ultimately, stablecoin-powered microtransactions are not simply about reducing payment friction. They unlock new business models built around real-time data and usage. By enabling instant, sub-cent payments, stablecoins let companies price, deliver, and monetize digital services in ways that were never feasible before, creating meaningful competitive advantages for those who adopt them early.

## Building with Tempo

True microtransactions require a blockchain that eliminates the economic floor of traditional payment fees. Tempo's architecture is designed to make sub-cent payments viable, unlocking entirely new business models for digital services, APIs, and content platforms. If you are calculating the economics of usage-based billing or machine-to-machine payments, we can help you run the numbers and explore the technical feasibility of building on Tempo.

<Cards>
  <Card description="Want to explore this use case on Tempo? Email us to learn more about building microtransaction solutions." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

# Turn payroll into a platform with stablecoins \[Faster funding, cheaper cross-border payouts, and new revenue streams for payroll providers.]

## The challenge with traditional payroll infrastructure

Payroll providers are starting to take stablecoins seriously. The reasons are familiar to anyone running global payroll: ACH funding takes 2-3 days and carries return risk, cross-border settlement routes through multiple intermediaries that each extract fees, and employees in emerging markets lose money to forced currency conversion.

## How stablecoins solve this

Stablecoins fix all of that, but the opportunity goes well beyond faster and cheaper payments. There are three distinct use cases, and they build on each other: faster payroll account funding, cheaper cross-border payouts to employee wallets, and embedded wallets that turn payroll into a financial services platform. Each stands on its own, and each increases in ambition and payoff.

### 1. Faster payroll account funding

Funding payroll accounts with stablecoins is the lowest-lift opportunity and the one most providers overlook.

Today, employers fund payroll accounts via ACH, which takes 2-3 days to settle and can be returned after employees have already been paid. The provider carries that exposure. Stablecoin funding settles in seconds. Same-day payroll cycles become possible without the provider absorbing settlement risk.

Nothing changes for employees here. They still receive payroll the same way. The improvement is entirely on the funding side: faster cycles, no float risk, simpler cash management. Banking platforms like Ramp, Brex, and Meow are already adding stablecoin support, which makes it increasingly easy for employers to fund payroll accounts in stablecoins.

For providers processing significant volume, eliminating 2-3 days of settlement risk and the operational overhead of managing ACH returns is meaningful on its own.

### 2. Cheaper cross-border payouts

Cross-border payroll routes through payment processors, correspondent banking networks, and local receiving banks. Each intermediary takes a cut and employees absorb FX spreads of 1-4% when their payment is converted to local currency — a cost they can't negotiate and often can't see.

Stablecoins cut through the intermediary chain. Payouts settle in seconds to wallets employees already have, regardless of time zone or bank holiday. Transaction costs drop to cents. The total [cost reduction for cross-border payouts runs 60-80%](/learn/use-cases/global-payouts). Providers don't need to build wallet infrastructure either; employees can bring their own.

For employees, the experience also changes for the better. They receive dollar-denominated stablecoins and choose when (or whether) to convert to local currency. In markets with currency volatility — like Argentina, Nigeria, or Turkey — the ability to hold dollars and convert on their own terms preserves purchasing power. Workers stop losing money to exchange rates set by banks they didn't choose.

This is where payroll providers start to differentiate. If your competitors are still routing through correspondent banking and your clients' contractors are getting paid in seconds at a fraction of the cost, that's a tangible advantage in competitive deals.

For a deeper look at cross-border payout mechanics, cost comparisons, and implementation steps, see [Global Payouts](/learn/use-cases/global-payouts).

### 3. Embedded wallets and financial services

The first two use cases make payroll faster and cheaper. The third one changes the business model.

Today, payroll providers handle the payout. Banks capture everything that happens after: employee deposits get monetized through cards, savings accounts, loans, and investment products. The payroll provider did the work of acquiring and paying the employee, but the bank captures the ongoing financial relationship.

Embedded wallets flip this. When a payroll provider issues a wallet to each employee, the provider controls the user interface and maintains the relationship after funds land. That opens three revenue streams that don't exist in traditional payroll:

* **Branded stablecoins and reserve yield.** Instead of paying employees in USDC, a provider can issue its own stablecoin backed 1:1 by reserves (US Treasuries and deposits). The provider earns the yield on those reserves for as long as employees hold balances. Partners like Bridge handle issuance and compliance.

* **Card interchange.** Stablecoin-backed cards with automatic conversion at point of sale generate 1-2% interchange on spend. For a client with 1,000 employees spending $2,000/month on cards, that's $240K-$480K in annual interchange revenue.

* **Tokenized investment products.** Wallets can offer tokenized money market funds yielding 3-3.5%, or structured credit products at 6-8%. This gives employees access to yields they wouldn't typically get through a traditional payroll deposit, and creates distribution revenue for the provider.

The wallet approach also simplifies global rollout. Non-custodial wallets don't hold customer funds, so they don't require banking or payment institution licenses in every jurisdiction. A provider can launch wallets across dozens of countries with the same infrastructure. That's fundamentally different from custodial financial services, which need per-market licensing.

This is the most ambitious path, and it requires investment in infrastructure, compliance, and product. However, it's also the path that transforms payroll from a low-margin transaction business into a platform with compounding revenue streams. The unit economics shift from "fee per payout" to "lifetime value of a financial relationship."

For more on embedded wallet patterns for platforms, see [Embedded Finance](/learn/use-cases/embedded-finance).

## What to evaluate before building

Not every payroll provider needs to go to level three on day one. The right starting point depends on your client base and where the pain is sharpest.

* **Where are your clients' employees?** If you're primarily in the US or Europe, the pain points are real but less acute. If you serve companies with contractors across Latin America, Africa, or Southeast Asia, the case for stablecoins is immediate and measurable.

* **What corridors are most expensive or unreliable?** Focus stablecoin payouts where correspondent banking is slowest and most expensive. Start there.

* **Do you want to capture value beyond the transaction fee?** If the answer is yes, the wallet path is worth serious evaluation. You can start with payroll account funding and cross-border payouts while building toward wallets.

This is a multi-year build, and partner selection matters more than most providers expect. Choose partners who are thinking long term.

## Other factors to consider

Stablecoins solve real problems, but they create new considerations.

* **Regulation and compliance don't disappear.** Stablecoins change the payment mechanism, not the regulatory framework. Tax withholding, labor law, and reporting requirements still apply in every jurisdiction. Some countries restrict or prohibit stablecoin payments entirely, so you need to verify the landscape in every market where you operate.

* **Not all employees will want stablecoins.** Maintaining parallel payroll rails adds complexity, but forcing adoption creates friction. Offer stablecoins as an option, not a mandate.

* **Employee education takes work.** Workers unfamiliar with digital wallets need clear onboarding. Support teams need training. This is operational investment that's easy to underestimate.

## Building with Tempo

The stablecoin you pay employees with is only as reliable as the infrastructure it runs on. At scale, the differences between chains become operationally significant.

* **Privacy for sensitive payroll data.** Salary information on a public blockchain is a non-starter. Tempo's opt-in privacy solution keeps salary amounts, employee identities, and payment patterns shielded from the public while maintaining full auditability for compliance and internal controls. Employees and employers get privacy by default. Auditors and regulators can access data when required.

* **Predictable delivery during congestion.** Dedicated payment lanes ensure payroll transactions process on schedule even when the network is busy. Missing a payroll cycle because of network congestion is not acceptable.

* **Compliance and reconciliation built into the chain.** Native memo fields attach travel rule identifiers, invoice references, and reconciliation metadata directly to transactions, so payroll records map cleanly to onchain activity. Allow/blocklists for transaction control. These aren't add-ons; they're native to the chain.

* **No account rent.** When you're provisioning wallets for hundreds of thousands of employees, account rent fees on other chains become a real cost line. Tempo doesn't charge account rent.

* **Low, predictable fees paid in stablecoins.** No token management overhead. No gas price volatility. Fees are measured in cents and can be sponsored so employees never see them.

<Cards>
  <Card description="Want to explore stablecoin payroll on Tempo? Email us to discuss your use case." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

## Related reading

<Cards>
  <Card title="Global Payouts" description="Cross-border payout mechanics, cost comparisons, and getting started steps." to="/learn/use-cases/global-payouts" icon="lucide:globe" />

  <Card title="Embedded Finance" description="Embedded wallet patterns for platforms and marketplaces." to="/learn/use-cases/embedded-finance" icon="lucide:wallet" />

  <Card title="Deep dive: Stablecoins for Payroll" description="Full blog post with detailed analysis and use case examples." to="https://tempo.xyz/blog/stablecoins-payroll" icon="lucide:book-open" />

  <Card title="TIP-20 Tokens" description="Reconciliation memos and stable fee mechanics." to="/learn/tempo/native-stablecoins" icon="lucide:tag" />
</Cards>

# Send money home faster and cheaper \[Deliver instant cross-border payments to your customers around the world with stablecoins on Tempo.]

## The challenge with traditional remittances

Cross-border payments are notoriously slow, expensive, and unpredictable. A single transfer often passes through multiple intermediaries, each adding cost, introducing delays, and increasing the risk of errors. Newer "instant" cross-border services improve the user experience, but typically require remittance companies to hold liquidity on both sides of a payment corridor, which increases operational and capital costs.

## How stablecoins make remittances better

Stablecoins can address these challenges by enabling cheap and near-instant cross-border payments. Beyond peer-to-peer transfers, where users send stablecoins directly to each other, three stablecoin-based models are now widely used in the remittance industry:

### Direct transfers

A sender, for example, in the United States, can onramp to stablecoins within the mobile banking app and transfer them directly to a recipient abroad. The recipient can choose to hold the funds in stablecoins, spend them with a stablecoin-linked card, or off-ramp into local currency and deposit into a bank account.

### Orchestrated payments

A sender initiates a cross-border payment from a mobile app, and the recipient receives funds directly into their bank account. Stablecoins are routed through a stablecoin orchestration platform that automatically converts them into local currency, preserving the speed and low cost of stablecoin transfers while delivering a familiar, traditional cross-border payment experience for both sender and recipient.

### Backend settlement

Stablecoins operate entirely behind the scenes. A remittance company uses stablecoins to move liquidity between its own entities across jurisdictions, eliminating the need for correspondent banks and removing the requirement to maintain expensive, pre-funded liquidity on each side of the corridor.

In each case, blockchains and stablecoins help eliminate the patchwork of correspondent banks in between the sender and the recipient, or the need to hold liquidity to emulate "instant" payments. Stablecoin transfers typically cost less than a cent and arrive within seconds, introducing noticeable cost reduction and increasing speed.

## Benefits beyond speed and cost

Beyond the speed and cost improvements, stablecoin-based remittances offer a far smoother user experience for both senders and recipients. With no correspondent banks or intermediate hops, there are fewer points of failure and no unexpected holds, returns, or error paths. Transfers settle onchain in seconds, at any time of day, and the recipient sees the funds immediately.

Further, users around the world increasingly value being able to hold USD-denominated stablecoins. These provide a simple and affordable way to send and receive remittances and pay for global digital services such as LLMs, software subscriptions, and online content platforms.

Onchain settlement also delivers major reconciliation benefits. Each transaction is recorded in real time on a single ledger, giving remittance providers instant visibility into balances and flows. This reduces reliance on delayed bank statements, minimizes reconciliation errors from intermediary hops, and streamlines audit and compliance through a single, authoritative onchain record.

## Building with Tempo

Tempo is purpose-built to handle the volume and cost requirements of modern remittance corridors, enabling providers to move beyond the limitations of correspondent banking. We understand that transitioning to onchain settlement involves navigating complex liquidity and operational questions.

If you are evaluating how to restructure your remittance corridors for higher speed and lower cost, our team can help you map out the architecture for your specific regions. We invite you to explore the technical and operational improvements stablecoins can bring to your flows.

<Cards>
  <Card description="Want to explore this use case with us? Email us to learn more about building remittance solutions on Tempo." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

# Move treasury liquidity instantly across borders \[Enable corporate treasury teams to improve liquidity management across banks, currencies, and regions with tokenized deposits.]

## The challenge with traditional treasury management

Operating across multiple geographies requires companies to maintain relationships with multiple banks, manage balances in several currencies, and navigate an array of local settlement systems, cutoff times, and time zones. For global treasury teams, this results in a fragmented operational landscape with inconsistent processes across regions.

Moving liquidity between a company's own accounts can take days and require subsidiaries to hold excess cash "just in case." Visibility into cash positions is incomplete, workflows vary by region, and reconciling activity across dozens of accounts becomes an ongoing operational burden. The result is inefficient use of capital and a patchwork of manual processes for controls and compliance.

For companies operating across multiple jurisdictions, correspondent banking creates three specific problems:

* **Higher borrowing costs** from trapped cash that cannot be deployed efficiently
* **Suboptimal hedging** based on incomplete or delayed data from disconnected systems
* **Excess bank fees** for accounts holding idle liquidity across regions

## How tokenized deposits and stablecoins solve this

Tokenized deposits and stablecoins offer a path toward simplifying this complexity. Instead of managing dozens of accounts across multiple banks, companies can operate a single wallet per subsidiary. Sitting alongside traditional bank accounts, these digital wallets become a natural extension of corporate treasury operations and provide a more efficient way to manage global liquidity.

Each wallet can hold stablecoins, tokenized deposits, and even tokenized money market funds on the same unified onchain infrastructure. Tokenized deposits and stablecoins introduce a shared set of benefits that transform how corporates store, move, and deploy liquidity:

* **Liquidity can be moved 24/7**, across time zones, and across borders, removing the delays of local settlement systems and cutoff times;
* **Reconciliation becomes simpler** through onchain settlement records instead of disparate bank statements and siloed reporting systems;
* **Idle balances can be deployed more efficiently**, improving working-capital usage and enabling immediate access to interest-bearing tokenized assets;
* **Treasury workflows such as approvals, sweeps, and controls can be automated** with smart contracts, reducing manual processes and operational overhead.

See also: [Global payouts with stablecoins](/learn/use-cases/global-payouts) for the outbound payments use case. For payment references and structured metadata, see [TIP-20 Tokens](/learn/tempo/native-stablecoins). For batching and scheduled treasury movements, see [Tempo Transactions](/learn/tempo/modern-transactions).

## How stablecoins fit into treasury workflows

Stablecoins are most useful when they remove timing and intermediary constraints (cutoff times, weekends, correspondent banks). Common first deployments:

* **Intercompany settlements:** Move USD liquidity between parent and subsidiary entities instantly and settle back to bank accounts on your own schedule.
* **Cash positioning and forecasting:** Use onchain balances as a real-time view of global liquidity rather than end-of-day bank reports.
* **International payouts:** Use stablecoins as the settlement leg for high-volume payouts; recipients can receive stablecoins or be paid in local currency via offramps.

## Current limitations

Stablecoins complement bank accounts rather than replace them. Key constraints to plan for:

* **Limited non-USD liquidity:** Most stablecoin liquidity is USD-denominated; EUR and GBP liquidity is improving but thinner.
* **Off-ramping coverage varies:** Not all markets have reliable bank offramps yet.
* **Custody and controls:** Decide between self-custody vs institutional custody (multi-sig, insurance, governance).
* **Systems integration:** Treasury systems may need adapters for onchain settlement data.
* **Operational risk differs by asset and network:** Prefer regulated, 1:1 reserve-backed assets; evaluate chain uptime and fee variability.

## Reconciliation and operational risk

### Automated GL reconciliation

Fast settlement only matters if transactions reconcile cleanly. Use transfer metadata (e.g., invoice ID, cost center, GL code) so treasury movements can auto-post back into ERP/TMS. Tempo TIP-20 supports native transfer memos designed for reconciliation: see [TIP-20 Tokens](/learn/tempo/native-stablecoins).

### Controls and auditability

24/7 rails require strong approval policy. Enforce role-based permissions and programmable approvals so each movement is attributable and auditable end-to-end.

## Understanding tokenized deposits vs. stablecoins

As digital wallets become integrated into corporate treasury operations, it is important to understand how stablecoins and tokenized deposits differ. They are distinct instruments with different issuers, obligations, and regulatory treatment:

* **Tokenized deposits** are commercial bank deposits issued on a blockchain. They remain a liability of the issuing bank and sit within the existing banking regulatory framework, behaving much like traditional deposits, but with the added benefits of programmability and real-time settlement.
* **Stablecoins**, by contrast, are issued by regulated non-bank stablecoin providers and backed 1:1 with reserves such as cash and short-term government securities. They are designed to maintain a stable value relative to currencies like the U.S. dollar or Euro and can move across blockchains unaffected by cutoff times, banking hours, or regional settlement windows.

## The opportunity for financial institutions

For financial institutions, tokenized deposits represent a major opportunity to strengthen existing corporate relationships and win market share as treasury infrastructure moves onchain. Large enterprises are already adopting stablecoins because they provide the speed, global reach, and programmability that traditional banking infrastructure cannot match.

Tokenized deposits give financial institutions a way to offer many of these same benefits while maintaining the trust and regulatory certainty that corporates rely on. Tokenized deposits are also far more familiar to large corporations: they behave like traditional deposits, remain a liability of the issuing bank, and fit naturally into existing accounting and compliance models.

The main challenge for banks today is interoperability. Most tokenized deposit pilots run inside the closed perimeter of a single institution, limiting their usefulness in multi-bank, multi-region treasury setups. Corporations will only adopt tokenized deposits at scale if they can move funds seamlessly across banks and easily convert between tokenized deposits, stablecoins, and other tokenized assets.

Public blockchains provide this missing bridge. They allow tokenized deposits from different banks to coexist on shared infrastructure, enabling frictionless swaps between tokenized deposits and stablecoins, and supporting cross-bank liquidity movement with the same speed as stablecoin rails. Banks that issue tokenized deposits on public chains gain the interoperability corporates require, while strengthening their role at the center of onchain financial flows.

## Key questions to answer

Before engaging providers, answer these questions:

1. **What problem are you solving?** Identify your highest-value use case: reducing FX costs, accelerating intercompany transfers, or improving cash visibility in specific regions.
2. **Use existing stablecoins or issue your own?** USDC and USDT are liquid and widely accepted for off-ramping. Issuing your own stablecoin allows you to move value between entities while maintaining yield, without converting to money market funds.
3. **Manage internally or via third party?** Wallet setup, custody, and liquidity provider integration can be complex, so many companies outsource to infrastructure providers like Bridge, BVNK, or ZeroHash. Some, like Ant Group, build in-house.

By answering these questions, you'll be ready to define the value more clearly and begin to meet providers.

## Getting started

* **Assess pain points:** Where is cash trapped (weekends, slow corridors, expensive FX)?
* **Build a business case:** Compare current fees, spreads, and delays vs stablecoin rails using your own data.
* **Choose build vs buy:** Many teams start with infrastructure providers that handle custody, on/offramps, and compliance.
* **Pilot a contained flow:** Start with one region or corridor and run in parallel before expanding.

## FAQs

### Do I have to hold and manage stablecoins?

No. You can use stablecoins purely as a settlement rail without holding balances directly. Third parties can manage the stablecoins outside your organization, while your existing bank relationships remain central to day-to-day operations. Over time, you may choose to hold stablecoins directly and expand into other onchain assets such as tokenized treasuries.

### Will my bank support this?

Many banks are actively developing stablecoin and tokenized deposit capabilities, and many more are planning to launch through the coming year. In the meantime, infrastructure providers such as Bridge and BVNK enable seamless movement between traditional bank accounts and stablecoins.

### Who do I need to integrate with?

There are two common approaches. In a buy model, a provider manages licensing, custody, wallets, and blockchain connectivity, so you may never interact with stablecoins directly. In a build model, you integrate directly with custodians, wallet providers, and blockchain networks. The right choice depends on your timeline, internal resources, and how much control you need.

### What about regulatory and audit concerns?

Any treasury implementation must meet regulatory expectations and withstand internal and external audit scrutiny.

* **Regulatory status:** In the US, the GENIUS Act provides a federal framework. The EU's MiCA regulations are in force. The UAE and Singapore have established frameworks, and many jurisdictions expect to publish theirs in the coming year.
* **Audit trail:** Onchain transactions are permanently recorded with timestamps and cryptographic proof.
* **Compliance:** Work with providers offering transaction monitoring, sanctions screening, and AML tools for blockchain.
* **External auditor comfort:** Major issuers like Circle (USDC) and Paxos (USDP) publish monthly attestations. Stablecoin-as-a-service providers like Agora, Bridge, and M0 offer similar capabilities for custom issuance.

### What are the risk considerations?

The primary risks associated with stablecoin-based treasury flows fall into three categories:

* **Counterparty risk:** Stablecoin issuer solvency and infrastructure provider stability. Mitigation: Stablecoins backed 1:1 by HQLA under regulatory frameworks like GENIUS represent lower risk.
* **Operational risk:** Variable fee structures and network performance across blockchains. Mitigation: Select providers offering fee consistency and evaluate reliability alongside speed.
* **Regulatory risk:** Potential restrictions in certain jurisdictions. Mitigation: Start with dollar-based movements between your own entities before expanding to external use cases.

### How does this integrate with our ERP/TMS?

Most TMS platforms (e.g. Kyriba, TreasuryXpress, GTreasury) support native integrations or API connections. A typical flow would look like this:

1. Payment instruction originates in ERP/TMS
2. Instruction routes to a stablecoin infrastructure provider
3. Settlement occurs onchain
4. Confirmation and settlement data flows back to TMS
5. Accounting entries are generated automatically

Tempo offers ISO 20022-compatible messaging, simplifying integration for teams already working with SWIFT MT messages.

## Building with Tempo

Tempo provides the neutral, high-performance infrastructure required for tokenized deposits and stablecoins to operate side-by-side. For treasury teams looking to modernize their liquidity stack, the challenge is often interoperability between these assets and existing banking systems. We collaborate with financial institutions and enterprises to model how these assets can coexist within your current treasury operations. Let's examine how onchain rails can fit into your broader liquidity management strategy.

<Cards>
  <Card description="Want to explore this use case on Tempo? Email us to learn more about building tokenized deposit solutions." to="mailto:partners@tempo.xyz" icon="lucide:mail" title="Get in Touch" />

  <Card description="Start building on Tempo with our guides, SDKs, and documentation." to="/quickstart/integrate-tempo" icon="lucide:rocket" title="Build on Tempo" />
</Cards>

## Related reading

<Cards>
  <Card title="Deep dive: Stablecoins for Corporate Treasury" description="Use cases (intercompany, cash positioning), limitations, and risk considerations." to="https://tempo.xyz/blog/corporate-treasury" icon="lucide:book-open" />

  <Card title="Global payouts" description="How stablecoins simplify outbound payouts and reduce cost 60-80%." to="/learn/use-cases/global-payouts" icon="lucide:send" />

  <Card title="TIP-20 Tokens" description="Transfer memos and compliance features that make reconciliation easier." to="/learn/tempo/native-stablecoins" icon="lucide:tag" />
</Cards>

# Consensus and Finality

Tempo uses Simplex BFT consensus to provide deterministic, sub-second finality. This page describes the consensus mechanism, finality guarantees, and fault tolerance properties.

## Simplex BFT Consensus

Tempo uses Simplex Consensus, implemented by [Commonware](https://www.commonware.xyz/). Simplex is a Byzantine Fault Tolerant consensus protocol optimized for fast finality with graceful degradation under adverse network conditions.

### Block Production

Blocks are produced approximately every 600ms under normal network conditions (500ms builder loop plus network latency and block validation). Proposer selection uses a VRF (Verifiable Random Function) for random leader election, providing DoS protection and MEV resistance. Once a block is finalized, it cannot be reverted.

### Deterministic Finality

Tempo provides deterministic finality rather than probabilistic finality. When a block is marked as finalized, transactions in that block are guaranteed to remain in the canonical chain. There is no reorg risk after finality.

For payment applications, this provides the settlement certainty that operators expect from traditional financial systems.

## Validator Set

### Current Configuration

The testnet operates with 4 validators in a permissioned configuration. Mainnet will launch with institutional validators, also permissioned initially. The roadmap includes a path to permissionless validation.

### Fault Tolerance

Simplex BFT tolerates Byzantine validators up to a threshold:

* The network maintains safety as long as fewer than one-third of validators are Byzantine
* The network maintains liveness as long as at least two-thirds of validators are honest and online

With 4 validators, the network tolerates 1 Byzantine validator. With 10 validators, the network tolerates 3 Byzantine validators.

## Distributed Validation

Tempo uses a distributed validator set rather than a single sequencer. Multiple validators share block production responsibility. Transactions can be included by any proposer, preventing single points of censorship. The network can continue finalizing blocks as long as two-thirds of validators are online and honest.

## Degraded State Behavior

Under adverse conditions, Simplex consensus degrades gracefully:

| Condition | Behavior |
|-----------|----------|
| Network partition | Block times may increase but finality guarantees are preserved |
| Validator offline within threshold | Network continues with remaining validators |
| More than one-third of validators offline | Network halts and resumes when threshold is restored |

The protocol prioritizes safety over liveness. It will halt rather than produce conflicting blocks.

## For Integrators

Treat finalized blocks as irreversible for settlement purposes. No additional confirmations are needed after finality. Query finalized blocks using `eth_getBlockByNumber` with the `finalized` tag.

## Further Reading

* [Commonware Simplex Documentation](https://docs.rs/commonware-consensus/0.0.65/commonware_consensus/simplex/)
* [Simplex with BLS12-381 Threshold Scheme](https://docs.rs/commonware-consensus/0.0.65/commonware_consensus/simplex/index.html#schemebls12381_threshold)

# Blockspace Overview

## Abstract

This specification defines the structure of valid blocks in the Tempo blockchain.

## Motivation

Tempo blocks extend the Ethereum block format in multiple ways: there are new header fields to account for payment lanes and sub-blocks, and system transactions are added to the block body for the fee AMM and other protocol operations. This specification contains all the modifications to the block format.

## Specification

### Header fields

Tempo extends an Ethereum header with three extra scalars.

```rust title="Header struct"
pub struct Header {
    pub general_gas_limit: u64,
    pub shared_gas_limit: u64,
    pub timestamp_millis_part: u64,
    pub inner: Header,
}
```

* `inner` is the canonical Ethereum header (parent\_hash, state\_root, gas\_limit, etc.).
* `general_gas_limit` and `shared_gas_limit` carve up the canonical `gas_limit` for payment and sub-block gas (see [payment lane specification](/protocol/blockspace/payment-lane-specification) and [sub-block specification](/protocol/blockspace/sub-block-specification)).
* `timestamp_millis_part` stores the sub‑second component; the full timestamp is `inner.timestamp * 1000 + timestamp_millis_part` .

### Block body

The block body in Tempo retains the canonical Ethereum block body structure, with the addition of system transactions. Transactions are ordered in the following sections:

1. Start-of-block system transaction(s) (must begin with the rewards registry call).
2. Proposer lane transactions, subject to `general_gas_limit` on non-payment transactions.
3. Sub-block transactions, grouped by proposer and prefixed with the reserved nonce key.
4. Gas incentive transactions that consume leftover shared gas.
5. End-of-block system transactions (see below).

### System transactions

A valid tempo block must contain the following system transactions:

* **Rewards Registry (start-of-block)** — must be the first transaction in the block body; refreshes validator rewards metadata before user transactions begin.  Detailed specification [here](/protocol/tip20-rewards/spec).
* **Subblock Metadata (end-of-block)** — contains metadata about the sub-blocks included in the block. Detailed specification [here](/protocol/blockspace/sub-block-specification).

# Payment Lane Specification

## Abstract

This specification introduces a second consensus gas constraint for **non-payment** transactions. Transactions are classified as either payments or non-payments based solely on their transaction data, without requiring any access to blockchain state. For a block to be valid, total `gas_used` by the block must be less than the `gas_limit`. Non-payment transactions executed in the proposer's lane (i.e. before the gas incentive section) must consume at most `general_gas_limit`, a new field added to the header. Once that budget is exhausted, any additional inclusion must come via the gas incentive lane defined in the [sub-blocks specification](/protocol/blockspace/sub-block-specification).

## Motivation

Tempo ensures that payment transactions always have available blockspace, even during periods of high network congestion from DeFi activity or complex smart contracts. No action is required by the user to take advantage of this feature.

This is achieved through **separate gas limits** for payment and non-payment transactions. When blocks are constructed, validators enforce two separate gas constraints:

1. **`gas_limit`** — The total gas available for all transactions (standard Ethereum behavior)
2. **`general_gas_limit`** — The maximum gas that non-payment transactions can consume

Non-payment transactions in the proposer's lane can only fill up to `general_gas_limit`, payment transactions can still use the remaining capacity up.

## Terminology

* **Payment transaction:** Determined by a function, `is_payment(tx) -> bool`.  This function returns true if the transaction is a payment transaction, false otherwise.
* **Non-payment transaction:** `!is_payment(tx)`.

## Specification

### 1. Transaction classification

A transaction is classified as a **payment transaction** when:

1. the recipient address (`tx.to`) starts with the TIP-20 payment prefix `0x20c0000000000000000000000000`, or,
2. for TempoTransactions, every entry in `tx.calls` targets an address starting with the TIP-20 payment prefix `0x20c0000000000000000000000000`.

This classification is performed entirely on the transaction payload, no account state is consulted.

:::info
Later upgrades may enable other kinds of transactions to be classified as payment transactions as well.
:::

### 2. Ordering of Transactions

The specification does not require any specific ordering of transactions: payment and non-payment transactions can be intermixed.

### 3. Gas accounting & validity (consensus)

Validity of a block requires that,

```
general_gas_limit >= Σ gas_consumed(tx[i])   
for all i such that !is_payment(tx[i]) and tx[i] is in the proposer's lane
```

Where `gas_consumed` includes intrinsic gas and gas burned by reverts, as in the existing protocol.

# Sub-block Specification

## Abstract

This proposal allows non-proposing validators to propose a limited set of transactions in each block through signed **sub-blocks**. Sub-blocks are sent directly to the main proposer and their transactions are included in the block as described below. Consensus does not enforce inclusion. The proposer is incentivized to include sub-blocks by provisioning additional gas upon sub-block inclusion, which permits them to include additional transactions at the bottom of the block as described below.

## Motivation

In traditional blockchains, only the current block proposer can include transactions. This means validators must wait for their scheduled slot to provide fast inclusion for their users. Tempo changes this by letting **all validators** contribute transactions to every block through sub-blocks.

For validators, this is good as they no longer have to wait for their turn as proposer to provide low-latency inclusion for their users. They have guaranteed access to blockspace in every block, allowing them to include transactions whenever needed. Validators can also ensure a specific transaction execution order within their sub-block, giving them controlled ordering of their transactions.

For users, this is good because transactions can be included faster since they can go through any validator, not just the current proposer. Access to blockspace becomes more predictable as it is smoothed across all validators rather than being concentrated with a single proposer. Time-sensitive transactions benefit from lower latency and can be included more quickly.

This proposal smooths access to blockspace across validators. It enables every validator to provide low-latency inclusion for themselves, their users, or their partners, without waiting for their turn as proposer.

## Specification

This specification describes the process in temporal order.

### 0. Definitions

* The gas limit of the whole block is `G`. There are `n` validators: 1 proposer and `n-1` other non-proposers.
* `f` fraction of the gas limit of the  block, `0 < f < 1` is reserved for the main proposer.

### 1. Sub-blocks

* Each validator can construct a sub-block. Sub-blocks follow this structure:

```
sub-block = rlp([version, parent_hash, fee_recipient, [transactions], signature])
```

where:

* `version = 1`,
* `parent_hash` is the parent hash of the previous block.
* `fee_recipient` is the EOA at which this validator wants to receive the fees included in this block.
* `[transactions]` is an ordered list of transactions. Transactions in a sub-block must satisfy additional conditions described below in [Section 1.1](#11-sub-block-transactions). We explicitly allow for this list to be empty: a validator with no transactions to propose may still send a sub-block so that the proposer gets extra gas for the gas incentive region, described below.
* The `signature` field is the validator signing over a hash computed as\
  `keccak256(magic_byte || rlp([version, parent_hash, fee_recipient, [transactions]]))`,
  where `magic_byte = 0x78`,  The signature ensures that this sub-block is valid only for the declared slot, and that the proposer cannot alter the order or set of transactions included in a sub-block.
* The validator sends this sub-block directly to the next proposer.

For each validator `i`, define

`unreservedGas[i] = (1 - f) * G / n - Σ(gasLimit of transactions in sub-block[i])`

#### 1.1 Sub-block Transactions

We use the two-dimensional nonce sequence to simplify transaction validity. In this construction, the nonce\_key is a `u256` value.

Let `validatorPubKey` be the public key of the validator proposing a given sub-block. Let `validatorPubKey120` be the most significant 120 bits of the validator's public key.

We reserve sequence keys to each validator by requiring that the first (most significant) byte of the `sequence key` is the constant byte `0x5b`, and the next 15 bytes (120 bits) encode `validatorPubKey120`.

Formally, we require that:

1. The `sequence key` of any transaction in the sub-block is of the form `(0x5b << 248) + (validatorPubKey120 << 128) + x`, where `x` is a value between `0` and `2**128 - 1`. In other words, the most significant byte of the sequence key is always `0x5b`, the next 15 bytes are the most significant 120 bits of the validator's public key, and the final 32 bytes (128 bits) still allow for 2D-nonces.

2. No two validators share the same `validatorPubKey120`; each validator's reserved space is distinct.

This explicit prefixing with `0x5b` ensures the reserved sequence key space is unambiguous and disjoint across validators. Sub-block proposers control all sequence keys of the form above, and can ensure that nonces are sequential within their space.

:::note\[Reserved Nonce Space]
To prevent transaction conflicts, each validator has a reserved nonce space. Transactions in sub-blocks use special nonce sequence keys that identify which validator proposed them. This ensures that validators can't interfere with each other's transactions.
:::

Further, we require that sub-block transactions are signed solely by the root EOA key of the address sending the transaction.

### 2. Block Construction

The proposer collects sub-blocks from other validators. It now constructs a block with the following contents:

```
transactions = [list of own transactions] | [sub-block transactions] | [gas incentive transactions]
```

* `list of own transactions` are regular transactions from the proposer with `f * G` gas limit.
* `sub-block transactions` are transactions from the included sub-blocks. **This includes a sub-block from the proposer itself if the proposer desires.** Nonce sequence keys with prefix  `0x5b` should only appear in this section.
* `gas incentive transactions` are additional transactions that the proposer can include after the sub-block transactions, with additional gas defined below.

We have the following new **header field**:

```
shared_gas_limit  // The total gas limit allocated for the sub-blocks and gas incentive transactions
```

#### 2.1 System transaction

The block includes a **new system transaction**, whose call data contains, for each included sub-block, the public key of the validator proposing, the `feeRecipient` for that sub-block and the signature of the sub-block. It is a no-op, and is there for execution layer blocks to be self-contained/carry all context.

| Field                                | Value / Requirement                                                                                          | Notes / Validation                                                                                                  |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Type**                              | Legacy transaction                                                                                            |                                                            |
| **Position in Block**                 | **Last transaction**                                                                                          | Block is **invalid** if absent.                                                                          |
| **From (sender)**                     | `0x0000000000000000000000000000000000000000`                                                                  | Zero address                                                                                           |
| **To (recipient)**                    | `0x0000000000000000000000000000000000000000`                                                                                 | No-op                                                                 |
| **Calldata**                          | `rlp([[version, validator_pubkey, fee_recipient, signature], ...])`                                                                |  Sub-block version (currently = 1), each included sub-block's validator public key, fee\_recipient, and signature.                                                                                               |
| **Value**                             | `0`                                                                                                           | No native token transfer.                                                                                             |
| **Nonce**                             | 0                                                                |                                                                             |
| **Gas Limit**                         | 0                                                           | Does **not** contribute to block gas accounting.                                                                      |
| **Gas Price**                         | 0                                                    | Independent of block base fee; does not pay fees.                                                                     |
| **Signature**                         | `r = 0`, `s = 0`, `yParity = false`                                                                           | Empty signature designates system transaction.                                                                        |

### 3. Proposer Behavior

* Construct Main Block in the usual way.
* Collect sub-blocks from validators, including from self. Verify signatures and gas bounds of sub-blocks. Skip (i.e., do not include) invalid or missing sub-blocks; include valid ones. Transactions from a sub-block must be contiguous in the block, but sub-blocks can be included in any order.
* Compute proposer Gas Incentive section limit:

  ```
  gasIncentiveLimit =  Σ(unreservedGas[i]) for all included sub-blocks [i]
  ```

* Append transactions at the bottom up to this gas limit.
* Construct and include the [system transaction](#21-system-transaction) at the bottom of the block.

#### 3.1 Proposer Incentives

* We do not enforce censorship-resistance for the transactions at consensus layer.
* Proposer is incentivized by additional gas from sub-blocks included and reciprocity.
* Additional gas is unrestricted so it could include backruns etc from sub-block transactions.

### 4. Block Validity Rules

We can now define what a valid block is:

1. Gas Limits:
   * `[list of own transactions]` uses gas at most `f * G`.
   * `[sub-block transactions]`: the sum of `gas_limits` of all transactions in each sub-block is lower than the per-sub block gas limit: `Σ(gasLimit of transactions in sub-block[i]) <= (1-f) * G / n`.
   * `[gas incentive transactions]` use total gas `<= gasIncentiveLimit`.
   * General transactions gas limit from payments lane spec applies to `[list of own transactions]`.
2. Transactions with nonce sequence key prefix `0x5b` appear only in the `[sub-block transactions]`. Transactions are contiguous by validator.
   The `[list of own transactions]` and `[gas incentive transactions]` can use any un-reserved `sequence key`.
3. [System transaction](#21-system-transaction) is present, in the correct position, and valid (matches contents of the block).
4. Transactions in the main proposers's section and the gas incentive section are valid in the standard way (signature, nonce, can pay fees).

#### 4.1  Failures for Sub-block Transactions

Even if a transaction can pay its fees when the sub-block is created (i.e., when the sub-block is sent to the proposer), it may not be able to pay its fees when the sub-block is included and the  block is processed. Here is a list of possible scenarios:

* **Fee Failure Scenarios**:

* The Fee AMM liquidity for the user's `fee_token` is insufficient (e.g., it was used up by previous transactions in the block).
* The user's balance of the `fee_token` is insufficient (e.g., the user spent that balance in previous transactions in the block).
* The user or validator changed their `fee_token` preference in the block and the transaction cannot pay its fees because of the new preference.

In all these scenarios, transaction is considered valid, increments the nonce, skips fee payment and execution, and results in an exceptional halt.

### 5. Transaction Fee Accounting

The fee manager is updated to handle fee accounting across sub-blocks:

* For the main proposer transactions, fees are paid to the main proposer's `fee_recipient` as usual.
* For the sub-block transactions, fees are paid to the `fee_recipient` of the sub-block (available from the system transaction).
* For the gas incentive transactions, fees are paid to the proposer's `fee_recipient`.

In all cases, the fee is paid in the preferred `fee_token` of the `fee_recipient`, using liquidity from the fee AMM as necessary (i.e., `validatorTokens[fee_recipient]` from the FeeManager contract). If the `fee_recipient`  has not set a preferred `fee_token`, then we use pathUSD as a fallback.

# DEX Balance

The Stablecoin DEX allows you to hold token balances directly using the DEX contract. This eliminates the need for token transfers on every trade, significantly reducing gas costs for active traders and liquidity providers.

## Why DEX Balances?

When you trade or provide liquidity on the DEX, constantly transferring tokens between your wallet and the DEX contract wastes gas. By maintaining a balance via the DEX contract, you can:

* **Save on gas costs** - Avoid ERC-20 transfer costs for each trade
* **Trade more efficiently** - Execute multiple swaps without transfers between each trade
* **Receive maker proceeds automatically** - When your limit orders are filled, proceeds are credited to your DEX balance instead of requiring a transfer for each fill

## Checking Your Balance

Use the DEX contract to view your balance of any token held on the DEX:

```solidity
function balanceOf(
    address user,
    address token
) external view returns (uint128)
```

**Example:**

```solidity
uint128 balance = exchange.balanceOf(msg.sender, USDC_ADDRESS);
```

## Using Your DEX Balance

Each transaction that you authorize will use your DEX balance before using funds you approve from your wallet. When you execute a swap or place an order, the DEX contract automatically:

1. Checks if you have sufficient balance in the DEX
2. If insufficient, transfers the needed amount from your wallet to your DEX balance
3. Uses your DEX balance for the operation

## Withdrawing from the DEX

Transfer tokens from your DEX balance back to your wallet:

```solidity
function withdraw(
    address token,
    uint128 amount
) external
```

**Parameters:**

* `token` - The token address to withdraw
* `amount` - The amount to withdraw

**Example:**

```solidity
// Withdraw 1000 USDC from exchange to your wallet
exchange.withdraw(USDC_ADDRESS, 1000e6);
```

:::warning
The withdraw function will revert if you attempt to withdraw more than your available balance on the exchange.
:::

## How Balances Work

### When Swapping

* **Before swap**: Exchange checks your balance, transfers from wallet if needed
* **After swap**: Output tokens are transferred directly to your wallet (not kept on exchange)

### When Placing Orders

* **On placement**: Required tokens are debited from your exchange balance (or transferred from wallet if insufficient)
* **When filled**: Proceeds are credited to your exchange balance
* **On cancellation**: Unfilled portion is refunded to your exchange balance

# Executing Swaps

## Swap Functions

The exchange provides two primary swap functions:

### Swap Exact Amount In

Specify the exact amount of tokens you want to sell, and receive at least a minimum amount:

```solidity
function swapExactAmountIn(
    address tokenIn,
    address tokenOut,
    uint128 amountIn,
    uint128 minAmountOut
) external returns (uint128 amountOut)
```

**Parameters:**

* `tokenIn` - The token address you're selling
* `tokenOut` - The token address you're buying
* `amountIn` - The exact amount of `tokenIn` to sell
* `minAmountOut` - Minimum amount of `tokenOut` you'll accept (slippage protection)

**Returns:**

* `amountOut` - The actual amount of `tokenOut` received

**Example:** Swap exactly 1000 USDC for at least 998 USDT:

```solidity
uint128 amountOut = exchange.swapExactAmountIn(
    USDC_ADDRESS,
    USDT_ADDRESS,
    1000e6,      // Sell exactly 1000 USDC
    998e6        // Receive at least 998 USDT
);
```

### Swap Exact Amount Out

Specify the exact amount of tokens you want to receive, and pay at most a maximum amount:

```solidity
function swapExactAmountOut(
    address tokenIn,
    address tokenOut,
    uint128 amountOut,
    uint128 maxAmountIn
) external returns (uint128 amountIn)
```

**Parameters:**

* `tokenIn` - The token address you're selling
* `tokenOut` - The token address you're buying
* `amountOut` - The exact amount of `tokenOut` to receive
* `maxAmountIn` - Maximum amount of `tokenIn` you'll pay (slippage protection)

**Returns:**

* `amountIn` - The actual amount of `tokenIn` spent

**Example:** Receive exactly 1000 USDT by spending at most 1002 USDC:

```solidity
uint128 amountIn = exchange.swapExactAmountOut(
    USDC_ADDRESS,
    USDT_ADDRESS,
    1000e6,      // Receive exactly 1000 USDT
    1002e6       // Pay at most 1002 USDC
);
```

## Quoting Prices

Before executing a swap, you can query the expected price using view functions that simulate the swap without executing it:

### Quote Exact Amount In

```solidity
function quoteSwapExactAmountIn(
    address tokenIn,
    address tokenOut,
    uint128 amountIn
) external view returns (uint128 amountOut)
```

Returns how much `tokenOut` you would receive for a given `amountIn`.

### Quote Exact Amount Out

```solidity
function quoteSwapExactAmountOut(
    address tokenIn,
    address tokenOut,
    uint128 amountOut
) external view returns (uint128 amountIn)
```

Returns how much `tokenIn` you would need to spend to receive a given `amountOut`.

**Example: Getting a price quote**

```solidity
// Check how much USDT you'd get for 1000 USDC
uint128 expectedOut = exchange.quoteSwapExactAmountIn(
    USDC_ADDRESS,
    USDT_ADDRESS,
    1000e6
);

// Only execute if the price is acceptable
if (expectedOut >= 998e6) {
    exchange.swapExactAmountIn(USDC_ADDRESS, USDT_ADDRESS, 1000e6, 998e6);
}
```

## How Swaps Execute

When you call a swap function:

1. **Balance Check**: The contract first checks your balance on the DEX
2. **Transfer if Needed**: If your DEX balance is insufficient, tokens are transferred from your wallet
3. **Order Matching**: The DEX walks through orders at each price tick, from best to worst:
   * Orders are consumed in price-time priority order
   * Each filled order credits the maker's balance on the DEX
   * Continues until your swap is complete or limit price is reached
4. **Slippage Check**: Reverts if `minAmountOut` (or `maxAmountIn`) constraints aren't met
5. **Settlement**: Your output tokens are transferred to your wallet

:::warning
Swaps will revert with an `InsufficientLiquidity` error if there isn't enough liquidity in the orderbook to satisfy your slippage constraints.
:::

## Gas Costs

Swap gas costs scale with the number of orders and ticks your trade crosses:

* Base swap cost (transfers and setup)
* Per-order cost (for each order filled)
* Per-tick cost (for each price level crossed)
* Per-flip cost (if any flip orders are triggered)

Larger swaps that cross more orders will cost more gas, but the cost per unit of volume decreases.

## Token Balances on the DEX

The DEX allows you to track token balances directly within the DEX contract, which saves gas by avoiding ERC-20 transfers on every trade. When you execute a swap, the contract first checks your DEX balance and only transfers from your wallet if needed.

For complete details on checking balances, depositing, withdrawing, and managing your DEX balance, see the [DEX Balance](/protocol/exchange/exchange-balance) page.

# Providing Liquidity

Provide liquidity to the DEX by placing limit orders or flip orders in the onchain orderbook.

When your orders are filled, you earn the spread between bid and ask prices while helping facilitate trades for other users.

You can only place orders on pairs between a token and its designated quote token. All TIP-20 tokens specify a quote token for trading pairs. [pathUSD](/protocol/exchange/quote-tokens#pathusd) can be used as a simple choice for a quote token.

## Overview

The DEX uses an onchain orderbook where you can place orders at specific price ticks. Orders are matched using price-time priority, meaning better-priced orders fill first, and within the same price, earlier orders fill first.

Unlike traditional AMMs, you specify exact prices where you want to buy or sell, giving you more precise control over your liquidity provision strategy.

## Order Types

### Limit Orders

Standard orders that remain in the book at a specific price until filled or cancelled.

```solidity
function place(
    address token,
    uint128 amount,
    bool isBid,
    int16 tick
) external returns (uint128 orderId)
```

**Parameters:**

* `token` - The token address you're trading (must trade against its quote token)
* `amount` - The amount of the token denominated in `token`
* `isBid` - `true` for a buy order, `false` for a sell order
* `tick` - The price tick: `(price - 1) * 100_000` where price is in quote token per token

**Returns:**

* `orderId` - Unique identifier for this order

**Example: Place a bid to buy 1000 USDC at $0.9990**

```solidity
// tick = (0.9990 - 1) * 100_000 = -10
uint128 orderId = exchange.place(
    USDC_ADDRESS,
    1000e6,      // Amount: 1000 USDC
    true,        // isBid: buying USDC
    -10          // tick: price = $0.9990
);
```

**Example: Place an ask to sell 1000 USDC at $1.0010**

```solidity
// tick = (1.0010 - 1) * 100_000 = 10
uint128 orderId = exchange.place(
    USDC_ADDRESS,
    1000e6,      // Amount: 1000 USDC
    false,       // isBid: selling USDC
    10           // tick: price = $1.0010
);
```

### Flip Orders

Special orders that automatically reverse to the opposite side when completely filled, creating perpetual liquidity similar to an automated market maker pool.

```solidity
function placeFlip(
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    int16 flipTick
) external returns (uint128 orderId)
```

**Parameters:**

* All parameters from `place()`, plus:
* `flipTick` - The price where the order will flip to when filled
  * Must be greater than `tick` if `isBid` is true
  * Must be less than `tick` if `isBid` is false

**Returns:**

* `orderId` - Unique identifier for this flip order

**Example: Place a flip order providing liquidity on both sides**

```solidity
// Place a bid at $0.9990 that flips to an ask at $1.0010
uint128 orderId = exchange.placeFlip(
    USDC_ADDRESS,
    1000e6,      // Amount: 1000 USDC
    true,        // isBid: start as a buy order
    -10,         // tick: buy at $0.9990
    10           // flipTick: sell at $1.0010 after filled
);
```

When this order is completely filled:

1. You buy 1000 USDC at $0.9990
2. A new order automatically sells 1000 USDC at $1.0010
3. When that fills, it flips back to a bid at $0.9990
4. This continues indefinitely, earning the spread each time

:::info
Flip orders act like a liquidity pool position, automatically providing liquidity on both sides of the market as they're filled back and forth.
:::

## Understanding Ticks

Prices are specified using ticks with 0.1 basis point (0.001%) precision:

**Tick Formula:** `tick = (price - 1) × 100_000`

**Price Formula:** `price = 1 + (tick / 100_000)`

Where `price` is the token price in quote token units.

### Example Tick Calculations

| Price | Tick | Calculation |
|-------|------|-------------|
| $0.9990 | -100 | (0.9990 - 1) × 100\_000 = -100 |
| $0.9998 | -20 | (0.9998 - 1) × 100\_000 = -20 |
| $1.0000 | 0 | (1.0000 - 1) × 100\_000 = 0 |
| $1.0002 | 20 | (1.0002 - 1) × 100\_000 = 20 |
| $1.0010 | 100 | (1.0010 - 1) × 100\_000 = 100 |

:::warning
Price ticks are limited to ±2% from peg (±2000 ticks). Orders outside this range will be rejected.
:::

## Bid vs Ask

* **Bid (isBid = true)**: An order to *buy* the token using its quote token
* **Ask (isBid = false)**: An order to *sell* the token for its quote token

For a USDC/USD pair where USD is the quote:

* A bid buys USDC with USD at your specified price
* An ask sells USDC for USD at your specified price

## Order Execution Timeline

Orders follow a specific lifecycle:

1. **Placement**: When you call `place()` or `placeFlip()`:
   * Tokens are debited from your DEX balance (or transferred if insufficient)
   * Order is immediately added to the active book and visible to other contracts
   * Returns an order ID immediately

2. **Filling**: As market orders execute against your order:
   * Your order fills partially or completely
   * Proceeds are credited to your DEX balance
   * If a flip order fills completely, a new order is immediately created on the opposite side

## Cancelling Orders

Remove an order from the book before it's filled:

```solidity
function cancel(
    uint128 orderId
) external
```

**Example:**

```solidity
// Cancel order #12345
exchange.cancel(12345);
```

Cancellations execute immediately, and any unfilled portion of your order is refunded to your [DEX balance](/protocol/exchange/exchange-balance).

:::warning
You can only cancel your own orders. Attempting to cancel another user's order will revert.
:::

# Quote Tokens

Each USD TIP-20 on Tempo can choose any other USD TIP-20 as its quote token—the token it is paired against on the native decentralized exchange. This guarantees that there is one path between any two tokens, which reduces fragmentation of liquidity and simplifies routing.

## pathUSD

pathUSD is a USD-denominated stablecoin that can be used as a quote token on Tempo's decentralized exchange. It is the first stablecoin deployed to the chain, and is used as a fallback gas token when the user or validator does not specify a gas token. Use of pathUSD is optional.

### Motivation

While on other chains, most liquidity accrues to a few stablecoins, or even one, Tempo allows you to choose which stablecoin to use as your quote token. As one option, you can select pathUSD, a USD-denominated stablecoin. PathUSD is not meant to compete as a consumer-facing stablecoin. Use of pathUSD is optional, and tokens are able to list any other token as their quote token if they choose.

pathUSD can also be accepted as a fee token by validators.

### Contract

pathUSD is a predeployed [TIP-20](/protocol/tip20/spec) at genesis. Since it is the first TIP-20 deployed, its quote token is the zero address.

| Property       | Value                                        |
| -------------- | -------------------------------------------- |
| address        | `0x20c0000000000000000000000000000000000000` |
| `name()`       | `"pathUSD"`                                  |
| `symbol()`     | `"pathUSD"`                                  |
| `currency()`   | `"USD"`                                      |
| `decimals()`   | `6`                                          |
| `quoteToken()` | `address(0)`                                 |

### Usage

When creating a USD stablecoin on Tempo, you can set pathUSD as its quote token:

```solidity
TIP20 token = factory.createToken(
  "My Company USD",
  "MCUSD",
  "USD",
  TIP20(0x20c0000000000000000000000000000000000000), // pathUSD
  msg.sender,
  bytes32("my-unique-salt") // salt for deterministic address
);
```

This means:

* Your token trades against pathUSD on the exchange.
* Users can swap between your token and other USD stablecoins that also use pathUSD, or ones connected by a multi-hop path.

### Tree Structure

Quote token relationships form a tree structure where all USD stablecoins are connected via multi-hop paths:

```
               USDX
                |
             pathUSD -- USDY -- USDZ
                |
               USDA
```

The tree structure guarantees a single path between any two USD stablecoins. This ensures simple routing, concentrated liquidity, and efficient pricing even for thinly-traded pairs.

### Example: Cross-Stablecoin Payment

1. Market makers provide liquidity for USDX/pathUSD and USDY/pathUSD pairs.
2. A user wants to send USDX to a merchant who prefers USDY.
3. The exchange atomically routes the payment: USDX to pathUSD to USDY.
4. This happens in a single transaction with no manual swaps required.

The user and merchant never hold pathUSD directly. It exists only as routing infrastructure.

# Stablecoin DEX

## Abstract

This specification defines an enshrined decentralized exchange for trading between TIP-20 stablecoins. The exchange currently only supports trading between TIP-20 stablecoins with USD as their currency. By only allowing each stablecoin to be paired against its designated "quote token" the exchange enforces that there is only one route for trading between any two tokens.

The exchange maintains price‑time priority at each discrete price tick, executes swaps immediately against the active book, and supports auto‑replenishing “flip orders” that recreate themselves on the opposite side after being fully filled.

Users maintain internal balances per token on the exchange. Order placement escrows funds from these balances (or transfers from the user if necessary), fills credit makers internally, and withdrawals transfer tokens out.

## Motivation

Tempo aims to provide high‑quality execution for cross‑stablecoin payments while avoiding unnecessary chain load and minimizing mid‑block MEV surfaces.

A simple, on‑chain, price‑time‑priority orderbook tailored to stable pairs encourages passive liquidity to rest on chain and allows takers to execute deterministically at the best available ticks.

Another design goal is to avoid fragmentation of liquidity across many different pairs. By enforcing that each stablecoin only trades against a single quote token, the system guarantees that there is only one path between any two tokens.

## Specification

### Contract and scope

The exchange is a singleton contract deployed at `0xdec0000000000000000000000000000000000000`. It exposes functions to create trading pairs, place and cancel orders (including flip orders), execute swaps, produce quotes, and manage internal balances.

### Key concepts

#### Internal balances

The contract maintains per‑user, per‑token internal balances. Order placement escrows funds from these balances (or transfers any shortfall from the user). When an order fills, the maker is credited internally with the counter‑asset at the order’s tick price. Users can withdraw available balances at any time.

#### Flip orders

A flip order behaves like a normal resting order until it is fully filled. When filled, the exchange places a new order for the same maker on the opposite side at a configured `flipTick` (which must be greater than `tick` for bids and less for asks). This enables passive liquidity with flexible strategies.

When a flip order flips, it draws escrow exclusively from the maker's internal exchange balance. Unlike initial order placement, the exchange does not fall back to `transferFrom` if the internal balance is insufficient—the flip simply does not occur. This ensures that flip execution is self-contained and does not require additional token approvals or external balance checks at fill time.

#### Pairs, ticks, and prices

Pairs are identified deterministically from the two token addresses (the base token is any TIP‑20, and its `quoteToken()` function points to the quote token). Prices are discretized into integer ticks with a tick size of 0.1 bps: with `PRICE_SCALE = 100_000`, `price = PRICE_SCALE + tick`. Orders may only be placed at ticks divisible by `TICK_SPACING = 10` (effectively setting a 1 bp tick size). The orderbook tracks best bid (highest active bid tick) and best ask (lowest active ask tick), and uses bitmaps over tick words for efficient discovery of the next initialized tick.

#### Quote tokens

Each TIP‑20 token specifies a single quote token in its metadata via `quoteToken()`. A trading pair on the Stablecoin DEX exists only between a base token and its designated quote token, and prices for the pair are denominated in units of the quote token.

This design reduces liquidity fragmentation by giving every token exactly one paired asset.

It also simplifies routing. We require that:

1. each token picks a single other stablecoin as its quote token, and,
2. quote token relationships cannot have circular dependencies.

This forces liquidity into a tree structure, which in turn implies that there is only one path between any two stablecoins

USD tokens can only choose USD tokens as their quote token. Non-USD TIP-20 tokens can pick any token as their quote token, but currently there is no support for cross-currency trading, or same-currency trading of non-USD tokens, on the DEX.

The platform offers a neutral USD stablecoin, [`pathUSD`](/protocol/exchange/quote-tokens#pathusd), as an option for quote token. PathUSD is the first stablecoin deployed on the chain, which means it has no quote token. Use of pathUSD is optional.

#### Swaps

Swaps execute immediately against the active book. Selling base for quote starts at the current best bid and walks downward as ticks are exhausted; selling quote for base starts at the best ask and walks upward. Within a tick, fills are FIFO and decrement the tick’s total liquidity. When a tick empties, it is de‑initialized.

Callers can swap between any two USD TIP-20 tokens. If `tokenIn` and `tokenOut` are not directly paired, the implementation finds the unique path between them through quote‑token relationships, and performs a multi‑hop swap/quote.

#### Crossed books

Crossed books are permitted; the implementation does not enforce that best bid ≤ best ask. This primarily supports flip‑order scenarios.

#### Constraints

* Only USD‑denominated tokens are supported, and their quotes must also be USD
* Orders must specify ticks within the configured bounds (±2000)
* Tick spacing is 10: `tick % 10 == 0` for orders and flip orders
* Withdrawals require sufficient internal balance

### Interface

Below is the complete on‑chain interface, organized by function. Behavior notes and constraints are included with each function where relevant.

#### Constants and pricing

```solidity
function PRICE_SCALE() external view returns (uint32);
```

Scaling factor for tick‑based prices. One tick equals 1/PRICE\_SCALE above or below the peg. Current value: `100_000` (0.001% per tick).

```solidity
function TICK_SPACING() external view returns (int16);
```

Orders must be placed on ticks divisible by `TICK_SPACING`. Current value: `10` (i.e., 1 bp grid).

```solidity
function MIN_TICK() external view returns (int16);
function MAX_TICK() external view returns (int16);
```

Inclusive tick bounds for order placement. Current range: ±2000 ticks (±2%).

```solidity
function MIN_PRICE() external view returns (uint32);
function MAX_PRICE() external view returns (uint32);
```

Price bounds implied by tick bounds and `PRICE_SCALE`.

```solidity
function tickToPrice(int16 tick) external pure returns (uint32 price);
function priceToTick(uint32 price) external pure returns (int16 tick);
```

Convert between discrete ticks and scaled prices. `priceToTick` reverts if `price` is out of bounds.

#### Pairing and orderbook

```solidity
function pairKey(address tokenA, address tokenB) external pure returns (bytes32 key);
```

Deterministic key for a pair derived from the two token addresses (order‑independent).

```solidity
function createPair(address base) external returns (bytes32 key);
```

Creates the pair between `base` and its `quoteToken()` (from TIP‑20). Both must be USD‑denominated. Reverts if the pair already exists or tokens are not USD.

```solidity
function books(bytes32 pairKey) external view returns (address base, address quote, int16 bestBidTick, int16 bestAskTick);
```

Returns pair metadata and current best‑of‑side ticks. Best ticks may be sentinel values when no liquidity exists.

```solidity
function getTickLevel(address base, int16 tick, bool isBid) external view returns (uint128 head, uint128 tail, uint128 totalLiquidity);
```

Returns FIFO head/tail order IDs and aggregate liquidity for a tick on a side, allowing indexers to reconstruct the active book.

#### Internal balances

```solidity
function balanceOf(address user, address token) external view returns (uint128);
```

Returns a user’s internal balance for `token` held on the exchange.

```solidity
function withdraw(address token, uint128 amount) external;
```

Transfers `amount` of `token` from the caller’s internal balance to the caller. Reverts if insufficient internal balance.

#### Order placement and lifecycle

```solidity
function place(address token, uint128 amount, bool isBid, int16 tick) external returns (uint128 orderId);
```

Places a limit order against the pair of `token` and its quote, immediately adding it to the active book. Escrows funds: bids escrow quote at tick price; asks escrow base.

Notes:

* `tick` must be within `[MIN_TICK, MAX_TICK]` and divisible by `TICK_SPACING` (10).
* The maker must be authorized by the TIP-403 transfer policies of both the base and quote tokens. This ensures makers cannot place orders to buy or sell tokens they are not permitted to transfer.
* Additionally, the DEX contract itself must be authorized by the TIP-20 transfer policies of both the base and quote tokens. This allows token issuers to prevent their tokens from being traded on the DEX.

```solidity
function placeFlip(address token, uint128 amount, bool isBid, int16 tick, int16 flipTick) external returns (uint128 orderId);
```

Like `place`, but marks the order as a flip order. When fully filled, a new order for the same maker is scheduled on the opposite side at `flipTick` (which must be greater than `tick` for bids and less for asks).

Notes:

* Both `tick` and `flipTick` must be within `[MIN_TICK, MAX_TICK]` and divisible by `TICK_SPACING` (10).
* When the order flips, escrow is drawn exclusively from the maker's internal exchange balance. If the internal balance is insufficient, the flip silently fails—no `transferFrom` is attempted, even if the maker has sufficient external balance and approval.
* The maker must be authorized by the TIP-403 transfer policies of both the base and quote tokens, both at initial placement and when the order flips. If the maker becomes unauthorized before a flip, the flip silently fails and no new order is created (although the existing order is executed).

```solidity
function cancel(uint128 orderId) external;
```

Cancels an order owned by the caller. When canceled, the order is removed from the tick queue, liquidity is decremented, and remaining escrow is refunded to the order owner's exchange balance which can then be withdrawn.

```solidity
function cancelStaleOrder(uint128 orderId) external;
```

Cancels an order where the maker is forbidden by the escrowed token's [TIP-403 transfer policy](/protocol/tip403/overview). Unlike `cancel`, this function can be called by anyone—not just the order maker—but only succeeds if the maker is no longer authorized to transfer the escrowed token (e.g., the maker has been blacklisted). This allows third parties to clean up stale orders from the book.

When canceled, the order is removed from the tick queue, liquidity is decremented, and remaining escrow is refunded to the order maker's exchange balance. Reverts with `OrderNotStale` if the maker is still authorized.

```solidity
function nextOrderId() external view returns (uint128);
```

Monotonic counter for next orderId.

#### Swaps and quoting

```solidity
function quoteSwapExactAmountIn(address tokenIn, address tokenOut, uint128 amountIn) external view returns (uint128 amountOut);
```

Simulates an exact‑in swap walking initialized ticks and returns the expected output. Reverts if the pair path lacks sufficient liquidity.

```solidity
function quoteSwapExactAmountOut(address tokenIn, address tokenOut, uint128 amountOut) external view returns (uint128 amountIn);
```

Simulates an exact‑out swap and returns the required input. Reverts if insufficient liquidity.

```solidity
function swapExactAmountIn(address tokenIn, address tokenOut, uint128 amountIn, uint128 minAmountOut) external returns (uint128 amountOut);
```

Executes an exact‑in swap against the active book. Deducts `amountIn` from caller’s internal balance (transferring any shortfall) and transfers output to the caller. Reverts if resulting `amountOut` is below `minAmountOut` or liquidity is insufficient.

```solidity
function swapExactAmountOut(address tokenIn, address tokenOut, uint128 amountOut, uint128 maxAmountIn) external returns (uint128 amountIn);
```

Executes an exact‑out swap. Deducts the actual input from the caller’s internal balance (transferring any shortfall from the user) and transfers `amountOut` to the caller. Reverts if required input exceeds `maxAmountIn` or liquidity is insufficient.

#### Events

```solidity
event PairCreated(bytes32 indexed key, address indexed base, address indexed quote);
event OrderPlaced(uint128 indexed orderId, address indexed maker, address indexed token, uint128 amount, bool isBid, int16 tick, bool isFlipOrder, int16 flipTick);
event OrderCancelled(uint128 indexed orderId);
event OrderFilled(uint128 indexed orderId, address indexed maker, address indexed taker, uint128 amountFilled, bool partialFill);
```

#### Errors

```solidity
error Unauthorized();
```

* Pair creation or usage: `PAIR_EXISTS`, `PAIR_NOT_EXISTS`, `ONLY_USD_PAIRS`
* Bounds: `TICK_OUT_OF_BOUNDS`, `FLIP_TICK_OUT_OF_BOUNDS`, `FLIP_TICK_MUST_BE_GREATER_FOR_BID`, `FLIP_TICK_MUST_BE_LESS_FOR_ASK`, "Price out of bounds"
* Tick spacing: `TICK_NOT_MULTIPLE_OF_SPACING`, `FLIP_TICK_NOT_MULTIPLE_OF_SPACING`
* Liquidity and limits: `INSUFFICIENT_LIQUIDITY`, `MAX_IN_EXCEEDED`, `INSUFFICIENT_OUTPUT`
* Authorization: `UNAUTHORIZED` (cancel not by maker)
* Stale orders: `ORDER_NOT_STALE` (cancelStaleOrder when maker is still authorized)
* Balance: `INSUFFICIENT_BALANCE` (withdraw)

# Fee AMM Overview

The Fee AMM (Automated Market Maker) is a dedicated system for converting transaction fees between different stablecoins. It enables users to pay fees in any supported stablecoin while allowing validators to receive fees in their preferred token.

## How It Works

When a user pays fees in a stablecoin that differs from the validator's preference, the Fee AMM automatically converts the payment:

* **User pays**: 1.0 of their chosen stablecoin
* **Validator receives**: 0.9970 of their preferred stablecoin
* **Liquidity providers earn**: 0.003 (0.3%) as fees

This conversion happens automatically at the end of each block through batched swaps, preventing MEV attacks like sandwiching.

## Learn More

<Cards>
  <Card description="Enable users to pay fees using your stablecoin" to="/guide/issuance/use-for-fees" icon="lucide:circle-dollar-sign" title="Use Your Stablecoin for Fees" />

  <Card description="Complete Fee AMM protocol specification" to="/protocol/fees/spec-fee-amm" icon="lucide:file-text" title="Fee AMM Specification" />

  <Card description="Provide liquidity to enable fee token conversions" to="/guide/stablecoin-dex/managing-fee-liquidity" icon="lucide:droplet" title="Managing Fee Liquidity" />
</Cards>

# Fees

## Abstract

This spec lays out how fees work on Tempo, including how fees are calculated, who pays them, and how the default fee token for a transaction is determined.

## Motivation

Tempo has no native token. Transaction fees are paid directly in USD-denominated stablecoins. This design removes the need for users or applications to hold volatile assets for gas, keeping the entire payment experience USD-native.

Users can pay gas fees in any [TIP-20](/protocol/tip20/spec) token whose currency is USD, as long as that stablecoin has sufficient liquidity on the enshrined [fee AMM](/protocol/fees/spec-fee-amm.mdx) against the token that the current validator wants to receive.

In determining *which* token a user pays fees in, we want to maximize customizability (so that wallets or users can implement more sophisticated UX than is possible at the protocol layer), minimize surprise (particularly surprises in which a user pays fees in a stablecoin they did not expect to), and have sane default behavior so that users can begin using basic functions like payments even using wallets that are not customized for Tempo support.

## Fee units

Fees in the `max_base_fee_per_gas` and `max_fee_per_gas` fields of transactions, as well as in the block's `base_fee_per_gas` field, are specified in **attodollars** (10^-18 USD) per gas. Since TIP-20 tokens have 6 decimal places — where 1 token unit = 1 **microdollar** (10^-6 USD) — the fee for a transaction can be calculated as `ceil(base_fee * gas_used / 10^12)`.

Attodollars provide sufficient precision for low-fee transactions. Since TIP-20 tokens have only 6 decimal places (microdollars), expressing fees directly in token units per gas would not provide enough precision for transactions with very low gas costs. By using attodollars (10^-18 USD) and dividing by 10^12 to convert to microdollars, the protocol ensures that even small fee amounts can be accurately represented and calculated.

### Base Fee Model

Tempo uses a fixed base fee rather than the dynamic base fee mechanism specified in EIP-1559. The base fee is set such that a TIP-20 transfer costs less than $0.001.

The fixed base fee combined with USD-denominated payment provides predictable unit economics. Applications can budget for transaction costs without exposure to fee volatility or native token price fluctuations.

Congestion is managed through:

* **Payment lanes**: Reserved blockspace for TIP-20 transfers as specified in the [Payment Lane Specification](/protocol/blockspace/payment-lane-specification). Approximately 94% of blockspace is reserved for payment transactions, with the remaining 6% available for general computation. This allocation is conservative and the blockspace available for general computation may increase over time as total throughput scales.
* **Priority fees**: The `max_priority_fee_per_gas` field allows transactions to bid for faster inclusion during periods of high demand.
* **Block gas limits**: Standard per-block gas limits constrain total computation per block.

The payment lane mechanism ensures that payment transactions are not crowded out by other network activity. General network congestion from non-payment use cases cannot affect payment throughput or fees, providing the consistency that payment applications require.

## Fee payment

Before the execution of each transaction, the protocol takes the following steps:

* Determine the [`fee_payer`](#fee-payer) of the transaction.
* Determine the `fee_token` of the transaction, according to the [rules for fee token preferences](#fee-token-preferences). If the fee token cannot be determined, the transaction is invalid.
* Compute the `max_fee` of the transaction as `gas_limit * gas_price`.
* Deduct `max_fee` from the `fee_payer`'s balance of `fee_token`. If `fee_payer` does not have sufficient balance in `fee_token`, the transaction is invalid.
* Reserve `max_fee` of liquidity on the [fee AMM](/protocol/fees/spec-fee-amm) between the `fee_token` and the validator's preferred fee token. If there is insufficient liquidity, the transaction is invalid.

After the execution of each transaction:

* Compute the `refund_amount` as `(gas_limit - gas_used) * gas_price`.
* Credit the `fee_payer`'s address with `refund_amount` of `fee_token`.
* Log a `Transfer` event from the user to the [fee manager contract](/protocol/fees/spec-fee-amm) for the net amount of the fee payment.

:::info\[Atomic fee handling]
The protocol executes the max fee deduction and refund atomically. If insufficient liquidity is encountered at any point during fee calculation (for example, if a previous transaction by the same sender in the same block exhausted the fee token reserves), the entire transaction reverts.
:::

## Fee payer

Tempo supports *sponsored transactions* in which the `fee_payer` is a different address from the `tx.origin` of the transaction. This is supported by Tempo's [new transaction type](/protocol/transactions/spec-tempo-transaction.mdx), which has a `fee_payer_signature` field.

If no `fee_payer_signature` is provided, then the `fee_payer` of the transaction is its sender (`tx.origin`).

If the `fee_payer_signature` field is set, then it is used to derive the `fee_payer` for the transaction, as described in the [transaction spec](/protocol/transactions/spec-tempo-transaction.mdx).

For purposes of [fee token preferences](#fee-token-preferences), the `fee_payer` is the account that chooses the fee token.

### Fee sponsorship flow

Presence of the `fee_payer_signature` field authorizes a third party to pay the transaction's gas costs while the original sender executes the transaction logic.

:::steps

#### Sender signs the transaction

The sender signs the transaction with their private key, signing over a blank fee token field. This means the sender delegates the choice of which fee token to use to the fee payer.

#### Fee payer selects and signs

The fee payer selects which fee token to use, then signs over the transaction.

#### Transaction submission

The fee token and fee payer signature is added to the transaction using the `fee_payer_signature` field and is then submitted.

#### Network validation

The network validates both signatures and executes the transaction.
:::

#### Validation

When `feePayerSignature` is present:

* Both sender and fee payer signatures must be valid
* Fee payer must have sufficient balance in the fee token
* Transaction is rejected if either signature fails or fee payer's balance is insufficient

## Fee token preferences

The protocol checks for token preferences in five ways, with this order of precedence:

1. Transaction (set by the `fee_token` field of the transaction)
2. Account (set on the FeeManager contract by the `fee_payer` of the transaction)
3. TIP-20 contract (if the transaction is calling `transfer`, `transferWithMemo`, or `startReward` on a TIP-20 token contract, the transaction uses that token as its fee token)
4. Stablecoin DEX (for certain swap calls, the transaction uses the `tokenIn` argument as its fee token)
5. PathUSD (as a fallback)

The protocol checks preferences at each of these levels, stopping at the first one at which a preference is specified. At that level, the protocol performs the following checks. If any of the checks fail, the transaction is invalid (without looking at any further levels):

* The token must be a TIP-20 token whose currency is USD.
* The user must have sufficient balance in that token to pay the `gasLimit` on the transaction at the transaction's `gasPrice`.
* There must be sufficient liquidity on the [fee AMM](/protocol/fees/spec-fee-amm.mdx), as discussed in that specification.

If no preference is specified at the transaction, account, or contract level, the protocol falls back to [pathUSD](#pathusd).

### Transaction level

Tempo's [new transaction type](/protocol/transactions/spec-tempo-transaction.mdx), allows transactions to specify a `fee_token` on the transaction. This overrides any preferences set at the account, contract, or validator level.

For [sponsored transactions](#fee-payer), the `tx.origin` address does not sign over the `fee_token` field (allowing the `fee_payer` to choose the fee token).

### Account level

An account can specify a fee token preference for all transactions for which it is the `fee_payer` (including both transactions it sponsors as well as non-sponsored transactions for which it is the `tx.origin`). This overrides any preference set at the contract or validator level.

To set its preference, the account can call the `setUserToken` function on the FeeManager precompile.

At this step, the protocol does one more check:

* If the transaction is not a [Tempo transaction](/protocol/transactions/spec-tempo-transaction.mdx) *and* the transaction is a top-level call to the `setUserToken` function on the FeeManager, then the protocol checks the `token` argument to the function:
  * If that token is a TIP-20 whose currency is USD, that token is used as the fee token (unless the transaction specifies a `fee_token` at the [transaction level](#transaction-level)).
  * If that token is not a TIP-20 or its currency is not USD, the transaction is invalid.

### TIP-20 contracts

If the top-level call of a transaction is to one of the following functions on a TIP-20 token whose currency is USD:

* `transfer(address to, uint256 amount)`
* `transferWithMemo(address to, uint256 amount, bytes32 memo)`
* `startReward(uint256 amount, uint32 seconds_)`

then that TIP-20 token is used as the user's fee token for that transaction (unless there is a preference specified at the [transaction](#transaction-level) or [account](#account-level) level).

For [Tempo transactions](/protocol/transactions/spec-tempo-transaction.mdx), this rule applies only if *all* top-level calls are to the same TIP-20 contract, and each such call is to one of the functions listed above, with `fee_payer == tx.origin`.

### Stablecoin DEX contract

If the top-level call of a transaction is to the [Stablecoin DEX](/protocol/exchange/spec.mdx) contract, the function being called is either `swapExactAmountIn` or `swapExactAmountOut`, and the `tokenIn` argument to that function is the address of a TIP-20 token for which the currency is USD, then the `tokenIn` argument is used as the user's fee token for the transaction (unless there is a preference specified at the [transaction](#transaction-level) or [account](#account-level) level).

For [Tempo transactions](/protocol/transactions/spec-tempo-transaction.mdx), this rule applies only if there is only one top-level call in the transaction.

### pathUSD

If no fee preference is set at the transaction, account, or contract level, the protocol falls back to [pathUSD](/protocol/exchange/quote-tokens#pathusd) as the user's fee token preference.

## Validator preferences

Validators can set a default fee token preference that determines which stablecoin they receive for transaction fees. When users pay in different tokens, the Fee AMM automatically converts to the validator's preferred token.

### Setting validator preference

To set their preference, validators call the `setValidatorToken` function on the FeeManager precompile:

```solidity
// Set your preferred fee token
feeManager.setValidatorToken(preferredTokenAddress);
```

After setting a validator token preference, all fees collected in blocks the validator proposes will be automatically converted to the chosen token (if needed) and transferred to the validator's account.

On the Moderato testnet, validators currently expect alphaUSD (one of the tokens distributed by the faucet) as their fee token.

If validators have not specified a fee token preference, the protocol falls back to expecting pathUSD as their fee token.

## Gas Parameters

As of [TIP-1010](/protocol/tips/tip-1010), Tempo uses the following mainnet gas parameters:

| Parameter | Value |
|-----------|-------|
| Base fee | 20 billion attodollars per gas (`2 × 10^10`) |
| Total block gas limit | 500M gas |
| General gas limit | 30M gas/block |

A standard TIP-20 transfer (~50,000 gas) costs approximately 1,000 microdollars (0.1 cent / $0.001) at the base fee.

### Removing validator preference

To remove a validator token preference, set it to the zero address:

```solidity
// Remove validator token preference
feeManager.setValidatorToken(address(0));
```

## Fee lifecycle

This section describes the complete flow of how fees are collected, converted, and distributed from user to validator.

### Fee flow steps

When a user submits a transaction on Tempo, fees are paid in their chosen stablecoin (determined by the [fee token preferences](#fee-token-preferences) hierarchy). If the validator prefers a different stablecoin, the Fee AMM automatically converts the user's payment to the validator's preferred token.

#### 1. User submits transaction

The transaction is submitted with the fee token determined by the preference hierarchy.

#### 2. Pre-transaction collection

Before the transaction executes, the `FeeManager` contract collects the maximum possible fee amount from the user:

* Verifies the user has sufficient balance in their chosen fee token
* Checks if the Fee AMM has enough liquidity (if conversion is needed)
* Collects the maximum fee amount based on the transaction's gas limit

If either check fails, the transaction is rejected before execution.

#### 3. Transaction execution

The transaction executes normally. The actual gas consumed may be less than the maximum that was collected.

#### 4. Post-transaction refund

After execution, the `FeeManager`:

* Calculates the actual fee owed based on gas used
* Refunds any unused tokens to the user
* Queues the actual fee amount for conversion (if needed)

#### 5. Fee swap execution

If the user's fee token differs from the validator's preferred token, the fee swap executes immediately during the post-transaction step at a fixed rate of **0.9970** (validator receives 0.9970 of their token per 1.0 user token paid).

If the user's fee token matches the validator's preference, no conversion is needed.

Fees accumulate in the FeeManager contract. Validators can claim their accumulated fees at any time by calling `distributeFees()`.

### Fee swap mechanics

Fee swaps always execute at a fixed rate of **0.9970**:

```
validatorTokenOut = userTokenIn × 0.9970
```

This means:

* User pays 1.0 USDC for fees
* Validator receives 0.9970 USDT (if that's their preferred token)
* The 0.003 (0.3%) difference goes to liquidity providers as a fee

### Example flow

Here's a complete example of the fee lifecycle:

1. **Alice** wants to send a transaction and pays fees in **USDC** (her preferred token)
2. **Validator** prefers to receive fees in **USDT**
3. Alice's transaction has a max fee of 1.0 USDC
4. The FeeManager collects 1.0 USDC from Alice before execution
5. Transaction executes and uses 0.8 USDC worth of gas
6. The FeeManager refunds 0.2 USDC to Alice
7. The Fee AMM immediately swaps 0.8 USDC → 0.7976 USDT (0.8 × 0.9970)
8. The 0.7976 USDT is added to the validator's accumulated fees
9. Validator calls `distributeFees()` to claim their accumulated fees
10. Liquidity providers earn 0.0024 USDT from the 0.3% fee

### Gas costs

The fee conversion process adds minimal overhead to transactions:

* **Pre-transaction**: ~5,000 gas for balance and liquidity checks
* **Post-transaction**: ~3,000 gas for refund and queue operations
* **Block settlement**: Amortized across all transactions in the block

For complete technical specifications on the Fee AMM mechanism, see the [Fee AMM Protocol Specification](/protocol/fees/spec-fee-amm).

# Fee AMM Specification

## Abstract

This specification defines a system of one-way Automated Market Makers (AMMs) designed to facilitate gas fee payments from a user using one stablecoin (the `userToken`) to a validator who prefers a different stablecoin (the `validatorToken`). Each AMM handles fee swaps from a `userToken` to a `validatorToken` at one price (0.9970 `validatorToken` per `userToken`), and allows rebalancing in the other direction at another fixed price (1.0015 `userToken` per `validatorToken`).

## Motivation

Current blockchain fee systems typically require users to hold native tokens for gas payments. This creates friction for users who prefer to transact in stablecoins.

The Fee AMM is a dedicated AMM for trading between stablecoins, which can only be used by the protocol (and by arbitrageurs rebalancing it to keep it balanced). The protocol automatically collects fees in many different coins and immediately swaps them (paying a constant price) into the token preferred by the validator. Fees accumulate in the FeeManager, and validators can claim them on-demand.

The system is designed to minimize several forms of MEV:

* **No Probabilistic MEV**: The fixed fee swap rate prevents profitable backrunning of fee swaps. There is no way to profitably spam the chain with transactions hoping an opportunity might arise.
* **No Sandwich Attacks**: Fee swaps execute at a fixed rate, eliminating sandwich attack vectors.
* **Top-of-Block Auction**: The main MEV in the AMM (from rebalancing) occurs as a single race at the top of the next block rather than creating probabilistic spam throughout.

## Specification

### Overview

The Fee AMM implements two distinct swap mechanisms:

1. **Fee Swaps**: Fixed-rate swaps at a price of `0.9970` (validator token per user token) from `userToken` to `validatorToken`
2. **Rebalancing Swaps**: Fixed-rate swaps at a price of `1.0015` (user token per validator token) from `validatorToken` to `userToken`

### Core Components

#### 1. FeeAMM Contract

The primary AMM contract managing liquidity pools and swap operations.

##### Pool Structure

```solidity
struct Pool {
    uint128 reserveUserToken;           // Reserve of userToken
    uint128 reserveValidatorToken;      // Reserve of validatorToken
}
```

Each pool is directional: `userToken` → `validatorToken`. For a pair of tokens A and B, there are two separate pools:

* Pool(A, B): for swapping A to B at fixed rate of 0.997 (fee swaps) and B to A at fixed rate of 0.9985 (rebalancing)
* Pool(B, A): for swapping B to A at fixed rate of 0.997 (fee swaps) and A to B at fixed rate of 0.9985 (rebalancing)

##### Constants

* `M = 9970` (scaled by 10000, representing 0.9970)
* `N = 9985` (scaled by 10000, representing 0.9985)
* `SCALE = 10000`
* `MIN_LIQUIDITY = 1000`

##### Key Functions

```solidity
function getPool(
    address userToken,
    address validatorToken
) external view returns (Pool memory)
```

Returns the pool structure for a given token pair.

```solidity
function getPoolId(
    address userToken,
    address validatorToken
) external pure returns (bytes32)
```

Returns the pool ID for a given token pair (used internally for pool lookup).

```solidity
function rebalanceSwap(
    address userToken,
    address validatorToken,
    uint256 amountOut,
    address to
) external returns (uint256 amountIn)
```

Executes rebalancing swaps from `validatorToken` to `userToken` at fixed rate of 1.0015 (user token per validator token). Can be executed by anyone. Calculates `amountIn = (amountOut * N) / SCALE + 1` (rounds up). Updates reserves immediately. Emits `RebalanceSwap` event.

```solidity
function mint(
    address userToken,
    address validatorToken,
    uint256 amountUserToken,
    uint256 amountValidatorToken,
    address to
) external returns (uint256 liquidity)
```

Adds liquidity to a pool with both tokens. First provider sets initial reserves and must burn `MIN_LIQUIDITY` tokens. Subsequent providers must provide proportional amounts. Receives fungible LP tokens representing pro-rata share of pool reserves.

```solidity
function mint(
    address userToken,
    address validatorToken,
    uint256 amountValidatorToken,
    address to
) external returns (uint256 liquidity)
```

Single-sided liquidity provision with validator token only. Treats the deposit as equivalent to performing a hypothetical `rebalanceSwap` first at rate `n = 0.9985` until the ratio of reserves match, then minting liquidity by depositing both. Formula: `liquidity = amountValidatorToken * _totalSupply / (V + n * U)`, where `n = N / SCALE`. Rounds down to avoid over-issuing LP tokens. Updates reserves by increasing only `validatorToken` by `amountValidatorToken`. Emits `Mint` event with `amountUserToken = 0`.

```solidity
function burn(
    address userToken,
    address validatorToken,
    uint256 liquidity,
    address to
) external returns (uint256 amountUserToken, uint256 amountValidatorToken)
```

Burns LP tokens and receives pro-rata share of reserves. Emits `Burn` event.

```solidity
function executeFeeSwap(
    address userToken,
    address validatorToken,
    uint256 amountIn
) internal returns (uint256 amountOut)
```

Executes a fee swap immediately. Calculates `amountOut = (amountIn * M) / SCALE`. Only executed by the protocol during transaction execution. Emits `FeeSwap` event. Note: `FeeSwap` events are not emitted for immediate swaps.

```solidity
function checkSufficientLiquidity(
    address userToken,
    address validatorToken,
    uint256 maxAmount
) internal view
```

Verifies sufficient validator token reserves for the fee swap. Calculates `maxAmountOut = (maxAmount * M) / SCALE`. Reverts if insufficient liquidity.

#### 2. FeeManager Contract

Tempo introduces a precompiled contract, the `FeeManager`, at the address `0xfeec000000000000000000000000000000000000`.

The `FeeManager` is a singleton contract that implements all the functions of the Fee AMM for every pool. It handles the collection and refunding of fees during each transaction, executes fee swaps immediately, stores fee token preferences for users and validators, and accumulates fees for validators to claim via `distributeFees()`.

##### Key Functions

```solidity
function setUserToken(address token) external
```

Sets the default fee token preference for the caller (user). Requires token to be a USD TIP-20 token. Emits `UserTokenSet` event. Access: Direct calls only (not via delegatecall).

```solidity
function setValidatorToken(address token) external
```

Sets the fee token preference for the caller (validator). Requires token to be a USD TIP-20 token. Cannot be called during a block built by that validator. Emits `ValidatorTokenSet` event. Access: Direct calls only (not via delegatecall).

```solidity
function collectFeePreTx(
    address user,
    address userToken,
    uint256 maxAmount
) external
```

Called by the protocol before transaction execution. The fee token (`userToken`) is determined by the protocol before calling using logic that considers: explicit tx fee token, setUserToken calls, stored user preference, tx.to if TIP-20. Reserves AMM liquidity if user token differs from validator token. Collects maximum possible fee from user. Access: Protocol only (`msg.sender == address(0)`).

```solidity
function collectFeePostTx(
    address user,
    uint256 maxAmount,
    uint256 actualUsed,
    address userToken
) external
```

Called by the protocol after transaction execution. The validator token and fee recipient are inferred from `block.coinbase`. Calculates refund amount: `refundAmount = maxAmount - actualUsed`. Refunds unused tokens to user. If user token differs from validator token, executes the fee swap immediately and accumulates the output for the validator. Access: Protocol only (`msg.sender == address(0)`).

```solidity
function distributeFees(address validator, address token) external
```

Allows anyone to trigger distribution of accumulated fees for a specific token to a validator. Transfers all accumulated fees in the specified token to the validator address. If no fees have accumulated for that token, this is a no-op.

```solidity
function collectedFees(address validator, address token) external view returns (uint256)
```

Returns the amount of accumulated fees for a validator and specific token that can be claimed via `distributeFees()`.

### Swap Mechanisms

#### Fee Swaps

* **Rate**: Fixed at m=0.9970 (validator receives 0.9970 of their preferred token per 1 user token that user pays)
* **Direction**: User token to validator token
* **Purpose**: Convert tokens paid by users as fees to tokens preferred by validators
* **Settlement**: Immediate during transaction execution
* **Access**: Protocol only

#### Rebalancing Swaps

* **Rate**: Fixed at n=0.9985 (swapper receives 1 of the user token for every 0.9985 that they put in of the validator's preferred token)
* **Direction**: Validator token to user token
* **Purpose**: Refill reserves of validator token in the pool
* **Settlement**: Immediate
* **Access**: Anyone

### Fee Collection Flow

1. **Pre-Transaction**:
   * Protocol determines user's fee token using logic that considers: explicit tx fee token, setUserToken calls, stored user preference, tx.to if TIP-20
   * Protocol calculates maximum gas needed (`maxAmount = gasLimit * maxFeePerGas`)
   * `FeeManager.collectFeePreTx(user, userToken, maxAmount)` is called:
     * If user token differs from validator token, checks AMM has sufficient liquidity via `checkSufficientLiquidity()`
     * Collects maximum fee from user using `transferFeePreTx()`
   * If any check fails (insufficient balance, insufficient liquidity), transaction is invalid

2. **Post-Transaction**:
   * Calculate actual gas used (`actualUsed = gasUsed * gasPrice`)
   * `FeeManager.collectFeePostTx(user, maxAmount, actualUsed, userToken)` is called:
     * Validator token and fee recipient are inferred from `block.coinbase`
     * Calculates refund: `refundAmount = maxAmount - actualUsed`
     * Refunds unused tokens to user via `transferFeePostTx()`
     * If user token differs from validator token and `actualUsed > 0`, executes fee swap immediately via `executeFeeSwap()`
     * Accumulates swapped fees for the validator

3. **Fee Distribution**:
   * Validators (or anyone) can call `distributeFees(validator)` at any time to transfer accumulated fees to the validator

### Events

```solidity
event RebalanceSwap(
    address indexed userToken,
    address indexed validatorToken,
    address indexed swapper,
    uint256 amountIn,
    uint256 amountOut
)
event FeeSwap(
    address indexed userToken,
    address indexed validatorToken,
    uint256 amountIn,
    uint256 amountOut
)
event Mint(
    address indexed sender,
    address indexed userToken,
    address indexed validatorToken,
    uint256 amountUserToken,
    uint256 amountValidatorToken,
    uint256 liquidity
)
event Burn(
    address indexed sender,
    address indexed userToken,
    address indexed validatorToken,
    uint256 amountUserToken,
    uint256 amountValidatorToken,
    uint256 liquidity,
    address to
)
event UserTokenSet(address indexed user, address indexed token)
event ValidatorTokenSet(address indexed validator, address indexed token)
```

`Transfer` events are emitted as usual for transactions, with the exception of paying gas fees via TIP20 tokens. For fee payments, a single `Transfer` event is emitted post execution to represent the actual fee amount consumed (i.e. `gasUsed * gasPrice`).

### Gas

Fee swaps are designed to be gas-free from the user perspective. The pre-tx and post-tx steps in each transaction do not cost any gas.

# TIP-20 Rewards

TIP-20 Rewards is a built-in mechanism that allows for efficient distribution of rewards to opted-in token holders proportional to their holdings, while maintaining low gas costs at scale and complying with [TIP-403 transfer policies](/protocol/tip403/spec).

Traditional reward mechanisms require tokens to be staked in separate contracts, which fragments user holdings and adds complexity to wallet implementations. TIP-20 Rewards solves this by:

* **Built-in Distribution**: Rewards are integrated directly into the token contract, no separate staking required
* **Opt-in Participation**: Users choose whether to participate by setting a reward recipient
* **Proportional Distribution**: Rewards accrue based on token holdings automatically
* **Instant Rewards**: Distribute rewards immediately to opted-in holders
* **Efficient at Scale**: Constant-time updates regardless of the number of token holders
* **Policy Compliant**: All reward transfers respect TIP-403 transfer policies

## Links

<Cards>
  <Card description="Complete technical specification for rewards distribution" to="/protocol/tip20-rewards/spec" icon="lucide:file-text" title="Rewards Specification" />

  <Card description="Distribute rewards to token holders" to="/guide/issuance/distribute-rewards" icon="lucide:trending-up" title="Guide: Distribute Rewards" />
</Cards>

# TIP-20 Rewards Distribution

## Abstract

An opt-in, scalable, pro-rata reward distribution mechanism built into TIP-20 tokens. The system uses a "reward-per-token" accumulator pattern to distribute rewards proportionally to opted-in holders without requiring staking or per-holder iteration. Rewards are distributed instantly; time-based streaming distributions are planned for a future upgrade.

## Motivation

Many applications require pro-rata distribution of tokens to existing holders (incentive programs, deterministic inflation, staking rewards). Building this into TIP-20 allows efficient distribution without forcing users to stake tokens elsewhere or requiring distributors to loop over all holders.

## Specification

The rewards mechanism allows anyone to distribute token rewards to opted-in holders proportionally based on holdings. Users must opt in to receiving rewards and may delegate rewards to a recipient address.

## TIP-20 Rewards Functions

These functions are part of the [ITIP20](/protocol/tip20/spec) interface:

```solidity
/// @notice Distribute rewards to opted-in token holders
/// @param amount Amount of tokens to distribute
function distributeReward(uint256 amount) external;

/// @notice Set the reward recipient for the caller (opt in/out of rewards)
/// @param newRewardRecipient Recipient address (address(0) to opt out)
function setRewardRecipient(address newRewardRecipient) external;

/// @notice Claim all pending rewards for the caller
/// @return maxAmount Amount claimed
function claimRewards() external returns (uint256 maxAmount);

/// @notice Get user reward info
function userRewardInfo(address user) external view returns (
    address rewardRecipient,
    uint256 rewardPerToken,
    uint256 rewardBalance
);

// State variables
function globalRewardPerToken() external view returns (uint256);
function optedInSupply() external view returns (uint128);
```

## Accrual Mechanism

The system uses an accumulator pattern:

* `globalRewardPerToken`: Cumulative rewards per token (scaled by 1e18)
* Each user stores a `rewardPerToken` snapshot; pending rewards = `(globalRewardPerToken - snapshot) * balance`

Instant distributions (`seconds_ == 0`) add directly to `globalRewardPerToken` as:
`deltaRPT = amount * 1e18 / optedInSupply`.

## Opt-In Model

Users must call `setRewardRecipient(recipient)` to opt in. When opted in:

* User's balance contributes to `optedInSupply`
* Rewards accrue to `rewardBalance` on balance-changing operations
* Users can delegate rewards to another address

Setting recipient to `address(0)` opts out.

## TIP-403 Integration

All token movements must pass TIP-403 policy checks:

* `distributeReward`: Validates funder authorization
* `setRewardRecipient`: Validates holder and recipient
* `claimRewards`: Validates msg.sender

## Invariants

* `globalRewardPerToken` must monotonically increase
* `optedInSupply` must equal the sum of balances for all opted-in users
* All token movements must comply with TIP-403 policies

# TIP-20 Token Standard

TIP-20 is Tempo's native token standard for stablecoins and payment tokens. TIP-20 is designed for stablecoin payments, and is the foundation for many token-related functions on Tempo including transaction fees, payment lanes, DEX quote tokens, and optimized routing for DEX liquidity on Tempo.

All TIP-20 tokens are created by interacting with the [TIP-20 Factory contract](/protocol/tip20/spec#tip20factory), calling the `createToken` function. If you're issuing a stablecoin on Tempo, we **strongly recommend** using the TIP-20 standard. Learn more about the benefits, or follow the guide on issuance [here](/guide/issuance).

## Benefits & Features of TIP-20 Tokens

Below are some of the key benefits and features of TIP-20 tokens:

### Payments

<Cards>
  <Card description="Only TIP-20 tokens can be used to pay for transaction fees on Tempo." to="#pay-fees-in-any-stablecoin" icon="lucide:wallet" title="Pay for Blockchain Transaction Fees" />

  <Card description="TIP-20 tokens have dedicated blockspace from all other transactions, ensuring predictable payment fees." to="#get-predictable-payment-fees" icon="lucide:route" title="Get Predictable Payment Fees" />

  <Card description="Attach 32-byte memos to transfers for payment references, invoice IDs, or transaction notes." to="#transfer-memos" icon="lucide:message-square" title="Transfer Memos" />

  <Card description="Opt-in reward distribution system for issuing rewards to token holders." to="#reward-distribution" icon="lucide:gift" title="Reward Distribution" />
</Cards>

### Exchange

<Cards>
  <Card description="Declare currency identifiers (e.g., USD, EUR) for proper routing and pricing in the Stablecoin DEX." to="#currency-declaration" icon="lucide:banknote" title="Currency Declaration" />

  <Card description="TIP-20 tokens can serve as quote tokens in Tempo's DEX for trading pairs and liquidity pools." to="#dex-quote-tokens" icon="lucide:arrow-left-right" title="DEX Quote Tokens" />
</Cards>

### Compliance & Controls

<Cards>
  <Card description="Set access control roles for minting, burning, pausing, and administrative operations." to="#role-based-access-control-rbac" icon="lucide:shield" title="Built-in Role-Based Access Control" />

  <Card description="Enforce compliance with whitelist and blacklist policies via the TIP-403 Policy Registry." to="#tip-403-transfer-policies" icon="lucide:file-check" title="Enforce Transfer Policies" />

  <Card description="Supply caps, pause/unpause controls, and 32-byte transfer memos for payment references." to="#operational-controls" icon="lucide:settings" title="Operational Controls" />
</Cards>

### Pay Fees in Any Stablecoin

Any USD-denominated TIP-20 token can be used to pay transaction fees on Tempo.

The [Fee AMM](/protocol/fees/spec-fee-amm) automatically converts your token to the validator's preferred fee token, eliminating the need for users to hold a separate gas token. This feature works natively: no additional infrastructure or integration required.

Full specification of this feature can be found in the [Payment Lanes Specification](/protocol/blockspace/payment-lane-specification).

### Get Predictable Payment Fees

Tempo has dedicated payment lanes: reserved blockspace for payment TIP-20 transactions that other applications cannot consume. Even if there are extremely popular applications on the chain competing for blockspace, payroll runs or customer disbursements execute predictably. Learn more about the [payments lane](/protocol/blockspace/payment-lane-specification).

### Role-Based Access Control (RBAC)

TIP-20 includes a built-in [RBAC system](/protocol/tip403/spec#tip-20-token-roles) that separates administrative responsibilities:

* **ISSUER\_ROLE**: Grants permission to mint and burn tokens, enabling controlled token issuance
* **PAUSE\_ROLE** / **UNPAUSE\_ROLE**: Allows pausing and unpausing token transfers for emergency controls
* **BURN\_BLOCKED\_ROLE**: Permits burning tokens from blocked addresses (e.g., for compliance actions)

Roles can be granted, revoked, and delegated without custom contract changes. This enables issuers to separate operational roles (e.g., who can mint) from administrative roles (e.g., who can pause). Learn more in the [TIP-20 specification](/protocol/tip20/spec#roles).

### TIP-403 Transfer Policies

TIP-20 tokens integrate with the [TIP-403 Policy Registry](/protocol/tip403/overview) to enforce compliance policies. Each token can reference a policy that controls who can send and receive tokens:

* **Whitelist policies**: Only addresses in the whitelist can transfer tokens
* **Blacklist policies**: Addresses in the blacklist are blocked from transferring tokens

Policies can be shared across multiple tokens, enabling consistent compliance enforcement across your token ecosystem. See the [TIP-403 specification](/protocol/tip403/spec) for details.

### Operational Controls

TIP-20 tokens can set **supply caps**, which allow you to set a maximum token supply to control issuance.

TIP-20 tokens also have **pause/unpause** commands, which provide emergency controls to halt transfers when needed.

### Transfer Memos

**Transfer memos** enable you to attach 32-byte memos to transfers for payment references, invoice IDs, or transaction notes.

### Reward Distribution

TIP-20 supports an opt-in [reward distribution system](/protocol/tip20-rewards/overview) that allows issuers to distribute rewards to token holders. Rewards can be claimed by holders or automatically forwarded to designated recipient addresses.

### Currency Declaration

A TIP-20 token can declare a currency identifier (e.g., `"USD"`, `"EUR"`) that identifies the real-world asset backing the token. This enables proper routing and pricing in Tempo's [Stablecoin DEX](/protocol/exchange). **Only `USD`-denominated stablecoins can be used to pay transaction fees on Tempo.** USD-denominated TIP-20 tokens also serve as quote tokens in the DEX.

Stablecoin currency identifiers should be [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-letter currency codes. Common examples include:

| Code  | Currency               |
|-------|------------------------|
| `USD` | United States Dollar   |
| `EUR` | Euro                   |
| `GBP` | British Pound Sterling |
| `JPY` | Japanese Yen           |
| `SGD` | Singapore Dollar       |
| `BRL` | Brazilian Real         |
| `AED` | UAE Dirham             |

The `currency` field represents the **denomination**, not the token itself — multiple tokens can share the same currency code:

| Token         | Correct `currency` | Incorrect `currency` |
|---------------|---------------------|----------------------|
| USDC          | `"USD"`          | `"USDC"`           |
| USDT          | `"USD"`          | `"USDT"`          |
| PYUSD         | `"USD"`          | `"PYUSD"`          |
| EURC          | `"EUR"`          | `"EURC"`           |

:::warning
The currency code is **immutable** — it cannot be changed after token creation. An incorrect currency code will affect fee payment eligibility, DEX routing, and quote token pairing.
:::

### DEX Quote Tokens

TIP-20 tokens can serve as quote tokens in Tempo's decentralized exchange (DEX). When creating trading pairs on the [Stablecoin DEX](/protocol/exchange), TIP-20 tokens function as the quote currency against which other tokens are priced and traded.

This enables efficient stablecoin-to-stablecoin trading and provides optimized routing for liquidity. For example, a USDC TIP-20 token can be paired with other stablecoins, allowing traders to swap between different USD-denominated tokens with minimal slippage through concentrated liquidity pools.

By using TIP-20 tokens as quote tokens, the DEX benefits from the same payment-optimized features like deterministic addresses, currency identifiers, and compliance policies, ensuring secure and efficient exchange operations.

## Additional Links

<Cards>
  <Card description="Learn how TIP-20 works and its features" to="/protocol/tip20/spec" icon="lucide:file-text" title="TIP-20 Specification" />

  <Card description="Send and receive payments using stablecoins on Tempo" to="/guide/payments" icon="lucide:send" title="Guide: Make Payments" />

  <Card description="Create and manage your own stablecoin on Tempo" to="/guide/issuance" icon="lucide:rocket" title="Guide: Issue Stablecoins" />

  <Card description="Solidity reference implementation of the TIP-20 standard" to="https://github.com/tempoxyz/tempo/blob/main/tips/ref-impls/src/TIP20.sol" icon="lucide:file-text" title="Reference Implementation" />
</Cards>

# TIP20

## Abstract

TIP20 is a suite of precompiles that provide a built-in optimized token implementation in the core protocol. It extends the ERC-20 token standard with built-in functionality like memo fields and reward distribution.

## Motivation

All major stablecoins today use the ERC-20 token standard. While ERC-20 provides a solid foundation for fungible tokens, it lacks features critical for stablecoin issuers today such as memos, transfer policies, and rewards distribution. Additionally, since each ERC-20 token has its own implementation, integrators can't depend on consistent behavior across tokens.
TIP-20 extends ERC-20, building these features into precompiled contracts that anyone can permissionlessly deploy on Tempo. This makes token operations much more efficient, allows issuers to quickly set up on Tempo, and simplifies integrations since it ensures standardized behavior across tokens.
It also enables deeper integration with token-specific Tempo features like paying gas in stablecoins and payment lanes.

## Specification

TIP-20 tokens support standard fungible token operations such as transfers, mints, and burns. They also support transfers, mints, and burns with an attached 32-byte memo; a role-based access control system for token administrative operations; and a system for opt-in [reward distribution](/protocol/tip20-rewards/spec).

## TIP20

The core TIP-20 contract exposes standard ERC-20 functions for balances, allowances, transfers, and delegated transfers, and also adds:

* 32-byte memo support on transfers, mints, and burns.
* A `TIP20Roles` module for permissioned actions like issuing, pausing, unpausing, and burning blocked balances.
* Configuration options for currencies, quote tokens, and transfer policies.

The complete TIP20 interface is defined below:

```solidity
interface ITIP20 {
    // =========================================================================
    //                      ERC-20 standard functions
    // =========================================================================

    /// @notice Returns the name of the token
    /// @return The token name
    function name() external view returns (string memory);
    
    /// @notice Returns the symbol of the token
    /// @return The token symbol
    function symbol() external view returns (string memory);
    
    /// @notice Returns the number of decimals for the token
    /// @return Always returns 6 for TIP-20 tokens
    function decimals() external pure returns (uint8);
    
    /// @notice Returns the total amount of tokens in circulation
    /// @return The total supply of tokens
    function totalSupply() external view returns (uint256);
    
    /// @notice Returns the token balance of an account
    /// @param account The address to check the balance for
    /// @return The token balance of the account
    function balanceOf(address account) external view returns (uint256);
    
    /// @notice Transfers tokens from caller to recipient
    /// @param to The recipient address
    /// @param amount The amount of tokens to transfer
    /// @return True if successful
    function transfer(address to, uint256 amount) external returns (bool);
    
    /// @notice Returns the remaining allowance for a spender
    /// @param owner The token owner address
    /// @param spender The spender address
    /// @return The remaining allowance amount
    function allowance(address owner, address spender) external view returns (uint256);
    
    /// @notice Approves a spender to spend tokens on behalf of caller
    /// @param spender The address to approve
    /// @param amount The amount to approve
    /// @return True if successful
    function approve(address spender, uint256 amount) external returns (bool);
    
    /// @notice Transfers tokens from one address to another using allowance
    /// @param from The sender address
    /// @param to The recipient address
    /// @param amount The amount to transfer
    /// @return True if successful
    function transferFrom(address from, address to, uint256 amount) external returns (bool);

    /// @notice Mints new tokens to an address (requires ISSUER_ROLE)
    /// @param to The recipient address
    /// @param amount The amount of tokens to mint
    function mint(address to, uint256 amount) external;

    /// @notice Burns tokens from caller's balance (requires ISSUER_ROLE)
    /// @param amount The amount of tokens to burn
    function burn(uint256 amount) external;

    // =========================================================================
    //                      TIP-20 extended functions
    // =========================================================================

    /// @notice Transfers tokens from caller to recipient with a memo
    /// @param to The recipient address
    /// @param amount The amount of tokens to transfer
    /// @param memo A 32-byte memo attached to the transfer
    function transferWithMemo(address to, uint256 amount, bytes32 memo) external;
    
    /// @notice Transfers tokens from one address to another with a memo using allowance
    /// @param from The sender address
    /// @param to The recipient address
    /// @param amount The amount to transfer
    /// @param memo A 32-byte memo attached to the transfer
    /// @return True if successful
    function transferFromWithMemo(address from, address to, uint256 amount, bytes32 memo) external returns (bool);
    
    /// @notice Mints new tokens to an address with a memo (requires ISSUER_ROLE)
    /// @param to The recipient address
    /// @param amount The amount of tokens to mint
    /// @param memo A 32-byte memo attached to the mint
    function mintWithMemo(address to, uint256 amount, bytes32 memo) external;
    
    /// @notice Burns tokens from caller's balance with a memo (requires ISSUER_ROLE)
    /// @param amount The amount of tokens to burn
    /// @param memo A 32-byte memo attached to the burn
    function burnWithMemo(uint256 amount, bytes32 memo) external;
    
    /// @notice Burns tokens from a blocked address (requires BURN_BLOCKED_ROLE)
    /// @param from The address to burn tokens from (must be unauthorized by transfer policy)
    /// @param amount The amount of tokens to burn
    function burnBlocked(address from, uint256 amount) external;
    
    /// @notice Returns the quote token used for DEX pairing
    /// @return The quote token address
    function quoteToken() external view returns (ITIP20);
    
    /// @notice Returns the next quote token staged for update
    /// @return The next quote token address (zero if none staged)
    function nextQuoteToken() external view returns (ITIP20);
    
    /// @notice Returns the currency identifier for this token
    /// @return The currency string
    function currency() external view returns (string memory);
    
    /// @notice Returns whether the token is currently paused
    /// @return True if paused, false otherwise
    function paused() external view returns (bool);
    
    /// @notice Returns the maximum supply cap for the token
    /// @return The supply cap (checked on mint operations)
    function supplyCap() external view returns (uint256);
    
    /// @notice Returns the current transfer policy ID from TIP-403 registry
    /// @return The transfer policy ID
    function transferPolicyId() external view returns (uint64);
    
    // =========================================================================
    //                            Admin Functions 
    // =========================================================================
    
    /// @notice Pauses the contract, blocking transfers (requires PAUSE_ROLE)
    function pause() external;
    
    /// @notice Unpauses the contract, allowing transfers (requires UNPAUSE_ROLE)
    function unpause() external;
    
    /// @notice Changes the transfer policy ID (requires DEFAULT_ADMIN_ROLE)
    /// @param newPolicyId The new policy ID from TIP-403 registry
    /// @dev Validates that the policy exists using TIP403Registry.policyExists().
    /// Built-in policies (ID 0 = always-reject, ID 1 = always-allow) are always valid.
    /// For custom policies (ID >= 2), the policy must exist in the TIP-403 registry.
    /// Reverts with InvalidTransferPolicyId if the policy does not exist.
    function changeTransferPolicyId(uint64 newPolicyId) external;
    
    /// @notice Stages a new quote token for update (requires DEFAULT_ADMIN_ROLE)
    /// @param newQuoteToken The new quote token address
    function setNextQuoteToken(ITIP20 newQuoteToken) external;
    
    /// @notice Completes the quote token update process (requires DEFAULT_ADMIN_ROLE)
    function completeQuoteTokenUpdate() external;
    
    /// @notice Sets the maximum supply cap (requires DEFAULT_ADMIN_ROLE)
    /// @param newSupplyCap The new supply cap (cannot be less than current supply)
    function setSupplyCap(uint256 newSupplyCap) external;
    
    // =========================================================================
    //                            Role Management
    // =========================================================================
    
    /// @notice Returns the BURN_BLOCKED_ROLE constant
    /// @return keccak256("BURN_BLOCKED_ROLE")
    function BURN_BLOCKED_ROLE() external view returns (bytes32);
    
    /// @notice Returns the ISSUER_ROLE constant
    /// @return keccak256("ISSUER_ROLE")
    function ISSUER_ROLE() external view returns (bytes32);
    
    /// @notice Returns the PAUSE_ROLE constant
    /// @return keccak256("PAUSE_ROLE")
    function PAUSE_ROLE() external view returns (bytes32);
    
    /// @notice Returns the UNPAUSE_ROLE constant
    /// @return keccak256("UNPAUSE_ROLE")
    function UNPAUSE_ROLE() external view returns (bytes32);
    
    /// @notice Grants a role to an account (requires role admin)
    /// @param role The role to grant (keccak256 hash)
    /// @param account The account to grant the role to
    function grantRole(bytes32 role, address account) external;
    
    /// @notice Revokes a role from an account (requires role admin)
    /// @param role The role to revoke (keccak256 hash)
    /// @param account The account to revoke the role from
    function revokeRole(bytes32 role, address account) external;
    
    /// @notice Allows an account to remove a role from itself
    /// @param role The role to renounce (keccak256 hash)
    function renounceRole(bytes32 role) external;
    
    /// @notice Changes the admin role for a specific role (requires current role admin)
    /// @param role The role whose admin is being changed
    /// @param adminRole The new admin role
    function setRoleAdmin(bytes32 role, bytes32 adminRole) external;
    
    // =========================================================================
    //                            System Functions
    // =========================================================================
    
    /// @notice System-level transfer function (restricted to precompiles)
    /// @param from The sender address
    /// @param to The recipient address
    /// @param amount The amount to transfer
    /// @return True if successful
    function systemTransferFrom(address from, address to, uint256 amount) external returns (bool);
    
    /// @notice Pre-transaction fee transfer (restricted to precompiles)
    /// @param from The account to charge fees from
    /// @param amount The fee amount
    function transferFeePreTx(address from, uint256 amount) external;
    
    /// @notice Post-transaction fee handling (restricted to precompiles)
    /// @param to The account to refund
    /// @param refund The refund amount
    /// @param actualUsed The actual fee used
    function transferFeePostTx(address to, uint256 refund, uint256 actualUsed) external;


    // =========================================================================
    //                                Events
    // =========================================================================

    /// @notice Emitted when a new allowance is set by `owner` for `spender`
    /// @param owner The account granting the allowance
    /// @param spender The account being approved to spend tokens
    /// @param amount The new allowance amount
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    /// @notice Emitted when tokens are burned from an address
    /// @param from The address whose tokens were burned
    /// @param amount The amount of tokens that were burned
    event Burn(address indexed from, uint256 amount);

    /// @notice Emitted when tokens are burned from a blocked address
    /// @param from The blocked address whose tokens were burned
    /// @param amount The amount of tokens that were burned
    event BurnBlocked(address indexed from, uint256 amount);

    /// @notice Emitted when new tokens are minted to an address
    /// @param to The address receiving the minted tokens
    /// @param amount The amount of tokens that were minted
    event Mint(address indexed to, uint256 amount);

    /// @notice Emitted when a new quote token is staged for this token
    /// @param updater The account that staged the new quote token
    /// @param nextQuoteToken The quote token that has been staged
    event NextQuoteTokenSet(address indexed updater, ITIP20 indexed nextQuoteToken);

    /// @notice Emitted when the pause state of the token changes
    /// @param updater The account that changed the pause state
    /// @param isPaused The new pause state; true if paused, false if unpaused
    event PauseStateUpdate(address indexed updater, bool isPaused);

    /// @notice Emitted when the quote token update process is completed
    /// @param updater The account that completed the quote token update
    /// @param newQuoteToken The new quote token that has been set
    event QuoteTokenUpdate(address indexed updater, ITIP20 indexed newQuoteToken);

    /// @notice Emitted when a holder sets or updates their reward recipient address
    /// @param holder The token holder configuring the recipient
    /// @param recipient The address that will receive claimed rewards
    event RewardRecipientSet(address indexed holder, address indexed recipient);

    /// @notice Emitted when a reward distribution is scheduled
    /// @param funder The account funding the reward distribution
    /// @param amount The total amount of tokens allocated to the reward
    event RewardDistributed(
        address indexed funder,
        uint256 amount,
    );

    /// @notice Emitted when the token's supply cap is updated
    /// @param updater The account that updated the supply cap
    /// @param newSupplyCap The new maximum total supply
    event SupplyCapUpdate(address indexed updater, uint256 indexed newSupplyCap);

    /// @notice Emitted for all token movements, including mints and burns
    /// @param from The address sending tokens (address(0) for mints)
    /// @param to The address receiving tokens (address(0) for burns)
    /// @param amount The amount of tokens transferred
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /// @notice Emitted when the transfer policy ID is updated
    /// @param updater The account that updated the transfer policy
    /// @param newPolicyId The new transfer policy ID from the TIP-403 registry
    event TransferPolicyUpdate(address indexed updater, uint64 indexed newPolicyId);

    /// @notice Emitted when a transfer, mint, or burn is performed with an attached memo
    /// @param from The address sending tokens (address(0) for mints)
    /// @param to The address receiving tokens (address(0) for burns)
    /// @param amount The amount of tokens transferred
    /// @param memo The 32-byte memo associated with this movement
    event TransferWithMemo(
        address indexed from,
        address indexed to,
        uint256 amount,
        bytes32 indexed memo
    );

    /// @notice Emitted when the membership of a role changes for an account
    /// @param role The role being granted or revoked
    /// @param account The account whose membership was changed
    /// @param sender The account that performed the change
    /// @param hasRole True if the role was granted, false if it was revoked
    event RoleMembershipUpdated(
        bytes32 indexed role,
        address indexed account,
        address indexed sender,
        bool hasRole
    );

    /// @notice Emitted when the admin role for a role is updated
    /// @param role The role whose admin role was changed
    /// @param newAdminRole The new admin role for the given role
    /// @param sender The account that performed the update
    event RoleAdminUpdated(
        bytes32 indexed role,
        bytes32 indexed newAdminRole,
        address indexed sender
    );

    // =========================================================================
    //                                Errors
    // =========================================================================

    /// @notice The token operation is blocked because the contract is currently paused
    error ContractPaused();

    /// @notice The spender does not have enough allowance for the attempted transfer
    error InsufficientAllowance();

    /// @notice The account does not have the required token balance for the operation
    /// @param currentBalance The current balance of the account
    /// @param expectedBalance The required balance for the operation to succeed
    /// @param token The address of the token contract
    error InsufficientBalance(uint256 currentBalance, uint256 expectedBalance, address token);

    /// @notice The provided amount is zero or otherwise invalid for the attempted operation
    error InvalidAmount();

    /// @notice The provided currency identifier is invalid or unsupported
    error InvalidCurrency();

    /// @notice The specified quote token is invalid, incompatible, or would create a circular reference
    error InvalidQuoteToken();

    /// @notice The recipient address is not a valid destination for this operation
    ///         (for example, another TIP-20 token contract)
    error InvalidRecipient();

    /// @notice The specified transfer policy ID does not exist in the TIP-403 registry
    error InvalidTransferPolicyId();

    /// @notice The new supply cap is invalid, for example lower than the current total supply
    error InvalidSupplyCap();

    /// @notice A rewards operation was attempted when no opted-in supply exists
    error NoOptedInSupply();

    /// @notice The configured transfer policy denies authorization for the sender or recipient
    error PolicyForbids();

    /// @notice The attempted operation would cause total supply to exceed the configured supply cap
    error SupplyCapExceeded();

    /// @notice The caller does not have the required role or permission for this operation
    error Unauthorized();

}
```

:::warning
When interacting with precompiles, **always use the provided ABI** rather than reading directly from storage slots. Direct storage access may lead to undefined behavior.
:::

## Memos

Memo functions `transferWithMemo`, `transferFromWithMemo`, `mintWithMemo`, and `burnWithMemo` behave like their ERC-20 equivalents but additionally emit memo data in dedicated events. The memo is always a fixed 32-byte field. Callers should pack shorter strings or identifiers directly into this field, and use hashes or external references when the underlying payload exceeds 32 bytes.

## TIP-403 Transfer Policies

All operations that move tokens: `transfer`, `transferFrom`, `transferWithMemo`, `transferFromWithMemo`, `mint`, `burn`, `mintWithMemo`, and `burnWithMemo` — enforce the token’s configured TIP-403 transfer policy.

Internally, this is implemented via a `transferAuthorized` modifier that:

* Calls `TIP403_REGISTRY.isAuthorized(transferPolicyId, from)` for the sender.
* Calls `TIP403_REGISTRY.isAuthorized(transferPolicyId, to)` for the recipient.

Both checks must return `true`, otherwise the call reverts with `PolicyForbids`.
Reward operations (`distributeReward`, `setRewardRecipient`, `claimRewards`) also perform the same TIP-403 authorization checks before moving any funds.

## Invalid Recipient Protection

TIP-20 tokens cannot be sent to other TIP-20 token contract addresses. The implementation uses a `validRecipient` guard that rejects recipients whose address is zero, or has the TIP-20 prefix (`0x20c000000000000000000000`).
Any attempt to transfer to a TIP-20 token address must revert with `InvalidRecipient`. This prevents accidental token loss by sending funds to token contracts instead of user accounts.

## Currencies and Quote Tokens

Each TIP-20 token declares a currency identifier and a corresponding `quoteToken` used for pricing and routing in the Stablecoin DEX. Stablecoin currency identifiers should be [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) three-letter codes representing the underlying fiat currency (e.g., `"USD"`, `"EUR"`, `"GBP"`) — not the token's own symbol. The currency is set at token creation and **cannot be changed afterward**. **Only tokens with `currency == "USD"` are eligible for paying transaction fees.** Tokens with `currency == "USD"` must pair with a USD-denominated TIP-20 token.

Updating the quote token occurs in two phases:

1. `setNextQuoteToken` stages a new quote token.
2. `completeQuoteTokenUpdate` finalizes the change.

The implementation must validate that the new quote token is a TIP-20 token, matches currency rules, and does not create circular quote-token chains.

:::note
While quote tokens can be changed, choose carefully as the update process requires careful coordination with the DEX.
:::

## Pause Controls

Pause controls `pause` and `unpause` govern all transfer operations and reward related flows. When paused, transfers and memo transfers halt, but administrative and configuration functions remain allowed. The `paused()` getter reflects the current state and must be checked by all affected entrypoints.

## TIP-20 Roles

TIP-20 uses a role-based authorization system. The main roles are:

* `ISSUER_ROLE`: controls minting and burning.
* `PAUSE_ROLE` / `UNPAUSE_ROLE`: controls the token’s paused state.
* `BURN_BLOCKED_ROLE`: allows burning balances belonging to addresses that fail TIP-403 authorization.

Roles are assigned and managed through `grantRole`, `revokeRole`, `renounceRole`, and `setRoleAdmin`, via the contract admin.

## System Functions

System level functions `systemTransferFrom`, `transferFeePreTx`, and `transferFeePostTx` are only callable by other Tempo protocol precompiles. These entrypoints power transaction fee collection, refunds, and internal accounting within the Fee AMM and Stablecoin DEX. They must not be callable by general contracts or users.

`transferFeePreTx` respects the token's pause state and will revert if the token is paused. However, `transferFeePostTx` is intentionally allowed to execute even when the token is paused. This ensures that a transaction which pauses the token can still complete successfully and receive its fee refund. Apart from this specific refund transfer, no other token transfers can occur after a pause event.

## Token Rewards Distribution

See [rewards distribution](/protocol/tip20-rewards/spec) for more information.

## TIP20Factory

The `TIP20Factory` contract is the canonical entrypoint for creating new TIP-20 tokens on Tempo. The factory derives deterministic deployment addresses using a caller-provided salt, combined with the caller's address, under a fixed 12-byte TIP-20 prefix. This ensures that every TIP-20 token exists at a predictable, collision-free address. The `TIP20Factory` precompile is deployed at `0x20Fc000000000000000000000000000000000000`.

Newly created TIP-20 addresses are deployed to a deterministic address derived from `TIP20_PREFIX || lowerBytes`, where:

* `TIP20_PREFIX` is the 12-byte prefix `20C000000000000000000000`
* `lowerBytes` is the highest 64 bits of `keccak256(msg.sender, salt)`

The first 1000 addresses (where `lowerBytes < 1000`) are reserved for protocol use and cannot be deployed to via the factory.

When creating a token, the factory performs several checks to guarantee consistency across the TIP-20 ecosystem:

* The specified Quote token must be a currently deployed TIP20.
* Tokens that specify their currency as USD must also specify a quote token that is denoted in USD.
* At deployment, the factory initializes defaults on the TIP-20:\
  `transferPolicyId = 1`, `supplyCap = type(uint128).max`, `paused = false`, and `totalSupply = 0`.
* The provided `admin` address receives `DEFAULT_ADMIN_ROLE`, enabling it to manage roles and token configurations.

The complete `TIP20Factory` interface is defined below:

```solidity
/// @title TIP-20 Factory Interface
/// @notice Deploys and initializes new TIP-20 tokens at deterministic addresses
interface ITIP20Factory {
    /// @notice Creates and deploys a new TIP-20 token
    /// @param name The token's ERC-20 name
    /// @param symbol The token's ERC-20 symbol
    /// @param currency The token's ISO 4217 currency code (e.g. "USD", "EUR"). Immutable after creation.
    /// @param quoteToken The TIP-20 quote token used for exchange pricing
    /// @param admin The address to receive DEFAULT_ADMIN_ROLE on the new token
    /// @param salt A unique salt for deterministic address derivation
    ///
    /// @return token The deployed TIP-20 token address
    /// @dev
    ///  - Computes the TIP-20 deployment address as TIP20_PREFIX || lowerBytes,
    ///    where lowerBytes is the highest 64 bits of keccak256(msg.sender, salt)
    ///  - Reverts with AddressReserved if lowerBytes < 1000
    ///  - Ensures the provided quote token is itself a valid TIP-20
    ///  - Enforces USD-denomination rules (USD tokens must use USD quote tokens)
    ///  - Initializes the token with default settings:
    ///         transferPolicyId = 1 (always-allow)
    ///         supplyCap        = type(uint128).max
    ///         paused           = false
    ///         totalSupply      = 0
    ///  - Grants DEFAULT_ADMIN_ROLE on the new token to `admin`
    ///  - Emits a {TokenCreated} event
    function createToken(
        string memory name,
        string memory symbol,
        string memory currency,
        ITIP20 quoteToken,
        address admin,
        bytes32 salt
    ) external returns (address token);

    // =========================================================================
    //                                Helpers
    // =========================================================================

    /// @notice Returns true if `token` is a valid TIP-20 address
    /// @param token The address to check
    /// @return True if the address is a well-formed TIP-20
    /// @dev Checks the TIP-20 prefix and verifies the token has code deployed
    function isTIP20(address token) external view returns (bool);

    /// @notice Computes the deterministic TIP-20 address for a given sender and salt
    /// @param sender The address that will call {createToken}
    /// @param salt The salt that will be passed to {createToken}
    /// @return token The TIP-20 address that would be deployed
    /// @dev Computes the address as TIP20_PREFIX || lowerBytes, where lowerBytes is
    ///      the highest 64 bits of keccak256(sender, salt), matching the factory deployment scheme.
    function getTokenAddress(address sender, bytes32 salt) external pure returns (address token);

    // =========================================================================
    //                                Events
    // =========================================================================

    /// @notice Emitted when a new TIP-20 token is created
    /// @param token The newly deployed TIP-20 address
    /// @param name The token name
    /// @param symbol The token symbol
    /// @param currency The token currency
    /// @param quoteToken The token's assigned quote token
    /// @param admin The address receiving DEFAULT_ADMIN_ROLE
    /// @param salt The salt used for deterministic address derivation
    event TokenCreated(
        address indexed token,
        string name,
        string symbol,
        string currency,
        ITIP20 quoteToken,
        address admin,
        bytes32 salt
    );

    // =========================================================================
    //                                Errors
    // =========================================================================

    /// @notice The computed address falls within the reserved range (lowerBytes < 1000)
    error AddressReserved();

    /// @notice The provided quote token address is invalid or not a TIP-20
    error InvalidQuoteToken();
}
```

## Invariants

* `totalSupply()` must always equal to the sum of all `balanceOf(account)` over all accounts.
* `totalSupply()` must always be `<= supplyCap`
* When `paused` is `true`, no functions that move tokens (`transfer`, `transferFrom`, memo variants, `systemTransferFrom`, `transferFeePreTx`, `distributeReward`, `setRewardRecipient`, `claimRewards`) can succeed.
* TIP20 tokens cannot be transferred to another TIP20 token contract address.
* `systemTransferFrom`, `transferFeePreTx`, and `transferFeePostTx` never change `totalSupply()`.

# TIP-403 Policy Registry

## What is TIP-403?

TIP-403 is Tempo's policy registry system that enables TIP-20 tokens to enforce access control. Instead of each token implementing its own logic, TIP-403 provides a registry where policies can be created once and shared across multiple tokens.

## Links

<Cards>
  <Card description="Learn how TIP-403 works and its features" to="/protocol/tip403/spec" icon="lucide:file-text" title="TIP-403 Specification" />

  <Card description="Manage your stablecoin's permissions, supply, and compliance settings" to="/guide/issuance/manage-stablecoin" icon="lucide:settings" title="Guide: Manage Your Stablecoin" />

  <Card description="Solidity reference implementation of the TIP-403 standard" to="https://github.com/tempoxyz/tempo/blob/main/tips/ref-impls/src/TIP403Registry.sol" icon="lucide:file-text" title="Reference Implementation" />

  <Card description="Rust implementation in the Tempo client" to="https://github.com/tempoxyz/tempo/tree/main/crates/precompiles/src/tip403_registry" icon="lucide:file-text" title="Rust Implementation" />
</Cards>

# Overview

## Abstract

TIP-403 provides a policy registry system that allows TIP-20 tokens to inherit access control and compliance policies. The registry supports two types of policies (whitelist and blacklist) and includes special built-in policies for common use cases. Policies can be shared across multiple tokens, enabling consistent compliance enforcement.

## Motivation

Token issuers often need to implement compliance policies such as KYC/AML requirements, access control, and risk management. Without a standardized system, each token would need to implement its own policy logic, making policy management more difficult and inconsistent across the ecosystem.

TIP-403 addresses this by providing a centralized registry that tokens can reference for authorization decisions. This enables consistent policy enforcement across multiple tokens and reduces implementation complexity for token issuers.

***

# Specification

The TIP-403 registry stores policies that TIP-20 tokens check against on any token transfer. Policies are associated with a unique `policyId`, can either be a blacklist or a whitelist policy, and contain a list of addresses. This list of addresses can be updated by the policy `admin`.

The TIP403Registry is deployed at address `0x403c000000000000000000000000000000000000`.

## Built-in Policies

Custom policies start with `policyId = 2`. The registry reserves the first two ids for built-in policies:

* `policyId = 0` is the `always-reject` policy and rejects all token transfers
* `policyId = 1` is the `always-allow` policy and allows all token transfers

The `policyIdCounter` starts at `2` and increments with each new policy creation.

## Policy Types

TIP-403 supports two policy types:

* **Whitelist Policies:** Only addresses in the whitelist can transfer tokens. All other addresses are blocked
* **Blacklist Policies:** Addresses in the blacklist are blocked from transferring tokens. All other addresses can transfer

## Storage and State

The registry maintains the following state:

* `policyIdCounter`: Starts at `2`, increments with each new policy creation. Returns the next policy ID that will be assigned.
* `policyData`: Mapping from `policyId` to `PolicyData` struct containing policy type and admin address.
* `policySet`: Internal mapping from `policyId` to address to boolean, tracking which addresses are in each policy's set.

## Interface Definition

The complete TIP403Registry interface is defined below:

```solidity
interface ITIP403Registry {
    // =========================================================================
    //                            Types and Enums
    // =========================================================================

    enum PolicyType {
        WHITELIST,
        BLACKLIST
    }

    struct PolicyData {
        PolicyType policyType;
        address admin;
    }

    // =========================================================================
    //                         Policy Creation
    // =========================================================================

    /// @notice Creates a new policy with the specified admin and type
    /// @param admin Address that can modify this policy
    /// @param policyType Type of policy (whitelist or blacklist)
    /// @return newPolicyId ID of the newly created policy
    /// @dev Anyone can create a policy. The creator specifies an admin address that can modify the policy.
    /// Assigns the next available policyId starting from 2, sets the policy admin, and initializes an empty policy set.
    /// Emits PolicyCreated and PolicyAdminUpdated events.
    function createPolicy(
        address admin,
        PolicyType policyType
    ) external returns (uint64 newPolicyId);

    /// @notice Creates a policy and immediately adds the provided accounts to the policy set
    /// @param admin Address that can modify this policy
    /// @param policyType Type of policy (whitelist or blacklist)
    /// @param accounts Initial addresses to add to the policy
    /// @return newPolicyId ID of the newly created policy
    /// @dev For whitelist policies: adds accounts as authorized. For blacklist policies: adds accounts as restricted.
    /// Emits PolicyCreated, PolicyAdminUpdated, and either WhitelistUpdated or BlacklistUpdated events for each account added.
    function createPolicyWithAccounts(
        address admin,
        PolicyType policyType,
        address[] calldata accounts
    ) external returns (uint64 newPolicyId);

    // =========================================================================
    //                        Policy Administration
    // =========================================================================

    /// @notice Transfers admin rights to another address
    /// @param policyId ID of the policy to update
    /// @param admin New admin address for the policy
    /// @dev Only the current policy admin can call this function. The new admin immediately gains full control over the policy.
    /// Emits PolicyAdminUpdated event.
    function setPolicyAdmin(uint64 policyId, address admin) external;

    /// @notice Adds or removes addresses from a whitelist policy
    /// @param policyId ID of the whitelist policy
    /// @param account Address to add or remove
    /// @param allowed true to allow, false to block
    /// @dev Only the policy admin can call this function. allowed = true adds the address to the whitelist (authorized to transfer).
    /// allowed = false removes the address from the whitelist (not authorized). Reverts if policy is not a whitelist.
    /// Emits WhitelistUpdated event.
    function modifyPolicyWhitelist(
        uint64 policyId,
        address account,
        bool allowed
    ) external;

    /// @notice Adds or removes addresses from a blacklist policy
    /// @param policyId ID of the blacklist policy
    /// @param account Address to add or remove
    /// @param restricted true to block, false to allow
    /// @dev Only the policy admin can call this function. restricted = true adds the address to the blacklist (not authorized to transfer).
    /// restricted = false removes the address from the blacklist (authorized). Reverts if policy is not a blacklist.
    /// Emits BlacklistUpdated event.
    function modifyPolicyBlacklist(
        uint64 policyId,
        address account,
        bool restricted
    ) external;

    // =========================================================================
    //                        Policy Queries
    // =========================================================================

    /// @notice Returns whether the provided user is allowed to transfer tokens under the provided policy ID
    /// @param policyId Policy ID to check against
    /// @param user Address to check
    /// @return True if authorized, false if blocked
    /// @dev For policyId = 0 (always-reject): Always returns false
    /// For policyId = 1 (always-allow): Always returns true
    /// For whitelist policies: Returns true if address is in the whitelist, false otherwise
    /// For blacklist policies: Returns true if address is NOT in the blacklist, false if it is
    function isAuthorized(uint64 policyId, address user) external view returns (bool);

    /// @notice Returns the next policy ID that will be assigned to a newly created policy
    /// @return The current policyIdCounter value
    /// @dev Starts at 2 and increments with each policy creation
    function policyIdCounter() external view returns (uint64);

    /// @notice Returns whether a policy exists
    /// @param policyId ID of the policy to check
    /// @return True if the policy exists, false otherwise
    /// @dev Policy IDs 0 and 1 (built-in policies) always exist. For custom policies (ID >= 2),
    /// checks if the policy ID is within the range of created policies based on policyIdCounter.
    function policyExists(uint64 policyId) external view returns (bool);

    /// @notice Returns the policy type and admin address of the policy associated with the provided policy ID
    /// @param policyId ID of the policy to query
    /// @return policyType Type of the policy (whitelist or blacklist)
    /// @return admin Admin address of the policy
    function policyData(uint64 policyId) external view returns (PolicyType policyType, address admin);

    // =========================================================================
    //                                Events
    // =========================================================================

    /// @notice Emitted when a new policy is created
    /// @param policyId ID of the newly created policy
    /// @param updater Address that created the policy
    /// @param policyType Type of policy created
    event PolicyCreated(
        uint64 indexed policyId,
        address indexed updater,
        PolicyType policyType
    );

    /// @notice Emitted when a policy's admin is changed
    /// @param policyId ID of the policy
    /// @param updater Address that made the change
    /// @param admin New admin address
    event PolicyAdminUpdated(
        uint64 indexed policyId,
        address indexed updater,
        address indexed admin
    );

    /// @notice Emitted when an address is added to or removed from a whitelist policy
    /// @param policyId ID of the whitelist policy
    /// @param updater Address that made the change
    /// @param account Account that was added or removed
    /// @param allowed true if added, false if removed
    event WhitelistUpdated(
        uint64 indexed policyId,
        address indexed updater,
        address indexed account,
        bool allowed
    );

    /// @notice Emitted when an address is added to or removed from a blacklist policy
    /// @param policyId ID of the blacklist policy
    /// @param updater Address that made the change
    /// @param account Account that was added or removed
    /// @param restricted true if blocked, false if unblocked
    event BlacklistUpdated(
        uint64 indexed policyId,
        address indexed updater,
        address indexed account,
        bool restricted
    );

    // =========================================================================
    //                                Errors
    // =========================================================================

    /// @notice Caller is not the policy admin
    error Unauthorized();

    /// @notice Wrong policy type for the operation
    error IncompatiblePolicyType();
}
```

## Usage with TIP-20 Tokens

TIP-20 tokens store the current TIP403 registry policy ID they adhere to in their storage. On any token transfer, they perform a TIP-403 policy check by calling `isAuthorized()` for both sender and recipient addresses. The policy to use for the token can only be set by the admin of the token.

**Default Policy:** New tokens start with `transferPolicyId = 1` (always-allow policy).

**Policy Changes:** When a token's transfer policy is changed via `changeTransferPolicyId()`, all future transfers are immediately subject to the new policy.

### Example Usage

Creating and setting a policy:

```solidity
address admin = address(this);

// Create policy with registry
uint64 policyId = tip403Registry.createPolicy(admin, PolicyType.WHITELIST);

// Add authorized addresses to whitelist
tip403Registry.modifyPolicyWhitelist(policyId, authorizedUser, true);

// Set policy on the token
token.changeTransferPolicyId(policyId);
```

## Authorization Logic

The `isAuthorized()` function implements the following logic:

```solidity
if (policyId < 2) {
    return policyId == 1; // 0 = reject, 1 = allow
}
PolicyData memory data = policyData[policyId];
return data.policyType == PolicyType.WHITELIST
    ? policySet[policyId][user]
    : !policySet[policyId][user];
```

# Invariants

* When policyId = 0, all authorization checks must return false for every address.
* When policyId = 1, all authorization checks must return true for every address.
* Only the policy’s current admin may update the admin address for that policy.

# TIP-XXXX: TIP Title

## Abstract

Short 2–4 sentence high level summary

## Motivation

Explain what problem this solves/functionality this introduces, and any alternatives considered (if applicable). Add context or links to other specs/resources that serve as prerequisites to this spec.

***

# Specification

This section should provide a complete description of the feature’s behavior and required interfaces.

If the feature introduces a precompile, this section should include the full interface definition along with comprehensive NatSpec. Each function should clearly describe its parameters, return values, and error conditions. The goal is to define the intended functionality clearly enough that an engineer can implement the reference contract, test suite, and node implementation without needing to infer any implementation details.

For features that do not introduce a precompile, this section should define the exact mechanics of the feature/system. Describe the relevant state transitions, data structures, encodings, etc. When the feature interacts with existing components, explain how they relate and how data moves between them each system component.

Where a feature involves multiple processes, state diagrams / flowcharts should be considered when helpful.

# Invariants

This section should describe invariants that must always hold, and outline the critical cases that the test suite must cover.

# TIP-1000: State Creation Cost Increase

* **Protocol Version**: T1

## Abstract

This TIP increases the gas cost for creating new state elements, accounts, and contract code to provide economic protection against state growth spam attacks. The proposal increases the cost of writing a new state element from 20,000 gas to 250,000 gas, introduces a 250,000 gas charge for account creation (when the account's nonce is first written), and implements a new contract creation cost model: 1,000 gas per byte of contract code plus 500,000 gas for keccak hash and codesize fields.

## Motivation

Tempo's high throughput capability (approximately 20,000 transactions per second) creates a vulnerability where an adversary could create a massive amount of state with the intent of permanently slowing the chain down. If each transaction is used to create a new account, and each account requires approximately 200 bytes of storage, then over 120 TB of storage could be created in a single year. Even if this storage is technically feasible, the database performance implications are unknown and would likely require significant R\&D on state management much earlier than needed for business requirements.

The current EVM gas schedule charges 20,000 gas for writing a new state element and has no cost for creating an account. This makes state creation attacks economically viable for adversaries. By increasing these costs to 250,000 gas each, we create a meaningful economic barrier: creating 1 TB of state would cost approximately $50 million, and creating 10 TB would cost approximately $500 million (based on the assumption that a TIP-20 transfer costs 50,000 gas = 0.1 cent, implying 1 cent per 500,000 gas).

### Alternatives Considered

1. **Storage rent**: Implementing a periodic fee for holding state. This was rejected due to complexity and poor user experience.
2. **State expiry**: Automatically removing unused state after a time period. This was rejected due to technical complexity and breaking changes to existing applications.
3. **Lower cost increases**: Using smaller multipliers (e.g., 50,000 gas instead of 250,000 gas). This was rejected as it would not provide sufficient economic deterrent against well-funded attackers.

## Terminology

This TIP uses the following economic unit terminology:

* **Microdollars**: TIP-20 token units at 10^-6 USD precision (6 decimals). One TIP-20 token unit = 1 microdollar = 0.000001 USD = 0.0001 cents.

* **Attodollars**: Gas accounting units at 10^-18 USD precision. Gas prices (basefee) are denominated in attodollars.

* **Conversion**: Gas cost in microdollars = (gas × basefee in attodollars) / 10^12

These units provide precise economic accounting while maintaining human-readable dollar relationships.

***

# Specification

## Gas Cost Changes

### New State Element Creation

**Current Behavior:**

* Writing a new state element (SSTORE to a zero slot) costs 20,000 gas

**Proposed Behavior:**

* Writing a new state element (SSTORE to a zero slot) costs 250,000 gas

This applies to all storage slot writes that transition from zero to non-zero, including:

* Contract storage slots
* TIP-20 token balances
* Nonce key storage in the Nonce precompile (when a new nonce key is first used)
* Rewards-related storage (userRewardInfo mappings, reward balances)
* Active key count tracking in the Nonce precompile
* Any other state elements stored in the EVM state trie

**Note:** Since Tempo-specific operations (nonce keys, rewards processing, etc.) ultimately use EVM storage operations (SSTORE), they are automatically subject to the new state creation pricing. The implementation must ensure all new state element creation is correctly charged at 250,000 gas, regardless of which precompile or contract creates the state.

### Account Creation

**Current Behavior:**

* Account creation has no explicit gas cost
* The account is created implicitly when its nonce is first written

**Proposed Behavior:**

* Account creation incurs a 250,000 gas charge when the account's nonce is first written
* This charge applies when the account is first used (e.g., sends its first transaction), not when it first receives tokens

**Implementation Details:**

* The charge is applied when `account.nonce` transitions from 0 to 1
* The charge also applies to other nonces with [nonce keys](/protocol/transactions/spec-tempo-transaction#specification) (2D nonces)
* Transactions with a nonce value of 0 need to supply at least 271,000 gas and are otherwise invalid
* For EOA accounts: charged on the first transaction sent from that address (when the account is first used)
* For contract accounts: charged when the contract is deployed (CREATE or CREATE2)
* **Important:** When tokens are transferred TO a new address, the recipient's nonce remains 0, so no account creation cost is charged. The account creation cost only applies when the account is first used (sends a transaction).
* The charge is in addition to any other gas costs for the transaction

### Contract Creation

**Current Behavior:**

* Contract creation (CREATE/CREATE2) has a base cost of 32,000 gas plus 200 gas per byte of contract code
* Total cost formula: `32,000 + (code_size × 200)` gas
* Example: A 1,000 byte contract costs 32,000 + (1,000 × 200) = 232,000 gas

**Proposed Behavior:**

* Contract creation replaces the existing EVM per-byte cost with a new pricing model:
  * Each byte: 1,000 gas per byte (linear pricing)
  * TX create cost: 2 × 250,000 gas = 500,000 gas for keccak hash and nonce fields
* This pricing applies to the contract code size (the bytecode being deployed)

**Implementation Details:**

* The code storage cost is calculated as: `code_size × 1,000`
* Additional state creation costs: 2 × 250,000 gas = 500,000 gas for keccak hash and codesize fields
* Total contract creation cost: `(code_size × 1,000) + 500,000` gas
* This replaces the existing EVM per-byte cost for contract creation (not an additional charge)
* Applies to both CREATE and CREATE2 operations
* The account creation cost (250,000 gas) is separate and still applies when the contract account's nonce transitions from 0 to 1

### Intrinsic transaction gas

A transaction is invalid if the minimal costs of a (reverting) transaction can't be covered by caller's balance. Those checks are done in the transaction pool as a DOS prevention measure as well as when a transaction is first executed as part of a block.

* Transaction with `nonce == 0` require an additional 250,000 gas
* Tempo transactions with any `nonce_key` and `nonce == 0` require an additional 250,000 gas
* Changes to EIP-7702 authorization lists:
  * EIP-7702 authorisation list entries with `auth_list.nonce == 0` require an additional 250,000 gas.
  * The base cost per authorization is reduced to 12,500 gas
  * There is no refund if the account already exists
* The additional initial cost for CREATE transactions that deploy a contract is increased to 500,000 from currently 32,000 (to reflect the upfront cost in contract creation)
  * If the first transaction in a batch is a CREATE transaction, the additional cost of 500,000 needs to be charged

### Other changes

The transaction gas cap is changed from 16M to 30M to accommodate the deployment of 24kb contracts.

Tempo transaction key authorisations can't determine whether it is going to create new storage or not. If the transaction cannot pay for the key authorization storage costs, the transaction reverts any authorization key that has been set.

## Gas Schedule Summary

| Operation | Current Gas Cost | Proposed Gas Cost | Change |
|-----------|------------------|-------------------|--------|
| New state element (SSTORE zero → non-zero) | 20,000 | 250,000 | +230,000 |
| Account creation (first nonce write) | 0 | 250,000 | +250,000 |
| Contract creation (per byte) | 200 | 1,000 | +800 |
| Contract creation (keccak + codesize fields) | Included in base | 500,000 | +500,000 |
| Existing state element (SSTORE non-zero → non-zero) | 5,000 | 5,000 | No change |
| Existing state element (SSTORE non-zero → zero) | -15,000 (refund) | -15,000 (refund) | No change |

## Economic Impact Analysis

### Cost Calculations

Based on the assumptions:

* TIP-20 transfer cost (to existing address, including base transaction and state update): 50,000 gas = 0.1 cent (1,000 microdollars)
* Implied gas price: 1 cent per 500,000 gas (10,000 microdollars per 500,000 gas)

**New State Element Creation:**

* Gas cost: 250,000 gas
* Dollar cost: 250,000 / 500,000 = **0.5 cents (5,000 microdollars) per state element**

**Account Creation:**

* Gas cost: 250,000 gas
* Dollar cost: 250,000 / 500,000 = **0.5 cents (5,000 microdollars) per account**

**Contract Creation:**

* Per byte: 1,000 gas = **0.002 cents (20 microdollars) per byte**
* Keccak + nonce fields: 500,000 gas (2 × 250,000) = **1.0 cent (10,000 microdollars)**
* Example: 1,000 byte contract = (1,000 × 1,000) + 500,000 = 1,500,000 gas = **3.0 cents (30,000 microdollars)**

### Attack Cost Analysis

**Creating 1 TB of state:**

* 1 TB = 1,000,000,000,000 bytes
* Assuming ~100 bytes per state element: 10,000,000,000 state elements
* Cost: 10,000,000,000 × 0.5 cents = **$50,000,000**

**Creating 10 TB of state:**

* 10 TB = 10,000,000,000,000 bytes
* Assuming ~100 bytes per state element: 100,000,000,000 state elements
* Cost: 100,000,000,000 × 0.5 cents = **$500,000,000**

These costs serve as a significant economic deterrent against state growth spam attacks.

## Impact on Normal Operations

### Transfer to New Address

**Current Cost:**

* TIP-20 transfer (base + operation): 50,000 gas
* New state element (balance): 20,000 gas
* **Total: ~70,000 gas ≈ 0.14 cents**
* Note: Account creation cost does not apply here because the recipient's nonce remains 0

**Proposed Cost:**

* TIP-20 transfer (base + operation): 50,000 gas
* New state element (balance): 250,000 gas
* **Total: ~300,000 gas ≈ 0.6 cents**
* Note: Account creation cost does not apply here because the recipient's nonce remains 0

**Impact:** A transfer to a new address increases from 0.14 cents to 0.6 cents, representing a 4.3x increase. The account creation cost (0.5 cents) will be charged separately when the recipient first uses their account.

### First Use of New Account

**Current Cost:**

* TIP-20 transfer (base + operation + state update): 50,000 gas
* Account creation: 0 gas
* **Total: 50,000 gas ≈ 0.1 cents**

**Proposed Cost:**

* TIP-20 transfer (base + operation + state update): 50,000 gas
* Account creation (nonce 0 → 1): 250,000 gas
* **Total: ~300,000 gas ≈ 0.6 cents**

**Impact:** The first transaction from a new account increases from 0.1 cents to 0.6 cents, representing a 6x increase. Combined with the initial transfer cost (0.6 cents), the total onboarding cost for a new user is approximately 1.2 cents.

### Transfer to Existing Address

**Current Cost:**

* TIP-20 transfer (base + operation + state update): 50,000 gas
* **Total: 50,000 gas ≈ 0.1 cents**

**Proposed Cost:**

* TIP-20 transfer (base + operation + state update): 50,000 gas
* **Total: 50,000 gas ≈ 0.1 cents**

**Impact:** No change for transfers to existing addresses.

### Contract Deployment

**Current Cost:**

* Contract code storage: 32,000 gas base + 200 gas per byte
* Example for 1,000 byte contract: 32,000 + (1,000 × 200) = 232,000 gas ≈ 0.46 cents

**Proposed Cost:**

* Account creation: 250,000 gas
* Contract code storage: code\_size × 1,000 gas
* Keccak + nonce fields: 500,000 gas (2 × 250,000)
* Example for 1,000 byte contract: 250,000 + (1,000 × 1,000) + 500,000 = 1,750,000 gas ≈ **3.5 cents**

**Impact:** Contract deployment costs increase significantly, especially for larger contracts. A 100 byte contract costs (100 × 1,000) + 500,000 + 250,000 = 850,000 gas = 1.7 cents total.

## Implementation Requirements

### Node Implementation

The node implementation must:

1. **Detect new state element creation:**
   * Track SSTORE operations that write to a zero slot
   * Charge 250,000 gas instead of 20,000 gas for these operations

2. **Detect account creation:**
   * Track when an account's nonce transitions from 0 to 1
   * Charge 250,000 gas for this transition
   * Apply to both EOA and contract account creation

3. **Implement contract creation pricing:**
   * Replace existing EVM per-byte cost for contract code storage
   * Charge 1,000 gas per byte of contract code (linear pricing)
   * Charge 500,000 gas (2 × 250,000) for keccak hash and codesize fields
   * Total formula: `(code_size × 1,000) + 500,000`
   * Apply to both CREATE and CREATE2 operations

4. **Maintain backward compatibility:**
   * Existing state operations (non-zero to non-zero, non-zero to zero) remain unchanged
   * Gas refunds for storage clearing remain unchanged

### Test Suite Requirements

The test suite must verify:

1. **New state element creation:**
   * SSTORE to zero slot charges 250,000 gas
   * Multiple new state elements in one transaction are each charged 250,000 gas
   * Existing state element updates (non-zero to non-zero) remain at 5,000 gas

2. **Account creation:**
   * First transaction from EOA charges 250,000 gas for account creation (when nonce transitions 0 → 1)
   * Contract deployment (CREATE) charges 250,000 gas for account creation
   * Contract deployment (CREATE2) charges 250,000 gas for account creation
   * Transfer TO a new address does NOT charge account creation fee (recipient's nonce remains 0)
   * Subsequent transactions from the same account do not charge account creation fee

3. **Contract creation:**
   * Contract code storage replaces EVM per-byte cost with new pricing model
   * Each byte of contract code costs 1,000 gas (linear pricing)
   * Keccak hash and codesize fields cost 500,000 gas (2 × 250,000) total
   * Total cost formula: `(code_size × 1,000) + 500,000` gas
   * Example: 100 byte contract costs (100 × 1,000) + 500,000 = 600,000 gas
   * Both CREATE and CREATE2 use the same pricing

4. **Tempo-specific state creation operations:**
   * Nonce key creation: First use of a new nonce key (nonce key > 0) creates storage in Nonce precompile
   * Active key count tracking: First nonce key for an account creates active key count storage
   * Rewards opt-in: `setRewardRecipient` creates new `userRewardInfo` mapping entry
   * Rewards recipient delegation: Setting reward recipient for a new recipient creates storage
   * Rewards balance creation: First reward accrual to a recipient creates storage if needed
   * All Tempo-specific operations that create new state elements must charge 250,000 gas per new storage slot

5. **Edge cases:**
   * Self-destruct and recreation of account
   * Contracts that create accounts via CREATE/CREATE2
   * Batch operations creating multiple accounts/state elements
   * Contract deployment with various code sizes (small, medium, large)
   * Multiple Tempo-specific operations in a single transaction

6. **Economic calculations:**
   * Verify gas costs match expected dollar amounts
   * Verify attack cost calculations for large-scale state creation
   * Verify contract creation costs match formula: `(code_size × 1,000) + 500,000 + 250,000` (including account creation)
   * Verify Tempo-specific operations charge correctly for new state creation

***

# Invariants

The following invariants must always hold:

1. **State Creation Cost Invariant:** Any SSTORE operation that writes a non-zero value to a zero slot MUST charge exactly 250,000 gas (not 20,000 gas).

2. **Account Creation Cost Invariant:** The first transaction that causes an account's nonce to transition from 0 to 1 MUST charge exactly 250,000 gas for account creation.

3. **Existing State Invariant:** SSTORE operations that modify existing non-zero state (non-zero to non-zero) MUST continue to charge 5,000 gas and MUST NOT be affected by this change.

4. **Storage Clearing Invariant:** SSTORE operations that clear storage (non-zero to zero) MUST continue to provide a 15,000 gas refund and MUST NOT be affected by this change.

5. **Gas Accounting Invariant:** The total gas charged for a transaction creating N new state elements and M new accounts (where M is the number of accounts whose nonce transitions from 0 to 1 in this transaction) MUST equal: base\_transaction\_gas + operation\_gas + (N × 250,000) + (M × 250,000). Note: Transferring tokens TO a new address does not create the account (nonce remains 0), so M = 0 in that case.

6. **Contract Creation Cost Invariant:** Contract creation (CREATE/CREATE2) MUST charge exactly `(code_size × 1,000) + 500,000` gas for code storage, replacing the existing EVM per-byte cost. This includes: 1,000 gas per byte of contract code (linear pricing) and 500,000 gas (2 × 250,000) for keccak hash and codesize fields. The account creation cost (250,000 gas) is charged separately.

7. **Economic Deterrent Invariant:** The cost to create 1 TB of state MUST be at least $50 million, and the cost to create 10 TB of state MUST be at least $500 million, based on the assumed gas price of 1 cent per 500,000 gas.

## Critical Test Cases

The test suite must cover:

1. **Basic state creation:** Single SSTORE to zero slot charges 250,000 gas
2. **Multiple state creation:** Multiple SSTORE operations to zero slots each charge 250,000 gas
3. **Account creation (EOA):** First transaction from new EOA charges 250,000 gas
4. **Account creation (CREATE):** Contract deployment via CREATE charges 250,000 gas for account creation
5. **Account creation (CREATE2):** Contract deployment via CREATE2 charges 250,000 gas for account creation
6. **Contract creation (small):** Contract with 100 bytes charges (100 × 1,000) + 500,000 = 600,000 gas for code storage
7. **Contract creation (medium):** Contract with 1,000 bytes charges (1,000 × 1,000) + 500,000 = 1,500,000 gas for code storage
8. **Contract creation (large):** Contract with 10,000 bytes charges (10,000 × 1,000) + 500,000 = 10,500,000 gas for code storage
9. **Existing state updates:** SSTORE to existing non-zero slot charges 5,000 gas (unchanged)
10. **Storage clearing:** SSTORE clearing storage provides 15,000 gas refund (unchanged)
11. **Mixed operations:** Transaction creating both new accounts and new state elements charges correctly for both
12. **Transfer to new address:** Complete transaction cost matches expected ~300,000 gas (no account creation cost, only new state element cost)
13. **First use of new account:** Complete transaction cost matches expected ~300,000 gas (account creation cost applies)
14. **Transfer to existing address:** Complete transaction cost matches expected 50,000 gas (unchanged)
15. **Batch operations:** Multiple account creations in one transaction each charge 250,000 gas
16. **Self-destruct and recreate:** Account that self-destructs and is recreated charges account creation fee again
17. **Transfer to new address does not create account:** Transferring tokens to a new address does not charge account creation fee (only new state element fee applies)
18. **Nonce key creation:** First use of a new nonce key creates a new storage slot and charges 250,000 gas
19. **Active key count tracking:** First nonce key for an account creates storage for active key count and charges 250,000 gas
20. **Rewards opt-in:** First call to `setRewardRecipient` creates a new entry and charges 250,000 gas
21. **Rewards recipient delegation:** Setting a new reward recipient creates storage and charges 250,000 gas
22. **Rewards balance creation:** First reward accrual creates storage and charges 250,000 gas (if needed)
23. **Multiple nonce keys:** Creating multiple nonce keys in one transaction each charges 250,000 gas
24. **Nonce key and rewards combined:** Transaction creating both nonce key and rewards storage charges 250,000 gas for each new state element

# TIP-1001: Place-only mode for next quote token

## Abstract

This TIP adds a `createNextPair` function to the Stablecoin DEX that creates a trading pair between a base token and its `nextQuoteToken()`, along with `place` and `placeFlip` overloads that accept a book key to target specific pairs. This enables market makers to place orders on the new pair before a quote token update is finalized, providing a smooth liquidity transition.

## Motivation

When a token issuer decides to change their quote token (via `setNextQuoteToken` and `completeQuoteTokenUpdate`), there is currently no way to establish liquidity on the new pair before the transition completes. This means that market makers will need to wait until the quote token has been updated before they can place orders, which could cause a period where there is no liquidity, or limited liquidity, for the token, which will interrupt swaps involving that token.

By allowing pair creation against `nextQuoteToken()`, this change allows users and market makers to add liquidity to the DEX before it is used on swaps. Since swaps route through `quoteToken()` (not `nextQuoteToken()`), the new pair operates in "place-only" mode: orders can be placed and cancelled, but no swaps route through it until `completeQuoteTokenUpdate()` is called.

***

# Specification

## New functions

Add the following functions to the Stablecoin DEX interface:

```solidity
/// @notice Creates a trading pair between a base token and its next quote token
/// @param base The base token address
/// @return key The pair key for the created pair
/// @dev Reverts if:
///   - The base token has no next quote token staged (nextQuoteToken is zero)
///   - The pair already exists
///   - Either token is not USD-denominated
function createNextPair(address base) external returns (bytes32 key);

/// @notice Places an order on a specific pair identified by book key
/// @param bookKey The pair key identifying the orderbook
/// @param token The base token of the pair
/// @param amount The order amount in base tokens
/// @param isBid True for buy orders, false for sell orders
/// @param tick The price tick for the order
/// @return orderId The ID of the placed order
function place(bytes32 bookKey, address token, uint128 amount, bool isBid, int16 tick) external returns (uint128 orderId);

/// @notice Places a flip order on a specific pair identified by book key
/// @param bookKey The pair key identifying the orderbook
/// @param token The base token of the pair
/// @param amount The order amount in base tokens
/// @param isBid True for buy orders, false for sell orders
/// @param tick The price tick for the order
/// @param flipTick The price tick for the flipped order when filled
/// @param internalBalanceOnly If true, only use internal balance for the flipped order
/// @return orderId The ID of the placed order
function placeFlip(bytes32 bookKey, address token, uint128 amount, bool isBid, int16 tick, int16 flipTick, bool internalBalanceOnly) external returns (uint128 orderId);
```

## Behavior

### Pair creation

`createNextPair(base)` creates a pair between `base` and `base.nextQuoteToken()`. The function:

1. Calls `nextQuoteToken()` on the base token
2. Reverts with `NO_NEXT_QUOTE_TOKEN` if the result is `address(0)`
3. Validates both tokens are USD-denominated (same as `createPair`)
4. Creates the pair using the same mechanism as `createPair`
5. Emits `PairCreated(key, base, nextQuoteToken)`

### Place-only mode

Once the pair exists, it supports the full order lifecycle:

* `place(bookKey, ...)` and `placeFlip(bookKey, ...)` allow placing orders on the pair
* `cancel` and `cancelStaleOrder` work normally (they use order ID, not pair lookup)
* `books` returns accurate data (it takes the book key directly)

The new `place` and `placeFlip` overloads are required because the existing functions derive the pair from `token.quoteToken()`, which would look up the wrong pair. The overloads accept a `bookKey` parameter to target the correct pair.

Swap functions (`swapExactAmountIn`, `swapExactAmountOut`) and quote functions (`quoteSwapExactAmountIn`, `quoteSwapExactAmountOut`) do not route through this pair because routing uses `quoteToken()` to find paths between tokens.

### After quote token update

When the token issuer calls `completeQuoteTokenUpdate()`:

1. The token's `quoteToken()` changes to what was `nextQuoteToken()`
2. The token's `nextQuoteToken()` becomes `address(0)`
3. The existing pair (created via `createNextPair`) is now the active pair
4. Swaps begin routing through the pair

The old pair (against the previous quote token) remains but will no longer be used for routing swaps involving this base token. Orders on it can be canceled using their ID.

## New error

```solidity
/// @notice The base token has no next quote token staged
error NO_NEXT_QUOTE_TOKEN();
```

## Events

No new events. The existing `PairCreated` event is emitted by `createNextPair`, and the existing `OrderPlaced` event is emitted by the `place` and `placeFlip` overloads.

***

# Invariants

* A pair created via `createNextPair` must be identical to one created via `createPair` once `completeQuoteTokenUpdate` is called
* `createNextPair` must revert if `nextQuoteToken()` returns `address(0)`
* `createNextPair` must revert if the pair already exists (same as `createPair`)
* Orders placed on a next-quote-token pair must be executable via swaps after the quote token update completes
* Swap routing must not change until `completeQuoteTokenUpdate` is called on the base token

# TIP-1002: Prevent crossed orders and allow same-tick flip orders

## Abstract

This TIP makes two related changes to the Stablecoin DEX:

1. **Prevent crossed orders**: Modify `place` and `placeFlip` to reject orders that would cross existing orders on the opposite side of the book. An order "crosses" when a bid is placed at a tick higher than the best ask, or an ask is placed at a tick lower than the best bid.

2. **Allow same-tick flip orders**: Relax the `placeFlip` validation to allow `flipTick` to equal `tick`, enabling flip orders that flip to the same price.

## Motivation

### Preventing crossed orders

Currently, the Stablecoin DEX allows orders to be placed at any valid tick, even if they would cross existing orders. Since matching only occurs during swaps (not during order placement), crossed orders can accumulate in the order book. This is unusual behavior and could confuse market makers who are accustomed to books that do not allow crossing.

By preventing crossed orders at placement time, the order book maintains a clean invariant: `best_bid_tick <= best_ask_tick`.

### Allowing same-tick flip orders

Currently, `placeFlip` requires `flipTick` to be strictly on the opposite side of `tick` (e.g., for a bid, `flipTick > tick`). This prevents use cases like instant token convertibility, where an issuer wants to place flip orders on both sides at the same tick to create a stable two-sided market that automatically replenishes when orders are filled.

***

# Specification

## Modified behavior

The `place` and `placeFlip` functions (including the `bookKey` overloads from TIP-1001) are modified to check for crossing before accepting an order:

* **For bids**: Revert if `tick > best_ask_tick` (when `best_ask_tick` exists)
* **For asks**: Revert if `tick < best_bid_tick` (when `best_bid_tick` exists)

### Same-tick orders

Orders at the same tick as the best order on the opposite side are **allowed**. This means:

* A bid at `tick == best_ask_tick` is allowed
* An ask at `tick == best_bid_tick` is allowed

While this is non-standard behavior for most order books (which would immediately match same-tick orders), it is intentionally permitted to support flip orders that flip to the same tick (see below).

## Same-tick flip orders

The `placeFlip` validation is relaxed to allow `flipTick == tick`:

* **Current behavior**: For bids, `flipTick > tick` required; for asks, `flipTick < tick` required
* **New behavior**: For bids, `flipTick >= tick` required; for asks, `flipTick <= tick` required

This enables use cases like instant token convertibility, where an issuer places flip orders on both sides at the same tick to create a stable two-sided market that automatically replenishes when orders are filled.

## Interaction with TIP-1001

If TIP-1001 is accepted, the crossing check only applies when the pair is **active**—that is, when the pair's quote token equals the base token's current `quoteToken()`.

For pairs created via `createNextPair` (where the quote token is the base token's `nextQuoteToken()`), the crossing check is skipped. This allows orders to accumulate freely during "place-only mode" before the quote token update is finalized. Such orders would likely be arbitraged nearly instantly once the pair launches, but this prevents someone from causing a denial-of-service to one side of the book by placing an extremely aggressive order on the other side.

## New error

```solidity
/// @notice The order would cross existing orders on the opposite side
error ORDER_WOULD_CROSS();
```

## Events

No new events.

***

# Invariants

* On active pairs, `best_bid_tick <= best_ask_tick` after any successful `place` or `placeFlip` call
* On inactive pairs (per TIP-1001), no crossing check is enforced
* Flip orders may create orders at the same tick as the opposite side, potentially resulting in `best_bid_tick == best_ask_tick`

# TIP-1003: Client order IDs

## Abstract

This TIP adds support for optional client order IDs (`clientOrderId`) to the Stablecoin DEX. Users can specify a `uint128` identifier when placing orders, which serves as an idempotency key and a predictable handle for the order. The system-generated `orderId` is not predictable before transaction execution, making client order IDs useful for order management.

## Motivation

Traditional exchanges allow users to specify a client order ID (called `ClOrdID` in FIX protocol, `cloid` in Hyperliquid) for several reasons:

1. **Idempotency**: If a transaction is submitted twice (e.g., due to network issues), the duplicate can be detected and rejected
2. **Predictable reference**: Users know the order identifier before the transaction confirms, enabling them to prepare cancel requests or track orders without waiting for confirmation
3. **Integration**: External systems can use their own ID schemes to correlate orders

***

# Specification

## New storage

A new mapping tracks active client order IDs per user:

```solidity
mapping(address user => mapping(uint128 clientOrderId => uint128 orderId)) public clientOrderIds;
```

## Modified functions

All order placement functions gain an optional `clientOrderId` parameter:

```solidity
/// @notice Places an order with an optional client order ID
/// @param token The base token of the pair
/// @param amount The order amount in base tokens
/// @param isBid True for buy orders, false for sell orders
/// @param tick The price tick for the order
/// @param clientOrderId Optional client-specified ID (0 for none)
/// @return orderId The system-assigned order ID
function place(
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    uint128 clientOrderId
) external returns (uint128 orderId);

/// @notice Places an order on a specific pair with an optional client order ID
/// @dev Overload from TIP-1001
function place(
    bytes32 bookKey,
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    uint128 clientOrderId
) external returns (uint128 orderId);

/// @notice Places a flip order with an optional client order ID
function placeFlip(
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    int16 flipTick,
    bool internalBalanceOnly,
    uint128 clientOrderId
) external returns (uint128 orderId);

/// @notice Places a flip order on a specific pair with an optional client order ID
/// @dev Overload from TIP-1001
function placeFlip(
    bytes32 bookKey,
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    int16 flipTick,
    bool internalBalanceOnly,
    uint128 clientOrderId
) external returns (uint128 orderId);
```

## New functions

```solidity
/// @notice Cancels an order by its client order ID
/// @param clientOrderId The client-specified order ID
function cancelByClientOrderId(uint128 clientOrderId) external;

/// @notice Gets the system order ID for a client order ID
/// @param user The user who placed the order
/// @param clientOrderId The client-specified order ID
/// @return orderId The system-assigned order ID, or 0 if not found
function getOrderByClientOrderId(address user, uint128 clientOrderId) external view returns (uint128 orderId);
```

## Behavior

### Placing orders with clientOrderId

When `clientOrderId` is non-zero:

1. Check if `clientOrderIds[msg.sender][clientOrderId]` maps to an active order
2. If it does, revert with `DUPLICATE_CLIENT_ORDER_ID`
3. Otherwise, proceed with order placement and set `clientOrderIds[msg.sender][clientOrderId] = orderId`

When `clientOrderId` is zero, no client order ID tracking occurs.

### Uniqueness and reuse

A `clientOrderId` must be unique among a user's **active orders**. Once an order is filled or cancelled, its `clientOrderId` can be reused. This matches the standard FIX protocol behavior where `ClOrdID` uniqueness is required only for working orders.

When an order reaches a terminal state (filled or cancelled), the `clientOrderIds` mapping entry is cleared.

### Flip orders

When a flip order is filled and creates a new order on the opposite side:

1. The new (flipped) order inherits the original order's `clientOrderId`
2. The `clientOrderIds` mapping is updated to point to the new order ID
3. This allows users to track their position across flips using a single `clientOrderId`

If the original order had no `clientOrderId` (was zero), the flipped order also has no `clientOrderId`.

### Cancellation

`cancelByClientOrderId(clientOrderId)` looks up `clientOrderIds[msg.sender][clientOrderId]` and cancels that order. It reverts if no active order exists for that `clientOrderId`.

## New event

```solidity
/// @notice Emitted when an order is placed (V2 with clientOrderId)
/// @dev Replaces OrderPlaced for new orders
event OrderPlacedV2(
    uint128 indexed orderId,
    address indexed maker,
    address token,
    uint128 amount,
    bool isBid,
    int16 tick,
    bool isFlipOrder,
    int16 flipTick,
    uint128 clientOrderId
);
```

`OrderPlacedV2` is identical to `OrderPlaced` but adds the `clientOrderId` field. When an order is placed, only `OrderPlacedV2` is emitted (not both events).

## New errors

```solidity
/// @notice The client order ID is already in use by an active order
error DUPLICATE_CLIENT_ORDER_ID();

/// @notice No active order found for the given client order ID
error CLIENT_ORDER_ID_NOT_FOUND();
```

***

# Invariants

* A non-zero `clientOrderId` maps to at most one active order per user
* `clientOrderIds[user][clientOrderId]` is cleared when the order is filled or cancelled
* Flip orders inherit `clientOrderId` and update the mapping atomically
* `clientOrderId = 0` is reserved to mean "no client order ID"

# TIP-1004: Permit for TIP-20

## Abstract

TIP-1004 adds EIP-2612 compatible `permit()` functionality to TIP-20 tokens, enabling gasless approvals via off-chain signatures. This allows users to approve token spending without submitting an on-chain transaction, with the approval being executed by any third party who submits the signed permit.

## Motivation

The standard ERC-20 approval flow requires users to submit a transaction to approve a spender before that spender can transfer tokens on their behalf. Among other things, this makes it difficult for a transaction to "sweep" tokens from multiple addresses that have never sent a transaction onchain.

EIP-2612 introduced the `permit()` function which allows approvals to be granted via a signed message rather than an on-chain transaction. This enables:

* **Gasless approvals**: Users can sign a permit off-chain, and a relayer or the spender can submit the transaction
* **Single-transaction flows**: DApps can batch the permit with the subsequent action (e.g., approve + swap) in one transaction
* **Improved UX**: Users don't need to wait for or pay for a separate approval transaction

Since TIP-20 aims to be a superset of ERC-20 with additional functionality, adding EIP-2612 permit support ensures TIP-20 tokens work seamlessly with existing DeFi protocols and tooling that expect permit functionality.

### Alternatives

While Tempo transactions provide solutions for most of the common problems that are solved by account abstraction, they do not provide a way to transfer tokens from an address that has never sent a transaction onchain, which means it does not provide an easy way for a batched transaction to "sweep" tokens from many addresses.

While we plan to have Permit2 deployed on the chain, it, too, requires an initial transaction from the address being transferred from.

Adding a function for `transferWithAuthorization`, which we are also considering, would also solve this problem. But `permit` is somewhat more flexible, and we think these functions are not mutually exclusive.

***

# Specification

## New functions

The following functions are added to the TIP-20 interface:

```solidity
interface ITIP20Permit {
    /// @notice Approves `spender` to spend `value` tokens on behalf of `owner` via a signed permit
    /// @param owner The address granting the approval
    /// @param spender The address being approved to spend tokens
    /// @param value The amount of tokens to approve
    /// @param deadline Unix timestamp after which the permit is no longer valid
    /// @param v The recovery byte of the signature
    /// @param r Half of the ECDSA signature pair
    /// @param s Half of the ECDSA signature pair
    /// @dev The permit is valid only if:
    ///      - The current block timestamp is <= deadline
    ///      - The signature is valid and was signed by `owner`
    ///      - The nonce in the signature matches the current nonce for `owner`
    ///      Upon successful execution, increments the nonce for `owner` by 1.
    ///      Emits an {Approval} event.
    function permit(
        address owner,
        address spender,
        uint256 value,
        uint256 deadline,
        uint8 v,
        bytes32 r,
        bytes32 s
    ) external;

    /// @notice Returns the current nonce for an address
    /// @param owner The address to query
    /// @return The current nonce, which must be included in any permit signature for this owner
    /// @dev The nonce starts at 0 and increments by 1 each time a permit is successfully used
    function nonces(address owner) external view returns (uint256);

    /// @notice Returns the EIP-712 domain separator for this token
    /// @return The domain separator bytes32 value
    /// @dev The domain separator is computed dynamically on each call as:
    ///      keccak256(abi.encode(
    ///          keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"),
    ///          keccak256(bytes(name())),
    ///          keccak256(bytes("1")),
    ///          block.chainid,
    ///          address(this)
    ///      ))
    ///      Dynamic computation ensures correct behavior after chain forks where chainId changes.
    function DOMAIN_SEPARATOR() external view returns (bytes32);
}
```

## EIP-712 Typed Data

The permit signature must conform to EIP-712 typed structured data signing. The domain and message types are defined as follows:

### Domain Separator

The domain separator is computed using the following parameters:

| Parameter | Value |
|-----------|-------|
| name | The token's `name()` |
| version | `"1"` |
| chainId | The chain ID where the token is deployed |
| verifyingContract | The TIP-20 token contract address |

```solidity
bytes32 DOMAIN_SEPARATOR = keccak256(abi.encode(
    keccak256("EIP712Domain(string name,string version,uint256 chainId,address verifyingContract)"),
    keccak256(bytes(name())),
    keccak256(bytes("1")),
    block.chainid,
    address(this)
));
```

### Permit Typehash

The permit message type is:

```solidity
bytes32 constant PERMIT_TYPEHASH = keccak256(
    "Permit(address owner,address spender,uint256 value,uint256 nonce,uint256 deadline)"
);
```

### Signature Construction

To create a valid permit signature, the signer must sign the following EIP-712 digest:

```solidity
bytes32 structHash = keccak256(abi.encode(
    PERMIT_TYPEHASH,
    owner,
    spender,
    value,
    nonces[owner],
    deadline
));

bytes32 digest = keccak256(abi.encodePacked(
    "\x19\x01",
    DOMAIN_SEPARATOR,
    structHash
));
```

The signature `(v, r, s)` must be produced by signing `digest` with the private key of `owner`.

## Behavior

### Nonces

Each address has an associated nonce that:

* Starts at `0` for all addresses
* Increments by `1` each time a permit is successfully executed for that address
* Must be included in the permit signature to prevent replay attacks

### Deadline

The `deadline` parameter is a Unix timestamp. The permit is only valid if `block.timestamp <= deadline`. This allows signers to limit the validity window of their permits.

### Pause State

The `permit()` function follows the same pause behavior as `approve()`. Since setting an allowance does not move tokens, `permit()` is allowed to execute even when the token is paused.

### TIP-403 Transfer Policy

The `permit()` function does not perform TIP-403 authorization checks, consistent with the behavior of `approve()`. Transfer policy checks are only enforced when tokens are actually transferred.

### Signature Validation

The implementation must:

1. Verify that `block.timestamp <= deadline`, otherwise revert with `PermitExpired`
2. Retrieve the current nonce for `owner` and use it to construct the `structHash` and `digest`
3. Increment `nonces[owner]`
4. Validate the signature:
   * The `v` parameter must be `27` or `28`. Values of `0` or `1` are **not** normalized and will revert with `InvalidSignature`. Callers using signing libraries that produce `v ∈ {0, 1}` must add `27` before calling `permit`.
   * Use `ecrecover` to recover a signer address from the digest
   * If `ecrecover` returns a non-zero address that equals `owner`, the signature is valid (EOA case)
   * Otherwise, revert with `InvalidSignature`
5. Set `allowance[owner][spender] = value`
6. Emit an `Approval(owner, spender, value)` event

\> **Note**: The nonce is included in the signed digest, so nonce verification is implicit in signature validation — if the wrong nonce was signed, `ecrecover` will return a different address.

## New errors

```solidity
/// @notice The permit signature has expired (block.timestamp > deadline)
error PermitExpired();

/// @notice The permit signature is invalid (wrong signer, malformed, or zero address recovered)
error InvalidSignature();
```

## New events

None. Successful permit execution emits the existing `Approval` event from TIP-20.

***

# Invariants

* `nonces(owner)` must only ever increase, never decrease
* `nonces(owner)` must increment by exactly 1 on each successful `permit()` call for that owner
* A permit signature can only be used once (enforced by nonce increment)
* A permit with a deadline in the past must always revert
* The recovered signer from a valid permit signature must exactly match the `owner` parameter
* After a successful `permit(owner, spender, value, ...)`, `allowance(owner, spender)` must equal `value`
* `DOMAIN_SEPARATOR()` must be computed dynamically and reflect the current `block.chainid`

## Test Cases

The test suite must cover:

1. **Happy path**: Valid permit sets allowance correctly
2. **Expired permit**: Reverts with `PermitExpired` when `deadline < block.timestamp`
3. **Invalid signature**: Reverts with `InvalidSignature` for malformed signatures
4. **Wrong signer**: Reverts with `InvalidSignature` when signature is valid but signer ≠ owner
5. **Replay protection**: Second use of same signature reverts (nonce already incremented)
6. **Nonce tracking**: Verify nonce increments correctly after each permit
7. **Zero address recovery**: Reverts with `InvalidSignature` if ecrecover returns zero address
8. **Pause state**: Permit works when token is paused
9. **Domain separator**: Verify correct EIP-712 domain separator computation
10. **Domain separator chain ID**: Verify domain separator changes if chain ID changes
11. **Max allowance**: Permit with `type(uint256).max` value works correctly
12. **Allowance override**: Permit can override existing allowance (including to zero)

# TIP-1005: Fix ask swap rounding loss

## Abstract

This TIP fixes a rounding bug in the `swapExactAmountIn` function when filling ask orders. Due to double-rounding, the maker can receive slightly less quote tokens than the taker paid, causing tokens to be lost.

## Motivation

When a taker swaps quote tokens for base tokens against an ask order, the following calculation occurs:

1. Convert taker's `amountIn` (quote) to base: `base_out = floor(amountIn / price)`
2. Credit maker with quote: `makerReceives = ceil(base_out * price)`

Due to the floor in step 1, `makerReceives` can be less than `amountIn`. For example:

* Taker pays `amountIn = 102001` quote at price 1.02 (tick 2000)
* `base_out = floor(102001 / 1.02) = 100000`
* `makerReceives = ceil(100000 * 1.02) = 102000`
* **1 token is lost**

This violates the zero-sum invariant: the taker pays more than the maker receives. It also means there is no canonical amount swapped—the trade for the maker is different from the trade for the taker.

***

# Specification

## Bug location

The bug is in `_fillOrdersExactIn` when processing ask orders (the `baseForQuote = false` path). Specifically, when a partial fill occurs:

1. `fillAmount` (base) is calculated by rounding down: `baseOut = (remainingIn * PRICE_SCALE) / price`
2. `_fillOrder` is called with `fillAmount`
3. Inside `_fillOrder`, the maker's quote credit is re-derived: `quoteAmount = ceil(fillAmount * price)`

The re-derivation in step 3 loses the original `remainingIn` information.

## Fix

For partial fills in the ask path, pass the actual `remainingIn` (quote) to `_fillOrder` and use it directly for the maker's credit, rather than re-deriving it from `fillAmount`.

The fix requires:

1. Modify `_fillOrder` to accept an optional `quoteOverride` parameter for ask orders
2. In `_fillOrdersExactIn`, when partially filling an ask, pass `remainingIn` as the quote override
3. When `quoteOverride` is provided, use it directly for the maker's balance increment instead of computing `ceil(fillAmount * price)`

## Reference implementation changes

The fix requires changes to two functions in [`docs/specs/src/StablecoinDEX.sol`](https://github.com/tempoxyz/tempo/blob/main/docs/specs/src/StablecoinDEX.sol):

### 1. `_fillOrder` ([line 551-556](https://github.com/tempoxyz/tempo/blob/main/docs/specs/src/StablecoinDEX.sol#L551-L556))

Add an optional `quoteOverride` parameter. When non-zero and the order is an ask, use `quoteOverride` directly for the maker's balance increment instead of computing `ceil(fillAmount * price)`.

```solidity
// Before:
uint128 quoteAmount =
    uint128((uint256(fillAmount) * uint256(price) + PRICE_SCALE - 1) / PRICE_SCALE);
balances[order.maker][book.quote] += quoteAmount;

// After:
uint128 quoteAmount = quoteOverride > 0
    ? quoteOverride
    : uint128((uint256(fillAmount) * uint256(price) + PRICE_SCALE - 1) / PRICE_SCALE);
balances[order.maker][book.quote] += quoteAmount;
```

### 2. `_fillOrdersExactIn` ([line 923-926](https://github.com/tempoxyz/tempo/blob/main/docs/specs/src/StablecoinDEX.sol#L923-L926))

In the partial fill branch for asks, pass `remainingIn` as the quote override:

```solidity
// Before:
orderId = _fillOrder(orderId, fillAmount);

// After (for partial fills where fillAmount == baseOut):
orderId = _fillOrder(orderId, fillAmount, remainingIn);
```

## Affected code paths

* `_fillOrdersExactIn` with `baseForQuote = false` (ask path), partial fill case only
* Full fills are not affected because the quote amount is derived from `order.remaining`, not `remainingIn`
* Bid swaps are not affected because the taker pays base tokens directly

## Example: Before and after

**Before (buggy):**

```
amountIn = 102001 quote
base_out = floor(102001 / 1.02) = 100000
makerReceives = ceil(100000 * 1.02) = 102000
Lost: 1 token
```

**After (fixed):**

```
amountIn = 102001 quote
base_out = floor(102001 / 1.02) = 100000
makerReceives = 102001 (passed directly)
Lost: 0 tokens
```

***

# Invariants

* Zero-sum: for any swap, `takerPaid == makerReceived` (within the same token)
* Taker receives `floor(amountIn / price)` base tokens (rounds in favor of protocol)
* Maker receives exactly what taker paid in quote tokens

# TIP-1006: Burn At for TIP-20 Tokens

## Abstract

This specification introduces a `burnAt` function to TIP-20 tokens, allowing holders of a new `BURN_AT_ROLE` to burn tokens from any address without transfer policy restrictions. This complements the existing `burnBlocked` function which is limited to burning from addresses blocked by the transfer policy.

## Motivation

The existing TIP-20 burn mechanisms have the following limitations:

1. `burn()` - Only burns from the caller's own balance, requires `ISSUER_ROLE`
2. `burnBlocked()` - Can burn from other addresses, but only if the target address is blocked by the transfer policy

There are legitimate use cases where token administrators may want a privileged caller to have the ability to burn tokens from any address regardless of their policy status, such as allowing a bridge contract to burn tokens that are being bridged out without requiring approval (as in the `crosschainBurn` function proposed in [ERC 7802](https://github.com/ethereum/ERCs/blob/master/ERCS/erc-7802.md)).

The `burnAt` function provides this capability with appropriate access controls via a dedicated role.

***

# Specification

## New Role

A new role constant is added to TIP-20:

```solidity
bytes32 public constant BURN_AT_ROLE = keccak256("BURN_AT_ROLE");
```

This role is administered by the `DEFAULT_ADMIN_ROLE` (same as other TIP-20 roles).

## New Event

```solidity
/// @notice Emitted when tokens are burned from any account.
/// @param from The address from which tokens were burned.
/// @param amount The amount of tokens burned.
event BurnAt(address indexed from, uint256 amount);
```

## New Function

```solidity
/// @notice Burns tokens from any account.
/// @dev Requires BURN_AT_ROLE. Cannot burn from protected precompile addresses.
/// @param from The address to burn tokens from.
/// @param amount The amount of tokens to burn.
function burnAt(address from, uint256 amount) external;
```

### Behavior

1. **Access Control**: Reverts with `Unauthorized` if caller does not have `BURN_AT_ROLE`
2. **Protected Addresses**: Reverts with `ProtectedAddress` if `from` is:
   * `TIP_FEE_MANAGER_ADDRESS` (0xfeEC000000000000000000000000000000000000)
   * `STABLECOIN_DEX_ADDRESS` (0xDEc0000000000000000000000000000000000000)
3. **Balance Check**: Reverts with `InsufficientBalance` if `from` has insufficient balance
4. **No Policy Check**: Unlike `burnBlocked`, this function does NOT check transfer policy authorization
5. **State Changes**:
   * Decrements `balanceOf[from]` by `amount`
   * Decrements `_totalSupply` by `amount`
   * Updates reward accounting if `from` is opted into rewards
6. **Events**: Emits `Transfer(from, address(0), amount)` and `BurnAt(from, amount)`

### Interface Addition

The `ITIP20` interface is extended with:

```solidity
/// @notice Returns the role identifier for burning tokens from any account.
/// @return The burn-at role identifier.
function BURN_AT_ROLE() external view returns (bytes32);

/// @notice Burns tokens from any account.
/// @param from The address to burn tokens from.
/// @param amount The amount of tokens to burn.
function burnAt(address from, uint256 amount) external;
```

# Invariants

1. **Role Required**: `burnAt` must always revert if caller lacks `BURN_AT_ROLE`
2. **Protected Addresses**: `burnAt` must never succeed when `from` is a protected precompile address
3. **Supply Conservation**: After `burnAt(from, amount)`:
   * `totalSupply` decreases by exactly `amount`
   * `balanceOf[from]` decreases by exactly `amount`
4. **Balance Constraint**: `burnAt` must revert if `amount > balanceOf[from]`
5. **Reward Accounting**: If `from` is opted into rewards:
   * Pending rewards must be accrued to the reward recipient's `rewardBalance` before the balance changes
   * `from`'s `rewardPerToken` snapshot must be synced to `globalRewardPerToken`
   * `optedInSupply` must decrease by `amount`
   * Any previously accrued `rewardBalance` remains claimable
6. **Policy Independence**: `burnAt` must succeed regardless of transfer policy status of `from`

## Test Cases

The test suite must verify:

1. Successful burn with `BURN_AT_ROLE`
2. Revert without `BURN_AT_ROLE` (Unauthorized)
3. Revert when burning from `TIP_FEE_MANAGER_ADDRESS` (ProtectedAddress)
4. Revert when burning from `STABLECOIN_DEX_ADDRESS` (ProtectedAddress)
5. Successful burn from policy-blocked address (same behavior as `burnBlocked`)
6. Successful burn from policy-authorized address (differs from `burnBlocked`, which reverts)
7. Revert on insufficient balance
8. Correct event emissions (`Transfer` and `BurnAt`)
9. Correct reward accounting updates (pending rewards accrued before burn, `rewardBalance` remains claimable)

# TIP-1007: Fee Token Introspection

## Abstract

TIP-1007 adds a `getFeeToken()` view function to the FeeManager precompile that returns the fee token address being used for the current transaction. This enables smart contracts to introspect which TIP-20 token is paying for gas fees during execution, allowing for dynamic logic based on the fee token choice.

## Motivation

Tempo transactions support paying gas fees in any USD-denominated TIP-20 token via the fee token preference system. However, prior to this TIP, there was no way for a smart contract to determine which fee token is being used for the current transaction during execution.

This capability was requested by a partner. It could be useful for contracts that want to:

* Adjust their internal logic based on which fee token is being used
* Provide fee token-aware pricing or routing decisions
* Emit events or logs that include the fee token for off-chain indexing
* Implement fee token-specific behavior in cross-chain messaging

***

# Specification

## New Function

The following function is added to the `IFeeManager` interface:

```solidity
interface IFeeManager {
    // ... existing functions ...

    /// @notice Returns the fee token being used for the current transaction
    /// @return The address of the TIP-20 token paying for gas fees
    /// @dev This value is set by the protocol before transaction execution begins.
    ///      Returns address(0) if no fee token has been set (e.g., in eth_call
    ///      simulations where the transaction handler does not run).
    function getFeeToken() external view returns (address);
}
```

## Behavior

### Fee Token Resolution

The fee token returned by `getFeeToken()` is the same token that was resolved by the protocol during transaction validation, following the [fee token preference rules](/protocol/fees/spec-fee#fee-token-resolution).

### Storage

The fee token is stored in **transient storage** (EIP-1153) within the FeeManager precompile. This means:

* The value is automatically cleared at the end of each transaction
* No persistent storage writes occur, minimizing gas costs
* The value is consistent across all calls within a transaction (including internal calls and subcalls)

### Timing

The fee token is set by the protocol in the `validate_against_state_and_deduct_caller` handler phase, before any user code executes. This ensures the value is available throughout the entire transaction execution.

### Gas Cost

Reading the fee token costs the standard warm transient storage read cost (100 gas for TLOAD). This is the cost of calling `getFeeToken()` itself; callers should account for additional gas used by the CALL opcode to invoke the precompile.

### Edge Cases

| Scenario | Return Value |
|----------|--------------|
| Normal transaction | The resolved fee token address |
| Free transaction (zero gas price) | The resolved fee token (may still be set) |
| `eth_call` simulation | `address(0)` (no transaction context) |

The only case where `address(0)` is returned is in simulation contexts (e.g., `eth_call`) where the protocol handler does not execute.

## Example Usage

```solidity
import { IFeeManager } from "./interfaces/IFeeManager.sol";

contract FeeTokenAware {
    IFeeManager constant FEE_MANAGER = IFeeManager(0xfeeC000000000000000000000000000000000000);
    address constant PATH_USD = 0x20C0000000000000000000000000000000000000;

    function doSomething() external {
        address feeToken = FEE_MANAGER.getFeeToken();

        if (feeToken == PATH_USD) {
            // User is paying fees in pathUSD
        } else if (feeToken != address(0)) {
            // User is paying fees in a different USD stablecoin
        } else {
            // No fee token context (e.g., eth_call simulation)
        }
    }
}
```

## Interface Addition

The following function is added to `IFeeManager`:

```solidity
/// @notice Returns the fee token being used for the current transaction
/// @return The address of the TIP-20 token paying for gas fees
function getFeeToken() external view returns (address);
```

***

# Invariants

* `getFeeToken()` must return a consistent value across all calls within the same transaction
* `getFeeToken()` must return `address(0)` in simulation contexts (e.g., `eth_call`) where no transaction handler runs
* `getFeeToken()` must be callable from `staticcall` contexts without reverting
* The fee token returned must match the token used for actual fee deduction in `collectFeePreTx` and `collectFeePostTx`
* Reading the fee token must not modify any state (view function)

## Test Cases

The test suite must cover:

1. **Basic functionality**: `getFeeToken()` returns the correct fee token address
2. **Zero when unset**: Returns `address(0)` when no fee token is set
3. **Consistency**: Same value returned from nested calls within a transaction
4. **Static call safety**: Works correctly when called via `staticcall`
5. **Transient storage**: Value is cleared between transactions
6. **Different fee tokens**: Works with various TIP-20 fee tokens (pathUSD, USDC, etc.)
7. **Dispatch coverage**: Function selector is correctly dispatched by the precompile

# TIP-1009: Expiring Nonces

## Abstract

TIP-1009 introduces expiring nonces, an alternative replay protection mechanism where transactions are valid only within a specified time window. Instead of tracking sequential nonces, the protocol uses transaction hashes with expiry timestamps to prevent replay attacks. This enables use cases like gasless transactions, meta-transactions, and simplified UX where users don't need to manage nonce ordering.

## Motivation

Traditional sequential nonces require careful ordering—if transaction N fails or is delayed, all subsequent transactions (N+1, N+2, ...) are blocked. This creates friction for:

1. **Gasless/Meta-transactions**: Relayers need complex nonce management across multiple users
2. **Parallel submission**: Users cannot submit multiple independent transactions simultaneously
3. **Recovery from failures**: Stuck transactions require explicit cancellation with the same nonce

Expiring nonces solve these problems by using time-based validity instead of sequence-based ordering. Each transaction is uniquely identified by its hash and is valid only until a specified `validBefore` timestamp.

***

# Specification

## Nonce Key

Expiring nonce transactions use a reserved nonce key:

```
TEMPO_EXPIRING_NONCE_KEY = uint256.max (2^256 - 1)
```

When a Tempo transaction specifies `nonceKey = uint256.max`, the protocol treats it as an expiring nonce transaction.

## Transaction Fields

Expiring nonce transactions require:

| Field | Type | Description |
|-------|------|-------------|
| `nonceKey` | `uint256` | Must be `uint256.max` to indicate expiring nonce mode |
| `nonce` | `uint64` | Must be `0` (unused, validated for consistency) |
| `validBefore` | `uint64` | Unix timestamp (seconds) after which the transaction is invalid |

## Validity Window

The `validBefore` timestamp must satisfy:

```
now < validBefore <= now + MAX_EXPIRY_SECS
```

Where:

* `now` is the current block timestamp
* `MAX_EXPIRY_SECS = 30` seconds

Transactions with `validBefore` in the past or more than 30 seconds in the future are rejected.

## Replay Protection

Replay protection uses a **circular buffer** data structure in the Nonce precompile:

### Storage Layout

```solidity
contract Nonce {
    // Existing 2D nonce storage
    mapping(address => mapping(uint256 => uint64)) public nonces;           // slot 0

    // Expiring nonce storage
    mapping(bytes32 => uint64) public expiringNonceSeen;                    // slot 1: txHash => expiry
    mapping(uint32 => bytes32) public expiringNonceRing;                    // slot 2: circular buffer
    uint32 public expiringNonceRingPtr;                                     // slot 3: buffer pointer
}
```

### Circular Buffer Design

The circular buffer has a fixed capacity:

```
EXPIRING_NONCE_SET_CAPACITY = 300,000
```

This capacity is sized for 10,000 TPS × 30 seconds = 300,000 transactions, ensuring entries expire before being overwritten.

### Algorithm

When processing an expiring nonce transaction:

1. **Validate expiry window**: Reject if `validBefore <= now` or `validBefore > now + 30`

2. **Replay check**: Read `expiringNonceSeen[txHash]`
   * If entry exists and `expiry > now`, reject as replay

3. **Get buffer position**: Read `expiringNonceRingPtr`, compute `idx = ptr % CAPACITY`

4. **Read existing entry**: Read `expiringNonceRing[idx]` to get `oldHash`

5. **Eviction check** (safety): If `oldHash != 0`:
   * Read `expiringNonceSeen[oldHash]`
   * If `expiry > now`, reject (buffer full of valid entries)
   * Clear `expiringNonceSeen[oldHash] = 0`

6. **Insert new entry**:
   * Write `expiringNonceRing[idx] = txHash`
   * Write `expiringNonceSeen[txHash] = validBefore`

7. **Advance pointer**: Write `expiringNonceRingPtr = ptr + 1`

### Pseudocode

```solidity
function checkAndMarkExpiringNonce(
    bytes32 txHash,
    uint64 validBefore,
    uint64 now
) internal {
    // 1. Validate expiry window
    require(validBefore > now && validBefore <= now + 30, "InvalidExpiry");

    // 2. Replay check
    uint64 seenExpiry = expiringNonceSeen[txHash];
    require(seenExpiry == 0 || seenExpiry <= now, "Replay");

    // 3-4. Get buffer position and existing entry
    uint32 ptr = expiringNonceRingPtr;
    uint32 idx = ptr % CAPACITY;
    bytes32 oldHash = expiringNonceRing[idx];

    // 5. Eviction check (safety)
    if (oldHash != bytes32(0)) {
        uint64 oldExpiry = expiringNonceSeen[oldHash];
        require(oldExpiry == 0 || oldExpiry <= now, "BufferFull");
        expiringNonceSeen[oldHash] = 0;
    }

    // 6. Insert new entry
    expiringNonceRing[idx] = txHash;
    expiringNonceSeen[txHash] = validBefore;

    // 7. Advance pointer
    expiringNonceRingPtr = ptr + 1;
}
```

## Gas Costs

The intrinsic gas cost for expiring nonce transactions includes:

```
EXPIRING_NONCE_GAS = 2 * COLD_SLOAD_COST + WARM_SLOAD_COST + 3 * WARM_SSTORE_RESET
                   = 2 * 2100 + 100 + 3 * 2900
                   = 13,000 gas
```

**Included operations:**

* 2 cold SLOADs: `seen[txHash]`, `ring[idx]` (unique slots per tx)
* 1 warm SLOAD: `seen[oldHash]` (warm because we just read `ring[idx]` which points to it)
* 3 SSTOREs at RESET price: `seen[oldHash]=0`, `ring[idx]`, `seen[txHash]`

**Excluded operations (amortized):**

* `ring_ptr` SLOAD/SSTORE: Accessed by almost every expiring nonce tx in a block, so amortized cost approaches ~200 gas. May be moved out of EVM storage in the future.

**Why SSTORE\_RESET (2,900) instead of SSTORE\_SET (20,000) for `seen[txHash]`:**

* SSTORE\_SET cost exists to penalize permanent state growth
* Expiring nonce data is ephemeral: evicted within 30 seconds, fixed-size buffer (300k entries)
* No permanent state growth, so the 20k penalty doesn't apply

## Transaction Pool Validation

The transaction pool performs preliminary validation:

1. Verify `nonceKey == uint256.max`
2. Verify `nonce == 0`
3. Verify `validBefore` is present
4. Verify `validBefore > currentTime` (not expired)
5. Verify `validBefore <= currentTime + MAX_EXPIRY_SECS` (within window)
6. Query `expiringNonceSeen[txHash]` storage slot to check for existing entry

Transactions failing these checks are rejected before entering the pool.

## Interaction with Other Features

### 2D Nonces

Expiring nonces and 2D nonces are mutually exclusive:

* `nonceKey = 0`: Protocol nonce (standard sequential)
* `nonceKey = 1..uint256.max-1`: 2D nonce keys
* `nonceKey = uint256.max`: Expiring nonce mode

### Access Keys (Keychain)

Expiring nonces work with access key signatures. The `validBefore` provides an additional security boundary—even if an access key is compromised, transactions signed with it become invalid after the expiry window.

### Fee Tokens

Expiring nonce transactions pay fees in TIP-20 fee tokens like any other Tempo transaction.

***

# Invariants

## Must Hold

| ID | Invariant | Description |
|----|-----------|-------------|
| **E1** | No replay | A transaction hash can never be executed twice (changing `validBefore` produces a different hash) |
| **E2** | Expiry enforcement | Transactions with `validBefore <= now` must be rejected |
| **E3** | Window bounds | Transactions with `validBefore > now + MAX_EXPIRY_SECS` must be rejected |
| **E4** | Nonce must be zero | Expiring nonce transactions must have `nonce == 0` |
| **E5** | Valid before required | Expiring nonce transactions must have `validBefore` set |
| **E6** | No nonce mutation | Expiring nonce txs do not increment protocol nonce or any 2D nonce |
| **E7** | Concurrent independence | Multiple expiring nonce txs from same sender can execute in same block |

## Invariant Tests

These invariants are tested in the Foundry invariant test suite (`TempoTransactionInvariant.t.sol`):

| Handler | Tests | Description |
|---------|-------|-------------|
| `handler_expiringNonceBasic` | Basic flow | Execute valid expiring nonce tx |
| `handler_expiringNonceReplay` | E1 | Replay must be rejected |
| `handler_expiringNonceExpired` | E2 | Tx with `validBefore <= now` must be rejected |
| `handler_expiringNonceWindowTooFar` | E3 | Tx with `validBefore > now + 30s` must be rejected |
| `handler_expiringNonceNonZeroNonce` | E4 | Tx with `nonce != 0` must be rejected |
| `handler_expiringNonceMissingValidBefore` | E5 | Tx without `validBefore` must be rejected |
| `handler_expiringNonceNoNonceMutation` | E6 | Protocol and 2D nonces unchanged after execution |
| `handler_expiringNonceConcurrent` | E7 | Multiple concurrent txs from same sender succeed |

## Test Cases

1. **Basic flow**: Submit transaction, verify execution, attempt replay (should fail)

2. **Expiry validation**:
   * `validBefore` in past → reject
   * `validBefore = now` → reject
   * `validBefore = now + 31` → reject
   * `validBefore = now + 30` → accept

3. **Nonce validation**:
   * `nonce = 0` → accept
   * `nonce > 0` → reject

4. **Required fields**:
   * `validBefore` missing → reject
   * `nonceKey != uint256.max` → not expiring nonce (uses 2D nonce rules)

5. **Post-expiry replay**: Submit tx, wait for expiry, submit same tx with new `validBefore` (should succeed)

6. **Buffer eviction**: Fill buffer, verify old entries are evicted when expired

7. **Concurrent transactions**: Submit multiple transactions with same `validBefore`, verify all succeed

***

# Benchmark Results

Benchmarks were run to measure state savings from expiring nonces compared to 2D nonces.

## Key Findings

| Metric | Value |
|--------|-------|
| Per-transaction state savings | ~100 bytes |
| Circular buffer capacity | 300,000 entries |
| Buffer fills at 5k TPS | ~60 seconds |

## Controlled Benchmark (100k transactions at 5k TPS)

| Nonce Type | Final DB Size | Transactions |
|------------|---------------|--------------|
| 2D Nonces | 4,342.85 MB | 100,000 |
| Expiring Nonces | 4,332.18 MB | 100,000 |
| **Difference** | **-10.67 MB** | - |

The ~107 bytes per transaction overhead includes MPT node overhead, MDBX metadata, and RLP encoding.

## Scaling Projections

| TPS | Daily Transactions | Daily State Savings |
|-----|-------------------|---------------------|
| 5,000 | 432M | 43.2 GB |
| 10,000 | 864M | 86.4 GB |

After the circular buffer fills, expiring nonces maintain constant storage while 2D nonces grow by ~100 bytes per transaction.

***

# Open Questions

## Safety Check for Buffer Eviction

The current implementation includes a safety check that reads `expiringNonceSeen[oldHash]` before evicting an entry from the ring buffer. This check verifies the entry is actually expired before overwriting.

**Rationale for keeping the check:**

* Protects against unexpected TPS spikes that could cause the buffer to fill with valid entries
* Defense-in-depth: prevents replay attacks if capacity assumptions are violated
* Cost is only incurred in the rare case when eviction is needed

**Rationale for removing the check:**

* The buffer is sized (300k entries) to guarantee entries expire before being overwritten at 10k TPS
* Removes 1 SLOAD (2,100 gas) from the critical path
* Simplifies the algorithm

**Current decision**: Keep the check but exclude it from gas accounting (charged as if it won't trigger in normal operation).

**Question**: Should this safety check be:

1. Kept with current gas accounting (not charged for the extra SLOAD)?
2. Removed entirely, trusting the capacity sizing?
3. Kept and fully charged (add 2,100 gas to `EXPIRING_NONCE_GAS`)?

## Buffer Capacity Sizing

The current capacity of 300,000 assumes:

* Maximum 10,000 TPS sustained
* 30 second expiry window

**Question**: Should the capacity be configurable per-chain or hardcoded? What happens if TPS requirements increase significantly?

## Transaction Hash Computation

The transaction hash used for replay protection must be computed before signature recovery.

**Question**: Should the spec explicitly define the hash computation (which fields, encoding) or reference the Tempo Transaction spec?

# TIP-1010: Mainnet Gas Parameters

## Abstract

This TIP specifies the initial gas parameters for Tempo mainnet, including base fee pricing, payment lane capacity, and main transaction gas limits. These parameters are calibrated to support Tempo's target of approximately 20,000 TPS for payment transactions while maintaining economically sustainable fee levels.

## Motivation

Tempo is designed as a high-throughput blockchain optimized for stablecoin payments. To achieve this, the gas parameters must be carefully calibrated to:

1. **Enable high throughput**: Support ~20,000 TPS for payment transactions
2. **Maintain low fees**: Target 0.1 cent per standard TIP-20 transfer
3. **Prevent spam**: Ensure fees are high enough to deter abuse
4. **Balance capacity**: Allocate appropriate gas limits between payment lane and general transactions

The parameters defined in this TIP represent the initial mainnet configuration and may be adjusted through future governance processes.

***

# Specification

## Base Fee

**Value**: `2 × 10^10` attodollars (20 billion attodollars per gas)

**Rationale**:

* A standard TIP-20 transfer costs approximately 50,000 gas
* At this basefee: 50,000 gas × 20 billion attodollars/gas = 10^15 attodollars = 1,000 microdollars = $0.001
* This targets approximately **0.1 cent (1,000 microdollars) per TIP-20 transfer**

**Note on units**: Attodollars (10^-18 USD) are the gas price unit. TIP-20 tokens use 6 decimals, so 1 token unit = 1 microdollar (10^-6 USD). Conversion: attodollars / 10^12 = microdollars.

**Note**: The base fee may fluctuate based on network demand through the existing EIP-1559-style mechanism. This value represents the target equilibrium base fee.

## Payment Lane Gas Limit

**Value**: 500,000,000 gas per block (total block gas limit)

**Rationale**:

* At 50,000 gas per TIP-20 transfer: `500,000,000 / 50,000 = 10,000 transfers per block`
* With 500ms block time: `10,000 × 2 = 20,000 TPS` for payment transactions
* This capacity supports Tempo's target throughput for payment use cases

**Constraints**:

* Only transactions qualifying for the payment lane (simple TIP-20 transfers, memos, etc.) may exceed the `general_gas_limit`
* Complex contract interactions use the general gas limit instead

:::info
**Shared capacity model**: The payment lane is non-dedicated. General and payment transactions selected by the proposer share the non-shared gas budget (`block_gas_limit - shared_gas_limit` = 450M). General transactions are capped at `general_gas_limit` (30M), guaranteeing that at least 420M gas remains available for proposer payment transactions. The remaining 50M (`shared_gas_limit`) is reserved for validator subblocks as defined in the Sub-block Specification.
:::

## Main Transaction Gas Limit

**Value**: 30,000,000 gas per block (`general_gas_limit`)

**Rationale**:

* Aligned with the transaction gas cap to ensure maximum-sized contract deployments can be included in a block
* Supports general smart contract interactions beyond simple payments
* Provides capacity for:
  * Contract deployments (including max 24KB contracts)
  * DEX swaps
  * Complex multi-step transactions
  * Other non-payment use cases

:::warning
**Transactions exceeding 16,000,000 gas are not recommended.** The elevated gas limits (30M) exist solely to accommodate maximum-sized contract deployments under TIP-1000 state creation costs. Applications should not rely on transactions consuming more than 16M gas for normal operations. When storage pricing is moved to a separate mechanism (e.g., storage rent or state expiry), the transaction gas cap is expected to return to 16,000,000 gas.
:::

## Transaction Gas Cap

**Value**: 30,000,000 gas per transaction

**Rationale**:

* Increased from the previous 16,000,000 gas limit
* Accommodates deployment of maximum-size contracts (24,576 bytes per EIP-170) under TIP-1000 state creation costs:
  * Base transaction cost: 21,000 gas
  * Calldata for initcode (up to 49,152 bytes per EIP-3860): ~500,000-800,000 gas
  * CREATE base cost (TIP-1000, includes keccak/codesize fields): 500,000 gas (replaces old 32,000)
  * Initcode execution: variable (~3,000 gas minimum)
  * Contract code storage (TIP-1000): `24,576 bytes × 1,000 gas/byte = 24,576,000 gas`
  * Account creation (TIP-1000): 250,000 gas
  * **Total**: ~25,850,000-26,150,000 gas (fits within 30M limit)

## Gas Schedule Summary

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Base fee | `2 × 10^10` attodollars | Target 0.1 cent (1,000 microdollars) per TIP-20 transfer |
| Total block gas limit | 500,000,000 gas/block | Total block capacity |
| Non-shared gas limit | 450,000,000 gas/block | Proposer pool transactions |
| Shared gas limit | 50,000,000 gas/block | Validator subblocks (see Sub-block Specification) |
| General gas limit | 30,000,000 gas/block | Cap for non-payment transactions |
| Transaction gas cap | 30,000,000 gas | Allow max-size contract deployment |

## Economic Analysis

### Fee Revenue Projections

At full payment lane utilization:

* 10,000 transfers per block × 1,000 microdollars = 10,000,000 microdollars ($10) per block
* At 2 blocks/second: $20/second
* Daily: ~$1,728,000 in base fees from payment lane alone

### Cost Per Operation

| Operation | Gas Cost | USD Cost (at target base fee) |
|-----------|----------|-------------------------------|
| TIP-20 transfer (existing recipient) | 50,000 | $0.001 (0.1 cent / 1,000 microdollars) |
| TIP-20 transfer (new recipient) | 300,000 | $0.006 (0.6 cent / 6,000 microdollars) |
| First transaction from new account | 300,000 | $0.006 (0.6 cent / 6,000 microdollars) |
| Small contract deployment (1KB) | ~1,800,000 | $0.036 (3.6 cents / 36,000 microdollars) |
| Max contract deployment (24,576 bytes) | ~26,200,000 | $0.524 (~52 cents / 524,000 microdollars) |

***

# Invariants

1. **Base Fee Floor**: The base fee MUST NOT fall below a minimum threshold that would enable economically viable spam attacks.

2. **Payment Lane Priority**: Transactions qualifying for the payment lane MUST be able to consume up to the remaining block gas capacity (total gas limit minus gas already consumed by general transactions).

3. **Shared Gas Pool**: Proposer pool transactions (payment and general) share the non-shared gas budget (450M). General transactions are additionally constrained by `general_gas_limit` (30M). The remaining 50M is reserved for validator subblocks.

4. **Transaction Gas Cap**: No single transaction MUST be allowed to consume more than the transaction gas cap (30,000,000 gas).

5. **Block Gas Validity**: A block MUST be invalid if either:
   * Payment lane transactions exceed the payment lane gas limit
   * General transactions exceed the general gas limit

## Implementation Notes

These parameters are configured at the chainspec level and applied during block validation. Future adjustments may be made through:

1. Hard fork upgrades (for significant changes)
2. Governance proposals (if on-chain governance is implemented)
3. Emergency response procedures (for critical security issues)

## Test Cases

1. **Base fee targeting**: Verify that at equilibrium, TIP-20 transfers cost approximately 0.1 cent (1,000 microdollars)
2. **Payment lane capacity**: Verify that 10,000 TIP-20 transfers can be included in a single block
3. **General gas limit**: Verify that general transactions are correctly bounded by the 25M gas limit
4. **Transaction gas cap**: Verify that transactions exceeding 30M gas are rejected
5. **Contract deployment**: Verify that a 24KB contract can be deployed within the transaction gas cap
6. **Lane separation**: Verify that payment lane and general transactions are independently tracked

# TIP-1011: Enhanced Access Key Permissions

## Abstract

This TIP extends Access Keys with two new permission features: (1) **periodic spending limits** that automatically reset after a configurable time period, enabling subscription-based access patterns, and (2) **destination address scoping** that restricts keys to only interact with specific contract addresses.

## Motivation

Currently, Access Keys support spending limits (per-TIP-20 token caps) and expiry timestamps. However, these primitives are insufficient for common real-world patterns:

### Periodic Spending Limits

The existing `TokenLimit` specifies a one-time spending cap that depletes permanently. This model doesn't support subscription-based patterns where:

* A service needs recurring access to a fixed amount per billing cycle
* Users want to authorize "up to X tokens per month" without re-authorizing
* dApps implement subscription models (e.g., streaming services, SaaS payments)

**Use cases:**

1. **Subscription services**: Authorize a streaming service to charge 10 USDC/month
2. **Recurring donations**: Allow an NPO to withdraw up to 5 USDC weekly
3. **Payroll systems**: Enable payroll contracts to transfer salaries monthly
4. **Rate-limited APIs**: Authorize API access keys with per-period token budgets

### Destination Address Scoping

Users have requested the ability to bind Access Keys to specific destinations (e.g., "only allow transactions to Uniswap"). This provides more granular permission scoping similar to Solana's delegate primitive.

**Use cases:**

1. **DeFi integrations**: Allow a trading bot key to only interact with specific DEX contracts
2. **Gaming**: Scope a session key to only interact with a game contract
3. **Subscription services**: Allow a key to only call a specific payment contract

**Current workaround**: Deploy a proxy contract that enforces destination restrictions, adding gas overhead and complexity.

***

# Specification

## Extended Data Structures

### TokenLimit

**Current:**

```solidity
struct TokenLimit {
    address token;
    uint256 limit;
}
```

**Proposed:**

```solidity
struct TokenLimit {
    address token;
    uint256 limit;      // Per-period limit when period > 0, one-time limit otherwise
    uint256 remainingInPeriod;  // Remaining allowance in current period
    uint64 period;      // Period duration in seconds (0 = one-time limit)
    uint64 periodEnd;   // Timestamp when current period expires
}
```

### KeyAuthorization

**Current fields retained:**

* `spendingLimits`: `TokenLimit[]`
* `expiry`: `uint64`

**New field:**

```solidity
struct KeyAuthorization {
    TokenLimit[] spendingLimits;
    uint64 expiry;
    address[] allowedDestinations; // Empty array = unrestricted
}
```

## Interface Changes

### IAccountKeychain.sol

```solidity
/// @notice Authorizes a key with enhanced permissions
/// @param key The public key to authorize
/// @param expiry Block timestamp when key expires
/// @param spendingLimits Token spending limits (may include periodic limits)
/// @param allowedDestinations Addresses the key may call (empty = unrestricted)
function authorizeKey(
    bytes calldata key,
    uint64 expiry,
    TokenLimit[] calldata spendingLimits,
    address[] calldata allowedDestinations
) external;

/// @notice Returns the allowed destinations for a key
/// @param key The public key to query
/// @return destinations Array of allowed destination addresses (empty = unrestricted)
function getAllowedDestinations(bytes calldata key) external view returns (address[] memory destinations);

/// @notice Returns the remaining limit for a token, accounting for period resets
/// @param key The public key to query
/// @param token The token address
/// @return remaining The remaining spending limit for the current period
/// @return periodEnd The timestamp when the current period ends (0 if one-time limit)
function getRemainingLimit(bytes calldata key, address token) external view returns (uint256 remaining, uint64 periodEnd);
```

## Semantic Behavior

### Periodic Limit Reset Logic

When a spending attempt occurs:

```
function verifyAndUpdateSpending(key, token, amount):
    limit = getTokenLimit(key, token)
    
    if limit.period > 0:  // Periodic limit
        if block.timestamp >= limit.periodEnd:
            // Reset period
            limit.periodEnd = block.timestamp + limit.period
            limit.remainingInPeriod = limit.limit  // Reset to per-period allowance
    
    if amount > limit.remainingInPeriod:
        revert SpendingLimitExceeded()
    
    limit.remainingInPeriod -= amount
```

### Destination Validation Logic

When a transaction is submitted with an Access Key:

```
function validateDestination(key, destination):
    allowed = getAllowedDestinations(key)
    
    if allowed.length == 0:
        return true  // Unrestricted
    
    for addr in allowed:
        if addr == destination:
            return true
    
    revert DestinationNotAllowed()
```

### Interaction Rules

1. **Mixed limits**: Keys can have a mix of one-time and periodic limits for different tokens
2. **Destination + limits**: Both constraints are evaluated independently; both must pass
3. **Period updates**: Calling `updateSpendingLimit()` updates the per-period amount and resets the current period
4. **Empty destinations**: An empty `allowedDestinations` array means the key is unrestricted (can call any address)

## Gas Costs

| Operation | Additional Gas |
|-----------|----------------|
| `authorizeKey` with N destinations | ~20,000 + 5,000 × N |
| `authorizeKey` with periodic limit | ~3,000 per periodic token |
| Destination check (per tx) | ~2,100 + 200 × N |
| Period reset (when triggered) | ~5,000 |

## Encoding

### Transaction Authorization

The `KeyAuthorization` struct is RLP-encoded in the transaction's authorization field:

```
KeyAuthorization := RLP([
    spendingLimits: [TokenLimit, ...],
    expiry: uint64,
    allowedDestinations: [address, ...]
])

TokenLimit := RLP([
    token: address,
    limit: uint256,
    remainingInPeriod: uint256,
    period: uint64,
    periodEnd: uint64
])
```

***

# Backward Compatibility

This TIP requires a **hardfork** due to changes in transaction encoding and execution semantics.

## RLP Encoding Changes

### TokenLimit (2 fields → 5 fields)

The current `TokenLimit` struct encodes as `[token, limit]`. This TIP extends it to `[token, limit, remainingInPeriod, period, periodEnd]`.

**Breaking change**: Old nodes cannot decode new transactions with 5-field `TokenLimit`. New nodes must implement version-tolerant decoding:

```
On decode:
  if list.len() == 2:
    // V1 (legacy one-time limit)
    remainingInPeriod = limit
    period = 0
    periodEnd = 0
  else if list.len() == 5:
    // V2 (periodic limit)
    decode all fields
  else:
    error
```

Post-fork, all new `TokenLimit` encodings MUST use the 5-field format for consistency.

### KeyAuthorization (trailing field addition)

`KeyAuthorization` uses `#[rlp(trailing)]` which allows appending optional fields. Adding `allowedDestinations: Option<Vec<Address>>` as the last field is compatible with this pattern:

* Old encodings (without `allowedDestinations`) decode as `allowedDestinations = None` (unrestricted)
* New encodings with `allowedDestinations` will be rejected by old nodes

## Compact/Database Encoding

Although `TokenLimit` has `#[derive(reth_codecs::Compact)]`, it is **not used in production storage**. The storage path is:

```
TempoTransaction (derived Compact)
  └─ key_authorization: Option<SignedKeyAuthorization>
       └─ SignedKeyAuthorization (custom Compact impl → uses RLP internally)
            └─ KeyAuthorization (RLP encoded)
                 └─ limits: Option<Vec<TokenLimit>> (RLP encoded)
```

`SignedKeyAuthorization` implements a custom `Compact` that wraps RLP encoding. Therefore, `TokenLimit` is always serialized as RLP bytes in the database, not via its derived Compact layout.

**Implication**: If we implement version-tolerant RLP decoding for `TokenLimit` (accept 2-field or 5-field lists), existing database entries will decode correctly. **No DB rebuild required** for this change.

## Precompile Storage Changes

The current storage layout:

* `keys[account][keyId] → AuthorizedKey` (packed slot)
* `spending_limits[key][token] → U256` (remaining amount)

This TIP requires additional per-token state for periodic limits. **Additive storage approach** (no migration required):

| Mapping | Type | Description |
|---------|------|-------------|
| `spending_limits[key][token]` | `U256` | Reinterpreted as `remainingInPeriod` |
| `spending_limit_max[key][token]` | `U256` | Per-period cap (new) |
| `spending_limit_period[key][token]` | `u64` | Period duration in seconds (new) |
| `spending_limit_period_end[key][token]` | `u64` | Current period end timestamp (new) |

For destination scoping:

| Mapping | Type | Description |
|---------|------|-------------|
| `allowed_destinations_len[key]` | `u64` | Number of allowed destinations |
| `allowed_destinations[key][index]` | `Address` | Allowed destination at index |

Legacy keys (pre-fork) have `period = 0`, `max = 0`, and behave as one-time limits.

## Hardfork-Gated Features

The following MUST be gated behind the hardfork activation:

1. **RLP decoding**: Accept 5-field `TokenLimit` and `allowedDestinations` in `KeyAuthorization`
2. **Periodic limit reset logic**: Check `periodEnd` and reset `remainingInPeriod` on spend
3. **Destination scoping enforcement**: Validate transaction `to` against `allowedDestinations`
4. **New precompile storage writes**: Write to new storage slots for period/destination data
5. **New precompile interface methods**: `getAllowedDestinations()`, updated `getRemainingLimit()` return type

Pre-fork blocks MUST be replayed with old semantics to preserve state root consistency.

***

# Invariants

1. **Period monotonicity**: `periodEnd` MUST only increase; it cannot be set to a past timestamp.

2. **Limit conservation**: For periodic limits, `remainingInPeriod` MUST NOT exceed `limit` after any reset.

3. **Destination enforcement**: If `allowedDestinations` is non-empty, transactions to addresses not in the list MUST revert.

4. **Backward compatibility**: Keys authorized without the new fields MUST behave as unrestricted (`allowedDestinations = []`) with one-time limits (`period = 0`).

5. **Expiry precedence**: Key expiry MUST be checked before spending limits or destination restrictions.

## Test Cases

1. **Periodic reset**: Verify that a periodic limit resets correctly after the period elapses
2. **Partial period usage**: Verify that unused periodic allowance does not roll over
3. **Destination allow**: Verify that transactions to allowed destinations succeed
4. **Destination deny**: Verify that transactions to non-allowed destinations revert
5. **Empty destinations**: Verify that empty `allowedDestinations` allows any destination
6. **Mixed limits**: Verify that a key can have both one-time and periodic limits for different tokens
7. **Upgrade path**: Verify that existing keys continue to function after upgrade

## References

* [AccountKeychain docs](https://docs.tempo.xyz/protocol/transactions/AccountKeychain)
* [IAccountKeychain.sol](https://github.com/tempoxyz/tempo-std/blob/master/src/interfaces/IAccountKeychain.sol)
* [GitHub Issue #1865](https://github.com/tempoxyz/tempo/issues/1865) - Periodic spending limits
* [GitHub Issue #1491](https://github.com/tempoxyz/tempo/issues/1491) - Destination address scoping

# TIP-1015: Compound Transfer Policies

## Abstract

This TIP extends the TIP-403 policy registry to support **compound policies** that allow token issuers to specify different authorization rules for senders, recipients, and mint recipients. A compound policy references three simple policies: one for sender authorization, one for recipient authorization, and one for mint recipient authorization. Compound policies are immutable once created.

## Motivation

The current TIP-403 system applies the same policy to both senders and recipients of a token transfer. However, real-world requirements often differ between sending and receiving:

* **Vendor credits**: A business may issue credits that can be minted to anyone and spent by holders to a specific vendor, but cannot be transferred peer-to-peer. This requires allowing all addresses as recipients (for minting) while restricting senders to only transfer to the vendor's address.
* **Sender restrictions**: An issuer may want to block sanctioned addresses from sending tokens, while allowing anyone to receive tokens (e.g., for refunds or seizure).
* **Recipient restrictions**: An issuer may require recipients to be KYC-verified, while allowing any holder to send tokens out.
* **Asymmetric compliance**: Different jurisdictions may have different requirements for inflows vs outflows.

Compound policies enable these use cases while maintaining backward compatibility with existing simple policies.

***

# Specification

## Policy Types

TIP-403 currently supports two policy types: `WHITELIST` and `BLACKLIST`. This TIP adds a third type:

```solidity
enum PolicyType {
    WHITELIST,
    BLACKLIST,
    COMPOUND
}
```

## Compound Policy Structure

A compound policy references three existing simple policies by their policy IDs:

```solidity
struct CompoundPolicyData {
    uint64 senderPolicyId;        // Policy checked for transfer senders
    uint64 recipientPolicyId;     // Policy checked for transfer recipients
    uint64 mintRecipientPolicyId; // Policy checked for mint recipients
}
```

All three referenced policies MUST be simple policies (WHITELIST or BLACKLIST), not compound policies. This prevents circular references and unbounded recursion.

## Storage Layout

Policy data is stored in a unified `PolicyRecord` struct that contains both base policy data and compound policy data:

```solidity
struct PolicyData {
    uint8 policyType;   // 0 = WHITELIST, 1 = BLACKLIST, 2 = COMPOUND
    address admin;      // Policy administrator (zero for immutable compound policies)
}

struct PolicyRecord {
    PolicyData base;          // offset 0: base policy data
    CompoundPolicyData compound;  // offset 1: compound policy data (only used when policyType == COMPOUND)
}
```

The TIP403Registry storage layout:

| Slot | Field | Description |
|------|-------|-------------|
| 0 | `policyIdCounter` | Counter for generating unique policy IDs |
| 1 | `policyRecords` (private) | `mapping(uint64 => PolicyRecord)` - Policy ID to policy record |
| 2 | `policySet` | `mapping(uint64 => mapping(address => bool))` - Whitelist/blacklist membership |

The `policyRecords` mapping is private (not exposed in the ABI). The existing `policyData(uint64 policyId)` view function provides backwards-compatible access to `PolicyData`.

For a given policy ID, storage locations are:

* **PolicyData**: `keccak256(policyId, 1)` (offset 0 within PolicyRecord)
* **CompoundPolicyData**: `keccak256(policyId, 1) + 1` (offset 1 within PolicyRecord)

This unified layout requires only **1 keccak computation + 2 SLOADs** for compound policy authorization, compared to 2 keccak computations with separate mappings.

## Interface Additions

The TIP403Registry interface is extended with the following:

```solidity
interface ITIP403Registry {
    // ... existing interface ...

    // =========================================================================
    //                      Compound Policy Creation
    // =========================================================================

    /// @notice Creates a new immutable compound policy
    /// @param senderPolicyId Policy ID to check for transfer senders
    /// @param recipientPolicyId Policy ID to check for transfer recipients
    /// @param mintRecipientPolicyId Policy ID to check for mint recipients
    /// @return newPolicyId ID of the newly created compound policy
    /// @dev All three policy IDs must reference existing simple policies (not compound).
    /// Compound policies are immutable - they cannot be modified after creation.
    /// Emits CompoundPolicyCreated event.
    function createCompoundPolicy(
        uint64 senderPolicyId,
        uint64 recipientPolicyId,
        uint64 mintRecipientPolicyId
    ) external returns (uint64 newPolicyId);

    // =========================================================================
    //                      Sender/Recipient Authorization
    // =========================================================================

    /// @notice Checks if a user is authorized as a sender under the given policy
    /// @param policyId Policy ID to check against
    /// @param user Address to check
    /// @return True if authorized to send, false otherwise
    /// @dev For simple policies: equivalent to isAuthorized()
    /// For compound policies: checks against the senderPolicyId
    function isAuthorizedSender(uint64 policyId, address user) external view returns (bool);

    /// @notice Checks if a user is authorized as a recipient under the given policy
    /// @param policyId Policy ID to check against
    /// @param user Address to check
    /// @return True if authorized to receive, false otherwise
    /// @dev For simple policies: equivalent to isAuthorized()
    /// For compound policies: checks against the recipientPolicyId
    function isAuthorizedRecipient(uint64 policyId, address user) external view returns (bool);

    /// @notice Checks if a user is authorized as a mint recipient under the given policy
    /// @param policyId Policy ID to check against
    /// @param user Address to check
    /// @return True if authorized to receive mints, false otherwise
    /// @dev For simple policies: equivalent to isAuthorized()
    /// For compound policies: checks against the mintRecipientPolicyId
    function isAuthorizedMintRecipient(uint64 policyId, address user) external view returns (bool);

    // =========================================================================
    //                      Compound Policy Queries
    // =========================================================================

    /// @notice Returns the constituent policy IDs for a compound policy
    /// @param policyId ID of the compound policy to query
    /// @return senderPolicyId Policy ID for sender checks
    /// @return recipientPolicyId Policy ID for recipient checks
    /// @return mintRecipientPolicyId Policy ID for mint recipient checks
    /// @dev Reverts if policyId is not a compound policy
    function compoundPolicyData(uint64 policyId) external view returns (
        uint64 senderPolicyId,
        uint64 recipientPolicyId,
        uint64 mintRecipientPolicyId
    );

    // =========================================================================
    //                      Events
    // =========================================================================

    /// @notice Emitted when a new compound policy is created
    /// @param policyId ID of the newly created compound policy
    /// @param creator Address that created the policy
    /// @param senderPolicyId Policy ID for sender checks
    /// @param recipientPolicyId Policy ID for recipient checks
    /// @param mintRecipientPolicyId Policy ID for mint recipient checks
    event CompoundPolicyCreated(
        uint64 indexed policyId,
        address indexed creator,
        uint64 senderPolicyId,
        uint64 recipientPolicyId,
        uint64 mintRecipientPolicyId
    );

    // =========================================================================
    //                      Errors
    // =========================================================================

    /// @notice The referenced policy is not a simple policy
    error PolicyNotSimple();

    /// @notice The referenced policy does not exist
    error PolicyNotFound();
}
```

## Authorization Logic

### isAuthorizedSender

```solidity
function isAuthorizedSender(uint64 policyId, address user) external view returns (bool) {
    PolicyRecord storage record = policyRecords[policyId];

    if (record.base.policyType == PolicyType.COMPOUND) {
        return isAuthorized(record.compound.senderPolicyId, user);
    }

    // For simple policies, sender authorization equals general authorization
    return isAuthorized(policyId, user);
}
```

### isAuthorizedRecipient

```solidity
function isAuthorizedRecipient(uint64 policyId, address user) external view returns (bool) {
    PolicyRecord storage record = policyRecords[policyId];

    if (record.base.policyType == PolicyType.COMPOUND) {
        return isAuthorized(record.compound.recipientPolicyId, user);
    }

    // For simple policies, recipient authorization equals general authorization
    return isAuthorized(policyId, user);
}
```

### isAuthorizedMintRecipient

```solidity
function isAuthorizedMintRecipient(uint64 policyId, address user) external view returns (bool) {
    PolicyRecord storage record = policyRecords[policyId];

    if (record.base.policyType == PolicyType.COMPOUND) {
        return isAuthorized(record.compound.mintRecipientPolicyId, user);
    }

    // For simple policies, mint recipient authorization equals general authorization
    return isAuthorized(policyId, user);
}
```

### isAuthorized (updated)

The existing `isAuthorized` function is updated to check both sender and recipient authorization:

```solidity
function isAuthorized(uint64 policyId, address user) external view returns (bool) {
    return isAuthorizedSender(policyId, user) && isAuthorizedRecipient(policyId, user);
}
```

This maintains backward compatibility: for simple policies both functions return the same result, so `isAuthorized` behaves identically to before. For compound policies, `isAuthorized` returns true only if the user is authorized as both sender and recipient.

## Required Code Changes

This TIP requires exactly 6 replacements of `isAuthorized` calls:

### Direct Replacements

| Location | Current | Replace With |
|----------|---------|--------------|
| TIP-20 `_mint` | `isAuthorized(to)` | `isAuthorizedMintRecipient(to)` |
| TIP-20 `burnBlocked` | `isAuthorized(from)` | `isAuthorizedSender(from)` |
| DEX `cancelStaleOrder` | `isAuthorized(maker)` | `isAuthorizedSender(maker)` |
| Fee payer `can_fee_payer_transfer` | `isAuthorized(fee_payer)` | `isAuthorizedSender(fee_payer)` |

### Core Authorization Logic

| Location | Current | Replace With |
|----------|---------|--------------|
| TIP-20 `isTransferAuthorized` | `isAuthorized(from)` | `isAuthorizedSender(from)` |
| TIP-20 `isTransferAuthorized` | `isAuthorized(to)` | `isAuthorizedRecipient(to)` |

All other call sites use `ensureTransferAuthorized(from, to)` which delegates to `isTransferAuthorized`, so they automatically inherit the correct behavior:

* **TIP-20**: `transfer`, `transferFrom`, `transferWithMemo`, `systemTransferFrom`
* **TIP-20 Rewards**: `distributeReward`, `setRewardRecipient`, `claimRewards`
* **Stablecoin DEX**: `decrementBalanceOrTransferFrom`, `placeLimitOrder`, `swapExactAmountIn`

## TIP-20 Integration

TIP-20 tokens MUST be updated to use the new sender/recipient authorization functions:

### Transfer Authorization (isTransferAuthorized)

```solidity
function isTransferAuthorized(address from, address to) internal view returns (bool) {
    uint64 policyId = transferPolicyId;
    
    bool fromAuthorized = TIP403_REGISTRY.isAuthorizedSender(policyId, from);
    bool toAuthorized = TIP403_REGISTRY.isAuthorizedRecipient(policyId, to);
    
    return fromAuthorized && toAuthorized;
}
```

### Mint Operations

Mint operations check the mint recipient policy:

```solidity
function _mint(address to, uint256 amount) internal {
    if (!TIP403_REGISTRY.isAuthorizedMintRecipient(transferPolicyId, to)) {
        revert PolicyForbids();
    }
    // ... mint logic
}
```

### Burn Blocked Operations

The `burnBlocked` function checks sender authorization to verify the address is blocked:

```solidity
function burnBlocked(address from, uint256 amount) external {
    require(hasRole(BURN_BLOCKED_ROLE, msg.sender));
    
    // Only allow burning from addresses blocked from sending
    if (TIP403_REGISTRY.isAuthorizedSender(transferPolicyId, from)) {
        revert PolicyForbids();
    }
    // ... burn logic
}
```

## Stablecoin DEX Integration

### Cancel Stale Order

The `cancelStaleOrder` function checks sender authorization on the token escrowed by the maker, since if the order is filled, the maker will have to send that token:

```solidity
function cancelStaleOrder(uint128 orderId) external {
    Order order = orders[orderId];
    address token = order.isBid() ? book.quote : book.base;
    uint64 policyId = TIP20(token).transferPolicyId();
    
    // Order is stale if maker can no longer send the escrowed token
    if (TIP403_REGISTRY.isAuthorizedSender(policyId, order.maker())) {
        revert OrderNotStale();
    }
    
    _cancelOrder(order);
}
```

## Immutability

Compound policies are immutable once created. To change policy behavior, token issuers must:

1. Create a new compound policy with the desired configuration
2. Update the token's `transferPolicyId` to the new policy

## Backward Compatibility

This TIP is fully backward compatible:

* Existing simple policies continue to work unchanged
* Tokens using simple policies will see identical behavior (since `isAuthorizedSender` and `isAuthorizedRecipient` return the same result for simple policies)
* The existing `isAuthorized` function continues to work for both simple and compound policies

***

# Invariants

1. **Simple Policy Constraint**: All three policy IDs in a compound policy MUST reference simple policies (WHITELIST or BLACKLIST). Compound policies cannot reference other compound policies.

2. **Immutability**: Once created, a compound policy's constituent policy IDs cannot be changed. The compound policy itself has no admin.

3. **Existence Check**: `createCompoundPolicy` MUST revert if any of the referenced policy IDs does not exist.

4. **Delegation Correctness**: For simple policies, `isAuthorizedSender(p, u)` MUST equal `isAuthorizedRecipient(p, u)` MUST equal `isAuthorizedMintRecipient(p, u)`.

5. **isAuthorized Equivalence**: `isAuthorized(p, u)` MUST equal `isAuthorizedSender(p, u) && isAuthorizedRecipient(p, u)`.

6. **Built-in Policy Compatibility**: Compound policies MAY reference built-in policies (0 = always-reject, 1 = always-allow) as any of their constituent policies.

7. **Non-existent Policy Revert**: All authorization functions (`isAuthorized`, `isAuthorizedSender`, `isAuthorizedRecipient`, `isAuthorizedMintRecipient`) MUST revert with `PolicyNotFound()` when called with a policy ID that does not exist. Built-in policies (0 and 1) always exist and are exempt from this check.

## Test Cases

1. **Simple policy equivalence**: Verify that for simple policies, all four authorization functions return the same result.

2. **Compound policy creation**: Verify that compound policies can be created with valid simple policy references.

3. **Invalid creation**: Verify that `createCompoundPolicy` reverts when referencing non-existent policies or compound policies.

4. **Sender/recipient differentiation**: Verify that a compound policy with different sender/recipient policies correctly authorizes asymmetric transfers.

5. **isAuthorized behavior**: Verify that `isAuthorized` on a compound policy returns `isAuthorizedSender() && isAuthorizedRecipient()`.

6. **TIP-20 mint**: Verify that mints check `isAuthorizedMintRecipient`, not `isAuthorizedRecipient`.

7. **TIP-20 burnBlocked**: Verify that burnBlocked checks sender authorization (and allows burning from blocked senders).

8. **Vendor credits**: Verify that a compound policy with `mintRecipientPolicyId = 1` (always-allow), `senderPolicyId = 1` (always-allow), and `recipientPolicyId = vendor whitelist` allows minting to anyone but only transfers to vendors.

# TIP-1016: Exempt Storage Creation from Gas Limits

## Abstract

Storage creation operations (new state elements, account creation, contract code storage) continue to consume and be charged for gas, but this gas does not count against transaction or block gas limits. This allows increasing contract code pricing to 2,500 gas/byte without preventing large contract deployments, and prevents new account creation from reducing effective throughput.

## Motivation

TIP-1000 increased storage creation costs to 250,000 gas per operation and 1,000 gas/byte for contract code. This created two problems:

1. **Contract deployment constraints**: 24KB contracts require ~26M gas, forcing us to:
   * Keep transaction gas cap at 30M (would prefer 16M)
   * Keep general gas limit at 30M (would prefer lower)
   * Limit contract code to 1,000 gas/byte (would prefer 2,500)

2. **New account throughput penalty**: TIP-20 transfer to new address costs ~300,000 gas total (~70k execution + 230k storage) vs ~50,000 gas to existing. At 500M payment lane gas limit:
   * With storage creation gas counting: only ~1,700 new account transfers/block = ~3,400 TPS
   * Without storage creation gas counting: ~7,100 new account transfers/block = ~14,200 TPS
   * Existing account transfers: ~10,000 transfers/block = ~20,000 TPS
   * \~4x throughput improvement for new accounts by exempting storage creation gas from limits

The root cause: storage creation gas counts against limits designed for execution time constraints. Storage creation is permanent (disk) not ephemeral (CPU), and shouldn't be bounded by per-block execution limits.

***

# Specification

## Gas Accounting

All operations consume gas, but storage creation operations now split their cost into two components:

* **Execution gas**: Compute, memory, calldata, and the computational cost of storage operations (writing, hashing)
  * Counts toward protocol limits (transaction and block)

* **Storage creation gas**: The permanent storage burden of storage creation
  * Does NOT count toward protocol limits
  * Still counts toward user's `gas_limit`

## Gas Limits

Storage creation gas counts against the user's transaction gas limit (to prevent surprise costs) but NOT against protocol limits:

```
User Authorization:
  execution_gas + storage_creation_gas <= transaction.gas_limit

Protocol Limits:
  execution_gas <= max_transaction_gas_limit (EIP-7825, e.g. 16M)
  general_execution_gas <= general_gas_limit (e.g. 25M, for non-payment txs)
  payment_execution_gas <= payment_lane_limit (500M, for payment txs)

Cost:
  total_gas = execution_gas + storage_creation_gas
  cost = total_gas × (base_fee_per_gas + priority_fee)
```

**Rationale**:

* User's `gas_limit` bounds total cost (no surprise charges)
* Protocol limits bound only execution gas (block time constraint, not disk I/O)
* Storage doesn't reduce block execution capacity or prevent large contracts
* Note: Tempo has two block limits - general gas limit (~25M) for contracts and payment lane limit (500M) for simple transfers

## Storage Gas Operations

Storage creation operations split their cost between execution gas (computational overhead) and storage creation gas (permanent storage burden):

| Operation | Execution Gas | Storage Gas | Total | Against Limits |
|-----------|---------------|-------------|-------|----------------|
| Cold SSTORE (zero → non-zero) | 20,000 | 230,000 | 250,000 | 20,000 |
| Hot SSTORE (non-zero → non-zero) | 2,900 | 0 | 2,900 | 2,900 |
| Account creation (nonce 0 → 1) | 25,000 | 225,000 | 250,000 | 25,000 |
| Contract code storage (per byte) | 200 | 2,300 | 2,500 | 200 |
| Contract metadata (keccak + nonce) | 32,000 | 468,000 | 500,000 | 32,000 |

**Notes:**

* Execution gas is set to at least the pre-TIP-1000 (standard EVM) cost for each operation, ensuring that exempting storage creation gas from limits never makes an operation cheaper against protocol limits than it was before TIP-1000
* Storage creation gas reflects permanent storage burden and does NOT count toward protocol limits
* All gas (execution + storage) counts toward user's `gas_limit` and is charged at `base_fee_per_gas`

## Contract Creation Pricing

Contract code storage cost increases from 1,000 to **2,500 gas/byte** (200 execution + 2,300 storage).

Example for 24KB contract:

* Contract code execution gas: `24,576 × 200 = 4,915,200`
* Contract code storage creation gas: `24,576 × 2,300 = 56,524,800`
* Contract metadata execution gas: `32,000`
* Contract metadata storage creation gas: `468,000`
* Account creation execution gas: `25,000`
* Account creation storage creation gas: `225,000`
* Deployment logic execution gas: ~2M

**Totals:**

* Execution gas: ~7M (counts toward protocol limits)
* Storage creation gas: ~57M (doesn't count toward protocol limits)
* Total gas: ~64M (user must authorize with `gas_limit >= 64M`)
* **Can deploy with protocol max\_transaction\_gas\_limit = 16M** (only ~7M counts)

## Examples

### TIP-20 Transfer to New Address

* Transfer logic: ~50,000 execution gas
* New balance slot: 20,000 execution gas + 230,000 storage creation gas
* **Total**: ~70,000 execution gas + 230,000 storage creation gas = ~300,000 gas
* User must authorize: `gas_limit >= 300,000`
* Counts toward block limit: ~70,000 execution gas
* Total cost: ~300,000 gas

### TIP-20 Transfer to Existing Address

* Transfer logic: ~50,000 execution gas
* Update existing slot: included in transfer logic
* **Total**: ~50,000 execution gas
* User must authorize: `gas_limit >= 50,000`
* Counts toward block limit: ~50,000 execution gas
* Total cost: ~50,000 gas

### Block Throughput

At 500M payment lane execution gas limit:

* New account transfers: ~70k execution gas each → ~7,100 transfers/block
* Existing account transfers: ~50k execution gas each → ~10,000 transfers/block
* \~8,500 TPS on average (vs ~3,400 TPS without exemption)
* Storage creation gas doesn't reduce block capacity

***

# Invariants

1. **User Authorization**: `execution_gas + storage_creation_gas` MUST NOT exceed `transaction.gas_limit` (prevents surprise costs)
2. **Protocol Transaction Limit**: `execution_gas` MUST NOT exceed `max_transaction_gas_limit` (EIP-7825 limit, e.g. 16M)
3. **Protocol Block Limits**: Block `execution_gas` MUST NOT exceed applicable limit:
   * General transactions: `general_gas_limit` (25M target, currently 30M)
   * Payment lane transactions: `payment_lane_limit` (500M)
4. **Storage Gas Exemption**: Storage creation gas component MUST NOT count toward protocol limits (transaction and block)
5. **Execution Gas Component**: Storage creation operations MUST charge execution gas for computational overhead (writing, hashing)
6. **Total Cost**: Transaction cost MUST equal `(execution_gas + storage_creation_gas) × (base_fee_per_gas + priority_fee)`
7. **Gas Split**: Storage creation operations MUST split cost into execution gas (computational) and storage creation gas (permanent burden)
8. **Hot vs Cold**: Hot SSTORE (non-zero → non-zero) has NO storage creation gas component; cold SSTORE (zero → non-zero) has both
9. **Execution Gas Floor**: The execution gas component of each storage creation operation MUST be at least the pre-TIP-1000 (standard EVM) cost for that operation (SSTORE: 20,000, account creation: 25,000, CREATE base: 32,000, code deposit: 200/byte)

***

# Changes from TIP-1000

| Parameter | TIP-1000 | TIP-1016 |
|-----------|----------|----------|
| Contract code pricing | 1,000 gas/byte | 2,500 gas/byte (200 exec + 2,300 storage) |
| Cold SSTORE pricing | 250,000 gas | 250,000 gas (20,000 exec + 230,000 storage) |
| Account creation pricing | 250,000 gas | 250,000 gas (25,000 exec + 225,000 storage) |
| Storage creation gas counts toward user's gas\_limit | Yes | Yes (no change) |
| Storage creation gas counts toward protocol limits | Yes | No (exempted) |
| Execution gas counts toward protocol limits | Yes | Yes (no change) |
| Max transaction gas limit (EIP-7825) | 30M | Can reduce to 16M |
| Block gas limit for execution | 30M | 25M (ideal target) |
| Block gas limit for payments lane | 500M | 500M (unchanged) |
| Block gas limit for storage | 500M (shared) | Unlimited (exempted) |

***

# Key Benefits

1. **Higher contract code pricing**: 2,500 gas/byte (vs 1,000) provides better state growth protection ($50M for 1TB vs $20M)
2. **Lower protocol transaction limit**: Can use 16M max\_transaction\_gas\_limit while deploying 24KB contracts (~7M execution gas counts)
3. **Better throughput for new accounts**: ~7,100 new account transfers/block vs ~1,700 without exemption (~4x improvement)
4. **Accounts for computational cost**: Storage operations still charge execution gas for writing/hashing (not completely free)
5. **No surprise costs**: User's `gas_limit` still bounds total cost (no griefing)
6. **No complexity**: Single gas unit, one basefee, existing transaction format works

## Economic Impact

| Operation | TIP-1000 Cost | TIP-1016 Cost |
|-----------|---------------|---------------|
| TIP-20 transfer (existing) | ~50k gas = 0.1 cent (1,000 microdollars) | ~50k gas = 0.1 cent (1,000 microdollars) |
| TIP-20 transfer (new) | ~300k gas = 0.6 cent (6,000 microdollars) | ~300k gas = 0.6 cent (6,000 microdollars) |
| 1KB contract | ~1.75M gas = 3.5 cents (35,000 microdollars) | ~3.25M gas = 6.5 cents (65,000 microdollars) |
| 24KB contract | ~30M gas = 60 cents (600,000 microdollars) | ~64M gas = 128 cents (1,280,000 microdollars) |

Cost calculations assume base\_fee = 2 × 10^10 attodollars (1 token unit = 1 microdollar = 10^-6 USD).

**Note**: Costs are similar to TIP-1000, but protocol limits now only count execution gas, enabling higher contract code pricing and better throughput.

# ValidatorConfig V2

This document specifies the second version of the Validator Config precompile,
introducing an append-only, delete-once design that eliminates the need for
historical state access during node recovery.

* **TIP ID**: TIP-1017
* **Authors/Owners**: Janis, Howy
* **Status**: In Review
* **Related Specs/TIPs**: N/A
* **Protocol Version**: T2

***

# Overview

## Abstract

TIP-1017 introduces ValidatorConfig V2, a new precompile for managing consensus
validators with append-only semantics. Unlike the original ValidatorConfig, V2
replaces the mutable `active` boolean with `addedAtHeight` (set when adding an
entry) and `deactivatedAtHeight` fields (set when deactivating), enabling nodes to
reconstruct the validator set for any historical epoch using only current state.
The new design also requires Ed25519 signature verification when adding
validators to prove key ownership.

## Motivation

The original ValidatorConfig precompile allows validators to be updated
arbitrarily, which creates challenges for node recovery:

1. **Historical state dependency**: To determine the validator set at a past
   epoch, nodes must access historical account state, which requires retaining
   and indexing all historical data.

2. **Key ownership verification**: V1 does not verify that the caller controls
   the private key corresponding to the public key being registered, allowing
   potential key squatting attacks.

3. **Validator re-registration**: V1 allows deleted validators to be re-added
   with different parameters, complicating historical queries.

V2 solves these problems with an append-only design where:

* Validators are immutable after creation (no `updateValidator`)
* `addedAtHeight` and `deactivatedAtHeight` fields enable historical reconstruction
  from current state
* Ed25519 signature verification proves key ownership at registration time
* Public keys remain reserved forever (even after deactivation); addresses are unique among current validators but can be reassigned via `transferValidatorOwnership`

### Key Design Principle

By recording `addedAtHeight` and `deactivatedAtHeight`, nodes can determine DKG players for any epoch using only current state. When preparing for a DKG ceremony in epoch `E+1`, a node reads the contract at `boundary(E)` and filters:

```
players(E+1) = validators.filter(v =>
    v.addedAtHeight <= boundary(E) &&
    (v.deactivatedAtHeight == 0 || v.deactivatedAtHeight > boundary(E))
)
```

Both addition and deactivation take effect at the next epoch boundary—there is no warmup or cooldown period.

This eliminates the need to retain historical account state for consensus recovery—nodes can derive DKG player sets from the current contract state alone.

***

# Specification

## Precompile Address

```solidity
address constant VALIDATOR_CONFIG_V2_ADDRESS = 0xCCCCCCCC00000000000000000000000000000001;
```

## Interface

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

/// @title IValidatorConfigV2 - Validator Config V2 Precompile Interface
/// @notice Interface for managing consensus validators with append-only, delete-once semantics
/// @dev This precompile manages the set of validators that participate in consensus.
///      V2 uses an append-only design that eliminates the need for historical state access
///      during node recovery. Validators are immutable after creation and can only be deleted once.
///
///      Key differences from V1:
///      - `active` bool replaced by `addedAtHeight` and `deactivatedAtHeight`
///      - No `updateValidator` - validators are immutable after creation
///      - Requires Ed25519 signature on `addValidator` to prove key ownership
///      - Both address and public key must be unique across all validators (including deleted)
interface IValidatorConfigV2 {

    /// @notice Thrown when caller lacks authorization to perform the requested action
    error Unauthorized();

    /// @notice Thrown when trying to add a validator with an address that already exists
    error AddressAlreadyHasValidator();

    /// @notice Thrown when trying to add a validator with a public key that already exists
    error PublicKeyAlreadyExists();

    /// @notice Thrown when validator is not found
    error ValidatorNotFound();

    /// @notice Thrown when trying to delete a validator that is already deleted
    error ValidatorAlreadyDeleted();

    /// @notice Thrown when public key is invalid (zero)
    error InvalidPublicKey();

    /// @notice Thrown when the Ed25519 signature verification fails
    error InvalidSignature();

    /// @notice Thrown when address is not in valid ip:port format
    /// @param field The field name that failed validation
    /// @param input The invalid input that was provided
    /// @param backtrace Additional error context
    error NotIpPort(string field, string input, string backtrace);

    /// @notice Thrown when trying to use an ingress IP already in use by another active validator
    /// @param ingress The ingress address that is already in use
    error IngressAlreadyExists(string ingress);

    /// @notice Validator information (V2 - append-only, delete-once)
    /// @param publicKey Ed25519 communication public key (non-zero, unique across all validators)
    /// @param validatorAddress Ethereum-style address of the validator (unique across all validators)
    /// @param ingress Address where other validators can connect (format: `<ip>:<port>`)
    /// @param egress IP address from which this validator will dial, e.g. for firewall whitelisting (format: `<ip>`)
    /// @param index Position in validators array (assigned at creation, immutable)
    /// @param addedAtHeight Block height when validator was added
    /// @param deactivatedAtHeight Block height when validator was deleted (0 = active)
    struct Validator {
        bytes32 publicKey;
        address validatorAddress;
        string ingress;
        string egress;
        uint64 index;
        uint64 addedAtHeight;
        uint64 deactivatedAtHeight;
    }

    /// @notice Get all validators (including deleted ones) in array order
    /// @return validators Array of all validators with their information
    function getAllValidators() external view returns (Validator[] memory validators);

    /// @notice Get only active validators (where deactivatedAtHeight == 0)
    /// @return validators Array of active validators
    function getActiveValidators() external view returns (Validator[] memory validators);

    /// @notice Get the height at which the contract was initialized
    /// @return the height at which the contract was initialized. Note that this
    ///         value only makes sense in conjunction with isInitialized()
    function getInitializedAtHeight() external view returns (uint64);

    /// @notice Get the owner of the precompile
    /// @return The owner address
    function owner() external view returns (address);

    /// @notice Get total number of validators ever added (including deleted)
    /// @return The count of validators
    function validatorCount() external view returns (uint64);

    /// @notice Get validator information by index in the validators array
    /// @param index The index in the validators array
    /// @return The validator struct at the given index
    function validatorByIndex(uint64 index) external view returns (Validator memory);

    /// @notice Get validator information by address
    /// @param validatorAddress The validator address to look up
    /// @return The validator struct for the given address
    function validatorByAddress(address validatorAddress) external view returns (Validator memory);

    /// @notice Get validator information by public key
    /// @param publicKey The validator's public key to look up
    /// @return The validator struct for the given public key
    function validatorByPublicKey(bytes32 publicKey) external view returns (Validator memory);

    /// @notice Get the epoch at which a fresh DKG ceremony will be triggered
    /// @return The epoch number, or 0 if no fresh DKG is scheduled.
    ///         The fresh DKG ceremony runs in epoch N, and epoch N+1 uses the new DKG polynomial.
    function getNextFullDkgCeremony() external view returns (uint64);

    /// @notice Add a new validator (owner only)
    /// @dev The signature must be an Ed25519 signature over:
    ///      keccak256(abi.encodePacked(bytes8(chainId), contractAddress, validatorAddress, ingress, egress))
    ///      using the namespace "TEMPO_VALIDATOR_CONFIG_V2_ADD_VALIDATOR".
    ///      This proves the caller controls the private key corresponding to publicKey.
    ///      Reverts if isInitialized() returns false.
    /// @param validatorAddress The address of the new validator
    /// @param publicKey The validator's Ed25519 communication public key
    /// @param ingress The validator's inbound address `<ip>:<port>` for incoming connections
    /// @param egress The validator's outbound IP address `<ip>` for firewall whitelisting
    /// @param signature Ed25519 signature (64 bytes) proving ownership of the public key
    function addValidator(
        address validatorAddress,
        bytes32 publicKey,
        string calldata ingress,
        string calldata egress,
        bytes calldata signature
    ) external;

    /// @notice Deactivates a validator (owner or existing validator)
    /// @dev Marks the validator as deactivated by setting deactivatedAtHeight to the current block height.
    ///      The validator's entry remains in storage for historical queries.
    ///      The public key remains reserved and cannot be reused. The address remains
    ///      reserved unless reassigned via transferValidatorOwnership.
    ///
    /// @param validatorAddress The validator address to deactivate
    function deactivateValidator(address validatorAddress) external;

    /// @notice Rotate a validator to a new identity (owner or validator only)
    /// @dev Atomically deletes the specified validator entry and adds a new one. This is equivalent
    ///      to calling deactivateValidator followed by addValidator, but executed atomically.
    ///      Can be called by the contract owner or by the validator's own address.
    ///      The same validation rules as addValidator apply:
    ///      - The new public key must not already exist
    ///      - Ingress parseable as <ip>:<port>.
    ///      - Egress must be parseable as <ip>.
    ///      - The signature must prove ownership of the new public key
    ///      The signature must be an Ed25519 signature over:
    ///      keccak256(abi.encodePacked(bytes8(chainId), contractAddress, validatorAddress, ingress, egress))
    ///      using the namespace "TEMPO_VALIDATOR_CONFIG_V2_ROTATE_VALIDATOR".
    /// @param validatorAddress The address of the validator to rotate
    /// @param publicKey The new validator's Ed25519 communication public key
    /// @param ingress The new validator's inbound address `<ip>:<port>` for incoming connections
    /// @param egress The new validator's outbound IP address `<ip>` for firewall whitelisting
    /// @param signature Ed25519 signature (64 bytes) proving ownership of the new public key
    function rotateValidator(
        address validatorAddress,
        bytes32 publicKey,
        string calldata ingress,
        string calldata egress,
        bytes calldata signature
    ) external;

    /// @notice Update a validator's IP addresses (owner or validator only)
    /// @dev Can be called by the contract owner or by the validator's own address.
    ///      This allows validators to update their network addresses without requiring
    ///      a full rotation.
    /// @param validatorAddress The address of the validator to update
    /// @param ingress The new inbound address `<ip>:<port>` for incoming connections
    /// @param egress The new outbound IP address `<ip>` for firewall whitelisting
    function setIpAddresses(
        address validatorAddress,
        string calldata ingress,
        string calldata egress
    ) external;

    /// @notice Transfer a validator entry to a new address (owner or validator only)
    /// @dev Can be called by the contract owner or by the validator's own address.
    ///      Updates the validator's address in the lookup maps.
    ///      Reverts if the new address already exists in the validator set.
    /// @param currentAddress The current address of the validator to transfer
    /// @param newAddress The new address to assign to the validator
    function transferValidatorOwnership(address currentAddress, address newAddress) external;

    /// @notice Transfer owner of the contract (owner only)
    /// @param newOwner The new owner address
    function transferOwnership(address newOwner) external;

    /// @notice Set the epoch at which a fresh DKG ceremony will be triggered (owner only)
    /// @param epoch The epoch in which to run the fresh DKG ceremony.
    ///        Epoch N runs the ceremony, and epoch N+1 uses the new DKG polynomial.
    function setNextFullDkgCeremony(uint64 epoch) external;

    /// @notice Migrate a single validator from V1 to V2 (owner only)
    /// @dev Can be called multiple times to migrate validators one at a time.
    ///      On first call, copies owner from V1 if V2 owner is address(0).
    ///      Active V1 validators get addedAtHeight=block.height and deactivatedAtHeight=0.
    ///      Inactive V1 validators get addedAtHeight=block.height and deactivatedAtHeight=block.height at migration time.
    ///      Reverts if already initialized or already migrated.
    ///      Reverts if idx != validatorsArray.length.
    ///      Reverts if `V2.isInitialized()` (no migrations after V2 is initialized).
    /// @param idx Index of the validator in V1 validators array (must equal current validatorsArray.length)
    function migrateValidator(uint64 idx) external;

    /// @notice Initialize V2 and enable reads (owner only)
    /// @dev Should only be called after all validators have been migrated via migrateValidator.
    ///      Sets initialized=true and initializedAtHeight=block.height. After this call,
    ///      CL reads from V2 instead of V1.
    ///      Copies nextDkgCeremony from V1.
    ///      Reverts if V2 validators count < V1 validators count (ensures all validators migrated).
    ///      Reverts if validator activity does not match between contracts:
    ///      + if `V1.active == true` then `V2.deactivatedAtHeight = 0`
    ///      + if `V1.active == false` then `V2.deactivatedAtHeight > 0`
    function initializeIfMigrated() external;

    /// @notice Check if V2 has been initialized from V1
    /// @return True if initialized, false otherwise
    function isInitialized() external view returns (bool);
}
```

## Behavior

### Validator Lifecycle

Unlike V1, validators in V2 follow a strict lifecycle:

1. **Addition**: `addValidator` creates an immutable validator entry with
   `addedAtHeight` set to the current block height and `deactivatedAtHeight = 0`
2. **Active period**: Validator participates in consensus while
   `deactivatedAtHeight == 0`
3. **Deactivation**: `deactivateValidator` sets `deactivatedAtHeight` to the current block
   height
4. **Preserved**: The validator entry remains in storage forever for historical
   queries

```
┌─────────────┐     addValidator()     ┌─────────────┐   deactivateValidator()   ┌─────────────┐
│             │ ────────────────────►  │             │ ────────────────────────► │             │
│  Not Exist  │                        │   Active    │                           │ Deactivated │
│             │                        │ deactiv.=0  │                           │ deactiv.>0  │
└─────────────┘                        └─────────────┘                           └─────────────┘
                                              │                                         │
                                              │◄────────────────────────/───────────────┘
                                              │         (No transition back)
```

### Signature Verification

When adding a validator, the caller must provide an Ed25519 signature proving ownership of the public key. The
signature is checked over the a full message containing: the length of the namespace in bytes, the namespace, and a
32-bytes hashed message.

**Namespace:** `b"TEMPO_VALIDATOR_CONFIG_V2_ADD_VALIDATOR"`

**Message:**

```
message = keccak256(abi.encodePacked(
    bytes8(chainId),      // uint64: Prevents cross-chain replay
    contractAddress,      // address: Prevents cross-contract replay
    validatorAddress,     // address: Binds to specific validator address
    ingress,              // string: Binds network configuration
    egress                // string: Binds network configuration
))
```

The Ed25519 signature is computed over the message using the namespace parameter
(see commonware's [signing scheme](https://github.com/commonwarexyz/monorepo/blob/abb883b4a8b42b362d4003b510bd644361eb3953/cryptography/src/ed25519/scheme.rs#L38-L40)
and [union format](https://github.com/commonwarexyz/monorepo/blob/abb883b4a8b42b362d4003b510bd644361eb3953/utils/src/lib.rs#L166-L174)).

For validator rotations, the namespace `b"TEMPO_VALIDATOR_CONFIG_V2_ROTATE_VALIDATOR"` is used instead.

### Determining Active Validators

Reading this contract alone is **not sufficient** to determine who the active validators (signers) are during a given epoch. The contract only records which validators are *eligible* to participate in DKG ceremonies—it does not record DKG outcomes.

To determine the actual validators for epoch `E+1`:

1. Read the DKG outcome from block `boundary(E)`
2. The DKG outcome contains the Ed25519 public keys of successful DKG players
3. Match these public keys against the contract via `validatorByPublicKey()` to obtain validator addresses and IP addresses

```
activeValidators(E+1) = dkgOutcome(boundary(E)).players.map(pubkey =>
    contract.validatorByPublicKey(pubkey)
)
```

This distinction matters because:

* The DKG can fail, reverting to the previous DKG outcome (for example, not all
  eligible players may successfully participate in the DKG due to network
  issues, crashes, etc.)
* The DKG outcome is the authoritative record of who holds valid key shares
* Only validators with valid shares can produce valid signatures in epoch `E+1`

### Address Validation

* **ingress**: Must be in `<ip>:<port>` format.
* **egress**: Must be in `<ip>` format.

Both IPv4 and IPv6 addresses are supported. For ingress, IPv6 addresses must be
enclosed in brackets: `[2001:db8::1]:8080`.

### IP Address Uniqueness

Only the ingress IP address must be unique among active validators:

* No two active validators can have the same ingress IP
* Egress addresses have no uniqueness constraint
* Deactivated validators excluded from checks, IP reuse is allowed after deactivation

**Implementation**: Tracked via storage mapping (`active_ingress_ips: Mapping<B256, bool>`) where keys are `keccak256(ingressIp)` for O(1) validation.

**Enforcement**:

* `migrateValidator`: Rejects if ingress IP already in use by active validators
* `addValidator`: Rejects if ingress IP already in use
* `rotateValidator`: Rejects if new ingress IP already in use (after removing old)
* `setIpAddresses`: Rejects if new ingress IP already in use (after removing old)

### Consensus Layer Behavior

**IP Address Changes**: When a validator's IP address changes via `setIpAddresses`, the consensus layer is expected to update its peer list on the next finalized block.

**Validator Addition and Deactivation**: When validators are added or deleted (this also applies to rotation),
there is no warmup period: deactivated validators are immediately removed from the set of players on the next epoch,
while activated validators are immediately added on the next epoch. This means that compared to validator config V1,
there is no cooldown and no warmup period.

**DKG Player Selection**: The consensus layer determines DKG players for epoch `E+1` by reading state at `boundary(E)` and filtering:

```
players(E+1) = validators.filter(v =>
    v.addedAtHeight <= boundary(E) &&
    (v.deactivatedAtHeight == 0 || v.deactivatedAtHeight > boundary(E))
)
```

This enables nodes to reconstruct DKG player sets without accessing historical account state—critical for node recovery and late-joining validators.

### Uniqueness Constraints

Both the validator address and public key must be globally unique across all
validators (including deleted ones):

* `AddressAlreadyHasValidator`: Reverts if the address has ever been registered
* `PublicKeyAlreadyExists`: Reverts if the public key has ever been registered

This ensures historical queries always return consistent results.

## Storage Layout

The contract stores the following state:

* `owner`: Contract owner address
* `initialized`: Whether V2 has been initialized from V1 (boolean)
* `initializedAtHeight`: Block height when V2 was initialized (uint64)
* `validatorsArray`: Append-only array of all validators (Validator\[])
* `addressToIndex`: Mapping from validator address to array index (mapping)
* `pubkeyToIndex`: Mapping from public key to array index (mapping)
* `nextDkgCeremony`: Next full DKG ceremony epoch (uint64)
* `active_ingress_ips`: Mapping from `keccak256(ingressIp)` to bool (Mapping\<B256, bool>)

Implementation details such as slot packing are left to the implementation.

## Differences from V1

| Aspect | V1 | V2 |
|--------|----|----|
| Status field | `active: bool` | `deactivatedAtHeight: uint64` (0 = active) |
| Creation tracking | None | `addedAtHeight: uint64` |
| Mutability | Mutable via `updateValidator()` | Immutable after creation |
| Deletion | Sets `active = false` | Sets `deactivatedAtHeight = block.number` |
| Re-registration | Allowed after deletion | Pubkey reserved forever; address reassignable via `transferValidatorOwnership` |
| Key ownership | Not verified | Ed25519 signature required |
| Historical queries | Requires historical state | Filter `getAllValidators()` by `addedAtHeight`/`deactivatedAtHeight` |
| Uniqueness | Address only | Address AND public key |
| Precompile address | `0xCCCC...0000` | `0xCCCC...0001` |

***

# Invariants

The following invariants must always hold:

1. **Append-only array**: The `validatorsArray` length only increases; it never
   decreases.

2. **Immutable identity**: Once a validator is added, its `publicKey`,
   `index`, and `addedAtHeight` fields never change. The `ingress` and `egress`
   fields can be updated via `setIpAddresses`. `validatorAddress` can only be
   changed by the contract owner.

3. **Address update**: `transferValidatorOwnership` updates the address of an
   existing validator without changing any other fields. This can be called
   by the contract owner or by the validator themselves and is required for
   post-migration fixes: validator contract v1 contains unusable dummy addresses
   that are not usable.

4. **Delete-once**: A validator's `deactivatedAtHeight` can only transition from 0
   to a non-zero value, never back to 0 or to a different non-zero value.

5. **Unique addresses**: No two validators (including deleted ones) can have the
   same `validatorAddress`.

6. **Unique public keys**: No two validators (including deleted ones) can have
   the same `publicKey`.

7. **Non-zero public keys**: All validators must have a non-zero `publicKey`.

8. **Monotonic index**: Validator `index` equals its position in
   `validatorsArray` and equals `validatorCount - 1` at creation time.

9. **Historical consistency**: For any height H, the active validator set
   consists of validators where `addedAtHeight &lt;= H && (deactivatedAtHeight == 0 ||
   deactivatedAtHeight &gt; H)`. Validators with `addedAtHeight == deactivatedAtHeight` are
   never considered active.

10. **Signature binding**: The signature message includes `chainId`,
    `contractAddress`, `validatorAddress`, `ingress`, and
    `egress`, preventing replay across chains, contracts, or parameter
    changes.

11. **Owner authorization**: Only the owner can call `addValidator`,
    `transferOwnership`, `migrateValidator`, `initializeIfMigrated`, and
    `setNextFullDkgCeremony`.

12. **Dual authorization**:
    * `rotateValidator` and `transferValidatorOwnership` can be called by either
      the owner or the validator itself. These functions require initialization.
    * `deactivateValidator` and `setIpAddresses` can be called by the owner or the validator itself.
      These functions do NOT require initialization and can be used during migration.

13. **Initialized once**: The `initialized` bit (bit 255 of slot 0) can only
    transition from 0 to 1, never back to 0.

14. **Atomic rotation**: `rotateValidator` atomically deletes the old validator
    (setting its `deactivatedAtHeight`), adds a new validator entry, and updates
    the `addresses[validatorAddress]` mapping to point to the new entry. Both
    operations occur in the same transaction with the same block height.

***

# Migration from V1

This section describes the migration strategy from ValidatorConfig V1 to V2.

## Overview

The migration uses a two-pronged approach:

1. **New hardfork**: Timestamp-based activation
2. **Manual migration**: Admin migrates validators one at a time, then calls
   `initializeIfMigrated()` to flip the flag. CL reads from V1 until the flag is set.

## Hardfork-Based Switching

The CL determines which contract to read based on:

1. Whether \<Hardfork> hardfork is active (timestamp-based)
2. Whether V2 is initialized (reads `isInitialized()` from V2)

```
if chainspec.is_<hardfork>_active_at_timestamp(block.timestamp) {
    if v2.isInitialized() {
        read_from_contract_v2_at_height(height)
    } else {
        read_from_contract_at_height(height)  // V1 until migration complete
    }
} else {
    read_from_contract_at_height(height)  // V1
}
```

This ensures:

* All nodes switch deterministically at hardfork time
* CL continues reading V1 until admin completes migration and flips the flag

## Manual Migration

V2 uses manual migration where the admin explicitly migrates validators one at a
time and then calls `initializeIfMigrated()` to flip the `initialized` flag. The
`initialized` bit (bit 255 of slot 0) tracks whether migration is complete.

### Motivation

The gas limit per transaction is 30 million as of [TIP-1010](./tip-1010.mdx#main-transaction-gas-limit),
with an `SSTORE` being 250 thousand gas as per [TIP-1000](./tip-1000.mdx#gas-schedule-summary).
This means migration of a single validator incurs at least 1 million gas cost, only
leaving enough room to migrate less than 30 validator entries at a time.

This runs the risk of potentially not leaving enough space to migrate all validators
in one go and would require logic to run several migrations. This would require
manual intervention anyway, and require extra logic in the precompile to check
which validators have already been migrated.

### Validator Deactivation During Migration

During the migration window (after `migrateValidator` calls begin but before `initializeIfMigrated()` is called):

* **Deactivation is allowed**: Both validators (self-deactivation) and the owner can call `deactivateValidator()` before initialization
* This allows validators to opt-out and the owner to manage the validator set during the migration window

Unlike other mutating operations (`addValidator`, `rotateValidator`, `transferValidatorOwnership`),
`deactivateValidator` and `setIpAddresses` do not require initialization. This design choice allows
flexible validator management and IP updates during the migration phase.

### CL Read Behavior

The CL checks `v2.isInitialized()` to determine which contract to read:

* **`initialized == false`**: CL reads from V1
* **`initialized == true`**: CL reads from V2

This is handled entirely in the CL logic, not in the V2 precompile. The V2
precompile does NOT proxy reads to V1.

### Migration Functions (Owner Only)

**`migrateValidator(idx)`**:

* Reverts if `isInitialized() == true`
* Reverts if `idx != validatorsArray.length` (ensures sequential migration)
* On first call (when `validatorsArray.length == 0`), copies `owner` from V1 if V2 owner is `address(0)`
* Reads the validator from V1 at index `idx`
* Creates a V2 validator entry with:
  * `publicKey`: copied from V1
  * `validatorAddress`: copied from V1
  * `ingress`: copied from V1 `inboundAddress`
  * `egress`: copied from V1 `outboundAddress`
  * `index`: set to `idx`
  * `addedAtHeight`: `block.height`
  * `deactivatedAtHeight`: set to `0` if V1 `active == true`, otherwise `block.height`
* Adds to `validatorsArray`
* Populates lookup maps (`validators[validatorAddress]`, `pubkeyToIndex[pubkey]`)

**`initializeIfMigrated()`**:

* Reverts if `validatorsArray.length < V1.getAllValidators().length` (ensures all validators migrated)
* Copies `nextDkgCeremony` from V1 to V2
* Sets `initialized = true` (bit 255 of slot 0)
* After this call, CL reads from V2 instead of V1

**`transferValidatorOwnership(validatorAddress, newAddress)`**:

* Reverts if caller is not owner and not the validator
* Reverts if `currentAddress` does not exist
* Reverts if `newAddress` already exists in the validator set
* Updates the validator with the new address
* Updates lookup maps: removes old address entry, adds new address entry

```solidity
// V1 interface used during migration
interface IValidatorConfigV1 {
    struct Validator {
        bytes32 publicKey;
        bool active;
        uint64 index;
        address validatorAddress;
        string inboundAddress;
        string outboundAddress;
    }

    function getAllValidators() external view returns (Validator[] memory);
    function getNextFullDkgCeremony() external view returns (uint64);
    function owner() external view returns (address);
}
```

### Properties

* **Per-validator migration**: Each validator is migrated with a separate tx
* **Owner controlled**: Only admin can migrate and initialize
* **Validator address copied**: The V2 validator address is copied from V1
* **Address changeable post-migration**: Owner or validator can update validator addresses via `transferValidatorOwnership`
* **No signatures required**: V1 validators are imported without Ed25519 signatures
  (they were already validated in V1)
* **All validators imported**: Both active and inactive V1 validators are
  imported; active ones have `addedAtHeight == block.height` and `deactivatedAtHeight == 0`,
  inactive ones have `addedAtHeight == deactivatedAtHeight == block.height`.
* **Initialize validates migration**: `initializeIfMigrated()` reverts if not
  all V1 validators have been migrated

## Timeline

```
Before Fork           Post-Fork (V2 not init)    Admin Migration           After initializeIfMigrated()
     │                      │                          │                          │
     │  CL reads V1         │  CL reads V1             │  migrateValidator()      │  CL reads V2
     │                      │  (isInitialized=false)   │  (one tx per validator)  │  isInitialized=true
     │                      │                          │                          │
─────┴──────────────────────┴──────────────────────────┴──────────────────────────┴───────────────►
                            │                          │                          │
                      hardforkTime           migrateValidator() x N         initializeIfMigrated()
```

## Migration Steps

### For Existing Networks (testnet, mainnet)

Existing networks are defined as those with hardfork\_timestamp > timestamp\_at\_genesis

1. **Release new node software** with \<Hardfork> hardfork support
2. **Schedule the fork** by updating chainspec with target `hardforkTime`
3. **At fork activation**: CL reads from V1 (since `isInitialized() == false`)
4. **Admin migrates validators** by calling `migrateValidator(idx)` for each validator
   * One transaction per validator
   * Example: `migrateValidator(0)`, `migrateValidator(1)`, `migrateValidator(2)`, etc.
   * Validator addresses are copied from V1
5. **Admin calls `initializeIfMigrated()`**
   * Sets `initialized = true`
   * CL now reads from V2
6. **Post-migration**: All reads/writes use V2 state directly

**Important**: Complete migration before an epoch boundary to avoid disrupting DKG.

### For New Networks

New networks are defined as those that have the V2 validator config contract at genesis.
In these cases, the V1 validator config contract is not required if validators are set up in V2 state.

1. Call `initializeIfMigrated()` to set `initialized = true` and `initializeAtHeight = 0`.
2. Call `addValidator()` for each initial validator
3. Set `<hardforkTime> = 0` to activate V2 immediately
4. V1 Validator Config contract/precompile is not necessary in this flow

***

## Test Cases

The test suite must cover:

### Basic Operations

1. **Add validator**: Successfully adds a validator with valid signature
2. **Delete validator**: Successfully marks validator as deleted
3. **Change owner**: Successfully transfers ownership
4. **Set next DKG ceremony**: Successfully sets the epoch
5. **Rotate validator**: Successfully deletes old validator and adds new one atomically

### Query Functions

1. **getAllValidators**: Returns all validators including deleted with correct
   `addedAtHeight` and `deactivatedAtHeight`
2. **getActiveValidators**: Returns only validators with `deactivatedAtHeight == 0`
   (note: validators with `addedAtHeight == deactivatedAtHeight` are excluded)
3. **validatorByPublicKey**: Returns validator by public key lookup
4. **validatorCount**: Returns total count including deleted

### Error Conditions

1. **Unauthorized**: Non-owner cannot call protected functions
2. **ValidatorAlreadyExists**: Cannot re-add same address
3. **PublicKeyAlreadyExists**: Cannot re-use same public key
4. **ValidatorNotFound**: Cannot query/delete non-existent validator
5. **ValidatorAlreadyDeleted**: Cannot delete twice
6. **InvalidPublicKey**: Rejects zero public key
7. **InvalidSignature**: Rejects wrong signature, wrong length, wrong signer
8. **IngressAlreadyExists**: Cannot use ingress IP already in use by active validator (even with different port)

### rotateValidator

1. **rotateValidator by owner**: Owner can rotate any active validator
2. **rotateValidator by validator**: Validator can rotate themselves
3. **rotateValidator unauthorized**: Non-owner and non-validator cannot rotate
4. **rotateValidator already deleted**: Cannot rotate already-deleted validator
5. **rotateValidator new pubkey exists**: Cannot rotate to existing public key
6. **rotateValidator invalid signature**: Rejects invalid signature for rotation
7. **rotateValidator validator not found**: Reverts if validatorAddress does not exist
8. **rotateValidator atomicity**: Old validator is deleted and new one added in same block
9. **rotateValidator preserves index**: New validator gets next available index, old index remains deleted

### Address Validation

1. **Valid IPv4:port**: Accepts `192.168.1.1:8080`
2. **Valid IPv6:port**: Accepts `[2001:db8::1]:8080`
3. **Invalid format**: Rejects malformed addresses

### Historical Filtering (Caller-side)

1. **addedAtHeight correctness**: Validators have correct `addedAtHeight` set
    at creation
2. **deactivatedAtHeight correctness**: Deleted validators have correct
    `deactivatedAtHeight` set
3. **Filter logic**: Caller can correctly filter by
    `addedAtHeight <= H && (deactivatedAtHeight == 0 || deactivatedAtHeight > H)`

### Manual Migration

1. **migrateValidator imports validator**: Calling `migrateValidator(i)`
    correctly imports validator at index i from V1 with the same address
2. **migrateValidator copies address from V1**: The V2 validator uses the address from V1
3. **migrateValidator reverts on duplicate**: Calling `migrateValidator(i)` reverts
    if `i != validatorsArray.length`
4. **migrateValidator reverts if initialized**: Calling `migrateValidator` reverts
    if `isInitialized() == true`
5. **migrateValidator owner only**: Non-owner cannot call `migrateValidator`
6. **All validators imported on migration**: Both V1 active and inactive validators
    are imported; active ones have `addedAtHeight > 0` and `deactivatedAtHeight == 0`,
    inactive ones have `addedAtHeight == deactivatedAtHeight > 0`.
7. **addedAtHeight set correctly**: All migrated validators have `addedAtHeight > 0` (block.height at migration time).
8. **deactivatedAtHeight set correctly**: Active validators have `deactivatedAtHeight == 0`.
    Inactive validators have `addedAtHeight == deactivatedAtHeight > 0` at migration time.
9. **initialize sets flag**: After `initializeIfMigrated()`, `isInitialized()` returns true
10. **migrateValidator copies owner**: V2 `owner()` matches V1 after first `migrateValidator` call
11. **initialize copies DKG ceremony**: V2 `getNextFullDkgCeremony()` matches V1
    after `initializeIfMigrated()`
12. **initialize owner only**: Non-owner cannot call `initialize`
13. **isInitialized returns correct value**: Returns false before initialize, true after
14. **Writes blocked before init**: `addValidator`, `rotateValidator`, `transferValidatorOwnership`
15. **initialize reverts if not all migrated**: `initializeIfMigrated()` reverts if
    `validatorsArray.length < V1.getAllValidators().length`

### transferValidatorOwnership

1. **transferValidatorOwnership by owner**: Owner can transfer any validator to a new address
2. **transferValidatorOwnership by validator**: Validator can transfer themselves to a new address
3. **transferValidatorOwnership unauthorized**: Non-owner and non-validator cannot transfer
4. **transferValidatorOwnership reverts on invalid validator**: Reverts if `validatorAddress` does not exist
5. **transferValidatorOwnership reverts on duplicate address**: Reverts if `newAddress` already exists
6. **transferValidatorOwnership updates lookup maps**: Old address is removed, new address is added to lookup

### setIpAddresses

1. **setIpAddresses by owner**: Owner can update any validator's IP addresses
2. **setIpAddresses by validator**: Validator can update their own IP addresses
3. **setIpAddresses unauthorized**: Non-owner and non-validator cannot update IP addresses
4. **setIpAddresses reverts on invalid validator**: Reverts if validator does not exist
5. **setIpAddresses reverts on deactivated validator**: Reverts if validator is already deactivated
6. **setIpAddresses validates format**: Rejects invalid `<ip>:<port>` format
7. **setIpAddresses before init (self)**: Validator can update their own IPs before initialization
8. **setIpAddresses before init (owner)**: Owner can update validator IPs before initialization
9. **deactivateValidator before init (self)**: Validator can deactivate themselves before initialization
10. **deactivateValidator before init (owner)**: Owner can deactivate validators before initialization

***

# Security Issues

## Migration Timing

The migration must be completed (including `initializeIfMigrated()`) before an epoch
boundary to avoid disrupting DKG. The admin should:

1. Schedule migration during a period with no imminent epoch transitions
2. Monitor the current epoch and time remaining
3. Complete all `migrateValidator` calls and `initializeIfMigrated()` with sufficient time buffer

# Account Keychain Precompile

**Address:** `0xAAAAAAAA00000000000000000000000000000000`

## Overview

The Account Keychain precompile manages authorized Access Keys for accounts, enabling Root Keys (e.g., passkeys) to provision scoped "secondary" Access Keys with expiry timestamps and per-TIP20 token spending limits.

## Motivation

The Tempo Transaction type unlocks a number of new signature schemes, including WebAuthn (Passkeys). However, for an Account using a Passkey as its Root Key, the sender will subsequently be prompted with passkey prompts for every signature request. This can be a poor user experience for highly interactive or multi-step flows. Additionally, users would also see "Sign In" copy in prompts for signing transactions which is confusing. This proposal introduces the concept of the Root Key being able to provision a (scoped) Access Key that can be used for subsequent transactions, without the need for repetitive end-user prompting.

## Concepts

### Access Keys

Access Keys are secondary signing keys authorized by an account's Root Key. They can sign transactions on behalf of the account with the following restrictions:

* **Expiry**: Unix timestamp when the key becomes invalid (0 = never expires, non-zero values must be > current timestamp)
* **Spending Limits**: Per-TIP20 token limits that deplete as tokens are spent
  * Limits deplete as tokens are spent and can be updated by the Root Key via `updateSpendingLimit()`
  * Spending limits only apply to TIP20 `transfer()`, `transferWithMemo()`, `approve()`, and `startReward()` calls
  * Spending limits only apply when `msg.sender == tx.origin` (direct EOA calls, not contract calls)
  * Native value transfers and `transferFrom()` are NOT limited
* **Privilege Restrictions**: Cannot authorize new keys or modify their own limits

### Authorization Hierarchy

The protocol enforces a strict hierarchy at validation time:

1. **Root Key**: The account's main key (derived from the account address)
   * Can call all precompile functions
   * Has no spending limits

2. **Access Keys**: Secondary authorized keys
   * Cannot call mutable precompile functions (only view functions are allowed)
   * Subject to per-TIP20 token spending limits
   * Can have expiry timestamps

## Storage

The precompile uses a `keyId` (address) to uniquely identify each access key for an account.

**Storage Mappings:**

* `keys[account][keyId]` → Packed `AuthorizedKey` struct (signature type, expiry, enforce\_limits, is\_revoked)
* `spendingLimits[keccak256(account || keyId)][token]` → Remaining spending amount for a specific token (uint256)
* `transactionKey` → Transient storage for the key ID that signed the current transaction (slot 0)

**AuthorizedKey Storage Layout (packed into single slot):**

* byte 0: signature\_type (u8)
* bytes 1-8: expiry (u64, little-endian)
* byte 9: enforce\_limits (bool)
* byte 10: is\_revoked (bool)

## Interface

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

interface IAccountKeychain {
    /*//////////////////////////////////////////////////////////////
                                STRUCTS
    //////////////////////////////////////////////////////////////*/

    /// @notice Signature type
    enum SignatureType {
        Secp256k1,
        P256,
        WebAuthn,
    }

    /// @notice Token spending limit structure
    struct TokenLimit {
        address token;   // TIP20 token address
        uint256 amount;  // Spending limit amount
    }

    /// @notice Key information structure
    struct KeyInfo {
        SignatureType signatureType; // Signature type of the key
        address keyId;               // The key identifier
        uint64 expiry;               // Unix timestamp when key expires (0 = never)
        bool enforceLimits;          // Whether spending limits are enforced for this key
        bool isRevoked;              // Whether this key has been revoked
    }

    /*//////////////////////////////////////////////////////////////
                                EVENTS
    //////////////////////////////////////////////////////////////*/

    /// @notice Emitted when a new key is authorized
    event KeyAuthorized(
        address indexed account,
        address indexed publicKey,
        uint8 signatureType,
        uint64 expiry
    );

    /// @notice Emitted when a key is revoked
    event KeyRevoked(address indexed account, address indexed publicKey);

    /// @notice Emitted when a spending limit is updated
    event SpendingLimitUpdated(
        address indexed account,
        address indexed publicKey,
        address indexed token,
        uint256 newLimit
    );

    /*//////////////////////////////////////////////////////////////
                                ERRORS
    //////////////////////////////////////////////////////////////*/

    error KeyAlreadyExists();
    error KeyNotFound();
    error KeyInactive();
    error KeyExpired();
    error KeyAlreadyRevoked();
    error SpendingLimitExceeded();
    error InvalidSignatureType();
    error ZeroPublicKey();
    error UnauthorizedCaller();

    /*//////////////////////////////////////////////////////////////
                        MANAGEMENT FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    /**
     * @notice Authorize a new key for the caller's account
     * @dev MUST only be called in transactions signed by the Root Key
     *      The protocol enforces this restriction by checking transactionKey[msg.sender]
     * @param keyId The key identifier (address) to authorize
     * @param signatureType Signature type of the key (0: Secp256k1, 1: P256, 2: WebAuthn)
     * @param expiry Unix timestamp when key expires (MUST be > current_timestamp, or 0 for never expires)
     * @param enforceLimits Whether to enforce spending limits for this key
     * @param limits Initial spending limits for tokens (only used if enforceLimits is true)
     */
    function authorizeKey(
        address keyId,
        SignatureType signatureType,
        uint64 expiry,
        bool enforceLimits,
        TokenLimit[] calldata limits
    ) external;

    /**
     * @notice Revoke an authorized key
     * @dev MUST only be called in transactions signed by the Root Key
     *      The protocol enforces this restriction by checking transactionKey[msg.sender]
     * @param keyId The key ID to revoke
     */
    function revokeKey(address keyId) external;

    /**
     * @notice Update spending limit for a specific token on an authorized key
     * @dev MUST only be called in transactions signed by the Root Key
     *      The protocol enforces this restriction by checking transactionKey[msg.sender]
     * @param keyId The key ID to update
     * @param token The token address
     * @param newLimit The new spending limit
     */
    function updateSpendingLimit(
        address keyId,
        address token,
        uint256 newLimit
    ) external;

    /*//////////////////////////////////////////////////////////////
                        VIEW FUNCTIONS
    //////////////////////////////////////////////////////////////*/

    /**
     * @notice Get key information
     * @param account The account address
     * @param keyId The key ID
     * @return Key information (returns default values if key doesn't exist)
     */
    function getKey(
        address account,
        address keyId
    ) external view returns (KeyInfo memory);

    /**
     * @notice Get remaining spending limit for a key-token pair
     * @param account The account address
     * @param keyId The key ID
     * @param token The token address
     * @return Remaining spending amount
     */
    function getRemainingLimit(
        address account,
        address keyId,
        address token
    ) external view returns (uint256);

    /**
     * @notice Get the transaction key used in the current transaction
     * @dev Returns Address::ZERO if the Root Key is being used
     * @return The key ID that signed the transaction
     */
    function getTransactionKey() external view returns (address);
}
```

## Behavior

### Key Authorization

* Creates a new key entry with the specified `signatureType`, `expiry`, `enforceLimits`, and `isRevoked` set to `false`
* If `enforceLimits` is `true`, initializes spending limits for each specified token
* Emits `KeyAuthorized` event

**Requirements:**

* MUST be called by Root Key only (verified by checking `transactionKey[msg.sender] == 0`)
* `keyId` MUST NOT be `address(0)` (reverts with `ZeroPublicKey`)
* `keyId` MUST NOT already be authorized with `expiry > 0` (reverts with `KeyAlreadyExists`)
* `keyId` MUST NOT have been previously revoked (reverts with `KeyAlreadyRevoked` - prevents replay attacks)
* `signatureType` MUST be `0` (Secp256k1), `1` (P256), or `2` (WebAuthn) (reverts with `InvalidSignatureType`)
* `expiry` CAN be any value (0 means never expires, stored as-is)
* `enforceLimits` determines whether spending limits are enforced for this key
* `limits` are only processed if `enforceLimits` is `true`

### Key Revocation

* Marks the key as revoked by setting `isRevoked` to `true` and `expiry` to `0`
* Once revoked, a `keyId` can NEVER be re-authorized for this account (prevents replay attacks)
* Key can no longer be used for transactions
* Emits `KeyRevoked` event

**Requirements:**

* MUST be called by Root Key only (verified by checking `transactionKey[msg.sender] == 0`)
* `keyId` MUST exist (key with `expiry > 0`) (reverts with `KeyNotFound` if not found)

### Spending Limit Update

* Updates the spending limit for a specific token on an authorized key
* Allows Root Key to modify limits without revoking and re-authorizing the key
* If the key had unlimited spending (`enforceLimits == false`), enables limits
* Sets the new remaining limit to `newLimit`
* Emits `SpendingLimitUpdated` event

**Requirements:**

* MUST be called by Root Key only (verified by checking `transactionKey[msg.sender] == 0`)
* `keyId` MUST exist and not be revoked (reverts with `KeyNotFound` or `KeyAlreadyRevoked`)
* `keyId` MUST not be expired (reverts with `KeyExpired`)

## Security Considerations

### Access Key Storage

Access Keys should be securely stored to prevent unauthorized access:

* **Device and Application Scoping**: Access Keys SHOULD be scoped to a specific client device AND application combination. Access Keys SHOULD NOT be shared between devices or applications, even if they belong to the same user.
* **Non-Extractable Keys**: Access Keys SHOULD be generated and stored in a non-extractable format to prevent theft. For example, use WebCrypto API with `extractable: false` when generating Keys in web browsers.
* **Secure Storage**: Private Keys MUST never be stored in plaintext. Private Keys SHOULD be encrypted and stored in a secure manner. For web applications, use browser-native secure storage mechanisms like IndexedDB with non-extractable WebCrypto keys rather than storing raw key material.

### Privilege Escalation Prevention

Access Keys cannot escalate their own privileges because:

1. Management functions (`authorizeKey`, `revokeKey`, `updateSpendingLimit`) are restricted to Root Key transactions
2. The protocol sets `transactionKey[account]` during transaction validation to indicate which key signed the transaction
3. These management functions check that `transactionKey[msg.sender] == 0` (Root Key) before executing
4. Access Keys cannot bypass this check - transactions will revert with `UnauthorizedCaller`

### Spending Limit Enforcement

* Spending limits are only enforced if `enforceLimits == true` for the key
* Keys with `enforceLimits == false` have unlimited spending (no limits checked)
* Spending limits are enforced by the protocol internally calling `verify_and_update_spending()` during execution
* Limits are per-TIP20 token and deplete as TIP20 tokens are spent
* Spending limits only track TIP20 token transfers (via `transfer` and `transferWithMemo`) and approvals (via `approve`)
* For approvals: only increases in approval amount count against the spending limit. This means approvals indirectly control `transferFrom` spending, since `transferFrom` requires a prior approval
* Non-TIP20 asset movements (ETH, NFTs) are not subject to spending limits
* Root keys (`keyId == address(0)`) have no spending limits - the function returns immediately
* Failed limit checks revert the entire transaction with `SpendingLimitExceeded`

### Key Expiry

* Keys with `expiry > 0` are checked against the current timestamp during validation
* Expired keys cause transaction rejection with `KeyExpired` error (checked via `validate_keychain_authorization()`)
* `expiry == 0` means the key never expires
* Expiry is checked as: `current_timestamp >= expiry` (key is expired when current time reaches or exceeds expiry)

## Usage Patterns

### First-Time Access Key Authorization

1. User signs Passkey prompt → signs over `key_authorization` for a new Access Key (e.g., WebCrypto P256 key)
2. User's Access Key signs the transaction
3. Transaction includes the `key_authorization` AND the Access Key `signature`
4. Protocol validates Passkey signature on `key_authorization`, sets `transactionKey[account] = 0`, calls `AccountKeychain.authorizeKey()`, then validates Access Key signature
5. Transaction executes with Access Key's spending limits enforced via internal `verify_and_update_spending()`

### Subsequent Access Key Usage

1. User's Access Key signs the transaction (no `key_authorization` needed)
2. Protocol validates the Access Key via `validate_keychain_authorization()`, sets `transactionKey[account] = keyId`
3. Transaction executes with spending limit enforcement via internal `verify_and_update_spending()`

### Root Key Revoking an Access Key

1. User signs Passkey prompt → signs transaction calling `revokeKey(keyId)`
2. Transaction executes, marking the Access Key as inactive
3. Future transactions signed by that Access Key will be rejected

# EIP-4337 and Tempo Transactions

EIP-4337 introduced account abstraction to Ethereum through a system of bundlers, paymasters, and an EntryPoint contract. Tempo Transactions achieve the same goals through protocol-native features that require no additional infrastructure.

## EIP-4337 Design Goals

EIP-4337 enables several key capabilities for Ethereum accounts:

* **Fee sponsorship**: Third parties can pay gas fees on behalf of users
* **Batched operations**: Multiple calls can execute atomically in one transaction
* **Alternative signatures**: Accounts can use signature schemes beyond secp256k1
* **Custom validation**: Accounts can define arbitrary validation logic

## How Tempo Achieves These Goals

Tempo Transactions provide these capabilities at the protocol level.

### Fee Sponsorship

EIP-4337 requires deploying a Paymaster contract, funding it with ETH, and running or paying for bundler infrastructure. The Paymaster validates sponsorship requests and the bundler aggregates UserOperations.

Tempo Transactions include a `fee_payer_signature` field directly in the transaction. A sponsor signs the transaction to agree to pay fees. The protocol validates both signatures and deducts fees from the sponsor. No contracts or infrastructure are required. See the [fee sponsorship guide](/guide/payments/sponsor-user-fees) for implementation details.

### Batched Operations

EIP-4337 bundles multiple UserOperations through an external bundler service. Each UserOperation can contain one call.

Tempo Transactions include a native `calls` array. Multiple contract calls execute atomically in a single transaction. The protocol handles execution directly without external services.

### Alternative Signatures

EIP-4337 requires deploying a custom validation contract for each signature scheme. The contract must implement signature verification logic.

Tempo Transactions natively support secp256k1, P256, and WebAuthn signatures. The protocol verifies these signatures directly. Passkey authentication works without custom contracts. See the [passkey accounts guide](/guide/use-accounts/embed-passkeys) for implementation details.

### Gas Token Flexibility

EIP-4337 Paymasters can accept alternative tokens but must convert them to ETH internally.

Tempo Transactions pay fees directly in any USD stablecoin that has liquidity on the Fee AMM. No conversion infrastructure is needed. See the [stablecoin fees guide](/guide/payments/pay-fees-in-any-stablecoin) for implementation details.

## Integration Comparison

| Aspect | EIP-4337 | Tempo Transactions |
|--------|----------|-------------------|
| Contracts to deploy | EntryPoint, Paymaster, Account | None required |
| Infrastructure to run | Bundler service | None required |
| Fee payment | ETH via Paymaster | Any USD stablecoin |
| Signature verification | Custom validation contract | Protocol-native |

## When to Use EIP-4337 on Tempo

Tempo has the ERC-4337 EntryPoint contract deployed for projects that require compatibility with existing 4337 tooling. Consider using native Tempo Transactions for lower gas costs and simpler integration.

## Getting Started

To start using Tempo Transactions, see the [Tempo Transactions guide](/guide/tempo-transaction) for SDK integration in TypeScript, Rust, Go, and Python. For the full technical specification, see the [Tempo Transaction Specification](/protocol/transactions/spec-tempo-transaction).

# EIP-7702 and Tempo Transactions

EIP-7702 allows EOAs to delegate to smart contract code temporarily within a transaction. Tempo Transactions build on this foundation and extend it with additional capabilities.

## EIP-7702 Design Goals

EIP-7702 enables EOAs to:

* **Delegate to contract code**: An EOA can execute as if it were a smart contract
* **Batch transactions**: Through delegation to a batching contract
* **Maintain EOA properties**: The account remains an EOA after the transaction

## How Tempo Extends EIP-7702

Tempo Transactions support EIP-7702 style delegation through the `aa_authorization_list` field. This field follows EIP-7702 semantics for delegation and execution.

### Extended Signature Support

EIP-7702 on Ethereum only supports secp256k1 signatures for the authorization.

Tempo extends this to support all Tempo signature types. Authorizations can be signed with secp256k1, P256, or WebAuthn. This enables delegation from passkey-based accounts.

### Native Features Beyond Delegation

EIP-7702 provides delegation as a building block. Applications must implement higher-level features through the delegated contract.

Tempo Transactions include these features natively:

* **Fee sponsorship**: Built into the transaction type, not requiring delegation. See the [fee sponsorship guide](/guide/payments/sponsor-user-fees).
* **Scheduled execution**: Native `validAfter` and `validBefore` timestamp windows for time-bounded transactions.
* **Parallelizable nonces**: Multiple nonce keys for concurrent transactions. See the [parallel transactions guide](/guide/payments/send-parallel-transactions).
* **Access keys**: Delegate signing to secondary keys with configurable permissions. See the [Account Keychain specification](/protocol/transactions/AccountKeychain).

### Combining Delegation with Native Features

Tempo Transactions can use EIP-7702 delegation alongside native features. An application can delegate an EOA to contract code while also using fee sponsorship and batched calls from the protocol.

## Feature Comparison

| Feature | EIP-7702 | Tempo Transactions |
|---------|----------|-------------------|
| EOA delegation | Yes | Yes |
| Signature schemes | secp256k1 only | secp256k1, P256, WebAuthn |
| Fee sponsorship | Via delegated contract | Native |
| Batching | Via delegated contract | Native |
| Scheduled execution | Not available | Native |
| Concurrent nonces | Not available | Native |

## Implementation

The `aa_authorization_list` field in Tempo Transactions contains authorizations that follow EIP-7702 structure. Each authorization delegates an account to a specified implementation contract and is signed by the account authority.

For full details on the authorization format, see the [Tempo Transaction Specification](/protocol/transactions/spec-tempo-transaction).

## Getting Started

To start using Tempo Transactions, see the [Tempo Transactions guide](/guide/tempo-transaction) for SDK integration in TypeScript, Rust, Go, and Python.

# Tempo Transaction

## Abstract

This spec introduces native protocol support for the following features, using a new Tempo transaction type:

* WebAuthn/P256 signature validation - enables passkey accounts
* Parallelizable nonces - allows higher tx throughput for each account
* Gas sponsorship - allows apps to pay for their users' transactions
* Call Batching - allows users to multicall efficiently and atomically
* Scheduled Txs - allow users to specify a time window in which their tx can be executed
* Access Keys - allow a sender's key to provision scoped access keys with spending limits

## Motivation

Current accounts are limited to secp256k1 signatures and sequential nonces, creating UX and scalability challenges.\
Users cannot leverage modern authentication methods like passkeys, applications face throughput limitations due to sequential nonces.

## Specification

### Transaction Type

A new EIP-2718 transaction type is introduced with type byte `0x76`:

```rust
pub struct TempoTransaction {
    // Standard EIP-1559 fields
    chain_id: ChainId,                          // EIP-155 replay protection
    max_priority_fee_per_gas: u128,
    max_fee_per_gas: u128,
    gas_limit: u64,
    calls: Vec<Call>,                           // Batch of calls to execute atomically
    access_list: AccessList,                    // EIP-2930 access list

    // nonce-related fields
    nonce_key: U256,                            // 2D nonce key (0 = protocol nonce, >0 = user nonces)
    nonce: u64,                                 // Current nonce value for the nonce key

    // Optional features
    fee_token: Option<Address>,                 // Optional fee token preference
    fee_payer_signature: Option<Signature>,     // Sponsored transactions (secp256k1 only)
    valid_before: Option<u64>,                  // Transaction expiration timestamp (seconds)
    valid_after: Option<u64>,                   // Transaction can only be included after this timestamp (seconds)
    key_authorization: Option<SignedKeyAuthorization>, // Access key authorization (optional)
    aa_authorization_list: Vec<TempoSignedAuthorization>, // EIP-7702 style authorizations with AA signatures
}

// Call structure for batching
pub struct Call {
    to: TxKind,      // Can be Address or Create
    value: U256,
    input: Bytes     // Calldata for the call
}

// Key authorization for provisioning access keys
// RLP encoding: [chain_id, key_type, key_id, expiry?, limits?]
pub struct KeyAuthorization {
    chain_id: u64,                              // Chain ID for replay protection (0 = valid on any chain)
    key_type: SignatureType,                    // Type of key: Secp256k1 (0), P256 (1), or WebAuthn (2)
    key_id: Address,                            // Key identifier (address derived from public key)
    expiry: Option<u64>,                        // Unix timestamp when key expires (None = never expires)
    limits: Option<Vec<TokenLimit>>,            // TIP20 spending limits (None = unlimited spending)
}

// Signed key authorization (authorization + root key signature)
pub struct SignedKeyAuthorization {
    authorization: KeyAuthorization,
    signature: PrimitiveSignature,              // Root key's signature over keccak256(rlp(authorization))
}

// TIP20 spending limits for access keys
pub struct TokenLimit {
    token: Address,                             // TIP20 token address
    limit: U256,                                // Maximum spending amount for this token
}
```

### Signature Types

Four signature schemes are supported. The signature type is determined by length and type identifier:

#### secp256k1 (65 bytes)

```rust
pub struct Signature {
    r: B256,        // 32 bytes
    s: B256,        // 32 bytes
    v: u8           // 1 byte (recovery id)
}
```

**Format**: No type identifier prefix (backward compatible). Total length: 65 bytes.
**Detection**: Exactly 65 bytes with no type identifier.

#### P256 (130 bytes)

```rust
pub struct P256SignatureWithPreHash {
    typeId: u8,         // 0x01
    r: B256,            // 32 bytes
    s: B256,            // 32 bytes
    pub_key_x: B256,    // 32 bytes
    pub_key_y: B256,    // 32 bytes
    pre_hash: bool      // 1 byte
}
```

**Format**: Type identifier `0x01` + 129 bytes of signature data. Total length: 130 bytes. The `typeId` is a wire format prefix (not a struct field) prepended during encoding.

Note: Some P256 implementers (like Web Crypto) require the digests to be pre-hashed before verification.
If `pre_hash` is set to `true`, then before verification: `digest = sha256(digest)`.

#### WebAuthn (Variable length, max 2KB)

```rust
pub struct WebAuthnSignature {
    typeId: u8,                 // 0x02
    webauthn_data: Bytes,       // Variable length (authenticatorData || clientDataJSON)
    r: B256,                    // 32 bytes
    s: B256,                    // 32 bytes
    pub_key_x: B256,            // 32 bytes
    pub_key_y: B256             // 32 bytes
}
```

**Format**: Type identifier `0x02` + variable webauthn\_data + 128 bytes (r, s, pub\_key\_x, pub\_key\_y). Total length: variable (minimum 129 bytes, maximum 2049 bytes). The `typeId` is a wire format prefix prepended during encoding. Parse by working backwards: last 128 bytes are r, s, pub\_key\_x, pub\_key\_y.

#### Keychain (Variable length)

```rust
pub struct KeychainSignature {
    typeId: u8,                     // 0x03
    user_address: Address,          // 20 bytes - root account address
    signature: PrimitiveSignature   // Inner signature (Secp256k1, P256, or WebAuthn)
}
```

**Format**: Type identifier `0x03` + user\_address (20 bytes) + inner signature. The `typeId` is a wire format prefix prepended during encoding.
**Purpose**: Allows an access key to sign on behalf of a root account. The handler validates that `user_address` has authorized the access key in the AccountKeychain precompile.

### Address Derivation

#### secp256k1

```solidity
address(uint160(uint256(keccak256(abi.encode(x, y)))))
```

#### P256 and WebAuthn

```solidity
function deriveAddressFromP256(bytes32 pubKeyX, bytes32 pubKeyY) public pure returns (address) {    
    // Hash 
    bytes32 hash = keccak256(abi.encodePacked(
        pubKeyX,
        pubKeyY
    ));
    
    // Take last 20 bytes as address
    return address(uint160(uint256(hash)));
}
```

### Tempo Authorization List

The `aa_authorization_list` field enables EIP-7702 style delegation with support for all three AA signature types (secp256k1, P256, and WebAuthn), not just secp256k1.

#### Structure

```rust
pub struct TempoSignedAuthorization {
    inner: Authorization,      // Standard EIP-7702 authorization
    signature: TempoSignature,    // Can be Secp256k1, P256, or WebAuthn
}
```

Each authorization in the list:

* Delegates an account to a specified implementation contract
* Is signed by the account's authority using any supported signature type
* Follows EIP-7702 semantics for delegation and execution

#### Validation

* Cannot have `Create` calls when `aa_authorization_list` is non-empty (follows EIP-7702 semantics)
* Authority address is recovered from the signature and matched against the authorization

### Parallelizable Nonces

* **Protocol nonce (key 0)**: Existing account nonce, incremented for regular txs, 7702 authorization, or `CREATE`
* **User nonces (keys 1-N)**: Enable parallel execution with special gas schedule
* **Reserved sequence keys**: Nonce sequence keys with the most significant byte `0x5b` are reserved for [sub-block transactions](/protocol/blockspace/sub-block-specification#11-sub-block-transactions).

#### Account State Changes

* `nonces: mapping(uint256 => uint64)` - 2D nonce tracking

**Implementation Note:** Nonces are stored in the storage of a designated precompile at address `0x4E4F4E4345000000000000000000000000000000` (ASCII hex for "NONCE"), as there is currently no clean way to extend account state in Reth.

**Storage Layout at 0x4E4F4E4345:**

* Storage key: `keccak256(abi.encode(account_address, nonce_key))`
* Storage value: `nonce` (uint64)

Note: Protocol Nonce key (0), is directly stored in the account state, just like normal transaction types.

#### Nonce Precompile

The nonce precompile implements the following interface for managing 2D nonces:

```solidity
/// @title INonce - Nonce Precompile Interface
/// @notice Interface for managing 2D nonces as per the Tempo Transaction spec
/// @dev This precompile manages user nonce keys (1-N) while protocol nonces (key 0)
///      are handled directly by account state. Each account can have multiple
///      independent nonce sequences identified by a nonce key.
interface INonce {
    /// @notice Emitted when a nonce is incremented for an account and nonce key
    /// @param account The account whose nonce was incremented
    /// @param nonceKey The nonce key that was incremented
    /// @param newNonce The new nonce value after incrementing
    event NonceIncremented(address indexed account, uint256 indexed nonceKey, uint64 newNonce);
    /// @notice Thrown when trying to access protocol nonce (key 0) through the precompile
    /// @dev Protocol nonce should be accessed through account state, not this precompile
    error ProtocolNonceNotSupported();
    /// @notice Thrown when an invalid nonce key is provided
    error InvalidNonceKey();
    /// @notice Thrown when a nonce value would overflow
    error NonceOverflow();
    /// @notice Get the current nonce for a specific account and nonce key
    /// @param account The account address
    /// @param nonceKey The nonce key (must be > 0, protocol nonce key 0 not supported)
    /// @return nonce The current nonce value
    function getNonce(address account, uint256 nonceKey) external view returns (uint64 nonce);
}
```

#### Precompile Implementation

The precompile contract maintains a single storage mapping:

```solidity
contract Nonce is INonce {
    /// @dev Mapping from account -> nonce key -> nonce value
    mapping(address => mapping(uint256 => uint64)) private nonces;
}
```

#### Gas Schedule

For transactions using nonce keys:

1. **Protocol nonce (key 0)**: No additional gas cost
   * Uses the standard account nonce stored in account state

2. **Existing user key (nonce > 0)**: Add 5,000 gas to base cost
   * Rationale: Cold SLOAD (2,100) + warm SSTORE reset (2,900)

3. **New user key (nonce == 0)**: Add 22,100 gas to base cost
   * Rationale: Cold SLOAD (2,100) + SSTORE set for 0 → non-zero (20,000)

We specify the complete gas schedule in more detail in the [gas costs section](#gas-costs)

### Transaction Validation

#### Signature Validation

1. Determine type from signature format:
   * 65 bytes (no type identifier) = secp256k1
   * First byte `0x01` + 129 bytes = P256 (total 130 bytes)
   * First byte `0x02` + variable data = WebAuthn (total 129-2049 bytes)
   * First byte `0x03` + 20 bytes + inner signature = Keychain
   * Otherwise invalid
2. Apply appropriate verification:
   * secp256k1: Standard `ecrecover`
   * P256: P256 curve verification with provided public key (sha256 pre-hash if flag set)
   * WebAuthn: Parse clientDataJSON, verify challenge and type, then P256 verify
   * Keychain: Verify inner signature, then validate access key authorization via AccountKeychain precompile

#### Nonce Validation

1. Fetch sequence for given nonce key
2. Verify sequence matches transaction
3. Increment sequence

#### Fee Payer Validation (if present)

1. Verify fee payer signature (K1 only initially)
2. Recover payer address via `ecrecover`
3. Deduct fees from payer instead of sender

### Fee Payer Signature Details

The Tempo Transaction Type (0x76) supports **gas sponsorship** where a third party (fee payer) can pay transaction fees on behalf of the sender. This is achieved through dual signature domains—the sender signs with transaction type byte `0x76`, while the fee payer signs with magic byte `0x78` to ensure domain separation and prevent signature reuse attacks.

#### Signing Domains

##### Sender Signature

For computing the transaction hash that the sender signs:

* Fields are preceded by transaction type byte `0x76`
* Field 11 (`fee_token`) is encoded as empty string (`0x80`) **if and only if** `fee_payer_signature` is present. This allows the fee payer to specify the fee token.
* Field 12 (`fee_payer_signature`) is encoded as:
  * Single byte `0x00` if fee payer signature will be present (placeholder)
  * Empty string `0x80` if no fee payer

**Sender Signature Hash:**

```rust
// When fee_payer_signature is present:
sender_hash = keccak256(0x76 || rlp([
    chain_id,
    max_priority_fee_per_gas,
    max_fee_per_gas,
    gas_limit,
    calls,
    access_list,
    nonce_key,
    nonce,
    valid_before,
    valid_after,
    0x80,  // fee_token encoded as EMPTY (skipped)
    0x00   // placeholder byte for fee_payer_signature
]))

// When no fee_payer_signature:
sender_hash = keccak256(0x76 || rlp([
    chain_id,
    max_priority_fee_per_gas,
    max_fee_per_gas,
    gas_limit,
    calls,
    access_list,
    nonce_key,
    nonce,
    valid_before,
    valid_after,
    fee_token,  // fee_token is INCLUDED
    0x80        // empty for no fee_payer_signature
]))
```

##### Fee Payer Signature

Only included for sponsored transactions. For computing the fee payer's signature hash:

* Fields are preceded by **magic byte `0x78`** (different from transaction type `0x76`)
* Field 11 (`fee_token`) is **always included** (20-byte address or `0x80` for None)
* Field 12 is serialized as the **sender address** (20 bytes). This commits the fee payer to sponsoring a specific sender.

**Fee Payer Signature Hash:**

```rust
fee_payer_hash = keccak256(0x78 || rlp([  // Note: 0x78 magic byte
    chain_id,
    max_priority_fee_per_gas,
    max_fee_per_gas,
    gas_limit,
    calls,
    access_list,
    nonce_key,
    nonce,
    valid_before,
    valid_after,
    fee_token,      // fee_token ALWAYS included
    sender_address  // 20-byte sender address
    key_authorization,
]))
```

#### Key Properties

1. **Sender Flexibility**: By omitting `fee_token` from sender signature when fee payer is present, the fee payer can specify which token to use for payment without invalidating the sender's signature
2. **Fee Payer Commitment**: Fee payer's signature includes `fee_token` and `sender_address`, ensuring they agree to:
   * Pay for the specific sender
   * Use the specific fee token
3. **Domain Separation**: Different magic bytes (`0x76` vs `0x78`) prevent signature reuse attacks between sender and fee payer roles
4. **Deterministic Fee Payer**: The fee payer address is statically recoverable from the transaction via secp256k1 signature recovery

#### Validation Rules

**Signature Requirements:**

* Sender signature MUST be valid (secp256k1, P256, or WebAuthn depending on signature length)
* If `fee_payer_signature` present:
  * MUST be recoverable via secp256k1 (only secp256k1 supported for fee payers)
  * Recovery MUST succeed, otherwise transaction is invalid
* If `fee_payer_signature` absent:
  * Fee payer defaults to sender address (self-paid transaction)

**Token Preference:**

* When `fee_token` is `Some(address)`, this overrides any account/validator-level preferences
* Validation ensures the token is a valid TIP-20 token with sufficient balance/liquidity
* Failures reject the transaction before execution (see Token Preferences spec)

**Fee Payer Resolution:**

* Fee payer signature present → recovered address via `ecrecover`
* Fee payer signature absent → sender address
* This address is used for all fee accounting (pre-charge, refund) via TIP Fee Manager precompile

#### Transaction Flow

1. **User prepares transaction**: Sets `fee_payer_signature` to placeholder (`Some(Signature::default())`)
2. **User signs**: Computes sender hash (with fee\_token skipped) and signs
3. **Fee payer receives** user-signed transaction
4. **Fee payer verifies** user signature is valid
5. **Fee payer signs**: Computes fee payer hash (with fee\_token and sender\_address) and signs
6. **Complete transaction**: Replace placeholder with actual fee payer signature
7. **Broadcast**: Transaction is sent to network with both signatures

#### Error Cases

* `fee_payer_signature` present but unrecoverable → invalid transaction
* Fee payer balance insufficient for `gas_limit * max_fee_per_gas` in fee token → invalid
* Any sender signature failure → invalid
* Malformed RLP → invalid

### RLP Encoding

The transaction is RLP encoded as follows:

**Signed Transaction Envelope:**

```
0x76 || rlp([
    chain_id,
    max_priority_fee_per_gas,
    max_fee_per_gas,
    gas_limit,
    calls,                   // RLP list of Call structs
    access_list,
    nonce_key,
    nonce,
    valid_before,            // 0x80 if None
    valid_after,             // 0x80 if None
    fee_token,               // 0x80 if None
    fee_payer_signature,     // 0x80 if None, RLP list [v, r, s] if Some
    aa_authorization_list,   // EIP-7702 style authorization list with AA signatures
    key_authorization?,      // Only encoded if present (backwards compatible)
    sender_signature         // TempoSignature bytes (secp256k1, P256, WebAuthn, or Keychain)
])
```

**Call Encoding:**

```
rlp([to, value, input])
```

**Key Authorization Encoding:**

```
rlp([
    chain_id,
    key_type,
    key_id,
    expiry?,         // Optional trailing field (omitted or 0x80 if None)
    limits?,         // Optional trailing field (omitted or 0x80 if None)
    signature        // PrimitiveSignature bytes
])
```

**Notes:**

* Optional fields encode as `0x80` (EMPTY\_STRING\_CODE) when `None`
* The `key_authorization` field is truly optional - when `None`, no bytes are encoded (backwards compatible)
* The `calls` field is a list that must contain at least one Call (empty calls list is invalid)
* The `sender_signature` field is the final field and contains the TempoSignature bytes (secp256k1, P256, WebAuthn, or Keychain)
* KeyAuthorization uses RLP trailing field semantics for optional `expiry` and `limits`

### WebAuthn Signature Verification

WebAuthn verification follows the [Daimo P256 verifier approach](https://github.com/daimo-eth/p256-verifier/blob/master/src/WebAuthn.sol).

#### Signature Format

```
signature = authenticatorData || clientDataJSON || r (32) || s (32) || pubKeyX (32) || pubKeyY (32)
```

Parse by working backwards:

* Last 32 bytes: `pubKeyY`
* Previous 32 bytes: `pubKeyX`
* Previous 32 bytes: `s`
* Previous 32 bytes: `r`
* Remaining bytes: `authenticatorData || clientDataJSON` (requires parsing to split)

#### Authenticator Data Structure (minimum 37 bytes)

```
Bytes 0-31:   rpIdHash (32 bytes)
Byte 32:      flags (1 byte)
              - Bit 0 (0x01): User Presence (UP) - must be set
Bytes 33-36:  signCount (4 bytes)
```

#### Verification Steps

```python
def verify_webauthn(tx_hash: bytes32, signature: bytes, require_uv: bool) -> bool:
    # 1. Parse signature
    pubKeyY = signature[-32:]
    pubKeyX = signature[-64:-32]
    s = signature[-96:-64]
    r = signature[-128:-96]
    webauthn_data = signature[:-128]

    # Parse authenticatorData and clientDataJSON
    # Minimum authenticatorData is 37 bytes
    # Simple approach: try to decode clientDataJSON from different split points
    authenticatorData, clientDataJSON = split_webauthn_data(webauthn_data)

    # 2. Validate authenticator data
    if len(authenticatorData) < 37:
        return False

    flags = authenticatorData[32]
    if not (flags & 0x01):  # UP bit must be set
        return False

    # 3. Validate client data JSON
    if not contains(clientDataJSON, '"type":"webauthn.get"'):
        return False

    challenge_b64url = base64url_encode(tx_hash)
    challenge_property = '"challenge":"' + challenge_b64url + '"'
    if not contains(clientDataJSON, challenge_property):
        return False

    # 4. Compute message hash
    clientDataHash = sha256(clientDataJSON)
    messageHash = sha256(authenticatorData || clientDataHash)

    # 5. Verify P256 signature
    return p256_verify(messageHash, r, s, pubKeyX, pubKeyY)
```

#### What We Verify

* Authenticator data minimum length (37 bytes)
* User Presence (UP) flag is set
* `"type":"webauthn.get"` in clientDataJSON
* Challenge matches tx\_hash (Base64URL encoded)
* P256 signature validity

#### What We Skip

* Origin verification (not applicable to blockchain)
* RP ID hash validation (no central RP in decentralized context)
* Signature counter (anti-cloning left to application layer)
* Backup flags (account policy decision)

#### Parsing authenticatorData and clientDataJSON

Since authenticatorData has variable length, finding the split point requires:

1. Check if AT flag (bit 6) is set at byte 32
2. If not set, authenticatorData is exactly 37 bytes
3. If set, need to parse CBOR credential data (complex, see implementation)
4. Everything after authenticatorData is clientDataJSON (valid UTF-8 JSON)

**Simplified approach:** For TempoTransactions, wallets should send minimal authenticatorData (37 bytes, no AT/ED flags) to minimize gas costs and simplify parsing.

### Access Keys

A sender can choose to authorize an Access Key to sign transactions on the sender's behalf. This is useful to enable
flows where a root key (e.g. a passkey) would provision a short-lived (scoped) Access Key to
be able to sign transactions on the sender's behalf without inducing another passkey prompt.

More information about Access Keys can be found in the [Account Keychain Specification](./AccountKeychain).

A sender can authorize a key by signing over a "key authorization" item that contains the following information:

* **Chain ID** for replay protection (0 = valid on any chain)
* **Key type** (Secp256k1, P256, or WebAuthn)
* **Key ID** (address derived from the public key)
* **Expiration** timestamp of when the key should expire (optional - None means never expires)
* TIP20 token **spending limits** for the key (optional - None means unlimited spending):
  * Limits deplete as tokens are spent
  * Root key can update limits via `updateSpendingLimit()` without revoking the key
  * Note: Spending limits only apply to TIP20 token transfers, not ETH or other asset transfers

#### RLP Encoding

**Unsigned Format:**

The root key signs over the keccak256 hash of the RLP encoded `KeyAuthorization`:

```
key_authorization_digest = keccak256(rlp([chain_id, key_type, key_id, expiry?, limits?]))

chain_id = u64 (0 = valid on any chain)
key_type = 0 (Secp256k1) | 1 (P256) | 2 (WebAuthn)
key_id = Address (derived from the public key)
expiry = Option<u64> (unix timestamp, None = never expires, stored as u64::MAX in precompile)
limits = Option<Vec<[token, limit]>> (None = unlimited spending)
```

**Signed Format:**

The signed format (`SignedKeyAuthorization`) includes all fields with the `signature` appended:

```
signed_key_authorization = rlp([chain_id, key_type, key_id, expiry?, limits?, signature])
```

The `signature` is a `PrimitiveSignature` (secp256k1, P256, or WebAuthn) signed by the root key.

Note: `expiry` and `limits` use RLP trailing field semantics - they can be omitted entirely when None.

#### Keychain Precompile

The Account Keychain precompile (deployed at address `0xAAAAAAAA00000000000000000000000000000000`) manages authorized access keys for accounts. It enables root keys to provision scoped access keys with expiry timestamps and per-TIP20 token spending limits.

**See the [Account Keychain Specification](./AccountKeychain) for complete interface details, storage layout, and implementation.**

#### Protocol Behavior

The protocol enforces Access Key authorization and spending limits natively.

##### Transaction Validation

When a TempoTransaction is received, the protocol:

1. **Identifies the signing key** from the transaction signature
   * If signature is a `Keychain` variant: extracts the `keyId` (address) of the Access Key
   * Otherwise: treats it as the Root Key (keyId = address(0))

2. **Validates KeyAuthorization** (if present in transaction)
   * The `key_authorization` field in `TempoTransaction` provisions a NEW Access Key
   * Root Key MUST sign:
     * The `key_authorization` digest: `keccak256(rlp([key_type, key_id, expiry, limits]))`
   * Access Key (being authorized) CAN sign the same tx which it is authorized in.
   * This enables "authorize and use" in a single transaction

3. **Sets transaction context**
   * Stores `transactionKey[account] = keyId` in protocol state
   * Used to enforce authorization hierarchy during execution, can
     also be used by DApps to see which key authorized the current tx.

4. **Validates Key Authorization** (for Access Keys)
   * Queries precompile: `getKey(account, keyId)` returns `KeyInfo`
   * Checks key is active (not revoked)
   * Checks expiry: `current_timestamp < expiry` (or `expiry == 0` for never expires)
   * Rejects transaction if validation fails

##### Authorization Hierarchy Enforcement

The protocol enforces a strict two-tier hierarchy:

**Root Key** (keyId = address(0)):

* The account's primary key (address matches account address)
* Can call ALL precompile functions
* No spending limits
* Can authorize, revoke, and update Access Keys

**Access Keys** (keyId != address(0)):

* Secondary keys authorized by Root Key
* CANNOT call mutable precompile functions (`authorizeKey`, `revokeKey`, `updateSpendingLimit`)
* Precompile functions check: `transactionKey[msg.sender] == 0` before allowing mutations
* Subject to per-TIP20 token spending limits
* Can have expiry timestamps

When an Access Key attempts to call `authorizeKey()`, `revokeKey()`, or `updateSpendingLimit()`:

1. Transaction executes normally until the precompile call
2. Precompile checks `getTransactionKey()` returns non-zero (Access Key)
3. Call reverts with `UnauthorizedCaller` error
4. Entire transaction is reverted

##### Spending Limit Enforcement

The protocol tracks and enforces spending limits for TIP20 token transfers:

**Scope:** Only TIP20 `transfer()`, `transferWithMemo()`, `approve()`, and `startReward()` calls are tracked

* Spending limits only apply when `msg.sender == tx.origin` (direct EOA calls)
* When a contract makes transfers on behalf of the user, spending limits do NOT apply (e.g., `transferFrom()`)
* Native value transfers are NOT limited
* NFT transfers are NOT limited
* Other asset types are NOT limited

**Tracking:** During transaction execution, when an Access Key's transaction directly calls TIP20 methods:

1. Protocol intercepts `transfer(to, amount)`, `transferWithMemo()`, `approve(spender, amount)`, and `startReward()` calls
2. For `transfer`/`transferWithMemo`, the full `amount` is checked against the remaining limit
3. For `approve`, only **increases** in approval (new approval minus previous allowance) are checked and counted against the limit
4. Queries: `getRemainingLimit(account, keyId, token)`
5. Checks: relevant amount (transfer amount or approval increase) `<= remaining_limit`
6. If check fails: reverts with `SpendingLimitExceeded`
7. If check passes: decrements the limit by the relevant amount
8. Updates are stored in precompile state

**Root Key Behavior:** Spending limit checks are skipped entirely (no limits apply)

**Limit Updates:**

* Limits deplete as tokens are spent
* Root Key can call `updateSpendingLimit(keyId, token, newLimit)` to set new limits
* Setting a new limit REPLACES the current remaining amount (does not add to it)
* Limits do not reset automatically (no time-based periods)

##### Creating and Using KeyAuthorization

**First-Time Authorization Flow:**

1. **Generate Access Key**

   ```typescript
   // Generate a new P256 or secp256k1 key pair
   const accessKey = generateKeyPair("p256"); // or "secp256k1"
   const keyId = deriveAddress(accessKey.publicKey);
   ```

2. **Create Authorization Message**

   ```typescript
   // Define key parameters
   const keyAuth = {
     key_type: SignatureType.P256,      // 1
     key_id: keyId,                     // address derived from public key
     expiry: timestamp + 86400,         // 24 hours from now (or 0 for never)
     limits: [
       { token: USDC_ADDRESS, amount: 1000000000 }, // 1000 USDC (6 decimals)
       { token: DAI_ADDRESS, amount: 500000000000000000000 }  // 500 DAI (18 decimals)
     ]
   };

   // Compute digest: keccak256(rlp([key_type, key_id, expiry, limits]))
   const authDigest = computeAuthorizationDigest(keyAuth);
   ```

3. **Root Key Signs Authorization**

   ```typescript
   // Sign with Root Key (e.g., passkey prompt)
   const rootSignature = await signWithRootKey(authDigest);
   ```

4. **Build TempoTransaction**

   ```typescript
   const tx = {
     chain_id: 1,
     nonce: await getNonce(account),
     nonce_key: 0,
     calls: [{ to: recipient, value: 0, input: "0x" }],
     gas_limit: 200000,
     max_fee_per_gas: 1000000000,
     max_priority_fee_per_gas: 1000000000,
     key_authorization: {
       key_type: keyAuth.key_type,
       expiry: keyAuth.expiry,
       limits: keyAuth.limits,
       key_id: keyAuth.key_id,
       signature: rootSignature  // Root Key's signature on authDigest
     },
     // ... other fields
   };
   ```

5. **Access Key Signs Transaction**

   ```typescript
   // Sign transaction with the NEW Access Key being authorized
   const txHash = computeTxSignatureHash(tx);
   const accessSignature = await signWithAccessKey(txHash, accessKey);

   // Wrap in Keychain signature
   const finalSignature = {
     Keychain: {
       user_address: account,
       signature: { P256: accessSignature }  // or Secp256k1
     }
   };
   ```

6. **Submit Transaction**
   * Protocol validates Root Key signed the `key_authorization`
   * Protocol calls `authorizeKey()` on the precompile to store the key
   * Protocol validates Access Key signature on transaction
   * Transaction executes with spending limits enforced

**Subsequent Usage (Key Already Authorized):**

```typescript
// Access Key is already authorized, just sign transactions directly
const tx = {
  chain_id: 1,
  nonce: await getNonce(account),
  calls: [{ to: recipient, value: 0, input: calldata }],
  key_authorization: null,  // No authorization needed
  // ... other fields
};

const txHash = computeTxSignatureHash(tx);
const accessSignature = await signWithAccessKey(txHash, accessKey);

const finalSignature = {
  Keychain: {
    user_address: account,
    signature: { P256: accessSignature }
  }
};

// Submit - protocol validates key is authorized and not expired
```

##### Key Management Operations

**Revoking an Access Key:**

```typescript
// Must be signed by Root Key
const tx = {
  chain_id: 1,
  nonce: await getNonce(account),
  calls: [{
    to: ACCOUNT_KEYCHAIN_ADDRESS,
    value: 0,
    input: encodeCall("revokeKey", [keyId])
  }],
  // ... sign with Root Key
};
```

**Updating Spending Limits:**

```typescript
// Must be signed by Root Key
const tx = {
  chain_id: 1,
  nonce: await getNonce(account),
  calls: [{
    to: ACCOUNT_KEYCHAIN_ADDRESS,
    value: 0,
    input: encodeCall("updateSpendingLimit", [
      keyId,
      USDC_ADDRESS,
      2000000000  // New limit: 2000 USDC
    ])
  }],
  // ... sign with Root Key
};
```

**Note:** After updating, the remaining limit is set to the `newLimit` value, not added to the current remaining amount.

##### Querying Key State

Applications can query key information and spending limits:

```typescript
// Check if key is authorized and get info
const keyInfo = await precompile.getKey(account, keyId);
// Returns: { signatureType, keyId, expiry }

// Check remaining spending limit for a token
const remaining = await precompile.getRemainingLimit(account, keyId, USDC_ADDRESS);
// Returns: uint256 amount remaining

// Get which key signed current transaction (callable from contracts)
const currentKey = await precompile.getTransactionKey();
// Returns: address (0x0 for Root Key, keyId for Access Key)
```

## Rationale

### Signature Type Detection by Length

Using signature length for type detection avoids adding explicit type fields while maintaining deterministic parsing. The chosen lengths (65, 129, variable) are naturally distinct.

### Linear Gas Scaling for Nonce Keys

The progressive pricing model prevents state bloat while keeping initial keys affordable. The 20,000 gas increment approximates the long-term state cost of maintaining each additional nonce mapping.

### No Nonce Expiry

Avoiding expiry simplifies the protocol and prevents edge cases where in-flight transactions become invalid. Wallets handle nonce key allocation to prevent conflicts.

### Backwards Compatibility

This spec introduces a new transaction type and does not modify existing transaction processing. Legacy transactions continue to work unchanged. We special case `nonce key = 0` (also referred to as the protocol nonce key) to maintain compatibility with existing nonce behavior.

## Gas Costs

### Signature Verification Gas Schedule

Different signature types incur different base transaction costs to reflect their computational complexity:

| Signature Type | Base Gas Cost | Calculation | Rationale |
|----------------|---------------|-------------|-----------|
| **secp256k1** | 21,000 | Standard | Includes 3,000 gas for ecrecover precompile |
| **P256** | 26,000 | 21,000 + 5,000 | Base 21k + additional 5k for P256 verification |
| **WebAuthn** | 26,000 + variable data cost | 26,000 + (calldata gas for clientDataJSON) | Base P256 cost plus variable cost for clientDataJSON based on size |
| **Keychain** | Inner signature + 3,000 | primitive\_sig\_cost + 3,000 | Inner signature cost + key validation overhead (2,100 SLOAD + 900 buffer) |

**Rationale:**

* The base 21,000 gas for standard transactions already includes the cost of secp256k1 signature verification via ecrecover (3,000 gas)
* [EIP 7951](https://eips.ethereum.org/EIPS/eip-7951) sets P256 verification cost at 6,900 gas. We add 1,100 gas to account for the additional 65 bytes of signature size (129 bytes total vs 64 bytes for secp256k1), giving 8,000 gas total. Since the base 21k already includes 3,000 gas for ecrecover (which P256 doesn't use), the net additional cost is 8,000 - 3,000 = **5,000 gas**.
* WebAuthn signatures require additional computation to parse and validate the clientDataJSON structure. We cap the total signature size at 2kb. The signature is also  charged using the same gas schedule as calldata (16 gas per non-zero byte, 4 gas per zero byte) to prevent the use of this signature space from spam.
* Keychain signatures wrap a primitive signature and are used by access keys. They add 3,000 gas to cover key validation during transaction validation (cold SLOAD to verify key exists + processing overhead).
* Individual per-signature-type gas costs allow us to add more advanced verification methods in the future like multisigs, which could have dynamic gas pricing.

### Nonce Key Gas Schedule

Transactions using parallelizable nonces incur additional costs based on the nonce key usage pattern:

#### Case 1: Protocol Nonce (Key 0)

* **Additional Cost:** 0 gas
* **Total:** 21,000 gas (base transaction cost)
* **Rationale:** Maintains backward compatibility with existing transaction flow

#### Case 2: Existing User Nonce Key (nonce > 0)

* **Additional Cost:** 5,000 gas
* **Total:** 26,000 gas
* **Rationale:** Cold SLOAD (2,100) + warm SSTORE reset (2,900) for incrementing an existing nonce

#### Case 3: New User Nonce Key (nonce == 0)

* **Additional Cost:** 22,100 gas
* **Total:** 43,100 gas
* **Rationale:** Cold SLOAD (2,100) + SSTORE set (20,000) for writing to a new storage slot

**Rationale for Fixed Pricing:**

1. **Simplicity:** Fixed costs based on actual EVM storage operations are straightforward to reason about
2. **Storage Pattern Alignment:** Costs directly mirror EVM cold SSTORE costs for new vs existing slots
3. **State Growth:** Creating new nonce keys incurs the higher cost naturally through SSTORE set pricing

### Key Authorization Gas Schedule

When a transaction includes a `key_authorization` field to provision a new access key, additional intrinsic gas is charged to cover signature verification and storage operations. This gas is charged **before execution** as part of the transaction's intrinsic gas cost.

#### Gas Components

| Component | Gas Cost | Notes |
|-----------|----------|-------|
| **Signature verification** | 3,000 (secp256k1) / 8,000 (P256) / 8,000 + calldata (WebAuthn) | Verifying the root key's signature on the authorization |
| **Key storage** | 22,000 | Cold SSTORE to store new key (0→non-zero) |
| **Overhead buffer** | 5,000 | Buffer for event emission, storage reads, and other overhead |
| **Per spending limit** | 22,000 each | Cold SSTORE per token limit (0→non-zero) |

**Signature verification rationale:** KeyAuthorization requires an *additional* signature verification beyond the transaction signature. Unlike the transaction signature (where ecrecover cost is included in the base 21k), KeyAuthorization must pay the full verification cost:

* **secp256k1**: 3,000 gas (ecrecover precompile cost)
* **P256**: 8,000 gas (6,900 from EIP-7951 + 1,100 for signature size). Note: the transaction signature schedule charges only 5,000 additional gas for P256 because it subtracts the 3,000 ecrecover "savings" already in base 21k. KeyAuthorization pays the full 8,000.
* **WebAuthn**: 8,000 + calldata gas for webauthn\_data

#### Gas Formula

```
KEY_AUTH_BASE_GAS = 30,000  # For secp256k1 signature (3,000 + 22,000 + 5,000)
KEY_AUTH_BASE_GAS = 35,000  # For P256 signature (5,000 + 3,000 + 22,000 + 5,000)
KEY_AUTH_BASE_GAS = 35,000 + webauthn_calldata_gas  # For WebAuthn signature

PER_LIMIT_GAS = 22,000  # Per spending limit entry

total_key_auth_gas = KEY_AUTH_BASE_GAS + (num_limits * PER_LIMIT_GAS)
```

#### Examples

| Configuration | Gas Cost | Calculation |
|--------------|----------|-------------|
| secp256k1, no limits | 30,000 | Base only |
| secp256k1, 1 limit | 52,000 | 30,000 + 22,000 |
| secp256k1, 3 limits | 96,000 | 30,000 + (3 × 22,000) |
| P256, no limits | 35,000 | Base with P256 verification |
| P256, 2 limits | 79,000 | 35,000 + (2 × 22,000) |

#### Rationale

1. **Pre-execution charging**: KeyAuthorization is validated and executed during transaction validation (before the EVM runs), so its gas must be included in intrinsic gas
2. **Storage cost alignment**: The 22,000 gas per storage slot approximates EVM cold SSTORE costs for new slots
3. **DoS prevention**: Progressive cost based on number of limits prevents abuse through excessive limit creation

### Reference Pseudocode

```python
def calculate_calldata_gas(data: bytes) -> uint256:
    """
    Calculate gas cost for calldata based on zero and non-zero bytes

    Args:
        data: bytes to calculate cost for

    Returns:
        gas_cost: uint256
    """
    CALLDATA_ZERO_BYTE_GAS = 4
    CALLDATA_NONZERO_BYTE_GAS = 16

    gas = 0
    for byte in data:
        if byte == 0:
            gas += CALLDATA_ZERO_BYTE_GAS
        else:
            gas += CALLDATA_NONZERO_BYTE_GAS

    return gas


def calculate_signature_verification_gas(signature: PrimitiveSignature) -> uint256:
    """
    Calculate gas cost for verifying a primitive signature.

    Returns the ADDITIONAL gas beyond the base 21k transaction cost.
    - secp256k1: 0 (already included in base 21k via ecrecover)
    - P256: 5,000 (8,000 full cost - 3,000 ecrecover already in base 21k)
    - WebAuthn: 5,000 + calldata gas for webauthn_data
    """
    # P256 full verification cost is 8,000 (6,900 from EIP-7951 + 1,100 for signature size)
    # But base 21k already includes 3,000 for ecrecover, so additional cost is 5,000
    P256_ADDITIONAL_GAS = 5_000

    if signature.type == Secp256k1:
        return 0  # Already included in base 21k
    elif signature.type == P256:
        return P256_ADDITIONAL_GAS
    elif signature.type == WebAuthn:
        webauthn_data_gas = calculate_calldata_gas(signature.webauthn_data)
        return P256_ADDITIONAL_GAS + webauthn_data_gas
    else:
        revert("Invalid signature type")


def calculate_key_authorization_gas(key_auth: SignedKeyAuthorization) -> uint256:
    """
    Calculate the intrinsic gas cost for a KeyAuthorization.

    This is charged BEFORE execution as part of transaction validation.

    Args:
        key_auth: SignedKeyAuthorization with fields:
            - signature: PrimitiveSignature (root key's signature)
            - limits: Optional[List[TokenLimit]]

    Returns:
        gas_cost: uint256
    """
    # Constants - KeyAuthorization pays FULL signature verification costs
    # (not the "additional" costs used for transaction signatures)
    ECRECOVER_GAS = 3_000   # Full ecrecover cost
    P256_FULL_GAS = 8_000   # Full P256 cost (6,900 + 1,100)
    COLD_SSTORE_SET_GAS = 22_000  # Storage cost for new slot
    OVERHEAD_BUFFER = 5_000  # Buffer for event emission, storage reads, etc.

    gas = 0

    # Step 1: Signature verification cost (full cost, not additional)
    if key_auth.signature.type == Secp256k1:
        gas += ECRECOVER_GAS  # 3,000
    elif key_auth.signature.type == P256:
        gas += P256_FULL_GAS  # 8,000
    elif key_auth.signature.type == WebAuthn:
        webauthn_data_gas = calculate_calldata_gas(key_auth.signature.webauthn_data)
        gas += P256_FULL_GAS + webauthn_data_gas  # 8,000 + calldata

    # Step 2: Key storage
    gas += COLD_SSTORE_SET_GAS  # 22,000 - store new key (0 → non-zero)

    # Step 3: Overhead buffer
    gas += OVERHEAD_BUFFER  # 5,000

    # Step 4: Per-limit storage cost
    num_limits = len(key_auth.limits) if key_auth.limits else 0
    gas += num_limits * COLD_SSTORE_SET_GAS  # 22,000 per limit

    return gas


def calculate_tempo_tx_base_gas(tx):
    """
    Calculate the base gas cost for a TempoTransaction

    Args:
        tx: TempoTransaction object with fields:
            - signature: TempoSignature (variable length)
            - nonce_key: uint192
            - nonce: uint64
            - sender_address: address
            - key_authorization: Optional[SignedKeyAuthorization]

    Returns:
        total_gas: uint256
    """

    # Constants
    BASE_TX_GAS = 21_000
    EXISTING_NONCE_KEY_GAS = 5_000   # Cold SLOAD (2,100) + warm SSTORE reset (2,900)
    NEW_NONCE_KEY_GAS = 22_100       # Cold SLOAD (2,100) + SSTORE set (20,000)
    KEYCHAIN_VALIDATION_GAS = 3_000  # 2,100 SLOAD + 900 processing buffer

    # Step 1: Determine signature verification cost
    # For Keychain signatures, use the inner primitive signature
    if tx.signature.type == Keychain:
        inner_sig = tx.signature.inner_signature
    else:
        inner_sig = tx.signature

    signature_gas = BASE_TX_GAS + calculate_signature_verification_gas(inner_sig)

    # Add keychain validation overhead if using access key
    if tx.signature.type == Keychain:
        signature_gas += KEYCHAIN_VALIDATION_GAS

    # Step 2: Calculate nonce key cost
    if tx.nonce_key == 0:
        # Protocol nonce (backward compatible)
        nonce_gas = 0
    else:
        # User nonce key
        current_nonce = get_nonce(tx.sender_address, tx.nonce_key)

        if current_nonce > 0:
            # Existing nonce key - cold SLOAD + warm SSTORE reset
            nonce_gas = EXISTING_NONCE_KEY_GAS
        else:
            # New nonce key - cold SLOAD + SSTORE set
            nonce_gas = NEW_NONCE_KEY_GAS

    # Step 3: Calculate key authorization cost (if present)
    if tx.key_authorization is not None:
        key_auth_gas = calculate_key_authorization_gas(tx.key_authorization)
    else:
        key_auth_gas = 0

    # Step 4: Calculate total base gas
    total_gas = signature_gas + nonce_gas + key_auth_gas

    return total_gas
```

## Security Considerations

### Mempool DOS Protection

Transaction pools perform pre-execution validation checks before accepting transactions. These checks are performed for free by the nodes, making them potential DOS vectors. The three primary validation checks are:

1. **Signature verification** - Must be valid
2. **Nonce verification** - Must match current account nonce
3. **Balance check** - Account must have sufficient balance to pay for transaction

This transaction type impacts all three areas:

#### Signature Verification Impact

* **P256 signatures**: Fixed computational cost similar to ecrecover.
* **WebAuthn signatures**: Variable cost due to clientDataJSON parsing, but **capped at 2KB total signature size** to prevent abuse
* **Mitigation**: All signature types have bounded computational costs that are in the same ballpark as standard ecrecover.

#### Nonce Verification Impact

* **2D nonce lookup**: Requires additional storage read from nonce precompile
* **Cost**: Equivalent to a cold SLOAD (~2,100 gas worth of free computation)
* **Mitigation**: Cost is bounded to a manageable value.

#### Fee Payer Impact

* **Additional account read**: When fee payer is specified, must fetch fee payer's account to verify balance
* **Cost**: Effectively doubles the free account access work for sponsored transactions
* **Mitigation**: Cost is still bounded to a single additional account read.

#### Comparison to Ethereum

The introduction of 7702 delegated accounts already created complex cross-transaction dependencies in the mempool, which prevents any static pool checks from being useful.
Because a single transaction can invalidate multiple others by spending balances of multiple accounts

**Assessment:** While this transaction type introduces additional pre-execution validation costs, all costs are bounded to reasonable limits. The mempool complexity issues around cross-transaction dependencies already exist in Ethereum due to 7702 and accounts with code, making static validation inherently difficult. So the incremental cost from this transaction type is acceptable given these existing constraints.

# Setup

Setup infinite pooled Tempo node instances in TypeScript using [`prool`](https://github.com/wevm/prool) by following the steps below.

::::steps

## Install

:::code-group

```bash [npm]
npm i prool
```

```bash [pnpm]
pnpm i prool
```

```bash [bun]
bun i prool
```

:::

* [Prool](https://github.com/wevm/prool) is a library that provides programmatic HTTP testing instances for Ethereum.

## Create Instance

You can programmatically start a Tempo node instance in TypeScript using `Instance.tempo`:

```ts
import { Instance, Server } from 'prool'

const server = Server.create({
  instance: Instance.tempo(),
});

// Start the node
await server.start()
// Instances available at: 
// - http://localhost:8545/1
// - http://localhost:8545/2
// - http://localhost:8545/3
// - http://localhost:8545/4
// - http://localhost:8545/n
```

:::tip
You can also set up the Tempo instance using `Instance.tempo` directly if you
do not need pooling.

```ts
import { Instance } from 'prool';

const instance = Instance.tempo()

// Start the node
await instance.start()
// Instance available at: http://localhost:8545
```

:::

## Next Steps

After you have set up Tempo with Prool, you can now:

* Easily use Tempo in your test suite with Vitest
* Run Tempo locally alongside your Vite or Next.js development server

::::

# `Handler.compose`

Composes multiple handlers into a single handler. This is useful when you want to run multiple services (like fee payer and key manager) from a single endpoint.

## Usage

```ts twoslash [server.ts]
// @noErrors
import { Handler, Kv } from 'tempo.ts/server'
import { tempoModerato } from 'viem/chains'
import { http } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'

const handler = Handler.compose([
  // Create a fee payer handler
  Handler.feePayer({
    account: privateKeyToAccount('0x...'),
    chain: tempoModerato.extend({ 
      feeToken: '0x20c0...0001' 
    }),
    transport: http(),
    path: '/fee-payer',
  })
  
  // Create a key manager handler
  Handler.keyManager({
    kv: Kv.memory(),
    path: '/keys',
    rp: 'example.com',
  })
])
```

Then plug `handler` into your server framework of choice. For example:

```ts
createServer(handler.listener) // Node.js
Bun.serve(handler) // Bun
Deno.serve(handler) // Deno
app.all('*', c => handler.fetch(c.request)) // Elysia
app.use(handler.listener) // Express
app.use(c => handler.fetch(c.req.raw)) // Hono
export const GET = handler.fetch // Next.js
export const POST = handler.fetch // Next.js
```

### Base Path

You can configure the base path for the composed handler.

```ts
const handler = Handler.compose([
  Handler.feePayer({ path: '/fee-payer', ... }),
  Handler.keyManager({ path: '/keys', ... }),
], { path: '/api' })
```

Requests are routed as follows:

* `POST /api/fee-payer` → Fee payer handler
* `GET /api/keys/challenge` → Key manager handler
* `GET /api/keys/:credentialId` → Key manager handler
* `POST /api/keys/:credentialId` → Key manager handler

## Parameters

### handlers

* **Type:** `Handler[]`

An array of handlers to compose. Handlers are tried in order, and the first one that doesn't return a 404 wins.

```ts twoslash
// @noErrors
import { Handler } from 'tempo.ts/server'

const handler = Handler.compose([
  Handler.feePayer({ /* ... */ }),
  Handler.keyManager({ /* ... */ }),
  // Add more handlers as needed
])
```

### options.path

* **Type:** `string`
* **Default:** `'/'`

The base path where all composed handlers will be mounted. This path is stripped from incoming requests before forwarding to individual handlers.

```ts twoslash
// @noErrors
import { Handler } from 'tempo.ts/server'

const handler = Handler.compose(
  [
    Handler.feePayer({ path: '/fee-payer', /* ... */ }),
    Handler.keyManager({ path: '/keys', /* ... */ }),
  ],
  { path: '/api' }, // [!code focus]
)

// Endpoints will be:
// POST /api/fee-payer
// GET  /api/keys/challenge
// GET  /api/keys/:credentialId
// POST /api/keys/:credentialId
```

# `Handler.feePayer`

Creates a server handler that acts as a fee payer for transactions.
This enables you to subsidize gas costs for your users by signing transactions with a dedicated fee payer account on your backend.

## Usage

:::code-group

```ts twoslash [server.ts]
// @noErrors
import { Handler } from 'tempo.ts/server'
import { tempoModerato } from 'viem/chains'
import { http } from 'viem'
import { privateKeyToAccount } from 'viem/accounts'

const handler = Handler.feePayer({
  account: privateKeyToAccount('0x...'),
  chain: tempoModerato.extend({ feeToken: '0x20c0...0001' }),
  path: '/fee-payer',
  transport: http(),
})
```

```ts twoslash [example.client.ts]
// @noErrors
import { createClient, http, walletActions } from 'viem'
import { tempoModerato } from 'viem/chains'
import { tempoActions, withFeePayer } from 'viem/tempo'

const client = createClient({
  chain: tempoModerato,
  transport: withFeePayer(
    http(), // Default transport
    http('http://localhost:3000/fee-payer'), // Fee payer transport (your server)
  ),
}).extend(tempoActions())

// Send a fee-sponsored payment
const receipt = await client.token.transferSync({
  amount: parseUnits('10', 6),
  feePayer: true,
  to: '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEbb',
  token: '0x20c0000000000000000000000000000000000001',
})
```

:::

Then plug `handler` into your server framework of choice. For example:

```ts
createServer(handler.listener) // Node.js
Bun.serve(handler) // Bun
Deno.serve(handler) // Deno
app.all('*', c => handler.fetch(c.request)) // Elysia
app.use(handler.listener) // Express
app.use(c => handler.fetch(c.req.raw)) // Hono
export const GET = handler.fetch // Next.js
export const POST = handler.fetch // Next.js
```

## How It Works

The fee payer handler intercepts RPC requests and handles the following methods:

* **`eth_signTransaction`** - Signs a transaction with the fee payer account
* **`eth_signRawTransaction`** - Signs a pre-serialized transaction with the fee payer account
* **`eth_sendRawTransaction`** - Signs and broadcasts a transaction with the fee payer account
* **`eth_sendRawTransactionSync`** - Signs, broadcasts, and waits for confirmation

For each of these methods, the handler:

1. Deserializes the transaction (if necessary)
2. Signs the transaction with your fee payer account
3. Returns the signed transaction or transaction hash

## Parameters

### account

* **Type:** `LocalAccount`
* **Required:** Yes

The account to use as the fee payer. This account will sign all transactions and pay the gas fees.

### chain

* **Type:** `Chain`

Chain (and fee token) to use.

### transport

* **Type:** `Transport`

Transport to use.

### path

* **Type:** `string`
* **Default:** `'/'`
* **Optional**

The path where the handler will listen for requests.

### onRequest

* **Type:** `(request: RpcRequest) => Promise<void>`
* **Optional**

A callback function that's called before processing each request. Useful for logging, rate limiting, or custom validation.

# `Handler.keyManager`

Creates a server handler that manages WebAuthn credential public keys. This handler stores and retrieves the public keys associated with passkey credentials, enabling users to access their accounts from any device.

## Usage

:::code-group

```ts twoslash [server.ts]
// @noErrors
import { Handler, Kv } from 'tempo.ts/server'

const handler = Handler.keyManager({
  kv: Kv.memory(),
  path: '/keys',
  rp: 'example.com',
})
```

```ts twoslash [wagmi.config.ts]
// @noErrors
import { tempoModerato } from 'viem/chains'
import { KeyManager, webAuthn } from 'wagmi/tempo'
import { createConfig, http } from 'wagmi'

export const config = createConfig({
  connectors: [
    webAuthn({
      keyManager: KeyManager.http('http://localhost:3000/keys'),
      rpId: 'example.com',
    }),
  ],
  chains: [tempoModerato],
  transports: {
    [tempo.id]: http(),
  },
})
```

:::

Then plug `handler` into your server framework of choice. For example:

```ts
createServer(handler.listener) // Node.js
Bun.serve(handler) // Bun
Deno.serve(handler) // Deno
app.all('*', c => handler.fetch(c.request)) // Elysia
app.use(handler.listener) // Express
app.use(c => handler.fetch(c.req.raw)) // Hono
export const GET = handler.fetch // Next.js
export const POST = handler.fetch // Next.js
```

:::warning

It is not recommended to use `Kv.memory()` in production. Instead, use a persistent store like Cloudflare or Vercel KV, or a Redis instance.

:::

## How It Works

The key manager handler exposes three endpoints:

### `GET /{path}/challenge`

Generates a random challenge for WebAuthn credential creation. The challenge is stored temporarily (with a 5-minute expiration) to be verified later during credential registration.

### `GET /{path}/:credentialId`

Retrieves the public key for a given credential ID. This is used when a user authenticates with an existing passkey.

### `POST /{path}/:credentialId`

Stores a public key for a new credential. This endpoint:

1. Verifies the challenge was previously issued and is still valid
2. Validates the credential's `clientDataJSON.type` is `'webauthn.create'`
3. Verifies the origin matches the configured RP ID (if set)
4. Extracts and stores the public key from the authenticator data

## Parameters

### kv

* **Type:** `Kv`
* **Required:** Yes

The key-value store to use for persisting challenges and public keys. tempo.ts provides adapters for common KV stores:

```ts twoslash
// @noErrors
import { Kv } from 'tempo.ts/server'

// In-memory store (for development/testing)
const kv = Kv.memory()

// Cloudflare KV
import { env } from 'cloudflare:workers'
const kv = Kv.cloudflare(env.KEY_STORE)
```

:::warning
`Kv.memory()` stores data only in memory and will be lost when the server restarts. Use a persistent store like Cloudflare or Vercel KV, or a Redis instance in production.
:::

### path

* **Type:** `string`

The base path where the handler will listen for requests. All three endpoints (`/challenge`, `/:credentialId`) will be mounted under this path.

```ts twoslash
// @noErrors
import { Handler } from 'tempo.ts/server'

const handler = Handler.keyManager({
  // ... other options
  path: '/api/keys', // [!code focus]
})

// Endpoints will be:
// GET  /api/keys/challenge
// GET  /api/keys/:credentialId
// POST /api/keys/:credentialId
```

### rp

* **Type:** `string | { id: string, name?: string }`

The Relying Party (RP) identifier and name. This is used to:

* Include RP information in the challenge response
* Verify the origin of credential registration requests

```ts twoslash
// @noErrors
import { Handler } from 'tempo.ts/server'

// Simple string (uses as both id and name)
const handler = Handler.keyManager({
  // ... other options
  rp: 'example.com', // [!code focus]
})

// Object with custom name
const handler2 = Handler.keyManager({
  // ... other options
  rp: { // [!code focus]
    id: 'example.com', // [!code focus]
    name: 'Example App', // [!code focus]
  }, // [!code focus]
})
```

:::info
The RP ID must match the domain where your application is hosted. For localhost, the origin verification is automatically skipped.
:::

## Storage Schema

The handler uses the following key patterns in the KV store:

* **`challenge:{hex}`** - Stores issued challenges
* **`credential:{credentialId}`** - Stores public keys

# Overview

Server handlers are framework-agnostic handlers that run on your backend to manage protocol operations that require server-side logic.

Handlers are compatible with any server framework that supports the:

* [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), and is exposed via the `Handler#fetch` function
* [Node.js `RequestListener` API](https://nodejs.org/api/http.html#http_class_http_serverrequestlistener), and is exposed via the `Handler#listener` function

```ts
import { Handler } from 'tempo.ts/server'
import { account, client } from './config'

const handler = Handler.feePayer({
  account,
  client,
  feeToken: '0x20c0…0001'
  path: '/fee-payer',
})

createServer(handler.listener) // Node.js

Bun.serve(handler) // Bun

Deno.serve(handler) // Deno

app.all('*', c => handler.fetch(c.request)) // Elysia

app.use(handler.listener) // Express

app.use(c => handler.fetch(c.req.raw)) // Hono

export const GET = handler.fetch // Next.js
export const POST = handler.fetch // Next.js
```

## Handlers

<Cards>
  <Card description="Server handler to handle transactions that require a fee payer" to="/sdk/typescript/server/handler.feePayer" icon="lucide:badge-dollar-sign" title="feePayer" />

  <Card description="Server handler to manage public key registrations" to="/sdk/typescript/server/handler.keyManager" icon="lucide:key-round" title="keyManager" />

  <Card description="Compose multiple handlers into a single handler" to="/sdk/typescript/server/handler.compose" icon="lucide:blocks" title="compose" />
</Cards>
