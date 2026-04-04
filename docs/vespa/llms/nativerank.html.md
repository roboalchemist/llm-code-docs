# Source: https://docs.vespa.ai/en/ranking/nativerank.html.md

# Source: https://docs.vespa.ai/en/reference/ranking/nativerank.html.md

# nativeRank Reference

 

The _nativeRank_ feature produces a reasonable text ranking score which is computed at an acceptable performance, and is a good candidate for [first phase](../../ranking/phased-ranking.html) ranking. The _nativeRank_ feature is a linear combination of the normalized scores computed by the features _nativeFieldMatch_, _nativeProximity_, and _nativeAttributeMatch_. All these features are described in detail below. See the [configuration properties](#configuration-properties) section for how to configure the features.

## nativeFieldMatch

The _nativeFieldMatch_ feature captures how well query terms match searched index fields by looking at the number of times a term occurs in a field and how early in the field it occurs. The significance and weight of the terms are also taken into account such that unusual terms give a higher rank contribution than common ones.

The score for _nativeFieldMatch_ is calculated as follows:

nativeFieldMatch=&Sum;intermSignificancei×termWeighti&Sum;jmfieldWeightjfirstOccImpj×firstOccBoostij+1-firstOccImpj×numOccBoostij&Sum;intermSignificancei×termWeighti&Sum;jmfieldWeightj×fmMaxTablej\[nativeFieldMatch = \frac{\sum\_i^ntermSignificance\_i \times termWeight\_i\sum\_j^mfieldWeight\_j(firstOccImp\_j \times firstOccBoost\_{ij} + (1 - firstOccImp\_j) \times numOccBoost\_{ij})}{\sum\_i^ntermSignificance\_i \times termWeight\_i\sum\_j^mfieldWeight\_j \times fmMaxTable\_j} \]

where _n_ is the number of query terms searched in index fields, _m_ is the number of fields searched by query term _i_, _firstOccImpj_ is the _firstOccurrenceImportance_ for field _j_, and _firstOccBoostij_, _numOccBoostij_ and _fmMaxTablej_ are given below.

firstOccBoostij=firstOccurrenceTablejfirstOccij×tableSizejmax6fieldLengthj\[firstOccBoost\_{ij} = firstOccurrenceTable\_j[\frac{firstOcc\_{ij} \times tableSize\_j}{max(6,fieldLength\_j)}] \]

where _firstOccurrenceTablej_ is the boost table configured for field _j_, typically an expdecay function (see the [boost tables](#boost-tables) section below), _firstOccij_ is the first occurrence of query term _i_ in field _j_, and _tableSizej_ is the size of the boost table.

numOccBoostij=occurrenceCountTablejnumOccsij×tableSizejmax6fieldLengthj\[numOccBoost\_{ij} = occurrenceCountTable\_j[\frac{numOccs\_{ij} \times tableSize\_j}{max(6,fieldLength\_j)}] \]

where _occurrenceCountTablej_ is the boost table configured for field _j_, typically a loggrowth function (see the [boost tables](#boost-tables) section below), _numOccsij_ is the number of occurrences of query term _i_ in field _j_, and _tableSizej_ is the size of the boost table.

fmMaxTablej=firstOccImpj×maxfirstOccurrenceTablej+1-firstOccImpj×maxoccurrenceCountTablej\[fmMaxTable\_j = firstOccImp\_j \times max(firstOccurrenceTable\_j) + (1 - firstOccImp\_j) \times max(occurrenceCountTable\_j) \]

where _max(boostTablej)_ is the max value in that table. _fmMaxTablej_ is 1 if table normalization is turned off (see the property _nativeRank.useTableNormalization_ in the [configuration properties](#configuration-properties) section).

The default behavior for _nativeFieldMatch_ is to consider all query terms searching in all index fields when calculating the score. The calculation can be limited to a specified set of index fields as follows:

`nativeFieldMatch(f1, f2)`

In this case only query terms searching in index fields _f1_ and _f2_ are considered.

## nativeProximity

The _nativeProximity_ feature captures how near the matched query terms occur in searched index fields by looking at the word distance between query terms in query term pairs. Two query terms that are close to each other should give a higher score than two terms that are far from each other.

The score for _nativeProximity_ is calculated as follows:

nativeProximity=&Sum;jmfieldWeightj&Sum;abtermPairWeightabproxImpj×proxTablejdistab-1+1-proxImpj×revProxTablejdistba-1&Sum;jmfieldWeightj&Sum;abtermPairWeightab×pMaxTablej\[nativeProximity = \frac{\sum\_j^mfieldWeight\_j\sum\_{ab}termPairWeight\_{ab}(proxImp\_j \times proxTable\_j[dist\_{ab} - 1] + (1 - proxImp\_j) \times revProxTable\_j[dist\_{ba} - 1])}{\sum\_j^mfieldWeight\_j\sum\_{ab}termPairWeight\_{ab} \times pMaxTable\_j} \]

where _m_ is the number of index fields, _ab_ is a term pair searched for in field _j_, _proxImpj_ is the _proximityImportance_ for field _j_, _proxTablej_ is the forward proximity boost table for field _j_, _distab_ is the minimum distance between occurrences of query terms _a_ and _b_ in field _j_, (_a_ occurs before _b_), _revProxTablej_ is the reverse proximity boost table for field _j_, _distba_ is the minimum distance between occurrences of query terms _b_ and _a_ in field _j_ (_b_ occurs before _a_), and _termPairWeightab_ and _pMaxTablej_ are given below.

For each field _j_ we consider all query terms searched in this field and generate a set of term pairs. The _slidingWindowSize_ parameter determines how many pairs that are generated. With a sliding window of size 3 over the terms _a b c d_, we first consider the terms _a b c_, then the terms _b c d_, and finally the terms _c d_. The following pairs are generated: _ab_, _ac_, _bc_, _bd_, and _cd_.

termPairWeightab=connectednessab×termSignificancea×termWeighta+termSignificanceb×termWeightb\[termPairWeight\_{ab} = connectedness\_{ab} \times (termSignificance\_a \times termWeight\_a + termSignificance\_b \times termWeight\_b) \]

connectednessac=minconnectednessabconnectednessbcdistac\[connectedness\_{ac} = \frac{min(connectedness\_{ab}, connectedness\_{bc})}{dist\_{ac}} \]

where _distac_ is the distance between term _a_ and _c_ in the query.

pMaxTablej=proxImpj×maxproxTablej+1-proxImpj×maxrevProxTablej\[pMaxTable\_j = proxImp\_j \times max(proxTable\_j) + (1 - proxImp\_j) \times max(revProxTable\_j) \]

where _max(boostTablej)_ is the max value in that table. _pMaxTablej_ is 1 if table normalization is turned off (see the property _nativeRank.useTableNormalization_ in the [configuration properties](#configuration-properties) section).

The default behavior for _nativeProximity_ is to consider all index fields and all query terms pairs searching in these fields when calculating the score. The calculation can be limited to a specified set of index fields as follows:

`nativeProximity(f1, f2)`

In this case only query term pairs searching in index fields _f1_ and _f2_ are considered.

For multi-value fields, setting [element-gap](../schemas/schemas.html#rank-element-gap) for the field in the rank profile enables distance calculation between adjacent elements.

## nativeAttributeMatch

The _nativeAttributeMatch_ feature captures how well query terms match searched attribute fields, and is calculated as follows:

nativeAttributeMatch=&Sum;intermWeighti×attributeWeightj×signwij×weightTablejabswij&Sum;intermWeighti×attributeWeightj×maxweightTablej\[nativeAttributeMatch = \frac{\sum\_i^ntermWeight\_i \times attributeWeight\_j \times sign(w\_{ij}) \times weightTable\_j[abs(w\_{ij})]}{\sum\_i^ntermWeight\_i \times attributeWeight\_j \times max(weightTable\_j)} \]

where _n_ is the number of query terms searched in attribute fields, _weightTablej_ is the boost table for attribute _j_, _max(weightTablej)_ is the max value in that table (1 if table normalization is turned off), _sign(wij)_ is the sign of _wij_. _wij_ is dependent on the attribute type:

- **Weighted set**: equals the weight associated with the key (represented by query term _i_) in attribute _j_.
- **Array**: equals the number of occurrences of query term _i_ in attribute _j_.
- **Single**: equals 1.

The default behavior for _nativeAttributeMatch_ is to consider all query terms searching in all attribute fields when calculating the score. The calculation can be limited to a specified set of attribute fields as follows:

`nativeAttributeMatch(a1, a2)`

In this case only query terms searching in attribute fields _a1_ and _a2_ are considered.

## nativeRank

The _nativeRank_ feature is just a linear combination of the three other features, and is calculated as follows:

nativeRank=fmw×nativeFieldMatch+pw×nativeProximity+amw×nativeAttributeMatchfmw+pw+amw\[nativeRank = \frac{fmw \times nativeFieldMatch + pw \times nativeProximity + amw \times nativeAttributeMatch}{fmw + pw + amw} \]

where _fmw_ is the _fieldMatchWeight_, _pw_ is the _proximityWeight_, and _amw_ is the _attributeMatchWeight_.

The default behavior when calculating the native rank score is to consider all query terms searching in all defined index fields and attribute fields. In many cases though only a subset of these fields are of interest in the rank score calculation. You can set up _nativeRank_ for a subset of fields by specifying the field names in the parameter list as follows:

```
first-phase {
    expression: nativeRank(title,body,tags)
}
```

In this case we have two index fields (_title_ and _body_) and one attribute field (_tags_), and the _nativeRank_ feature is calculated based on the features _nativeFieldMatch(title,body)_, _nativeProximity(title,body)_, and _nativeAttributeMatch(tags)_. Note that the CPU cost of calculating the native rank score is also reduced when specifying a subset of the fields.

## Variables

This is a list of the common variables used in the formulas above:

| Variable | Description |
| --- | --- |
| _attributeWeightj_ | The weight of attribute field _j_. See the [schema reference](../schemas/schemas.html#weight) for how to set this weight. The default value is 100. |
| _connectednessab_ | The connectedness between query terms _a_ and _b_. |
| _fieldLengthj_ | The length of field _j_ in number of words. |
| _fieldWeightj_ | The weight of index field _j_. See the [schema reference](../schemas/schemas.html#weight) for how to set this weight. The default value is 100. |
| _termSignificancei_ | The significance of query term _i_. |
| _termWeighti_ | The weight of query term _i_. |

## Configuration properties

This is a comprehensive list of all the configuration properties to all native rank features:

| Feature | Parameter | Default | Description |
| --- | --- | --- | --- |
| `nativeFieldMatch` | `averageFieldLength` | The actual length of the field in the given document. | When set this replaces the true field length in the nativeFieldMatch formula for all documents. |
|
| |
| `nativeFieldMatch` | `firstOccurrenceTable` | expdecay(8000,12.50) | The default table used when calculating boost for the first occurrence in a field. |
| `nativeFieldMatch` | `firstOccurrenceTable.fieldName` | The value of `firstOccurrenceTable` | The table used when calculating boost for the first occurrence in the given field. |
| `nativeFieldMatch` | `occurrenceCountTable` | loggrowth(1500,4000,19) | The default table used when calculating boost for the number of occurrences in a field. |
| `nativeFieldMatch` | `occurrenceCountTable.fieldName` | The value of `occurrenceCountTable` | The table used when calculating boost for the number of occurrences in the given field. |
| `nativeFieldMatch` | `firstOccurrenceImportance` | 0.5 | The default importance value used for weighting the boosts for first occurrence and number of occurrences in a field. This value should be in the interval [0, 1]. |
| `nativeFieldMatch` | `firstOccurrenceImportance.fieldName` | The value of `firstOccurrenceImportance` | The importance value used for the given field. |
| `nativeProximity` | `proximityTable` | expdecay(500,3) | The default table used when calculating forward proximity boost in a field. |
| `nativeProximity` | `proximityTable.fieldName` | The value of `proximityTable` | The table used when calculating forward proximity boost in the given field. |
| `nativeProximity` | `reverseProximityTable` | expdecay(400,3) | The default table used when calculating reverse proximity boost in a field. |
| `nativeProximity` | `reverseProximityTable.fieldName` | The value of `reverseProximityTable` | The table used when calculating reverse proximity boost in the given field. |
| `nativeProximity` | `proximityImportance` | 0.5 | The default importance value used for weighting the boosts for forward and reverse proximity in a field. This value should be in the interval [0, 1]. |
| `nativeProximity` | `proximityImportance.fieldName` | The value of `proximityImportance` | The importance value used for the given field. |
| `nativeProximity` | `slidingWindowSize` | 4 | The size of the sliding window used when generating term pairs. |
| 
 **Deprecated:** The elementGap rank property is deprecated and will be removed in Vespa 9.
 |
| `nativeProximity` | 

`elementGap.fieldName`

 | infinity | 

The gap between positions in adjacent elements in multi-value fields. Use the [element-gap](../schemas/schemas.html#rank-element-gap) rank setting instead.

 |
| `nativeAttributeMatch` | `weightTable` | linear(1,0) | The default table used when calculating boost for matching in an attribute field. |
| `nativeAttributeMatch` | `weightTable.attributeName` | The value of `weightTable` | The table used when calculating boost for matching in the given attribute. |
| `nativeRank` | `fieldMatchWeight` | 100.0 | How much to weight the score from _nativeFieldMatch_. |
| `nativeRank` | `proximityWeight` | 25.0 | How much to weight the score from _nativeProximity_. If table normalization is turned off the default value is 100.0. |
| `nativeRank` | `attributeMatchWeight` | 100.0 | How much to weight the score from _nativeAttributeMatch_. |
| `nativeRank` | `useTableNormalization` | true | Whether we should use table normalization for the native rank features. Set this property to _false_ to turn off table normalization |

For example, to override the _occurrenceCountTable_ and _reverseProximityTable_ for the index field _content_, add the following to the rank profile in the sd file:

```
rank-properties {
    nativeFieldMatch.occurrenceCountTable.content: "linear(0,0)"
    nativeProximity.reverseProximityTable.content: "linear(0,0)"
}
```

See the [search definitions](../schemas/schemas.html#rank-properties) reference for more information on rank-properties.

### Boost tables

The following boost tables are supported by the native rank features:

| Name | Function | Description |
| --- | --- | --- |
| expdecay(w,t) | `w * exp(-x/t)` | Represents an exponential decay function where _w_ is the weight controlling the amplitude and _t_ is the tune parameter controlling the slope. |
| loggrowth(w,t,s) | `w * log(1 + (x/s)) + t` | Represents a logarithmic growth function where _w_ is the weight controlling the amplitude, _t_ is the tune parameter controlling the offset, and _s_ is a scale parameter controlling the sensitivity to the variable _x_ |
| linear(w,t) | `w * x + t` | Represents a linear function where _w_ controls the slope and _t_ controls the offset. |

The parameters _w_, _t_, and _s_ are floating point numbers, the same as the content of the tables. The default table size is 256 with x in the interval [0,255]. You can override this default size by specifying an optional last parameter to the table name. For instance, if you use _linear(1.5,0,512)_ you get a table with size 512 populated with the result of evaluating the function _1.5\*x + 0_ for all x in the interval [0,511].

### Rank types

Four predefined rank types are supported by _nativeRank_: _about_ (default), _identity_, _tags_, and _empty_. Each type is associated with a set of boost tables that are used by the native rank features. See the [rank type](rank-types.html) document for detailed information on these type.

When setting up the sd file, either use one of the predefined rank types for a field, or explicitly specify the boost tables to use for that field as a set of rank-properties. If you don't specify anything you get the boost tables associated with the _about_ type. The _about_ boost tables for _nativeFieldMatch_ and _nativeProximity_ are already optimized for textual match, while the boost table for _nativeAttributeMatch_ is data dependent and must be optimized for each use case.

## nativeRank limitations

The nativeRank feature is a pure text match scoring feature. In particular, it does not take the following concepts into account for documents that match a query:

- Static rank or any other relevancy contribution that is based on a numeric value. Use the _attribute_ feature in a ranking expression to get this concept into the final relevancy score. 
- Geographical location of a match correlated to a location associated with the query. Use the _distance_ or _closeness_ feature in a ranking expression to take this into account. 
- The age of the matching documents. Use the _freshness_ feature in a ranking expression to take this into account. 

 Copyright © 2026 - [Cookie Preferences](#)

### On this page:

- [nativeFieldMatch](#nativeFieldMatch)
- [nativeProximity](#nativeProximity)
- [nativeAttributeMatch](#nativeAttributeMatch)
- [nativeRank](#nativeRank)
- [Variables](#variables)
- [Configuration properties](#configuration-properties)
- [Boost tables](#boost-tables)
- [Rank types](#rank-types)
- [nativeRank limitations](#nativeRank-limitations)

