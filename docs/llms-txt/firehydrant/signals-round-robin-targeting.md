# Source: https://docs.firehydrant.com/docs/signals-round-robin-targeting.md

# Round Robin Targeting

Round-robin functionality in Escalation Policy Steps allows users to configure even or consistent rotation sequences for notifications, enabling more flexible and automated notification patterns. This feature is particularly useful for teams wanting to distribute on-call responsibilities across team members.

## Configuring Round-Robin Distribution

To set up round-robin notifications:

1. Navigate to your team's Escalation Policy page
2. Create a new Escalation Policy or edit an existing one
3. In any step, toggle on the round-robin feature
4. Choose your distribution method:
   * **Distribute evenly**: Each time a new alert arrives, notifications cycle to the next target in sequence
   * **Distribute consistently**: Each time a new alert arrives, notifications always start with the first target
5. Add notification targets:
   * Team members
   * On-call schedules
   * Slack channels (if configured for the team)
   * External team members (users not on the current team)
6. Optional: Add additional steps
   * Click "Add another step"
   * Set duration for the new step
   * Configure different round-robin groups or targets
7. Configure any handoffs if needed
8. Click "Create escalation policy"

<Image alt="Round robin example" align="center" src="https://files.readme.io/207a99713f90339fef592b68ce73c246f2b89318fccaccd100812662819e4ef6-robin-robin-steps.png">
  Round robin example
</Image>

## Distribution Methods

### Distribute evenly

With even distribution, FireHydrant advances through the sequence for each new alert. For example:

* First Alert: Alice → Bob → Charlie
* Second Alert: Bob → Charlie → Alice
* Third Alert: Charlie → Alice → Bob

### Distribute consistently

With consistent distribution, FireHydrant always starts with the first person in the sequence for each new alert. For example:

* First Alert: Alice → Bob → Charlie
* Second Alert: Alice → Bob → Charlie
* Third Alert: Alice → Bob → Charlie

### Notification targets

When configuring round-robin steps, you can include various notification targets:

* On-call schedules
* Slack channels
* External team members
* Webhooks

> 📘 Note:
>
> If a notification target (such as an on-call schedule) has no active user, FireHydrant will immediately advance to the next target in the sequence.

### Best Practices

* Use even distribution when you want to rotate the notification load across team members
* Use consistent distribution when you want alerts to always follow the same notification sequence
* Combine round-robin with appropriate delays between steps to give responders time to acknowledge alerts
* Review and adjust your distribution patterns periodically based on team feedback and alert volumes

### Permissions

Users with <Glossary>Member</Glossary> permissions can configure round-robin settings within their teams' escalation policies. Users with <Glossary>Owner</Glossary> permission can configure these settings for all teams.

For more information about permissions, visit [Role-Based Access Controls](🔗).