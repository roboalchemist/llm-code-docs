# Source: https://docs.jit.io/docs/google-secops-integration.md

# Google SecOps (Chronicle) Integration

Jit’s integration with **Google SecOps** allows organizations to seamlessly stream audit logs and security findings for enhanced visibility, analysis, and risk management.

You can learn more about Jit's audit logs [here](https://docs.jit.io/docs/audit-logs#ingesting-audits-to-your-systems).

<br />

> 📘 Ingestion API and Log Type
>
> Jit sends **JIT** as the log type and uses the [unstructured](https://cloud.google.com/chronicle/docs/reference/ingestion-api#unstructuredlogentries) ingestion API.

<br />

# Step-by-Step Integration Guide

1. In the Jit platform, go to **Settings > Integrations**, scroll to find the **Google SecOps (Chronicle)** card, and click **Connect**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aef979b71c8b09210935934af9d0eb40c31c7d7df24bc7780b09e7b5ec8fc1ec-google-secops-card.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "300px"
    }
  ]
}
[/block]

<br />

2. You should now see an integration window. Click on "**Sign in with Google**" at the top right corner.\
   Ensure that you have the necessary admin permissions to proceed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/150eeda804a70e42ebf4427016c95483fd633b5c8f9fbae61f05183221d1c768-google-secops-overview.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

3. You will now need to provide your connection details, Pay attention to the required fields.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4555d3e2be66c8d53a4f06ac38e14749dc2649a1b38a06c7df1da33be5107151-google-secops-settings.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]

<br />

**Client ID:**

This is your `customer_id`, a unique identifier for your *Google Security Operations* instance. You can find it in your *Google Security Operations settings* (`/settings/profile`).

**Client Secret**

