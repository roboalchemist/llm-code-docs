# Source: https://docs.gitguardian.com/internal-monitoring/remediate/remediation-scenarios/historical-incidents.md

# Historical incidents

> Step-by-step workflow for triaging and remediating historical secret incidents, including handling orphan incidents from departed developers.

## Before you start

Incidents are not all created equal. Before diving headfirst into remediating hundreds or thousands of your historical incidents, we suggest you set a few rules to prioritize them first. Here are some elements to consider before deciding on the severity of an incident and the priority it should get:

| **Criteria**       | **Example question**                                                |
| ------------------ | ------------------------------------------------------------------- |
| **Type**           | Are these Kubernetes cluster credentials or Slack webhook URLs?     |
| **Validity**       | Can this secret still be exploited?                                 |
| **Presence**       | Is it still in the git history?                                     |
| **Leak status**    | Has my secret leaked outside my organization's perimeter?           |
| **Exposure**       | Is this secret exposed on a public repository my organization owns? |
| **Recency**        | Is this secret from last quarter or from 5 years ago?               |
| **Occurrences**    | Has this secret been exposed in multiple files and repositories?    |
| **Test directory** | Is this secret used for testing purposes?                           |
| **Secret Manager** | Is this secret stored in one or several Secret Managers?            |

In the GitGuardian Internal Monitoring incidents table, make sure you use the searching, filtering, and sorting features to their maximum.

## Tackling historical incidents

### Step 1. Identify your active developers

Export all historical incidents from your GitGuardian dashboard: Filter your incidents using the Tags field with the value From historical scan. Alternatively, you can use the REST API for this operation.

### Step 2. Involve developers in the remediation process

Notify all developers involved, two options are available:

- Option 1 â Share incidents using Developer-in-the-Loop: Use GitGuardianâs REST API to fetch the incidents
  and generate unique sharing links you will have to send to the active developers by email.
- Option 2 â Invite active developers to join your GitGuardian workspace:
  - To give developers access to all their past incidents, use GitGuardianâs SSO login link with a default access level set to Member for new workspace members in combination with the auto-access granting playbook.
  - Go ahead and assign the historical incidents to developers: make sure developers are aware of the remediation process and the expectations you have set for them.

### Step 3. Track your developers' remediation progress

- Workspace Managers can see all historical incidents. Search for a specific developer/commit author email or filter on a specific assignee to see all their incidents.
- View incidents that were left untreated (not ignored or resolved) and leave a note for the developer to get back on the remediation process.

If you choose to remediate historical incidents in batches, you can use the REST API to fetch all incidents matching the conditions
of your choice. Donât forget to store the list of incident Ids of the associated batch to poll the API again and verify if remediation has been conducted. Visit the GitGuardian public [API reference documentation](https://api.gitguardian.com/docs).

## The special case of "orphan incidents"

Your remediation process for historical incidents needs to factor in an important detail: is the developer involved still on staff?
We will refer to incidents that were committed by developers that have left your organization as orphan incidents.
These developers can no longer contribute to the remediation process. You will, unfortunately, have to do without their help or context.
Here is what you can do when faced in this situation:

- If possible, verify the developer is no longer on staff:
  You can query your LDAP or Active Directory if you have one. In the process, identify which teams the developer belonged to when they were active.
- In any case, identify repository admins or users with write access (incident location).

Now, replace **Step 2. Involving developers in the remediation process** described above with the following alternative:

### Step 2. Involve team leads or security champions in the remediation process

- Once all teams impacted by orphan incidents are identified,
  you can assign the historical incidents to engineering leads, repo admins, or any other members in the GitGuardian dashboard.
- Alternatively, if you have a âSecurity Championsâ program in place, you can leverage this helpful resource. Security Champions can take on the task of remediating historical incidents on behalf of the developers no longer on staff.

:::tip

Choose your assignees wisely! Team members involved in the remediation process need to be able to access the repositories or files in which the secrets occurrences were found. Without this, their scope for action might be too limited to help move the remediation process forward.

:::
