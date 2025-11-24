# Source: https://docs.datafold.com/integrations/bi-data-apps/dbt.md

# dbt Exposures

> Incorporate dbt Exposures into your Datafold lineage.

In dbt, Exposures allow you to define downstream uses of your data (e.g., in dashboards). You can include dbt Exposures in lineage within Data Explorer using our dbt Exposures integration.

## Set up the integration

<Note>
  If you haven't aleady created a dbt CI integration, please start [there](/integrations/orchestrators/).
</Note>

1. Visit Settings > BI & Data Apps > Add new integration
2. Select "dbt Exposures"
3. Enter a name for the integration (this can be anything)
4. Select your existing dbt CI integration from the dropdown
5. Save the integration

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=46667baf3b545a6f0665c15874359703" alt="Add dbt Exposures integration" data-og-width="2176" width="2176" data-og-height="766" height="766" data-path="images/dbt-exposures-add-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ae8ea705a4713091682b412adb5b5f13 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=58b3982ad41999bed202c0719b217e51 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=fb0fbf4dedd43ae2400d43b0b22e3e15 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5cd052a02b04d0f2caf8fd0abc2a1e4a 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=6723bcf6bad8c9b6ce2e137d91341c80 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-add-integration.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=52cf2abad78cf3b0b7cf87b0d6bf2ea6 2500w" />
<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=ebeb4396e6ef3fa3eda620f1783950fa" alt="Configure dbt Exposures integration" data-og-width="1378" width="1378" data-og-height="318" height="318" data-path="images/dbt-exposures-integration-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c85f719dfda4413e898551a6758e6bd4 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=daae5797a2c526c102e4c4518af37317 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=97f74960a66aae3376cefbdba316435b 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=27d566789c4c9c7be1bd6bad4dec745e 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=011bcf46f08639a3065fd87da95a752a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-integration-config.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=65f9196b17a53707b96c6e10dc5615e9 2500w" />

## View dbt Exposures in Data Explorer

<Note>
  Your dbt Exposures may not appear in lineage immediately after setting up the integration. To force an update, return to the integration settings and select "Sync now".
</Note>

When you visit Data Explorer, you'll now see the option to filter for dbt Exposures:

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=2269a6543d2ef3112cd727d79e717bb2" alt="Filter for dbt Exposures" data-og-width="3420" width="3420" data-og-height="1436" height="1436" data-path="images/dbt-exposures-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f2e5dae9572c375abdd47d185998c94b 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=8ec7cf3f0bc7b5a5b6eec594e1478ed4 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1e5b7e8106c84f5475a1e6374b8f703a 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=58803f774dfde2d2be4089f71f4742e6 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=19b1754db1f11145fa86a2d38fa4abcd 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-filters.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=824b540aefcc17bcacd7c2b896734f8d 2500w" />

Your dbt Exposures will also appear in lineage:

<img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f0f28de9f5aa1e521d94184efe3d9342" alt="View dbt Exposures in lineage" data-og-width="3420" width="3420" data-og-height="1962" height="1962" data-path="images/dbt-exposures-lineage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=901ebd14c0f0c372f49d08043c0c1af9 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=16b748b2821b30abea415022e45c3bec 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=44ba5a4d17759b61c1b63851e5b1729e 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=4d8bde289da0695e6d6540d4ea6418df 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1773f4a8d1730e2f90e0415ed8b7b7f8 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/dbt-exposures-lineage.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=c98d0fc7fdea2fed0b983154e8a482e3 2500w" />
