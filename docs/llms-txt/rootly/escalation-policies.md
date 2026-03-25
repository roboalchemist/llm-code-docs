# Source: https://docs.rootly.com/on-call/escalation-policies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Escalation Policies

> Learn how to create, configure, and manage escalation policies to ensure alerts are acknowledged and acted on.

## Overview

Escalation Policies define **how Rootly notifies responders when an alert requires attention** and what happens if that alert is not acknowledged in time. They are the backbone of on-call reliability—ensuring alerts reach a human, escalate predictably, and never fall through the cracks.

An escalation policy answers three core questions:

* Who should be notified first?
* What should happen if no one responds?
* How long should Rootly continue escalating before stopping?

Once created, escalation policies are assigned to **Services** or **Teams**, where they become active and drive paging behavior.

***

## Create an Escalation Policy

Escalation policies are created from the On-Call section of the web app.

To create a new escalation policy:

1. Navigate to **On-Call → Escalation Policies**
2. Click **+ Add Escalation Policy**
3. Enter an **Escalation Policy Name** (required) and an optional description

<Tip>
  Some alert sources resolve themselves quickly. If this is common, consider adding a short delay before the first escalation step so transient issues don’t immediately page responders.
</Tip>

***

## Step 1: Who Do We Notify?

This step defines **who is initially responsible** for responding when an alert is triggered.

Rootly supports notifying:

* Individual users
* On-call schedules
* Teams or team admins
* Slack channels (for visibility)
* Other escalation policies (via escalation targets)

When multiple responders are eligible, you may optionally enable **Round Robin assignment**. This prevents the same person from being repeatedly paged and helps distribute alert load fairly.

Rootly offers two Round Robin strategies:

* **Alert-Based**, which rotates ownership per alert
* **Cycle-Based**, which rotates ownership on a fixed cycle

