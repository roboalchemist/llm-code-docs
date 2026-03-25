# Jobs: pausing and resuming crawls

Sometimes, for big sites, it’s desirable to pause crawls and be able to resume
them later.

Scrapy supports this functionality out of the box by providing the following
facilities:

- 

a scheduler that persists scheduled requests on disk

- 

a duplicates filter that persists visited requests on disk

- 

an extension that keeps some spider state (key/value pairs) persistent
between batches

## Job directory

To enable persistence support you just need to define a *job directory* through
the `JOBDIR` setting. This directory will be for storing all required data to
keep the state of a single job (i.e. a spider run).  It’s important to note that
this directory must not be shared by different spiders, or even different
jobs/runs of the same spider, as it’s meant to be used for storing the state of
a *single* job.

## How to use it

To start a spider with persistence support enabled, run it like this:

```
scrapy crawl somespider -s JOBDIR=crawls/somespider-1

```