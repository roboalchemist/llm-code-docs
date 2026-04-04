# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/automations/create-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Automation

> Create an automation.

For more information, see https://docs.prefect.io/v3/concepts/automations.



## OpenAPI

````yaml post /automations/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /automations/:
    post:
      tags:
        - Automations
      summary: Create Automation
      description: >-
        Create an automation.


        For more information, see
        https://docs.prefect.io/v3/concepts/automations.
      operationId: create_automation_automations__post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomationCreate'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Automation'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    AutomationCreate:
      properties:
        name:
          type: string
          title: Name
          description: The name of this automation
        description:
          type: string
          title: Description
          description: A longer description of this automation
          default: ''
        enabled:
          type: boolean
          title: Enabled
          description: Whether this automation will be evaluated
          default: true
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags associated with this automation
        trigger:
          anyOf:
            - $ref: '#/components/schemas/EventTrigger'
            - $ref: '#/components/schemas/CompoundTrigger-Input'
            - $ref: '#/components/schemas/SequenceTrigger-Input'
          title: Trigger
          description: >-
            The criteria for which events this Automation covers and how it will
            respond to the presence or absence of those events
        actions:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions
          description: The actions to perform when this Automation triggers
        actions_on_trigger:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions On Trigger
          description: >-
            The actions to perform when an Automation goes into a triggered
            state
        actions_on_resolve:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions On Resolve
          description: >-
            The actions to perform when an Automation goes into a resolving
            state
        owner_resource:
          anyOf:
            - type: string
            - type: 'null'
          title: Owner Resource
          description: The resource to which this automation belongs
      additionalProperties: false
      type: object
      required:
        - name
        - trigger
        - actions
      title: AutomationCreate
    Automation:
      properties:
        name:
          type: string
          title: Name
          description: The name of this automation
        description:
          type: string
          title: Description
          description: A longer description of this automation
          default: ''
        enabled:
          type: boolean
          title: Enabled
          description: Whether this automation will be evaluated
          default: true
        tags:
          items:
            type: string
          type: array
          title: Tags
          description: A list of tags associated with this automation
        trigger:
          anyOf:
            - $ref: '#/components/schemas/EventTrigger'
            - $ref: '#/components/schemas/CompoundTrigger-Output'
            - $ref: '#/components/schemas/SequenceTrigger-Output'
          title: Trigger
          description: >-
            The criteria for which events this Automation covers and how it will
            respond to the presence or absence of those events
        actions:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions
          description: The actions to perform when this Automation triggers
        actions_on_trigger:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions On Trigger
          description: >-
            The actions to perform when an Automation goes into a triggered
            state
        actions_on_resolve:
          items:
            anyOf:
              - $ref: '#/components/schemas/DoNothing'
              - $ref: '#/components/schemas/RunDeployment'
              - $ref: '#/components/schemas/PauseDeployment'
              - $ref: '#/components/schemas/ResumeDeployment'
              - $ref: '#/components/schemas/CancelFlowRun'
              - $ref: '#/components/schemas/ChangeFlowRunState'
              - $ref: '#/components/schemas/PauseWorkQueue'
              - $ref: '#/components/schemas/ResumeWorkQueue'
              - $ref: '#/components/schemas/SendNotification'
              - $ref: '#/components/schemas/CallWebhook'
              - $ref: '#/components/schemas/PauseAutomation'
              - $ref: '#/components/schemas/ResumeAutomation'
              - $ref: '#/components/schemas/SuspendFlowRun'
              - $ref: '#/components/schemas/ResumeFlowRun'
              - $ref: '#/components/schemas/PauseWorkPool'
              - $ref: '#/components/schemas/ResumeWorkPool'
          type: array
          title: Actions On Resolve
          description: >-
            The actions to perform when an Automation goes into a resolving
            state
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
      type: object
      required:
        - name
        - trigger
        - actions
        - id
        - created
        - updated
      title: Automation
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    EventTrigger:
      properties:
        type:
          type: string
          const: event
          title: Type
          default: event
        id:
          type: string
          format: uuid
          title: Id
          description: The unique ID of this trigger
        match:
          $ref: '#/components/schemas/ResourceSpecification'
          description: Labels for resources which this trigger will match.
        match_related:
          anyOf:
            - $ref: '#/components/schemas/ResourceSpecification'
            - items:
                $ref: '#/components/schemas/ResourceSpecification'
              type: array
          title: Match Related
          description: Labels for related resources which this trigger will match.
        after:
          items:
            type: string
          type: array
          uniqueItems: true
          title: After
          description: >-
            The event(s) which must first been seen to fire this trigger.  If
            empty, then fire this trigger immediately.  Events may include
            trailing wildcards, like `prefect.flow-run.*`
        expect:
          items:
            type: string
          type: array
          uniqueItems: true
          title: Expect
          description: >-
            The event(s) this trigger is expecting to see.  If empty, this
            trigger will match any event.  Events may include trailing
            wildcards, like `prefect.flow-run.*`
        for_each:
          items:
            type: string
          type: array
          uniqueItems: true
          title: For Each
          description: >-
            Evaluate the trigger separately for each distinct value of these
            labels on the resource.  By default, labels refer to the primary
            resource of the triggering event.  You may also refer to labels from
            related resources by specifying `related:<role>:<label>`.  This will
            use the value of that label for the first related resource in that
            role.  For example, `"for_each":
            ["related:flow:prefect.resource.id"]` would evaluate the trigger for
            each flow.
        posture:
          type: string
          enum:
            - Reactive
            - Proactive
          title: Posture
          description: >-
            The posture of this trigger, either Reactive or Proactive.  Reactive
            triggers respond to the _presence_ of the expected events, while
            Proactive triggers respond to the _absence_ of those expected
            events.
        threshold:
          type: integer
          title: Threshold
          description: >-
            The number of events required for this trigger to fire (for Reactive
            triggers), or the number of events expected (for Proactive triggers)
          default: 1
        within:
          type: number
          title: Within
          description: >-
            The time period over which the events must occur.  For Reactive
            triggers, this may be as low as 0 seconds, but must be at least 10
            seconds for Proactive triggers
          default: 0
      type: object
      required:
        - posture
      title: EventTrigger
      description: >-
        A trigger that fires based on the presence or absence of events within a
        given

        period of time.
    CompoundTrigger-Input:
      properties:
        type:
          type: string
          const: compound
          title: Type
          default: compound
        id:
          type: string
          format: uuid
          title: Id
          description: The unique ID of this trigger
        triggers:
          items:
            anyOf:
              - $ref: '#/components/schemas/EventTrigger'
              - $ref: '#/components/schemas/CompoundTrigger-Input'
              - $ref: '#/components/schemas/SequenceTrigger-Input'
          type: array
          title: Triggers
        within:
          anyOf:
            - type: number
            - type: 'null'
          title: Within
        require:
          anyOf:
            - type: integer
            - type: string
              enum:
                - any
                - all
          title: Require
      type: object
      required:
        - triggers
        - within
        - require
      title: CompoundTrigger
      description: |-
        A composite trigger that requires some number of triggers to have
        fired within the given time period
    SequenceTrigger-Input:
      properties:
        type:
          type: string
          const: sequence
          title: Type
          default: sequence
        id:
          type: string
          format: uuid
          title: Id
          description: The unique ID of this trigger
        triggers:
          items:
            anyOf:
              - $ref: '#/components/schemas/EventTrigger'
              - $ref: '#/components/schemas/CompoundTrigger-Input'
              - $ref: '#/components/schemas/SequenceTrigger-Input'
          type: array
          title: Triggers
        within:
          anyOf:
            - type: number
            - type: 'null'
          title: Within
      type: object
      required:
        - triggers
        - within
      title: SequenceTrigger
      description: |-
        A composite trigger that requires some number of triggers to have fired
        within the given time period in a specific order
    DoNothing:
      properties:
        type:
          type: string
          const: do-nothing
          title: Type
          default: do-nothing
      type: object
      title: DoNothing
      description: Do nothing when an Automation is triggered
    RunDeployment:
      properties:
        type:
          type: string
          const: run-deployment
          title: Type
          default: run-deployment
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected deployment (given
            by `deployment_id`), or to a deployment that is inferred from the
            triggering event.  If the source is 'inferred', the `deployment_id`
            may not be set.  If the source is 'selected', the `deployment_id`
            must be set.
          default: selected
        deployment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Id
          description: The identifier of the deployment
        parameters:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Parameters
          description: >-
            The parameters to pass to the deployment, or None to use the
            deployment's default parameters
        job_variables:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Job Variables
          description: >-
            The job variables to pass to the created flow run, or None to use
            the deployment's default job variables
        schedule_after:
          type: number
          title: Schedule After
          description: >-
            The amount of time to wait before running the deployment. Defaults
            to running the deployment immediately.
      type: object
      title: RunDeployment
      description: Runs the given deployment with the given parameters
    PauseDeployment:
      properties:
        type:
          type: string
          const: pause-deployment
          title: Type
          default: pause-deployment
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected deployment (given
            by `deployment_id`), or to a deployment that is inferred from the
            triggering event.  If the source is 'inferred', the `deployment_id`
            may not be set.  If the source is 'selected', the `deployment_id`
            must be set.
          default: selected
        deployment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Id
          description: The identifier of the deployment
      type: object
      title: PauseDeployment
      description: Pauses the given Deployment
    ResumeDeployment:
      properties:
        type:
          type: string
          const: resume-deployment
          title: Type
          default: resume-deployment
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected deployment (given
            by `deployment_id`), or to a deployment that is inferred from the
            triggering event.  If the source is 'inferred', the `deployment_id`
            may not be set.  If the source is 'selected', the `deployment_id`
            must be set.
          default: selected
        deployment_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Deployment Id
          description: The identifier of the deployment
      type: object
      title: ResumeDeployment
      description: Resumes the given Deployment
    CancelFlowRun:
      properties:
        type:
          type: string
          const: cancel-flow-run
          title: Type
          default: cancel-flow-run
      type: object
      title: CancelFlowRun
      description: Cancels a flow run associated with the trigger
    ChangeFlowRunState:
      properties:
        type:
          type: string
          const: change-flow-run-state
          title: Type
          default: change-flow-run-state
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: The name of the state to change the flow run to
        state:
          $ref: '#/components/schemas/StateType'
          description: The type of the state to change the flow run to
        message:
          anyOf:
            - type: string
            - type: 'null'
          title: Message
          description: An optional message to associate with the state change
        force:
          type: boolean
          title: Force
          description: Force the state change even if the transition is not allowed
          default: false
      type: object
      required:
        - state
      title: ChangeFlowRunState
      description: Changes the state of a flow run associated with the trigger
    PauseWorkQueue:
      properties:
        type:
          type: string
          const: pause-work-queue
          title: Type
          default: pause-work-queue
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected work queue (given
            by `work_queue_id`), or to a work queue that is inferred from the
            triggering event.  If the source is 'inferred', the `work_queue_id`
            may not be set.  If the source is 'selected', the `work_queue_id`
            must be set.
          default: selected
        work_queue_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Queue Id
          description: The identifier of the work queue to pause
      type: object
      title: PauseWorkQueue
      description: Pauses a Work Queue
    ResumeWorkQueue:
      properties:
        type:
          type: string
          const: resume-work-queue
          title: Type
          default: resume-work-queue
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected work queue (given
            by `work_queue_id`), or to a work queue that is inferred from the
            triggering event.  If the source is 'inferred', the `work_queue_id`
            may not be set.  If the source is 'selected', the `work_queue_id`
            must be set.
          default: selected
        work_queue_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Queue Id
          description: The identifier of the work queue to pause
      type: object
      title: ResumeWorkQueue
      description: Resumes a Work Queue
    SendNotification:
      properties:
        type:
          type: string
          const: send-notification
          title: Type
          default: send-notification
        block_document_id:
          type: string
          format: uuid
          title: Block Document Id
          description: The identifier of the notification block to use
        subject:
          type: string
          title: Subject
          default: Prefect automated notification
        body:
          type: string
          title: Body
          description: The text of the notification to send
      type: object
      required:
        - block_document_id
        - body
      title: SendNotification
      description: Send a notification when an Automation is triggered
    CallWebhook:
      properties:
        type:
          type: string
          const: call-webhook
          title: Type
          default: call-webhook
        block_document_id:
          type: string
          format: uuid
          title: Block Document Id
          description: The identifier of the webhook block to use
        payload:
          type: string
          title: Payload
          description: An optional templatable payload to send when calling the webhook.
          default: ''
      type: object
      required:
        - block_document_id
      title: CallWebhook
      description: Call a webhook when an Automation is triggered.
    PauseAutomation:
      properties:
        type:
          type: string
          const: pause-automation
          title: Type
          default: pause-automation
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected automation (given
            by `automation_id`), or to an automation that is inferred from the
            triggering event.  If the source is 'inferred', the `automation_id`
            may not be set.  If the source is 'selected', the `automation_id`
            must be set.
          default: selected
        automation_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Automation Id
          description: The identifier of the automation to act on
      type: object
      title: PauseAutomation
      description: Pauses a Work Queue
    ResumeAutomation:
      properties:
        type:
          type: string
          const: resume-automation
          title: Type
          default: resume-automation
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected automation (given
            by `automation_id`), or to an automation that is inferred from the
            triggering event.  If the source is 'inferred', the `automation_id`
            may not be set.  If the source is 'selected', the `automation_id`
            must be set.
          default: selected
        automation_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Automation Id
          description: The identifier of the automation to act on
      type: object
      title: ResumeAutomation
      description: Resumes a Work Queue
    SuspendFlowRun:
      properties:
        type:
          type: string
          const: suspend-flow-run
          title: Type
          default: suspend-flow-run
      type: object
      title: SuspendFlowRun
      description: Suspends a flow run associated with the trigger
    ResumeFlowRun:
      properties:
        type:
          type: string
          const: resume-flow-run
          title: Type
          default: resume-flow-run
      type: object
      title: ResumeFlowRun
      description: Resumes a paused or suspended flow run associated with the trigger
    PauseWorkPool:
      properties:
        type:
          type: string
          const: pause-work-pool
          title: Type
          default: pause-work-pool
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected work pool (given
            by `work_pool_id`), or to a work pool that is inferred from the
            triggering event.  If the source is 'inferred', the `work_pool_id`
            may not be set.  If the source is 'selected', the `work_pool_id`
            must be set.
          default: selected
        work_pool_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Pool Id
          description: The identifier of the work pool to pause
      type: object
      title: PauseWorkPool
      description: Pauses a Work Pool
    ResumeWorkPool:
      properties:
        type:
          type: string
          const: resume-work-pool
          title: Type
          default: resume-work-pool
        source:
          type: string
          enum:
            - selected
            - inferred
          title: Source
          description: >-
            Whether this Action applies to a specific selected work pool (given
            by `work_pool_id`), or to a work pool that is inferred from the
            triggering event.  If the source is 'inferred', the `work_pool_id`
            may not be set.  If the source is 'selected', the `work_pool_id`
            must be set.
          default: selected
        work_pool_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Pool Id
          description: The identifier of the work pool to pause
      type: object
      title: ResumeWorkPool
      description: Resumes a Work Pool
    CompoundTrigger-Output:
      properties:
        type:
          type: string
          const: compound
          title: Type
          default: compound
        id:
          type: string
          format: uuid
          title: Id
          description: The unique ID of this trigger
        triggers:
          items:
            anyOf:
              - $ref: '#/components/schemas/EventTrigger'
              - $ref: '#/components/schemas/CompoundTrigger-Output'
              - $ref: '#/components/schemas/SequenceTrigger-Output'
          type: array
          title: Triggers
        within:
          anyOf:
            - type: number
            - type: 'null'
          title: Within
        require:
          anyOf:
            - type: integer
            - type: string
              enum:
                - any
                - all
          title: Require
      type: object
      required:
        - triggers
        - within
        - require
      title: CompoundTrigger
      description: |-
        A composite trigger that requires some number of triggers to have
        fired within the given time period
    SequenceTrigger-Output:
      properties:
        type:
          type: string
          const: sequence
          title: Type
          default: sequence
        id:
          type: string
          format: uuid
          title: Id
          description: The unique ID of this trigger
        triggers:
          items:
            anyOf:
              - $ref: '#/components/schemas/EventTrigger'
              - $ref: '#/components/schemas/CompoundTrigger-Output'
              - $ref: '#/components/schemas/SequenceTrigger-Output'
          type: array
          title: Triggers
        within:
          anyOf:
            - type: number
            - type: 'null'
          title: Within
      type: object
      required:
        - triggers
        - within
      title: SequenceTrigger
      description: |-
        A composite trigger that requires some number of triggers to have fired
        within the given time period in a specific order
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
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    ResourceSpecification:
      additionalProperties:
        anyOf:
          - type: string
          - items:
              type: string
            type: array
      type: object
      title: ResourceSpecification
    StateType:
      type: string
      enum:
        - SCHEDULED
        - PENDING
        - RUNNING
        - COMPLETED
        - FAILED
        - CANCELLED
        - CRASHED
        - PAUSED
        - CANCELLING
      title: StateType
      description: Enumeration of state types.

````

Built with [Mintlify](https://mintlify.com).