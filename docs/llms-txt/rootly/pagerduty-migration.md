# Source: https://docs.rootly.com/on-call/pagerduty-migration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PagerDuty Migration

> Migrate users, schedules, escalation policies, and notification settings from PagerDuty to Rootly On-Call with API-based data transfer.

## Overview

Migrating from PagerDuty to Rootly On-Call is an API-driven import process that recreates your paging configuration in Rootly so you can cut over with confidence. The migration is designed to preserve the structure your responders rely on—who is on-call, how alerts escalate, and how responders are notified—while also applying Rootly’s operational guardrails (for example, preventing schedule dependency loops and ensuring notification rules remain actionable).

A typical migration has two goals:

1. **Parity at cutover:** responders can acknowledge and resolve alerts in Rootly with familiar routing and escalation behavior.
2. **Clean operational ownership:** once you cut over, schedules and escalation policies in Rootly become your new source of truth going forward.

Rootly migrations are performed using **read-only PagerDuty API access**, meaning Rootly does not modify or delete any resources in PagerDuty. Your PagerDuty instance remains intact and can be kept running in parallel during a transition window if you want an added safety net.

To get started, simply **contact Rootly**. Your onboarding or customer success representative will walk you through scope, timing, and required access, then coordinate and execute the migration for you.

## What You Can Migrate

Rootly can migrate the core building blocks of on-call operations. Each section below explains what is migrated, how Rootly maps it, and where you should expect differences.

### Users

Rootly imports users in a way that prioritizes safe, deterministic matching.

**How users are matched**

* Rootly matches PagerDuty users to Rootly users using **email address**.
* If a Rootly user with that email already exists (including soft-deleted users), Rootly will reuse that user rather than creating a duplicate.
* If no Rootly user exists for the email, Rootly creates a new Rootly user automatically.

**Team membership and on-call access**

* Imported users are added to the target Rootly team/workspace.
* Your team’s defaults (and any relevant workspace configuration) may apply to newly created memberships, including default on-call role assignment.
* If your workspace uses on-call seat limits, users without an available on-call seat cannot be added into schedule rotations until seats are available.

**Contact methods that are migrated**
Rootly migrates user contact information used for paging, including:

* Email address(es)
* SMS-capable phone number(s)
* Call-capable phone number(s)

**How notification rules are migrated**
PagerDuty notification rules are translated to Rootly’s notification rule model where compatible:

* PagerDuty **urgency = low** maps to Rootly **quiet** notification rules.
* PagerDuty **urgency ≠ low** maps to Rootly **audible** notification rules.
* PagerDuty notification start delays map to Rootly rule delays when possible.
* Contact method types are mapped into Rootly’s supported contact methods, which include:
  * Email
  * SMS
  * Phone call
  * Critical mobile push (bypasses device Do Not Disturb when configured)
  * Non-critical mobile push (respects device Do Not Disturb when configured)

**What happens when a rule cannot be mapped**

* If a PagerDuty rule uses a configuration that does not translate cleanly, Rootly skips that rule rather than importing a partial or misleading configuration.
* After import, Rootly can also seed defaults (if needed) so every responder has a safe baseline configuration (for example, an email-based quiet rule).

**Important behavioral expectations**

* Rootly enforces practical paging constraints in the UI for audible notification rules. For example, initial audible steps typically must include an immediately actionable path (critical push or call) so responders cannot accidentally configure an audible chain that can never reach them.
* Where your PagerDuty rules include escalations or multi-step paging, validate your Rootly notification rules post-import to ensure the “audible” versus “quiet” intent matches your team’s reality.

### Schedules

Rootly imports schedules with the intent of preserving rotation logic and future coverage.

**What schedule data is migrated**

* Schedule definitions (name, description where applicable)
* Rotations and rotation membership
* Overrides
* Shift generation behavior (Rootly will generate future shifts based on imported rotation configuration)

**Supported schedule membership types**
Rootly schedules support rotation members that are:

* Individual users
* Other schedules (nested schedules), with safeguards to prevent circular dependencies

If your PagerDuty design effectively represents a team as a “target,” Rootly typically models that as a schedule rather than embedding a “team” directly inside a schedule rotation.

**Schedule validation and skip behavior**
Some schedules may be intentionally skipped for safety or compatibility. A notable case:

* Schedules with rotation turn lengths shorter than **24 hours** may be skipped during migration.

If schedules are skipped, the migration should record them as skipped resources so you can review and decide whether to recreate them manually using Rootly-native patterns.

**Syncing schedules vs. creating schedules**
Depending on migration settings:

* You can import schedules into a clean workspace (create-only), or
* You can **synchronize** against existing Rootly schedules (sync mode). In sync mode, Rootly may rebuild base shifts and clean up removed overrides to match the source.

