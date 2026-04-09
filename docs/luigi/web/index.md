[https://actions-badge.atrox.dev/spotify/luigi/goto?ref=master]

 [https://codecov.io/gh/spotify/luigi?branch=master]

 [https://pypi.python.org/pypi/luigi]

 [https://pypi.python.org/pypi/luigi]

 [https://luigi.readthedocs.io/en/stable/?badge=stable]

Luigi is a Python (3.10, 3.11, 3.12, 3.13 tested) package that helps you build complex
pipelines of batch jobs. It handles dependency resolution, workflow management,
visualization, handling failures, command line integration, and much more.

# Getting Started

Run `pip install luigi` to install the latest stable version from PyPI [https://pypi.python.org/pypi/luigi]. Documentation for the latest release [https://luigi.readthedocs.io/en/stable/] is hosted on readthedocs.

Run `pip install luigi[toml]` to install Luigi with TOML-based configs [https://luigi.readthedocs.io/en/stable/configuration.html] support.

For the bleeding edge code, `pip install
git+https://github.com/spotify/luigi.git`. Bleeding edge documentation [https://luigi.readthedocs.io/en/latest/] is also available.

# Background

The purpose of Luigi is to address all the plumbing typically associated
with long-running batch processes. You want to chain many tasks,
automate them, and failures *will* happen. These tasks can be anything,
but are typically long running things like
Hadoop [http://hadoop.apache.org/] jobs, dumping data to/from
databases, running machine learning algorithms, or anything else.

There are other software packages that focus on lower level aspects of
data processing, like Hive [http://hive.apache.org/],
Pig [http://pig.apache.org/], or
Cascading [http://www.cascading.org/]. Luigi is not a framework to
replace these. Instead it helps you stitch many tasks together, where
each task can be a Hive query [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.hive.html],
a Hadoop job in Java [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.hadoop_jar.html],
a  Spark job in Scala or Python [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.spark.html],
a Python snippet,
dumping a table [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.sqla.html]
from a database, or anything else. It’s easy to build up
long-running pipelines that comprise thousands of tasks and take days or
weeks to complete. Luigi takes care of a lot of the workflow management
so that you can focus on the tasks themselves and their dependencies.

You can build pretty much any task you want, but Luigi also comes with a
*toolbox* of several common task templates that you use. It includes
support for running
Python mapreduce jobs [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.hadoop.html]
in Hadoop, as well as
Hive [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.hive.html],
and Pig [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.pig.html],
jobs. It also comes with
file system abstractions for HDFS [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.hdfs.html],
and local files that ensures all file system operations are atomic. This
is important because it means your data pipeline will not crash in a
state containing partial data.

# Visualiser page

The Luigi server comes with a web interface too, so you can search and filter
among all your tasks.

# Dependency graph example

Just to give you an idea of what Luigi does, this is a screen shot from
something we are running in production. Using Luigi’s visualiser, we get
a nice visual overview of the dependency graph of the workflow. Each
node represents a task which has to be run. Green tasks are already
completed whereas yellow tasks are yet to be run. Most of these tasks
are Hadoop jobs, but there are also some things that run locally and
build up data files.

# Philosophy

Conceptually, Luigi is similar to GNU
Make [http://www.gnu.org/software/make/] where you have certain tasks
and these tasks in turn may have dependencies on other tasks. There are
also some similarities to Oozie [http://oozie.apache.org/]
and Azkaban [https://azkaban.github.io/]. One major
difference is that Luigi is not just built specifically for Hadoop, and
it’s easy to extend it with other kinds of tasks.

Everything in Luigi is in Python. Instead of XML configuration or
similar external data files, the dependency graph is specified *within
Python*. This makes it easy to build up complex dependency graphs of
tasks, where the dependencies can involve date algebra or recursive
references to other versions of the same task. However, the workflow can
trigger things not in Python, such as running
Pig scripts [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.pig.html]
or scp’ing files [https://luigi.readthedocs.io/en/latest/api/luigi.contrib.ssh.html].

# Who uses Luigi?

We use Luigi internally at Spotify [https://www.spotify.com] to run
thousands of tasks every day, organized in complex dependency graphs.
Most of these tasks are Hadoop jobs. Luigi provides an infrastructure
that powers all kinds of stuff including recommendations, toplists, A/B
test analysis, external reports, internal dashboards, etc.

Since Luigi is open source and without any registration walls, the exact number
of Luigi users is unknown. But based on the number of unique contributors, we
expect hundreds of enterprises to use it. Some users have written blog posts
or held presentations about Luigi:

- 

Spotify [https://www.spotify.com] (presentation, 2014) [http://www.slideshare.net/erikbern/luigi-presentation-nyc-data-science]

- 

Foursquare [https://foursquare.com/] (presentation, 2013) [http://www.slideshare.net/OpenAnayticsMeetup/luigi-presentation-17-23199897]

- 

Mortar Data (Datadog) [https://www.datadoghq.com/] (documentation / tutorial) [http://help.mortardata.com/technologies/luigi]

- 

Stripe [https://stripe.com/] (presentation, 2014) [http://www.slideshare.net/PyData/python-as-part-of-a-production-machine-learning-stack-by-michael-manapat-pydata-sv-2014]

- 

Buffer [https://buffer.com/] (blog, 2014) [https://buffer.com/resources/buffers-new-data-architecture/]

- 

SeatGeek [https://seatgeek.com/] (blog, 2015) [http://chairnerd.seatgeek.com/building-out-the-seatgeek-data-pipeline/]

- 

Treasure Data [https://www.treasuredata.com/] (blog, 2015) [http://blog.treasuredata.com/blog/2015/02/25/managing-the-data-pipeline-with-git-luigi/]

- 

Growth Intelligence [http://growthintel.com/] (presentation, 2015) [http://www.slideshare.net/growthintel/a-beginners-guide-to-building-data-pipelines-with-luigi]

- 

AdRoll [https://www.adroll.com/] (blog, 2015) [http://tech.adroll.com/blog/data/2015/09/22/data-pipelines-docker.html]

- 

17zuoye (presentation, 2015) [https://speakerdeck.com/mvj3/luiti-an-offline-task-management-framework]

- 

Custobar [https://www.custobar.com/] (presentation, 2016) [http://www.slideshare.net/teemukurppa/managing-data-workflows-with-luigi]

- 

Blendle [https://launch.blendle.com/] (presentation) [http://www.anneschuth.nl/wp-content/uploads/sea-anneschuth-streamingblendle.pdf#page=126]

- 

TrustYou [http://www.trustyou.com/] (presentation, 2015) [https://speakerdeck.com/mfcabrera/pydata-berlin-2015-processing-hotel-reviews-with-python]

- 

Groupon [https://www.groupon.com/] / OrderUp [https://orderup.com] (alternative implementation) [https://github.com/groupon/luigi-warehouse]

- 

Red Hat - Marketing Operations [https://www.redhat.com] (blog, 2017) [https://github.com/rh-marketingops/rh-mo-scc-luigi]

- 

GetNinjas [https://www.getninjas.com.br/] (blog, 2017) [https://labs.getninjas.com.br/using-luigi-to-create-and-monitor-pipelines-of-batch-jobs-eb8b3cd2a574]

- 

voyages-sncf.com [https://www.voyages-sncf.com/] (presentation, 2017) [https://github.com/voyages-sncf-technologies/meetup-afpy-nantes-luigi]

- 

Open Targets [https://www.opentargets.org/] (blog, 2017) [https://blog.opentargets.org/using-containers-with-luigi]

- 

Leipzig University Library [https://ub.uni-leipzig.de] (presentation, 2016) [https://de.slideshare.net/MartinCzygan/build-your-own-discovery-index-of-scholary-eresources] / (project) [https://finc.info/de/datenquellen]

- 

Synetiq [https://synetiq.net/] (presentation, 2017) [https://www.youtube.com/watch?v=M4xUQXogSfo]

- 

Glossier [https://www.glossier.com/] (blog, 2018) [https://medium.com/glossier/how-to-build-a-data-warehouse-what-weve-learned-so-far-at-glossier-6ff1e1783e31]

- 

Data Revenue [https://www.datarevenue.com/] (blog, 2018) [https://www.datarevenue.com/en/blog/how-to-scale-your-machine-learning-pipeline]

- 

Uppsala University [http://pharmb.io] (tutorial) [http://uppnex.se/twiki/do/view/Courses/EinfraMPS2015/Luigi.html]   / (presentation, 2015) [https://www.youtube.com/watch?v=f26PqSXZdWM] / (slides, 2015) [https://www.slideshare.net/SamuelLampa/building-workflows-with-spotifys-luigi] / (poster, 2015) [https://pharmb.io/poster/2015-sciluigi/] / (paper, 2016) [https://doi.org/10.1186/s13321-016-0179-6] / (project) [https://github.com/pharmbio/sciluigi]

- 

GIPHY [https://giphy.com/] (blog, 2019) [https://engineering.giphy.com/luigi-the-10x-plumber-containerizing-scaling-luigi-in-kubernetes/]

- 

xtream [https://xtreamers.io/] (blog, 2019) [https://towardsdatascience.com/lessons-from-a-real-machine-learning-project-part-1-from-jupyter-to-luigi-bdfd0b050ca5]

- 

CIAN [https://cian.ru/] (presentation, 2019) [https://www.highload.ru/moscow/2019/abstracts/6030]

Some more companies are using Luigi but haven’t had a chance yet to write about it:

- 

Schibsted [http://www.schibsted.com/]

- 

enbrite.ly [http://enbrite.ly/]

- 

Dow Jones / The Wall Street Journal [http://wsj.com]

- 

Hotels.com [https://hotels.com]

- 

Newsela [https://newsela.com]

- 

Squarespace [https://www.squarespace.com/]

- 

OAO [https://adops.com/]

- 

Grovo [https://grovo.com/]

- 

Weebly [https://www.weebly.com/]

- 

Deloitte [https://www.Deloitte.co.uk/]

- 

Stacktome [https://stacktome.com/]

- 

LINX+Neemu+Chaordic [https://www.chaordic.com.br/]

- 

Foxberry [https://www.foxberry.com/]

- 

Okko [https://okko.tv/]

- 

ISVWorld [http://isvworld.com/]

- 

Big Data [https://bigdata.com.br/]

- 

Movio [https://movio.co.nz/]

- 

Bonnier News [https://www.bonniernews.se/]

- 

Starsky Robotics [https://www.starsky.io/]

- 

BaseTIS [https://www.basetis.com/]

- 

Hopper [https://www.hopper.com/]

- 

VOYAGE GROUP/Zucks [https://zucks.co.jp/en/]

- 

Textpert [https://www.textpert.ai/]

- 

Tracktics [https://www.tracktics.com/]

- 

Whizar [https://www.whizar.com/]

- 

xtream [https://www.xtreamers.io/]

- 

Skyscanner [https://www.skyscanner.net/]

- 

Jodel [https://www.jodel.com/]

- 

Mekar [https://mekar.id/en/]

- 

M3 [https://corporate.m3.com/en/]

- 

Assist Digital [https://www.assistdigital.com/]

- 

Meltwater [https://www.meltwater.com/]

- 

DevSamurai [https://www.devsamurai.com/]

- 

Veridas [https://veridas.com/]

- 

Aidentified [https://www.aidentified.com/]

We’re more than happy to have your company added here. Just send a PR on GitHub.

# External links

- 

Mailing List [https://groups.google.com/d/forum/luigi-user/] for discussions and asking questions. (Google Groups)

- 

Releases [https://pypi.python.org/pypi/luigi] (PyPI)

- 

Source code [https://github.com/spotify/luigi] (GitHub)

- 

Hubot Integration [https://github.com/houzz/hubot-luigi] plugin for Slack, Hipchat, etc (GitHub)

# Authors

Luigi was built at Spotify [https://www.spotify.com], mainly by
Erik Bernhardsson [https://github.com/erikbern] and
Elias Freider [https://github.com/freider].
Many other people [https://github.com/spotify/luigi/graphs/contributors]
have contributed since open sourcing in late 2012.
Arash Rouhani [https://github.com/tarrasch] was the chief maintainer from 2015 to 2019, and now
Spotify’s Data Team maintains Luigi.

# Table of Contents

- Example – Top Artists

  - Step 1 - Aggregate Artist Streams

  - Running this Locally

  - Step 1b - Aggregate artists with Spark

  - Step 2 – Find the Top Artists

  - Step 3 - Insert into Postgres

  - Using the Central Planner

- Building workflows

  - Target

  - Task

  - Parameter

  - Dependencies

- Tasks

  - Task.requires

  - Requiring another Task

  - Task.output

  - Task.run

  - Task.input

  - Dynamic dependencies

  - Task status tracking

  - Events and callbacks

  - But I just want to run a Hadoop job?

  - Task priority

  - Namespaces, families and ids

  - Instance caching

- Parameters

  - Instance caching

  - Insignificant parameters

  - Parameter visibility

  - Parameter types

  - Setting parameter value for other classes

  - Parameter resolution order

- Running Luigi

  - Running from the Command Line

  - Running from Python code

  - Response of luigi.build()/luigi.run()

  - Luigi on Windows

- Using the Central Scheduler

  - The luigid server

  - Enabling Task History

- Execution Model

  - Workers and task execution

  - Scheduler

  - Triggering tasks

- Luigi Patterns

  - Code Reuse

  - Triggering Many Tasks

  - Triggering recurring tasks

  - Efficiently triggering recurring tasks

  - Backfilling tasks

  - Propagating parameters with Range

  - Batching multiple parameter values into a single run

  - Tasks that regularly overwrite the same data source

  - Avoiding concurrent writes to a single file

  - Decreasing resources of running tasks

  - Monitoring task pipelines

  - Atomic Writes Problem

  - Sending messages to tasks

  - Gathering custom metrics from tasks’ executions

- Configuration

  - Parameters from config Ingestion

  - Configurable options

  - [core]

  - [cors]

  - [worker]

  - [elasticsearch]

  - [email]

  - [batch_email]

  - [hadoop]

  - [hdfs]

  - [hive]

  - [kubernetes]

  - [mysql]

  - [postgres]

  - [prometheus]

  - [redshift]

  - [resources]

  - [retcode]

  - [scalding]

  - [scheduler]

  - [sendgrid]

  - [smtp]

  - [spark]

  - [task_history]

  - [execution_summary]

  - [webhdfs]

  - [datadog]

  - Per Task Retry-Policy

  - Retry-Policy Fields

- Configure logging

  - Config options:

  - Config section

  - Luigid CLI options:

  - Worker CLI options:

  - Configuration options resolution order:

- Design and limitations

- Mypy plugin

  - How to use

  - Examples