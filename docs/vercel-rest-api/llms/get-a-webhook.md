# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/get-a-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a webhook

> Get a webhook



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/webhooks/{id}
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/webhooks/{id}:
    get:
      tags:
        - webhooks
      summary: Get a webhook
      description: Get a webhook
      operationId: getWebhook
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  events:
                    items:
                      type: string
                      enum:
                        - budget.reached
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
                        - firewall.system-rule-anomaly
                        - firewall.custom-rule-anomaly
                        - alerts.triggered
                        - integration-configuration.permission-upgraded
                        - integration-configuration.removed
                        - integration-configuration.scope-change-confirmed
                        - integration-configuration.transferred
                        - integration-resource.project-connected
                        - integration-resource.project-disconnected
                        - project.created
                        - project.removed
                        - project.renamed
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
                        - ai-gateway.balance-depleted
                        - ai-gateway.auto-reload.limit-reached
                        - observability.anomaly
                        - observability.anomaly-error
                        - observability.usage-anomaly
                        - observability.error-anomaly
                        - botid.anomaly
                        - test-webhook
                      example: deployment.created
                      description: The webhooks events
                      x-speakeasy-enums:
                        budget.reached: BudgetReached
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
                    type: string
                    description: The webhook id
                    example: account_hook_GflD6EYyo7F4ViYS
                  url:
                    type: string
                    description: A string with the URL of the webhook
                    example: https://my-webhook.com
                  ownerId:
                    type: string
                    description: The unique ID of the team the webhook belongs to
                    example: ZspSRT4ljIEEmMHgoDwKWDei
                  createdAt:
                    type: number
                    description: >-
                      A number containing the date when the webhook was created
                      in in milliseconds
                    example: 1567024758130
                  updatedAt:
                    type: number
                    description: >-
                      A number containing the date when the webhook was updated
                      in in milliseconds
                    example: 1567024758130
                  projectIds:
                    items:
                      type: string
                    type: array
                    description: The ID of the projects the webhook is associated with
                    example:
                      - prj_12HKQaOmR5t5Uy6vdcQsNIiZgHGB
                required:
                  - createdAt
                  - events
                  - id
                  - ownerId
                  - updatedAt
                  - url
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````