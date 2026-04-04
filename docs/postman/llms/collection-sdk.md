# collection-sdk

Create and manage collections using the Collection SDK | Postman Docs
===============

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK to automate part of your collection run workflow, you can integrate your Collection SDK development with the Postman CLI or with Newman.

* To learn more about integrating your Collection SDK development with the Postman CLI, visit [Explore Postman's command-line companion](/docs/postman-cli/postman-cli-overview/).
* To learn more about running collections with Newman, visit [Run and test collections from the command line using Newman CLI](/docs/collections/using-newman-cli/command-line-integration-with-newman/).

---

Create and manage collections using the Collection SDK
====================================================

The Collection SDK is a Node.js module that enables you to work with Postman [Collections](/docs/sending-requests/create-requests/intro-to-collections/) and build them dynamically into your API project pipeline.

With the Collection SDK, you can create and manipulate, and export collections. You can then run them with the [Postman CLI](/docs/postman-cli/postman-cli-overview/) and the [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) command-line collection runner.

## Accessing the Collection SDK

The Collection SDK is an open-source project. [Visit the repo](https://github.com/postmanlabs/postman-collection) for more detail on using the module in your own projects. The [SDK documentation](http://www.postmanlabs.com/postman-collection/) provides an overview of the available objects and methods within the SDK, and an intro to the related [concepts](http://www.postmanlabs.com/postman-collection/tutorial-concepts.html).

You can install the SDK from [npm](https://www.npmjs.com/package/postman-collection) or directly from the repo. The following excerpt demonstrates using the SDK to read a file and parse it into a collection object in JavaScript:

```js
var fs = require('fs'),
  Collection = require('postman-collection').Collection,
  myCollection;
myCollection = new Collection(JSON.parse
  (fs.readFileSync('sample-collection.json').toString()));
console.log(myCollection.toJSON());
```

The Collection SDK provides an interface for working with the data structures defined by the [Postman Collection Schema](https://schema.postman.com/). You can use the SDK methods to create and manipulate collection elements, define request detail, variables, and authentication.

Get started with the Collection SDK from the [project repo](https://github.com/postmanlabs/postman-collection), installing it and using the methods to build collections in a way that suits your development or testing project. You can also fork and contribute to the project, or create issues for any problems or feature requests.

## Next steps

If you're working with the Collection SDK