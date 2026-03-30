# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/how-to-allow-list-in-microsoft-defender-smartscreen.md

# How to Allow List in Microsoft Defender SmartScreen

Microsoft Defender SmartScreen protects users from suspicious websites—but during phishing simulations, it may block or warn against legitimate Keepnet campaign URLs. This can distort your results and interrupt phishing simulation training.

To ensure smooth and accurate simulation performance across your organization, Keepnet recommends allowlisting simulation domains using centralized, scalable methods.

## Step 1: Identify Keepnet Simulation Domains

You should allowlist all domains used in simulations. Please follow the steps below to get the full list of the simulation domains:

* Log in to the **Keepnet Platform**
* Go to **Phishing Simulator → Settings → Domains**, then export or copy your domain list.

## Step 2: Choose Your Allow Listing Method

| Environment                                | Recommended Method                           |
| ------------------------------------------ | -------------------------------------------- |
| Microsoft Defender for Endpoint            | **Method A: Defender Indicators**            |
| Domain-joined Devices via Active Directory | **Method B: Group Policy (GPO)**             |
| Intune-managed Windows/macOS devices       | **Method C: Microsoft Intune Configuration** |

### Method A: Microsoft Defender for Endpoint (Indicators)

**Best for**: Organizations using Microsoft Defender for Endpoint (MDE).

#### Steps:

1. Log into the [Microsoft 365 Defender portal](https://security.microsoft.com).
2. Navigate to: **Settings → Endpoints → Indicators → URLs/Domains → Add item**
3. For each domain:
   * Add wildcards (e.g. `*.test.com`)
   * Set **Action**: `Allow`
   * Enter a clear description (e.g., “Keepnet Simulation Domains”)
   * Choose an **expiration** (or “Never”)
4. Click **Next → Save**
5. Allow up to **24 hours** for changes to propagate across enrolled devices.

This method ensures SmartScreen does not block simulation domains across Defender-protected endpoints.

### Method B: Allowlisting via Group Policy (GPO)

**Best for**: Enterprises managing Windows devices through Active Directory.

This method deploys SmartScreen allowlist rules via GPO across all domain-joined endpoints.

#### 1. Access Group Policy Management

* On your **domain controller**, open the **Group Policy Management Console (GPMC)**.
* Create a **new Group Policy Object (GPO)** or edit an existing one linked to the appropriate **Organizational Unit(s)** (OUs) that include your user or computer accounts.

#### 2. Navigate to SmartScreen Policies

* In the GPO editor, go to:

  ```
  Computer Configuration → Administrative Templates → Windows Components → Microsoft Edge
  ```

  *(Or Internet Explorer if still in use.)*
* Locate **SmartScreen Settings** or **Microsoft Defender SmartScreen** configurations.
  * Policy names may vary based on OS version and browser updates.

#### 3. Configure Allowlist Settings

* Find the policy setting: **SmartScreenAllowListDomains** or **Configure Windows Defender SmartScreen**
* Set the policy to **Enabled**.
* Click **Show** and input each Keepnet domain using wildcards, such as:

  ```
  *.test.com
  *.keepnetlabs.com
  ```
* Click **OK**, then **Apply**, and close the editor.

#### 4. Update Group Policy

* On client machines, update policies by running:

  ```
  bashCopyEditgpupdate /force
  ```

  * Or wait for the next scheduled Group Policy refresh cycle.
* Use **Group Policy Results (gpresult)** or **edge://policy** in Microsoft Edge to confirm application.

#### 5. Confirm Functionality

* From a domain-joined client:
  * Open Edge and visit one of the allowlisted simulation URLs.
  * Confirm that **no SmartScreen warning appears** and the page loads properly.

This ensures consistent, secure, and interruption-free access to all Keepnet campaign resources across your environment.

### Method C: Allowlisting via Microsoft Intune (Windows and macOS)

**Best for**: Organizations managing Windows and macOS devices through Microsoft Intune.

Use this method to centrally configure Microsoft Defender SmartScreen to trust Keepnet simulation domains on all assigned devices.

#### Steps to Allowlist in Intune (Mac and Windows)

1. Navigate to **Devices** in [Microsoft Intune admin center](https://intune.microsoft.com/#home).
2. Select the OS you want to configure (**Windows** or **macOS**).
3. Click **Configuration**.
4. Click **Create → New policy**.
5. Select **Settings catalog → Create**.
6. Enter a name for the profile, such as: `Defender SmartScreen Allowlist for Keepnet Domains`. Then click **Next**.
7. Click **Add settings**.
8. In the search bar, type **"smartscreen"**.
   * Click on **Microsoft Edge** from the search results.
9. Select both:
   * **Configure Microsoft Defender SmartScreen**
   * **Domains where Microsoft Defender SmartScreen won’t trigger warnings**
10. On the left panel:
    * **Enable** the option for **Configure Microsoft Defender SmartScreen**.
    * Add your list of Keepnet simulation domains:

      ```
      *.test.com
      *.keepnetlabs.com
      ```
11. Click **Next**.
12. Under **Scope tags**, click **Next**.
13. Under **Assignments**, assign the profile to the appropriate user or device group(s), then click **Next**.
14. Review the summary and click **Create** to finalize the profile.

This will push SmartScreen allowlisting settings to all assigned devices in your selected group(s), supporting both **Windows** and **macOS** endpoints centrally.

## Step 3: Test and Verify

Before launching your campaign to all of your employees:

* Run a **pilot test** with a small internal group.
* Ensure:
  * Emails are delivered successfully.
  * Clicking links leads to landing pages with **no SmartScreen interruption**.
* Recheck policy configurations if warnings persist.

For more information, see [Microsoft Defender SmartScreen overview](https://learn.microsoft.com/en-us/windows/security/operating-system-security/virus-and-threat-protection/microsoft-defender-smartscreen/)

By correctly applying these allowlisting methods, you can ensure Keepnet simulations are **not blocked or flagged**, enabling accurate measurement of user behavior and uninterrupted campaign execution across your entire organization.
