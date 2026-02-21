# Source: https://airflow.apache.org/docs/helm-chart/stable/index.html

Title: Helm Chart for Apache Airflow — helm-chart Documentation

URL Source: https://airflow.apache.org/docs/helm-chart/stable/index.html

Markdown Content:
![Image 1: _images/helm-logo.svg](https://airflow.apache.org/docs/helm-chart/stable/_images/helm-logo.svg)

This chart bootstraps an [Airflow](https://airflow.apache.org/) deployment on a [Kubernetes](http://kubernetes.io/) cluster using the [Helm](https://helm.sh/) package manager.

Requirements[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

*   Kubernetes 1.30+ cluster

*   Helm 3.10+

*   PV provisioner support in the underlying infrastructure (optionally)

Features[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#features "Link to this heading")
---------------------------------------------------------------------------------------------------------

*   Supported executors (all Airflow versions): `LocalExecutor`, `CeleryExecutor`, `KubernetesExecutor`

*   Supported hybrid static executors (Airflow version `2.X.X`): `LocalKubernetesExecutor`, `CeleryKubernetesExecutor`

*   Supported Hybrid Executors (`2.10+`)

*   Supported AWS executors with AWS provider version `8.21.0+`:
    *   `airflow.providers.amazon.aws.executors.batch.AwsBatchExecutor`

    *   `airflow.providers.amazon.aws.executors.ecs.AwsEcsExecutor`

*   Supported AWS executors with AWS provider version `9.9.0+`:
    *   `airflow.providers.amazon.aws.executors.aws_lambda.lambda_executor.AwsLambdaExecutor`

*   Supported Edge executor with edge3 provider version `1.0.0+`:
    *   `airflow.providers.edge3.executors.EdgeExecutor`

*   Supported Airflow version: `1.10+`, `2.0+`, `3.0+`

*   Supported database backend: `PostgreSQL`, `MySQL`

*   Autoscaling for `CeleryExecutor` provided by KEDA

*   `PostgreSQL` and `PgBouncer` with a battle-tested configuration

*   Monitoring:

> *   StatsD/Prometheus metrics for Airflow
> 
>     *   Prometheus metrics for PgBouncer
> 
>     *   Flower

*   Automatic database migration after a new deployment

*   Administrator account creation during deployment

*   Kerberos secure configuration

*   One-command deployment for any type of executor. You don’t need to provide other services e.g. Redis/Database to test the Airflow.

Installing the Chart[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#installing-the-chart "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

To install this chart using Helm 3, run the following commands:

helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace

The command deploys Airflow on the Kubernetes cluster in the default configuration. The [Parameters reference](https://airflow.apache.org/docs/helm-chart/stable/parameters-ref.html) section lists the parameters that can be configured during installation.

Tip

List all releases using `helm list`.

Upgrading the Chart[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#upgrading-the-chart "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

To upgrade the chart with the release name `airflow`:

helm upgrade airflow apache-airflow/airflow --namespace airflow

Note

To upgrade to a new version of the chart, run `helm repo update` first.

Uninstalling the Chart[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#uninstalling-the-chart "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

To uninstall/delete the `airflow` deployment:

helm delete airflow --namespace airflow

The command removes all the Kubernetes components associated with the chart and deletes the release.

Note

Some kubernetes resources created by the chart [helm hooks](https://helm.sh/docs/topics/charts_hooks/#hook-resources-are-not-managed-with-corresponding-releases) might be left in the namespace after executing `helm uninstall`, for example, `brokerUrlSecret` or `fernetKeySecret`.

Installing the Chart with Argo CD, Flux, Rancher or Terraform[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#installing-the-chart-with-argo-cd-flux-rancher-or-terraform "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When installing the chart using Argo CD, Flux, Rancher or Terraform, you MUST set the four following values, or your application will not start as the migrations will not be run:

createUserJob:
 useHelmHooks: false
 applyCustomEnv: false
migrateDatabaseJob:
 useHelmHooks: false
 applyCustomEnv: false

This is so these CI/CD services can perform updates without issues and preserve the immutability of Kubernetes Job manifests.

This also applies if you install the chart using `--wait` in your `helm install` command.

Note

While deploying this Helm chart with Argo, you might encounter issues with database migrations not running automatically on upgrade.

To run database migrations with Argo CD automatically, you will need to add:

migrateDatabaseJob:
 jobAnnotations:
 "argocd.argoproj.io/hook": Sync

This will run database migrations every time there is a `Sync` event in Argo CD. While it is not ideal to run the migrations on every sync, it is a trade-off that allows them to be run automatically.

If you use the Celery(Kubernetes)Executor with the built-in Redis, it is recommended that you set up a static Redis password either by supplying `redis.passwordSecretName` and `data.brokerUrlSecretName` or `redis.password`.

By default, Helm hooks are also enabled for `extraSecrets` or `extraConfigMaps`. When using the above CI/CD tools, you might encounter issues due to these default hooks.

To avoid potential problems, it is recommended to disable these hooks by setting `useHelmHooks=false` as shown in the following examples:

extraSecrets:
 '{{ .Release.Name }}-example':
 useHelmHooks: false
 data: |
 AIRFLOW_VAR_HELLO_MESSAGE: "Hi!"

extraConfigMaps:
 '{{ .Release.Name }}-example':
 useHelmHooks: false
 data: |
 AIRFLOW_VAR_HELLO_MESSAGE: "Hi!"

Naming Conventions[¶](https://airflow.apache.org/docs/helm-chart/stable/index.html#naming-conventions "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

For new installations it is highly recommended to start using standard naming conventions. It is not enabled by default as this may cause unexpected behaviours on existing installations. However you can enable it using `useStandardNaming`:

useStandardNaming: true

For existing installations, all your resources will be recreated with a new name and helm will delete previous resources.

This won’t delete existing PVCs for logs used by StatefulSets/Deployments, but it will recreate them with brand new PVCs. If you do want to preserve logs history you’ll need to manually copy the data of these volumes into the new volumes after deployment. Depending on what storage backend/class you’re using this procedure may vary. If you don’t mind starting with fresh logs/redis volumes, you can just delete the old persistent volume claims, for example:

kubectl delete pvc -n airflow logs-gta-triggerer-0
kubectl delete pvc -n airflow logs-gta-worker-0
kubectl delete pvc -n airflow redis-db-gta-redis-0

Note

If you do not change `useStandardNaming` or `fullnameOverride` after upgrade, you can proceed as usual and no unexpected behaviours will be presented.
