tenable::types
# Struct Asset 
Source 

```
pub struct Asset {}
```

## Fields§
§`id: Option<String>`

The UUID of the asset. Use this value as the unique key for the asset.
§`has_agent: Option<bool>`

A value specifying whether a Nessus agent scan detected the asset (`true`).
§`last_seen: Option<String>`

The ISO timestamp of the scan that most recently detected the asset.
§`last_scan_target: Option<String>`

The IPv4 address, IPv6 address, or FQDN that the scanner last used to evaluate the asset.
§`sources: Option<Vec<Source>>`

The sources of the scans that identified the asset.
§`acr_score: Option<i32>`

The Asset Criticality Rating (ACR) for the asset. With Lumin, Tenable assigns an ACR to each asset on your network to represent the asset’s relative risk as an integer from 1 to 10. For more information, see Lumin Metrics in the *Tenable.io Vulnerability Management User Guide*.  This attribute is only present if you have a Lumin license.
§`acr_drivers: Option<Vec<AcrDriver>>`

The key drivers that Tenable uses to calculate an asset’s Tenable-provided ACR. For more information, see Lumin Metrics in the *Tenable.io Vulnerability Management User Guide*.  This attribute is only present if you have a Lumin license.
§`exposure_score: Option<i32>`

The Asset Exposure Score (AES) for the asset. For more information, see Lumin Metrics in the *Tenable.io Vulnerability Management User Guide*.  This attribute is only present if you have a Lumin license.
§`scan_frequency: Option<Vec<ScanFrequency>>`

Information about how often scans ran against the asset during specified intervals. This attribute is only present if you have a Lumin license.
§`ipv4: Option<Vec<String>>`

A list of IPv4 addresses for the asset.
§`ipv6: Option<Vec<String>>`

A list of IPv6 addresses for the asset.
§`fqdn: Option<Vec<String>>`

A list of fully-qualified domain names (FQDNs) for the asset.
§`netbios_name: Option<Vec<String>>`

The NetBIOS name for the asset.
§`operating_system: Option<Vec<String>>`

The operating systems that scans have associated with the asset record.
§`agent_name: Option<Vec<String>>`

The names of any Nessus agents that scanned and identified the asset.
§`aws_ec2_name: Option<Vec<String>>`

The name of the virtual machine instance in AWS EC2.
§`mac_address: Option<Vec<String>>`

A list of MAC addresses for the asset.

## Trait Implementations§