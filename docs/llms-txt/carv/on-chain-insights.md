# Source: https://docs.carv.io/d.a.t.a.-ai-framework/examples/on-chain-insights.md

# On-Chain Insights

In this section, we showcase how the AI Agent processes a user query and returns a structured response based on the query.

#### **User Query:**

*Which address on Ethereum was the most active in the last 24 hours.*

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FwfGLOzecGlxz7eY538pq%2Fimage.png?alt=media&#x26;token=89d0ef6a-9e74-4412-ae1d-65bdf74f4a53" alt=""><figcaption><p>Ai Agent return result</p></figcaption></figure>

D.A.T.A framework generated query:

```json
{
 "sql": {
   "query": "WITH address_activity AS (\n    SELECT\n        from_address AS address,\n        COUNT(*) AS tx_count\n    FROM\n        eth.transactions\n    WHERE date_parse(date, '%Y-%m-%d') >= date_add('day', -1, current_date)\n    GROUP BY\n        from_address\n    UNION ALL\n    SELECT\n        to_address AS address,\n        COUNT(*) AS tx_count\n    FROM\n        eth.transactions\n    WHERE\n        date_parse(date, '%Y-%m-%d') >= date_add('day', -1, current_date)\n    GROUP BY\n        to_address\n)\nSELECT\n    address,\n    SUM(tx_count) AS total_transactions\nFROM\n    address_activity\nGROUP BY\n    address\nORDER BY\n    total_transactions DESC\nLIMIT 1;",
   "explanation": "This query identifies the most active Ethereum address in the last 24 hours by counting transactions where the address was either the sender (from_address) or the receiver (to_address). The results are aggregated and ordered by the total number of transactions, with the most active address returned.",
   "timeRange": "Last 24 hours"
 },
 "analysis": {
   "overview": {
     "totalTransactions": "Number of transactions involving the most active address",
     "timeSpan": "Last 24 hours",
     "keyMetrics": ["Total transactions involving the address", "Address activity rank"]
   },
   "patterns": {
     "transactionPatterns": ["High frequency of transactions", "Potential bot or automated activity"],
     "addressBehavior": ["Possible exchange or DeFi protocol address", "High volume of incoming/outgoing transactions"],
     "temporalTrends": ["Peak activity during specific hours", "Consistent transaction frequency"]
   },
   "statistics": {
     "averages": {
       "transactionsPerHour": "Average transactions per hour for the address"
     },
     "distributions": {
       "transactionTypes": ["Incoming vs outgoing transactions", "Smart contract interactions"]
     },
     "anomalies": ["Unusual spikes in transaction volume", "Sudden changes in activity patterns"]
   },
   "insights": [
     "The address may belong to a high-frequency trading bot or a centralized exchange.",
     "High transaction volume could indicate market-making activity or arbitrage opportunities."
   ],
   "recommendations": [
     "Monitor the address for continued high activity to identify potential market trends.",
     "Investigate the nature of transactions (e.g., DeFi interactions, NFT trades) for deeper insights."
   ]
 }
}
```

D.A.T.A framework query result

```sql
   %%%% D.A.T.A. Generated SQL query: 
   WITH address_activity AS (
      SELECT
          from_address AS address,
          COUNT(*) AS tx_count
      FROM
          eth.transactions
      WHERE date_parse(date, '%Y-%m-%d') >= date_add('day', -1, current_date)
      GROUP BY
          from_address
      UNION ALL
      SELECT
          to_address AS address,
          COUNT(*) AS tx_count
      FROM
          eth.transactions
      WHERE
          date_parse(date, '%Y-%m-%d') >= date_add('day', -1, current_date)
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
  LIMIT 1; 

 ◎ LOGS
   %%%% D.A.T.A. queryResult 
   {
      "success": true,
      "data": [
        {
          "address": "0xdac17f958d2ee523a2206206994597c13d831ec7",
          "total_transactions": "118841"
        }
      ],
      "metadata": {
        "total": 1,
        "queryTime": "2025-01-15T08:04:54.644Z",
        "queryType": "aggregate",
        "executionTime": 0,
        "cached": false
      }
    } 
```

**User Query:**

*What is the gas prive average on Ethereum last 3 days.*

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FfDEP27dUdGB03hTsorNE%2Fimg_v3_02ii_5ec13e0a-8f04-4dc8-87e8-b32ad80ad1hu.jpg?alt=media&#x26;token=174c0033-da78-4b97-a355-4db735a61df6" alt=""><figcaption><p>Example response when Ai Agent integrate with D.A.T.A.</p></figcaption></figure>

#### **User Query:**

*Which stablecoin had the highest trading volume on Ethereum in the last 24 hours.*

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FKWXYhyDkeQeczna1fNt0%2Fimage.png?alt=media&#x26;token=eabe2cdd-cae8-436e-8423-6b2bf1c7a384" alt=""><figcaption><p>Example response when Ai Agent integrate with D.A.T.A.</p></figcaption></figure>
