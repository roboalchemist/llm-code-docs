# Exporting

To export data is to go from the Schematics representation of data to some
other form.  It’s also possible you want to adjust some things along the way,
such as skipping over some fields or providing empty values for missing fields.

The general mechanism for data export is to call a function on every field in
the model.  The function probably converts the field’s value to some other
format, but you can easily modify it.

We’ll use the following model for the examples:

```
from schematics.models import Model
from schematics.types import StringType, DateTimeType
from schematics.transforms import blacklist

class Movie(Model):
    name = StringType()
    director = StringType()
    release_date = DateTimeType
    personal_thoughts = StringType()
    class Options:
        roles = {'public': blacklist('personal_thoughts')}

```