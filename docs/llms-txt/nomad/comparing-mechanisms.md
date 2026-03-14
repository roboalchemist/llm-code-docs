# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/comparing-mechanisms.md

# Comparing Mechanisms

Each of the previously discussed verification mechanisms ([native](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification), [external](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification), [optimistic](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification)) has its benefits and costs. As the famous economist, Thomas Sowell, once said:

> “There are no solutions. There are only trade-offs.”

Therefore, there is no *best* solution for all use cases, rather trade-offs that must be made by the application developer deciding to use the messaging system. In this section, we will present a simplified exploration of the trade-off space.

### Comparison of Mechanisms

<table><thead><tr><th width="150">Verification Mechanism</th><th width="150">Trust Assumption</th><th width="150">Security</th><th width="150">Extensibility / Reusability</th><th width="150">Cost</th></tr></thead><tbody><tr><td>Light Client Relay</td><td>Untrusted with synchrony assumptions</td><td><mark style="background-color:green;">Very High</mark></td><td><mark style="background-color:red;">Low</mark></td><td><mark style="background-color:red;">High</mark></td></tr><tr><td>Optimistic</td><td>Honest 1-of-n</td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:yellow;">Medium</mark></td></tr><tr><td>Validator / PoS</td><td>Honest k-of-n with social slashing</td><td><mark style="background-color:yellow;">Medium</mark></td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:yellow;">Medium</mark></td></tr><tr><td>Multi-signature Addresses</td><td>Honest k-of-n</td><td><mark style="background-color:red;">Low</mark></td><td><mark style="background-color:green;">Very High</mark></td><td><mark style="background-color:green;">Low</mark></td></tr></tbody></table>
