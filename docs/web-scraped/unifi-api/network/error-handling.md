# error-handling

Source: https://developer.ui.com/network/v10.1.68/error-handling

UniFi APIEndpoints combined into Ansible Modules for customized workflows.Overview
This API uses a standard error response structure across all endpoints. When an error occurs, the API returns an error object with detailed information to help you identify and resolve the issue.
Error Response Structure
All error responses follow this schema:
FieldTypeFormatDescriptionExamplestatusCodeintegerint32HTTP status code400statusNamestring-HTTP status name"UNAUTHORIZED"codestring-API-specific error code for programmatic handling"api.authentication.missing-credentials"messagestring-Human-readable error message"Missing credentials"timestampstringdate-timeISO 8601 timestamp when the error occurred"2024-11-27T08:13:46.966Z"requestPathstring-The API endpoint path that was requested"/integration/v1/sites/123"requestIdstringuuidUnique identifier for tracking the request. For Internal Server Errors (statusCode = 500), this ID can be used to track down the error in server logs"3fa85f64-5717-4562-b3fc-2c963f66afa6"
Example Error Response
{  "statusCode": 400,  "statusName": "UNAUTHORIZED",  "code": "api.authentication.missing-credentials",  "message": "Missing credentials",  "timestamp": "2024-11-27T08:13:46.966Z",  "requestPath": "/integration/v1/sites/123",  "requestId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}
Using Error Information
Programmatic Error Handling
Use the code field to handle specific error scenarios in your application:
if (error.code === 'api.authentication.missing-credentials') {  // Redirect user to login} else if (error.code === 'api.rate-limit.exceeded') {  // Implement retry logic}
Troubleshooting Server Errors
For Internal Server Errors (statusCode: 500), include the requestId when contacting support. This UUID allows the support team to locate the specific error in server logs for faster resolution.
Error Context
The requestPath and timestamp fields provide context about when and where the error occurred, which is useful for debugging and monitoring.