# Source: https://help.aikido.dev/pentests/starting-an-assessment.md

# How to Setup a Pentest

Setting up a pentest shouldn't involve weeks of emailing or complex scoping documents. Aikido streamlines the process so you can get your assessment running immediately, whether you're prepping for an audit or just hardening your security posture.

You can watch the 3-minute walkthrough below, or follow the step-by-step guide further down.

{% embed url="<https://www.loom.com/share/2acd4f4b88ec43fbb97cc7562f322d3c>" %}

<p align="center"><a href="https://www.loom.com/share/2acd4f4b88ec43fbb97cc7562f322d3c">How to setup a pentest in Aikido? - Watch Video</a></p>

### Step-by-step Guide

#### Prerequisites

Before starting, ensure you have:

* **Manage Pentests** [permission](https://help.aikido.dev/getting-started/automated-user-management/setting-roles-and-permissions) in Aikido
* **Sufficient credits** in your [wallet](https://help.aikido.dev/miscellaneous-info/wallet-and-credits).
* **Authorization** to scan the target domains.

To launch the wizard, navigate to **Pentests** in Aikido, open your **Project** and click **Create Assessment**.

#### 1. Scope

We recommend focusing on a single application per assessment to keep the report actionable.

{% hint style="warning" %}
**Use a test environment:** Pentests involve destructive actions. To avoid downtime or data corruption, always run assessments on a Staging or QA environment.
{% endhint %}

1. **Enter Domain:** Input your application's URL.
2. **Scope:** Choose to test the entire application or give specific instructions on where to focus the test on.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FaQhQDTvPlYrgrKJOmGyP%2FScreenshot%202025-11-24%20at%2016.32.19.png?alt=media&#x26;token=ae8ddd2e-1fd3-45c6-9186-360adbce10cc" alt=""><figcaption></figcaption></figure></div>

#### **2. Review Discovered Domains**

The system will detect dependencies (e.g., authentication service, API gateways, ... ).

* **Add and mark domains as** `In scope` to be included in the pentest.
* **Add and mark domains as** `Allowed to reach` to allow usage, but exclude from pentesting.
* **Blocked:** Anything that is not defined will be blocked by default for safety.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FENb9IgBG5Pg2Pcw4MWxS%2FScreenshot%202025-11-24%20at%2016.40.38.png?alt=media&#x26;token=50d54887-a44a-42f6-8de2-2d21972522e5" alt=""><figcaption></figcaption></figure></div>

#### 3. Authentication

Aikido uses AI agents to navigate complex login flows. You don't need complex scripts, just tell us how to log in.

* **Define Roles:** Create credential sets for different user types (e.g., `Admin`, `Tenant A User`, `Read-Only User`). This ensures we test authorization logic, not just authentication.
* **Write Instructions:** Use plain English.

  > *Example: "Navigate to /admin. Login with user 'admin' and password '1234'. If a 2FA prompt appears, use the provided OTP secret."*
* **Self-Registration:** If your app allows public sign-ups, the agent can create its own account.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FqsuhuKZMMwDkyfO0BsyP%2FScreenshot%202025-11-24%20at%2016.44.02.png?alt=media&#x26;token=b7ba5eec-2829-4125-bdf8-06cd9eb86d38" alt=""><figcaption></figcaption></figure></div>

#### 4. Code and Documentation

White Box testing significantly increases the ability to analyse deep logic and lowers the risk of missing critical issues. More detailed information [here](https://help.aikido.dev/pentests/leveraging-code-and-documentation).

* **Link Repositories:** Connect your code repo. We index the codebase to identify logic flaws that aren't visible from the outside.
* **Upload Specs:** Attach OpenAPI/Swagger specs or previous pentest reports to guide the scanner toward known sensitive areas.
* **Additional Context:** Provide any additional context that helps to understand the behaviour of the application.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FQWs5T1T4Q8fModJASp2k%2FScreenshot%202025-11-24%20at%2016.47.13.png?alt=media&#x26;token=a91a57c4-6aff-49b5-aa1e-a89252dd7b97" alt=""><figcaption></figcaption></figure></div>

#### 5. Safety

Pentests can be intense. Configure these settings to prevent service degradation.

* **Maximum Requests Per Second:**
  * **High:** Faster completion, higher server load.
  * **Low:** Slower, more gentle load on your system.
* **Allowed Scanning Time:** Restrict pentesting to specific hours to avoid impacting other work.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ff8jYvHr2mMOMrpidH1Hu%2FScreenshot%202025-11-24%20at%2016.48.40.png?alt=media&#x26;token=b465f0e4-f9f4-4977-9cd4-02b16045d2ab" alt=""><figcaption></figcaption></figure></div>

#### 6. Select Assessment Type

Choose the assessment profile that matches your goal.

<table data-view="cards"><thead><tr><th>Scan Type</th><th>Best For</th><th>Output</th></tr></thead><tbody><tr><td><strong>Regular Scan</strong></td><td>Comprehensive audit </td><td>Full PDF Report usable for SOC2 and ISO27001 compliance.</td></tr><tr><td><strong>Release Scan</strong></td><td>CI/CD &#x26; Deployments</td><td>Quick check for low hanging fruit.</td></tr><tr><td><strong>Right-Sized</strong></td><td>Large/complex applications</td><td>Custom coverage &#x26; agent count.</td></tr></tbody></table>

#### 7. Summary & Launch

Review your configuration and click **Run Assessment** to start the scan.

* **Cancellation Policy:** If you realize you made a mistake or something went wrong in the run, you can cancel immediately after launch.
  * *Note: If cancelled early, your credits will be automatically refunded.*

#### Need help?

If the scanner is failing to authenticate or you're unsure about scoping, open the **Intercom chat** in the bottom right corner. Our team is here to help!
