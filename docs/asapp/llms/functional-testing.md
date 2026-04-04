# Source: https://docs.asapp.com/generativeagent/configuring/functional-testing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Functional Testing

> Learn how to test GenerativeAgent to ensure it handles customer scenarios correctly before production launch.

Functional Testing is a critical step in evaluating GenerativeAgent after setting requirements for Tasks and Functions. Given the dynamic nature of Large Language Models (LLMs), it's essential to validate that GenerativeAgent works as expected in various scenarios. Testing is the best strategy to ensure reliability and performance before launching any task into production.

This testing phase is a crucial part of your integration process. We strongly recommend completing thorough functional testing, with assistance from the ASAPP team, before deploying GenerativeAgent in a live environment. This process involves verifying, validating, and confirming that GenerativeAgent functions as expected across a wide range of potential user interactions.

It's helpful to have a high-level overview of how GenerativeAgent works while planning your testing. GenerativeAgent assumes it is engaging with a customer who has a problem it can help resolve. GenerativeAgent uses a combination of:

* Task Instructions
* API Response Data
* Retrieved Knowledge Base Articles

If GenerativeAgent cannot help the customer or is unsure about what to do, it will offer to escalate to a live agent.

### Acceptance Testing Objectives

* Ensure GenerativeAgent does not make mistakes given expected inputs
* Focus on preventing potential hallucinations or bad inputs
* Ensure GenerativeAgent handles expected customer scenarios correctly

You perform Functional Testing after your ASAPP Team has configured GenerativeAgent Tasks and Functions. You will be able to fully integrate GenerativeAgent into your apps after the tests are passed.

## Testing Process

### Pretesting

In the pretesting phase, keep in mind cases like the following use case scenarios:

Reading a sample of production scenarios for this task:

* Read summaries for 100 sample conversations to understand typical conversations within this use case across both the virtual agent and those that escalate to a live agent
* Have clear should/must-dos for each task
* Have a clear idea of the things that GenerativeAgent should do vs. must do within each task
* Keep in mind the common scenarios you expect users to go through based on the sample of real conversations
* Clear test users to do the testing
* Consider the permutations of test data that are important to cover. For example:
  * Someone with a flight canceled a few minutes ago
  * Someone with two flights, one which is canceled and one which is not
  * Someone with elite status vs. someone with no status

### Testing GenerativeAgent

Once you've completed the pretesting phase, you're ready to start testing GenerativeAgent itself. This phase involves simulating real-world scenarios and interactions to ensure GenerativeAgent performs as expected. Here are some key points to keep in mind:

* Aim to test approximately 100 conversations per use case
* Go through the expected conversation scenarios, as relevant, for each of the test users
* Make sure to operate in a manner that is consistent with the data in the test account you are using
* Formulate questions, based on the sample of conversations, that aim to test the knowledge articles available to GenerativeAgent
* Plan to repeat some scenarios with slight variation to ensure GenerativeAgent responses are consistent (though no response is likely to ever be exactly the same due to its generative nature)

## Example Test

The following is an example scenario of Functional Testing for a task.

### Test Scenario

If a customer asks about their flight status, GenerativeAgent should provide the relevant details.

### Preconditions

A correct confirmation number and last name

### Test Procedure

1. IF a customer asks about their current flight status
2. THEN GenerativeAgent will invoke the flight\_status task
3. AND GenerativeAgent will request the necessary criteria to look up the customer's flight details
4. AND if the customer provides a valid confirmation number and last name
5. THEN GenerativeAgent will call the appropriate API
6. AND GenerativeAgent will retrieve the required information
7. AND GenerativeAgent will inform the customer of their current flight status based on the API response

### Test Objectives

1. Confirm that GenerativeAgent correctly invokes the flight\_status task
2. Verify that GenerativeAgent identifies the necessary information from the customer to verify the flight
3. Ensure that GenerativeAgent requests the required information (confirmation number and last name)
4. Check that the appropriate API is called
5. Validate the information provided by the customer through the API
6. Ensure GenerativeAgent gathers the necessary flight status information
7. Confirm GenerativeAgent accurately communicates the flight status to the customer

This example illustrates the "happy path." But there are other scenarios such as: what if the customer only provides a confirmation number? Can they provide alternative information? What if the customer doesn't have a confirmation number? Consider other potential scenarios and instructions to test against.

## Next Steps

With correct Acceptance Testing, you are ready to support real users.

You may find one of the following sections helpful in advancing your integration:

<CardGroup cols={3}>
  <Card title="Connect your APIs" href="/generativeagent/configuring/connect-apis" />

  <Card title="Safety and Troubleshooting" href="/generativeagent/configuring/safety-and-troubleshooting" />

  <Card title="Go Live" href="/generativeagent/go-live" />
</CardGroup>
