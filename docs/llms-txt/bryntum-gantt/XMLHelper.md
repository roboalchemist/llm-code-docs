# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/XMLHelper.md

# [XMLHelper](https://bryntum.com/docs/gantt/api/Core/helper/XMLHelper)

Helper for XML manipulation.

## Functions

Functions are methods available for calling on the class

[convertFromObject](https://bryntum.com/docs/gantt/api/Core/helper/XMLHelper#function-convertFromObject-static)
Convert a JavaScript object to an XML string.

From:

```
{
    name : 'Task 1',
    data : [
        {
            text : 'foo 1',
            ref  : 'fooItem 1'
        },
        {
            text : 'foo 2',
            ref  : 'fooItem 2'
        }
    ]
}
```

To:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<root>
    <name>Task 1</name>
    <data>
        <element>
            <text>foo 1</text>
            <ref>fooItem 1</ref>
        </element>
        <element>
            <text>foo 2</text>
            <ref>fooItem 2</ref>
        </element>
    </data>
</root>
```
