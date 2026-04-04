# Source: https://docs.logrocket.com/reference/ngrx-middleware-1.md

# NgRx Middleware

The `logrocket-ngrx` package augments LogRocket sessions by including actions and state from your [NgRx](https://github.com/ngrx/platform) store. The middleware is compatible with NgRx v4+.

![858](https://files.readme.io/610d6a7-687474703a2f2f692e696d6775722e636f6d2f696147547837412e706e67.png "687474703a2f2f692e696d6775722e636f6d2f696147547837412e706e67.png")

To use LogRocket with Angular and NgRx, first install `logrocket` and the `logrocket-ngrx` middleware:

```shell
npm i --save logrocket logrocket-ngrx
```

Initialize LogRocket in your app's root component:

```typescript app.component.ts
import { Component } from '@angular/core';

import * as LogRocket from 'logrocket';

// substitute your LogRocket appID here
LogRocket.init('your/appID');

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'yourApp';
}
```

Then, in your root module, inject the `logrocket-ngrx` middleware with a `Provider` using the `USER_PROVIDED_META_REDUCERS` injection token. [Registering middleware via dependency injection](https://ngrx.io/guide/store/recipes/injecting#injecting-meta-reducers) helps avoid issues with AOT compilation.

```typescript app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { StoreModule, MetaReducer, USER_PROVIDED_META_REDUCERS } from '@ngrx/store';
import * as LogRocket from 'logrocket';
import createNgrxMiddleware from 'logrocket-ngrx';

import { AppComponent } from './app.component';
import { State, reducers, metaReducers } from './reducers';

// options is the same object you would pass to LogRocket.reduxMiddleware()
const logrocketMiddleware = createNgrxMiddleware(LogRocket, options);

export function getMetaReducers(): MetaReducer<State>[] {
  return metaReducers.concat([logrocketMiddleware]);
}

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    StoreModule.forRoot(reducers),
  ],
  providers: [
    {
      provide: USER_PROVIDED_META_REDUCERS,
      useFactory: getMetaReducers,
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

`createNgrxMiddleware()` supports the same configuration `options` as [reduxMiddleware()](https://docs.logrocket.com/reference/redux-logging).

> 📘 Session Filtering
>
> This plugin is implemented by wrapping our Redux middleware. You can filter over sessions containing NgRx state changes using the  **Redux Action Type** filter. Actions and state appear under the **Redux** label in the session view's log entry pane.