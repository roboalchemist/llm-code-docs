# Source: https://docs.nomad.xyz/token-bridge/smart-contracts/bridgerouter.md

# BridgeRouter

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol>

The BridgeRouter contract is the entry point for the token bridge application and implements its interface, per [the Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern). It enables users to “send” tokens from Chain A to Chain B via a lock-and-mint mechanism.

### Sending and Receiving Tokens

#### Sending&#x20;

The sending side logic is implemented in the [`send`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L134) function:

```solidity
// ======== External: Send Token =========

/**
 * @notice Send tokens to a recipient on a remote chain
 * @param _token The token address
 * @param _amount The token amount
 * @param _destination The destination domain
 * @param _recipient The recipient address
 */
function send(
    address _token,
    uint256 _amount,
    uint32 _destination,
    bytes32 _recipient,
    bool /*_enableFast - deprecated field, left argument for backwards compatibility */
) external;
```

#### Receiving

The receiving side logic is implemented in the [`handle`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L96) function:

```
// ======== External: Handle =========

/**
 * @notice Handles an incoming message
 * @param _origin The origin domain
 * @param _nonce The unique identifier for the message from origin to destination
 * @param _sender The sender address
 * @param _message The message
 */
function handle(
    uint32 _origin,
    uint32 _nonce,
    bytes32 _sender,
    bytes memory _message
) external override onlyReplica onlyRemoteRouter(_origin, _sender);
```

#### Lock-and-Mint Mechanism

The BridgeRouter enforces the following strict invariant:

> The amount locked on the chain where the token originates must always be equal to the circulation of representational tokens minted on all destination chains.

You can see this in the codebase here:

* Sending side: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L149>
* Receiving side: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L278>

### Enrolling Custom Representations

The BridgeRouter enables custom tokens to be enrolled by calling [`enrollCustom`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L200):

```solidity
    // ======== External: Custom Tokens =========

    /**
     * @notice Enroll a custom token. This allows projects to work with
     * governance to specify a custom representation.
     * @param _domain the domain of the canonical Token to enroll
     * @param _id the bytes32 ID of the canonical of the Token to enroll
     * @param _custom the address of the custom implementation to use.
     */
    function enrollCustom(
        uint32 _domain,
        bytes32 _id,
        address _custom
    ) external onlyOwner {
        // Sanity check. Ensures that human error doesn't cause an
        // unpermissioned contract to be enrolled.
        IBridgeToken(_custom).mint(address(this), 1);
        IBridgeToken(_custom).burn(address(this), 1);
        tokenRegistry.enrollCustom(_domain, _id, _custom);
    }
```
