# Source: https://planetscale.com/docs/security/teams.md

# Teams

> PlanetScale allows you to create teams within organizations.

## Overview

This allows you to easily manage administrator access to one or multiple databases all in one spot.

## Create and manage Teams

You can manage teams straight from your PlanetScale dashboard by going to "**Settings**" > "**Teams**".

<Note>
  Only [Organization Administrators](/docs/security/access-control#organization-administrator) can create and
  manage Teams.
</Note>

Once you add databases to a team, any members on that team will have [Database Administrator access](/docs/security/access-control#database-level-permissions) to those databases. Review our [Access control documentation](/docs/security/access-control) to understand the full scope of Database Administrator access.

### Create a team

<Steps>
  <Step>
    On your PlanetScale overview page, click "**Settings**".
  </Step>

  <Step>
    Click "**Teams**" in the left nav.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5a76414f2aaa68cf4715cd5bfde59d88" alt="Dashboard UI - Create a PlanetScale team" data-og-width="1800" width="1800" data-og-height="1236" height="1236" data-path="docs/images/assets/docs/concepts/teams/create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=03f51e5dadd8b2fd8985435950a6ce2f 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5189e60c0b7b56c72b21ad36e5f545f8 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6120f683423e37f6188ddfc06d394a9c 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9eb11a5459d6b649d8a22e8f7a7f4c4a 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f5b8589a78376edba51ce13d45d40862 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/create.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5c6a49210763325fcc966ff81eddee27 2500w" />
    </Frame>
  </Step>

  <Step>
    Give your team a name and description (*optional*).
  </Step>

  <Step>
    Click "**Create team**".
  </Step>
</Steps>

### Add members

<Steps>
  <Step>
    Click "**Add a member**".
  </Step>

  <Step>
    You'll see a list of your Organization members. Select the member(s) one at a time that you wish to add to the team.
  </Step>
</Steps>

### Add databases

<Steps>
  <Step>
    Click "**Add databases**".
  </Step>

  <Step>
    Select the databases you want this team to have [database administrator access](/docs/security/access-control#database-level-permissions) to.
  </Step>
</Steps>

Now, when you go to the Settings page for any databases you've added to a team, you'll also be able to view and revoke access straight from the database Administrators page.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=386d47dd32e1e710e3c97a098c9f8de1" alt="Dashboard UI - Database Administrators settings page" data-og-width="1800" width="1800" data-og-height="825" height="825" data-path="docs/images/assets/docs/concepts/teams/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3dd1aad781d127fd05018f9426d69b21 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9957c4bbab41541e5fe2dffb34d78332 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=dfa30d507dcf4f53b46879659a007cc3 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=614c92326df3e30cb8b25d6b00e1b947 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=8b3f836736aa319dc7e538deb8b22801 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/settings.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=846fc8debf5472cb9cfa27fbdd6175b3 2500w" />
</Frame>

### Remove members and databases

To remove a member from a team, find their name in the member list and click "**Remove**". At this time, you'll also be able to delete any passwords this member has created to ensure you've completely revoked their access to the database.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d9546a59b294ee6c754aad0deefc33f6" alt="Dashboard UI - Delete a member from a team" data-og-width="1800" width="1800" data-og-height="1146" height="1146" data-path="docs/images/assets/docs/concepts/teams/member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=cda2a415580d69bed26e018e42f253aa 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c9ca89ca00ee4b54fd98e600a99acd0a 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=142f1c81ec6b89aacd2e969bcfbb99be 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=98b118baaf2c61143f3a44ca21653d62 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3e221d1a81bb1f5ae3fa939a441c3cba 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/member.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2a5fdea6d2df8e493809b411c7557311 2500w" />
</Frame>

To remove a database from a team, click the "**x**" next to the database name under "Administrator permissions". This will remove database administrator access for all members of the team.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c5489e95e5970efb19945c91c8b759c8" alt="Dashboard UI - Delete a database from a team" data-og-width="1800" width="1800" data-og-height="1146" height="1146" data-path="docs/images/assets/docs/concepts/teams/database.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=38a9a0619e6375dc539e2e6480861e8b 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=8d4f326783d6d6371f6830da1e3eb3a4 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=83352e1ec4589a307d6fdd8abfce857d 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3ebb0fa3b48ebad8b749f1ddd6d0a544 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6ff0b8688837a0ca97b7568a57db87ca 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/teams/database.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=64a31a7fdbbdcbc476ae3927302b33e4 2500w" />
</Frame>

## Directory Sync with Teams

If you have [SSO with Directory Sync](/docs/security/sso#directory-sync) enabled, all Teams will be managed by your Directory Sync directory. You can add and remove database access to teams, but member management must be done through your directory.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ea6e8a6fedd17bed9a398d4c4d20e626" alt="Dashboard UI - Directory-managed Teams page" data-og-width="1800" width="1800" data-og-height="1392" height="1392" data-path="docs/images/assets/docs/concepts/sso/managed.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=fdfc6d5163dd5b23a8d6971a86f20e16 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d8ad85a927fcfd4d0d5d14179714a681 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2fa39492d377c6acce22cb0bfaca0543 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=25d11d732a3c830f28c921fc73cf7182 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0a8170a05664fddda91741021d1a4fd1 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/sso/managed.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ec15613c1c96e61e5787255432b6baee 2500w" />
</Frame>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt