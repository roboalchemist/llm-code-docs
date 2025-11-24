# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/creates-a-webhook.md

# Creates a webhook

> Creates a webhook

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/webhooks
paths:
  path: /v1/webhooks
  method: post
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query:
        teamId:
          schema:
            - type: string
              description: The Team identifier to perform the request on behalf of.
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        slug:
          schema:
            - type: string
              description: The Team slug to perform the request on behalf of.
              example: my-team-url-slug
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              url:
                allOf:
                  - format: uri
                    pattern: ^https?://
                    type: string
              events:
                allOf:
                  - minItems: 1
                    type: array
                    items:
                      type: string
                      enum:
                        - budget.reached
                        - budget.reset
                        - domain.created
                        - domain.dns.records.changed
                        - domain.transfer-in.started
                        - domain.transfer-in.completed
                        - domain.transfer-in.failed
                        - domain.certificate.add
                        - domain.certificate.add.failed
                        - domain.certificate.renew
                        - domain.certificate.renew.failed
                        - domain.certificate.deleted
                        - domain.renewal
                        - domain.renewal.failed
                        - domain.auto-renew.changed
                        - deployment.created
                        - deployment.cleanup
                        - deployment.error
                        - deployment.canceled
                        - deployment.succeeded
                        - deployment.ready
                        - deployment.check-rerequested
                        - deployment.promoted
                        - deployment.integration.action.start
                        - deployment.integration.action.cancel
                        - deployment.integration.action.cleanup
                        - deployment.checkrun.start
                        - deployment.checkrun.cancel
                        - edge-config.created
                        - edge-config.deleted
                        - edge-config.items.updated
                        - firewall.attack
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.domain.created
                        - project.domain.updated
                        - project.domain.deleted
                        - project.domain.verified
                        - project.domain.unverified
                        - project.domain.moved
                        - project.rolling-release.started
                        - project.rolling-release.aborted
                        - project.rolling-release.completed
                        - project.rolling-release.approved
                        - deployment.checks.failed
                        - deployment.checks.succeeded
                        - deployment-checks-completed
                        - deployment-ready
                        - deployment-prepared
                        - deployment-error
                        - deployment-check-rerequested
                        - deployment-canceled
                        - project-created
                        - project-removed
                        - domain-created
                        - deployment
                        - integration-configuration-permission-updated
                        - integration-configuration-removed
                        - integration-configuration-scope-change-confirmed
                        - marketplace.member.changed
                        - marketplace.invoice.created
                        - marketplace.invoice.paid
                        - marketplace.invoice.notpaid
                        - marketplace.invoice.refunded
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - observability.anomaly-botId
                        - test-webhook
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
                        budget.reset: BudgetReset
                        domain.created: DomainCreated
                        domain.dns.records.changed: DomainDnsRecordsChanged
                        domain.transfer-in.started: DomainTransferInStarted
                        domain.transfer-in.completed: DomainTransferInCompleted
                        domain.transfer-in.failed: DomainTransferInFailed
                        domain.certificate.add: DomainCertificateAdd
                        domain.certificate.add.failed: DomainCertificateAddFailed
                        domain.certificate.renew: DomainCertificateRenew
                        domain.certificate.renew.failed: DomainCertificateRenewFailed
                        domain.certificate.deleted: DomainCertificateDeleted
                        domain.renewal: DomainRenewal
                        domain.renewal.failed: DomainRenewalFailed
                        domain.auto-renew.changed: DomainAutoRenewChanged
                        deployment.created: DeploymentCreated
                        deployment.cleanup: DeploymentCleanup
                        deployment.error: DeploymentError
                        deployment.canceled: DeploymentCanceled
                        deployment.succeeded: DeploymentSucceeded
                        deployment.ready: DeploymentReady
                        deployment.check-rerequested: DeploymentCheckRerequested
                        deployment.promoted: DeploymentPromoted
                        deployment.integration.action.start: DeploymentIntegrationActionStart
                        deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                        deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                        deployment.checkrun.start: DeploymentCheckrunStart
                        deployment.checkrun.cancel: DeploymentCheckrunCancel
                        edge-config.created: EdgeConfigCreated
                        edge-config.deleted: EdgeConfigDeleted
                        edge-config.items.updated: EdgeConfigItemsUpdated
                        firewall.attack: FirewallAttack
                        integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                        integration-configuration.removed: IntegrationConfigurationRemoved
                        integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                        integration-resource.project-connected: IntegrationResourceProjectConnected
                        integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                        project.created: ProjectCreated
                        project.removed: ProjectRemoved
                        project.domain.created: ProjectDomainCreated
                        project.domain.updated: ProjectDomainUpdated
                        project.domain.deleted: ProjectDomainDeleted
                        project.domain.verified: ProjectDomainVerified
                        project.domain.unverified: ProjectDomainUnverified
                        project.domain.moved: ProjectDomainMoved
                        project.rolling-release.started: ProjectRollingReleaseStarted
                        project.rolling-release.aborted: ProjectRollingReleaseAborted
                        project.rolling-release.completed: ProjectRollingReleaseCompleted
                        project.rolling-release.approved: ProjectRollingReleaseApproved
                        deployment.checks.failed: DeploymentChecksFailed
                        deployment.checks.succeeded: DeploymentChecksSucceeded
                        deployment-checks-completed: DeploymentChecksCompleted
                        deployment-ready: DeploymentReadyHyphen
                        deployment-prepared: DeploymentPreparedHyphen
                        deployment-error: DeploymentErrorHyphen
                        deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                        deployment-canceled: DeploymentCanceledHyphen
                        project-created: ProjectCreatedHyphen
                        project-removed: ProjectRemovedHyphen
                        domain-created: DomainCreatedHyphen
                        deployment: Deployment
                        integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                        integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                        integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                        marketplace.invoice.created: MarketplaceInvoiceCreated
                        marketplace.invoice.paid: MarketplaceInvoicePaid
                        marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                        marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                        observability.anomaly: ObservabilityAnomaly
                        observability.anomaly-error: ObservabilityAnomalyError
                        test-webhook: TestWebhook
              projectIds:
                allOf:
                  - minItems: 1
                    maxItems: 50
                    type: array
                    items:
                      pattern: ^[a-zA-z0-9_]+$
                      type: string
            required: true
            requiredProperties:
              - url
              - events
            additionalProperties: false
        examples:
          example:
            value:
              url: <string>
              events:
                - budget.reached
              projectIds:
                - <string>
    codeSamples:
      - label: createWebhook
        lang: go
        source: "package main\n\nimport(\n\t\"os\"\n\t\"github.com/vercel/vercel\"\n\t\"context\"\n\t\"log\"\n)\n\nfunc main() {\n    s := vercel.New(\n        vercel.WithSecurity(os.Getenv(\"VERCEL_BEARER_TOKEN\")),\n    )\n\n    ctx := context.Background()\n    res, err := s.Webhooks.CreateWebhook(ctx, nil, nil, nil)\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.Object != nil {\n        // handle response\n    }\n}"
      - label: createWebhook
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.webhooks.createWebhook({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              slug: "my-team-url-slug",
              requestBody: {
                url: "https://experienced-sailor.biz/",
                events: [
                  "domain.auto-renew.changed",
                ],
              },
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              secret:
                allOf:
                  - type: string
                    description: The webhook secret used to sign the payload
              events:
                allOf:
                  - items:
                      type: string
                      enum:
                        - budget.reached
                        - budget.reset
                        - domain.created
                        - domain.dns.records.changed
                        - domain.transfer-in.started
                        - domain.transfer-in.completed
                        - domain.transfer-in.failed
                        - domain.certificate.add
                        - domain.certificate.add.failed
                        - domain.certificate.renew
                        - domain.certificate.renew.failed
                        - domain.certificate.deleted
                        - domain.renewal
                        - domain.renewal.failed
                        - domain.auto-renew.changed
                        - deployment.created
                        - deployment.cleanup
                        - deployment.error
                        - deployment.canceled
                        - deployment.succeeded
                        - deployment.ready
                        - deployment.check-rerequested
                        - deployment.promoted
                        - deployment.integration.action.start
                        - deployment.integration.action.cancel
                        - deployment.integration.action.cleanup
                        - deployment.checkrun.start
                        - deployment.checkrun.cancel
                        - edge-config.created
                        - edge-config.deleted
                        - edge-config.items.updated
                        - firewall.attack
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.domain.created
                        - project.domain.updated
                        - project.domain.deleted
                        - project.domain.verified
                        - project.domain.unverified
                        - project.domain.moved
                        - project.rolling-release.started
                        - project.rolling-release.aborted
                        - project.rolling-release.completed
                        - project.rolling-release.approved
                        - deployment.checks.failed
                        - deployment.checks.succeeded
                        - deployment-checks-completed
                        - deployment-ready
                        - deployment-prepared
                        - deployment-error
                        - deployment-check-rerequested
                        - deployment-canceled
                        - project-created
                        - project-removed
                        - domain-created
                        - deployment
                        - integration-configuration-permission-updated
                        - integration-configuration-removed
                        - integration-configuration-scope-change-confirmed
                        - marketplace.member.changed
                        - marketplace.invoice.created
                        - marketplace.invoice.paid
                        - marketplace.invoice.notpaid
                        - marketplace.invoice.refunded
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - observability.anomaly-botId
                        - test-webhook
                      description: The webhooks events
                      example: deployment.created
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
                        budget.reset: BudgetReset
                        domain.created: DomainCreated
                        domain.dns.records.changed: DomainDnsRecordsChanged
                        domain.transfer-in.started: DomainTransferInStarted
                        domain.transfer-in.completed: DomainTransferInCompleted
                        domain.transfer-in.failed: DomainTransferInFailed
                        domain.certificate.add: DomainCertificateAdd
                        domain.certificate.add.failed: DomainCertificateAddFailed
                        domain.certificate.renew: DomainCertificateRenew
                        domain.certificate.renew.failed: DomainCertificateRenewFailed
                        domain.certificate.deleted: DomainCertificateDeleted
                        domain.renewal: DomainRenewal
                        domain.renewal.failed: DomainRenewalFailed
                        domain.auto-renew.changed: DomainAutoRenewChanged
                        deployment.created: DeploymentCreated
                        deployment.cleanup: DeploymentCleanup
                        deployment.error: DeploymentError
                        deployment.canceled: DeploymentCanceled
                        deployment.succeeded: DeploymentSucceeded
                        deployment.ready: DeploymentReady
                        deployment.check-rerequested: DeploymentCheckRerequested
                        deployment.promoted: DeploymentPromoted
                        deployment.integration.action.start: DeploymentIntegrationActionStart
                        deployment.integration.action.cancel: DeploymentIntegrationActionCancel
                        deployment.integration.action.cleanup: DeploymentIntegrationActionCleanup
                        deployment.checkrun.start: DeploymentCheckrunStart
                        deployment.checkrun.cancel: DeploymentCheckrunCancel
                        edge-config.created: EdgeConfigCreated
                        edge-config.deleted: EdgeConfigDeleted
                        edge-config.items.updated: EdgeConfigItemsUpdated
                        firewall.attack: FirewallAttack
                        integration-configuration.permission-upgraded: IntegrationConfigurationPermissionUpgraded
                        integration-configuration.removed: IntegrationConfigurationRemoved
                        integration-configuration.scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmed
                        integration-resource.project-connected: IntegrationResourceProjectConnected
                        integration-resource.project-disconnected: IntegrationResourceProjectDisconnected
                        project.created: ProjectCreated
                        project.removed: ProjectRemoved
                        project.domain.created: ProjectDomainCreated
                        project.domain.updated: ProjectDomainUpdated
                        project.domain.deleted: ProjectDomainDeleted
                        project.domain.verified: ProjectDomainVerified
                        project.domain.unverified: ProjectDomainUnverified
                        project.domain.moved: ProjectDomainMoved
                        project.rolling-release.started: ProjectRollingReleaseStarted
                        project.rolling-release.aborted: ProjectRollingReleaseAborted
                        project.rolling-release.completed: ProjectRollingReleaseCompleted
                        project.rolling-release.approved: ProjectRollingReleaseApproved
                        deployment.checks.failed: DeploymentChecksFailed
                        deployment.checks.succeeded: DeploymentChecksSucceeded
                        deployment-checks-completed: DeploymentChecksCompleted
                        deployment-ready: DeploymentReadyHyphen
                        deployment-prepared: DeploymentPreparedHyphen
                        deployment-error: DeploymentErrorHyphen
                        deployment-check-rerequested: DeploymentCheckRerequestedHyphen
                        deployment-canceled: DeploymentCanceledHyphen
                        project-created: ProjectCreatedHyphen
                        project-removed: ProjectRemovedHyphen
                        domain-created: DomainCreatedHyphen
                        deployment: Deployment
                        integration-configuration-permission-updated: IntegrationConfigurationPermissionUpdatedHyphen
                        integration-configuration-removed: IntegrationConfigurationRemovedHyphen
                        integration-configuration-scope-change-confirmed: IntegrationConfigurationScopeChangeConfirmedHyphen
                        marketplace.invoice.created: MarketplaceInvoiceCreated
                        marketplace.invoice.paid: MarketplaceInvoicePaid
                        marketplace.invoice.notpaid: MarketplaceInvoiceNotpaid
                        marketplace.invoice.refunded: MarketplaceInvoiceRefunded
                        observability.anomaly: ObservabilityAnomaly
                        observability.anomaly-error: ObservabilityAnomalyError
                        test-webhook: TestWebhook
                    type: array
                    description: The webhooks events
                    example: deployment.created
              id:
                allOf:
                  - type: string
                    description: The webhook id
                    example: account_hook_GflD6EYyo7F4ViYS
              url:
                allOf:
                  - type: string
                    description: A string with the URL of the webhook
                    example: https://my-webhook.com
              ownerId:
                allOf:
                  - type: string
                    description: The unique ID of the team the webhook belongs to
                    example: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was created
                      in in milliseconds
                    example: 1567024758130
              updatedAt:
                allOf:
                  - type: number
                    description: >-
                      A number containing the date when the webhook was updated
                      in in milliseconds
                    example: 1567024758130
              projectIds:
                allOf:
                  - items:
                      type: string
                    type: array
                    description: The ID of the projects the webhook is associated with
                    example:
                      - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
            requiredProperties:
              - secret
              - events
              - id
              - url
              - ownerId
              - createdAt
              - updatedAt
        examples:
          example:
            value:
              secret: <string>
              events: deployment.created
              id: account_hook_GflD6EYyo7F4ViYS
              url: https://my-webhook.com
              ownerId: ZspSRT4ljIEEmMHgoDwKWDei
              createdAt: 1567024758130
              updatedAt: 1567024758130
              projectIds:
                - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
        description: ''
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: One of the provided values in the request body is invalid.
        examples: {}
        description: One of the provided values in the request body is invalid.
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: The request is not authorized.
        examples: {}
        description: The request is not authorized.
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: You do not have permission to access this resource.
        examples: {}
        description: You do not have permission to access this resource.
  deprecated: false
  type: path
components:
  schemas: {}

````