Because schedule sync can rebuild future shifts, migrations often support a configurable delay between shift recreation steps to prevent racing or partial computations.

### Escalation Policies

Escalation policies are imported to preserve “who is notified, when, and in what order.”

**What escalation policy data is migrated**

* Escalation policy definitions and levels
* Targets within each level (where compatible)
* Ordering and delays

**Audible vs. quiet escalation paths**
Rootly can optionally create separate escalation paths to mirror PagerDuty urgency behavior, such as:

* A quiet path designed for low urgency routing
* An audible path designed for urgent paging

Whether you enable this depends on how strictly you separate low urgency vs. high urgency in your operational model.

**Target types you can expect**
Escalation levels in Rootly can target combinations of:

* Users
* Schedules
* Teams/groups (in Rootly terminology, groups)
* Slack channels
* Services (depending on configuration)

Rootly also supports paging strategies and targeting modes (including round robin strategies) that you can layer on top after migration if you want more control than your original PagerDuty setup provided.

### Services and Teams (Optional)

Depending on migration settings, Rootly can also import:

* PagerDuty teams into Rootly groups
* PagerDuty services into Rootly services

If enabled, Rootly can optionally set owning teams for services to preserve operational ownership and improve reporting and routing downstream.

## Configuration Options You May Be Asked To Choose

PagerDuty migrations often include a small number of explicit choices so the resulting Rootly configuration matches your intent.

Common migration options include:

* **PagerDuty region:** US or EU
* **Import scope controls:**
  * Import all escalation policies, or only specific escalation policy IDs
  * Exclude certain schedule IDs
  * Import all users, or restrict to users referenced by migrated schedules/policies
* **Resource strategy:**
  * Create-only import
  * Synchronize existing Rootly resources
* **Escalation policy behavior:**
  * Create separate quiet and audible escalation paths
* **Operational hygiene options:**
  * Disable shift reminders for imported users (helpful if you want responders to opt in later)
* **Timing controls:**
  * Delay between escalation policy imports and schedule imports
  * Delay before schedule shift recreation in sync mode
* **Dry run mode:**
  * Validate and produce a report of what would be imported (including validation errors) without writing resources into Rootly

If you are unsure which options to select, a good default is to start with a dry run, then run a create-only import into a staging workspace (or a safe test team) before importing into production.

## Migration Process

### Step 1: Define Scope and Success Criteria

Before any technical setup, define what “success” means for your organization. This reduces rework and prevents ambiguous expectations.

Recommended scoping questions:

* Are you migrating one team or multiple teams?
* Are you migrating only schedules and escalation policies, or also services and teams?
* Do you need parity for low-urgency workflows (quiet routing), or only urgent paging?
* Do you need to preserve existing Rootly resources, or can this be a clean import?

Common “success criteria” examples:

* Every responder can be paged in Rootly via at least one reliable channel.
* Every critical service has an escalation policy attached and can page an on-call responder.
* The most important schedules generate correct upcoming shifts for the next 2–4 weeks.
* Escalation policies correctly notify schedules/users in the intended order with expected delays.

### Step 2: Create a Read-Only PagerDuty API Key

Rootly migrations use the PagerDuty API to read configuration.

In PagerDuty:

1. Navigate to **Integrations → Developer Tools → API Access Keys**
2. Create a new API key
3. Name the key clearly (example: “Rootly Migration – Read Only”)
4. Ensure the key is **read-only**
5. Copy the key securely and share it with the Rootly onboarding team using your approved secure channel

<Note>
  Use a read-only key. Rootly does not need write access to PagerDuty to perform migration.
</Note>

### Step 3: Run a Dry Run (Strongly Recommended)

A dry run validates what Rootly can import and highlights any resources that will be skipped or require attention. This is especially valuable if your PagerDuty instance contains edge cases (complex layers, unusual rotation lengths, legacy artifacts).

A dry run typically surfaces:

* Users that cannot be matched cleanly (missing emails, invalid data)
* Schedules that will be skipped (for example, short turn lengths)
* Policies that reference unsupported patterns
* Any validation errors that would prevent import

If you are migrating a large environment, a dry run is the safest way to avoid surprises.

### Step 4: Execute the Migration

After dry run validation, Rootly runs the migration asynchronously. Imports are typically staged so dependencies resolve correctly (for example, users exist before schedules reference them).

At a high level, a migration commonly progresses through:

* Users (and optional teams/groups)
* Services (optional)
* Schedules (and overrides, then shift generation)
* Escalation policies

Because the migration runs in the background, you can continue normal work while it completes, and then validate the results after completion.

### Step 5: Validate in Rootly Before Cutover

