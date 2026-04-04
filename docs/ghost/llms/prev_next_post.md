# Source: https://docs.ghost.org/themes/helpers/utility/prev_next_post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# prev_post & next_post

> Usage: `{{#prev_post}}{{title}}{{/prev_post}}` - `{{#next_post}}{{title}}{{/next_post}}`

***

When in the scope of a post, you can call the next or previous post helper, which performs a query against the API to fetch the next or previous post in accordance with the chronological order of the site.

Inside of the opening and closing tags of the `{{#next_post}}{{/next_post}}` or `{{#prev_post}}{{/prev-post}}` helper, the normal helpers for outputting posts will work, but will output the details of the post that was fetched from the API, rather than the original post.

```handlebars  theme={"dark"}
{{#post}}
	{{#prev_post}}
		<a href="{{url}}">{{title}}</a>
	{{/prev_post}}

	{{#next_post}}
		<a href="{{url}}">{{title}}</a>
	{{/next_post}}
{{/post}}
```

You can also scope where to pull the previous and next posts from using the `in` parameter

```handlebars  theme={"dark"}
{{#post}}
	{{#prev_post in="primary_tag"}}
		<a href="{{url}}">{{title}}</a>
	{{/prev_post}}

	{{#next_post in="primary_tag"}}
		<a href="{{url}}">{{title}}</a>
	{{/next_post}}
{{/post}}
```


Built with [Mintlify](https://mintlify.com).