# Source: https://docs.hypermode.com/dgraph/guides/message-board-app/graphql/load-schema-to-dgraph-cloud.md

# Deploy the Schema

> Building a Message Board App in React. Step 2: With the schema defined, it’s just one step to get a running GraphQL backend for the app.

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

With the schema defined, it's just one step to get a running GraphQL backend for
the app.

Copy the schema, navigate to the **Schema** tab in Dgraph Cloud, paste the
schema in, and press **Deploy**.

<img src="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=9ec30d2b940d9ba2c384459ccd452d7e" alt="Deploy Dgraph Cloud schema" width="3584" height="2240" data-path="images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png" srcset="https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=280&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=732c47aba5368ab4d0a483406be6847a 280w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=560&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=1ed229544393b768d7ddc3c20501bd81 560w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=840&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=19ac75d733004e6a52c0ad74e7c53975 840w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=1100&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=e54a27c78a0e7d8f2c289ab440c48ef2 1100w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=1650&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=c09ff5a4605da4637c8236908ef3bbac 1650w, https://mintcdn.com/hypermode/UzHAxAOBRpNLwtpT/images/dgraph/guides/message-board-app/dgraph-cloud-deploy-schema-success.png?w=2500&fit=max&auto=format&n=UzHAxAOBRpNLwtpT&q=85&s=230746059c714fa4a5fd0f17a325ea72 2500w" data-optimize="true" data-opv="2" />

As soon as the schema is added, Dgraph Cloud generates and deploys a GraphQL API
for the app.

Next you'll [learn about GraphQL operations](./graphql-operations) like queries,
mutations and subscriptions.
