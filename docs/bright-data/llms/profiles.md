# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/linkedin/profiles.md

# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/instagram/profiles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Profiles API

> Collect detailed information about Instagram profiles using the profile URL.

The Profiles API allows you to collect detailed information about Instagram profiles using the profile URL.

***

### Collect by URL

This endpoint allows users to collect comprehensive data from an Instagram profile, including business information, engagement metrics, posts, and user details.

#### Input Parameters

<ParamField path="URL" type="string" required>
  The Instagram profile URL.
</ParamField>

#### Output Structure

Includes detailed profile, engagement, and account data.

**Page and profile details**

* `account`
* `id`
* `followers`
* `posts_count`
* `is_business_account`
* `is_professional_account`
* `is_verified`
* `avg_engagement`
* `profile_name`
* `profile_url`
* `profile_image_link`
* and more

> For the full list of fields,\
> [View complete output reference](https://brightdata.com/cp/scrapers/gd_l1vikfch901nx3by4?tab=overview)

This endpoint provides a complete snapshot of an Instagram profile, making it suitable for profile analysis, engagement tracking, and account insights.


## OpenAPI

````yaml cn-web-scraper-ide-rest-api POST /profiles/collect
openapi: 3.0.3
info:
  title: Web Scraper IDE REST API
  description: >-
    APIs for scraping and collecting structured data from web sources including
    social media platforms.
  version: 1.0.0
servers:
  - url: https://api.brightdata.com
security:
  - bearerAuth: []
tags:
  - name: Instagram
    description: Instagram scraping endpoints
paths:
  /profiles/collect:
    post:
      tags:
        - Instagram
      summary: Collect Instagram profile by URL
      description: >-
        Collect comprehensive data from a public Instagram profile including
        account metadata and engagement metrics.
      operationId: collectInstagramProfile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProfileCollectRequest'
            example:
              url: https://www.instagram.com/natgeo/
      responses:
        '200':
          description: Profile data collected successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProfileCollectResponse'
              example:
                account: natgeo
                id: '1234567890'
                followers: 282000000
                posts_count: 29000
                is_business_account: true
                is_professional_account: true
                is_verified: true
                avg_engagement: 0.021
                profile_name: National Geographic
                profile_url: https://www.instagram.com/natgeo/
                profile_image_link: https://instagram.fxyz1-1.fna.fbcdn.net/profile.jpg
        '400':
          description: Bad Request – invalid input
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Invalid input
                message: The provided Instagram profile URL is not valid.
        '401':
          description: Unauthorized – invalid or missing API token
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Unauthorized
                message: Invalid or missing API token.
      x-codeSamples:
        - lang: curl
          source: |-
            curl -X POST "https://api.brightdata.com/profiles/collect" \
              -H "Authorization: Bearer YOUR_API_TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"url":"https://www.instagram.com/natgeo/"}'
        - lang: JavaScript
          source: |-
            fetch("https://api.brightdata.com/profiles/collect", {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_TOKEN",
                "Content-Type": "application/json"
              },
              body: JSON.stringify({ url: "https://www.instagram.com/natgeo/" })
            })
            .then(res => res.json())
            .then(data => console.log(data));
        - lang: Python
          source: |-
            import requests

            url = "https://api.brightdata.com/profiles/collect"
            headers = {
              "Authorization": "Bearer YOUR_API_TOKEN",
              "Content-Type": "application/json"
            }
            payload = {"url": "https://www.instagram.com/natgeo/"}

            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
        - lang: Java
          source: >-
            HttpClient client = HttpClient.newHttpClient();

            String body = "{\"url\":\"https://www.instagram.com/natgeo/\"}";

            HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://api.brightdata.com/profiles/collect"))
              .header("Authorization", "Bearer YOUR_API_TOKEN")
              .header("Content-Type", "application/json")
              .POST(HttpRequest.BodyPublishers.ofString(body))
              .build();
            HttpResponse<String> response = client.send(request,
            HttpResponse.BodyHandlers.ofString());

            System.out.println(response.body());
        - lang: Go
          source: >-
            client := &http.Client{}

            body :=
            strings.NewReader(`{"url":"https://www.instagram.com/natgeo/"}`)

            req, _ := http.NewRequest("POST",
            "https://api.brightdata.com/profiles/collect", body)

            req.Header.Add("Authorization", "Bearer YOUR_API_TOKEN")

            req.Header.Add("Content-Type", "application/json")

            res, _ := client.Do(req)

            defer res.Body.Close()

            b, _ := io.ReadAll(res.Body)

            fmt.Println(string(b))
components:
  schemas:
    ProfileCollectRequest:
      type: object
      required:
        - url
      properties:
        url:
          type: string
          format: uri
          description: Instagram profile URL
    ProfileCollectResponse:
      type: object
      properties:
        account:
          type: string
        id:
          type: string
        followers:
          type: integer
        posts_count:
          type: integer
        is_business_account:
          type: boolean
        is_professional_account:
          type: boolean
        is_verified:
          type: boolean
        avg_engagement:
          type: number
        profile_name:
          type: string
        profile_url:
          type: string
        profile_image_link:
          type: string
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````