# Source: https://relay.dev/docs/guides/testing-relay-components/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Testing and Debugging]
-   [Testing Relay Components]

[Version: v20.1.0]

On this page

<div>

# Testing Relay Components

</div>

## Abstract[​](#abstract "Direct link to Abstract") 

The purpose of this document is to cover the Relay APIs for testing Relay components.

The content is focused mostly on jest unit-tests (testing individual components) and integration tests (testing a combination of components). But these testing tools may be applied in different cases: screenshot-tests, production smoke-tests, \"Redbox\" tests, fuzz-tests, e2e test, etc.

What are the benefits of writing jest tests:

-   In general, it improves the stability of the system. Flow helps with catching a various set of Javascript errors, but it is still possible to introduce regressions to the components. Unit-tests help find, reproduce, and fix regressions, and prevent them in the future.
-   It simplifies the refactoring process: when properly written (testing public interface, not implementation) - tests help with changing the internal implementation of the components.
-   It may speed up and improve the development workflow. Some people may call it Test Driven Development (TM). But essentially it\'s just writing tests for public interfaces of your components, and then writing the components that implement those interfaces. Jest ---watch mode really shines in this case.
-   It will simplify the on-boarding process for new developers. Having tests helps new developers ramp up on the new code base, allowing them to fix bugs and deliver features.

One thing to notice: while jest unit- and integration tests will help improve the stability of the system, they should be considered one part of a bigger stability infrastructure with multiple layers of automated testing: flow, e2e, screenshot, \"Redbox\", performance tests.

## Testing with Relay[​](#testing-with-relay "Direct link to Testing with Relay") 

Testing applications that use Relay may be challenging, because of the additional data fetching layer that wraps the actual product code.

And it\'s not always easy to understand the mechanics of all processes that are happening behind Relay, and how to properly handle interactions with the framework.

Fortunately, there are tools that aim to simplify the process of writing tests for Relay components, by providing imperative APIs for controlling the request/response flow and additional API for mock data generation.

There are two main Relay modules that you may use in your tests:

-   `createMockEnvironment(options): RelayMockEnvironment`
-   `MockPayloadGenerator` and the `@relay_test_operation` directive

With `createMockEnvironment,` you will be able to create an instance of `RelayMockEnvironment`, a Relay environment specifically for your tests. The instance created by `createMockEnvironment` implements the Relay Environment Interface and it also has an additional Mock layer, with methods that allow you to resolve/reject and control the flow of operations (queries/mutations/subscriptions).

The main purpose of `MockPayloadGenerator` is to improve the process of creating and maintaining the mock data for tested components.

One of the patterns you may see in the tests for Relay components: 95% of the test code is the test preparation---the gigantic mock object with dummy data, manually created, or just a copy of a sample server response that needs to be passed as the network response. And the remaining 5% is actual test code. As a result, people don\'t test much. It\'s hard to create and manage all these dummy payloads for different cases. Hence, writing tests is time-consuming and tests are sometimes painful to maintain.

With the `MockPayloadGenerator` and `@relay_test_operation`, we want to get rid of this pattern and switch the developer\'s focus from the preparation of the test to the actual testing.

## Testing with React and Relay[​](#testing-with-react-and-relay "Direct link to Testing with React and Relay") 