This is your **Google Service Account Credentials** - Obtain it by following [this guide.](https://cloud.google.com/chronicle/docs/reference/ingestion-api#getting_api_authentication_credentials)

The credentials usually look like:

```json
{
  "type": "service_account",
  "project_id": "<PROJECT_ID>",
  "private_key_id": "<PRIVATE_KEY_ID>",
  "private_key": "-----BEGIN PRIVATE KEY-----XXXXXXXX\n-----END PRIVATE KEY-----\n",
  "client_email": "sa-name@project_id.iam.gserviceaccount.com",
  "client_id": "<CLIENT_ID>",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ABC.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

**API Region**

Provide the prefix of your [regional endpoint ](https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) based on your location. Example regions:

```
US: malachiteingestion-pa
London: europe-west2-malachiteingestion-pa
Germany: europe-west3-malachiteingestion-pa
```

## Configuration

Configure the ingestion parameters by supplying the following fields:

* **Label Key** + **Label Value** - This is the label applied to the logs.

To enable audit log ingestion, **toggle** the option on in the configuration screen.

### Sample event

```json json
{
   "severity":"Info",
   "action":"Export plan results",
   "description":"Export Plan Test Plan results",
   "userAgent":"Mozilla/5.0",
   "ip":"192.168.0.1",
   "email":"test@example.com",
   "plan_name":"Test Plan"
}
```

# Ingesting findings and other data through Jit Workflows

You can now use **Google SecOps** to ingest findings.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/09904ce7f488965cb4bcb9ab9413a5c1a86174f6b37d92302aa73db72b4a8066-Screenshot_2025-02-27_at_19.03.41.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

<br />

### Sample event

```json json
{
  "id": "11111111-2222-3333-4444-555555555555",
  "status": "PASS",
  "tenant_id": "aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "asset_id": "ffffffff-gggg-hhhh-iiii-jjjjjjjjjjjj",
  "asset_type": "repo",
  "asset_name": "SampleRepo",
  "asset_domain": "TestProject",
  "workflow_suite_id": "kkkkkkkk-llll-mmmm-nnnn-oooooooooooo",
  "workflow_id": "pppppppp-qqqq-rrrr-ssss-tttttttttttt",
  "first_workflow_suite_id": "kkkkkkkk-llll-mmmm-nnnn-oooooooooooo",
  "first_workflow_id": "pppppppp-qqqq-rrrr-ssss-tttttttttttt",
  "jit_event_id": "uuuuuuuu-vvvv-wwww-xxxx-yyyyyyyyyyyy",
  "jit_event_name": "merge_default_branch",
  "first_jit_event_name": "merge_default_branch",
  "execution_id": "zzzzzzzz-aaaa-bbbb-cccc-dddddddddddd",
  "fixed_at_jit_event_id": null,
  "fixed_at_execution_id": null,
  "job_name": "static-code-analysis-python-semgrep",
  "vendor": "github",
  "responsible": null,
  "control_name": "semgrep",
  "test_name": "Unsafe system call with risk of command injection",
  "fingerprint": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
  "test_id": "python.lang.security.audit.dangerous-system-call.dangerous-system-call",
  "issue_text": "Found dynamic content used in a system call. This is dangerous if external data can reach this function call because it allows a malicious actor to execute commands. Use the 'subprocess' module instead, which is easier to use without accidentally exposing a command injection vulnerability.",
  "issue_confidence": "UNDEFINED",
  "issue_severity": "HIGH",
  "plan_layer": "code",
  "vulnerability_type": "code_vulnerability",
  "cwes": [
    "CWE-78"
  ],
  "cves": null,
  "resolution": "IGNORED",
  "references": [
    {
      "name": "https://semgrep.dev/r/python.lang.security.audit.dangerous-system-call.dangerous-system-call",
      "url": "https://semgrep.dev/r/python.lang.security.audit.dangerous-system-call.dangerous-system-call"
    }
  ],
  "location": "https://github.com/TestProject/SampleRepo/blob/abcdef1234567890abcdef1234567890abcdef12/sample.py#L218-L218",
  "location_text": "TestProject/SampleRepo",
  "code_attributes": {
    "branch": "main",
    "pr_number": null,
    "filename": "sample.py",
    "line_range": "218-218",
    "code_snippet": "requires login",
    "head_sha": "abcdef1234567890abcdef1234567890abcdef12",
    "base_sha": "",
    "last_head_sha": "abcdef1234567890abcdef1234567890abcdef12",
    "user_vendor_id": "987654321",
    "user_vendor_username": "SampleUser"
  },
  "cloud_attributes": null,
  "app_attributes": null,
  "created_at": "2025-02-12T13:20:00.741995",
  "ended_at": null,
  "modified_at": "2025-02-12T15:49:15.165855",
  "last_detected_at": "2025-02-12T13:20:00.741995",
  "fix_suggestion": {
    "guidelines": "The auto-remediation feature will replace uses of os.system with subprocess.run in the vulnerable code, ensuring a safer way of executing system commands. The vulnerability will be fixed by changing the command execution method and adapting the command input format.",
    "title": "Avoid using os.system for executing system commands",
    "reason": "Using os.system to execute system commands can lead to command injection vulnerabilities if user-supplied data is not properly sanitized. It is recommended to use the subprocess module for executing system commands, as it provides a more secure interface and avoids potential security risks associated with command injection.",
    "source": "ai",
    "filename": "sample.py",
    "start_line": 218,
    "end_line": 218,
    "current_text": "    os.system(command)",
    "new_text": "    subprocess.run(command, shell=False, check=True, text=True)",
    "is_outside_of_pr_diff": false
  },
  "backlog": true,
  "ignore_rules_ids": [
    "bbbbbbbb-cccc-dddd-eeee-ffffffffffff"
  ],
  "ignored": true,
  "tags": [],
  "priority_factors": [],
  "priority_score": 0,
  "priority_context": null,
  "original_priority_factors": [],
  "original_priority_context": null,
  "manual_factors": {
    "added": [],
    "removed": []
  },
  "asset_priority_score": 0,
  "filename": "sample.py",
  "jobs": [
    {
      "workflow_slug": "workflow-sast",
      "job_name": "static-code-analysis-python-semgrep"
    }
  ],
  "scan_scope": {
    "language": "python",
    "branch": "main",
    "filepath": "sample.py"
  },
  "plan_items": [
    "item-code-vulnerability"
  ],
  "tickets": [],
  "fix_pr_url": null,
  "teams": []
}

```