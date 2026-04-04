# Source: https://docs.jit.io/docs/scanners-rule-configuration.md

# Scanners Rule Configuration

# Default Rules

Jit's SAST scanner uses **Semgrep** to detect security vulnerabilities in your code. Jit ships a curated ruleset sourced from the [Semgrep community rule registry](https://semgrep.dev/r), covering the most impactful security patterns across all supported languages. You can browse the full registry to see what rules are available.

**Current Semgrep version:** 1.109.0

**Supported languages:**

| Language                |
| ----------------------- |
| Python                  |
| Java                    |
| JavaScript / TypeScript |
| Kotlin                  |
| Scala                   |
| C#                      |
| Swift                   |
| Rust                    |
| PHP                     |
| Ruby                    |
| C / C++                 |
| YAML                    |
| Bash                    |

**Severity:** Jit surfaces **HIGH** and **MEDIUM** severity findings. INFO-level findings are not shown.

| Semgrep severity | Jit severity |
| ---------------- | ------------ |
| ERROR            | HIGH         |
| WARNING          | MEDIUM       |
| INFO             | Not shown    |

***

## Customizing Your Configuration

You can extend the default ruleset with your own Semgrep rules. Custom rules run alongside Jit's defaults - they don't replace them.

### Using the UI editor

From the Jit platform, go to **Settings → Security Tools** and open the **Semgrep** configuration editor.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1cc9499a9e3a4c93ec8cb7d943067e7e911d3289dbabc348f049306d2dbc3338-Screenshot_2026-02-22_at_12.39.00.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Enter your rules in standard [Semgrep rule syntax](https://semgrep.dev/docs/writing-rules/rule-syntax) and save. You can also upload a pre-configured file from the same page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/78d608e10ff697cb515c749f15602d0ecdec3174789267432fc4d646e853d4b7-Screenshot_2026-02-22_at_13.04.54.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/59e5d650fba7fcfd5ad1fedf237d20bce25f5a4cc0de6f6377b91ed46c408083-Screenshot_2026-02-22_at_13.05.48.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Changes take effect on the next scan.

***

## Semgrep Pro

If your organization has a Semgrep Pro subscription, you can use it in Jit instead of the default scanner for deeper inter-procedural and taint analysis. See [Semgrep Pro Tier Integration](https://docs.jit.io/docs/integrating-with-semgrep-pro).