# Source: https://docs.meson.fi/protocol/security/waiting-time.md

# Waiting Time

### How long to wait for a transaction on each chain?

In the process of atomic swaps, participants need to wait for the previous step to be executed and safely confirmed before proceeding to the next step. This will determine the overall time of the swap. During the process of a Meson swap, we recommend the following waiting times.

#### From `postSwap` → `bondSwap`

Right away. If `postSwap` transaction is reverted, `bondSwap` cannot be executed. If `postSwap` tx is replaced by another swap with the same encoding but different initiator, the LP can still bond to it because the swap properties are the same.

Notice that `postSwap` may specify the bonded provider. In this case `bondSwap` is not needed and cannot be executed.

#### From `postSwap` / `bondSwap` → `lock`

Wait for enough confirmations on the initial chains. Otherwise, `postSwap` or `bondSwap` transaction may be reverted.

#### From `lock` → publish release signature

Wait for enough confirmations on the target chains. Otherwise, the `lock` transaction may be reverted.

#### From publish release signature → `release` & `executeSwap`

Right away. The order doesn’t matter.
