# Types

*class *`BaseType`(*required=False*, *default=Undefined*, *serialized_name=None*, *choices=None*, *validators=None*, *deserialize_from=None*, *export_level=None*, *serialize_when_none=None*, *messages=None*, *metadata=None*)

A base class for Types in a Schematics model. Instances of this
class may be added to subclasses of `Model` to define a model schema.

Validators that need to access variables on the instance
can be defined be implementing methods whose names start with `validate_`
and accept one parameter (in addition to `self`)

Parameters

- 

**required** – Invalidate field when value is None or is not supplied. Default:
False.

- 

**default** – When no data is provided default to this value. May be a callable.
Default: None.

- 

**serialized_name** – The name of this field defaults to the class attribute used in the
model. However if the field has another name in foreign data set this
argument. Serialized data will use this value for the key name too.

- 

**deserialize_from** – A name or list of named fields for which foreign data sets are
searched to provide a value for the given field.  This only effects
inbound data.

- 

**choices** – A list of valid choices. This is the last step of the validator
chain.

- 

**validators** – A list of callables. Each callable receives the value after it has been
converted into a rich python type. Default: []

- 

**serialize_when_none** – Dictates if the field should appear in the serialized data even if the
value is None. Default: None.

- 

**messages** – Override the error messages with a dict. You can also do this by
subclassing the Type and defining a MESSAGES dict attribute on the
class. A metaclass will merge all the MESSAGES and override the
resulting dict with instance level messages and assign to
self.messages.

- 

**metadata** – 

Dictionary for storing custom metadata associated with the field.
To encourage compatibility with external tools, we suggest these keys
for common metadata:
- *label* : Brief human-readable label
- *description* : Explanation of the purpose of the field. Used for

help, tooltips, documentation, etc.