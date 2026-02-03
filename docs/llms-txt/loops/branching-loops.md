# Source: https://loops.so/docs/loop-builder/branching-loops.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Branching Loops

> Branching loops allow you to send different emails based on a contact's properties within a single Loop.

A common use case for crafting a user journey is to send different emails based on whether a contact has completed an action or not.

For example, you may want to send a different email to free users versus paid users.

You can do this by adding a **Branch** node to your loop.

<img src="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=f28b3a021d8215d32331cb9e6fd35066" alt="Branches in a loop" data-og-width="2280" width="2280" data-og-height="1479" height="1479" data-path="images/loop-builder-branching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=280&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=ff9789af355e784e7c69aa548dea8bac 280w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=560&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=376818c45ff13412f6af850d670a9af8 560w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=840&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=f9f8543329ad6424e702a0ce860fd31d 840w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=1100&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=47edac897c29edb4f90005d0420f590f 1100w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=1650&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=a53133c2587d35c445348aea4c7d5d60 1650w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=2500&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=d748e070abf937973fd04e041639a819 2500w" />

## Creating a branching loop

<img src="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=1dc0d68fb37d51d32124bf5372321a8e" alt="Adding a node to a branch" data-og-width="2280" width="2280" data-og-height="1653" height="1653" data-path="images/loop-builder-branching-add-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=280&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=5ddd66f67399d79d6410eac3991b31b4 280w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=560&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=05033a0f839beccf5535806b25608528 560w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=840&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=339fa307995a11c68f4d6c35c64624cf 840w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=1100&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=a7b345844e65280a88e030b424366b36 1100w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=1650&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=4a31095c56c0bce9afd0a50f8b161210 1650w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching-add-node.png?w=2500&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=1531eaed44e049dfe6a172c7874a1f5c 2500w" />

To create a branching loop, click the `+` icon where you want branching to be added and select the **Branch** node type.

Two audience filter nodes are automatically created for you. Edit the audience filter settings for each to send different contacts down each branch, based on their properties.

You can add as many branches as you like to your loop. Add more branches by clicking the `+ Branch` option that appears on hover just below the Branch node.

Each branch can contain emails, timers, audience filters, more branches, and experiments.

<CardGroup columns="2">
  <Card title="Node types" icon="input-text" href="/loop-builder#nodes">
    Learn about the different node types.
  </Card>

  <Card title="Experiments" icon="vial" href="/loop-builder/experiments">
    Add A/B testing to your loops.
  </Card>
</CardGroup>

## Audience filters

Every branch is defined by an audience filter, which is always the first node in a branch. Filters determine which contacts follow each branch.

When a contact reaches a branch node, the audience filter nodes are evaluated left-to-right as defined in the loop builder. The contact will proceed to the first matching filter and the remaining filters are skipped. If the contact matches none of the filters, they exit the loop.

You can create the equivalent of a "default path" by making the right-most filter have empty conditions so that it matches any contact.

<Note>
  #### Upgrade notice

  Previously, a branch node would send contacts who matched multiple filters down multiple parallel branches.

  This behavior has been changed; now, in any new branches added to loops, contacts will only follow the first branch they match.

  Branches with the old behavior are marked in your loops. They will retain the old logic until you explicitly press the "Upgrade Branch Node" button shown in the Branch head node's options panel. For more information, see the [branch node upgrade documentation](/loop-builder/branch-node-upgrade).
</Note>

The audience filter nodes created after a branching node can be toggled between two settings:

* **All following nodes:** The audience filter will apply to *all nodes* downstream of the filter. If a contact stops matching the filter later down the branch, they will be removed from the loop.
* **Next node only:** The audience filter will only apply when contacts reach the next node in the branch. If a contact stops matching the filter later in the branch, they will remain in the loop.

<CardGroup columns="2">
  <Card title="Audience filters" icon="filter" href="/loop-builder#audience-filters">
    Read more about audience filters.
  </Card>
</CardGroup>

## Converging branches

A common use case is to have different branches converge back to the same path. For example, you may want to create branches with different filters that lead to different onboarding emails, but have all branches converge on a single timer that waits a week before sending the same follow-up email.

Here's how you can set up converging paths in Loops:

