# Source: https://docs.jit.io/docs/splunk.md

# Splunk Integration

Jit's integration with **Splunk Cloud** makes it easy to stream your audit logs to Splunk for storage and analysis using Splunk's event collector.

You can learn more about Jit's audit logs [here](https://docs.jit.io/docs/audit-logs#ingesting-audits-to-your-systems).

## Quickstart

1. In Jit's web app, go to the **Integrations page**.

2. Find the "**Splunk Cloud**" card and click "**Connect**".

3. You should now see a Splunk integration window. Click on "Connect" at the top right corner.

   ![](https://files.readme.io/8213ac62f754b8a3dba58e7bf9a7814008613bc3c4bee8d8c4a3d861931c0ce3-image.png)

   * You will now need to provide your deployment name (from your splunk URL) and the HTTP Event Collector (HEC) token that will be used to send events.

     ![](https://files.readme.io/78cc05f338ef8a00482938c7f9b9468e3e82a4e61de0a901491e470b020a49de-image.png)
   * Log into your Splunk Cloud account.
   * Navigate to **Settings > Data Inputs**

   ![](https://files.readme.io/42e9da19f10702ddc618619f566ccfb23547979e813fdff258e9b1beeeed4a4f-image.png)

   * Under **Local Inputs**,  **HTTP Event Collector** click **Add new**

   ![](https://files.readme.io/3294bd07bb457ed4740a5b11cc89464b7c71914631a690cf994ad09efaaa7aa2-image.png)

   * Follow these steps:

     * Name your token (e.g., "Jit Integration").

     * Make sure `Enable indexer acknowledgement` is **Unchecked**

[block:image]{"images":[{"image":["https://files.readme.io/046b0beeeb9ab3a391f9f88907deb79669eedb43c39c37a4172e67252b13bf16-image.png",null,""],"align":"center","border":true}]}[/block]

* Click **Next**

* Choose the indexes that will ingest Jit's audit logs (under `Selected items(s)`)

[block:image]{"images":[{"image":["https://files.readme.io/503bb171468ad2b21f0e5d4cb105c7158643194488a3098323db5b78f3b56285-image.png",null,""],"align":"center","border":true}]}[/block]

* Click **Review** -> **Submit** and copy the generated token. **Please note** that if the token is deleted or modified, events from Jit will no longer be logged to Splunk Cloud.

[block:image]{"images":[{"image":["https://files.readme.io/984d913ef1db906cc72d61f53ea3734d3d4dde9cb0f5da7a9944867ee6da9911-image.png",null,""],"align":"center","border":true}]}[/block]

Learn more in [Splunk documentation](https://docs.splunk.com/Documentation/SplunkCloud/latest/Data/UsetheHTTPEventCollector).

4. Paste the token in the "**Event collector token**" textbox and click **Continue**.

   If the token is valid, your integration is now active, and you can begin ingesting audits to your instance.

5. Enable audits ingest, and select the desired index. The index must be included in your token configuration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/15792b06fb2af93338858824a36c0b9c61920c7f428c6161f90877b3d488cb89-Screenshot_2025-02-25_at_12.21.22.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "650px"
    }
  ]
}
[/block]

## Sample event

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

<br />

<br />

# Ingesting findings and other data through Jit Workflows

1. First, enable the `Ingest workflows results` in order to activate it. You may choose different index from the audits one.

[block:image]{"images":[{"image":["https://files.readme.io/6b188a08a8c4b63c49991fe4d1c8a38e83d583c85a1d69da6f32066c5d322aec-Screenshot_2025-02-25_at_12.28.56.png","",""],"align":"center"}]}[/block]

2. You can now use splunk as a target in your workflows

[block:image]{"images":[{"image":["https://files.readme.io/bbec8bbdfe536f68e5560c52e1d0d78e3db3b21716e3b90a1d4de52eb51bda1d-Screenshot_2025-02-25_at_12.33.32.png","",""],"align":"center"}]}[/block]

## Sample event

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

## Notes

* Ensure that the Splunk HEC endpoint is accessible from Jit.

* If the token is invalid or the endpoint is inaccessible, You will have to re-integrate.