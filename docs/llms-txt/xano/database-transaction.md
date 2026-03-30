# Source: https://docs.xano.com/the-function-stack/functions/database-requests/database-transaction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Database Transaction

## What are database transactions?

Database transactions allows you to treat a set of functions as a whole. This means that every function must succeed properly in order for all of them to be executed. Usually, you would use this if you have two or more database operations that are mission critical for the end result.

> Let's consider a financial application as an example. During a money transfer, if money is successfully withdrawn from one account but something goes wrong with the deposit to the second account, then you would want the entire transfer to be cancelled. Otherwise, the money would still be withdrawn from the first account even though it was never received by the second account.

<Warning>
  Only **database operations** are considered when determining whether or not to roll back the changes made to the database. This means that for other function types, like conditionals or data transformation, those can still encounter errors without impacting the database transaction.
</Warning>

## Using Database Transactions

<Frame>
  <iframe src="https://demo.arcade.software/SbCUI1OkMs2paTuaucOa?embed" title="https://demo.arcade.software/SbCUI1OkMs2paTuaucOa?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

<Steps>
  <Step title="Add a Database Transaction function to your function stack.">
    There are no additional settings for a database transaction, so just click Save on the panel that opens.
  </Step>

  <Step title="Add steps to the database transaction.">
    You can click and drag to move existing steps into the transaction, or add new functions.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).