# Source: https://docs.baseten.co/development/chain/watch.md

# Watch

> Live-patch deployed code

The [watch command](/reference/cli/chains/chains-cli#watch) (`truss chains watch`) combines
the best of local development and full deployment. `watch` lets you run on an
exact copy of the production hardware and interface but gives you live code
patching that lets you test changes in seconds without creating a new
deployment.

To use `truss chains watch`:

1. Push a chain in development mode (i.e. `publish` and `promote` flags are
   false).
2. Run the watch command `truss chains watch SOURCE`. You can also add the
   `watch` option to the `push` command and combine both to a single step.
3. Each time you edit a file and save the changes, the watcher patches the
   remote deployments. Updating the deployments might take a moment, but is
   generally *much* faster than creating a new deployment.
4. You can call the chain with test data via `cURL` or the playground dialogue
   in the UI and observe the result and logs.
5. Iterate steps 3. and 4. until your chain behaves in the desired way.

### Selective Watch

Some large ML models might have a slow cycle time to reload (e.g. if the
weights are huge). For this case, we provide a "selective" watch option. For
example if your chain has such a heavy model Chainlet and other Chainlets
that contain only business logic, you can iterate on those, while not patching
and reloading the heavy model Chainlet.

<Warning>
  This feature is really useful for advanced use case, but must be used with
  caution.
  If you change the code of a Chainlet not watched, in particular I/O types,
  you get an inconsistent deployment.
</Warning>

Add the Chainlet names you want to watch as a comma separated list:

```shell  theme={"system"}
truss chains watch ... --experimental-chainlet-names=ChainletA,ChainletB
```
