# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hierarchical-json-input/example-hierarchical-json-input.md

# Examples

The following data is example JSON data in a file that you can load into PDI:

```
{
     "employees": [
           {
                    "name" : "emp_name_1" ,
                    "age" : 35,
                    "addresses" :[
                           {
                                  "country":"Country_1"
                           },
                           {
                                  "country":"Country_2"
                           }
                    ]
           },
           {
                    "name" : "emp_name_2",
                    "age" : 35,
                    "addresses" :[
                           {
                                  "country" :"Country_3"
                            },
                            {
                                  "country" :"Country_4"
                            {
                    ]
           }
     ]
}
```

## Example 1

The following data is extracted from this JSON file when you specify the **Split rows across path** option as `$.employees[*]` and do not specify any filters:

![Hierarchical JSON Input step example output](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-27023896aa6a540b2dafe40993a12d593edb0b18%2FPDI%20Heirachical%20JSON%20input%20step%20example%20data.png?alt=media)

## Example 2

if you configure the step with an example split path of `$.employees[*]`, and are only interested in the name and age, use the filters of `$.name` and `$.age` on the **Filters** tab. This produces two rows on the stream of the Hierarchical JSON Input step:

Row 1

```
 {
                    "name" : "emp_name_1" ,
                    "age" : 35
           }

```

Row 2

```
{
                    "name" : "emp_name_2",
                    "age" : 35
           }

```

## Example 3

If you wanted a filtered entry in a single HDT row, leave the **Split rows across path** field blank, and use the filter paths

```
$.employees[*].name
$.employees[*].age

```

This will result in a single row with one HDT that does not have the input split as follows:

```
{
     "employees": [
           {
                    "name" : "emp_name_1" ,
                    "age" : 35
           },
           {
                    "name" : "emp_name_2",
                    "age" : 35
           }
     ]
}

```
