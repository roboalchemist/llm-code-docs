# transactionAsync

> Same as \`transaction\`, but runs async—as a background job.

This method has the same signature as [transaction](https://docs.basehub.com/api-reference/javascript-sdk/basehub-client/mutation/transaction). It’s useful in the case of a long-running job you don’t want to sit around waiting. You can use `transactionStatus` to get the status of the transaction in another Mutation call.

## Example

Check out our Mutation API Playground for full examples.

*   [Playground](https://mutation-api-playground.vercel.app/).
    
*   [Source](https://github.com/basehub-ai/mutations-api-example).
    
*   [Content](https://basehub.com/basehub/mutation-api-playground/explore).