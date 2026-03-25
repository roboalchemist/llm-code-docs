# Source: https://docs.rootly.com/on-call/opsgenie-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Opsgenie Migration

> Migrate users, schedules, teams, services, routing rules, and notification settings from Opsgenie to Rootly On-Call with a Rootly-led, API-based import.

## Overview

Migrating from Opsgenie to Rootly On-Call is a **Rootly-led, API-driven import process** that recreates your on-call configuration in Rootly so you can cut over with confidence. The migration is designed to preserve the operational structure your responders rely on—who is on call, how rotations work, how overrides are applied, and how responders are notified—while also applying Rootly’s guardrails to keep the resulting configuration safe and maintainable.

A typical migration has two goals:

1. **Parity at cutover:** responders can acknowledge and resolve alerts in Rootly with familiar routing and escalation behavior.
2. **Clean operational ownership:** once you cut over, schedules, routing rules, and responder preferences in Rootly become your new source of truth going forward.

Rootly migrations are performed using **read-only Opsgenie API access**, meaning Rootly does not modify or delete any resources in Opsgenie. Your Opsgenie instance remains intact and can be kept running in parallel during a transition window if you want an added safety net.

To get started, simply **contact Rootly**. Your onboarding or customer success representative will walk you through scope, timing, and required access, then coordinate and execute the migration for you.

## What You Can Migrate

Rootly can migrate the core building blocks of Opsgenie on-call operations. Each section below explains what is migrated, how Rootly maps it, and where you should expect differences.

### Users

Rootly imports users in a way that prioritizes safe, deterministic matching and produces a usable on-call configuration immediately.

#### How users are matched

* Rootly matches Opsgenie users to Rootly users using the Opsgenie user `username`, which is treated as the user’s **email address**.
* If a Rootly user already exists with that email (including soft-deleted users), Rootly reuses that user rather than creating a duplicate.
* If no Rootly user exists for that email, Rootly creates a new Rootly user automatically and populates the email and name fields from Opsgenie.

#### User profile and time zone normalization

* Rootly imports the user’s name from Opsgenie (for example, `full_name`) and applies a normalized time zone value when available.
* If a user’s time zone in Opsgenie is empty or does not map cleanly, Rootly will fall back to your workspace defaults. Time zones primarily affect how times are displayed (and certain time-based features), not the underlying schedule logic.

#### Membership and on-call access

* Imported users are added to the target Rootly team/workspace.
* If your workspace uses on-call seat limits, users without an available on-call seat cannot be placed into rotations until seats are available. This is an operational constraint rather than a migration failure; it simply means you may need to assign seats before final cutover.

#### Contact methods and notification rules

Opsgenie user notification behavior is represented as **notification rule steps**, and Rootly translates those steps into Rootly’s notification rules:

* Opsgenie contact method `email` maps to Rootly email targets.
* Opsgenie contact method `sms` maps to Rootly SMS targets.
* Opsgenie contact method `voice` maps to Rootly call targets.
* The Opsgenie delay per step (for example, `sendAfter.timeAmount`) maps to the Rootly rule delay so responders are notified at the intended time offset.

Imported contact targets are created as verified targets during migration so that the resulting notification rules are immediately usable. After migration, responders can review and update their targets and preferences in Rootly (for example, changing their primary number or adding a mobile device for push notifications).

#### Default rule seeding (safety baseline)

After importing a user’s Opsgenie-derived rules, Rootly will seed any missing default Rootly notification rules that are required to give responders a safe baseline configuration. This ensures that users do not end up with a partially configured state if Opsgenie rules were missing, sparse, or not fully mappable.

### Teams and Routing

Opsgenie team structure typically represents operational ownership and routing boundaries. Rootly can import this structure into Rootly’s grouping model and import routing rules when present.

#### Teams to groups

* Opsgenie teams are imported as Rootly groups (teams/groups in Rootly terminology), allowing you to preserve ownership and organize responders in Rootly the same way they are organized in Opsgenie.
* Group membership and the imported users are aligned so schedules and routing rules can reference the correct owners.

#### Routing rules

* If your Opsgenie setup includes team routing logic, Rootly imports the team’s routing rules so that inbound alert flows can preserve the same “where should this go?” behavior.
* Routing rule import is handled as part of the team import stage so that teams exist before schedules and downstream references are created.

#### Slack integration import (optional, conditional)

Slack-related migration is supported only when all of the following are true:

* You choose to include `slack_integrations` in the migration scope.
* Your Rootly team has a connected Slack integration.
* You include one or more Opsgenie team IDs so Rootly knows which teams should have Slack integration configuration imported.

If those prerequisites are not met, Slack integration import is skipped. This prevents partially configured Slack behavior and keeps the resulting Rootly configuration deterministic.

### Services (Optional)

If you want Rootly to preserve Opsgenie service structure, Rootly can import Opsgenie services into Rootly services.

#### Service matching and name behavior