**[React Testing Library](https://testing-library.com/react)** is a set of helpers that let you test React components without relying on their implementation details. This approach makes refactoring a breeze and also nudges you towards best practices for accessibility. Although it doesn\'t provide a way to \"shallowly\" render a component without its children, a test runner like Jest lets you do this by [mocking](https://reactjs.org/docs/testing-recipes.html#mocking-modules).

## RelayMockEnvironment API Overview[​](#relaymockenvironment-api-overview "Direct link to RelayMockEnvironment API Overview") 

RelayMockEnvironment is a special version of Relay Environment with additional API methods for controlling the operation flow: resolving and rejection operations, providing incremental payloads for subscriptions, working with the cache.

-   Methods for finding operations executed on the environment
    -   `getAllOperations()` - get all operation executed during the test by the current time
    -   `findOperation(findFn => boolean) `- find particular operation in the list of all executed operations, this method will throw, if operation is not available. Maybe useful to find a particular operation when multiple operations executed at the same time
    -   `getMostRecentOperation() -` return the most recent operation, this method will throw if no operations were executed prior this call.
-   Methods for resolving or rejecting operations
    -   `nextValue(request | operation, data)` - provide payload for operation(request), but not complete request. Practically useful when testing incremental updates and subscriptions
    -   `complete(request | operation)` - complete the operation, no more payloads are expected for this operation, when it\'s completed.
    -   `resolve(request | operation, data)` - resolve the request with provided GraphQL response. Essentially, it\'s nextValue(\...) and complete(\...)
    -   `reject(request | operation, error)` - reject the request with particular error
    -   `resolveMostRecentOperation(operation => data)` - resolve and getMostRecentOperation work together
    -   `rejectMostRecentOperation(operation => error)` - reject and getMostRecentOperation work together
    -   `queueOperationResolver(operation => data | error)` - adds an OperationResolver function to the queue. The passed resolver will be used to resolve/reject operations as they appear
    -   `queuePendingOperation(query, variables)` - in order for the `usePreloadedQuery` hook to not suspend, one must call these functions:
        -   `queueOperationResolver(resolver)`
        -   `queuePendingOperation(query, variables)`
        -   `preloadQuery(mockEnvironment, query, variables)` with the same `query` and `variables` that were passed to `queuePendingOperation`. `preloadQuery` must be called after `queuePendingOperation`.
-   Additional utility methods
    -   `isLoading(request | operation)` - will return `true` if operations has not been completed, yet.
    -   `cachePayload(request | operation, variables, payload)` - will add payload to QueryResponse cache
    -   `clearCache() `- will clear QueryResponse cache

## Mock Payload Generator and the `@relay_test_operation` Directive[​](#mock-payload-generator-and-the-relay_test_operation-directive "Direct link to mock-payload-generator-and-the-relay_test_operation-directive") 

`MockPayloadGenerator` may drastically simplify the process of creating and maintaining mock data for your tests. `MockPayloadGenerator` can generate dummy data for the selection that you have in your operation. There is an API to modify the generated data - Mock Resolvers. With Mock Resolvers, you may adjust the data for your needs. Mock Resolvers are defined as an object where **keys are names of GraphQL types (`ID`, `String`, `User`, `Comment`, etc),** and values are functions that return the default data for the type.

Example of a simple Mock Resolver:

``` 
,
  String() 
}
```

It is possible to define more resolvers for Object types

``` 
,
    };
  },
}
```

### Mock Resolver Context[​](#mock-resolver-context "Direct link to Mock Resolver Context") 

The first argument of the MockResolver is the object that contains Mock Resolver Context. It is possible to return dynamic values from mock resolvers based on the context - for instance, name or alias of the field, a path in the selection, arguments, or parent type.

``` 

    if (context.path != null && context.path.join('.') === 'node.actor.name') 
    if (context.parentType === 'Image' && context.name === 'uri') 
  }
}
```

### ID Generation[​](#id-generation "Direct link to ID Generation") 

The second argument of the Mock Resolver is a function that will generate a sequence of integers, useful to generate unique ids in the tests

``` 
`;
  },
}
```

### Float, Integer, Boolean, etc\...[​](#float-integer-boolean-etc "Direct link to Float, Integer, Boolean, etc...") 

Please note, that for production queries we don\'t have full type information for Scalar fields - like Boolean, Integer, Float. And in the MockResolvers, they map to String. You can use `context` to adjust return values, based on the field name, alias, etc.

### \@relay_test_operation[​](#relay_test_operation "Direct link to @relay_test_operation") 

Most of GraphQL type information for a specific field in the selection is not available during Relay runtime. By default, Relay, cannot get type information for a scalar field in the selection, or an interface type of the object.

Operation with the \@relay_test_operation directive will have additional metadata that will contain GraphQL type info for fields in the operation\'s selection. And it will improve the quality of the generated data. You also will be able to define Mock resolvers for Scalar (not only ID and String) and Abstract types:

``` 
,
  Boolean(context) 
    return false;
  },
  Node() ;
  }
}
```

## Examples[​](#examples "Direct link to Examples") 

### Relay Component Test[​](#relay-component-test "Direct link to Relay Component Test") 

Using `createMockEnvironment` and `MockPayloadGenerator` allows writing concise tests for components that use Relay hooks. Both those modules can be imported from `relay-test-utils`

``` 
// Say you have a component with the useLazyLoadQuery or a QueryRenderer
const MyAwesomeViewRoot = require('MyAwesomeViewRoot');
const  = require('relay-test-utils');
const  = require('@testing-library/react');

