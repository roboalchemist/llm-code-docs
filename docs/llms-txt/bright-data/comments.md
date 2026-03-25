# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/instagram/comments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Comments API

> Collect the latest comments from Instagram posts.

### Collect by URL

This API allows users to collect the latest comments from a specific Instagram post by providing the post URL.

<Note>
  This API retrieves the most recent 10 comments along with associated metadata.
</Note>

**Input Parameters**

<ParamField path="URL" type="string" required="true">
  The Instagram post URL.
</ParamField>

**Output Structure**

Includes comprehensive data points:

* **Comment details**
  * `comment_id`

  * `comment_user`

  * `comment_user_url`

  * `comment_date`

  * `comment`

  * `likes_number`

  * `replies_number`

  * `replies`

  * `hashtag_comment`

  * `tagged_users_in_comment`

  * and more
  > For all data points, [click here](https://brightdata.com/cp/scrapers/gd_ltppn085pokosxh13?tab=overview).

* **User details**
  * `user_name`

  * `user_id`

  * `user_url`
  > We provide a limited set of data points about the profile.

* **Post metadata**
  * `post_url`
  * `post_user`
  * `post_id`


## OpenAPI

````yaml cn-web-scraper-ide-rest-api POST /comments/collect
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
  /comments/collect:
    post:
      tags:
        - Instagram
      summary: Collect Instagram comments by post URL
      description: >-
        Collect the latest comments from a specific Instagram post. Returns the
        most recent 10 comments along with user and post metadata.
      operationId: collectInstagramComments
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CommentCollectRequest'
            example:
              url: https://www.instagram.com/p/POST_ID/
      responses:
        '200':
          description: Comments collected successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommentCollectResponse'
              example:
                post_id: POST_ID
                post_url: https://www.instagram.com/p/POST_ID/
                post_user: natgeo
                comments:
                  - comment_id: '17895695668004550'
                    comment_user: john_doe
                    comment_user_url: https://www.instagram.com/john_doe/
                    comment_date: '2024-01-12T10:45:00Z'
                    comment: Amazing shot 🔥
                    likes_number: 120
                    replies_number: 3
                    replies:
                      - reply_id: '17895695668009999'
                        reply_user: natgeo
                        reply: Thanks!
                    hashtag_comment:
                      - travel
                    tagged_users_in_comment:
                      - '@friend'
        '400':
          description: Bad Request – invalid post URL
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Invalid input
                message: The provided Instagram post URL is not valid.
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
            curl -X POST "https://api.brightdata.com/comments/collect" \
              -H "Authorization: Bearer YOUR_API_TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"url":"https://www.instagram.com/p/POST_ID/"}'
        - lang: JavaScript
          source: |-
            fetch("https://api.brightdata.com/comments/collect", {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_TOKEN",
                "Content-Type": "application/json"
              },
              body: JSON.stringify({ url: "https://www.instagram.com/p/POST_ID/" })
            })
            .then(res => res.json())
            .then(data => console.log(data));
        - lang: Python
          source: |-
            import requests

            url = "https://api.brightdata.com/comments/collect"
            headers = {
              "Authorization": "Bearer YOUR_API_TOKEN",
              "Content-Type": "application/json"
            }
            payload = {"url": "https://www.instagram.com/p/POST_ID/"}

            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
        - lang: Java
          source: >-
            HttpClient client = HttpClient.newHttpClient();

            String body = "{\"url\":\"https://www.instagram.com/p/POST_ID/\"}";

            HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://api.brightdata.com/comments/collect"))
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
            strings.NewReader(`{"url":"https://www.instagram.com/p/POST_ID/"}`)

            req, _ := http.NewRequest("POST",
            "https://api.brightdata.com/comments/collect", body)

            req.Header.Add("Authorization", "Bearer YOUR_API_TOKEN")

            req.Header.Add("Content-Type", "application/json")

            res, _ := client.Do(req)

            defer res.Body.Close()

            b, _ := io.ReadAll(res.Body)

            fmt.Println(string(b))
components:
  schemas:
    CommentCollectRequest:
      type: object
      required:
        - url
      properties:
        url:
          type: string
          format: uri
          description: Instagram post URL
    CommentCollectResponse:
      type: object
      properties:
        post_id:
          type: string
        post_url:
          type: string
        post_user:
          type: string
        comments:
          type: array
          items:
            type: object
            properties:
              comment_id:
                type: string
              comment_user:
                type: string
              comment_user_url:
                type: string
              comment_date:
                type: string
              comment:
                type: string
              likes_number:
                type: integer
              replies_number:
                type: integer
              replies:
                type: array
                items:
                  type: object
                  properties:
                    reply_id:
                      type: string
                    reply_user:
                      type: string
                    reply:
                      type: string
              hashtag_comment:
                type: array
                items:
                  type: string
              tagged_users_in_comment:
                type: array
                items:
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