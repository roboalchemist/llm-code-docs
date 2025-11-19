# Source: https://docs.solidfi.com/v2/api-reference/getting-started/simulation.md

# Simulation

> Solid Platform simulates transactions

Solid platform lets you simulate payments to test your integration in the sandbox environment. The platform currently supports simulating ACH payment methods and spending on issued cards.

Currently, the platform supports:

* [Simulating an Incoming ACH Push](/v2/api-reference/simulation/simulate-an-incoming-ach-push)

* [Simulating an Incoming ACH Pull](/v2/api-reference/simulation/simulate-an-incoming-ach-pull)

* [Simulating a Card Auth Transaction](/v2/api-reference/simulation/simulate-an-auth-transaction)

<Warning>You should not stress-test your integration in the sandbox environment, as the rate limits would block the requests.</Warning>
