# Source: https://docs.pinot.apache.org/release-0.12.1/operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/operating-pinot/separating-data-storage-by-age.md

# Source: https://docs.pinot.apache.org/operators/operating-pinot/separating-data-storage-by-age.md

# Separating data storage by age

In order to optimize for low latency, we often recommend using high performance SSDs as server nodes. But if such a use case has vast amount of data, and need the high performance only when querying few recent days of data, it might become desirable to keep only the recent time ranges on SSDs, and keep the less frequently queried ones on cheaper nodes such as HDDs.

By storing data separately at different storage tiers, one can keep large amounts of data in Pinot while having control over the cost of the cluster. Usually, the most recent data is recommended to put in storage tier with fast disk access to support real-time analytics queries of low latency and high throughput; and older data in cheaper and slower storage tiers for analytics where higher query latency can be accepted.

Note that separating data storage by age is not about to achieve the compute-storage decoupled architecture for Pinot.

{% content-ref url="separating-data-storage-by-age/moving-segments-across-tenants" %}
[moving-segments-across-tenants](https://docs.pinot.apache.org/operators/operating-pinot/separating-data-storage-by-age/moving-segments-across-tenants)
{% endcontent-ref %}

{% content-ref url="separating-data-storage-by-age/using-multiple-directories" %}
[using-multiple-directories](https://docs.pinot.apache.org/operators/operating-pinot/separating-data-storage-by-age/using-multiple-directories)
{% endcontent-ref %}
