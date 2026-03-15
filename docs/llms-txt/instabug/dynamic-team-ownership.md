# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/team-ownership/dynamic-team-ownership.md

# GitHub Integration For Team Ownership

The GitHub CODEOWNERS integration allows Luciq to automatically generate and maintain Crashes team ownership rules based on the `CODEOWNERS` file in your GitHub repository.

Instead of manually configuring file paths and assigning them to teams, Luciq fetches and syncs your CODEOWNERS file to ensure accurate, up-to-date ownership rules at scale.

### How It Works?

{% stepper %}
{% step %}
Once connected, Luciq fetches your `CODEOWNERS` file from your GitHub repository.
{% endstep %}

{% step %}
Parses all ownership patterns (paths, filenames).
{% endstep %}

{% step %}
Extracts teams (GitHub teams).
{% endstep %}

{% step %}
Lets you map teams to Luciq teams in a simple UI.
{% endstep %}

{% step %}
Generates crash ownership rules automatically based on this mapping.
{% endstep %}

{% step %}
Keeps rules in sync whenever your `CODEOWNERS` file changes on GitHub.
{% endstep %}
{% endstepper %}

This automation ensures that crash reports are always routed to the correct team without manual updates.

### Prerequisites

Before you begin:

* You must be an **Owner** or **Admin** or have permissions to manage Team Ownership.
* Your GitHub organization must allow installing GitHub apps.
* Your repository must contain a valid `CODEOWNERS` file.

***

#### How to Set it up?

{% stepper %}
{% step %}

#### Connect Luciq to GitHub

1. Go to **Settings → Source Code Management** in the Luciq dashboard.<br>

   <figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fc3s5BlWbRrEAIbDr9ZhS%2Fimage.png?alt=media&#x26;token=257f60f2-9430-4131-8cda-9f807596feaf" alt=""><figcaption></figcaption></figure>
2. Click **Connect with GitHub**.
3. Install Luciq App on GitHub or use the Installation ID if you already installed the App<br>

   <figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2Fbm5qUXDUH89wQJb0Yiqf%2Fimage.png?alt=media&#x26;token=a6960dde-ef65-41b0-aa2e-746140d90985" alt=""><figcaption></figcaption></figure>
4. On GitHub; choose the repository you want Luciq to access.
5. Confirm permissions and return to Luciq.
   {% endstep %}

{% step %}

#### Select Repository, Branch, and Features

After connecting:

1. Choose the **repository** that contains your `CODEOWNERS` file.
2. Select the **branch** (e.g., `main`, `master`) where `CODEOWNERS` lives.
3. Select which features should access the integration:
   * `CODEOWNERS` file: allows you to define crashes team ownership by fetching and processing GitHub `CODEONWERS` file.
   * Resolve Agent: An AI-powered feature designed to automate the process of resolving mobile app crashes, enabling developers to resolve issues within minutes. [Learn more](https://docs.luciq.ai/docs/product-guides-smart-resolve#/)
4. Click Continue<br>

   <figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FLhYX6RKj75BjMAf3hcVD%2Fimage.png?alt=media&#x26;token=f4761ad3-638e-4b6b-8381-1dd972f3a6f2" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}

#### Important Note

CODEOWNERS file feature requires only read-access to the `CODEOWNERS` file. It doesn't access your code or make any changes to your Repository.
{% endhint %}
{% endstep %}

{% step %}

#### Review and confirm configuration

Luciq will let you review all the configuration settings including:

* Organization
* Repository
* Branch
* Enabled features

Then you can select whether you want to enable auto-sync for `CODEOWNERS` file or not. The auto-sync will automatically update team ownership rules once the `CODEOWNERS` file is updated on GitHub.

Finally once you confirm all settings and click **Connect**, Luciq will fetch and process the `CODEOWNERS` file

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FBBqBxf42XVFc1XS2Rl30%2Fimage.png?alt=media&#x26;token=7f5244d8-a831-43c3-b955-90ad45c69f7f" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Map `CODEOWNERS` to Luciq Teams

Luciq will extract all teams from your `CODEOWNERS` file (GitHub teams), then try to match the team names to Luciq teams. If matching is not successful then you will see a list of teams that need to be mapped to Luciq teams.

For each team:

1. Select a **Luciq team** that represents their ownership.
2. Save the mapping.
3. You can revisit and update this mapping anytime.

This mapping allows Luciq to convert `CODEOWNERS` rules into crash ownership rules.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2F2ZiPGd8dXuBiuRDR97uA%2Fimage.png?alt=media&#x26;token=dbf40e50-5f4e-46df-8fca-0b651b5690b9" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ownership rules are defined for mapped teams only. For Unmapped teams, their rules are defined once the mapping is complete.
{% endhint %}
{% endstep %}

{% step %}

#### Automatic Rule Generation

Once mapping is complete:

* Luciq automatically generates **Team Ownership Rules** based on the parsed `CODEOWNERS` patterns.
* These rules appear on the **Team Ownership** page in your dashboard.
* Each rule references the associated Luciq team.

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FLnnA0cK14mgAtqK1bx4u%2Fimage.png?alt=media&#x26;token=bdf20ca6-b471-4860-a1a0-6e12e7042b41" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Automatic Syncing For `CODEOWNERS` File

Luciq keeps your rules in sync by:

* Monitoring your GitHub repository for any updates to `CODEOWNERS`.
* Re-processing the file when changes are detected.
* Updating ownership rules automatically.
* Sending email notifications to admins when:
  * Code ownership changes
  * New owners appear that need mapping
  * Rules are updated

<figure><img src="https://2991836969-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCha1KrkvNKPdcC0aGvuB%2Fuploads%2FpRoT2d1yqZaOFlGuFh9a%2Fimage.png?alt=media&#x26;token=d2f440da-8062-4969-9c53-03593cd7e2bb" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}

