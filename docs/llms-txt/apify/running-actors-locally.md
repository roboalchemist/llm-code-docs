# Source: https://docs.apify.com/sdk/python/docs/overview/running-actors-locally.md

# Running Actors locally

Copy for LLM

In this page, you'll learn how to create and run Apify Actors locally on your computer.

## Requirements[](#requirements)

The Apify SDK requires Python version 3.10 or above to run Python Actors locally.

## Creating your first Actor[](#creating-your-first-actor)

To create a new Apify Actor on your computer, you can use the [Apify CLI](https://docs.apify.com/cli), and select one of the [Python Actor templates](https://apify.com/templates/categories/python).

For example, to create an Actor from the Python SDK template, you can use the [`apify create`](https://docs.apify.com/cli/docs/reference#apify-create-actorname) command.

```
apify create my-first-actor --template python-start
```

This will create a new folder called `my-first-actor`, download and extract the "Getting started with Python" Actor template there, create a virtual environment in `my-first-actor/.venv`, and install the Actor dependencies in it.

## Running the Actor[](#running-the-actor)

To run the Actor, you can use the [`apify run`](https://docs.apify.com/cli/docs/reference#apify-run) command:

```
cd my-first-actor
apify run
```

This will activate the virtual environment in `.venv` (if no other virtual environment is activated yet), then start the Actor, passing the right environment variables for local running, and configure it to use local storages from the `storage` folder.

The Actor input, for example, will be in `storage/key_value_stores/default/INPUT.json`.

## Adding dependencies[](#adding-dependencies)

Adding dependencies into the Actor is simple.

First, add them in the [`requirements.txt`](https://pip.pypa.io/en/stable/reference/requirements-file-format/) file in the Actor source folder.

Then activate the virtual environment in `.venv`:

* Linux / macOS
* Windows

```
source .venv/bin/activate
```

```
.venv\Scripts\activate
```

Then install the dependencies:

```
python -m pip install -r requirements.txt
```
