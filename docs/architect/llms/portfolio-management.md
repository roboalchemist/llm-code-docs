# Source: https://docs.architect.co/sdk-reference/portfolio-management.md

# Source: https://docs.architect.co/concepts/portfolio-management.md

# Accounts and portfolio management

In the Architect PMS, portfolios are represented as accounts, which contain balances and positions. Accounts are mapped one-to-one with their correspondent on each venue, exchange, or clearing entity. All Architect-managed accounts are uniquely identified by UUID. The following are some examples of different kinds of accounts:

| Account                                 | Example accout name                           | Description                                                               |
| --------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------- |
| US futures and options clearing account | STONEX:ABC123/JohnDoe                         |                                                                           |
| US equities clearing account            | DORMAN:44444R/BLast                           |                                                                           |
| Coinbase portfolio                      | COINBASE:a2868946-2b80-4b9e-a672-cdda4bb200dc | For prop trading, the portfolio ID of a connected Coinbase crypto account |

### Balances and positions

Account balances describe the amount of cash or assets held; for example, an account may hold 5 BTC or 20 shares of AAPL, and have a margin balance of 1000 USD.&#x20;

Positions represent ownership or exposure to financial instruments in an account; for example, an account may be net short 10 shares of TSLA or net long 3 CME GC contracts. By default, positions are unaggregated and separate orders in the same instrument will result in distinct positions.
