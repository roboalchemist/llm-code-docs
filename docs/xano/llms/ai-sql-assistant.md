# Source: https://docs.xano.com/xano-ai/ai-sql-assistant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SQL Assistant

<Warning>
  ## **PREVENTING SQL INJECTION ATTACKS**

  Xano offers some filters to help ensure that any dynamic / user input is not parsed in a way that might harm your database or cause other unintended consequences.

  Make sure to process your inputs **before** they are used in any SQL queries with the appropriate filter.

  These filters are [sql\_alias and sql\_esc](/the-function-stack/filters/text#sql_alias)
</Warning>

<Steps>
  <Step title="When using the Direct Database Query function, click SQL Assistant to access the AI SQL assistant.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_oKnuVg5Nf4VhJM4/images/4eaec823-image.jpeg?fit=max&auto=format&n=_oKnuVg5Nf4VhJM4&q=85&s=16b03c8773fff19df121a0ab3840becd" width="156" height="62" data-path="images/4eaec823-image.jpeg" />
    </Frame>

    The assistant can help you write queries against your Xano database.
  </Step>

  <Step title="Provide the assistant with the query you would like it to build.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/757a3322-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=fc9e5035cfea683d9eefa59e55b08c10" width="946" height="204" data-path="images/757a3322-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Once complete, the assistant will present you with the query, along with an explanation of how it works and some records that satisfy the query.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/22cc94f1-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=787bd1f048c1c2e2df10503b8d8a5889" width="2304" height="1674" data-path="images/22cc94f1-image.jpeg" />
    </Frame>
  </Step>

  <Step title="If the query returns the expected results, click Update SQL. Otherwise, you can ask the assistant to make any desired modifications or fixes.">
    You can also make your own modifications to the query, such as adding ? characters to represent dynamic values.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).