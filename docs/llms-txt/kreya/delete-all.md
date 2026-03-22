# Source: https://kreya.app/docs/scripting-and-tests/samples/delete-all.md

# Delete all entities [Pro / Enterprise](/pricing.md)

This sample shows how to delete all items exposed by a REST API using Kreya scripting. You will:

* Create a List Books operation that collects all book IDs into a user variable
* Create a Delete Book operation that deletes a single book by ID using templating
* Run a Kreya script that loops until there are no more items

## Create the list books operation[​](#create-the-list-books-operation "Direct link to Create the list books operation")

Create a REST operation named "List Books" that calls `GET /books`. Add the following operation script to extract IDs from the response and store them in the user variable `bookIds`.

```
kreya.rest.onCallCompleted(ctx => {
  if (!ctx.status.isSuccess || ctx.response.content.length == 0) {
    kreya.variables.delete('bookIds');
    return;
  }

  const bookIds = ctx.response.content.map(x => x.id);
  kreya.variables.set('bookIds', bookIds);
});
```

## Create the delete book operation[​](#create-the-delete-book-operation "Direct link to Create the delete book operation")

Create a REST operation named "Delete Book" that calls `DELETE /books/{{ vars.bookId }}`. Use templating to read the ID from the user variable `bookId`: When the script runs, it will set `vars.bookId` for each item.

## Create and run the script[​](#create-and-run-the-script "Direct link to Create and run the script")

Create a new Kreya script and paste the following code. It does the following:

* List books to populate bookIds
* Iterates `bookIds`, sets `bookId`, and invokes `Delete Book` for each

```
// list all books and store the ids in bookIds variable
// loop through all books, set the bookId for each book and invoke the delete book operation
await kreya.invokeOperation('./Get books');

const ids = kreya.variables.get('bookIds');
for (var i = 0; i < ids.length; i++) {
  kreya.variables.set('bookId', ids[i]);
  await kreya.invokeOperation('./Delete book');
}
```

You can use the user variables view (open via Project > User variables) to see the contents of `bookIds` and `bookId`.

## What’s happening[​](#whats-happening "Direct link to What’s happening")

* The List Books operation script writes all IDs to a user variable (bookIds).
* The invoker script iterates those IDs, sets bookId, and invokes the Delete Book operation once per item.
* The process repeats until List Books no longer finds any IDs, at which point the script exits.

## Related[​](#related "Direct link to Related")

* Scripting overview: [Scripting and tests](/docs/scripting-and-tests.md)
* Invoker scripts API: [Scripts API reference](/docs/scripting-and-tests/invoker-scripts/api-reference.md)
* REST operation scripts: [REST script API reference](/docs/scripting-and-tests/operation-scripts/rest-script-api-reference.md)
* Templating basics: [Templating](/docs/templating.md)
* Example project: [Kreya example project on GitHub](https://github.com/riok/Kreya) (see `example-project/Kreya features/UseCases/DeleteAll`)
