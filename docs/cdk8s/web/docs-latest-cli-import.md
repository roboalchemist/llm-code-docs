# Source: https://cdk8s.io/docs/latest/cli/import/

Title: import - cdk8s

URL Source: https://cdk8s.io/docs/latest/cli/import/

Markdown Content:
The `import` command generates low-level (L1) constructs for Kubernetes API objects and Custom Resources (CRDs).

General Options[¶](https://cdk8s.io/docs/latest/cli/import/#general-options "Permanent link")
---------------------------------------------------------------------------------------------

### Target programming language (`--language`)[¶](https://cdk8s.io/docs/latest/cli/import/#target-programming-language-language "Permanent link")

You can specify your desired language with the `--language` flag. For example:

CLI:

```
cdk8s import --language typescript
```

`cdk8s.yaml`:

```
language: typescript
```

### Output directory (`--output`)[¶](https://cdk8s.io/docs/latest/cli/import/#output-directory-output "Permanent link")

The `--output` (or `-o`) option can be used to specify the output directory for your imports.

CLI:

```
cdk8s import --output ./path/to/imports
```

`cdk8s.yaml`:

```
importDirectory: ./path/to/imports
```

### Class name prefix (`--class-prefix`)[¶](https://cdk8s.io/docs/latest/cli/import/#class-name-prefix-class-prefix "Permanent link")

For `k8s` imports, all imported classes will have a `Kube` prefix to denote that those are core Kubernetes APIs. For CRD imports, the class name will match the resource kind.

You can use the `--class-prefix` option to specify an alternative prefix or `--no-class-prefix` to disable this behavior for `k8s` imports.

### Module name[¶](https://cdk8s.io/docs/latest/cli/import/#module-name "Permanent link")

You can also override the default behavior for `cdk8s` importing. This will be helpful to you if you would like to name your CRD imports differently from their kind. Here is how you do it:

CLI:

```
cdk8s import example:=my_crd.yaml
```

`cdk8s.yaml`:

```
imports:
  - example:=my_crd.yaml
```

If your CRD contained two kinds, `Cluster` and `Autoscaler`, you would have two imports. You could use them in this fashion:

Typescript Python

```
import { Cluster } from './imports/example-cluster';
import { Autoscaler } from './imports/example-autoscaler';
```

```
not yet supported
```

Import Types[¶](https://cdk8s.io/docs/latest/cli/import/#import-types "Permanent link")
---------------------------------------------------------------------------------------

The `import` command supports two types of imports:

1.   `k8s`: generates constructs from the core Kubernetes API
2.   `CRDs`: generates constructs from custom resource definitions
3.   `Helm Charts`: generates constructs from helm charts.

This section describes specific behavior related to each type of import.

### Kubernetes APIs[¶](https://cdk8s.io/docs/latest/cli/import/#kubernetes-apis "Permanent link")

To generate constructs for all Kubernetes API objects of a certain version, use:

```
cdk8s import k8s
```

The `import` command will generate files under an “imports” directory inside your project with constructs for each API object in the Kubernetes spec.

Tip

It is recommended to _commit_ these generated files into your source control.

By default, generated class names will be named `KubeXyz` where `Xyz` is the API object kind (e.g. `KubeDeployment`).

#### Kubernetes Versions[¶](https://cdk8s.io/docs/latest/cli/import/#kubernetes-versions "Permanent link")

Use the `@version` notation to import a specific Kubernetes version:

```
cdk8s import k8s@1.16.0
```

Alternatively, you can specify your `k8s` import in the `cdk8s.yaml` config file:

```
imports:
  - k8s@1.17.0
```

#### API Object Versions[¶](https://cdk8s.io/docs/latest/cli/import/#api-object-versions "Permanent link")

When importing the core Kubernetes API objects, `cdk8s import` will generate constructs both for stable APIs (e.g. `v1`) and pre-stable APIs (`v1beta1`). To ensure compatibility across Kubernetes versions, construct classes generated for non-stable resources will include a postfix with the API level.

For example, the import for `k8s@1.18` includes `KubeIngressV1Beta1` as the only `Ingress` resource. This is because `Ingress` has not been stabilized yet. The import for `k8s@1.19` will also include an `Ingress` construct which represents the `v1` resource.

### CRDs[¶](https://cdk8s.io/docs/latest/cli/import/#crds "Permanent link")

You can import CRDs from local files or URLs:

```
cdk8s import my_crd.yaml
```

Or from `cdk8s.yaml`:

```
imports:
  - my_crd.yaml
```

A CRD with group `mygroup.io` and kind `Foo` will be imported to the following locations:

*   TypeScript: `imports/mygroup.io.ts`
*   Python: `imports/mygroup/io`

#### Importing CRDs from a cluster[¶](https://cdk8s.io/docs/latest/cli/import/#importing-crds-from-a-cluster "Permanent link")

If the imported YAML is a `List` of CRDs, all these CRDs will be imported. This is useful, for example, to import all the CRDs from a running cluster:

```
kubectl get crds -o json | cdk8s import /dev/stdin
```

> Yes, this works!

### Helm Charts[¶](https://cdk8s.io/docs/latest/cli/import/#helm-charts "Permanent link")

You can import a helm chart and code generate a dedicated construct for it. To do this, pass either a url or a local path to the helm chart. For example, running the following command would code generate [bitnami’s mysql](https://github.com/bitnami/charts/tree/main/bitnami/mysql) helm chart:

```
cdk8s import helm:https://charts.bitnami.com/bitnami/mysql@9.10.10
```

> The format for the helm chart url is: `helm:<repo-url>/<chart-name>@<chart-version>`.

You can use this generated construct in your cdk8s application,

```
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';
import { Mysql, MysqlArchitecture } from './imports/mysql';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    new Mysql(this, 'MySql', {
      values: {
        architecture: MysqlArchitecture.STANDALONE,     // <------- type safe property
      }
    });
  }
}

const app = new App();
new MyChart(app, 'Typescript-App');
app.synth();
```

Note

You would need `helm` to be installed on your machine for using this feature. For accessing private helm repositories, you must be authenticated to the repository in a way that the `helm pull` command recognizes.

This feature is an extension to [helm](https://cdk8s.io/docs/latest/basics/helm/) support in cdk8s and you will find similar properties of Helm construct in these generated constructs.

#### Values Schema[¶](https://cdk8s.io/docs/latest/cli/import/#values-schema "Permanent link")

If the helm chart that you are importing contains a schema file (`values.schema.json`) within it, then the `values` property of the construct properties will be typed according to that schema.

For example:

```
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';
import { Mysql, MysqlArchitecture } from './imports/mysql';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    new Mysql(this, 'MySql', {
      values: {
        architecture: 'foo',    // <------- This will give an error since this is not `MysqlArchitecture` type which is generated from Schema
      }
    });
  }
}

const app = new App();
new MyChart(app, 'Typescript-App');
app.synth();
```

If there is no schema present in the helm chart, then `values` will not have type support and you can pass in any values.

#### Additional Values and Globals[¶](https://cdk8s.io/docs/latest/cli/import/#additional-values-and-globals "Permanent link")

The generated construct’s `values` property will also include following special properties:

*   `additionalValues`: If the imported helm chart has a schema but that schema does not cover all values accepted by the chart, then you can use this property to pass in those values to the chart.
*   `global`: This property can be used to set global values. For more information, see [here](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values).

For example:

```
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';
import { Mysql, MysqlArchitecture } from './imports/mysql';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    new Mysql(this, 'MySql', {
      values: {
        architecture: MysqlArchitecture.STANDALONE,
        global: {                                   // <------- global values
          imageRegistry: 'bar',
        },
        additionalValues: {                         // <------- values missing in schema which are not code generated
          nameOverride: "baz"
        },
      }
    });
  }
}

const app = new App();
new MyChart(app, 'Typescript-App');
app.synth();
```

#### Dependencies[¶](https://cdk8s.io/docs/latest/cli/import/#dependencies "Permanent link")

If the imported helm chart has any dependencies mentioned in `Chart.yaml`, then you will find those as properties in the generated construct. You can use those to pass in values to the dependency.

```
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';
import { Mysql, MysqlArchitecture } from './imports/mysql';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);

    new Mysql(this, 'MySql', {
      values: {
        architecture: MysqlArchitecture.STANDALONE,
        common: {                                   // <------- `common` is a dependency for the MySql helm chart
          names: {
            namespace: 'foo',
          }
        },
      }
    });
  }
}

const app = new App();
new MyChart(app, 'Typescript-App');
app.synth();
```
