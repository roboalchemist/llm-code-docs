# Source: https://docs.meson.fi/protocol/security.md

# Security Precautions

In order to ensure the safety of the funds of both parties of users and LPs, some necessary matters need to be paid attention to during the swap process.

Worth mentioning that Meson does not rely on cross-chain services such as bridges and oracles in its swap process, so it will not be affected by the security issues of third-party services.

### Precautions for Users

#### Swap signature phishing

Severity: 🟥🟥🟥

Attackers might attempt to forge a website for Meson and phish for users' signatures. This attempt, if succeeded, could mislead users to sign for unintended cross-chain swaps that transfer funds to attackers' addresses, causing a loss of funds to users. Users should exercise a high degree of caution to make sure they're on Meson's official website (\[<https://meson.fi>]) while making cross-chain swaps.

#### Congested target chain

Severity: 🟥🟥🟥

When the target chain of a cross-chain swap becomes congested, the swap might not be able to complete. Users might need to pay a higher gas fee to support the execution of `release` operation within the lock period. Otherwise, the LP could `unlock` the fund after the lock ends, causing a loss of funds to the user.

We recommend against cross-chain swaps when the network is very congested. Usually in this case, the initial step of the swap `bondSwap` cannot be completed.

**WIP**

#### Release too late

Severity: 🟥🟥🟥

If the user posts the release signature after the lock period, the LP could `unlock` his/her fund and use the release signature to retrieve the user's fund, causing a loss of fund to the user. We strongly recommend users only post the release signature in a timely manner and do not attempt to sign for release if it's deemed too late. The Meson app has procedures in place to deal with such circumstances.

#### Release too early

Severity: 🟨🟨⬜️

If the user does not wait for enough block confirmations and posts the release signature too soon, the `lock` transaction might be reverted and the user will not be able to get swapped funds on the target chain. We strongly recommend users wait for enough block confirmations before signing the release signature. The Meson app has procedures in place to deal with such circumstances.

#### No release

Severity: 🟨🟨⬜️

Upon receiving the release signature from the user, a misbehaved LP could only call `execute` but not `release`. This LP will hence retrieve the user's fund on the initial chain without paying out to the user on the target chain. If the `release` operation is not called within the lock period, the LP could `unlock` and the user will not be able to get swapped funds. However, anyone, including the user, could complete the release process once the release signature is revealed. Meson will guarantee the execution of `release` operation within the proper time period.

In the future, We will introduce penalties for such misbehaved LPs.

#### No lock

Severity: 🟩⬜️⬜️

The swap process will not continue if a misbehaved LP does not `lock` after successful `bondSwap` operation. However, such LPs will have to pay gas fees but receive no benefit at all. Users will need to wait until expiration to withdraw their funds and restart a new swap.

In the future, We will introduce penalties for such misbehaved LPs.

#### Front-running

Severity: 🟩⬜️⬜️

When a swap request is submitted, attackers might forge a fake swap with the same encoding and execute it on the initial chain to block the user's swap, as only one swap is allowed per encoding. However, the attacker will have to lock his/her own fund for 1-2 hours and pay gas fees, but receive no benefit at all. Users who encountered this type of issue can simply bypass it by resubmitting another swap.

### Precautions for LPs

#### Congested initial chain

Severity: 🟥🟥🟥

When the initial chain of a cross-chain swap becomes congested, swaps might not be able to complete. LPs might need to pay a higher gas fee to support the execution of `executeSwap` operation to retrieve users' funds. Otherwise, the user could withdraw the fund after the swap expires, causing a loss of funds to the LP.

We recommend against cross-chain swaps when the network is very congested. Usually in this case, the initial step of the swap `lock` cannot be completed.

**WIP**

#### Lock too late

Severity: 🟥🟥🟥

If the LP `lock`s a swap too late causing the fund remains locked beyond the swap's expiration time, the user could temporarily hold his/her release signature till the swap expires. Hereafter, the user could execute `cancelSwap` to withdraw his/her fund and attempt `release` operation to retrieve the LP's fund, causing loss of fund to the LP. We strongly recommend LPs call `lock` operation in a timely manner and do not attempt to `lock` when it's deemed too late. The Meson LP service has procedures in place to deal with such circumstances.

#### Lock too early

Severity: 🟨🟨⬜️

If the LP does not wait for enough block confirmations of `postSwap/bondSwap` operations before calling `lock`, the `postSwap/bondSwap` transaction might be reverted and LPs will not be able to get swapping funds on the initial chain. We strongly recommend LPs wait for enough block confirmations before calling `lock`. The Meson LP service has procedures in place to deal with such circumstances.

#### No release signature

Severity: 🟩⬜️⬜️

A misbehaved user might choose not to post the release signature after submission of swap request and fund being locked. Although funds on both intial and target chains stay safe, a part of LP's liquidity will be locked for a period of time and paid gas fees were wasted. However, the user's fund will also be locked for longer time.

In the future, We will introduce penalties for such misbehaved users.

#### Double spending

Severity: 🟩⬜️⬜️

A misbehaved user might repeatedly submit multiple swap requests without enough available stablecoins in his/her address. The Meson contract need to acquire swapping fund when executing `postSwap`, whereas the lack of balance or approval will lead to execution failure. In this case, the LP may waste some gas fees for failed transactions. We recommend LPs perform balance and approval checks before processing users' swap requests.

In the future, We will introduce penalties for such misbehaved users.

### Attack to Relayers

#### Spamming

Severity: 🟨🟨⬜️

Attackers may spam the Meson relayer with excessive trash messages to congest the relayer service. The Meson relayer will check each received request to confirm the data conforms to the Meson protocol and the swap initiator has enough balance to carry out the cross-chain swap. Meson also requires at least US$0.01 in stablecoins to be transferred per swap. After the conditions are met, the relayer will broadcast the data to other connected nodes or LP services. In this way, the spamming attack will only affect one relayer node, and other relayers can still continue to operate.
