# Source: https://console.groq.com/docs/security/gcp-private-service-connect

---
description: Connect to Groq using Google Cloud Private Service Connect for secure, private network connectivity
title: GCP Private Service Connect - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [Google Cloud Private Service Connect](#google-cloud-private-service-connect)

Private Service Connect (PSC) enables you to access Groq's API services through private network connections, eliminating exposure to the public internet. This guide explains how to set up Private Service Connect for secure access to Groq services.

### [Overview](#overview)

Groq exposes its API endpoints in Google Cloud Platform as PSC _published services_. By configuring PSC endpoints, you can:

* Access Groq services through private IP addresses within your VPC
* Eliminate public internet exposure
* Maintain strict network security controls
* Minimize latency
* Reduce data transfer costs

curl

```
Your VPC Network                 Google Cloud PSC                 Groq Network
+------------------+           +------------------+           +------------------+
|                  |           |                  |           |                  |
|  +-----------+   |           |                  |           |   +-----------+  |
|  |           |   |  Private  |     Service      |  Internal |   |   Groq    |  |
|  |   Your    |   | 10.0.0.x  |                  |           |   |   API     |  |
|  |   App     +---+--> IP <---+---> Connect <----+--> LB <---+---+ Service   |  |
|  |           |   |           |                  |           |   |           |  |
|  +-----------+   |           |                  |           |   +-----------+  |
|                  |           |                  |           |                  |
|  DNS Resolution  |           |                  |           |                  |
|  api.groq.com    |           |                  |           |                  |
|  -> 10.0.0.x     |           |                  |           |                  |
|                  |           |                  |           |                  |
+------------------+           +------------------+           +------------------+
```

### [Prerequisites](#prerequisites)

* A Google Cloud project with [Private Service Connect enabled](https://cloud.google.com/vpc/docs/configure-private-service-connect-consumer)
* VPC network where you want to create the PSC endpoint
* Appropriate IAM permissions to create PSC endpoints and DNS zones
* Enterprise plan with Groq
* Provided Groq with your GCP Project ID
* Groq has accepted your GCP Project ID to our Private Service Connect

### [Setup](#setup)

The steps below use us as an example. Make sure you configure your system according to the region(s) you want to use.

#### [1\. Connect an endpoint](#1-connect-an-endpoint)

1. Navigate to **Network services** \> **Private Service Connect** in your Google Cloud Console
2. Go to the **Endpoints** section and click **Connect endpoint**  
   * Under **Target**, select _Published service_  
   * For **Target service**, enter a [published service](#published-services) target name.  
   * For **Endpoint name**, enter a descriptive name (e.g., `groq-api-psc`)  
   * Select your desired **Network** and **Subnetwork**  
   * For **IP address**, create and select an internal IP from your subnet  
   * Enable **Global access** if you need to connect from multiple regions
3. Click **Add endpoint** and verify the status shows as _Accepted_

#### [2\. Configure Private DNS](#2-configure-private-dns)

1. Go to **Network services** \> **Cloud DNS** in your Google Cloud Console
2. Create the first zone for groq.com:  
   * Click **Create zone**  
   * Set **Zone type** to _Private_  
   * Enter a descriptive **Zone name** (e.g., `groq-api-private`)  
   * For **DNS name**, enter `groq.com.`  
   * Create an `A` record:  
         * **DNS name**: `api`  
         * **Resource record type**: `A`  
         * Enter your PSC endpoint IP address  
   * Link the private zone to your VPC network
3. Create the second zone for groqcloud.com:  
   * Click **Create zone**  
   * Set **Zone type** to _Private_  
   * Enter a descriptive **Zone name** (e.g., `groqcloud-api-private`)  
   * For **DNS name**, enter `groqcloud.com.`  
   * Create an `A` record:  
         * **DNS name**: `api.us`  
         * **Resource record type**: `A`  
         * Enter your PSC endpoint IP address  
   * Link the private zone to your VPC network

#### [3\. Validate the Connection](#3-validate-the-connection)

To verify your setup:

1. SSH into a VM in your VPC network
2. Test DNS resolution for both endpoints:  
curl  
```  
dig +short api.groq.com  
dig +short api.us.groqcloud.com  
```  
Both should return your PSC endpoint IP address
3. Test API connectivity (using either endpoint):  
curl  
```  
curl -i https://api.groq.com  
# or  
curl -i https://api.us.groqcloud.com  
```  
Should return a successful response through your private connection

### [Published Services](#published-services)

| Service | PSC Target Name                                                   | Private DNS Names                            |
| ------- | ----------------------------------------------------------------- | -------------------------------------------- |
| API     | projects/groq-pe/regions/me-central2/serviceAttachments/groqcloud | api.groq.com, api.me-central-1.groqcloud.com |
| API     | projects/groq-pe/regions/us-central1/serviceAttachments/groqcloud | api.groq.com, api.us.groqcloud.com           |

### [Troubleshooting](#troubleshooting)

If you encounter connectivity issues:

1. Verify DNS resolution is working correctly for both domains
2. Check that your security groups and firewall rules allow traffic to the PSC endpoint
3. Ensure your service account has the necessary permissions
4. Verify the PSC endpoint status is _Accepted_
5. Confirm the model you are requesting is operating in the target region

### [Alerting](#alerting)

To monitor and alert on an unexpected change in connectivity status for the PSC endpoint, use a [Google Cloud log-based alerting policy](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

Below is an example of an alert policy that will alert the given notification channel in the case of a connection being _Closed_. This will require manual intervention to reconnect the endpoint.

curl

```
resource "google_monitoring_alert_policy" "groq_psc" {
  display_name = "Groq - Private Service Connect"
  combiner     = "OR"

  conditions {
    display_name = "Connection Closed"
    condition_matched_log {
      filter = <<-EOF
        resource.type="gce_forwarding_rule"
        protoPayload.methodName="LogPscConnectionStatusUpdate"
        protoPayload.metadata.pscConnectionStatus="CLOSED"
      EOF
    }
  }

  notification_channels = [google_monitoring_notification_channel.my_alert_channel.id]
  severity              = "CRITICAL"

  alert_strategy {
    notification_prompts = ["OPENED"]

    notification_rate_limit {
      period = "600s"
    }
  }

  documentation {
    mime_type = "text/markdown"
    subject   = "Groq forwarding rule was unexpectedly closed"
    content   = <<-EOF
    Forwarding rule $${resource.label.forwarding_rule_id} was unexpectedly closed. Please contact Groq Support ([email protected]) for remediation steps.

    - **Project**: $${project}
    - **Alert Policy**: $${policy.display_name}
    - **Condition**: $${condition.display_name}
    EOF

    links {
      display_name = "Dashboard"
      url          = "https://console.cloud.google.com/net-services/psc/list/consumers?project=${var.project_id}"
    }
  }
}
```

### [Further Reading](#further-reading)

* [Google Cloud Private Service Connect Documentation](https://cloud.google.com/vpc/docs/private-service-connect)