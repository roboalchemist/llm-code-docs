# Source: https://docs.upsun.com/environments/change-parent.md

# Change an environment's parent

All environments default to having another environment as their parent.
If you [branched](https://docs.upsun.com/glossary.md#branch) the environment from another,
its parent starts as the environment it was created from.
If you pushed a branch through Git or a [source integration](https://docs.upsun.com../integrations/source.md),
the parent defaults to the default environment.

To change the environment's parent, follow these steps:

Run the following command:

```bash {}
upsun environment:info -e <CHILD_ENVIRONMENT_NAME> parent <PARENT_ENVIRONMENT_NAME>
```

So if you have the environment ``new-feature`` and want to change its parent to ``main``, run the following:

```bash {}
upsun environment:info -e new-feature parent main
```

If you're not using a [source integration](https://docs.upsun.com/integrations/source.md),
you can also set a parent for your environment when pushing changes to it.
To do so, run the following command:

```bash
git push -o "environment.parent=<PARENT_ENVIRONMENT_NAME>"
```

Learn more about how to [trigger actions on `push`](https://docs.upsun.com/environments.md#push-options).

