# Source: https://docs.statsig.com/feature-flags/permanent-and-stale-gates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Permanent and Stale Gates

> Learn how to manage feature gates lifecycle with Types to track flags ready for cleanup or permanent integration

It is important for your codebase and team to bring feature gates to a final state (i.e. flags now permanently part of your codebase or completely removed) when they have served their purpose, as described [here](/feature-flags/feature-flags-lifecycle). On Statsig, you can use feature gate **Types** to easily keep track of your flags that might be ready to brought to their final state.

## Types

In your feature gates catalog, you'll see different **Types** displayed in the Status column, as well as under the filter option -

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/permanent-and-stale-gates/224765362-9b9686f2-62b0-4605-8b8c-911987d343e0.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=a93f17ae1cfc5cfab1c8b2e840ca08c3" alt="Feature gates catalog with status types filter" width="2476" height="1202" data-path="images/feature-flags/permanent-and-stale-gates/224765362-9b9686f2-62b0-4605-8b8c-911987d343e0.png" />
</Frame>

* **Permanent Gates** (set by you)
  * **Permanent feature gates** are expected to live in your codebase for an extended period of time, beyond a feature release, usually for operations or infrastructure control. Common examples include user permissions (e.g. premium features based on subscription level) or circuit breakers/kill switches (e.g. terminating a connection to prevent negative customer impact) or even supporting legacy features in old app versions.
    * There are two ways to mark a gate as **Permanent**:
      * When creating the gate: the **Permanent** box in the gate creation flow
        <Frame>
          <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/permanent-and-stale-gates/224768058-1a1b74a2-6b5d-4bfd-b73c-e2fc1f4a7a7f.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=bcb5ce7e2b0a3c229b7c20e6192f87b2" alt="Permanent checkbox in gate creation flow" width="2504" height="1292" data-path="images/feature-flags/permanent-and-stale-gates/224768058-1a1b74a2-6b5d-4bfd-b73c-e2fc1f4a7a7f.png" />
        </Frame>
      * After a gate has been created: click on the "..." menu and then "Mark Gate Permanent"
        <Frame>
          <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/permanent-and-stale-gates/224763304-2002e482-8ef0-4025-b13c-acb92ffb2bcc.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=4cc38136016a8570637bf67ddc690f27" alt="Mark Gate Permanent menu option" width="2564" height="1244" data-path="images/feature-flags/permanent-and-stale-gates/224763304-2002e482-8ef0-4025-b13c-acb92ffb2bcc.png" />
        </Frame>
  * Implications of marking a gate as **Permanent**
    * No change in the gate's behavior when called
    * Easy filtering on feature gates catalog
    * More caution in its management: while you are able to archive or delete a **permanent** feature gate, there will be a warning shown before proceeding
    * Statsig will forgo reminding you to clean up these gates and may display them differently in the console
  * You will be able to change the gate back to **Temporary** at any point.
    * All newly created feature gates are marked as **Temporary**, unless marked otherwise (i.e. Permanent). Therefore, Statsig will not display the phrase **Temporary** in the feature gates Catalog or within the individual gates page.
* **Stale Gates** (set by Statsig)
  * **Stale feature gates** indicate to your team that these gates could be a good candidate for cleanup. Statsig automatically marks gates as stale based on the following definition (excludes Permanent and archived gates)
    * Gates created less than 30 days ago, modified in the last 30 days, or referenced by other gates/experiments/dynamic configs are never consider stale
    * Otherwise, any of the following conditions make a gate stale:
      * The gate has had 0 checks within last 30 days
      * The gate is still being checked but its earliest check was at least 30 days ago
  * Implications of gates being marked as **Stale**
    * No change in the gate's behavior when called
    * Easy filtering on Feature Gates catalog
    * Will include the gate in Statsig's nudges for cleanup (more below)
  * **Stale Reasons** are the reason why a gate has been set as stale. This information can be queried on the [Console API](/console-api/gates).
    * **None** No Stale Gates should have their reason set as None, this is exclusively for **Temporary** or **Permanent** gates.
    * **STALE\_PROBABLY\_DEAD\_CHECK** There have been no checks in the last 30 days.
    * **STALE\_PROBABLY\_LAUNCHED** The Gate is marked as launched or has an everyone rule passing 100% (rollout rate of 100%).
    * **STALE\_PROBABLY\_UNLAUNCHED** The Gate is marked as disabled or has an everyone rule passing 0% (rollout rate of 0%).
    * **STALE\_PROBABLY\_FORGOTTEN** This gate appears to have been only partially launched for some time. You might want to launch/disable it, or make it permanent if you need to keep it around.
    * **STALE\_NO\_RULES** The Gate has no set rules.
    * **STALE\_ALL\_TRUE** The Gate has been returning true every time it has been checked for the last 30 days (or number of days configured in project settings). It could probably be removed.
    * **STALE\_ALL\_FALSE** The Gate has been returning false every time it has been checked for the last 30 days (or number of days configured in project settings). It could probably be removed.
    * **STALE\_EMPTY\_CHECKS** The Gate has been returning empty (probably indicating an error) every time it has been checked for the last 30 days (or number of days configured in project settings). It could probably be removed or might need to be investigated.

## Nudges to clean up Stale gates

Using the **Stale** type discussed above, Statsig provides both in-console and external nudges to remind you to cleanup (or make Permanent) your feature gates.

* **In-console:** See the reminder at the top of the individual feature gate page
  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/LlhWAKAM8RRcyVab/images/feature-flags/permanent-and-stale-gates/224457644-16844256-e7f8-4490-b07e-74f0d85eb6ee.png?fit=max&auto=format&n=LlhWAKAM8RRcyVab&q=85&s=610d555dc9c8fa6124258d7dd190a8cc" alt="Stale gate cleanup reminder notification" width="2502" height="826" data-path="images/feature-flags/permanent-and-stale-gates/224457644-16844256-e7f8-4490-b07e-74f0d85eb6ee.png" />
  </Frame>
* **Email/Slack:** We will proactively reach out to you with an email/ Slack reminder (if you've enabled the Slack integration) to clean up or mark permanent any stale gates you own. We will send this reminder nudge monthly until the gates are either cleaned up or marked as permanent.


Built with [Mintlify](https://mintlify.com).