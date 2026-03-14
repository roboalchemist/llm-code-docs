# Source: https://docs.statsig.com/client/Angular.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Statsig in Angular

> Statsig's SDK for Experimentation and Feature Flags in Angular applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    <CodeGroup>
      ```bash npm theme={null}
      npm install @statsig/angular-bindings
      ```

      ```bash yarn theme={null}
      yarn add @statsig/angular-bindings
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    The Statsig Angular bindings package provides a `StatsigService` that can be injected into your components. The way you provide and inject this service can vary depending on how you structure your app.

    ```ts  theme={null}
    import { STATSIG_INIT_CONFIG } from '@statsig/angular-bindings';

    const StatsigConfig = {
            sdkKey: "client-KEY",
            user: {}, // initial user object
            options: {...} // optional
    }
    ```

    ### using app config

    ```ts  theme={null}
    // app.config.ts
    import { ApplicationConfig } from '@angular/core';
    import { STATSIG_INIT_CONFIG } from '@statsig/angular-bindings';

    export const appConfig: ApplicationConfig = {
      providers: [
        {
          provide: STATSIG_INIT_CONFIG,
          useValue: StatsigConfig,
        },
      ],
    };

    //main.ts
    import { AppComponent } from './app/app.component';
    import { appConfig } from './app/app.config';

    bootstrapApplication(AppComponent, appConfig).catch((err) =>
      console.error(err),
    );
    ```

    ### using app module

    ```ts  theme={null}
    // app.module.ts
    import { StatsigService } from '@statsig/angular-bindings';
    import { AppComponent } from './app.component';

    @NgModule({
      declarations: [AppComponent],
      imports: [],
      providers: [
        {
          provide: STATSIG_INIT_CONFIG,
          useValue: StatsigConfig,
        },
      ],
      bootstrap: [AppComponent],
    })
    export class AppModule {}
    ```
  </Step>
</Steps>

## Use the SDK

Once you have provided the statsig config token, you can now inject the service into a component or another service and use it.

```ts  theme={null}
// example.component.ts
import { Component } from '@angular/core';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  selector: 'app-example',
  template: `...`,
})
export class ExampleComponent {
  constructor(private statsigService: StatsigService) {}
}
```

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```ts  theme={null}
// feature-gate.component.ts
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  standalone: true,
  selector: 'app-feature-gate',
  imports: [CommonModule],
  template: `<div *ngIf="isFeatureEnabled">Feature is enabled!</div>`,
})
export class FeatureGateComponent implements OnInit {
  isFeatureEnabled = false;

  constructor(private statsigService: StatsigService) {}

  ngOnInit(): void {
    this.isFeatureEnabled = this.statsigService.checkGate('feature_gate_name');
  }
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```ts  theme={null}
// dynamic-config.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  standalone: true,
  selector: 'app-dynamic-config',
  imports: [CommonModule],
  template: `<div *ngIf="configValue">Config Value: {{ configValue }}</div>`,
})
export class DynamicConfigComponent implements OnInit {
  configValue: string | null = null;

  constructor(private statsigService: StatsigService) {}

  ngOnInit(): void {
    const dynamicConfig = this.statsigService.getDynamicConfig('config_name');
    this.configValue = dynamicConfig.get('key', 'default_value');
  }
}
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```ts  theme={null}
// experiment.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  standalone: true,
  selector: 'app-experiment',
  imports: [CommonModule],
  template: `<div *ngIf="experimentValue">Experiment Value: {{ experimentValue }}</div>`,
})
export class ExperimentComponent implements OnInit {
  experimentValue: string | null = null;

  constructor(private statsigService: StatsigService) {}

  ngOnInit(): void {
    const experiment = this.statsigService.getExperiment('experiment_name');
    this.experimentValue = experiment.get('experiment_key', 'default');
  }
}
```

```ts  theme={null}
// layer.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  standalone: true,
  selector: 'app-layer',
  imports: [CommonModule],
  template: `<div *ngIf="layerValue">Layer Value: {{ layerValue }}</div>`,
})
export class LayerComponent implements OnInit {
  layerValue: string | null = null;

  constructor(private statsigService: StatsigService) {}

