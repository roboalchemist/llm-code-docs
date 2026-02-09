# Source: https://docs.bito.ai/other-bito-ai-tools/bito-cli/faqs.md

# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/faqs.md

# Source: https://docs.bito.ai/ai-code-reviews-in-git/faqs.md

# FAQs

## How do I whitelist Bito's gateway IP address for my on-premise Git platform?

To ensure the [AI Code Review Agent](https://docs.bito.ai/ai-code-reviews-in-git/overview) operates smoothly with your **GitHub (Self-Managed)** or **GitLab (Self-Managed)**, please whitelist all of Bito's gateway IP addresses in your firewall to allow incoming traffic from Bito. This will enable Bito to access your self-hosted repository.

**List of IP addresses to whitelist:**

* **`18.188.201.104`**
* **`3.23.173.30`**
* **`18.216.64.170`**

The agent response can come from any of these IPs.

## How can I prevent the AI Code Review Agent from stopping due to token expiry?

You should set a longer expiration period for your **GitHub Personal Access Token (Classic)** or **GitLab Personal Access Token**. We recommend setting the expiration to at least one year. This prevents the token from expiring early and avoids disruptions in the AI Code Review Agent's functionality.

Additionally, we highly recommend updating the token before expiry to maintain seamless integration and code review processes.

For more details on how to create tokens, follow these guides:

* **GitHub Personal Access Token (Classic):** [**View Guide**](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
* **GitLab Personal Access Token:** [**View Guide**](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)

## What is "Estimated effort to review" in code review output?

This is an estimate, on a scale of 1-5 (inclusive), of the time and effort required to review this Pull Request (PR) by an experienced and knowledgeable developer. A score of 1 means a short and easy review, while a score of 5 means a long and hard review. It takes into account the size, complexity, quality, and the needed changes of the PR code diff. The score is produced by AI.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FrRiW74jFIfoO1sB43Ipg%2Fscrnli_3_28_2024_6-13-26%20AM.png?alt=media&#x26;token=54a484a5-3be7-48b3-8d51-712779b7f7ac" alt=""><figcaption></figcaption></figure>

## Why does Bito need access to my Git account?&#x20;

Bito requires certain permissions to analyze pull requests and provide AI-powered code reviews. It never stores your code and only accesses the necessary data to deliver review insights.

## What permissions does Bito need?&#x20;

Bito requires: &#x20;

1. Read access to code and metadata: To analyze PRs and suggest improvements&#x20;
2. Read and write access to issues and pull requests: To post AI-generated review comments &#x20;
3. Read access to organization members: To provide better review context&#x20;

## I don’t have admin permissions. Can I still use Bito?&#x20;

If you don’t have admin access, you’ll need your administrator to install Bito on your organization’s Git account. Once installed, you can use it for PR reviews on allowed repositories. GitHub also sends a notification to the organization owner to request the organization owner to install the app.

## Does Bito store my code?&#x20;

No, Bito does not store or train models on your code. It only analyzes pull request data in real-time and provides suggestions directly within the PR.

## Can I choose which repositories Bito has access to?&#x20;

Yes, after installation, you can select specific repositories instead of granting access to all. You can also manage repository access later through our web dashboard.

## What happens after I install the Bito App?&#x20;

Once installed, you’ll be redirected to Bito, where you can:&#x20;

1. Select repositories for AI-powered reviews&#x20;
2. Customize review settings to fit your workflow&#x20;
3. Open a pull request to start receiving AI-driven suggestions

## Where can I get help if I have issues installing Bito?&#x20;

Contact <support@bito.ai> for any assistance.&#x20;
