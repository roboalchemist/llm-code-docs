# MassTransit Agent Instructions

This file is for coding agents. Treat it as behavioral guidance for generating MassTransit code in this repository.

## Source Priority

1. [Skills Runbook](/skills/README.md)
2. Foundation skills in `/skills/*.md`
3. Linked concepts/configuration/guides pages from each skill

If sources conflict, follow the skill file that best matches the task, then verify against linked docs.

## Skill Selection

- Consumer implementation: [Consumer Foundation](/skills/consumer-foundation.md)
- Saga state machine: [Saga State Machine Foundation](/skills/saga-state-machine-foundation.md)
- Routing slip activity: [Routing Slip Activity Foundation](/skills/routing-slip-activity-foundation.md)
- Request/response flow: [Request Response Foundation](/skills/request-response-foundation.md)
- Tests and harness setup: [Test Harness Foundation](/skills/test-harness-foundation.md)
- Outbox reliability: [Outbox Foundation](/skills/outbox-foundation.md)
- Endpoint naming and topology: [Endpoint Configuration Foundation](/skills/endpoint-configuration-foundation.md)

## Required Defaults

- Use `record` types for message contracts.
- Keep consumers focused on one business responsibility.
- Configure endpoints via registration and definitions when possible.
- Use convention-based routing when possible, do not hard code endpoint names, etc. unless specifically asked.
- Apply retry and outbox patterns where reliability matters.
- Use async all the way; avoid sync-over-async.

## Do

- Reuse patterns from the selected skill before inventing new structure.
- Keep naming, endpoint format, and transport topology consistent with existing code.
- Model expected negative outcomes as response messages when using request/response.
- Add or update tests for happy path and failure/retry paths.
- Run build/tests and ensure checks in the skill are satisfied.

## Do Not

- Do not use interfaces for message contracts in new code.
- Do not publish/send side effects before durable state changes.
- Do not swallow exceptions or hide failure context.
- Do not mix unrelated workflows inside one consumer.
- Do not introduce transport-specific behavior without explicit configuration.

## Output Expectations

- Generated code should compile and align with the selected skill checklist.
- Include only the minimum complexity needed for the requested behavior.
- If multiple skills apply, start with one foundation skill and layer others explicitly.
