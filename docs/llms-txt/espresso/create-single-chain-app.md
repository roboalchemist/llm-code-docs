# Source: https://docs.espressosys.com/network/guides/dapp/create-single-chain-app.md

# Create a Single-Chain Application Reading From a Caff Node

This guide showcases how to use Espresso Caff Nodes to enable instant token swaps inside a single rollup chain. Specifically, we create a Swap application on Rari testnet where users can swap TokenA ↔ TokenB with fast confirmation from Espresso.

The flow is the following:

* User calls swap() on the smart contract.
* The Sequencer orders the transaction, Batch Poster posts to the Parent Chain.
* Espresso Caff Node immediately indexes the swap result and exposes it via API.
* The dApp frontend queries the Caff Node to show the updated balance instantly.

### Before You Begin

* Clone the repo: <https://github.com/enoldev/espresso-examples>, and move to the `instant-swap` folder.
* Install Foundry and ensure forge, cast, and anvil are available.
* Have ETH on Rari testnet (for deployment and gas fees).
* Ensure you have an Espresso Caff Node running (use the provided testnet endpoint or spin up your own).

### The Instant Swap Application

We’ll implement a very simple Automated Market Maker (AMM) smart contract:

* Users can deposit TokenA and TokenB into the pool.
* Users can call swapAForB(amount) or swapBForA(amount).
* The contract uses the constant product formula (x \* y = k) for swaps.

#### Inspect the Code

In order to test the AMM contract, we will need to mock the ERC20 tokens. The following contract is a very simple `MockERC20`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract MockERC20 {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function mint(address to, uint256 amount) external {
        balanceOf[to] += amount;
        totalSupply += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "ERC20: insufficient");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        uint256 allowed = allowance[from][msg.sender];
        require(allowed >= amount, "ERC20: allowance");
        require(balanceOf[from] >= amount, "ERC20: from balance");
        allowance[from][msg.sender] = allowed - amount;
        balanceOf[from] -= amount;
        balanceOf[to] += amount;
        emit Transfer(from, to, amount);
        return true;
    }
}
```

The AMM contract includes very simple logic for token swaps (TokenA and TokenB):

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

interface IERC20Minimal { // 1.
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract SimpleAMM {
    IERC20Minimal public tokenA;
    IERC20Minimal public tokenB;

    uint256 public reserveA; // 2.
    uint256 public reserveB;

    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    event SwapAForB(address indexed trader, uint256 amountAIn, uint256 amountBOut);

    constructor(address _tokenA, address _tokenB) { // 3.
        tokenA = IERC20Minimal(_tokenA);
        tokenB = IERC20Minimal(_tokenB);
    }

    function _updateReserves() internal {
        reserveA = tokenA.balanceOf(address(this));
        reserveB = tokenB.balanceOf(address(this));
    }

    /// @notice Add liquidity (caller must approve this contract)
    function addLiquidity(uint256 amountA, uint256 amountB) external { // 4.
        require(amountA > 0 && amountB > 0, "zero amounts");
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "transferA failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountB), "transferB failed");
        _updateReserves();
        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    /// @notice Swap exact amountA for tokenB. Very simple pricing: amountOut = amountAIn * reserveB / (reserveA + amountAIn)
    function swapExactAForB(uint256 amountAIn, uint256 minBOut) external returns (uint256 amountBOut) { // 5.
        require(amountAIn > 0, "zero in");
        // transfer A in
        require(tokenA.transferFrom(msg.sender, address(this), amountAIn), "transferFrom A failed");

        // read reserves before adding amountAIn
        uint256 oldReserveA = reserveA;
        uint256 oldReserveB = reserveB;
        require(oldReserveA > 0 && oldReserveB > 0, "empty pool");

        // Simple constant product without fees:
        // amountBOut = amountAIn * reserveB / (reserveA + amountAIn)
        amountBOut = (amountAIn * oldReserveB) / (oldReserveA + amountAIn);
        require(amountBOut >= minBOut, "insufficient output amount");

        // send B to trader
        require(tokenB.transfer(msg.sender, amountBOut), "transfer B failed");

        // update reserves
        _updateReserves();

        emit SwapAForB(msg.sender, amountAIn, amountBOut);
    }
}
```

1. We declare a minimal ERC20 interface (`IERC20Minimal`) with only the functions we need: transferFrom, transfer, and balanceOf. This avoids importing the full OpenZeppelin ERC20 implementation, keeping the example lightweight.
2. The contract stores two ERC20 tokens (TokenA, TokenB) that can be swapped. `reserveA` and `reserveB` track the balances of each token held in the contract — representing the liquidity pool.
3. The constructor sets the token addresses for TokenA and TokenB that this AMM will support.
4. `addLiquidity` lets a user deposit both TokenA and TokenB into the pool. The caller must first approve the AMM contract to spend their tokens. Transfers the tokens in, updates reserves, and emits a LiquidityAdded event.
5. `swapExactAForB` allows a user to swap a specific amount of TokenA for TokenB. It first requires the user to approve TokenA spending. Then it pulls amountAIn into the contract

#### Deploy the Smart Contracts

The `script/Deploy.s.sol` file contains the logic to deploy two tokens: `TKA` and `TKB`, and the `AMM` contract. It also sends the tokens to the *deployer* address (the address used to deploy the contracts).

```bash
forge script script/Deploy.s.sol:Deploy \
  --rpc-url https://rari-testnet.calderachain.xyz/http \
  --private-key $PRIVATE_KEY \
  --broadcast -vv
```

After executing the script, the addresses of the deployer, tokens and AMM contract will be displayed in the logs. Create the environment variables.

```bash
export AMM_ADDR=0x
export TKA=0x
export TKB=0x
export DEPLOYER=0x
```

#### Test the App

Now, you can use the Rari Testnet Caff Node to test the application:

1. First, check the balance of the deployer address for each token. If the deployment script has been executed correctly, the deployer address must be funded with both tokens.

```bash
cast call $TKA "balanceOf(address)(uint256)" $DEPLOYER --rpc-url https://rari.caff.testnet.espresso.network
```

```bash
cast call $TKB "balanceOf(address)(uint256)" $DEPLOYER --rpc-url https://rari.caff.testnet.espresso.network
```

1. Then, execute the `approve(...)` function in the `TKA` smart contract (this is necessary to comply with the ERC20 standard).

```bash
cast send $TKA "approve(address,uint256)" $AMM_ADDR 1000000000000000000000 \
  --private-key $PRIVATE_KEY --rpc-url https://rari.caff.testnet.espresso.network
```

2. Now, you will be able to call the `swapExactAForB(...)` function:

```bash
cast send $AMM_ADDR "swapExactAForB(uint256,uint256)" 1000000000000000000 0 \ 
  --private-key $PRIVATE_KEY --rpc-url https://rari.caff.testnet.espresso.network
```
