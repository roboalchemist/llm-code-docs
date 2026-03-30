# Source: https://docs.jit.io/docs/regional-jit.md

# Jit's Support Regions

Jit now supports data residency and transfer across both the US and EU regions, ensuring organizations can meet compliance, privacy, and performance requirements based on their geographic and regulatory needs. You can choose where your data is stored and processed, providing greater control and alignment with regional data handling policies.

## Switching Between Regions

You can switch between regions through the login page or by accessing the region-specific URLs directly:

US Region: <https://platform.jit.io>\
EU Region: <https://platform.eu.jit.io>

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1993b3090acf542762f19fe178f907b173f573d807758d73f2655af366c8c7f1-regions.gif",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Regional Configuration Reference

Use this table to configure your integrations and tools for the correct regional infrastructure:

[block:parameters]
{
  "data": {
    "h-0": "Configuration",
    "h-1": "US Region",
    "h-2": "EU Region",
    "0-0": "Jit's Platform URL",
    "0-1": "<https://platform.jit.io>",
    "0-2": "<https://platform.eu.jit.io>",
    "1-0": "API base URL - Used for Jit's public APIs  \n<https://docs.jit.io/reference>",
    "1-1": "<https://api.jit.io>",
    "1-2": "<https://api.eu.jit.io>",
    "2-0": "IP Whitelists - DAST scanners (ZAP) +  \nCalls to cloud based SCMs",
    "2-1": "- 3.220.250.224/32\n- 52.45.232.22/32",
    "2-2": "- 18.198.245.94/32\n- 18.157.204.182/32",
    "3-0": "IP Whitelists - Splunk Cloud integration",
    "3-1": "- 18.205.92.162\n- 18.215.215.164\n- 34.225.59.94\n- 44.210.155.28\n- 52.45.12.206\n- 54.235.127.238",
    "3-2": "- 18.153.211.96\n- 35.158.48.176"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]

* Once you create an account in a specific region, your data remains within that region's infrastructure
* API tokens and configurations are region-specific and cannot be used across regions
* Make sure to use the correct base URLs when configuring integrations to avoid connection issues