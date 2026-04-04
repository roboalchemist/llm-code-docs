# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/incident-responder-dashboard.md

# Incident Responder Dashboard

This section will help you comprehend and utilize the Incident Responder product's fundamental features. To access all details described in this section, please click on **Incident Responder > Incident Responder**.

## **Widgets**

### **Phishing Reporter**

This provides details on how many users have the suspicious email reporter plugin (Outlook Desktop version) installed in total and how many users have been active in the past four minutes.

By clicking on the shortcut on the upper right corner of the box, you can access the page where the suspicious email notification add-in is installed and the user details are shown in more detail.

### **Incident Analysis**

The Incident Analysis box displays the total number of emails reported to the Incident Responder and highlights how many of them were found to be harmful.

### **Investigations**

Within the Investigations box, you can see the number of automatic investigations launched on the Incident Responder and the number of manual investigations.

By clicking on the shortcut on the upper right corner of the box, you can access the page where the investigations have been started.

### **ROI Summary**

This widget summarizes the performance and evaluates the efficiency and profitability of Incident Responder investment.

In order for this feature to produce accurate results, you need to arrange the time and money details specific to your institution. You can specify these details by clicking the '**Settings**' button in the **ROI Summary** menu in the upper right corner.

<table data-header-hidden><thead><tr><th width="150"></th><th width="582.1428571428571"></th></tr></thead><tbody><tr><td>Average hours saved per reported email(hours)</td><td>You can enter how much time a SOC team member spends time on each reported suspicious email to analyze, investigate, delete or other such actions.</td></tr><tr><td>Average total cost per hour($)</td><td>You can enter how much money it cost the company when a SOC team member spends time (hours) on each reported suspicious email to analyze, investigate, delete or other such actions.</td></tr></tbody></table>

An example from real life scenario. There is a **SOC team** who has **five members** and only **one person** is dedicated to taking these **"analyze, share results with the reporter, investigate, delete phishing email"** actions of **each** **email** reported by employees.

The person spends approximately **one** **hour** on each email, and depending on the salary, the person's one hour is equal to **200$** to the company\*\*,\*\* then set the **"average hours = 1 hour"** and set the **"average total cost = 200$"** in the widget settings.

The product will calculate based on this information how much money and time is saved by using the Incident Responder based on the each reported email to the product.

### **Top Rules**

The **Top Rules** section displays the five rules with the highest number of matches, based on the rules created in the Playbook.

### **Recent Investigations**

The **Recent Investigations** section provides details of the last five investigations initiated. It includes the investigation name, progress, and current status (Running, Canceled, Finished, or Expired).

### **Recent Incidents**

The **Recent Incidents** widget shows the five most recently reported email incidents along with their analysis status.

### **Reported Email Trends**

The **Reported Email Trends** widget presents a monthly breakdown of Undetected, Malicious, and Phishing emails. It highlights the months with the highest number of reported Malicious, Phishing, and Undetected emails.

## **Reported Emails**

This table contains all emails and analysis statuses reported to the Incident Responder product. This table includes information such as who reported suspicious emails, the status of the email analysis, and other details.

### **Actions**

You can take manual action on suspicious emails reported to the Incident Responder. You can click the buttons under the action and take the appropriate steps you want to perform.

#### **Edit**

The incident that was reported to the Incident Responder can be edited. You can add a tag or make notes on the case, as well as amend the analysis result or status of the related case. The table below contains comprehensive information on each field.

<table data-header-hidden><thead><tr><th width="150"></th><th width="583.1428571428571"></th></tr></thead><tbody><tr><td>Subject</td><td>Name of the subject</td></tr><tr><td>Reporter By</td><td>The email address of the user reported the incident.</td></tr><tr><td>Case ID</td><td>It is the case number that is created specific to the case.</td></tr><tr><td>Analysis Source</td><td>Analysis source detail that is automatic or linked to a Playbook rule.</td></tr><tr><td>Result</td><td>Analysis result of the case.</td></tr><tr><td>Status</td><td>Analysis status of the case. The status can be open, closed, in analysis, false positive, or in progress.</td></tr><tr><td>Tags</td><td>This is the area where you can add reminder tag information.</td></tr><tr><td>Notes</td><td>This is the area where the analyst can write their notes for this case.</td></tr><tr><td>Notify Reporting User About This Update</td><td>A feature where the notification message can be sent to the person who reported the incident using default templates by default or custom templates by clicking the <strong>change</strong> button and choosing the custom template.</td></tr><tr><td>Add Custom Message</td><td>Area where you can add a custom message in the email notification to be sent to the person reported the incident.</td></tr><tr><td>Date Created</td><td>The report date of the incident.</td></tr><tr><td>Last Update</td><td>The date of the last update on the incident.</td></tr></tbody></table>

You have the option to see the incident, look over its specifics, begin researching it, and take actions like rescanning the incident for integrations. By selecting the **three dots** “**︙**” button next to the Action title, you can execute actions on the related titles below.

#### **Preview Email**

By clicking the Preview button, you can visit the page with the image of the reported incident.

#### **Details**

By clicking the **Details** button, you can visit the page with the details of the reported incident.

The information on the reporting page is detailed in the table below.

