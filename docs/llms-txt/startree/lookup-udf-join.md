# Source: https://docs.startree.ai/corecapabilities/query_data/functions/lookup-udf-join.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lookup UDF Join

<Info>
  The Lookup UDF Join is only supported with the single-stage query engine (v1). For more information about using JOINs with the multi-stage query engine, see JOINs.
</Info>

Lookup UDF is used to get dimension data via primary key from a dimension table allowing a decoration join functionality. Lookup UDF can only be used with a dimension table in Pinot.

## Syntax

The UDF function syntax is listed as below:

```json  theme={null}
lookupUDFSpec:
    LOOKUP
    '('
    '''dimTable'''
    '''dimColToLookup'''
    [ '''dimJoinKey''', factJoinKey ]*
    ')'
```

* `dimTable` Name of the dim table to perform the lookup on.
* `dimColToLookUp` The column name of the dim table to be retrieved to decorate our result.
* `dimJoinKey` The column name on which we want to perform the lookup i.e. the join column name for dim table.
* `factJoinKey` The column name on which we want to perform the lookup against e.g. the join column name for fact table

<Note>
  - all the dim-table-related expressions are expressed as literal strings, this is the LOOKUP UDF syntax limitation: we cannot express column identifier which doesn't exist in the query's main table, which is the f`actTable` table.
  - the syntax definition of `[ '''dimJoinKey''', factJoinKey ]*` indicates that if there are multiple dim partition columns, there should be multiple join key pair expressed.
</Note>

## Examples

### Single-partition-key-column Example

Consider the table `baseballStats`

| Column                | Type   |
| --------------------- | ------ |
| playerID              | STRING |
| yearID                | INT    |
| teamID                | STRING |
| league                | STRING |
| playerName            | STRING |
| playerStint           | INT    |
| numberOfGames         | INT    |
| numberOfGamesAsBatter | INT    |
| AtBatting             | INT    |
| runs                  | INT    |

And the dim table `dimBaseballTeams`

| Column      | Type   |
| :---------- | :----- |
| teamID      | STRING |
| teamName    | STRING |
| teamAddress | STRING |

Valid queries include the following:

### Dim-Fact LOOKUP example

```json  theme={null}
SELECT 
  playerName, 
  teamID, 
  LOOKUP('dimBaseballTeams', 'teamName', 'teamID', teamID) AS teamName, 
  LOOKUP('dimBaseballTeams', 'teamAddress', 'teamID', teamID) AS teamAddress
FROM baseballStats 
```

| playerName  | teamID | teamName                                                                   | teamAddress                          |
| :---------- | :----- | -------------------------------------------------------------------------- | ------------------------------------ |
| David Allan | BOS    | Boston Red Caps/Beaneaters (from 1876–1900) or Boston Red Sox (since 1953) | 4 Jersey Street, Boston, MA          |
| David Allan | CHA    | null                                                                       | null                                 |
| David Allan | SEA    | Seattle Mariners (since 1977) or Seattle Pilots (1969)                     | 1250 First Avenue South, Seattle, WA |
| David Allan | SEA    | Seattle Mariners (since 1977) or Seattle Pilots (1969)                     | 1250 First Avenue South, Seattle, WA |

### Self LOOKUP example

```json  theme={null}
SELECT 
  teamID, 
  teamName AS nameFromLocal,
  LOOKUP('dimBaseballTeams', 'teamName', 'teamID', teamID) AS nameFromLookup
FROM dimBaseballTeams 
```

| teamID | nameFromLocal                                               | nameFromLookup                                              |
| :----- | :---------------------------------------------------------- | :---------------------------------------------------------- |
| ANA    | Anaheim Angels                                              | Anaheim Angels                                              |
| ARI    | Arizona Diamondbacks                                        | Arizona Diamondbacks                                        |
| ATL    | Atlanta Braves                                              | Atlanta Braves                                              |
| BAL    | Baltimore Orioles (original- 1901–1902 current- since 1954) | Baltimore Orioles (original- 1901–1902 current- since 1954) |

### Complex-partition-key-columns Example

Consider a single dimension table with the following schema:

BILLING SCHEMA

| Column        | Type    |
| :------------ | :------ |
| customerId    | INT     |
| creditHistory | STRING  |
| firstName     | STRING  |
| lastName      | STRING  |
| isCarOwner    | BOOLEAN |
| city          | STRING  |
| maritalStatus | STRING  |
| buildingType  | STRING  |
| missedPayment | STRING  |
| billingMonth  | STRING  |

### Self LOOKUP example

```json  theme={null}
select 
  customerId,
  missedPayment, 
  LOOKUP('billing', 'city', 'customerId', customerId, 'creditHistory', creditHistory) AS lookedupCity 
from billing 
```

| customerId | missedPayment | lookedupCity  |
| :--------- | :------------ | :------------ |
| 341        | Paid          | Palo Alto     |
| 374        | Paid          | Mountain View |
| 398        | Paid          | Palo Alto     |
| 427        | Paid          | Cupertino     |
| 435        | Paid          | Cupertino     |

## Usage

* The data return type of the UDF will be that of the `dimColToLookUp` column type.
* When multiple primary key columns are used for the dimension table (e.g. composite primary key), ensure that the order of keys appearing in the lookup() UDF is the same as the order defined in the `primaryKeyColumns` from the dimension table schema.

Built with [Mintlify](https://mintlify.com).
