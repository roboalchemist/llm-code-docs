# Extending

For most non trivial cases, the base types may not be enough. Schematics is designed to be flexible to allow for extending data types in order to accomodate custom logic.

## Simple Example

A simple example is allowing for value transformations.

Say that there is a model that requires email validation. Since emails are case insenstive, it might be helpful to convert the input email to lower case before continuing to validate.

This can be achieved by Extending the Email class

```
>>> from schematics.types import EmailType
>>> class LowerCaseEmailType(EmailType):
...
...     # override convert method
...     def convert(self, value, context=None):
...        value = super().convert(value, context)
...        return value.lower() # value will be converted to lowercase

```