# Source: https://docs.safetycli.com/safety-docs/firewall/using-firewall/firewall-policy-management.md

# Firewall Policy Management

### Understanding Firewall Policies

Policies define how Safety Firewall responds when users attempt to install packages. You can configure policies to:

* Warn users about vulnerabilities
* Block installation of vulnerable or malicious packages
* Apply different rules based on vulnerability severity
* Set organization-wide or codebase-specific policies

### Policy Hierarchy

Safety Firewall policies follow a hierarchical structure:

1. **Organization Policies**: Apply to all users and codebases
2. **Codebase Policies**: Specific to individual codebases, override organization policies
3. **Default Policies**: Applied when no specific policies are defined

{% hint style="info" %}
More specific policies always override more general policies. For example, a codebase policy takes precedence over an organization policy.
{% endhint %}

### Default Policies

Safety Firewall includes sensible default policies out of the box:

* **Installation**: Warns on all vulnerability severities
* **Scanning**: Reports all vulnerabilities regardless of severity
* **Malicious Packages**: Blocks known malicious packages

### Accessing Policy Management

To manage policies:

1. Log in to Safety Platform at [platform.safetycli.com](https://platform.safetycli.com)
2. Navigate to "Organization" → "Policies" for organization-wide policies
3. Navigate to a specific codebase and select the "Policies" tab for codebase-specific policies

{% hint style="warning" %}
**IMPORTANT:** the visual Policy Builder wizard in Safety Platform does not yet support Firewall policies. Until this is supported, you must select the **Advanced Configuration** option on the policy configuration page.
{% endhint %}

### Policy Structure and Syntax

Safety Firewall policies use a JSON structure with specific rules for allowing and denying packages or vulnerabilities.

#### Basic Policy Structure

{% code overflow="wrap" %}

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "allow": {
      // Allow rules
    },
    "deny": {
      // Deny rules
    }
  }
}
```

{% endcode %}

{% hint style="info" %}
The `default-action` determines what happens when no specific rule matches. We recommend keeping this as `"allow"` and defining specific denial rules for vulnerabilities and packages.
{% endhint %}

### Configuring Allow and Deny Rules

#### Allow Rules

Allow rules specify packages or vulnerabilities that should be explicitly permitted:

```json
"allow": {
  "packages": [
    {
      "ecosystem": "pip",
      "specifications": [
        "boto3==2.14",
        "django>=2.0",
        "flask>=1.0",
        "jinja2~=2.0"
      ]
    }
  ],
  "vulnerabilities": {
    "59901": {
      "reason": "We are not impacted by this vulnerability",
      "expires": "2024-03-15"
    },
    "62044": {
      "reason": "No upstream python images provide updated pip yet",
      "expires": "2024-06-01"
    }
  }
}
```

{% hint style="info" %}
Allow rules for vulnerabilities are helpful for temporarily ignoring specific vulnerabilities that don't affect your application or can't be remediated immediately. Always include an expiration date to ensure these exceptions are revisited.
{% endhint %}

#### Deny Rules

Deny rules specify packages or vulnerabilities that should trigger warnings or blocks:

```json
"deny": {
  "packages": {
    "warning-on-any-of": {
      "age-below": "3 months",
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "safety"
          ]
        }
      ]
    },
    "block-on-any-of": {
      "age-below": "1 month",
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "safety"
          ]
        }
      ]
    }
  },
  "vulnerabilities": {
    "warning-on-any-of": {
      "cvss-severity": [
        "critical",
        "high"
      ]
    },
    "block-on-any-of": {
      "cvss-severity": [
        "critical"
      ]
    }
  }
}
```

### Complete Policy Example

Here's a complete policy example that:

* Allows specific package versions
* Exempts specific vulnerabilities with explanations
* Warns on packages less than 3 months old and on critical/high vulnerabilities
* Blocks packages less than 1 month old and packages with critical vulnerabilities

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "allow": {
      "packages": [
        {
          "ecosystem": "pip",
          "specifications": [
            "boto3==2.14",
            "django>=2.0",
            "flask>=1.0",
            "jinja2~=2.0"
          ]
        }
      ],
      "vulnerabilities": {
        "59901": {
          "reason": "We are not impacted by this vulnerability",
          "expires": "2024-03-15"
        },
        "62044": {
          "reason": "No upstream python images provide updated pip yet",
          "expires": "2024-06-01"
        }
      }
    },
    "deny": {
      "packages": {
        "warning-on-any-of": {
          "age-below": "3 months",
          "packages": [
            {
              "ecosystem": "pip",
              "specifications": [
                "safety"
              ]
            }
          ]
        },
        "block-on-any-of": {
          "age-below": "1 month",
          "packages": [
            {
              "ecosystem": "pip",
              "specifications": [
                "safety"
              ]
            }
          ]
        }
      },
      "vulnerabilities": {
        "warning-on-any-of": {
          "cvss-severity": [
            "critical",
            "high"
          ]
        },
        "block-on-any-of": {
          "cvss-severity": [
            "critical"
          ]
        }
      }
    }
  }
}
```

{% hint style="info" %}
When defining package specifications, you can use the same version specifiers as in requirements.txt files: exact versions (`==`), minimum versions (`>=`), compatible releases (`~=`), etc.
{% endhint %}

### Common Policy Patterns

#### Basic Security Policy

Warn on high severity vulnerabilities, block critical ones:

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "deny": {
      "vulnerabilities": {
        "warning-on-any-of": {
          "cvss-severity": [
            "high"
          ]
        },
        "block-on-any-of": {
          "cvss-severity": [
            "critical"
          ]
        }
      }
    }
  }
}
```

#### New Package Caution

Warn about packages that are less than 3 months old:

```json
{
  "installation": {
    "default-action": "allow",
    "audit-logging": {
      "enabled": true
    },
    "deny": {
      "packages": {
        "warning-on-any-of": {
          "age-below": "3 months"
        }
      }
    }
  }
}
```

### Best Practices for Policy Management

* **Start Permissive**: Begin with warning-only policies to minimize disruption
* **Gradually Increase Restrictions**: Tighten policies as your team becomes familiar with Safety Firewall
* **Communicate Changes**: Inform your team before implementing blocking policies
* **Add Documentation**: Use the `"reason"` field to document why exceptions are being made
* **Set Expirations**: Always include an `"expires"` date for vulnerability exceptions
* **Monitor Impact**: Watch the Firewall logs to see how policies affect your team's workflow

{% hint style="info" %}
Blocking policies can disrupt developer workflows. Before implementing blocking policies, start with warnings and communicate the planned changes to your team.
{% endhint %}
