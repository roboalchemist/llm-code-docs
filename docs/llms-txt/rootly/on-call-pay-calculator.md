# Source: https://docs.rootly.com/on-call/on-call-pay-calculator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# On-Call Pay Calculator

> Accurately calculate and export on-call compensation based on real schedule data.

## Overview

The On-Call Pay Calculator helps teams confidently and consistently calculate compensation for on-call work using real schedule data from Rootly. Instead of manually stitching together spreadsheets or reconciling shifts by hand, Rootly automatically tracks on-call coverage across your schedules and produces exportable pay reports that reflect how your team actually operated.

Pay reports are generated directly from schedules that are actively connected to escalation policies, ensuring only real, paged on-call time is included. Reports can be downloaded in **Excel (XLSX)** or **CSV** format and are suitable for payroll processing, audits, or internal review.

All reports are generated asynchronously in the background. Once a report is ready, you’ll receive an email notification so you can download it without waiting in the app.

<Frame>
  <img src="https://mintcdn.com/rootly/iYRzT1wc8VvbaOKl/images/on-call-pay-calculator/mainpage.png?fit=max&auto=format&n=iYRzT1wc8VvbaOKl&q=85&s=d141874966836659d239e3d8e1151d97" width="1750" height="712" data-path="images/on-call-pay-calculator/mainpage.png" />
</Frame>

## How Pay Calculation Works

At a high level, the Pay Calculator pulls on-call shift data from your schedules, applies your configured pay rules, and aggregates time per user over a selected date range. The system supports both **hourly-based** and **daily-based** compensation models, making it flexible enough for a wide range of team policies.

Only schedules that are assigned to escalation policies are included in pay calculations. This ensures the calculator reflects actual on-call responsibility rather than theoretical coverage. Any gaps in coverage are attributed to the schedule owner, preserving accountability and accuracy.

Pay rules are snapshotted at the time a report is created. This means changes to rates or configuration going forward will not retroactively alter previously generated reports.

## Configuring Pay Rules

Before generating your first report, you’ll need to configure your team’s pay rules. These rules define how time is counted, how compensation is calculated, and what level of detail appears in exported reports.

To access pay rule configuration, navigate to **On-Call → On-Call Schedules → Pay Calculator tab**, then select **Configure Rules**.

<Frame>
  <img src="https://mintcdn.com/rootly/iYRzT1wc8VvbaOKl/images/on-call-pay-calculator/buttons.png?fit=max&auto=format&n=iYRzT1wc8VvbaOKl&q=85&s=715db2d3950749eb19a61e7fb1d4e1b3" width="1474" height="339" data-path="images/on-call-pay-calculator/buttons.png" />
</Frame>

### Choosing a Pay Type

The Pay Calculator supports two compensation models: **Hourly** and **Daily**.

With **Hourly pay**, Rootly calculates compensation based on the exact duration of on-call time, tracked down to the minute. Time is categorized into business hours (9 AM–5 PM on weekdays), outside business hours on weekdays, and weekends. This model is ideal for teams that pay based on actual availability or workload.

With **Daily pay**, Rootly counts unique calendar days that a user was on-call. Days are separated into weekdays and weekends, and each qualifying day is counted once regardless of shift length. This model works well for teams that offer a flat daily on-call stipend.

<Frame>
  <img src="https://mintcdn.com/rootly/iYRzT1wc8VvbaOKl/images/on-call-pay-calculator/payrules.png?fit=max&auto=format&n=iYRzT1wc8VvbaOKl&q=85&s=b26fce555f703ada87c24744ceb5da2b" width="1699" height="479" data-path="images/on-call-pay-calculator/payrules.png" />
</Frame>

### Configuring Rates

You can choose whether Rootly should calculate total pay automatically or simply report time worked.

When **Single Rate** is enabled, you specify a currency and either an hourly or daily rate. Rootly will calculate total compensation per user and include it directly in the report.

When **Single Rate** is disabled, Rootly will still calculate hours or days worked but will leave rate and total pay fields empty. This is useful if rates vary by individual, seniority, or geography, or if final compensation is calculated outside of Rootly.

