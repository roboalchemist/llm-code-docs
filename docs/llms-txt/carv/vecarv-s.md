# Source: https://docs.carv.io/carv-token/utility/vecarv-s.md

# veCARV(s)

## Intro

We are excited to announce the launch of veCARV(s), a new staking token designed to empower our community with flexible staking options and enhanced reward potential. Inspired by the Curve model, veCARV(s) allows users to lock their CARV tokens for varying durations, from one month to three years, with corresponding multipliers that increase the longer the stake is held. This model not only incentivizes long-term commitment but also provides users with the flexibility to choose a staking period that best aligns with their investment strategy. The longer you stake, the higher the reward multiplier, offering up to a 9x boost for a three-year commitment. This tiered multiplier structure ensures that every participant, whether they prefer short-term or long-term staking, can benefit from the veCARV(s) system.

**Code:** <https://github.com/carv-protocol/carv-contracts-alphanet/blob/staking/contracts/staking/veCarvs.sol>

## Function Description

1. veCarv(s) is not a standard ERC20 token and does not support `transfer`, `approve`, `allowance`, or `transferFrom`.
2. The ERC20 interfaces supported by veCarv(s) are: `name`, `symbol`, `balanceOf`, and `totalSupply`.

## Staking

1. Users obtain veCarv(s) tokens by staking CARV into the veCarv(s) contract. The veCarv(s) tokens are not actually transferred to the user’s address; instead, each time a user calls `balanceOf`, a real-time balance is calculated for the user (the same applies to `totalSupply`).
2. The initial amount of veCarv(s) a user receives after staking CARV is calculated as: the amount of CARV \* staking duration \* staking coefficient (where the staking coefficient is tentatively set at 1/120D, meaning that when the staking duration is 120 days, the user initially receives veCarv(s) at a 1:1 ratio).
3. A user’s veCarv(s) balance will decay linearly over time (decaying per block, meaning that without new staking, the user’s balance will decrease with each block).
4. Each time a user stakes, a new position is created for the user, recording the amount of CARV tokens staked and the lock-up expiration time.
5. There are no restrictions on the amount of CARV a user can stake or the number of positions a user can hold. However, the lock-up duration of each position must be a multiple of the minimum period T.
6. Users can initiate staking at any time, but the start time of each position in the contract is the start time of the current period T (for example, if T is one week and a user initiates staking on Wednesday, the actual staking start time is Monday at midnight, meaning that the tokens have already decayed partially by the time the staking is initiated).
7. When a user holds multiple positions, the balance is the sum of all positions, but each position can only be redeemed upon expiration; it cannot be added to or have its duration extended.

## Redemption

1. Users can only redeem positions that have reached their expiration date. The redeemed amount will be equal to the staked amount.
2. After the user’s position expires, they can either redeem positions individually or combine them for redemption.

## Minimum Period T

1. To calculate `totalSupply` and `balanceOf`, the contract implements a special algorithm (for detailed explanation, refer to the section \[Algorithm Description] below). This algorithm introduces the concept of the minimum period T into the contract.
2. T is the smallest unit for contract settlement (settlement can be either automatic or triggered by external assistance; external assistance is optional and will not affect the contract’s functionality if absent). The recommended range for T is 1 day to 1 week.
3. If T is too short, it will increase the gas costs for users and CARV officials; if T is too long, it will reduce the flexibility of user operations (because the lock-up duration must be a multiple of T, and the start time for each position must align with the start time of a given T).

## Interface Description

*(This section only covers core function interfaces; non-core interfaces are not described here)*

<table><thead><tr><th width="370">Endpoints</th><th></th></tr></thead><tbody><tr><td><strong>balanceOf</strong>(address user)</td><td>Queries the veCarv(s) balance of a specified user.</td></tr><tr><td><strong>balanceOfAt</strong>(address user, uint256 timestamp)<br></td><td><p>Queries the veCarv(s) balance of a specified user at a specific time.</p><p>Note⚠️: This specified time can be any time in the future or past but does not support times before the contract deployment.</p></td></tr><tr><td><strong>totalSupply</strong>()</td><td>Queries the current total supply of veCarv(s).</td></tr><tr><td><strong>totalSupplyAt</strong>(uint256 timestamp)</td><td>Queries the total supply of veCarv(s) at a specific time.<br><strong>Note⚠️:</strong> The time rules are the same as for <code>balanceOfAt</code>.</td></tr><tr><td><strong>deposit</strong>(uint256 amount, uint256 duration)</td><td>The user inputs the amount to stake and the lock-up duration, and the contract creates a position.<br><strong>Note⚠️:</strong> The staked amount can be any quantity, but the lock-up duration must be a multiple of the minimum period T.</td></tr><tr><td><strong>withdraw</strong>(uint64 positionID)</td><td>The user inputs a position ID to redeem an expired position. Multiple positions can be redeemed together (via <code>multicall</code>).</td></tr><tr><td><strong>positions</strong>(uint64 positionID)</td><td>Queries the status of a position by its ID (such as the staked amount, lock-up expiration time, etc.).</td></tr></tbody></table>

