# Source: https://bryntum.com/products/gantt/docs-llm/guide/Gantt/basics/resource-costs.md

# Calculation of costs

Costs in a project are calculated on multiple levels starting from assignments and summing up to resources, tasks
(rolling up to their parents) and finally end up on the project.
Assignment cost is either calculated or provided manually depending on the assigned resource type, For _work_ and
_material_ resources it can be calculated based on a their rates or a fixed per use cost.
And for a _cost_-type resource assignment a cost value is provided manually.

## Configuring assignment costs

Configuring an assignment cost depends on the assigned resource type.
There are three resource types supported:

- _work_ resource (default type) - a resource that contributes effort to tasks (like a worker or an equipment).
- _cost_ resource - a resource that provides some total cost (like taxes, travel cost or lodging).
- _material_ resource - a resource that contributes a material expenditure (like cement or wood expenditure).

When you assign a _cost_-type resource you simply provide cost value right on the assignment record.
This can be done on the task editor "Resources" tab in the "Cost" column.

## Specifying work and material resource rates

_Work_ and _material_ resource costs can be collected using the resource rates.

For example a worker rate is `$20/hour` and he works for `8 hours` on a task. Then his cost on the task is `$160` (`$20 * 8`). Or cement expenditure on a task is `2 tons` and its price is `$155/ton` which results the material cost on the task is `$310` (`2 * $155`).

