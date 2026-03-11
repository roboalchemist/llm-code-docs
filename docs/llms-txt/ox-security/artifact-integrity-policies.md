# Source: https://docs.ox.security/ox-policies/artifact-integrity-policies.md

# Artifact Integrity Policies

Artifact Integrity policies validate the source and integrity of artifacts running in cloud environments.

These policies ensure that artifacts originate from approved build pipelines and trusted registries, helping confirm that deployed software has not been altered or introduced outside authorized processes. Enforcing artifact integrity reduces supply chain risk and helps maintain trust in the software delivery process.

The article describes the policies in this category, configuration options, and the impact of policy violations. For an overview of policies and policy management, see the [Policies](https://docs.ox.security/ox-policies) article and a more detailed article on the policy group [Artifact Integrity](https://docs.ox.security/ox-policies/artifact-integrity).

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-856a7880a6e4b63f2bbb5111525fac3c0f95db33%2Fartifact%20integriy%20summary%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

## View and manage Artifact Integriy policies

Open each policy to view the business impact and optional settings.

<details>

<summary><mark style="color:purple;">Cloud artifact is not from a trusted registry</mark></summary>

**Purpose:** Detect running artifacts that originate from registries not associated with an approved CI/CD process.

**Business impact:** Artifacts from untrusted registries increase the risk of deploying tampered or malicious images. This can lead to security breaches, data exposure, or compromised runtime environments.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0d179604419ad22397bb4221a3d26775331bfd58%2Fartifact%20integriy%20Cloud%20artifact%20is%20not%20from%20trusted%20registry.png?alt=media" alt=""><figcaption></figcaption></figure>

| Setting                                                                  | Description                                                           | Default               |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------- | --------------------- |
| ON/OFF (toggle)                                                          | Enable/disable the policy.                                            | OFF                   |
| Ignore Application Business Priority for severity calculation (checkbox) | When enabled, severity is not adjusted based on application priority. | <p>OFF</p><p><br></p> |
| Trusted registry and images                                              | Click to add                                                          | Current setting       |

</details>

<details>

<summary><mark style="color:purple;">Registry artifact is not from CI/CD</mark></summary>

**Purpose:** Validates that artifacts running in the cloud have a corresponding build record in the CI/CD pipeline to confirm they were produced through an approved build process. Enforcing CI/CD provenance helps ensure artifact integrity and reduces the risk of supply-chain compromise.

**Business impact:** Running artifacts that cannot be traced back to a CI/CD pipeline may have been introduced outside approved workflows. This increases the risk of deploying tampered or malicious artifacts.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ea71224a1d1dee50f3d38f9e1b839d53570f1fca%2Fartifact%20integriy%20Registry%20artifact%20not%20from%20CICD.png?alt=media" alt=""><figcaption></figcaption></figure>

| Setting                                                                  | Description                                                           | Default               |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------- | --------------------- |
| ON/OFF (toggle)                                                          | Enable/disable the policy.                                            | OFF                   |
| Ignore Application Business Priority for severity calculation (checkbox) | When enabled, severity is not adjusted based on application priority. | <p>OFF</p><p><br></p> |
| Trusted registry and images                                              | Click to add                                                          | Current setting       |

</details>

## View policy issues

1. Open the Active Issues page.
2. Use the **Category** filter and select the policy category to view related active issues.
3. Use the **Policy** filter to narrow the list to a specific policy.
4. Apply the Category and Policy filters separately or together, depending on how specific you want the results to be.
5. Use the search box to refine results, such as filtering by file name, keyword, or rule identifier.

## Create or save policy profiles

When you change a policy’s severity, ON/OFF toggle or any other setting, you must save the current profile or create a new one.

* To save the current profile, click **SAVE** in the page header.
* To create a new profile, click **SAVE AS** in the page header. For instructions, see the section [Create or edit policy profiles](https://open-2c.gitbook.com/url/preview/site_RHimt/~/revisions/esBak1HVuTgsCEeNbzHE/policies?theme=light#create-or-edit-policy-profiles)in the [Policies](https://docs.ox.security/ox-policies/policies)article.

***

<br>
