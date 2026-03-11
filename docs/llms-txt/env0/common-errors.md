# Source: https://docs.envzero.com/guides/admin-guide/variables/common-errors.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling Common Errors

> Troubleshoot common variable errors including TF_VAR formatting issues for lists, maps, and sensitive values

## "The root module input variable '\[variable\_name]' is not set, and has no default value" or "Error: Variables not allowed"

This is commonly associated with using `TF_VAR_*` where the variable type is a list or map.  Please make sure the value is properly formatted for the variable type.
`list` type expects an array with quotes around the list item.  e.g. `["listitem1", "listitem2"]`
`map` type expects a key/value map surrounded curly brackets. e.g. `{"key1": "value1", "key2": "value2"}`

## "Error: Incorrect attribute value type"

This can occur if your template variables do not specify the type and you are trying to assign the value in the Environment Variables section.  e.g.

<Info>
  ```bash  theme={null}
  export TF_VAR_myvar='["listitem1","listitem2"]'
  ```

  ```hcl  theme={null}
  variable "myvar" {
    type = list(string) // make sure you add this field to your variable
  }
  ```

</Info>

Built with [Mintlify](https://mintlify.com).
