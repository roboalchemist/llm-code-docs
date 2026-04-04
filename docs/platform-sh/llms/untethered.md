# Source: https://docs.upsun.com/development/local/untethered.md

# Untethered local development

It's possible to run your entire site locally on your computer.
That way you get better performance as there's no extra latency to connect to a remote database and doesn't require an active Internet connection to work.
But it does require running all necessary services (databases, search servers, and so on) locally.
These can be set up however you prefer, although Upsun recommends using a virtual machine to make it easier to share configuration between developers.

If you already have a development workflow in place that works for you, you can keep using it with virtually no changes.

To synchronize data from an environment on Upsun, consult the documentation for each [service](https://docs.upsun.com../../add-services.md).
Each service type has its own native data import/export process and Upsun doesn't get in the way of that.
It's also straightforward to [download user files](https://docs.upsun.com/learn/tutorials/exporting.md) from your application using rsync.

