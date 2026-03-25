# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/6.-setup-phishing-reporter/integrate-native-microsoft-phishing-report-button-with-keepnet.md

# Integrate Native Microsoft Phishing Report Button with Keepnet

This integration allows your employees to continue using **Microsoft’s** **Phishing** **Reporting** button to report suspicious emails to your **SOC** **team** or **Microsoft** **Defender**. Along with that, this integration adds new benefits by forwarding reported emails to **Keepnet’s** **Incident** **Responder**. This ensures deeper analysis and tracking capabilities while maintaining your existing reporting process.

**Key Benefits:**

* **Dual Reporting:** Emails reported via the Microsoft Phishing Reporting Button are sent to both Microsoft Defender and Keepnet's Incident Responder product for advanced analysis.
* **Simulation Tracking:** During phishing simulation campaigns, Keepnet tracks employees who report simulated phishing emails, helping administrators measure awareness and provide training.

## Steps to Set Up the Integration

### **Step 1: Create a Shared Mailbox for Reports**

If you don’t already have a shared inbox for phishing reports:

1. Log into the [**Microsoft Exchange Admin Center**](https://admin.exchange.microsoft.com).
2. Navigate to **Recipients > Mailboxes > Add a Shared Mailbox**.
3. Enter a **Display** **Name** and **Email** **Address** for the shared mailbox.
4. Click the **Create** button to create a shared mailbox.

### **Step 2: Set Up a Mail Flow Rule**

Forward reported phishing emails to Keepnet using a mail flow rule:

1. Please [**contact the support team**](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk) of Keepnet to get the **Keepnet email address for forwarding**.
2. Log into the [**Microsoft 365 Admin Center**](https://admin.exchange.microsoft.com) and open the Exchange Admin Center.
3. Go to **Mail Flow > Rules** and click **Create New Rule**.
4. Configure the rule:
   * **Name:** Enter a name such as **"Forward Reported Emails to Keepnet"**.
   * **Set Apply this rule** **if:** Select the **"The recipient"** and then select the **"is this person"** option. Please enter the shared mailbox email address that you created in the previous section.
   * **Do the following:** Select the **"Add Recipients"** and then select the **"to the To box"** option. Please enter the email address that you got from the Keepnet Support Team.
5. Leave the **"Except if"** option as default and then click **Next**.
6. Leave the **"Set rule settings"** page settings as default and then click **Next**.
7. Click **Finish** to create the rule.

### **Step 3: Configure the Microsoft Phishing Reporting Add-In**

1. Open [**User Submission Settings**](https://security.microsoft.com/securitysettings/userSubmission) in your Microsoft 365 portal.
2. Ensure **“Monitor reported messages in Outlook”** is active.
3. Choose **“Use the built-in Report button in Outlook”**.
4. Set **“Reported message destinations”** to **“Microsoft and my reporting mailbox”** or **“My reporting mailbox only”.**
5. **Add** **your** **shared** **mailbox** that you created at the beginning of the document to the **"Add an exchange online mailbox to send reported messages to:"** field and save.

### **Step 4:** Install the Microsoft Outlook 365 'Report Phishing' Add-In

If not already installed:

1. Visit **Microsoft AppSource** and search for **“Report Phishing”**.
2. Click **Get it now** and follow the installation instructions.
3. Wait up to 12 hours for the add-in to appear in Outlook.

### **Step 5: Test the Integration**

1. Launch a phishing simulation campaign through Keepnet.
2. Report a simulation email using the **Microsoft** **Phishing** **Reporting** button. Then, go to your campaign report and click the **Reporters** menu to verify that you reported the simulation email.
3. Verify the email is also visible on Keepnet’s **Incident** **Responder** page.

## Possible Considerations

* **Reporting Delays:** When Microsoft forwards reported emails to the specified email destination, there may be a delay caused by Microsoft’s internal processing. For example, some emails may appear immediately whilst other emails may take 10 minutes to get reported to Keepnet from Microsoft.
* **Blocked Emails:** Emails flagged as phishing might be quarantined by Microsoft or other security solutions, causing delays in forwarding.
* **Interference:** External security solutions, such as Data Loss Prevention (DLP) systems, may interfere with email forwarding from Microsoft to Keepnet. This can result in delays or prevent emails from being reported altogether.
* **Email Quarantine:** Emails flagged as phishing might be quarantined by Microsoft or other security solutions, causing delays in forwarding.
* **Policy Conflicts:** Custom email policies on the customer’s Microsoft tenant could block or redirect reported emails, affecting Keepnet’s tracking.
* **Server Downtime:** Temporary unavailability of Microsoft or Keepnet’s email servers can result in reporting delays.

## How to Send Only Simulation Emails to Keepnet

If your organisation doesn't prefer to send all reported emails via the Microsoft button to Keepnet for analysis and reporting, you can only send simulation emails to Keepnet.

To do this, please follow the steps below.

1. Please first complete the [Step 1](#step-1-create-a-shared-mailbox-for-reports) , [Step 2](#step-2-set-up-a-mail-flow-rule) and [Step 3](#step-3-configure-the-microsoft-phishing-reporting-add-in) sections.
2. Log in to the [Microsoft 365 Admin Centre](https://admin.exchange.microsoft.com/) and open the Exchange Admin Centre.
3. Go to **Mail Flow > Rules** and **edit the rule** that you recently created.
4. Click the **+** button next to **'Apply this rule if'** condition to create an **AND** condition.
5. Select **'The subject or body'** and then select **'subject or body matches these text patterns'** option.
6. Add this **'x-keepnet-tid: \[0-9a-zA-Z]+'** to the text field.
7. Click the **Save** button to apply the changes.

Here is a screenshot reference of the above rule:

<figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FcCA9H8dxOBytf0gJpsrk%2FScreenshot%202025-10-23%20at%2011.26.51.png?alt=media&#x26;token=c22814cf-0aa2-496f-8da7-9408be320fb7" alt="Mail flow rule — subject/body pattern for forwarding only simulation emails to Keepnet." width="375"><figcaption><p>Mail flow rule — subject/body pattern for forwarding only simulation emails to Keepnet.</p></figcaption></figure>

Now, when an employee reports an email by using the Microsoft Phishing Reporter button, only simulation emails will be sent to Keepnet; any other emails will not be sent to Keepnet.
