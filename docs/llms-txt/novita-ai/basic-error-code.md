# Source: https://novita.ai/docs/api-reference/basic-error-code.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API Error Codes

## Image / Video / Audio

<table class="table table-big">
  <thead>
    <tr>
      <th>Error Name</th>
      <th>Status Code</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>INVALID\_REQUEST\_BODY</td>
      <td>400</td>
      <td>Request parameter validation failed</td>
    </tr>

    <tr>
      <td>IMAGE\_FILE\_EXCEEDS\_MAX\_SIZE</td>
      <td>400</td>
      <td>Image size exceeds limit</td>
    </tr>

    <tr>
      <td>INVALID\_IMAGE\_FORMAT</td>
      <td>400</td>
      <td>Image format does not meet requirements</td>
    </tr>

    <tr>
      <td>IMAGE\_EXCEEDS\_MAX\_RESOLUTION</td>
      <td>400</td>
      <td>Image resolution exceeds limit</td>
    </tr>

    <tr>
      <td>INVALID\_IMAGE\_SIZE</td>
      <td>400</td>
      <td>Image width or height exceeds limit</td>
    </tr>

    <tr>
      <td>API\_NOT\_FOUND</td>
      <td>404</td>
      <td>API not found</td>
    </tr>

    <tr>
      <td>IMAGE\_NO\_FACE\_DETECTED</td>
      <td>400</td>
      <td>No face detected</td>
    </tr>

    <tr>
      <td>INVALID\_CUSTOM\_OUTPUT\_PATH</td>
      <td>400</td>
      <td>Invalid OSS path</td>
    </tr>

    <tr>
      <td>ILLEGAL\_PROMPT</td>
      <td>400</td>
      <td>Prompt contains inappropriate content</td>
    </tr>

    <tr>
      <td>ILLEGAL\_IMAGE\_CONTENT</td>
      <td>400</td>
      <td>Image contains inappropriate content</td>
    </tr>

    <tr>
      <td>INVALID\_AUDIO\_FILE</td>
      <td>400</td>
      <td>Invalid audio input</td>
    </tr>

    <tr>
      <td>BILLING\_FAILED</td>
      <td>500</td>
      <td>Billing service error</td>
    </tr>

    <tr>
      <td>BILLING\_AUTH\_FAILED</td>
      <td>403</td>
      <td>Billing service authentication failed</td>
    </tr>

    <tr>
      <td>BILLING\_BALANCE\_NOT\_ENOUGH</td>
      <td>400</td>
      <td>Insufficient balance</td>
    </tr>

    <tr>
      <td>MISSING\_API\_KEY</td>
      <td>400</td>
      <td>API Key not provided</td>
    </tr>

    <tr>
      <td>INVALID\_API\_KEY</td>
      <td>403</td>
      <td>API Key validation failed</td>
    </tr>

    <tr>
      <td>FEATURE\_NOT\_ALLOWED</td>
      <td>403</td>
      <td>No permission to upload model</td>
    </tr>

    <tr>
      <td>API\_NOT\_ALLOWED</td>
      <td>403</td>
      <td>No permission to use this API</td>
    </tr>

    <tr>
      <td>RATE\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>Rate limit exceeded</td>
    </tr>

    <tr>
      <td>NEED\_REAL\_NAME\_VERIFY</td>
      <td>403</td>
      <td>Enterprise verification not completed</td>
    </tr>

    <tr>
      <td>CREATE\_TASK\_FAILED</td>
      <td>500</td>
      <td>Failed to create task</td>
    </tr>

    <tr>
      <td>TASK\_NOT\_FOUND</td>
      <td>404</td>
      <td>Task not found</td>
    </tr>

    <tr>
      <td>GET\_RESULT\_FAILED</td>
      <td>500</td>
      <td>Failed to get task result</td>
    </tr>

    <tr>
      <td>TASK\_FAILED</td>
      <td>500</td>
      <td>Task execution failed</td>
    </tr>
  </tbody>
