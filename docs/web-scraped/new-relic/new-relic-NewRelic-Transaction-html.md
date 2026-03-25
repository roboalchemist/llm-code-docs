# Source: https://hexdocs.pm/new_relic/NewRelic.Transaction.html

Title: NewRelic.Transaction — new_relic v0.2.0

URL Source: https://hexdocs.pm/new_relic/NewRelic.Transaction.html

Markdown Content:
NewRelic.Transaction — new_relic v0.2.0
===============

[new_relic](https://hexdocs.pm/new_relic/api-reference.html)

* [Pages](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#full-list)
* [Modules](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#full-list)

* [NewRelic](https://hexdocs.pm/new_relic/NewRelic.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.html#functions)
    * [start/2](https://hexdocs.pm/new_relic/NewRelic.html#start/2)

* [NewRelic.Agent](https://hexdocs.pm/new_relic/NewRelic.Agent.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Agent.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Agent.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Agent.html#functions)
    * [connect/3](https://hexdocs.pm/new_relic/NewRelic.Agent.html#connect/3)
    * [connect_payload/1](https://hexdocs.pm/new_relic/NewRelic.Agent.html#connect_payload/1)
    * [get_redirect_host/0](https://hexdocs.pm/new_relic/NewRelic.Agent.html#get_redirect_host/0)
    * [push/3](https://hexdocs.pm/new_relic/NewRelic.Agent.html#push/3)
    * [push_data/2](https://hexdocs.pm/new_relic/NewRelic.Agent.html#push_data/2)
    * [push_error_data/3](https://hexdocs.pm/new_relic/NewRelic.Agent.html#push_error_data/3)
    * [push_metric_data/3](https://hexdocs.pm/new_relic/NewRelic.Agent.html#push_metric_data/3)
    * [request/2](https://hexdocs.pm/new_relic/NewRelic.Agent.html#request/2)
    * [url/1](https://hexdocs.pm/new_relic/NewRelic.Agent.html#url/1)
    * [url/2](https://hexdocs.pm/new_relic/NewRelic.Agent.html#url/2)

* [NewRelic.Collector](https://hexdocs.pm/new_relic/NewRelic.Collector.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Collector.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Collector.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Collector.html#functions)
    * [child_spec/1](https://hexdocs.pm/new_relic/NewRelic.Collector.html#child_spec/1)
    * [init/1](https://hexdocs.pm/new_relic/NewRelic.Collector.html#init/1)
    * [poll/0](https://hexdocs.pm/new_relic/NewRelic.Collector.html#poll/0)
    * [record_error/2](https://hexdocs.pm/new_relic/NewRelic.Collector.html#record_error/2)
    * [record_value/2](https://hexdocs.pm/new_relic/NewRelic.Collector.html#record_value/2)
    * [start_link/1](https://hexdocs.pm/new_relic/NewRelic.Collector.html#start_link/1)

* [NewRelic.Plug.Instrumentation](https://hexdocs.pm/new_relic/NewRelic.Plug.Instrumentation.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Plug.Instrumentation.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Plug.Instrumentation.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Plug.Instrumentation.html#functions)
    * [instrument_db/4](https://hexdocs.pm/new_relic/NewRelic.Plug.Instrumentation.html#instrument_db/4)

* [NewRelic.Plug.Phoenix](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html#functions)
    * [call/2](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html#call/2)
    * [init/1](https://hexdocs.pm/new_relic/NewRelic.Plug.Phoenix.html#init/1)

* [NewRelic.Plug.Repo](https://hexdocs.pm/new_relic/NewRelic.Plug.Repo.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Plug.Repo.html#content)

* [NewRelic.Poller](https://hexdocs.pm/new_relic/NewRelic.Poller.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Poller.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Poller.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Poller.html#functions)
    * [child_spec/1](https://hexdocs.pm/new_relic/NewRelic.Poller.html#child_spec/1)
    * [init/1](https://hexdocs.pm/new_relic/NewRelic.Poller.html#init/1)
    * [start_link/2](https://hexdocs.pm/new_relic/NewRelic.Poller.html#start_link/2)

* [NewRelic.Statman](https://hexdocs.pm/new_relic/NewRelic.Statman.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Statman.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Statman.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Statman.html#functions)
    * [db_total/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#db_total/1)
    * [errors_total/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#errors_total/1)
    * [pluck/3](https://hexdocs.pm/new_relic/NewRelic.Statman.html#pluck/3)
    * [poll/0](https://hexdocs.pm/new_relic/NewRelic.Statman.html#poll/0)
    * [summary/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#summary/1)
    * [summary/2](https://hexdocs.pm/new_relic/NewRelic.Statman.html#summary/2)
    * [transform_aggregated_metrics/3](https://hexdocs.pm/new_relic/NewRelic.Statman.html#transform_aggregated_metrics/3)
    * [transform_counter/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#transform_counter/1)
    * [transform_error_counter/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#transform_error_counter/1)
    * [transform_histogram/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#transform_histogram/1)
    * [webtransaction_total/1](https://hexdocs.pm/new_relic/NewRelic.Statman.html#webtransaction_total/1)

* [NewRelic.Transaction](https://hexdocs.pm/new_relic/NewRelic.Transaction.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#summary)
  * [Types](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#types)
    * [action/0](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:action/0)
    * [interval/0](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:interval/0)
    * [model/0](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:model/0)
    * [query/0](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:query/0)
    * [t/0](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)

  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#functions)
    * [finish/1](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#finish/1)
    * [record_db/3](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#record_db/3)
    * [start/1](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#start/1)
    * [update_name/2](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#update_name/2)

* [NewRelic.Utils](https://hexdocs.pm/new_relic/NewRelic.Utils.html)
  * [Top](https://hexdocs.pm/new_relic/NewRelic.Utils.html#content)
  * [Summary](https://hexdocs.pm/new_relic/NewRelic.Utils.html#summary)
  * [Functions](https://hexdocs.pm/new_relic/NewRelic.Utils.html#functions)
    * [elixir_environment/0](https://hexdocs.pm/new_relic/NewRelic.Utils.html#elixir_environment/0)
    * [hostname/0](https://hexdocs.pm/new_relic/NewRelic.Utils.html#hostname/0)
    * [utilization/0](https://hexdocs.pm/new_relic/NewRelic.Utils.html#utilization/0)

new_relic v0.2.0 NewRelic.Transaction
=====================================

Records information about an instrumented web transaction.

[Link to this section](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#summary) Summary
==============================================================================================

[Types](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#types)
---------------------------------------------------------------------

[action()](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:action/0)

The name of a repository action.

[interval()](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:interval/0)

Elapsed time in microseconds.

[model()](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:model/0)

The name of a model.

[query()](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:query/0)

The name of a query.

[t()](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)

A New Relixir transaction context.

[Functions](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#functions)
-----------------------------------------------------------------------------

[finish(transaction)](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#finish/1)

Finishes a web transaction.

[record_db(transaction, query, elapsed)](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#record_db/3)

Records a database query for the current web transaction.

[start(name)](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#start/1)

Creates a new web transaction.

[update_name(transaction, new_name)](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#update_name/2)

Updates the name of an existing transaction

[Link to this section](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#types) Types
==========================================================================================

[Link to this type](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:action/0 "Link to this type")
action()
========

action() :: [atom](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

The name of a repository action.

[Link to this type](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:interval/0 "Link to this type")
interval()
==========

interval() :: [non_neg_integer](https://hexdocs.pm/elixir/typespecs.html#basic-types)()

Elapsed time in microseconds.

[Link to this type](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:model/0 "Link to this type")
model()
=======

model() :: [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)()

The name of a model.

[Link to this type](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:query/0 "Link to this type")
query()
=======

query() :: [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)() | {[model](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:model/0)(), [action](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:action/0)()}

The name of a query.

[Link to this opaque](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0 "Link to this opaque")
t()
===

(opaque)

[t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)()

A New Relixir transaction context.

[Link to this section](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#functions) Functions
==================================================================================================

[Link to this function](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#finish/1 "Link to this function")
finish(transaction)
===================

finish([t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)()) :: :ok

Finishes a web transaction.

This method should be called just after processing a web transaction. It will record the elapsed time of the transaction.

[Link to this function](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#record_db/3 "Link to this function")
record_db(transaction, query, elapsed)
======================================

record_db([t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)(), [query](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:query/0)(), [interval](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:interval/0)()) :: :ok

Records a database query for the current web transaction.

The query name can either be provided as a raw string or as a tuple containing a model and action name.

[Link to this function](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#start/1 "Link to this function")
start(name)
===========

start([String.t](https://hexdocs.pm/elixir/String.html#t:t/0)()) :: [t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)()

Creates a new web transaction.

This method should be called just before processing a web transaction.

[Link to this function](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#update_name/2 "Link to this function")
update_name(transaction, new_name)
==================================

update_name([t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)(), [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)()) :: [t](https://hexdocs.pm/new_relic/NewRelic.Transaction.html#t:t/0)()

Updates the name of an existing transaction

This method allows you to specify the name of a transaction after start to facilitate the use case where the transaction name is not known at start time.

Built using [ExDoc](https://github.com/elixir-lang/ex_doc "ExDoc") (v0.21.1),  designed by [Friedel Ziegelmayer](https://twitter.com/dignifiedquire "@dignifiedquire") for the [Elixir programming language](https://elixir-lang.org/ "Elixir").

Toggle night mode Disable tooltips Enable tooltips Display keyboard shortcuts  Go to a HexDocs package

Keyboard Shortcuts

×

c Toggle sidebar n Toggle night mode / or s  Focus search bar g  Go to a HexDocs package ? Bring up this help dialog

Go to a HexDocs package

×
