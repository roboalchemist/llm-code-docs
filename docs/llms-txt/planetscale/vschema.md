# Source: https://planetscale.com/docs/vitess/sharding/vschema.md

# VSchema

> PlanetScale databases are powered by Vitess.

## VSchema overview

Each Vitess cluster can have one or more [keyspaces](https://vitess.io/docs/concepts/keyspace/).
For unsharded databases, there is a 1:1 relationship between a keyspace and a database within MySQL.
For sharded databases, a single keyspace can map to multiple MySQL databases under the hood.

Each keyspace in your PlanetScale database has an associated [VSchema](https://vitess.io/docs/api/reference/features/vschema/).
The VSchema contains information about how the keyspace is sharded, sequence tables, and other Vitess schema information.

## Viewing VSchema

In order to view your VSchema, first go to the "Branches" tab in the PlanetScale app.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=05fdd7b66a6b41b6a08808293f087986" alt="PlanetScale app tab bar" data-og-width="3660" width="3660" data-og-height="678" height="678" data-path="docs/images/assets/docs/enterprise/tabs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=cf847ba05c261a718af590c87460c6b4 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=98cc0feee3b9611e2008a3b4f1b8528a 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1f5ac50bd86a6f3585b03c46ee974b88 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7063a2616744fde48d52fc75a411379a 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=bfe9f01d0912069a7ab3a33f5882435d 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tabs.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1b060ca9ab747db94b4f7ca6dc58673f 2500w" />
</Frame>

Click on the branch you would like to view the VSchema for.
Then, select the keyspace and expand out the "Configuration Files" drop-down.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9f5f37b5d3a1e021639ce95d428df246" alt="PlanetScale keyspace selection and configuration files drop down" data-og-width="3734" width="3734" data-og-height="1844" height="1844" data-path="docs/images/assets/docs/enterprise/keyspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6c1af78af9c842c81974c4ac1c0fc05e 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=32adee6fab4901584c60a8f8ad296241 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0f2bfb59897cc01d804149af86121e8d 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3c9b0efc073487d0fbee40edee2afbe9 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c323d1a04f276caccddbbab4292ad59c 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/keyspace.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9997ac30601fd8f0bf572cc7eb24f074 2500w" />
</Frame>

From here, you can inspect your VSchema configuration JSON file.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=dc4aa182fcf0fad12298ecbf5b300186" alt="VSchema JSON view" data-og-width="2358" width="2358" data-og-height="1926" height="1926" data-path="docs/images/assets/docs/enterprise/vschema.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=e8d7e3f995e9f4d25965764a863d0362 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=7a31e13e76332c8e4cb971be062bdce2 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=a9000cfdf8e34804ffa194c04b2c4cc6 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1374c6eee8f94b9a6651eca0c6f4f67e 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=0b55c34ce42efb1dbf25186029b6d46d 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/vschema.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=ef1a5483966ed4faab7b993cf6c2ff34 2500w" />
</Frame>

## Modifying VSchema

You must have a sharded keyspace in order to make VSchema changes.

If you have a database with at least one sharded keyspace, you can modify its VSchema either in the [Clusters](/docs/vitess/cluster-configuration) tab in the dashboard, from the [pscale CLI](/docs/cli/keyspace), or using `ALTER VSCHEMA ...` commands.

### Using the Clusters page

We do not recommend modifying the VSchema directly on your production branch. In fact, it is not possible to do if you have [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled (as recommended). Instead, to modify the VSchema, you should first [create a new development branch](/docs/vitess/schema-changes/branching). Once you have your branch ready, follow these steps:

<Steps>
  <Step>
    To update on the Clusters page, select your new development branch from the dropdown at the top, and then select the
    keyspace below that has the VSchema you'd like to modify.
  </Step>

  <Step>Next, click the tab labeled "VSchema".</Step>

  <Step>
    Modify the VSchema configuration JSON file as needed. Refer to the [VSchema
    documentation](/docs/vitess/sharding/vschema) for more information about the available options.
  </Step>

  <Step>
    When finished, click "Save changes". We will validate your VSchema, and if it is valid, the changes will be saved.
    If there are errors, we will warn you here to change them before saving.
  </Step>

  <Step>
    Go back to your "Branches" tab and click on the development branch that you modified. You should see a note on the
    right that says "Updated VSchema configuration" which lets you know the VSchema(s) for this branch has been
    modified.
  </Step>

  <Step>
    From here, go through the normal [deploy request process](/docs/vitess/schema-changes/deploy-requests) to deploy
    this change to production.
  </Step>
</Steps>

Once your change is deployed to production, you can come back to the Clusters page, switch to your production branch, and view the updates to your VSchema. You can also click the "Changes" tab to see information, such as the resize event, status, and start/end time for any previous changes to the VSchema.

### Using `ALTER VSchema`

PlanetScale recommends making all such modifications in a development branch.
When ready, you can make a deploy request to get the changes into production.
Consider the following database with two keyspaces.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1f749d13c6772db5be0938b808d19ad6" alt="Sharded keyspace" data-og-width="3648" width="3648" data-og-height="2060" height="2060" data-path="docs/images/assets/docs/enterprise/sharded-keyspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=32b3289924e54ee98b412b6aa3fd7f5b 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=250b42fe84f59c901ec9b12a70e74053 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=394828d9c2a9a40cd1fbe5a440ae57f4 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=fdfbfd0d5d0ed50161a2d18b134a75ff 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=4d0d870bddbd5a0c2b4fdd73570a60d4 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sharded-keyspace.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=434c98012eb0664937167881aa4578d9 2500w" />
</Frame>

`sharded` is a sharded keyspace with two shards and `tweeter` is unsharded.
Also note that safe migrations are enabled.
In order to make a VSchema change for the production branch in this configuration, we first must create a new branch.
We'll call it `add-tweets`

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2e915c3aeb14e8f103969926942a6d1c" alt="New branch" data-og-width="5092" width="5092" data-og-height="1613" height="1613" data-path="docs/images/assets/docs/enterprise/new-branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=22e928a3462687b2a9ddba83eb5209dc 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=05cd7d77d98f239bfc61a769f00e2e3a 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ec977a1fcb478aa760438f86ad574f58 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2e519a77dde5c15a23f89c5572801808 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=252d56fcf60a980b9000e7b82d612da8 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/new-branch.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2ac367dfbbb17b14b289219267d2c74a 2500w" />
</Frame>

On this branch you can make your VSchema and schema changes.
In this case, we'll create a new table called `tweets` in the sharded keyspace and also update the VSchema.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=c156d09dd87eb488cd6f8c4c3a1b96d8" alt="Create the tweets table" data-og-width="5102" width="5102" data-og-height="2654" height="2654" data-path="docs/images/assets/docs/enterprise/tweets-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=280&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=b67dcbb3c8a746426e6424b270fe518c 280w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=560&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=84295a41f91fa556c01e161ca1388b09 560w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=840&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=421a6fd180d0708fe69b11d129a2ca6a 840w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=1100&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=f250fe6640308969c79aaa6f67b1711e 1100w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=1650&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=d4ef01741c364f02747ae69f0de78601 1650w, https://mintcdn.com/planetscale-cad1a68a/Iq7wyPq-ODOtm89r/docs/images/assets/docs/enterprise/tweets-table.png?w=2500&fit=max&auto=format&n=Iq7wyPq-ODOtm89r&q=85&s=1aba21a61ae5a9f4273eedac1eaf332b 2500w" />
</Frame>

We will also create a sequence table in the unsharded keyspace, and update the VSchema accordingly:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bcde96b109fc62b9faa8981715821ac3" alt="Create the sequence table" data-og-width="5100" width="5100" data-og-height="2650" height="2650" data-path="docs/images/assets/docs/enterprise/sequence-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=284cbebd84a952c0e022330534625638 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a66cf7798c1ae22f5506cf3f7ec6c845 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a569476cf7c2dd86b2d7f8bd78d733b0 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=187cedff80264c995b70387b7a885925 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bac014c4d9fcf3b532d955385aa427f0 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/sequence-table.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=68893c162351632d9a0ea9b0926ebe56 2500w" />
</Frame>

We have now made updates both to our Vitess VSchema and MySQL schema.
To get these changes into production, navigate to the "Branches" page and select the `add-tweets` branch.
Here, you will be presented with a diff of both the VSchema and schema changes:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=157793f483cdc6bd563c50849c94eb4a" alt="Schema diff" data-og-width="1850" width="1850" data-og-height="2432" height="2432" data-path="docs/images/assets/docs/enterprise/schema-diff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3f78be609b263b4c65d3d08b170ff534 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bdd14416d4fedbd014b611c59e51a371 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2b9107b483159059aaf90e6aa7ff3f9c 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=dcbe388ccac476c5c8aa01e3657c57ff 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2fcc7cce1503427287a7d2ba8860c542 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/schema-diff.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ada16d70fb4c028403b937b531e82ae8 2500w" />
</Frame>

Click "Create deploy request."
The deploy request should indicate that it is going to apply both VSchema and Schema changes:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1a177bd74147e4f51c1551e5aa8c8489" alt="Deploy request" data-og-width="2890" width="2890" data-og-height="1162" height="1162" data-path="docs/images/assets/docs/enterprise/deploy-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=fe2b6570f90d387512bc3f9867a6b9d9 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=df9d994f1a1c984b31ccf807711284a5 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3adf240b436db7daad56b5306202ed88 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=864ae5a6ceb2267dfede973a8f212d9d 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7404c3a8d0688ad8de974b5a72d8a5e8 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/enterprise/deploy-request.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=533c1e92271d67c79e554b9fd219534f 2500w" />
</Frame>

Click "Deploy changes."
Once complete, the Vschema and schema changes will be applied to your production branch.

<Warning>
  You can only use `ALTER VSCHEMA ...` commands in branches that have at least one sharded keyspace.
  If you do not, you will get an error message when attempting to execute `ALTER VSCHEMA ...`.
</Warning>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt