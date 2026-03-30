# Source: https://docs.xano.com/ci-cd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CI/CD

> Learn more about CI/CD inside of Xano

<Info>
  **Quick Summary**

  CI/CD stands for \*\*continuous integration and continuous delivery \*\*and is a set of best practices that define how new logic is tested and deployed.

  While fully automated CI/CD is not available today in Xano, we have a number of features designed to replicate the most important pieces of the concept, outlined below.

  Each feature mentioned below offers its own in-depth documentation, which we also recommend reviewing.
</Info>

## CI/CD Explained

CI/CD is a technique used in software development to make the process of updating applications faster and more reliable.

CI, or Continuous Integration, involves regularly adding small updates to the codebase, helping developers catch and fix errors quickly. CD, or Continuous Delivery, ensures these updates can be automatically tested and deployed to production environments seamlessly. Together, these practices help deliver new features and improvements to users more efficiently, ensuring a better, more stable experience.

In Xano, you can think of any function stacks you're building as your **codebase**. Features such as **branching/merging, unit and workflow tests**, and **triggers** can all play a role in building a seamless CI/CD-style workflow in Xano for you and your team.

## Achieving CI/CD in Xano

<Steps>
  <Step title="Build your Dev, Stage, and Prod Environments">
    Typically, you'll have at least three environments for proper development.

    * **Dev** - This is where you build updates and new features
    * **Stage** - This is where you deploy changes and initiate testing to ensure they work as expected, and there are no new bugs or regressions (old bugs returning) introduced
    * **Prod** - This is the production environment that serves the live experience to your users

    These environments in Xano are best laid out differently, depending on your plan.

    * **Launch / Self-Serve Plans**: Use [Branching & Merging](/team-collaboration/branching-and-merging) and create separate branches for dev, stage, and prod. Your frontend should typically only be calling production endpoints, but you can also deploy a second frontend for testing that defaults to stage or dev
    * **Scale, Pro, Custom or Enterprise Plans with Xano Link**: Deploy your changes to separate workspaces using [Xano Link](/xano-features/advanced-back-end-features/xano-link)
    * **Enterprise or Custom Plans with Tenant Center**: Create separate tenants in your [Tenant Center](/enterprise/enterprise-features/tenant-center) for each environment, and deploy releases to them
  </Step>

  <Step title="Build Tests">
    You should always be building tests for your function stacks using our [Unit Tests](/testing-debugging/unit-tests) and [Test Suites](/testing-debugging/test-suites) features. Unit Tests are designed to run a test on a single function stack (such as a sign-up API), and Test Suites (Workflow Tests) are designed to check what would be a typical multi-step flow for your application (such as a user signing up, purchasing a subscription plan, and receiving a confirmation email).

    To ensure full coverage, make sure that your tests not only check for positive results, but they also check for proper error handling when things go wrong. The goal is not necessarily to achieve 100% success, but to achieve 100% coverage for all possible scenarios.
  </Step>

  <Step title="Deploy Changes to Stage & Test">
    Deploy your changes to Stage and run your [Unit Tests](/testing-debugging/unit-tests) and [Test Suites](/testing-debugging/test-suites) to ensure everything is behaving as expected.

    If you have tests that fail, it would be recommended to head back to your development environment and make any corrections necessary, and deploy those new changes back to Stage to test again.
  </Step>

  <Step title="Pushing to Production">
    Once you've confirmed that your tests pass and you have full coverage, you can push your changes to your production branch or environment.
  </Step>
</Steps>

<Warning>
  **How do tests impact my database?**

  [Test Suites](/testing-debugging/test-suites) create a duplicate copy of your database, temporarily, just for testing. So, if your production database is large or complex, you may have trouble completing your tests or experience additional complications. It is strongly recommended to utilize [Data Sources](/the-database/database-basics/data-sources) to navigate around this potential issue.

  You can also run tests with no database **(Empty)** if a database is not necessary for that specific test, or if your tests can run from an empty database, such as if they're only adding data that isn't used later anywhere.
</Warning>

## Additional Notes

### Managing Environment Variables

If you're working with external services, you may require different configurations between your development, stage, and production environments, such as different API keys. Typically, you'd store these in your [Environment Variables](/the-function-stack/environment-variables).

* **If you're using Branching/Merging**, you'll be limited to storing all environment variables together. You can use statements like [Get Environment Variables](/the-function-stack/functions/utility-functions#get-environment-variables) to manually parse all available environment variables and retrieve the ones necessary depending on the branch you're on.
* **If you're using Xano Link**, each workspace can contain its own environment variables, and no additional logic is necessary.
* **If you're using Tenant Center**, you have the ability to manage each tenant's environment variables from the Tenant Center. Each tenant can contain its own environment variables, and no additional logic is necessary.

### Managing Development Across Teams

Each team or team member should be responsible for developing specific features. Ideally, these features would not cross-contaminate function stacks that separate teams or team members might be working on.

If you find that multiple team members need to work on the same function stacks, we have [Team Collaboration](/team-collaboration/realtime-collaboration) features built right into Xano to ensure that the experience is as smooth as possible.

If your plan has access to RBAC (Role-based Access Control), it is imperative that you manage permissions properly to ensure that only specific team members can push changes from development to stage, and even more so from stage to production. Be sure to review our documentation on [Role-based Access Control (RBAC)](/team-collaboration/role-based-access-control-rbac) for more information.

### Using Mock Responses for Test-Driven Development

For certain steps, you should also be [Mocking Responses](/testing-debugging/unit-tests#mocking-responses) both for the sake of speed and consistency when running your tests.

As an example, if you're calling an external API and want to ensure that you always test with the same response, you can add a mock response to your unit test to accommodate that. This allows for **test driven development**, or essentially being able to have different team members build endpoints that you'll be relying on, but might not be complete yet. Adding a mock response allows you to continue working alongside the other team member, instead of having to wait.


Built with [Mintlify](https://mintlify.com).