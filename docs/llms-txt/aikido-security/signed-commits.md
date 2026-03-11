# Source: https://help.aikido.dev/aikido-autofix/configure/signed-commits.md

# Signed Commits

Aikido supports signed commits for both **GitHub** and **GitLab** to ensure the authenticity of code changes. While GitHub requires no configuration, GitLab users must add a specific Aikido-provided SSH key to their profile.

## Why use signed commits?

Signed commits provide a layer of cryptographic assurance, proving that code changes originated from Aikido and haven't been altered. This is essential for:

* **Identity Verification:** Guarantees that the commit was actually made by the authorized service.
* **Trust & Security:** Prevents "commit spoofing" where a malicious actor pretends to be a trusted contributor.
* **Audit Readiness:** Helps satisfy security compliance frameworks like **SOC2**, **ISO 27001**, and **HIPAA**.

## Setup

### GitHub

**No configuration required.** GitHub automatically recognizes and signs commits made via the Aikido integration. These will appear with a **"Verified"** badge in your commit history immediately.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FAS40y6xiMC3Vhb7AmDhN%2Fimage.png?alt=media&#x26;token=85c099d2-f8ac-487b-8d9f-d2ae6dc2bc52" alt=""><figcaption></figcaption></figure>

### GitLab

To enable signed commits on GitLab, you must use **Personal Access Token (PAT)** authentication; this feature is not available via OAuth.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F7ikAKnNSaXe8Ey4QqowX%2Fimage.png?alt=media&#x26;token=f34e274c-916d-4998-b86e-3c7696fe9a7d" alt=""><figcaption></figcaption></figure>

**Important Note on Users:** GitLab only supports signed commits for **real user accounts**, not service accounts. The PAT used in Aikido must belong to a real user.

Setup steps:

1. **Navigate to Settings:** In Aikido, go to the [**AutoFix settings** page](https://app.aikido.dev/issues/fix/settings) and click **Authorize** (on initial setup) or **Manage Personal Access Token** (when a token is already set).
2. **Configure the PAT:** Enter the Personal Access Token you generated in GitLab's User Settings in Aikido.
3. **Generate SSH Key:** Click **Generate SSH key** within Aikido to create your unique signing key.
4. **Add to GitLab:**
   * Copy the public key provided by Aikido.
   * In GitLab, click the **User icon** on the top right **> Edit profile > SSH Keys > Add new key**
   * Paste the key and ensure the **Usage type** is set to **"Authentication & Signing"**.
5. **Validate:** Return to Aikido and click **Validate SSH key** to confirm the connection is active.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FEkqVHxici5YIwGGtMpcS%2Fimage.png?alt=media&#x26;token=8c17920c-00c4-4303-b37e-732b2c3e98ee" alt=""><figcaption></figcaption></figure>

You will now see the `Verified` badge on the commits from Aikido:

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fu51WO5mTwljy2CotYpHb%2Fimage.png?alt=media&#x26;token=132ae9d0-2645-49ec-8389-289df385e7db" alt=""><figcaption></figcaption></figure>

Aikido creates a unique SSH key for each account, this SSH key can be recreated by clicking `Delete SSH Key` and creating a new key.
