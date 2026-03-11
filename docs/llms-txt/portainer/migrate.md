# Source: https://docs.portainer.io/2.33-lts/user/docker/stacks/migrate.md

# Source: https://docs.portainer.io/sts/user/docker/stacks/migrate.md

# Source: https://docs.portainer.io/user/docker/stacks/migrate.md

# Migrate, duplicate or rename a stack

To migrate, duplicate, or rename a stack, open your environment, go to **Stacks**, and select the stack you want to change.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/zXL5F6cBTC6qDi0RqMr4/2.36.0-duplicate-migrate-stacks.gif" alt=""><figcaption></figcaption></figure>

## Migrating a stack

In the **Stack duplication / migration** section, select the destination environment for the stack, and optionally define a new name for the stack. Click **Migrate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lQjo4j0KUh5scrYsNsRu/2.36.0-stacks-migrate.png" alt=""><figcaption></figcaption></figure>

Migrating does not relocate the content of any persistent volumes that may be attached to the stack. Acknowledge this warning and confirm the migration by clicking **Migrate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/S9mhqbZ48QcJFrCF12cR/2.15-stack-migrate-confirm.png" alt=""><figcaption></figcaption></figure>

## Duplicating a stack

In the **Stack duplication / migration** section, give the new stack a descriptive name then select the environment the stack should duplicate to. When you're ready, click **Duplicate**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/lQjo4j0KUh5scrYsNsRu/2.36.0-stacks-migrate.png" alt=""><figcaption></figcaption></figure>

## Rename a stack

In the **Stack duplication / migration** section, give the stack a new descriptive name and select the environment that the stack is currently on. When you're ready, click **Rename**.&#x20;

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/3IXtWVrkhJTa21tmttkZ/2.36.0-stacks-rename.png" alt=""><figcaption></figcaption></figure>

Renaming creates a new stack instance and does not transfer the content of any persistent volumes that may be attached to the stack. Acknowledge this warning and confirm the migration by clicking **Rename**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/y3kBag9h8yeQAIt1m0Yk/2.38-Stack-rename.png" alt=""><figcaption></figcaption></figure>
