# Quickstart Guide

Working with Schematics begins with modeling the data, so this tutorial will
start there.

After that we will take a quick look at serialization, validation, and what it
means to save this data to a database.

## Simple Model

Let’s say we want to build a structure for storing weather data.  At it’s core,
we’ll need a way to represent some temperature information and where that temp
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