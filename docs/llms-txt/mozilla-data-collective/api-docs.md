# Source: https://datacollective.mozillafoundation.org/api-reference/docs

#### Base URL 

All API requests should be made to the following base URL:

``` 
https://datacollective.mozillafoundation.org/api
```

#### Authentication 

All authenticated endpoints require an API key in the Authorization header:

``` 
Authorization: Bearer YOUR_API_KEY
```

You can create and manage your API keys in your [profile settings](/profile/credentials).

### API Endpoints 

[GET]`/datasets/:datasetId`

##### Get Dataset Details 

Retrieves the details of a specific dataset.

###### Authentication 

[Required]

Bearer token in Authorization header

###### Path Parameters 

`datasetId`

string

[Required]

The ID of the dataset

###### Success Response (200 OK) 

``` 
,
  "license": "CC0-1.0",
  "task": "ASR",
  "format": "MP3",
  "datasetUrl": "https://datacollective.mozillafoundation.org/datasets/dataset-1"
}
```

###### Error Responses 

[404]

Dataset not found

[403]

Access denied. Private dataset requires organization membership

[POST]`/datasets/:datasetId/download`

##### Create Download Session 

Creates a download session and returns a download token. The user must have previously agreed to the dataset\'s terms of use through the web interface.

###### Authentication 

[Required]

Bearer token in Authorization header

###### Path Parameters 

`datasetId`

string

[Required]

The ID of the dataset

###### Success Response (200 OK) 

``` 

```

###### Error Responses 

[403]

You must agree to the terms of use before downloading this dataset

[404]

Dataset not found

[401]

Authentication required

[429]

Rate limit exceeded

[GET]`/datasets/:datasetId/download/:downloadToken`

##### Download Dataset File 

Downloads the actual dataset file.

###### Authentication 

[Required]

Bearer token in Authorization header

###### Request Headers 

`Range`

string

[Optional]

Byte range for partial downloads e.g. \'Range: bytes=0-100\'

###### Path Parameters 

`datasetId`

string

[Required]

The ID of the dataset

`downloadToken`

string

[Required]

The temporary download token

###### Success Response (200 OK) 

Response Headers:

Content-Length: 268435456000

Content-Type: application/zip

Content-Disposition: attachment; filename=\"common-voice-corpus-22.zip\"

``` 
Binary file data
```

###### Success Response (206 Partial Content) 

Response Headers:

Content-Length: 100

Content-Type: application/zip

Content-Range: bytes 0-100/268435456000

Content-Disposition: attachment; filename=\"common-voice-corpus-22.zip\"

``` 
Partial binary file data
```

###### Error Responses 

[401]

Invalid or expired download token

[404]

Dataset or download session not found

[416]

Requested Range Not Satisfiable

[429]

Bandwidth limit exceeded

### Rate Limiting 

The API employs organization-level rate limiting to ensure fair usage and stability. Rate limits apply to both API requests and bandwidth consumption.

##### Request Rate Limiting 

When request limits are exceeded, the API responds with status code 429 and includes these headers:

`X-RateLimit-Limit`[Total requests allowed in current window]

`X-RateLimit-Remaining`[Requests remaining in current window]

`Retry-After`[Seconds until next request allowed]

##### Bandwidth Rate Limiting 

Download endpoints enforce bandwidth limits at the organization level. When exceeded, connections are terminated with a 429 error.

``` 

}
```

### Implementation Notes 

###### Single Use Downloads 

Each download token can only be used for one complete download session. Once a file is fully downloaded, the token is invalidated.

###### Proxied Downloads 

All downloads are proxied through the API server for real-time rate limiting, access control, and analytics tracking.

###### Terms Agreement Required 

Users must agree to dataset terms through the web interface before downloading. API-only terms agreement is not supported.

### Error Handling 

##### Common Error Responses 

[400]

###### Bad Request 

Malformed request or invalid parameters

``` 

}
```

[401]

###### Unauthorized 

Missing or invalid authentication

``` 

```

[429]

###### Too Many Requests 

Rate limit exceeded

``` 

```