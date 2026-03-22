# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/linkedin/posts.md

# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/instagram/posts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Posts API

> Collect and discover Instagram posts from post URLs or public profiles.

The Posts API allows you to collect and discover Instagram posts from individual post URLs or public profile URLs.

***

### Collect by URL

This endpoint allows users to collect detailed data from a single Instagram post by providing the post URL.

#### Input Parameters

<ParamField path="URL" type="string" required>
  The Instagram post URL.
</ParamField>

#### Output Structure

Includes detailed post, profile, and media data.

**Post details**

* `post_id`
* `description`
* `hashtags`
* `date_posted`
* `num_comments`
* `likes`
* `content_type`
* `video_view_count`
* `video_play_count`
* and more

> For the full list of fields,\
> [View complete output reference](https://brightdata.com/cp/scrapers/gd_lk5ns7kz21pck8jpis?tab=overview)

**Page and profile details**

* `user_posted`
* `followers`
* `posts_count`
* `profile_image_link`
* `is_verified`
* `profile_url`

> We provide a limited set of data points about the profile.

**Attachments and media**

* `photos`
* `videos`
* `thumbnail`
* `display_url` (link only, not the file itself)
* `audio`

***

### Discover by URL

This endpoint allows users to discover recent Instagram posts from a public profile by providing the profile URL and optional filtering parameters.

#### Input Parameters

<ParamField path="URL" type="string" required>
  The Instagram profile URL.
</ParamField>

<ParamField path="num_of_posts" type="number">
  The number of recent posts to collect. If omitted, there is no limit.
</ParamField>

<ParamField path="posts_to_not_include" type="array">
  Array of post IDs to exclude from the results.
</ParamField>

<ParamField path="start_date" type="string">
  Start date for filtering posts in MM-DD-YYYY format (must be earlier than `end_date`).
</ParamField>

<ParamField path="end_date" type="string">
  End date for filtering posts in MM-DD-YYYY format (must be later than `start_date`).
</ParamField>

<ParamField path="post_type" type="string">
  Specify the type of posts to collect (for example, `post` or `reel`).
</ParamField>

#### Output Structure

Includes detailed post, profile, and media information.

**Post details**

* `post_id`
* `description`
* `hashtags`
* `date_posted`
* `num_comments`
* `likes`
* `video_view_count`
* `video_play_count`
* and more

> For the full list of fields,\
> [View complete output reference](https://brightdata.com/cp/scrapers/gd_lk5ns7kz21pck8jpis/url?tab=overview)

**Page and profile details**

* `user_posted`
* `followers`
* `posts_count`
* `profile_image_link`
* `is_verified`
* `profile_url`
* `is_paid_partnership`
* `partnership_details`
* `user_posted_id`

**Attachments and media**

* `photos`
* `videos`
* `thumbnail`
* `audio`
* `display_url`
* `content_type`
* `product_type`
* `coauthor_producers`
* `tagged_users`

This endpoint supports advanced post discovery using filters, exclusions, and post type selection, making it suitable for analytics and large-scale data collection.


## OpenAPI

````yaml cn-web-scraper-ide-rest-api POST /posts/collect
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
  /posts/collect:
    post:
      tags:
        - Instagram Posts
      summary: Collect Instagram post by URL
      description: >-
        Collect detailed information from a single Instagram post, including
        engagement metrics, media, and profile metadata.
      operationId: collectInstagramPost
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PostCollectRequest'
            example:
              url: https://www.instagram.com/p/POST_ID/
      responses:
        '200':
          description: Post data collected successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PostCollectResponse'
              example:
                post_id: POST_ID
                description: Exploring the world 🌍
                hashtags:
                  - travel
                  - nature
                date_posted: '2024-01-10'
                num_comments: 542
                likes: 10234
                content_type: image
                video_view_count: null
                video_play_count: null
                user_posted: natgeo
                followers: 282000000
                profile_url: https://www.instagram.com/natgeo/
                profile_image_link: https://instagram.fxyz1-1.fna.fbcdn.net/profile.jpg
                photos:
                  - https://cdn.instagram.com/photo1.jpg
                videos: []
                thumbnail: https://cdn.instagram.com/thumb.jpg
                display_url: https://instagram.com/p/POST_ID/
                audio: null
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
            curl -X POST "https://api.brightdata.com/posts/collect" \
              -H "Authorization: Bearer YOUR_API_TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"url":"https://www.instagram.com/p/POST_ID/"}'
        - lang: JavaScript
          source: |-
            fetch("https://api.brightdata.com/posts/collect", {
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

            url = "https://api.brightdata.com/posts/collect"
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
              .uri(URI.create("https://api.brightdata.com/posts/collect"))
              .header("Authorization", "Bearer YOUR_API_TOKEN")
              .header("Content-Type", "application/json")
              .POST(HttpRequest.BodyPublishers.ofString(body))
              .build();
            HttpResponse<String> response = client.send(request,
            HttpResponse.BodyHandlers.ofString());

            System.out.println(response.body());
        - lang: Ruby
          source: >-
            require 'net/http'

            require 'json'


            uri = URI('https://api.brightdata.com/posts/collect')

            req = Net::HTTP::Post.new(uri)

            req['Authorization'] = 'Bearer YOUR_API_TOKEN'

            req['Content-Type'] = 'application/json'

            req.body = { url: 'https://www.instagram.com/p/POST_ID/' }.to_json


            res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do
            |http|
              http.request(req)
            end


            puts res.body
        - lang: Go
          source: >-
            client := &http.Client{}

            body :=
            strings.NewReader(`{"url":"https://www.instagram.com/p/POST_ID/"}`)

            req, _ := http.NewRequest("POST",
            "https://api.brightdata.com/posts/collect", body)

            req.Header.Add("Authorization", "Bearer YOUR_API_TOKEN")

            req.Header.Add("Content-Type", "application/json")

            res, _ := client.Do(req)

            defer res.Body.Close()

            b, _ := io.ReadAll(res.Body)

            fmt.Println(string(b))
components:
  schemas:
    PostCollectRequest:
      type: object
      required:
        - url
      properties:
        url:
          type: string
          format: uri
          description: Instagram post URL
    PostCollectResponse:
      type: object
      properties:
        post_id:
          type: string
        description:
          type: string
        hashtags:
          type: array
          items:
            type: string
        date_posted:
          type: string
        num_comments:
          type: integer
        likes:
          type: integer
        content_type:
          type: string
        video_view_count:
          type: integer
          nullable: true
        video_play_count:
          type: integer
          nullable: true
        user_posted:
          type: string
        followers:
          type: integer
        profile_url:
          type: string
        profile_image_link:
          type: string
        photos:
          type: array
          items:
            type: string
        videos:
          type: array
          items:
            type: string
        thumbnail:
          type: string
        display_url:
          type: string
        audio:
          type: string
          nullable: true
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