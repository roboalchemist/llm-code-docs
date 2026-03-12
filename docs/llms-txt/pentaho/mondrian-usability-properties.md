# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/configure-mondrian-engine/edit-the-mondrian-properties-file/mondrian-usability-properties.md

# Mondrian Usability Properties

You can set certain properties to improve usability. Pay particular attention to the following engine properties:

```
mondrian.result.limit=5000000
```

In the event that pushdown cannot occur, this is the largest cross join size that Mondrian should try to process. Anything that exceeds this will likely send the CPU for a toss and result in long server hangs. If this limit is hit, Analyzer will present the user a nice warning suggesting options to simplify the report.

```
mondrian.olap.case.sensitive=true
```

This is important for Equals filters because the UI will preserve the casing of filter values. If the user defines a filter on `John Doe`, then the filter should only apply to "John Doe" and not "john doe".

```
mondrian.olap.ignoreInvalidMembers=true
```

This is important for saved reports because the user may build a report with a filter on 10 sales rep and after the next ETL, one of them is gone. The report should continue to run and return just the 9 remaining sales reps.

```
mondrian.olap.ignoreInvalidMembersDuringQuery=true
```

See `mondrian.olap.ignoreInvalidMembers`

```
mondrian.olap.iterationLimit=5000000
```

Similar to **mondrian.result.limit** except for controlling limits on aggregate evaluation.

```
mondrian.olap.compareSiblingsByOrderKey=true
```

This is required for sorting members in a dimension A->Z or Z->A. This property fixes a bug in Mondrian but was added for backward compatibility.

```
mondrian.olap.NullDenominatorProducesNull=true
```

The best way to understand this property is via an example. Suppose you want to see quota attainment for your sales reps which is computed as `Booked Deals / Quota`. Some reps may not have quotas and so quota attainment is either infinity or null. By treating "divide by null" as infinity, Mondrian will return these sales reps in the report. Otherwise, if "divide by null" equates to null, then Mondrian will filter those reps out (due to the `NON EMPTY`).
