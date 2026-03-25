# Source: https://doc.keepnetlabs.com/next-generation-product/platform/email-threat-simulator/view-scan-report.md

# View Scan Report

This section describes the capabilities and features of the threat simulation reports that can be generated using the **Email Threat Simulator > Scan > Report** button.

The components of the **Scan Reports** page are explained below.

## Summary

The **Summary** provides a brief synopsis of the threat scan and options for further action.

### Summary Widgets

<table data-header-hidden><thead><tr><th width="146"></th><th></th></tr></thead><tbody><tr><td>Total Attacks Sent</td><td>The number of emails sent to the target email address.</td></tr><tr><td>Secure Endpoints</td><td>The number of emails successfully blocked by email security solutions.</td></tr><tr><td>Insecure Endpoints</td><td>The number of emails that could not be blocked by email security solutions</td></tr><tr><td>Unchecked Emails</td><td>The number of emails not checked by the platform because the automated scan was not enabled or authentication of a target email account failed</td></tr></tbody></table>

### Scan Info

<table data-header-hidden><thead><tr><th width="117"></th><th></th></tr></thead><tbody><tr><td>Start Date</td><td>The date and time the scan of a target email address was initiated</td></tr><tr><td>Status</td><td>The status of the scan: completed, continuous or in progress</td></tr><tr><td>Email</td><td>The attack vector target email address</td></tr></tbody></table>

### Threat Scan Score

The score is calculated based on the number of emails determined to be insecure and the severity value of the risk posed by these emails.

### Stats

The attack vectors are listed by attack type or by email status: **Malicious** **Attachments**, **Ransomware** **Samples** or **Insecure** **Emails**.

## Attacks Sent

This section provides a summary report of the attack vectors exploited to target an email address.

<table data-header-hidden><thead><tr><th width="126"></th><th></th></tr></thead><tbody><tr><td>Attack Vector</td><td>The name of the attack vector</td></tr><tr><td>Extention</td><td>The extention of the file.</td></tr><tr><td>Category</td><td>The type of the attack vector</td></tr><tr><td>Hash</td><td>The hash of the file.</td></tr><tr><td>SHA256</td><td>The SHA256 of the file.</td></tr><tr><td>Severity</td><td>The risk level of each attack, shown as a severity rating from 1 (lowest risk) to 10 (highest risk).</td></tr><tr><td>Status</td><td><p>Send status of the attack vector: in progress, successful, or error</p><ul><li><strong>In</strong> <strong>Progress:</strong> The attack vector email is in the queue to be sent.</li><li><strong>Successful:</strong> The attack vector email was sent successfully.</li><li><strong>Error:</strong> An error occurred in the delivery of the attack vector.</li></ul></td></tr><tr><td>Result</td><td><p>The results of the attack: Secure, Insecure or Unchecked.</p><ul><li><strong>Secure:</strong> The attack vector was sent successfully but not delivered.</li><li><strong>Insecure:</strong> The attack vector was sent successfully and delivered to the inbox.</li><li><strong>Unchecked:</strong> The attack vector might be sent successfully but delivery is not checked.</li></ul></td></tr><tr><td>Email Sent Date</td><td>Date and time that attack vector email was sent to the target email address.</td></tr></tbody></table>

## **FAQ**

### Q: Can I download a list of the attack vectors sent?

**A:** Yes, you can download a detailed report of the launched attack vectors in .xls, .pdf, or .csv format using the **Download** button.

### Q: Can I export reports into my own reporting tool (e.g., Qlik Sense, Tableau, PowerBI)?

A: Yes. You can transfer all of our reports through an API. This flexibility allows you to use the information as needed to suit your business.
