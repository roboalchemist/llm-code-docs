# Source: https://docs.carv.io/d.a.t.a.-ai-framework/use-cases-and-implementation/getting-on-chain-data-for-ai-agents.md

# Getting On-Chain Data for AI Agents

## **Using D.A.T.A Framework Backend for Query Generation**

The **D.A.T.A Framework** provides a backend service that can generate dynamic queries based on user input. The backend supports various types of queries, including SQL, key-value queries, and vector-based queries for more advanced use cases such as AI-driven data retrieval.

**How It Works:**

1. **User Input**: The AI agent receives a natural language query from the user. The query could be something like, “What is the total gas used yesterday, and how many transactions occurred yesterday?”
2. **Query Generation**: The AI agent send the user query to **D.A.T.A Framework** backend, which processes the user input and generates the corresponding queries (SQL, key-value, vector) to fetch the required data. This is done by analyzing the query and breaking it down into structured data requests.
3. **Query Types**:
   * **SQL Queries**: For complex data retrieval from on-chain transaction histories, token transfers, gas usage, etc.
   * **Key-Value Queries**: For fetching specific data points like balances, token ownership, etc.
   * **Vector Queries**: For fetching off-chain data related to blockchain activity, such as relevant social media posts or market sentiment analysis.
4. **Assembling the Query**: After generating the necessary queries, the backend will assemble them into a **response format**. The output typically includes the SQL or key-value queries with placeholders for the result (e.g., `{{result}}`), which will later be replaced with actual data.
5. **Query Execution**: The generated queries are then posted to the **D.A.T.A Framework backend**. The backend handles querying the relevant blockchain or data sources, processes the data, and formats the response accordingly.
6. **Response Handling**: After execution, the **provider info** is returned to the AI agent in a structured format, allowing it to make informed decisions or trigger further actions.

**Example Workflow:**

1. **User Query**: “What is the total gas used yesterday, and how many transactions happened yesterday?”
2. **AI Agent send the user query to D.A.T.A framework backend and then generates SQL Query**:

   ```json
   {
       "status": "success",
       "network": "Ethereum",
       "dataSources": [
           {
               "type": "sql",
               "data": "SELECT SUM(gas_used) AS total_gas_used FROM eth.blocks WHERE block_timestamp >= TIMESTAMP '2024-12-01 00:00:00' AND block_timestamp < TIMESTAMP '2024-12-02 00:00:00';",
               "resultFormat": "total_gas_used (Ethereum): {{result}}"
           },
           {
               "type": "sql",
               "data": "SELECT COUNT(*) AS transaction_count FROM eth.transactions WHERE block_timestamp >= TIMESTAMP '2024-12-01 00:00:00' AND block_timestamp < TIMESTAMP '2024-12-02 00:00:00';",
               "resultFormat": "transaction_count (Ethereum): {{result}}"
           }
       ]
   }
   ```
3. **AI Agent posts to D.A.T.A Backend**: The AI agent sends these SQL queries to the D.A.T.A backend.
4. **Response Format**: The backend executes the queries, retrieves the data, and returns a structured response with the requested information:

   ```json
   {
       "status": "success",
       "total_gas_used": 5000000,
       "transaction_count": 1000
   }
   ```

## **2. Using Arbtrary AI Models to Generate Queries and Assemble Output**

In addition to using the **D.A.T.A Framework** backend for query generation, any AI models can also be used to generate custom queries based on prompts. This allows developers to integrate the **D.A.T.A Framework** into their own AI models, giving them flexibility in how they interact with on-chain data.

**How It Works:**

