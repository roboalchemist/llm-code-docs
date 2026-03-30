# luigi.contrib.salesforce

Functions

`ensure_utf`(value)

`get_soql_fields`(soql)

Gets queried columns names.

`parse_results`(fields, data)

Traverses ordered dictionary, calls _traverse_results() to recursively read into the dictionary depth of data

Classes

`QuerySalesforce`(*args, **kwargs)

`SalesforceAPI`(username, password, security_token)

Class used to interact with the SalesforceAPI.

`salesforce`(*args, **kwargs)

Config system to get config vars from 'salesforce' section in configuration file.

luigi.contrib.salesforce.get_soql_fields(*soql*)

Gets queried columns names.

luigi.contrib.salesforce.ensure_utf(*value*)

luigi.contrib.salesforce.parse_results(*fields*, *data*)

Traverses ordered dictionary, calls _traverse_results() to recursively read into the dictionary depth of data

class luigi.contrib.salesforce.salesforce(**args*, ***kwargs*)

Config system to get config vars from ‘salesforce’ section in configuration file.

Did not include sandbox_name here, as the user may have multiple sandboxes.

username

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```