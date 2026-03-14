# Source: https://docs.getint.io/getintio-platform/workflows/shared-mappings-in-getint-centralized-mapping-for-efficient-integrations.md

# Shared Mappings in Getint – Centralized Mapping for Efficient Integrations

In Getint, **shared mappings** offer a powerful and efficient way to streamline the integration process, especially when managing users, sprints, and other fields across multiple integrations. Shared mappings allow you to define and manage mappings in one central location and reuse them across various integrations. This approach simplifies the synchronization of frequently used fields, making your integration process more efficient and scalable.

This guide will explain how shared mappings work, how to configure them, and the benefits and limitations of using shared mappings, particularly in **Jira to Azure DevOps integrations**. We’ll also provide a table of supported fields and how to manage potential errors and considerations when working with shared mappings across different projects.

***

### Supported Fields for Shared Mappings <a href="#supported-fields-for-shared-mappings" id="supported-fields-for-shared-mappings"></a>

| **Field**            | **Jira**       | **Azure DevOps** |
| -------------------- | -------------- | ---------------- |
| **Assignee**         | Supported      | Supported        |
| **Sprint**           | Supported      | Not Applicable   |
| **Fix Version**      | Supported      | Not Applicable   |
| **Iteration Path**   | Not Applicable | Supported        |
| **Custom Dropdowns** | Not Applicable | Supported        |

At present, **only the fields listed above** support shared mappings in Getint. This means that for these fields, you can create centralized mappings that can be reused across multiple integrations.

***

### What Are Shared Mappings? <a href="#what-are-shared-mappings" id="what-are-shared-mappings"></a>

Shared mappings are reusable mappings that allow you to centralize the configuration of certain fields—such as assignees, sprints, and iteration paths—across multiple integrations. Instead of configuring the same field mappings for every integration individually, you can create a shared mapping once and apply it across multiple integrations.

Shared mappings are particularly useful when:

* You have multiple integrations involving the same users, teams, or project structures.
* You want to ensure consistency across different projects by reusing the same mappings for fields like **Assignees**, **Sprints**, and **Iteration Paths**.
* It is necessary to manage field mappings efficiently across large projects with many integrations.

***

### How Shared Mappings Work <a href="#how-shared-mappings-work" id="how-shared-mappings-work"></a>

#### **1. Creating Shared Mappings**

* When setting up your integration, you can configure fields manually or convert them to shared mappings. For example, when mapping **Assignees** between Jira and Azure DevOps, you can create a shared mapping to handle this centrally.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FklzAJiShQ5rgt2oncKSk%2FShared%20mappings.png?alt=media&#x26;token=3b674839-9321-4ab2-8ff4-7eaddd896ff1" alt=""><figcaption></figcaption></figure>

* Navigate to the field you want to map (e.g., Assignees, Sprints, or Iteration Paths) and select the **Shared Mapping** option:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Ff8dCoOyWWavOqOaazBV6%2FSelecting%20Shared%20mapping.png?alt=media&#x26;token=4ef402cc-6005-42df-b15e-1c2b6cba7909" alt=""><figcaption></figcaption></figure>

* Name the shared mapping and click **Create**:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fb9N3arAYKYQXZRmtKX4A%2FShared%20mapping%20name.png?alt=media&#x26;token=3db5fc31-fb98-4b1e-bcff-66be1ad8c07c" alt=""><figcaption></figcaption></figure>

* The shared mapping will now appear as a centrally managed resource for that field, which you can edit or convert back to standard mapping if needed.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FuOLcK3pomWxqfKL6a7qs%2FAssignees%20shared%20mapping.png?alt=media&#x26;token=f1545bb8-99e9-4ea1-9f1c-b86098334b49" alt=""><figcaption></figcaption></figure>

* To edit or add new assignees, you may either select the option to **Edit Shared Mappings** or go to Workflows → Shared Mappings in the menu tab to access the mappings:

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FgQP5G2Uc4qWfnG7gXqec%2FEditing%20shared%20mappings.png?alt=media&#x26;token=94437b86-d028-45be-aa68-0a399d7e12ac" alt=""><figcaption></figcaption></figure>

#### **2. Reusing Shared Mappings**

