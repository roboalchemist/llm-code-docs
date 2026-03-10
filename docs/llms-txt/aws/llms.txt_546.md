# Source: https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/llms.txt

# Amazon Managed Blockchain AMB Query API Reference

> Amazon Managed Blockchain (AMB) Query provides you with convenient access to multi-blockchain network data, which makes it easier for you to extract contextual data related to blockchain activity. You can use AMB Query to read data from public blockchain networks, such as Bitcoin Mainnet and Ethereum Mainnet. You can also get information such as the current and historical balances of addresses, or you can get a list of blockchain transactions for a given time period. Additionally, you can get details of a given transaction, such as transaction events, which you can further analyze or use in business logic for your applications.

- [Welcome](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Operations.html)

- [BatchGetTokenBalance](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalance.html): Gets the token balance for a batch of tokens by using the BatchGetTokenBalance action for every token in the request.
- [GetAssetContract](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetAssetContract.html): Gets the information about a specific contract deployed on the blockchain.
- [GetTokenBalance](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTokenBalance.html): Gets the balance of a specific token, including native tokens, for a given address (wallet or contract) on the blockchain.
- [GetTransaction](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_GetTransaction.html): Gets the details of a transaction.
- [ListAssetContracts](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListAssetContracts.html): Lists all the contracts for a given contract type deployed by an address (either a contract address or a wallet address).
- [ListFilteredTransactionEvents](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListFilteredTransactionEvents.html): Lists all the transaction events for an address on the blockchain.
- [ListTokenBalances](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTokenBalances.html): This action returns the following for a given blockchain network:
- [ListTransactionEvents](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactionEvents.html): Lists all the transaction events for a transaction
- [ListTransactions](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactions.html): Lists all the transaction events for a transaction.


## [Data Types](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Types.html)

- [AddressIdentifierFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_AddressIdentifierFilter.html): This is the container for the unique public address on the blockchain.
- [AssetContract](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_AssetContract.html): This container contains information about an contract.
- [BatchGetTokenBalanceErrorItem](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceErrorItem.html): Error generated from a failed BatchGetTokenBalance request.
- [BatchGetTokenBalanceInputItem](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceInputItem.html): The container for the input for getting a token balance.
- [BatchGetTokenBalanceOutputItem](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BatchGetTokenBalanceOutputItem.html): The container for the properties of a token balance output.
- [BlockchainInstant](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_BlockchainInstant.html): The container for time.
- [ConfirmationStatusFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ConfirmationStatusFilter.html): The container for the ConfirmationStatusFilter that filters for the finality of the results.
- [ContractFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ContractFilter.html): The contract or wallet address by which to filter the request.
- [ContractIdentifier](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ContractIdentifier.html): Container for the blockchain address and network information about a contract.
- [ContractMetadata](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ContractMetadata.html): The metadata of the contract.
- [ListFilteredTransactionEventsSort](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListFilteredTransactionEventsSort.html): Lists all the transaction events for an address on the blockchain.
- [ListTransactionsSort](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ListTransactionsSort.html): The container for determining how the list transaction result will be sorted.
- [OwnerFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_OwnerFilter.html): The container for the owner information to filter by.
- [OwnerIdentifier](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_OwnerIdentifier.html): The container for the owner identifier.
- [TimeFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TimeFilter.html): This container is used to specify a time frame.
- [TokenBalance](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenBalance.html): The balance of the token.
- [TokenFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenFilter.html): The container of the token filter like the contract address on a given blockchain network or a unique token identifier on a given blockchain network.
- [TokenIdentifier](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TokenIdentifier.html): The container for the identifier for the token including the unique token ID and its blockchain network.
- [Transaction](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Transaction.html): There are two possible types of transactions used for this data type:
- [TransactionEvent](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TransactionEvent.html): The container for the properties of a transaction event.
- [TransactionOutputItem](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_TransactionOutputItem.html): The container of the transaction output.
- [ValidationExceptionField](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ValidationExceptionField.html): The resource passed is invalid.
- [VoutFilter](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_VoutFilter.html): This container specifies filtering attributes related to BITCOIN_VOUT event types


## [Service-specific Errors](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_Errors.html)

- [AccessDeniedException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_AccessDeniedException.html): The AWS account doesnât have access to this resource.
- [InternalServerException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_InternalServerException.html): The request processing has failed because of an internal error in the service.
- [ResourceNotFoundException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ResourceNotFoundException.html): The resource was not found.
- [ServiceQuotaExceededException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ServiceQuotaExceededException.html): The service quota has been exceeded for this resource.
- [ThrottlingException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ThrottlingException.html): The request or operation couldn't be performed because a service is throttling requests.
- [ValidationException](https://docs.aws.amazon.com/managed-blockchain/latest/AMBQ-APIReference/API_ValidationException.html): The resource passed is invalid.
