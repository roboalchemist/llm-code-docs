# Source: https://docs.nomad.xyz/developers/quickstart/send-messages.md

# Send Messages

Send messages to other chains by calling the `dispatch()` method on the `Home` contract.

### Interface

The `dispatch` method is simple. Just specify the destination chain, the message recipient, and the message you want to send!

* `_destination` is a Nomad domain. List of domains **here**
* `_recipient` is the address that will receive the message on the destination chain. The `_recipient` must be set up to **receive** Nomad messages by implementing `handle`.
* `_message` contains the contents of your cross-chain message&#x20;

```solidity
/*
 * @notice Dispatch the message to the destination domain & recipient
 * @param _destination Domain of destination chain
 * @param _recipient Address of recipient on destination chain as bytes32
 * @param _message Raw bytes content of message
 */
 function dispatch(
     uint32 _destination,
     bytes32 _recipient,
     bytes memory _message
 ) external {
   // message is sent to recipient address on destination chain
 }
```

### Hello World

The example app we know and love - but make it cross-chain :handshake:&#x20;

```solidity
 import {TypeCasts} from "@nomad-xyz/contracts-core/libs/TypeCasts.sol";
 
 contract HelloWorld {
    // address of the Nomad Home contract
    immutable address public home;

    /*
     * @notice Send a Hello message to another chain :)
     * @param _destination Domain of destination chain
     * @param _recipient Address of recipient on destination chain
     */
    function hello(uint32 _destination, address _recipient) {
        // craft your hello message
        bytes memory _message = "hello world >:~)";
        // cast recipient to bytes32
        bytes32 _recip = TypeCasts.addressToBytes32(_recipient);
        // dispatch your message across chains!
        home.dispatch(_destination, _recipient, _message);
    }
}
```

### Example Usage

Ready to get a little more advanced? Let's play PingPong across chains :ping\_pong:

```solidity
contract PingPong {
    // registry of opponents on each chain
    mapping(uint32 => bytes32) public opponents;

    /**
     * @notice Start a PingPong match with the destination chain
     * by serving the ball.
     * @param _destination The domain to initiate the match with
     */
    function serve(uint32 _destination) external {
        // serve to your opponent on the destination domain
        bytes32 _recipient = opponents[_destination];
        // Create a message for the first volley.
        // the PingPong match always begins with a Ping
        bool _ping = true;
        // the volley count always starts at 0
        uint256 _volley = 0;
        // encode the PingPong message using abi.encode
        bytes memory _message = abi.encode(_ping, _volley);
        // dispatch your message across chains!
        home.dispatch(_destination, _recipient, _message);
    }

}
```

### Advanced Examples

* `BridgeRouter.sol` [send](https://github.com/nomad-xyz/monorepo/blob/93daaf931378b79c53e3c494af9671c59e843ee1/packages/contracts-bridge/contracts/BridgeRouter.sol#L134)
* `GovernanceRouter.sol` [executeGovernanceActions](https://github.com/nomad-xyz/monorepo/blob/497a0f702100800db7e37576ca16f76c180830f5/packages/contracts-core/contracts/governance/GovernanceRouter.sol#L254)

### **FAQs**

**Why domains instead of chain IDs?**

Chain IDs change during intentional consensus splits such as the merge to Eth2.0; additionally, not all chains even have a Chain ID! We created Nomad domains to have a clean standard for chains supported by Nomad which didn't suffer from these challenges. &#x20;

**Why are recipients `bytes32` instead of `address`?**

We use `bytes32` instead of `address` so that, in the future, messages will be compatible with other chain VMs like Cosmos and Polkadot. In the EVM, addresses are 20 bytes long, but most other chains have 32 byte addresses. Worry not - we have a `TypeCasts.sol` library to help convert between these types easily.