* Rootly attempts to match a service by Opsgenie service ID first.
* If no match exists by ID, Rootly attempts to match by name.
* If a name collision exists (for example, a different service already uses that name), Rootly may uniquify the imported service name by appending the Opsgenie service ID so you can distinguish them cleanly.

Imported services can then be used in analytics, ownership, and downstream routing/alerting workflows in Rootly.

### Schedules

Schedules are one of the most sensitive parts of an on-call migration because they affect real paging behavior. Rootly migrates schedules with the goal of preserving rotation logic and ensuring future coverage is computed correctly.

#### What schedule data is migrated

* Schedule definitions (name, ownership context)
* Rotations (including rotation rules)
* Overrides (coverage changes applied over time)
* Future shift generation derived from the imported rotation configuration

#### Overlapping rotations and schedule strategy

Opsgenie schedules can contain rotation patterns that overlap in ways that are difficult to represent cleanly as a single schedule in some systems. Rootly supports two strategies:

* **Single schedule strategy:** rotations are imported into one Rootly schedule, and overrides are created from Opsgenie schedule overrides.
* **Split rotations into separate schedules:** when enabled (`import_rotations_as_separate_schedules`), Rootly detects overlapping rotations and creates **one Rootly schedule per rotation**. This can make the resulting schedules easier to reason about and reduces ambiguity in overlap resolution.

The best choice depends on how your Opsgenie schedules are structured and how you expect schedule ownership to work after cutover. Rootly will recommend an approach during scoping if your environment has overlap-heavy schedules.

#### Syncing schedules vs. create-only schedules

Rootly can run an Opsgenie migration in either of these modes:

* **Create-only import:** recommended for clean cutovers or staged testing. Rootly creates new schedules without attempting to reconcile with existing Rootly schedules.
* **Sync existing:** recommended when you have already created Rootly resources and want the migration to update them. In sync mode, Rootly may remove and rebuild base (non-override) shifts and clean up removed overrides to maintain parity with the Opsgenie source.

Because sync mode can rebuild future shifts, it is typically used deliberately and validated carefully in a controlled window.

#### Shift recreation and throttling

When syncing schedules, Rootly can introduce a configurable delay before recreating shifts (`schedule_shift_recreation_delay`). This is a practical safety mechanism to avoid partial computations in environments with many schedules or heavy background job load.

Rootly can also throttle schedule imports (`schedule_import_delay`) to keep the migration stable and predictable for larger workspaces.

## Configuration Options You May Be Asked To Choose

Opsgenie migrations often include a few explicit choices so the resulting Rootly configuration matches your operational intent.

Common migration options include:

* **Migration scope controls (resources):**
  * `users`
  * `teams`
  * `schedules`
  * `services`
  * `slack_integrations`
* **Filtering and inclusion controls:**
  * Migrate only specific Opsgenie teams (`team_ids`)
  * Exclude specific Opsgenie teams (`excluded_team_ids`)
  * Migrate only a subset of users by email (`user_emails`)
* **Schedule behavior:**
  * Import overlapping rotations as separate schedules (`import_rotations_as_separate_schedules`)
  * Synchronize into existing Rootly resources (`sync_existing`)
  * Add delays for stability (`schedule_import_delay`, `schedule_shift_recreation_delay`)
* **Responder hygiene:**
  * Disable shift reminders for imported users (`disable_shift_reminders`)
* **Dry run mode:**
  * Validate and produce a report of what would be imported (including validation errors) without writing resources into Rootly (`dry_run`)

If you are unsure which options to select, a strong default is to begin with a dry run, then perform a create-only migration into a staging workspace (or a safe test team) before importing into production.

## Migration Process

### Step 1: Define scope and success criteria

Before any technical setup, define what “success” means for your organization. This reduces rework and prevents ambiguous expectations.

Recommended scoping questions:

* Are you migrating one Opsgenie team or many?
* Are you importing only schedules, or also services and routing rules?
* Do you need Slack integration behavior imported, or will it be reconfigured natively in Rootly?
* Do you need to preserve existing Rootly schedules (sync), or can this be a clean import?

Example success criteria:

* Every responder can be paged in Rootly via at least one reliable channel.
* Each core schedule generates correct upcoming shifts for the next 2–4 weeks.
* Critical services and teams have the correct ownership structure and routing.
* Overrides and coverage changes are represented correctly for upcoming time windows.

### Step 2: Create a read-only Opsgenie API key

Rootly migrations use the Opsgenie API to read configuration.

In Opsgenie:

1. Navigate to **Settings → App Settings → API key management**
2. Click **Add new API key**
3. Name the key clearly (example: “Rootly Migration – Read Only”)
4. Assign **Read** permissions for the relevant resources (users, teams, schedules, services as needed)
5. Copy the key securely and share it with the Rootly team using your approved secure channel

<Note>
  Use read-only permissions. Rootly does not need write access to Opsgenie to perform migration.
</Note>

### Step 3: Run a dry run (strongly recommended)

A dry run validates what Rootly can import and highlights any resources that will be skipped or require attention. This is especially valuable if your Opsgenie environment contains complex schedule overlap patterns or historical artifacts that are no longer actively used.

