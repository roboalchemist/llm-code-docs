# Source: https://docs.iredmail.org/easy.to.ee.html

Title: Migrate from iRedMail Easy to iRedMail Enterprise Edition

URL Source: https://docs.iredmail.org/easy.to.ee.html

Published Time: Thu, 26 Feb 2026 14:16:47 GMT

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Migrate from iRedMail Easy to iRedMail Enterprise Edition](https://docs.iredmail.org/easy.to.ee.html#migrate-from-iredmail-easy-to-iredmail-enterprise-edition)
    *   [Summary](https://docs.iredmail.org/easy.to.ee.html#summary)
    *   [Notes before getting started](https://docs.iredmail.org/easy.to.ee.html#notes-before-getting-started)
    *   [Migrate](https://docs.iredmail.org/easy.to.ee.html#migrate)
    *   [FAQ](https://docs.iredmail.org/easy.to.ee.html#faq)
        *   [DKIM signature is now signed by the new milter program](https://docs.iredmail.org/easy.to.ee.html#dkim-signature-is-now-signed-by-the-new-milter-program)

Attention

iRedMail Team can help migrate your iRedMail server, feel free to [Contact Us](https://www.iredmail.org/contact.html).

Summary
-------

iRedMail Enterprise Edition (`EE` for short) uses almost same deployment code as iRedMail Easy, migrating from iRedMail Easy to EE is a breeze.

Notes before getting started
----------------------------

*   iRedAdmin and iRedAdmin-Pro are not available after migrated to iRedMail EE, because iRedMail EE offers same (and more) features as iRedAdmin-Pro, hence no need to run iRedAdmin(-Pro) after migrated.
*   An EE license is required. Please login or sign up to our iRedMail Store website to get a free trial license or purchase one: [https://store.iredmail.org/](https://store.iredmail.org/).
*   We recommend to [manage ssl cert with the builtin certificate manager](https://docs.iredmail.org/ee.cert.html) offered by EE after migration.

Migrate
-------

*   Login to iRedMail Easy platform: [https://easy.iredmail.org/](https://easy.iredmail.org/)
*   Click `Mail Servers` on left sidebar.
*   Click `Export` button right beside the server hostname you want to migrate. It will display a modal window to show you the server settings.
*   Click `Copy` on the modal window to copy server settings in JSON format.

![Image 1](https://docs.iredmail.org/images/ee/easy.to.ee-1.png)![Image 2](https://docs.iredmail.org/images/ee/easy.to.ee-2.png)

*   Follow [the iRedMail EE installation tutorial](https://docs.iredmail.org/install.ee.html) to download and launch EE on the server you deployed with iRedMail Easy platform.

EE launches the http service on port `8080`, please stop the firewall temporarily so that you can access this port:

    *   on RHEL/CentOS/Rocky/Alma, run: `service firewalld stop`
    *   on Debian/Ubuntu, run: `service nftables stop`
    *   on OpenBSD, run: `pfctl -d`

*   Visit http port 8080 with a web browser which supports JavaScript, you should see page like below:

![Image 3](https://docs.iredmail.org/images/ee/easy.to.ee-3.png)

*   Paste the copied server settings, then click `Migrate` button to import settings.
*   Click `Next` to review the settings.
*   Click `Migrate` to start the migration immediately. It should finish in seconds.
*   After migrated, access the new web UI `https://<your-server>/admin/`, login with same admin accounts you used to login to iRedAdmin or iRedAdmin-Pro.
*   After logged in, click `Deployments` on left sidebar, then click `Re-perform full deployment` to apply configuration changes to fully migrated to EE.

That's all. If you experienced any issue, please report via the ticket system on the [iRedMail Store](https://store.iredmail.org/tickets) website.

FAQ
---

### DKIM signature is now signed by the new milter program

*   Existing DKIM keys were migrated by EE automatically during migration.
*   DKIM signature is now signed by the new milter program (`/usr/local/bin/milter*`), it's developed by iRedMail team.
*   DKIM keys are stored in SQL table `vmail.dkim`.
*   After login to EE as global admin, you can click the `DNS` badge on domain list page to check DNS records of the email domain, including DKIM key.
*   Feel free to generate DKIM key for each domain, then publish the public key on DNS.