So resources of work or material type can have rates for collecting their costs. It can be configured in [the resource](#SchedulerPro/widget/ResourceEditor) and [the task editor](#Gantt/widget/TaskEditor) popups.

## Resource editor

The [resource editor](#SchedulerPro/widget/ResourceEditor) is a popup allowing to edit a resource data.
It's available in the resource grid when enabling `resourceEdit` feature:

```javascript
const resourceGrid = new ResourceGrid({
    features : {
        // enable resource editor dialog
        resourceEdit : true
    },
    ...
});
```

After enabling the feature please right click on a resource and pick **"Edit resource"** from the context menu.

<div class="external-example" data-file="SchedulerPro/view/ResourceGrid.js"></div>

When editing a _work_ or _material_ resource the editor has **"Costs"** tab where user can change the resource rates.

## Rate tables

_Work_ and _material_ resource rates are stored in rate tables which are basically collections of rates with dates
they should start acting from.
A resource might have multiple of such tables to have flexible rates for different cases.

For example some equipment is more in demand based on a season and have different rates respectively.
Then when making an assignment user can pick which rates should be used.

## Managing rates tables in the resource editor

In order to edit rates please proceed to the resource editor **"Costs"** tab and click **"New table"** button in the resource
editor **"Costs"** tab to add a new rate table.
Then editing of the rate table name can be done in the **"Name"** field and its rates can be edited in the grid below.
The **"Start date"** column should be used to enter the date a rate should start of and **"Standard rate"** column for the
actual rate.
Please use **"Per use cost"** column if the resource has a cost per use (can be used in addition to rate-based pay or
instead of it).

Checking the **"Use by default for the resource assignment"** makes the selected rate table default for the future
assignments of the resource.

Please use **"Rate table"** combo to pick a rate table for editing its data.

The button next to **"New table"** removes the selected rate table.

<div class="external-example" data-file="SchedulerPro/widget/ResourceEditor.js"></div>

## Picking rates in the task editor

In order to start cost calculations for an assignment it should have a rate table or a cost value specified.
This can be done on the task editor **"Resources"** tab. The grid on the tab has **"Rate table"** column editable for _work_
and _material_ resources where user can pick a rate table.
A _material_-resource should also have the material expenditure provided in the "Quantity" column.

And for _cost_-resources there is an editable **"Cost"** column where a cost value can be provided.

**Please note** user can also edit rates from the task editor if needed. The column editor has **"Edit rate table"**
trigger icon which opens [the rate table editor](#SchedulerPro/widget/ResourceRateTableEditor) widget.

## Managing costs on the data level

As mentioned above `cost` field exists on assignment, resource, task and project models. All of the fields are
calculated except for a _cost_-type resource assignment where it's meant to be provided manually.

### Cost values rolling up

Changing an assignment `cost` starts automatic triggering of the corresponding task and resource costs (which are
basically sums of all its assignment costs).
And then in turn the task cost is rolled up to their parent tasks ending up on the project model.

### Dealing with cost resources

_Cost_-type resources are designed to provide some total costs (like taxes, travel cost or lodging).
Here is an example of such resource usage with data API:

```javascript
// make two "cost"-type resources - airfare & lodging
const [airfare, lodging] = project.resourceStore.add([{
    type : 'cost',
    name : 'Airfare'
},
{
    type : 'cost',
    name : 'Lodging'
}]);

// Now we can assign the resource to tasks in order to add corresponding totals to the tasks costs

// add airfare of $250 and lodging of $1000 to task1
project.assignmentStore.add([
    { event : task1, resource : airfare, cost : 250 },
    { event : task1, resource : lodging, cost : 1000 }
]);

// add airfare of $600 to task2
project.assignmentStore.add(
    { event : task2, resource : airfare, cost : 600 }
);
```

Specified costs will add up to `task1` and `task2` costs:

```javascript
// task1 cost is $1250 (airfare $250 + lodging $1000)
console.log(task1.cost);
// task2 cost is $600 due to its airfare cost
console.log(task2.cost);
```

That also allows to see totals of airfare and lodging across all the project by just checking the resources `cost` values:

```javascript
// output airfare total to console
console.log(airfare.cost);
// output lodging total to console
console.log(lodging.cost);
```

That's basically all for _cost_-resources usage. And dealing with _work_ and _material_
resources cost is a bit more complex.

### Work and material resource rates

_Work_ and _material_-type resource costs are collected based on the resource effort and material expenditure
respectively multiplied by the resource effective rate.

### Rate tables

_Work_ and _material_ resource rates are stored in rate tables. A resource can have multiple rate tables to have different rates for different occasions.
Each table in turn can store multiple rates if they change in time.

### Configuring resource rates

_Work_ and _material_ resources have rate tables in their [rateTables](#Gantt/model/ResourceModel#field-rateTables)
field. The field value is a store of [ResourceRateTableModel](#SchedulerPro/model/ResourceRateTableModel) instances.
A record has [rates](#SchedulerPro/model/ResourceRateTableModel#field-rates) field that stores rates of the
corresponding table. The field value is a store of [ResourceRateModel](#SchedulerPro/model/ResourceRateModel)
instances.

To register a new rate table resource [addRateTable](#Gantt/model/ResourceModel#function-addRateTable) method can be
used:

```javascript
// Adding a new rate table to worker1 resource.
const rateTable1 = worker1.addRateTable({
    name  : '10% off rates',
    // The table will have a single rate of $10
    // starting from the current date
    rates : [{
        startDate    : new Date(),
        standardRate : 10
    }]
})[0];
```

In order to add a new rate in runtime one can use
[addRate](#SchedulerPro/model/ResourceRateTableModel#function-addRate) method:

```javascript
// add a rate to the table
rateTable1.addRate({
    startDate    : new Date(),
    standardRate : 10
});
```

or in a bit longer way using a rate table [rates](#SchedulerPro/model/ResourceRateTableModel#field-rates) field
directly:

```javascript
// add a rate to the table
rateTable1.rates.add({
    startDate    : new Date(),
    standardRate : 10
});
```

After adding a rate table it can be applied to an assignment record
[rateTable](#Gantt/model/AssignmentModel#field-rateTable) and then its rates will be used for collecting
the assignment cost:

```javascript
// use the "10% off rates" rate table for assignment1
assignment1.rateTable = rateTable1;

// and this assignment cost will be zero
assignment2.rateTable = null;
```

The Engine processes the provided values asynchronously so cost values are not collected
right after the above lines. The code should wait for `project.commitAsync` completion to get calculated cost values:

```javascript
// use the "10% off rates" rate table for the assignment
assignment1.rateTable = rateTable1;

await project.commitAsync()

// here costs are updated now
console.log('Project cost is', project.cost);
console.log('assignment1 cost is', assignment1.cost);
```

Alternatively the application can use `setRateTable` method that returns a `Promise` resolving once the Engine processes the change:

```javascript
// use the "10% off rates" rate table for the assignment
await assignment1.setRateTable(rateTable1);

// here costs are updated

// here costs are updated now
console.log('Project cost is', project.cost);
console.log('assignment1 cost is', assignment1.cost);
```

## Toggling a resource default rate table

A resource can specify which rate table to be used by default on its `defaultRateTable` field.
Setting the field value will result using the provided rate table when assigning
the resource.

```javascript
// resource1 will use rateTable1 rate table by default
resource1.defaultRateTable = rateTable1;
// resource2 is going to be free by default
resource2.defaultRateTable = null;
```

**Please note that** changing the field doesn't update already existing assignments of the resource. It affect **only** further added assignments.

## Data load example

In order to show an overall resource data setup here is an example of data loading package with `Celia` resource
having two rate tables `Default` and `20% off`. The resource uses `Default` rate table by default:

```json
{
    "resources" : {
        "rows" : [
            {
                "id"               : 1,
                "name"             : "Celia",
                "defaultRateTable" : 101,
                "costAccrual"      : "start",
                "rateTables"       : [
                    {
                        "id"    : 101,
                        "name"  : "Default",
                        "rates" : [
                            {
                                "id"                     : 1,
                                "startDate"              : "2025-01-01",
                                "standardRate"           : 40,
                                "standardRateEffortUnit" : "hour",
                                "perUseCost"             : 5
                            }
                        ]
                    },
                    {
                        "id"    : 199,
                        "name"  : "20% off",
                        "rates" : [
                            {
                                "id"                     : 1,
                                "startDate"              : "2025-01-01",
                                "standardRate"           : 32,
                                "standardRateEffortUnit" : "hour",
                                "perUseCost"             : 4
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

## Cost accrual date

Resource model has got [costAccrual](#Gantt/model/ResourceModel#field-costAccrual) field specifying how the resource
cost get accrued in time.

The field possible values are:

- `prorated` (default) - the resource cost is accrued proportionally across its assigned task duration
- `start` - the resource cost is accrued when its assigned task starts
- `end` - the resource cost is accrued when its assigned task ends

The field does not affect the cost value amount it only affects the value allocation in time which can be seen in the
resource utilization view.

## Resource utilization view

The view supports displaying of cost and material quantity values.
There are three series of data it can display: `effort` (shown by default), `cost` and `quantity`.
The `cost` and `quantity` series are designed to display cost and material expenditure allocation respectively.
To see the latter two series please use the following code:

```javascript
new ResourceUtilization({
    // enable showing resource cost & quantity series too
    // (in addition to resource effort)
    series : {
        cost : {
            disabled : false
        },
        quantity : {
            disabled : false
        }
    },

    // extend the row height to fit all three series data
    rowHeight : 45,
    ...
});
```

Please check [this demo](https://bryntum.com/products/gantt/examples/resourceutilization/) to see how it works.
