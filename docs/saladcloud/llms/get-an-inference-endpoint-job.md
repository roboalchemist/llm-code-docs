# Source: https://docs.salad.com/reference/transcription-lite/inference_endpoints/get-an-inference-endpoint-job.md

# Source: https://docs.salad.com/reference/transcribe/inference_endpoints/get-an-inference-endpoint-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get job for Salad Transcription API

> Retrieves a job for Salad Transcription API

*Last Updated: October 24, 2024*


## OpenAPI

````yaml transcribe get /organizations/{organization_name}/inference-endpoints/transcribe/jobs/{job_id}
openapi: 3.0.3
info:
  title: Salad Transcription API
  description: Salad Transcription API
  termsOfService: https://salad.com/terms
  contact:
    name: SaladCloud Support
    url: https://salad.com
    email: cloud@salad.com
  license:
    name: MIT
  version: 0.9.0-alpha.5
servers:
  - url: https://api.salad.com/api/public
security:
  - ApiKeyAuth: []
tags:
  - name: container_groups
    description: Container Groups
  - name: inference_endpoints
    description: Inference Endpoints
  - name: organization_data
    description: Auxiliary organization data and info
  - name: queues
    description: Job Queues
  - name: quotas
    description: quotas
  - name: workload_errors
    description: Workload Errors
  - name: webhook_secret_key
    description: Webhook Secret Key
paths:
  /organizations/{organization_name}/inference-endpoints/transcribe/jobs/{job_id}:
    summary: Job for Salad Transcription API
    description: Operations for a Salad Transcription API job
    parameters:
      - $ref: '#/components/parameters/organization_name'
      - $ref: '#/components/parameters/job_id'
    get:
      tags:
        - inference_endpoints
      summary: Get job for Salad Transcription API
      description: Retrieves a job for Salad Transcription API
      operationId: get_inference_endpoint_job
      responses:
        '200':
          $ref: '#/components/responses/GetSaladCloudTranscriptionAPIJob'
        '404':
          $ref: '#/components/responses/404'
        '429':
          $ref: '#/components/responses/429'
        default:
          $ref: '#/components/responses/UnknownError'