<Frame>
  <img src="https://mintcdn.com/rootly/iYRzT1wc8VvbaOKl/images/on-call-pay-calculator/payrate.png?fit=max&auto=format&n=iYRzT1wc8VvbaOKl&q=85&s=e173c4be3e4fcf3213a52f30ea625ced" width="1503" height="753" data-path="images/on-call-pay-calculator/payrate.png" />
</Frame>

### Data Inclusion Options

The Pay Calculator includes several options that control how much detail is captured and surfaced in generated pay reports.

* **Granular Time Breakdown (Hourly pay only)**\
  When enabled, Rootly analyzes alert activity during each hour of an on-call shift and categorizes time into:
  * **Non-paged hours** — time spent on call with no alerts received
  * **Paged hours** — time during which alerts were triggered but not yet acknowledged or resolved
  * **Acknowledged / resolved hours** — time spent actively responding to incidents\
    This breakdown allows teams to distinguish between passive standby time and active incident response, and apply different compensation rules if needed.

* **Include Shadow Shifts**\
  When enabled, time spent shadowing on-call duties is included in pay calculations. This is commonly used for training or onboarding scenarios. Rootly automatically adjusts for overlaps so shadow time is not double-counted if a user is both shadowing and actively on call during the same period.

* **Show Individual Shift Data**\
  When enabled, reports include detailed per-shift columns for each user, including:
  * Schedule name
  * Shift start time (in the team’s timezone)
  * Shift end time (in the team’s timezone)\
    This option is especially useful for audits, payroll verification, and validating how totals were calculated.

<Frame>
  <img src="https://mintcdn.com/rootly/iYRzT1wc8VvbaOKl/images/on-call-pay-calculator/datainclude.png?fit=max&auto=format&n=iYRzT1wc8VvbaOKl&q=85&s=573c3ea1088b89dd28fcb5933de29aa3" width="1633" height="582" data-path="images/on-call-pay-calculator/datainclude.png" />
</Frame>

## Generating Pay Reports

Once pay rules are configured, generating a report is straightforward. Select a start and end date (up to a maximum of six months per report) and create the report. Rootly processes the report in the background and attaches both CSV and XLSX files once complete.

Each report includes a configuration summary that documents the pay type, currency, rate usage, and whether shadow shifts were included. This ensures reports remain self-describing even when reviewed months later.

## Best Practices

Follow these best practices to ensure your on-call pay reports remain accurate, consistent, and easy to interpret.

* **Attach schedules to escalation policies**\
  Only schedules that are connected to escalation policies are considered active. If a schedule is not assigned to an escalation policy, it will be excluded from pay calculations.

* **Finalize pay rules before generating reports**\
  Pay reports snapshot the active configuration at the time they are created. Reviewing and locking in your pay rules before running a report helps avoid discrepancies and confusion later.

* **Use granular time breakdown for differentiated pay models**\
  If your organization compensates active incident response differently from passive standby time, enable granular time breakdown early. This gives you visibility into alert-driven activity and allows you to validate the data before using it for payroll.

* **Explicitly include shadow shifts when compensating training time**\
  If shadowing is considered paid training, make sure shadow shift inclusion is enabled. This ensures shadow hours are consistently tracked and prevents missed or inconsistent compensation.

## Frequently Asked Questions (FAQs)

<AccordionGroup>
  <Accordion title="Which schedules are included in pay reports?">
    Only schedules that are actively connected to escalation policies are included. This ensures pay reports reflect real on-call responsibility rather than unused or draft schedules.
  </Accordion>

  <Accordion title="Can I change pay rules after generating a report?">
    You can change pay rules at any time, but changes only apply to future reports. Each report captures a snapshot of the rules used at the time it was generated.
  </Accordion>

  <Accordion title="How are business hours defined?">
    Business hours are defined as 9 AM to 5 PM on weekdays. All weekend time is categorized separately.
  </Accordion>

  <Accordion title="What happens if a user is both on-call and shadowing?">
    Rootly automatically removes overlapping time so the user is not double-paid for the same period.
  </Accordion>

  <Accordion title="Why is my report missing some users or shifts?">
    This usually means the schedule was not attached to an escalation policy during the selected date range, or the report exceeds the allowed six-month duration.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).