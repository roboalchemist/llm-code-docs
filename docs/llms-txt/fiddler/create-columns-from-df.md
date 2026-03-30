# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/utils/create-columns-from-df.md

# create\_columns\_from\_df

Helper function to create Columns from a pandas DataFrame column dtypes. timedelta, period, interval & object dtypes are converted to string. Sparse dtypes are not handled.

## Returns

ModelSchema

## Parameters

| Parameter | Type        | Required | Default | Description            |
| --------- | ----------- | -------- | ------- | ---------------------- |
| `df`      | `DataFrame` | ✗        | `None`  | Input pandas DataFrame |
