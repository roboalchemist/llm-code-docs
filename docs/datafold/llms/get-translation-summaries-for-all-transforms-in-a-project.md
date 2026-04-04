# Source: https://docs.datafold.com/api-reference/dma_v2/get-translation-summaries-for-all-transforms-in-a-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get translation summaries for all transforms in a project

> Get translation summaries for all transforms in a project.

Returns a list of transform summaries including transform group metadata,
validation status, and execution results. Use this to monitor translation
progress and identify failed transforms.



## OpenAPI

````yaml openapi-public.json get /api/v1/dma/v2/projects/{project_id}/transforms
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/dma/v2/projects/{project_id}/transforms:
    get:
      tags:
        - DMA_V2
      summary: Get translation summaries for all transforms in a project
      description: >-
        Get translation summaries for all transforms in a project.


        Returns a list of transform summaries including transform group
        metadata,

        validation status, and execution results. Use this to monitor
        translation

        progress and identify failed transforms.
      operationId: list_transform_summaries
      parameters:
        - in: path
          name: project_id
          required: true
          schema:
            title: Translation project id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiListTransformsResponse'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiListTransformsResponse:
      properties:
        transform_summaries:
          items:
            $ref: '#/components/schemas/TransformSummary'
          title: Transform Summaries
          type: array
      required:
        - transform_summaries
      title: ApiListTransformsResponse
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    TransformSummary:
      properties:
        asset_count:
          title: Asset Count
          type: integer
        iterations:
          title: Iterations
          type: integer
        source:
          title: Source
          type: string
        status:
          title: Status
          type: string
        transform_chain:
          $ref: '#/components/schemas/TransformChain'
        transform_group:
          title: Transform Group
          type: string
        uuid:
          title: Uuid
          type: string
        validations:
          additionalProperties:
            type: string
          title: Validations
          type: object
      required:
        - transform_group
        - iterations
        - uuid
        - status
        - validations
        - asset_count
        - source
        - transform_chain
      title: TransformSummary
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object
    TransformChain:
      properties:
        chain:
          items:
            $ref: '#/components/schemas/TransformCollection'
          title: Chain
          type: array
        root_transform_group:
          $ref: '#/components/schemas/TransformGroup'
      required:
        - root_transform_group
        - chain
      title: TransformChain
      type: object
    TransformCollection:
      properties:
        parent_transform_group:
          $ref: '#/components/schemas/TransformGroup'
        transforms:
          items:
            $ref: '#/components/schemas/Transform'
          title: Transforms
          type: array
      required:
        - transforms
        - parent_transform_group
      title: TransformCollection
      type: object
    TransformGroup:
      description: >-
        A TransformGroup defines what operations and database objects are
        transformed together.


        There can be multiple TransformGroups pointing to the same set of
        objects+operations to

        translate. We do this to allow chained transforms, and to be able to
        keep track of what

        is transformed and what is not.
      properties:
        computed_pk:
          default: '--invalid-pk-you-shouldn''t-be-seeing-this-ever--'
          title: Computed Pk
          type: string
        debug:
          additionalProperties: true
          title: Debug
          type: object
        side:
          $ref: '#/components/schemas/SideEnum'
        tags:
          items:
            type: string
          title: Tags
          type: array
          uniqueItems: true
        uuid:
          format: uuid4
          title: Uuid
          type: string
      required:
        - side
      title: TransformGroup
      type: object
    Transform:
      description: >-
        Represents a transformation.

        Transformation can be a translation, splitting, perf optimization,
        refactoring, etc.


        Translation is linked to inputs and outputs with InputOf and OutputOf
        edges.

        Inputs and outputs are:

        - operations and database objects that transform acts on

        - versions of input and output operations (that references
        FileFragments)
          - output operations have templated code

        - looks like hyperedges would be helpful to link (src, target, transform
        but
          we can't have this.

        - we can tag source transform group with "done" tag if transform is Done
          according to acceptance criteria. We can also add other user-level tags.
          The target transform group will be marked as "done" only if it's the final transform.
          This is denormalization, kind of + workflow tracking.

        - Every iteration produces a new Transform structure. If we start off
        not from 0,
          but from another Transform, we add "BuildsOnTopOf" / "DerivedFrom" / "ChildOf"
          edge.

        - For a "parentless" transform we always create a new TransformGroup,
          even if it's a refactor transform in the same database. We put "draft" tag
          on the TransformGroup so that we don't mess up reporting. When transform
          is Done, we remove the "draft" tag. For transform with a parent, we
          reuse the same TransformGroup. If the new transform succeeds, we mark
          it as the main one.

        - Validation tracking: we have to validate multiple artifacts and
        potentially
          multiple types of artifacts. We create a full set of TransformValidationOfDataset
          along with Transform, in a single transaction.
      properties:
        computed_pk:
          default: '--invalid-pk-you-shouldn''t-be-seeing-this-ever--'
          title: Computed Pk
          type: string
        debug:
          additionalProperties: true
          description: Debug information
          title: Debug
          type: object
        failure_summary:
          anyOf:
            - $ref: '#/components/schemas/FailureSummary'
            - type: 'null'
          deprecated: true
          description: >-
            DEPRECATED: Use TransformGroupSummary artifact instead. Summaries
            are per transform group attempt, not per transform iteration.
        lifecycle_state:
          $ref: '#/components/schemas/TransformLifecycleState'
        side:
          $ref: '#/components/schemas/SideEnum'
        tags:
          items:
            type: string
          title: Tags
          type: array
          uniqueItems: true
        transform_kind:
          $ref: '#/components/schemas/TransformKind'
        uuid:
          format: uuid4
          title: Uuid
          type: string
        validation_results:
          items:
            $ref: '#/components/schemas/ValidationEntry'
          title: Validation Results
          type: array
      required:
        - side
        - transform_kind
        - lifecycle_state
        - validation_results
      title: Transform
      type: object
    SideEnum:
      enum:
        - source
        - target
      title: SideEnum
      type: string
    FailureSummary:
      description: >-
        Structured failure summary with separate problem, error, and solution
        sections.
      properties:
        error_message:
          title: Error Message
          type: string
        location:
          anyOf:
            - type: string
            - type: 'null'
          title: Location
        problem:
          title: Problem
          type: string
        reason:
          $ref: '#/components/schemas/FailureReason'
        solution:
          title: Solution
          type: string
      required:
        - problem
        - error_message
        - solution
        - reason
      title: FailureSummary
      type: object
    TransformLifecycleState:
      enum:
        - created
        - running
        - done
        - error
      title: TransformLifecycleState
      type: string
    TransformKind:
      enum:
        - squash
        - bundle
      title: TransformKind
      type: string
    ValidationEntry:
      description: Represents something that was validated, and how it was validated.
      properties:
        created_at:
          format: date-time
          title: Created At
          type: string
        description:
          description: Description of the performed validation
          title: Description
          type: string
        finished_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Finished At
        last_updated_at:
          format: date-time
          title: Last Updated At
          type: string
        notes:
          description: Optional notes/comments
          items:
            type: string
          title: Notes
          type: array
        related_assets:
          description: >-
            Assets involved in the validation (mapping between source and
            destination DWH objects, may be the same for in-db refactorings)
          items:
            maxItems: 2
            minItems: 2
            prefixItems:
              - $ref: >-
                  #/components/schemas/Gfk_Union_Table__View__SqlSequence__StoredProcedure__UserDefinedFunction__BuiltinFunction__UnresolvedSqlObject__
              - $ref: >-
                  #/components/schemas/Gfk_Union_Table__View__SqlSequence__StoredProcedure__UserDefinedFunction__BuiltinFunction__UnresolvedSqlObject__
            type: array
          title: Related Assets
          type: array
        requested_validation_kind:
          $ref: '#/components/schemas/ValidationResultKind'
          description: Kind of validation performed by this gate
        result:
          anyOf:
            - discriminator:
                mapping:
                  code_execution: '#/components/schemas/GroupExecutionResult'
                  diff: '#/components/schemas/DiffValidationResult'
                  error: '#/components/schemas/ErrorResult'
                  manual_review: '#/components/schemas/CodeReviewResult'
                  pk_inference: '#/components/schemas/PkInferenceResult'
                  test_case_generation: '#/components/schemas/TestCaseGenerationResult'
                propertyName: kind
              oneOf:
                - $ref: '#/components/schemas/DiffValidationResult'
                - $ref: '#/components/schemas/CodeReviewResult'
                - $ref: '#/components/schemas/GroupExecutionResult'
                - $ref: '#/components/schemas/ErrorResult'
                - $ref: '#/components/schemas/TestCaseGenerationResult'
                - $ref: '#/components/schemas/PkInferenceResult'
            - type: 'null'
          description: >-
            Validation result. May be different than requested validation kind
            (in case of a fatal error for example.
          title: Result
        status:
          $ref: '#/components/schemas/ValidationStatus'
          description: Current validation status
      required:
        - description
        - status
        - requested_validation_kind
        - result
        - related_assets
      title: ValidationEntry
      type: object
    FailureReason:
      description: Reasons why an agent failed to complete its task.
      enum:
        - max_iterations
        - tool_error
        - resignation
      title: FailureReason
      type: string
    ValidationResultKind:
      enum:
        - manual_review
        - diff
        - code_execution
        - compilation
        - test_case_generation
        - pk_inference
        - error
      title: ValidationResultKind
      type: string
    DiffValidationResult:
      description: >-
        Diff validation result (produced data-sets are expected to match with
        reference datasets)
      properties:
        datadiff_id:
          description: Identifier of started data-diff
          title: Datadiff Id
          type: integer
        diff_result:
          anyOf:
            - $ref: '#/components/schemas/DataDiffResultValues'
            - type: 'null'
          description: Data-diff result (null if diff is currently running)
        has_schema_type_differences:
          default: false
          description: >-
            Whether there are schema differences we care about (e.g., timestamp
            timezone mismatch)
          title: Has Schema Type Differences
          type: boolean
        human_readable_feedback:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            A human-readable representation of the diff results (typically given
            as feedback to the human-in-the-loop or LLM agent.
          title: Human Readable Feedback
        incremental_iteration:
          anyOf:
            - type: integer
            - type: 'null'
          deprecated: true
          description: The iteration number of the incremental operation, if applicable
          title: Incremental Iteration
        is_zero_row_diff:
          default: false
          description: >-
            Whether the diff was performed on datasets with zero rows on both
            sides
          title: Is Zero Row Diff
          type: boolean
        kind:
          const: diff
          default: diff
          title: Kind
          type: string
        reference_dataset:
          $ref: '#/components/schemas/Gfk_DfTable_'
          description: >-
            Reference dataset: the reference dataset. Typically, this would be
            the asset in the source DWH. In the data-diff, this is the
            left-hand-side table.
        total_iterations:
          anyOf:
            - type: integer
            - type: 'null'
          deprecated: true
          description: >-
            The total number of iterations of the incremental operation, if
            applicable
          title: Total Iterations
        validated_dataset:
          $ref: '#/components/schemas/Gfk_DfTable_'
          description: >-
            Validated dataset: the dataset produced by the transformed code,
            compared against the reference dataset. Typically, this would be the
            asset in the destination DWH (or in the source DWH in case of a
            refactoring). In the data-diff, this is the right-hand-side table.
      required:
        - reference_dataset
        - validated_dataset
        - datadiff_id
        - diff_result
        - human_readable_feedback
      title: DiffValidationResult
      type: object
    CodeReviewResult:
      description: >-
        Code review: a user or agent reviewed the transformed code and approved
        / rejected with or

        without comments.
      properties:
        feedback:
          description: Optional feedback left by user / agent
          items:
            anyOf:
              - $ref: '#/components/schemas/GeneralReviewComment'
              - $ref: '#/components/schemas/CodeChunkComment'
          title: Feedback
          type: array
        kind:
          const: manual_review
          default: manual_review
          title: Kind
          type: string
        review_status:
          $ref: '#/components/schemas/ReviewStatus'
          description: Review outcome
        reviewed_by:
          anyOf:
            - $ref: '#/components/schemas/User'
            - $ref: '#/components/schemas/AIAgent'
          description: Who submitted the review
          title: Reviewed By
      required:
        - reviewed_by
        - review_status
      title: CodeReviewResult
      type: object
    GroupExecutionResult:
      description: >-
        Group execution result (all transformed steps are expected to execute
        successfully)
      properties:
        execution_group:
          $ref: '#/components/schemas/Gfk_ExecutionGroup_'
          description: Executed group of operations
        execution_result_set:
          anyOf:
            - $ref: '#/components/schemas/Gfk_ExecutionResultSet_'
            - type: 'null'
          description: >-
            The execution result set (only set if end-to-end execution was
            successful)
        failed_execution_steps:
          description: Steps that failed within the group, and associated error metadata
          items:
            $ref: '#/components/schemas/ExecutionErrorInfo'
          title: Failed Execution Steps
          type: array
        kind:
          const: code_execution
          default: code_execution
          title: Kind
          type: string
      required:
        - execution_group
        - failed_execution_steps
        - execution_result_set
      title: GroupExecutionResult
      type: object
    ErrorResult:
      description: >-
        Generic error result, to be used in cases where the validation
        errored/crashed.
      properties:
        kind:
          const: error
          default: error
          title: Kind
          type: string
        message:
          description: Error message
          title: Message
          type: string
        stack_trace:
          anyOf:
            - type: string
            - type: 'null'
          description: Optional crash stack trace
          title: Stack Trace
      required:
        - message
      title: ErrorResult
      type: object
    TestCaseGenerationResult:
      description: TestCaseGenerationResult
      properties:
        kind:
          const: test_case_generation
          default: test_case_generation
          title: Kind
          type: string
        test_case_generation_error:
          anyOf:
            - type: string
            - type: 'null'
          title: Test Case Generation Error
        test_cases:
          description: Test cases
          items:
            $ref: '#/components/schemas/TestCase'
          title: Test Cases
          type: array
      required:
        - test_cases
      title: TestCaseGenerationResult
      type: object
    PkInferenceResult:
      description: Primary key inference validation result
      properties:
        candidates_found:
          default: 0
          description: Number of PK candidates found during inference
          title: Candidates Found
          type: integer
        dataset:
          $ref: '#/components/schemas/Gfk_Union_Table__View__DfTable__'
          description: Dataset for which PK was inferred
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          title: Error Message
        inference_settings:
          anyOf:
            - $ref: '#/components/schemas/PkInferenceSettings'
            - type: 'null'
          description: Settings used to infer dataset PK
        inference_success:
          description: Whether PK inference succeeded
          title: Inference Success
          type: boolean
        inferred_pk_columns:
          anyOf:
            - items:
                type: string
              type: array
            - maxItems: 1
              minItems: 1
              prefixItems:
                - type: string
              type: array
            - type: 'null'
          title: Inferred Pk Columns
        kind:
          const: pk_inference
          default: pk_inference
          title: Kind
          type: string
        uniqueness_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Uniqueness Ratio
      required:
        - dataset
        - inference_success
      title: PkInferenceResult
      type: object
    ValidationStatus:
      enum:
        - pending
        - running
        - failed
        - success
      title: ValidationStatus
      type: string
    DataDiffResultValues:
      enum:
        - error
        - bad-pks
        - different
        - missing-pks
        - identical
        - empty
      title: DataDiffResultValues
      type: string
    Gfk_DfTable_:
      maxItems: 2
      minItems: 2
      prefixItems:
        - title: Kind
          type: string
        - title: Fk
          type: string
      type: array
    GeneralReviewComment:
      properties:
        comment:
          title: Comment
          type: string
        comment_kind:
          const: global
          default: global
          title: Comment Kind
          type: string
      required:
        - comment
      title: GeneralReviewComment
      type: object
    CodeChunkComment:
      properties:
        comment:
          title: Comment
          type: string
        comment_kind:
          const: code_chunk
          default: code_chunk
          title: Comment Kind
          type: string
        end_line_no:
          title: End Line No
          type: integer
        start_line_no:
          title: Start Line No
          type: integer
      required:
        - start_line_no
        - end_line_no
        - comment
      title: CodeChunkComment
      type: object
    ReviewStatus:
      enum:
        - signed_off
        - adjustments_needed
      title: ReviewStatus
      type: string
    User:
      properties:
        agent_kind:
          const: human
          default: human
          title: Agent Kind
          type: string
        user_id:
          title: User Id
          type: integer
      required:
        - user_id
      title: User
      type: object
    AIAgent:
      properties:
        agent_description:
          title: Agent Description
          type: string
        agent_kind:
          const: ai_agent
          default: ai_agent
          title: Agent Kind
          type: string
      required:
        - agent_description
      title: AIAgent
      type: object
    Gfk_ExecutionGroup_:
      maxItems: 2
      minItems: 2
      prefixItems:
        - title: Kind
          type: string
        - title: Fk
          type: string
      type: array
    Gfk_ExecutionResultSet_:
      maxItems: 2
      minItems: 2
      prefixItems:
        - title: Kind
          type: string
        - title: Fk
          type: string
      type: array
    ExecutionErrorInfo:
      properties:
        compiled_sql:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            Compiled SQL (with Jinja resolved) if available, useful for
            debugging syntax errors
          title: Compiled Sql
        error_message:
          description: Error received when trying to execute the step
          title: Error Message
          type: string
        execution_step:
          $ref: '#/components/schemas/Gfk_SqlExecutionStep_'
          description: Execution step that failed to execute
      required:
        - execution_step
        - error_message
      title: ExecutionErrorInfo
      type: object
    TestCase:
      description: >-
        TestCase for validating a number of transformed SQL operations.


        TestCase provides full data environment required to execute transformed
        SQL

        operations in the Target system, and captured "reference" state of the

        system after the code gets executed.


        Testcase is generated based on list of operations in the Source system
        that

        we want to test, and a mapping between objects in the Source and Target
        systems.

        The mapping is nessesary for us to know where to copy the data, and to
        formulate

        the test in terms of objects in the Target system, so it's ready to use.


        `before` and `after` represent (relevant) state of the system before and
        after the

        code gets executed. They are maps between:
         - "canonical" object ref in the system where the test case is to be executed.
            E.g. if it's a test built for Target system, then those names reference
            Target system objects.
         - value is where the actual data is stored.

        NOTE:

        - DfTables in `before` are in the Target system so that we can readily
        execute
          transformed code with zero friction.
        - DfTables in `after` may be in the Source or Target system, depending
        on `config`.
          We usually don't care much, since we have cross-db diffs. In some cases, though,
          we copy the data over to use in-db diffs. Sometimes in Live mode we can't connect
          to the Source system at all, so we are forced to use Target system from the start.

        This node is linked to:
         - Self -InputOf-> ExecutionGroup (which execution group this tests)
      properties:
        computed_pk:
          default: '--invalid-pk-you-shouldn''t-be-seeing-this-ever--'
          title: Computed Pk
          type: string
        config:
          discriminator:
            mapping:
              live_full_rebuild: '#/components/schemas/LiveFullRebuildConfig'
              live_incremental: '#/components/schemas/LiveIncrementalConfig'
              sandboxed_full_rebuild: '#/components/schemas/SandboxedFullRebuildConfig'
              sandboxed_incremental: '#/components/schemas/SandboxedIncrementalConfig'
            propertyName: kind
          oneOf:
            - $ref: '#/components/schemas/SandboxedFullRebuildConfig'
            - $ref: '#/components/schemas/SandboxedIncrementalConfig'
            - $ref: '#/components/schemas/LiveFullRebuildConfig'
            - $ref: '#/components/schemas/LiveIncrementalConfig'
          title: Config
        debug:
          additionalProperties: true
          description: Debug information
          title: Debug
          type: object
        expanded_config:
          anyOf:
            - discriminator:
                mapping:
                  live_full_rebuild: '#/components/schemas/LiveFullRebuildConfig'
                  live_incremental: '#/components/schemas/LiveIncrementalConfig'
                  sandboxed_full_rebuild: '#/components/schemas/SandboxedFullRebuildConfig'
                  sandboxed_incremental: '#/components/schemas/SandboxedIncrementalConfig'
                propertyName: kind
              oneOf:
                - $ref: '#/components/schemas/SandboxedFullRebuildConfig'
                - $ref: '#/components/schemas/SandboxedIncrementalConfig'
                - $ref: '#/components/schemas/LiveFullRebuildConfig'
                - $ref: '#/components/schemas/LiveIncrementalConfig'
            - type: 'null'
          title: Expanded Config
        expected_outputs:
          additionalProperties:
            $ref: '#/components/schemas/Gfk_DfTable_'
          propertyNames:
            $ref: '#/components/schemas/Gfk_Union_Table__View__'
          title: Expected Outputs
          type: object
        inputs:
          additionalProperties:
            $ref: '#/components/schemas/Gfk_DfTable_'
          propertyNames:
            $ref: '#/components/schemas/Gfk_Union_Table__View__'
          title: Inputs
          type: object
        is_complete:
          default: true
          title: Is Complete
          type: boolean
        order:
          default: 0
          title: Order
          type: integer
        side:
          $ref: '#/components/schemas/SideEnum'
          default: target
        tags:
          items:
            type: string
          title: Tags
          type: array
          uniqueItems: true
        uuid:
          format: uuid4
          title: Uuid
          type: string
      required:
        - inputs
        - expected_outputs
        - config
      title: TestCase
      type: object
    Gfk_Union_Table__View__DfTable__:
      maxItems: 2
      minItems: 2
      prefixItems:
        - title: Kind
          type: string
        - title: Fk
          type: string
      type: array
    PkInferenceSettings:
      properties:
        allow_null_pks:
          default: false
          title: Allow Null Pks
          type: boolean
        excluded_columns:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Excluded Columns
      title: PkInferenceSettings
      type: object
    Gfk_SqlExecutionStep_:
      maxItems: 2
      minItems: 2
      prefixItems:
        - title: Kind
          type: string
        - title: Fk
          type: string
      type: array
    SandboxedFullRebuildConfig:
      description: >-
        Our usual when we can run operations at the source.

        - Collect input data at the source,

        - Execute operations,

        - Copy the data to the destination (we can optionally copy the outputs
        to use
          for in-db diffs instead of cross-db diffs),
      properties:
        collect_at_destination:
          $ref: '#/components/schemas/CollectAtDestinationOptions'
          default: inputs
        kind:
          const: sandboxed_full_rebuild
          default: sandboxed_full_rebuild
          title: Kind
          type: string
        max_synth_scenarios:
          default: 0
          title: Max Synth Scenarios
          type: integer
        source:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/TakeSample'
            - $ref: '#/components/schemas/Synthesize'
            - $ref: '#/components/schemas/GroupDownsample'
            - $ref: '#/components/schemas/PointToData'
          title: Source
      required:
        - source
      title: SandboxedFullRebuildConfig
      type: object
    SandboxedIncrementalConfig:
      description: >-
        Use to test incremental logic, when existing tables are updated with new
        data.


        At t1 we collect outputs in the source data. At t2 we collect inputs,

        so that they have additional data (hopefully).
      properties:
        collect_at_destination:
          $ref: '#/components/schemas/CollectAtDestinationOptions'
          default: inputs
        kind:
          const: sandboxed_incremental
          default: sandboxed_incremental
          title: Kind
          type: string
        max_synth_scenarios:
          default: 0
          title: Max Synth Scenarios
          type: integer
        source_t1:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
          title: Source T1
        source_t2:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
          title: Source T2
      required:
        - source_t1
        - source_t2
      title: SandboxedIncrementalConfig
      type: object
    LiveFullRebuildConfig:
      description: |-
        Live mode where we can't run anything at the source, and instead we are
        comparing our results with live prod data, expecting some drift.

        We support few modes here:
        - we can freeze source data and copy it to the destination ourselves,
        - we can point to live prod data & do copy of that,
        - we can skip data collection at source entrirely, and rely
          on data captured at destination for both inputs and outputs,
          if the customer copied the data over already.

        One fundamental problem with Live mode is that it's not usually enough
        to capture data as-is and call it a day. If we do it, then data "before"
        and "after" execution will be the same, and no-op translation (that does
        literally nothing)will be accepted by validator just fine.

        So we usually have to mangle the data somehow, e.g. "truncate"
        the tables that are supposed to be outputs, or chip off some portion
        of the data (e.g. for the last couple of days).
      properties:
        collect_at_destination:
          $ref: '#/components/schemas/CollectAtDestinationOptions'
          default: inputs
        destination_after:
          discriminator:
            mapping:
              apply_sql_filter: '#/components/schemas/ApplySqlFilter'
              copy_data: '#/components/schemas/CopyData'
              freeze: '#/components/schemas/Freeze'
              multiplex_on_mutability: '#/components/schemas/MultiplexOnMutability'
              point_to_data: '#/components/schemas/PointToData'
            propertyName: kind
          oneOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/MultiplexOnMutability'
            - $ref: '#/components/schemas/ApplySqlFilter'
            - $ref: '#/components/schemas/CopyData'
          title: Destination After
        destination_before:
          discriminator:
            mapping:
              apply_sql_filter: '#/components/schemas/ApplySqlFilter'
              copy_data: '#/components/schemas/CopyData'
              freeze: '#/components/schemas/Freeze'
              multiplex_on_mutability: '#/components/schemas/MultiplexOnMutability'
              point_to_data: '#/components/schemas/PointToData'
            propertyName: kind
          oneOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/MultiplexOnMutability'
            - $ref: '#/components/schemas/ApplySqlFilter'
            - $ref: '#/components/schemas/CopyData'
          title: Destination Before
        kind:
          const: live_full_rebuild
          default: live_full_rebuild
          title: Kind
          type: string
        max_synth_scenarios:
          default: 0
          title: Max Synth Scenarios
          type: integer
        source_after:
          anyOf:
            - discriminator:
                mapping:
                  apply_sql_filter: '#/components/schemas/ApplySqlFilter'
                  freeze: '#/components/schemas/Freeze'
                  multiplex_on_mutability: '#/components/schemas/MultiplexOnMutability'
                  point_to_data: '#/components/schemas/PointToData'
                propertyName: kind
              oneOf:
                - $ref: '#/components/schemas/Freeze'
                - $ref: '#/components/schemas/PointToData'
                - $ref: '#/components/schemas/MultiplexOnMutability'
                - $ref: '#/components/schemas/ApplySqlFilter'
            - type: 'null'
          title: Source After
        source_before:
          anyOf:
            - discriminator:
                mapping:
                  apply_sql_filter: '#/components/schemas/ApplySqlFilter'
                  freeze: '#/components/schemas/Freeze'
                  multiplex_on_mutability: '#/components/schemas/MultiplexOnMutability'
                  point_to_data: '#/components/schemas/PointToData'
                propertyName: kind
              oneOf:
                - $ref: '#/components/schemas/Freeze'
                - $ref: '#/components/schemas/PointToData'
                - $ref: '#/components/schemas/MultiplexOnMutability'
                - $ref: '#/components/schemas/ApplySqlFilter'
            - type: 'null'
          title: Source Before
      required:
        - source_before
        - source_after
        - destination_before
        - destination_after
      title: LiveFullRebuildConfig
      type: object
    LiveIncrementalConfig:
      description: >-
        Use to test incremental logic, when existing tables are updated with new
        data.


        At t1 we collect outputs in the source data. At t2 we collect inputs,

        so that they have additional data (hopefully).
      properties:
        collect_at_destination:
          $ref: '#/components/schemas/CollectAtDestinationOptions'
          default: inputs
        destination_t1:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/CopyData'
          title: Destination T1
        destination_t2:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/CopyData'
          title: Destination T2
        kind:
          const: live_incremental
          default: live_incremental
          title: Kind
          type: string
        max_synth_scenarios:
          default: 0
          title: Max Synth Scenarios
          type: integer
        source_t1:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - type: 'null'
          title: Source T1
        source_t2:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - type: 'null'
          title: Source T2
      required:
        - source_t1
        - source_t2
        - destination_t1
        - destination_t2
      title: LiveIncrementalConfig
      type: object
    CollectAtDestinationOptions:
      description: >-
        To verify transforms at the destination, we require Inputs to be there.


        We can optionally collect also "Asset" datasets. If we do it, then we
        can

        use in-db diffs instead of cross-db diffs.


        Additionally we can copy / collect everything that's referenced, just in
        case.

        We don't care about non-asset outputs, but in presense of bugs we might
        want

        to copy everything that's possibly related to have a full set of data.

        We'll be more safe if we discover later that we got some mutability
        wrong,

        etc.


        How exactly collection is done (is it freeze, copy, etc.) is determined
        by testcase

        config.
      enum:
        - inputs
        - inputs_and_asset_results
        - inputs_and_all_results
      title: CollectAtDestinationOptions
      type: string
    Freeze:
      additionalProperties: false
      description: Create an immutable copy of a table/view.
      properties:
        end_time:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: End Time
        kind:
          const: freeze
          default: freeze
          title: Kind
          type: string
        source_path_remap_label:
          anyOf:
            - type: string
            - type: 'null'
          title: Source Path Remap Label
        start_time:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Start Time
      title: Freeze
      type: object
    TakeSample:
      additionalProperties: false
      description: >-
        Uncorrelated sampling, ranges from "pick whatever N rows" to "pick N
        rows pseudo-randomly".
      properties:
        kind:
          const: take_sample
          default: take_sample
          title: Kind
          type: string
        method:
          $ref: '#/components/schemas/SimpleSamplingMethod'
        target_sample_size:
          title: Target Sample Size
          type: integer
      required:
        - target_sample_size
        - method
      title: TakeSample
      type: object
    Synthesize:
      additionalProperties: false
      description: Generate a set of data with LLM. It's specific to an execution group.
      properties:
        fail_on_incomplete_data:
          title: Fail On Incomplete Data
          type: boolean
        kind:
          const: synthesize
          default: synthesize
          title: Kind
          type: string
        max_iterations_per_table:
          title: Max Iterations Per Table
          type: integer
        maximum_rows:
          title: Maximum Rows
          type: integer
        minimum_rows:
          title: Minimum Rows
          type: integer
        scenario:
          anyOf:
            - $ref: '#/components/schemas/Scenario'
            - type: 'null'
      required:
        - minimum_rows
        - maximum_rows
        - max_iterations_per_table
        - fail_on_incomplete_data
      title: Synthesize
      type: object
    GroupDownsample:
      additionalProperties: false
      description: >-
        Take a sample out of data produced by any sampler of execution group
        scope type.

        We are using this to generate ad-hoc data to test incrementals.
      properties:
        base:
          $ref: '#/components/schemas/Synthesize'
        kind:
          const: group_downsample
          default: group_downsample
          title: Kind
          type: string
        ratio:
          title: Ratio
          type: number
      required:
        - base
        - ratio
      title: GroupDownsample
      type: object
    PointToData:
      additionalProperties: false
      description: |-
        Just point to existing tables / views.
        They could be live prod data, or data pre-frozen by us or customer.

        TODO: what about pointing to dftable if it's same db?
      properties:
        kind:
          const: point_to_data
          default: point_to_data
          title: Kind
          type: string
        source_path_remap_label:
          anyOf:
            - type: string
            - type: 'null'
          title: Source Path Remap Label
      title: PointToData
      type: object
    MultiplexOnMutability:
      additionalProperties: false
      description: |-
        Collection of unholy ad-hoc data mangling strategies, mostly for
        Live Full Rebuild mode.

        V1 is here since I expect this to be disposable.
        Alternative approach could be providing name of
      properties:
        kind:
          const: multiplex_on_mutability
          default: multiplex_on_mutability
          title: Kind
          type: string
        read_only:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/CreateEmptyDataset'
            - $ref: '#/components/schemas/ApplySqlFilter'
          title: Read Only
        read_write:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/CreateEmptyDataset'
            - $ref: '#/components/schemas/ApplySqlFilter'
          title: Read Write
        write_only:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
            - $ref: '#/components/schemas/CreateEmptyDataset'
            - $ref: '#/components/schemas/ApplySqlFilter'
          title: Write Only
      required:
        - read_only
        - write_only
        - read_write
      title: MultiplexOnMutability
      type: object
    ApplySqlFilter:
      additionalProperties: false
      description: Filter data with a SQL query.
      properties:
        base:
          anyOf:
            - $ref: '#/components/schemas/Freeze'
            - $ref: '#/components/schemas/PointToData'
          title: Base
        kind:
          const: apply_sql_filter
          default: apply_sql_filter
          title: Kind
          type: string
        label:
          title: Label
          type: string
        where_clause:
          title: Where Clause
          type: string
      required:
        - label
        - base
        - where_clause
      title: ApplySqlFilter
      type: object
    CopyData:
      additionalProperties: false
      description: >-
        Copy data from one database to another.

        This might not belong here, actually, and may be need to moved to
        testcases.
      properties:
        kind:
          const: copy_data
          default: copy_data
          title: Kind
          type: string
      title: CopyData
      type: object
    SimpleSamplingMethod:
      enum:
        - limit
        - system
        - pseudo_random
      title: SimpleSamplingMethod
      type: string
    Scenario:
      description: >-
        Describes what aspect of a query should be tested.


        Not a Node - just a structured data type embedded in TestCase and
        Synthesize.

        Used for type safety and caching (frozen model enables equality
        comparison).


        ARCHITECTURE NOTE:

        Currently the full Scenario is embedded in Synthesize, making it part of

        DataCollectionConfigNode's cache key. This works because all Scenario
        fields

        currently affect data generation.


        FUTURE: If we add fields that don't affect data (e.g., parameters or
        vars) but

        would be executed against the same data, different query branches, we
        could:

        1. Add a `data_cache_key` property that hashes only data-affecting
        fields of the scenario

        2. Modify caching in get_or_create_options_node() to use the
        data_cache_key property
      properties:
        prompt:
          title: Prompt
          type: string
        source:
          default: llm
          enum:
            - llm
            - project_setting
            - synthetic
          title: Source
          type: string
      required:
        - prompt
      title: Scenario
      type: object
    CreateEmptyDataset:
      additionalProperties: false
      description: >-
        Create an empty dataset with same schema as the source dataset but with
        no data.
      properties:
        kind:
          const: create_empty_dataset
          default: create_empty_dataset
          title: Kind
          type: string
      title: CreateEmptyDataset
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````