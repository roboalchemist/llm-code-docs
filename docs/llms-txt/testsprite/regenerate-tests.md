# Source: https://docs.testsprite.com/mcp/core/regenerate-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Regenerate Tests

> Regenerate test suites for existing projects to update coverage.

There are two different ways to regenerate tests depending on whether you want to update just a few cases or start over completely.

<Tabs>
  <Tab title="Regenerate Subset of Test Cases">
    <Frame>
      <img src="https://mintcdn.com/testspriteinc/yJGuYRYLVPSec7Ng/images/test-plan.png?fit=max&auto=format&n=yJGuYRYLVPSec7Ng&q=85&s=656bc55a25359cecaa1975755dd541e6" alt="plan" width="1906" height="895" data-path="images/test-plan.png" />
    </Frame>

    <Steps>
      <Step title="Open your TestSprite test plan file">
        Open your TestSprite test plan file (e.g. `testsprite_frontend_test_plan.json`).
      </Step>

      <Step title="Edit the test case description">
        Find the test case you want to change, edit the descriptionand, and save the file ( <Tooltip tip="Cmd/Ctrl + S"><kbd>⌘S</kbd></Tooltip> ). For example:

        ```md Before/After Example theme={null}
        Before: Verify user can log in with valid email and password
        After: Verify user can log in with email 'example@gmail.com', password 'xxxxxx'
        ```
      </Step>

      <Step title="Prompt in your IDE">
        ```text Example Prompt theme={null}
         Rerun the Xth test for me using testsprite_generate_code_and_execute
        ```
      </Step>

      <Step title="TestSprite runs the updated tests">
        TestSprite will detect your change, update the relevant test code, and run the updated tests automatically.
      </Step>
    </Steps>

    <Info>
      **Key Point:** You only need to change the description in the plan. TestSprite handles the rest.
    </Info>
  </Tab>

  <Tab title="Regenerate Entire Project">
    If you want a clean start or have made major changes:

    <Steps>
      <Step title="Delete the testsprite_tests folder">
        Delete the `testsprite_tests` folder in your project.

        <Frame>
          <img src="https://mintcdn.com/testspriteinc/ex3lblqbetJSa-ak/images/delete-project.png?fit=max&auto=format&n=ex3lblqbetJSa-ak&q=85&s=d74badb1a62d00f4cd42cdbc1f98c6a7" alt="delete" width="1906" height="539" data-path="images/delete-project.png" />
        </Frame>

        <Info>
          This ensures no outdated files remain.
        </Info>
      </Step>

      <Step title="Prompt in your IDE">
        In your IDE, type again:

        ```text Example Prompt theme={null}
        Help me test this project with TestSprite
        ```
      </Step>

      <Step title="TestSprite generates new tests">
        TestSprite will generate a brand new test plan and test code for the whole project.
      </Step>
    </Steps>

    <Warning>
      **When to use this:** If your project has changed a lot and the old test plan no longer matches well.
    </Warning>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).