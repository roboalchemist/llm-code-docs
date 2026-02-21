# Source: https://dramatiq.io/installation.html

Title: Installation — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/installation.html

Markdown Content:
Dramatiq supports Python versions 3.10 and up and is installable via [pip](https://pip.pypa.io/en/stable/) or from source.

Via pip[¶](https://dramatiq.io/installation.html#via-pip "Link to this heading")
--------------------------------------------------------------------------------

To install dramatiq, simply run the following command in a terminal:

$ pip install -U 'dramatiq[rabbitmq, watch]'

[RabbitMQ](https://www.rabbitmq.com/) is the recommended message broker, but Dramatiq also supports [Redis](https://redis.io/).

If you would like to use it with [Redis](https://redis.io/) then run:

$ pip install -U 'dramatiq[redis, watch]'

If you don’t have [pip](https://pip.pypa.io/en/stable/) installed, check out [this guide](http://docs.python-guide.org/en/latest/starting/installation/).

### Optional Requirements[¶](https://dramatiq.io/installation.html#optional-requirements "Link to this heading")

If you’re using Redis as your broker and aren’t planning on using PyPy then you should additionally install the `hiredis` package to get an increase in throughput.

From Source[¶](https://dramatiq.io/installation.html#from-source "Link to this heading")
----------------------------------------------------------------------------------------

To install the latest development version of dramatiq from source, clone the repo from [GitHub](https://github.com/Bogdanp/dramatiq)

$ git clone https://github.com/Bogdanp/dramatiq

then install it to your local site-packages by running

$ python setup.py install

in the cloned directory.