// Relay may trigger 3 different states
// for this component: Loading, Error, Data Loaded
// Here is examples of tests for those states.
test('Loading State', async () =>  />,
  );

  // Here we just verify that the spinner is rendered
  expect(await renderer.findByTestId('spinner')).toBeDefined();
});

test('Data Render', async () =>  />,
  );

  // Wrapping in act will ensure that components
  // are fully updated to their final state.
  act(() => );

  // At this point operation will be resolved
  // and the data for a query will be available in the store
  expect(await renderer.findByTestId('myButton')).toBeDefined();
});

test('Error State', async () =>  />,
  );

  // Wrapping in act will ensure that components
  // are fully updated to their final state.
  act(() => );

  expect(await renderer.findByTestId('errorMessage')).toBeDefined();
});
```

#### Component Tests With Deferred Fragments[​](#component-tests-with-deferred-fragments "Direct link to Component Tests With Deferred Fragments") 

When using `MockPayloadGenerator` to generate data for a Query that has fragments with `@defer` you may want to generate the deferred data as well. To do so, you can use `MockPayloadGenerator.generateWithDefer` passing the option `generateDeferredPayload`:

``` 
// Say you have a component with useFragment
const ChildComponent = (props: ) => 
  `, props.user);
  return <View></View>;
};

// Say you have a parent component that fetches data with useLazyLoadQuery and `@defer`s the data for the ChildComponent.
const ParentComponent = () => 
  }
  `, );
  return (
    <View>
      
      <Suspense fallback=>
         />}
      </Suspense>
    </View>
  );
};

const  = require('relay-test-utils');
const  = require('@testing-library/react');

test('Data Render with @defer', () => >
      <ParentComponent />,
    </RelayEnvironmentProvider>
  );

  // Wrapping in ReactTestRenderer.act will ensure that components
  // are fully updated to their final state.
  act(() => );
    environment.mock.resolve(mockData);

    // You may need this to make sure all payloads are retrieved
    jest.runAllTimers();
  });

  // At this point operation will be resolved
  // and the data for a query will be available in the store
  expect(renderer.container.textContent).toEqual(['id', 'name']);
});
```

### Fragment Component Tests[​](#fragment-component-tests "Direct link to Fragment Component Tests") 

Essentially, in the example above, `resolveMostRecentOperation` will generate data for all child fragment containers (pagination, refetch). But, usually the root component may have many child fragment components and you may want to exercise a specific component that uses `useFragment`. The solution for that would be to wrap your fragment container with the `useLazyLoadQuery` component that renders a Query that spreads fragments from your fragment component:

``` 
test('Fragment', () => 
        }
      `,
      ,
    );
    return <MyFragmentComponent myData= />
  };

  const renderer = render(
    <RelayEnvironmentProvider environment=>
      <Suspense fallback="Loading...">
        <TestRenderer />
      </Suspense>
    </RelayEnvironmentProvider>
  );

  // Wrapping in act will ensure that components
  // are fully updated to their final state.
  act(() => );

  expect(renderer).toMatchSnapshot();
});
```

### Pagination Component Test[​](#pagination-component-test "Direct link to Pagination Component Test") 

Essentially, tests for pagination components (e.g. using `usePaginationFragment`) are not different from fragment component tests. But we can do more here, we can actually see how the pagination works - we can assert the behavior of our components when performing pagination (load more, refetch).

``` 
// Pagination Example
test('`Pagination` Container', async () => 
          }
        }
      `,
      ,
    );
    return <MyPaginationContainer connection= />
  };

  const renderer = render(
    <RelayEnvironmentProvider environment=>
      <Suspense fallback="Loading...">
        <TestRenderer />
      </Suspense>
    </RelayEnvironmentProvider>
  );

  // Wrapping in act will ensure that components
  // are fully updated to their final state.
  act(() => `;
        },
        PageInfo() ;
        },
      }),
    );
  });

  // Let's find a `loadMore` button and click on it to initiate pagination request, for example
  const loadMore = await renderer.findByTestId('loadMore');
  expect(loadMore.props.disabled).toBe(false);
  loadMore.props.onClick();

  // Wrapping in act will ensure that components
  // are fully updated to their final state.
  act(() => `;
        },
        PageInfo() ;
        },
      }),
    );
  });

  expect(loadMore.props.disabled).toBe(true);
});
```

### Refetch Component[​](#refetch-component "Direct link to Refetch Component") 

We can use similar approach here with wrapping the component with a query. And for the sake of completeness, we will add an example here:

``` 
test('Refetch Container', async () => 
        }
      `,
      ,
    );
    return <MyRefetchContainer data= />
  };

  const renderer = render(
    <RelayEnvironmentProvider environment=>
      <Suspense fallback="Loading...">
        <TestRenderer />
      </Suspense>
    </RelayEnvironmentProvider>
  );

  act(() => );

  // Assuming we have refetch button in the Container
  const refetchButton = await renderer.findByTestId('refetch');

  // This should trigger the `refetch`
  refetchButton.props.onClick();

  act(() => ),
    );
  });

  expect(renderer).toMatchSnapshot();
});
```

### Mutations[​](#mutations "Direct link to Mutations") 

Mutations themselves are operations, so we can test them independently (unit-test) for a specific mutation, or in combination with the view from which this mutation is called.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

the `useMutation` API is an improvement over calling `commitMutation` directly.

``` 
// Say, you have a mutation function
function sendMutation(environment, onCompleted, onError, variables)
  commitMutation(environment, );
}

// Example test may be written like so
test('it should send mutation', () => );
  const operation = environment.mock.getMostRecentOperation();

  act(() => );

  expect(onCompleted).toBeCalled();
});
```

### Subscription[​](#subscription "Direct link to Subscription") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

The `useSubscription` API is an improvement over calling `requestSubscription` directly.

We can test subscriptions similarly to how we test mutations.

``` 
// Example subscribe function
function subscribe(environment, onNext, onError, variables)
  requestSubscription(environment, );
}

// Example test may be written like so
test('it should subscribe', () => );
  const operation = environment.mock.getMostRecentOperation();

  act(() => );

  expect(onNext).toBeCalled();
});
```

### Example with `queueOperationResolver`[​](#example-with-queueoperationresolver "Direct link to example-with-queueoperationresolver") 

With `queueOperationResolver` it is possible to define responses for operations that will be executed on the environment

``` 
// Say you have a component with the QueryRenderer
const MyAwesomeViewRoot = require('MyAwesomeViewRoot');
const  = require('relay-test-utils');

test('Data Render', async () =>  />,
  );

  // At this point operation will be resolved
  // and the data for a query will be available in the store
  expect(await renderer.findByTestId('myButton')).toBeDefined();
});

test('Error State', async () =>  />,
  );

  expect(await renderer.findByTestId('myButton')).toBeDefined();
});
```

### With Relay Hooks[​](#with-relay-hooks "Direct link to With Relay Hooks") 

The examples in this guide should work for testing components both with Relay Hooks, Containers or Renderers. When writing tests that involve the `usePreloadedQuery` hook, please also see the `queuePendingOperation` note above.

### toMatchSnapshot(\...)[​](#tomatchsnapshot "Direct link to toMatchSnapshot(...)") 

Even though in all of the examples here you can see assertions with `toMatchSnapshot()`, we keep it that way just to make examples concise. But it\'s not the recommended way to test your components.

### More Examples[​](#more-examples "Direct link to More Examples") 

