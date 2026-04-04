# Source: https://docs.ghost.org/themes/helpers/utility/reading_time.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# reading_time

> Usage: `{{reading_time}}`

***

`{{reading_time}}` renders the estimated reading time for a post.

The helper counts the words in the post and calculates an average reading time of 275 words per minute. For the first image present, 12s is added, for the second 11s is added, for the third 10, and so on. From the tenth image onwards every image adds 3s.

By *default* the helper will render a text like this:

* `x min read` for estimated reading time longer than one minute
* `1 min read` for estimated reading time shorter than or equal to one minute

You can override the default text.

### Example Code

```handlebars  theme={"dark"}
{{#post}}
    {{reading_time}}
{{/post}}
```

## Custom labelling

Singular minute and plural minutes labelling can be customised using the options `minute` and `minutes`, using `%` as the plural minutes value.

### Example

```handlebars  theme={"dark"}
{{reading_time minute="Only a minute" minutes="Takes % minutes"}}
```

[See our full tutorial](https://ghost.org/tutorials/reading-time/) on how to customise and build upon the `reading_time` Handlebars helper.


Built with [Mintlify](https://mintlify.com).