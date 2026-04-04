# Source: https://docs.meson.fi/protocol/meson/lp.md

# Liquidity Providers

Liquidity Providers (LPs) of Meson are responsible for matching incoming swap orders submitted by users. A swap is completed when user sends the designated fund to the LP pool on the initial chain, followed by the release of fund to the user from the LP pool on the target chain. Meson's atomic swap mechanism guarantees that either transfers of funds happen on both networks or neither happens at all, enforcing funds security for both users and LPs.

Pool owner is the designated owner of LP. Any valid wallet address signing up to become a LP of Meson is designated by Meson as the pool owner. Signing up for LP requires depositing liquidity to more than one networks supported by Meson. LPs can have their own choices of supported networks and tokens and deposit liquidity accordingly to the Meson smart contract on respective networks.

Each LP manage and operate his/her own independent liquidity pools designated by a unique pool index. LP is required to register a pool index (see `depositAndRegister` method) when they deposit liquidity for the first time. When a cross-chain swap is requested, LPs are opt to make independent decision whether they would like to match this specific swap order (which requires signature). However, only one LP will eventually match and complete the swap with the user. Therefore, there will be one unique pool index matching every successful swap, representing the pair of atomic swaps between user and the designated LP pool on the origin and target chains.

## Access to LP Pools

### Pool owner

Each LP pool has an *owner*. Owner address is the sole wallet address that is permitted to perform depositing and withdrawing liquidity opreations on LP pools. When an LP deposit liquidity to Meson for the first time and register a pool index, the signer address will be recorded as the owner for the LP pool created. Each address is only allowed to own one LP pool per network.

#### Permitted interactions for pool owners

Only the pool owner is permitted to call the following contract methods:

* `depositAndRegister`: First-time deposit of liquidity and register pool index; Caller becomes the pool owner;
* `deposit`: Deposit of liquidity to an existing LP pool
* `withdraw`: Withdrawal of liquidity from an existng LP pool

![Operations of Pool Owners](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-bfe951fc36f8c932de6b6a889f11dd44a9a136ff%2FMeson-LP-flow.png?alt=media)

### Authorized addresses

As LPs are required to sign for each swap, Meson allows the pool owner to grant others as *authorized addresses* to perform swaps on its behalf. Please note the pool owner is always an authorized address of its own pool.

In this design of authorization, LPs no longer need to expose their private key every time to perform swaps after depositing liquidity, whereas authorized addresses could call Meson smart contract to perform swaps with the liquidity available in the pools. Funds only moves around the designated LP pools on different networks and therefore exposes to very low security risk by authorizing swaps. Authorized addresses are not permitted to withdraw liquidity under any circumstances, as only the pool owner is permitted to do so.

#### Permitted interactions for authorized addresses

Authorized addresses are permitted to call the following contract methods:

* `bondSwap`: Upon acknowledgement of user's swap request, call on the initial chain to match the user swap order (no pool fund movement involved);
* `lock`: Upon acknowledgement of user swap request, call on the target chain to lock in funds in the pool, which will be releasd to user in the following `release` call;
* `release`: Upon successful order match (both `bondSwap` and `lock` executed), call on the target chain to release the locked funds to the user to complete the swap (meanwhile, call to `executeSwap` will be exectued to acquire the inbound fund from user and add it to the LP pool on the initial chain).

![Operations of Authorized Addresses](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-aabe8b0a1f3030f80d33692029ad3acea8361fb2%2FMeson-LP-flow-authAccess.png?alt=media)
