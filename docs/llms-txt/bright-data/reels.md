# Source: https://docs.brightdata.com/api-reference/web-scraper-api/social-media-apis/instagram/reels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reels API

> Collect and discover Instagram Reels.

The Reels API allows you to collect and discover Instagram Reels from public profiles using reel URLs or search-based discovery.

***

### Collect by URL

This endpoint allows users to collect detailed data about an Instagram Reel by providing the reel URL.

#### Input Parameters

<ParamField path="URL" type="string" required>
  The Instagram reel URL.
</ParamField>

#### Output Structure

Includes detailed reel, profile, and media data.

**Reel details**

* `post_id`
* `description`
* `hashtags`
* `date_posted`
* `tagged_users`
* `num_comments`
* `likes`
* `views`
* `video_play_count`
* `length`
* and more

> For the full list of fields,\
> [View complete output reference](https://brightdata.com/cp/scrapers/gd_lyclm20il4r5helnj?tab=overview)

**Profile details**

* `user_posted`
* `followers`
* `posts_count`
* `profile_image_link`
* `is_verified`
* `profile_url`

> We provide a limited set of data points about the profile.

**Attachments and media**

* `video_url`
* `thumbnail`
* `audio_url`

***

> For the full list of fields,\
> [View complete output reference](https://brightdata.com/cp/scrapers/gd_lyclm20il4r5helnj/url?tab=overview)

**Profile details**

* `user_posted`
* `followers`
* `posts_count`
* `following`

**Attachments and media**

* `video_url`
* `thumbnail`
* `audio_url` (link only, not the file itself)

This endpoint supports advanced reel discovery using filtering, exclusions, and date ranges, making it suitable for analytics and content tracking use cases.


## OpenAPI

````yaml cn-web-scraper-ide-rest-api POST /reels/collect
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
  /reels/collect:
    post:
      tags:
        - Instagram
      summary: Collect Instagram Reel by URL
      description: Collect detailed data from a single Instagram Reel using the reel URL.
      operationId: collectInstagramReel
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ReelCollectRequest'
            example:
              url: https://www.instagram.com/reel/REEL_ID/
      responses:
        '200':
          description: Reel data collected successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReelCollectResponse'
        '400':
          description: Bad Request – invalid reel URL
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized – invalid or missing API token
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      x-codeSamples:
        - lang: curl
          source: |-
            curl -X POST "https://api.brightdata.com/reels/collect" \
              -H "Authorization: Bearer YOUR_API_TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"url":"https://www.instagram.com/reel/REEL_ID/"}'
        - lang: JavaScript
          source: |-
            fetch("https://api.brightdata.com/reels/collect", {
              method: "POST",
              headers: {
                "Authorization": "Bearer YOUR_API_TOKEN",
                "Content-Type": "application/json"
              },
              body: JSON.stringify({ url: "https://www.instagram.com/reel/REEL_ID/" })
            })
            .then(res => res.json())
            .then(console.log);
        - lang: Node.js
          source: |-
            import axios from "axios";

            const response = await axios.post(
              "https://api.brightdata.com/reels/collect",
              { url: "https://www.instagram.com/reel/REEL_ID/" },
              {
                headers: {
                  Authorization: "Bearer YOUR_API_TOKEN",
                  "Content-Type": "application/json"
                }
              }
            );

            console.log(response.data);
        - lang: Python
          source: |-
            import requests

            url = "https://api.brightdata.com/reels/collect"
            headers = {
              "Authorization": "Bearer YOUR_API_TOKEN",
              "Content-Type": "application/json"
            }
            payload = {
              "url": "https://www.instagram.com/reel/REEL_ID/"
            }

            response = requests.post(url, json=payload, headers=headers)
            print(response.json())
        - lang: Java
          source: >-
            HttpClient client = HttpClient.newHttpClient();

            String body =
            "{\"url\":\"https://www.instagram.com/reel/REEL_ID/\"}";


            HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create("https://api.brightdata.com/reels/collect"))
              .header("Authorization", "Bearer YOUR_API_TOKEN")
              .header("Content-Type", "application/json")
              .POST(HttpRequest.BodyPublishers.ofString(body))
              .build();

            HttpResponse<String> response = client.send(request,
            HttpResponse.BodyHandlers.ofString());

            System.out.println(response.body());
        - lang: Go
          source: |-
            package main

            import (
              "bytes"
              "fmt"
              "net/http"
            )

            func main() {
              body := []byte(`{"url":"https://www.instagram.com/reel/REEL_ID/"}`)

              req, _ := http.NewRequest("POST", "https://api.brightdata.com/reels/collect", bytes.NewBuffer(body))
              req.Header.Set("Authorization", "Bearer YOUR_API_TOKEN")
              req.Header.Set("Content-Type", "application/json")

              client := &http.Client{}
              res, _ := client.Do(req)
              defer res.Body.Close()

              fmt.Println(res.Status)
            }
        - lang: PHP
          source: |-
            <?php

            $ch = curl_init("https://api.brightdata.com/reels/collect");

            curl_setopt_array($ch, [
              CURLOPT_RETURNTRANSFER => true,
              CURLOPT_POST => true,
              CURLOPT_HTTPHEADER => [
                "Authorization: Bearer YOUR_API_TOKEN",
                "Content-Type: application/json"
              ],
              CURLOPT_POSTFIELDS => json_encode([
                "url" => "https://www.instagram.com/reel/REEL_ID/"
              ])
            ]);

            $response = curl_exec($ch);
            curl_close($ch);

            echo $response;
        - lang: Ruby
          source: >-
            require 'net/http'

            require 'json'


            uri = URI('https://api.brightdata.com/reels/collect')

            req = Net::HTTP::Post.new(uri)

            req['Authorization'] = 'Bearer YOUR_API_TOKEN'

            req['Content-Type'] = 'application/json'

            req.body = { url: 'https://www.instagram.com/reel/REEL_ID/'
            }.to_json


            res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do
            |http|
              http.request(req)
            end


            puts res.body
components:
  schemas:
    ReelCollectRequest:
      type: object
      required:
        - url
      properties:
        url:
          type: string
          format: uri
          description: Instagram reel URL
    ReelCollectResponse:
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
        tagged_users:
          type: array
          items:
            type: string
        num_comments:
          type: integer
        likes:
          type: integer
        views:
          type: integer
        video_play_count:
          type: integer
        length:
          type: number
        user_posted:
          type: string
        followers:
          type: integer
        posts_count:
          type: integer
        profile_image_link:
          type: string
        is_verified:
          type: boolean
        profile_url:
          type: string
        video_url:
          type: string
        thumbnail:
          type: string
        audio_url:
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