<Steps>
  <Step title="Reroute a connection">
    Click **Reroute connection** located below a node.
    <img src="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=f0268eced39b8d0ac2f3c6c458fd3427" alt="Click reroute button" data-og-width="2280" width="2280" data-og-height="1572" height="1572" data-path="images/reroute-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=280&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=8e50ac755033ead1d4ff8e79f6e4dfc5 280w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=560&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=ec751ba37f195fdfaa92725231578c84 560w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=840&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=e0a736e613907665adf9a21828ac4013 840w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=1100&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=25a35805cf45d2d49173a5ae8c1221d4 1100w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=1650&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=014f0d184057f3e03a8206d40e712246 1650w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-button.png?w=2500&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=b4f9235d7b78cd2daf9b629d90c0ed4b 2500w" />
  </Step>

  <Step title="Click on a target node">
    Now select the target node you want to reroute to.

    Since loops do not allow circular paths, only valid target nodes will be visible, and any invalid target nodes will be dimmed.
    <img src="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=45bd16039ec49a4f00530fea547b004e" alt="Click target node" data-og-width="2280" width="2280" data-og-height="1412" height="1412" data-path="images/reroute-select-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=280&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=b71b806beab2a217ca0825e89b841c82 280w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=560&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=e843dc481602c8e324977beb9b0884a0 560w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=840&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=303a5ccb7491530e1e52d3b274351fc1 840w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=1100&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=1274a125e3aadd5c8f0ded61b36128f7 1100w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=1650&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=ef33f815c92cd1ee29427917fb86f394 1650w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-select-node.png?w=2500&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=d42014ead75a5f239a409b914bea2b71 2500w" />
  </Step>

  <Step title="End result">
    You'll end up with multiple nodes converging on the same target.
    <img src="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=2a09ec7139c947e116e8949b75d56ede" alt="Rerouting done" data-og-width="2280" width="2280" data-og-height="1479" height="1479" data-path="images/reroute-done.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=280&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=08fc613189efde54d80895a9c11d8b0d 280w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=560&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=84ed432090b4a486661e2e68e15601c7 560w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=840&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=817c876bbd878dd11f680e16f63fcfb8 840w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=1100&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=9e54879233ff8ad5860ca7426acc0cc8 1100w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=1650&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=672ba3f96ef59056b2b8b973d5962dc5 1650w, https://mintcdn.com/loops/EzJp4LEUiY1GGCG6/images/reroute-done.png?w=2500&fit=max&auto=format&n=EzJp4LEUiY1GGCG6&q=85&s=cb3b554a1c2eb64d71125446c17ac6e6 2500w" />
  </Step>
</Steps>

## Deleting branches

To delete all branches, select the head Branch node and click the trash icon. This will remove all branches—including all nodes—following it.

<img src="https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=a86fe66e99b6f94658800837c0661d0a" alt="Delete branch node" data-og-width="2280" width="2280" data-og-height="1452" height="1452" data-path="images/delete-branches.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=280&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=27cb74abe2500107b1c68140d99a2252 280w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=560&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=e3f8e417d37ef3de84451180bdca62c2 560w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=840&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=2240d7d37777d85e2fedaad546ade11c 840w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=1100&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=3f00f8d858c22be9fba63359275dc26a 1100w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=1650&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=aef8d5c30a48d760570b2a15a4a4bc7c 1650w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-branches.png?w=2500&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=cb868f956e700e2e5bb087ee7e70b157 2500w" />

If you want to delete a single branch, you can do so by deleting each node in the branch you want removed. When the final node is deleted, the branch will be removed.

<img src="https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=52d31f3a851e2cb0b9edc290aee713b8" alt="Delete single branch" data-og-width="2280" width="2280" data-og-height="1572" height="1572" data-path="images/delete-single-branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=280&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=53fb2a257873382d2029f1b324212581 280w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=560&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=eef12d4848eec97e2fbe96d64b6dddb6 560w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=840&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=fcc403e477df67086dc06b7ae8b42d7b 840w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=1100&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=2ee7d09ee055045c222d9f80a496b2d7 1100w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=1650&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=979d6e2d8d4dbe8dbabeb0a6f7924bd7 1650w, https://mintcdn.com/loops/TjVq5Pxm6qkzPWKN/images/delete-single-branch.png?w=2500&fit=max&auto=format&n=TjVq5Pxm6qkzPWKN&q=85&s=43c09944e9bd3b41e172fd7b49ff2ed4 2500w" />
