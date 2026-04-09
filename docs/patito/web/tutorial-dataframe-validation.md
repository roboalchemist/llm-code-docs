# Using Patito for DataFrame Validation

Have you ever found yourself relying on some column of an external data source being non-nullable only to find out much later that the assumption proved to be false?
What about discovering that a production machine learning model has had a huge performance regression because a new category was introduced to a categorical column?
You might not have encountered any of these exact scenarios, but perhaps similar ones; they illustrate the necessity of validating your data.

A machine learning model might ingest data from a production system that changes frequently, and the author of the model wants to be notified if certain assumptions no longer hold.
Or perhaps a data analyst might rely on a pre-processing step that removes all discontinued products from a data set, and this should be validated and communicated clearly in their Jupyter notebook.

patito [https://github.com/kolonialno/patito] is a dataframe validation library built on top of polars [https://github.com/pola-rs/polars] initially open sourced by Oda, which tries to solve this problem.
The polars dataframe library has lately been making the rounds among data scientists, and for good reasons.
It can be considered as a total replacement of the well-known pandas [https://github.com/pandas-dev/pandas] library, initially tempting you with its advertised top-notch performance [https://www.pola.rs/benchmarks.html], but then sealing the deal with its intuitive and expressive API.
The exact virtues of polars is a topic for another article, but suffice it to say that it is highly recommended and it has some great introductory documentation [https://pola-rs.github.io/polars-book/user-guide/].

The core idea of Patito is that you should define a so-called “model” for each of your data sources.
A model is a declarative python class which describes the general properties of a tabular data set: the names of all the columns, their types, value bounds, and so on…
These models can then be used to validate the data sources when they are ingested into your project’s data pipeline.
In turn, your models become a trustworthy, centralized catalog of all the core facts about your data, facts you can safely rely upon during development.

Enough chit chat, let’s get into some technical details!
Let’s say that your project keeps track of products, and that these products have four core properties:

- 

A unique, numeric identifier

- 

A name

- 

An ideal temperature zone of either `"dry"`, `"cold"`, or `"frozen"`

- 

A product demand given as a percentage of the total sales forecast for the next week

In tabular form the data might look something like this.

Table 1: Products

`product_id`

`name`

`temperature_zone`

`demand_percentage`

1

Apple

dry

0.23%

2

Milk

cold

0.61%

3

Ice cubes

frozen

0.01%

…

…

…

…

We now start to model the restrictions we want to put upon our data.
In Patito this is done by defining a class which inherits from `patito.Model`, a class which has one field annotation for each column in the data.
These models should preferably be defined in a centralized place, conventionally `<YOUR_PROJECT_NAME>/models.py`, where you can easily find and refer to them.

project/models.py