1. **Custom AI Agent**: In this approach, the user or developer integrates the **D.A.T.A Framework** with their custom AI agent, leveraging any model capable of understanding user prompts and generating the necessary queries (SQL, key-value, vector, etc.).
2. **Query Generation via Prompts**: The AI model generates the queries based on pre-trained data and the user’s request. For example, the prompt might instruct the model to generate a SQL query to fetch the total gas usage and transaction counts for a specific date range.
3. **Prompt Example for SQL Query Generation**:&#x20;
4. **Prompt**:

   ````typescript
   getDatabaseSchema(): string {
           return `
           CREATE EXTERNAL TABLE transactions(
               hash string,
               nonce bigint,
               block_hash string,
               block_number bigint,
               block_timestamp timestamp,
               date string,
               transaction_index bigint,
               from_address string,
               to_address string,
               value double,
               gas bigint,
               gas_price bigint,
               input string,
               max_fee_per_gas bigint,
               max_priority_fee_per_gas bigint,
               transaction_type bigint
           ) PARTITIONED BY (date string)
           ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
           STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
           OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat';

           CREATE EXTERNAL TABLE token_transfers(
               token_address string,
               from_address string,
               to_address string,
               value double,
               transaction_hash string,
               log_index bigint,
               block_timestamp timestamp,
               date string,
               block_number bigint,
               block_hash string
           ) PARTITIONED BY (date string)
           ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
           STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
           OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat';
           `;
       }

       getQueryExamples(): string {
           return `
           Common Query Examples:

           1. Find Most Active Addresses in Last 7 Days:
           WITH address_activity AS (
               SELECT
                   from_address AS address,
                   COUNT(*) AS tx_count
               FROM
                   eth.transactions
               WHERE date_parse(date, '%Y-%m-%d') >= date_add('day', -7, current_date)
               GROUP BY
                   from_address
               UNION ALL
               SELECT
                   to_address AS address,
                   COUNT(*) AS tx_count
               FROM
                   eth.transactions
               WHERE
                   date_parse(date, '%Y-%m-%d') >= date_add('day', -7, current_date)
               GROUP BY
                   to_address
           )
           SELECT
               address,
               SUM(tx_count) AS total_transactions
           FROM
               address_activity
           GROUP BY
               address
           ORDER BY
               total_transactions DESC
           LIMIT 10;

           2. Analyze Address Transaction Statistics (Last 30 Days):
           WITH recent_transactions AS (
               SELECT
                   from_address,
                   to_address,
                   value,
                   block_timestamp,
                   CASE
                       WHEN from_address = :address THEN 'outgoing'
                       WHEN to_address = :address THEN 'incoming'
                       ELSE 'other'
                   END AS transaction_type
               FROM eth.transactions
               WHERE date >= date_format(date_add('day', -30, current_date), '%Y-%m-%d')
                   AND (from_address = :address OR to_address = :address)
           )
           SELECT
               transaction_type,
               COUNT(*) AS transaction_count,
               SUM(CASE WHEN transaction_type = 'outgoing' THEN value ELSE 0 END) AS total_outgoing_value,
               SUM(CASE WHEN transaction_type = 'incoming' THEN value ELSE 0 END) AS total_incoming_value
           FROM recent_transactions
           GROUP BY transaction_type;

           3. Token Transfer Analysis:
           WITH filtered_transactions AS (
               SELECT
                   token_address,
                   from_address,
                   to_address,
                   value,
                   block_timestamp
               FROM eth.token_transfers
               WHERE token_address = :token_address
                   AND date >= :start_date
           )
           SELECT
               COUNT(*) AS transaction_count,
               SUM(value) AS total_transaction_value,
               MAX(value) AS max_transaction_value,
               MIN(value) AS min_transaction_value,
               MAX_BY(from_address, value) AS max_value_from_address,
               MAX_BY(to_address, value) AS max_value_to_address,
               MIN_BY(from_address, value) AS min_value_from_address,
               MIN_BY(to_address, value) AS min_value_to_address
           FROM filtered_transactions;

           Note: Replace :address, :token_address, and :start_date with actual values when querying.
           `;
       }

       getQueryTemplate(): string {
           return `
           # Database Schema
           {{databaseSchema}}

           # Query Examples
           {{queryExamples}}

           # User's Query
           {{userQuery}}

           # Query Guidelines:
           1. Time Range Requirements:
              - ALWAYS include time range limitations in queries
              - Default to last 3 months if no specific time range is mentioned
              - Use date_parse(date, '%Y-%m-%d') >= date_add('month', -3, current_date) for default time range
              - Adjust time range based on user's specific requirements

           2. Query Optimization:
              - Include appropriate LIMIT clauses
              - Use proper indexing columns (date, address, block_number)
              - Consider partitioning by date
              - Add WHERE clauses for efficient filtering

           3. Response Format Requirements:
              You MUST respond in the following JSON format:
              {
                "sql": {
                  "query": "your SQL query string",
                  "explanation": "brief explanation of the query",
                  "timeRange": "specified time range in the query"
                },
                "analysis": {
                  "overview": {
                    "totalTransactions": "number",
                    "timeSpan": "time period covered",
                    "keyMetrics": ["list of important metrics"]
                  },
                  "patterns": {
                    "transactionPatterns": ["identified patterns"],
                    "addressBehavior": ["address analysis"],
                    "temporalTrends": ["time-based trends"]
                  },
                  "statistics": {
                    "averages": {},
                    "distributions": {},
                    "anomalies": []
                  },
                  "insights": ["key insights from the data"],
                  "recommendations": ["suggested actions or areas for further investigation"]
                }
              }

           4. Analysis Requirements:
              - Focus on recent data patterns
              - Identify trends and anomalies
              - Provide statistical analysis
              - Include risk assessment
              - Suggest further investigations

           Example Response:
           {
             "sql": {
               "query": "WITH recent_txs AS (SELECT * FROM eth.transactions WHERE date_parse(date, '%Y-%m-%d') >= date_add('month', -3, current_date))...",
               "explanation": "Query fetches last 3 months of transactions with aggregated metrics",
               "timeRange": "Last 3 months"
             },
             "analysis": {
               "overview": {
                 "totalTransactions": 1000000,
                 "timeSpan": "2024-01-01 to 2024-03-12",
                 "keyMetrics": ["Average daily transactions: 11000", "Peak day: 2024-02-15"]
               },
               "patterns": {
                 "transactionPatterns": ["High volume during Asian trading hours", "Weekend dips in activity"],
                 "addressBehavior": ["5 addresses responsible for 30% of volume", "Increasing DEX activity"],
                 "temporalTrends": ["Growing transaction volume", "Decreasing gas costs"]
               },
               "statistics": {
                 "averages": {
                   "dailyTransactions": 11000,
                   "gasPrice": "25 gwei"
                 },
                 "distributions": {
                   "valueRanges": ["0-1 ETH: 60%", "1-10 ETH: 30%", ">10 ETH: 10%"]
                 },
                 "anomalies": ["Unusual spike in gas prices on 2024-02-01"]
               },
               "insights": [
                 "Growing DeFi activity indicated by smart contract interactions",
                 "Whale addresses showing increased accumulation"
               ],
               "recommendations": [
                 "Monitor growing gas usage trend",
                 "Track new active addresses for potential market signals"
               ]
             }
           }
           `;
       }

       getAnalysisInstruction(): string {
           return `
               1. Data Overview:
                   - Analyze the overall pattern in the query results
                   - Identify key metrics and their significance
                   - Note any unusual or interesting patterns

               2. Transaction Analysis:
                   - Examine transaction values and their distribution
                   - Analyze gas usage patterns
                   - Evaluate transaction frequency and timing
                   - Identify significant transactions or patterns

               3. Address Behavior:
                   - Analyze address interactions
                   - Identify frequent participants
                   - Evaluate transaction patterns for specific addresses
                   - Note any suspicious or interesting behavior

               4. Temporal Patterns:
                   - Analyze time-based patterns
                   - Identify peak activity periods
                   - Note any temporal anomalies
                   - Consider seasonal or cyclical patterns

               5. Token Analysis (if applicable):
                   - Examine token transfer patterns
                   - Analyze token holder behavior
                   - Evaluate token concentration
                   - Note significant token movements

               6. Statistical Insights:
                   - Provide relevant statistical measures
                   - Compare with typical blockchain metrics
                   - Highlight significant deviations
                   - Consider historical context

               7. Risk Assessment:
                   - Identify potential suspicious activities
                   - Note any unusual patterns
                   - Flag potential security concerns
                   - Consider regulatory implications

               Please provide a comprehensive analysis of the Ethereum blockchain data based on these ethereum information.
               Focus on significant patterns, anomalies, and insights that would be valuable for understanding the blockchain activity.
               Use technical blockchain terminology and provide specific examples from the data to support your analysis.

               Note: This analysis is based on simulated data for demonstration purposes.
           `;
       }
   ```
   ````
5. **Posting Queries to D.A.T.A Backend**: Once the model generates the queries, they are posted to the **D.A.T.A Framework backend** for execution, just like in the first approach. The backend handles querying the blockchain data, processes the data, and returns the results in a structured format.
6. **Response Handling**: The response is then provided to the AI agent, and depending on the implementation, it can trigger further actions or display results to the user.

**Example of a Custom AI Agent Prompt and Query Handling in Eliza:**

````javascript
import { onchainDataPlugin } from "@elizaos/plugin-d.a.t.a";

const provider = databaseProvider(runtime);
const schema = provider.getDatabaseSchema();
const examples = provider.getQueryExamples();
const template = provider.getQueryTemplate();

if (!state) {
    state = (await runtime.composeState(message)) as State;
} else {
    state = await runtime.updateRecentMessageState(state);
}

const buildContext = template
    .replace("{{databaseSchema}}", schema)
    .replace("{{queryExamples}}", examples)
    .replace("{{userQuery}}", message.content.text || "");

const context = JSON.stringify({
    user: runtime.agentId,
    content: buildContext,
    action: "fetch_transactions",
});

const preResponse = await generateMessageResponse({
    runtime: runtime,
    context: context,
    modelClass: ModelClass.LARGE,
});

const userMessage = {
    agentId: runtime.agentId,
    roomId: message.roomId,
    userId: message.userId,
    content: message.content,
};

// Save response to memory
const preResponseMessage: Memory = {
    id: stringToUuid(message.id + "-" + runtime.agentId),
    ...userMessage,
    userId: runtime.agentId,
    content: preResponse,
    embedding: getEmbeddingZeroVector(),
    createdAt: Date.now(),
};

await runtime.messageManager.createMemory(preResponseMessage);
await runtime.updateRecentMessageState(state);

// Check for SQL query in the response using class method
const sqlQuery = provider.extractSQLQuery(preResponse);
if (sqlQuery) {
    const analysisInstruction = provider.getAnalysisInstruction();
    try {
        // Call query method on provider
        const queryResult = await provider.query(sqlQuery);

        // Return combined context with query results and analysis instructions
        return `
        # query by user
        ${preResponse.text}

        # query result
        ${JSON.stringify(queryResult, null, 2)}

        # Analysis Instructions
        ${analysisInstruction}
        `;
    } catch (error) {
        elizaLogger.error("Error executing query:", error);
        return context;
    }
} else {
    elizaLogger.log("no SQL query found");
}
return context;
```
````

***

#### **Response Format Handling**

Whether you are using the **D.A.T.A Framework backend** or your own custom AI model to generate queries, the response format is consistent. Here’s what you can expect:

* **SQL Queries**: Executed against the blockchain data sources and returned as JSON with placeholders for results.
* **Key-Value Data**: Specific data points such as balances, transaction counts, or token holdings.
* **Vector Data**: For more advanced use cases, such as AI-powered analysis or machine learning tasks.

The framework is designed to ensure that responses are easy to handle and can be integrated seamlessly into the AI agent's decision-making process.

***

#### **Summary of Approaches**

1. **Using the D.A.T.A Framework Backend**:
   * Automatically generate and execute SQL, key-value, or vector queries based on user input.
   * AI agents can autonomously fetch on-chain data and trigger actions based on that data.
2. **Using Custom AI Models for Query Generation**:
   * Leverage AI models to generate custom queries based on specific prompts.
   * AI agents use these custom queries to interact with the **D.A.T.A Framework backend** for data retrieval, enabling more flexibility and adaptability in querying blockchain data.

Both approaches enable AI agents to query on-chain data effectively, making them more intelligent and autonomous in blockchain-driven decision-making.
