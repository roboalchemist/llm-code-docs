# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.waf_acl.dataset.md

---
title: WAF ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WAF ACL
---

# WAF ACL

This table represents the WAF ACL resource from Amazon Web Services.

```
aws.waf_acl
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| default_action | core | json       | The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. The action is specified by the <a>WafAction</a> object.                                                                                                                                                                                                                                |
| metric_name    | core | string     | A friendly name or description for the metrics for this <code>WebACL</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change <code>MetricName</code> after you create the <code>WebACL</code>. |
| name           | core | string     | A friendly name or description of the <code>WebACL</code>. You can't change the name of a <code>WebACL</code> after you create it.                                                                                                                                                                                                                                                         |
| rules          | core | json       | An array that contains the action for each <code>Rule</code> in a <code>WebACL</code>, the priority of the <code>Rule</code>, and the ID of the <code>Rule</code>.                                                                                                                                                                                                                         |
| tags           | core | hstore_csv |
| web_acl_arn    | core | string     | Tha Amazon Resource Name (ARN) of the web ACL.                                                                                                                                                                                                                                                                                                                                             |
| web_acl_id     | core | string     | A unique identifier for a <code>WebACL</code>. You use <code>WebACLId</code> to get information about a <code>WebACL</code> (see <a>GetWebACL</a>), update a <code>WebACL</code> (see <a>UpdateWebACL</a>), and delete a <code>WebACL</code> from AWS WAF (see <a>DeleteWebACL</a>). <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.                   |
