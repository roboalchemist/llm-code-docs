# Importing

The general mechanism for data import is to call a function on every field in
the data and coerce it into the most appropriate representation in Python. A
date string, for example, would be converted to a `datetime.datetime`.

Perhaps we’re writing a web API that receives song data.  Let’s model the song.

```
class Song(Model):
    name = StringType()
    artist = StringType()
    url = URLType()

```