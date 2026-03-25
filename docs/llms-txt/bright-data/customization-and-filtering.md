# Source: https://docs.brightdata.com/datasets/marketplace/customization-and-filtering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customization and filtering

<Frame>
    <img src="https://mintcdn.com/brightdata/2-G3wocTpDaL5JJE/images/datasets/marketplace/customization-and-filtering/customize-button.png?fit=max&auto=format&n=2-G3wocTpDaL5JJE&q=85&s=8c631da0930dd38e989a146572e5c60b" alt="" width="1920" height="941" data-path="images/datasets/marketplace/customization-and-filtering/customize-button.png" />
</Frame>

## Customize Fields

<Frame>
    <img src="https://mintcdn.com/brightdata/2-G3wocTpDaL5JJE/images/datasets/marketplace/customization-and-filtering/customize-fields.png?fit=max&auto=format&n=2-G3wocTpDaL5JJE&q=85&s=d4a4403eb9de6c3579fe84fb46e56f47" alt="" width="1920" height="941" data-path="images/datasets/marketplace/customization-and-filtering/customize-fields.png" />
</Frame>

## Filter

<Frame>
    <img src="https://mintcdn.com/brightdata/2-G3wocTpDaL5JJE/images/datasets/marketplace/customization-and-filtering/filter.png?fit=max&auto=format&n=2-G3wocTpDaL5JJE&q=85&s=2aa528ede12acbdc3feb9e6bcda96068" alt="" width="1920" height="941" data-path="images/datasets/marketplace/customization-and-filtering/filter.png" />
</Frame>

### Filtering a Dataset Using the UI

1. Start by navigating to the dataset you want to filter.
2. Click on the top right button with the filter icon.
3. A menu will appear where you can add a name for the view to help you identify the query.
4. Choose the appropriate filters under the "Include filters" section, such as country, job title, or date.
5. Click the "create subset" button to create the filtered view.

### Filter Functions

#### **Select**

* Use this function to select one or more exact matches from a predefined list, such as countries or regions. This is useful when dealing with a known set of values.

#### **Boolean**

* Filter by boolean values (true or false) to find specific records meeting criteria, such as verified or unverified social media profiles.

#### **Date**

* Use this filter to specify a date range, with start and end dates, useful for trend analysis or filtering events by date.

#### **Number**

* Options include:
  * **Is:** Matches exact numerical values.
  * **Not:** Excludes specified values.
  * **Exist:** Filters non-empty numerical fields.
  * **List (exact match):** Matches exact values from a list.
  * **Lower than / Lower or equal to:** Filters values below or up to a specific number.
  * **Greater than / Greater or equal to:** Filters values above or up to a specific number.

#### **String**

* Filter by string values using options like exact match, exclusion, list matching, or pattern inclusion to refine searches.

#### **Array**

* Use the "Array includes" filter to check if a value exists within an array field, such as specific tags.

### Creating Rule-Based Group Filters

* Create group filters by clicking on the “+Add filter” dropdown and selecting “Add group.”
* Group filters allow you to set rules, such as filtering a dataset where the category is “Electronics” and the brand is “Dell” or “Apple.”

### Limitations

* Groups cannot be nested, and a maximum of two groups per filter is allowed.\
  If you require more complex queries, contact your account manager for assistance with custom queries and filters.

* 4-Input per group.\
  There's a limit of 4 inputs per filter group. To filter by more values, upload them as a CSV list instead of adding each one separately. This lets you filter by many values using just one input slot.
