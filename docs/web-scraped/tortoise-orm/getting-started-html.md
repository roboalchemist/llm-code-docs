# Source: https://tortoise.github.io/getting_started.html

Title: Getting started - Tortoise ORM v1.1.6 Documentation

URL Source: https://tortoise.github.io/getting_started.html

Published Time: Thu, 05 Mar 2026 07:20:56 GMT

Markdown Content:
Getting started - Tortoise ORM v1.1.6 Documentation
===============
- [x] - [x] [![Image 1: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation")

 Tortoise ORM 1.1.6 Documentation 

 Getting started 

[](javascript:void(0) "Share")

 Initializing search 

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   [Getting started](https://tortoise.github.io/getting_started.html#)
*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

[![Image 2: logo](https://tortoise.github.io/_static/tortoise.png)](https://tortoise.github.io/toc.html "Tortoise ORM v1.1.6 Documentation") Tortoise ORM v1.1.6 Documentation  

[tortoise-orm](https://github.com/tortoise/tortoise-orm "Go to repository")

*   [Tortoise ORM](https://tortoise.github.io/index.html)
*   - [x] Getting started [Getting started](https://tortoise.github.io/getting_started.html#) Table of contents  
    *   [Installation](https://tortoise.github.io/getting_started.html#installation)
        *   [Optional Dependencies](https://tortoise.github.io/getting_started.html#optional-dependencies)

    *   [Tutorial](https://tortoise.github.io/getting_started.html#tutorial)

*   [Reference](https://tortoise.github.io/reference.html)
*   [Examples](https://tortoise.github.io/examples.html)
*   [Contrib](https://tortoise.github.io/contrib.html)
*   [Migration Guide: Tortoise 1.0](https://tortoise.github.io/migration_guide.html)
*   [Changelog](https://tortoise.github.io/CHANGELOG.html)
*   [Roadmap](https://tortoise.github.io/roadmap.html)
*   [Contribution Guide](https://tortoise.github.io/CONTRIBUTING.html)
*   [Thanks](https://tortoise.github.io/CONTRIBUTORS.html)

Getting started[¶](https://tortoise.github.io/getting_started.html#getting-started "Link to this heading")
==========================================================================================================

Installation[¶](https://tortoise.github.io/getting_started.html#installation "Link to this heading")
----------------------------------------------------------------------------------------------------

Note

Tortoise ORM requires **Python 3.10** or later.

The following table shows the available installation options for different databases (note that there are multiple options of clients for some databases):

Available Installation Options[¶](https://tortoise.github.io/getting_started.html#id2 "Link to this table")| Database | Installation Command |
| --- | --- |
| SQLite | `pip install tortoise-orm` |
| PostgreSQL (psycopg) | `pip install "tortoise-orm[psycopg]"` |
| PostgreSQL (asyncpg) | `pip install "tortoise-orm[asyncpg]"` |
| MySQL (aiomysql) | `pip install "tortoise-orm[aiomysql]"` |
| MySQL (asyncmy) | `pip install "tortoise-orm[asyncmy]"` |
| MS SQL | `pip install "tortoise-orm[asyncodbc]"` |
| Oracle | `pip install "tortoise-orm[asyncodbc]"` |

### Optional Dependencies[¶](https://tortoise.github.io/getting_started.html#optional-dependencies "Link to this heading")

The following libraries can be used to improve performance:

*   [orjson](https://pypi.org/project/orjson/): Automatically used if installed for JSON SerDes.

*   [uvloop](https://pypi.org/project/uvloop/): Shown to improve performance as an alternative to `asyncio`.

*   [ciso8601](https://pypi.org/project/ciso8601/): Automatically used if installed. Not automatically installed on Windows due to often a lack of a C compiler. Default on Linux/CPython.

The following command will install all optional dependencies:

```
pip install "tortoise-orm[accel]"
```

Tutorial[¶](https://tortoise.github.io/getting_started.html#tutorial "Link to this heading")
--------------------------------------------------------------------------------------------

Define the models by inheriting from `tortoise.models.Model`.

```
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    # References to other models are defined in format
    # "{app_name}.{model_name}" - where {app_name} is defined in the tortoise config
    tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')

class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
```

Note

You can read more on defining models in [Models](https://tortoise.github.io/models.html#models)

After defining the models, Tortoise ORM needs to be initialized to establish the relationships between models and connect to the database. The code below creates a connection to a SQLite DB database with the `aiosqlite` client. `generate_schema` sets up schema on an empty database. `generate_schema` is for development purposes only, see [Migrations](https://tortoise.github.io/migration.html#migration) for schema migration tools.

```
from tortoise import Tortoise, run_async

async def main():
    # Here we connect to a SQLite DB file.
    # also specify the app name of "models"
    # which contain models from "app.models
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()

run_async(main())
```

`run_async` is a helper function to run simple Tortoise scripts. For production use, see [Tortoise-ORM FastAPI integration](https://tortoise.github.io/contrib/fastapi.html#contrib-fastapi), [Tortoise-ORM Sanic integration](https://tortoise.github.io/contrib/sanic.html#contrib-sanic) and other integrations, as welll as check out [The Importance of Cleaning Up](https://tortoise.github.io/setup.html#cleaningup).

With the Tortoise initialized, the models are available for use:

```
async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()

    # Creating an instance with .save()
    tournament = Tournament(name='New Tournament')
    await tournament.save()

    # Or with .create()
    await Event.create(name='Without participants', tournament=tournament)
    event = await Event.create(name='Test', tournament=tournament)
    participants = []
    for i in range(2):
        team = await Team.create(name='Team {}'.format(i + 1))
        participants.append(team)

    # Many to Many Relationship management is quite straightforward
    # (there are .remove(...) and .clear() too)
    await event.participants.add(*participants)

    # Iterate over related entities with the async context manager
    async for team in event.participants:
        print(team.name)

    # The related entities are cached and can be iterated in the synchronous way afterwards
    for team in event.participants:
        pass

    # Use prefetch_related to fetch related objects
    selected_events = await Event.filter(
        participants=participants[0].id
    ).prefetch_related('participants', 'tournament')
    for event in selected_events:
        print(event.tournament.name)
        print([t.name for t in event.participants])

    # Prefetch multiple levels of related entities
    await Team.all().prefetch_related('events__tournament')

    # Filter and order by related models too
    await Tournament.filter(
        events__name__in=['Test', 'Prod']
    ).order_by('-events__participants__name').distinct()

run_async(main())
```

Note

Find more examples (including transactions, using multiple databases and more complex querying) in [Examples](https://tortoise.github.io/examples.html#examples) and [Query API](https://tortoise.github.io/query.html#query-api).

 Back to top 

 © Copyright 2018 - 2026, Andrey Bondar & Nickolas Grigoriadis & long2ice. 

 Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. and [Sphinx-Immaterial](https://github.com/jbms/sphinx-immaterial/)
