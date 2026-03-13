# Source: https://docs.safetycli.com/safety-docs/output/detecting-vulnerabilities-and-sharing-results-via-email.md

# Detecting Vulnerabilities and Sharing Results via Email

This process involves configuring a policy file to define the behavior of the scan and crafting a command to execute the scan and send the email based on the scan results.

Configuring the Policy FileTo begin, generate a policy file that will dictate how the Safety CLI scanner operates. This policy file allows for customization of the scanning process, including setting parameters that prevent the scan from failing with an exit code when vulnerabilities are detected.&#x20;

Follow these steps:

1. **Generate a new policy file by running:**

```
safety generate policy_file
```

2. Open the generated `.safety_policy.yml` file and modify it as follows to prevent the scanner from exiting with a failure code due to detected vulnerabilities:

```
version: '3.0'

scanning-settings:
  max-depth: 8
  exclude: []
  include-files: []
  system:
    targets: []

report:
  dependency-vulnerabilities:
    enabled: true
    auto-ignore-in-report:
      python:
        environment-results: true
        unpinned-requirements: true
      cvss-severity: []

fail-scan-with-exit-code:
  dependency-vulnerabilities:
    enabled: false

security-updates:
  dependency-vulnerabilities:
    auto-security-updates-limit:
      - patch

```

​Place this `.safety_policy.yml` at the root of your project directory. For more detailed information on Safety CLI's policy file and its configurations, refer to the official documentation.

#### Running the Scan and Emailing Results <a href="#running-the-scan-and-emailing-results" id="running-the-scan-and-emailing-results"></a>

{% tabs %}
{% tab title="macOS and Unix" %}
This command performs a vulnerability scan using the Safety CLI tool, checks for any detected vulnerabilities, and sends an email notification if any vulnerabilities are found. It is designed to be executed in Unix and macOS environments.

1. **Scan Execution:** The Safety CLI tool is executed with a specified API key and stage. The results are saved in both JSON and human-readable text formats.
2. **Vulnerability Detection:** The `jq` tool is used to parse the JSON output to check for any known vulnerabilities.
3. **Email Notification:** If vulnerabilities are detected, an email is sent with the contents of the text report.

#### Command

Execute the command below in your terminal:

```
safety --key "API_KEY" –stage cicd scan --save-as json report.json > text_report && jq 'any(.scan_results.projects[].files[].results.dependencies[].specifications[].vulnerabilities.known_vulnerabilities[]; .id != null)' report.json | xargs -I {} test {} = "true" && cat text_report | mail -s "Vulnerabilities found" email@domain.com || true
```

* The `--save-as json report.json > text_report` part saves Safety CLI results in a JSON format to `report.json`, while redirecting the standard output to be saved as human-readable `text_report`.
* The `jq` command checks for the presence of any vulnerabilities by examining the `id` fields within the scan results. If any vulnerabilities are found (`true`), the subsequent command is triggered.
* `xargs -I {} test {} = "true"` uses the result from `jq` to conditionally proceed with sending an email if vulnerabilities are detected.
* The `mail` command constructs an email with the subject "Vulnerabilities found" and the content of `text_report`, sending it to the specified email address.
* The `|| true` ensures that, regardless of the exit codes in the pipe, the command sequence exits with a status code of `0` to prevent interrupting any automated pipelines due to a failure status.
  {% endtab %}

{% tab title="Windows" %}
This command performs a vulnerability scan using the Safety CLI tool, checks for any detected vulnerabilities, and sends an email notification if any vulnerabilities are found. It is designed to be executed in a Windows PowerShell environment.

1. **Scan Execution:** The Safety CLI tool is executed with a specified API key and stage. The results are saved in both JSON and human-readable text formats.
2. **Vulnerability Detection:** The vulnerability detection process involves the script first checking if the report.json file exists. Upon confirming its presence, the script then parses the JSON output to identify any known vulnerabilities.
3. **Email Notification:** If vulnerabilities are detected, an email is sent with the contents of the text report. The email configuration is specified using SMTP server details.

