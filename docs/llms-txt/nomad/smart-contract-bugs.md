# Source: https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/smart-contract-bugs.md

# Smart Contract Bugs

The third set of attacks we've seen on interoperability protocols are those exploiting smart contract vulnerabilities. Unlike key compromise and economic attacks however, smart contract bugs do not explicitly target the root of trust — meaning they do not attempt to take control of keys.

Rather, they find holes in the application or networking logic that were enshrined on-chain. A perfect example of this was [the Wormhole exploit](https://blog.chainalysis.com/reports/wormhole-hack-february-2022/), where the attacker exploited faulty smart contract code that allowed them to mint 120,000 WETH on Solana without escrowing the necessary collateral on the Ethereum side.

## How They Work

Smart contract vulnerabilities, like economic attacks, are myriad. Anytime logic interacting with user funds is deployed on-chain, it has the potential to introduce unintended behavior. As such, we've seen a range of smart contract vulnerabilities over time which eventually become well understood, like  [re-entrancy attacks](https://quantstamp.com/blog/what-is-a-re-entrancy-attack).

At their core, smart contract hacks involve hackers exploiting logic that does something different from what the app developer intended. The most severe outcome is the loss of all funds the contracts manage. Rather than enumerate the different categories of smart contract bugs here, we will point you to [this list of known attacks compiled by Consensys](https://consensys.github.io/smart-contract-best-practices/attacks/).

## Defense

Smart contract bugs are unfortunately incredibly common, and the only way to defend against them is to follow established and safe patterns, thoroughly test code, get multiple audits, and then pray that nobody missed anything.

Unfortunately, whenever on-chain logic begins interacting with and custodying significant value, one must expect hackers to comb through the code looking for vulnerabilities. Rather than repeating what many security experts have said here, we will point to [OpenZeppelin's documentation](https://docs.openzeppelin.com/).

In the context of interoperability, we need to ensure that both the messaging passing layer, as well as any cross-chain applications like token bridges have been thoroughly tested and audited by developers. In the case of Nomad, all of our smart contracts have been fully[ audited by Quantstamp](https://docs.nomad.xyz/operational-security/audits), and we also have [ImmuneFi bug bounties](https://docs.nomad.xyz/operational-security/bug-bounty) paying out $1M for critical vulnerabilities.