components:
  parameters:
    organization_name:
      in: path
      name: organization_name
      required: true
      schema:
        type: string
        maxLength: 63
        minLength: 2
        pattern: ^[a-z][a-z0-9-]{0,61}[a-z0-9]$
      description: >-
        Your organization name. This identifies the billing context for the API
        operation and represents a security boundary for SaladCloud resources.
        The organization must be created before using the API, and you must be a
        member of the organization.
      example: acme-corp
    job_id:
      in: path
      name: job_id
      description: The ID of the job for Salad Transcription API
      required: true
      schema:
        type: string
        format: uuid
  responses:
    '404':
      description: Not Found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
          examples:
            jsonExample:
              value:
                type: about:blank
                title: Not Found
                status: 404
                detail: Not Found
                instance: 72ea5f29
    '429':
      description: Too Many Requests
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
          examples:
            jsonExample:
              value:
                type: about:blank
                title: Too Many Requests
                status: 409
                detail: Too Many Requests
                instance: cd6306ee
    GetSaladCloudTranscriptionAPIJob:
      description: Ok
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SaladCloudTranscriptionAPIJob'
          examples:
            jsonExample:
              value:
                id: 123e4567-e89b-12d3-a456-426614174001
                inference_endpoint_name: transcribe
                input:
                  property1: value1
                  property2: value2
                metadata: null
                organization_name: acme-corp
                status: pending
                events: []
                create_time: '2024-05-01T19:00:00Z'
                update_time: '2024-05-01T19:00:00Z'
    UnknownError:
      description: Unknown Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProblemDetails'
          examples:
            jsonExample:
              value:
                type: about:blank
                title: Unknown Error
                status: 500
                detail: Unknown Error
                instance: 188f9bbb
  schemas:
    SaladCloudTranscriptionAPIJob:
      description: Job input schema for Salad Transcription API
      type: object
      properties:
        id:
          type: string
          format: uuid
        input:
          $ref: '#/components/schemas/SaladCloudTranscriptionAPIInput'
        inference_endpoint_name:
          description: The inference endpoint name
          type: string
        metadata:
          type: object
          maxProperties: 20
          nullable: true
        webhook:
          type: string
          format: url
          nullable: true
        status:
          type: string
          enum:
            - pending
            - running
            - succeeded
            - cancelled
            - failed
        events:
          type: array
          items:
            $ref: '#/components/schemas/InferenceEndpointJobEvent'
          maxItems: 1000
          minItems: 0
        organization_name:
          description: The organization name
          type: string
        output:
          $ref: '#/components/schemas/SaladCloudTranscriptionAPIOutput'
        create_time:
          type: string
          format: date-time
        update_time:
          type: string
          format: date-time
      additionalProperties: false
      required:
        - id
        - input
        - status
        - events
        - create_time
        - update_time
        - inference_endpoint_name
        - organization_name
    ProblemDetails:
      description: Represents a problem
      type: object
      properties:
        type:
          description: The URI reference that identifies the problem type
          type: string
          default: about:blank
          nullable: true
        title:
          description: A short, human-readable summary of the problem type
          type: string
          nullable: true
        status:
          description: The HTTP status code generated by the origin server
          type: integer
          nullable: true
        detail:
          description: >-
            A human-readable explanation specific to this occurrence of the
            problem
          type: string
          nullable: true
        instance:
          description: >-
            The URI reference that identifies the specific occurrence of the
            problem
          type: string
          nullable: true
      additionalProperties: false
    SaladCloudTranscriptionAPIInput:
      type: object
      properties:
        url:
          type: string
          format: uri
          description: URL of the audio file to process. Must be a downloadable link.
          example: https://example.com/audiofile.mp3
        language_code:
          type: string
          description: Language code for the transcription. Defaults to 'en' (English).
          example: en
          enum:
            - en
            - zh
            - de
            - es
            - ru
            - ko
            - fr
            - ja
            - pt
            - tr
            - pl
            - ca
            - nl
            - ar
            - sv
            - it
            - id
            - hi
            - fi
            - vi
            - he
            - uk
            - el
            - ms
            - cs
            - ro
            - da
            - hu
            - ta
            - 'no'
            - th
            - ur
            - hr
            - bg
            - lt
            - la
            - mi
            - ml
            - cy
            - sk
            - te
            - fa
            - lv
            - bn
            - sr
            - az
            - sl
            - kn
            - et
            - mk
            - br
            - eu
            - is
            - hy
            - ne
            - mn
            - bs
            - kk
            - sq
            - sw
            - gl
            - mr
            - pa
            - si
            - km
            - sn
            - yo
            - so
            - af
            - oc
            - ka
            - be
            - tg
            - sd
            - gu
            - am
            - yi
            - lo
            - uz
            - fo
            - ht
            - ps
            - tk
            - nn
            - mt
            - sa
            - lb
            - my
            - bo
            - tl
            - mg
            - as
            - tt
            - haw
            - ln
            - ha
            - ba
            - jw
            - su
            - yue
        return_as_file:
          type: boolean
          default: false
          description: Whether to return the result as a file.
        sentence_level_timestamps:
          type: boolean
          default: false
          description: Return sentence-level timestamps in the transcription.
        word_level_timestamps:
          type: boolean
          default: false
          description: Return word-level timestamps in the transcription.
        diarization:
          type: boolean
          default: false
          description: >-
            Perform speaker diarization (separate speakers in multi-speaker
            audio).
        sentence_diarization:
          type: boolean
          default: false
          description: Perform sentence-level speaker diarization.
        srt:
          type: boolean
          default: false
          description: Generate an SRT file (SubRip Subtitle format).
        translate:
          type: string
          description: >-
            Translate the transcription to English (set to 'to eng' to enable
            translation).
          example: to_eng
        custom_prompt:
          type: string
          description: >-
            Custom prompt for LLM-driven tasks such as summarization or
            classification.
          example: Summarize the main points of the conversation.
        summarize:
          type: integer
          default: 0
          description: Summarize the transcription. Integer specifies the word limit.
          example: 100
        llm_translation:
          type: string
          description: >-
            List of languages for LLM-based translation, e.g., 'german, italian,
            french, english, portuguese, hindi, spanish, thai'.
          example: french, german
        srt_translation:
          type: string
          description: >-
            List of languages for SRT translation, e.g., 'german, italian,
            french, english, portuguese, hindi, spanish, thai'.
          example: spanish, hindi
        custom_vocabulary:
          type: string
          description: >-
            Custom vocabulary to improve transcription accuracy for specific
            terms.
          example: AI, NLP, cloud computing
        classification_labels:
          type: string
          description: >-
            List of labels to use for sentence classification, e.g., 'INTERVIEW,
            MEETING, CALL'.
          example: INTERVIEW, MEETING, CALL
        overall_classification:
          type: boolean
          default: false
          description: Perform overall classification of the transcription.
        overall_sentiment_analysis:
          type: boolean
          default: false
          description: Perform overall sentiment analysis on the transcription.
      required:
        - url
      additionalProperties: false
    InferenceEndpointJobEvent:
      description: Represents an event for inference endpoint job
      type: object
      properties:
        action:
          type: string
          enum:
            - created
            - started
            - succeeded
            - cancelled
            - failed
        time:
          type: string
          format: date-time
      additionalProperties: false
      required:
        - action
        - time
    SaladCloudTranscriptionAPIOutput:
      type: object
      properties:
        sentence_level_timestamps:
          type: array
          description: >-
            List of sentences with timestamps, speaker identification, sentiment
            analysis, and classification.
          items:
            type: object
            properties:
              text:
                type: string
                description: Transcribed sentence.
                example: You know that little voice in your head?
              timestamp:
                type: array
                items:
                  type: number
                  format: float
                description: Start and end times of the sentence in seconds.
                example:
                  - 0
                  - 5.9
              start:
                type: number
                format: float
                description: Start time of the sentence in seconds.
                example: 0
              end:
                type: number
                format: float
                description: End time of the sentence in seconds.
                example: 5.9
              speaker:
                type: string
                description: Identified speaker label.
                example: SPEAKER_02
              sentiment:
                type: array
                description: Sentiment analysis results for the sentence.
                items:
                  type: object
                  properties:
                    label:
                      type: string
                      description: Sentiment label.
                      example: NEGATIVE
                    score:
                      type: number
                      format: float
                      description: Confidence score for the sentiment label.
                      example: 0.9837925434112549
              classification:
                type: object
                description: >-
                  Classification labels and their confidence scores for the
                  sentence.
                properties:
                  label:
                    type: array
                    items:
                      type: string
                    description: List of classification labels.
                    example:
                      - VOICEMAIL
                      - PHONE_CALL
                      - PRESENTATION
                  scores:
                    type: array
                    items:
                      type: number
                      format: float
                    description: >-
                      Confidence scores corresponding to each classification
                      label.
                    example:
                      - 0.2575797736644745
                      - 0.20001687109470367
                      - 0.15546734631061554
            required:
              - text
              - start
              - end
              - speaker
        word_segments:
          type: array
          description: >-
            List of words with timestamps, confidence scores, and speaker
            identification.
          items:
            type: object
            properties:
              word:
                type: string
                description: Transcribed word.
                example: You
              start:
                type: number
                format: float
                description: Start time of the word in seconds.
                example: 4.274
              end:
                type: number
                format: float
                description: End time of the word in seconds.
                example: 4.395
              score:
                type: number
                format: float
                description: Confidence score for the transcribed word.
                example: 0.89
              speaker:
                type: string
                description: Identified speaker label.
                example: SPEAKER_02
            required:
              - word
              - start
              - end
              - score
              - speaker
        srt_content:
          type: string
          description: Generated SRT (SubRip Subtitle) content.
          example: |-
            1
            00:00:04,274 --> 00:00:05,880
            You know that little voice in your head?

            2
            00:00:10,506 --> 00:00:13,240
            The one that tells you to ignore a tasteless joke?
            ...
        summary:
          type: string
          description: Summarized version of the transcription.
          example: Silence oppressive voices, amplify your own.
        llm_translations:
          type: object
          description: LLM-generated translations of the transcription.
          additionalProperties:
            type: string
            description: Translation of the transcription in the specified language.
            example: >-
              Vous savez cette petite voix dans votre tête ? Celle qui vous dit
              de passer outre un blague sans goût ? ...
        srt_translation:
          type: object
          description: Translations of the SRT content in various languages.
          additionalProperties:
            type: string
            description: Translated SRT content in the specified language.
            example: |-
              1
              00:00:04,274 --> 00:00:05,880
              Du weißt die kleine Stimme in deinem Kopf?
              ...
        llm_result:
          type: string
          description: Main idea or key takeaway generated by the LLM.
          example: 'The main idea is: Speak up against injustice and stereotypes.'
        overall_classification:
          type: string
          description: Overall classification labels for the transcription.
          example: PRESENTATION, INTERVIEW
        overall_sentiment:
          type: string
          description: Overall sentiment of the transcription.
          example: POSITIVE
        text:
          type: string
          description: Full transcribed text from the audio.
          example: >-
            You know that little voice in your head? The one that tells you to
            ignore a tasteless joke? ...
        duration:
          type: number
          format: float
          description: Duration of the audio file in hours.
          example: 0.04
        processing_time:
          type: number
          format: float
          description: Time taken to process the transcription in seconds.
          example: 69.79421997070312
      required:
        - text
        - duration
        - processing_time
      additionalProperties: false
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Salad-Api-Key

````