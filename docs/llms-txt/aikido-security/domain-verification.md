# Source: https://help.aikido.dev/miscellaneous-info/domain-verification.md

# Domain verification

Domain verification confirms that you own or control a domain before Aikido allows scans or integrations that reference it.

{% hint style="danger" %}
Only verify domains that belong to your organization. Verification grants permission to scan and analyze assets associated with that domain.
{% endhint %}

This step prevents misuse of scanning features against domains you do not own and protects both your organization and others from malicious or accidental scans.

<div data-with-frame="true"><figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FBcd5RpJsLFQUFdOkZVg6%2FScreenshot%202025-12-18%20at%2010.42.52.png?alt=media&#x26;token=913874e1-bc55-4ae0-a2e0-075594ab62ff" alt=""><figcaption></figcaption></figure></div>

## Verification methods

You can verify a domain using one of the following methods. All methods prove control over DNS or hosting for the domain.

### Option 1: CNAME record

You add a CNAME record to your domain’s DNS configuration.

* Aikido provides a unique CNAME value
* You create the record in your DNS provider
* Aikido checks that the record resolves correctly

### Option 2: TXT record

You add a TXT record to your domain’s DNS configuration.

* Aikido provides a unique TXT value
* You add the record to your DNS provider
* Aikido verifies the presence of the record

### Option 3: TXT file on the domain (AI Pentest only)

{% hint style="warning" %}
The TXT file is accessed from the [Code and Container scanning IPs](https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning). Make sure these IPs are allowlisted, or domain verification will fail.
{% endhint %}

You upload a TXT file to a root path on your domain.

* Aikido provides a filename and verification token
* You host the file at the required URL
* Aikido confirms the file is publicly accessible from the [allowing-ip-addresses-for-code-container-scanning](https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning "mention"), make sure to add these for validation to succeed

This option is useful when you do not control DNS but can deploy files to the domain.
