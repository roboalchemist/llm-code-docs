# Create a geo radius filter
query_filter = models.Filter(
    must=[\
        models.FieldCondition(\
            key="cafe.location",\
            geo_radius=models.GeoRadius(\
                center=models.GeoPoint(\
                    lon=location.longitude,\
                    lat=location.latitude,\
                ),\
                radius=location.radius_km * 1000,\
            ),\
        )\
    ]
)

```

Such a filter needs [a payload index](https://qdrant.tech/documentation/concepts/indexing/#payload-index) to work efficiently, and it was created on a collection
we used to create the snapshot. When you import it into your instance, the index will be already there.

## [Anchor](https://qdrant.tech/articles/food-discovery-demo/\#using-the-demo) Using the demo

The Food Discovery Demo [is available online](https://food-discovery.qdrant.tech/), but if you prefer to run it locally, you can do it with Docker. The
[README](https://github.com/qdrant/demo-food-discovery/blob/main/README.md) describes all the steps more in detail, but here is a quick start:

```bash
git clone git@github.com:qdrant/demo-food-discovery.git
cd demo-food-discovery