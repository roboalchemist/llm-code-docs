# Source: https://docs.ox.security/ox-integrations/ai-appsec-advisor/chatgpt.md

# ChatGPT

## Introduction

Integrate ChatGPT with OX to analyze security issues at scale, prioritize remediation, and generate fix guidance directly within the OX platform.

OX uses ChatGPT to summarize issues by risk and type, rank findings by business impact, and create code-level remediation instructions. You can analyze many issues at once and obtain prioritized actions without leaving OX.

After you connect, you can use ChatGPT capabilities when working with security findings in the Active Issues page.

## What OX adds

* **Issue summarization:** ChatGPT summarizes security issues by risk level and type across your entire portfolio (for example, 10 critical SQL injection vulnerabilities and 20 high-risk exposed secrets).
* **Prioritized remediation:** ChatGPT ranks issues by business impact and provides a recommended fix order to maximize security improvements.
* **Code-level fix guidance:** ChatGPT generates specific remediation instructions and code suggestions for each finding, accelerating resolution.

## Connection methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with an OpenAI API key.

## Prerequisites

**OX**

* Permission to configure connectors

**ChatGPT/OpenAI**

* OpenAI user account with permissions to create and manage API keys

## Connect with a token

### Step 1: Create API key \[OpenAI]

For OpenAI documentation, see the article [API Overview](https://platform.openai.com/docs/api-reference/authentication).

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your OpenAI account.
3. From the header, select **API Platform**.
4. From the left menu, select **API keys**.
5. Select **+ Create new secret key**.
6. In **Create new secret key**, enter the details:
   * **Owned by:** You or Service Account.
   * **Name:** A name for the key.
   * **Project:** Select a project or accept the default.
   * **Permissions:** All, Restricted, or Read only. If restricted, apply the relevant permissions.\ <br>

     <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4722c1f53f6e099e1bbd06eabe3b9f17c36e0338%2FPicture9.png?alt=media" alt="" width="241"><figcaption></figcaption></figure></div>
7. Select **Create secret key**.
8. Copy and store the API key in a secure location. You cannot view it again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate the API key according to your policy.

### Step 2: Connect to OX \[OX]

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > AI AppSec Advisor** and select **ChatGPT**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e664e05a940332907c9b25d911bf1f493b0f44d1%2FchatGPT%20%E2%80%93%20config%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. In **Configure your ChatGPT credentials**, enter the API key i(token).
4. Select **VERIFY CONNECTIVITY**.
5. A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your API key and permissions.
6. Select **CONNECT**.