To send an email notification about detected vulnerabilities, you need to configure an SMTP (Simple Mail Transfer Protocol) server. An SMTP server is a critical component for email communication, acting as the mail delivery agent that sends outgoing emails from your system to the recipient’s email server. Configuring the SMTP server involves specifying the server address (e.g., smtp.sendgrid.net), the port number (typically 587 for TLS or 465 for SSL), and authentication credentials, which include the SMTP username and password, usually corresponding to an API key and its value. These credentials ensure secure and authenticated communication between your system and the SMTP server.

#### Command Variables

Before executing the command, you need to set the following variables:

* **API\_KEY**: The API key for the Safety CLI scan.
* **SMTP\_SERVER**: The SMTP server address (e.g., smtp.sendgrid.net).
* **SMTP\_PORT**: The SMTP server port (e.g., 587).
* **SMTP\_USER**: The SMTP username, typically an API key identifier.
* **SMTP\_PASSWORD**: The SMTP password, typically the API key value.
* **RECIPIENT\_EMAIL**: The email address to which the report will be sent.
* **SENDER\_EMAIL**: The email address from which the report will be sent.

#### Command

```powershell
safety scan --key <API_KEY> --stage cicd --save-as json report.json > text_report.txt
if (Test-Path -Path "report.json") {
    $jsonReport = Get-Content report.json | ConvertFrom-Json
    $vulnerabilitiesFound = $false
    foreach ($project in $jsonReport.scan_results.projects) {
        foreach ($file in $project.files) {
            foreach ($dependency in $file.results.dependencies) {
                foreach ($specification in $dependency.specifications) {
                    if ($specification.vulnerabilities.known_vulnerabilities.Count -gt 0) {
                        $vulnerabilitiesFound = $true
                        break
                    }
                }
                if ($vulnerabilitiesFound) { break }
            }
            if ($vulnerabilitiesFound) { break }
        }
        if ($vulnerabilitiesFound) { break }
    }
    if ($vulnerabilitiesFound) {
        $smtpServer = "<SMTP_SERVER>"
        $smtpPort = <SMTP_PORT>
        $smtpUser = "<SMTP_USER>"
        $smtpPassword = "<SMTP_PASSWORD>"
        $emailTo = "<RECIPIENT_EMAIL>"
        $emailFrom = "<SENDER_EMAIL>"
        $subject = "Vulnerabilities found"
        $body = Get-Content text_report.txt -Raw
        $smtpClient = New-Object Net.Mail.SmtpClient($smtpServer, $smtpPort)
        $smtpClient.EnableSsl = $true
        $smtpClient.Credentials = New-Object System.Net.NetworkCredential($smtpUser, $smtpPassword)
        $mailMessage = New-Object System.Net.Mail.MailMessage
        $mailMessage.From = $emailFrom
        $mailMessage.To.Add($emailTo)
        $mailMessage.Subject = $subject
        $mailMessage.Body = $body
        $mailMessage.IsBodyHtml = $true
        try {
            $smtpClient.Send($mailMessage)
            Write-Output "Email sent successfully"
        } catch {
            Write-Output "Failed to send email: $_"
            Write-Output "SMTP Server: $smtpServer"
            Write-Output "SMTP Port: $smtpPort"
            Write-Output "SMTP User: $smtpUser"
            Write-Output "SMTP Password: $smtpPassword"
        }
    } else {
        Write-Output "No vulnerabilities found"
    }
} else {
    Write-Output "report.json was not created, scan might have failed"
}
```

{% endtab %}
{% endtabs %}

#### Alternative Approaches <a href="#alternative-approaches" id="alternative-approaches"></a>

While the above command provides a quick and integrated solution for scanning and alerting, it's possible to incorporate this logic into a script for more complex workflows or to enhance readability and maintainability. This guide aims to facilitate a seamless integration of vulnerability scanning and notification within your CI/CD pipeline, ensuring that your team is promptly informed of any security issues detected in your project dependencies.
