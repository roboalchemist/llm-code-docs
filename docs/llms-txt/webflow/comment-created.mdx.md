# Source: https://developers.webflow.com/data/reference/webhooks/events/comment-created.mdx

# New Comment Thread

POST 

Information about a new comment thread or reply

<Note title="Timing of comment webhooks">
  There may be a delay of up to 5 minutes before new comments appear in the system and trigger the webhook notification.
</Note>


Reference: https://developers.webflow.com/data/reference/webhooks/events/comment-created

## OpenAPI 3.1 Webhook Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths: {}
webhooks:
  comment-created:
    post:
      operationId: comment-created
      summary: New Comment Thread
      description: |
        Information about a new comment thread or reply

        <Note title="Timing of comment webhooks">
          There may be a delay of up to 5 minutes before new comments appear in the system and trigger the webhook notification.
        </Note>
      responses:
        '200':
          description: Webhook received successfully
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                triggerType:
                  type: string
                  description: The type of event that triggered the request
                payload:
                  $ref: >-
                    #/components/schemas/WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayload
                  description: >
                    The comment webhook payload contains data for the thread and
                    for replies.  Check the type to determine if the payload is
                    for a thread or a reply.  The webhook payload may be delayed
                    by up to 5 minutes.
components:
  schemas:
    WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadAuthor:
      type: object
      properties:
        userId:
          type: string
          description: The unique identifier of the author
        email:
          type: string
          description: Email of the author
        name:
          type: string
          description: Name of the author
      required:
        - userId
        - email
        - name
      title: WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadAuthor
    WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadMentionedUsersItems:
      type: object
      properties:
        userId:
          type: string
          description: The unique identifier of the mentioned user
        email:
          type: string
          description: Email of the user
        name:
          type: string
          description: Name of the  User
      required:
        - userId
        - email
        - name
      title: >-
        WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadMentionedUsersItems
    WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayload:
      type: object
      properties:
        threadId:
          type: string
          description: Unique identifier for the comment thread
        commentId:
          type: string
          description: Unique identifier for the comment reply
        type:
          type: string
          description: The type of comment payload
        siteId:
          type: string
          description: The site unique identifier
        pageId:
          type: string
          description: The page unique identifier
        localeId:
          type:
            - string
            - 'null'
          description: The locale unique identifier
        itemId:
          type:
            - string
            - 'null'
          description: The item unique identifier
        breakpoint:
          type: string
          description: The breakpoint the comment was left on
        url:
          type: string
          description: The URL of the page the comment was left on
        content:
          type: string
          description: The content of the comment reply
        isResolved:
          type: boolean
          default: false
          description: Boolean determining if the comment thread is resolved
        author:
          $ref: >-
            #/components/schemas/WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadAuthor
        mentionedUsers:
          type: array
          items:
            $ref: >-
              #/components/schemas/WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayloadMentionedUsersItems
          description: >-
            List of mentioned users. This is an empty array until email
            notifications are sent, which can take up to 5 minutes after the
            comment is created.
        createdOn:
          type: string
          format: date-string
          description: The date the item was created
        lastUpdated:
          type: string
          format: date-string
          description: The date the item was last updated
      required:
        - threadId
        - commentId
        - type
        - siteId
        - pageId
        - localeId
        - itemId
        - breakpoint
        - url
        - content
        - isResolved
        - author
        - mentionedUsers
        - createdOn
        - lastUpdated
      description: >
        The comment webhook payload contains data for the thread and for
        replies.  Check the type to determine if the payload is for a thread or
        a reply.  The webhook payload may be delayed by up to 5 minutes.
      title: WebhooksCommentCreatedPayloadContentApplicationJsonSchemaPayload

```