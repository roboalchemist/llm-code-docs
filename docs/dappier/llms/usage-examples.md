# Usage Examples

## Example 1: Stock Market Analysis

**Use Case:** Get real-time market summary for Tesla (TSLA) inside a Ravenala agent.

### User Prompt:

```
What is the current price and market performance of TSLA?
```

### Ravenala Agent Behavior:

1. Detects the presence of a stock ticker
2. Routes the request to the `DAPPIER_STOCK_MARKET_DATA` tool
3. Calls the tool via the installed Dappier App
4. Returns a real-time response

### Expected Response:

```
TSLA is currently trading at $289.45, up 2.5% today. Latest news includes upcoming earnings expected this Thursday.
```

## Example 2: General News Search

**Use Case:** Create a news aggregator that fetches the latest headlines on any topic.

### User Prompt:

```
Give me the latest headlines about the stock market
```

### Expected Response:

```
Here are today's top stock market headlines:

1. S&P 500 reaches new all-time high, up 0.8% in morning trading
2. Federal Reserve signals potential rate cut in upcoming meeting
3. Tech stocks lead market rally with NVIDIA up 3.2%
4. Retail sector shows mixed results as consumer spending data released
5. European markets also trending upward following positive US economic data
```

## Example 3: Sports News Aggregator

**Use Case:** Build a sports news assistant that provides the latest updates on specific sports.

### User Prompt:

```
Summarize latest football news
```

### Expected Response:

```
Here are the latest football headlines:

1. NFL: Kansas City Chiefs sign defensive tackle to 3-year extension worth $45 million
2. Premier League: Manchester United announces new head coach starting next season
3. College Football: Top quarterback prospect commits to Ohio State for 2025
4. NFL Draft: Analysts predict record number of quarterbacks in first round
5. International: FIFA announces expanded Club World Cup format for 2025
```

## Example 4: Sustainability Content Curator

**Use Case:** Create a sustainability advisor that provides eco-friendly tips and news.

### User Prompt:

```
Show me new articles about sustainability
```

### Expected Response:

```
Here are the latest sustainability articles:

1. "10 Simple Ways to Reduce Your Carbon Footprint at Home"
2. "Major Companies Announce New Net-Zero Carbon Commitments"
3. "Innovative Recycling Technologies Transforming Plastic Waste"
4. "The Rise of Sustainable Fashion: Brands Leading the Change"
5. "How Regenerative Agriculture is Combating Climate Change"
```

***