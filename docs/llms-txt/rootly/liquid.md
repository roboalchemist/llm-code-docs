# Source: https://docs.rootly.com/liquid/liquid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Learn how to use the Liquid templating engine in Rootly workflows to dynamically manipulate data, format content, and create powerful automation expressions.

Rootly supports the use of the [Liquid](https://shopify.github.io/liquid/ "Liquid") templating engine in Workflows Tasks. Liquid provides a number of useful filters which can be used to manipulate the contents of options blocks. For example, the expression `{{ 'hello' | upcase }}` uses the upcase filter, when inserted into an options block it will render HELLO. You can string multiple Liquid filters together, with the expression processed left-to-right.

<Note>
  You can find our variables on the following pages:

  * [Incident Variables](/liquid/incident-variables)﻿﻿

  * [Action Item Variables](/liquid/action-item-variables)﻿﻿

  * [Alert Variables](/liquid/alert-variables)﻿﻿

  * [Pulse Variables](/liquid/pulse-variables) ﻿﻿
</Note>

## Examples[](#641mI)

### Get the Current Date and Time in yyyymmdd Format[](#DMtCh)

Expression: `{{ "now" | date: "%Y-%m-%d" }}`

Sample result: "2018-04-24"

[Reference](https://shopify.github.io/liquid/filters/date/ "Reference")

### Get the Size of an Array and Multiply by 10[](#5FRvZ)

Expression: `{{ .my_array | size | times: 10 }}`

Sample result: 50

[Reference](https://shopify.github.io/liquid/filters/size/ "Reference")

## Full List of Available Filters[](#eLdDh)

[Available filters](/liquid/filters)


Built with [Mintlify](https://mintlify.com).