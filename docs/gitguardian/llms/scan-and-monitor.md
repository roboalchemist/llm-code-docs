# Source: https://docs.gitguardian.com/public-monitoring/explore/scan-and-monitor.md

# Scan and monitor search results

> Scan Explore search results for secrets, create incidents from findings, and set up scheduled monitoring for ongoing automated detection.

After running a search query in Explore, you can scan the results for secrets and set up ongoing monitoring to catch new exposures automatically.

## Scanning search results

### Running a scan
1. Execute your search query to find relevant commits
2. Review the number of results - **scanning is only possible with 10,000 commits or fewer**
3. If results exceed 10,000, refine your search query to reduce the number of matches
4. Click **Scan for secrets** to analyze the commits with GitGuardian's detection engine
5. Wait for the scan to complete - processing time depends on the number of results

## Viewing scan results

### Secret findings
Scan results show:
- **Detected secrets**: Type, severity, and confidence level
- **Source context**: Repository, commit, and file information  
- **Patch details**: Exact location and surrounding code
- **Metadata**: Author, date, and commit message

![Explore scan results](/img/public-monitoring/explore/explore-scan-results.png)

### Creating incidents
For each detected secret, you can:
- **Review context**: Examine the full commit and file details
- **Assess impact**: Determine if the secret poses a real risk to your organization
- **Create incident**: Convert the finding into a public secret incident

:::info
Incidents created from Explore will have the attachment reason "From Explore" to help you track their origin in your incident management workflow.
:::

![Create incident from Explore](/img/public-monitoring/explore/explore-create-incident.png)

## Scheduled monitoring

### Setting up automated scans
You can transform any relevant search into ongoing monitoring:

1. **Name the scan** (optional): After running a search and scan, you can give it a descriptive name
2. **Set frequency**: Choose daily or weekly automated scanning
3. **Automatic incident creation**: New secrets found in subsequent scans automatically become incidents
4. **Continuous protection**: Stay protected as new commits matching your criteria appear

## Next step

- Review [incident remediation](../remediate/remediate-incidents.md) for handling Explore findings
