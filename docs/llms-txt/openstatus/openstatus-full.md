# Openstatus Documentation

Source: https://docs.openstatus.dev/llms-full.txt

---

<SYSTEM>This is the full developer documentation for openstatus docs</SYSTEM>

# OpenStatus Documentation

> Learn how to create your status page, monitor your services, and keep your users informed — all open source.

### What is openstatus?

[Section titled “What is openstatus?”](#what-is-openstatus)

[openstatus](https://www.openstatus.dev) is an open-source status page platform with uptime monitoring. Monitor your websites, APIs, and services from multiple global locations and share real-time status updates with your users.

### Why OpenStatus?

[Section titled “Why OpenStatus?”](#why-openstatus)

* **Open source** — fully open-source, self-hostable, and transparent
* **Beautiful status pages** — keep your users informed with public or audience specific status pages
* **30+ global locations** — monitor from your users’ perspective, not just your own
* **HTTP, TCP & DNS monitors** — check APIs, servers, and DNS resolution
* **12 notification channels** — Slack, Discord, PagerDuty, OpsGenie, email, SMS, and more
* **Monitoring as code** — define monitors in YAML, manage with CLI or Terraform
* **OpenTelemetry export** — send metrics to Grafana, Datadog, Honeycomb, or any OTLP endpoint
* **Private locations** — deploy lightweight probes inside your own infrastructure

### How to use this documentation

[Section titled “How to use this documentation”](#how-to-use-this-documentation)

Our documentation follows the [Diátaxis framework](https://diataxis.fr/), organizing content into four distinct categories to help you find what you need:

[📚 Tutorials ](/tutorial/getting-started/)Step-by-step lessons to learn openstatus from scratch. Start here if you're new!

[🛠️ How-to Guides ](/guides/getting-started/)Practical guides to solve specific problems and accomplish particular tasks.

[💡 Concepts ](/concept/getting-started/)In-depth explanations of key concepts, design decisions, and best practices.

[📖 Reference ](/reference)Technical specifications, API documentation, and configuration references.

**Not sure where to start?**

* **New users**: Begin with our [tutorials](/tutorial/getting-started/) to create your first monitor
* **Experienced users**: Check out [how-to guides](/guides/getting-started/) for specific tasks
* **Need help?** Visit our [help section](/help/support/) or join our community

### Join the community

[Section titled “Join the community”](#join-the-community)

Join the community to get help, share your ideas or just to say hi.

[Bluesky ](https://bsky.app/profile/openstatus.dev)

[Discord ](https://www.openstatus.dev/discord)

[GitHub ](https://www.openstatus.dev/github)

# Not Found

> This page could not be found.



# Building Trust with Status Pages

> Understanding how to communicate effectively during incidents and build user trust through transparency.

```plaintext
+------------------------------------------------+
|               openstatus Status Page           |
+------------------------------------------------+
| Service Name      | Status | Uptime            |
+-------------------+--------+-------------------+
| Web Server        | ✅ OK       | 99.9%        |
| Database          | ✅ OK       | 99.8%        |
| API Gateway       | ⚠️ Degraded | 99.5%        |
| Monitoring        | ✅ OK       | 100%         |
| Payment Processing| ✅ OK       | 99.7%        |
+-------------------+--------+-------------------+
| Incidents:                                     |
|                                                |
|   - Degraded performance on API Gateway due    |
|     to high traffic. Our team is investigating.|
+------------------------------------------------+
```

## The purpose of a status page

[Section titled “The purpose of a status page”](#the-purpose-of-a-status-page)

A status page is more than just a dashboard of green lights. It’s a critical tool for communication and a cornerstone of building trust with your users. Its primary purpose is to provide a single, authoritative source of truth about your service’s health and any ongoing incidents.

When done right, a status page:

* **Reduces support burden**: Users can self-serve information about outages instead of contacting your team.
* **Builds trust**: Proactive transparency, even when things go wrong, demonstrates accountability.
* **Improves communication**: It provides a central and consistent channel for incident updates.
* **Demonstrates professionalism**: It shows that you take reliability and user experience seriously.

This article explores the principles that make a status page an effective tool for building trust.

## Principles of Effective Status Pages

[Section titled “Principles of Effective Status Pages”](#principles-of-effective-status-pages)

### Maintain Transparency and Honesty

[Section titled “Maintain Transparency and Honesty”](#maintain-transparency-and-honesty)

A status page’s effectiveness hinges on being a reliable source of truth. Be upfront about issues, even minor ones. Hiding problems erodes user trust and can lead to frustration and a higher support load.

* **Communicate Clearly:** Use simple, non-technical language. Your users shouldn’t need a technical dictionary to understand the impact of an issue.

* **Be Timely:** Update the page as soon as an incident is confirmed. Provide regular, predictable updates throughout the resolution process, even if the only update is “we’re still working on it.”

### Automate Where Possible

[Section titled “Automate Where Possible”](#automate-where-possible)

Manual updates during a high-stress outage are prone to error and can be slow. Automation ensures that your status page reflects reality quickly and accurately.

* **Integrate Monitoring Tools:** Your status page should be directly connected to your internal monitoring and alerting systems. When a metric crosses a threshold (e.g., a high error rate), the status page can be updated automatically to reflect a degraded state.

* **Use an API:** We provide APIs that allow you to programmatically update component statuses and post new incidents, integrating your status page into your incident response workflows.

### Provide Context-Rich Incident Communication

[Section titled “Provide Context-Rich Incident Communication”](#provide-context-rich-incident-communication)

When an incident occurs, a structured narrative helps users understand the situation.

* **Start with the Impact:** Clearly and concisely state what the problem is from the user’s perspective. For example, “Users are currently unable to log in.”

* **Explain the Cause (When Known):** Briefly explain the root cause if you’ve identified it. Transparency here is key.

* **Outline Next Steps and ETA:** Explain what is being done to resolve the issue and provide an estimated time to resolution if possible. It’s better to give a conservative estimate or no estimate than to give one you can’t meet.

A typical incident communication lifecycle looks like this:

* **Investigating:** “We’re currently investigating an issue affecting user logins.”

* **Identified:** “We’ve identified the root cause as a database connection issue and are working on a fix.”

* **Monitoring:** “A fix has been deployed, and we’re monitoring the system to ensure stability.”

* **Resolved:** “The issue has been resolved. We will publish a post-mortem within 48 hours.”

### Ensure Easy Accessibility

[Section titled “Ensure Easy Accessibility”](#ensure-easy-accessibility)

Your status page is useless if no one can find it.

* **Prominent Link:** Link to your status page from your application’s footer, your main website, and your support documentation.

* **Custom Domain:** Use a simple, memorable URL like `status.yourcompany.com`.

## Advanced Considerations for Deeper Trust

[Section titled “Advanced Considerations for Deeper Trust”](#advanced-considerations-for-deeper-trust)

### Scheduled Maintenance

[Section titled “Scheduled Maintenance”](#scheduled-maintenance)

Communicating planned downtime is just as important as communicating unexpected incidents.

* Announce maintenance well in advance (e.g., at least 72 hours).
* Display upcoming maintenance windows clearly on the status page.
* Send reminders to subscribers before maintenance begins.

### Historical Data and Post-Mortems

[Section titled “Historical Data and Post-Mortems”](#historical-data-and-post-mortems)

Demonstrate your commitment to reliability by being open about your track record.

* Display historical uptime percentages (e.g., over the last 30/60/90 days).
* Link to past incidents and their post-mortems. Being honest about past failures and what you’ve learned from them is a powerful trust-builder.

### Subscriber Notifications

[Section titled “Subscriber Notifications”](#subscriber-notifications)

Allow users to opt-in to the level of communication they want.

* Email notifications for new incidents and resolutions.
* SMS for critical alerts (if applicable).
* RSS/Atom feeds for users who want to integrate your status into their own monitoring.

## Common Pitfalls to Avoid

[Section titled “Common Pitfalls to Avoid”](#common-pitfalls-to-avoid)

1. **Claiming unrealistic uptime**: Don’t claim 100% uptime unless you can back it up. Honesty is better than perfection.
2. **Hiding or downplaying incidents**: Users will find out anyway. It’s better they hear it from you.
3. **Using technical jargon**: Write for a broad audience, not just other engineers.
4. **Leaving users in the dark**: During an incident, regular updates are crucial, even if there’s no new information. A simple “still investigating” is better than silence.
5. **Hosting your status page on the same infrastructure**: Your status page must be available even when your main service is down.

## Implementing with openstatus

[Section titled “Implementing with openstatus”](#implementing-with-openstatus)

openstatus is designed to make implementing these principles straightforward:

* **[Create a status page](/tutorial/how-to-create-status-page)** - Get set up in minutes.
* **[Configure your page](/tutorial/how-to-configure-status-page)** - Customize its appearance to match your brand.
* **[Understand uptime calculations](/concept/uptime-calculation-and-values)** - Be transparent about how you measure uptime.

## Next steps

[Section titled “Next steps”](#next-steps)

* **[Understanding uptime monitoring](/concept/uptime-monitoring)** - Learn more about monitoring what you communicate.
* **[Status page reference](/reference/status-page)** - Dive into technical configuration options.

# Foundational Concepts

> Understand uptime monitoring, latency vs response time, SLA calculations, and the design decisions behind OpenStatus.

## Building a solid foundation

[Section titled “Building a solid foundation”](#building-a-solid-foundation)

This section of our documentation is dedicated to explanation. It’s not about quick fixes or step-by-step instructions. Instead, it’s here to help you build a deep understanding of uptime monitoring and the principles behind OpenStatus.

A solid mental model will empower you to use our tools more effectively, make better decisions for your own systems, and communicate with your team and stakeholders with clarity and confidence.

We’ll explore the “why” behind the “what,” covering core concepts, best practices, and the design philosophy that guides our development.

### Core Concepts

[Section titled “Core Concepts”](#core-concepts)

Start here to grasp the fundamental building blocks of uptime monitoring.

* **[Uptime Monitoring](/concept/uptime-monitoring)**: What is it, why does it matter, and how does it work?
* **[Uptime Calculation and Values](/concept/uptime-calculation-and-values)**: A look under the hood at how uptime percentages are calculated and what they truly represent.
* **[Latency vs Response Time](/concept/latency-vs-response-time)**: Untangle the difference between these two critical performance metrics.

### Best Practices & Philosophy

[Section titled “Best Practices & Philosophy”](#best-practices--philosophy)

Learn from experience and understand our approach to modern monitoring.

* **[Building Trust with Status Pages](/concept/best-practices-status-page)**: How to communicate effectively during incidents and maintain user trust.
* **[Uptime Monitoring as Code](/concept/uptime-monitoring-as-code)**: The why and how of managing your monitoring configuration in a GitOps workflow.

Have questions or want to discuss these concepts? [Join our community](/help/support/) and share your thoughts!

# Understanding Latency vs Response Time

> Deep dive into the difference between latency and response time, and why both matter for monitoring

## The confusion

[Section titled “The confusion”](#the-confusion)

Latency and response time are often used interchangeably, but they measure different things. Understanding the distinction is crucial for effective monitoring and performance optimization.

**The key difference:**

* **Latency** measures network travel time
* **Response time** measures total time including server processing

Both metrics matter, but for different reasons.

## What is latency?

[Section titled “What is latency?”](#what-is-latency)

Latency and response time are two different metrics used in uptime monitoring. Latency measures the time it takes for a request to travel from the probes to the server and back. Response time is the time it takes for the server to process the request and send back a response, plus the latency.

```plaintext
openstatus                  Network                 Server (Website)
  |                           |                          |
  |------- Request ---------->|                          |
  | (Timestamp A: Send)       |                          |
  |                           |------- Process --------->|
  |                           | (Server processing time) |
  |                           |<------- Response --------|
  |                           | (Timestamp B: Receive)   |
  |                           |                          |
Latency = Timestamp B - Timestamp A
```

Latency is the time it takes for data to travel from its source to its destination. Think of it as the round-trip time (RTT) for a network packet. This delay is influenced by several factors:

* **Distance:** The physical distance between the client and the server. Data traveling across continents will have higher latency than data traveling within the same city.

* **Network Congestion:** When too much data is on the network, it can slow down transmission, similar to a traffic jam on a highway.

To measure latency, you can monitor endpoints like `/ping` or `/healthcheck` with minimum server processing time.

## What Is Response Time?

[Section titled “What Is Response Time?”](#what-is-response-time)

```plaintext
    openstatus                 Network                Server
        |                         |                     |
(Start) |------- Request -------->|                     |
(T1)    |                         |                     |
        |                         |--- Processing ----->|
        |                         |   (Server's work)   |
        |                         |<-- Response Data ---|
        |                         |                     |
(End)   |<--- (Received) ---------|                     |
(T2)    |                         |                     |


 Response Time = T2 - T1
```

Response time is the total time from the moment a user’s request is sent until the moment the first byte of the server’s response is received. It includes both the network latency and the server’s processing time.

Response time = Network Latency + Server Processing Time

The server processing time is the duration the server spends on tasks like:

* Executing database queries.
* Running application logic.
* Generating the HTML or JSON response.

A high response time often indicates a problem with the server-side application itself. For example, slow database queries or inefficient can dramatically increase the response time, even if the network latency is low.

## Why the distinction matters for uptime monitoring

[Section titled “Why the distinction matters for uptime monitoring”](#why-the-distinction-matters-for-uptime-monitoring)

Understanding the difference between these two metrics is crucial for diagnosing performance issues.

* If your monitoring shows a **high response time but low latency**, the problem is likely with your server’s performance. You should investigate your application’s code, database queries, and server resources.

* If both your **latency and response time** are high, the issue is likely network-related. This could be due to a poor connection between the monitoring location and your server, or a broader network issue.

* **Response time is the ultimate measure of user experience** because it reflects the full journey of a request. Users don’t just care how fast a packet can get to the server; they care how long it takes to see the results.

By monitoring both metrics, you can quickly pinpoint whether a performance slowdown is caused by your application or by the network.

## Practical implications

[Section titled “Practical implications”](#practical-implications)

### For monitoring strategy

[Section titled “For monitoring strategy”](#for-monitoring-strategy)

* **Monitor both metrics**: Don’t rely on just one
* **Set appropriate thresholds**: Latency thresholds should be lower than response time thresholds
* **Consider geographic factors**: Latency varies by monitoring location
* **Track trends**: Sudden changes in either metric indicate issues

### For optimization

[Section titled “For optimization”](#for-optimization)

* **Reduce latency**: Use CDNs, optimize routing, choose closer hosting
* **Improve response time**: Optimize code, database queries, caching
* **User location matters**: Users far from your server will always see higher latency

### Common scenarios

[Section titled “Common scenarios”](#common-scenarios)

**Scenario 1: Consistent latency, variable response time**

* Indicates server-side performance issues
* Look at: Database queries, API calls, resource utilization

**Scenario 2: High latency from specific regions**

* Indicates geographic network issues
* Solution: Add regional monitoring points or CDN

**Scenario 3: Both metrics degrading**

* Could be network saturation or DDoS attack
* Check: Network bandwidth, traffic patterns, security

## What openstatus tracks

[Section titled “What openstatus tracks”](#what-openstatus-tracks)

openstatus monitors and displays:

* **Total response time**: The complete user experience
* **Detailed timing breakdown**: DNS, TCP, TLS, request, response
* **Regional differences**: Compare performance across locations
* **Historical trends**: Identify patterns over time

## Next steps

[Section titled “Next steps”](#next-steps)

* **[Create your first monitor](/tutorial/how-to-create-monitor)** - Start tracking these metrics
* **[Understanding uptime monitoring](/concept/uptime-monitoring)** - Broader monitoring concepts
* **[HTTP monitor reference](/reference/http-monitor)** - Technical specifications

# Uptime Calculation and Shared Values

Let’s face it - uptime values can be a complete lie if they’re not properly connected to monitoring.

We want to make uptime transparent and configurable. You decide how your uptime is calculated and which values you want to share on your status page. When monitoring an endpoint, a check can end up in one of three states:

* ✅ Success – everything’s fine
* ⚠️ Degraded – slow or partially failing
* ❌ Down – no response or full failure

We now offer multiple types of uptime calculation:

* **Absolute** (default): derived directly from your monitoring data

  * **Duration**: aggregated from the incidents duration
  * **Requests** (default): aggregated from the request values

* **Manual**: for teams that prefer full control over what’s shown

**TL;DR**

| Type                    | Source of Truth     | What Users See                         | Best For                        |
| ----------------------- | ------------------- | -------------------------------------- | ------------------------------- |
| **Duration** (Absolute) | Incident duration   | Time based uptime, proportional colors | Accurate long-term view         |
| **Request** (Absolute)  | Every ping result   | Request-based uptime %                 | Real-time reflection            |
| **Manual**              | Manually set status | Controlled, narrative updates          | Transparency without monitoring |



Let’s break them down!

## Absolute Type

[Section titled “Absolute Type”](#absolute-type)

The absolute type calculates uptime based on actual monitoring results. It’s the most accurate reflection of what’s really happening, and comes in two variants: *Duration* and *Request*. Both of these share real data with your users - incidents, degraded states, and historical uptime - but they differ in how they aggregate and display that data.

***

### Duration

[Section titled “Duration”](#duration)

The duration value is calculated from the **total monitoring time and the duration of incidents**.

In simple terms: `uptime = (total time - incident duration) / total time`

This means uptime is based on how long something was down, not how many checks failed. Only incident durations are included in the calculation.

Temporary single-region ping failures (e.g., one location failing once, sometimes this just happens) are not propagated to users - because these often don’t represent a real outage. That’s also why we recommend at least three locations per monitor for redundancy.

The proportional colors in the status bar are drawn from these duration values. Hovering over a day shows both incidents and status reports, so users can explore what happened.

***

### Request

[Section titled “Request”](#request)

The request value is more straightforward - it looks at each ping result individually. **Every check we run contributes to your uptime score**.

In simple terms: `uptime = (success + degraded - error) / total requests`

This is the current default mode for most openstatus users. It’s simple, data-driven, and updates immediately as new results come in.

Like with duration, hover cards display incidents and status reports, giving your users a quick overview of recent events.

***

## Manual Type

[Section titled “Manual Type”](#manual-type)

The manual type is for teams who want to **fully control what’s shown** on your status page, without relying on automatic checks. By default, your monitor is marked operational. You can then manually create status reports whenever you want to reflect changes - independent of any monitoring data.

This is ideal if:

* you don’t have synthetic monitoring set up yet,
* or you’re sharing updates that aren’t tied to uptime (e.g., service degradation due to external dependencies).

In this mode, all displayed uptime values and statuses come from your shared report data, not from active pings.

In simple terms: `uptime = (total duration - status report duration) / total duration`

> **Note**: the values you are defining are attached to a status page. You cannot change them per monitor (for now).

# Understanding Uptime Monitoring

> A deep dive into uptime monitoring concepts, architecture, and best practices

## What is uptime monitoring?

[Section titled “What is uptime monitoring?”](#what-is-uptime-monitoring)

Uptime monitoring is the practice of continuously asking a simple question: “Is our service working correctly for our users?” It’s a systematic, automated process for checking the availability, performance, and correctness of a website, server, or application.

Instead of waiting for users to report a problem, uptime monitoring acts as a proactive defense, alerting you the moment an issue arises. This helps you minimize downtime and protect your reputation.

At its core, uptime monitoring answers three critical questions:

1. **Is my service available?** Can users reach it?
2. **Is it performing well?** Are response times fast enough?
3. **Is it functioning correctly?** Is it returning the expected data and behaving as intended?

```plaintext
+----------------+
| Service to be  |
| Monitored      |
+----------------+
      ▲
      |
      |   (Network Latency)
      |
+-----+-------+   +-----+-------+   +-----+-------+
| Monitoring  |   | Monitoring  |   | Monitoring  |
| Node (USA)  |   | Node (EU)   |   | Node (Asia) |
+-----+-------+   +-----+-------+   +-----+-------+
      |               |                 |
      |---------------|-----------------|
      ▼               ▼                 ▼
+------------------------------------------------+
|       Global Uptime Monitoring Service         |
|                                                |
| - Sends automated requests (e.g., pings or     |
|   HTTP checks) from all nodes at set intervals |
| - Records response time and success/failure    |
| - Compares results from different nodes        |
| - If a failure or a slow response is detected, |
|   it triggers an alert.                        |
+------------------------------------------------+
      |
      | (Alerts: Email, SMS, Slack, etc.) 🔔
      |
+-----+-----+
| Your Team |
+-----------+
```

## Key Concepts

[Section titled “Key Concepts”](#key-concepts)

* **Downtime**: The period when a service is unavailable or not functioning as expected. It can be caused by server failures, network issues, software bugs, or even cyberattacks.

* **Uptime**: The percentage of time a service is available and operational. A high uptime percentage (e.g., 99.9% or “three nines”) indicates reliability.

* **Alerting**: The system of notifying a team or individual when downtime is detected. Alerts can be sent via email, SMS, Slack, or other communication channels.

## Why Uptime Monitoring is Crucial

[Section titled “Why Uptime Monitoring is Crucial”](#why-uptime-monitoring-is-crucial)

* **Business Continuity**: Downtime can lead to significant financial losses, damage to reputation, and loss of customer trust. Uptime monitoring helps you address issues quickly, ensuring your services are always available to your users.

* **Performance Insight**: Monitoring tools often provide data on latency and response times, giving you insights into your service’s performance beyond just availability. This can help you optimize your infrastructure and user experience.

* **Proactive Problem Solving**: Instead of waiting for a customer to report an issue, uptime monitoring allows you to be the first to know about it. This enables you to troubleshoot and resolve problems before they escalate.

## How it Works

[Section titled “How it Works”](#how-it-works)

Uptime monitoring typically involves a monitoring agent that periodically sends a request (like an HTTP GET request) to your service.

* If the service responds with a successful status code (e.g., 200 OK), it’s considered up.

* If the service returns an error code, a timeout, or no response, the agent will perform a re-check from a different location to confirm the outage. This helps prevent false alarms caused by temporary network glitches.

* Upon confirmation, the system triggers an alert, notifying the relevant team members. The monitoring system will continue to check the service until it’s back online, at which point a recovery alert is often sent.

Common types of checks include:

* **HTTP/HTTPS checks:** Verify a website is accessible and returns a valid response.
* **TCP checks:** Confirm a server is reachable on the network.

## Planning an Uptime Monitoring System

[Section titled “Planning an Uptime Monitoring System”](#planning-an-uptime-monitoring-system)

When planning your own uptime monitoring system, consider the following:

1. Define What to Monitor: Identify all critical services, websites, APIs, and servers that need to be monitored. Prioritize based on business impact.

2. Select a Monitoring Tool: Choose a tool that fits your needs. Options range from simple free services to complex enterprise-level platforms. Look for features like:

   * **Multiple locations:** Checks from various geographic regions to ensure global availability.

   * **Customizable alerting:** Set up different alert thresholds and notification methods.

   * **Reporting and dashboards:** Visualize uptime history, performance metrics, and incident reports.

   * **Integrations:** Connect with your existing tools like Slack, PagerDuty, or email.

3. **Establish Alerting Rules:** Determine who should be notified and when. Set up an escalation policy, for example, if a primary on-call engineer doesn’t respond within 15 minutes, the alert is sent to a manager.

4. **Regularly Review and Optimize:** Monitor your monitoring system itself. Review historical data to identify recurring issues, fine-tune alert thresholds, and update your list of monitored services as your infrastructure evolves.

## The human factor

[Section titled “The human factor”](#the-human-factor)

While uptime monitoring is largely automated, it’s important to remember the human aspects:

* **Alert fatigue**: Too many false positives can lead teams to ignore alerts. Fine-tune your monitoring to reduce noise.
* **On-call burden**: Distribute monitoring responsibilities fairly and ensure adequate coverage.
* **Communication**: During incidents, clear communication with users is as important as technical fixes.
* **Post-mortems**: Learn from downtime by conducting blameless post-mortems.

## Monitoring philosophy

[Section titled “Monitoring philosophy”](#monitoring-philosophy)

Different approaches to monitoring reflect different philosophies:

* **Optimistic monitoring**: Assume everything is working unless proven otherwise. Alert on failures.
* **Pessimistic monitoring**: Assume nothing works unless actively verified. Alert on missing data.
* **SLI/SLO based**: Monitor Service Level Indicators against defined Service Level Objectives.

openstatus supports all these approaches, letting you choose what works best for your team.

## Beyond basic availability

[Section titled “Beyond basic availability”](#beyond-basic-availability)

Modern uptime monitoring goes beyond simple “up or down” checks:

* **Performance monitoring**: Track response times and identify degradation before outages.
* **Geographic monitoring**: Verify availability from multiple regions to catch regional issues.
* **Synthetic monitoring**: Simulate user journeys to catch functional issues.
* **Real user monitoring (RUM)**: Complement synthetic checks with actual user experience data.

## Next steps

[Section titled “Next steps”](#next-steps)

Now that you understand uptime monitoring concepts:

* **[Get started with a monitor](/tutorial/how-to-create-monitor)** - Apply these concepts in practice
* **[Learn about uptime calculations](/concept/uptime-calculation-and-values)** - Understand how uptime percentages work
* **[Building Trust with Status Pages](/concept/best-practices-status-page)** - Communicate effectively during incidents
* **[Monitoring as Code](/concept/uptime-monitoring-as-code)** - Manage monitoring configuration programmatically

# Understanding Monitoring as Code

> Why and how to manage monitoring configuration as code for GitOps workflows

## The traditional approach (and its problems)

[Section titled “The traditional approach (and its problems)”](#the-traditional-approach-and-its-problems)

Traditionally, monitoring is configured through web dashboards:

1. Log into a web interface
2. Click through forms to create monitors
3. Manually replicate configuration across environments
4. No audit trail of who changed what
5. Difficult to review changes before they go live

This works for small teams with few monitors, but doesn’t scale.

## What is monitoring as code?

[Section titled “What is monitoring as code?”](#what-is-monitoring-as-code)

**Monitoring as Code** treats your monitoring configuration the same way you treat your application code: as text files that can be versioned, reviewed, and deployed through automated pipelines.

Instead of clicking buttons, you define monitors in YAML:

Uptime monitoring is a vital part of any robust system, ensuring your services are online and available to users. Historically, this has involved manually configuring monitors through a web interface, which can be tedious and prone to human error. Uptime Monitoring as Code changes this by treating your monitoring configurations like any other part of your application-as code.

## Why Use Uptime Monitoring as Code?

[Section titled “Why Use Uptime Monitoring as Code?”](#why-use-uptime-monitoring-as-code)

This approach offers significant advantages:

* **Version Control:** By defining your monitors in a YAML file, you can track every change, rollback to previous versions, and see who made which modifications using tools like Git. This is crucial for auditing and troubleshooting.

* **Automation and Consistency:** Your monitoring setup can be part of your automated deployment pipeline. When you deploy a new service, its monitors are created automatically, ensuring consistency across your entire infrastructure. This eliminates the risk of forgetting to set up monitoring for a new service.

* **Collaboration:** A code-based approach simplifies collaboration among teams. A developer can create a new monitor definition in the YAML file and submit it for peer review, just as they would with any other code change. This promotes a shared understanding of your system’s health.

* **Scalability:** Manually setting up hundreds of monitors is a nightmare. With a code-based approach, you can programmatically generate configurations for a large number of services, making it easy to scale your monitoring as your infrastructure grows.

* **Simplified Auditing:** Since the entire configuration is in a file, it’s easy to see the current state of your monitors at a glance. You don’t have to navigate through multiple screens in a web UI.

## How It Works with openstatus

[Section titled “How It Works with openstatus”](#how-it-works-with-openstatus)

We offer the use ofa simple, human-readable YAML file to define all uptime monitors. This file serves as the single source of truth for your monitoring setup. You define each monitor with its URL, expected status code, and other parameters.

Here’s an example of what your `openstatus.yaml` file might look like:

openstatus.yaml

```yaml
# yaml-language-server: $schema=https://www.openstatus.dev/schema.json
uptime-monitor:
  name: "Uptime Monitor"
  description: "Uptime monitoring example"
  frequency: "10m"
  active: true
  regions:
    - iad
    - ams
    - syd
    - jnb
    - gru
  retry: 3
  kind: http
  request:
    url: https://openstat.us
    method: GET
    headers:
      User-Agent: openstatus
  assertions:
    - kind: statusCode
      compare: eq
      target: 200


graphql-monitor:
  name: "Graphql"
  description: "GitHub GraphQL API"
  frequency: "10m"
  active: true
  regions:
    - iad
    - ams
    - syd
    - jnb
    - gru
  retry: 3
  kind: http
  request:
    url: https://api.github.com/graphql
    method: POST
    headers:
      User-Agent: openstatus
      Authorization: Bearer YOUR_TOKEN_HERE
    body: |
      {
        "query": "query { viewer { login }}"
      }
```

### Making Changes with the CLI

[Section titled “Making Changes with the CLI”](#making-changes-with-the-cli)

Once your `openstatus.yaml` file is ready, you use our [command-line interface (CLI)](/tutorial/get-started-with-openstatus-cli) to apply the changes. The CLI compares your local configuration with the current state of your monitors and applies only the necessary changes creating new monitors, updating existing ones, or deleting those no longer defined.

**Common CLI Commands:**

* `openstatus monitors apply`: Applies the changes defined in your `openstatus.yaml` file.
* `openstatus monitors import`: Import the monitors from your dashboard to a new `openstatus.yaml` file.

By integrating this **Uptime Monitoring as Code** workflow into your development lifecycle, you can achieve a more reliable, consistent, and scalable system. It’s about moving from manual clicks to automated, version-controlled operations.

## Best practices

[Section titled “Best practices”](#best-practices)

1. **Start simple**: Begin with a few monitors, expand as you learn
2. **Use templates**: Create reusable patterns for common monitor types
3. **Environment variables**: Use secrets management for tokens and sensitive data
4. **Review changes**: Always review diffs before applying
5. **Document decisions**: Use commit messages to explain “why”

## Next steps

[Section titled “Next steps”](#next-steps)

Ready to implement monitoring as code?

* **[Get Started with CLI](/tutorial/get-started-with-openstatus-cli)** - Install and configure the CLI
* **[Monitor Your MCP Server](/guides/how-to-monitor-mcp-server/)** - Real-world example
* **[CLI Reference](/reference/cli-reference)** - Complete command documentation
* **[YAML Examples](https://github.com/openstatusHQ/cli-template)** - Sample configurations

# How-to Guides

> Practical guides for integrating OpenStatus with GitHub Actions, OTLP endpoints, Cloudflare, and more.

## 🛠️ How-to Guides

[Section titled “🛠️ How-to Guides”](#️-how-to-guides)

### What you’ll find here

[Section titled “What you’ll find here”](#what-youll-find-here)

Our how-to guides are designed to help you:

* Solve specific problems with step-by-step instructions
* Implement advanced features and integrations
* Customize and extend your openstatus setup

### Monitoring & Integration

[Section titled “Monitoring & Integration”](#monitoring--integration)

Extend your monitoring capabilities:

* **[Monitor Your MCP Server](/guides/how-to-monitor-mcp-server/)** - Set up monitoring for Model Context Protocol servers
* **[Export Metrics to OTLP Endpoint](/guides/how-to-export-metrics-to-otlp-endpoint)** - Send monitoring data to your observability platform
* **[Run Synthetic Tests in GitHub Actions](/guides/how-to-run-synthetic-test-github-action/)** - Automate testing in your CI/CD pipeline

### Status Pages & Widgets

[Section titled “Status Pages & Widgets”](#status-pages--widgets)

Share your status with users:

* **[Add SVG Status Badge to GitHub README](/guides/how-to-add-svg-status-badge)** - Display real-time status in your repository
* **[Use React Status Widget](/guides/how-to-use-react-widget)** - Embed live status updates in your React application
* **[Deploy Status Page on Cloudflare Pages](/guides/how-deploy-status-page-cf-pages)** - Host your status page on Cloudflare’s edge network

### Infrastructure & Deployment

[Section titled “Infrastructure & Deployment”](#infrastructure--deployment)

Self-host and customize your setup:

* **[Deploy Private Locations on Cloudflare Containers](/guides/how-to-deploy-probes-cloudflare-containers)** - Run monitoring agents in your own infrastructure
* **[Self-Host openstatus](/guides/self-hosting-openstatus)** - Deploy openstatus on your own servers
* **[Self-Host Status Page Only](/guides/self-host-status-page-only)** - Deploy only the status page without monitoring

### Related sections

[Section titled “Related sections”](#related-sections)

* **[Tutorials](/tutorial/getting-started/)** - If you need step-by-step learning instead
* **[Explanations](/concept/getting-started/)** - To understand the concepts behind these guides
* **[Reference](/reference)** - For detailed technical specifications

# How to Deploy a Status Page to Cloudflare Pages

> Learn how to use openstatus monitoring data to deploy a status page on Cloudflare Pages.

## Problem

[Section titled “Problem”](#problem)

You need a fast, reliable, and automated status page, but you don’t want to manage the hosting infrastructure. Manually updating a status page during an incident is inefficient and error-prone.

## Solution

[Section titled “Solution”](#solution)

Deploy a custom status page to Cloudflare’s global edge network using openstatus as the data source. This guide shows you how to use our Astro-based template to create a status page that automatically reflects your monitoring data.

The code for the template is available on [GitHub](https://github.com/openstatusHQ/astro-status-page).

![Astro Status Page](/_astro/status-page.zwzKuYfz_joNjj.webp)

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A Cloudflare account
* An [openstatus account](https://www.openstatus.dev) with at least one monitor configured.

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### 1. Get your openstatus API key

[Section titled “1. Get your openstatus API key”](#1-get-your-openstatus-api-key)

First, you need an API key to fetch your monitoring data.

1. Navigate to your openstatus dashboard.
2. Go to **Settings** → **API Token**.
3. Click **Create API Key** and copy the key.

### 2. Set up the Astro project

[Section titled “2. Set up the Astro project”](#2-set-up-the-astro-project)

Clone our status page template and install the dependencies.

```bash
git clone https://github.com/openstatusHQ/astro-status-page.git
cd astro-status-page
npm install
```

### 3. Customize the status page

[Section titled “3. Customize the status page”](#3-customize-the-status-page)

You need to specify which monitors to display on your page.

1. Open the `src/pages/index.astro` file.

2. Find the following line of code:

   ```javascript
   const monitorIds = [1]
   ```

3. Replace the `1` with the ID of the monitor you want to display. You can find the monitor ID in the URL when you view a monitor in the openstatus dashboard (`/monitors/[ID]`). You can also add multiple IDs: `[1, 2, 5]`.

### 4. Configure your Cloudflare environment variable

[Section titled “4. Configure your Cloudflare environment variable”](#4-configure-your-cloudflare-environment-variable)

Before deploying, you must provide your openstatus API key to Cloudflare.

1. Go to your Cloudflare dashboard and click on **Workers & Pages**.

2. Select your site and go to the **Settings** tab.

3. Navigate to **Environment variables** and add a new variable:

   * **Variable name**: `API_KEY`
   * **Value**: Paste your openstatus API key here.

### 5. Deploy to Cloudflare Pages

[Section titled “5. Deploy to Cloudflare Pages”](#5-deploy-to-cloudflare-pages)

Now you can deploy your status page.

```bash
npm run pages:deploy
```

After the command completes, your status page will be live on Cloudflare Pages. 🎉

# How to Add a Status Badge to a GitHub README

> A step-by-step guide to adding a real-time SVG or PNG status badge to your GitHub repository.

## Problem

[Section titled “Problem”](#problem)

You want to display the real-time status of your service directly in your GitHub repository’s README file. This provides immediate visibility to your users and team members about the health of your application.

## Solution

[Section titled “Solution”](#solution)

openstatus provides embeddable status badges that you can add to any Markdown file, including your `README.md`. You can choose between a modern SVG badge or a legacy PNG badge.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An openstatus account with a configured status page.
* The “slug” of your status page (the unique name in its URL, e.g., `https://[slug].openstatus.dev`).

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### Step 1: Choose your badge type

[Section titled “Step 1: Choose your badge type”](#step-1-choose-your-badge-type)

We recommend using the modern SVG badge (v2) as it offers more customization options.

* **SVG Badge (v2)**: More flexible, better styling, and uses a monospaced font.
* **PNG Badge (Legacy)**: Simpler, but with fewer customization options.

### Step 2: Add the badge to your README

[Section titled “Step 2: Add the badge to your README”](#step-2-add-the-badge-to-your-readme)

Copy the Markdown snippet for your chosen badge type and paste it into your `README.md` file. **Remember to replace `[slug]` with your status page slug.**

***

#### Option A: Modern SVG Badge (Recommended)

[Section titled “Option A: Modern SVG Badge (Recommended)”](#option-a-modern-svg-badge-recommended)

This is the recommended badge for most use cases.

##### Base URL

[Section titled “Base URL”](#base-url)

```plaintext
https://[slug].openstatus.dev/badge/v2
```

##### Markdown Snippet

[Section titled “Markdown Snippet”](#markdown-snippet)

```plaintext
![Status](https://[slug].openstatus.dev/badge/v2)
```

**Example:**

![Status](https://status.openstatus.dev/badge/v2)

##### Customization

[Section titled “Customization”](#customization)

You can customize the badge by adding query parameters to the URL.

* **Theme**: `?theme=dark` (default is `light`)
* **Size**: `?size=md` (options: `sm`, `md`, `lg`, `xl`; default is `sm`)
* **Variant**: `?variant=outline` (adds a border; default has no border)

**Example with all options:**

```plaintext
![Status](https://[slug].openstatus.dev/badge/v2?theme=dark&size=lg&variant=outline)
```

***

#### Option B: Legacy PNG Badge

[Section titled “Option B: Legacy PNG Badge”](#option-b-legacy-png-badge)

Use this badge if you prefer the older style.

##### Base URL

[Section titled “Base URL”](#base-url-1)

```plaintext
https://[slug].openstatus.dev/badge
```

##### Markdown Snippet

[Section titled “Markdown Snippet”](#markdown-snippet-1)

```markdown
![Status](https://[slug].openstatus.dev/badge)
```

**Example:**

![Status](https://status.openstatus.dev/badge)

##### Customization

[Section titled “Customization”](#customization-1)

* **Theme**: `?theme=dark` (default is `light`)
* **Size**: `?size=lg` (options: `sm`, `md`, `lg`, `xl`; default is `sm`)

**Example with all options:**

```plaintext
![Status](https://[slug].openstatus.dev/badge?theme=dark&size=lg)
```

### Step 3: Commit your changes

[Section titled “Step 3: Commit your changes”](#step-3-commit-your-changes)

Save your `README.md` file and commit it to your repository. The status badge will now be visible to anyone visiting your repository. It will automatically update to reflect the current status of your services.

# How to Deploy a Private Probe on Cloudflare Containers

> A step-by-step guide to deploying an openstatus private monitoring probe on Cloudflare Containers.

## Problem

[Section titled “Problem”](#problem)

You need to monitor internal services that are not accessible from the public internet, or you want to run checks from your own infrastructure for compliance or performance reasons. You need a lightweight, serverless way to run these monitoring probes without managing virtual machines.

## Solution

[Section titled “Solution”](#solution)

Deploy the openstatus private location probe as a serverless container using Cloudflare Containers. This allows you to run monitoring checks from within your own network infrastructure, managed by Cloudflare. This guide will walk you through the entire process, from creating the private location in openstatus to deploying the container.

The code for the Cloudflare Worker template is available on [GitHub](https://github.com/openstatusHQ/private-location-cloudflare-container).

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A Cloudflare account
* An [openstatus account](https://www.openstatus.dev)
* `pnpm` and `docker` installed on your local machine

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### 1. Create a private location in openstatus

[Section titled “1. Create a private location in openstatus”](#1-create-a-private-location-in-openstatus)

First, you need to create a private location in your openstatus workspace to get an access key.

1. Go to the openstatus dashboard.
2. Click on **Private locations** in the sidebar.
3. Click **Create Private Location**.
4. Give it a human-readable name (e.g., “Cloudflare-EU”).
5. Copy the generated token and save it somewhere secure.
6. Click **Submit** to save the new private location.

### 2. Set up the Cloudflare project

[Section titled “2. Set up the Cloudflare project”](#2-set-up-the-cloudflare-project)

Next, create a new Cloudflare project using the containers template.

```bash
pnpm create cloudflare@latest --template=cloudflare/templates/containers-template
```

### 3. Pull and tag the probe Docker image

[Section titled “3. Pull and tag the probe Docker image”](#3-pull-and-tag-the-probe-docker-image)

Pull the official openstatus private location image from Docker Hub. You must specify the `linux/amd64` platform, as this is what Cloudflare Containers supports.

```bash
# Pull the image
docker pull --platform linux/amd64 ghcr.io/openstatushq/private-location:latest


# Tag the image for Cloudflare (you cannot use the 'latest' tag)
docker tag ghcr.io/openstatushq/private-location:latest openstatus-private-location:v1
```

### 4. Push the image to Cloudflare Container Registry

[Section titled “4. Push the image to Cloudflare Container Registry”](#4-push-the-image-to-cloudflare-container-registry)

Push the tagged image to your Cloudflare account’s container registry.

```bash
pnpm wrangler containers push openstatus-private-location:v1
```

### 5. Configure `wrangler.toml`

[Section titled “5. Configure wrangler.toml”](#5-configure-wranglertoml)

Now, configure your Cloudflare project to use the container and run it on a schedule.

1. Open the `wrangler.toml` file.

2. Add a `[containers]` section to link the image you pushed. Replace `GENERATED_ID` with the actual ID from the previous step’s output.

   ```toml
   [containers]
   image = "registry.cloudflare.com/GENERATED_ID/openstatus-private-location:v1"
   ```

3. Add a `triggers` section to run the worker on a cron schedule. This keeps the container alive, as Cloudflare Containers automatically scales to zero.

   ```toml
   triggers = { cron = ["*/2 * * * *"] } # Runs every 2 minutes
   ```

### 6. Configure the worker

[Section titled “6. Configure the worker”](#6-configure-the-worker)

Update the worker script (`index.ts`) to start the container with the correct environment variables.

1. Set the `sleepAfter` value to control how long the container runs after being invoked.

   ```typescript
   sleepAfter = "150s";
   ```

2. Update the `scheduled` function to pass your openstatus key to the container.

   ```typescript
   async scheduled(_controller: any, env: Env) {
     try {
       const container = getContainer(env.MY_CONTAINER);
       await container.start({
         envVars: {
           OPENSTATUS_KEY: env.OPENSTATUS_KEY,
         },
       });
     } catch (e) {
       console.error("Error in scheduled task:", e);
     }


     return new Response("ok");
   },
   ```

### 7. Add your openstatus key as a secret

[Section titled “7. Add your openstatus key as a secret”](#7-add-your-openstatus-key-as-a-secret)

Securely provide your private location token to the Cloudflare worker.

```bash
# Paste the token you saved in Step 1 when prompted
pnpm wrangler secret put OPENSTATUS_KEY
```

### 8. Deploy the application

[Section titled “8. Deploy the application”](#8-deploy-the-application)

Finally, deploy the worker and container to Cloudflare.

```bash
pnpm wrangler deploy
```

Your private location probe is now running on Cloudflare Containers and will start picking up monitoring jobs from your openstatus workspace.

## Verify the deployment

[Section titled “Verify the deployment”](#verify-the-deployment)

You can check the logs of your Cloudflare Worker to see the probe in action. In your openstatus dashboard, the private location should now show as connected.

![Cloudflare Workers Logs showing openstatus Private Location running](/_astro/cloudflare-log.b7TJfsDP_2cgtRQ.webp) ![openstatus Private Location connected](/_astro/private-location.FbLeUNWm_23kgwk.webp)

# How to Export Metrics to an OTLP Endpoint

> A step-by-step guide to sending openstatus metrics to your observability platform via OTLP.

## Problem

[Section titled “Problem”](#problem)

You want to analyze your openstatus monitoring data alongside other telemetry data in your existing observability platform (like Grafana, New Relic, or Honeycomb). You need a standardized way to export these metrics without building a custom integration.

## Solution

[Section titled “Solution”](#solution)

openstatus can export monitoring metrics to any OTLP (OpenTelemetry Protocol) compatible endpoint. By adding a simple configuration to your `openstatus.yaml` file, you can have metrics from every check sent directly to your monitoring stack.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An observability platform that supports OTLP metric ingestion over HTTP.
* An `openstatus.yaml` file to configure your monitors.
* The [openstatus CLI](/tutorial/get-started-with-openstatus-cli) to apply your configuration.

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### 1. Locate your OTLP endpoint URL and headers

[Section titled “1. Locate your OTLP endpoint URL and headers”](#1-locate-your-otlp-endpoint-url-and-headers)

First, you need to find the specific URL and any required authentication headers from your observability platform. This is usually found in the documentation under “OTLP,” “OpenTelemetry,” or “Metrics Export.”

* **Endpoint URL**: Look for an HTTP endpoint for OTLP metrics. It will typically end in `/v1/metrics`. For example: `https://otlp.your-provider.com/v1/metrics`.
* **Headers**: You will likely need an authentication header, such as `Authorization: Bearer YOUR_API_KEY` or `X-API-Key: YOUR_API_KEY`.

### 2. Configure your `openstatus.yaml` file

[Section titled “2. Configure your openstatus.yaml file”](#2-configure-your-openstatusyaml-file)

Open your `openstatus.yaml` file and add the `openTelemetry` block at the top level.

```yaml
# yaml-language-server: $schema=https://www.openstatus.dev/schema.json


openTelemetry:
  endpoint: <YOUR_OTLP_ENDPOINT_URL>
  headers:
    Authorization: Bearer <YOUR_TOKEN>
    # Add any other required headers here


# Your monitors are defined below
my-first-monitor:
  # ...
```

Replace `<YOUR_OTLP_ENDPOINT_URL>` and `<YOUR_TOKEN>` with the values you found in step 1.

**Note**: Currently, we only support OTLP over HTTP.

### 3. Apply the configuration

[Section titled “3. Apply the configuration”](#3-apply-the-configuration)

Use the openstatus CLI to apply the changes to your account.

```bash
openstatus apply
```

After applying the configuration, openstatus will send metrics to your specified endpoint after every check is completed.

### 4. Verify in your observability platform

[Section titled “4. Verify in your observability platform”](#4-verify-in-your-observability-platform)

Go to your observability platform and look for the new metrics coming from openstatus. You should be able to build dashboards and alerts based on this data.

Here are some examples of what it can look like:

#### Grafana

[Section titled “Grafana”](#grafana)

![openstatus metrics in grafana](/_astro/grafana.geHk6gGv_29QwSY.webp)

#### Honeycomb

[Section titled “Honeycomb”](#honeycomb)

![openstatus metrics in honeycomb](/_astro/honeycomb.B46bTQYB_1gqk2P.webp)

#### New Relic

[Section titled “New Relic”](#new-relic)

![openstatus metrics in new-relic](/_astro/newrelic.W685D2N9_ZAwqvT.webp)

#### SigNoz

[Section titled “SigNoz”](#signoz)

![openstatus metrics in signoz](/_astro/signoz.2LNt7nwP_FuEeB.webp)

# How to Monitor Your Model Context Provider (MCP) Server

> Learn how to monitor your MCP server with openstatus using JSON-RPC ping checks

## Problem: Ensuring Your MCP Server is Always Responsive

[Section titled “Problem: Ensuring Your MCP Server is Always Responsive”](#problem-ensuring-your-mcp-server-is-always-responsive)

Running a Model Context Provider (MCP) server is critical for your AI applications, but traditional HTTP monitoring often falls short. MCP servers communicate using the JSON-RPC 2.0 protocol, requiring specific request/response patterns that standard health checks don’t cover. How can you confidently ensure your MCP server is healthy and responsive at all times, without custom scripts or complex setups?

## Solution: JSON-RPC Ping Monitoring with openstatus

[Section titled “Solution: JSON-RPC Ping Monitoring with openstatus”](#solution-json-rpc-ping-monitoring-with-openstatus)

openstatus offers a robust solution for monitoring your MCP servers. By sending precise JSON-RPC `ping` requests to your endpoint from multiple global locations, openstatus verifies not only network reachability but also the correct functioning of your server’s JSON-RPC interface. This guide will walk you through setting up comprehensive monitoring for any MCP server using the openstatus CLI.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

Before you begin, ensure you have:

* An [openstatus account](https://www.openstatus.dev/app/login).
* The [openstatus CLI installed](/tutorial/get-started-with-openstatus-cli). (If you haven’t installed it yet, follow this guide first).
* An MCP server with a publicly accessible endpoint.
* A basic understanding of the [JSON-RPC 2.0 protocol](https://www.jsonrpc.org/specification).

## Background: Understanding MCP for Monitoring

[Section titled “Background: Understanding MCP for Monitoring”](#background-understanding-mcp-for-monitoring)

A Model Context Provider (MCP) is a crucial component that extends AI models with external context, data, or capabilities via the **Model Context Protocol (MCP)**. Essentially, it acts as a bridge, allowing AI models to interact with resources like databases, APIs, or file systems that aren’t part of their core training.

### The MCP Server and JSON-RPC 2.0

[Section titled “The MCP Server and JSON-RPC 2.0”](#the-mcp-server-and-json-rpc-20)

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### 1. Create your `openstatus.yaml` file

[Section titled “1. Create your openstatus.yaml file”](#1-create-your-openstatusyaml-file)

openstatus allows you to define and manage your monitors using a YAML configuration file, which is ideal for GitOps workflows. This approach ensures your monitoring setup is version-controlled, auditable, and easily deployable.

Create a file named `openstatus.yaml` and add the following configuration, adapting it for your own MCP endpoint. This example targets a Hugging Face MCP server.

```yaml
# yaml-language-server: $schema=https://www.openstatus.dev/schema.json


mcp-server:
  name: "HF MCP Server"
  description: "Hugging Face MCP server monitoring"
  frequency: "1m"
  active: true
  regions: ["iad", "ams", "lax"]
  retry: 3
  kind: http
  request:
    url: https://hf.co/mcp
    method: POST
    body: >
      {
        "jsonrpc": "2.0",
        "id": "openstatus",
        "method": "ping"
      }
    headers:
      User-Agent: openstatus
      Accept: application/json, text/event-stream
      Content-Type: application/json
  assertions:
    - kind: statusCode
      compare: eq
      target: 200
    - kind: textBody
      compare: eq
      target: '{"result":{},"jsonrpc":"2.0","id":"openstatus"}'
```

### 2. Understand the configuration

[Section titled “2. Understand the configuration”](#2-understand-the-configuration)

Let’s break down the key fields in this YAML configuration:

* `name` & `description`: A human-readable name and explanation for your monitor.

* `frequency`: How often openstatus will run the check (e.g., `1m`, `5m`, `10m`).

* `regions`: An array of geographic regions from which to perform checks (e.g., `["iad", "ams", "lax"]`). Monitoring from multiple regions helps detect localized issues.

* `retry`: The number of times to retry a failed check before marking it as down.

* `kind`: Must be `http` for MCP servers.

* `request`:

  * `url`: The full URL of your MCP server’s JSON-RPC endpoint.
  * `method`: Must be `POST` for JSON-RPC requests.
  * `body`: The JSON-RPC `ping` request payload.
  * `headers`: Standard HTTP headers for JSON-RPC communication.

* `assertions`: Rules to validate the server’s response.

  * `statusCode`: Ensures the HTTP response is `200 OK`.
  * `textBody`: Verifies that the response payload exactly matches the expected JSON-RPC `ping` result.

### 3. Test your MCP server (Optional)

[Section titled “3. Test your MCP server (Optional)”](#3-test-your-mcp-server-optional)

Before deploying your monitor, you can manually test your MCP server’s `ping` endpoint with `curl` to confirm it responds as expected. This helps verify the `target` value for your `textBody` assertion.

```bash
curl -X POST \\
  -H "Content-Type: application/json" \\
  -d '{"jsonrpc": "2.0", "id": "openstatus", "method": "ping"}' \\
  https://hf.co/mcp # Replace with your MCP server URL
```

A healthy server should return a JSON response like `{"result":{},"jsonrpc":"2.0","id":"openstatus"}`.

### 4. Deploy your monitor

[Section titled “4. Deploy your monitor”](#4-deploy-your-monitor)

Once your `openstatus.yaml` file is ready, use the openstatus CLI to create the monitor:

```bash
openstatus create openstatus.yaml
```

This command uploads your configuration, and monitoring will begin immediately.

## Conclusion: Comprehensive MCP Server Monitoring Achieved

[Section titled “Conclusion: Comprehensive MCP Server Monitoring Achieved”](#conclusion-comprehensive-mcp-server-monitoring-achieved)

This guide has equipped you with the knowledge to effectively monitor your MCP server using openstatus. By leveraging YAML configuration and the openstatus CLI, you can ensure your critical AI infrastructure remains healthy and responsive.

## What You’ve Accomplished

[Section titled “What You’ve Accomplished”](#what-youve-accomplished)

* ✅ Successfully configured a JSON-RPC based monitor for your MCP server.
* ✅ Implemented precise assertions to validate `ping` responses.
* ✅ Set up global monitoring to detect localized or widespread issues.
* ✅ Automated monitor deployment using a version-controlled YAML configuration.

## Next Steps

[Section titled “Next Steps”](#next-steps)

Now that your MCP server is under robust monitoring, consider further enhancing your setup:

* **[Export Metrics to OTLP](/guides/how-to-export-metrics-to-otlp-endpoint)**: Integrate your MCP monitoring data with your existing observability platform for centralized analytics.
* **[Run Synthetic Tests in GitHub Actions](/guides/how-to-run-synthetic-test-github-action/)**: Incorporate these synthetic checks into your CI/CD pipeline for pre-deployment validation.

## Related Resources

[Section titled “Related Resources”](#related-resources)

* **[JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)**: Deep dive into the JSON-RPC protocol.
* **[MCP Official Documentation](https://modelcontextprotocol.io/docs/concepts/architecture#debugging-and-monitoring)**: Official insights into MCP health checks.
* **[HTTP Monitor Reference](/reference/http-monitor)**: Comprehensive API reference for HTTP monitors.
* **[CLI Reference](/reference/cli-reference)**: Full documentation for the openstatus CLI.

# How to Run Synthetic Tests in GitHub Actions

> Integrate openstatus synthetic monitoring into your CI/CD pipeline

## Problem

[Section titled “Problem”](#problem)

You want to validate that your application’s critical endpoints are working before deploying to production. Running synthetic tests in your CI/CD pipeline catches issues early and prevents broken deployments.

## Solution

[Section titled “Solution”](#solution)

openstatus provides a GitHub Action that runs your configured monitors as part of your CI/CD workflow. This guide shows you how to set it up.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An [openstatus](https://www.openstatus.dev) account
* A GitHub repository
* At least one monitor configured in openstatus
* Admin access to your GitHub repository (for secrets)

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### 1. Create a configuration file

[Section titled “1. Create a configuration file”](#1-create-a-configuration-file)

Create a file named `openstatus.config.yaml` in your repository root:

```yaml
tests:
  ids:
    - 1
    - 2
```

**Finding monitor IDs:**

1. Go to your openstatus dashboard
2. Click on a monitor
3. The ID is in the URL: `https://www.openstatus.dev/app/[workspace]/monitors/[ID]`

**Tip:** Start with your most critical monitors and expand from there.

### 2. Get your openstatus API key

[Section titled “2. Get your openstatus API key”](#2-get-your-openstatus-api-key)

1. Go to your openstatus workspace settings
2. Navigate to the API section
3. Create a new API key or copy an existing one
4. Store it securely - you’ll need it for the next step

### 3. Add your API key to GitHub Secrets

[Section titled “3. Add your API key to GitHub Secrets”](#3-add-your-api-key-to-github-secrets)

Secure your API key as a GitHub secret:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `OPENSTATUS_API_KEY`
5. Value: Your openstatus API key
6. Click **Add secret**

### 4. Create the GitHub Action workflow

[Section titled “4. Create the GitHub Action workflow”](#4-create-the-github-action-workflow)

Create `.github/workflows/openstatus.yml`:

```yaml
name: Run openstatus Synthetics CI


on:
  workflow_dispatch:  # Manual trigger
  push:
    branches: [ main ]  # Trigger on push to main
  pull_request:        # Run on PRs (optional)


jobs:
  synthetic_ci:
    runs-on: ubuntu-latest
    name: Run openstatus Synthetics CI
    steps:
      - name: Checkout
        uses: actions/checkout@v4


      - name: Run openstatus Synthetics CI
        uses: openstatushq/openstatus-github-action@v1
        with:
          api_key: ${{ secrets.OPENSTATUS_API_KEY }}
```

### 5. Commit and push

[Section titled “5. Commit and push”](#5-commit-and-push)

```bash
git add openstatus.config.yaml .github/workflows/openstatus.yml
git commit -m "Add openstatus synthetic tests to CI"
git push origin main
```

The GitHub Action will run automatically on the next push to `main`.

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Great work! You’ve successfully:

* ✅ Integrated openstatus into your CI/CD pipeline
* ✅ Automated synthetic testing on every deployment
* ✅ Added a safety check before production releases
* ✅ Set up continuous validation of critical endpoints

## Customization options

[Section titled “Customization options”](#customization-options)

### Run on different branches

[Section titled “Run on different branches”](#run-on-different-branches)

```yaml
on:
  push:
    branches: [ main, staging, develop ]
```

### Run on pull requests

[Section titled “Run on pull requests”](#run-on-pull-requests)

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
```

### Run on a schedule

[Section titled “Run on a schedule”](#run-on-a-schedule)

```yaml
on:
  schedule:
    - cron: '0 */4 * * *'  # Every 4 hours
```

### Multiple configuration files

[Section titled “Multiple configuration files”](#multiple-configuration-files)

```yaml
- name: Run openstatus Synthetics CI
  uses: openstatushq/openstatus-github-action@v1
  with:
    api_key: ${{ secrets.OPENSTATUS_API_KEY }}
    config_file: .openstatus/production.yaml
```

## Best practices

[Section titled “Best practices”](#best-practices)

1. **Start small**: Begin with 2-3 critical monitors
2. **Fail fast**: Run synthetic tests early in your pipeline
3. **Monitor the monitors**: Track your synthetic test success rate
4. **Environment-specific**: Use different monitors for staging vs production
5. **Document failures**: Investigate and document any CI failures

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Action fails with authentication error:**

* Verify `OPENSTATUS_API_KEY` secret is set correctly
* Check that your API key hasn’t expired

**Monitors not found:**

* Confirm monitor IDs are correct in `openstatus.config.yaml`
* Ensure monitors are active in your openstatus dashboard

**Tests timing out:**

* Check that your endpoints are accessible from GitHub’s runners
* Consider increasing timeouts in monitor configuration

## Next steps

[Section titled “Next steps”](#next-steps)

* **[Monitor Your MCP Server](/guides/how-to-monitor-mcp-server/)** - Advanced monitoring examples
* **[Monitoring as Code](/concept/uptime-monitoring-as-code)** - Manage monitors with YAML
* **[CLI Reference](/reference/cli-reference)** - Automate monitor management
* **[Export Metrics](/guides/how-to-export-metrics-to-otlp-endpoint)** - Send data to your observability platform

## Related resources

[Section titled “Related resources”](#related-resources)

* **[GitHub Action on Marketplace](https://github.com/marketplace/actions/openstatus-synthetics-ci)** - Official action
* **[Example Repository](https://github.com/openstatusHQ/github-action-example)** - Working examples
* **[Join Discord](https://www.openstatus.dev/discord)** - Get help from the community

# How to Use openstatus React Widget

Install the [npm](https://www.npmjs.com/package/@openstatus/react) package:

```bash
npm install @openstatus/react
```

## React Server Component

[Section titled “React Server Component”](#react-server-component)

```tsx
import { StatusWidget } from "@openstatus/react";


export function Page() {
  return <StatusWidget slug="status" />;
}
```

It will automatically attach the slug to the href to allow the user to open a new tab on click to `https://slug.openstatus.dev`. If you want to redirect him to a specific page, use the `href` property, like so:

```tsx
<StatusWidget slug="documenso" href="https://status.documenso.com" />
```

> `StatusWidget` is an **async function** and will only work with RSC. Using it within a dead simple React App will not work.

### Styling

[Section titled “Styling”](#styling)

#### With tailwindcss

[Section titled “With tailwindcss”](#with-tailwindcss)

tailwind.config.js

```ts
module.exports = {
  content: [
    "./app/**/*.{tsx,ts,mdx,md}",
    "./node_modules/@openstatus/react/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
```

#### Without tailwindcss

[Section titled “Without tailwindcss”](#without-tailwindcss)

app/layout.tsx

```tsx
import "@openstatus/react/dist/styles.css";
```

## Typed fetch function

[Section titled “Typed fetch function”](#typed-fetch-function)

```tsx
import { getStatus } from "@openstatus/react";


// React Server Component
async function CustomStatusWidget() {
  const res = await getStatus("slug");
  // ^StatusResponse = { status: Status }


  const { status } = res;
  // ^Status = "unknown" | "operational" | "degraded_performance" | "partial_outage" | "major_outage" | "under_maintenance" | "incident"


  return <div>{/* customize */}</div>;
}
```

# Self-Host the OpenStatus Status Page (Lightweight)

> Deploy only the openstatus status page and dashboard on your own infrastructure, without monitoring, analytics, or background services.

## Problem

[Section titled “Problem”](#problem)

You want a status page to communicate incidents and maintenance to your users, but you don’t need automated monitoring, analytics, or alerting. You may already have your own monitoring tools, or you simply want a lightweight way to manage your public-facing status page.

## Solution

[Section titled “Solution”](#solution)

OpenStatus provides a lightweight Docker Compose setup that runs only 4 services: a database, a one-shot migration runner, the dashboard, and the status page. This is ideal for teams who only want to self-host the status page without monitoring, or for teams that manage incidents manually using external monitoring tools.

## Lightweight vs Full

[Section titled “Lightweight vs Full”](#lightweight-vs-full)

The lightweight stack strips away all monitoring infrastructure. Here’s what each version includes:

| Feature                       | Full | Lightweight |
| ----------------------------- | ---- | ----------- |
| Status page                   | Yes  | Yes         |
| Dashboard                     | Yes  | Yes         |
| Database (libSQL)             | Yes  | Yes         |
| Automated monitoring          | Yes  | **No**      |
| Analytics & charts (Tinybird) | Yes  | **No**      |
| API server                    | Yes  | **No**      |
| Private location probes       | Yes  | **No**      |

If you need automated monitoring, follow the [full self-hosting guide](/guides/self-hosting-openstatus) instead.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Docker and Docker Compose installed
* Git installed
* Command line experience

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

### Part 1: Initial Setup and Service Launch

[Section titled “Part 1: Initial Setup and Service Launch”](#part-1-initial-setup-and-service-launch)

1. **Clone the Repository**

   Get the latest version of openstatus:

   ```bash
   git clone https://github.com/openstatushq/openstatus
   cd openstatus
   ```

2. **Configure Your Environment**

   Copy the example environment file. This is a simplified version of the full configuration, with only the variables relevant to the status page and dashboard.

   ```bash
   cp .env.docker-lightweight.example .env.docker
   ```

   Open `.env.docker` in a text editor. You **must** set values for the following variables:

   * `AUTH_SECRET` — required for authentication. Generate a value with:

     ```bash
     openssl rand -base64 32
     ```

   * `RESEND_API_KEY` — required for magic link login emails. Get a key from [resend.com](https://resend.com).

   Optionally, you can configure GitHub or Google OAuth providers by filling in the `AUTH_GITHUB_*` or `AUTH_GOOGLE_*` variables in the same file.

3. **Build and Start Services**

   Use Docker Compose to build and run all services in the background:

   ```bash
   docker compose -f docker-compose-lightweight.yaml up -d
   ```

   The first build takes several minutes as it compiles the Next.js applications. Subsequent starts are much faster.

   Check the status of the services:

   ```bash
   docker compose -f docker-compose-lightweight.yaml ps
   ```

   Wait until all services show as `healthy` before proceeding. The `db-migrate` service will show as exited — this is expected, as it runs once and stops.

### Part 2: Application Configuration

[Section titled “Part 2: Application Configuration”](#part-2-application-configuration)

4. **Access the Applications**

   * **Dashboard:** `http://localhost:3000`
   * **Status Page:** `http://localhost:3001`

   Log in to the dashboard using email authentication (magic link). This will create your account and workspace.

5. **Set Workspace Limits**

   Because this is a self-hosted instance, you need to manually set the feature limits for your workspace directly in the database. The following command updates the limits for the workspace with `id = 1`:

   ```bash
   curl -X POST http://localhost:8080/ -H "Content-Type: application/json" \
     -d '{"statements":["UPDATE workspace SET limits = '\''{\\"monitors\\":100,\\"periodicity\\":[\\"30s\\",\\"1m\\",\\"5m\\",\\"10m\\",\\"30m\\",\\"1h\\"],\\"multi-region\\":true,\\"data-retention\\":\\"24 months\\",\\"status-pages\\":20,\\"maintenance\\":true,\\"status-subscribers\\":true,\\"custom-domain\\":true,\\"password-protection\\":true,\\"white-label\\":true,\\"notifications\\":true,\\"sms\\":true,\\"pagerduty\\":true,\\"notification-channels\\":50,\\"members\\":\\"Unlimited\\",\\"audit-log\\":true,\\"private-locations\\":true}'\'' WHERE id = 1"]}'
   ```

   You can find your workspace ID by querying the database:

   ```bash
   curl -X POST http://localhost:8080/ -H "Content-Type: application/json" \
     -d '{"statements":["SELECT id, name FROM workspace"]}'
   ```

6. **Create Your Status Page**

   In the dashboard, create a new status page, add components for the services you want to display, and publish it. Your status page will be available at `http://localhost:3001`.

## Service architecture

[Section titled “Service architecture”](#service-architecture)

| Service     | Container              | Host Port | Purpose                                              |
| ----------- | ---------------------- | --------- | ---------------------------------------------------- |
| libsql      | openstatus-libsql      | 8080      | Database (HTTP API)                                  |
| db-migrate  | openstatus-db-migrate  | —         | One-shot database migration (exits after completion) |
| dashboard   | openstatus-dashboard   | 3000      | Admin interface                                      |
| status-page | openstatus-status-page | 3001      | Public status page                                   |

## Data persistence

[Section titled “Data persistence”](#data-persistence)

All application data is stored in the `openstatus-libsql-data` Docker volume.

* `docker compose down` **preserves** your data.
* `docker compose down -v` **destroys** the volume and all data.

For production use, back up this volume regularly.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Containers won’t start:** Check the logs for the failing service:

```bash
docker compose -f docker-compose-lightweight.yaml logs <service-name>
```

**Magic link emails not arriving:** Verify that `RESEND_API_KEY` is set correctly in `.env.docker`.

**Dashboard shows errors on first load:** The `db-migrate` service may still be running. Check its status:

```bash
docker compose -f docker-compose-lightweight.yaml ps
```

**Port conflicts:** If ports 3000, 3001, or 8080 are already in use on your machine, update the host port mappings in `docker-compose-lightweight.yaml`. For example, change `"3000:3000"` to `"4000:3000"` to use port 4000 instead.

## Next steps

[Section titled “Next steps”](#next-steps)

* **[Self-Host openstatus (Full)](/guides/self-hosting-openstatus)** — Add automated monitoring, analytics, and alerting
* **[Join our Discord](https://www.openstatus.dev/discord)** — Get help from the community

# How to Self-Host openstatus

> Complete guide to deploying openstatus on your own infrastructure

## Problem

[Section titled “Problem”](#problem)

You want to run openstatus on your own infrastructure instead of using the hosted service. This gives you full control over your data, customization options, and the ability to monitor internal services not accessible from the public internet.

## Solution

[Section titled “Solution”](#solution)

openstatus provides a Docker Compose setup that makes self-hosting straightforward. This guide walks you through deploying all necessary services and configuring your self-hosted instance.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Docker and Docker Compose installed
* Basic understanding of Docker and containerization
* Command line experience
* Git installed

## Known limitations

[Section titled “Known limitations”](#known-limitations)

Self-hosting openstatus currently has these constraints:

* It only works with private locations. You have to deploy our probes to the cloud provider of your choice.

## Step-by-step guide

[Section titled “Step-by-step guide”](#step-by-step-guide)

This guide is divided into three parts: launching the services, setting up the database and analytics, and configuring the application through the UI.

### Part 1: Initial Setup and Service Launch

[Section titled “Part 1: Initial Setup and Service Launch”](#part-1-initial-setup-and-service-launch)

1. **Clone the Repository**

   Get the latest version of openstatus:

   ```bash
   git clone https://github.com/openstatushq/openstatus
   cd openstatus
   ```

2. **Configure Your Environment**

   Copy the example environment file. This file will hold all your configuration variables.

   ```bash
   cp .env.docker.example .env.docker
   ```

   Open `.env.docker` in a text editor. At a minimum, you **must** set a value for `AUTH_SECRET` for authentication to work. For a complete setup, review the file for other variables like OAuth providers or email services.

3. **Build and Start Services**

   Use Docker Compose to build and run all openstatus services in the background.

   ```bash
   export DOCKER_BUILDKIT=1
   docker compose up -d
   ```

   You can check the status of the services with `docker compose ps`. It might take a few minutes for all services to be healthy.

### Part 2: Database and Analytics Setup

[Section titled “Part 2: Database and Analytics Setup”](#part-2-database-and-analytics-setup)

4. **Run Database Migrations**

   The database container starts with an empty database. You must run migrations to set up the required schema.

   ```bash
   # Make sure you are in the root of the openstatus project
   cd packages/db
   pnpm install
   pnpm migrate
   cd ../.. # Return to the project root
   ```

   If you do not have or want to avoid installing the necessary tools on the host, you can run this command to create a one-shot container that will remove itself after completion.

   ```plaintext
   # Make sure you are in the root of the openstatus project
   # For RHEL derivatives, make sure to end /work with :Z for SELinux, "$PWD":/work:Z
   sudo docker run --rm -it \
     --network openstatus \
     --env-file .env.docker \
     -v "$PWD":/work \
     -w /work/packages/db \
     node:22-trixie \
     bash -lc '
       set -euo pipefail
       export DEBIAN_FRONTEND=noninteractive
       apt-get update -qq
       apt-get install -y -qq curl ca-certificates unzip
       curl -fsSL https://bun.sh/install -o /tmp/bun-install.sh
       bash /tmp/bun-install.sh
       export PATH="$HOME/.bun/bin:$PATH"
       npm i -g pnpm
       pnpm install
       bun src/migrate.mts
     '
   ```

5. **Deploy Local Tinybird Analytics**

   Tinybird is used for analytics. Deploy the local datasources, pipes, and endpoints.

   ```bash
   # Make sure you are in the root of the openstatus project
   cd packages/tinybird
   pnpm install
   tb --local deploy
   cd ../.. # Return to the project root
   ```

6. **Configure Tinybird API Key**

   You need to get your local Tinybird admin token and add it to your environment file.

   ```bash
   cd packages/tinybird
   tb --local open # This opens the Tinybird UI in your browser
   ```

   In the Tinybird UI, find and copy your admin token. Then, add it to your `.env.docker` file in the root of the project:

   ```env
   TINY_BIRD_API_KEY="your-tinybird-admin-token"
   ```

   After adding the token, restart your services for the changes to take effect:

   ```bash
   # Make sure you are in the root of the openstatus project
   docker compose restart
   ```

### Part 3: Application Configuration

[Section titled “Part 3: Application Configuration”](#part-3-application-configuration)

Now that the services are running, you can access the dashboard and perform the final setup steps.

* **Dashboard:** `http://localhost:3002`
* **Status Pages:** `http://localhost:3003`

7. **Create a Workspace and Set Limits**

   * Navigate to the dashboard at `http://localhost:3002`.
   * Sign up and create a new workspace.
   * Because this is a self-hosted instance, you need to manually set the feature limits for your workspace directly in the database.

   The following command updates the limits for the workspace with `id = 1`. If your workspace has a different ID, change the `WHERE id = 1` part of the command.

   ```bash
   curl -X POST http://localhost:8080/ -H "Content-Type: application/json" \
     -d '{"statements":["UPDATE workspace SET limits = '\''{\\"monitors\\":100,\\"periodicity\\":[\\"30s\\",\\"1m\\",\\"5m\\",\\"10m\\",\\"30m\\",\\"1h\\"],\\"multi-region\\":true,\\"data-retention\\":\\"24 months\\",\\"status-pages\\":20,\\"maintenance\\":true,\\"status-subscribers\\":true,\\"custom-domain\\":true,\\"password-protection\\":true,\\"white-label\\":true,\\"notifications\\":true,\\"sms\\":true,\\"pagerduty\\":true,\\"notification-channels\\":50,\\"members\\":\\"Unlimited\\",\\"audit-log\\":true,\\"private-locations\\":true}'\'' WHERE id = 1"]}'
   ```

   You can find your workspace ID by inspecting the database with a command like `curl -X POST http://localhost:8080/ -H "Content-Type: application/json" -d '{"statements":["SELECT id, name FROM workspace"]}'`.

   If you want to unlock the paid features, you need to upgrade your workspace inside the database. The following command assumes that you want to change the payment plan for the workspace with the ID of 1, and that you want to change it to a “Pro” instance indefinitely.

   ```plaintext
   curl -sS -X POST "http://localhost:8080/" \
     -H "Content-Type: application/json" \
     -d "{\"statements\":[
       \"UPDATE workspace SET plan='team', paid_until=strftime('%s','now') + 315360000, ends_at=NULL WHERE id=1;\",
       \"SELECT id, plan, paid_until, ends_at FROM workspace WHERE id=1;\"
     ]}"
   ```

8. **Deploy a Private Location**

   The self-hosted version relies on private locations to perform checks.

   * In the dashboard, navigate to **Settings -> Private Locations** and create a new one.

   * Copy the generated `OPENSTATUS_KEY`.

   * Deploy the private location probe to your infrastructure using the Docker image `ghcr.io/openstatushq/private-location:latest`.

   * When deploying, you must provide two environment variables to the container:

     * `OPENSTATUS_KEY`: The key you just copied.
     * `OPENSTATUS_INGEST_URL`: The URL of your self-hosted server’s API endpoint (e.g., `http://<your-server-ip-or-domain>:3001`).

   * For a detailed guide on deploying a private location, see **[Deploy Private Locations on Cloudflare Containers](/guides/how-to-deploy-probes-cloudflare-containers)**.

9. **Create Monitors**

   You’re all set! You can now create monitors in the dashboard. They will be checked by the private location you deployed.

![openstatus running locally with self-hosted services](/_astro/local-openstatus.Cm59_Aih_1jP952.webp)

## Service architecture

[Section titled “Service architecture”](#service-architecture)

openstatus consists of multiple services running together:

| Service          | Port | Purpose                             |
| ---------------- | ---- | ----------------------------------- |
| workflows        | 3000 | Background jobs and scheduled tasks |
| server           | 3001 | API backend (tRPC)                  |
| dashboard        | 3002 | Admin interface for configuration   |
| status-page      | 3003 | Public status pages                 |
| private-location | 8081 | Monitoring agent for checks         |
| libsql           | 8080 | Database (HTTP)                     |
| libsql           | 5001 | Database (gRPC)                     |
| tinybird-local   | 7181 | Analytics and metrics               |

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Congratulations! You’ve successfully:

* ✅ Deployed openstatus on your own infrastructure
* ✅ Configured all required services
* ✅ Set up a private location for monitoring
* ✅ Created your first self-hosted monitor

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Containers won’t start**: Check Docker logs with `docker compose logs [service-name]`

**Database migrations fail**: Ensure you’re in the correct directory and have pnpm installed

**Private location not connecting**: Verify the `OPENSTATUS_KEY` and `OPENSTATUS_INGEST_URL` are correct

**Tinybird issues**: Make sure the Tinybird token is correctly set in `.env.docker`

## Next steps

[Section titled “Next steps”](#next-steps)

* **[Deploy Private Locations](/guides/how-to-deploy-probes-cloudflare-containers)** - Set up monitoring from multiple regions
* **[Create Monitors](/tutorial/how-to-create-monitor)** - Start monitoring your services

## Additional resources

[Section titled “Additional resources”](#additional-resources)

* **[Docker Compose file](https://github.com/openstatusHQ/openstatus/blob/main/docker-compose.yaml)** - Review the complete configuration
* **[Private Location Reference](/reference/private-location)** - Technical specifications
* **[Join our Discord](https://www.openstatus.dev/discord)** - Get help from the community

# Need help?

> We're always here to help.

If you have any questions, feedback, or need help you can:

* Schedule a [call](https://cal.com/team/openstatus/30min) with us.
* Join our [Discord](https://www.openstatus.dev/discord) community.
* Send us an email at <ping@openstatus.dev>
* Open an issue on our [GitHub](https://www.github.com/openstatushq/openstatus) repository.

# Monitoring Overview

> Introduction to synthetic monitoring with openstatus

## What is synthetic monitoring?

[Section titled “What is synthetic monitoring?”](#what-is-synthetic-monitoring)

With openstatus, you can simulate user requests to check the availability and performance of your website, API, or server from different locations around the globe. This proactive approach helps you find issues before your users do.

Synthetic monitoring complements real user monitoring (RUM) by providing:

* **Consistent baseline**: Predictable checks at regular intervals
* **Early warning system**: Detect issues before they affect many users
* **Global perspective**: Monitor from multiple regions simultaneously
* **24/7 coverage**: Continuous monitoring, even when you have no traffic

![openstatus dashboard showing status codes and response time charts](/_astro/dashboard.DrG8m1cm_fLj39.webp)

## How it works

[Section titled “How it works”](#how-it-works)

We send a request to your specified endpoint on a regular schedule and record the response. If your website or API is down, timing out, or doesn’t return the expected response, we’ll alert you right away.

## What is a monitor?

[Section titled “What is a monitor?”](#what-is-a-monitor)

A **monitor** is a job that runs periodically to check the status of a service. This could be a website, an API, or any other service that can be automatically checked. Each monitor you create runs a request to your endpoint and records the results for you to review.

## Creating a Monitor

[Section titled “Creating a Monitor”](#creating-a-monitor)

You can create a new monitor in one of four ways:

* Dashboard: Use our intuitive dashboard to quickly set up and manage your monitors.
* API: Integrate monitor creation into your workflow using our [API](https://api.openstatus.dev/v1#tag/monitor/POST/monitor).
* CLI: Use our command-line interface to create and manage monitors with [YAML configuration files](https://github.com/openstatusHQ/cli-template).
* Terraform: Automate the process with our [Terraform provider](/reference/terraform/).

### Monitor types

[Section titled “Monitor types”](#monitor-types)

* **HTTP**: Check the availability and performance of your web services by sending HTTP requests and analyzing the responses.
* **TCP**: Verify that your servers are accepting connections on specific ports, ensuring that critical
* **DNS**: Monitor the health of your DNS records by performing lookups and validating responses.

## Getting started

[Section titled “Getting started”](#getting-started)

Ready to start monitoring? Follow these guides:

1. **[Create Your First Monitor](/tutorial/how-to-create-monitor)** - Step-by-step tutorial

## Learn more

[Section titled “Learn more”](#learn-more)

* **[Understanding Uptime Monitoring](/concept/uptime-monitoring)** - Core concepts explained

# Reference Documentation

> Technical specifications, API documentation, and configuration references

## 📖 Reference

[Section titled “📖 Reference”](#-reference)

Reference documentation provides **technical specifications** and detailed information about openstatus components, APIs, and configuration options. This is where you look up exact parameter names, return types, and available options.

### When to use reference docs

[Section titled “When to use reference docs”](#when-to-use-reference-docs)

Reference documentation is ideal when you:

* Need to look up specific API endpoints or parameters
* Want to know all available configuration options
* Are looking for technical specifications
* Need to understand data structures and types

### Monitor Types

[Section titled “Monitor Types”](#monitor-types)

Detailed specifications for each monitor type:

[HTTP Monitor ](/reference/http-monitor)Complete reference for HTTP/HTTPS endpoint monitoring

[TCP Monitor ](/reference/tcp-monitor)TCP port monitoring specifications

[DNS Monitor ](/reference/dns-monitor)DNS resolution monitoring reference

### Components & Features

[Section titled “Components & Features”](#components--features)

[Status Page ](/reference/status-page)Status page configuration options

[Status Report ](/reference/status-report)Status report specifications

[Subscriber ](/reference/subscriber)Status page subscriber reference

[Incident ](/reference/incident)Incident management reference

[Notification ](/reference/notification)Notification channel specifications

### Infrastructure & Tools

[Section titled “Infrastructure & Tools”](#infrastructure--tools)

[CLI Reference ](/reference/cli-reference)Complete command-line interface documentation

[Terraform Provider ](/reference/terraform)Infrastructure as code with Terraform

[Private Location ](/reference/private-location)Self-hosted monitoring agent reference

### API Documentation

[Section titled “API Documentation”](#api-documentation)

For programmatic access to openstatus:

* **[REST API](https://api.openstatus.dev/v1)** - Full REST API reference with interactive examples

### Related sections

[Section titled “Related sections”](#related-sections)

* **[Tutorials](/tutorial/getting-started/)** - Learn how to use these features step-by-step
* **[How-to guides](/guides/getting-started/)** - Practical examples of common use cases
* **[Explanations](/concept/getting-started/)** - Understand the concepts behind the reference material

# CLI Reference

## CLI interface - openstatus

[Section titled “CLI interface - openstatus”](#cli-interface---openstatus)

openstatus is a command line interface for managing your monitors and triggering your synthetics tests.

This is openstatus Command Line Interface, the openstatus.dev CLI.

Usage:

```bash
$ openstatus [COMMAND] [COMMAND FLAGS] [ARGUMENTS...]
```

### `monitors` command

[Section titled “monitors command”](#monitors-command)

Manage your monitors.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors [ARGUMENTS...]
```

### `monitors apply` subcommand

[Section titled “monitors apply subcommand”](#monitors-apply-subcommand)

Create or update monitors.

> openstatus monitors apply \[options]

Creates or updates monitors according to the openstatus configuration file.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors apply [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                                           |   Default value   |  Environment variables |
| --------------------------- | ----------------------------------------------------- | :---------------: | :--------------------: |
| `--config="…"` (`-c`)       | The configuration file containing monitor information | `openstatus.yaml` |         *none*         |
| `--access-token="…"` (`-t`) | openstatus API Access Token                           |                   | `OPENSTATUS_API_TOKEN` |
| `--auto-accept` (`-y`)      | Automatically accept the prompt                       |      `false`      |         *none*         |

### `monitors import` subcommand

[Section titled “monitors import subcommand”](#monitors-import-subcommand)

Import all your monitors.

> openstatus monitors import \[options]

Import all your monitors from your workspace to a YAML file; it will also create a lock file to manage your monitors with ‘apply’.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors import [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                 |   Default value   |  Environment variables |
| --------------------------- | --------------------------- | :---------------: | :--------------------: |
| `--access-token="…"` (`-t`) | openstatus API Access Token |                   | `OPENSTATUS_API_TOKEN` |
| `--output="…"` (`-o`)       | The output file name        | `openstatus.yaml` |         *none*         |

### `monitors info` subcommand

[Section titled “monitors info subcommand”](#monitors-info-subcommand)

Get a monitor information.

> openstatus monitors info \[MonitorID]

Fetch the monitor information. The monitor information includes details such as name, description, endpoint, method, frequency, locations, active status, public status, timeout, degraded after, and body. The body is truncated to 40 characters.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors info [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                 | Default value |  Environment variables |
| --------------------------- | --------------------------- | :-----------: | :--------------------: |
| `--access-token="…"` (`-t`) | openstatus API Access Token |               | `OPENSTATUS_API_TOKEN` |

### `monitors list` subcommand

[Section titled “monitors list subcommand”](#monitors-list-subcommand)

List all monitors.

> openstatus monitors list \[options]

List all monitors. The list shows all your monitors attached to your workspace. It displays the ID, name, and URL of each monitor.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors list [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                               | Default value |  Environment variables |
| --------------------------- | ----------------------------------------- | :-----------: | :--------------------: |
| `--all`                     | List all monitors including inactive ones |    `false`    |         *none*         |
| `--access-token="…"` (`-t`) | openstatus API Access Token               |               | `OPENSTATUS_API_TOKEN` |

### `monitors trigger` subcommand

[Section titled “monitors trigger subcommand”](#monitors-trigger-subcommand)

Trigger a monitor execution.

> openstatus monitors trigger \[MonitorId] \[options]

Trigger a monitor execution on demand. This command allows you to launch your tests on demand.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] monitors trigger [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                 | Default value |  Environment variables |
| --------------------------- | --------------------------- | :-----------: | :--------------------: |
| `--access-token="…"` (`-t`) | openstatus API Access Token |               | `OPENSTATUS_API_TOKEN` |

### `run` command (aliases: `r`)

[Section titled “run command (aliases: r)”](#run-command-aliases-r)

Run your synthetics tests.

> openstatus run \[options]

Run the synthetic tests defined in the config.openstatus.yaml.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] run [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                 |       Default value      |  Environment variables |
| --------------------------- | --------------------------- | :----------------------: | :--------------------: |
| `--config="…"`              | The configuration file      | `config.openstatus.yaml` |         *none*         |
| `--access-token="…"` (`-t`) | openstatus API Access Token |                          | `OPENSTATUS_API_TOKEN` |

### `whoami` command (aliases: `w`)

[Section titled “whoami command (aliases: w)”](#whoami-command-aliases-w)

Get your workspace information.

> openstatus whoami \[options]

Get your current workspace information, display the workspace name, slug, and plan.

Usage:

```bash
$ openstatus [GLOBAL FLAGS] whoami [COMMAND FLAGS] [ARGUMENTS...]
```

The following flags are supported:

| Name                        | Description                 | Default value |  Environment variables |
| --------------------------- | --------------------------- | :-----------: | :--------------------: |
| `--access-token="…"` (`-t`) | openstatus API Access Token |               | `OPENSTATUS_API_TOKEN` |

# DNS Monitor Reference

> Complete technical specification for DNS record monitoring

## Overview

[Section titled “Overview”](#overview)

A DNS Monitor is a component designed to verify the availability and correctness of DNS records. It performs periodic lookups for specified DNS record types against a target domain or subdomain from various geographical locations.

**Use cases:**

* Validating domain name resolution
* Monitoring changes to critical DNS records (e.g., A, CNAME, MX)
* Ensuring proper load balancing via DNS (when combined with multi-region checks)
* Detecting unauthorized DNS alterations

## Configuration

[Section titled “Configuration”](#configuration)

### URI

[Section titled “URI”](#uri)

**Type:** String (required) **Format:** Domain name or subdomain

The fully qualified domain name or subdomain to be monitored.

**Examples:**

* `openstat.us`
* `api.example.com`
* `mail.example.org`

### Record Types

[Section titled “Record Types”](#record-types)

The monitor supports fetching and validating the following DNS record types:

* `A` (Address Record): Maps a domain name to an IPv4 address.
* `AAAA` (IPv6 Address Record): Maps a domain name to an IPv6 address.
* `CNAME` (Canonical Name Record): Maps an alias domain name to another canonical domain name.
* `MX` (Mail Exchange Record): Specifies the mail servers responsible for accepting email messages on behalf of a domain name.
* `NS` (Name Server Record): Delegates a domain or subdomain to a set of authoritative name servers.
* `TXT` (Text Record): Carries arbitrary human-readable text and is also used for various purposes like SPF, DKIM, DMARC, and site verification.

### Regions

[Section titled “Regions”](#regions)

The geographical locations from which the DNS monitoring checks are performed. This allows for verification of DNS propagation and performance across different networks.

**Africa**

* Johannesburg, South Africa 🇿🇦 (free)

**Asia**

* Hong Kong, Hong Kong 🇭🇰 (free)
* Mumbai, India 🇮🇳
* Singapore, Singapore 🇸🇬
* Tokyo, Japan 🇯🇵

**Europe**

* Amsterdam, Netherlands 🇳🇱 (free)
* Bucharest, Romania 🇷🇴
* Frankfurt, Germany 🇩🇪
* London, United Kingdom 🇬🇧
* Madrid, Spain 🇪🇸
* Paris, France 🇫🇷
* Stockholm, Sweden 🇸🇪
* Warsaw, Poland 🇵🇱

**North America**

* Ashburn, Virginia, USA 🇺🇸 (free)
* Atlanta, Georgia, USA 🇺🇸
* Boston, Massachusetts, USA 🇺🇸
* Chicago, Illinois, USA 🇺🇸
* Dallas, Texas, USA 🇺🇸
* Denver, Colorado, USA 🇺🇸
* Guadalajara, Mexico 🇲🇽
* Los Angeles, California, USA 🇺🇸
* Miami, Florida, USA 🇺🇸
* Montreal, Canada 🇨🇦
* Phoenix, Arizona, USA 🇺🇸
* Queretaro, Mexico 🇲🇽
* Seattle, Washington, USA 🇺🇸
* San Jose, California, USA 🇺🇸
* Toronto, Canada 🇨🇦

**South America**

* Bogota, Colombia 🇨🇴
* Buenos Aires, Argentina 🇦🇷
* Rio de Janeiro, Brazil 🇧🇷
* Sao Paulo, Brazil 🇧🇷 (free)
* Santiago, Chile 🇨🇱

**Oceania**

* Sydney, Australia 🇦🇺 (free)

### Frequency

[Section titled “Frequency”](#frequency)

The interval at which the DNS checks are performed. Supported frequencies:

* 30 seconds
* 1 minute
* 5 minutes
* 10 minutes
* 30 minutes
* 1 hour

### Response Time Thresholds

[Section titled “Response Time Thresholds”](#response-time-thresholds)

#### Timeout

[Section titled “Timeout”](#timeout)

**Type:** Duration (optional) **Default:** `45 seconds`

The maximum duration to wait for a DNS response. If the lookup exceeds this time, the check is considered failed.

#### Degraded

[Section titled “Degraded”](#degraded)

**Type:** Duration (optional)

The duration after which a DNS response is considered degraded. This indicates a performance issue without being a complete failure.

### Retry

[Section titled “Retry”](#retry)

**Type:** Integer (optional) **Default:** `3`

The number of times the monitor will retry a failed DNS lookup before reporting a definitive failure. For example: `3`

## Related resources

[Section titled “Related resources”](#related-resources)

* **[CLI Reference](/reference/cli-reference)** - Manage monitors as code using the OpenStatus CLI.

# HTTP Monitor Reference

> Complete technical specification for HTTP/HTTPS endpoint monitoring

## Overview

[Section titled “Overview”](#overview)

An HTTP Monitor is a component that allows you to monitor the status of HTTP and HTTPS endpoints. It can be used to monitor websites, APIs, webhooks, or any other HTTP-accessible service.

**Use cases:**

* Website uptime monitoring
* API health checks
* Webhook endpoint validation
* CDN performance monitoring
* Authentication endpoint testing

## Configuration

[Section titled “Configuration”](#configuration)

### URL

[Section titled “URL”](#url)

**Type:** String (required)\
**Format:** Full URL including protocol

The URL of the HTTP endpoint you want to monitor.

**Examples:**

* `https://openstat.us`
* `https://api.example.com/health`
* `http://internal-service.local:8080/status`

**Note:** We recommend using HTTPS for better security.

### Methods

[Section titled “Methods”](#methods)

**Type:** String (required)\
**Default:** `GET`

The HTTP method to use when making the request to the endpoint.

**Available methods:**

* `GET` - Retrieve data (most common for health checks)
* `POST` - Send data to create/trigger actions
* `PUT` - Update existing resources
* `DELETE` - Remove resources
* `HEAD` - Like GET but without response body
* `OPTIONS` - Query supported methods
* `PATCH` - Partial resource updates
* `TRACE` - Echo request for debugging

**Common usage:**

* Health checks: `GET`
* API testing: `POST`, `PUT`, `DELETE`
* Webhook testing: `POST`

### Body

[Section titled “Body”](#body)

**Type:** String (optional)\
**Available for:** `POST`, `PUT`, `PATCH` methods

The request body to send with the HTTP request. Supports both text and binary data.

**Text body examples:**

```json
{ "key": "value" }
```

**Binary data:** For binary content (e.g., images), use base64 encoding with data URI:

```plaintext
data:image/jpeg;base64,/9j...
```

**Content type:** Set the appropriate `Content-Type` header (e.g., `application/json`, `application/octet-stream`).

### Headers

[Section titled “Headers”](#headers)

**Type:** Key-value pairs (optional)

Custom HTTP headers to include with your request.

**Common examples:**

```plaintext
Content-Type: application/json
Authorization: Bearer your_token_here
Accept: application/json
User-Agent: Custom-Agent/1.0
```

**Use cases:**

* **Authentication:** Send API tokens or credentials
* **Content negotiation:** Specify accepted response formats
* **Custom identification:** Add tracking or debugging headers

**Note:** openstatus automatically adds `User-Agent: openstatus/1.0` to all requests.

### Regions

[Section titled “Regions”](#regions)

**Type:** Array of Strings (required) **Format:** Region identifiers (e.g., `iad`, `jnb`)

The geographical regions from which the HTTP request will be triggered. This allows for monitoring global availability and performance.

**Africa**

* Johannesburg, South Africa 🇿🇦 (free)

**Asia**

* Hong Kong, Hong Kong 🇭🇰 (free)
* Mumbai, India 🇮🇳
* Singapore, Singapore 🇸🇬
* Tokyo, Japan 🇯🇵

**Europe**

* Amsterdam, Netherlands 🇳🇱 (free)
* Bucharest, Romania 🇷🇴
* Frankfurt, Germany 🇩🇪
* London, United Kingdom 🇬🇧
* Madrid, Spain 🇪🇸
* Paris, France 🇫🇷
* Stockholm, Sweden 🇸🇪
* Warsaw, Poland 🇵🇱

**North America**

* Ashburn, Virginia, USA 🇺🇸 (free)
* Atlanta, Georgia, USA 🇺🇸
* Boston, Massachusetts, USA 🇺🇸
* Chicago, Illinois, USA 🇺🇸
* Dallas, Texas, USA 🇺🇸
* Denver, Colorado, USA 🇺🇸
* Guadalajara, Mexico 🇲🇽
* Los Angeles, California, USA 🇺🇸
* Miami, Florida, USA 🇺🇸
* Montreal, Canada 🇨🇦
* Phoenix, Arizona, USA 🇺🇸
* Queretaro, Mexico 🇲🇽
* Seattle, Washington, USA 🇺🇸
* San Jose, California, USA 🇺🇸
* Toronto, Canada 🇨🇦

**South America**

* Bogota, Colombia 🇨🇴
* Buenos Aires, Argentina 🇦🇷
* Rio de Janeiro, Brazil 🇧🇷
* Sao Paulo, Brazil 🇧🇷 (free)
* Santiago, Chile 🇨🇱

**Oceania**

* Sydney, Australia 🇦🇺 (free)

### Frequency

[Section titled “Frequency”](#frequency)

**Type:** String (required) **Format:** Duration string (e.g., `30s`, `1m`, `1h`)

The interval at which the HTTP monitor will perform checks. Supported frequencies:

* `30 seconds`
* `1 minute`
* `5 minutes`
* `10 minutes`
* `30 minutes`
* `1 hour`

### Response Time Thresholds

[Section titled “Response Time Thresholds”](#response-time-thresholds)

#### Timeout

[Section titled “Timeout”](#timeout)

**Type:** Duration (optional) **Default:** `45 seconds`

The maximum duration to wait for the HTTP request to complete. If the request exceeds this time, it is considered a failure.

#### Degraded

[Section titled “Degraded”](#degraded)

**Type:** Duration (optional)

The duration after which the HTTP request is considered to be performing in a degraded state. This threshold allows for proactive alerting on performance issues before a complete outage.

### Retry

[Section titled “Retry”](#retry)

**Type:** Integer (optional) **Default:** `3`

The number of times the monitor will automatically retry the HTTP request upon failure before reporting a definitive error. For example: `3`

### Assertions

[Section titled “Assertions”](#assertions)

Assertions allow you to validate specific aspects of the HTTP response.

#### Body Assertions

[Section titled “Body Assertions”](#body-assertions)

Validate the content of the HTTP response body.

**Comparisons:**

* `Contains`: The response body must include the specified string.
* `Not Contains`: The response body must not include the specified string.
* `Equal`: The response body must exactly match the specified string.
* `Not Equal`: The response body must not exactly match the specified string.
* `Empty`: The response body must be empty.

#### Status Code Assertions

[Section titled “Status Code Assertions”](#status-code-assertions)

Validate the HTTP status code of the response.

**Comparisons:**

* `Equal`: The status code must be exactly the specified value.
* `Not Equal`: The status code must not be the specified value.
* `Greater Than`: The status code must be greater than the specified value.
* `Greater Than or Equal`: The status code must be greater than or equal to the specified value.
* `Less Than`: The status code must be less than the specified value.
* `Less Than or Equal`: The status code must be less than or equal to the specified value.

#### Headers Assertions

[Section titled “Headers Assertions”](#headers-assertions)

Validate the presence or content of specific HTTP response headers.

**Purpose:** Verify cache headers, check security headers (e.g., `X-Frame-Options`), validate content-type.

**Comparisons:**

* `Contains`: A header’s value must include the specified string.
* `Not Contains`: A header’s value must not include the specified string.
* `Equal`: A header’s value must exactly match the specified string.
* `Not Equal`: A header’s value must not exactly match the specified string.
* `Empty`: A header’s value must be empty or the header must not be present.

**Example Use Cases:**

* Verify `Cache-Control` headers are present and correct.
* Check for the existence of security-related headers like `Strict-Transport-Security`.
* Validate the `Content-Type` header in API responses.

### OpenTelemetry

[Section titled “OpenTelemetry”](#opentelemetry)

Configures the export of monitoring metrics to an OpenTelemetry-compatible observability platform.

#### OTLP Endpoint

[Section titled “OTLP Endpoint”](#otlp-endpoint)

**Type:** String (optional)\
**Protocol:** HTTP only

The OTLP (OpenTelemetry Protocol) endpoint URL where collected metrics should be exported.

**Example:** `https://otlp.example.com/v1/metrics`

#### OTLP Headers

[Section titled “OTLP Headers”](#otlp-headers)

**Type:** Key-value pairs (optional)

Custom headers to include when sending metrics to your OTLP endpoint. Commonly used for authentication or tenant identification.

**Common example:**

```plaintext
Authorization: Bearer <your_token>
```

### Public

[Section titled “Public”](#public)

**Type:** Boolean\
**Default:** `false`

Controls the visibility of monitor data on your public status page.

* `true`: Monitor metrics and status are visible to all visitors of your status page.
* `false`: Monitor data remains private, accessible only within your OpenStatus dashboard.

**Use cases for public visibility:**

* Enhancing transparency with users regarding service health.
* Providing public API status pages.
* Displaying SaaS service availability to customers.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Create Your First Monitor](/tutorial/how-to-create-monitor)** - Step-by-step tutorial on setting up a monitor.
* **[CLI Reference](/reference/cli-reference)** - Guide to managing OpenStatus monitors programmatically using the command-line interface.

# Incident Reference

> Technical specification for incident management and lifecycle

## Overview

[Section titled “Overview”](#overview)

An incident in OpenStatus represents a detected problem or service disruption related to a monitored resource. Incidents are automatically generated when a monitor reports a failure condition that meets predefined criteria. They serve as a central point for tracking, managing, and resolving service impairments.

**Key characteristics:**

* Automatically triggered by monitor failures.
* Aggregates related failure events for a single monitor.
* Provides a clear status of service health.

## Incident Triggering

[Section titled “Incident Triggering”](#incident-triggering)

An incident is triggered when a significant percentage of recent monitoring checks for a given monitor report a failed status. This mechanism prevents false positives from transient network issues.

**Trigger Condition:**

* **Failure Threshold:** An incident is initiated when at least 50% of the checks within a defined window (e.g., the last `N` checks or within a `T` duration) have reported a `failure` or `degraded` status.

## Incident Lifecycle and States

[Section titled “Incident Lifecycle and States”](#incident-lifecycle-and-states)

Incidents progress through several states reflecting their current resolution status. These states are managed through status reports (see [Status Report Reference](/reference/status-report)).

**Primary States:**

* `investigating`: The incident has been detected, and the team is actively looking into the root cause.
* `identified`: The root cause of the incident has been identified.
* `monitoring`: A fix has been deployed or a mitigation is in place, and the service is being monitored to confirm resolution.
* `resolved`: The incident has been fully resolved, and the service is operating normally.

## Properties

[Section titled “Properties”](#properties)

While an incident is active, it collects and displays key information related to the service disruption.

* **Monitor Association:** Each incident is directly linked to the monitor that triggered it, providing immediate context to the affected service.
* **Start Time:** Timestamp indicating when the incident was first detected and created.
* **Status Reports:** A chronological log of all updates and state changes applied to the incident.
* **Impacted Locations:** Details on the geographical regions from which the monitor reported failures.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Status Report Reference](/reference/status-report)** - Details on how incident statuses are managed and reported.

# Location Reference

> Complete technical specification for Location monitoring

## Overview

[Section titled “Overview”](#overview)

OpenStatus monitors your endpoints from multiple global locations to ensure accurate uptime and latency reporting. Each monitoring location corresponds to a Fly.io region, with both IPv4 and IPv6 addresses available for each.

You can use these locations to:

* Configure region-specific checks
* Allowlist monitoring IPs in your firewall
* Understand where requests originate during synthetic monitoring

### Fly.io Regions & Monitoring IPs

[Section titled “Fly.io Regions & Monitoring IPs”](#flyio-regions--monitoring-ips)

Below is the complete list of regions used for monitoring, along with their associated IPv4 and IPv6 addresses.

| Region Code | Location Name    | IPv4 Address  | IPv6 Address                 |
| ----------- | ---------------- | ------------- | ---------------------------- |
| ams         | Amsterdam        | 209.71.64.1   | 2a09:8280:e601:1:0:22:b79b:0 |
| arn         | Stockholm        | 209.71.98.189 | 2a09:8280:e602:1:0:22:b79b:0 |
| bom         | Mumbai           | 209.71.68.172 | 2a09:8280:e605:1:0:22:b79b:0 |
| cdg         | Paris            | 209.71.86.183 | 2a09:8280:e607:1:0:22:b79b:0 |
| dfw         | Dallas           | 209.71.71.89  | 2a09:8280:e609:1:0:22:b79b:0 |
| ewr         | Newark           | 209.71.69.221 | 2a09:8280:e610:1:0:22:b79b:0 |
| fra         | Frankfurt        | 209.71.90.204 | 2a09:8280:e612:1:0:22:b79b:0 |
| gru         | São Paulo        | 209.71.94.28  | 2a09:8280:e615:1:0:22:b79b:0 |
| iad         | Washington, D.C. | 209.71.81.6   | 2a09:8280:e618:1:0:22:b79b:0 |
| jnb         | Johannesburg     | 209.71.83.120 | 2a09:8280:e620:1:0:22:b79b:0 |
| lax         | Los Angeles      | 209.71.91.96  | 2a09:8280:e621:1:0:22:b79b:0 |
| lhr         | London           | 209.71.85.82  | 2a09:8280:e622:1:0:22:b79b:0 |
| nrt         | Tokyo            | 209.71.88.150 | 2a09:8280:e625:1:0:22:b79b:0 |
| ord         | Chicago          | 209.71.89.1   | 2a09:8280:e626:1:0:22:b79b:0 |
| sin         | Singapore        | 209.71.80.112 | 2a09:8280:e632:1:0:22:b79b:0 |
| sjc         | San Jose         | 209.71.101.37 | 2a09:8280:e633:1:0:22:b79b:0 |
| syd         | Sydney           | 209.71.97.108 | 2a09:8280:e634:1:0:22:b79b:0 |
| yyz         | Toronto          | 209.71.99.51  | 2a09:8280:e637:1:0:22:b79b:0 |

***

## Railway Regions & Monitoring IPs

[Section titled “Railway Regions & Monitoring IPs”](#railway-regions--monitoring-ips)

Below is the complete list of Railway regions used for monitoring, along with their associated IPv4 addresses.

| Region Code            | Location Name  | IPv4 Address   |
| ---------------------- | -------------- | -------------- |
| europe-west4-drams3a   | Europe West    | 208.77.244.15  |
| asia-southeast1-eqsg3a | Asia Southeast | 208.77.246.15  |
| us-east4-eqdc4a        | US East        | 162.220.234.15 |
| us-west2               | US West        | 162.220.232.99 |

***

## Koyeb Regions & Monitoring IPs

[Section titled “Koyeb Regions & Monitoring IPs”](#koyeb-regions--monitoring-ips)

Koyeb does not provide static IP addresses for their regions. For more information, please refer to Koyeb’s [documentation](https://www.koyeb.com/docs/faqs/general#i-want-to-restrict-access-to-a-database-or-other-application-by-ip-address-what-ip-addresses-does-koyeb-use).

***

**Note:**

* Both IPv4 and IPv6 addresses are provided for allowlisting and diagnostics.
* Location names are for reference and may be used in the dashboard UI.

# Notification Channels Reference

> Technical specification for OpenStatus notification channels and alert payloads.

## Overview

[Section titled “Overview”](#overview)

Notifications in OpenStatus provide real-time alerts regarding changes in monitor status, such as recovery from an outage or detection of a new failure. By default, no notification channels are configured in a new workspace. Users must configure and enable specific channels to receive alerts.

## Notification Channels

[Section titled “Notification Channels”](#notification-channels)

Each notification channel requires specific configuration parameters to enable alert delivery.

### Slack

[Section titled “Slack”](#slack)

Integrates with Slack to send alerts to a designated channel.

**Configuration:**

* **Incoming Webhook URL:** (Required) A [Slack incoming webhook URL](https://api.slack.com/incoming-webhooks) where notifications will be posted. **Example**: `https://hooks.slack.com/services/XXX/YYY/ZZZ`

You can [download the openstatus logo](https://www.openstatus.dev/assets/logos/openstatus.jpeg) to add a custom logo.

### Email

[Section titled “Email”](#email)

Sends alerts directly to a specified email address.

**Configuration:**

* **Email Address:** (Required) The recipient’s email address.

### Discord

[Section titled “Discord”](#discord)

Delivers alerts to a Discord channel via a webhook.

**Configuration:**

* **Webhook URL:** (Required) A [Discord webhook URL](https://support.discord.com/hc/en-us/articles/228383668) for the target channel. **Example:** `https://discordapp.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz1234567890`

You can [download the openstatus logo](https://www.openstatus.dev/assets/logos/openstatus.jpeg) to add a custom logo.

### Grafana OnCall IRM

[Section titled “Grafana OnCall IRM”](#grafana-oncall-irm)

Sends notifications to a Grafana OnCall IRM.

**Configuration:**

* **Webhook URL:** (Required) A [Grafana OnCall IRM webhook URL](https://grafana.com/docs/grafana-cloud/alerting-and-irm/irm/configure/integrations/webhooks/incoming-webhooks/oncall-webhooks/).

### Google Chat

[Section titled “Google Chat”](#google-chat)

Sends notifications to a Google Chat space.

**Configuration:**

* **Webhook URL:** (Required) A [Google Chat webhook URL](https://developers.google.com/workspace/chat/quickstart/webhooks) for the target space.

### SMS

[Section titled “SMS”](#sms)

Sends alerts as SMS messages to a mobile phone number.

**Configuration:**

* **Phone Number:** (Required) The recipient’s phone number in international format (e.g., `+14155552671`).

**Note:** SMS delivery can vary by country due to provider routing. Contact support if delivery issues are encountered. WhatsApp notifications may be an alternative.

### WhatsApp

[Section titled “WhatsApp”](#whatsapp)

Sends alerts as WhatsApp messages to a mobile phone number.

**Configuration:**

* **Phone Number:** (Required) The recipient’s phone number in international format (e.g., `+14155552671`).

### Telegram

[Section titled “Telegram”](#telegram)

Delivers alerts to a specified Telegram chat.

**Configuration:**

* **Chat ID:** (Required) The unique identifier for the Telegram chat. This typically requires manual retrieval; users can ask `@raw_info_bot` for their chat ID.

**Bot ID:** The official OpenStatus Telegram bot ID is `@openstatushq_bot`.

### Webhook

[Section titled “Webhook”](#webhook)

Sends HTTP POST requests to a custom endpoint with a JSON payload.

**Configuration:**

* **URL:** (Required) The endpoint URL to which the webhook payload will be sent.
* **Headers:** (Optional) Custom HTTP headers to include with the webhook request (key-value pairs).

#### Notification Payloads

[Section titled “Notification Payloads”](#notification-payloads)

Webhook notifications utilize specific JSON payloads for different monitor status changes.

##### Monitor Recovery Payload

[Section titled “Monitor Recovery Payload”](#monitor-recovery-payload)

Sent when a monitor recovers from a `degraded` or `error` state.

```json
{
  "monitor": {
    "id": 1,
    "name": "test",
    "url": "http://openstat.us"
  },
  "cronTimestamp": 1744023705307,
  "status": "recovered",
  "statusCode": 200,
  "latency": 1337
}
```

**Payload Fields:**

| Field           | Type     | Description                                                    |
| :-------------- | :------- | :------------------------------------------------------------- |
| `monitor.id`    | `number` | Unique identifier of the monitor.                              |
| `monitor.name`  | `string` | Name of the monitor.                                           |
| `monitor.url`   | `string` | The URL or URI being monitored.                                |
| `cronTimestamp` | `number` | Timestamp of the check execution in milliseconds since epoch.  |
| `status`        | `string` | Indicates the monitor status: `"recovered"`.                   |
| `statusCode`    | `number` | (Optional) HTTP status code returned by the monitored service. |
| `latency`       | `number` | (Optional) Time taken to complete the check in milliseconds.   |

##### Monitor Failure Payload

[Section titled “Monitor Failure Payload”](#monitor-failure-payload)

Sent when a monitor enters an `error` or `degraded` state.

```json
{
  "monitor": {
    "id": 1,
    "name": "test",
    "url": "http://openstat.us"
  },
  "cronTimestamp": 1744023705307,
  "status": "error",
  "errorMessage": "Connection refused"
}
```

**Payload Fields:**

| Field           | Type     | Description                                                         |
| :-------------- | :------- | :------------------------------------------------------------------ |
| `monitor.id`    | `number` | Unique identifier of the monitor.                                   |
| `monitor.name`  | `string` | Name of the monitor.                                                |
| `monitor.url`   | `string` | The URL or URI being monitored.                                     |
| `cronTimestamp` | `number` | Timestamp of the check execution in milliseconds since epoch.       |
| `status`        | `string` | Indicates the monitor status: `"degraded"` or `"error"`.            |
| `errorMessage`  | `string` | (Optional) A description of the error encountered during the check. |

#### Zod Schema

[Section titled “Zod Schema”](#zod-schema)

The validation schema for webhook payloads:

```ts
import { z } from "zod";


export const PayloadSchema = z.object({
  monitor: z.object({
    id: z.number(),
    name: z.string(),
    url: z.string(),
  }),
  cronTimestamp: z.number(),
  status: z.enum(["degraded", "error", "recovered"]),
  statusCode: z.number().optional(),
  latency: z.number().optional(),
  errorMessage: z.string().optional(),
});
```

### OpsGenie

[Section titled “OpsGenie”](#opsgenie)

Integrates with OpsGenie for incident management.

**Configuration:**

* **API Key:** (Required) An API key obtained from your OpsGenie account.

### PagerDuty

[Section titled “PagerDuty”](#pagerduty)

Integrates with PagerDuty for incident alerting.

**Configuration:**

* **Integration Steps:** (Required) Follow the specific integration steps provided within the PagerDuty workflow to set up this channel.

### Ntfy

[Section titled “Ntfy”](#ntfy)

Sends notifications to an Ntfy topic.

**Configuration:**

* **Ntfy Topic:** (Required) The topic name to which notifications will be published.
* **Custom Server URL:** (Optional) The URL of a custom Ntfy server if not using the default.
* **Bearer Token:** (Optional) An authentication token for accessing the Ntfy server.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Incident Reference](/reference/incident)** - Information about incident creation and management.

# Page Components Reference

> Complete specification for OpenStatus page components on status pages.

## Overview

[Section titled “Overview”](#overview)

Page components are the individual elements displayed on your status page that show the operational status of your services. They provide a flexible way to organize and present both monitored services and static content on your status page.

**Key features:**

* Support for both monitor-linked and static components.
* Organize components into logical groups.
* Custom ordering and arrangement.
* Individual status tracking with incidents, reports, and maintenances.
* Granular control over what appears on your status page.

## Component Types

[Section titled “Component Types”](#component-types)

Page components come in two distinct types, each serving different purposes on your status page.

### Monitor Components

[Section titled “Monitor Components”](#monitor-components)

**Type:** `monitor`

Monitor components are linked to an active monitor in your workspace. They automatically inherit the monitor’s status and display real-time health information.

**Characteristics:**

* Display live monitor status (up, degraded, down).
* Show active incidents from the linked monitor.
* Include historical uptime data.
* Reflect the monitor’s current operational state.
* Automatically update when the monitor changes.

**Use cases:**

* Displaying API endpoint health.
* Showing website availability.
* Tracking critical service dependencies.
* Monitoring infrastructure components.

#### Configuring Monitor Components

[Section titled “Configuring Monitor Components”](#configuring-monitor-components)

When you create a monitor component, you link it to an existing monitor in your workspace. This connection provides several benefits:

**Automatic incident tracking:** When your monitor detects a failure (connection timeout, HTTP error, assertion failure), an incident is automatically created and displayed on the status page. The component will show an **error** status until the monitor recovers.

**Real-time status updates:** The component reflects the current operational state of your monitor. If the monitor is actively checking and healthy, your visitors see a **success** status. If checks fail, they immediately see the issue.

**Historical data visualization:** Monitor components display historical uptime data through status trackers. Depending on your [tracker configuration](/tutorial/how-to-configure-status-page#1-tracker-configuration), you can show:

* **Absolute bar with duration card**: Shows the time spent in each status (success, error, degraded, maintenance).
* **Absolute bar with request card**: Shows the number of successful vs. failed requests.
* **Manual bar**: Shows only the most significant status of each day.

**Uptime calculations:** Monitor components calculate uptime percentages based on:

* Duration of successful vs. failed checks (for duration-based tracking).
* Number of successful vs. failed requests (for request-based tracking).
* Includes incidents and status reports in the calculation.

**Monitor selection:** When adding a monitor component, the dashboard shows you available monitors with indicators for:

* **Public/Private status**: Whether the monitor is already public.
* **Active status**: Only active monitors can be linked.
* **Already linked**: Monitors already used on this status page are unavailable.

Tip

You can customize the component name to be different from the monitor name. For example, your monitor might be named “prod-api-health-check” internally, but the component can display as “API Server” for your visitors.

**Status hierarchy:**

1. **Error** - Active incidents from the linked monitor.
2. **Degraded** - Unresolved status reports affecting this component.
3. **Info** - Ongoing scheduled maintenance.
4. **Success** - Healthy and operational.

**What affects monitor components:**

* ✅ Automatic incidents (from monitor failures)
* ✅ Manual status reports
* ✅ Scheduled maintenances

### Static Components

[Section titled “Static Components”](#static-components)

**Type:** `static`

Static components are independent elements not linked to any monitor. They allow you to display services or systems that you manually manage through status reports and maintenance windows only.

**Characteristics:**

* No automatic status updates.
* Status controlled exclusively by manual status reports and scheduled maintenances.
* Useful for third-party services or manual tracking.
* Do not display incidents (no automatic incident creation).
* Provide flexibility for non-monitored services.

**Use cases:**

* Third-party service dependencies (e.g., payment providers like Stripe, email services like SendGrid).
* Manual status tracking for systems without monitors.
* Services monitored through external tools.
* Components that only need maintenance window communication.
* Legacy systems without API endpoints to monitor.

Caution

Static components **only** respond to manual status reports and scheduled maintenances. They never automatically detect issues or create incidents. If you need automatic failure detection, use a monitor component instead.

#### Managing Static Components

[Section titled “Managing Static Components”](#managing-static-components)

Static components give you full manual control over what your visitors see:

**Status reports:** Create status reports to indicate issues or degraded performance for static components. For example:

* “Stripe payment processing experiencing delays” (degraded status).
* “Email delivery service partially unavailable” (degraded status).

Once you resolve the issue and mark the status report as resolved, the component returns to a success status.

**Maintenance windows:** Schedule maintenance windows to inform visitors about planned downtime:

* “Scheduled database backup - Sunday 2:00 AM - 4:00 AM” (info status).
* “Third-party CDN maintenance window” (info status).

During the maintenance window, the component shows an info status. After the window ends, it returns to its previous status.

**No automatic monitoring:** Static components do not perform any health checks or generate incidents. You are responsible for:

* Monitoring the service through other means.
* Creating status reports when issues occur.
* Updating reports when issues are resolved.
* Communicating maintenance windows in advance.

**Status hierarchy:**

1. **Degraded** - Unresolved status reports affecting this component.
2. **Info** - Ongoing scheduled maintenance.
3. **Success** - No active reports or maintenances.

**What affects static components:**

* ✅ Manual status reports
* ✅ Scheduled maintenances
* ❌ Automatic incidents (not supported)

## Component Groups

[Section titled “Component Groups”](#component-groups)

Component groups allow you to organize related page components into logical sections on your status page. Groups improve readability and help visitors understand your service architecture.

**Benefits:**

* Visual organization of related services.
* Collapsible sections for better page structure.
* Independent ordering within groups.
* Clear service categorization.

**Examples of grouping strategies:**

| Group Name                | Components                                  |
| ------------------------- | ------------------------------------------- |
| **API Services**          | Authentication API, Data API, WebSocket API |
| **Infrastructure**        | Database, Cache, Message Queue              |
| **External Dependencies** | Payment Provider, Email Service, CDN        |
| **Regional Services**     | US Region, EU Region, APAC Region           |

**Group configuration:**

* **Name:** The group heading displayed on your status page.
* **Order:** Position of the group relative to other groups and ungrouped components.
* **Components:** The page components contained within this group.

## Events and Status

[Section titled “Events and Status”](#events-and-status)

Page components can be affected by up to three types of events that influence their displayed status. The type of component determines which events apply:

| Event Type         | Monitor Components | Static Components |
| ------------------ | ------------------ | ----------------- |
| **Incidents**      | ✅ Automatic        | ❌ Not supported   |
| **Status Reports** | ✅ Manual           | ✅ Manual          |
| **Maintenances**   | ✅ Manual           | ✅ Manual          |

### Incidents

[Section titled “Incidents”](#incidents)

**Applies to:** Monitor components only

Incidents are automatically generated when a monitor detects a failure. They represent unplanned outages or degraded performance discovered through active monitoring.

**How incidents are created:**

* Monitor check fails (connection timeout, HTTP error, DNS failure).
* Monitor assertion fails (wrong status code, unexpected response body).
* Monitor reaches degraded threshold (response time too slow).

**Status impact:** Components with active incidents show an **error** status. This takes the highest priority in the status hierarchy.

**Resolution:** Incidents are automatically resolved when the monitor recovers and checks succeed again.

Note

Static components **never** generate incidents because they are not linked to monitors. Use status reports for manual issue tracking on static components.

### Status Reports

[Section titled “Status Reports”](#status-reports)

**Applies to:** Both monitor and static components

Status reports are manually created updates about component health or issues. They provide a way to communicate problems that may not trigger automatic monitoring or to manually report issues with static components.

**Status impact:** Components with unresolved status reports show a **degraded** status (unless overridden by an incident for monitor components).

**Use cases for monitor components:**

* Reporting known issues that don’t cause complete outages.
* Communicating performance degradation not captured by monitoring.
* Providing context for intermittent issues.

**Use cases for static components:**

* Reporting third-party service issues (e.g., “Stripe processing delays”).
* Communicating external service degradation.
* Announcing partial outages of non-monitored systems.

**Attaching to components:** When creating a status report, you can select which components are affected. Multiple components can be attached to a single report.

### Maintenances

[Section titled “Maintenances”](#maintenances)

**Applies to:** Both monitor and static components

Maintenances are scheduled maintenance windows that you create in advance. They inform visitors about planned downtime or service interruptions for both monitored and static components.

**Status impact:** Components with ongoing maintenances show an **info** status (unless overridden by incidents or reports).

**Use cases for monitor components:**

* Scheduled system upgrades that will cause downtime.
* Infrastructure changes that affect monitored services.
* Planned deployments requiring service restarts.

**Use cases for static components:**

* Third-party maintenance windows (e.g., “Payment provider scheduled maintenance”).
* External service upgrade notifications.
* Planned downtime for non-monitored dependencies.

**Scheduling:** Maintenances have a defined start and end time. The info status automatically appears during the window and disappears when the maintenance ends.

**Attaching to components:** When creating a maintenance, you select which components will be affected. This allows you to communicate maintenance impact across multiple services.

## Managing Components

[Section titled “Managing Components”](#managing-components)

### Adding Components

[Section titled “Adding Components”](#adding-components)

You can add components to your status page in two ways:

1. **Individual components:** Add a single component outside of any group.
2. **Components within groups:** Add a component directly into a new or existing group.

When adding a monitor component, you can only select from monitors that:

* Are currently active.
* Have not been deleted.
* Are not already linked to another component on this status page.

### Reordering Components

[Section titled “Reordering Components”](#reordering-components)

Components and groups can be reordered using drag-and-drop functionality in the dashboard. The order determines how they appear on your status page from top to bottom.

**Ordering tips:**

* Place your most critical services at the top.
* Group related services together.
* Consider visitor priorities when ordering.

### Editing Components

[Section titled “Editing Components”](#editing-components)

You can modify the following properties of existing components:

* Component name and description.
* Group assignment (move between groups or make ungrouped).
* Display order.

**Note:** You cannot change a component’s type (monitor to static or vice versa) after creation. To change types, delete the component and create a new one.

### Deleting Components

[Section titled “Deleting Components”](#deleting-components)

When you delete a component, any associations with status reports and maintenances are automatically removed. The linked monitor (if applicable) is not deleted and remains available in your workspace.

**Warning:** Deletion is permanent and cannot be undone. Ensure you want to remove the component before confirming deletion.

## Deprecation Notice

[Section titled “Deprecation Notice”](#deprecation-notice)

The legacy monitor-only system for status pages is deprecated in favor of the more flexible page component system.

**Deprecated approach:**

* Status pages directly referenced monitors.
* No support for static content.
* Limited organizational flexibility.

**Current approach (page components):**

* Status pages contain page components.
* Components can be monitors or static content.
* Full support for grouping and custom ordering.
* Better separation between monitoring and status page presentation.

### API Compatibility

[Section titled “API Compatibility”](#api-compatibility)

**v1 API (backward compatibility):** The v1 API continues to display `monitorIds` and `monitors` fields in status page responses to avoid breaking changes for existing integrations. However, these fields now only include page components that are explicitly of type `monitor`. Static components are not included in these legacy fields.

**Future API versions:** Newer API versions will primarily use the `pageComponents` structure. The legacy `monitors` and `monitorIds` fields will be removed in future API versions. We recommend migrating your integrations to use `pageComponents` for full feature support.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Status Page Reference](/reference/status-page)** - Complete status page configuration reference.
* **[Status Report Reference](/reference/status-report)** - Details on creating and managing status reports.
* **[Create Status Page](/tutorial/how-to-create-status-page)** - Step-by-step tutorial on creating a status page.
* **[HTTP Monitor Reference](/reference/http-monitor)** - Technical specification for HTTP monitors that can be linked to components.

# Private Location Reference

> Technical specification for configuring and utilizing private monitoring locations.

## Overview

[Section titled “Overview”](#overview)

A private location in OpenStatus enables users to deploy monitoring probes within their own infrastructure or private networks. This capability is essential for monitoring internal services, APIs, or systems that are not publicly accessible from the internet, such as those behind firewalls or within a Virtual Private Cloud (VPC).

**Key benefits:**

* **Internal Monitoring:** Monitor services running on private networks.
* **Security:** Keep sensitive internal endpoints protected from public exposure.
* **Compliance:** Meet specific regulatory or security compliance requirements by controlling data paths.
* **Reduced Latency:** Conduct checks closer to your services for more accurate performance metrics.

## How it Works

[Section titled “How it Works”](#how-it-works)

When a private location is configured, OpenStatus provides a mechanism (e.g., a container image or agent) that you deploy within your private environment. This deployed component acts as a local monitoring probe, executing checks on behalf of your OpenStatus account.

1. **Deployment:** You deploy the OpenStatus private probe within your chosen infrastructure (e.g., a Docker container on a server, a Kubernetes pod).
2. **Secure Connection:** The private probe establishes a secure, outbound-only connection to the OpenStatus platform, eliminating the need for inbound firewall rules.
3. **Check Execution:** OpenStatus dispatches monitoring tasks to your private probe via this secure connection. The probe then executes the configured checks against your internal services.
4. **Result Reporting:** The private probe securely sends the monitoring results (e.g., status, latency, response data) back to the OpenStatus platform for processing, alerting, and visualization.

## Configuration

[Section titled “Configuration”](#configuration)

Detailed steps for setting up a private location involve:

1. **Probe Deployment:** Provisioning a server or container environment within your private network.
2. **Agent Installation:** Deploying the OpenStatus private probe agent (e.g., Docker image) onto your infrastructure.
3. **Authentication:** Configuring the probe with necessary API keys or tokens to securely authenticate with your OpenStatus workspace.
4. **Network Access:** Ensuring the deployed probe has network access to the internal services it needs to monitor, as well as outbound access to the OpenStatus platform.

**Example Use Cases:**

* Monitoring an internal REST API that is only accessible from within your corporate network.
* Checking the health of a database server running on a private subnet.
* Performing synthetic transactions on an internal web application before it’s exposed publicly.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[How to Deploy Probes on Cloudflare Containers](/guides/how-to-deploy-probes-cloudflare-containers)** - A guide for deploying private probes using Cloudflare Workers/Containers. (Example deployment guide)
* **[CLI Reference](/reference/cli-reference)** - Manage monitors as code, including those utilizing private locations.

# Status Page Reference

> Complete technical specification for OpenStatus status page configuration.

## Overview

[Section titled “Overview”](#overview)

A status page is a dedicated web interface provided by OpenStatus that publicly displays the operational status of your services and systems. It serves as a transparent communication tool during incidents and for showcasing overall service health.

**Key features:**

* Real-time service status updates.
* Incident communication and history.
* Customizable branding and domain.
* Multiple access control options.

## Configuration

[Section titled “Configuration”](#configuration)

OpenStatus provides several configuration options to customize your status page’s appearance, accessibility, and functionality.

### Slug

[Section titled “Slug”](#slug)

**Type:** String (required) **Format:** URL-friendly string (e.g., `my-service-status`)

A unique identifier that forms part of your status page’s default URL. For example, a slug of `status` will result in a URL like `https://status.openstatus.dev`.

### Custom Domain

[Section titled “Custom Domain”](#custom-domain)

**Type:** String (optional) **Format:** Valid domain name (e.g., `status.example.com`)

Allows you to host your status page on a custom domain. Once configured, your status page will be accessible at `https://your-custom-domain.com`.

### Password (Basic Auth)

[Section titled “Password (Basic Auth)”](#password-basic-auth)

**Type:** String (optional)

Enables basic password protection for your status page. If a password is set, users will be redirected to a login page (`/login`) to gain access. The password is stored in a cookie upon successful authentication.

**Sharing with password:** You can provide direct access by appending the password as a URL search parameter: `https://[slug].openstatus.dev/?pw=your-secret-password`. This method is also useful for authenticating private RSS feeds.

### Magic Link (Session Auth)

[Section titled “Magic Link (Session Auth)”](#magic-link-session-auth)

**Type:** Boolean (add-on feature)

Restricts access to your status page to users with approved email domains. Users receive a magic link via email, which, upon clicking, authenticates them via a session token. This feature is typically available as a paid add-on for specific plans.

### Favicon

[Section titled “Favicon”](#favicon)

**Type:** Image file (e.g., `.ico`, `.png`)

Allows you to upload a custom favicon that will appear in browser tabs and bookmarks for your status page.

### JSON Feed

[Section titled “JSON Feed”](#json-feed)

**Type:** Read-only endpoint **Format:** JSON

Provides a machine-readable JSON representation of your status page data. This feed can be accessed by appending `/feed/json` to your status page URL.

**Example:** `https://status.openstatus.dev/feed/json`

**Deprecation Notice:**

The following fields are deprecated and will be removed in a future version:

* **`monitors`** (top-level): Use `pageComponents` instead, which provides a more flexible component-based structure that supports both monitors and external services.
* **`maintenances[].monitors`**: Use `maintenances[].pageComponents` instead, which references page component IDs rather than monitor IDs.
* **`statusReports[].monitors`**: Use `statusReports[].pageComponents` instead, which references page component IDs rather than monitor IDs.

These deprecated fields are currently maintained for backward compatibility but may be removed in future versions.

### SSH Command

[Section titled “SSH Command”](#ssh-command)

**Type:** Command-line utility

Allows you to quickly check the current status page status directly from your terminal using an SSH command.

**Usage:**

```bash
ssh [slug]@ssh.openstatus.dev
```

**Example:** `ssh my-service@ssh.openstatus.dev`

### White Label

[Section titled “White Label”](#white-label)

**Type:** Boolean (add-on feature)

Removes the “powered by openstatus.dev” footer from your status page, providing a fully branded experience. This feature is typically available as a paid add-on for Starter and Pro plans and is enabled via your workspace settings, affecting all status pages within that workspace.

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Create Status Page](/tutorial/how-to-create-status-page)** - Step-by-step tutorial on creating a status page.
* **[How to Configure Status Page](/tutorial/how-to-configure-status-page)** - Guide on advanced status page configuration.
* **[Status Report Reference](/reference/status-report)** - Details on how incident statuses are managed and reported.

# Status Report Reference

> Technical specification for incident status updates within OpenStatus.

## Overview

[Section titled “Overview”](#overview)

A status report is a chronological update or event associated with an ongoing incident in OpenStatus. These reports are crucial for communicating the progress of an incident, from initial detection to final resolution, providing transparency to stakeholders.

**Purpose:**

* To document the lifecycle and progress of an incident.
* To communicate current incident status and actions taken.
* To provide historical context for post-incident analysis.

## Relationship to Incidents

[Section titled “Relationship to Incidents”](#relationship-to-incidents)

Each status report is directly linked to a specific incident. As an incident progresses through its resolution process, new status reports are added to provide updates, often accompanied by a change in the incident’s overall status.

## Configuration and Properties

[Section titled “Configuration and Properties”](#configuration-and-properties)

A status report consists of several key properties that define its content and context.

### Status

[Section titled “Status”](#status)

**Type:** Enumerated String (required)

Represents the current stage or state of the associated incident at the time the report is issued. The available statuses are:

* `investigating`: The incident has been detected, and the team is actively looking into the root cause.
* `identified`: The root cause of the incident has been identified.
* `monitoring`: A fix has been deployed or a mitigation is in place, and the service is being monitored to confirm resolution.
* `resolved`: The incident has been fully resolved, and the service is operating normally.

### Date

[Section titled “Date”](#date)

**Type:** Datetime (required) **Format:** ISO 8601 (e.g., `2026-01-05T12:30:00Z`)

The timestamp indicating when the status report was created or when the reported status took effect. This provides a clear timeline for incident progression.

### Message

[Section titled “Message”](#message)

**Type:** String (required)

A descriptive message detailing the update, actions taken, or any relevant information regarding the incident at the time of the report. This message should be clear and concise, providing context to the status change.

**Example Messages:**

* `"Initial detection of elevated error rates on the API. Investigating potential upstream issues."`
* `"Root cause identified as a misconfigured caching layer. Working on a rollback."`
* `"Fix deployed to production. Monitoring service health for full recovery."`
* `"All services restored to normal operation. Incident resolved."`

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Incident Reference](/reference/incident)** - Detailed information on incident creation and lifecycle.
* **[Status Page Reference](/reference/status-page)** - Information on how status reports are displayed on public status pages.

# Subscriber Reference

> Technical specification for managing status page subscribers and their notifications.

## Overview

[Section titled “Overview”](#overview)

A subscriber in OpenStatus is an entity (typically a user or an integration) that opts to receive real-time notifications and updates regarding incidents and status changes on a specific status page. Subscribers play a crucial role in maintaining transparent communication during service disruptions.

**Key functions of subscribers:**

* Receive automated alerts when monitor statuses change or incidents are updated.
* Stay informed about service health without actively monitoring the status page.
* Choose preferred notification channels for receiving updates.

## Subscription Process

[Section titled “Subscription Process”](#subscription-process)

Users typically subscribe to a status page’s updates through a dedicated interface provided on the status page itself. The process involves:

1. **Inputting Contact Information:** Providing an email address, phone number, or other contact details depending on the available notification channels.
2. **Opt-in Confirmation:** Confirming their subscription, often through a verification link sent to the provided contact to prevent unwanted subscriptions.
3. **Channel Selection (Optional):** Selecting which specific notification channels (e.g., email, SMS, Slack webhook) they wish to receive updates through, if multiple options are available.

## Notification Types Received

[Section titled “Notification Types Received”](#notification-types-received)

Subscribers receive notifications for key events affecting the monitored services linked to the status page:

* **Incident Creation:** When a new incident is detected and published.
* **Incident Updates:** When status reports are published for an ongoing incident (e.g., status changes from `investigating` to `identified`, `monitoring`, or `resolved`).
* **Monitor Status Changes:** Direct alerts for individual monitor status changes if configured to do so (less common for public subscribers).

## Subscriber Management

[Section titled “Subscriber Management”](#subscriber-management)

Status page administrators can manage their subscriber lists, including:

* **Viewing Subscribers:** Accessing a list of all active subscribers for a status page.
* **Adding/Removing Subscribers:** Manually adding or removing subscribers.
* **Communication:** Sending ad-hoc notifications to the subscriber list (if supported by the platform).

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Status Page Reference](/reference/status-page)** - Detailed information on managing and configuring status pages.
* **[Notification Channels Reference](/reference/notification)** - Technical specifications for the various notification delivery methods.
* **[Incident Reference](/reference/incident)** - Information about incident creation and management.

# TCP Monitor Reference

> Complete technical specification for TCP service monitoring.

## Overview

[Section titled “Overview”](#overview)

A TCP Monitor is a component that establishes a connection to a specified TCP endpoint (IP address and port) to verify its reachability and responsiveness. This is fundamental for monitoring the availability of services that communicate over TCP, such as databases, mail servers, and custom network services.

**Use cases:**

* Database server availability checks (e.g., PostgreSQL, MySQL).
* Mail server (SMTP, IMAP, POP3) reachability.
* Custom application service port monitoring.
* Validating network connectivity to specific endpoints.

## Configuration

[Section titled “Configuration”](#configuration)

### URI

[Section titled “URI”](#uri)

**Type:** String (required) **Format:** Hostname or IP address with port (e.g., `example.com:8080`, `192.168.1.1:22`)

The endpoint of the TCP service you want to monitor. This includes the hostname or IP address and the port number.

**Examples:**

* `openstat.us:443`
* `db.internal:5432`
* `10.0.0.5:3306`

### Regions

[Section titled “Regions”](#regions)

**Type:** Array of Strings (required) **Format:** Region identifiers (e.g., `iad`, `jnb`)

The geographical regions from which the TCP connection attempt will be initiated. This allows for verification of service availability and network latency across different global locations.

**Africa**

* Johannesburg, South Africa 🇿🇦 (free)

**Asia**

* Hong Kong, Hong Kong 🇭🇰 (free)
* Mumbai, India 🇮🇳
* Singapore, Singapore 🇸🇬
* Tokyo, Japan 🇯🇵

**Europe**

* Amsterdam, Netherlands 🇳🇱 (free)
* Bucharest, Romania 🇷🇴
* Frankfurt, Germany 🇩🇪
* London, United Kingdom 🇬🇧
* Madrid, Spain 🇪🇸
* Paris, France 🇫🇷
* Stockholm, Sweden 🇸🇪
* Warsaw, Poland 🇵🇱

**North America**

* Ashburn, Virginia, USA 🇺🇸 (free)
* Atlanta, Georgia, USA 🇺🇸
* Boston, Massachusetts, USA 🇺🇸
* Chicago, Illinois, USA 🇺🇸
* Dallas, Texas, USA 🇺🇸
* Denver, Colorado, USA 🇺🇸
* Guadalajara, Mexico 🇲🇽
* Los Angeles, California, USA 🇺🇸
* Miami, Florida, USA 🇺🇸
* Montreal, Canada 🇨🇦
* Phoenix, Arizona, USA 🇺🇸
* Queretaro, Mexico 🇲🇽
* Seattle, Washington, USA 🇺🇸
* San Jose, California, USA 🇺🇸
* Toronto, Canada 🇨🇦

**South America**

* Bogota, Colombia 🇨🇴
* Buenos Aires, Argentina 🇦🇷
* Rio de Janeiro, Brazil 🇧🇷
* Sao Paulo, Brazil 🇧🇷 (free)
* Santiago, Chile 🇨🇱

**Oceania**

* Sydney, Australia 🇦🇺 (free)

### Frequency

[Section titled “Frequency”](#frequency)

**Type:** String (required) **Format:** Duration string (e.g., `30s`, `1m`, `1h`)

The interval at which the TCP monitor will attempt to connect to the target URI. Supported frequencies:

* `30 seconds`
* `1 minute`
* `5 minutes`
* `10 minutes`
* `30 minutes`
* `1 hour`

### Response Time Thresholds

[Section titled “Response Time Thresholds”](#response-time-thresholds)

#### Timeout

[Section titled “Timeout”](#timeout)

**Type:** Duration (optional) **Default:** `45 seconds`

The maximum duration to wait for a successful TCP connection. If the connection cannot be established within this time, the check is considered a failure.

#### Degraded

[Section titled “Degraded”](#degraded)

**Type:** Duration (optional)

The duration after which a TCP connection attempt is considered to be in a degraded performance state. This allows for early warning of network latency or service slowdowns.

### Retry

[Section titled “Retry”](#retry)

**Type:** Integer (optional) **Default:** `3`

The number of times the monitor will automatically retry a failed TCP connection attempt before reporting a definitive error. For example: `3`

### OpenTelemetry

[Section titled “OpenTelemetry”](#opentelemetry)

Configures the export of monitoring metrics to an OpenTelemetry-compatible observability platform.

#### OTLP Endpoint

[Section titled “OTLP Endpoint”](#otlp-endpoint)

**Type:** String (optional) **Protocol:** HTTP only

The OTLP (OpenTelemetry Protocol) endpoint URL where collected metrics should be exported. Only HTTP endpoints are supported for metric export.

#### OTLP Headers

[Section titled “OTLP Headers”](#otlp-headers)

**Type:** Key-value pairs (optional)

Custom headers to include when sending metrics to your OTLP endpoint. Commonly used for authentication or tenant identification.

**Common example:**

```plaintext
Authorization: Bearer <your_token>
```

## Related resources

[Section titled “Related resources”](#related-resources)

* **[Create Your First Monitor](/tutorial/how-to-create-monitor)** - Step-by-step tutorial on setting up a monitor.
* **[CLI Reference](/reference/cli-reference)** - Guide to managing OpenStatus monitors programmatically using the command-line interface.

# Terraform Provider Reference

> Technical specification for the OpenStatus Terraform Provider.

## Overview

[Section titled “Overview”](#overview)

The OpenStatus Terraform provider enables you to manage your OpenStatus monitors and status pages programmatically using HashiCorp Terraform. This allows for Infrastructure as Code (IaC) practices, version control, and automated deployment of your monitoring configurations.

**Key capabilities:**

* Define and manage OpenStatus monitors as Terraform resources.
* Automate the deployment and updates of monitoring configurations.
* Integrate OpenStatus into your existing IaC workflows.

## Installation

[Section titled “Installation”](#installation)

To use the OpenStatus Terraform provider, declare it in your Terraform configuration file (`.tf`). Terraform will automatically download and install the provider when you run `terraform init`.

```terraform
terraform {
  required_providers {
    openstatus = {
      source = "openstatusHQ/openstatus"
      version = "~> 0.1" # Use the latest version
    }
  }
}
```

For the latest provider version, refer to the [official Terraform Registry](https://registry.terraform.io/providers/openstatusHQ/openstatus/latest).

## Provider Configuration

[Section titled “Provider Configuration”](#provider-configuration)

The OpenStatus Terraform provider requires authentication via an API token.

### `openstatus_api_token`

[Section titled “openstatus\_api\_token”](#openstatus_api_token)

**Type:** String (required) **Description:** Your OpenStatus API Access Token. This token is used to authenticate your Terraform requests with the OpenStatus API.

**Example:**

```terraform
provider "openstatus" {
  openstatus_api_token = "YOUR_OPENSTATUS_API_TOKEN"
}
```

## Resources

[Section titled “Resources”](#resources)

The provider currently supports managing `openstatus_monitor` resources.

### `openstatus_monitor`

[Section titled “openstatus\_monitor”](#openstatus_monitor)

Manages an OpenStatus monitor. This resource allows you to define and control the parameters of a synthetic monitor.

**Arguments:**

| Argument         | Type                     | Required | Default | Description                                                                                                                      |
| :--------------- | :----------------------- | :------- | :------ | :------------------------------------------------------------------------------------------------------------------------------- |
| `url`            | `string`                 | Yes      |         | The URL or URI of the endpoint to be monitored. Format depends on the monitor type (e.g., full URL for HTTP, host:port for TCP). |
| `regions`        | `list(string)`           | Yes      |         | A list of region identifiers (e.g., `"iad"`, `"jnb"`) from where the monitor checks will be performed.                           |
| `periodicity`    | `string`                 | Yes      |         | The frequency at which the monitor will perform checks. Supported values: `"30s"`, `"1m"`, `"5m"`, `"10m"`, `"30m"`, `"1h"`.     |
| `name`           | `string`                 | Yes      |         | A human-readable name for the monitor.                                                                                           |
| `active`         | `bool`                   | Yes      |         | Specifies whether the monitor is active (`true`) or paused (`false`).                                                            |
| `description`    | `string` (optional)      | No       | `""`    | A detailed description of the monitor’s purpose or configuration.                                                                |
| `monitor_type`   | `string`                 | Yes      |         | The type of monitor to create. Supported values: `"HTTP"`, `"TCP"`, `"DNS"`                                                      |
| `method`         | `string` (optional)      | No       | `"GET"` | (HTTP monitors only) The HTTP method to use for the request (e.g., `"GET"`, `"POST"`).                                           |
| `body`           | `string` (optional)      | No       | `""`    | (HTTP monitors only) The request body to send for `POST`, `PUT`, `PATCH` methods.                                                |
| `headers`        | `map(string)` (optional) | No       | `{}`    | (HTTP monitors only) A map of custom HTTP headers to include with the request.                                                   |
| `timeout`        | `string` (optional)      | No       | `"45s"` | The maximum duration to wait for a response. Format: duration string (e.g., `"30s"`, `"1m"`).                                    |
| `degraded_after` | `string` (optional)      | No       | `""`    | The duration after which a response is considered degraded. Format: duration string.                                             |
| `retries`        | `number` (optional)      | No       | `3`     | The number of times the monitor will retry a failed check.                                                                       |
| `public`         | `bool` (optional)        | No       | `false` | Controls whether monitor data is accessible on your public status page.                                                          |
| `otlp_endpoint`  | `string` (optional)      | No       | `""`    | The OTLP (OpenTelemetry Protocol) endpoint URL for exporting metrics.                                                            |
| `otlp_headers`   | `map(string)` (optional) | No       | `{}`    | Custom headers to include when exporting metrics to your OTLP endpoint.                                                          |

**Example Usage:**

```terraform
resource "openstatus_monitor" "my_website_monitor" {
  name        = "My Website Availability"
  description = "Checks the main website for uptime and response time."
  url         = "https://www.example.com"
  monitor_type = "HTTP"
  method      = "GET"
  regions     = ["us-east-1", "eu-west-1"]
  periodicity = "1m"
  active      = true
  public      = true
  timeout     = "60s"
}


resource "openstatus_monitor" "internal_api_monitor" {
  name        = "Internal API Health Check"
  description = "Monitors the health of a critical internal API."
  url         = "https://api.internal.corp:8443/health"
  monitor_type = "HTTP"
  method      = "GET"
  regions     = ["private-location-id"]
  periodicity = "5m"
  active      = true
  public      = false
  headers = {
    "Authorization" = "Bearer ${var.internal_api_token}"
    "Accept"        = "application/json"
  }
}


resource "openstatus_monitor" "database_port_monitor" {
  name        = "Database TCP Port Check"
  description = "Ensures the PostgreSQL port is open and reachable."
  url         = "db.example.com:5432"
  monitor_type = "TCP"
  regions     = ["us-west-2"]
  periodicity = "30s"
  active      = true
}
```

## Related resources

[Section titled “Related resources”](#related-resources)

* **[HTTP Monitor Reference](/reference/http-monitor)** - Detailed specification for HTTP monitor configuration.
* **[TCP Monitor Reference](/reference/tcp-monitor)** - Detailed specification for TCP monitor configuration.
* **[DNS Monitor Reference](/reference/dns-monitor)** - Detailed specification for DNS monitor configuration.
* **[CLI Reference](/reference/cli-reference)** - Manage monitors using the OpenStatus command-line interface.

# Getting Started

> Install and start using the OpenStatus Node.js SDK

## Get Your API Key

[Section titled “Get Your API Key”](#get-your-api-key)

Before using the SDK, you need an API key:

1. Log in to the [OpenStatus dashboard](https://www.openstatus.dev/app/login)
2. Go to **Settings** > **API Keys**
3. Click **Create API Key** and copy it

Tip

Store your API key as an environment variable (`OPENSTATUS_API_KEY`) — never commit it to source control.

## Installation

[Section titled “Installation”](#installation)

### npm

[Section titled “npm”](#npm)

```bash
npm install @openstatus/sdk-node
```

### JSR

[Section titled “JSR”](#jsr)

```bash
npx jsr add @openstatus/sdk-node
```

### Deno

[Section titled “Deno”](#deno)

```typescript
import { createOpenStatusClient } from "jsr:@openstatus/sdk-node";
```

### Bun

[Section titled “Bun”](#bun)

```bash
bun add @openstatus/sdk-node
```

## Quick Start

[Section titled “Quick Start”](#quick-start)

```typescript
import {
  createOpenStatusClient,
  Periodicity,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


// Create an HTTP monitor
const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "My API",
    url: "https://api.example.com/health",
    periodicity: Periodicity.PERIODICITY_1M,
    regions: [Region.FLY_AMS, Region.FLY_IAD, Region.FLY_SYD],
    active: true,
  },
});


console.log(`Monitor created: ${monitor?.id}`);


// List all monitors
const { httpMonitors, tcpMonitors, dnsMonitors, totalSize } =
  await client.monitor.v1.MonitorService.listMonitors({});


console.log(`Found ${totalSize} monitors`);
```

## Runtime Support

[Section titled “Runtime Support”](#runtime-support)

| Runtime | Version | Module Format |
| ------- | ------- | ------------- |
| Node.js | 18+     | ESM and CJS   |
| Deno    | 2+      | ESM (native)  |
| Bun     | Latest  | ESM           |

## Full Workflow Example

[Section titled “Full Workflow Example”](#full-workflow-example)

A complete example: create a monitor, set up a status page, add the monitor as a component, configure a Slack notification, and check overall status.

```typescript
import {
  createOpenStatusClient,
  NotificationProvider,
  Periodicity,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


// 1. Check API health
const health = await client.health.v1.HealthService.check({});
console.log(`API status: ${health.status}`);


// 2. Create an HTTP monitor
const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "Production API",
    url: "https://api.example.com/health",
    periodicity: Periodicity.PERIODICITY_1M,
    regions: [Region.FLY_AMS, Region.FLY_IAD, Region.FLY_SYD],
    active: true,
  },
});


// 3. Create a status page
const { statusPage } = await client.statusPage.v1.StatusPageService
  .createStatusPage({
    title: "Example Status",
    slug: "example-status",
    description: "Status page for Example services",
  });


// 4. Add the monitor as a component
const { component } = await client.statusPage.v1.StatusPageService
  .addMonitorComponent({
    pageId: statusPage!.id,
    monitorId: monitor!.id,
    name: "Production API",
  });


// 5. Set up Slack notifications
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Slack Alerts",
    provider: NotificationProvider.SLACK,
    data: {
      data: {
        case: "slack",
        value: { webhookUrl: "https://hooks.slack.com/services/..." },
      },
    },
    monitorIds: [monitor!.id],
  });


// 6. Check overall status
const { overallStatus } = await client.statusPage.v1.StatusPageService
  .getOverallStatus({
    identifier: { case: "id", value: statusPage!.id },
  });


console.log(`Overall status: ${overallStatus}`);
```

# Authentication

> Configure API key authentication for the OpenStatus Node.js SDK

## Recommended: createOpenStatusClient

[Section titled “Recommended: createOpenStatusClient”](#recommended-createopenstatusclient)

Create a client with your API key. The key is automatically included in all requests via an interceptor.

```typescript
import { createOpenStatusClient } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


// No headers needed on individual calls
const { httpMonitors } = await client.monitor.v1.MonitorService.listMonitors({});
```

## Alternative: Manual Headers

[Section titled “Alternative: Manual Headers”](#alternative-manual-headers)

Use the default `openstatus` client and pass headers on each call.

```typescript
import { openstatus } from "@openstatus/sdk-node";


const headers = {
  "x-openstatus-key": process.env.OPENSTATUS_API_KEY,
};


await openstatus.monitor.v1.MonitorService.listMonitors({}, { headers });
```

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

| Variable             | Description             | Default                          |
| -------------------- | ----------------------- | -------------------------------- |
| `OPENSTATUS_API_KEY` | Your OpenStatus API key | Required for authenticated calls |
| `OPENSTATUS_API_URL` | Custom API endpoint     | `https://api.openstatus.dev/rpc` |

Get your API key from the [OpenStatus dashboard](https://www.openstatus.dev/app).

## Custom Base URL

[Section titled “Custom Base URL”](#custom-base-url)

For self-hosted instances or staging environments:

```typescript
import { createOpenStatusClient } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
  baseUrl: "https://api.staging.example.com/rpc",
});
```

The `baseUrl` option takes precedence over the `OPENSTATUS_API_URL` environment variable.

# Error Handling

> Handle errors and implement retry strategies with the OpenStatus Node.js SDK

The SDK uses ConnectRPC. Errors are thrown as `ConnectError` instances from the `@connectrpc/connect` package.

```typescript
import { ConnectError } from "@connectrpc/connect";


try {
  await client.monitor.v1.MonitorService.deleteMonitor({ id: "invalid" });
} catch (error) {
  if (error instanceof ConnectError) {
    console.error(`Code: ${error.code}`);
    console.error(`Message: ${error.message}`);
  }
}
```

## Common Error Codes

[Section titled “Common Error Codes”](#common-error-codes)

| Code                | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `unauthenticated`   | Missing or invalid API key                                            |
| `not_found`         | Resource does not exist                                               |
| `invalid_argument`  | Validation failure (e.g., missing required field, value out of range) |
| `permission_denied` | No access to this workspace or resource                               |
| `already_exists`    | Duplicate resource (e.g., slug already taken)                         |

## Retry Strategy

[Section titled “Retry Strategy”](#retry-strategy)

ConnectRPC does not retry by default. For transient failures (`unavailable`, `deadline_exceeded`), implement your own retry logic:

```typescript
import { ConnectError } from "@connectrpc/connect";


async function withRetry<T>(fn: () => Promise<T>, maxRetries = 3): Promise<T> {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (
        error instanceof ConnectError &&
        (error.code === "unavailable" || error.code === "deadline_exceeded") &&
        attempt < maxRetries
      ) {
        await new Promise((resolve) => setTimeout(resolve, 1000 * 2 ** attempt));
        continue;
      }
      throw error;
    }
  }
  throw new Error("Unreachable");
}


const { httpMonitors } = await withRetry(() =>
  client.monitor.v1.MonitorService.listMonitors({})
);
```

# Getting Started

> Install and start using the OpenStatus Node.js SDK

## Get Your API Key

[Section titled “Get Your API Key”](#get-your-api-key)

Before using the SDK, you need an API key:

1. Log in to the [OpenStatus dashboard](https://www.openstatus.dev/app/login)
2. Go to **Settings** > **API Keys**
3. Click **Create API Key** and copy it

Tip

Store your API key as an environment variable (`OPENSTATUS_API_KEY`) — never commit it to source control.

## Installation

[Section titled “Installation”](#installation)

### npm

[Section titled “npm”](#npm)

```bash
npm install @openstatus/sdk-node
```

### JSR

[Section titled “JSR”](#jsr)

```bash
npx jsr add @openstatus/sdk-node
```

### Deno

[Section titled “Deno”](#deno)

```typescript
import { createOpenStatusClient } from "jsr:@openstatus/sdk-node";
```

### Bun

[Section titled “Bun”](#bun)

```bash
bun add @openstatus/sdk-node
```

## Quick Start

[Section titled “Quick Start”](#quick-start)

```typescript
import {
  createOpenStatusClient,
  Periodicity,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


// Create an HTTP monitor
const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "My API",
    url: "https://api.example.com/health",
    periodicity: Periodicity.PERIODICITY_1M,
    regions: [Region.FLY_AMS, Region.FLY_IAD, Region.FLY_SYD],
    active: true,
  },
});


console.log(`Monitor created: ${monitor?.id}`);


// List all monitors
const { httpMonitors, tcpMonitors, dnsMonitors, totalSize } =
  await client.monitor.v1.MonitorService.listMonitors({});


console.log(`Found ${totalSize} monitors`);
```

## Runtime Support

[Section titled “Runtime Support”](#runtime-support)

| Runtime | Version | Module Format |
| ------- | ------- | ------------- |
| Node.js | 18+     | ESM and CJS   |
| Deno    | 2+      | ESM (native)  |
| Bun     | Latest  | ESM           |

## Full Workflow Example

[Section titled “Full Workflow Example”](#full-workflow-example)

A complete example: create a monitor, set up a status page, add the monitor as a component, configure a Slack notification, and check overall status.

```typescript
import {
  createOpenStatusClient,
  NotificationProvider,
  Periodicity,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


// 1. Check API health
const health = await client.health.v1.HealthService.check({});
console.log(`API status: ${health.status}`);


// 2. Create an HTTP monitor
const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "Production API",
    url: "https://api.example.com/health",
    periodicity: Periodicity.PERIODICITY_1M,
    regions: [Region.FLY_AMS, Region.FLY_IAD, Region.FLY_SYD],
    active: true,
  },
});


// 3. Create a status page
const { statusPage } = await client.statusPage.v1.StatusPageService
  .createStatusPage({
    title: "Example Status",
    slug: "example-status",
    description: "Status page for Example services",
  });


// 4. Add the monitor as a component
const { component } = await client.statusPage.v1.StatusPageService
  .addMonitorComponent({
    pageId: statusPage!.id,
    monitorId: monitor!.id,
    name: "Production API",
  });


// 5. Set up Slack notifications
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Slack Alerts",
    provider: NotificationProvider.SLACK,
    data: {
      data: {
        case: "slack",
        value: { webhookUrl: "https://hooks.slack.com/services/..." },
      },
    },
    monitorIds: [monitor!.id],
  });


// 6. Check overall status
const { overallStatus } = await client.statusPage.v1.StatusPageService
  .getOverallStatus({
    identifier: { case: "id", value: statusPage!.id },
  });


console.log(`Overall status: ${overallStatus}`);
```

# Health Service

> Check the OpenStatus API health status using the Node.js SDK

Check API health status. No authentication required.

```typescript
import { openstatus, ServingStatus } from "@openstatus/sdk-node";


const { status } = await openstatus.health.v1.HealthService.check({});
console.log(ServingStatus[status]); // "SERVING"
```

Or with a configured client:

```typescript
import { createOpenStatusClient, ServingStatus } from "@openstatus/sdk-node";


const client = createOpenStatusClient();
const { status } = await client.health.v1.HealthService.check({});
console.log(ServingStatus[status]); // "SERVING"
```

# Maintenance Service

> Manage scheduled maintenance windows with the OpenStatus Node.js SDK

Manage scheduled maintenance windows. The Maintenance Service provides 5 RPC methods.

## Create Maintenance Window

[Section titled “Create Maintenance Window”](#create-maintenance-window)

```typescript
const { maintenance } = await client.maintenance.v1.MaintenanceService
  .createMaintenance({
    title: "Database Upgrade",
    message: "We will be upgrading our database infrastructure.",
    from: "2024-01-20T02:00:00Z",
    to: "2024-01-20T04:00:00Z",
    pageId: "page_123",
    pageComponentIds: ["comp_456"],
    notify: true,
  });


console.log(`Maintenance created: ${maintenance?.id}`);
```

All date fields (`from`, `to`) must be in RFC 3339 format.

## List Maintenances

[Section titled “List Maintenances”](#list-maintenances)

List maintenance windows with optional page filtering.

```typescript
const { maintenances, totalSize } = await client.maintenance.v1
  .MaintenanceService.listMaintenances({
    limit: 10,
    offset: 0,
    pageId: "page_123",
  });


console.log(`Found ${totalSize} maintenance windows`);
```

## Get / Update / Delete Maintenance Windows

[Section titled “Get / Update / Delete Maintenance Windows”](#get--update--delete-maintenance-windows)

### Get Maintenance

[Section titled “Get Maintenance”](#get-maintenance)

```typescript
const { maintenance } = await client.maintenance.v1.MaintenanceService
  .getMaintenance({ id: "maint_123" });


console.log(`Title: ${maintenance?.title}`);
console.log(`From: ${maintenance?.from}`);
console.log(`To: ${maintenance?.to}`);
```

### Update Maintenance

[Section titled “Update Maintenance”](#update-maintenance)

```typescript
const { maintenance } = await client.maintenance.v1.MaintenanceService
  .updateMaintenance({
    id: "maint_123",
    title: "Extended Database Upgrade",
    to: "2024-01-20T06:00:00Z",
  });
```

### Delete Maintenance

[Section titled “Delete Maintenance”](#delete-maintenance)

```typescript
const { success } = await client.maintenance.v1.MaintenanceService
  .deleteMaintenance({ id: "maint_123" });
```

# Monitor Service

> Create and manage HTTP, TCP, and DNS monitors with the OpenStatus Node.js SDK

Manage HTTP, TCP, and DNS monitors. The Monitor Service provides 12 RPC methods for creating, updating, listing, triggering, deleting, and querying monitor status and metrics.

All examples assume you have created a client:

```typescript
import { createOpenStatusClient } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});
```

## HTTP Monitors

[Section titled “HTTP Monitors”](#http-monitors)

### Create HTTP Monitor

[Section titled “Create HTTP Monitor”](#create-http-monitor)

```typescript
import {
  createOpenStatusClient,
  HTTPMethod,
  NumberComparator,
  Periodicity,
  Region,
  StringComparator,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "My API",
    url: "https://api.example.com/health",
    periodicity: Periodicity.PERIODICITY_1M,
    method: HTTPMethod.HTTP_METHOD_GET,
    regions: [Region.FLY_AMS, Region.FLY_IAD, Region.FLY_SYD],
    active: true,
    timeout: BigInt(30000),
    retry: BigInt(3),
    followRedirects: true,
    degradedAt: BigInt(5000),
    headers: [
      { key: "Authorization", value: "Bearer my-token" },
    ],
    statusCodeAssertions: [
      { comparator: NumberComparator.EQUAL, target: BigInt(200) },
    ],
    bodyAssertions: [
      { comparator: StringComparator.CONTAINS, target: '"status":"ok"' },
    ],
    headerAssertions: [
      {
        key: "content-type",
        comparator: StringComparator.CONTAINS,
        target: "application/json",
      },
    ],
    description: "Health check for the production API",
    public: false,
    openTelemetry: {
      endpoint: "https://otel.example.com/v1/traces",
      headers: [{ key: "Authorization", value: "Bearer otel-token" }],
    },
  },
});


console.log(`Created monitor: ${monitor?.id}`);
```

### Update HTTP Monitor

[Section titled “Update HTTP Monitor”](#update-http-monitor)

Updates are partial — only include the fields you want to change.

```typescript
const { monitor } = await client.monitor.v1.MonitorService.updateHTTPMonitor({
  id: "mon_123",
  monitor: {
    name: "Updated API Monitor",
    active: false,
  },
});
```

### HTTP Monitor Options

[Section titled “HTTP Monitor Options”](#http-monitor-options)

| Option                 | Type                   | Required | Description                                 |
| ---------------------- | ---------------------- | -------- | ------------------------------------------- |
| `name`                 | string                 | Yes      | Monitor name (max 256 chars)                |
| `url`                  | string                 | Yes      | URL to monitor (max 2048 chars)             |
| `periodicity`          | Periodicity            | Yes      | Check interval                              |
| `method`               | HTTPMethod             | No       | HTTP method (default: GET)                  |
| `body`                 | string                 | No       | Request body                                |
| `headers`              | Headers\[]             | No       | Custom headers `{ key, value }[]`           |
| `timeout`              | bigint                 | No       | Timeout in ms (default: 45000, max: 120000) |
| `retry`                | bigint                 | No       | Retry attempts (default: 3, max: 10)        |
| `followRedirects`      | boolean                | No       | Follow redirects (default: true)            |
| `regions`              | Region\[]              | No       | Regions for checks                          |
| `active`               | boolean                | No       | Enable monitoring (default: false)          |
| `public`               | boolean                | No       | Public visibility (default: false)          |
| `degradedAt`           | bigint                 | No       | Latency threshold (ms) for degraded status  |
| `description`          | string                 | No       | Monitor description (max 1024 chars)        |
| `statusCodeAssertions` | StatusCodeAssertion\[] | No       | Status code assertions                      |
| `bodyAssertions`       | BodyAssertion\[]       | No       | Body assertions                             |
| `headerAssertions`     | HeaderAssertion\[]     | No       | Header assertions                           |
| `openTelemetry`        | OpenTelemetryConfig    | No       | OpenTelemetry export configuration          |

## TCP Monitors

[Section titled “TCP Monitors”](#tcp-monitors)

### Create TCP Monitor

[Section titled “Create TCP Monitor”](#create-tcp-monitor)

```typescript
import {
  createOpenStatusClient,
  Periodicity,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { monitor } = await client.monitor.v1.MonitorService.createTCPMonitor({
  monitor: {
    name: "Database",
    uri: "db.example.com:5432",
    periodicity: Periodicity.PERIODICITY_5M,
    regions: [Region.FLY_AMS, Region.FLY_IAD],
    active: true,
  },
});
```

### Update TCP Monitor

[Section titled “Update TCP Monitor”](#update-tcp-monitor)

```typescript
const { monitor } = await client.monitor.v1.MonitorService.updateTCPMonitor({
  id: "mon_123",
  monitor: {
    name: "Updated Database Monitor",
  },
});
```

### TCP Monitor Options

[Section titled “TCP Monitor Options”](#tcp-monitor-options)

| Option          | Type                | Required | Description                                 |
| --------------- | ------------------- | -------- | ------------------------------------------- |
| `name`          | string              | Yes      | Monitor name (max 256 chars)                |
| `uri`           | string              | Yes      | `host:port` to monitor (max 2048 chars)     |
| `periodicity`   | Periodicity         | Yes      | Check interval                              |
| `timeout`       | bigint              | No       | Timeout in ms (default: 45000, max: 120000) |
| `retry`         | bigint              | No       | Retry attempts (default: 3, max: 10)        |
| `regions`       | Region\[]           | No       | Regions for checks                          |
| `active`        | boolean             | No       | Enable monitoring (default: false)          |
| `public`        | boolean             | No       | Public visibility (default: false)          |
| `degradedAt`    | bigint              | No       | Latency threshold (ms) for degraded status  |
| `description`   | string              | No       | Monitor description (max 1024 chars)        |
| `openTelemetry` | OpenTelemetryConfig | No       | OpenTelemetry export configuration          |

## DNS Monitors

[Section titled “DNS Monitors”](#dns-monitors)

### Create DNS Monitor

[Section titled “Create DNS Monitor”](#create-dns-monitor)

```typescript
import {
  createOpenStatusClient,
  Periodicity,
  RecordComparator,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { monitor } = await client.monitor.v1.MonitorService.createDNSMonitor({
  monitor: {
    name: "DNS Check",
    uri: "example.com",
    periodicity: Periodicity.PERIODICITY_10M,
    regions: [Region.FLY_AMS],
    active: true,
    recordAssertions: [
      {
        record: "A",
        comparator: RecordComparator.EQUAL,
        target: "93.184.216.34",
      },
      {
        record: "CNAME",
        comparator: RecordComparator.CONTAINS,
        target: "cdn",
      },
    ],
  },
});
```

### Update DNS Monitor

[Section titled “Update DNS Monitor”](#update-dns-monitor)

```typescript
const { monitor } = await client.monitor.v1.MonitorService.updateDNSMonitor({
  id: "mon_123",
  monitor: {
    name: "Updated DNS Check",
  },
});
```

### DNS Monitor Options

[Section titled “DNS Monitor Options”](#dns-monitor-options)

| Option             | Type                | Required | Description                                 |
| ------------------ | ------------------- | -------- | ------------------------------------------- |
| `name`             | string              | Yes      | Monitor name (max 256 chars)                |
| `uri`              | string              | Yes      | Domain to resolve (max 2048 chars)          |
| `periodicity`      | Periodicity         | Yes      | Check interval                              |
| `timeout`          | bigint              | No       | Timeout in ms (default: 45000, max: 120000) |
| `retry`            | bigint              | No       | Retry attempts (default: 3, max: 10)        |
| `regions`          | Region\[]           | No       | Regions for checks                          |
| `active`           | boolean             | No       | Enable monitoring (default: false)          |
| `public`           | boolean             | No       | Public visibility (default: false)          |
| `degradedAt`       | bigint              | No       | Latency threshold (ms) for degraded status  |
| `description`      | string              | No       | Monitor description (max 1024 chars)        |
| `recordAssertions` | RecordAssertion\[]  | No       | DNS record assertions                       |
| `openTelemetry`    | OpenTelemetryConfig | No       | OpenTelemetry export configuration          |

## List Monitors

[Section titled “List Monitors”](#list-monitors)

List all monitors with offset-based pagination. Returns monitors grouped by type.

```typescript
const { httpMonitors, tcpMonitors, dnsMonitors, totalSize } =
  await client.monitor.v1.MonitorService.listMonitors({
    limit: 10,
    offset: 0,
  });


console.log(`Total: ${totalSize}`);
console.log(`HTTP: ${httpMonitors.length}`);
console.log(`TCP: ${tcpMonitors.length}`);
console.log(`DNS: ${dnsMonitors.length}`);
```

Pagination parameters:

| Parameter | Type              | Description                               |
| --------- | ----------------- | ----------------------------------------- |
| `limit`   | number (optional) | Max results to return (1–100, default 50) |
| `offset`  | number (optional) | Number of results to skip (default 0)     |

## Get Monitor

[Section titled “Get Monitor”](#get-monitor)

Get a single monitor by ID. The response uses a `MonitorConfig` oneof type that contains one of HTTP, TCP, or DNS configuration.

```typescript
const { monitor } = await client.monitor.v1.MonitorService.getMonitor({
  id: "mon_123",
});


if (monitor?.config.case === "http") {
  console.log(`HTTP Monitor: ${monitor.config.value.name} — ${monitor.config.value.url}`);
} else if (monitor?.config.case === "tcp") {
  console.log(`TCP Monitor: ${monitor.config.value.name} — ${monitor.config.value.uri}`);
} else if (monitor?.config.case === "dns") {
  console.log(`DNS Monitor: ${monitor.config.value.name} — ${monitor.config.value.uri}`);
}
```

## Trigger Monitor

[Section titled “Trigger Monitor”](#trigger-monitor)

Trigger an immediate check for a monitor.

```typescript
const { success } = await client.monitor.v1.MonitorService.triggerMonitor({
  id: "mon_123",
});


console.log(`Trigger successful: ${success}`);
```

## Delete Monitor

[Section titled “Delete Monitor”](#delete-monitor)

```typescript
const { success } = await client.monitor.v1.MonitorService.deleteMonitor({
  id: "mon_123",
});
```

## Get Monitor Status

[Section titled “Get Monitor Status”](#get-monitor-status)

Get the current status of a monitor across all configured regions.

```typescript
import {
  createOpenStatusClient,
  MonitorStatus,
  Region,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { id, regions } = await client.monitor.v1.MonitorService.getMonitorStatus(
  { id: "mon_123" },
);


for (const { region, status } of regions) {
  console.log(`${Region[region]}: ${MonitorStatus[status]}`);
}
```

## Get Monitor Summary

[Section titled “Get Monitor Summary”](#get-monitor-summary)

Get aggregated metrics and latency percentiles for a monitor over a time range.

```typescript
import { createOpenStatusClient, TimeRange } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const summary = await client.monitor.v1.MonitorService.getMonitorSummary({
  id: "mon_123",
  timeRange: TimeRange.TIME_RANGE_7D,
  regions: [],
});


console.log(`Last ping: ${summary.lastPingAt}`);
console.log(`Successful: ${summary.totalSuccessful}`);
console.log(`Degraded: ${summary.totalDegraded}`);
console.log(`Failed: ${summary.totalFailed}`);
console.log(`P50: ${summary.p50}ms`);
console.log(`P75: ${summary.p75}ms`);
console.log(`P90: ${summary.p90}ms`);
console.log(`P95: ${summary.p95}ms`);
console.log(`P99: ${summary.p99}ms`);
```

The latency fields (`p50`, `p75`, `p90`, `p95`, `p99`) and count fields (`totalSuccessful`, `totalDegraded`, `totalFailed`) are `bigint` values. The `regions` parameter is optional — pass an empty array to get metrics across all regions.

# Notification Service

> Manage notification channels and providers with the OpenStatus Node.js SDK

Manage notification channels for monitor alerts. Supports 12 providers. The Notification Service provides 7 RPC methods.

## Create Notification

[Section titled “Create Notification”](#create-notification)

```typescript
import {
  createOpenStatusClient,
  NotificationProvider,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Slack Alerts",
    provider: NotificationProvider.SLACK,
    data: {
      data: {
        case: "slack",
        value: { webhookUrl: "https://hooks.slack.com/services/..." },
      },
    },
    monitorIds: ["mon_123", "mon_456"],
  });


console.log(`Notification created: ${notification?.id}`);
```

The `data` field uses a nested oneof pattern: the outer `data` is the `NotificationData` message, and `data.data` is the oneof that selects the provider-specific configuration. The `case` must match the provider type in lowercase.

## Provider Configurations

[Section titled “Provider Configurations”](#provider-configurations)

Each provider shown as a complete `createNotification` call.

### Slack

[Section titled “Slack”](#slack)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Slack Alerts",
    provider: NotificationProvider.SLACK,
    data: {
      data: {
        case: "slack",
        value: { webhookUrl: "https://hooks.slack.com/services/..." },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Discord

[Section titled “Discord”](#discord)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Discord Alerts",
    provider: NotificationProvider.DISCORD,
    data: {
      data: {
        case: "discord",
        value: { webhookUrl: "https://discord.com/api/webhooks/..." },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Email

[Section titled “Email”](#email)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Email Alerts",
    provider: NotificationProvider.EMAIL,
    data: {
      data: {
        case: "email",
        value: { email: "alerts@example.com" },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### PagerDuty

[Section titled “PagerDuty”](#pagerduty)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "PagerDuty Alerts",
    provider: NotificationProvider.PAGERDUTY,
    data: {
      data: {
        case: "pagerduty",
        value: { integrationKey: "your-integration-key" },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Opsgenie

[Section titled “Opsgenie”](#opsgenie)

```typescript
import { NotificationProvider, OpsgenieRegion } from "@openstatus/sdk-node";


const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Opsgenie Alerts",
    provider: NotificationProvider.OPSGENIE,
    data: {
      data: {
        case: "opsgenie",
        value: { apiKey: "your-api-key", region: OpsgenieRegion.US },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Telegram

[Section titled “Telegram”](#telegram)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Telegram Alerts",
    provider: NotificationProvider.TELEGRAM,
    data: {
      data: {
        case: "telegram",
        value: { chatId: "123456789" },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Google Chat

[Section titled “Google Chat”](#google-chat)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Google Chat Alerts",
    provider: NotificationProvider.GOOGLE_CHAT,
    data: {
      data: {
        case: "googleChat",
        value: { webhookUrl: "https://chat.googleapis.com/v1/spaces/..." },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Grafana OnCall

[Section titled “Grafana OnCall”](#grafana-oncall)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Grafana OnCall",
    provider: NotificationProvider.GRAFANA_ONCALL,
    data: {
      data: {
        case: "grafanaOncall",
        value: { webhookUrl: "https://oncall.example.com/..." },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Ntfy

[Section titled “Ntfy”](#ntfy)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Ntfy Alerts",
    provider: NotificationProvider.NTFY,
    data: {
      data: {
        case: "ntfy",
        value: {
          topic: "my-alerts",
          serverUrl: "https://ntfy.sh",
          token: "tk_...",
        },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### SMS

[Section titled “SMS”](#sms)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "SMS Alerts",
    provider: NotificationProvider.SMS,
    data: {
      data: {
        case: "sms",
        value: { phoneNumber: "+1234567890" },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### WhatsApp

[Section titled “WhatsApp”](#whatsapp)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "WhatsApp Alerts",
    provider: NotificationProvider.WHATSAPP,
    data: {
      data: {
        case: "whatsapp",
        value: { phoneNumber: "+1234567890" },
      },
    },
    monitorIds: ["mon_123"],
  });
```

### Custom Webhook

[Section titled “Custom Webhook”](#custom-webhook)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .createNotification({
    name: "Custom Webhook",
    provider: NotificationProvider.WEBHOOK,
    data: {
      data: {
        case: "webhook",
        value: {
          endpoint: "https://api.example.com/webhook",
          headers: [
            { key: "Authorization", value: "Bearer token" },
            { key: "X-Custom-Header", value: "value" },
          ],
        },
      },
    },
    monitorIds: ["mon_123"],
  });
```

## Send Test Notification

[Section titled “Send Test Notification”](#send-test-notification)

Verify a notification configuration without creating a channel.

```typescript
import { NotificationProvider } from "@openstatus/sdk-node";


const { success, errorMessage } = await client.notification.v1
  .NotificationService.sendTestNotification({
    provider: NotificationProvider.SLACK,
    data: {
      data: {
        case: "slack",
        value: { webhookUrl: "https://hooks.slack.com/services/..." },
      },
    },
  });


if (success) {
  console.log("Test notification sent successfully");
} else {
  console.log(`Test failed: ${errorMessage}`);
}
```

## Check Notification Limits

[Section titled “Check Notification Limits”](#check-notification-limits)

Check if the workspace has reached its notification channel limit.

```typescript
const { limitReached, currentCount, maxCount } = await client.notification.v1
  .NotificationService.checkNotificationLimit({});


console.log(`${currentCount}/${maxCount} notification channels used`);
if (limitReached) {
  console.log("Notification limit reached — upgrade your plan");
}
```

## List / Get / Update / Delete Notifications

[Section titled “List / Get / Update / Delete Notifications”](#list--get--update--delete-notifications)

### List Notifications

[Section titled “List Notifications”](#list-notifications)

```typescript
const { notifications, totalSize } = await client.notification.v1
  .NotificationService.listNotifications({ limit: 10, offset: 0 });


console.log(`Found ${totalSize} notification channels`);
```

### Get Notification

[Section titled “Get Notification”](#get-notification)

```typescript
import { NotificationProvider } from "@openstatus/sdk-node";


const { notification } = await client.notification.v1.NotificationService
  .getNotification({ id: "notif_123" });


console.log(`Name: ${notification?.name}`);
console.log(`Provider: ${NotificationProvider[notification?.provider ?? 0]}`);
```

### Update Notification

[Section titled “Update Notification”](#update-notification)

```typescript
const { notification } = await client.notification.v1.NotificationService
  .updateNotification({
    id: "notif_123",
    name: "Updated Slack Alerts",
    monitorIds: ["mon_123", "mon_456", "mon_789"],
  });
```

### Delete Notification

[Section titled “Delete Notification”](#delete-notification)

```typescript
const { success } = await client.notification.v1.NotificationService
  .deleteNotification({ id: "notif_123" });
```

# Reference

> Complete reference for enums, regions, assertions, and TypeScript type exports in the OpenStatus Node.js SDK

## Enums

[Section titled “Enums”](#enums)

### Periodicity

[Section titled “Periodicity”](#periodicity)

| Value             | Description      |
| ----------------- | ---------------- |
| `PERIODICITY_30S` | Every 30 seconds |
| `PERIODICITY_1M`  | Every 1 minute   |
| `PERIODICITY_5M`  | Every 5 minutes  |
| `PERIODICITY_10M` | Every 10 minutes |
| `PERIODICITY_30M` | Every 30 minutes |
| `PERIODICITY_1H`  | Every 1 hour     |

### HTTPMethod

[Section titled “HTTPMethod”](#httpmethod)

| Value                 | Description |
| --------------------- | ----------- |
| `HTTP_METHOD_GET`     | GET         |
| `HTTP_METHOD_POST`    | POST        |
| `HTTP_METHOD_HEAD`    | HEAD        |
| `HTTP_METHOD_PUT`     | PUT         |
| `HTTP_METHOD_PATCH`   | PATCH       |
| `HTTP_METHOD_DELETE`  | DELETE      |
| `HTTP_METHOD_TRACE`   | TRACE       |
| `HTTP_METHOD_CONNECT` | CONNECT     |
| `HTTP_METHOD_OPTIONS` | OPTIONS     |

### MonitorStatus

[Section titled “MonitorStatus”](#monitorstatus)

| Value      | Description                |
| ---------- | -------------------------- |
| `ACTIVE`   | Monitor is healthy         |
| `DEGRADED` | Latency threshold exceeded |
| `ERROR`    | Monitor is failing         |

### TimeRange

[Section titled “TimeRange”](#timerange)

| Value            | Description   |
| ---------------- | ------------- |
| `TIME_RANGE_1D`  | Last 24 hours |
| `TIME_RANGE_7D`  | Last 7 days   |
| `TIME_RANGE_14D` | Last 14 days  |

### StatusReportStatus

[Section titled “StatusReportStatus”](#statusreportstatus)

| Value           | Description                      |
| --------------- | -------------------------------- |
| `INVESTIGATING` | Actively investigating the issue |
| `IDENTIFIED`    | Root cause has been identified   |
| `MONITORING`    | Fix deployed, monitoring         |
| `RESOLVED`      | Issue fully resolved             |

### OverallStatus

[Section titled “OverallStatus”](#overallstatus)

| Value            | Description                 |
| ---------------- | --------------------------- |
| `OPERATIONAL`    | All systems operational     |
| `DEGRADED`       | Performance is degraded     |
| `PARTIAL_OUTAGE` | Some systems are down       |
| `MAJOR_OUTAGE`   | Major systems are down      |
| `MAINTENANCE`    | Scheduled maintenance       |
| `UNKNOWN`        | Status cannot be determined |

### NotificationProvider

[Section titled “NotificationProvider”](#notificationprovider)

| Value            | Description         |
| ---------------- | ------------------- |
| `DISCORD`        | Discord webhook     |
| `EMAIL`          | Email notification  |
| `GOOGLE_CHAT`    | Google Chat webhook |
| `GRAFANA_ONCALL` | Grafana OnCall      |
| `NTFY`           | Ntfy push service   |
| `PAGERDUTY`      | PagerDuty           |
| `OPSGENIE`       | Opsgenie            |
| `SLACK`          | Slack webhook       |
| `SMS`            | SMS notification    |
| `TELEGRAM`       | Telegram bot        |
| `WEBHOOK`        | Custom webhook      |
| `WHATSAPP`       | WhatsApp            |

### OpsgenieRegion

[Section titled “OpsgenieRegion”](#opsgenieregion)

| Value | Description |
| ----- | ----------- |
| `US`  | US region   |
| `EU`  | EU region   |

### PageAccessType

[Section titled “PageAccessType”](#pageaccesstype)

| Value                | Description             |
| -------------------- | ----------------------- |
| `PUBLIC`             | Publicly accessible     |
| `PASSWORD_PROTECTED` | Requires password       |
| `AUTHENTICATED`      | Requires authentication |

### PageTheme

[Section titled “PageTheme”](#pagetheme)

| Value    | Description         |
| -------- | ------------------- |
| `SYSTEM` | Follow system theme |
| `LIGHT`  | Light theme         |
| `DARK`   | Dark theme          |

### PageComponentType

[Section titled “PageComponentType”](#pagecomponenttype)

| Value     | Description               |
| --------- | ------------------------- |
| `MONITOR` | Linked to a monitor       |
| `STATIC`  | Static component (manual) |

### NumberComparator

[Section titled “NumberComparator”](#numbercomparator)

| Value                   | Description           |
| ----------------------- | --------------------- |
| `EQUAL`                 | Equal to target       |
| `NOT_EQUAL`             | Not equal to target   |
| `GREATER_THAN`          | Greater than target   |
| `GREATER_THAN_OR_EQUAL` | Greater than or equal |
| `LESS_THAN`             | Less than target      |
| `LESS_THAN_OR_EQUAL`    | Less than or equal    |

### StringComparator

[Section titled “StringComparator”](#stringcomparator)

| Value                   | Description                                       |
| ----------------------- | ------------------------------------------------- |
| `CONTAINS`              | Contains target string                            |
| `NOT_CONTAINS`          | Does not contain target                           |
| `EQUAL`                 | Equal to target                                   |
| `NOT_EQUAL`             | Not equal to target                               |
| `EMPTY`                 | Value is empty                                    |
| `NOT_EMPTY`             | Value is not empty                                |
| `GREATER_THAN`          | Lexicographically greater                         |
| `GREATER_THAN_OR_EQUAL` | Lexicographically greater than or equal to target |
| `LESS_THAN`             | Lexicographically less                            |
| `LESS_THAN_OR_EQUAL`    | Lexicographically less than or equal to target    |

### RecordComparator

[Section titled “RecordComparator”](#recordcomparator)

| Value          | Description             |
| -------------- | ----------------------- |
| `EQUAL`        | Equal to target         |
| `NOT_EQUAL`    | Not equal to target     |
| `CONTAINS`     | Contains target string  |
| `NOT_CONTAINS` | Does not contain target |

### ServingStatus

[Section titled “ServingStatus”](#servingstatus)

| Value         | Description                    |
| ------------- | ------------------------------ |
| `SERVING`     | Service is healthy and serving |
| `NOT_SERVING` | Service is not healthy         |

## Regions

[Section titled “Regions”](#regions)

Monitor from 28 global locations across multiple providers.

```typescript
import { Region } from "@openstatus/sdk-node";


regions: [Region.FLY_AMS, Region.FLY_IAD, Region.KOYEB_FRA];
```

### Fly.io Regions (18)

[Section titled “Fly.io Regions (18)”](#flyio-regions-18)

| Enum Value | Location        |
| ---------- | --------------- |
| `FLY_AMS`  | Amsterdam       |
| `FLY_ARN`  | Stockholm       |
| `FLY_BOM`  | Mumbai          |
| `FLY_CDG`  | Paris           |
| `FLY_DFW`  | Dallas          |
| `FLY_EWR`  | Newark          |
| `FLY_FRA`  | Frankfurt       |
| `FLY_GRU`  | São Paulo       |
| `FLY_IAD`  | Washington D.C. |
| `FLY_JNB`  | Johannesburg    |
| `FLY_LAX`  | Los Angeles     |
| `FLY_LHR`  | London          |
| `FLY_NRT`  | Tokyo           |
| `FLY_ORD`  | Chicago         |
| `FLY_SJC`  | San Jose        |
| `FLY_SIN`  | Singapore       |
| `FLY_SYD`  | Sydney          |
| `FLY_YYZ`  | Toronto         |

### Koyeb Regions (6)

[Section titled “Koyeb Regions (6)”](#koyeb-regions-6)

| Enum Value  | Location      |
| ----------- | ------------- |
| `KOYEB_FRA` | Frankfurt     |
| `KOYEB_PAR` | Paris         |
| `KOYEB_SFO` | San Francisco |
| `KOYEB_SIN` | Singapore     |
| `KOYEB_TYO` | Tokyo         |
| `KOYEB_WAS` | Washington    |

### Railway Regions (4)

[Section titled “Railway Regions (4)”](#railway-regions-4)

| Enum Value                | Location       |
| ------------------------- | -------------- |
| `RAILWAY_US_WEST2`        | US West        |
| `RAILWAY_US_EAST4`        | US East        |
| `RAILWAY_EUROPE_WEST4`    | Europe West    |
| `RAILWAY_ASIA_SOUTHEAST1` | Asia Southeast |

## Assertions

[Section titled “Assertions”](#assertions)

### Status Code Assertions

[Section titled “Status Code Assertions”](#status-code-assertions)

Validate HTTP response status codes using `NumberComparator`.

```typescript
import { NumberComparator } from "@openstatus/sdk-node";


statusCodeAssertions: [
  { comparator: NumberComparator.EQUAL, target: BigInt(200) },
  { comparator: NumberComparator.LESS_THAN, target: BigInt(400) },
];
```

### Body Assertions

[Section titled “Body Assertions”](#body-assertions)

Validate response body content using `StringComparator`.

```typescript
import { StringComparator } from "@openstatus/sdk-node";


bodyAssertions: [
  { comparator: StringComparator.CONTAINS, target: '"status":"ok"' },
  { comparator: StringComparator.NOT_EMPTY, target: "" },
];
```

### Header Assertions

[Section titled “Header Assertions”](#header-assertions)

Validate response headers using `StringComparator` with a header `key`.

```typescript
import { StringComparator } from "@openstatus/sdk-node";


headerAssertions: [
  {
    key: "content-type",
    comparator: StringComparator.CONTAINS,
    target: "application/json",
  },
];
```

### DNS Record Assertions

[Section titled “DNS Record Assertions”](#dns-record-assertions)

Validate DNS records using `RecordComparator`. Supported record types: `A`, `AAAA`, `CNAME`, `MX`, `TXT`.

```typescript
import { RecordComparator } from "@openstatus/sdk-node";


recordAssertions: [
  {
    record: "A",
    comparator: RecordComparator.EQUAL,
    target: "93.184.216.34",
  },
  {
    record: "CNAME",
    comparator: RecordComparator.CONTAINS,
    target: "cdn",
  },
];
```

## TypeScript Type Exports

[Section titled “TypeScript Type Exports”](#typescript-type-exports)

All types and enums exported from `@openstatus/sdk-node`:

### Monitor Types

[Section titled “Monitor Types”](#monitor-types)

* `HTTPMonitor`, `Headers`, `OpenTelemetryConfig` — HTTP monitor configuration
* `TCPMonitor` — TCP monitor configuration
* `DNSMonitor` — DNS monitor configuration
* `StatusCodeAssertion`, `BodyAssertion`, `HeaderAssertion`, `RecordAssertion` — assertion types
* `CreateHTTPMonitorRequest`, `CreateHTTPMonitorResponse` — HTTP monitor CRUD
* `CreateTCPMonitorRequest`, `CreateTCPMonitorResponse` — TCP monitor CRUD
* `CreateDNSMonitorRequest`, `CreateDNSMonitorResponse` — DNS monitor CRUD
* `UpdateHTTPMonitorRequest`, `UpdateHTTPMonitorResponse`
* `UpdateTCPMonitorRequest`, `UpdateTCPMonitorResponse`
* `UpdateDNSMonitorRequest`, `UpdateDNSMonitorResponse`
* `ListMonitorsRequest`, `ListMonitorsResponse`
* `DeleteMonitorRequest`, `DeleteMonitorResponse`
* `TriggerMonitorRequest`, `TriggerMonitorResponse`
* `GetMonitorStatusRequest`, `GetMonitorStatusResponse`, `RegionStatus`
* `GetMonitorSummaryRequest`, `GetMonitorSummaryResponse`

### Monitor Enums

[Section titled “Monitor Enums”](#monitor-enums)

* `Periodicity` — check interval
* `Region` — monitoring region
* `MonitorStatus` — active / degraded / error
* `HTTPMethod` — HTTP methods
* `TimeRange` — metrics time range
* `NumberComparator`, `StringComparator`, `RecordComparator` — assertion comparators

### Health Types

[Section titled “Health Types”](#health-types)

* `CheckRequest`, `CheckResponse`
* `ServingStatus` — serving / not serving

### Status Report Types

[Section titled “Status Report Types”](#status-report-types)

* `StatusReport`, `StatusReportSummary`, `StatusReportUpdate`
* `CreateStatusReportRequest`, `CreateStatusReportResponse`
* `GetStatusReportRequest`, `GetStatusReportResponse`
* `ListStatusReportsRequest`, `ListStatusReportsResponse`
* `UpdateStatusReportRequest`, `UpdateStatusReportResponse`
* `DeleteStatusReportRequest`, `DeleteStatusReportResponse`
* `AddStatusReportUpdateRequest`, `AddStatusReportUpdateResponse`
* `StatusReportStatus` — investigating / identified / monitoring / resolved

### Status Page Types

[Section titled “Status Page Types”](#status-page-types)

* `StatusPage`, `StatusPageSummary`
* `PageComponent`, `PageComponentGroup`
* `PageSubscriber`
* `CreateStatusPageRequest`, `CreateStatusPageResponse`
* `GetStatusPageRequest`, `GetStatusPageResponse`
* `ListStatusPagesRequest`, `ListStatusPagesResponse`
* `UpdateStatusPageRequest`, `UpdateStatusPageResponse`
* `DeleteStatusPageRequest`, `DeleteStatusPageResponse`
* `AddMonitorComponentRequest`, `AddMonitorComponentResponse`
* `AddStaticComponentRequest`, `AddStaticComponentResponse`
* `RemoveComponentRequest`, `RemoveComponentResponse`
* `UpdateComponentRequest`, `UpdateComponentResponse`
* `CreateComponentGroupRequest`, `CreateComponentGroupResponse`
* `DeleteComponentGroupRequest`, `DeleteComponentGroupResponse`
* `UpdateComponentGroupRequest`, `UpdateComponentGroupResponse`
* `SubscribeToPageRequest`, `SubscribeToPageResponse`
* `UnsubscribeFromPageRequest`, `UnsubscribeFromPageResponse`
* `ListSubscribersRequest`, `ListSubscribersResponse`
* `GetStatusPageContentRequest`, `GetStatusPageContentResponse`
* `GetOverallStatusRequest`, `GetOverallStatusResponse`, `ComponentStatus`
* `OverallStatus`, `PageAccessType`, `PageTheme`, `PageComponentType`

### Maintenance Types

[Section titled “Maintenance Types”](#maintenance-types)

* `Maintenance`, `MaintenanceSummary`
* `CreateMaintenanceRequest`, `CreateMaintenanceResponse`
* `GetMaintenanceRequest`, `GetMaintenanceResponse`
* `ListMaintenancesRequest`, `ListMaintenancesResponse`
* `UpdateMaintenanceRequest`, `UpdateMaintenanceResponse`
* `DeleteMaintenanceRequest`, `DeleteMaintenanceResponse`

### Notification Types

[Section titled “Notification Types”](#notification-types)

* `Notification`, `NotificationSummary`
* `NotificationData`
* `DiscordData`, `EmailData`, `GoogleChatData`, `GrafanaOncallData`, `NtfyData`, `OpsgenieData`, `PagerDutyData`, `SlackData`, `SmsData`, `TelegramData`, `WebhookData`, `WebhookHeader`, `WhatsappData`
* `CreateNotificationRequest`, `CreateNotificationResponse`
* `GetNotificationRequest`, `GetNotificationResponse`
* `ListNotificationsRequest`, `ListNotificationsResponse`
* `UpdateNotificationRequest`, `UpdateNotificationResponse`
* `DeleteNotificationRequest`, `DeleteNotificationResponse`
* `SendTestNotificationRequest`, `SendTestNotificationResponse`
* `CheckNotificationLimitRequest`, `CheckNotificationLimitResponse`
* `NotificationProvider`, `OpsgenieRegion`

### Client Types

[Section titled “Client Types”](#client-types)

* `OpenStatusClient` — client interface
* `OpenStatusClientOptions` — client configuration
* `createOpenStatusClient` — factory function
* `openstatus` — default client instance

# Status Page Service

> Manage status pages, components, groups, and subscribers with the OpenStatus Node.js SDK

Manage status pages, components, component groups, and subscribers. The Status Page Service provides 17 RPC methods.

## Status Page CRUD

[Section titled “Status Page CRUD”](#status-page-crud)

### Create Status Page

[Section titled “Create Status Page”](#create-status-page)

```typescript
const { statusPage } = await client.statusPage.v1.StatusPageService
  .createStatusPage({
    title: "My Service Status",
    slug: "my-service",
    description: "Status page for My Service",
    homepageUrl: "https://example.com",
    contactUrl: "https://example.com/contact",
  });


console.log(`Status page created: ${statusPage?.id}`);
```

### Get Status Page

[Section titled “Get Status Page”](#get-status-page)

```typescript
const { statusPage } = await client.statusPage.v1.StatusPageService
  .getStatusPage({ id: "page_123" });
```

### List Status Pages

[Section titled “List Status Pages”](#list-status-pages)

```typescript
const { statusPages, totalSize } = await client.statusPage.v1.StatusPageService
  .listStatusPages({ limit: 10, offset: 0 });


console.log(`Found ${totalSize} status pages`);
```

### Update Status Page

[Section titled “Update Status Page”](#update-status-page)

```typescript
const { statusPage } = await client.statusPage.v1.StatusPageService
  .updateStatusPage({
    id: "page_123",
    title: "Updated Title",
    description: "Updated description",
  });
```

### Delete Status Page

[Section titled “Delete Status Page”](#delete-status-page)

```typescript
const { success } = await client.statusPage.v1.StatusPageService
  .deleteStatusPage({ id: "page_123" });
```

## Components

[Section titled “Components”](#components)

Components represent individual services on a status page. They can be linked to a monitor (automatically reflects monitor status) or static (manually managed).

### Add Monitor Component

[Section titled “Add Monitor Component”](#add-monitor-component)

```typescript
const { component } = await client.statusPage.v1.StatusPageService
  .addMonitorComponent({
    pageId: "page_123",
    monitorId: "mon_456",
    name: "API Server",
    description: "Main API endpoint",
    order: 1,
    groupId: "group_789",
  });
```

### Add Static Component

[Section titled “Add Static Component”](#add-static-component)

```typescript
const { component } = await client.statusPage.v1.StatusPageService
  .addStaticComponent({
    pageId: "page_123",
    name: "Third-party Service",
    description: "External dependency",
    order: 2,
  });
```

### Update Component

[Section titled “Update Component”](#update-component)

```typescript
const { component } = await client.statusPage.v1.StatusPageService
  .updateComponent({
    id: "comp_123",
    name: "Updated Component Name",
    description: "Updated description",
    order: 3,
    groupId: "group_789",
    groupOrder: 1,
  });
```

### Remove Component

[Section titled “Remove Component”](#remove-component)

```typescript
const { success } = await client.statusPage.v1.StatusPageService
  .removeComponent({ id: "comp_123" });
```

## Component Groups

[Section titled “Component Groups”](#component-groups)

Group related components together on a status page.

### Create Component Group

[Section titled “Create Component Group”](#create-component-group)

```typescript
const { group } = await client.statusPage.v1.StatusPageService
  .createComponentGroup({
    pageId: "page_123",
    name: "Core Services",
  });
```

### Update Component Group

[Section titled “Update Component Group”](#update-component-group)

```typescript
const { group } = await client.statusPage.v1.StatusPageService
  .updateComponentGroup({
    id: "group_123",
    name: "Updated Group Name",
  });
```

### Delete Component Group

[Section titled “Delete Component Group”](#delete-component-group)

```typescript
const { success } = await client.statusPage.v1.StatusPageService
  .deleteComponentGroup({ id: "group_123" });
```

## Subscribers

[Section titled “Subscribers”](#subscribers)

Manage email subscriptions to status page updates.

### Subscribe to Page

[Section titled “Subscribe to Page”](#subscribe-to-page)

```typescript
const { subscriber } = await client.statusPage.v1.StatusPageService
  .subscribeToPage({
    pageId: "page_123",
    email: "user@example.com",
  });
```

### Unsubscribe from Page

[Section titled “Unsubscribe from Page”](#unsubscribe-from-page)

Unsubscribe by email or subscriber ID using the `identifier` oneof:

```typescript
// By email
const { success } = await client.statusPage.v1.StatusPageService
  .unsubscribeFromPage({
    pageId: "page_123",
    identifier: { case: "email", value: "user@example.com" },
  });


// By subscriber ID
const { success: success2 } = await client.statusPage.v1.StatusPageService
  .unsubscribeFromPage({
    pageId: "page_123",
    identifier: { case: "id", value: "sub_456" },
  });
```

### List Subscribers

[Section titled “List Subscribers”](#list-subscribers)

```typescript
const { subscribers, totalSize } = await client.statusPage.v1.StatusPageService
  .listSubscribers({
    pageId: "page_123",
    limit: 50,
    offset: 0,
    includeUnsubscribed: false,
  });
```

## Get Status Page Content

[Section titled “Get Status Page Content”](#get-status-page-content)

Get the full content of a status page including components, groups, active status reports, and maintenance windows. Identify the page by ID or slug.

```typescript
const content = await client.statusPage.v1.StatusPageService
  .getStatusPageContent({
    identifier: { case: "slug", value: "my-service" },
  });


console.log(`Page: ${content.statusPage?.title}`);
console.log(`Components: ${content.components.length}`);
console.log(`Groups: ${content.groups.length}`);
console.log(`Active reports: ${content.statusReports.length}`);
console.log(`Maintenances: ${content.maintenances.length}`);
```

## Get Overall Status

[Section titled “Get Overall Status”](#get-overall-status)

Get the aggregated status of a status page and per-component statuses.

```typescript
import { createOpenStatusClient, OverallStatus } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { overallStatus, componentStatuses } = await client.statusPage.v1
  .StatusPageService.getOverallStatus({
    identifier: { case: "id", value: "page_123" },
  });


console.log(`Overall: ${OverallStatus[overallStatus]}`);
for (const { componentId, status } of componentStatuses) {
  console.log(`  ${componentId}: ${OverallStatus[status]}`);
}
```

# Status Report Service

> Manage incident reports and status updates with the OpenStatus Node.js SDK

Manage incident reports with update timelines. The Status Report Service provides 6 RPC methods.

## Create Status Report

[Section titled “Create Status Report”](#create-status-report)

```typescript
import {
  createOpenStatusClient,
  StatusReportStatus,
} from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { statusReport } = await client.statusReport.v1.StatusReportService
  .createStatusReport({
    title: "API Degradation",
    status: StatusReportStatus.INVESTIGATING,
    message: "We are investigating reports of increased latency.",
    date: "2024-01-15T10:30:00Z",
    pageId: "page_123",
    pageComponentIds: ["comp_456"],
    notify: true,
  });


console.log(`Status report created: ${statusReport?.id}`);
```

## Add Status Report Update

[Section titled “Add Status Report Update”](#add-status-report-update)

Add a new entry to a status report’s timeline.

```typescript
import { StatusReportStatus } from "@openstatus/sdk-node";


const { statusReport } = await client.statusReport.v1.StatusReportService
  .addStatusReportUpdate({
    statusReportId: "sr_123",
    status: StatusReportStatus.IDENTIFIED,
    message: "The issue has been identified as a database connection problem.",
    date: "2024-01-15T11:00:00Z",
    notify: true,
  });
```

## List Status Reports

[Section titled “List Status Reports”](#list-status-reports)

List status reports with optional status filtering and pagination.

```typescript
import { StatusReportStatus } from "@openstatus/sdk-node";


const { statusReports, totalSize } = await client.statusReport.v1
  .StatusReportService.listStatusReports({
    limit: 10,
    offset: 0,
    statuses: [StatusReportStatus.INVESTIGATING, StatusReportStatus.IDENTIFIED],
  });


console.log(`Found ${totalSize} status reports`);
```

## Get / Update / Delete Status Reports

[Section titled “Get / Update / Delete Status Reports”](#get--update--delete-status-reports)

### Get Status Report

[Section titled “Get Status Report”](#get-status-report)

Returns the full report including the updates timeline.

```typescript
import { StatusReportStatus } from "@openstatus/sdk-node";


const { statusReport } = await client.statusReport.v1.StatusReportService
  .getStatusReport({ id: "sr_123" });


console.log(`Title: ${statusReport?.title}`);
console.log(`Status: ${StatusReportStatus[statusReport?.status ?? 0]}`);


for (const update of statusReport?.updates ?? []) {
  console.log(`  ${update.date}: [${StatusReportStatus[update.status]}] ${update.message}`);
}
```

### Update Status Report

[Section titled “Update Status Report”](#update-status-report)

```typescript
const { statusReport } = await client.statusReport.v1.StatusReportService
  .updateStatusReport({
    id: "sr_123",
    title: "Updated Title",
    pageComponentIds: ["comp_456", "comp_789"],
  });
```

### Delete Status Report

[Section titled “Delete Status Report”](#delete-status-report)

```typescript
const { success } = await client.statusReport.v1.StatusReportService
  .deleteStatusReport({ id: "sr_123" });
```

# TypeScript Tips

> Tips for working with bigint fields, oneof types, and migrating clients in the OpenStatus Node.js SDK

## Working with bigint Fields

[Section titled “Working with bigint Fields”](#working-with-bigint-fields)

Protocol Buffers `int64` fields map to `bigint` in TypeScript. This affects:

* **Monitor configuration**: `timeout`, `retry`, `degradedAt`
* **Assertions**: `StatusCodeAssertion.target`
* **Monitor summary**: `totalSuccessful`, `totalDegraded`, `totalFailed`, `p50`, `p75`, `p90`, `p95`, `p99`

Use `BigInt()` to create values:

```typescript
const { monitor } = await client.monitor.v1.MonitorService.createHTTPMonitor({
  monitor: {
    name: "My API",
    url: "https://example.com",
    periodicity: Periodicity.PERIODICITY_1M,
    active: true,
    timeout: BigInt(30000),       // 30 seconds
    retry: BigInt(5),             // 5 retries
    degradedAt: BigInt(3000),     // degraded after 3s
    statusCodeAssertions: [
      { comparator: NumberComparator.EQUAL, target: BigInt(200) },
    ],
  },
});
```

Reading bigint values:

```typescript
const summary = await client.monitor.v1.MonitorService.getMonitorSummary({
  id: "mon_123",
  timeRange: TimeRange.TIME_RANGE_7D,
  regions: [],
});


// bigint values — use Number() for display if values are safe
console.log(`P95 latency: ${summary.p95}ms`);
console.log(`Total checks: ${summary.totalSuccessful + summary.totalDegraded + summary.totalFailed}`);
```

## Handling oneof Types

[Section titled “Handling oneof Types”](#handling-oneof-types)

Several responses use protobuf `oneof` fields, which map to discriminated unions in TypeScript.

### MonitorConfig (getMonitor)

[Section titled “MonitorConfig (getMonitor)”](#monitorconfig-getmonitor)

```typescript
const { monitor } = await client.monitor.v1.MonitorService.getMonitor({
  id: "mon_123",
});


switch (monitor?.config.case) {
  case "http":
    // monitor.config.value is HTTPMonitor
    console.log(`URL: ${monitor.config.value.url}`);
    break;
  case "tcp":
    // monitor.config.value is TCPMonitor
    console.log(`URI: ${monitor.config.value.uri}`);
    break;
  case "dns":
    // monitor.config.value is DNSMonitor
    console.log(`Domain: ${monitor.config.value.uri}`);
    break;
}
```

### NotificationData (createNotification)

[Section titled “NotificationData (createNotification)”](#notificationdata-createnotification)

The `data.data` field selects the provider-specific configuration:

```typescript
// The case string matches the provider in camelCase
data: {
  data: { case: "slack", value: { webhookUrl: "..." } }
}
data: {
  data: { case: "googleChat", value: { webhookUrl: "..." } }
}
data: {
  data: { case: "grafanaOncall", value: { webhookUrl: "..." } }
}
```

### Status Page Identifiers

[Section titled “Status Page Identifiers”](#status-page-identifiers)

`getStatusPageContent` and `getOverallStatus` accept a page identifier by ID or slug:

```typescript
// By ID
{ identifier: { case: "id", value: "page_123" } }


// By slug
{ identifier: { case: "slug", value: "my-service" } }
```

### Unsubscribe Identifier

[Section titled “Unsubscribe Identifier”](#unsubscribe-identifier)

`unsubscribeFromPage` accepts an email or subscriber ID:

```typescript
// By email
{ identifier: { case: "email", value: "user@example.com" } }


// By subscriber ID
{ identifier: { case: "id", value: "sub_456" } }
```

## Migrating from Default Client to createOpenStatusClient

[Section titled “Migrating from Default Client to createOpenStatusClient”](#migrating-from-default-client-to-createopenstatusclient)

**Before** — manual headers on every call:

```typescript
import { openstatus } from "@openstatus/sdk-node";


const headers = { "x-openstatus-key": process.env.OPENSTATUS_API_KEY };


const { httpMonitors } = await openstatus.monitor.v1.MonitorService
  .listMonitors({}, { headers });


const { monitor } = await openstatus.monitor.v1.MonitorService
  .createHTTPMonitor({
    monitor: { name: "API", url: "https://example.com", periodicity: 2, active: true },
  }, { headers });
```

**After** — configure once, use everywhere:

```typescript
import { createOpenStatusClient, Periodicity } from "@openstatus/sdk-node";


const client = createOpenStatusClient({
  apiKey: process.env.OPENSTATUS_API_KEY,
});


const { httpMonitors } = await client.monitor.v1.MonitorService
  .listMonitors({});


const { monitor } = await client.monitor.v1.MonitorService
  .createHTTPMonitor({
    monitor: {
      name: "API",
      url: "https://example.com",
      periodicity: Periodicity.PERIODICITY_1M,
      active: true,
    },
  });
```

# Get Started with openstatus CLI

> Step-by-step tutorial to install and use the openstatus CLI for monitoring as code

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

|                   |                                             |
| ----------------- | ------------------------------------------- |
| **Time**          | \~10 minutes                                |
| **Level**         | Intermediate                                |
| **Prerequisites** | openstatus account, command line experience |

In this tutorial, you’ll learn how to use the openstatus CLI to manage your monitors as code. This enables you to version control your monitoring configuration, automate deployments, and implement GitOps workflows.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An openstatus account
* Command line experience
* API token from your openstatus workspace (Settings → API)

### What you’ll build

[Section titled “What you’ll build”](#what-youll-build)

By the end of this tutorial, you’ll have:

* openstatus CLI installed on your system
* Monitors exported to a YAML configuration file
* Understanding of monitoring as code workflows
* Ability to manage monitors programmatically

![openstatus CLI in action showing monitor management](/_astro/CLI.CsaLWqfo_BUIOJ.webp)

## Installation

[Section titled “Installation”](#installation)

Install the openstatus CLI to manage your monitors directly from code.

### macOS

[Section titled “macOS”](#macos)

Using Homebrew (recommended):

```bash
brew install openstatusHQ/cli/openstatus --cask
```

Or using the install script:

```bash
curl -fsSL https://raw.githubusercontent.com/openstatusHQ/cli/refs/heads/main/install.sh | bash
```

### Linux

[Section titled “Linux”](#linux)

```bash
curl -fsSL https://raw.githubusercontent.com/openstatusHQ/cli/refs/heads/main/install.sh | bash
```

### Windows

[Section titled “Windows”](#windows)

```powershell
iwr https://raw.githubusercontent.com/openstatusHQ/cli/refs/heads/main/install.ps1 | iex
```

### Verify installation

[Section titled “Verify installation”](#verify-installation)

Run the following command to confirm the CLI is installed:

```bash
openstatus --version
```

You should see output like:

```plaintext
openstatus version x.x.x
```

## Configure API authentication

[Section titled “Configure API authentication”](#configure-api-authentication)

Create an API key in your workspace settings (Settings → API), then set it as an environment variable:

```bash
# macOS / Linux
export OPENSTATUS_API_TOKEN=<your-api-token>
```

```powershell
# Windows PowerShell
$env:OPENSTATUS_API_TOKEN="<your-api-token>"
```

Note

Add this to your shell profile (`~/.bashrc`, `~/.zshrc`) to persist across sessions.

## Import existing monitors

[Section titled “Import existing monitors”](#import-existing-monitors)

Start by importing your existing monitors from your workspace to a YAML file:

```bash
openstatus monitors import
```

You should see output confirming the import:

```plaintext
Successfully imported X monitors to openstatus.yaml
```

This creates an `openstatus.yaml` file containing all your current monitors. This file becomes your single source of truth for monitoring configuration.

**Checkpoint:** Open the `openstatus.yaml` file and verify it contains your monitors. You should see entries with your monitor names and URLs.

## Manage monitors as code

[Section titled “Manage monitors as code”](#manage-monitors-as-code)

Now you can add, remove, or update monitors in the YAML file and apply your changes:

```bash
openstatus monitors apply
```

The CLI will show you a diff of changes before applying them, ensuring you’re aware of what will be modified.

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Excellent work! You’ve successfully:

* ✅ Installed the openstatus CLI
* ✅ Configured API authentication
* ✅ Imported monitors to a YAML file
* ✅ Learned the monitoring as code workflow

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### ”command not found: openstatus”

[Section titled “”command not found: openstatus””](#command-not-found-openstatus)

**Cause:** The CLI binary is not in your PATH.

**Fix (macOS/Homebrew):**

```bash
brew reinstall openstatusHQ/cli/openstatus --cask
```

**Fix (install script):** Ensure `~/.local/bin` is in your PATH:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### “unauthorized” or “invalid token” error

[Section titled ““unauthorized” or “invalid token” error”](#unauthorized-or-invalid-token-error)

**Cause:** Your API token is missing or incorrect.

**Fix:**

1. Verify the token is set: `echo $OPENSTATUS_API_TOKEN`
2. Regenerate the token in your workspace settings (Settings → API)
3. Make sure there are no extra spaces or newlines in the token value

### ”no monitors found” on import

[Section titled “”no monitors found” on import”](#no-monitors-found-on-import)

**Cause:** Your workspace has no monitors, or the token belongs to a different workspace.

**Fix:** Create at least one monitor in the dashboard first, then retry the import.

## What’s next?

[Section titled “What’s next?”](#whats-next)

Now that you have the CLI set up, you can:

* **[Monitor Your MCP Server](/guides/how-to-monitor-mcp-server/)** - Example of CLI-based monitor configuration
* **[CLI Reference](/reference/cli-reference)** - Complete command documentation
* **[Set up CI/CD](/guides/how-to-run-synthetic-test-github-action/)** - Automate monitoring in your pipeline

### Advanced workflows

[Section titled “Advanced workflows”](#advanced-workflows)

With the CLI, you can:

* Version control your monitoring configuration with Git
* Review monitoring changes in pull requests
* Automate monitor creation for new services
* Sync monitors across multiple environments
* Implement GitOps for infrastructure monitoring

## Learn more

[Section titled “Learn more”](#learn-more)

* **[Monitoring as Code Concept](/concept/uptime-monitoring-as-code)** - Why manage monitors as code
* **[CLI Reference](/reference/cli-reference)** - All available commands
* **[YAML Configuration Examples](https://github.com/openstatusHQ/cli-template)** - Sample configurations

# Tutorials Overview

> Step-by-step tutorials to create monitors, status pages, and private locations with OpenStatus.

## Tutorials

[Section titled “Tutorials”](#tutorials)

### What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

Our tutorials are designed to help you:

* Get your first monitor up and running
* Create and configure status pages
* Set up monitoring infrastructure
* Use openstatus CLI for automation

### Core Tutorials

[Section titled “Core Tutorials”](#core-tutorials)

Start your journey with openstatus:

* **[Create Your First Monitor](/tutorial/how-to-create-monitor)** (\~5 min) - Learn the fundamentals by setting up uptime monitoring for your first endpoint
* **[Create a Status Page](/tutorial/how-to-create-status-page)** (\~5 min) - Build a public status page to communicate service health to your users
* **[Configure Your Status Page](/tutorial/how-to-configure-status-page)** (\~10 min) - Customize your status page with monitors, domains, and protection
* **[Set Up the Slack Agent](/tutorial/how-to-setup-slack-agent)** (\~5 min) - Manage incidents directly from Slack

### Advanced Tutorials

[Section titled “Advanced Tutorials”](#advanced-tutorials)

Once you’re comfortable with the basics:

* **[Create a Private Location (Beta)](/tutorial/how-to-create-private-location)** (\~15 min) - Set up monitoring from your own infrastructure
* **[Get Started with openstatus CLI](/tutorial/get-started-with-openstatus-cli)** (\~10 min) - Automate monitor management with our command-line tool

### What’s next?

[Section titled “What’s next?”](#whats-next)

After completing these tutorials, you’ll be ready to:

* Explore [how-to guides](/guides/getting-started) for specific tasks and advanced scenarios
* Dive into [explanations](/concept/getting-started) to understand the concepts behind the features
* Reference our [technical documentation](/reference/cli-reference) for detailed specifications

# Configure Your Status Page

> A step-by-step tutorial to customize and configure your status page

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

In this tutorial, you’ll learn how to customize your status page’s appearance and behavior. You’ll explore different display options, themes, and configuration settings to create a status page that matches your brand and communication style.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An openstatus account
* A status page already created (see [Create a Status Page](/tutorial/how-to-create-status-page))
* At least one monitor added to your status page

### What you’ll build

[Section titled “What you’ll build”](#what-youll-build)

By the end of this tutorial, you’ll have:

* A customized status page with your preferred theme
* Configured status trackers displaying data your way
* Links to important resources
* Preview and live configuration experience

## Status Page Customization

[Section titled “Status Page Customization”](#status-page-customization)

OpenStatus offers enhanced status page customization with multiple themes and display options.

Explore available themes: <https://themes.openstatus.dev>

## Get started

[Section titled “Get started”](#get-started)

Go to the **Status Page Redesign** section in your status page settings and toggle `Enable New Version`. Once enabled, you’ll see three subsections:

1. **Tracker Configuration**
2. **Theme Explorer**
3. **Links**

![Create your status page](/_astro/configure-status-page-1.hK4aWELq_zNQYG.webp)

### View and configure status page

[Section titled “View and configure status page”](#view-and-configure-status-page)

Before choosing to enable the new page, we provide you with a way to check the configuration first. Click on the **View and configure status page** and you’ll get forwarded to your status page and a bottom right floating button will appear. Once you’re done, click on the **Dashboard** and you’ll be forwarded to your page where you get asked to save the config before continuing.

![Status page floating configuration popover](/_astro/status-page-floating.Bv9sHxZn_CKyED.webp)

***

Note

Once enabled, the subdomain will have a rewrite to the new project. We are adding a `maxAge: 600` request cookie to improve the page load. **If you decide to deactivate the new version, it might take up to 10 minutes for the user to see the old page.**

### 1. Tracker Configuration

[Section titled “1. Tracker Configuration”](#1-tracker-configuration)

We have three new status tracker configurations to provide you with a maximum choice of displaying the collected data.

**Bar Type**: How every ‘day’ is displayed in for a status tracker. Either **absolute** or **manual**.

**Card Type**: The card type is only configurable if the bar type is **absolute**. You’ll then be able to choose between **duration**, which will show the duration of “success”, “error”, “degraded” or “maintenance” reports or **requests** where we will share the number of request status itself. If **manual** bar type is chosen, we will only show the most significant status of the day.

**Show Uptime**: The uptime is calculated by either the **duration** of the different reports *or* the **request** values depending on what you’ve chosen for the **absolute** value (incl. incidents). If you’ve chosen **manual**, it only gets calculated by the duration of your status reports.

A few examples to understand it:

Example of **absolute bar** with **duration card** and **showing uptime**

![absolute bar type with duration card and showing uptime](/_astro/status-page-beta-3.CmE8RTBu_SjevX.webp)

Example of **absolute bar** with **request card** and **hiding uptime**

![absolute bar type with request card and hiding uptime](/_astro/status-page-beta-4.Dn8UYLB6_Z1S7KU2.webp)

Example of **manual bar** with **simple card** and **hiding uptime**

![manual bar type and hiding uptime](/_astro/status-page-beta-2.CXXTocNq_6KIQI.webp)

### 2. Theme Explorer

[Section titled “2. Theme Explorer”](#2-theme-explorer)

You can choose between different themes. We start with the following three:

* `default` (openstatus)
* `supabase`
* `github-high-contrast`

Visit [themes.openstatus.dev](https://themes.openstatus.dev) to see the list of supported themes. If you want, you can contribute your own to the list.

### 3. Links

[Section titled “3. Links”](#3-links)

Let’s have a closer look at your status page header navigation:

![Header navigation of your status page](/_astro/status-page-beta-1.CYMWZuV4_Z1rht8c.webp)

**Homepage URL**: Your logo will support linking to your own website.

**Contact URL**: If filled out, you will see a `Message` icon that users can click to forward them to a contact page. This can also be an email client by starting the input with `mailto:` (e.g. `mailto:support@openstatus.dev`).

***

We are continuously adding new features. Feel free to let us know what’s missing!

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Excellent work! You’ve successfully:

* ✅ Enabled and configured the new status page design
* ✅ Customized status tracker display options
* ✅ Explored and applied theme settings
* ✅ Added navigation links to your status page
* ✅ Previewed changes before making them live

## What’s next?

[Section titled “What’s next?”](#whats-next)

Now that your status page is configured, you can:

* **[Building Trust with Status Pages](/concept/best-practices-status-page)** - Learn effective incident communication
* **[Add Status Subscribers](/reference/subscriber)** - Let users subscribe to updates

### Learn more

[Section titled “Learn more”](#learn-more)

* **[Status Page Reference](/reference/status-page)** - Complete configuration options
* **[Uptime Calculation Values](/concept/uptime-calculation-and-values)** - How uptime percentages work

## Video Tutorial

[Section titled “Video Tutorial”](#video-tutorial)

[Play](https://youtube.com/watch?v=igMbSrej6RQ)

View, configure and enable the new status page

# Create an Uptime Monitor in 5 Minutes

> Set up your first uptime monitor with OpenStatus — track response time, status codes, and availability from 35+ global locations.

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

In this tutorial, you’ll learn how to create your first monitor an automated watchdog for your services. A monitor periodically checks your endpoints to ensure they are available, performant, and returning the correct data. Think of it as a `curl` command that runs 24/7, providing continuous insights into the health of your application.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An openstatus account (free tier available at [openstatus.dev](https://www.openstatus.dev))
* A URL endpoint to monitor (can be your own service or any public URL)

### What you’ll build

[Section titled “What you’ll build”](#what-youll-build)

By the end of this tutorial, you’ll have:

* A working uptime monitor checking your endpoint every minute
* Real-time metrics showing response time and status codes
* Understanding of how to customize HTTP requests for different scenarios

## Get Started in 1 Minute

[Section titled “Get Started in 1 Minute”](#get-started-in-1-minute)

Let’s get your first uptime check up and running.

### 1. Create the Monitor

[Section titled “1. Create the Monitor”](#1-create-the-monitor)

![Monitors page showing the Create Monitor button in the sidebar](/_astro/create-monitor-1.B7jpNW9J_ZHK3o.webp)

Navigate to the **Monitors** page from the sidebar and click the **Create Monitor** button. This will open a new configuration screen.

### 2. Configure the Basics

[Section titled “2. Configure the Basics”](#2-configure-the-basics)

![Monitor creation form with name and URL fields](/_astro/create-monitor-2.rJvYlxg6_Z17kWLv.webp)

To get your monitor started, you only need to provide two essential pieces of information:

* **Name:** A clear, descriptive name for your monitor (e.g., “Production API Health Check” or “Homepage Uptime”).
* **URL:** The full URL of the endpoint you want to test (e.g., `https://openstat.us`).

As soon as you enter the URL, our monitoring tool will automatically begin tracking key performance metrics for every check, including:

* **Response Time:** The total time it takes for the request to complete.

* **Status Code:** The HTTP status code returned by the server (e.g., 200, 404, 500).

* **Response Headers:** A detailed view of the headers returned by the server.

* **Detailed Timing Metrics:** A breakdown of the time spent on each phase of the request (DNS lookup, TCP connection, TLS handshake, etc.)

  ![Monitor overview dashboard showing response time and status code charts](/_astro/monitor-overview.DZ1tKCST_ZrgMDc.webp)

**Checkpoint:** After saving, you should see your monitor’s overview page with response time and status code charts. If data appears within a few seconds, your monitor is running.

### 3. Customizing the HTTP Request

[Section titled “3. Customizing the HTTP Request”](#3-customizing-the-http-request)

Your monitor doesn’t just have to be a simple `GET` request. You can customize the HTTP request to simulate real-world traffic and test specific scenarios.

#### HTTP Method

[Section titled “HTTP Method”](#http-method)

Choose the appropriate HTTP method for your check. While `GET` is the default and most common for simple health checks, you can also select `POST`, `HEAD`, `OPTIONS`, `PUT`, `PATCH`, `DELETE`, or `TRACE`.

* `GET`: Retrieve data from an endpoint. The most common choice for health checks.
* `POST`: Send data to an endpoint, for example, to test a form submission or API creation endpoint.
* `HEAD`: Same as `GET`, but without the response body. Useful for quickly checking if a resource exists.
* `OPTIONS`: Retrieve the supported HTTP methods for a resource.
* `PUT`: Update an existing resource.
* `PATCH`: Partially update an existing resource.
* `DELETE`: Delete a resource.
* `TRACE`: Echo the request back to the client.

#### Request Body

[Section titled “Request Body”](#request-body)

If you select the `POST` method, you can add a Request Body to your monitor’s configuration. This is essential for testing API endpoints that require a JSON, form-encoded, or other data payload. Simply enter the data you want to send in the provided text area.

#### Custom Headers

[Section titled “Custom Headers”](#custom-headers)

You can add any number of custom HTTP headers to your request. This is particularly useful for:

* **Authentication:** Sending an Authorization token (e.g., a Bearer token) to test a protected endpoint.
* **Content Type:** Setting a `content-type` header to specify a content type (e.g., `application/json`).
* **Content Negotiation:** Setting an Accept header to request a specific content type from the server (e.g., `application/json`).
* **Simulating Clients:** Adding a User-Agent header to simulate traffic from a specific browser or device.

We've got your User-Agent covered!

openstatus automatically includes the `"User-Agent": "openstatus/1.0"` header in every request. This makes it easy to identify and filter out our monitoring traffic from your server logs or analytics.

## Important Considerations

[Section titled “Important Considerations”](#important-considerations)

### Monitoring Third-Party Endpoints

[Section titled “Monitoring Third-Party Endpoints”](#monitoring-third-party-endpoints)

Note

If you’re monitoring a URL you don’t own (like `google.com` or a partner API), your requests might be blocked by firewalls or rate limiters (e.g., Cloudflare). This is a security measure on their end to prevent scraping or denial-of-service attacks.

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Congratulations! You’ve successfully:

* ✅ Created your first uptime monitor
* ✅ Configured basic HTTP monitoring settings
* ✅ Learned about customizing requests with methods, headers, and body
* ✅ Understood key monitoring metrics (response time, status codes, timing breakdown)

## What’s next?

[Section titled “What’s next?”](#whats-next)

Now that you have a monitor running, you can:

* **[Create a Status Page](/tutorial/how-to-create-status-page)** - Share your service status publicly with users

### Learn more

[Section titled “Learn more”](#learn-more)

* **[Understanding Uptime Monitoring](/concept/uptime-monitoring)** - Deep dive into monitoring concepts
* **[HTTP Monitor Reference](/reference/http-monitor)** - Complete technical specifications

## Video Tutorial

[Section titled “Video Tutorial”](#video-tutorial)

[Play](https://youtube.com/watch?v=nYti3DjHoWY)

Create your first monitor

# Create a Private Location

> Set up monitoring from your own infrastructure using Docker-based private probes

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

|                   |                                      |
| ----------------- | ------------------------------------ |
| **Time**          | \~15 minutes                         |
| **Level**         | Advanced                             |
| **Prerequisites** | OpenStatus account, Docker installed |

In this tutorial, you’ll set up a **private location** — a monitoring probe running on your own infrastructure. This lets you monitor internal applications, private APIs, and network resources behind your firewall without exposing them to the public internet.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An OpenStatus account ([openstatus.dev](https://www.openstatus.dev))
* Docker installed on your server or local machine (`docker --version` to verify)
* At least one monitor already created (see [Create Your First Monitor](/tutorial/how-to-create-monitor))

### What you’ll build

[Section titled “What you’ll build”](#what-youll-build)

By the end of this tutorial, you’ll have:

* A private location configured in OpenStatus
* A Docker container running the monitoring probe on your infrastructure
* Monitors assigned to check from your private location

Caution

Private locations are currently in **beta**. Some features like incident creation and public status page support are not yet available for private locations.

## What are private locations?

[Section titled “What are private locations?”](#what-are-private-locations)

Private locations allow you to monitor internal applications from within your own infrastructure, rather than solely relying on our public cloud-based regions. By deploying monitoring probes as Docker containers on your own machines, you can:

* Monitor internal APIs and services behind your firewall
* Get detailed timing and latency data from your specific deployment location
* Monitor from on-prem servers, Raspberry Pi devices, or any Docker-capable machine

## Step 1: Create a private location

[Section titled “Step 1: Create a private location”](#step-1-create-a-private-location)

1. Navigate to **Settings** > **Private Locations** in your OpenStatus dashboard
2. Click **Create Private Location**
3. Give your location a descriptive name (e.g., “Office Network”, “AWS us-east-1 VPC”)
4. Save the configuration

After creation, you’ll receive a **token**. Copy this token — you’ll need it in the next step.

Caution

Keep your token secure. It authenticates your probe with the OpenStatus platform.

## Step 2: Deploy the Docker probe

[Section titled “Step 2: Deploy the Docker probe”](#step-2-deploy-the-docker-probe)

Run the monitoring probe on your server using Docker:

```bash
docker run -d \
  --name openstatus-probe \
  --restart unless-stopped \
  -e OPENSTATUS_TOKEN=<your-token> \
  ghcr.io/openstatushq/probe:latest
```

Replace `<your-token>` with the token from Step 1.

### Verify the container is running

[Section titled “Verify the container is running”](#verify-the-container-is-running)

```bash
docker ps --filter name=openstatus-probe
```

You should see the container listed with a status of `Up`:

```plaintext
CONTAINER ID   IMAGE                              STATUS         NAMES
abc123         ghcr.io/openstatushq/probe:latest  Up 2 minutes   openstatus-probe
```

## Step 3: Assign monitors to your private location

[Section titled “Step 3: Assign monitors to your private location”](#step-3-assign-monitors-to-your-private-location)

1. Go to **Settings** > **Private Locations** and select your location
2. Choose which monitors should run from this private location
3. Alternatively, edit an individual monitor and select your private location in its settings

**Checkpoint:** Within a couple of minutes, you should see monitoring data appearing in your monitor’s overview from your private location.

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

You’ve successfully:

* ✅ Created a private location in OpenStatus
* ✅ Deployed a monitoring probe on your own infrastructure
* ✅ Assigned monitors to check from your private location

## Current limitations

[Section titled “Current limitations”](#current-limitations)

* Incidents are **not yet created** for monitors running via private locations. Continue using OpenStatus public regions if you need alerting.
* Public monitors on status pages **do not yet support** private locations.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Container exits immediately

[Section titled “Container exits immediately”](#container-exits-immediately)

Check the container logs for errors:

```bash
docker logs openstatus-probe
```

Common causes:

* **Invalid token:** Double-check the token value — ensure no extra spaces or newlines
* **Network issues:** Ensure the container can reach `api.openstatus.dev` on port 443

### No data appearing in the dashboard

[Section titled “No data appearing in the dashboard”](#no-data-appearing-in-the-dashboard)

1. Verify the container is running: `docker ps --filter name=openstatus-probe`
2. Check that you’ve assigned at least one monitor to the private location
3. Wait 2-3 minutes — there may be a short delay before the first check runs

### Container can’t reach internal services

[Section titled “Container can’t reach internal services”](#container-cant-reach-internal-services)

If the probe needs to reach services on your host machine, use Docker’s host networking:

```bash
docker run -d \
  --name openstatus-probe \
  --restart unless-stopped \
  --network host \
  -e OPENSTATUS_TOKEN=<your-token> \
  ghcr.io/openstatushq/probe:latest
```

## What’s next?

[Section titled “What’s next?”](#whats-next)

* **[Read our Raspberry Pi deployment guide](https://www.openstatus.dev/blog/deploy-private-locations-raspberry-pi)** — Deploy probes on low-cost hardware
* **[Create a Monitor](/tutorial/how-to-create-monitor)** — Set up more monitors to run from your private location

# Create a Status Page

> A step-by-step tutorial to create and publish your first status page

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

|                   |                                          |
| ----------------- | ---------------------------------------- |
| **Time**          | \~5 minutes                              |
| **Level**         | Beginner                                 |
| **Prerequisites** | OpenStatus account, at least one monitor |

In this tutorial, you’ll create a public status page to communicate your service’s health to users. A status page is a transparent way to show real-time uptime information and keep your users informed during incidents.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An openstatus account
* At least one monitor created (see [Create Your First Monitor](/tutorial/how-to-create-monitor))

### What you’ll build

[Section titled “What you’ll build”](#what-youll-build)

By the end of this tutorial, you’ll have:

* A public status page showing your service health
* Monitors displayed on your status page
* Understanding of privacy and security options

## Get started

[Section titled “Get started”](#get-started)

### 1. Create the status page

[Section titled “1. Create the status page”](#1-create-the-status-page)

Navigate to the **Status Pages** page from the sidebar and click the **Create Status Page** button. This will open a new configuration screen.

![Status Pages sidebar with the Create Status Page button highlighted](/_astro/create-status-page-1.Cm9BkNSE_29jhOA.webp)

### 2. Configure the status page

[Section titled “2. Configure the status page”](#2-configure-the-status-page)

Fill in the basic details for your status page:

* **Title:** A name for your status page (e.g., “Acme Status” or “API Health”)
* **Slug:** The URL path for your status page (e.g., `acme` creates `acme.openstatus.dev`)

![Status page configuration form showing title, slug, and monitor selection](/_astro/create-status-page-2.xnQ6FhF5_Z10PRqL.webp)

#### Add monitors

[Section titled “Add monitors”](#add-monitors)

Select the monitors you want to display on your status page. Each monitor will show as a separate service with its own uptime bar. You can add multiple monitors to give users a complete picture of your infrastructure health.

#### Custom domain

[Section titled “Custom domain”](#custom-domain)

You can use your own domain (e.g., `status.yourdomain.com`) instead of the default `*.openstatus.dev` subdomain. To set this up:

1. Enter your custom domain in the **Custom Domain** field
2. Add a CNAME record pointing to `status.openstatus.dev` in your DNS provider
3. Wait for DNS propagation (usually a few minutes, up to 48 hours)

See the [Status Page Reference](/reference/status-page) for detailed DNS configuration instructions.

#### Password protection

[Section titled “Password protection”](#password-protection)

Enable password protection to restrict access to your status page. This is useful for internal status pages that should only be visible to your team or specific customers. Enter a password, and visitors will be prompted to authenticate before viewing the page.

**Checkpoint:** After saving, click the link to your status page (shown at the top of the settings). You should see your monitors listed with uptime bars.

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Great work! You’ve successfully:

* ✅ Created your first status page
* ✅ Added monitors to display service health
* ✅ Learned about custom domains and password protection

## What’s next?

[Section titled “What’s next?”](#whats-next)

Now that you have a basic status page, you can:

* **[Configure Your Status Page](/tutorial/how-to-configure-status-page)** - Customize appearance and add more features
* **[Building Trust with Status Pages](/concept/best-practices-status-page)** - Learn how to communicate effectively

### Learn more

[Section titled “Learn more”](#learn-more)

* **[Status Page Reference](/reference/status-page)** - Complete configuration options
* **[Understanding Uptime Values](/concept/uptime-calculation-and-values)** - How uptime is calculated

# Set Up the OpenStatus Slack Agent

> A step-by-step tutorial to install the OpenStatus Slack agent and manage incidents directly from Slack

## What you’ll learn

[Section titled “What you’ll learn”](#what-youll-learn)

|                   |                                                  |
| ----------------- | ------------------------------------------------ |
| **Time**          | \~5 minutes                                      |
| **Level**         | Beginner                                         |
| **Prerequisites** | OpenStatus account, Slack workspace admin access |

In this tutorial, you’ll learn how to install the OpenStatus Slack agent so you can manage incidents directly from your Slack workspace — no need to switch to the dashboard.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An OpenStatus account ([openstatus.dev](https://www.openstatus.dev))
* A Slack workspace where you have permission to install apps

### What you’ll get

[Section titled “What you’ll get”](#what-youll-get)

By the end of this tutorial, you’ll have:

* The OpenStatus Slack agent installed in your workspace
* The ability to create, update, and resolve incidents from Slack

## Install the Slack Agent

[Section titled “Install the Slack Agent”](#install-the-slack-agent)

### 1. Go to Settings

[Section titled “1. Go to Settings”](#1-go-to-settings)

Navigate to **Settings** > **Integrations** in your OpenStatus dashboard.

### 2. Install the Slack Integration

[Section titled “2. Install the Slack Integration”](#2-install-the-slack-integration)

Click the **Install Slack** button. You’ll be redirected to Slack’s authorization page where you can select the workspace and channel you want to connect.

Grant the requested permissions and click **Allow** to complete the installation.

Note

Make sure you select the correct Slack workspace if you belong to multiple workspaces.

### 3. Verify the Installation

[Section titled “3. Verify the Installation”](#3-verify-the-installation)

After completing the OAuth flow, go to the Slack channel you selected and type:

```plaintext
@openstatus what's the status of my monitors?
```

The bot should respond with a summary of your monitors. If you see a response, the installation is working.

Tip

The bot only responds when mentioned with `@openstatus` — it won’t interrupt your conversations.

### 4. Start Managing Incidents from Slack

[Section titled “4. Start Managing Incidents from Slack”](#4-start-managing-incidents-from-slack)

Here are some examples of what you can do:

#### Create an incident

[Section titled “Create an incident”](#create-an-incident)

Notify your subscribers about a new issue.

```plaintext
@openstatus create an incident for the payment API – high latency detected.
```

#### Update an incident

[Section titled “Update an incident”](#update-an-incident)

Keep your status page updated while you investigate.

```plaintext
@openstatus keep the status page updated that we are still monitoring the issue.
```

#### Resolve an incident

[Section titled “Resolve an incident”](#resolve-an-incident)

Close an active incident and let your subscribers know.

```plaintext
@openstatus resolve the ongoing incident on my API status page.
```

#### Schedule maintenance

[Section titled “Schedule maintenance”](#schedule-maintenance)

Plan downtime so subscribers are informed in advance.

```plaintext
@openstatus schedule a maintenance window for my database next Friday from 2–3 PM.
```

## What you’ve accomplished

[Section titled “What you’ve accomplished”](#what-youve-accomplished)

Congratulations! You’ve successfully:

* ✅ Installed the OpenStatus Slack agent in your workspace
* ✅ Connected your OpenStatus account to Slack
* ✅ Learned how to manage incidents directly from Slack

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### The bot doesn’t respond when mentioned

[Section titled “The bot doesn’t respond when mentioned”](#the-bot-doesnt-respond-when-mentioned)

1. **Check the channel:** Make sure you’re mentioning `@openstatus` in the channel you selected during installation.
2. **Check permissions:** Go to **Settings** > **Integrations** and verify the Slack integration shows as connected.
3. **Reinstall:** If the integration appears disconnected, click **Install Slack** again to re-authorize.

### ”Not authorized” or permission errors

[Section titled “”Not authorized” or permission errors”](#not-authorized-or-permission-errors)

Your Slack workspace admin may need to approve the app. Ask your workspace admin to go to **Slack Admin** > **Manage Apps** and approve the OpenStatus integration.

### Bot responds but can’t find monitors

[Section titled “Bot responds but can’t find monitors”](#bot-responds-but-cant-find-monitors)

Make sure you have at least one monitor and one status page created in your OpenStatus workspace before using incident commands.

## What’s next?

[Section titled “What’s next?”](#whats-next)

* **[Create a Status Page](/tutorial/how-to-create-status-page)** — share your service status publicly with users
* **[Create a Monitor](/tutorial/how-to-create-monitor)** — set up uptime monitoring for your endpoints