</table>

## LLM

<table class="table table-big">
  <thead>
    <tr>
      <th>Error Name</th>
      <th>Status Code</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>INVALID\_API\_KEY</td>
      <td>403</td>
      <td>API Key not provided</td>
    </tr>

    <tr>
      <td>MODEL\_NOT\_FOUND</td>
      <td>404</td>
      <td>Model not found</td>
    </tr>

    <tr>
      <td>FAILED\_TO\_AUTH</td>
      <td>401</td>
      <td>Authentication failed</td>
    </tr>

    <tr>
      <td>NOT\_ENOUGH\_BALANCE</td>
      <td>403</td>
      <td>Insufficient balance</td>
    </tr>

    <tr>
      <td>INVALID\_REQUEST\_BODY</td>
      <td>400</td>
      <td>Request body format error, see message for details</td>
    </tr>

    <tr>
      <td>RATE\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>Too many requests, please try again later</td>
    </tr>

    <tr>
      <td>TOKEN\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>Token limit exceeded, please try again later</td>
    </tr>

    <tr>
      <td>SERVICE\_NOT\_AVAILABLE</td>
      <td>503</td>
      <td>Service unavailable</td>
    </tr>

    <tr>
      <td>ACCESS\_DENY</td>
      <td>403</td>
      <td>Access denied</td>
    </tr>
  </tbody>
</table>

## GPU

