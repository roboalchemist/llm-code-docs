# luigi.contrib.external_daily_snapshot

Classes

`ExternalDailySnapshot`(*args, **kwargs)

Abstract class containing a helper method to fetch the latest snapshot.

class luigi.contrib.external_daily_snapshot.ExternalDailySnapshot(**args*, ***kwargs*)

Abstract class containing a helper method to fetch the latest snapshot.

Example:

```
class MyTask(luigi.Task):
  def requires(self):
    return PlaylistContent.latest()

```