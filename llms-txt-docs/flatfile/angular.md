# Source: https://flatfile.com/docs/embedding/angular.md

# Angular Embedding

> Embed Flatfile in Angular applications

Embed Flatfile in your Angular application using our Angular SDK. This provides Angular components and services for seamless integration.

## Installation

```bash
npm install @flatfile/angular-sdk
```

## Basic Implementation

### 1. Import the Module

Add the `SpaceModule` to your Angular module:

```typescript
import { NgModule } from "@angular/core";
import { SpaceModule } from "@flatfile/angular-sdk";

@NgModule({
  imports: [
    SpaceModule,
    // your other imports
  ],
  // ...
})
export class AppModule {}
```

### 2. Create Component

Create a component to handle the Flatfile embed:

```typescript
import { Component } from "@angular/core";
import { SpaceService, ISpace } from "@flatfile/angular-sdk";

@Component({
  selector: "app-import",
  template: `
    <div>
      <h1>Welcome to our app</h1>
      <button (click)="openFlatfile()">Import Data</button>
    </div>
  `,
})
export class ImportComponent {
  constructor(private spaceService: SpaceService) {}

  spaceProps: ISpace = {
    publishableKey: "pk_your_publishable_key",
    displayAsModal: true,
  };

  openFlatfile() {
    this.spaceService.OpenEmbed(this.spaceProps);
  }
}
```

### 3. Get Your Credentials

**publishableKey**: Get from [Platform Dashboard](https://platform.flatfile.com) → Developer Settings

**Authentication & Security**: For production applications, implement proper authentication and space management on your server. See [Advanced Configuration](./advanced-configuration) for authentication guidance.

## Complete Example

<Note>
  The example below will open an empty space. To create the sheet your users
  should land on, you'll want to create a workbook as shown further down this
  page.
</Note>

```typescript
// app.module.ts
import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { SpaceModule } from "@flatfile/angular-sdk";

import { AppComponent } from "./app.component";

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, SpaceModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

```typescript
// app.component.ts
import { Component } from "@angular/core";
import { SpaceService, ISpace } from "@flatfile/angular-sdk";

@Component({
  selector: "app-root",
  template: `
    <div>
      <h1>My Application</h1>
      <button (click)="openFlatfile()">Import Data</button>
    </div>
  `,
})
export class AppComponent {
  constructor(private spaceService: SpaceService) {}

  spaceProps: ISpace = {
    publishableKey: "pk_your_publishable_key",
    displayAsModal: true,
  };

  openFlatfile() {
    this.spaceService.OpenEmbed(this.spaceProps);
  }
}
```

## Creating New Spaces

To create a new Space each time:

1. Add a `workbook` configuration object. Read more about workbooks [here](../core-concepts/workbooks).
2. Optionally [deploy](../core-concepts/listeners) a `listener` for custom data processing. Your listener will contain your validations and transformations

```typescript
spaceProps: ISpace = {
  publishableKey: "pk_your_publishable_key",
  workbook: {
    name: "My Import",
    sheets: [
      {
        name: "Contacts",
        slug: "contacts",
        fields: [
          { key: "name", type: "string", label: "Name" },
          { key: "email", type: "string", label: "Email" },
        ],
      },
    ],
  },
  displayAsModal: true,
};
```

For detailed workbook configuration, see the [Workbook API Reference](https://reference.flatfile.com/api-reference/workbooks).

## Reusing Existing Spaces

For production applications, implement proper space management on your server to ensure security and proper access control:

```typescript
// Frontend Component
@Component({
  selector: "app-import",
  template: `
    <div>
      <button (click)="openFlatfile()" [disabled]="loading">
        {{ loading ? "Loading..." : "Import Data" }}
      </button>
    </div>
  `,
})
export class ImportComponent {
  loading = false;

  constructor(private spaceService: SpaceService, private http: HttpClient) {}

  async openFlatfile() {
    this.loading = true;

    try {
      // Get space credentials from your server
      const response = await this.http
        .get<{
          publishableKey: string;
          spaceId: string;
          accessToken?: string;
        }>("/api/flatfile/space")
        .toPromise();

      const spaceProps: ISpace = {
        space: {
          spaceId: response.spaceId,
          accessToken: response.accessToken,
        },
        displayAsModal: true,
      };

      this.spaceService.OpenEmbed(spaceProps);
    } catch (error) {
      console.error("Failed to load Flatfile space:", error);
    } finally {
      this.loading = false;
    }
  }
}
```

For server implementation details, see the [Server Setup](/embedding/server-setup) guide.

## Configuration Options

For detailed configuration options, authentication settings, and advanced features, see the [Advanced Configuration](./advanced-configuration) guide.

## Using Space Component Directly

You can also use the `flatfile-space` component directly in your template:

```typescript
@Component({
  selector: "app-import",
  template: `
    <flatfile-space
      [spaceProps]="spaceProps"
      [showSpace]="showSpace"
      (closeSpace)="onCloseSpace()"
    >
    </flatfile-space>
    <button (click)="toggleSpace()">
      {{ showSpace ? "Close" : "Open" }} Import
    </button>
  `,
})
export class ImportComponent {
  showSpace = false;

  spaceProps: ISpace = {
    publishableKey: "pk_your_publishable_key",
    displayAsModal: true,
  };

  toggleSpace() {
    this.showSpace = !this.showSpace;
  }

  onCloseSpace() {
    this.showSpace = false;
  }
}
```

## TypeScript Support

The Angular SDK is built with TypeScript and includes full type definitions:

```typescript
import { ISpace, SpaceService } from "@flatfile/angular-sdk";

interface ImportData {
  name: string;
  email: string;
}

@Component({
  // component definition
})
export class ImportComponent {
  spaceProps: ISpace;

  constructor(private spaceService: SpaceService) {
    this.spaceProps = {
      publishableKey: "pk_your_publishable_key",
      spaceId: "us_sp_your_space_id",
    };
  }
}
```

## Next Steps

* **Advanced Configuration**: Set up [authentication, listeners, and advanced options](./advanced-configuration)
* **Server Setup**: Implement [backend integration and space management](./server-setup)
* **Data Processing**: Set up Listeners in your Space for custom data transformations
* **API Integration**: Use [Flatfile API](https://reference.flatfile.com) to retrieve processed data
* **Angular SDK Documentation**: See [@flatfile/angular-sdk documentation](https://www.npmjs.com/package/@flatfile/angular-sdk)

## Quick Links

<CardGroup cols={2}>
  <Card title="Advanced Configuration" icon="gear" href="/embedding/advanced-configuration">
    Authentication, listeners, and advanced options
  </Card>

  <Card title="Server Setup" icon="server" href="/embedding/server-setup">
    Backend integration and space management
  </Card>
</CardGroup>

## Example Projects

<CardGroup cols={2}>
  <Card title="Angular Example" icon="angular" href="https://github.com/FlatFilers/create-flatfile-angular">
    Complete Angular application with Flatfile embedding
  </Card>
</CardGroup>
