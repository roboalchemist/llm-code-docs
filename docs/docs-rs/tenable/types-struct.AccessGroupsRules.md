tenable::types
# Struct AccessGroupsRules 
Source 

```
pub struct AccessGroupsRules {
    pub _type: Option<String>,
    pub operator: Option<String>,
    pub terms: Option<Vec<String>>,
}
```

## Fields§
§`_type: Option<String>`

The type of asset rule. The asset rule type corresponds to the type of data you can specify in the `terms` parameter. For a complete list of supported rule types, use the GET /access-groups/filters endpoint.
§`operator: Option<String>`

The operator that specifies how Tenable.io matches the terms value to asset data.   Possible operators include:   - eq—Tenable.io matches the rule to assets based on an exact match of the specified term. Note: Tenable.io interprets the operator as `equals` for ipv4 rules that specify a single IP address, but interprets the operator as `contains` for ipv4 rules that specify an IP range or CIDR range.  - match—Tenable.io matches the rule to assets based a partial match of the specified term.  - starts—Tenable.io matches the rule to assets that start with the specified term.  - ends—Tenable.io matches the rule to assets that end with the specified term.  For a complete list of operators by rule type, use the GET /access-groups/rules/filters endpoint.
§`terms: Option<Vec<String>>`

The values that Tenable.io uses to match an asset to the rule. A term must correspond to the rule type.  For example:  - If the rule type is `aws_account`, the term is an AWS account ID.  - If the rule type is `fqdn`, the term is a hostname or a fully-qualified domain name (FQDN).  - If the rule type is `ipv4`, the term is an individual IPv4 address, a range of IPv4 addresses (for example, 172.204.81.57-172.204.81.60), or a CIDR range (for example, 172.204.81.57/24).   For a complete list of supported values by rule type, use the GET /access-groups/rules/filters endpoint.    If you specify multiple terms values, Tenable.io includes an asset in the access group if the asset’s attributes match any of the terms in the rule. 
You can specify up to 100,000 terms per asset rule.

## Trait Implementations§