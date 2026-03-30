# Source: https://docs.architect.co/user-guide/futures-101/expiration-settlement-and-roll.md

# Expiration, Settlement, and Roll

At a specified date, a futures contract will cease trading and expire, through a process called final settlement. The exact schedule and mechanism varies by product. Traders have three main choices if they hold a position in a future nearing settlement: close out positions, letting the futures expire, or roll forward to another contract.&#x20;

**Close out positions:** \
This is the simplest option, and appropriate if the trader no longer wants the position or exposure. This requires no special help from anyone like Architect or the Exchange. The trader would buy back any short positions or sell out any long positions, and end with a position of zero going into expiration. \
\
**Letting futures expire:**\
Holding a position in a future through expiration means to go to the final settlement process.&#x20;

* Physically Settled Futures:\
  For some contracts, final expiration requires a physical delivery between the short and long position holders. This is common in agriculture, interest rates, precious metals, and energy futures. **Architect currently does not support expiration of physically settled futures, and open positions approaching expiration may be liquidated without notice.** To avoid physical delivery, expiration here means the earlier of the Last Trade Date and First Notice Date.
* Financial/Cash Settled Futures:\
  For most contracts, delivery takes place financially, meaning as cash based on the final settlement value. Each future's final settlement procedure is published by the exchange, and after this value is known, the futures position is removed from the account and a final profit/loss is booked.&#x20;

**Roll forward to another contract:**\
Rolling forward means to close out the position in the expiring future, and open a new futures position in a later-expiring contract. This is used if the trader wants to maintain the exposure past the original expiration date, and is commonly done a few days before futures expiration.&#x20;
