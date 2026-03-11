# Source: https://docs.architect.co/algos-book/spreader/spread-level-configuration.md

# Spread Level Configuration

| Parameter                                   | Description                                                                                                                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dir *(OrderDir)*                            | Designate your order as buy or sell with the binary enums `OrderDir.BUY` or `OrderDir.SELL`                                                                                               |
| quantity *(decimal)*                        | The quantity to execute. The algorithm terminates when each leg `i` is filled to the nearest lot less than or equal to `quantity * quantity_ratio[i]`                                     |
| limit\_price *(decimal)*                    | The most aggressive price the spread will take or quote at defined as a spread price.                                                                                                     |
| leg1 *(LegParams)*                          | See [Leg Configuration](https://docs.architect.co/algos-book/spreader/leg-configuration)                                                                                                  |
| leg2 *(LegParams)*                          | See [Leg Configuration](https://docs.architect.co/algos-book/spreader/leg-configuration)                                                                                                  |
| taking\_parameters *(TakingParameters)*     | See [TakingParameters](#takingparameters)                                                                                                                                                 |
| missed\_hedge\_policy *(MissedTakePolicy)*  | Specify how you want to deal with missed hedges or takes on one leg. Either **MissedTakePolicy.Halt** to pause the autospreader, or **MissedTakePolicy.Continue** to  ignore and continue |
| missed\_hedge\_wait\_time *(HumanDuration)* | Specify a certain amount of time an unfilled hedge waits before your configured **MissedTakePolicy** triggers                                                                             |

### TakingParameters

| Parameter                                      | Description                                                                                                                                                                                                                                           |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| min\_quantity\_threshold *(decimal, optional)* | Minimum quantity needed on the spread quantity for the spread before firing. However, if the remaining spread quantity is below this threshold, the `min_quantity_threshold` will be ignored so that the spread can submit the remainder of its order |
| max\_fire\_quantity *(decimal, optional)*      | Maximum fire/take quantity at once                                                                                                                                                                                                                    |
| take\_lockout *(HumanDuration)*                | Specify a certain amount of time before another spread-taking order can fire again                                                                                                                                                                    |

{% tabs %}
{% tab title="Python" %}

```python
from architect_py import (
    SpreaderParams,
    LegParams,
    QuotingParameters,
    TakingParameters,
    MissedTakePolicy,
    OrderDir,
    HumanDuration,
)
 
symbol1 = 'NQ 20251219 CME Future' 
symbol2 = 'MNQ 20251219 CME Future'
tp1 = f"{symbol1}/USD"
tp2 = f"{symbol2}/USD"
account = "PAPER:example@email.com"
venue = "CME"
params = SpreaderParams.new(
    dir=OrderDir.BUY,
    quantity=100,
    limit_price=10,
    leg1=LegParams.new(
        symbol=tp1,
        marketdata_venue=venue,
        execution_venue=venue,
        quantity_ratio=1,
        price_multiplier=1,
        price_offset=0,
        chase_ticks=0,
        quoting_parameters=QuotingParameters.new(max_quote_quantity=2),
    ),
    leg2=LegParams.new(
        symbol=tp2,
        marketdata_venue=venue,
        execution_venue=venue,
        quantity_ratio=-10,
        price_multiplier=-1,
        price_offset=0,
        chase_ticks=0,
        quoting_parameters=QuotingParameters.new(max_quote_quantity=20),
    ),
    taking_parameters=TakingParameters.new(
        min_quantity_threshold=None,
        max_fire_quantity=None,
        take_lockout=None,
    ),
    missed_hedge_policy=MissedTakePolicy.Halt,
    missed_hedge_wait_time=HumanDuration('30s'),
)

order = await client.place_algo_order(params=params, account=account)
```

{% endtab %}
{% endtabs %}