<table class="table table-big">
  <thead>
    <tr>
      <th>Error Name</th>
      <th>Status Code</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>UNKNOWN</td>
      <td>500</td>
      <td>Unknown error</td>
    </tr>

    <tr>
      <td>GET\_TOKEN\_FAILED</td>
      <td>400</td>
      <td>Failed to obtain token</td>
    </tr>

    <tr>
      <td>FORBIDDEN</td>
      <td>403</td>
      <td>Access forbidden / No permission</td>
    </tr>

    <tr>
      <td>UNAUTHORIZED</td>
      <td>401</td>
      <td>Unauthorized</td>
    </tr>

    <tr>
      <td>USER\_ALREADY\_EXISTS</td>
      <td>400</td>
      <td>User already exists</td>
    </tr>

    <tr>
      <td>INVALID\_USER\_OR\_PASSWORD</td>
      <td>400</td>
      <td>Invalid username or password</td>
    </tr>

    <tr>
      <td>INVALID\_CODE</td>
      <td>400</td>
      <td>Invalid verification code</td>
    </tr>

    <tr>
      <td>USER\_NOT\_FOUND</td>
      <td>400</td>
      <td>User not found</td>
    </tr>

    <tr>
      <td>USER\_PHONE\_NOT\_CONSIST</td>
      <td>400</td>
      <td>User phone number mismatch</td>
    </tr>

    <tr>
      <td>SEND\_CODE\_TOO\_FAST</td>
      <td>429</td>
      <td>Verification code sent too frequently</td>
    </tr>

    <tr>
      <td>INVALID\_PUBLIC\_KEY</td>
      <td>400</td>
      <td>Invalid public key</td>
    </tr>

    <tr>
      <td>USER\_NOT\_ACTIVATED</td>
      <td>400</td>
      <td>User not activated</td>
    </tr>

    <tr>
      <td>USER\_ALREADY\_ACTIVATED</td>
      <td>400</td>
      <td>User already activated</td>
    </tr>

    <tr>
      <td>INVALID\_USER\_TOKEN</td>
      <td>400</td>
      <td>Invalid user token</td>
    </tr>

    <tr>
      <td>BANNED\_USER</td>
      <td>400</td>
      <td>Account has been banned</td>
    </tr>

    <tr>
      <td>RATE\_LIMIT\_EXCEEDED</td>
      <td>429</td>
      <td>Request rate limit exceeded</td>
    </tr>

    <tr>
      <td>RESOURCE\_NOT\_FOUND</td>
      <td>400</td>
      <td>Resource not found (e.g., container not found)</td>
    </tr>

    <tr>
      <td>CONFLICT</td>
      <td>400</td>
      <td>Conflict (e.g., container conflict)</td>
    </tr>

    <tr>
      <td>VALIDATOR\_PARAM</td>
      <td>400</td>
      <td>Parameter validation failed / Invalid parameter</td>
    </tr>

    <tr>
      <td>REQUEST</td>
      <td>400</td>
      <td>Request error</td>
    </tr>

    <tr>
      <td>OPERATION\_LIMIT</td>
      <td>400</td>
      <td>Operation limit reached</td>
    </tr>

    <tr>
      <td>INSUFFICIENT\_RESOURCE</td>
      <td>400</td>
      <td>Insufficient resources</td>
    </tr>

    <tr>
      <td>CLUSTER\_STATUS</td>
      <td>400</td>
      <td>Cluster status abnormal</td>
    </tr>

    <tr>
      <td>NODE\_STATUS</td>
      <td>400</td>
      <td>Node status abnormal</td>
    </tr>

    <tr>
      <td>DEPENDENT\_RESOURCE\_STATE</td>
      <td>400</td>
      <td>Dependent resource state abnormal</td>
    </tr>

    <tr>
      <td>PREPAID\_INSTANCE\_NOT\_SUPPORT\_RELEASE</td>
      <td>400</td>
      <td>Prepaid instance does not support release</td>
    </tr>

    <tr>
      <td>CREATING\_INSTANCE\_NOT\_SUPPORT\_RENEWAL</td>
      <td>400</td>
      <td>Instance in creation does not support renewal</td>
    </tr>

    <tr>
      <td>INSTANCE\_LOCAL\_STORAGE\_NOT\_FOUND</td>
      <td>400</td>
      <td>Instance local storage not found</td>
    </tr>

    <tr>
      <td>INVALID\_COMMAND\_PARAM</td>
      <td>400</td>
      <td>Invalid instance startup command parameter</td>
    </tr>

    <tr>
      <td>GPU\_SPEC\_USED</td>
      <td>400</td>
      <td>GPU specification already in use</td>
    </tr>

    <tr>
      <td>INCORRECT\_USER\_SYNCER\_REQUIRE\_PARAMS</td>
      <td>400</td>
      <td>Incorrect user syncer request parameters</td>
    </tr>

    <tr>
      <td>MIGRATE\_INSUFFICIENT\_RESOURCE</td>
      <td>400</td>
      <td>Insufficient resources for migration</td>
    </tr>

    <tr>
      <td>WALLET\_NOT\_FOUND</td>
      <td>500</td>
      <td>Wallet not found</td>
    </tr>

    <tr>
      <td>WALLET\_UNSUPPORT\_RECHARGE\_METHOD</td>
      <td>400</td>
      <td>Unsupported wallet recharge method</td>
    </tr>

    <tr>
      <td>BALANCE\_NOT\_ENOUGH</td>
      <td>400</td>
      <td>Insufficient balance</td>
    </tr>

    <tr>
      <td>UNSUPPORTED\_BILLING\_MODE</td>
      <td>400</td>
      <td>Unsupported billing mode</td>
    </tr>

    <tr>
      <td>EXPIRED\_OR\_BALANCE\_NOT\_ENOUGH</td>
      <td>400</td>
      <td>Expired or insufficient balance</td>
    </tr>

    <tr>
      <td>ORDER\_NOT\_FOUND</td>
      <td>400</td>
      <td>Order not found</td>
    </tr>

    <tr>
      <td>SAVING\_PLAN\_ALREADY\_EXISTS</td>
      <td>400</td>
      <td>Saving plan already exists</td>
    </tr>

    <tr>
      <td>CREATE\_INSTANCE\_LIMIT</td>
      <td>400</td>
      <td>Instance creation limit reached, please recharge or delete other instances</td>
    </tr>

    <tr>
      <td>NETWORK\_STORAGE\_TOO\_LARGE</td>
      <td>400</td>
      <td>Network storage size exceeds limit</td>
    </tr>

    <tr>
      <td>CUR\_CLUSTER\_NETWORK\_STORAGE\_NOT\_SUPPORT</td>
      <td>400</td>
      <td>Network storage not supported in current region</td>
    </tr>

    <tr>
      <td>NETWORK\_STORAGE\_IN\_USE</td>
      <td>400</td>
      <td>Network storage is in use</td>
    </tr>

    <tr>
      <td>NETWORK\_STORAGE\_UNAVAILABLE</td>
      <td>400</td>
      <td>Network storage unavailable</td>
    </tr>

    <tr>
      <td>NETWORK\_STORAGE\_NOT\_FOUND</td>
      <td>400</td>
      <td>Network storage not found</td>
    </tr>

    <tr>
      <td>IMAGE\_NOT\_FOUND</td>
      <td>400</td>
      <td>Image not found</td>
    </tr>

    <tr>
      <td>IMAGE\_AUTH\_IN\_USE</td>
      <td>400</td>
      <td>Image authentication in use</td>
    </tr>

    <tr>
      <td>NETWORK\_NOT\_FOUND</td>
      <td>400</td>
      <td>Instance network not found</td>
    </tr>

    <tr>
      <td>NETWORK\_IN\_USE</td>
      <td>400</td>
      <td>Instance network in use</td>
    </tr>

    <tr>
      <td>NETWORK\_MAX\_LIMIT</td>
      <td>400</td>
      <td>Instance network creation limit exceeded</td>
    </tr>

    <tr>
      <td>SEND\_MSG\_ERROR</td>
      <td>400</td>
      <td>Message sending error</td>
    </tr>

    <tr>
      <td>JOB\_NOT\_FOUND</td>
      <td>400</td>
      <td>Instance job not found</td>
    </tr>

    <tr>
      <td>SERVERLESS\_ENDPOINT\_NOT\_FOUND</td>
      <td>400</td>
      <td>Serverless endpoint not found</td>
    </tr>

    <tr>
      <td>SERVERLESS\_WORKER\_NOT\_FOUND</td>
      <td>400</td>
      <td>Serverless worker not found</td>
    </tr>

    <tr>
      <td>SERVERLESS\_PRODUCT\_NOT\_FOUND</td>
      <td>400</td>
      <td>Serverless product not found</td>
    </tr>

    <tr>
      <td>SERVERLESS\_APP\_NAME\_IS\_EXIST</td>
      <td>400</td>
      <td>Serverless application name already exists</td>
    </tr>

    <tr>
      <td>TEMPLATE\_IS\_PRIVATE</td>
      <td>400</td>
      <td>Template is private</td>
    </tr>

    <tr>
      <td>TEMPLATE\_NOT\_FOUND</td>
      <td>400</td>
      <td>Template not found</td>
    </tr>
  </tbody>
</table>

## Billing

<table class="table table-big">
  <thead>
    <tr>
      <th>Error Name</th>
      <th>Status Code</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>UNKNOWN</td>
      <td>500</td>
      <td>Unknown error, please contact us</td>
    </tr>

    <tr>
      <td>LIST\_BILL\_TOO\_FAST</td>
      <td>429</td>
      <td>Requests are too frequent, please try again later</td>
    </tr>

    <tr>
      <td>INVALID\_PRODUCT\_CATEGORY</td>
      <td>400</td>
      <td>Invalid productCategory parameter</td>
    </tr>

    <tr>
      <td>INVALID\_BILL\_CYCLE</td>
      <td>400</td>
      <td>Invalid cycle parameter</td>
    </tr>

    <tr>
      <td>LIST\_BILL\_ERROR</td>
      <td>500</td>
      <td>Query error, please contact us</td>
    </tr>
  </tbody>
</table>


Built with [Mintlify](https://mintlify.com).