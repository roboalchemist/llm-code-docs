# Source: https://docs.xano.com/deployment-readiness.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Readiness

> Ensure your Xano backend is production-ready with performance checks, testing, and validation strategies.

<Info>
  **Quick Summary**

  Before deploying your Xano backend to production, you need to validate that it's ready to handle real-world usage. This involves **checking performance metrics**, **building and running comprehensive tests**, **dry-running your application with test data**, and optionally **load testing with external tools**. This checklist ensures your backend is stable, performant, and reliable before your users interact with it.
</Info>

Deploying to production without proper validation is like launching a rocket without a pre-flight checklist—you're flying blind. Deployment readiness is about **confidence**: knowing that your backend will perform as expected under real-world conditions, handle edge cases gracefully, and maintain data integrity.

This guide walks you through the essential steps to ensure your Xano backend is production-ready.

***

## How to Ensure Deployment Readiness

### 1. Check and Review Performance

Before deploying, you need to understand how your backend is currently performing and identify any bottlenecks or slow operations.

<Steps>
  <Step title="Access Performance Insights">
    From the **Library** tab in the left-hand navigation, select **Performance Insights**.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/XlIAg1M2l6fscwDG/images/performance-insights-20250919-153718.png?fit=max&auto=format&n=XlIAg1M2l6fscwDG&q=85&s=e8bb75b665823851487297cac75d002d" alt="Performance Insights Location" width="1536" height="1238" data-path="images/performance-insights-20250919-153718.png" />
    </Frame>
  </Step>

  <Step title="Review Key Metrics">
    Analyze your backend's performance across different time periods (last 24 hours, 7 days, or 30 days):

    * **Average Execution Time**: How long does each function or API take to run on average?
    * **Total Execution Count**: Which endpoints are being called most frequently?
    * **Resource-Intensive Operations**: Identify the top 5 slowest database queries or functions.

    Focus on:

    * API endpoints that will receive high traffic
    * Database queries (especially Query All Records operations)
    * External API calls or Lambda functions
    * Background tasks that process large datasets
  </Step>

  <Step title="Optimize Slow Operations">
    For any operations that seem slow or resource-intensive:

    * Review the function stack to identify inefficiencies
    * Optimize database queries using filters, pagination, or indexes
    * Consider caching frequently accessed data
    * Break down complex operations into smaller, parallelizable tasks
    * Use [mocking responses](/testing-debugging/unit-tests#mocking-responses) for external API calls during testing
  </Step>

  <Step title="Monitor Request History">
    Review your [Request History](/maintenance-monitoring-and-logging/request-history) to:

    * Identify failed API calls and their causes
    * Check average runtime across all endpoints
    * Review input/output sizes to ensure data payloads are reasonable
    * Filter by duration to spot performance outliers
  </Step>
</Steps>

**Why this matters**: Performance issues that are minor during development can become critical under production load. Identifying and resolving bottlenecks before deployment prevents user-facing slowdowns and service interruptions.

***

### 2. Build and Run Unit & Workflow Tests

Testing validates that your backend behaves correctly across all scenarios—both success cases and error handling.

<Steps>
  <Step title="Create Unit Tests for Individual Endpoints">
    Build [Unit Tests](/testing-debugging/unit-tests) for each critical API endpoint and custom function:

    * From any API or function, use **Run & Debug** to test with sample inputs
    * Once you achieve the desired result, click **Create Unit Test**
    * Define **Expects** statements to validate the output (e.g., "response.authToken is defined")
    * Add multiple expect statements to test different aspects of the response

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f55250f4-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=8607c041b673a99bef9e465fdb3b71e2" alt="Create Unit Test" width="687" height="466" data-path="images/f55250f4-image.jpeg" />
    </Frame>

    **Best Practices**:

    * Test both success scenarios (valid inputs) and failure scenarios (invalid inputs, missing data, etc.)
    * Use [mock responses](/testing-debugging/unit-tests#mocking-responses) for external API calls to ensure consistent, fast tests
    * Set up auth token handling to avoid expiration issues during testing
  </Step>

  <Step title="Build Workflow Tests for User Flows">
    Create [Test Suites (Workflow Tests)](/testing-debugging/test-suites) to validate multi-step processes:

    * From **Library** > **Workflow Tests**, create a new test suite
    * Add **Run Stack** functions to call your APIs in sequence (e.g., signup → login → purchase → confirmation email)
    * Add **Test Expression** functions to validate each step's output
    * Test complete user journeys from start to finish

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/27f6db14-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=e2e919d740e545a6410bbe775729c497" alt="Workflow Test Example" width="994" height="693" data-path="images/27f6db14-image.jpeg" />
    </Frame>

    **Example workflow tests**:

    * User registration → Email verification → Profile setup
    * Add to cart → Apply coupon → Checkout → Payment → Order confirmation
    * Data import → Processing → Validation → Export
  </Step>

  <Step title="Run All Tests and Review Coverage">
    From the **Unit Tests** page in your Library:

    * Click **Run Test Suites** to execute all tests at once
    * Review your **coverage percentage** (what % of your function stacks have tests)
    * Check your **success rate** (what % of tests are passing)
    * Filter by "Failed Only" to quickly identify and fix issues

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a477590e-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=a3790a5eb6e1e6a9a43f451eab7e161e" alt="Test Suite Results" width="1079" height="555" data-path="images/a477590e-image.jpeg" />
    </Frame>

    **Goal**: Aim for 100% coverage of critical paths and 100% success rate before deployment.
  </Step>
</Steps>

**Why this matters**: Tests act as a safety net, catching bugs and regressions before they reach production. They enable you to deploy with confidence, knowing that your backend behaves correctly across all scenarios. Tests also enable **continuous integration**—as you make changes, you can quickly validate that nothing broke.

***

### 3. Use a Test Data Source to Dry-Run Your Application

Never test or iterate on your live production data. Use [Data Sources](/the-database/database-basics/data-sources) to create isolated test environments.

<Steps>
  <Step title="Create a Test Data Source">
    * From the left-side navigation, click on your current data source indicator (e.g., "Live")
    * Click **+ Add Data Source**
    * Give it a descriptive name like "Test" or "Staging"
    * Assign a distinct color (this color will appear throughout Xano to remind you which data source you're using)

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cfb50a9d-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=5a2a1893df2f39107eb7bf2882c243aa" alt="Create Data Source" width="508" height="228" data-path="images/cfb50a9d-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Populate Your Test Data Source">
    You have several options:

    **Option 1: Migrate from Live**

    * Go to **Manage Data Sources** > **Migrate**
    * Select your live data source as the source
    * Select your test data source as the destination
    * Choose which tables to migrate
    * This creates a copy of your live data for testing

    **Option 2: Create Sample Data**

    * Manually add representative test records
    * Use realistic data that mirrors production scenarios
    * Include edge cases (empty strings, null values, maximum lengths, etc.)

    **Option 3: Start Empty**

    * For workflow tests that only add data, you can start with an empty database
  </Step>

  <Step title="Switch to Your Test Data Source">
    * Click the data source indicator in the left navigation
    * Select your test data source from the list
    * All Run & Debug operations, unit tests, and workflow tests will now use test data

    <Info>
      Switching data sources in Xano only affects your development work—it does **not** change what your live application uses.
    </Info>
  </Step>

  <Step title="Dry-Run Your Application Internally">
    * Run through typical user workflows manually using Run & Debug
    * Execute your unit tests and workflow tests against the test data
    * Make changes and iterate without fear of corrupting production data
    * Test destructive operations (deletes, bulk updates) safely
  </Step>

  <Step title="Connect a Test Frontend (Optional)">
    If you have a frontend application:

    * Deploy a separate staging/test version of your frontend
    * Use the `X-Data-Source` header in API requests to target your test data:
      ```bash  theme={null}
      X-Data-Source: test
      ```
    * Or append a URL parameter:
      ```
      ?x-data-source=test
      ```
    * This allows your test frontend to interact with test data while your production frontend uses live data
  </Step>
</Steps>

**Why this matters**: Test data sources isolate your development and testing from production data. This prevents accidental data corruption, allows you to test destructive operations safely, and speeds up testing by avoiding the overhead of large production databases. For [CI/CD workflows](/ci-cd), separate data sources are essential for maintaining development, staging, and production environments.

***

### 4. Load Testing (External Tools Required)

Xano doesn't provide built-in load testing, but you can use external tools to simulate high-traffic scenarios and ensure your backend can handle production load.

<Steps>
  <Step title="Choose a Load Testing Tool">
    Popular options include:

    * **[Apache JMeter](https://jmeter.apache.org/)**: Open-source, highly configurable
    * **[Artillery](https://www.artillery.io/)**: Modern, developer-friendly, YAML-based
    * **[k6](https://k6.io/)**: JavaScript-based, excellent for developers
    * **[Loader.io](https://loader.io/)**: Cloud-based, easy to use
    * **[BlazeMeter](https://www.blazemeter.com/)**: Enterprise-grade, integrates with JMeter
  </Step>

  <Step title="Design Your Load Tests">
    Create scenarios that mirror real-world usage:

    * **Concurrent Users**: How many users will use your app simultaneously?
    * **Request Patterns**: What endpoints do users hit most frequently?
    * **Ramp-Up Period**: How quickly does traffic increase?
    * **Peak Load**: What's the maximum expected traffic (e.g., during a product launch)?

    **Example scenario**:

    * Start with 10 concurrent users
    * Ramp up to 1,000 users over 10 minutes
    * Each user performs: Login → Browse products → Add to cart → Checkout
    * Measure response times, error rates, and throughput
  </Step>

  <Step title="Configure Your Test Environment">
    **Important**: Load test against a **staging environment** or **test branch**, not production!

    * If you're on Launch, Starter, or Essential: Use [Branching](/team-collaboration/branching-and-merging) to create a staging branch
    * If you're on Pro/Scale/Custom/Enterprise Plans: Consider a separate workspace or use [Xano Link](/xano-features/advanced-back-end-features/xano-link)
    * Use a test data source to avoid impacting live data
    * Ensure your test environment mirrors production configuration
  </Step>

  <Step title="Run the Load Test">
    Execute your load test and monitor:

    * **Response Times**: Are endpoints responding quickly under load?
    * **Error Rates**: Are requests failing? What status codes are returned?
    * **Throughput**: How many requests per second can your backend handle?
    * **Resource Usage**: Monitor API and database node utilization (if you have access to these metrics)
  </Step>

  <Step title="Analyze Results and Scale Accordingly">
    Based on your load test results:

    * If performance degrades under load, review [Performance Insights](/maintenance-monitoring-and-logging/performance-insights) to identify bottlenecks
    * Consider [upgrading your Scale plan](/adjust-server-performance) if you're hitting resource limits
    * Optimize slow queries, add caching, or refactor complex operations
    * Re-run tests after optimizations to measure improvement

    **Scale Plan Considerations**:

    * **API Nodes**: Handle business logic and endpoint requests
    * **Database Nodes**: Handle concurrent database queries
    * As usage grows, you may need to upgrade from Scale 1x → 2x → 4x → 8x
    * Enterprise plans offer auto-scaling and horizontal database scaling
  </Step>
</Steps>

**Why this matters**: Load testing reveals how your backend behaves under realistic (or extreme) traffic conditions. It helps you identify breaking points, plan capacity, and ensure a smooth user experience even during traffic spikes. Without load testing, you're guessing at your backend's capabilities.

***

## The Mental Model: Why This Flow Works

Deployment readiness is about **progressive validation**—starting small and building confidence as you expand your testing scope.

### The Pyramid of Confidence

```
        🚀 Production
       /            \
      /   Load Test   \     ← External validation
     /                  \
    /   Dry-Run (Test)   \  ← Real-world simulation
   /                      \
  /  Workflow Tests (Flow) \ ← Multi-step validation
 /                          \
/    Unit Tests (Function)   \ ← Foundational validation
--------------------------------
   Performance Insights       ← Baseline understanding
```

1. **Performance Insights** give you a baseline understanding of how things currently perform
2. **Unit Tests** validate individual components work correctly in isolation
3. **Workflow Tests** validate that components work together in realistic flows
4. **Dry-Running with Test Data** simulates real-world usage without risk
5. **Load Testing** validates your backend can handle production-level traffic
6. **Production Deployment** happens with confidence, knowing you've validated every layer

### Why This Order?

* **Bottom-up confidence**: Fix individual issues before testing complex flows
* **Iterative refinement**: Each layer reveals different types of issues
* **Risk mitigation**: Catch problems early when they're cheaper to fix
* **Data safety**: Test data isolation prevents production data corruption
* **Performance planning**: Load testing informs infrastructure decisions before you need to scale

### Integration with CI/CD

This deployment readiness checklist integrates seamlessly with [CI/CD workflows](/ci-cd):

* **Dev**: Build features, create unit tests
* **Stage**: Run workflow tests, dry-run with test data
* **Pre-Production**: Load test, review performance insights
* **Production**: Deploy with confidence

***

## Deployment Readiness Checklist

Before deploying to production, ensure you've completed:

* [ ] Reviewed [Performance Insights](/maintenance-monitoring-and-logging/performance-insights) for the past 7-30 days
* [ ] Identified and optimized slow-running queries and functions
* [ ] Created [Unit Tests](/testing-debugging/unit-tests) for all critical API endpoints
* [ ] Built [Workflow Tests](/testing-debugging/test-suites) for key user flows
* [ ] Achieved 100% test coverage for critical paths
* [ ] Achieved 100% test success rate (or documented acceptable failures)
* [ ] Created and populated a [Test Data Source](/the-database/database-basics/data-sources)
* [ ] Dry-run your application using test data
* [ ] Performed load testing with external tools (optional but recommended)
* [ ] Reviewed [Request History](/maintenance-monitoring-and-logging/request-history) for errors and anomalies
* [ ] Verified that your [Scale plan](/adjust-server-performance) can handle expected traffic
* [ ] Set up proper [branching strategy](/team-collaboration/branching-and-merging) for ongoing deployments
* [ ] Reviewed [OpenAPI documentation](/the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation) to ensure endpoints are clearly documented

***

## Next Steps

Once you've validated deployment readiness:

1. **Publish your changes**: Ensure all drafted work is published to your live environment
2. **Review your branching strategy**: See [Branching & Merging](/team-collaboration/branching-and-merging)
3. **Connect your frontend**: Follow the [Connecting to a Frontend](/connecting-to-a-frontend) guide
4. **Set up monitoring**: Use [Request History](/maintenance-monitoring-and-logging/request-history) and [Performance Insights](/maintenance-monitoring-and-logging/performance-insights) to monitor production performance
5. **Plan for scale**: Review [Adjust Server Performance](/adjust-server-performance) if you anticipate growth

> 💡 **Pro Tip**: Deployment readiness isn't a one-time checklist—it's an ongoing practice. As you add new features, repeat these steps to maintain confidence in your backend's stability.


Built with [Mintlify](https://mintlify.com).