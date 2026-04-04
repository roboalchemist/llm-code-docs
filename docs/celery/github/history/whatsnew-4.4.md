# What\'s new in Celery 4.4 (Cliffs) {#whatsnew-4.4}

Author

:   Asif Saif Uddin (`auvipy at gmail.com`)

::: sidebar
**Change history**

What\'s new documents describe the changes in major versions, we also
have a `changelog`{.interpreted-text role="ref"} that lists the changes
in bugfix releases (0.0.x), while older series are archived under the
`history`{.interpreted-text role="ref"} section.
:::

Celery is a simple, flexible, and reliable distributed programming
framework to process vast amounts of messages, while providing
operations with the tools required to maintain a distributed system with
python.

It\'s a task queue with focus on real-time processing, while also
supporting task scheduling.

Celery has a large and diverse community of users and contributors, you
should come join us `on IRC <irc-channel>`{.interpreted-text role="ref"}
or `our mailing-list <mailing-list>`{.interpreted-text role="ref"}.

To read more about Celery you should go read the
`introduction <intro>`{.interpreted-text role="ref"}.

While this version is backward compatible with previous versions it\'s
important that you read the following section.

This version is officially supported on CPython 2.7, 3.5, 3.6, 3.7 & 3.8
and is also supported on PyPy2 & PyPy3.

::: topic
**Table of Contents**

Make sure you read the important notes before upgrading to this version.
:::

::: {.contents local="" depth="2"}
:::

## Preface

The 4.4.0 release continues to improve our efforts to provide you with
the best task execution platform for Python.

This release has been codenamed
[Cliffs](https://www.youtube.com/watch?v=i524g6JMkwI) which is one of my
favorite tracks.

This release focuses on mostly bug fixes and usability improvement for
developers. Many long standing bugs, usability issues, documentation
issues & minor enhancement issues were squashed which improve the
overall developers experience.

Celery 4.4 is the first release to support Python 3.8 & pypy36-7.2.

As we now begin to work on Celery 5, the next generation of our task
execution platform, at least another 4.x is expected before Celery 5
stable release & will get support for at least 1 years depending on
community demand and support.

We have also focused on reducing contribution friction and updated the
contributing tools.

*--- Asif Saif Uddin*

### Wall of Contributors

::: note
::: title
Note
:::

This wall was automatically generated from git history, so sadly it
doesn\'t not include the people who help with more important things like
answering mailing-list questions.
:::

## Upgrading from Celery 4.3

Please read the important notes below as there are several breaking
changes.

## Important Notes {#v440-important}

### Supported Python Versions

The supported Python Versions are:

-   CPython 2.7
-   CPython 3.5
-   CPython 3.6
-   CPython 3.7
-   CPython 3.8
-   PyPy2.7 7.2 (`pypy2`)
-   PyPy3.5 7.1 (`pypy3`)
-   PyPy3.6 7.2 (`pypy3`)

### Dropped support for Python 3.4

Celery now requires either Python 2.7 or Python 3.5 and above.

Python 3.4 has reached EOL in March 2019. In order to focus our efforts
we have dropped support for Python 3.4 in this version.

If you still require to run Celery using Python 3.4 you can still use
Celery 4.3. However we encourage you to upgrade to a supported Python
version since no further security patches will be applied for Python
3.4.

### Kombu

Starting from this release, the minimum required version is Kombu 4.6.6.

### Billiard

Starting from this release, the minimum required version is Billiard
3.6.1.

### Redis Message Broker

Due to multiple bugs in earlier versions of redis-py that were causing
issues for Celery, we were forced to bump the minimum required version
to 3.3.0.

### Redis Result Backend

Due to multiple bugs in earlier versions of redis-py that were causing
issues for Celery, we were forced to bump the minimum required version
to 3.3.0.

### DynamoDB Result Backend

The DynamoDB result backend has gained TTL support. As a result the
minimum boto3 version was bumped to 1.9.178 which is the first version
to support TTL for DynamoDB.

### S3 Results Backend

To keep up with the current AWS API changes the minimum boto3 version
was bumped to 1.9.125.

### SQS Message Broker

To keep up with the current AWS API changes the minimum boto3 version
was bumped to 1.9.125.

### Configuration

[CELERY_TASK_RESULT_EXPIRES]{.title-ref} has been replaced with
[CELERY_RESULT_EXPIRES]{.title-ref}.

## News {#v440-news}

### Task Pools

#### Threaded Tasks Pool

We reintroduced a threaded task pool using
[concurrent.futures.ThreadPoolExecutor]{.title-ref}.

The previous threaded task pool was experimental. In addition it was
based on the [threadpool](https://pypi.org/project/threadpool/) package
which is obsolete.

You can use the new threaded task pool by setting
`worker_pool`{.interpreted-text role="setting"} to \'threads\` or by
passing [\--pool threads]{.title-ref} to the [celery worker]{.title-ref}
command.

### Result Backends

#### ElasticSearch Results Backend

##### HTTP Basic Authentication Support

You can now use HTTP Basic Authentication when using the ElasticSearch
result backend by providing the username and the password in the URI.

Previously, they were ignored and only unauthenticated requests were
issued.

#### MongoDB Results Backend

##### Support for Authentication Source and Authentication Method

You can now specify the authSource and authMethod for the MongoDB using
the URI options. The following URI does just that:

> `mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-256`

Refer to the
[documentation](https://api.mongodb.com/python/current/examples/authentication.html)
for details about the various options.

### Tasks

#### Task class definitions can now have retry attributes

You can now use [autoretry_for]{.title-ref}, [retry_kwargs]{.title-ref},
[retry_backoff]{.title-ref}, [retry_backoff_max]{.title-ref} and
[retry_jitter]{.title-ref} in class-based tasks:

``` python
class BaseTaskWithRetry(Task):
  autoretry_for = (TypeError,)
  retry_kwargs = {'max_retries': 5}
  retry_backoff = True
  retry_backoff_max = 700
  retry_jitter = False
```

### Canvas

#### Replacing Tasks Eagerly

You can now call [self.replace()]{.title-ref} on tasks which are run
eagerly. They will work exactly the same as tasks which are run
asynchronously.

#### Chaining Groups

Chaining groups no longer result in a single group.

The following used to join the two groups into one. Now they correctly
execute one after another:

    >>> result = group(add.si(1, 2), add.si(1, 2)) | group(tsum.s(), tsum.s()).delay()
    >>> result.get()
    [6, 6]
