# Source: https://docs.architect.co/algos-book/spreader/leg-configuration.md

# Leg Configuration

Spreads are defined by a weighted sum of the individual leg's prices, using `price_multiplier`, with an optional `price_offset`.&#x20;

$$
SpreadPrice =\sum\_{i=1}^n PriceMultiplier\_i \* (Price\_i + PriceOffset)
$$

The `quantity_ratio` actually determines the ratio of contracts quantities you are trading in each leg. Most of the time, the `quantity_ratio` should be equal to `price_multiplier`. However, there are some instances where you may want the `quantity_ratio` to differ, such as when there are contract point values at play. For example, imagine a [ES](https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html) - [MES](https://www.cmegroup.com/markets/equities/sp/micro-e-mini-sandp-500.contractSpecs.html) spread. While you may wish to price it as long 1 ES, short 1 MES (`price_multiplier` of 1 and -1, respectively), ES has a contract point value of $50, whereas MES has one of $5. This means that to actually achieve the correct *notional* exposure that matches your long 1 ES, short 1 MES spread price, you would need to use a `quantity_ratio` of 1 and -10. Any multiple of this ratio, such as 0.1 and -1 works the same.

For another example, take [Heating-Oil (HO)](https://www.cmegroup.com/markets/energy/refined-products/heating-oil.html) vs [Gasoil (G)](https://www.ice.com/products/34361119/low-sulphur-gasoil-futures):\
\- HO is priced in $ / per gallon, G is priced in $ / metric ton\
\- HO contract size is 42,000 gallons, G contract size is 100 metric tons

If we want to standardize the units of these two contracts and trade the resulting spread, we could set:\
\- 1 gallon of heating oil is around 0.00318 metric tons, so the `price_multiplier` would be `1 HO x -0.00318 G`\
\- 42,000 gallons of heating oil is around 133.56 metric tons, so a `quantity_ratio` of `3 HO x -4 G` would yield a similar tonnage (\~400 vs 400 metric tons)

{% hint style="info" %}
The sign of your `price_multiplier` for each leg **must match** that of your `quantity_ratio` , as the algo needs to take into account the buy/sell direction of your order to price using the corresponding bid/ask.
{% endhint %}

{% hint style="info" %}
Fractional units can be given, but quantities will be rounded down if they cannot be rounded to a whole lot.&#x20;
{% endhint %}

### LegParams

| Parameter                                           | Description                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| price\_multiplier *(decimal)*                       | The weight to assign to this leg for spread pricing                                                                                                                                                                                                                                                                                             |
| quantity\_ratio *(decimal)*                         | The quantity ratio of contracts to trade this leg with respect to a spread unit. Note that when a spread quote or take order hits the market, quantity\_ratio determines your legs' relative order sizing, not the price\_multiplier, as the latter is only used for the spread pricing                                                         |
| price\_offset *(decimal)*                           | The offset to apply to this leg *before* weighing it with price\_multiplier. This might be used if there is some bias, costs or other adjustment you wish to make to this leg's price before computing the overall spread price                                                                                                                 |
| chase\_ticks *(unsigned integer)*                   | The number of ticks more aggressive than the desired price for a taking order. Using chase\_ticks > 0 decreases your changes of "getting hung", or remaining unhedged relative to the spread, after another leg gets a fill. However, when chase\_ticks > 0, it is possible to get filled at a spread price that is worse than your limit price |
| quoting\_parameters *(QuotingParameters, optional)* | Specify optional quoting parameters (see below). If not specified or left as None, this leg will **not quote**                                                                                                                                                                                                                                  |
| symbol *(str)*                                      |                                                                                                                                                                                                                                                                                                                                                 |
| marketdata\_venue *(str)*                           |                                                                                                                                                                                                                                                                                                                                                 |
| execution\_venue *(str)*                            |                                                                                                                                                                                                                                                                                                                                                 |
| account *(str)*                                     |                                                                                                                                                                                                                                                                                                                                                 |

### QuotingParameters

Under the hood, Spreader utilizes the [QuoteOneSide](https://docs.architect.co/algos-book/quoteoneside) algo for smart quoting behavior, if the `quoting_parameters` field is specified.&#x20;

| Parameter                                  | Description                                                                                                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| max\_quote\_quantity *(decimal, optional)* | Maximum quantity to quote at a time for this leg. If left as None, the quantity quoted will be the minimum of the posted liquidity on the **other leg,** or the remaining quantity to satisfy the spreader order |

{% embed url="<https://docs.rs/architect-api/latest/architect_api/algo/spreader/struct.SpreaderParams.html>" %}
