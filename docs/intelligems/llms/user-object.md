# Source: https://docs.intelligems.io/developer-resources/javascript-api/user-object.md

# User Object

## Intelligems ID

`window.igData?.user.igId` *(string)*

<details>

<summary>Example</summary>

```javascript
let igId = window.igData?.user.igId;

console.log(igId);

"ig_71e855a9313945b63eb35e0abd5b63361d48"
```

</details>

## Experiments

`window.igData?.user.getExperiments()` *(Array\<experiment>)*

This function returns all experiments that are currently in scope for this user. The logic underneath takes into account whether or not an experiment is active, the user is eligible, and the experiment should run on this page (see [Audience and Page Targeting](https://docs.intelligems.io/general-features/targeting)). If you are previewing an experiment using the intelligems Preview mode, only that experiment will be returned here.

<details>

<summary><strong>Example</strong></summary>

```javascript

console.log(window.igData?.user.getExperiments());

[
    {
        "id": "8bce9d31-cd20-4f4a-a070-a6970c7e9803",
        "name": "Price Test",
        "isPreview": true
    }
]
```

</details>

## Test Groups

### Get All Test Groups in the Experiment

`window.igData?.user.getTestGroups(experimentId)` *(Array\<TestGroup>)*

We will return all Test Groups that are available for this experiment.

<details>

<summary>Example</summary>

```javascript
console.log(window.igData?.user.getTestGroups("8bce9d31-cd20-4f4a-a070-a6970c7e9803"))

[{
    id: "8cead46f-a9d1-41dd-a864-86fc718ee133", 
    name: "Control Group",
    percentage: 50,
    isControl: true,
    freeShippingThreshold: 150,     // number | undefined
    shippingRate:                   // number | undefined
},
{
    id: "c2fdce4d-c3e2-4cf0-92aa-d3498ee67cc9", 
    name: "Test Group 1",
    percentage: 50,
    isControl: false,
    freeShippingThreshold: 150,     // number | undefined
    shippingRate:                   // number | undefined
}]

```

</details>

### Get Test Group by Experiment ID

`window.igData?.user.getTestGroup(experimentId)` (*TestGroup | null*)

We will return a Test Group object based on the user's assignment for a given experiment. If the experiment is not live or the user has no assignment, we will return null.

<details>

<summary><strong>Example</strong></summary>

```javascript
console.log(window.igData?.user.getTestGroup("8bce9d31-cd20-4f4a-a070-a6970c7e9803"))

{
    id: "8cead46f-a9d1-41dd-a864-86fc718ee133", 
    name: "Control Group",
    percentage: 50,
    isControl: true,
    freeShippingThreshold: 150,     // number | undefined
    shippingRate:                   // number | undefined
}

```

</details>

### Assign User to Test Group

`window.igData?.user.assignTestGroup(experimentId, testGroupId)`

We will assign the user to the Test Group provided. This explicit assignment will take precedence over Audience Targeting, Page Targeting, or any other exclusions.

<details>

<summary>Example</summary>

<pre class="language-javascript"><code class="lang-javascript"><strong>window.igData?.user.assignTestGroup("8bce9d31-cd20-4f4a-a070-a6970c7e9803", 
</strong><strong>"c2fdce4d-c3e2-4cf0-92aa-d3498ee67cc9"))
</strong></code></pre>

</details>
