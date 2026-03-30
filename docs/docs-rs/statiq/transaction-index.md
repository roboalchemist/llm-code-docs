statiq
# Module transaction 
Source 
## Structs§
TransactionAn active database transaction.
## Functions§
with_retryExecute a closure inside a transaction, retrying on deadlock up to `max_retries`.