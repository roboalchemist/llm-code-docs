# Source: https://docs.architect.co/algos-book/overview.md

# Overview

{% hint style="warning" %}
Generally, users should never manually cancel individual orders sent by an algo. If you want to cancel the individual order, the user is expected to stop the entire algo.
{% endhint %}

{% tabs %}
{% tab title="Python" %}

```python
# params defined according to which algo you want to use. 
# Then all that's left is to call:
order = await client.place_algo_order(params=params, account=account)

# you can monitor it later with:
status = await client.get_algo_order_status(order.id)

# or view historical algo orders
historical_orders = await client.get_historical_algo_orders(order.id)

# modify the order if necessary
new_order = await client.modify_algo_order(algo_order_id=order.id, params=params)

# or just stop it
stop_respose = await client.stop_algo_order(order.id)
```

{% endtab %}
{% endtabs %}
