# luigi.contrib.sqla

Support for SQLAlchemy. Provides SQLAlchemyTarget for storing in databases
supported by SQLAlchemy. The user would be responsible for installing the
required database driver to connect using SQLAlchemy.

Minimal example of a job to copy data to database using SQLAlchemy is as shown
below:

```
from sqlalchemy import String
import luigi
from luigi.contrib import sqla

class SQLATask(sqla.CopyToTable):
    # columns defines the table schema, with each element corresponding
    # to a column in the format (args, kwargs) which will be sent to
    # the sqlalchemy.Column(*args, **kwargs)
    columns = [
        (["item", String(64)], {"primary_key": True}),
        (["property", String(64)], {})
    ]
    connection_string = "sqlite://"  # in memory SQLite database
    table = "item_property"  # name of the table to store data

    def rows(self):
        for row in [("item1", "property1"), ("item2", "property2")]:
            yield row

if __name__ == '__main__':
    task = SQLATask()
    luigi.build([task], local_scheduler=True)

```