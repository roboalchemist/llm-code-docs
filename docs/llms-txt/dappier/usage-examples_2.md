# Usage Examples

## Example 1: Stock Market with Payment

**Use Case:** Fetch Tesla stock data (TSLA) with automated payment.

**User Prompt:**

```
Get me the latest TSLA stock price
```

**Workflow:**

1. Find Dappier in Skyfire marketplace
2. Generate authentication token
3. Decode token for verification
4. Connect to Dappier MCP
5. Estimate cost (\$0.007)
6. Create payment token
7. Decode payment token
8. Execute `STOCK_MARKET_DATA` query
9. Charge payment token

**Expected Response:**

```
TSLA is trading at $289.45, up 2.5% today. Earnings call expected Thursday.
(Payment of $0.007 processed via Skyfire)
```

***

## Example 2: AI News with Token Charging

**User Prompt:**

```
What are the latest news about AI?
```

**Expected Response:**

```
1. OpenAI announces new model capabilities
2. Google DeepMind releases robotics update
3. Anthropic secures $1B funding round
(Payment processed via Skyfire for Dappier query)
```

***

## Example 3: Sports News Aggregator

**User Prompt:**

```
Summarize today’s football news
```

**Expected Response:**

```
1. NFL: Chiefs extend defensive tackle for $45M
2. Premier League: Manchester United announces new coach
3. FIFA expands Club World Cup for 2025
(Payment processed via Skyfire)
```

***