* Once a shared mapping is created, it can be reused across multiple integrations. For instance, if you have mapped an assignee from Jira to Azure DevOps, that shared mapping can be applied to other integrations using the same users.
* To do that, go to the integration, select the field, in this case Assignee, and click on Convert to shared mapping. Using the dropdown menu, select the already created Shared Mapping and click on Done. Apply and save the integration.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fd16EFdWY5WbRur4dh8ZO%2FReusing%20old%20mappings.png?alt=media&#x26;token=75a2784d-5d48-418c-ae64-387632082747" alt=""><figcaption></figcaption></figure>

* As soon as shared mappings are applied and saved, any changes made to the mapping will automatically propagate across all integrations using that shared mapping. This makes it easy to manage changes centrally without the need to update each integration individually.
* **Example – Mapping Sprints and Iteration Paths**:

Consider a scenario where you're mapping **Sprints** in Jira to **Iteration Paths** in Azure DevOps. You can create a shared mapping between these fields, but it will only apply to integrations where you've specifically converted the field mappings to shared mappings and chosen that particular shared mapping from the list. This means the shared mapping won't automatically apply to all integrations involving sprints and iteration paths—only to those where it has been manually selected and reused.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTulY3Nv2zl8xkcflONii%2FSelecting%20your%20shared%20mappings.png?alt=media&#x26;token=06ba16fb-ecd6-4dfd-ba7f-e1259686f55c" alt=""><figcaption></figcaption></figure>

When new sprints or iteration paths are added, the shared mapping will update centrally, ensuring that all integrations using the shared mapping are updated automatically.

* **Handling Assignees**:

Similarly, you can map **Assignees** across different integrations. By using shared mappings for assignees, you can easily manage user assignments across projects. If a new user joins the team, you can update the shared mapping in one place, and it will be reflected in all integrations using that mapping.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FOilp9y3KLxlJzdoROz2U%2FHandling%20Assignees.png?alt=media&#x26;token=032c56cf-3817-47c5-8385-b0b1514ca3c7" alt=""><figcaption></figcaption></figure>

***

#### Key Benefits of Shared Mappings

* **Centralized Management**: Instead of configuring mappings for every individual integration, shared mappings allow you to manage your field mappings from one central location.
* **Efficiency**: Shared mappings save time by eliminating the need to repeat the same configurations for each integration.
* **Consistency**: By using shared mappings, you ensure consistency across all integrations, especially when dealing with fields like **Sprints**, **Assignees**, or **Priorities**.
* **Scalability**: As your integrations grow, shared mappings enable you to scale efficiently by managing field mappings globally.

***

#### Potential Limitations and Considerations

* **Field Availability Across Projects**:
  * If the mapped option (e.g., a sprint or user) is not available in the other system or project, the integration will throw an error. To avoid this, ensure that the required options exist in both systems before setting up shared mappings.
* **Project-Specific Fields**:
  * Some fields, such as **Sprints** and **Iteration Paths**, are project-specific and may not work well with shared mappings if the same projects are not part of multiple integrations. For example, if a sprint exists in one project but not in another, reusing the shared mapping could cause conflicts.
  * You need to carefully manage which shared mappings are applied to which projects, particularly when fields are specific to individual projects.
* **Error Handling**:
  * If an option mapped in the shared mapping does not exist in the target project (e.g., a user or sprint), the integration will fail, and an error will be logged. It is important to monitor these errors and make adjustments as needed.
  * For example, if you map an assignee that doesn't exist in Azure DevOps, the system will return an error, and you may need to create the missing user in the target system.

***

#### Important Notes

* **Auto-Propagation**: Any updates to a shared mapping will automatically be reflected across all integrations that use that shared mapping. For example, if a new user is added, all integrations using the shared mapping for assignees will automatically update with the new user.
* **Global Access**: Shared mappings are controlled globally, but only users with access to the connections involved can modify them. If a user doesn’t have access to the connection, they won’t be able to update or use the shared mapping.
* **Field-Specific Mapping**: Not all fields are suitable for shared mappings. Fields like **Sprints** and **Iteration Paths** may be project-specific, whereas **Assignees** can typically be managed globally across projects.

***

#### Conclusion

Shared mappings are a powerful feature within Getint, designed to streamline the integration process and improve efficiency across multiple integrations. By centralizing the mapping of frequently used fields like **Assignees** or **Sprints**, you save time and maintain consistency across your integrations.

However, it’s essential to be mindful of the potential limitations, especially when working with project-specific fields. Always ensure that the mapped options exist on both sides of the integration to avoid errors during synchronization.

For further assistance on using shared mappings or resolving issues, please visit our [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