## Algorithm Description

{% hint style="info" %}
**What problem does this algorithm solve?**

In the process of calculating balanceOf and totalSupply for veCarv(s), there is no actual map that records the balance of each user or the global balance. The smallest unit of storage in the contract is the position. To calculate the real-time totalSupply, the most straightforward method would be to traverse and calculate all positions, which is obviously impractical. This algorithm was developed to address this issue (by allocating a small amount of storage in exchange for reducing the number of read operations during each calculation).

This algorithm draws inspiration from parts of the Curve algorithm and has been modified to better suit the needs of veCarv(s).
{% endhint %}

**How does this algorithm calculate veCarv(s) `totalSupply`?**

1. To aid understanding, we establish a two-dimensional coordinate system, with the horizontal axis representing time and the vertical axis representing the quantity of veCarv(s).
2. First, let's consider the simplest scenario where only one user has created a single position. The relationship between the global veCarv(s) quantity and time is given by:\
   $$TotalSupply = slope \* (t - t\_{end})$$, where `slope` is the rate of decline: $$slope = \frac{0-initialSupply}{t\_{end} - t\_{begin}}$$, where ​`t` is the time variable, and its valid range is $$t\_{begin} ～ t\_{end}$$. `initialSupply` is the initial veCarv(s) quantity after the user creates the position, as shown in the figure below:<br>

   <figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FD4qGPiT1P7bWYOAxcvGl%2Fimage.png?alt=media&#x26;token=f6473b8b-04c2-476d-a70b-d4f5042839d8" alt=""><figcaption></figcaption></figure>
3. At this point, we can easily calculate the `totalSupply` of veCarv(s) at any time between $$t\_{begin} ～ t\_{end}$$ using this formula.
4. However, when the system has multiple positions simultaneously, the graph will look like the one below, where each black solid line represents the decay curve of a single position.<br>

   <figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FRJ5mOb4pcId712zXySJ5%2Fimage.png?alt=media&#x26;token=4003dbac-2305-4123-864c-f981f21d4f3c" alt=""><figcaption></figcaption></figure>
5. By summing the functions of these three black solid lines, we can obtain the global decay function of `totalSupply`. It's also evident that the slope of the global decay function changes at each time point t1 to t6, which correspond to the start and end times of each position. These are the points where the slope of the global decay curve changes.
6. We can store the global curve in an array of `Point`s, where each `Point` stores three values:
   1. The horizontal coordinate `t`, which represents the time.
   2. The vertical coordinate `bias`, which represents the initial `totalSupply` at the current time.
   3. The slope, which indicates the rate of decay of the curve until the next `Point`.
7. With this `Point` array, calculating `totalSupply` at the current time or at any future time becomes very simple:
   1. Suppose we want to calculate `totalSupply` at the time $$t\_{target}$$​, and the most recent `Point` corresponds to the time $$t\_{current}$$​.
   2. If $$t\_{target} > t\_{current}$$, the slope of the curve changes as the current active positions expire, so we calculate by iterating forward.
   3. If $$t\_{target} < t\_{current}$$​, we can iterate backward through the `Point`s to find the corresponding interval and then calculate.
8. Below is an explanation of how this `Point` array is constructed:
   1. Define the minimum operation period T. The `Point`s are discrete, and the minimum interval between `Point`s is T, but the entire curve is continuous (continuity of the curve means that `totalSupply` and `balanceOf` can be calculated at any time).
   2. Initialization: The first `Point` is (0, 0), and the slope is also 0.
   3. For each subsequent position's start and end time, a new element is added to the `Point` array. The code is as follows:

```solidity
solidityCopy code// From the previous Point's t to the current t
for (uint32 epochIndex = lastRecordEpoch + 1; epochIndex <= currentEpoch; epochIndex++) {
    // Update epochPoints only if the slope changes or the current t is reached
    if (slopeChanges[epochIndex] == 0 && epochIndex < currentEpoch) {
        continue;
    }

    // Previous Point
    EpochPoint memory lastEpochPoint = epochPoints[epochPoints.length - 1];
    // New Point
    EpochPoint memory epochPoint;
    // slopeChanges records (t => slope change)
    // New slope = old slope + current slope change (the current slope change can be + or -)
    epochPoint.slope = lastEpochPoint.slope + slopeChanges[epochIndex];
    // Current initial supply = previous point's slope * time decay + new positions added at this t
    epochPoint.bias = lastEpochPoint.bias - (uint256(lastEpochPoint.slope) * (epochIndex - lastEpochPoint.epochIndex) * DURATION_PER_EPOCH);
    // Record t
    epochPoint.epochIndex = epochIndex;
    epochPoints.push(epochPoint);
}
```

9. Using the above algorithm, we can calculate `totalSupply` at any given time with relatively low cost. Similarly, we can also calculate `balanceOf` (which is the `totalSupply` at the user address level).
