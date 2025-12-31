# Source: https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/install-run-via-cli.md

# Install/run via CLI

1. **Prerequisites:** Before proceeding, ensure you've completed all necessary [**prerequisites for self-hosted**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/prerequisites) AI Code Review Agent.
2. **Start Docker:** Ensure Docker is running on your machine.
3. **Repository Download:** [**Download the AI Code Review Agent**](https://github.com/gitbito/codereviewagent) GitHub repository to your machine.
4. **Extract and Navigate:**

* Extract the downloaded .zip file to a preferred location.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBauSkjRmacbzGKV3ESwO%2F1.PNG?alt=media&#x26;token=4faa99de-529c-4b75-bb73-2c5bccf26850" alt=""><figcaption></figcaption></figure>

* Navigate to the extracted folder and then to the “cra-scripts” subfolder.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FeupW2typotZUOO8hbmke%2F2.PNG?alt=media&#x26;token=f955c60c-cdd4-480a-8bda-f90ef3c5376c" alt=""><figcaption></figcaption></figure>

* Note the full path to the “cra-scripts” folder for later use.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJB3b2oKe3UEEz0xBIzI1%2Fcra_5.png?alt=media&#x26;token=86d352d7-990b-4392-9e3f-3cf451b22d5c" alt=""><figcaption></figcaption></figure>

5. **Open Command Line:**
   * Use Bash for Linux and macOS.
   * Use PowerShell for Windows.
6. **Set Directory:**
   * Change the current directory in Bash/PowerShell to the “cra-scripts” folder.
   * Example command: `cd [Path to cra-scripts folder]`
   * Adjust the path based on your extraction location.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F1VSZoDtgl9NwqFqu3A44%2F6.PNG?alt=media&#x26;token=3fdefd2a-dad1-436d-911f-51f216d1ef76" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FFGkgrLhGlvDiTc5lLePW%2F7.PNG?alt=media&#x26;token=2058e7a7-7819-49cc-ad69-8b4b90af9d12" alt=""><figcaption></figcaption></figure>

7. **Configure Properties:**
   * Open the **bito-cra.properties** file in a text editor from the “cra-scripts” folder. Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
   * Set mandatory properties:
     * mode = cli
     * pr\_url
     * bito\_cli.bito.access\_key
     * git.provider
     * git.access\_token

{% hint style="info" %}
**Note:** Valid values for git.provider are GITHUB, GITLAB, or BITBUCKET.
{% endhint %}

* Optional properties (can be skipped or set as needed):
  * git.domain
  * code\_feedback
  * static\_analysis
  * dependency\_check
  * dependency\_check.snyk\_auth\_token
  * review\_scope
  * exclude\_branches
  * exclude\_files
  * exclude\_draft\_pr

{% hint style="info" %}
**Note:** Detailed information for each property is provided on [**Agent Configuration: bito-cra.properties File**](https://docs.bito.ai/ai-code-reviews-in-git/install-run-as-a-self-hosted-service/agent-configuration-bito-cra.properties-file) page.
{% endhint %}

{% hint style="info" %}
Check the [**Required Access Tokens**](https://docs.bito.ai/ai-code-reviews-in-git/prerequisites#required-access-tokens) guide to learn more about creating the access tokens needed to configure the Agent.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Ftwj5rCsz3vdrUfflvjxI%2Fproperties_file.png?alt=media&#x26;token=e39a928d-accf-454a-af03-ffb97dbc68a5" alt=""><figcaption></figcaption></figure>

8. **Run the Agent:**
   * On Linux/macOS in Bash: Run `./bito-cra.sh bito-cra.properties`
   * On Windows in PowerShell: Run `./bito-cra.ps1 bito-cra.properties`

{% hint style="info" %}
This step might take time initially as it pulls the Docker image and performs the code review.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSjDE0OgQ9x2lZfR5mjh6%2F8.PNG?alt=media&#x26;token=f122f4a8-cd4f-46e2-8afd-6fa7efc80234" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FK41KV7WlXAmuZpZCqojj%2Fcra_6.png?alt=media&#x26;token=0c66339b-6cce-4942-b4d5-f1ae85cdae64" alt=""><figcaption></figcaption></figure>

9. **Final Steps:**
   * The script may prompt values of mandatory/optional properties if they are not preconfigured.
   * Upon completion, a code review comment is automatically posted on the Pull Request specified in the **pr\_url** property.

{% hint style="info" %}
**Note:** To improve efficiency, the AI Code Review Agent is disabled by default for pull requests involving the **"main"** branch. This prevents unnecessary processing and token usage, as changes to the **"main"** branch are typically already reviewed in release or feature branches. To change this default behavior and include the **"main"** branch, please [**contact support**](mailto:support@bito.ai).
{% endhint %}

## Screenshots

### Screenshot # 1

{% hint style="info" %}
*AI-generated pull request (PR) summary*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fk5wsTj4siolCcaZqHRIX%2Fscrnli_9_13_2024_12-33-56%20PM.png?alt=media&#x26;token=63cb7da9-21ca-41a1-83ba-9b107d07a6cf" alt=""><figcaption></figcaption></figure>

### Screenshot # 2

{% hint style="info" %}
**Changelist** showing key changes and impacted files in a pull request.
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FyH8h3KVhYqjy8nSHQCby%2Fchangelist_by_bito.png?alt=media&#x26;token=99c64f3d-f554-47fd-aab7-f2d8d9994c09" alt=""><figcaption><p>Changelist in AI Code Review Agent's feedback.</p></figcaption></figure>

### Screenshot # 3

{% hint style="info" %}
*AI code review feedback posted as comments on the pull request.*
{% endhint %}

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FP0sUIAZ3Lq0FqL9ytfPF%2Fscrnli_9_13_2024_12-49-29%20PM_cropped_3.png?alt=media&#x26;token=d74d3b27-4831-4735-9559-6f9da191e910" alt=""><figcaption></figcaption></figure>
