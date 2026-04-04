# Source: https://docs.architect.co/algos-book/spreader.md

# Spreader

Configure the spreader to trade a designated **spread** between multiple products. You define the parameters for each leg of the spread, and some general spread settings to match your desired execution preferences.&#x20;

The spreader can be used for a variety of different strategies, including cross-exchange arbitrage, futures vs spot basis trading, and relative value trading. Common examples of spreads are ES-SPY, HO-G, BTC Fut - BTC Perp, BTC Perp - BTC Spot.&#x20;

{% hint style="info" %}
Currently, the spreader supports two-leg spread configurations. Support for n-leg spreads is planned for a future release.
{% endhint %}

The spreader works through 2 execution styles:

1. **Spread Taking**
   1. No orders out until the spread hits the desired level
   2. The algo will then send orders out relative to the **far side** (the crossing side) of the BBO
2. **Quote then Hedge**
   1. Each product can quote relative to the **near side** of the BBO. If it gets filled, all other legs will fire a taking order at the far side of their order books. Therefore, the price of each quote is based on the required price to get the desired spread value assuming that all the other legs are takes

<figure><img src="https://1135553376-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FeAUlgqmwkYTmKcyTbHKL%2Fuploads%2FMmwukQTEt0LwQDCd4ms1%2Fimage.png?alt=media&#x26;token=63fb24b8-0bc9-4d76-b478-37cefa5255ea" alt=""><figcaption><p>Figure 1: Execution for a spread that trades with <a href="spreader/leg-configuration">price multipliers</a> of 1 and -1 respectively. Note that the same execution holds true for market 2 (in particular, the labelling of market 1 and 2 is completely arbitrary)</p></figcaption></figure>

A spread will have **legs** with **quoting** parameters that you [configure](https://docs.architect.co/algos-book/spreader/leg-configuration). **Taking** parameters apply at the [spread level](https://docs.architect.co/algos-book/spreader/spread-level-configuration). The **taking** **params** will be relative to the far side of the bbo. The **quoting params** will be relative to the near sid&#x65;**.**

{% hint style="info" %}
Every leg will have *at most* one taking order, one quoting order, and one quote hedge out at once.
{% endhint %}

### Setting the Limit Price

The [`limit_price` ](https://docs.architect.co/algos-book/spreader/spread-level-configuration)is similar to the price of a limit order in the synthetic spread orderbook. It is the most aggressive (i.e. worse price you are willing to accept) level you are looking for the algo to trade the spread. This parameter will determine how the algo quotes and takes in each leg.

For example, in *Figure 1* if the `limit_price` is -0.06 we will quote in market 2, assuming we can hedge aggressively into the bid in market 1. However, we will not quote in market 1, because if we do get filled, we cannot hedge immediately at the best bid of 100.5 in market 2 without violating our `limit_price` of -0.06 (assuming we get the fill, it would come to a spread price of -0.05). We will also not submit any simultaneous **spread taking** orders, as these will grab us fills with an aggregate spread price at -0.04.

In real markets, While the spreader's quotes and spread takes in each leg are priced with prospective fills in other legs in mind, these orders might not get filled if the market moves away from you in market B right after a fill in market A, leaving you "hung".

[`chase_ticks`](https://docs.architect.co/algos-book/spreader/leg-configuration) is designed to reduce the probability of getting "hung" on one leg as the other moves away from you, by designating a certain amount of ticks you are willing to pay up by on that leg. While this greatly alleviates the fill probability issue and is generally recommended for securing hedges, it introduces **slippage**. Slippage, particularly in the leg that is hedging or taking, is the difference between the expected execution price and the price of the fill. With slippage it is possible for the spreader algo to get prices worse than the designated `limit_price`. Therefore, the `chase_ticks` parameter should be configured cleverly by the user to strike a balance between higher hedge fill probability and lower slippage.

{% embed url="<https://docs.rs/architect-api/latest/architect_api/algo/spreader/struct.SpreaderParams.html>" %}
