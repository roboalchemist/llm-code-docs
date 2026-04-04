# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/carv-nft-license.md

# CARV NFT License

## CARV NFT License

1. Non-transferable ERC-721 (can be updated with governance).
2. Only syndicate funds can transfer NFT once and redistribute to their community.
3. A maximum of 100,000 tokens can be minted, with token IDs incrementing automatically.
4. Upon redemption, the token ID is permanently destroyed, and any unclaimed veCARV reverts to the foundation.
5. To redeem the NFT License, transfer the NFT to our predefined address. Redemption will be available 6 months after the TGE.

**Function Definitions & Explanations**

```Solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.20;

interface ICarvNft {
    /**
     * @notice This struct represents meta information bound to TokenID,
     *
     * `code`: code of this token entered by buyer
     * `price`: price of this token paid by buyer
     * `tier`: tier of this token
     */
    struct MetaData {
        string code;
        uint64 price;
        uint8 tier;
    }

    /**
     * @notice mint {count} nft to {receiver}.
     * @notice totalSupply 100,000
     *
     * @dev Auth: Only Owner.
     *
     * @param receiver: nft receiver
     * @param count: how many nft to be minted to receiver
     * @param meta: `MetaData` of this tokenID
     */
    function mint(address receiver, uint256 count, MetaData calldata meta) external;

    /**
     * @notice mint {counts} nft to {receivers}.
     * @notice call `mint`
     *
     * @dev Auth: Only Owner.
     *
     * @param receivers: array of receivers
     * @param counts: array of counts
     * @param metas: array of meta
     */
    function mintBatch(address[] calldata receivers, uint256[] calldata counts, MetaData[] calldata metas) external;

    /**
     * @notice Set BaseURI of all the tokens
     *
     * @dev Auth: Only Owner.
     *
     * @param newBaseURI: newBaseURI
     */
    function setBaseURI(string memory newBaseURI) external;

    /**
     * @notice Set TransferProhibitedUntil
     * @notice When the time has not reached the `TransferProhibitedUntil`, ordinary tokens cannot be transferred.
     *
     * @dev Auth: Only Owner.
     *
     * @param newTransferProhibitedUntil: newTransferProhibitedUntil
     */
    function setTransferProhibitedUntil(uint256 newTransferProhibitedUntil) external;

    /**
     * @notice Set RedeemAddress
     * @notice When `transfer.to` is RedeemAddress, the token can be transferred under any circumstances
     *
     * @dev Auth: Only Owner.
     *
     * @param newRedeemAddress: newRedeemAddress
     */
    function setRedeemAddress(address newRedeemAddress) external;

    /**
     * @notice Set TransferOnceWhitelist
     * @notice Addresses in the whitelist can transfer tokens once before `TransferProhibitedUntil`
     *
     * @dev Auth: Only Owner.
     *
     * @param whitelist: whitelist
     */
    function setTransferOnceWhitelist(address[] calldata whitelist) external;
}
```
