# Detections | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/detections

[API Reference][Email Security][Investigate]
# Detections

##### [Get message detection details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/detections
##### ModelsExpand Collapse
DetectionGetResponse  { action, attachments, headers, 5 more } action: string[]attachments: array of  { size, content_type, detection, 2 more } size: numberminimum0[]content_type: optional string[]detection: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][]encrypted: optional boolean[]name: optional string[][]headers: array of  { name, value } name: string[]value: string[][]links: array of  { href, text } href: string[]text: optional string[][]sender_info:  { as_name, as_number, geo, 2 more } as_name: optional string
The name of the autonomous system.
[]as_number: optional number
The number of the autonomous system.
formatint64[]geo: optional string[]ip: optional string[]pld: optional string[][]threat_categories: array of  { id, description, name } id: numberformatint64[]description: optional string[]name: optional string[][]validation:  { comment, dkim, dmarc, spf } comment: optional string[]dkim: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]dmarc: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][]spf: optional "pass" or "neutral" or "fail" or 2 moreOne of the following:"pass"[]"neutral"[]"fail"[]"error"[]"none"[][][]final_disposition: optional "MALICIOUS" or "MALICIOUS-BEC" or "SUSPICIOUS" or 7 moreOne of the following:"MALICIOUS"[]"MALICIOUS-BEC"[]"SUSPICIOUS"[]"SPOOF"[]"SPAM"[]"BULK"[]"ENCRYPTED"[]"EXTERNAL"[]"UNKNOWN"[]"NONE"[][][]