Dry runs typically surface:

* Users that cannot be matched cleanly (missing/invalid emails)
* Schedules that require a split-rotation strategy to preserve clarity
* Validation errors that would prevent import
* A summary report you can use to confirm the migration plan before anything is written

### Step 4: Execute the migration

After dry run validation, Rootly runs the migration asynchronously. Imports are staged so dependencies resolve correctly and scheduling logic remains stable.

At a high level, a migration commonly progresses through:

* Users and services
* Teams (and routing rules)
* Schedules (rotations, overrides, then shift generation)
* Slack integrations (only when configured and included)

Because the migration runs in the background, you can continue normal work while it completes, and then validate the results after completion.

### Step 5: Validate in Rootly before cutover

After import, treat validation as an explicit step. You should validate configuration correctness and real paging behavior.

Recommended validation checklist:

* Confirm each core schedule shows a correct “currently on-call” responder and upcoming shifts.
* Confirm rotation structure matches expected handoffs and time zones.
* Confirm overrides appear where you expect them for upcoming windows.
* Confirm a sample of responders have correct notification rules and reachable targets.
* Confirm team/group membership matches expectations and routing rules are present if imported.
* If Slack integration behavior matters, validate it only after Slack is fully connected in Rootly and `slack_integrations` was included in scope.

### Step 6: Cut over and monitor

When you are ready, shift your alert sources to route into Rootly On-Call, then actively monitor the first hours/days of production usage.

The most common cutover issues are not schedule logic problems—they are responder readiness and deliverability issues (for example, responders missing a mobile device connection or carriers filtering SMS). Validate reachable channels proactively.

## Best Practices

* **Start with a dry run.** Dry runs catch schedule edge cases early, when changes are easiest.
* **Decide schedule strategy up front.** If your Opsgenie schedules rely on overlapping rotations, consider splitting rotations into separate schedules for clarity.
* **Migrate in a controlled window.** Even without downtime, you want time reserved for validation and quick fixes.
* **Validate paging with real tests.** It’s not enough for rules to exist; verify a handful of responders can actually receive notifications via the channels you rely on.
* **Plan a staged cutover.** Many organizations keep Opsgenie running briefly while validating Rootly paging reliability, then fully cut over.
* **Communicate responder expectations early.** Tell responders what to install, what to verify, and what to expect during the transition.
* **Document any skipped or excluded resources.** If you exclude teams or only migrate specific users, keep a written record so the end state remains intentional.

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Does Rootly modify anything in Opsgenie during migration?">
    No. Rootly migrations use read-only Opsgenie API access. Rootly reads your Opsgenie configuration and recreates equivalent resources in Rootly, but does not write back to Opsgenie or delete anything in your Opsgenie account.
  </Accordion>

  <Accordion title="How does Rootly match users between Opsgenie and Rootly?">
    Users are matched by email address. Opsgenie’s user <code>username</code> is treated as the user’s email. If a Rootly user exists with the same email (including soft-deleted users), Rootly reuses that user. If no match exists, Rootly creates a new Rootly user and adds them to the team so schedules and routing can reference them.
  </Accordion>

  <Accordion title="How are Opsgenie notification rules mapped into Rootly?">
    Opsgenie notification rule steps are translated into Rootly notification rules. The Opsgenie contact method (<code>email</code>, <code>sms</code>, <code>voice</code>) maps to Rootly’s email, SMS, and call targets. The step delay (<code>sendAfter.timeAmount</code>) maps to the Rootly rule delay so the timing behavior stays consistent.
  </Accordion>

  <Accordion title="What happens if a schedule has overlapping rotations?">
    Rootly can import schedules in one of two ways. By default, rotations are imported into a single Rootly schedule and overrides are recreated. If your environment has overlapping rotations and you enable <code>import\_rotations\_as\_separate\_schedules</code>, Rootly can split rotations into separate Rootly schedules to keep overlap behavior clearer and reduce ambiguity.
  </Accordion>

  <Accordion title="Can I migrate only a subset of teams, schedules, or users?">
    Yes. The migration supports scope controls such as importing only specific team IDs, excluding specific team IDs, or limiting users by email address. This is useful for phased migrations where you transition one department or service group at a time.
  </Accordion>

  <Accordion title="Will Slack integrations be migrated automatically?">
    Slack integrations are imported only when you include <code>slack\_integrations</code> in migration scope and your Rootly workspace has a connected Slack integration. If those prerequisites are not met, Slack import is skipped to prevent partial or misleading configuration.
  </Accordion>

  <Accordion title="Who do I contact if something looks wrong after migration?">
    Contact your Rootly onboarding representative or Rootly Support. Share the relevant Opsgenie resource identifiers (team IDs, schedule IDs, service IDs) and a short description of what doesn’t match expectations so the Rootly team can diagnose quickly.
  </Accordion>
</AccordionGroup>

***

Need help planning or executing a migration? Contact your Rootly onboarding representative or email **[support@rootly.com](mailto:support@rootly.com)**.


Built with [Mintlify](https://mintlify.com).