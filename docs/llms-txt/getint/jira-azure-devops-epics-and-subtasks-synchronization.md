# Source: https://docs.getint.io/guides/integration-synchronization/jira-azure-devops-integration/jira-azure-devops-epics-and-subtasks-synchronization.md

# Jira - Azure DevOps: Epics and Subtasks Synchronization

Integrating Jira with Azure DevOps can significantly improve team collaboration and workflows. One of the key aspects of this integration is syncing Epics and Subtasks between the two platforms. This article will guide you through the process of setting up and maintaining subtask synchronization using a third-party tool called Getint.

### How to Map Epics and Subtasks

#### 1. Mapping Epics and Subtasks

* Ensure that Epics and Tasks are mapped accordingly between Jira and Azure DevOps. Match the counterpart items on both sides of the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fdu5Wa1K93MlG6Yq2BOvE%2FEpics%20and%20Subtasks%20synchronization.png?alt=media&#x26;token=402fe976-3e1c-4e1a-9978-0d46d176cb67" alt=""><figcaption><p>Example of the correct order for hierarchy levels.</p></figcaption></figure>

{% hint style="warning" %}
When mapping Epics from Jira, don't forget to also map the **Epic Name** (if available). Otherwise, the epics will fail to create.
{% endhint %}

#### 2. Enable the Epic and Subtask Links

* Open the Task - Task type mapping. Then, click on the **Hierarchy** tab, and check the box to enable the **Epic relationship**. Afterward, display the dropdown option and select the corresponding parent link for both sides.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXguLyUTlNiWxRBX3EFYa%2FEnabling%20epic%20relantionship%20in%20Jira%20Azure%20DevOps%20integration.png?alt=media&#x26;token=8167ebcf-b4cb-4167-b703-021182428680" alt=""><figcaption></figcaption></figure>

* For Subtasks, access the relevant type mapping. Next, activate the **Synchronize Subtasks relationship**. Finally, open the dropdown menu and choose the **Parent Link** option. Determine whether the subtasks should synchronize with their counterpart or be linked to a specific parent task by providing the task's ID.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FqntZzr8XaABWBdu2ctWA%2FEnabling%20subtasks%20relantionship%20Jira%20Azure%20Integration.png?alt=media&#x26;token=4f109c68-7dde-48b8-ac8d-cfcd3ecedbc0" alt=""><figcaption></figcaption></figure>

* After enabling this feature, any new Epics and Subtasks will be automatically synchronized with their parent/child task on Jira and Azure DevOps.

{% embed url="<https://www.loom.com/share/7df417d3d42042cba54f7115ae042005?sid=65b9aa78-e9cf-4ac7-9560-b6b088c17eae>" %}

* Click **Apply** to submit the changes and save your integration.

#### 3. Considerations to Take

* **Respect hierarchy levels:** Use Quickbuild to automatically align type mappings and create links. For manual integration, order issues correctly to prevent sync errors: **Epics** first, **Stories/Tasks/Bugs** second, and **Subtasks** last.
* **For existing projects:** Move or bulk-move issues in order, starting with Epics, followed by Tasks and Subtasks. This ensures proper sync with existing parents on the other side.

{% hint style="warning" %}
Do not modify the **Hierarchy** options within Epics, as this will break the integration. Only enable relationships for Stories/Tasks/Bugs and Subtasks.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
