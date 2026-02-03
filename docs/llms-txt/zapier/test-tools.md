# Source: https://docs.zapier.com/platform/build/test-tools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Tools

> The Zapier platform provides a set of tools to help inform and validate your integration before pushing changes out to users.

## Canary Testing

Canary testing is a way to test new changes temporarily with real users in production with the goal of validating changes to ship new changes with more confidence and reducing bugs. These users are not informed or aware of the changes, as this is usually done at random and in small subsets to obtain a sample. Builders should have careful monitoring in place to watch for errors and rollback when necessary.

### Prerequisites

* Completed build of your Zapier integration, built from the CLI
* If you haven't used Zapier before, you'll want to learn the basics in our [Zapier Getting Started Guide](https://zapier.com/learn/zapier-quick-start-guide/)
* Access to Zapier CLI version 15.16.0 or later

You may want to use the canary tool when adding a new feature, or fixing a bug. For example, if you are planning to roll out a bug fix, you may want to test this out to see if the fix will work. The usual validation steps may include unit tests, and [setting up Zaps for validation](/platform/build/test-monitoring). Unit tests will ensure your integration code functionality matches what you intended to do. Setting up Zaps will ensure the trigger or action works with the inputs you provide. The canary tool ensures your changes work for many existing live Zaps, with different inputs and outputs.

[`zapier-platform canary`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#canarycreate) provides a new way to validate your integration and build confidence that the change can work for all different types of automation set ups.

### Usage Examples

```bash  theme={null}
# Create a canary routing 10% of traffic for 1 hour (3600 seconds)
zapier-platform canary:create 1.0.0 1.1.0 -p 10 -d 3600

# Target specific user for testing with 25% traffic for 30 minutes
zapier-platform canary:create 1.0.0 1.1.0 -p 25 -d 1800 --user user@example.com

# Target specific account (Zapier staff only)
zapier-platform canary:create 1.0.0 1.1.0 -p 15 -d 7200 --account-id 12345

# Check active canary status
zapier-platform canary:list

# Stop canary early if issues are detected
zapier canary:delete 1.0.0 1.1.0
```

### Available Commands

[`zapier-platform canary:create`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#canarycreate) allows you to set the version you want to test with, the version you want to replace with, the percentage of traffic, and a duration before the versions are rolled back.

[`zapier-platform canary:list`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#canarylist) allows you to see the active canary and see how much time is left.

[`zapier-platform canary:delete`](https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#canarydelete) (or deprecated `zapier canary:delete`) You can choose to delete the canary test before the duration is expired in case something unexpected occurs.

### Best Practices

* **Start Small**: Begin with 5-10% of traffic for initial testing
* **Short Duration**: Start with 30-60 minutes for first canary tests
* **Monitor Closely**: Watch for error rate increases, performance degradation, and user reports
* **Test Non-Breaking Changes Only**: Avoid canary testing for breaking changes like API modifications that change input/output formats, authentication flows, or schema structures
* **Use Targeted Testing**: Leverage `--user` or `--account-id` flags to test with specific users - either those who experienced issues you're fixing, or create dedicated test accounts with controlled Zap setups to isolate and validate your changes
* **Communicate**: Inform your team about the canary test timeline and rollback procedures
* **Have Rollback Ready**: Know how to quickly stop the canary if issues arise
* **Document Changes**: Keep notes on what you're testing and expected outcomes

### Monitoring Your Canary

While canary testing, monitor these key metrics:

* **Error Rates**: Watch for spikes in failed Zap runs
* **Task Success Rate**: Monitor successful vs failed task executions
* **Response Times**: Check for performance degradation
* **User Reports**: Monitor support channels for unusual complaints

**Monitoring Tools:**

* Use your integration's analytics dashboard to compare error rates
* Check Zapier's platform metrics for task failure patterns
* Monitor logs for new error types or increased frequency

<Tip>
  Currently, monitoring tools don't isolate canary traffic, so watch for overall
  pattern changes during your test window.
</Tip>

### Troubleshooting

* **High Error Rate (>5% increase)**: Stop canary immediately with `zapier-platform canary:delete` (or deprecated `zapier canary:delete`) and investigate logs
* **Performance Degradation**: Reduce traffic percentage by stopping current canary and creating new one with lower percentage
* **User Complaints**: Check if complaints correlate with canary start time, rollback if confirmed
* **Authentication Failures**: Immediate rollback - auth issues affect user experience significantly
* **Timeouts**: May indicate resource constraints, consider infrastructure scaling before retrying

### FAQ

<AccordionGroup>
  <Accordion title="What happens if I don't rollback in time?">
    The system will automatically rollback to the previous version after the
    specified duration expires.
  </Accordion>

  <Accordion title="Can I extend the duration of a canary test?">
    Yes, you can extend the duration by stopping the existing canary with
    `zapier-platform canary:delete` (or deprecated `zapier canary:delete`), then
    re-running `zapier-platform canary:create` (or deprecated `zapier
        canary:create`) with a new duration.
  </Accordion>

  <Accordion title="How do I monitor the canary test?">
    Use Zapier's monitoring tools and logs to track test performance. Currently,
    there's no way to isolate canary-specific monitoring, so watch for overall
    pattern changes during your test window.
  </Accordion>

  <Accordion title="Can I run multiple canaries at once?">
    No, only one canary can be active at a time. You must delete the current
    canary before creating a new one.
  </Accordion>

  <Accordion title="What percentage of traffic should I start with?">
    Start with 5-10% for initial testing. You can increase gradually if the test
    goes well by creating a new canary with higher percentage.
  </Accordion>

  <Accordion title="How long should a canary test run?">
    Start with 30-60 minutes for initial tests. Longer durations (2-4 hours) are
    appropriate for more extensive validation, but ensure you can monitor
    throughout.
  </Accordion>
</AccordionGroup>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
