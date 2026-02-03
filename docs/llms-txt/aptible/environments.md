# Source: https://www.aptible.com/docs/core-concepts/architecture/environments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Environments

> Learn about grouping resources with environments

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=c262a51b2953bb9da872880ed5966c34" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/2-app-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=cb9a641e157a3d45de78154c9bfe39f3 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=aaf1912d1d2754d461ac880240aaf5a7 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=af812d52b35da2694515cd23588faabc 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=003642c5f4dfe37c28dbc47d3315a01b 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=11232bdf1609b1a73c1ffca30a81efe3 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/2-app-ui.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=851a7ac73ac246b765b686538b9b943d 2500w" />

# Overview

Environments live within [Stacks](/core-concepts/architecture/stacks) and provide logical isolation of resources. Environments on the same Stack share networks and underlying hosts.

[User Permissions](/core-concepts/security-compliance/access-permissions), [Activity Reports](/core-concepts/architecture/operations#activity-reports), and [Database Backup Retention Policies](/core-concepts/managed-databases/managing-databases/database-backups) are also managed on the Environment level.

<Tip> You may want to consider having your production Environments in separate Stacks from staging, testing, and development Environments to ensure network-level isolation. </Tip>

# FAQ

<AccordionGroup>
  <Accordion title="Is there a limit to how many Environments I can have in a given stack?">
    No, there is no limit to the number of Environments you can have.
  </Accordion>

  <Accordion title="How do I create Environments?">
    ### Read more

    <Card title="How to create environments" icon="book-open-reader" iconType="duotone" href="/how-to-guides/platform-guides/create-environment" />
  </Accordion>

  <Accordion title="How do I delete Environments?">
    ### Read more

    <Card title="How to delete environments" icon="book-open-reader" iconType="duotone" href="/how-to-guides/platform-guides/delete-environment" />
  </Accordion>

  <Accordion title="How do I rename Environments?">
    Environments can be renamed from the Aptible Dashboard within the Environment's Settings.
  </Accordion>

  <Accordion title="How do I migrate Environments?">
    ### Read more

    <Card title="How to migrate environments" icon="book-open-reader" iconType="duotone" href="/how-to-guides/platform-guides/migrate-environments" />
  </Accordion>
</AccordionGroup>