Learn more in the [Round Robin documentation](https://docs.rootly.com/on-call/round-robin-functionality#round-robin-functionality).

If an alert needs to be handed off to another group, you can use an **Escalate** target. This triggers the destination team’s escalation policy **in parallel**, while the original policy continues executing.

<Note>
  When you create an escalation policy, a **Default Escalation Path** is automatically created with **Audible notifications** enabled. This default path cannot be deleted and acts as a fallback if no other escalation paths match.
</Note>

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-06-11at15.27.11@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=2d28962c79fd4eb36fb8f036fdb192bb" alt="Escalation targets" width="1522" height="592" data-path="images/CleanShot2025-06-11at15.27.11@2x.png" />

<Warning>
  If your alert source sends a re-trigger event, Rootly will re-page the responder who last acknowledged the alert. If the alert remains unacknowledged, escalation continues according to the policy’s steps.
</Warning>

***

## Step 2: Add Escalation Steps

Escalation steps define **what happens next if an alert is not acknowledged**.

Each step includes:

* A delay (in minutes)
* One or more notification targets

Delays start counting from the previous step (or alert creation for the first step). This allows escalation to widen gradually as urgency increases.

<Note>
  Each escalation path can also define an **initial delay** (up to one week) before the first escalation step begins. This path-level delay is separate from step-level delays.
</Note>

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=db574eb3c111e53c69a967edb75df0fb" alt="" width="956" height="614" data-path="images/escalation-policies/2.webp" />
</Frame>

***

## Step 3: Configure Repeat Behavior

If an alert remains unacknowledged after all steps complete, you can choose to **repeat the escalation policy**.

When enabled, Rootly restarts escalation from the beginning and continues until:

* The alert is acknowledged, or
* The repeat limit is reached

This is commonly used for high-severity alerts where acknowledgement is mandatory.

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/3.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=f43e31715529319a07915dbfd97825d8" alt="" width="964" height="719" data-path="images/escalation-policies/3.webp" />
</Frame>

***

## Step 4: Save and Assign the Policy

Saving the policy does not activate it.

Escalation policies only run once they are assigned to a **Service** or **Team**, which determines which alerts will trigger the policy.

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/4.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=5ec9fd7fb1e886c4457b344c49145788" alt="" width="976" height="291" data-path="images/escalation-policies/4.webp" />
</Frame>

***

## Step 5: Assign the Escalation Policy to a Service or Team

Escalation policies only run once they are assigned to a **Service** or **Team**.\
This assignment determines which alerts will trigger the policy.

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/4.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=5ec9fd7fb1e886c4457b344c49145788" alt="" width="976" height="291" data-path="images/escalation-policies/4.webp" />
</Frame>

### Assigning to a Team

Assigning an escalation policy to a team ensures alerts routed to that team follow the defined escalation logic.

* Open the Team you want to configure
* Navigate to the **On-Call** tab
* Select the desired escalation policy

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/5.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=ae17211ba45680a127da0a36b18f61fd" alt="" width="966" height="734" data-path="images/escalation-policies/5.webp" />
</Frame>

### Assigning to a Service

Assigning an escalation policy to a service is recommended when alerts clearly map to a specific system or component.

* Open the Service you want to configure
* Navigate to the **On-Call** tab
* Select the desired escalation policy

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/6.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=a51af3e82f98ddd90452d1330aa40d26" alt="" width="970" height="212" data-path="images/escalation-policies/6.webp" />
</Frame>

***

## Escalation Paths (Advanced)

Escalation policies can contain **multiple escalation paths**, each with its own rules, steps, and notification behavior.

Paths allow you to model scenarios such as:

* Business hours vs after hours
* High vs low urgency alerts
* Different behavior based on alert metadata

Rootly evaluates paths **top to bottom** and selects the **first matching path**.\
The **Default Escalation Path** is always positioned at the bottom and is used as a fallback when no other paths match.

Each path can define:

* Matching rules and time restrictions
* An initial delay before escalation begins
* Its own escalation steps and repeat behavior
* Whether notifications are **Audible** or **Quiet**

### Audible vs Quiet Notifications

Each escalation path is either **Audible** or **Quiet**:

* **Audible paths** are designed to wake responders and trigger critical notifications
* **Quiet paths** respect Do Not Disturb and are used for lower-urgency alerts

Audible and Quiet paths map directly to each user’s notification rules.\
Learn more in [Audible and Quiet Notifications](/on-call/on-call-notifications).

### Limits and Constraints

Escalation policies have a few important limits:

* **Maximum escalation levels:** 20 per path
* **Maximum targets per level:** 25
* **Repeat count:** 1–9 cycles
* **Maximum delay per step:** 10,080 minutes (1 week)

Keeping policies simple and within these bounds improves reliability and maintainability.

***

## Edit or Delete an Escalation Policy

To edit or delete a policy:

1. Navigate to **On-Call → Escalation Policies**
2. Click the `…` menu next to the policy
3. Select **Edit** or **Delete**

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/escalation-policies/7.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=3f69bce697c3c987667021523bfaf93f" alt="" width="964" height="705" data-path="images/escalation-policies/7.webp" />
</Frame>

<Warning>
  Deleting an escalation policy is permanent. To disable a policy temporarily, unassign it from all teams and services instead.
</Warning>

***

## Best Practices

* Use short delays for high-severity alerts
* Assign policies to services whenever ownership is clear
* Avoid overly complex escalation trees
* Test policies with non-critical alerts before production use
* Use escalation paths to model time-based or urgency-based behavior

***

## FAQs

<AccordionGroup>
  <Accordion title="What happens if no one acknowledges an alert?" icon="circle-question">
    Escalation continues through all steps and repeat cycles until the alert is acknowledged or the policy completes.
  </Accordion>

  <Accordion title="Can escalation continue after acknowledgment?" icon="clock-rotate-left">
    Yes. If an acknowledgment timeout is configured and expires without resolution, escalation may resume.
  </Accordion>

  <Accordion title="Can one alert trigger multiple escalation policies?" icon="shuffle">
    Yes. Using an Escalate target triggers the destination policy while the original policy continues in parallel.
  </Accordion>

  <Accordion title="Do escalation policies create incidents automatically?" icon="circle-info">
    No. Escalation policies page responders. Incident creation is controlled separately through alert routing and workflows.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).