  ngOnInit(): void {
    const layer = this.statsigService.getLayer('layer_name');
    this.layerValue = layer.get('layer_key', 'default_layer_value');
  }
}
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```ts  theme={null}
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  standalone: true,
  selector: 'app-log-event',
  imports: [CommonModule],
  template: `
    <button (click)="logUserAction()">Click Me</button>
    <p *ngIf="message">{{ message }}</p>
  `,
})
export class LogEventComponent {
  message: string | null = null;

  constructor(private statsigService: StatsigService) {}

  logUserAction(): void {
    this.statsigService.logEvent('UserClickedButton', 1, {
      buttonColor: 'blue',
      buttonText: 'Click Me',
    });

    this.message = 'Event logged: UserClickedButton';
  }
}
```

## Updating user properties (e.g., Login)

Sometimes you'll need to update user properties, say when the user logs in and a userID is assigned, or a set of new properties have been identified. This would require Statsig to go fetch new values for all the gates, experiments and config evaluations. This is achieved by the calling `updateUserAsync` from the service:

```ts  theme={null}
import { Component } from '@angular/core';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  selector: 'app-user-update',
  template: `
    <button (click)="updateUser()">Update User</button>
  `,
})
export class UserUpdateComponent {
  constructor(private statsigService: StatsigService) {}

  updateUser(): void {
    const user = {
      userID: 'user-1234',
      email: 'user@example.com',
      // Add other user properties here
    };

    this.statsigService.updateUserAsync(user)
      .then(() => {
        console.log('User updated successfully');
      })
      .catch((error) => {
        console.error('Error updating user:', error);
      });
  }
}
```

## Loading State

Dependent on your setup, you may want to wait for the latest values before checking a gate or experiment.
You can use the `isLoading` observable to determine if the SDK is still loading and display a loading state.

```ts  theme={null}
import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { StatsigService } from '@statsig/angular-bindings';

@Component({
  selector: 'app-loading-state',
  imports: [CommonModule],
  template: `
    <div *ngIf="isLoading | async; else content">
      <p>Loading...</p>
    </div>
    <ng-template #content>
      <p>Content loaded successfully!</p>
    </ng-template>
  `,
})
export class LoadingStateComponent implements OnInit {
  isLoading = this.statsigService.isLoading$;

  constructor(private statsigService: StatsigService) {}

  ngOnInit(): void {
    // other initialization logic here
  }
}
```

## Angular Directives

### Statsig Module

To use the directives, you need to import the `StatsigModule` in your Angular module.

```ts  theme={null}
// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { StatsigModule } from '@statsig/angular-bindings';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, StatsigModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

### Check gate directive

The stgCheckGate directive allows you to conditionally display content in your Angular templates based on the evaluation of a Feature Gate from Statsig. It listens for updates to the feature gate's value and dynamically adds or removes content based on whether the gate is enabled or not.

```ts  theme={null}
// feature-demo.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-feature-demo',
  template: `
    <div *stgCheckGate="'new_feature_gate'">
      <p>This content will only show if the 'new_feature_gate' is enabled.</p>
    </div>
  `,
})
export class FeatureDemoComponent {}
```

## Session Replay

By including the [`@statsig/session-replay`](https://www.npmjs.com/package/@statsig/session-replay) package in your project, you can automatically capture and log user sessions as videos.
This feature is useful for debugging and understanding user behavior. Read more about [Session Replay](/session-replay/overview).

```ts  theme={null}
import { STATSIG_INIT_CONFIG } from '@statsig/angular-bindings';
import { StatsigSessionReplayPlugin } from '@statsig/session-replay';

const StatsigConfig = {
        sdkKey: "client-KEY",
        user: { userID: 'a-user' },
        options: { plugins: [ new StatsigSessionReplayPlugin() ] }
}
```

## Web Analytics / Auto Capture

By including the [`@statsig/web-analytics`](https://www.npmjs.com/package/@statsig/web-analytics) package in your project, you can automatically capture common web events like clicks and page views.

For more information on filtering events, enabling console log capture, and other configuration options available in web analytics, see the [Web Analytics Configuration](/webanalytics/overview#event-filtering-and-console-configuration) documentation.

```ts  theme={null}
import { STATSIG_INIT_CONFIG } from '@statsig/angular-bindings';
import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

const StatsigConfig = {
        sdkKey: "client-KEY",
        user: { userID: 'a-user' },
        options: { plugins: [ new StatsigAutoCapturePlugin() ] }
}
```


Built with [Mintlify](https://mintlify.com).