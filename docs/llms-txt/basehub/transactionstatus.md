# transactionStatus

> Gets the current transaction status based on its ID.

## Example

You can explore the full code for this example in [Github](https://github.com/basehub-ai/mutations-api-example/blob/c4d1ccd2609598f707d58204ade29134fd283d8f/lib/mutate-action.ts#L4-L14).

```
export async function getStatus(id: string) {
  const response = await basehub().mutation({
    transactionStatus: {
      __args: {
        id,
      },
    },
  });

  return response.transactionStatus;
}
```