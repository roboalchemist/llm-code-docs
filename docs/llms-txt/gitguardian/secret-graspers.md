# Source: https://docs.gitguardian.com/public-monitoring/perimeter/secret-graspers.md

# Secret graspers

> How secret graspers use company-specific terms to identify and attach publicly detected secrets to your organization.

Secret graspers are company-specific terms that allow GitGuardian to identify secrets relevant to your organization. When a secret grasper appears in the context of detected secrets, GitGuardian will attach the secret to your company and create a public secret incident.

![Secret graspers](/img/public-monitoring/perimeter/secret-graspers-list.png)
*In the above example, GitGuardian will create a public secret incident whenever it detects a secret exposed alongside "jira.dev.acme.io" on public GitHub.*

### Adding a new secret grasper

Secret grasper requests can be submitted from the [dedicated settings page](https://dashboard.gitguardian.com/settings/public-monitoring/secret-graspers) and must be validated by GitGuardian to ensure complete relevance. 

To request a new secret grasper:

1. Navigate to [Settings > Public Monitoring > Secret Graspers](https://dashboard.gitguardian.com/settings/public-monitoring/secret-graspers)
2. Click "Request new secret grasper"
3. Provide a name, the term or pattern you want to monitor, and select the type:
   - **Raw**: Exact text matching. GitGuardian will look for the exact string you specify (e.g., `mycompany.com` will match exactly `mycompany.com`)
   - **Regex**: Pattern matching using regular expressions. Allows for more flexible matching (e.g., `mycompany\.(com|org)` will match both `mycompany.com` and `mycompany.org`)
4. If necessary, define tags for this secret grasper (incidents created from this secret grasper will inherit the tag)
5. Submit the request for GitGuardian review

![Request secret grasper](/img/public-monitoring/perimeter/create-secret-grasper-request.png)

### Secret grasper statuses

- **Submitted**: the secret grasper request has yet to be reviewed by GitGuardian.
- **Active**: the secret grasper has been accepted and is actively monitored
- **Paused**: the secret grasper has been accepted but you have chosen to Pause the monitoring. Existing incidents linked to this secret grasper still exist.
- **Rejected**: the secret grasper request has been rejected by GitGuardian. 

:::info
GitGuardian will reject a secret grasper request if: 
- it is not related to your company;
- it is too "generic" and will result in too many non-related findings.
:::

It is possible to delete a secret grasper - if it's not rejected. In this case, the related incidents/occurrences will be deleted permanently. 
If you prefer to stop the monitoring of the secret grasper while keeping the existing incidents, you will want to "pause" it.
