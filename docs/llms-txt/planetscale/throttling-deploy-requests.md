# Source: https://planetscale.com/docs/vitess/schema-changes/throttling-deploy-requests.md

# Throttling deploy requests

## Overview

Deploy requests, though non-blocking, do of course consume some resources as the online schema change process occurs. Normally, you don't need to get involved, as the [Vitess tablet throttler](https://vitess.io/docs/api/reference/features/tablet-throttler/) automatically identifies when replication lag is high on your database and [slows down migration progress](https://vitess.io/docs/user-guides/schema-changes/audit-and-control/#controlling-throttling).

For long-running schema changes that take several minutes or hours, you may wish to increase throttling on your deploy request to mitigate load on your database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=0ad57abb86183b8e3d13a484f83274c3" alt="Deploy request throttling settings page" data-og-width="2080" width="2080" data-og-height="1416" height="1416" data-path="docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=53aa1302878ae46d4d0c69aa45a94fba 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=94d2fb142cf5e8754bdb1ae418f1f521 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=94d09d57af01799b2a164606a64d7874 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=6528d3ce29002c1246dedc83d233aabc 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=26b9344d2d254ee80bb51303953d5981 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/schema-changes/throttling-deploy-requests/deploy-request-throttling.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=5a5093c57ddcd7396c3f7abb78ff65f4 2500w" />
</Frame>

## How it works

The throttle setting allows you to adjust the underlying Vitess tablet throttler for deploy requests. The throttle setting is a value between 0 and 95, where 0 means throttling is effectively disabled, and 95 is nearly fully throttled, which will drastically slow down migrations. 95 is currently the max throttle setting available.

For example, if you set the throttle value to 25, deploy requests will run at about 75% of their normal speed. The lower the number, the less throttling.

## Managing throttler settings

There are three ways to adjust the throttler for deploy requests:

* At the database level
* At the keyspace level
* At the deploy request level

You must be an [Organization Administrator](/docs/security/access-control#organization-administrator) or [Database Administrator](/docs/security/access-control#database-administrator) for the database that you're configuring in order to change these settings at the database level.

However, any organization member who has permission to deploy a deploy request is able to adjust the configuration at the deploy request level.

### Managing throttler settings at the database or keyspace level

For the first two options, first select your database, click "Settings" in the left nav, and scroll down to "Advanced settings". Here, you'll see the options to configure deploy request throttling.

You can adjust the slider or manually type in the value you'd like to set throttling to.

If you'd like to set throttling at the [keyspace](/docs/vitess/sharding/keyspaces) level so that each keyspace is throttled differently, check "Set throttling per keyspace". This will give you the option to individually adjust the sliders for each keyspace.

Click "Save throttling settings". Going forward, these throttler settings will apply to every deploy request as configured.

### Managing throttler settings per deploy request

You also have the option to manually configure throttler settings on each deploy request.

Once you click "Deploy changes" on a deploy request, click the arrow next to "throttling" to show the settings to adjust the throttle value for that deploy request. From here, you'll see the same options to adjust the value for each keyspace or for all keyspaces.

Changes to throttler configuration on the deploy request page will only apply to that individual deploy request and will not affect the database level throttler configurations.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt