# Source: https://docs.redwoodjs.com/docs/tutorial/chapter5/testing

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 5]
-   [Introduction to Testing]

[Version: 8.8]

<div>

# Introduction to Testing

</div>

Let\'s run the test suite to make sure everything is working as expected (you can keep the dev server running and start this in a new terminal window):

``` 
yarn rw test
```

The `test` command starts a persistent process which watches for file changes and automatically runs any tests associated with the changed file(s) (changing a component *or* its tests will trigger a test run).

Since we just started the suite, and we haven\'t changed any files yet, it may not actually run any tests at all. Hit `a` to tell it run **a**ll tests and we should get something like this:

![tests_running](https://user-images.githubusercontent.com/46945607/165376937-89ed9254-0d8e-4945-a0d9-17178764a4b0.png)

If you cloned the example repo during the intermission and followed along with the Storybook tutorial in this chapter, the test run should finish and you will see something like this:

![suite_finished](https://user-images.githubusercontent.com/46945607/165378519-2859dd0d-d46a-448f-a62e-0b8f91c55a87.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

If you decided to keep your codebase from the first part of the tutorial, then you\'ll get the following error after running

``` 
yarn rw test

Error: Get config: Schema Parsing P1012

error: Error validating datasource `db`: the URL must start with the protocol `postgresql://` or `postgres://`.
  -->  schema.prisma:3
   |
 2 |   provider = "postgresql"
 3 |   url      = env("DATABASE_URL")
   |

Validation Error Count: 1

error Command failed with exit code 1.
```

To clear the error and to proceed with running the test suite, head over to your `.env` file and add the following line:

``` 
TEST_DATABASE_URL=<the same url as DATABASE_URL>
```

Note that the summary on the bottom indicates that there was 1 test that failed. If you feel curious, you can scroll up in your terminal and see more details on the test that failed. We\'ll also take a look at that failed test shortly.

If you continued with your own repo from chapters 1-4, you may see some other failures here or none at all: we made a lot of changes to the pages, components and cells we generated, but didn\'t update the tests to reflect the changes we made. (Another reason to start with the [example repo](/docs/tutorial/intermission#using-the-example-repo-recommended)!)

To switch back to the default mode where test are **only** run for changed files, press `o` now (or quit and restart `yarn rw test`).

What we want to aim for is all green in that left column and no failed tests. In fact best practices tell us you should not even commit any code to your repo unless the test suite passes locally. Not everyone adheres to this policy quite as strictly as others\...*\<cough, cough\>*

We\'ve got an excellent document on [Testing](/docs/testing) which you should definitely read if you\'re brand new to testing, especially the [Terminology](/docs/testing#terminology) and [Redwood and Testing](/docs/testing#redwood-and-testing) sections. For now though, proceed to the next section and we\'ll go over our approach to getting that last failed test passing.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter5/testing.md)