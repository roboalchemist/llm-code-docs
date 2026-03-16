# Source: https://docs.testsprite.com/mcp/core/rerun-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerun Existing Tests

> Execute previously generated tests to validate your application.

Sometimes you just want to rerun the same tests as the previous run—maybe to double-check after a bug fix.

<Tip>
  This is useful after you fix a bug or change code and want to confirm nothing is broken.
</Tip>

<Tabs>
  <Tab title="Rerun All Tests">
    <Frame>
      <img src="https://mintcdn.com/testspriteinc/Kj9Oj-XCI1XCbQc_/images/rerun-all.png?fit=max&auto=format&n=Kj9Oj-XCI1XCbQc_&q=85&s=410b09a7dfd297da595de354f6acb9fe" alt="prd" width="1906" height="895" data-path="images/rerun-all.png" />
    </Frame>

    In your coding IDE, simply type:

    ```text Example Prompt theme={null}
    Help me rerun all the tests with TestSprite.
    ```

    TestSprite will automatically detect your existing project test suite and execute all of the tests again with the `testsprite_rerun_tests` tool. You'll see updated results directly in **your IDE** or **TestSprite dashboard**.
  </Tab>

  <Tab title="Rerun Subset of Tests">
    TestSprite gives you the flexibility to rerun only **a subset of your tests** instead of executing the entire suite. This is useful when you want to quickly validate specific scenarios without waiting for every test to finish.

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/Kj9Oj-XCI1XCbQc_/images/rerun-subset.png?fit=max&auto=format&n=Kj9Oj-XCI1XCbQc_&q=85&s=1035b3229d4423daee46fbe22d4901f5" alt="prd" width="1906" height="1101" data-path="images/rerun-subset.png" />
    </Frame>

    You can annotate the tests you want to rerun and pass their indexes directly to the `testsprite_rerun_tests` command. For example, to re-run only the 1st, 3rd, and 12th tests:

    ```text Example Prompt theme={null}
    Help me rerun the 1, 3 and 12th tests with TestSprite.
    ```
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).