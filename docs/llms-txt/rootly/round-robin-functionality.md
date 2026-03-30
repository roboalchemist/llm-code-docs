# Source: https://docs.rootly.com/on-call/round-robin-functionality.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Round Robin Functionality

> Learn about the Round Robin functionalities.

## Overview

Rootly's round robin feature introduces a streamlined way to manage escalation policies by automatically rotating the paging responsibilities among on-call team members. This ensures that alerts are distributed evenly and efficiently, reducing the burden on any single individual.

This feature is included out-of the box and is available for use today.

## Key Features

### Paging Methods

#### Alert-Based Paging

This is the most common style of round robin paging. Incoming alerts are cycled through the rotation of users. For example, the first incoming will page User A, if User A doesn't respond, it will escalate to level 2. The next incoming alert will page User B to ensure even distribution of alerts.

<Frame>
  <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/round-robin/1.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=23b40407ea640d8acdb881f52be5862f" width="910" height="897" data-path="images/round-robin/1.webp" />
</Frame>

#### Cycle-Based Paging

The cycle-based feature ensures each user in the escalation level is paged in sequential order before escalating to the next level.

<Frame>
  <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/round-robin/2.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=b51c163636d2504dfe771ff76391c1f7" width="929" height="1103" data-path="images/round-robin/2.webp" />
</Frame>

### Dynamic Updates

Rootly's web UI dynamically updates to show the current pageable person and the order of escalation. Timeline events also indicate the strategy used for each page.

### Configuring Round Robin

<iframe width="100%" height="420" src="https://www.loom.com/embed/7068151e897d4671b444ca8aaef205f9?t=0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen autoplay />

1. Navigate to Escalation Policies:
   * Go to the escalation policies section in your Rootly dashboard.
   * On-Call --> Escalation Policies
2. Create/Select an Escalation Policy:
   * Create a new escalation policy or choose an existing policy you want to configure for round robin.
3. Enable Round Robin:
   * When the feature flag for round robin is enabled, toggle the round robin option in each escalation policy level.

<Frame>
  <img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/round-robin/3.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=0e2a2b04877ab5c0ee290b9a76ff0d3d" width="893" height="349" data-path="images/round-robin/3.webp" />
</Frame>

4. Select either Alert-Based or Cycle-Based Paging:
   * Set the levels to be alert-based, where each new alert pages the next person in line.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/round-robin/4.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=8c7912ef8e465ba755e2ac3a45369ccc" width="897" height="341" data-path="images/round-robin/4.webp" />
</Frame>

#### Example Scenario (Alert-based)

In this example, we have an escalation policy named "SRE - Round Robin EP" with one round robin alert-based level. The first pageable person is Alexandra. When alert A comes in, if Alexandra doesn't respond within five minutes, the alert moves to Andre, and then to Purvai.

* When alert B comes in, it will then go to Shadab and then escalate to the next level.
* When alert C comes in, it will then go to Andre and then escalate to the next level.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/round-robin/5.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=1cc977c88d4f8c06f52fa9f9d8505ad1" width="1280" height="927" data-path="images/round-robin/5.webp" />
</Frame>

1. Initial Alert:
   * Alexandra receives the first alert.
2. Escalation to Next Person:
   * After five minutes without a response, the alert escalates to Andre.
3. Further Escalation:
   If Andre also doesn’t respond, the alert moves to Purvai.
4. Repeat Cycle:
   * The repeat feature cycles the alerts back to Alexandra after Purvai.

#### Example Scenario (Cycle-Based)

In this example, we have an escalation policy named "SRE - Round Robin EP" with one cycle-based level. The first pageable person is Alexandra. When alert A comes in, it will first go to Alexandra and if she does not respond, then the alert moves to Shadab, and then to Andre.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/round-robin/6.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=440e8dfb5cdb04d93df34b725c3d7fcd" width="1280" height="480" data-path="images/round-robin/6.webp" />
</Frame>

1. Initial Alert:
   * Alexandra receives the first alert.
2. Escalation to Next Person:
   * After one minute without a response, the alert escalates to Shadab.
3. Further Escalation:
   * If Shadab also doesn’t respond, the alert moves to Andre.
4. Repeat Cycle:
   * The repeat feature cycles the alerts back to Alexandra after Andre.

### Timeline Events

Timeline events will now show an indication of the strategy used for each page, providing clarity on how the alert was escalated and which strategy was employed.


Built with [Mintlify](https://mintlify.com).