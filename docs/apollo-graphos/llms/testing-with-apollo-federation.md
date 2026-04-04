# Source: https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md

# Testing with Apollo Federation

If you're an enterprise customer looking for more material on this topic, try the [Enterprise best practices: Testing](https://www.apollographql.com/tutorials/testing) course on Odyssey.

Not an enterprise customer? [Learn about GraphOS for Enterprise.](https://www.apollographql.com/pricing?referrer=docs-content)

Testing in GraphQL may seem like it can involve more steps, but that is because your GraphQL architecture can involve many areas of your tech stack, from your frontend with Apollo Client to a backend with Apollo Server, or your infrastructure with your GraphOS Router to the individual subgraphs in your supergraph. In practice, all these areas should be properly tested the same way if you were using any other API technology, but often the testing across boundaries like teams or applications can involve some new steps. By the end of this guide you should have:

* [Unit testing](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#unit-testing) in individual subgraphs
* [Integration testing](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#integration-testing) for the individual subgraphs
* [End-to-end testing](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#end-to-end-testing) for your entire supergraph
* [Composition testing](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#composition-testing) for supergraph schema generation
* [Component and operation testing](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#component-and-operation-testing) for your clients

## Unit testing

Apollo recommends creating unit tests for each of your subgraph server resolvers. Resolvers are the code that gets called for each type or field in your schema, which creates a natural boundary to test in isolation. When doing so, Apollo recommends mocking as much data as possible using a package like [`@faker-js/faker`](https://www.npmjs.com/package/@faker-js/faker). This package generates realistic fake data for mocking inputs and outputs.

Using `@faker-js/faker` to mock a return value in `jest` looks something like the following:

```js
import {faker} from '@faker-js/faker';

const testUser = {
  userId: faker.datatype.uuid(),
  username: faker.internet.userName(),
  email: faker.internet.email(),
  avatar: faker.image.avatar(),
  password: faker.internet.password(),
  birthdate: faker.date.birthdate(),
  registeredAt: faker.date.past()
};

const mockedFunction = jest.fn().mockReturnValue(testUser);
```

### Simplify unit testing with thin resolvers

To enable easier unit testing, Apollo recommends that you keep your resolvers as "thin" as possible, where the logic to retrieve data is separate from the resolver. This separation of concerns allows you to mock the data retrieval logic and more easily unit test the data retrieval process instead of the invocation of the resolver, as mocking a resolver requires a more complex setup.

An example of a thin resolver might look like:

```js
const resolvers = {
  Query: {
    user: async (_, {id}, {dataSources}) => {
      return dataSources.userAPI.getUserById(id);
    }
  }
};
```

### Reference resolvers in unit tests

The `__resolveReference` function (also known as a [reference resolver](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro#2-define-a-reference-resolver)) enables different subgraphs to resolve the fields of a federated entity. Reference resolvers are vital to the successful execution of federated operations, so they are important to validate.

Following the advice above, Apollo recommends making these resolvers as [thin](https://www.apollographql.com/docs/graphos/platform/production-readiness/testing-with-apollo-federation.md#simplify-unit-testing-with-thin-resolvers) as possible, and to mock the data retrieval logic in your unit tests.

## Integration testing

Integration tests for subgraphs should start up a single subgraph and send operations to the schema in a mocked or test environment. To test just the subgraph in isolation, validate all the fields giving special focus to the top-level fields in your queries and mutations, and use all permutations of your inputs to check your schema matches your resolvers.

For more information on integration testing with Apollo Server, see the [Apollo Server testing guide](https://www.apollographql.com/docs/apollo-server/testing/testing).

### Entity resolvers in integration tests

Depending on your schema and operations, the resulting [query plan](https://www.apollographql.com/docs/federation/query-plans) may fetch data from a subgraph using the entity resolvers. The integration tests in this situation involves mimicking the router. You can execute [an `_entities` query](https://www.apollographql.com/docs/federation/subgraph-spec/#understanding-query_entities) during integration tests and your test cases should cover all the entity types that can be resolved by the individual subgraph (all the types marked with `@key`).

This looks like the following:

```graphql
query GetEntities($representations: [_Any!]!) {
  _entities(representations: $representations) {
    ... on User {
      firstName
    }
  }
}
```

with the following input:

```json
{
  "representations": [
    {
      "__typename": "User",
      "id": "5"
    }
  ]
}
```

For types with multiple keys, or compound keys, ensure you test all permutations of the keys.

To see more examples on how to run these operations, see [`Query._entities`](https://www.apollographql.com/docs/federation/building-supergraphs/subgraphs-overview/#query_entities), and if you would like to generate a list of `_entities` queries from known operations, see [this tool from the Apollo Solutions organization to do so](https://github.com/apollosolutions/entity-requests-from-queryplan).

### End-to-end testing

Follow these best practices when creating end-to-end tests for your supergraph:

* Run all your subgraphs and router in a test environment with either mocked or test data
* Use example operations that are actually executed against your supergraph.
  * You can view the details of recent operations in GraphOS Studio.
  * Avoid boilerplate or randomly generated operations, as these don't reflect actual traffic.
  * If you are not in production yet, Apollo suggests making these tests as close to what you think they will be as possible.
  * Make sure to include operation that span multiple subgraphs to validate entity resolvers
* Use variables to ensure high operation cardinality.
  * If your test operations don't use any GraphQL variables (or if you use the same variable values across executions), your supergraph is likely to return cached data. This circumvents large portions of execution logic, limiting test effectiveness.
  * By using a variety of operations and variable values, you help make sure that your tests result in minimal cache hits.

## Composition testing

Composition testing is specific to a federated architecture. It involves testing that your subgraph schemas successfully [compose into a supergraph schema](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition) that can resolve the operations sent by clients. You perform these tests with the [Rover CLI](https://www.apollographql.com/docs/rover/), via the [`rover subgraph check`](https://www.apollographql.com/docs/rover/commands/subgraphs#subgraph-check) command. Apollo recommends performing this check in your CI pipeline as part of code-reviews and in your CD pipeline to confirm the changes you are about to deploy are still valid since the last time you ran the check.

## Component and operation testing

Fortunately, clients are not actually aware of when they are using a Federated GraphQL API versus a non-Federated one so the testing best practices remain the same. Our schema can provide a convenient layer to [mock our data fetching](https://www.apollographql.com/docs/react/development-testing/client-schema-mocking/), or for individual components you can mock the specific client providers that inject or fetch your GraphQL data:

* [Apollo Client React `MockProvider`](https://www.apollographql.com/docs/react/development-testing/testing/)
* [Apollo Client iOS Test Mocks](https://www.apollographql.com/docs/ios/testing/test-mocks)
* [Apollo Client Kotlin Test Tools](https://www.apollographql.com/docs/kotlin/testing/overview)