#### **Important Notes**

* **The `CODEOWNERS` file sync process runs once per day at 00:00 UTC.**
* When automatic syncing is enabled, team ownership rules created by `CODEOWNERS` file cannot be edited. The only way to edit these rules is by updating the `CODEOWNERS` file on GitHub.
  {% endhint %}

{% hint style="success" %}
If Automatic syncing is disabled, you will see a banner in the team ownership page to notify you that the `CODEOWNERS` file has changed on GitHub.

You can manually update ownership rules directly from the banner.
{% endhint %}

***

### Processing `CODEOWNERS` File

#### Sample of CODEOWNERS file

`CODEOWNERS` file is a text file that contains paths and/or filenames assigned to certain teams in the following format:

{% code title="CODEOWNERS" %}

```
## App folders
/apps/web/ @frontend-team
/apps/mobile/ @mobile-team @qa-team

## Library and shared folders
/libs/api/ @backend-team
/libs/shared/ @platform-team

## Specific files
/README.md @documentation-team
/scripts/deploy.sh @devops-team

## Wildcard (valid pattern)
*/src/payment @payments-team
/src/checkout/* @checkout-team

## Specific file inside a path
/src/payments/invoice_service.py @payments-team
```

{% endcode %}

#### iOS

Refer to [Matching iOS paths](https://docs.luciq.ai/product-guides-and-integrations/product-guides/automation-and-workflows/team-ownership/..#matching-paths-packages) for more information.

{% hint style="info" %}
Flutter and React-Native uses the same matching logic for iOS.
{% endhint %}

#### Android

Unlike other platforms Android relies on packages (not paths) to assign crashes to teams. Hence, the paths in the `CODEOWNERS` file should include the package.

For example:

Assume the package is named: com.luciq.crashes; Then the path in the `CODEOWNERS` file should be: `/src/main/git/com/luciq/crashes`

#### Supported Wildcard Patterns

On GitHub, you can use wildcards to assign certain patterns to teams but Luciq supports only the following wildcard patterns:

{% hint style="success" %}

### **Example**

**\*/src/payments**

**/src/payments/\***
{% endhint %}

{% hint style="danger" %}

#### Examples of unsupported wildcard patterns

* ***/src/\******/payment/**
* *\***.rb***
* **src/**\*\***/test/**
* **src/action**\*\* /test
  {% endhint %}

#### Team Selection Logic

If multiple teams are assigned to the same path, only the first team on the line will be used.

Example:

```
/src/payment/file1.txt @teamA @teamB
```

@teamA will be assigned to this path
