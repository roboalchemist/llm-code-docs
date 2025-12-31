# Source: https://docs.unstructured.io/api-reference/general/summary.md

# Summary

> Description

## OpenAPI

````yaml https://api.unstructuredapp.io/general/openapi.json post /general/v0/general
paths:
  path: /general/v0/general
  method: post
  servers:
    - url: https://api.unstructuredapp.io
      description: Serverless SaaS API
    - url: http://localhost:8000
      description: Development server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            unstructured-api-key:
              type: apiKey
          cookie: {}
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
    parameters:
      path: {}
      query: {}
      header:
        unstructured-api-key:
          schema:
            - type: string
              required: false
              title: Unstructured-Api-Key
            - type: 'null'
              required: false
              title: Unstructured-Api-Key
      cookie: {}
    body:
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              files:
                allOf:
                  - type: string
                    format: binary
                    description: The file to extract
                    required: 'true'
                    examples:
                      - summary: File to be partitioned
                        externalValue: >-
                          https://github.com/Unstructured-IO/unstructured/blob/98d3541909f64290b5efb65a226fc3ee8a7cc5ee/example-docs/layout-parser-paper.pdf
              coordinates:
                allOf:
                  - type: boolean
                    title: Coordinates
                    description: >-
                      If `True`, return coordinates for each element extracted
                      via OCR. Default: `False`
                    default: false
              content_type:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Content type
                    description: >-
                      A hint about the content type to use (such as
                      text/markdown), when there are problems processing a
                      specific file. This value is a MIME type in the format
                      type/subtype.
              encoding:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Encoding
                    description: >-
                      The encoding method used to decode the text input.
                      Default: utf-8
              extract_image_block_types:
                allOf:
                  - items:
                      type: string
                    type: array
                    title: Image block types to extract
                    description: >-
                      The types of elements to extract, for use in extracting
                      image blocks as base64 encoded data stored in metadata
                      fields.
                    default: []
              gz_uncompressed_content_type:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Uncompressed Content Type
                    description: If file is gzipped, use this content type after unzipping.
              hi_res_model_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Hi Res Model Name
                    description: >-
                      The name of the inference model used when strategy is
                      hi_res
              include_page_breaks:
                allOf:
                  - type: boolean
                    title: Include Page Breaks
                    description: >-
                      If true, the output will include page breaks if the
                      filetype supports it. Default: false
                    default: false
              languages:
                allOf:
                  - items:
                      type: string
                    type: array
                    title: OCR Languages
                    description: >-
                      The languages present in the document, for use in
                      partitioning and/or OCR. See the Tesseract documentation
                      for a full list of languages.
                    default: []
              ocr_languages:
                allOf:
                  - items:
                      type: string
                    type: array
                    title: OCR Languages
                    description: >-
                      Deprecated! The languages present in the document, for use
                      in partitioning and/or OCR
                    default: []
              output_format:
                allOf:
                  - type: string
                    enum:
                      - application/json
                      - text/csv
                    title: Output Format
                    description: >-
                      The format of the response. Supported formats are
                      application/json and text/csv. Default: application/json.
                    default: application/json
                    x-speakeasy-unknown-values: allow
              pdf_infer_table_structure:
                allOf:
                  - type: boolean
                    title: Pdf Infer Table Structure
                    description: >-
                      Deprecated! Use skip_infer_table_types to opt out of table
                      extraction for any file type. If False and
                      strategy=hi_res, no Table Elements will be extracted from
                      pdf files regardless of skip_infer_table_types contents.
                    default: true
              skip_infer_table_types:
                allOf:
                  - items:
                      type: string
                    type: array
                    title: Skip Infer Table Types
                    description: >-
                      The document types that you want to skip table extraction
                      with. Default: []
                    default: []
              starting_page_number:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: PDF Starting Page Number
                    description: >-
                      When PDF is split into pages before sending it into the
                      API, providing this information will allow the page number
                      to be assigned correctly. Introduced in 1.0.27.
              strategy:
                allOf:
                  - type: string
                    enum:
                      - fast
                      - hi_res
                      - auto
                      - ocr_only
                      - od_only
                      - vlm
                    title: Strategy
                    description: >-
                      The strategy to use for partitioning PDF/image. Options
                      are fast, hi_res, auto. Default: hi_res
                    default: hi_res
                    examples:
                      - auto
                      - hi_res
                      - vlm
                    x-speakeasy-unknown-values: allow
              vlm_model_provider:
                allOf:
                  - type: string
                    enum:
                      - openai
                      - anthropic
                      - bedrock
                      - anthropic_bedrock
                      - vertexai
                      - google
                      - azure_openai
                    title: VLM Model Provider
                    description: The VLM Model provider to use.
                    examples:
                      - openai
                      - anthropic
                      - bedrock
                    x-speakeasy-unknown-values: allow
              vlm_model:
                allOf:
                  - type: string
                    title: VLM Model
                    description: The VLM Model to use.
                    examples:
                      - gpt-4o
                    x-speakeasy-unknown-values: allow
              table_ocr_agent:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Table OCR Agent
                    description: The OCR agent to use for table ocr inference.
                    default: >-
                      unstructured.partition.utils.ocr_models.tesseract_ocr.OCRAgentTesseract
              unique_element_ids:
                allOf:
                  - type: boolean
                    title: Unique Element IDs
                    description: >-
                      When `True`, assign UUIDs to element IDs, which guarantees
                      their uniqueness (useful when using them as primary keys
                      in database). Otherwise a SHA-256 of element text is used.
                      Default: `False`
                    default: false
              xml_keep_tags:
                allOf:
                  - type: boolean
                    title: Xml Keep Tags
                    description: >-
                      If `True`, will retain the XML tags in the output.
                      Otherwise it will simply extract the text from within the
                      tags. Only applies to XML documents.
                    default: false
              chunking_strategy:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Chunking Strategy
                    description: >-
                      Use one of the supported strategies to chunk the returned
                      elements after partitioning. When 'chunking_strategy' is
                      not specified, no chunking is performed and any other
                      chunking parameters provided are ignored. Supported
                      strategies: 'basic', 'by_page', 'by_similarity', or
                      'by_title'
                    examples:
                      - by_title
                      - basic
                    x-speakeasy-unknown-values: allow
              combine_under_n_chars:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Combine Under N Chars
                    description: >-
                      If chunking strategy is set, combine elements until a
                      section reaches a length of n chars. Default: 500
              include_orig_elements:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Include original elements in chunks
                    description: >-
                      When a chunking strategy is specified, each returned chunk
                      will include the elements consolidated to form that chunk
                      as `.metadata.orig_elements`. Default: true.
              tracking_enabled:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Tracking enabled
                    description: Tracking enabled
              max_characters:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Characters
                    description: >-
                      If chunking strategy is set, cut off new sections after
                      reaching a length of n chars (hard max). Default: 500
              multipage_sections:
                allOf:
                  - type: boolean
                    title: Multipage Sections
                    description: >-
                      If chunking strategy is set, determines if sections can
                      span multiple sections. Default: true
                    default: true
              new_after_n_chars:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: New after n chars
                    description: >-
                      If chunking strategy is set, cut off new sections after
                      reaching a length of n chars (soft max). Default: 1500
              overlap:
                allOf:
                  - type: integer
                    title: Overlap
                    description: >-
                      Specifies the length of a string ('tail') to be drawn from
                      each chunk and prefixed to the next chunk as a
                      context-preserving mechanism. By default, this only
                      applies to split-chunks where an oversized element is
                      divided into multiple chunks by text-splitting. Default: 0
                    default: 0
              overlap_all:
                allOf:
                  - type: boolean
                    title: Overlap all
                    description: >-
                      When `True`, apply overlap between 'normal' chunks formed
                      from whole elements and not subject to text-splitting. Use
                      this with caution as it entails a certain level of
                      'pollution' of otherwise clean semantic chunk boundaries.
                      Default: False
                    default: false
              similarity_threshold:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: similarity-threshold
                    description: >-
                      A value between 0.0 and 1.0 describing the minimum
                      similarity two elements must have to be included in the
                      same chunk. Note that similar elements may be separated to
                      meet chunk-size criteria; this value can only guarantees
                      that two elements with similarity below the threshold will
                      appear in separate chunks.
              do_not_break_similarity_on_footer_header:
                allOf:
                  - type: boolean
                    title: do-not-break-similarity-on-footer-header
                    description: >-
                      When `True`, footer, header, and page number are always
                      considered similar to the text before them for chunk by
                      similarity method. This allows chunk by similarity to
                      connect contents across page better.
                    default: false
              include_slide_notes:
                allOf:
                  - type: boolean
                    title: include_slide_notes
                    description: >-
                      When `True`, slide notes from .ppt and .pptx files will be
                      included in the response. Default: `True`
                    default: true
              pdfminer_line_overlap:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: PDFMiner Line Overlap
                    description: >-
                      If two characters have more overlap than this they are
                      considered to be on the same line. The overlap is
                      specified relative to the minimum height of both
                      characters.
              pdfminer_char_margin:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: PDFMiner Char Margin
                    description: >-
                      If two characters are closer together than this margin
                      they are considered part of the same line. The margin is
                      specified relative to the width of the character.
              pdfminer_line_margin:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: PDFMiner Line Margin
                    description: >-
                      If two lines are close together they are considered to be
                      part of the same paragraph. The margin is specified
                      relative to the height of a line.
              pdfminer_word_margin:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: PDFMiner Word Margin
                    description: >-
                      If two characters on the same line are further apart than
                      this margin then they are considered to be two separate
                      words, and an intermediate space will be added for
                      readability. The margin is specified relative to the width
                      of the character.
                    default: 0.185
            required: true
            title: Partition Parameters
            refIdentifier: '#/components/schemas/partition_parameters'
            requiredProperties:
              - files
        examples:
          example:
            value:
              coordinates: false
              content_type: <string>
              encoding: <string>
              extract_image_block_types: []
              gz_uncompressed_content_type: <string>
              hi_res_model_name: <string>
              include_page_breaks: false
              languages: []
              ocr_languages: []
              output_format: application/json
              pdf_infer_table_structure: true
              skip_infer_table_types: []
              starting_page_number: 123
              strategy: auto
              vlm_model_provider: openai
              vlm_model: gpt-4o
              table_ocr_agent: <string>
              unique_element_ids: false
              xml_keep_tags: false
              chunking_strategy: by_title
              combine_under_n_chars: 123
              include_orig_elements: true
              tracking_enabled: true
              max_characters: 123
              multipage_sections: true
              new_after_n_chars: 123
              overlap: 0
              overlap_all: false
              similarity_threshold: 123
              do_not_break_similarity_on_footer_header: false
              include_slide_notes: true
              pdfminer_line_overlap: 123
              pdfminer_char_margin: 123
              pdfminer_line_margin: 123
              pdfminer_word_margin: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Element'
            title: Elements
            description: A list of element dictionaries extracted from the file
        examples:
          example:
            value:
              - type: Title
                element_id: 6aa0ff22f91bbe7e26e8e25ca8052acd
                text: >-
                  LayoutParser: A Unified Toolkit for Deep Learning Based
                  Document Image Analysis
                metadata:
                  languages:
                    - eng
                  page_number: 1
                  filename: layout-parser-paper.pdf
                  filetype: application/pdf
        description: Successful Response
      text/csv:
        schemaArray:
          - type: string
            title: CSV-Element
            description: A string containing elements in csv format
        examples:
          example:
            value: <string>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - oneOf:
                      - type: array
                        items:
                          $ref: '#/components/schemas/ValidationError'
                      - type: string
            refIdentifier: '#/components/schemas/HTTPValidationError'
            example:
              detail:
                - type: int_parsing
                  loc:
                    - body
                    - combine_under_n_chars
                  msg: >-
                    Input should be a valid integer, unable to parse string as
                    an integer
                  input: forty
        examples:
          example:
            value:
              detail:
                - type: int_parsing
                  loc:
                    - body
                    - combine_under_n_chars
                  msg: >-
                    Input should be a valid integer, unable to parse string as
                    an integer
                  input: forty
        description: Validation Error
    5XX:
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ServerError'
            example:
              detail: An error occurred
        examples:
          example:
            value:
              detail: An error occurred
        description: Server Error
  deprecated: false
  type: path
components:
  schemas:
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    Element:
      title: Element
      type: object
      additionalProperties: true
      example:
        type: Title
        element_id: 6aa0ff22f91bbe7e26e8e25ca8052acd
        text: >-
          LayoutParser: A Unified Toolkit for Deep Learning Based Document Image
          Analysis
        metadata:
          languages:
            - eng
          page_number: 1
          filename: layout-parser-paper.pdf
          filetype: application/pdf

````