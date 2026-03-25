# Source: https://docs.testsprite.com/web-portal/maintenance/test-lists.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.testsprite.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Lists

> Organize test collections, track execution history, and manage testing projects efficiently.

Test Lists are organized collections of test cases that help you group related tests together. Whether you're testing different features, environments, or user flows, Test Lists provide a structured way to manage your testing efforts.

<Frame>
  <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/test-list.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=cac7b677cd8b19505ed1483e7ec99d43" alt="plan" width="1642" height="977" data-path="images/test-list.png" />
</Frame>

## Key Features

| Feature                                | Description                                                                                                                                                                                                                              |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <kbd>Centralized Test Management</kbd> | View all test lists in one dashboard, track execution status across collections, search and filter by name or status, and sort by date, count, or type                                                                                   |
| <kbd>Test Organization</kbd>           | Organize Frontend Tests with browser automation, Backend Tests for API functionality, and Mixed Collections combining both test types                                                                                                    |
| <kbd>Execution Tracking</kbd>          | Track your **previous execution** status to view the test's last run with **status indicators** showing **Passed** (all tests completed successfully), **Attention** (some tests need review), or **Failed** (tests encountered errors). |

## Creating Test Lists

<Steps>
  <Step title="Navigate to Test Lists">
    Go to <kbd>Dashboard</kbd> → <kbd>Test Lists</kbd> and click <kbd>New List</kbd> to get started

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/navigate-testlist.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=ea4737756f57bf6a195fa82c592d3cdc" alt="plan" width="1642" height="705" data-path="images/navigate-testlist.png" />
    </Frame>
  </Step>

  <Step title="Add Test Cases">
    Add test cases from existing creations in <kbd>All Test</kbd>, or create new tests by configuring web application information and letting TestSprite's AI generate comprehensive test cases

    <Frame>
      <img src="https://mintcdn.com/testspriteinc/QYauUtR7JhW8Lgzr/images/add-test.png?fit=max&auto=format&n=QYauUtR7JhW8Lgzr&q=85&s=3505262df315c0f422164769773cb525" alt="mcp intro" width="1642" height="705" data-path="images/add-test.png" />
    </Frame>
  </Step>

  <Step title="Organize and Configure">
    Name your test list descriptively, review and customize generated test cases, and maintain your test lists as needed
  </Step>
</Steps>

## Managing Test Lists

<Tabs>
  <Tab title="Search & Filter">
    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/testlist-filter.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=660f401abdd9cadbb3b3c534a7876319" alt="plan" width="1642" height="442" data-path="images/testlist-filter.png" />
    </Frame>

    | Option                | Description                                                   |
    | :-------------------- | :------------------------------------------------------------ |
    | <kbd>Search</kbd>     | Search by test list name to quickly find specific collections |
    | <kbd>All Status</kbd> | View all test lists regardless of status                      |
    | <kbd>Passed</kbd>     | Show only successfully executed test lists                    |
    | <kbd>Attention</kbd>  | Filter test lists needing review                              |
    | <kbd>Failed</kbd>     | Display test lists with execution errors                      |
  </Tab>

  <Tab title="Sorting Options">
    <Frame>
      <img src="https://mintcdn.com/testspriteinc/etE5QHi14YOHx37z/images/testlist-sort.png?fit=max&auto=format&n=etE5QHi14YOHx37z&q=85&s=0550940ec67f0af9e653e1f37f8d85e2" alt="plan" width="1642" height="644" data-path="images/testlist-sort.png" />
    </Frame>

    | Option                             | Description                          |
    | :--------------------------------- | :----------------------------------- |
    | <kbd>Total test cases</kbd>        | Order by number of tests in the list |
    | <kbd>Total frontend test</kbd>     | Order by frontend test count         |
    | <kbd>Total backend test</kbd>      | Sort by backend test count           |
    | <kbd>Previous execution date</kbd> | Sort by most recently executed       |
  </Tab>
</Tabs>

## Test List Details

Each test list displays:

| Field                          | Description                                     |
| :----------------------------- | :---------------------------------------------- |
| <kbd>Test List Name</kbd>      | Descriptive identifier for your test collection |
| <kbd>Previous Execution</kbd>  | Last run date and time                          |
| <kbd>Total Test Cases</kbd>    | Combined count of all tests in the list         |
| <kbd>Total Frontend Test</kbd> | Number of UI/browser tests                      |
| <kbd>Total Backend Test</kbd>  | Number of API/server tests                      |

## Execution Actions

| Action                  | Description                          |
| :---------------------- | :----------------------------------- |
| <kbd>Run Tests</kbd>    | Execute all tests in the list        |
| <kbd>View Results</kbd> | Review detailed test reports         |
| <kbd>Delete List</kbd>  | Remove test list (with confirmation) |


Built with [Mintlify](https://mintlify.com).