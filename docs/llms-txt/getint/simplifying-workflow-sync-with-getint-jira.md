# Source: https://docs.getint.io/getting-started-with-the-platform/preparing-for-the-integration/simplifying-workflow-sync-with-getint-jira.md

# Simplifying Workflow Sync with Getint: Jira

Integrating project management workflows, particularly in environments involving Jira among other systems, requires careful consideration of status and transition mappings to maintain consistency across platforms. The process of aligning these elements can become complex, underscoring the need for a well-considered strategy. Such mappings often employ a one-to-one approach, where statuses like "To Do" and "In Progress" are directly correlated across systems, ensuring a streamlined workflow. Nevertheless, certain integration scenarios demand a more flexible one-to-many mapping strategy, where a single status in the source system corresponds to multiple statuses in the target system, adapting to the varied requirements of different workflows.

### Status Mapping with Getint

Within Getint, status mappings are designed to be versatile, supporting both one-to-one and one-to-many approaches for integrating Jira with various systems. This adaptability ensures that whether you're aligning Jira instances or integrating Jira with other project management tools, the process remains seamless. Getint provides visual representations of these mappings, delivering a clear and concise overview of your integrated workflows, thus making it a universal solution for managing complex workflow integrations involving Jira.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fe1IpPr3nyOV3Ik2uZSXf%2Fimage-20240105-082023.png?alt=media&#x26;token=b8a7a997-dd16-4cf6-8bea-1e062d53d35e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Getint makes it easy to map statuses for both one-to-one and one-to-many scenarios. However, if your integration requirements are more complex and involve detailed transition setups, additional customization may be necessary. Our extensive documentation and dedicated [support](mailto:support@getint.io) team are available to assist you in optimizing your workflow transitions.
{% endhint %}

The correct synchronization of a real workflow with restrictions can feel like a puzzle. We want transitions to flow freely, but even with the right transitions, weird warnings might pop up in the logs.

### Understanding the Integration Challenge of Synchronizing Transitions Between Restricted Workflows

While status mappings define the overall relationship, the true challenge lies in synchronizing transitions between restricted workflows. From a technical perspective, transitions cannot always be perfectly mirrored due to inherent limitations in how workflows are configured in Jira. Each status change is governed by strict validation rules to ensure the workflow path is followed correctly. During synchronization, disparities in transition rules between systems can lead to errors that hinder the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fwaznoj4Wt5l7jKQbFBil%2FScreen%2BShot%2B2020-04-14%2Bat%2B11.22.04%2BAM.png?alt=media&#x26;token=0b09fb7a-b6c5-4c09-b356-9a7894170c13" alt=""><figcaption><p>Image from Atlassian Support</p></figcaption></figure>

### Addressing Workflow Restrictions in Status Transitions

While status mappings define the primary relationships, synchronizing transitions within restricted workflows can present challenges. Jira workflows often enforce strict transition rules and validation processes, meaning transitions cannot always be perfectly mirrored across systems. Discrepancies in transition rules may lead to errors during synchronization, which can impact integration stability.

{% hint style="danger" %}
If your Jira workflow restricts necessary transitions, you may encounter an error like this: `[WARN ] 2024-10-25T06:16:32.401Z - [a673999b6-30-177094-1] Change to status [name='Test'] was not possible. It looks like the workflow does not contain the required transition to that status.`

If this occurs, please review and adjust your Jira transition settings or contact our support team for further assistance.
{% endhint %}

#### **Strategies for Effective Workflow Integration:**

1. **Mirror Workflow Structure:** Replicating the original workflow structure, including identical status names and paths, ensures workflow consistency across integrations involving Jira, whether it's Jira to Jira, Jira to ServiceNow, or other project management tools. This replication minimizes the likelihood of errors due to discrepancies in workflow configuration, ensuring smooth and reliable synchronization across all platforms.
2. **Master Account Permissions:** Initiate synchronization from an account with Master Admin privileges. This approach ensures the synchronization process has the necessary permissions to adjust workflows appropriately.
3. **Enable All-to-All Transitions:** Provide the flexibility to change the workflow as needed by adopting a workflow model that allows transitions from one state to another.

### Enhancing Workflow Flexibility with User-Specific Permissions <a href="#enhancing-workflow-flexibility-with-user-specific-permissions" id="enhancing-workflow-flexibility-with-user-specific-permissions"></a>

An important flexibility aspect comes into play when managing user permissions within a workflow. It's feasible to design a workflow that appears less restricted for certain users while maintaining restrictions for others. This approach caters to the need for both synchronization flexibility and control.

**Steps to Customize Workflows with User-Specific Permissions:**

1. **Access Workflow Management in Jira:**
   * Select the gear icon next to your profile picture on the top right corner of the screen.
   * Select "Issues" to configure the workflows.
   * Go to Workflows, then modify or make a copy of your workflow that you would like to change.
2. **Add New Status and Transition:**
   * Add a new status and create a transition that allows moving from any status. You can name it “Rest user transition” and connect it to the restricted status.
   * Save the changes.
3. **Configure Conditions:**
   * Select “Conditions” and add a condition such as “User is in Any Group.”
   * Add the groups that are allowed to change these statuses.
4. **Publish and Test:**
   * Publish the draft and test the workflow to ensure the new permissions work as expected.

{% embed url="<https://www.youtube.com/watch?v=bfCghlkLwls>" %}

### Assessing Project Needs and Customizing Workflows

1. **Review Project Requirements:**
   * Identify key stages and transitions needed for the task or issue lifecycle.
2. **Create or Edit Workflows:**
   * Add a new workflow or edit an existing one to customize statuses and transitions.
3. **Define Statuses and Transition Rules:**
   * Configure statuses like "To Do," "In Progress," and "Completed," and specify transitions for each status.
4. **Implement Transition Screens:**
   * Attach screens to transitions to gather necessary information during status changes.
5. **Testing and Feedback:**
   * Test the new workflow extensively and collect feedback to refine the setup.
6. **Make Transitions Exclusive:**
   * Tailor-specific transitions to be accessible only by certain users or groups.

### Conclusion <a href="#conclusion" id="conclusion"></a>

Integrating Jira workflows with Getint improves operations and strengthens collaboration. By applying status mappings, adjusting workflows to user permissions, and following a systematic approach of planning, testing, and refinement, teams can align project practices with their needs. These strategies help organizations overcome workflow synchronization challenges, leading to better outcomes and a more adaptive project environment.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
