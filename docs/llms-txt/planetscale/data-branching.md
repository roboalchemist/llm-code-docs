# Source: https://planetscale.com/docs/vitess/schema-changes/data-branching.md

# Data branching®

export const VimeoEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://player.vimeo.com/video/${id}?dnt=true`} title={title} className="aspect-video w-full" allow="autoplay; fullscreen; picture-in-picture" />
    </Frame>;
};

## Overview

The PlanetScale Data Branching® feature allows you to create isolated copies of your database that include both the schema and data. This differs from our [regular branching feature](/docs/vitess/schema-changes/branching), which only includes the schema.

## Enable the Data Branching® feature for your database.

Before you can use the feature, you have to enable it in your database settings page.

<Steps>
  <Step>Navigate to the database that you'd like to enable.</Step>
  <Step>Click on the "**Settings**" link in the header navigation bar.</Step>
  <Step>Scroll to the option with the text "**Enable Data Branching®**"</Step>
  <Step>Enable this option and click "**Save database settings**".</Step>
</Steps>

## Create a new seeded branch

<Steps>
  <Step>After enabling the Data Branching feature, navigate to the dashboard page of the database.</Step>

  <Step>
    Clicking on "**New Branch**" should now offer an option to select "**Seed Data**". - **None** — Creates a database
    branch with only the **schema** copied to the new branch. - **From most recent backup** — Creates a database branch
    with both the **schema and data** from the latest backup of the Base branch.

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=bc2b83230c10dcd3abe260686370a5b1" alt="PlanetScale dashboard new branch dialog with seed option" data-og-width="991" width="991" data-og-height="955" height="955" data-path="docs/images/assets/docs/concepts/data-branching/branch.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=280&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=e9997bb3c6264f20988b93520922d85b 280w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=560&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=de94e1aaed988368df028e8fb8cd8cc7 560w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=840&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=b1cc602424ce92731e90f04fa420beeb 840w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=1100&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=312068484874c1290b7956c0e8cd9999 1100w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=1650&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=8da17a5c22e21b8a0f4a75d3bfc96f1f 1650w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/data-branching/branch.jpg?w=2500&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=069b39673fecb57597d86aec0f021f74 2500w" />
    </Frame>
  </Step>
</Steps>

<Warning>
  Branching off of a production branch and seeding it with data can incur additional charges, as branches seeded from production are treated as production branches instead of development branches. See [question 5](/docs/vitess/schema-changes/#faq) in the FAQ below for more information.
</Warning>

3. Once you've selected an option, click "**Create branch**" to create a new branch.

   <VimeoEmbed id="830572488" title="Data Branching" />

### FAQ

<AccordionGroup>
  <Accordion title="Can I pick which backup is used for the new branch?">
    PlanetScale picks the latest backup so that your new branch has the latest dataset to work with.
  </Accordion>

  <Accordion title="Can I pick which tables are copied into the new branch?">
    PlanetScale seeds the new branch with **all the schema & data** from the base branch. We do not offer a way to filter out data or schema when creating a new branch.
  </Accordion>

  <Accordion title="Is data in the new branch kept up to date with changes to the base branch?">
    PlanetScale does not provide data syncing between a production branch and a development branch.
  </Accordion>

  <Accordion title="When I merge my deploy request, will any data changes be merged back to the base branch?">
    PlanetScale does not provide data syncing between a production branch and a development branch.
  </Accordion>

  <Accordion title="Will enabling the Data Branching® feature affect my billing?">
    Yes, it can. If you are branching and seeding from a *development* branch, the new branch will count towards your [development branch usage hours](/docs/planetscale-plans#development-branches) in the same way that regular branching does, but because you're seeding it with data, it will also be billed for storage.

    However, if you branch and seed from a *production* branch, the new branch will be created as a production branch at the same resource size as the source production branch, and will therefore be billed at that size. It will also be seeded with the production data and include the 2 default production replicas, so you will be charged for the storage as well for however long the branch stays running.

    For example, if you are branching off a `PS-80` production branch with 100 GB of storage, and you seed the new branch with that source production branch's data, you will be billed for the new seeded branch as follows:

    * `PS-80` — \$179
    * 100 GB — ($0.50 \* 100 GB) \* 3 replicas = $135

    We spin the new branch up using the same resource size as the production branch to ensure that large datasets initialize correctly and efficiently. After initialization, you may downgrade the branch size on the [Clusters page](/docs/vitess/cluster-configuration#adjust-your-cluster-size). All billing is prorated, so you will only be charged for the time your seeded branch is live. To avoid incurring extra charges, be sure to downsize your seeded branch, and delete it once you're done using it
  </Accordion>
</AccordionGroup>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt