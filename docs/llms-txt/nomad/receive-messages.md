# Source: https://docs.nomad.xyz/developers/quickstart/receive-messages.md

# Receive Messages

Receive messages from other chains by implementing the `handle()` method in your cross-chain application.

### Interface

The `handle` method passes a cross-chain message to the application.

* `_origin` is a Nomad domain. List of domains **here**
* `_nonce` is unique for each message within a (`origin` domain, `destination` domain) tuple. Many apps won't need to use this field, but it can be used to ensure uniqueness of a message.
* `_sender` is the address that **sent** the message on the origin domain
* `_message` contains the contents of the cross-chain message&#x20;

```solidity
/*
 * @notice Receive a message from a sender on the origin domain 
 * @param _origin Domain of the origin chain
 * @param _nonce Unique nonce for the (origin, destination) tuple. 
 * @param _sender Address of sender on origin chain as bytes32
 * @param _message Raw bytes content of message
 */
 function handle(
    uint32 _origin,
    uint32 _nonce,
    bytes32 _sender,
    bytes memory _message
) external;
```

### Hello World

The example app we know and love - but make it cross-chain :handshake:&#x20;

```solidity
 import {TypeCasts} from "@nomad-xyz/contracts-core/libs/TypeCasts.sol";
 
 contract HelloWorld {
    // emitted when a Hello message is received   
    event Hello(uint32 origin, address sender, string memory message);
    
   /*
    * @notice Receive a Hello message from any sender :) 
    * @param _origin Domain of the origin chain
    * @param _sender Address of sender on origin chain as bytes32
    * @param _message Raw bytes content of message
    */
    function handle(
       uint32 _origin,
       uint32 _nonce,
       bytes32 _sender,
       bytes memory _message
    ) onlyReplica {
       address _sendr = TypeCasts.bytes32ToAddress(_sender);
       // emit the message so off-chain friends can see it
       emit Hello(_origin, _sendr, _message);
    }
}
```

### Example Usage

Ready to get a little more advanced? Let's play PingPong across chains :ping\_pong:

```solidity
contract PingPong {
    // registry of opponents on each chain
    mapping(uint32 => bytes32) public opponents;
    
    // emitted when a Ping volley is received
    event Ping(uint32 domain, bytes32 opponent, uint256 volleyNumber);
    // emitted when a Pong volley is received
    event Pong(uint32 domain, bytes32 opponent, uint256 volleyNumber);

    /**
     * @notice Start a PingPong match with the destination chain
     * by serving the ball.
     * @param _destination The domain to initiate the match with
     */
    function handle(
       uint32 _origin,
       uint32 _nonce,
       bytes32 _sender,
       bytes memory _message
    ) onlyReplica {
        // validate the message comes from a known opponent
        require(opponents[_origin] == _sender, "not a registered opponent!");
        // decode the message contents using abi.decode
        bool _ping;
        uint256 _volley;
        (_ping, _volley) = abi.decode(_message, (bool, uint256));
        // emit an event for your off-chain spectators
        if (ping) {
            emit Ping(_origin, _sender, _volley);
        } else {
            emit Pong(_origin, _sender, _volley);
        }
        // send a PingPong message back to your opponent!
        bytes memory _message = abi.encode(!_ping, _volley + 1);
        // dispatch your message across chains
        home.dispatch(_origin, _sender, _message);
    }
}
```

### Advanced Examples

* `BridgeRouter.sol`[ handle](https://github.com/nomad-xyz/monorepo/blob/93daaf931378b79c53e3c494af9671c59e843ee1/packages/contracts-bridge/contracts/BridgeRouter.sol#L105)
* `GovernanceRouter.sol` [handle](https://github.com/nomad-xyz/monorepo/blob/497a0f702100800db7e37576ca16f76c180830f5/packages/contracts-core/contracts/governance/GovernanceRouter.sol#L222)
* Gnosis `NomadModule.sol` [handle](https://github.com/gnosis/zodiac-module-nomad/blob/609a044936a95d51dcd6063b902494ea9baafa8a/contracts/NomadModule.sol#L153)

### **FAQs**

**Why ensure messages come from `onlyReplica`?**

This ensures that the message is a real cross-chain message coming from the Nomad system, not an impostor!&#x20;
