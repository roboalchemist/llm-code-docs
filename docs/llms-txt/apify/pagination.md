# Source: https://docs.apify.com/api/client/python/docs/concepts/pagination.md

# Pagination

Copy for LLM

Most methods named `list` or `list_something` in the Apify client return a [`ListPage`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md) object. This object provides a consistent interface for working with paginated data and includes the following properties:

* `items` - The main results you're looking for.
* `total` - The total number of items available.
* `offset` - The starting point of the current page.
* `count` - The number of items in the current page.
* `limit` - The maximum number of items per page.

Some methods, such as `list_keys` or `list_head`, paginate differently. Regardless, the primary results are always stored under the items property, and the limit property can be used to control the number of results returned.

The following example demonstrates how to fetch all items from a dataset using pagination:

* Async client
* Sync client

```
from apify_client import ApifyClientAsync

TOKEN = 'MY-APIFY-TOKEN'


async def main() -> None:
    apify_client = ApifyClientAsync(TOKEN)

    # Initialize the dataset client
    dataset_client = apify_client.dataset('dataset-id')

    # Define the pagination parameters
    limit = 1000  # Number of items per page
    offset = 0  # Starting offset
    all_items = []  # List to store all fetched items

    while True:
        # Fetch a page of items
        response = await dataset_client.list_items(limit=limit, offset=offset)
        items = response.items
        total = response.total

        print(f'Fetched {len(items)} items')

        # Add the fetched items to the complete list
        all_items.extend(items)

        # Exit the loop if there are no more items to fetch
        if offset + limit >= total:
            break

        # Increment the offset for the next page
        offset += limit

    print(f'Overall fetched {len(all_items)} items')
```

```
from apify_client import ApifyClient

TOKEN = 'MY-APIFY-TOKEN'


def main() -> None:
    apify_client = ApifyClient(TOKEN)

    # Initialize the dataset client
    dataset_client = apify_client.dataset('dataset-id')

    # Define the pagination parameters
    limit = 1000  # Number of items per page
    offset = 0  # Starting offset
    all_items = []  # List to store all fetched items

    while True:
        # Fetch a page of items
        response = dataset_client.list_items(limit=limit, offset=offset)
        items = response.items
        total = response.total

        print(f'Fetched {len(items)} items')

        # Add the fetched items to the complete list
        all_items.extend(items)

        # Exit the loop if there are no more items to fetch
        if offset + limit >= total:
            break

        # Increment the offset for the next page
        offset += limit

    print(f'Overall fetched {len(all_items)} items')
```

The [`ListPage`](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md) interface offers several key benefits. Its consistent structure ensures predictable results for most `list` methods, providing a uniform way to work with paginated data. It also offers flexibility, allowing you to customize the `limit` and `offset` parameters to control data fetching according to your needs. Additionally, it provides scalability, enabling you to efficiently handle large datasets through pagination. This approach ensures efficient data retrieval while keeping memory usage under control, making it ideal for managing and processing large collections.
