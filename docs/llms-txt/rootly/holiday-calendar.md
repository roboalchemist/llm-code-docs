# Source: https://docs.rootly.com/on-call/holiday-calendar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding a Holiday Calendar

> Preview team holidays and PTO directly alongside your on-call schedules to proactively identify coverage gaps.

## Overview

Holiday calendars allow you to overlay your team’s **holidays, vacations, and paid time off (PTO)** directly on top of your Rootly on-call schedules. By visualizing time off alongside on-call coverage, teams can proactively identify potential gaps, avoid paging unavailable responders, and make adjustments before incidents occur.

Rather than reacting to conflicts after an alert fires, holiday calendars help you plan coverage with confidence—especially for global teams, shared rotations, and extended leave periods.

Holiday calendars are read-only previews. They do not automatically change schedules, but they make it easy to spot conflicts and quickly create overrides when needed.

***

## Creating a Holiday Calendar

Holiday calendars are added using an **iCal (ICS) feed**, which allows Rootly to continuously sync events from your existing calendar tools.

To create a new holiday calendar:

1. Navigate to **On-Call → Schedules** in the Rootly dashboard.
2. In the calendar preview, open the **Holiday calendars** dropdown.
3. Select **Add your team’s holiday calendar**, then choose **Add a holiday calendar**.
4. Paste the **iCal URL** for your team’s holiday or PTO calendar.
5. Provide a clear, descriptive name so teammates understand what the calendar represents.
6. Select the appropriate timezone (or leave it blank to allow Rootly to infer it from the calendar).
7. Click **Add** to save.

Once added, Rootly will fetch the calendar and sync its events automatically.

Back in the schedule view, you can select the holiday calendar from the dropdown to immediately see upcoming holidays and PTO displayed alongside your on-call shifts.

<img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/on-call/holiday-calendar-schedule-integration.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=ef67de83a6c4a94f370e39158a26b1e2" alt="Holiday calendar preview with schedule" width="2010" height="672" data-path="images/on-call/holiday-calendar-schedule-integration.webp" />

***

## How Holiday Calendars Work in Practice

When a holiday calendar is enabled for preview, Rootly overlays calendar events directly onto the on-call schedule timeline. This makes it easy to see when a responder is scheduled to be on call during a holiday or vacation period.

Rootly intelligently expands recurring events, applies the correct timezone, and normalizes all-day events so conflicts are accurately detected. If a shift overlaps with a holiday or PTO event, that shift is visually highlighted to draw attention to the potential issue.

Holiday calendars are continuously kept up to date. Rootly automatically resyncs events in the background, so changes made in your source calendar are reflected without manual intervention.

***

## Identifying and Resolving Conflicts

When Rootly detects a potential conflict—such as an on-call responder being on vacation—it highlights the affected shift directly in the schedule view.

From there, you have a few options:

* Review the conflict and confirm coverage is acceptable.
* Create a temporary override to assign another responder.
* Adjust the schedule to redistribute coverage.
* Intentionally ignore the conflict if the responder is still available.

To take action quickly, you can click directly into the highlighted event and start the override flow with dates and times prefilled.

For step-by-step guidance on making these adjustments, see\
[Creating Overrides](https://docs.rootly.com/on-call/on-call-shifts#create-overrides-for-on-call-shifts).

***

## Best Practices

Using holiday calendars effectively can significantly improve on-call reliability. Many teams follow these best practices:

* Maintain a single shared PTO calendar per team or region.
* Use clear naming conventions (for example, “EMEA Holidays & PTO”).
* Review upcoming conflicts during on-call handoffs or planning meetings.
* Combine holiday calendars with overrides rather than editing schedules directly.
* Keep calendars synced rather than manually managing time-off in multiple systems.

Holiday calendars work best as an early-warning system—helping teams stay ahead of coverage issues instead of reacting under pressure.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Do holiday calendars automatically change my on-call schedule?">
    No. Holiday calendars are used for **visibility and planning only**.\
    They do not automatically reassign shifts or remove responders. You remain in full control of when and how overrides are created.
  </Accordion>

  <Accordion title="What calendar formats are supported?">
    Rootly supports standard **iCal / ICS feeds**. These can come from tools like Google Calendar, Outlook, or other calendar providers that expose an iCal URL.
  </Accordion>

  <Accordion title="How often does Rootly sync holiday events?">
    Holiday calendars are synced automatically in the background.\
    Rootly refreshes events on creation and continues to resync periodically to ensure changes in your source calendar are reflected accurately.
  </Accordion>

  <Accordion title="What happens if an event is recurring or all-day?">
    Rootly expands recurring events and normalizes all-day events so conflicts are detected correctly.\
    This ensures that multi-day vacations and company-wide holidays are fully accounted for when reviewing coverage.
  </Accordion>

  <Accordion title="Can I use multiple holiday calendars?">
    Yes. Teams can add multiple holiday calendars and choose which ones to preview in the schedule view.\
    This is useful for organizations with multiple regions, departments, or distinct PTO policies.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).