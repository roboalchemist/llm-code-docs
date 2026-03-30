# Source: https://directus.io/docs/raw/guides/connect/errors.md

# Error Codes

> Learn about Directus error codes - understand what each code means, from validation failures to rate limits exceeded. Troubleshoot issues with your API requests and resolve errors efficiently.

Below are the global error codes used within Directus, and what they mean.

<table>
<thead>
  <tr>
    <th>
      Error Code
    </th>
    
    <th>
      Status
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        FAILED_VALIDATION
      </code>
    </td>
    
    <td>
      400
    </td>
    
    <td>
      Validation for this particular item failed.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        FORBIDDEN
      </code>
    </td>
    
    <td>
      403
    </td>
    
    <td>
      You are not allowed to do the current action.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_TOKEN
      </code>
    </td>
    
    <td>
      403
    </td>
    
    <td>
      Provided token is invalid.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        TOKEN_EXPIRED
      </code>
    </td>
    
    <td>
      401
    </td>
    
    <td>
      Provided token is valid but has expired.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_CREDENTIALS
      </code>
    </td>
    
    <td>
      401
    </td>
    
    <td>
      Username / password or access token is wrong.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_IP
      </code>
    </td>
    
    <td>
      401
    </td>
    
    <td>
      Your IP address isn't allow-listed to be used with this user.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_OTP
      </code>
    </td>
    
    <td>
      401
    </td>
    
    <td>
      Incorrect OTP was provided.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_PAYLOAD
      </code>
    </td>
    
    <td>
      400
    </td>
    
    <td>
      Provided payload is invalid.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        INVALID_QUERY
      </code>
    </td>
    
    <td>
      400
    </td>
    
    <td>
      The requested query parameters can not be used.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        UNSUPPORTED_MEDIA_TYPE
      </code>
    </td>
    
    <td>
      415
    </td>
    
    <td>
      Provided payload format or <code>
        Content-Type
      </code>
      
       header is unsupported.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        REQUESTS_EXCEEDED
      </code>
    </td>
    
    <td>
      429
    </td>
    
    <td>
      You have exceeded the rate limit.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ROUTE_NOT_FOUND
      </code>
    </td>
    
    <td>
      404
    </td>
    
    <td>
      Endpoint does not exist.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        SERVICE_UNAVAILABLE
      </code>
    </td>
    
    <td>
      503
    </td>
    
    <td>
      Could not use external service.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        UNPROCESSABLE_CONTENT
      </code>
    </td>
    
    <td>
      422
    </td>
    
    <td>
      You tried doing something illegal.
    </td>
  </tr>
</tbody>
</table>

To prevent revealing which items exist, all actions for non-existing items will return a `FORBIDDEN` error.
