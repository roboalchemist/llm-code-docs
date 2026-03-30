# Source: https://docs.ghost.org/themes/helpers/data/total_paid_members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# total_paid_members

> Usage: `{{total_paid_members}}`

***

The total\_paid\_members helper outputs a rounded number of total paid members from your Ghost publication in a human readable format. Example:

```handlebars  theme={"dark"}
{{total_paid_members}}
```

If you have 1225 paying members, it will output `1,200+`.

For values above 100,000 it will output `100k+` and `3m+` respectively.


Built with [Mintlify](https://mintlify.com).