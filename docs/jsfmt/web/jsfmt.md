# Source: http://rdio.github.io/jsfmt/

Title: For formatting, searching, and rewriting javascript

URL Source: http://rdio.github.io/jsfmt/

Markdown Content:
jsfmt
-----

### Formatting to help keep your code neat.

					
```
# Format `source.js` and print the results to stdout.
jsfmt source.js

# Format `source.js` and write the results to disk.
jsfmt -w=true source.js

# View a diff of all formatting changes in `source.js` without writing them.
jsfmt -d=true source.js

# List all files that need formatting in the `src/` directory.
# Directories are recursively traversed.
jsfmt -l=true -w=false src/
```

				

### Searching to smartly find patterns.

					
```
# Find all instances of _.reduce() in `source.js`.
# Single letter identifiers act as wildcards, and whitespace is ignored.
jsfmt --search="_.reduce(a, b, c)" source.js

# Find all calls to console.log() in your project's `src/` directory.
jsfmt --search="console.log(s)" src/
```

				

### Rewriting for easy cleaning and refactoring.

					
```
# Replace underscore.js's reduce with the native reduce method in `source.js`.
jsfmt --rewrite="_.reduce(a, b, c) -> a.reduce(b, c)" source.js

# Do it again, but this time save the changes to disk.
jsfmt --write=true --rewrite="_.reduce(a, b, c) -> a.reduce(b, c)" source.js

# Replace modulo with an expression that always returns a positive number, and run the results.
jsfmt --rewrite="x % y -> ((x % y) + y) % y" source.js | node
```

				

#### Intelligent

Built on [esprima](http://esprima.org/) and [esformatter](https://github.com/millermedeiros/esformatter) for smart code parsing and formatting. Jsfmt works on your code's [AST](http://en.wikipedia.org/wiki/Abstract_syntax_tree), not just on its text.

#### Full API

You can `require` jsfmt from any node app. Every feature available through the command line is also available through its module. Check [our docs](https://github.com/rdio/jsfmt) for more information.

#### Active Development

Jsfmt is currently in development, and is constantly changing and improving. Follow along [on Github](https://github.com/rdio/jsfmt), and feel free to report bugs or request features [here.](https://github.com/rdio/jsfmt/issues?state=open)
