# Source: https://docs.logrocket.com/reference/mobx.md

# MobX

The LogRocket MobX plugin allows you to logs changes to a single MobX observable.

![1698](https://files.readme.io/24b2b1a-Screen_Shot_2018-08-03_at_2.45.47_PM.png "Screen Shot 2018-08-03 at 2.45.47 PM.png")

## Installation

1. Install the LogRocket MobX plugin from NPM:
2. Be sure you have installed the peer dependencies (mobx\@5 and logrocket)

Typescript definition files are [included in the package](https://unpkg.com/logrocket-mobx@2.0.2/dist/types/plugin.d.ts).

```shell
npm i --save logrocket-mobx
```

> 🚧 Using MobX v3?
>
> If you are using MobX v3 use the [logrocket-mobx@0.1.5](mailto:logrocket-mobx@0.1.5) version. We do not support MobX v4.

## Usage

Setup

```javascript
import createPlugin from 'logrocket-mobx';
import { observable } from 'mobx';


// hook up the plugin to LogRocket
const lr = createPlugin(LogRocket);

// lr object contains 4 functions
lr.watchValue(target, options) // target is a boxed value
lr.watchArray(target, options)
lr.watchObject(target, options)
lr.watchObject(target, property, options) // watch a specific property
lr.watchMap(target, options)
lr.watchMap(target, key, options) // watch a specific key
// target must be a MobX observable

// options object has two optional properties:
// name: String  (optional string to identify the observable in LogRocket)
// sanitizer: change => change (optional sanitizer function which receives and returns the change object
```

The plugin is implemented by calling [MobX's observe function](https://mobx.js.org/refguide/observe.html#observe) on the target observable and logging to logrocket the changes. The logs will appear in the sessions recording's log pane but not your local console tab. You can provide an optional identifier string and a sanitizer function if you wish.

> 🚧 Session Filtering
>
> There currently is no way to filter over sessions containing a given MobX observable change. They will appear as log entries in your session.

##