After import, treat validation as an explicit step—not an afterthought. You should validate both configuration correctness and real paging behavior.

Recommended validation checklist:

* Confirm each core schedule shows a correct “currently on-call” responder and upcoming shifts.
* Confirm escalation policies reference the intended schedules/users/targets.
* Confirm a sample of responders have correct notification rules (audible + quiet).
* Use “test notifications” (where available) to confirm SMS/call/push delivery for a few responders.
* Confirm that any intentionally excluded resources are documented so you can recreate them manually if needed.

### Step 6: Cut Over and Monitor

When you are ready, shift your alert sources to route into Rootly On-Call, then actively monitor the first hours/days of production usage.

During cutover, the most common issues are not configuration problems—they are deliverability or responder readiness issues (for example, a responder never installed the mobile app or has not verified a phone number). Use Rootly’s readiness tooling and test notifications proactively.

## Best Practices

These practices reduce risk and make the migration easier to validate and operate.

* **Start with a dry run.** Dry runs catch incompatible schedules and policy edge cases early, when changes are easiest.
* **Migrate in a controlled window.** Even if Rootly doesn’t require downtime, you want your team mentally prepared for validation and quick fixes.
* **Plan a staged cutover.** Many organizations keep PagerDuty live briefly while they validate Rootly paging reliability, then fully cut over.
* **Validate paging with real test notifications.** It’s not enough for rules to exist; verify that responders actually receive calls/SMS/push.
* **Decide your urgency model up front.** If you rely heavily on low urgency workflows, enable separate quiet and audible escalation paths. If you don’t, keep it simple.
* **Communicate responder expectations early.** Tell responders what to install (mobile app), what to verify (phone numbers), and what to expect during the transition.
* **Document “skipped resources.”** If something is skipped (such as a schedule layer with short rotation length), write down why and your replacement approach in Rootly.

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Does Rootly modify anything in PagerDuty during migration?">
    No. Rootly migrations use read-only PagerDuty API access. Rootly reads your PagerDuty configuration and recreates equivalent resources in Rootly, but does not write back to PagerDuty or delete anything in your PagerDuty account.
  </Accordion>

  <Accordion title="How does Rootly match users between PagerDuty and Rootly?">
    Users are matched by email address. If a Rootly user exists with the same email (including soft-deleted users), Rootly reuses that user. If no match exists, Rootly creates a new Rootly user and adds them to the team so schedules and escalation policies can reference them.
  </Accordion>

  <Accordion title="Are notification rules migrated exactly as-is?">
    Notification rules are migrated when compatible. PagerDuty low urgency rules map to Rootly quiet rules, while all other rules map to Rootly audible rules. Delays are preserved where supported, and contact methods are mapped into Rootly’s supported channels (email, SMS, call, and mobile push). If a rule cannot be mapped reliably, Rootly skips it to avoid creating misleading paging behavior.
  </Accordion>

  <Accordion title="Why were some schedules skipped?">
    Some schedules may be skipped due to compatibility guardrails—most commonly when a schedule layer uses rotation turn lengths shorter than 24 hours. Skipped resources should be reviewed and recreated using Rootly-native patterns if they are operationally important.
  </Accordion>

  <Accordion title="Can I migrate only part of my PagerDuty configuration?">
    Yes. You can limit migration scope—for example, importing only specific escalation policy IDs, excluding certain schedules, or controlling whether all users are imported. This is useful for phased migrations where you transition one team or service group at a time.
  </Accordion>

  <Accordion title="Can Rootly sync into an existing Rootly workspace with existing schedules and users?">
    Yes. Migrations can be configured to synchronize against existing resources rather than always creating new ones. Sync mode may rebuild future shifts and clean up removed overrides to maintain parity with the PagerDuty source, so it should be used deliberately and validated carefully.
  </Accordion>

  <Accordion title="What should we validate before routing alerts to Rootly?">
    Validate that schedules show correct on-call responders, escalation policies point to the right targets, and a sample of responders can receive pages via at least one reliable channel. If you use mobile push, confirm responders have devices connected. If you use SMS/calls, confirm phone numbers are correct and deliverability is acceptable for your region and carriers.
  </Accordion>

  <Accordion title="Who do I contact if something looks wrong after migration?">
    Contact your Rootly onboarding representative or Rootly Support. Come prepared with the PagerDuty resource IDs (schedule IDs, escalation policy IDs) and a short description of the mismatch you’re seeing so the issue can be diagnosed quickly.
  </Accordion>
</AccordionGroup>

***

Need help planning or executing a migration? Contact your Rootly onboarding representative or email **[support@rootly.com](mailto:support@rootly.com)**.


Built with [Mintlify](https://mintlify.com).