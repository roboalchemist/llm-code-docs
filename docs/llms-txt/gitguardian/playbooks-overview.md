# Source: https://docs.gitguardian.com/platform/automate-with-playbooks/playbooks-overview.md

# Automate with playbooks

> Overview of GitGuardian playbooks for automating incident response workflows such as developer notification and severity management.

Playbooks enable you to **automate some remediation behaviors** across your workspace. They are process flows that run a series of automated jobs without manual intervention from security or software engineers.

Playbooks are accessible in [your workspace settings](https://dashboard.gitguardian.com/settings/workspace/playbooks).

:::info
Playbooks is a business feature.
Only managers can activate/deactivate playbooks.
:::

<iframe width="560" height="315" src="https://www.youtube.com/embed/_q4r8DlioRU?controls=0&modestbranding=1" title="Working With GitGuardian Playbooks To Automate Your Workflows" frameBorder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>

## How playbooks work

Playbooks operate through **event-driven automation**:

1. **Trigger event**: Something happens in your GitGuardian workspace (e.g., new incident detected)
2. **Condition check**: The playbook evaluates if its conditions are met  
3. **Automated action**: If conditions match, the playbook executes its configured actions
4. **Audit trail**: All actions are logged with "GitGuardian Bot" attribution

## Apply to Internal and/or Public Monitoring

Playbooks can be configured to work with:
- **Internal incidents** (from [Internal Monitoring](../../internal-monitoring/home))
- **Public incidents** (from [Public Monitoring](../../public-monitoring/home) - if this product is enabled for your workspace) 

Each playbook shows an "Apply to" section where you can toggle support for internal incidents and/or public incidents.

Learn more about [available playbooks](./available-playbooks.md).

> If you need additional playbooks, submit your request [here](https://roadmap.gitguardian.com/tabs/10-ongoing/submit-idea).
