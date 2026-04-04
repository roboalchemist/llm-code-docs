# Source: https://docs.datadoghq.com/security/guide/findings-schema.md

---
title: Security Findings Schema Reference
description: >-
  Complete reference for the Security Findings schema, including all attributes,
  namespaces, and data model for querying vulnerabilities, misconfigurations,
  and security risks.
breadcrumbs: Docs > Datadog Security > Security Guides > Security Findings Schema Reference
---

# Security Findings Schema Reference

## Overview{% #overview %}

Security findings in Datadog represent vulnerabilities, misconfigurations, and security risks identified across your infrastructure and applications. Each finding contains structured data organized into namespaces that describe the nature, impact, status, and context of the security issue.

All findings share a common schema that enables unified querying and analysis across different security products.

{% callout %}
Learn about migrating to this new schema so you can avoid any interruptions to your workflows.

[LEARN MORE](https://docs.datadoghq.com/security/guide/security-findings-migration/)
{% /callout %}

## Examples{% #examples %}

There are eleven different categories for security findings. Click on a category to view a sample security finding belonging to that category.

{% tab title="API Security" %}

```json
{
  "api_endpoint": {
    "method": "GET",
    "operation_name": "aspnet_core.request",
    "path": "/swagger/v1/swagger.json",
    "resource_name": "GET /swagger/v1/swagger.json"
  },
  "description": "This publicly exposed API endpoint does not implement the X-Frame-Options header. This header allows to control whether a browser should be allowed to render the response in a frame, iframe, embed, or object. Without this header, the API response could be vulnerable to clickjacking attacks. Remediation: Implement the X-Frame-Options header in all API responses with appropriate values. Example header values: Use DENY to prevent any domain from framing the content (X-Frame-Options: DENY), or use SAMEORIGIN to allow framing only by the same site (X-Frame-Options: SAMEORIGIN).",
  "detection_changed_at": 1766083119000,
  "finding_id": "YXBpLXNlYy1leGFtcGxlLWZpbmRpbmctaWQtMTIzNDU2Nzg5MA==",
  "finding_type": "api_security",
  "first_seen_at": 1766083119000,
  "is_in_security_inbox": false,
  "last_seen_at": 1766090321000,
  "metadata": {
    "schema_version": "2"
  },
  "resource_id": "ZXhhbXBsZS1zZXJ2aWNlfEdFVCAvc3dhZ2dlci92MS9zd2FnZ2VyLmpzb258YXNwbmV0X2NvcmUucmVxdWVzdA==",
  "resource_name": "ZXhhbXBsZS1zZXJ2aWNlfEdFVCAvc3dhZ2dlci92MS9zd2FnZ2VyLmpzb258YXNwbmV0X2NvcmUucmVxdWVzdA==",
  "resource_type": "endpoint",
  "rule": {
    "default_rule_id": "def-000-bh2",
    "id": "def-000-bh2",
    "name": "Missing X-Frame-Options HTTP header",
    "type": "api_security",
    "version": 3
  },
  "service": {
    "name": "example-service"
  },
  "severity": "low",
  "severity_details": {
    "adjusted": {
      "score": 2,
      "value": "low",
      "value_id": 1
    }
  },
  "status": "open",
  "tags": [
    "scored:true",
    "security:compliance",
    "method:get",
    "env:",
    "dd_rule_type:api_security",
    "scope:api-findings",
    "service:example-service",
    "owasp:api8_2023",
    "owasp_url:https://owasp.org/api-security/editions/2023/en/0xa8-security-misconfiguration/"
  ],
  "title": "Missing X-Frame-Options HTTP header",
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Attack Path" %}

```json
{
  "cloud_resource": {
    "configuration": {
      "context": {
        "associated_pods": [
          {
            "node_name": "ip-10-0-1-101.ec2.internal",
            "pod_name": "checkout-service-6648f57868-7sn4q",
            "pod_uuid": "a1b2c3d4-e5f6-4042-b0fe-111111111111",
            "service": "checkout-service"
          },
          {
            "node_name": "gke-prod-cluster-default-pool-abc12345-x1y2",
            "pod_name": "checkout-service-9977c988b-2wbt5",
            "pod_uuid": "a1b2c3d4-e5f6-4042-b0fe-222222222222",
            "service": "checkout-service"
          }
        ],
        "public_trace": {
          "hostname": "gke-prod-cluster-default-pool-abc12345-x1y2.c.example-project.internal",
          "image": "gcr.io/example-project/checkout-service",
          "last_seen_trace": "abc123def4560000001234567890abcd",
          "url": "http://checkout-service:8080/health"
        },
        "service": {
          "env": "dev",
          "name": "checkout-service"
        },
        "vulnerabilities": {
          "cve_ids": [
            "CVE-2024-50379",
            "CVE-2024-56337"
          ]
        }
      },
      "dd_computed_attributes": {
        "Vulnerabilities": [
          {
            "cve_ids": [
              "CVE-2024-50379"
            ],
            "cwe_ids": [
              "CWE-502",
              "CWE-367"
            ],
            "exploit_available": false,
            "exploit_sources": [
              "NIST",
              "GitHub"
            ],
            "title": "Apache Tomcat Time-of-check Time-of-use (TOCTOU) Race Condition vulnerability",
            "type": "COMPONENT_WITH_KNOWN_VULNERABILITY",
            "vulnerability_id": "abc123def456789012345678901234ab"
          }
        ],
        "is_publicly_accessible": true
      },
      "external_id": "",
      "seen_at": 1766088954
    },
    "display_name": "checkout-service"
  },
  "compliance": {
    "evaluation": "fail"
  },
  "description": "Unpatched vulnerabilities in publicly accessible applications can increase the likelihood of exposing weaknesses, creating an entry point for attackers to gain unauthorized access to the pod or container. Granting excessive capabilities to a pod or container can lead to unintended lateral movement to other containers or to the underlying node resources. Remediation: 1. Review any associated vulnerability references or advisories. 2. Apply the appropriate patch based on remediation guidance. If no patch is available, apply compensating controls such as disabling or removing the vulnerable component. 3. Review your Kubernetes pod or container security context configurations to ensure they provide proper isolation boundaries. Possible mitigations include using Kubernetes Pod Security Policies, SELinux, AppArmor, or Seccomp filters.",
  "detection_changed_at": 1765692948000,
  "finding_id": "ZXhhbXBsZS1hdHRhY2stcGF0aC1pZC0xMjM0NTY3ODkw",
  "finding_type": "attack_path",
  "first_seen_at": 1765692948000,
  "is_in_security_inbox": true,
  "last_seen_at": 1766088954000,
  "metadata": {
    "schema_version": "2"
  },
  "resource_id": "eyJuYW1lIjoiY2hlY2tvdXQtc2VydmljZSIsImVudiI6ImRldiJ9",
  "resource_name": "checkout-service",
  "resource_type": "service",
  "risk": {
    "is_publicly_accessible": true
  },
  "risk_details": {
    "is_publicly_accessible": {
      "value": true
    }
  },
  "rule": {
    "default_rule_id": "def-000-iqr",
    "id": "def-000-iqr",
    "name": "Publicly accessible application with a critical vulnerability in a container with elevated privileges",
    "type": "cloud configuration",
    "version": 1
  },
  "severity": "critical",
  "severity_details": {
    "adjusted": {
      "score": 9.5,
      "value": "critical",
      "value_id": 4
    }
  },
  "status": "open",
  "tags": [
    "scope:kubernetes",
    "security:compliance",
    "scored:false",
    "dd_rule_type:combination",
    "source:kubernetes",
    "team:backend"
  ],
  "title": "Publicly accessible application with a critical vulnerability in a container with elevated privileges",
  "workflow": {
    "automations": [
      {
        "rule_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "rule_name": "PCI",
        "rule_type": "due_date"
      },
      {
        "rule_id": "ffffffff-1111-2222-3333-444444444444",
        "rule_name": "Security Inbox Default Misconfiguration Ruleset",
        "rule_type": "security_inbox"
      }
    ],
    "due_date": {
      "due_at": 1766297748000,
      "is_overdue": false,
      "rule_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
    },
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Runtime Code Vulnerability" %}

```json
{
  "api_endpoint": {
    "method": "GET",
    "path": "/api/users"
  },
  "base_severity": "low",
  "code_location": {
    "filename": "com.example.app.handlers.UserHandler",
    "symbol": "processRequest"
  },
  "detection_changed_at": 1765803753960,
  "exposure_time_seconds": 22273153,
  "finding_id": "ZXhhbXBsZS1ydW50aW1lLWNvZGUtdnVsbi0xMjM0NTY=",
  "finding_type": "runtime_code_vulnerability",
  "first_seen_at": 1743345105948,
  "git": {
    "repository_id": "github.com/example-org/web-app",
    "repository_url": "github.com/example-org/web-app"
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1765803753960,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "apm"
  ],
  "related_services": [
    "user-service"
  ],
  "remediation": {
    "is_available": true
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "user-service",
  "resource_type": "service",
  "risk": {
    "is_production": true
  },
  "risk_details": {
    "is_production": {
      "impact_cvss": "neutral",
      "value": true
    }
  },
  "rule": {
    "id": "weak_randomness",
    "name": "Weak Randomness",
    "type": "weak_randomness"
  },
  "runtime_context": {
    "span_id": "1234567890123456789",
    "stacktrace_id": "4",
    "trace_id": "abcdef1234567890abcdef1234567890"
  },
  "service": {
    "git_repository_url": "github.com/example-org/web-app",
    "name": "user-service"
  },
  "severity": "low",
  "severity_details": {
    "adjusted": {
      "score": 3.7,
      "value": "low",
      "value_id": 1,
      "vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N/E:X/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:X/MAC:X/MPR:X/MUI:X/MS:X/MC:X/MI:X/MA:X"
    },
    "base": {
      "score": 3.7,
      "value": "low",
      "value_id": 1,
      "vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N"
    }
  },
  "status": "auto_closed",
  "tags": [
    "dd_rule_type:not-empty",
    "env:prod",
    "scored:false",
    "service:user-service",
    "source:datadog",
    "team:backend",
    "origin:apm"
  ],
  "title": "Weak Randomness",
  "vulnerability": {
    "cwes": [
      "CWE-338"
    ],
    "first_commit": "abc123def456789012345678901234567890abcd",
    "hash": "1234567890",
    "last_commit": "def456abc789012345678901234567890123abcd",
    "owasp_top10_years": [
      2021
    ],
    "stack": {
      "language": "jvm"
    }
  },
  "workflow": {
    "auto_closed_at": 1765803753960,
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Static Code Vulnerability" %}

```json
{
  "base_severity": "critical",
  "code_location": {
    "column_end": 71,
    "column_start": 13,
    "filename": "src/Controllers/UserController.cs",
    "is_test_file": false,
    "line_end": 21,
    "line_start": 21
  },
  "detection_changed_at": 1765912051837,
  "detection_tool": {
    "name": "datadog-static-analyzer",
    "version": "0.7.2"
  },
  "exposure_time_seconds": 2946321,
  "finding_id": "ZXhhbXBsZS1zdGF0aWMtY29kZS12dWxuLTEyMzQ1Ng==",
  "finding_type": "static_code_vulnerability",
  "first_seen_at": 1762873392359,
  "git": {
    "default_branch": "main",
    "is_default_branch": true,
    "repository_id": "github.com/example-org/backend-api",
    "repository_url": "github.com/example-org/backend-api",
    "sha": "abc123def456789012345678901234567890abcd"
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1765912051837,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "ci"
  ],
  "remediation": {
    "codegen": {
      "id": "abc123def456789012345678901234567890abcdef123456",
      "status": "not_available_confidence_too_low"
    },
    "is_available": false
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "github.com/example-org/backend-api",
  "resource_type": "repository",
  "rule": {
    "id": "csharp-security/ensure-secure-logging",
    "name": "Do not log sensitive information",
    "type": "static_analysis"
  },
  "severity": "critical",
  "severity_details": {
    "adjusted": {
      "score": 9,
      "value": "critical",
      "value_id": 4,
      "vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H/E:X/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:X/MAC:X/MPR:X/MUI:X/MS:X/MC:X/MI:X/MA:X"
    },
    "base": {
      "score": 9,
      "value": "critical",
      "value_id": 4,
      "vector": "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H"
    }
  },
  "status": "auto_closed",
  "tags": [
    "dd_rule_type:not-empty",
    "team:backend",
    "scored:false",
    "source:datadog",
    "origin:ci",
    "env:hosted-scan"
  ],
  "title": "Do not log sensitive information",
  "vulnerability": {
    "confidence": "not_evaluated",
    "cwes": [
      "CWE-778"
    ],
    "first_commit": "abc123def456789012345678901234567890aaaa",
    "hash": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
    "last_commit": "abc123def456789012345678901234567890abcd",
    "owasp_top10_years": [
      2017,
      2021
    ],
    "stack": {
      "language": "csharp"
    }
  },
  "workflow": {
    "auto_closed_at": 1765912051836,
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Host & Container Vulnerability" %}

```json
{
  "advisory": {
    "aliases": [
      "CVE-2023-26242"
    ],
    "cve": "CVE-2023-26242",
    "id": "TRIVY-CVE-2023-26242",
    "modified_at": 1746461731000,
    "published_at": 1676942111000,
    "summary": "CVE-2023-26242 found in linux-tools-common 5.15.0-161.171",
    "type": "component_with_known_vulnerability"
  },
  "base_severity": "high",
  "cloud_resource": {
    "account": "123456789012",
    "cloud_provider": "aws",
    "display_name": "i-0abc123def456789a",
    "region": "us-east-1"
  },
  "detection_changed_at": 1766504273553,
  "finding_id": "ZXhhbXBsZS1ob3N0LXZ1bG4tMTIzNDU2Nzg5MGFiY2RlZg==",
  "finding_type": "host_and_container_vulnerability",
  "first_seen_at": 1766504260849,
  "host": {
    "cloud_provider": "aws",
    "image": "ami-0abc123def456789a",
    "name": "i-0abc123def456789a",
    "os": {
      "name": "ubuntu",
      "version": "22.04"
    }
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1766504273553,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "agentless-scanner"
  ],
  "package": {
    "additional_names": [
      "linux-libc-dev",
      "linux-tools-common"
    ],
    "name": "linux",
    "normalized_name": "linux",
    "version": "5.15.0-161.171"
  },
  "related_services": [
    "exposed_to_attacks:false"
  ],
  "remediation": {
    "is_available": false
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "i-0abc123def456789a",
  "resource_type": "host",
  "risk": {
    "has_exploit_available": false,
    "has_high_exploitability_chance": false,
    "is_production": true,
    "is_publicly_accessible": false
  },
  "risk_details": {
    "has_exploit_available": {
      "evidence": {
        "type": "unavailable"
      },
      "impact_cvss": "safer",
      "value": false
    },
    "has_high_exploitability_chance": {
      "evidence": {
        "epss_score": 0.00017,
        "epss_severity": "low"
      },
      "impact_cvss": "safer",
      "value": false
    },
    "is_production": {
      "impact_cvss": "neutral",
      "value": true
    },
    "is_publicly_accessible": {
      "value": false
    }
  },
  "severity": "medium",
  "severity_details": {
    "adjusted": {
      "score": 6.4,
      "value": "medium",
      "value_id": 2,
      "vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:X/MAC:H/MPR:X/MUI:X/MS:X/MC:X/MI:X/MA:X"
    },
    "base": {
      "score": 7.8,
      "value": "high",
      "value_id": 3,
      "vector": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H"
    }
  },
  "status": "open",
  "tags": [
    "origin:agentless-scanner",
    "package_name:linux",
    "package_version:5.15.0-161.171",
    "fix_available:unavailable",
    "availability-zone:us-east-1e",
    "source:datadog",
    "vulnerability_status:open",
    "scored:false",
    "alias:cve-2023-26242",
    "asset_type:host",
    "os_name:ubuntu",
    "in_production:true",
    "cve:cve-2023-26242",
    "public_exploit_available:false",
    "base_score:7.8",
    "score:6.4",
    "severity:medium",
    "dd_rule_type:not-empty",
    "region:us-east-1",
    "ecosystem:deb",
    "os_version:22.04",
    "base_severity:high",
    "cloud_provider:aws",
    "type:component_with_known_vulnerability",
    "epss_raw_score:0.00017"
  ],
  "title": "CVE-2023-26242 found in linux-tools-common 5.15.0-161.171",
  "vulnerability": {
    "cwes": [
      "CWE-190"
    ],
    "hash": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
    "stack": {
      "ecosystem": "deb"
    }
  },
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="IaC Misconfiguration" %}

```json
{
  "base_severity": "low",
  "code_location": {
    "column_end": 37,
    "column_start": 1,
    "filename": "k8s/services/templates/api-service.yaml",
    "is_test_file": false,
    "line_end": 5,
    "line_start": 5
  },
  "description": "As a best practice, ensure namespaces are used correctly to group and administer resources. Kubernetes authorization mechanisms, such as RBAC, can enforce policies that segregate or restrict user access to namespaces. This rule scans cluster manifests for resources that specify a namespace and aggregates the namespaces in use, reporting them for review. Review the reported namespaces to confirm they are required, appropriately configured, and governed by suitable access controls (for example, RoleBindings, NetworkPolicies, or admission controllers). Rule ID: [e84eaf4d-2f45-47b2-abe8-e581b06deb66]",
  "detection_changed_at": 1765825694643,
  "detection_tool": {
    "name": "Datadog IaC Scanning",
    "version": "full_scan"
  },
  "exposure_time_seconds": 5097262,
  "finding_id": "ZXhhbXBsZS1pYWMtbWlzY29uZmlnLTEyMzQ1Ng==",
  "finding_type": "iac_misconfiguration",
  "first_seen_at": 1760620587440,
  "git": {
    "default_branch": "main",
    "is_default_branch": true,
    "repository_id": "github.com/example-org/infrastructure",
    "repository_url": "github.com/example-org/infrastructure",
    "sha": "abc123def456789012345678901234567890abcd"
  },
  "iac_resource": {
    "platform": "kubernetes"
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1765825694643,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "ci"
  ],
  "remediation": {
    "codegen": {
      "id": "abc123def456789012345678901234567890abcdef123456",
      "status": "generated"
    },
    "description": "[]",
    "is_available": false
  },
  "resource_id": "Service.api-service",
  "resource_name": "api-service",
  "resource_type": "Service",
  "rule": {
    "id": "e84eaf4d-2f45-47b2-abe8-e581b06deb66",
    "name": "Ensure administrative boundaries between resources",
    "type": "access_control"
  },
  "severity": "low",
  "severity_details": {
    "adjusted": {
      "score": 2.8,
      "value": "low",
      "value_id": 1,
      "vector": "CVSS:3.1/AV:P/AC:L/PR:H/UI:R/S:U/C:L/I:L/A:N/E:X/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:X/MAC:X/MPR:X/MUI:X/MS:X/MC:X/MI:X/MA:X"
    },
    "base": {
      "score": 2.8,
      "value": "low",
      "value_id": 1,
      "vector": "CVSS:3.0/AV:P/AC:L/PR:H/UI:R/S:U/C:L/I:L/A:N"
    }
  },
  "status": "auto_closed",
  "tags": [
    "dd_rule_type:not-empty",
    "team:backend",
    "scored:false",
    "env:hosted-scan",
    "origin:ci",
    "source:datadog"
  ],
  "title": "namespaces in use: default, staging, production",
  "vulnerability": {
    "confidence": "not_evaluated",
    "first_commit": "abc123def456789012345678901234567890aaaa",
    "hash": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
    "last_commit": "abc123def456789012345678901234567890abcd",
    "stack": {
      "language": "yaml"
    }
  },
  "workflow": {
    "auto_closed_at": 1765825694643,
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Identity Risk" %}

```json
{
  "cloud_resource": {
    "account": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "category": "serverless",
    "cloud_provider": "azure",
    "configuration": {
      "availability_state": "Normal",
      "azure_app_service_plan_key": "abc123def456789012345678901234ab",
      "azure_function_key": "def456abc789012345678901234567cd",
      "client_affinity_enabled": false,
      "client_cert_enabled": false,
      "client_cert_mode": "Required",
      "container_size": 1536,
      "custom_domain_verification_id": "ABC123DEF456789012345678901234567890ABCDEF123456789012345678901234",
      "daily_memory_time_quota": 0,
      "default_host_name": "my-function-app.azurewebsites.net",
      "enabled": true,
      "enabled_host_names": [
        "my-function-app.azurewebsites.net",
        "my-function-app.scm.azurewebsites.net"
      ],
      "external_id": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/example-rg/providers/Microsoft.Web/sites/my-function-app",
      "host_names": [
        "my-function-app.azurewebsites.net"
      ],
      "host_names_disabled": false,
      "https_only": true,
      "hyper_v": false,
      "is_xenon": false,
      "key_vault_reference_identity": "SystemAssigned",
      "kind": "functionapp",
      "last_modified_time_utc": "2025-10-20T18:07:00.17Z",
      "location": "East US",
      "name": "my-function-app",
      "outbound_ip_addresses": "10.0.0.1,10.0.0.2,10.0.0.3",
      "possible_outbound_ip_addresses": "10.0.0.1,10.0.0.2,10.0.0.3,10.0.0.4,10.0.0.5",
      "redundancy_mode": "None",
      "repository_site_name": "my-function-app",
      "reserved": false,
      "resource_group": "example-rg",
      "scm_site_also_stopped": false,
      "server_farm_id": "/subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/example-rg/providers/Microsoft.Web/serverfarms/ASP-example",
      "site_config_acr_use_managed_identity_creds": false,
      "site_config_always_on": false,
      "site_config_ftps_state": "FtpsOnly",
      "site_config_function_app_scale_limit": 200,
      "site_config_min_tls_version": "1.2",
      "site_config_net_framework_version": "v6.0",
      "site_config_number_of_workers": 1,
      "site_config_publishing_username": "REDACTED",
      "state": "Running",
      "storage_account_required": false,
      "subscription_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "subscription_name": "example-subscription",
      "type": "Microsoft.Web/sites",
      "usage_state": "Normal"
    },
    "display_name": "my-function-app",
    "region": "eastus"
  },
  "compliance": {
    "evaluation": "pass"
  },
  "description": "This rule identifies when an Azure Function has administrative level permissions at the subscription scope. Administrative Azure role assignments at the subscription scope grant extensive privileges that can affect all resources within the subscription. This broad access increases the risk of accidental or malicious changes. Remediation: Datadog recommends reducing the permissions and scope of a role assignment to the minimum necessary. Where possible, assign roles at the resource group or individual resource level and use built-in roles with limited privileges tailored to operational requirements.",
  "detection_changed_at": 1766084844000,
  "finding_id": "ZXhhbXBsZS1pZGVudGl0eS1yaXNrLTEyMzQ1Ng==",
  "finding_type": "identity_risk",
  "first_seen_at": 1766084844000,
  "is_in_security_inbox": false,
  "last_seen_at": 1766093845000,
  "metadata": {
    "schema_version": "2"
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "my-function-app",
  "resource_type": "azure_function",
  "risk": {
    "has_privileged_access": false
  },
  "risk_details": {
    "has_privileged_access": {
      "value": false
    }
  },
  "rule": {
    "default_rule_id": "def-000-s2l",
    "id": "def-000-s2l",
    "name": "Azure function has admin level privileges at the subscription scope",
    "type": "cloud configuration",
    "version": 5
  },
  "severity": "medium",
  "severity_details": {
    "adjusted": {
      "score": 5.5,
      "value": "medium",
      "value_id": 2
    }
  },
  "status": "open",
  "tags": [
    "scored:true",
    "security:compliance",
    "scope:azure.security",
    "cloud_provider:azure",
    "dd_rule_type:ciem",
    "operating_system:windows",
    "source:azure.security",
    "region:eastus"
  ],
  "title": "Azure function has admin level privileges at the subscription scope",
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Library Vulnerability" %}

```json
{
  "advisory": {
    "aliases": [
      "CVE-2025-46392"
    ],
    "cve": "CVE-2025-46392",
    "id": "GHSA-pvp8-3xj6-8c6x",
    "type": "component_with_known_vulnerability"
  },
  "base_severity": "medium",
  "code_location": {
    "column_end": 22,
    "column_start": 9,
    "filename": "test/plugin/scenarios/hystrix-scenario/pom.xml",
    "line_end": 77,
    "line_start": 73
  },
  "detection_changed_at": 1766518394577,
  "finding_id": "ZXhhbXBsZS1saWJyYXJ5LXZ1bG4tMTIzNDU2Nzg5MGFi",
  "finding_type": "library_vulnerability",
  "first_seen_at": 1763488117383,
  "git": {
    "author": {
      "name": "ci-bot"
    },
    "default_branch": "main",
    "is_default_branch": true,
    "repository_id": "github.com/example-org/java-app",
    "repository_url": "github.com/example-org/java-app",
    "sha": "abc123def456789012345678901234567890abcd"
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1766522443454,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "ci"
  ],
  "package": {
    "declaration": {
      "block": {
        "column_end": 22,
        "column_start": 9,
        "filename": "test/plugin/scenarios/hystrix-scenario/pom.xml",
        "line_end": 77,
        "line_start": 73
      },
      "name": {
        "column_end": 37,
        "column_start": 25,
        "filename": "test/plugin/scenarios/hystrix-scenario/pom.xml",
        "line_end": 75,
        "line_start": 75
      },
      "version": {
        "column_end": 39,
        "column_start": 33,
        "filename": "test/plugin/scenarios/hystrix-scenario/pom.xml",
        "line_end": 34,
        "line_start": 34
      }
    },
    "dependency_type": "transitive",
    "manager": "maven",
    "name": "commons-configuration:commons-configuration",
    "normalized_name": "commons-configuration:commons-configuration",
    "root_parents": [
      {
        "declaration": {
          "version": {
            "column_end": 39,
            "column_start": 33,
            "filename": "test/plugin/scenarios/hystrix-scenario/pom.xml",
            "line_end": 34,
            "line_start": 34
          }
        },
        "language": "jvm",
        "name": "com.netflix.hystrix:hystrix-core",
        "version": "1.4.20"
      }
    ],
    "scope": "production",
    "version": "1.8"
  },
  "related_services": [
    "example-service"
  ],
  "remediation": {
    "description": "Try upgrading to a version > 1.10 (if released)",
    "is_available": true,
    "package": {
      "closest_no_vulnerabilities": [
        {
          "fixed_advisories": [
            {
              "base_severity": "medium",
              "id": "GHSA-pvp8-3xj6-8c6x"
            }
          ],
          "name": "org.apache.commons:commons-configuration2",
          "version": "2.10.1"
        }
      ],
      "latest_no_vulnerabilities": [
        {
          "fixed_advisories": [
            {
              "base_severity": "medium",
              "id": "GHSA-pvp8-3xj6-8c6x"
            }
          ],
          "name": "commons-configuration:commons-configuration",
          "version": "20041012.002804"
        }
      ]
    },
    "recommended": {
      "fixed_advisories": [
        {
          "base_severity": "medium",
          "id": "GHSA-pvp8-3xj6-8c6x"
        }
      ],
      "name": "org.apache.commons:commons-configuration2",
      "original_library_name": "commons-configuration:commons-configuration",
      "version": "2.10.1",
      "vulnerable_package": true
    }
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "github.com/example-org/java-app",
  "resource_type": "repository",
  "risk": {
    "has_exploit_available": false,
    "has_high_exploitability_chance": false,
    "is_exposed_to_attacks": false,
    "is_function_reachable": false,
    "is_production": true
  },
  "risk_details": {
    "has_exploit_available": {
      "evidence": {
        "type": "unavailable"
      },
      "impact_cvss": "safer",
      "value": false
    },
    "has_high_exploitability_chance": {
      "evidence": {
        "epss_score": 0.00181,
        "epss_severity": "low"
      },
      "impact_cvss": "safer",
      "value": false
    },
    "is_exposed_to_attacks": {
      "impact_cvss": "neutral",
      "value": false
    },
    "is_function_reachable": {
      "value": false
    },
    "is_production": {
      "impact_cvss": "neutral",
      "value": true
    }
  },
  "severity": "low",
  "severity_details": {
    "adjusted": {
      "score": 1.7,
      "value": "low",
      "value_id": 1,
      "vector": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N/E:U/MAC:H"
    },
    "base": {
      "score": 6.9,
      "value": "medium",
      "value_id": 2,
      "vector": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N/E:U"
    }
  },
  "status": "open",
  "tags": [
    "dd_rule_type:not-empty",
    "team:backend",
    "scored:false",
    "origin:ci",
    "source:datadog",
    "service:example-service"
  ],
  "title": "Apache Commons Configuration Uncontrolled Resource Consumption",
  "vulnerability": {
    "cwes": [
      "CWE-400"
    ],
    "first_commit": "abc123def456789012345678901234567890aaaa",
    "hash": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
    "last_commit": "abc123def456789012345678901234567890abcd",
    "stack": {
      "ecosystem": "maven",
      "language": "jvm"
    }
  },
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Misconfiguration" %}

```json
{
  "cloud_resource": {
    "display_name": "batch-processor-job-12345678"
  },
  "compliance": {
    "evaluation": "pass",
    "framework_requirement_controls": [
      "cis-kubernetes/Pod-Security-Standards-Baseline/5.2.4",
      "pci-dss/Install-and-Maintain-Network-Security-Controls/1.5",
      "nist-800-53/System and Communications Protection/SC-28"
    ],
    "framework_requirements": [
      "cis-kubernetes/Pod-Security-Standards-Baseline",
      "pci-dss/Install-and-Maintain-Network-Security-Controls",
      "nist-800-53/System and Communications Protection"
    ],
    "frameworks": [
      {
        "control": "5.2.3",
        "framework": "cis-kubernetes",
        "is_default": true,
        "requirement": "Pod-Security-Standards-Baseline",
        "version": "1.9.0"
      },
      {
        "control": "SC-28",
        "framework": "nist-800-53",
        "is_default": true,
        "requirement": "System and Communications Protection",
        "version": "rev5"
      },
      {
        "control": "1.5",
        "framework": "pci-dss",
        "is_default": true,
        "requirement": "Install-and-Maintain-Network-Security-Controls",
        "version": "4.0.1"
      }
    ]
  },
  "description": "Sharing host namespaces in Kubernetes poses security risks by allowing pods to access the host's network, process, and IPC namespaces. To enhance cluster security, sharing of host namespaces must be disallowed. Remediation: 1. Check your pod specifications for `hostNetwork`, `hostPID`, and `hostIPC` settings. 2. Ensure these fields are set to `false` or removed. 3. Apply changes with `kubectl apply -f <manifest-file>`. 4. Verify that pods do not share host namespaces.",
  "detection_changed_at": 1766095392000,
  "finding_id": "ZXhhbXBsZS1taXNjb25maWd1cmF0aW9uLTEyMzQ1Ng==",
  "finding_type": "misconfiguration",
  "first_seen_at": 1766095392000,
  "is_in_security_inbox": false,
  "k8s": {
    "cluster_id": "prod-gke-cluster-us-central1"
  },
  "last_seen_at": 1766095392000,
  "metadata": {
    "schema_version": "2"
  },
  "resource_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
  "resource_name": "batch-processor-job-12345678",
  "resource_type": "kubernetes_job",
  "rule": {
    "default_rule_id": "def-000-qtt",
    "id": "def-000-qtt",
    "name": "Jobs should not share the host namespace",
    "type": "cloud configuration",
    "version": 4
  },
  "severity": "low",
  "severity_details": {
    "adjusted": {
      "score": 2,
      "value": "low",
      "value_id": 1
    }
  },
  "status": "open",
  "tags": [
    "scored:true",
    "kube_cluster_name:prod-gke-cluster-us-central1",
    "scope:kubernetes",
    "security:compliance",
    "framework:cis-kubernetes",
    "framework:pci-dss",
    "framework:nist-800-53",
    "env:dev",
    "namespace:default",
    "kube_distribution:gke",
    "source:kubernetes"
  ],
  "title": "Jobs should not share the host namespace",
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Secret" %}

```json
{
  "base_severity": "critical",
  "code_location": {
    "column_end": 33,
    "column_start": 13,
    "filename": "docs/deployment/README.md",
    "is_test_file": false,
    "line_end": 22,
    "line_start": 22
  },
  "detection_changed_at": 1765912291919,
  "detection_tool": {
    "name": "datadog-static-analyzer",
    "version": "0.7.2"
  },
  "exposure_time_seconds": 2831065,
  "finding_id": "ZXhhbXBsZS1zZWNyZXQtMTIzNDU2",
  "finding_type": "secret",
  "first_seen_at": 1762988619532,
  "git": {
    "default_branch": "main",
    "is_default_branch": true,
    "repository_id": "github.com/example-org/backend-api",
    "repository_url": "github.com/example-org/backend-api",
    "sha": "abc123def456789012345678901234567890abcd"
  },
  "is_in_security_inbox": false,
  "last_seen_at": 1765912291919,
  "metadata": {
    "schema_version": "2"
  },
  "origin": [
    "ci"
  ],
  "remediation": {
    "codegen": {
      "id": "abc123def456789012345678901234567890abcdef123456",
      "status": "not_available_confidence_too_low"
    },
    "description": "Matches a sequence of characters representing an AWS Access Key ID, which consists of a 4 uppercase letters indicating the type of resource the ID applies to, followed by 16 alphanumeric characters.\n\nExamples of matching formats:\n- `AIDAJQABLZS4A3QDU576`\n- `AROADBQP57FF2EXAMPLE`",
    "is_available": false
  },
  "resource_id": "abc123def456789012345678901234ab",
  "resource_name": "github.com/example-org/backend-api",
  "resource_type": "repository",
  "rule": {
    "id": "secrets/aws-access-key-id",
    "name": "AWS Access Key ID Scanner",
    "type": "secret"
  },
  "secret": {
    "validation_status": "valid"
  },
  "severity": "critical",
  "severity_details": {
    "adjusted": {
      "score": 9,
      "value": "critical",
      "value_id": 4,
      "vector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H/E:X/RL:X/RC:X/CR:X/IR:X/AR:X/MAV:X/MAC:X/MPR:X/MUI:X/MS:X/MC:X/MI:X/MA:X"
    },
    "base": {
      "score": 9,
      "value": "critical",
      "value_id": 4,
      "vector": "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H"
    }
  },
  "status": "auto_closed",
  "tags": [
    "dd_rule_type:not-empty",
    "team:backend",
    "scored:false",
    "source:datadog",
    "origin:ci",
    "env:secrets-hosted-scan"
  ],
  "title": "AWS Access Key ID Scanner",
  "vulnerability": {
    "confidence": "not_evaluated",
    "first_commit": "abc123def456789012345678901234567890aaaa",
    "hash": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
    "last_commit": "abc123def456789012345678901234567890abcd",
    "stack": {
      "language": "markdown"
    }
  },
  "workflow": {
    "auto_closed_at": 1765912291918,
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}

{% tab title="Workload Activity" %}

```json
{
  "description": "Compilers should not be present or executed in production containers. Container images should be built with pre-compiled binaries and follow immutable infrastructure principles.",
  "detection_changed_at": 1766024414711,
  "finding_id": "ZXhhbXBsZS13b3JrbG9hZC1hY3Rpdml0eS0xMjM0NTY=",
  "finding_type": "workload_activity",
  "first_seen_at": 1766024414711,
  "host": {
    "name": "gke-prod-cluster-default-pool-abc12345.c.example-project.internal"
  },
  "is_in_security_inbox": false,
  "k8s": {
    "cluster_id": "prod-gke-cluster-us-central1"
  },
  "last_seen_at": 1766025229714,
  "metadata": {
    "schema_version": "2"
  },
  "resource_id": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
  "resource_name": "abc123def456789012345678901234567890abcdef12345678901234567890ab",
  "resource_type": "container",
  "rule": {
    "default_rule_id": "def-000-krp",
    "id": "def-000-krp",
    "name": "Containers should not execute compilers",
    "type": "workload_activity",
    "version": 1
  },
  "severity": "medium",
  "severity_details": {
    "adjusted": {
      "score": 5.5,
      "value": "medium",
      "value_id": 2
    }
  },
  "status": "open",
  "tags": [
    "scored:true",
    "dd_rule_type:workload_activity",
    "cloud_provider:gcp",
    "cluster_name:prod-gke-cluster-us-central1",
    "policy:threat-detection",
    "region:us-central1",
    "env:staging",
    "kube_namespace:default",
    "security:compliance",
    "type:exec",
    "rule_id:compiler_in_container",
    "kube_container_name:runner",
    "source:runtime-security-agent",
    "tactic:ta0005-defense-evasion",
    "policy:best-practice"
  ],
  "title": "Containers should not execute compilers",
  "workflow": {
    "mute": {
      "is_muted": false
    }
  }
}
```

{% /tab %}



## Schema Reference{% #schema-reference %}

The following sections describe all available attributes in the Security Findings schema, organized by namespace.

{% collapsible-section #core-attributes %}
### Core Attributes

These attributes are present on all security findings and describe the fundamental nature and status of the finding.

| Attribute name          | Type           | Description                                                                                                                                                                                                                                                                                                        |
| ----------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `severity`              | string         | **Path:** `@severity`Datadog-adjusted severity level of the finding. Valid values: `critical`, `high`, `medium`, `low`, `info`, `none`, `unknown`.                                                                                                                                                                 |
| `base_severity`         | string         | **Path:** `@base_severity`Base severity level of the finding before any adjustments. Valid values: `critical`, `high`, `medium`, `low`, `info`, `none`, `unknown`.                                                                                                                                                 |
| `status`                | string         | **Path:** `@status`Workflow status of the finding. Valid values: `open`, `muted`, `auto_closed`.                                                                                                                                                                                                                   |
| `finding_type`          | string         | **Path:** `@finding_type`Category of the finding. Valid values: `api_security`, `attack_path`, `runtime_code_vulnerability`, `static_code_vulnerability`, `host_and_container_vulnerability`, `iac_misconfiguration`, `identity_risk`, `library_vulnerability`, `misconfiguration`, `secret`, `workload_activity`. |
| `finding_id`            | string         | **Path:** `@finding_id`Unique identifier of the finding.                                                                                                                                                                                                                                                           |
| `title`                 | string         | **Path:** `@title`Human-readable title for the finding.                                                                                                                                                                                                                                                            |
| `description`           | string         | **Path:** `@description`Human-readable explanation of the finding. May include Markdown formatting.                                                                                                                                                                                                                |
| `resource_id`           | string         | **Path:** `@resource_id`Unique identifier of the resource affected by the finding.                                                                                                                                                                                                                                 |
| `resource_name`         | string         | **Path:** `@resource_name`Human-readable name of the resource affected by the finding.                                                                                                                                                                                                                             |
| `resource_type`         | string         | **Path:** `@resource_type`Type of the resource.                                                                                                                                                                                                                                                                    |
| `first_seen_at`         | integer        | **Path:** `@first_seen_at`Timestamp in milliseconds (UTC) when the finding was first detected.                                                                                                                                                                                                                     |
| `last_seen_at`          | integer        | **Path:** `@last_seen_at`Timestamp in milliseconds (UTC) when the finding was most recently detected.                                                                                                                                                                                                              |
| `detection_changed_at`  | integer        | **Path:** `@detection_changed_at`Timestamp in milliseconds (UTC) when the finding's evaluation or detection state last changed.                                                                                                                                                                                    |
| `origin`                | array (string) | **Path:** `@origin`Detection origins that produced the finding, such as agentless scans, APM, SCI (Software Composition Analysis), or CI (Continuous Integration).                                                                                                                                                 |
| `exposure_time_seconds` | integer        | **Path:** `@exposure_time_seconds`Indicates the time elapsed, in seconds, between when the finding was last closed and when it was detected again.                                                                                                                                                                 |
| `is_in_security_inbox`  | boolean        | **Path:** `@is_in_security_inbox`True if the finding appears in the Security Inbox; false otherwise.                                                                                                                                                                                                               |
| `detection_tool`        | object         | **Path:** `@detection_tool`Information about the tool or engine responsible for detecting the finding.                                                                                                                                                                                                             |

{% /collapsible-section %}

{% collapsible-section #workflow %}
### Workflow

All mutable information related to the management of a finding after it was detected. Includes fields that can be updated manually through the UI or automatically through pipelines.

| Attribute name   | Type           | Description                                                                                                                        |
| ---------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `triage`         | object         | **Path:** `@workflow.triage`Assignment and status information. Assignment may be synchronized with case or Jira information.       |
| `auto_closed_at` | integer        | **Path:** `@workflow.auto_closed_at`Timestamp in milliseconds (UTC) when the finding was automatically closed by the system.       |
| `due_date`       | object         | **Path:** `@workflow.due_date`Due date rule applied to the finding.                                                                |
| `mute`           | object         | **Path:** `@workflow.mute`Muting information and metadata.                                                                         |
| `automations`    | array (object) | **Path:** `@workflow.automations`Information about any automation rules that apply to the finding.                                 |
| `integrations`   | object         | **Path:** `@workflow.integrations`Integrations like Jira, Case Management, or ServiceNow used to triage and remediate the finding. |

### Triage{% #triage %}

Assignment and status information. Assignment may be synchronized with case or Jira information.

| Attribute name                | Type    | Description                                                                                                                                             |
| ----------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assignee`                    | object  | **Path:** `@workflow.triage.assignee`User assigned to this finding.                                                                                     |
| `time_to_acknowledge_seconds` | integer | **Path:** `@workflow.triage.time_to_acknowledge_seconds`Time in seconds between when the finding was first detected and the first manual triage action. |
| `time_to_resolution_seconds`  | integer | **Path:** `@workflow.triage.time_to_resolution_seconds`Time in seconds between when the finding was first detected and when it was resolved.            |

#### Assignee{% #assignee %}

User assigned to this finding.

| Attribute name | Type    | Description                                                                                                          |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| `name`         | string  | **Path:** `@workflow.triage.assignee.name`Display name of the assignee.                                              |
| `id`           | string  | **Path:** `@workflow.triage.assignee.id`Unique identifier in UUID format for the assignee.                           |
| `updated_at`   | integer | **Path:** `@workflow.triage.assignee.updated_at`Timestamp in milliseconds (UTC) when the assignee was last modified. |
| `updated_by`   | object  | **Path:** `@workflow.triage.assignee.updated_by`User who last modified the assignee.                                 |

##### Updated By{% #updated-by %}

User who last modified the assignee.

| Attribute name | Type   | Description                                                                                                                     |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | string | **Path:** `@workflow.triage.assignee.updated_by.id`Unique identifier in UUID format of the user who last modified the assignee. |
| `name`         | string | **Path:** `@workflow.triage.assignee.updated_by.name`Display name of the user who last modified the assignee                    |

### Due Date{% #due-date %}

Due date rule applied to the finding.

| Attribute name | Type    | Description                                                                                            |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------ |
| `due_at`       | integer | **Path:** `@workflow.due_date.due_at`Timestamp in milliseconds (UTC) for the finding's due date.       |
| `is_overdue`   | boolean | **Path:** `@workflow.due_date.is_overdue`True if the due date has been reached; false otherwise.       |
| `rule_id`      | string  | **Path:** `@workflow.due_date.rule_id`Unique identifier for the due date rule applied to this finding. |

### Mute{% #mute %}

Muting information and metadata.

| Attribute name     | Type    | Description                                                                                                                                                                                                                                                   |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `is_muted`         | boolean | **Path:** `@workflow.mute.is_muted`True if the finding is muted; false if it is active.                                                                                                                                                                       |
| `reason`           | string  | **Path:** `@workflow.mute.reason`Reason provided for muting the finding. Valid values: `none`, `no_pending_fix`, `human_error`, `no_longer_accepted_risk`, `other`, `pending_fix`, `false_positive`, `accepted_risk`, `no_fix`, `duplicate`, `risk_accepted`. |
| `description`      | string  | **Path:** `@workflow.mute.description`Free-text explanation for why the finding was muted.                                                                                                                                                                    |
| `expire_at`        | integer | **Path:** `@workflow.mute.expire_at`Timestamp in milliseconds (UTC) when the mute expires. If not set, the mute is permanent.                                                                                                                                 |
| `is_muted_by_rule` | boolean | **Path:** `@workflow.mute.is_muted_by_rule`True if the finding is muted by an automation rule; false otherwise. If true, the relevant automation rule is referenced in the workflow.automations section.                                                      |
| `rule_id`          | string  | **Path:** `@workflow.mute.rule_id`Unique identifier for the automation rule that muted this finding. Only set when `is_muted_by_rule` is true.                                                                                                                |
| `rule_name`        | string  | **Path:** `@workflow.mute.rule_name`Human-readable name of the automation rule that muted this finding. Only set when `is_muted_by_rule` is true.                                                                                                             |
| `muted_at`         | integer | **Path:** `@workflow.mute.muted_at`Timestamp in milliseconds (UTC) when the finding was muted.                                                                                                                                                                |
| `muted_by`         | object  | **Path:** `@workflow.mute.muted_by`User who muted the finding.                                                                                                                                                                                                |

#### Muted By{% #muted-by %}

User who muted the finding.

| Attribute name | Type   | Description                                                                                               |
| -------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| `id`           | string | **Path:** `@workflow.mute.muted_by.id`Unique identifier in UUID format of the user who muted the finding. |
| `name`         | string | **Path:** `@workflow.mute.muted_by.name`Display name of the user who muted the finding.                   |

### Integrations{% #integrations %}

Integrations like Jira, Case Management, or ServiceNow used to triage and remediate the finding.

| Attribute name  | Type           | Description                                                                                                                               |
| --------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `cases`         | array (object) | **Path:** `@workflow.integrations.cases`Array of cases attached to the finding.                                                           |
| `jira`          | array (string) | **Path:** `@workflow.integrations.jira`Jira issue keys attached to this finding in the format `PROJECT-NUMBER` (for example, `PROJ-123`). |
| `pull_requests` | array (object) | **Path:** `@workflow.integrations.pull_requests`Pull requests used to remediate this finding.                                             |

{% /collapsible-section %}

{% collapsible-section #risk %}
### Risk

Risk-related attributes for the finding. Each key must have a matching key in the `risk_details` namespace.

| Attribute name                   | Type    | Description                                                                                                                                                                |
| -------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `has_sensitive_data`             | boolean | **Path:** `@risk.has_sensitive_data`True if the finding has access to a resource that contains sensitive data; false otherwise.                                            |
| `is_function_reachable`          | boolean | **Path:** `@risk.is_function_reachable`True if the vulnerable function can be executed; false otherwise.                                                                   |
| `is_exposed_to_attacks`          | boolean | **Path:** `@risk.is_exposed_to_attacks`True if attacks have already been detected on this resource; false otherwise.                                                       |
| `has_privileged_access`          | boolean | **Path:** `@risk.has_privileged_access`True if the finding's resource is running with elevated privileges or has the ability to assume a privileged role; false otherwise. |
| `is_production`                  | boolean | **Path:** `@risk.is_production`True if the finding's resource is running in production; false otherwise.                                                                   |
| `is_publicly_accessible`         | boolean | **Path:** `@risk.is_publicly_accessible`True if the finding's resource is publicly accessible; false otherwise.                                                            |
| `has_exploit_available`          | boolean | **Path:** `@risk.has_exploit_available`True if known exploits exist for this finding; false otherwise.                                                                     |
| `has_high_exploitability_chance` | boolean | **Path:** `@risk.has_high_exploitability_chance`True if the EPSS (Exploit Prediction Scoring System) score is above 1%; false otherwise.                                   |
| `is_tainted_from_request_url`    | boolean | **Path:** `@risk.is_tainted_from_request_url`True if the final URL contains tainted parts originating from the request URL; false otherwise.                               |
| `is_tainted_from_query_string`   | boolean | **Path:** `@risk.is_tainted_from_query_string`True if the string is tainted with elements derived from an HTTP query string; false otherwise.                              |
| `is_tainted_from_database`       | boolean | **Path:** `@risk.is_tainted_from_database`True if the string is tainted due to originating from an untrusted database source; false otherwise.                             |
| `is_using_sha1`                  | boolean | **Path:** `@risk.is_using_sha1`True if SHA1 is used in a weak hash; false otherwise.                                                                                       |

{% /collapsible-section %}

{% collapsible-section #risk-details %}
### Risk Details

Contextual risk factors that help assess the potential impact of a finding. These fields describe characteristics like exposure, sensitivity, and signs of active exploitation.

| Attribute name                   | Type   | Description                                                                                                                                                                                         |
| -------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `has_sensitive_data`             | object | **Path:** `@risk_details.has_sensitive_data`Evidence and indicators about whether the affected resource has sensitive data.                                                                         |
| `is_function_reachable`          | object | **Path:** `@risk_details.is_function_reachable`Groups evidence and indicators about whether the vulnerable function or module is used in the code.                                                  |
| `is_exposed_to_attacks`          | object | **Path:** `@risk_details.is_exposed_to_attacks`Groups evidence and indicators about whether the service where the finding was detected is exposed to attacks.                                       |
| `has_privileged_access`          | object | **Path:** `@risk_details.has_privileged_access`Groups evidence and indicators about whether the resource has privileged access.                                                                     |
| `is_production`                  | object | **Path:** `@risk_details.is_production`Groups evidence and indicators about whether the resource associated with the finding is running in a production environment.                                |
| `is_publicly_accessible`         | object | **Path:** `@risk_details.is_publicly_accessible`Groups information about whether the affected resource is accessible from the public internet.                                                      |
| `has_exploit_available`          | object | **Path:** `@risk_details.has_exploit_available`Groups information about whether a known exploit exists for this finding advisory.                                                                   |
| `has_high_exploitability_chance` | object | **Path:** `@risk_details.has_high_exploitability_chance`Groups evidence and indicators about whether the vulnerability is likely to be exploited based on EPSS (Exploit Prediction Scoring System). |
| `is_tainted_from_request_url`    | object | **Path:** `@risk_details.is_tainted_from_request_url`Groups information about whether the tainted parts originate from the request URL.                                                             |
| `is_tainted_from_query_string`   | object | **Path:** `@risk_details.is_tainted_from_query_string`Groups information about whether the tainted parts originate from a query string.                                                             |
| `is_tainted_from_database`       | object | **Path:** `@risk_details.is_tainted_from_database`Groups information about whether tainted parts originate from a database.                                                                         |
| `is_using_sha1`                  | object | **Path:** `@risk_details.is_using_sha1`Groups information about whether SHA1 is used in a weak hash.                                                                                                |

### Has Sensitive Data{% #has-sensitive-data %}

Evidence and indicators about whether the affected resource has sensitive data.

| Attribute name | Type    | Description                                                                                                                                                                   |
| -------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.has_sensitive_data.impact_cvss`Describes how sensitive data presence changes the CVSS score. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.has_sensitive_data.value`Same as `risk.has_sensitive_data`.                                                                                          |
| `evidence`     | object  | **Path:** `@risk_details.has_sensitive_data.evidence`Evidence supporting the presence of sensitive data.                                                                      |

#### Evidence{% #evidence %}

Evidence supporting the presence of sensitive data.

| Attribute name | Type   | Description                                                                                                                                    |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `sds_id`       | string | **Path:** `@risk_details.has_sensitive_data.evidence.sds_id`Identifier of a sensitive data entry discovered by Datadog Sensitive Data Scanner. |

### Is Function Reachable{% #is-function-reachable %}

Groups evidence and indicators about whether the vulnerable function or module is used in the code.

| Attribute name | Type    | Description                                                                                                                                                                              |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_function_reachable.impact_cvss`Describes how function reachability changes the CVSS risk assessment. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_function_reachable.value`True if the function is reachable; false otherwise.                                                                                 |
| `evidence`     | object  | **Path:** `@risk_details.is_function_reachable.evidence`Contains the evidence used to determine whether the function is reachable.                                                       |

#### Evidence{% #evidence-1 %}

Contains the evidence used to determine whether the function is reachable.

| Attribute name | Type   | Description                                                                                                             |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| `locations`    | object | **Path:** `@risk_details.is_function_reachable.evidence.locations`Array of code locations where the function is called. |

##### Locations{% #locations %}

Array of code locations where the function is called.

| Attribute name | Type    | Description                                                                                                                                                          |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filename`     | string  | **Path:** `@risk_details.is_function_reachable.evidence.locations.filename`Name of the file where the root parent package version is declared.                       |
| `line_start`   | integer | **Path:** `@risk_details.is_function_reachable.evidence.locations.line_start`Line number where the root parent package version declaration starts in the file.       |
| `column_start` | integer | **Path:** `@risk_details.is_function_reachable.evidence.locations.column_start`Column position where the root parent package version declaration starts on the line. |
| `line_end`     | integer | **Path:** `@risk_details.is_function_reachable.evidence.locations.line_end`Line number where the root parent package version declaration ends in the file.           |
| `column_end`   | integer | **Path:** `@risk_details.is_function_reachable.evidence.locations.column_end`Column position where the root parent package version declaration ends on the line.     |
| `is_test_file` | boolean | **Path:** `@risk_details.is_function_reachable.evidence.locations.is_test_file`True if the code file is a test file; false otherwise.                                |
| `url`          | string  | **Path:** `@risk_details.is_function_reachable.evidence.locations.url`URL to view the file online (for example, in GitHub), highlighting the code location.          |
| `symbol`       | string  | **Path:** `@risk_details.is_function_reachable.evidence.locations.symbol`                                                                                            |

### Is Exposed To Attacks{% #is-exposed-to-attacks %}

Groups evidence and indicators about whether the service where the finding was detected is exposed to attacks.

| Attribute name | Type    | Description                                                                                                                                                                        |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_exposed_to_attacks.impact_cvss`Describes how the resource's exposure affects the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_exposed_to_attacks.value`Same as `risk.is_exposed_to_attacks`.                                                                                         |
| `evidence`     | object  | **Path:** `@risk_details.is_exposed_to_attacks.evidence`Contains evidence for the presence of attacks.                                                                             |

#### Evidence{% #evidence-2 %}

Contains evidence for the presence of attacks.

| Attribute name    | Type   | Description                                                                                                                                   |
| ----------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `trace_example`   | object | **Path:** `@risk_details.is_exposed_to_attacks.evidence.trace_example`Example of a trace with attacks detected on the finding's resource.     |
| `trace_query`     | string | **Path:** `@risk_details.is_exposed_to_attacks.evidence.trace_query`Query used to find traces with attacks related to the finding's resource. |
| `attacks_details` | object | **Path:** `@risk_details.is_exposed_to_attacks.evidence.attacks_details`Contains details about one of the detected attacks.                   |

### Has Privileged Access{% #has-privileged-access %}

Groups evidence and indicators about whether the resource has privileged access.

| Attribute name | Type    | Description                                                                                                                                                                  |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.has_privileged_access.impact_cvss`Describes how privileged access changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.has_privileged_access.value`True if the resource associated with the finding has privileged access; false otherwise.                                |
| `evidence`     | object  | **Path:** `@risk_details.has_privileged_access.evidence`Contains evidence showing proof of privileged access.                                                                |

#### Evidence{% #evidence-3 %}

Contains evidence showing proof of privileged access.

| Attribute name | Type   | Description                                                                                                                               |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `resource_key` | string | **Path:** `@risk_details.has_privileged_access.evidence.resource_key`Canonical Cloud Resource Identifier with proof of privileged access. |

### Is Production{% #is-production %}

Groups evidence and indicators about whether the resource associated with the finding is running in a production environment.

| Attribute name | Type    | Description                                                                                                                                                                      |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_production.impact_cvss`Describes how production environment status affects the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_production.value`Same as `risk.is_production`.                                                                                                       |
| `evidence`     | object  | **Path:** `@risk_details.is_production.evidence`Contains the `env` tag value that determines if the resource is in production.                                                   |

### Is Publicly Accessible{% #is-publicly-accessible %}

Groups information about whether the affected resource is accessible from the public internet.

| Attribute name | Type    | Description                                                                                                                                                                      |
| -------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_publicly_accessible.impact_cvss`Describes how public accessibility affects the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_publicly_accessible.value`Same as `risk.is_publicly_accessible`.                                                                                     |
| `evidence`     | object  | **Path:** `@risk_details.is_publicly_accessible.evidence`Contains evidence showing proof of access from the internet.                                                            |

#### Evidence{% #evidence-4 %}

Contains evidence showing proof of access from the internet.

| Attribute name | Type   | Description                                                                                                                                             |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resource_key` | string | **Path:** `@risk_details.is_publicly_accessible.evidence.resource_key`Canonical Cloud Resource Identifier of the resource accessible from the internet. |

### Has Exploit Available{% #has-exploit-available %}

Groups information about whether a known exploit exists for this finding advisory.

| Attribute name | Type    | Description                                                                                                                                                                                   |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.has_exploit_available.impact_cvss`Describes how the availability of known exploits changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.has_exploit_available.value`True if known exploits exist for this finding; false otherwise.                                                                          |
| `evidence`     | object  | **Path:** `@risk_details.has_exploit_available.evidence`Contains evidence about exploit availability.                                                                                         |

#### Evidence{% #evidence-5 %}

Contains evidence about exploit availability.

| Attribute name    | Type           | Description                                                                                                                                                      |
| ----------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`            | string         | **Path:** `@risk_details.has_exploit_available.evidence.type`Type of evidence. Valid values: `production_ready`, `poc`, `unavailable`.                           |
| `exploit_urls`    | array (string) | **Path:** `@risk_details.has_exploit_available.evidence.exploit_urls`Lists exploit URLs associated with the finding.                                             |
| `exploit_sources` | array (string) | **Path:** `@risk_details.has_exploit_available.evidence.exploit_sources`Lists exploit sources associated with the finding (for example, NIST, CISA, Exploit-DB). |

### Has High Exploitability Chance{% #has-high-exploitability-chance %}

Groups evidence and indicators about whether the vulnerability is likely to be exploited based on EPSS (Exploit Prediction Scoring System).

| Attribute name | Type    | Description                                                                                                                                                                                    |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.has_high_exploitability_chance.impact_cvss`Describes how high exploitability chance affects the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.has_high_exploitability_chance.value`True if the EPSS score is above 1%; false otherwise.                                                                             |
| `evidence`     | object  | **Path:** `@risk_details.has_high_exploitability_chance.evidence`Contains evidence of the EPSS score.                                                                                          |

#### Evidence{% #evidence-6 %}

Contains evidence of the EPSS score.

| Attribute name  | Type   | Description                                                                                                                                                                         |
| --------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `epss_score`    | number | **Path:** `@risk_details.has_high_exploitability_chance.evidence.epss_score`EPSS score as a percentage representing the chance of exploitation.                                     |
| `epss_severity` | string | **Path:** `@risk_details.has_high_exploitability_chance.evidence.epss_severity`EPSS score severity level. Valid values: `Critical`, `High`, `Medium`, `Low`.                        |
| `threshold`     | number | **Path:** `@risk_details.has_high_exploitability_chance.evidence.threshold`Minimum EPSS score required for a vulnerability to be considered as having a high exploitability chance. |

### Is Tainted From Request Url{% #is-tainted-from-request-url %}

Groups information about whether the tainted parts originate from the request URL.

| Attribute name | Type    | Description                                                                                                                                                                           |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_tainted_from_request_url.impact_cvss`Describes how request URL tainting changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_tainted_from_request_url.value`True if the final URL contains tainted parts originating from the request URL; false otherwise.                            |

### Is Tainted From Query String{% #is-tainted-from-query-string %}

Groups information about whether the tainted parts originate from a query string.

| Attribute name | Type    | Description                                                                                                                                                                             |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_tainted_from_query_string.impact_cvss`Describes how query string tainting changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_tainted_from_query_string.value`True if the string contains elements derived from an HTTP query string; false otherwise.                                    |

### Is Tainted From Database{% #is-tainted-from-database %}

Groups information about whether tainted parts originate from a database.

| Attribute name | Type    | Description                                                                                                                                                                     |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_tainted_from_database.impact_cvss`Describes how database tainting changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_tainted_from_database.value`True if the string is tainted due to originating from an untrusted database source; false otherwise.                    |

### Is Using Sha1{% #is-using-sha1 %}

Groups information about whether SHA1 is used in a weak hash.

| Attribute name | Type    | Description                                                                                                                                                   |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `impact_cvss`  | string  | **Path:** `@risk_details.is_using_sha1.impact_cvss`Describes how SHA1 usage changes the CVSS scoring. Valid values: `riskier`, `neutral`, `safer`, `unknown`. |
| `value`        | boolean | **Path:** `@risk_details.is_using_sha1.value`True if SHA1 is used in a weak hash; false otherwise.                                                            |

{% /collapsible-section %}

{% collapsible-section #rule %}
### Rule

Describes how to discover a vulnerability. Vulnerability findings with rules mean the vulnerability was detected in source code or running code. Rules are also used for non-vulnerability findings such as misconfigurations or API security.

| Attribute name    | Type    | Description                                                                                                                |
| ----------------- | ------- | -------------------------------------------------------------------------------------------------------------------------- |
| `type`            | string  | **Path:** `@rule.type`Type of the rule that generated the finding.                                                         |
| `name`            | string  | **Path:** `@rule.name`Name of the rule that generated the finding.                                                         |
| `id`              | string  | **Path:** `@rule.id`Identifier of the rule that generated the finding.                                                     |
| `version`         | integer | **Path:** `@rule.version`Version of the rule that generated the finding.                                                   |
| `default_rule_id` | string  | **Path:** `@rule.default_rule_id`Default rule identifier of the rule. Custom rules will not have default rule identifiers. |

{% /collapsible-section %}

{% collapsible-section #advisory %}
### Advisory

Ties a vulnerability to a set of specific software versions. Vulnerability findings with advisories mean a vulnerable version of the software was detected (typically through SBOMs).

| Attribute name | Type           | Description                                                                                                                                                                                                   |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | string         | **Path:** `@advisory.id`Internal identifier for the advisory.                                                                                                                                                 |
| `cve`          | string         | **Path:** `@advisory.cve`Primary globally recognized identifier for a security vulnerability, following the `CVE-YYYY-NNNN` format.                                                                           |
| `aliases`      | array (string) | **Path:** `@advisory.aliases`Contains additional identifiers referring to the same vulnerability, created by other entities.                                                                                  |
| `published_at` | integer        | **Path:** `@advisory.published_at`Timestamp in milliseconds (UTC) when the advisory was published.                                                                                                            |
| `modified_at`  | integer        | **Path:** `@advisory.modified_at`Timestamp in milliseconds (UTC) when the advisory was last updated.                                                                                                          |
| `summary`      | string         | **Path:** `@advisory.summary`Short summary of the advisory.                                                                                                                                                   |
| `type`         | string         | **Path:** `@advisory.type`Specifies the type of the advisory. Valid values: `component_with_known_vulnerability`, `unmaintained`, `end_of_life`, `dangerous_workflows`, `risky_license`, `malicious_package`. |

{% /collapsible-section %}

{% collapsible-section #vulnerability %}
### Vulnerability

Contains information specific to vulnerabilities.

| Attribute name      | Type            | Description                                                                                                                                                                         |
| ------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cwes`              | array (string)  | **Path:** `@vulnerability.cwes`CWE (Common Weakness Enumeration) identifier associated with this vulnerability. Each entry must use the `CWE-<id>` format (for example, `CWE-416`). |
| `hash`              | string          | **Path:** `@vulnerability.hash`Vulnerability hash used to correlate the same vulnerability across SCA (Software Composition Analysis) runtime and static analysis.                  |
| `first_commit`      | string          | **Path:** `@vulnerability.first_commit`Identifies the commit in which this vulnerability was first introduced.                                                                      |
| `last_commit`       | string          | **Path:** `@vulnerability.last_commit`Identifies the commit in which this vulnerability was fixed.                                                                                  |
| `owasp_top10_years` | array (integer) | **Path:** `@vulnerability.owasp_top10_years`Indicates the years the vulnerability appeared in the OWASP Top 10 list of critical vulnerabilities.                                    |
| `confidence`        | string          | **Path:** `@vulnerability.confidence`Assesses the likelihood of the vulnerability being a true positive. Possible values: `low`, `high`, `not_evaluated`.                           |
| `confidence_reason` | string          | **Path:** `@vulnerability.confidence_reason`Provides the rationale behind the assigned confidence level.                                                                            |
| `is_emerging`       | boolean         | **Path:** `@vulnerability.is_emerging`True if this vulnerability is classified as an emerging threat; false otherwise.                                                              |
| `stack`             | object          | **Path:** `@vulnerability.stack`Specifies the technological stack where the vulnerability was found.                                                                                |

### Stack{% #stack %}

Specifies the technological stack where the vulnerability was found.

| Attribute name | Type   | Description                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `language`     | string | **Path:** `@vulnerability.stack.language`Specifies the language where the vulnerability was found.                                                                                                                                                                                                                                             |
| `ecosystem`    | string | **Path:** `@vulnerability.stack.ecosystem`Indicates the package management ecosystem or source registry from which the vulnerable component originates. Possible values: `pypi`, `maven`, `nuget`, `npm`, `rubygems`, `go`, `packagist`, `deb`, `rpm`, `apk`, `windows`, `macos`, `oci`, `generic`, `bottlerocket`, `conan`, `crates`, `none`. |

{% /collapsible-section %}

{% collapsible-section #remediation %}
### Remediation

Groups information about the finding's remediation.

| Attribute name     | Type    | Description                                                                                                                                                                                                       |
| ------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `codegen`          | object  | **Path:** `@remediation.codegen`Tracks finding status for the code generation platform.                                                                                                                           |
| `is_available`     | boolean | **Path:** `@remediation.is_available`True if a remediation is currently available for this finding; false otherwise.                                                                                              |
| `description`      | string  | **Path:** `@remediation.description`Description of the remediation.                                                                                                                                               |
| `recommended_type` | string  | **Path:** `@remediation.recommended_type`Indicates the recommended remediation type for this finding. Possible values: `package`, `host_image`, `container_image`, `code_update`, `microsoft_kb`, `root_package`. |
| `recommended`      | object  | **Path:** `@remediation.recommended`Contains the recommended remediation.                                                                                                                                         |
| `package`          | object  | **Path:** `@remediation.package`Groups remediation package information.                                                                                                                                           |
| `root_package`     | object  | **Path:** `@remediation.root_package`Groups remediation root package information.                                                                                                                                 |
| `host_image`       | object  | **Path:** `@remediation.host_image`Contains remediation suggesting the latest host image version that may remediate the vulnerability.                                                                            |
| `container_image`  | object  | **Path:** `@remediation.container_image`Contains remediation suggesting a newer container image version that may remediate the vulnerability.                                                                     |
| `code_update`      | object  | **Path:** `@remediation.code_update`                                                                                                                                                                              |
| `microsoft_kb`     | object  | **Path:** `@remediation.microsoft_kb`Contains remediation strategy using a Microsoft Knowledge Base (KB) article.                                                                                                 |

### Codegen{% #codegen %}

Tracks finding status for the code generation platform.

| Attribute name | Type   | Description                                                                                                                                                                                                                                                                                                                                                          |
| -------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status`       | string | **Path:** `@remediation.codegen.status`Status of the automated fix generation. Valid values: `generated`, `not_available_non_default_branch`, `not_available_unsupported_tool`, `not_available_unsupported_rule`, `not_available_confidence_low`, `not_available_disabled`, `not_available_git_provider_not_supported`, `not_available_confidence_too_low`, `error`. |
| `id`           | string | **Path:** `@remediation.codegen.id`Identifier used to track the remediation in the code generation backend.                                                                                                                                                                                                                                                          |

### Package{% #package %}

Groups remediation package information.

| Attribute name               | Type           | Description                                                                                                                                                             |
| ---------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `latest_no_critical`         | array (object) | **Path:** `@remediation.package.latest_no_critical`Contains remediation suggesting the latest package version with no critical vulnerabilities (based on base score).   |
| `closest_no_critical`        | array (object) | **Path:** `@remediation.package.closest_no_critical`Contains remediation suggesting the closest package version with no critical vulnerabilities (based on base score). |
| `latest_no_vulnerabilities`  | array (object) | **Path:** `@remediation.package.latest_no_vulnerabilities`Contains remediation suggesting the latest package version with no vulnerabilities.                           |
| `closest_no_vulnerabilities` | array (object) | **Path:** `@remediation.package.closest_no_vulnerabilities`Contains remediation suggesting the closest package version with no vulnerabilities.                         |
| `base`                       | array (object) | **Path:** `@remediation.package.base`                                                                                                                                   |

### Root Package{% #root-package %}

Groups remediation root package information.

| Attribute name               | Type           | Description                                                                                                                                                                  |
| ---------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `latest_no_critical`         | array (object) | **Path:** `@remediation.root_package.latest_no_critical`Contains remediation suggesting the latest package version with no critical vulnerabilities (based on base score).   |
| `closest_no_critical`        | array (object) | **Path:** `@remediation.root_package.closest_no_critical`Contains remediation suggesting the closest package version with no critical vulnerabilities (based on base score). |
| `latest_no_vulnerabilities`  | array (object) | **Path:** `@remediation.root_package.latest_no_vulnerabilities`Contains remediation suggesting the latest package version with no vulnerabilities.                           |
| `closest_no_vulnerabilities` | array (object) | **Path:** `@remediation.root_package.closest_no_vulnerabilities`Contains remediation suggesting the closest package version with no vulnerabilities.                         |
| `base`                       | array (object) | **Path:** `@remediation.root_package.base`                                                                                                                                   |

### Host Image{% #host-image %}

Contains remediation suggesting the latest host image version that may remediate the vulnerability.

| Attribute name | Type   | Description                                                                                                                                            |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `latest_major` | object | **Path:** `@remediation.host_image.latest_major`Contains information about the latest Amazon Machine Image (AMI) that may remediate the vulnerability. |

#### Latest Major{% #latest-major %}

Contains information about the latest Amazon Machine Image (AMI) that may remediate the vulnerability.

| Attribute name | Type   | Description                                                                                                                                                      |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | string | **Path:** `@remediation.host_image.latest_major.name`Name of the latest Amazon Machine Image (for example, `ami-12345678`) that may remediate the vulnerability. |

### Container Image{% #container-image %}

Contains remediation suggesting a newer container image version that may remediate the vulnerability.

| Attribute name               | Type   | Description                                                                                                                                                                                |
| ---------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `closest_no_vulnerabilities` | object | **Path:** `@remediation.container_image.closest_no_vulnerabilities`Contains remediation suggesting to upgrade the container image to a newer version that may remediate the vulnerability. |

#### Closest No Vulnerabilities{% #closest-no-vulnerabilities %}

Contains remediation suggesting to upgrade the container image to a newer version that may remediate the vulnerability.

| Attribute name  | Type           | Description                                                                                                                                                                        |
| --------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `layer_digests` | array (string) | **Path:** `@remediation.container_image.closest_no_vulnerabilities.layer_digests`Contains the layer digests of the currently vulnerable container image that needs to be upgraded. |
| `image_url`     | string         | **Path:** `@remediation.container_image.closest_no_vulnerabilities.image_url`URL of the container image that may remediate the vulnerability.                                      |
| `name`          | string         | **Path:** `@remediation.container_image.closest_no_vulnerabilities.name`Name of the container image that may remediate the vulnerability.                                          |
| `tag`           | string         | **Path:** `@remediation.container_image.closest_no_vulnerabilities.tag`Tag of the container image that may remediate the vulnerability.                                            |

### Code Update{% #code-update %}

| Attribute name | Type           | Description                                                                                         |
| -------------- | -------------- | --------------------------------------------------------------------------------------------------- |
| `edits`        | array (object) | **Path:** `@remediation.code_update.edits`Lists the code changes required to remediate the finding. |

### Microsoft Kb{% #microsoft-kb %}

Contains remediation strategy using a Microsoft Knowledge Base (KB) article.

| Attribute name         | Type   | Description                                                                                                                      |
| ---------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `closest_fix_advisory` | object | **Path:** `@remediation.microsoft_kb.closest_fix_advisory`Specifies the closest patch available to address the current advisory. |

#### Closest Fix Advisory{% #closest-fix-advisory %}

Specifies the closest patch available to address the current advisory.

| Attribute name | Type   | Description                                                                                           |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| `article`      | string | **Path:** `@remediation.microsoft_kb.closest_fix_advisory.article`Article name for the closest patch. |

{% /collapsible-section %}

{% collapsible-section #compliance %}
### Compliance

Contains information specific to compliance findings, such as compliance rule or evaluation (pass/fail).

| Attribute name                   | Type           | Description                                                                                                                                                 |
| -------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `evaluation`                     | string         | **Path:** `@compliance.evaluation`Compliance evaluation result. Valid values: `pass` (resource is properly configured), `fail` (resource is misconfigured). |
| `frameworks`                     | array (object) | **Path:** `@compliance.frameworks`Lists the compliance frameworks mapped to this finding.                                                                   |
| `framework_requirements`         | array (string) | **Path:** `@compliance.framework_requirements`Lists the requirements within the compliance framework that this finding relates to.                          |
| `framework_requirement_controls` | array (string) | **Path:** `@compliance.framework_requirement_controls`Lists the controls within the framework requirement that this finding maps to.                        |

{% /collapsible-section %}

{% collapsible-section #cloud-resource %}
### Cloud Resource

Groups attributes identifying the cloud resource affected by the finding.

| Attribute name               | Type           | Description                                                                                                                                             |
| ---------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tags`                       | array (string) | **Path:** `@cloud_resource.tags`Lists tags applied to the cloud resource.                                                                               |
| `category`                   | string         | **Path:** `@cloud_resource.category`Category the resource type belongs to.                                                                              |
| `key`                        | string         | **Path:** `@cloud_resource.key`Canonical Cloud Resource Identifier (CCRID).                                                                             |
| `cloud_provider_url`         | string         | **Path:** `@cloud_resource.cloud_provider_url`Link to the resource in the cloud provider console.                                                       |
| `cloud_provider`             | string         | **Path:** `@cloud_resource.cloud_provider`Indicates the cloud provider hosting the resource. Valid values: `aws`, `azure`, `gcp`, `oci`.                |
| `configuration`              | object         | **Path:** `@cloud_resource.configuration`Configuration of the cloud resource, as returned by the cloud provider.                                        |
| `context`                    | object         | **Path:** `@cloud_resource.context`Context for the cloud resource.                                                                                      |
| `account`                    | string         | **Path:** `@cloud_resource.account`Cloud account that owns the cloud resource (for example, AWS account, Azure subscription, GCP project, OCI tenancy). |
| `display_name`               | string         | **Path:** `@cloud_resource.display_name`Display name of the resource.                                                                                   |
| `region`                     | string         | **Path:** `@cloud_resource.region`Cloud region where the resource is located.                                                                           |
| `public_accessibility_paths` | array (string) | **Path:** `@cloud_resource.public_accessibility_paths`Describes the network paths through which the resource is accessible from the public internet.    |
| `public_port_ranges`         | array (object) | **Path:** `@cloud_resource.public_port_ranges`List of port ranges on the resource that are exposed to the public internet.                              |

{% /collapsible-section %}

{% collapsible-section #iac-resource %}
### Iac Resource

Groups attributes identifying the Infrastructure as Code (IaC) resource related to the finding.

| Attribute name | Type   | Description                                                                                                                                                                                                                            |
| -------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `provider`     | string | **Path:** `@iac_resource.provider`Indicates the IaC (Infrastructure as Code) provider where the resource is defined (for example, `aws`, `gcp`, `azure`). Possible values: `aws`, `gcp`, `azure`.                                      |
| `platform`     | string | **Path:** `@iac_resource.platform`Indicates which IaC (Infrastructure as Code) platform the vulnerability was found on (for example, `terraform`, `kubernetes`). Possible values: `cicd`, `terraform`, `kubernetes`, `cloudformation`. |

{% /collapsible-section %}

{% collapsible-section #k8s %}
### K8S

Contains Kubernetes fields for findings generated against Kubernetes resources.

| Attribute name | Type   | Description                                               |
| -------------- | ------ | --------------------------------------------------------- |
| `cluster_id`   | string | **Path:** `@k8s.cluster_id`Kubernetes cluster identifier. |

{% /collapsible-section %}

{% collapsible-section #host %}
### Host

Contains host information.

| Attribute name   | Type   | Description                                                                                                        |
| ---------------- | ------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`           | string | **Path:** `@host.name`Host name.                                                                                   |
| `key`            | string | **Path:** `@host.key`Canonical Cloud Resource Identifier (CCRID).                                                  |
| `cloud_provider` | string | **Path:** `@host.cloud_provider`Cloud provider the host belongs to. Possible values: `aws`, `azure`, `gcp`, `oci`. |
| `image`          | string | **Path:** `@host.image`Name of the host image used to build the host (for example, `ami-1234`).                    |
| `os`             | object | **Path:** `@host.os`Groups attributes of the operating system running on the host.                                 |

### Os{% #os %}

Groups attributes of the operating system running on the host.

| Attribute name | Type   | Description                                           |
| -------------- | ------ | ----------------------------------------------------- |
| `name`         | string | **Path:** `@host.os.name`Operating system name.       |
| `version`      | string | **Path:** `@host.os.version`Operating system version. |

{% /collapsible-section %}

{% collapsible-section #service %}
### Service

| Attribute name       | Type   | Description                                                                                                                                                                        |
| -------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`               | string | **Path:** `@service.name`Name of the service where this finding was detected.                                                                                                      |
| `git_commit_sha`     | string | **Path:** `@service.git_commit_sha`Git commit SHA of the latest commit where this finding was detected for the service. Available only when Source Code Integration is configured. |
| `git_repository_url` | string | **Path:** `@service.git_repository_url`URL of the Git repository for the service associated with this finding. Available only when Source Code Integration is configured.          |

{% /collapsible-section %}

{% collapsible-section #container-image %}
### Container Image

| Attribute name         | Type           | Description                                                                                                                                                                         |
| ---------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `registries`           | array (string) | **Path:** `@container_image.registries`Indicates the container registry where the image is stored or from which it was pulled.                                                      |
| `repository`           | string         | **Path:** `@container_image.repository`Repository of the container image.                                                                                                           |
| `repo_digests`         | array (string) | **Path:** `@container_image.repo_digests`Repository digests of the container image where this finding was detected.                                                                 |
| `git_repository_url`   | string         | **Path:** `@container_image.git_repository_url`URL of the Git repository for the code used to build the container image. Available only when Source Code Integration is configured. |
| `oses`                 | array (object) | **Path:** `@container_image.oses`Operating systems associated with the container image.                                                                                             |
| `architectures`        | array (string) | **Path:** `@container_image.architectures`Architectures associated with the container image.                                                                                        |
| `image_layer_digests`  | array (string) | **Path:** `@container_image.image_layer_digests`                                                                                                                                    |
| `image_layer_diff_ids` | array (string) | **Path:** `@container_image.image_layer_diff_ids`                                                                                                                                   |
| `name`                 | string         | **Path:** `@container_image.name`Full name of the container image.                                                                                                                  |
| `tags`                 | array (string) | **Path:** `@container_image.tags`Tag part of the container image name (for example, `latest` or `1.2.3`).                                                                           |

{% /collapsible-section %}

{% collapsible-section #git %}
### Git

Contains Git metadata linking a finding to source code context. Includes information about the repository, branch, commit, author, and committer.

| Attribute name          | Type           | Description                                                                                                                                               |
| ----------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `repository_id`         | string         | **Path:** `@git.repository_id`Normalized identifier of the Git repository.                                                                                |
| `repository_url`        | string         | **Path:** `@git.repository_url`Git repository URL related to the finding.                                                                                 |
| `repository_visibility` | string         | **Path:** `@git.repository_visibility`Indicates the visibility of the repository. Valid values: `public`, `private`, `not_detected`.                      |
| `branch`                | string         | **Path:** `@git.branch`Name of the Git branch related to the finding.                                                                                     |
| `default_branch`        | string         | **Path:** `@git.default_branch`Default branch defined for the Git repository.                                                                             |
| `is_default_branch`     | boolean        | **Path:** `@git.is_default_branch`True if the current branch is the default branch for the repository; false otherwise.                                   |
| `sha`                   | string         | **Path:** `@git.sha`Git commit identifier (SHA).                                                                                                          |
| `author`                | object         | **Path:** `@git.author`Contains details about the author of the commit.                                                                                   |
| `committer`             | object         | **Path:** `@git.committer`Contains details about the committer.                                                                                           |
| `codeowners`            | array (string) | **Path:** `@git.codeowners`Includes code owner teams extracted from the SCM (Source Control Management) provider's CODEOWNERS file (for example, GitHub). |

### Author{% #author %}

Contains details about the author of the commit.

| Attribute name | Type    | Description                                                                                             |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `name`         | string  | **Path:** `@git.author.name`Name of the commit author.                                                  |
| `email`        | string  | **Path:** `@git.author.email`Email address of the commit author.                                        |
| `authored_at`  | integer | **Path:** `@git.author.authored_at`Timestamp in milliseconds (UTC) when the original changes were made. |

### Committer{% #committer %}

Contains details about the committer.

| Attribute name | Type    | Description                                                                                                                                                                 |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | string  | **Path:** `@git.committer.name`Name of the committer.                                                                                                                       |
| `email`        | string  | **Path:** `@git.committer.email`Email address of the committer.                                                                                                             |
| `committed_at` | integer | **Path:** `@git.committer.committed_at`Timestamp in milliseconds (UTC) when the changes were last significantly modified (for example, during a rebase or amend operation). |

{% /collapsible-section %}

{% collapsible-section #code-location %}
### Code Location

Groups attributes pinpointing the specific file and line numbers where the finding is located.

| Attribute name | Type    | Description                                                                                                                  |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `filename`     | string  | **Path:** `@code_location.filename`Name of the file where the root parent package version is declared.                       |
| `line_start`   | integer | **Path:** `@code_location.line_start`Line number where the root parent package version declaration starts in the file.       |
| `column_start` | integer | **Path:** `@code_location.column_start`Column position where the root parent package version declaration starts on the line. |
| `line_end`     | integer | **Path:** `@code_location.line_end`Line number where the root parent package version declaration ends in the file.           |
| `column_end`   | integer | **Path:** `@code_location.column_end`Column position where the root parent package version declaration ends on the line.     |
| `is_test_file` | boolean | **Path:** `@code_location.is_test_file`True if the code file is a test file; false otherwise.                                |
| `url`          | string  | **Path:** `@code_location.url`URL to view the file online (for example, in GitHub), highlighting the code location.          |
| `symbol`       | string  | **Path:** `@code_location.symbol`                                                                                            |

{% /collapsible-section %}

{% collapsible-section #package %}
### Package

Contains package manager information. A package manager automates the installation, upgrading, configuration, and removal of software packages.

| Attribute name             | Type           | Description                                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                     | string         | **Path:** `@package.name`Name of the package or library where the vulnerability was identified.                                                                                                                                                                                                                                                      |
| `version`                  | string         | **Path:** `@package.version`Version of the package or library where the vulnerability was identified.                                                                                                                                                                                                                                                |
| `additional_names`         | array (string) | **Path:** `@package.additional_names`List of affected package names when a cloud vulnerability impacts multiple packages derived from the same source package.                                                                                                                                                                                       |
| `normalized_name`          | string         | **Path:** `@package.normalized_name`Normalized name according to the ecosystem of the package or library where the vulnerability was identified.                                                                                                                                                                                                     |
| `manager`                  | string         | **Path:** `@package.manager`Indicates the package management ecosystem or source registry from which the vulnerable component originates. Possible values: `maven`, `gradle`, `npm`, `yarn`, `pnpm`, `requirements`, `pipfile`, `pdm`, `poetry`, `nuget`, `bundler`, `golang`, `composer`, `crates`, `conan`, `hex`, `pub`, `renv`, `uv`, `unknown`. |
| `dependency_type`          | string         | **Path:** `@package.dependency_type`Indicates whether this package is a direct dependency, transitive dependency, or not supported if the information cannot be retrieved. Possible values: `direct`, `transitive`, `not_supported`.                                                                                                                 |
| `loading_type`             | string         | **Path:** `@package.loading_type`Indicates if the component is always loaded and running (`hot`), running infrequently (`cold`), or loaded on demand (`lazy`). Possible values: `hot`, `cold`, `lazy`.                                                                                                                                               |
| `dependency_location_text` | string         | **Path:** `@package.dependency_location_text`                                                                                                                                                                                                                                                                                                        |
| `declaration`              | object         | **Path:** `@package.declaration`Contains code locations of the package definition.                                                                                                                                                                                                                                                                   |
| `scope`                    | string         | **Path:** `@package.scope`Indicates the intended usage scope of the package (`production` or `development`). Possible values: `production`, `development`.                                                                                                                                                                                           |
| `root_parents`             | array (object) | **Path:** `@package.root_parents`Contains a list of the dependencies for which this package is a transitive dependency.                                                                                                                                                                                                                              |

### Declaration{% #declaration %}

Contains code locations of the package definition.

| Attribute name | Type   | Description                                                                                                             |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| `block`        | object | **Path:** `@package.declaration.block`Contains the location of the code that declares the whole dependency declaration. |
| `name`         | object | **Path:** `@package.declaration.name`Contains the location of the code that declares the dependency name.               |
| `version`      | object | **Path:** `@package.declaration.version`Version declared for the root parent.                                           |

#### Block{% #block %}

Contains the location of the code that declares the whole dependency declaration.

| Attribute name | Type    | Description                                                                                                                              |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `filename`     | string  | **Path:** `@package.declaration.block.filename`Name of the file where the root parent package version is declared.                       |
| `line_start`   | integer | **Path:** `@package.declaration.block.line_start`Line number where the root parent package version declaration starts in the file.       |
| `column_start` | integer | **Path:** `@package.declaration.block.column_start`Column position where the root parent package version declaration starts on the line. |
| `line_end`     | integer | **Path:** `@package.declaration.block.line_end`Line number where the root parent package version declaration ends in the file.           |
| `column_end`   | integer | **Path:** `@package.declaration.block.column_end`Column position where the root parent package version declaration ends on the line.     |
| `is_test_file` | boolean | **Path:** `@package.declaration.block.is_test_file`True if the code file is a test file; false otherwise.                                |
| `url`          | string  | **Path:** `@package.declaration.block.url`URL to view the file online (for example, in GitHub), highlighting the code location.          |
| `symbol`       | string  | **Path:** `@package.declaration.block.symbol`                                                                                            |

#### Name{% #name %}

Contains the location of the code that declares the dependency name.

| Attribute name | Type    | Description                                                                                                                             |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `filename`     | string  | **Path:** `@package.declaration.name.filename`Name of the file where the root parent package version is declared.                       |
| `line_start`   | integer | **Path:** `@package.declaration.name.line_start`Line number where the root parent package version declaration starts in the file.       |
| `column_start` | integer | **Path:** `@package.declaration.name.column_start`Column position where the root parent package version declaration starts on the line. |
| `line_end`     | integer | **Path:** `@package.declaration.name.line_end`Line number where the root parent package version declaration ends in the file.           |
| `column_end`   | integer | **Path:** `@package.declaration.name.column_end`Column position where the root parent package version declaration ends on the line.     |
| `is_test_file` | boolean | **Path:** `@package.declaration.name.is_test_file`True if the code file is a test file; false otherwise.                                |
| `url`          | string  | **Path:** `@package.declaration.name.url`URL to view the file online (for example, in GitHub), highlighting the code location.          |
| `symbol`       | string  | **Path:** `@package.declaration.name.symbol`                                                                                            |

#### Version{% #version %}

Version declared for the root parent.

| Attribute name | Type    | Description                                                                                                                                |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `filename`     | string  | **Path:** `@package.declaration.version.filename`Name of the file where the root parent package version is declared.                       |
| `line_start`   | integer | **Path:** `@package.declaration.version.line_start`Line number where the root parent package version declaration starts in the file.       |
| `column_start` | integer | **Path:** `@package.declaration.version.column_start`Column position where the root parent package version declaration starts on the line. |
| `line_end`     | integer | **Path:** `@package.declaration.version.line_end`Line number where the root parent package version declaration ends in the file.           |
| `column_end`   | integer | **Path:** `@package.declaration.version.column_end`Column position where the root parent package version declaration ends on the line.     |
| `is_test_file` | boolean | **Path:** `@package.declaration.version.is_test_file`True if the code file is a test file; false otherwise.                                |
| `url`          | string  | **Path:** `@package.declaration.version.url`URL to view the file online (for example, in GitHub), highlighting the code location.          |
| `symbol`       | string  | **Path:** `@package.declaration.version.symbol`                                                                                            |

{% /collapsible-section %}

{% collapsible-section #secret %}
### Secret

| Attribute name      | Type   | Description                                                                                                                                                                               |
| ------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `validation_status` | string | **Path:** `@secret.validation_status`Result of attempting to validate if the secret is active. Possible values: `valid`, `invalid`, `not_validated`, `validation_error`, `not_available`. |

{% /collapsible-section %}

{% collapsible-section #api-endpoint %}
### Api Endpoint

Contains the HTTP endpoint representation.

| Attribute name   | Type   | Description                                                                                                                  |
| ---------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `operation_name` | string | **Path:** `@api_endpoint.operation_name`Name of the entry point into a service (for example, `http.request`, `grpc.server`). |
| `path`           | string | **Path:** `@api_endpoint.path`Relative path of the endpoint.                                                                 |
| `method`         | string | **Path:** `@api_endpoint.method`Method of the endpoint (HTTP verb or gRPC method).                                           |
| `resource_name`  | string | **Path:** `@api_endpoint.resource_name`Internal identification of the endpoint in the format `{method} {path}`.              |

{% /collapsible-section %}

## Tags{% #tags %}

Key-value metadata in the format `name:value`. Enables flexible filtering and grouping of findings. Must include at least `source` and `origin`.

## Further reading{% #further-reading %}

- [Cloud Security Management](https://docs.datadoghq.com/security/cloud_security_management/)
- [Code Security](https://docs.datadoghq.com/security/code_security/)
- [Application Security](https://docs.datadoghq.com/security/application_security/)
