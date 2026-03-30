# Source: https://docs.meson.fi/implementation/smart-contracts/time.md

# Time

### Bond time and lock time

In the process of an atomic swap, both parties need to lock the funds on the initial and target chains respectively for a certain period of time. In order to ensure the safety and smoothness of swaps, the lock time for Meson is based on the related chains and swap amount. For chains that require longer confirmation times or swaps that have larger amounts, longer lock times are required.

### Time to finish a swap

Total time equals the sum of

* Time for `postSwap` / `bondSwap` with confirmations (confirmation time on the initial chain)
* Time for `lock` with confirmations (confirmation time on target chain)
* The duration between the swap is securely locked and the user publishes the release signature
* Time for `release` (confirmation time on target chain)

The time for broadcasting swap requests and swap releases on the relayer can be neglected which only takes \~1 second.

If the user signs for release right away, the total time for the swap equals one confirmation time on the initial chain plus two confirmation times on the target chain. For example,

* Ethereum → Non-Ethereum: 3-12 min
* Non-Ethereum → Ethereum: 6-20 min
* Non-Ethereum → Non-Ethereum: \~3 min

For some swaps of small amounts between non-Ethereum chains, users can even receive swapped amounts within 1 minute.