<table data-header-hidden><thead><tr><th width="150"></th><th width="581.7800776196638"></th></tr></thead><tbody><tr><td>Details</td><td><p>This is the area where the details of the email are shown. See the following information:</p><ul><li>Analysis date of the reported email</li><li>From</li><li>From Name</li><li>To</li><li>CC</li><li>BCC</li><li>The date and time the user received the email</li><li>Sender IP of the email</li><li>The name of the folder where the email is located</li><li>The number of attachments</li><li>The number of URLs</li><li>The location of the sender IP address.</li></ul><p><br>At the same time, the email server IP address to which the email is sent, blacklist control is performed in analysis services. You can see the results on this screen under the <strong>Sender</strong> <strong>IP</strong> <strong>Blacklist</strong> <strong>Check</strong> title.</p></td></tr><tr><td>Header</td><td>The header information of the email is displayed in this field.</td></tr><tr><td>Email Preview</td><td>The preview of the email is shown in this area.</td></tr><tr><td>URLs</td><td>URLs and their analysis results in the email are displayed in this field. If the main domain redirects, each subsequent domain in the redirection chain is extracted and scanned until the final destination.</td></tr><tr><td>Attachments</td><td>The name of the attachment files and their hash information as well as analysis results are displayed in this field.</td></tr></tbody></table>

#### **Investigate**

By clicking the Investigation button, you can initiate an investigation to match the criteria of the report.

#### **Re-Analyze**

By clicking the Re-analyze button, you can re-analyze the incident using analysis services on integrations.

### **Cluster View**

You can utilize **Cluster View** to view notifications more clearly when there are too many of them on the Incident Responder screen. By selecting the “⇩” button located in the top right corner of the **Reported Emails** table, you can take the following actions.

#### **Cluster by Subject**

Cases are classified according to their titles and displayed accordingly.

#### **Cluster by Reported by**

Incidents are classified by reporters and displayed accordingly.

### Filter by MD5 or SHA512 Hash

Search the reported emails based on the MD5 or SHA512 hash of files. If the MD5 or SHA512 hash matches with a file attached on the reported email, the reported email will be listed on the reported emails table.

## **Use Cases**

### **SOAR Integration**

In case the end user reports an email, the relevant email is analyzed by the services with which the Incident Responder product is integrated. If the analysis result appears to be malicious, the institution's SOC team will apply additional measures such as using antivirus, firewall, EDR, proxy etc. to target this malicious email. This manual process will take a lot of time and will delay the intervention to the incident in a timely manner.

If the email reported to the platform is determined to be phishing or malicious after analysis, your current SOAR solution can obtain this detail from the platform via API and automatically perform the necessary actions on your solutions such as EDR, Proxy, and Firewall. In this way, the process will be manageable due to the quick action taken. API usage details are explained in detail in this document.

## Tutorial Video

{% embed url="<https://youtu.be/jQH01f_bEnM>" %}

## **FAQ**

### **Q: Can I delete incident records from the platform?**

A: You can update the status of the incidents as “closed”, but the incident cannot be deleted from the interface.

### **Q: Are the actions I take in the cluster view applied to all cases in the cluster?**

A: Yes, the actions you take in the cluster view are effective in all the cases.

### Q: What will happen if the email I reported is detected to be malicious?

A: If the analysis determines the data as malicious or phishing, an automatic investigation is launched, and any suspicious emails detected in other mailboxes are scanned. Additionally, you can also take steps like Investigate and Re-Analyze.

### **Q: Is the reported email sent to another service?**

A: No, the email reported by your users is never sent to any other service.

### Q: Does automatic analysis start when the analysis result of the reported email is Phishing, Malicious or Undetected?

A: Automatic analysis starts only when the analysis result is determined to be Phishing and Malicious, and the relevant malicious email is automatically searched throughout the company.

### **Q: How Sandbox analyzes my suspicious emails?**

A: We analyze suspicious email by header, body and attachments using our third-party analysis engines integrated into our platform. The reported email itself is not forwarded to the integrations. Our platform parses the URL, Attachment and Sender IP and makes the analysis.

### Q: Can I integrate the reported emails with my SOAR products by obtaining the details using the API?

A: You can perform almost every operation in the Incident Responder product using API. You can refer to our Rest API [document](https://api.keepnetlabs.com/docs/index.html) to see the details.

### **Q: Are the emails sent by users for analysis securely stored on the server?**

A: The platform generates a random key that is unique for each customer, then encrypts all reported emails on disk with AES 256 algorithm.

### **Q: How does the Incident Responder handle redirected URLs?**

A: Incident Responder product extracts and scans every domain in the redirection chain, starting from the main domain and continuing through each redirection step until the final destination is reached.

### Q: How does the Incident Responder handle the QR code emails?

A: Incident Responder product extracts and scans the QR codes by default. It can scan the QR code that is added to the body of the email or attached.

### **Q: Why doesn't Keepnet automatically start an investigation when an email is marked as malicious?**

A: If the *Incident Responder* initially marks an email as *Undetected* and you later change it to *Malicious* or *Phishing*, Keepnet does not start an automatic investigation.

This is because emails often contain multiple elements (attachments, URLs, sender IPs), and the system cannot determine which one is actually malicious. Investigating all elements could lead to false positives and unnecessary alerts.

To ensure accuracy, we suggest starting a manual investigation to focus on the specific malicious attachment or phishing link.

### **Q: Does Incident Responder support analyzing emails reported with IPv6 Sender IP addresses?**

A: Yes. Incident Responder fully supports detecting and analyzing IPv6 addresses included as Sender IPs in reported emails, enabling comprehensive investigations of emails originating from IPv6 IP addresses.
