# Source: https://docs.infrahub.app/python-sdk/guides/branches.md

# Branch management

The Python SDK provides multiple methods to manage the branches in an Infrahub instance.

## Get a single branch[​](#get-a-single-branch "Direct link to Get a single branch")

* Async
* Sync

```
from infrahub_sdk import InfrahubClient
client = InfrahubClient()
branch = await client.branch.get(branch_name="main")
```

```
from infrahub_sdk import InfrahubClientSync
client = InfrahubClientSync()
branch = client.branch.get(branch_name="main")
```

## Get all the branches[​](#get-all-the-branches "Direct link to Get all the branches")

* Async
* Sync

```
from asyncio import run as aiorun

from rich import print as rprint

from infrahub_sdk import InfrahubClient


async def main():
    client = InfrahubClient(address="http://localhost:8000")
    branches = await client.branch.all()
    rprint(branches)


if __name__ == "__main__":
    aiorun(main())
```

```
from rich import print as rprint

from infrahub_sdk import InfrahubClientSync


def main():
    client = InfrahubClientSync(address="http://localhost:8000")
    branches = client.branch.all()
    rprint(branches)


if __name__ == "__main__":
    main()
```

## Create a branch[​](#create-a-branch "Direct link to Create a branch")

* Async
* Sync

```
from asyncio import run as aiorun

from infrahub_sdk import InfrahubClient


async def main():
    client = InfrahubClient(address="http://localhost:8000")
    await client.branch.create(branch_name="new-branch", description="description", sync_with_git=False)
    print("New branch created")


if __name__ == "__main__":
    aiorun(main())
```

```
from infrahub_sdk import InfrahubClientSync


def main():
    client = InfrahubClientSync(address="http://localhost:8000")
    client.branch.create(branch_name="new-branch2", description="description", sync_with_git=False)
    print("New branch created")


if __name__ == "__main__":
    main()
```

## Rebase a branch[​](#rebase-a-branch "Direct link to Rebase a branch")

* Async
* Sync

```
from asyncio import run as aiorun

from infrahub_sdk import InfrahubClient


async def main():
    client = InfrahubClient(address="http://localhost:8000")
    await client.branch.rebase(branch_name="new-branch")


if __name__ == "__main__":
    aiorun(main())
```

```
from infrahub_sdk import InfrahubClientSync


def main():
    client = InfrahubClientSync(address="http://localhost:8000")
    client.branch.rebase(branch_name="new-branch")


if __name__ == "__main__":
    main()
```

## Merge a branch[​](#merge-a-branch "Direct link to Merge a branch")

* Async
* Sync

```
from asyncio import run as aiorun

from infrahub_sdk import InfrahubClient


async def main():
    client = InfrahubClient(address="http://localhost:8000")
    await client.branch.merge(branch_name="new-branch")


if __name__ == "__main__":
    aiorun(main())
```

```
from infrahub_sdk import InfrahubClientSync


def main():
    client = InfrahubClientSync(address="http://localhost:8000")
    client.branch.merge(branch_name="new-branch")


if __name__ == "__main__":
    main()
```

## Delete a branch[​](#delete-a-branch "Direct link to Delete a branch")

* Async
* Sync

```
from infrahub_sdk import InfrahubClient
client = InfrahubClient()
await client.branch.delete(branch_name="new-branch")
```

```
from infrahub_sdk import InfrahubClientSync
client = InfrahubClientSync()
client.branch.delete(branch_name="new-branch")
```

## Generating a diff for a branch[​](#generating-a-diff-for-a-branch "Direct link to Generating a diff for a branch")

* Async
* Sync

```
from infrahub_sdk import InfrahubClient
client = await InfrahubClient()
diff = await client.branch.diff_data(branch_name="new-branch")
```

```
from infrahub_sdk import InfrahubClientSync
client = InfrahubClientSync()
diff = client.branch.diff_data(branch_name="new-branch")
```
