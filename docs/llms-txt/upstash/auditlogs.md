# Source: https://upstash.com/docs/common/account/auditlogs.md

# Audit Logs

Audit logs give you a chronological set of activity records that have affected
your databases and Upstash account. You can see the list of all activities on a
single page. You can access your audit logs under `Account > Audit Logs` in your
console:

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=a1f7bdb500057b952aae98ae04f15e78" data-og-width="2082" width="2082" data-og-height="978" height="978" data-path="img/auditlogs/audit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=bedfa2c84d30469398105a583090524e 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=5a89ea16be9559b0e9b3bbde56c85fe3 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=f9b7e364704446997beacce5ee41faa3 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=20743e4ba4cbac1722195f8a6ba588da 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=50c179cdda75724cd1e2e63fd33c514d 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/auditlogs/audit.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=0b090d4b57972436502d749a42f6b194 2500w" />
</Frame>

Here the `Source` column shows if the action has been called by the console or via
an API key. The `Entity` column gives you the name of the resource that has been
affected by the action. For example, when you delete a database, the name of the
database will be shown here. Also, you can see the IP address which performed the
action.

## Security

You can track your audit logs to detect any unusual activity on your account and
databases. When you suspect any security breach, you should delete the API key
related to suspicious activity and inform us by emailing
[support@upstash.com](mailto:support@upstash.com)

## Retention period

After the retention period, the audit logs are deleted. The retention period for free databases is 7 days, for pay-as-you-go databases, it is 30 days, and for the Pro tier, it is one year.
