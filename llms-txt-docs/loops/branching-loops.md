# Source: https://loops.so/docs/loop-builder/branching-loops.md

# Branching Loops

> Branching loops allow you to send different emails based on a contact's properties within a single Loop.

A common use case for crafting a user journey is to send different emails based on whether a contact has completed an action or not.

For example, you may want to send a different email to free users versus paid users.

You can do this by adding a **Branch** node to your loop.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=91036180f9de862a99a393e431a80960" alt="Branches in a loop" data-og-width="1707" width="1707" data-og-height="1138" height="1138" data-path="images/loop-builder-branching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6b2657a8b28a98eaee91918efca8bca2 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=de5dd848d22f71843b1a58e6e637eb4d 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1539737f6d97ea6f1cac423d7a722c7b 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a216c8a0428be8e01e35dfbe96a2b126 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=936f5a0d8e08ca46eee492c4dd93cb73 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=80825241a83c5021d9b0005179f1b676 2500w" />

<Info>
  It's not currently possible to converge branches back into a single branch.
</Info>

## Creating a branching loop

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8eee5f157d53df682fbcf412e51b0aad" alt="Adding a node to a branch" data-og-width="1545" width="1545" data-og-height="1030" height="1030" data-path="images/loop-builder-branching-add-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=97abc41aa0c6a0c2e6b2573c8659de58 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9fd3d484c1bd630e9be8abdaafd671f6 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e0bc79616e79d75f9aadfa8a589f6b07 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=e620789b8c749c4fe92dfcace1f0ffd8 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=13cf4227b40f07ae4fc84d78270274b8 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-builder-branching-add-node.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9ffd2c9c119fce854ca799e09e01bc75 2500w" />

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

## Deleting branches

To delete all branches, select the head Branch node and click the trash icon. This will remove all branches—including all nodes—following it.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ae85ffed07e6a30feaaa52f8dd421da4" alt="Delete branch node" data-og-width="2280" width="2280" data-og-height="1452" height="1452" data-path="images/delete-branches.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b39555e6e1d47bc99aecab3462b207ed 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=90226a1ef6ce164fc79fe1e4b0628966 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=6bce2adea5fdc06a398f8393e93b7814 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b4a28f61027eab659a1c944451f2ac0d 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=edbff485001af110a1adc401776c05de 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-branches.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=88ea86aea59cae257a87cdb146de8494 2500w" />

If you want to delete a single branch, you can do so by deleting each node in the branch you want removed. When the final node is deleted, the branch will be removed.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=8324e52faaec0e6e39e6126bc1a2b7fa" alt="Delete single branch" data-og-width="2280" width="2280" data-og-height="1572" height="1572" data-path="images/delete-single-branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=784a1d1054450b81af5b8b5ecb1ca7a5 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=8228fdcaf60355065f9e7c1427f52e2f 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a86ba604c28d9ff0b11c831e33c50460 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=eea03f2bc94cdbd309403843bc9d56c4 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=097cb8f52e2842f6e7a037d31108b11d 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/delete-single-branch.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=2b364630f6ea633e9b5d215b6975d1f1 2500w" />
