# Generate validator signature
./bin/0gchaind deposit create-delegation-validator \
    $STAKING_ADDRESS \
    $AMOUNT \
    $HOMEDIR/config/genesis.json \
    --home $HOMEDIR \
    --chaincfg.chain-spec=mainnet \
    --override-rpc-url \
    --rpc-dial-url https://evmrpc.0g.ai
```

**Output:**
```
✅ Staking message created successfully!
Note: This is NOT a transaction receipt; use these values to create a validator initialize transaction by Staking Contract.

stakingAddress: 0xea224dBB52F57752044c0C86aD50930091F561B9
pubkey: 0x8497312cd37eef3a7a50017cfbebcb00a9bc400c5881ffb1011cba1c3f29e5d005a980880b7b919b558b95565bc1e628
validatorAddress: 0xA47171b1be26C75732766Ea3433a90A724b3590d
amount: 500000000000
signature: 0xb1dae1164d931c46178785246203eb1c4496b403a7c417bfb33bdfd3c26b552bdbec8e466ed6712ade0b99cc9b0ee8b004cc766687565ba5b0929a1382997a6cc548cf5e390b69f849933c7ac017fbddc612cb3de285fdf89e6fe32e0ccbfc43
```

### Step 2: Validate the Signature

Before submitting the validator initialization transaction, validate the signature:

```bash