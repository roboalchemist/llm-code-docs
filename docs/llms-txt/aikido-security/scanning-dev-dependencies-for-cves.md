# Source: https://help.aikido.dev/code-scanning/scanning-practices/scanning-dev-dependencies-for-cves.md

# Scanning Dev Dependencies for CVEs

{% hint style="warning" %}
Aikido **always** scans dev dependencies for malware. The following article relates to CVE scanning and how to enable.
{% endhint %}

**By default**, Aikido will **not** report vulnerabilities for dependencies that are only installed on the developer machine (devdeps). The assumption here is that they will not ship to production and won't impact the security of your live product.

However, there are some cases in which scanning for dev dependencies might be a valuable addition to the other scans:

* Compliance reasons, including the software that is only available on the developer machines
* SvelteKit: packages are often marked as dev dependency although they make it into production.

We support **JavaScript, Java and Python.**

### Enabling Dev Dependencies Per Repository <a href="#enabling-dev-dependencies-per-repository" id="enabling-dev-dependencies-per-repository"></a>

It is possible to enable dev dependency scanning on per repo basis.

**Step 1.** Contact Aikido to enable the functionality. Quickest way to do this is contact us via chat.

**Step 2.** Go to the detail page of a specific repository and click '**Configure**'.

![Security scan dashboard showing critical PHP issues with statuses and recommended fix times.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0313942cb5d3bcf91797f1718dc117c50813161c%2Fscanning-dev-dependencies-for-cves_b68f0f11-f4e3-4c53-aa1e-60949980d75e.png?alt=media)

**Step 3.** Scroll down in the modal to enable dev dependency scanning

![Option to enable or disable scanning of developer dependencies with warning about false positives.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4099cfa9b8495551c258be88dcce9469cf4e6cd3%2Fscanning-dev-dependencies-for-cves_4c91b233-fb86-4085-b110-18ebc8a54155.png?alt=media)

**Step 4.** Manually trigger a rescan (or wait until the nightly scan) and see new issues coming in.
