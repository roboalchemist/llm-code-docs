# Source: https://help.aikido.dev/getting-started/general-information/scanning-frequencies.md

# Scanning Frequencies

Aikido provides default scanning frequencies for various components to ensure security and performance. Here, you'll learn about these defaults and how to change them.

### Scanning Frequencies <a href="#scanning-frequencies" id="scanning-frequencies"></a>

* By default, for all paid plans, Aikido does **daily** scans for open-source dependencies, SAST, IaC, secrets, cloud, containers, and Front-End Domains.
* Domains scanned with Hosted Domains and APIs are by default done **twice a week** as this has a higher load on your system.
* In case you quickly want to verify whether a fix was implemented correctly, you can trigger a **manual scan** by clicking 'Start Scan' in the UI.

  ![Repositories page showing 9 active repos and a prominent "Start Scan" button.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fcbe998577438b0fd3fe84c23bd2b5f0e13db781%2Fscanning-frequencies_e678ed08-9cb8-4f4f-a651-7ca041202b17.png?alt=media)

> Workspaces on a free plan are scanned every 3 days, and users cannot trigger scans manually. Hosted domains are scanned once a week.

### Changing Scanning Frequency <a href="#changing-scanning-frequency" id="changing-scanning-frequency"></a>

In case you want to change your scanning frequency, you can do this by going to [Advanced Settings](https://app.aikido.dev/settings/advanced) (admins only) and click **Change Scanning Frequency**.

![Set automated scan frequency: daily, every 3 days, weekly, or monthly.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ef470ef8e18ca1021a301bc3c79060a7829f1eec%2Fscanning-frequencies_e91e1100-9205-4824-af06-f00bf304e481.png?alt=media)
