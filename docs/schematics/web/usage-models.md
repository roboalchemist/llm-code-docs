# Models

Schematics models are the next form of structure above types. They are a
collection of types in a class. When a Type is given a name inside a Model,
it is called a field.

## Simple Model

Let’s say we want to build a social network for weather. At its core, we’ll
need a way to represent some temperature information and where that temperature
was found.

```
import datetime
from schematics.models import Model
from schematics.types import StringType, DecimalType, DateTimeType

class WeatherReport(Model):
    city = StringType()
    temperature = DecimalType()
    taken_at = DateTimeType(default=datetime.datetime.now)

```