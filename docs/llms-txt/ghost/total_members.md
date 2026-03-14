# Source: https://docs.ghost.org/themes/helpers/data/total_members.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# total_members

> Usage: `{{total_members}}`

***

The total\_members helper outputs a rounded number of total members from your Ghost publication in a human readable format. Example:

```handlebars  theme={"dark"}
{{total_members}}
```

If you have 1225 members, it will output `1,200+`.

For values above 100,000 it will output `100k+` and `3m+` respectively.


Built with [Mintlify](https://mintlify.com).