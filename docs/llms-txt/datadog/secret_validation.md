# Source: https://docs.datadoghq.com/security/code_security/secret_scanning/secret_validation.md

---
title: Secret Validation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Code Security > Secret Scanning > Secret Validation
---

# Secret Validation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## About validity checks{% #about-validity-checks %}

For certain detections (see the list below), Datadog checks whether a detected secret is valid during scans. For these live validation checks, Datadog makes API requests to provider endpoints to confirm that a credential is active. Datadog only makes requests to endpoints that do not return sensitive data or personally identifiable information (PII), and only to verify if the credential can still access the provider endpoint.

For secret types with validation available, Datadog displays the validation status in the explorer as "Active" or "Inactive". You can also filter or query detections by their Validation Status.

For some secret types, Datadog uses static validation methods, such as computing a checksum, to confirm that a detected secret is not a false positive. Static validation results are not displayed and all references to "validation" in the explorer correspond to live validation results.

## List of supported validators{% #list-of-supported-validators %}

| Secret type                                 | Static validator available | Live validator available |
| ------------------------------------------- | -------------------------- | ------------------------ |
| `adobe_access_token`                        | â                          | â                        |
| `adobe_refresh_token`                       | â                          | â                        |
| `adafruit_io_key`                           | â                          | â                        |
| `aiven_personal_token`                      | â                          | â                        |
| `anthropic's_claude_api_key`                | â                          | â                        |
| `asana_oauth_token`                         | â                          | â                        |
| `asana_personal_access_token`               | â                          | â                        |
| `atlassian_access_token`                    | â                          | â                        |
| `atlassian_refresh_token`                   | â                          | â                        |
| `aws_access_key_id`                         | â                          | â                        |
| `aws_secret_access_key`                     | â                          | â                        |
| `azure_container_registry_key`              | â                          | â                        |
| `azure_entra_id_token`                      | â                          | â                        |
| `beamer_api_token`                          | â                          | â                        |
| `bitbucket_oauth_access_token`              | â                          | â                        |
| `buildkite_access_token`                    | â                          | â                        |
| `circleci_personal_access_token`            | â                          | â                        |
| `circleci_project_access_token`             | â                          | â                        |
| `cloudflare_api_token`                      | â                          | â                        |
| `cloudflare_origin_ca_key`                  | â                          | â                        |
| `contentful_access_token`                   | â                          | â                        |
| `datadog_api_key`                           | â                          | â                        |
| `datadog_nonce_session_token`               | â                          | â                        |
| `datadog_personal_access_token`             | â                          | â                        |
| `discord_application_oauth_access_token`    | â                          | â                        |
| `discord_application_token`                 | â                          | â                        |
| `discord_bot_token`                         | â                          | â                        |
| `docker_access_token`                       | â                          | â                        |
| `doppler_access_token`                      | â                          | â                        |
| `dropbox_access_token`                      | â                          | â                        |
| `duffel_test_access_token`                  | â                          | â                        |
| `fastly_api_token`                          | â                          | â                        |
| `flutterwave_api_secret_key`                | â                          | â                        |
| `frame_io_developer_token`                  | â                          | â                        |
| `frame_io_oauth_session_secret`             | â                          | â                        |
| `github_access_token`                       | â                          | â                        |
| `github_fine-grained_personal_access_token` | â                          | â                        |
| `heroku_api_key`                            | â                          | â                        |
| `hugging_face_access_token`                 | â                          | â                        |
| `intercom_access_token`                     | â                          | â                        |
| `launchdarkly_access_token`                 | â                          | â                        |
| `lichess_personal_access_token`             | â                          | â                        |
| `non_expired_json_web_token`                | â                          | â                        |
| `notion_integration_token`                  | â                          | â                        |
| `npm_access_token`                          | â                          | â                        |
| `openai_project_api_key`                    | â                          | â                        |
| `openai_user_api_key`                       | â                          | â                        |
| `oracle_access_token`                       | â                          | â                        |
| `pagerduty_api_token`                       | â                          | â                        |
| `perfect_cloud_api_key`                     | â                          | â                        |
| `postman_api_key`                           | â                          | â                        |
| `pulumi_access_token`                       | â                          | â                        |
| `rubygems_api_key`                          | â                          | â                        |
| `sendgrid_api_key`                          | â                          | â                        |
| `sentry_organization_token`                 | â                          | â                        |
| `sentry_personal_token`                     | â                          | â                        |
| `shippo_api_key`                            | â                          | â                        |
| `shippo_jwt`                                | â                          | â                        |
| `snowflake_personal_access_token`           | â                          | â                        |
| `square_access_token`                       | â                          | â                        |
| `typeform_personal_access_token`            | â                          | â                        |
| `twilio_access_token`                       | â                          | â                        |
| `workos_api_key`                            | â                          | â                        |
| `xai_(grok)_api_key`                        | â                          | â                        |
