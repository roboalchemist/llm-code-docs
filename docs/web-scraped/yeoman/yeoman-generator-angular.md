# Source: https://github.com/yeoman/generator-angular

Title: GitHub - yeoman/generator-angular: Yeoman generator for AngularJS

URL Source: https://github.com/yeoman/generator-angular

Markdown Content:
> Yeoman generator for AngularJS - lets you quickly set up a project with sensible defaults and best practices.

There are many starting points for building a new Angular single page app, in addition to this one. You can find other options in this list at [Yeoman.io](http://yeoman.io/generators).

[Roadmap for upcoming plans/features/fixes](https://github.com/yeoman/generator-angular/issues/553)

Usage
-----

[](https://github.com/yeoman/generator-angular#usage)
For step-by-step instructions on using Yeoman and this generator to build a TODO AngularJS application from scratch see [this tutorial.](http://yeoman.io/codelab/)

Install `yo`, `grunt-cli`, `bower`, `generator-angular` and `generator-karma`:

```
npm install -g grunt-cli bower yo generator-karma generator-angular
```

If you are planning on using Sass, you will need to first install Ruby and Compass:

* Install Ruby by downloading from [here](http://rubyinstaller.org/downloads/) or use Homebrew
* Install the compass gem:

```
gem install compass
```

Make a new directory, and `cd` into it:

```
mkdir my-new-project && cd $_
```

Run `yo angular`, optionally passing an app name:

```
yo angular [app-name]
```

Run `grunt` for building and `grunt serve` for preview

Generators
----------

[](https://github.com/yeoman/generator-angular#generators)
Available generators:

* [angular](https://github.com/yeoman/generator-angular#app) (aka [angular:app](https://github.com/yeoman/generator-angular#app))
* [angular:controller](https://github.com/yeoman/generator-angular#controller)
* [angular:directive](https://github.com/yeoman/generator-angular#directive)
* [angular:filter](https://github.com/yeoman/generator-angular#filter)
* [angular:route](https://github.com/yeoman/generator-angular#route)
* [angular:service](https://github.com/yeoman/generator-angular#service)
* [angular:provider](https://github.com/yeoman/generator-angular#service)
* [angular:factory](https://github.com/yeoman/generator-angular#service)
* [angular:value](https://github.com/yeoman/generator-angular#service)
* [angular:constant](https://github.com/yeoman/generator-angular#service)
* [angular:decorator](https://github.com/yeoman/generator-angular#decorator)
* [angular:view](https://github.com/yeoman/generator-angular#view)

### App

[](https://github.com/yeoman/generator-angular#app)
Sets up a new AngularJS app, generating all the boilerplate you need to get started. The app generator also optionally installs Bootstrap and additional AngularJS modules, such as angular-resource (installed by default).

Example:

yo angular

### Route

[](https://github.com/yeoman/generator-angular#route)
Generates a controller and view, and configures a route in `app/scripts/app.js` connecting them.

Example:

yo angular:route myroute

Produces `app/scripts/controllers/myroute.js`:

angular.module('myMod').controller('MyrouteCtrl', function ($scope) {
  // ...
});

Produces `app/views/myroute.html`:

<p>This is the myroute view</p>

**Explicitly provide route URI**

Example:

yo angular:route myRoute --uri=my/route

Produces controller and view as above and adds a route to `app/scripts/app.js` with URI `my/route`

### Controller

[](https://github.com/yeoman/generator-angular#controller)
Generates a controller in `app/scripts/controllers`.

Example:

yo angular:controller user

Produces `app/scripts/controllers/user.js`:

angular.module('myMod').controller('UserCtrl', function ($scope) {
  // ...
});

### Directive

[](https://github.com/yeoman/generator-angular#directive)
Generates a directive in `app/scripts/directives`.

Example:

yo angular:directive myDirective

Produces `app/scripts/directives/myDirective.js`:

angular.module('myMod').directive('myDirective', function () {
  return {
    template: '<div></div>',
    restrict: 'E',
    link: function postLink(scope, element, attrs) {
      element.text('this is the myDirective directive');
    }
  };
});

### Filter

[](https://github.com/yeoman/generator-angular#filter)
Generates a filter in `app/scripts/filters`.

Example:

yo angular:filter myFilter

Produces `app/scripts/filters/myFilter.js`:

angular.module('myMod').filter('myFilter', function () {
  return function (input) {
    return 'myFilter filter:' + input;
  };
});

### View

[](https://github.com/yeoman/generator-angular#view)
Generates an HTML view file in `app/views`.

Example:

yo angular:view user

Produces `app/views/user.html`:

<p>This is the user view</p>

### Service

[](https://github.com/yeoman/generator-angular#service)
Generates an AngularJS service.

Example:

yo angular:service myService

Produces `app/scripts/services/myService.js`:

angular.module('myMod').service('myService', function () {
  // ...
});

You can also do `yo angular:factory`, `yo angular:provider`, `yo angular:value`, and `yo angular:constant` for other types of services.

### Decorator

[](https://github.com/yeoman/generator-angular#decorator)
Generates an AngularJS service decorator.

Example:

yo angular:decorator serviceName

Produces `app/scripts/decorators/serviceNameDecorator.js`:

angular.module('myMod').config(function ($provide) {
    $provide.decorator('serviceName', function ($delegate) {
      // ...
      return $delegate;
    });
  });

Options
-------

[](https://github.com/yeoman/generator-angular#options)
In general, these options can be applied to any generator, though they only affect generators that produce scripts.

### CoffeeScript and TypeScript

[](https://github.com/yeoman/generator-angular#coffeescript-and-typescript)
For generators that output scripts, the `--coffee` option will output CoffeeScript instead of JavaScript, and `--typescript` will output TypeScript instead of JavaScript.

For example:

yo angular:controller user --coffee

Produces `app/scripts/controller/user.coffee`:

angular.module('myMod')
  .controller 'UserCtrl', ($scope) ->

For example:

yo angular:controller user --typescript

Produces `app/scripts/controller/user.ts`:

/// <reference path="../app.ts" />

'use strict';

module demoApp {
    export interface IUserScope extends ng.IScope {
        awesomeThings: any[];
    }

    export class UserCtrl {

        constructor (private $scope:IUserScope) {
         $scope.awesomeThings = [
              'HTML5 Boilerplate',
              'AngularJS',
              'Karma'
            ];
        }
    }
}

angular.module('demoApp')
  .controller('UserCtrl', demoApp.UserCtrl);

### Minification Safe

[](https://github.com/yeoman/generator-angular#minification-safe)
**tl;dr**: You don't need to write annotated code as the build step will handle it for you.

By default, generators produce unannotated code. Without annotations, AngularJS's DI system will break when minified. Typically, these annotations that make minification safe are added automatically at build-time, after application files are concatenated, but before they are minified. The annotations are important because minified code will rename variables, making it impossible for AngularJS to infer module names based solely on function parameters.

The recommended build process uses `ng-annotate`, a tool that automatically adds these annotations. However, if you'd rather not use it, you have to add these annotations manually yourself. Why would you do that though? If you find a bug in the annotated code, please file an issue at [ng-annotate](https://github.com/olov/ng-annotate/issues).

### Add to Index

[](https://github.com/yeoman/generator-angular#add-to-index)
By default, new scripts are added to the index.html file. However, this may not always be suitable. Some use cases:

* Manually added to the file
* Auto-added by a 3rd party plugin
* Using this generator as a subgenerator

To skip adding them to the index, pass in the skip-add argument:

yo angular:service serviceName --skip-add

Bower Components
----------------

[](https://github.com/yeoman/generator-angular#bower-components)
The following packages are always installed by the [app](https://github.com/yeoman/generator-angular#app) generator:

* angular
* angular-mocks

The following additional modules are available as components on bower, and installable via `bower install`:

* angular-animate
* angular-aria
* angular-cookies
* angular-messages
* angular-resource
* angular-sanitize

All of these can be updated with `bower update` as new versions of AngularJS are released.

`json3` and `es5-shim` have been removed as Angular 1.3 has dropped IE8 support and that is the last version that needed these shims. If you still require these, you can include them with: `bower install --save json3 es5-shim`. `wiredep` should add them to your index.html file but if not you can manually add them.

Configuration
-------------

[](https://github.com/yeoman/generator-angular#configuration)
Yeoman generated projects can be further tweaked according to your needs by modifying project files appropriately.

### Output

[](https://github.com/yeoman/generator-angular#output)
You can change the `app` directory by adding an `appPath` property to `bower.json`. For instance, if you wanted to easily integrate with Express.js, you could add the following:

{
  "name": "yo-test",
  "version": "0.0.0",
  ...
  "appPath": "public"
}

This will cause Yeoman-generated client-side files to be placed in `public`.

Note that you can also achieve the same results by adding an `--appPath` option when starting generator:

yo angular [app-name] --appPath=public

Testing
-------

[](https://github.com/yeoman/generator-angular#testing)
Running `grunt test` will run the unit tests with karma.

Contribute
----------

[](https://github.com/yeoman/generator-angular#contribute)
See the [contributing docs](https://github.com/yeoman/yeoman/blob/master/contributing.md)

When submitting an issue, please follow the [guidelines](https://github.com/yeoman/yeoman/blob/master/contributing.md#issue-submission). Especially important is to make sure Yeoman is up-to-date, and providing the command or commands that cause the issue.

When submitting a PR, make sure that the commit messages match the [AngularJS conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/).

When submitting a bugfix, write a test that exposes the bug and fails before applying your fix. Submit the test alongside the fix.

When submitting a new feature, add tests that cover the feature.

Changelog
---------

[](https://github.com/yeoman/generator-angular#changelog)
Recent changes can be viewed on Github on the [Releases Page](https://github.com/yeoman/generator-angular/releases)

Sponsors
--------

[](https://github.com/yeoman/generator-angular#sponsors)
Love Yeoman work and community? Help us keep it alive by donating funds to cover project expenses!

 [[Become a sponsor](https://opencollective.com/yeoman#support)]

[![Image 1](https://camo.githubusercontent.com/848cf8ce3e5d2d56ee7b1234b402f039115954d0be595d42dd580b9b85fcb34b/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f302f617661746172)](https://opencollective.com/yeoman/backers/0/website)[![Image 2](https://camo.githubusercontent.com/6f60f930b2ed521802ca7ed4df2ef51a35fab44ab1eb074a9f51096b2231bd1c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f312f617661746172)](https://opencollective.com/yeoman/backers/1/website)[![Image 3](https://camo.githubusercontent.com/30bbb41d9d344beec5ecb272c43361c8c48c169585d40367a15076243d6329a2/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f322f617661746172)](https://opencollective.com/yeoman/backers/2/website)[![Image 4](https://camo.githubusercontent.com/a37fe87954fcf7a724d1e453d30136b37c23e5eac85bf8cb20315bf5eddc91c7/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f332f617661746172)](https://opencollective.com/yeoman/backers/3/website)[![Image 5](https://camo.githubusercontent.com/15f03d20dc8b43665398ad5bc8fcc26bd40e4e4a0f3f6a2b2673374b37cd31c2/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f342f617661746172)](https://opencollective.com/yeoman/backers/4/website)[![Image 6](https://camo.githubusercontent.com/3b80c444b3b35c01dc599145756f1b5c4f5a53ff1840285a02ba8689dce32301/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f352f617661746172)](https://opencollective.com/yeoman/backers/5/website)[![Image 7](https://camo.githubusercontent.com/dc3d821721acd82b247706cd662aad46005d63a981dce63e739d8b675ab43c23/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f362f617661746172)](https://opencollective.com/yeoman/backers/6/website)[![Image 8](https://camo.githubusercontent.com/2229d4dce59975695337d188bdfda71a5297dde4bf37992c819789f1cfa77a18/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f372f617661746172)](https://opencollective.com/yeoman/backers/7/website)[![Image 9](https://camo.githubusercontent.com/51a982c4436f0d787687f2bf22d77437c742af14a89a07fb95c468b7f35642d9/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f382f617661746172)](https://opencollective.com/yeoman/backers/8/website)[![Image 10](https://camo.githubusercontent.com/e59bb5fdcca235b6f1ed7f904360bf8de0d04dcd167d010bde6363a8e078f8a1/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f392f617661746172)](https://opencollective.com/yeoman/backers/9/website)[![Image 11](https://camo.githubusercontent.com/0a5ef79677a2bb402bff349e5798dd016c0241e30776c8ff48d5b112367a8a88/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31302f617661746172)](https://opencollective.com/yeoman/backers/10/website)[![Image 12](https://camo.githubusercontent.com/e88c2155124870f9d18f4e0a086bbf5e7a2a7d855d8f8ed06305fe76a4042db1/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31312f617661746172)](https://opencollective.com/yeoman/backers/11/website)[![Image 13](https://camo.githubusercontent.com/5381ea66cb23771a8733cd193e200e12d756226b5e5e0eb0bce62200d05a307e/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31322f617661746172)](https://opencollective.com/yeoman/backers/12/website)[![Image 14](https://camo.githubusercontent.com/95904f8a05624ecdea918b0a3374e42e685e368cbac0c5e1f29c70e9e0061253/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31332f617661746172)](https://opencollective.com/yeoman/backers/13/website)[![Image 15](https://camo.githubusercontent.com/97303bf86bf8a1a17bfb7a64b9996a98651c41b7d59594636a93685e6609a689/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31342f617661746172)](https://opencollective.com/yeoman/backers/14/website)[![Image 16](https://camo.githubusercontent.com/34a69976f6acdb3be6acbf90720d80f2801a02d8471f58b0d9ecdf2442bcacd7/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31352f617661746172)](https://opencollective.com/yeoman/backers/15/website)[![Image 17](https://camo.githubusercontent.com/42f3ca6736f106dbfb6b2b22afaef77ec120ccbb1e639970ef9c7fe755467baa/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31362f617661746172)](https://opencollective.com/yeoman/backers/16/website)[![Image 18](https://camo.githubusercontent.com/178af4c57f2aa0de530cad60a13e444b5d1ff31e6d848442d0aef2c7dae696ad/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31372f617661746172)](https://opencollective.com/yeoman/backers/17/website)[![Image 19](https://camo.githubusercontent.com/f4063cdf70b78233c94ce414f2ec52f758010fe8d5952aa6669acda35381a441/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31382f617661746172)](https://opencollective.com/yeoman/backers/18/website)[![Image 20](https://camo.githubusercontent.com/671dc4ff4326f5172e8553cc0f09be1d6b871f83705327db23abfaa0e3acce7e/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f31392f617661746172)](https://opencollective.com/yeoman/backers/19/website)[![Image 21](https://camo.githubusercontent.com/bee5c9b65254012d9e75b1acb64f6974065b2234471cf345605b63627042d2f8/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32302f617661746172)](https://opencollective.com/yeoman/backers/20/website)[![Image 22](https://camo.githubusercontent.com/1f52df869a220e72da205f4aaeda20d8415248a92da66e38253dddf0cf78ec6a/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32312f617661746172)](https://opencollective.com/yeoman/backers/21/website)[![Image 23](https://camo.githubusercontent.com/c10c52d14f9558095b5bd3785a1e6949551e3e4e54a44a850f6e18160c028c86/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32322f617661746172)](https://opencollective.com/yeoman/backers/22/website)[![Image 24](https://camo.githubusercontent.com/0aa8e4d1345446c55af1257d538f3afabcdf33f77733bdb2363337aae7f57111/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32332f617661746172)](https://opencollective.com/yeoman/backers/23/website)[![Image 25](https://camo.githubusercontent.com/86a3a97d9e8f22125f90148817c1e5173c261e684218271d14b8cda50b87067a/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32342f617661746172)](https://opencollective.com/yeoman/backers/24/website)[![Image 26](https://camo.githubusercontent.com/bb095ff722a3f2951176b8796407234924bb6140b070d333705a99b3bb262dde/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32352f617661746172)](https://opencollective.com/yeoman/backers/25/website)[![Image 27](https://camo.githubusercontent.com/0bc85ba810745d652e5445e51f762d3dc1ff7cb9d8cb1b05d2793680f7d65699/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32362f617661746172)](https://opencollective.com/yeoman/backers/26/website)[![Image 28](https://camo.githubusercontent.com/f06a93565f16d98b0290ae5cd78538266e992cf6372884781f20020f60c3065f/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32372f617661746172)](https://opencollective.com/yeoman/backers/27/website)[![Image 29](https://camo.githubusercontent.com/0a07738dbc301dbe71cc79882aae95cd9830a03da968bf2a1248d69abeb9e5ae/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32382f617661746172)](https://opencollective.com/yeoman/backers/28/website)[![Image 30](https://camo.githubusercontent.com/2485d38879da4f309e3b3669f835e608515c74998c119a49507c99a92b20920c/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f79656f6d616e2f6261636b6572732f32392f617661746172)](https://opencollective.com/yeoman/backers/29/website)
License
-------

[](https://github.com/yeoman/generator-angular#license)
[BSD license](http://opensource.org/licenses/bsd-license.php)
