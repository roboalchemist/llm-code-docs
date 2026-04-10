# Source: https://dev.writer.com/api-reference-legacy/content/post-contentorganization-team-check.md

# null

## OpenAPI

````yaml post /content/organization/{organizationId}/team/{teamId}/check
paths:
  path: /content/organization/{organizationId}/team/{teamId}/check
  method: post
  servers:
    - url: https://enterprise-api.writer.com
  request:
    security: []
    parameters:
      path:
        organizationId:
          schema:
            - type: integer
              required: true
        teamId:
          schema:
            - type: integer
              required: true
      query: {}
      header:
        Authorization:
          schema:
            - type: string
              required: true
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              content:
                allOf:
                  - type: string
              settings:
                allOf:
                  - $ref: '#/components/schemas/ContentSettings'
            required: true
            refIdentifier: '#/components/schemas/ContentRequest'
            requiredProperties:
              - content
              - settings
        examples:
          example:
            value:
              content: <string>
              settings:
                passiveVoice: true
                wordiness: true
                unclearReference: true
                genderInclusivePronouns: true
                genderInclusiveNouns: true
                ageAndFamilyStatus: true
                disability: true
                genderIdentitySensitivity: true
                raceEthnicityNationalitySensitivity: true
                sexualOrientationSensitivity: true
                substanceUseSensitivity: true
                confidence: true
                healthyCommunication: true
                grammar: true
                spelling: true
                contentSafeguards: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              issues:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/ContentIssue'
            refIdentifier: '#/components/schemas/ProcessedContent'
        examples:
          example:
            value:
              issues:
                - from: 123
                  until: 123
                  service: common-mistakes
                  suggestions:
                    - <string>
                  description: <string>
                  meta: <any>
        description: ''
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - &ref_0
                    type: string
              errors:
                allOf:
                  - &ref_1
                    type: array
                    items:
                      $ref: '#/components/schemas/FailMessage'
              extras:
                allOf:
                  - &ref_2
                    $ref: '#/components/schemas/Json'
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: &ref_3
              - tpe
              - extras
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              tpe:
                allOf:
                  - *ref_0
              errors:
                allOf:
                  - *ref_1
              extras:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/FailResponse'
            requiredProperties: *ref_3
        examples:
          example:
            value:
              tpe: <string>
              errors:
                - description: <string>
                  key: <string>
                  extras: <any>
              extras: <any>
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas:
    FailMessage:
      required:
        - description
        - key
        - extras
      type: object
      properties:
        description:
          type: string
        key:
          type: string
        extras:
          $ref: '#/components/schemas/Json'
    Json: {}
    ContentIssue:
      required:
        - from
        - until
        - service
      type: object
      properties:
        from:
          type: integer
        until:
          type: integer
        service:
          type: string
          enum:
            - common-mistakes
            - banned-words
            - dictionary
            - gec
            - infinitive
            - spelling
            - writing-style
            - custom-rules
            - sentence-case
            - acronym
            - oxford-comma
            - ml-punctuation
            - emojis
            - gender-pronouns
            - sensitivity
            - plagiarism
            - readability
            - sentence-complexity
            - vocabulary
            - paragraph-length
            - plain-language
            - healthy-commn
            - confidence
            - data-loss-prevention
            - hate-speech
            - content-safeguards
            - feedback
            - claim
            - quote
            - gender-nouns
            - gender-tone
            - grammar
            - punctuation-dark
            - formatting
            - twitter
            - gec-dark
            - gec-gpt3
        suggestions:
          type: array
          items:
            type: string
        description:
          type: string
        meta:
          $ref: '#/components/schemas/Json'
    ContentSettings:
      required:
        - passiveVoice
        - wordiness
        - unclearReference
        - genderInclusivePronouns
        - genderInclusiveNouns
        - ageAndFamilyStatus
        - disability
        - genderIdentitySensitivity
        - raceEthnicityNationalitySensitivity
        - sexualOrientationSensitivity
        - substanceUseSensitivity
        - confidence
        - healthyCommunication
        - grammar
        - spelling
        - contentSafeguards
      type: object
      properties:
        passiveVoice:
          type: boolean
        wordiness:
          type: boolean
        unclearReference:
          type: boolean
        genderInclusivePronouns:
          type: boolean
        genderInclusiveNouns:
          type: boolean
        ageAndFamilyStatus:
          type: boolean
        disability:
          type: boolean
        genderIdentitySensitivity:
          type: boolean
        raceEthnicityNationalitySensitivity:
          type: boolean
        sexualOrientationSensitivity:
          type: boolean
        substanceUseSensitivity:
          type: boolean
        confidence:
          type: boolean
        healthyCommunication:
          type: boolean
        grammar:
          type: boolean
        spelling:
          type: boolean
        contentSafeguards:
          type: boolean

````