# Mitigations | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/abuse_reports/subresources/mitigations

[API Reference][Abuse Reports]
# Mitigations

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