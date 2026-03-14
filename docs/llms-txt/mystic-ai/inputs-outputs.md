# Source: https://docs.mystic.ai/docs/inputs-outputs.md

# Inputs and outputs

Pipelines implement typed IO fields for predictable inference

When you write the code for your Pipeline, you must define its inputs and outputs using the python SDK. These are then used by our API services to check that run requests contain the correct inputs. This page will give an overview of what input and output (**IO**) types are available, what extra options can be used, and how to work with things like files.

# Types

There are 10 types of IO variables used across all Mystic services ([source](https://github.com/mystic-ai/pipeline/blob/3372a21d8281c10732c0e5e173216f44f712609f/pipeline/cloud/schemas/runs.py#L91)):

* Integer - `integer`
* String - `string`
* Floating point - `fp`
* Dictionary - `dictionary`
* Boolean - `boolean`
* None/null - `none`
* Array - `array`
* Pickle\* (*Soon to be deprecated*) - `pkl`
* File - `file`
* Stream\* - `stream`

***\*Output only***

<br />

Numbers, strings and flags are fairly straightforward: you can use basic Python types such as `int`, `str` or `bool`. You can also use `list` to pass in an array of values. For example:

```python
name = Variable(
        str,
        title="Name",
    )
age = Variable(
        int,
        title="Just a number",
    )
book_recommendations = Variable(list)

output_var = my_model.predict(name, age, book_recommendations)
```

Each of these inputs can be configured with optional information and validation settings:

* `default` (type: `any`) - The default value of the variable
* `title` (type : `str`) - The name of the variable
* `description` (type : `str`) - Basic description of the variable
* `examples` (type : `list`) - List of possible inputs
* `gt` (type : `int`) - Greater than (int/float)
* `ge` (type : `int`) - Greater than or equal to (int/float)
* `lt` (type : `int`) - Less than (int/float)
* `le` (type : `int`) - Less than or equal to (int/float)
* `multiple_of` (type : `int`) - Must be a multiple of this number (int/float)
* `allow_inf_nan` (type : `bool`) - Whether to allow infinities or nan values (int/float)
* `max_digits` (type : `int`) - Maximum number of digits in the number to allow (int/float)
* `decimal_places` (type : `int`) - maximum number of decimal places to allow in the number (int/float)
* `min_length` (type : `int`) - Minimum length of an input string (string)
* `max_length` (type : `int`) - Maximum length of the input string (string)
* `choices` (type : `list`) - A list of the only inputs that can be entered

For example:

```python
num = Variable(
        int | None,
        description="A basic input number to do things with",
        title="Input number",
        gt=1,
        lt=100,
    )
color = Variable(str, choices=["blue", "green", "red"])
```

Also note how we can make variables optional by typing them as `None`.

# InputSchema

You can group sets of variables into input schemas for better organisation.

```python
from pipeline.objects.graph import InputSchema, InputField

class MyInputSchema(InputSchema):
    num = InputField(
        int,
        description="A basic input number to do things with",
        title="Input number",
        gt=1,
        lt=100,
    )
    choices = InputField(str, choices=["blue", "green", "red"])

schema = Variable(MyInputSchema)
output_var = my_model.predict(schema)
```

> 🚧 You can only use `InputFields` in the schema definition

To make a field optional you need the following typing and kwarg (by default all fields are required):

```python
class MyInputSchema(InputSchema):
    num: int | None = InputField(
        ...
        optional=True,
    )
```