The best source of example tests is in [the relay-experimental package](https://github.com/facebook/relay/tree/main/packages/relay-experimental/__tests__).

Testing is good. You should definitely do it.

------------------------------------------------------------------------

Is this page useful?![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnN1cCIgYWx0PSJMaWtlIiBpZD0iZG9jc1JhdGluZy1saWtlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA4MS4xMyA4OS43NiI+PHBhdGggZD0iTTIyLjkgNmExOC41NyAxOC41NyAwIDAwMi42NyA4LjQgMjUuNzIgMjUuNzIgMCAwMDguNjUgNy42NmMzLjg2IDIgOC42NyA3LjEzIDEzLjUxIDExIDMuODYgMy4xMSA4LjU3IDcuMTEgMTEuNTQgOC40NXMxMy41OS4yNiAxNC42NCAxLjE3YzEuODggMS42MyAxLjU1IDktLjExIDE1LjI1LTEuNjEgNS44Ni01Ljk2IDEwLjU1LTYuNDggMTYuODYtLjQgNC44My0yLjcgNC44OC0xMC45MyA0Ljg4aC0xLjM1Yy0zLjgyIDAtOC4yNCAyLjkzLTEyLjkyIDMuNjJhNjggNjggMCAwMS05LjczLjVjLTMuNTcgMC03Ljg2LS4wOC0xMy4yNS0uMDgtMy41NiAwLTQuNzEtMS44My00LjcxLTQuNDhoOC40MmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOGEyLjg5IDIuODkgMCAwMS0yLjg4LTIuODggMS45MSAxLjkxIDAgMDEuNzctMS43OGgxNi40NmEzLjUxIDMuNTEgMCAwMDAtN0gxMi4yOWMtMy4yMSAwLTQuODQtMS44My00Ljg0LTRhNi40MSA2LjQxIDAgMDExLjE3LTMuNzhoMTkuMDZhMy41IDMuNSAwIDEwMC03SDkuNzVBMy41MSAzLjUxIDAgMDE2IDQyLjI3YTMuNDUgMy40NSAwIDAxMy43NS0zLjQ4aDEzLjExYzUuNjEgMCA3LjcxLTMgNS43MS01LjUyLTQuNDMtNC43NC0xMC44NC0xMi42Mi0xMS0xOC43MS0uMTUtNi41MSAyLjYtNy44MyA1LjM2LTguNTZtMC02YTYuMTggNi4xOCAwIDAwLTEuNTMuMmMtNi42OSAxLjc3LTEwIDYuNjUtOS44MiAxNC41LjA4IDUuMDkgMi45OSAxMS4xOCA4LjUyIDE4LjA5SDkuNzRhOS41MiA5LjUyIDAgMDAtNi4yMyAxNi45IDEyLjUyIDEyLjUyIDAgMDAtMi4wNyA2Ljg0IDkuNjQgOS42NCAwIDAwMy42NSA3LjcgNy44NSA3Ljg1IDAgMDAtMS43IDUuMTMgOC45IDguOSAwIDAwNS4zIDguMTMgNiA2IDAgMDAtLjI2IDEuNzZjMCA2LjM3IDQuMiAxMC40OCAxMC43MSAxMC40OGgxMy4yNWE3My43NSA3My43NSAwIDAwMTAuNi0uNTYgMzUuODkgMzUuODkgMCAwMDcuNTgtMi4xOCAxNy44MyAxNy44MyAwIDAxNC40OC0xLjM0aDEuMzVjNC42OSAwIDcuNzkgMCAxMC41LTEgMy44NS0xLjQ0IDYtNC41OSA2LjQxLTkuMzguMi0yLjQ2IDEuNDItNC44NSAyLjg0LTcuNjJhNDEuMyA0MS4zIDAgMDAzLjQyLTguMTMgNDggNDggMCAwMDEuNTktMTAuNzljLjEtNS4xMy0xLTguNDgtMy4zNS0xMC41NS0yLjE2LTEuODctNC42NC0xLjg3LTkuNi0xLjg4YTQ2Ljg2IDQ2Ljg2IDAgMDEtNi42NC0uMjljLTEuOTItLjk0LTUuNzItNC04LjUxLTYuM2wtMS41OC0xLjI4Yy0xLjYtMS4zLTMuMjctMi43OS00Ljg3LTQuMjMtMy4zMy0zLTYuNDctNS43OS05LjYxLTcuNDVhMjAuMiAyMC4yIDAgMDEtNi40My01LjUzIDEyLjQ0IDEyLjQ0IDAgMDEtMS43Mi01LjM2IDYgNiAwIDAwLTYtNS44NnoiPjwvcGF0aD48L3N2Zz4=)![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaV90aHVtYnNkb3duIiBhbHQ9IkRpc2xpa2UiIGlkPSJkb2NzUmF0aW5nLWRpc2xpa2UiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld2JveD0iMCAwIDgxLjEzIDg5Ljc2Ij48cGF0aCBkPSJNMjIuOSA2YTE4LjU3IDE4LjU3IDAgMDAyLjY3IDguNCAyNS43MiAyNS43MiAwIDAwOC42NSA3LjY2YzMuODYgMiA4LjY3IDcuMTMgMTMuNTEgMTEgMy44NiAzLjExIDguNTcgNy4xMSAxMS41NCA4LjQ1czEzLjU5LjI2IDE0LjY0IDEuMTdjMS44OCAxLjYzIDEuNTUgOS0uMTEgMTUuMjUtMS42MSA1Ljg2LTUuOTYgMTAuNTUtNi40OCAxNi44Ni0uNCA0LjgzLTIuNyA0Ljg4LTEwLjkzIDQuODhoLTEuMzVjLTMuODIgMC04LjI0IDIuOTMtMTIuOTIgMy42MmE2OCA2OCAwIDAxLTkuNzMuNWMtMy41NyAwLTcuODYtLjA4LTEzLjI1LS4wOC0zLjU2IDAtNC43MS0xLjgzLTQuNzEtNC40OGg4LjQyYTMuNTEgMy41MSAwIDAwMC03SDEyLjI4YTIuODkgMi44OSAwIDAxLTIuODgtMi44OCAxLjkxIDEuOTEgMCAwMS43Ny0xLjc4aDE2LjQ2YTMuNTEgMy41MSAwIDAwMC03SDEyLjI5Yy0zLjIxIDAtNC44NC0xLjgzLTQuODQtNGE2LjQxIDYuNDEgMCAwMTEuMTctMy43OGgxOS4wNmEzLjUgMy41IDAgMTAwLTdIOS43NUEzLjUxIDMuNTEgMCAwMTYgNDIuMjdhMy40NSAzLjQ1IDAgMDEzLjc1LTMuNDhoMTMuMTFjNS42MSAwIDcuNzEtMyA1LjcxLTUuNTItNC40My00Ljc0LTEwLjg0LTEyLjYyLTExLTE4LjcxLS4xNS02LjUxIDIuNi03LjgzIDUuMzYtOC41Nm0wLTZhNi4xOCA2LjE4IDAgMDAtMS41My4yYy02LjY5IDEuNzctMTAgNi42NS05LjgyIDE0LjUuMDggNS4wOSAyLjk5IDExLjE4IDguNTIgMTguMDlIOS43NGE5LjUyIDkuNTIgMCAwMC02LjIzIDE2LjkgMTIuNTIgMTIuNTIgMCAwMC0yLjA3IDYuODQgOS42NCA5LjY0IDAgMDAzLjY1IDcuNyA3Ljg1IDcuODUgMCAwMC0xLjcgNS4xMyA4LjkgOC45IDAgMDA1LjMgOC4xMyA2IDYgMCAwMC0uMjYgMS43NmMwIDYuMzcgNC4yIDEwLjQ4IDEwLjcxIDEwLjQ4aDEzLjI1YTczLjc1IDczLjc1IDAgMDAxMC42LS41NiAzNS44OSAzNS44OSAwIDAwNy41OC0yLjE4IDE3LjgzIDE3LjgzIDAgMDE0LjQ4LTEuMzRoMS4zNWM0LjY5IDAgNy43OSAwIDEwLjUtMSAzLjg1LTEuNDQgNi00LjU5IDYuNDEtOS4zOC4yLTIuNDYgMS40Mi00Ljg1IDIuODQtNy42MmE0MS4zIDQxLjMgMCAwMDMuNDItOC4xMyA0OCA0OCAwIDAwMS41OS0xMC43OWMuMS01LjEzLTEtOC40OC0zLjM1LTEwLjU1LTIuMTYtMS44Ny00LjY0LTEuODctOS42LTEuODhhNDYuODYgNDYuODYgMCAwMS02LjY0LS4yOWMtMS45Mi0uOTQtNS43Mi00LTguNTEtNi4zbC0xLjU4LTEuMjhjLTEuNi0xLjMtMy4yNy0yLjc5LTQuODctNC4yMy0zLjMzLTMtNi40Ny01Ljc5LTkuNjEtNy40NWEyMC4yIDIwLjIgMCAwMS02LjQzLTUuNTMgMTIuNDQgMTIuNDQgMCAwMS0xLjcyLTUuMzYgNiA2IDAgMDAtNi01Ljg2eiI+PC9wYXRoPjwvc3ZnPg==)

Help us make the site even better by [answering a few quick questions](https://www.surveymonkey.com/r/FYC9TCJ).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/guides/testing-relay-components.md)