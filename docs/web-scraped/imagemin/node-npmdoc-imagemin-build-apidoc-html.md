# Source: https://npmdoc.github.io/node-npmdoc-imagemin/build/apidoc.html

Title: 

URL Source: https://npmdoc.github.io/node-npmdoc-imagemin/build/apidoc.html

Published Time: Tue, 18 Apr 2017 18:33:12 GMT

Markdown Content:
[module imagemin](https://npmdoc.github.io/node-npmdoc-imagemin/build/apidoc.html#apidoc.module.imagemin)
---------------------------------------------------------------------------------------------------------

[function imagemin (input, output, opts)](https://npmdoc.github.io/node-npmdoc-imagemin/build/apidoc.html#apidoc.element.imagemin.imagemin)
-------------------------------------------------------------------------------------------------------------------------------------------

*   description and source-code(input, output, opts) => {
	if (!Array.isArray(input)) {
		return Promise.reject(new TypeError('Expected an array'));
	}

	if (typeof output === 'object') {
		opts = output;
		output = null;
	}

	opts = Object.assign({plugins: []}, opts);
	opts.plugins = opts.use || opts.plugins;

	return globby(input, {nodir: true}).then(paths => Promise.all(paths.map(x => handleFile(x, output, opts))));
}
*   example usage n/a

[function imagemin.buffer (input, opts)](https://npmdoc.github.io/node-npmdoc-imagemin/build/apidoc.html#apidoc.element.imagemin.buffer)
----------------------------------------------------------------------------------------------------------------------------------------

*   description and source-code(input, opts) => {
	if (!Buffer.isBuffer(input)) {
		return Promise.reject(new TypeError('Expected a buffer'));
	}

	opts = Object.assign({plugins: []}, opts);
	opts.plugins = opts.use || opts.plugins;

	const pipe = opts.plugins.length > 0 ? promisePipe(opts.plugins)(input) : Promise.resolve(input);

	return pipe.then(buf => buf.length < input.length ? buf : input);
}
*   example usage...

##### plugins

Type: `array`

Array of [plugins](https://www.npmjs.com/browse/keyword/imageminplugin) to use.

### imagemin.buffer(buffer, [options])

Returns a promise for a buffer.

#### buffer

Type: `buffer`
...
