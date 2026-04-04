# Jobs | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/ai_search/subresources/instances/subresources/jobs

[API Reference][AI Search][Instances]
# Jobs

##### [List Jobs]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs
##### [Create new job]
POST/accounts/{account_id}/ai-search/instances/{id}/jobs
##### [Get a Job Details]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}
##### [List Job Logs]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}/logs
##### ModelsExpand Collapse
JobListResponse  { id, source, description, 4 more } id: string[]source: "user" or "schedule"One of the following:"user"[]"schedule"[][]description: optional string[]end_reason: optional string[]ended_at: optional string[]last_seen_at: optional string[]started_at: optional string[][]JobCreateResponse  { id, source, description, 4 more } id: string[]source: "user" or "schedule"One of the following:"user"[]"schedule"[][]description: optional string[]end_reason: optional string[]ended_at: optional string[]last_seen_at: optional string[]started_at: optional string[][]JobGetResponse  { id, source, description, 4 more } id: string[]source: "user" or "schedule"One of the following:"user"[]"schedule"[][]description: optional string[]end_reason: optional string[]ended_at: optional string[]last_seen_at: optional string[]started_at: optional string[][]JobLogsResponse = array of  { id, created_at, message, message_type } id: number[]created_at: number[]message: string[]message_type: number[][]