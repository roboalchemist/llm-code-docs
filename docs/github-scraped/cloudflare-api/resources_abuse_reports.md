# Abuse Reports | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/abuse_reports

[API Reference]
# Abuse Reports

##### [Submit an abuse report]
POST/accounts/{account_id}/abuse-reports/{report_param}
##### [Abuse Report Details]
GET/accounts/{account_id}/abuse-reports/{report_param}
##### [List abuse reports]
GET/accounts/{account_id}/abuse-reports
##### ModelsExpand Collapse
AbuseReportCreateResponse = string
The result should be ‘success’ for successful response
[]AbuseReportGetResponse  { id, cdate, domain, 7 more } id: string
Public facing ID of abuse report, aka abuse_rand.
[]cdate: string
Creation date of report. Time in RFC 3339 format ([https://www.rfc-editor.org/rfc/rfc3339.html])
[]domain: string
Domain that relates to the report.
[]mitigation_summary:  { accepted_url_count, active_count, external_host_notified, 2 more }
A summary of the mitigations related to this report.
accepted_url_count: number
How many of the reported URLs were confirmed as abusive.
[]active_count: number
How many mitigations are active.
[]external_host_notified: boolean
Whether the report has been forwarded to an external hosting provider.
[]in_review_count: number
How many mitigations are under review.
[]pending_count: number
How many mitigations are pending their effective date.
[][]status: "accepted" or "in_review"
An enum value that represents the status of an abuse record
One of the following:"accepted"[]"in_review"[][]type: "PHISH" or "GEN" or "THREAT" or 6 more
The abuse report type
One of the following:"PHISH"[]"GEN"[]"THREAT"[]"DMCA"[]"EMER"[]"TM"[]"REG_WHO"[]"NCSEI"[]"NETWORK"[][]justification: optional string
Justification for the report.
[]original_work: optional string
Original work / Targeted brand in the alleged abuse.
[]submitter: optional  { company, email, name, telephone }
Information about the submitter of the report.
company: optional string[]email: optional string[]name: optional string[]telephone: optional string[][]urls: optional array of string[][]AbuseReportListResponse  { reports } reports: array of  { id, cdate, domain, 7 more } id: string
Public facing ID of abuse report, aka abuse_rand.
[]cdate: string
Creation date of report. Time in RFC 3339 format ([https://www.rfc-editor.org/rfc/rfc3339.html])
[]domain: string
Domain that relates to the report.
[]mitigation_summary:  { accepted_url_count, active_count, external_host_notified, 2 more }
A summary of the mitigations related to this report.
accepted_url_count: number
How many of the reported URLs were confirmed as abusive.
[]active_count: number
How many mitigations are active.
[]external_host_notified: boolean
Whether the report has been forwarded to an external hosting provider.
[]in_review_count: number
How many mitigations are under review.
[]pending_count: number
How many mitigations are pending their effective date.
[][]status: "accepted" or "in_review"
An enum value that represents the status of an abuse record
One of the following:"accepted"[]"in_review"[][]type: "PHISH" or "GEN" or "THREAT" or 6 more
The abuse report type
One of the following:"PHISH"[]"GEN"[]"THREAT"[]"DMCA"[]"EMER"[]"TM"[]"REG_WHO"[]"NCSEI"[]"NETWORK"[][]justification: optional string
Justification for the report.
[]original_work: optional string
Original work / Targeted brand in the alleged abuse.
[]submitter: optional  { company, email, name, telephone }
Information about the submitter of the report.
company: optional string[]email: optional string[]name: optional string[]telephone: optional string[][]urls: optional array of string[][][]
#### Abuse ReportsMitigations

##### [List abuse report mitigations]
GET/accounts/{account_id}/abuse-reports/{report_id}/mitigations
##### [Request review on mitigations]
POST/accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal
##### ModelsExpand Collapse
MitigationListResponse  { mitigations } mitigations: array of  { id, effective_date, entity_id, 3 more } id: string
ID of remediation.
[]effective_date: string
Date when the mitigation will become active. Time in RFC 3339 format ([https://www.rfc-editor.org/rfc/rfc3339.html])
[]entity_id: string[]entity_type: "url_pattern" or "account" or "zone"One of the following:"url_pattern"[]"account"[]"zone"[][]status: "pending" or "active" or "in_review" or 2 more
The status of a mitigation
One of the following:"pending"[]"active"[]"in_review"[]"cancelled"[]"removed"[][]type: "legal_block" or "misleading_interstitial" or "phishing_interstitial" or 4 more
The type of mitigation
One of the following:"legal_block"[]"misleading_interstitial"[]"phishing_interstitial"[]"network_block"[]"rate_limit_cache"[]"account_suspend"[]"redirect_video_stream"[][][][]MitigationReviewResponse  { id, effective_date, entity_id, 3 more } id: string
ID of remediation.
[]effective_date: string
Date when the mitigation will become active. Time in RFC 3339 format ([https://www.rfc-editor.org/rfc/rfc3339.html])
[]entity_id: string[]entity_type: "url_pattern" or "account" or "zone"One of the following:"url_pattern"[]"account"[]"zone"[][]status: "pending" or "active" or "in_review" or 2 more
The status of a mitigation
One of the following:"pending"[]"active"[]"in_review"[]"cancelled"[]"removed"[][]type: "legal_block" or "misleading_interstitial" or "phishing_interstitial" or 4 more
The type of mitigation
One of the following:"legal_block"[]"misleading_interstitial"[]"phishing_interstitial"[]"network_block"[]"rate_limit_cache"[]"account_suspend"[]"redirect_video_stream"[][][]