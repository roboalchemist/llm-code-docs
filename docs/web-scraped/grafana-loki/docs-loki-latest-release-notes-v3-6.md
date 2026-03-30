# Source: https://grafana.com/docs/loki/latest/release-notes/v3-6/

Title: v3.6 | Grafana Loki documentation

URL Source: https://grafana.com/docs/loki/latest/release-notes/v3-6/

Markdown Content:
Grafana Labs and the Loki team are excited to announce the release of Loki 3.6. Here’s a summary of new enhancements and important fixes.

One of the focuses of Loki 3.0 was cleaning up unused code and old features that had been previously deprecated but not removed. Loki 3.0 removed a number of previous deprecations and introduces some new deprecations. Some of the main areas with changes include:

To learn more about breaking changes in this release, refer to the [Upgrade guide](https://grafana.com/docs/loki/latest/setup/upgrade/).

*   **aggregated metrics:** Hide `__aggregated_metric__` in /series and /labels. This will alleviate confusion for people using a tool like logcli series –analyze-labels for cardinality analysis. ([#14677](https://github.com/grafana/loki/issues/14677)) ([4b0aaaa](https://github.com/grafana/loki/commit/4b0aaaaf2e22575381d2cfe90564a2cee6ddc7e8))

*   **build:** Update purgo package ([#17807](https://github.com/grafana/loki/pull/17807))

*   **build:** Remove busybox from dockerfile ([#19502](https://github.com/grafana/loki/issues/19502))

> Note
> 
> 
> You cannot exec into the container with a shell anymore. For more information see the [upgrade topic](https://grafana.com/docs/loki/latest/setup/upgrade/#loki-358). 
*   **build:** Remove UI from docker build ([#19425](https://github.com/grafana/loki/issues/19425))

*   **build:** RPM signature config ([#19476](https://github.com/grafana/loki/issues/19476))

*   **build:** Update ckit ([#18997](https://github.com/grafana/loki/issues/18997))

*   **ci:** Fix deprecation errors from staticcheck linter ([#17210](https://github.com/grafana/loki/issues/17210)) ([cfe3675](https://github.com/grafana/loki/commit/cfe36752952cfa1aac6f59bb5804999e09ef1e41))

*   **ci:** Fix lambda-promtail image build ([#18443](https://github.com/grafana/loki/issues/18443)) ([8f0ba2e](https://github.com/grafana/loki/commit/8f0ba2eae6e01d96523d8a0d71fb0bf1ae29a224))

*   **ci:** Fix workflow timeout added in wrong format ([#18348](https://github.com/grafana/loki/issues/18348)) ([53ba9c7](https://github.com/grafana/loki/commit/53ba9c7fd63465209e9919ef1e5346dbeb66b2aa))

*   **ci:** Read releaseLibRef from jsonnet.json lockfile ([#18538](https://github.com/grafana/loki/issues/18538)) ([26417b5](https://github.com/grafana/loki/commit/26417b594593269339e440df2d3cfbdf6bb06541))

*   **chunkenc:** Avoid memory allocations when loading symbolizer from a flushed chunk ([#17953](https://github.com/grafana/loki/issues/17953))

*   **compactor:** Return request ID in response header ([#19444](https://github.com/grafana/loki/issues/19444))

*   **compactor:** Concurrent map access for processedSeries in delete requests manager ([#17469](https://github.com/grafana/loki/issues/17469)) ([32c5088](https://github.com/grafana/loki/commit/32c50888b04de299380895585dce1c77755c488c))

*   **compactor:** Fix timeout and series progress marker for same requests with different shards ([#17125](https://github.com/grafana/loki/issues/17125)) ([288ec8c](https://github.com/grafana/loki/commit/288ec8c64dca6457fb2287deed9ba841e70c61ae))

*   **compactor:** Move the check for duplicate series up the call stack to fix an issue when retention is enabled ([#17663](https://github.com/grafana/loki/issues/17663)) ([a5e95ba](https://github.com/grafana/loki/commit/a5e95bacee50ce4d2512945f697a7aaff4403139))

*   **compactor:** Wire up deletion series progress tracking ([#17099](https://github.com/grafana/loki/issues/17099)) ([db59d0e](https://github.com/grafana/loki/commit/db59d0e9b2c463d85238e13a0c8dfa8a66e3967d))

*   **compactor:** Do not try to merge the already consolidated delete requests while listing them ([#18544](https://github.com/grafana/loki/issues/18544)) ([8054076](https://github.com/grafana/loki/commit/8054076873f925a539119e46422a4129766b9541))

*   **compactor:** Ensure to return delete requests only for the requested tenant ([#18589](https://github.com/grafana/loki/issues/18589)) ([cdb190b](https://github.com/grafana/loki/commit/cdb190be96eeed8087c9692726abae01ce6e7208))

*   **compactor:** Fix handling of duplicate delete requests ([#18460](https://github.com/grafana/loki/issues/18460)) ([255fce2](https://github.com/grafana/loki/commit/255fce20d813fc0b39758b6dbf51b23b987f0609))

*   **compactor:** Fix lint failure in retention.go ([#17894](https://github.com/grafana/loki/issues/17894))

*   **compactor:** Use the custom objectExists function to work around bug in Thanos object client ([#18820](https://github.com/grafana/loki/issues/18820))

*   **compactor:** Fix panic while applying storage updates when a whole chunk is deleted by line filters ([#19262](https://github.com/grafana/loki/issues/19262))

*   **compactor:** Set delete request batch to empty when we load to fail requests ([#17810](https://github.com/grafana/loki/issues/17810))

*   **config_wrapper:** Apply `instance_enable_ipv6` from common to all components ([#18254](https://github.com/grafana/loki/issues/18254)) ([5bc5853](https://github.com/grafana/loki/commit/5bc58538384a0895db47f57338a36cbe16049e52))

*   **deps:** Update to Go 1.24.2 (#17804)

*   **deps:** Update go toolchain to 1.24.6 ([#19449](https://github.com/grafana/loki/issues/19449))

*   **deps:** Patch mapstructure dependency to remove CVE (#19447)

*   **deps:** Remove workspace files from ignore and regenerate vendor (#17234)

*   **deps:** Update dskit dependency ([#18711](https://github.com/grafana/loki/issues/18711)) ([19233d0](https://github.com/grafana/loki/commit/19233d0461e7028e8bdb394f775cc22339c2c38c))

*   **deps:** Update dskit to fix linux/arm build ([#18715](https://github.com/grafana/loki/issues/18715)) ([f39fc1e](https://github.com/grafana/loki/commit/f39fc1e6e623bc88bf4d5d8e2e0c2ca039f5967f))

*   **deps:** Update dependency @hookform/resolvers to v5.2.2 (main) (#19276)

*   **deps:** Update dependency @radix-ui.react-checkbox to v1.3.3 (main) ([#18836](https://github.com/grafana/loki/issues/18836))

*   **deps:** Update dependency @radix-ui/react-collapsible to v1.1.8 (main) ([#17382](https://github.com/grafana/loki/issues/17382)) ([0a4aec6](https://github.com/grafana/loki/commit/0a4aec6ea74745a194fd5b0de833f027928322f3))

*   **deps:** Update dependency @radix-ui.react-dialog to v1.1.15 (main) ([#18841](https://github.com/grafana/loki/issues/18841))

*   **deps:** Update dependency @radix-ui.react-dropdown-menu to v2.1.16 (main) ([#18845](https://github.com/grafana/loki/issues/18845))

*   **deps:** Update dependency @radix-ui.react-hover-card to v1.1.15 (main)([#18849](https://github.com/grafana/loki/issues/18849))

*   **deps:** Update dependency @radix-ui/react-label to v2.1.7 (main) ([#17877](https://github.com/grafana/loki/issues/17877))

*   **deps:** Update dependency @radix-ui.react-popover to v1.1.15 (main) ([#18850](https://github.com/grafana/loki/issues/18850))

*   **deps:** Update dependency @radix-ui/react-progress to v1.1.7 (main) ([#17879](https://github.com/grafana/loki/issues/17879))

*   **deps:** Update dependency @radix-ui.react-scroll-area to v1.2.10 (main) ([#18852](https://github.com/grafana/loki/issues/18852))

*   **deps:** Update dependency @radix-ui.react-select to v2.2.6 (main) ([#18853](https://github.com/grafana/loki/issues/18853))

*   **deps:** Update dependency @radix-ui/react-separator to v1.1.7 (main) ([#17882](https://github.com/grafana/loki/issues/17882))

*   **deps:** Update dependency @radix-ui/react-slot to v1.2.3 (main) ([#17883](https://github.com/grafana/loki/issues/17883))

*   **deps:** Update dependency @radix-ui.react-switch to v1.2.6 (main)([#18854](https://github.com/grafana/loki/issues/18854))

*   **deps:** Update dependency @radix-ui/react-tabs to v1.1.9 (main) ([#17389](https://github.com/grafana/loki/issues/17389)) ([23a2f2d](https://github.com/grafana/loki/commit/23a2f2d0efde80d48acfb7f2561ad2cafe02b62f))

*   **deps:** Update dependency @radix-ui/react-toast to v1.2.7 (main) ([#17148](https://github.com/grafana/loki/issues/17148)) ([1a1cbb3](https://github.com/grafana/loki/commit/)

*   **deps:** Update dependency @radix-ui.react-toggle to v1.1.10 (main)([#18859](https://github.com/grafana/loki/issues/18859))

*   **deps:** Update dependency @radix-ui.react-toggle-group to v1.1.11 (main) ([#18860](https://github.com/grafana/loki/issues/18860))

*   **deps:** Update dependency @radix-ui.react-tooltip to v1.2.8 (main) ([#18862](https://github.com/grafana/loki/issues/18862))

*   **deps:** Update dependency @tanstack.react-query to v5.85.5 (main) ([#18962](https://github.com/grafana/loki/issues/18962))

*   **deps:** Update dependency @tanstack/react-query-devtools to v5.85.5 (main) ([#18963](https://github.com/grafana/loki/issues/18963))

*   **deps:** Update dependency @types/lodash to v4.17.20 (main) ([#18305](https://github.com/grafana/loki/issues/18305)) ([90ca918](https://github.com/grafana/loki/commit/90ca91834ebc01a733a3b866d6322df6ba514a2d))

*   **deps:** Update module cloud.google.com/go/bigtable to v1.40.1 (main) ([#19337](https://github.com/grafana/loki/issues/19337))

*   **deps:** Update module cloud.google.com/go/pubsub to v1.49.0 (main) ([#17187](https://github.com/grafana/loki/issues/17187)) ([cbd73d0](https://github.com/grafana/loki/commit/cbd73d0a883f9f9ac0d7151e02785841062bdf4c))

*   **deps:** Update module cloud.google.com/go/storage to v1.57.0 (main) ([#19312](https://github.com/grafana/loki/issues/19312))

*   **deps:** Update module dario.cat/mergo to v1.0.2 (main) ([#17651](https://github.com/grafana/loki/issues/17651)) ([bb8a9d9](https://github.com/grafana/loki/commit/bb8a9d9187c16773c4455197222911b6fc5c69d8))

*   **deps:** Update module github.com.prometheus/otlptranslator to v0.0.2 (main) (#18782)

*   **deps:** Update module github.com/alecthomas/chroma/v2 to v2.20.0 (main) ([#18710](https://github.com/grafana/loki/issues/18710)) ([c8e87dd](https://github.com/grafana/loki/commit/c8e87ddfe5ef2139b2396b6d904f6afca3eca03a))

*   **deps:** Update module github.com/alicebob/miniredis/v2 to v2.35.0 (main) (#18029)

*   **deps:** Update module github.com/apache/arrow-go/v18 to v18.4.0 (main) ([#18519](https://github.com/grafana/loki/issues/18519)) ([600fc9e](https://github.com/grafana/loki/commit/600fc9e7ede39625f7afff278e17744a5df6b793))

*   **deps:** Update module github.com/aws/aws-lambda-go to v1.49.0 (main) ([#18036](https://github.com/grafana/loki/issues/18036))

*   **deps:** Update module github.com/aws/aws-sdk-go to v1.55.7 (main) ([#17402](https://github.com/grafana/loki/issues/17402)) ([06a803d](https://github.com/grafana/loki/commit/06a803d6550c74d821b34d42db3e84558b66054f))

*   **deps:** Update module github.com/aws/aws-sdk-go-v2 to v1.36.6 (main) ([#18506](https://github.com/grafana/loki/issues/18506)) ([1d51304](https://github.com/grafana/loki/commit/1d51304359f96fb57d23d6f90787b5583acb8d9f))

*   **deps:** Update module github.com/aws/aws-sdk-go-v2/config to v1.29.18 (main) ([#18507](https://github.com/grafana/loki/issues/18507)) ([4ea7409](https://github.com/grafana/loki/commit/4ea7409b5bdc619c6bf9d9493567e6743e475540))

*   **deps:** Update module github.com/aws/aws-sdk-go-v2/credentials to v1.18.16 (main) ([#19352](https://github.com/grafana/loki/issues/19352))

*   **deps:** Update module github.com/aws/aws-sdk-go-v2/service/dynamodb to v1.51.0 (main) ([#19388](https://github.com/grafana/loki/issues/19388))

*   **deps:** Update module github.com/aws/aws-sdk-go-v2/service/s3 to v1.84.1 (main) ([#18508](https://github.com/grafana/loki/issues/18508)) ([4fdae62](https://github.com/grafana/loki/commit/4fdae62915990afec358a9724894a5b23e201b52))

*   **deps:** Update module github.com/baidubce/bce-sdk-go to v0.9.245 (main) ([#19278](https://github.com/grafana/loki/issues/19278))

*   **deps:** Update module github.com/bmatcuk/doublestar/v4 to v4.9.1 (main) ([#18599](https://github.com/grafana/loki/issues/18599)) ([17b377f](https://github.com/grafana/loki/commit/17b377fd17b70342816362cd5f338dec9e6f288b))

*   **deps:** Update module github.com/charmbracelet/bubbles to v0.21.0 (main) ([#17191](https://github.com/grafana/loki/issues/17191)) ([3e9c07e](https://github.com/grafana/loki/commit/3e9c07e400df29cada15e62f8fef897bc8fc9347))

*   **deps:** Update module github.com/charmbracelet/bubbletea to v1.3.10 (main) ([#19279](https://github.com/grafana/loki/issues/19279))

*   **deps:** Update module github.com/coder/quartz to v0.2.1 (main) ([#17922](https://github.com/grafana/loki/issues/17922)) ([3cb216c](https://github.com/grafana/loki/commit/3cb216c33c948338014db91ff49b26aa0800eeac))

*   **deps:** Update module github.com/docker/docker to v28.5.0+incompatible (main) ([#19414](https://github.com/grafana/loki/issues/19414))

*   **deps:** Update module github.com/fsnotify/fsnotify to v1.9.0 (main) ([#17192](https://github.com/grafana/loki/issues/17192)) ([eb4b651](https://github.com/grafana/loki/commit/eb4b651adf810b0c1b8b7dcd2be0040ff37f5a05))

*   **deps:** Update module github.com/fsouza/fake-gcs-server to v1.52.3 (main) (#18999)

*   **deps:** Update module github.com/go-logfmt/logfmt to v0.6.1 (main) (#19412)

*   **deps:** Update module github.com/grafana/loki/v3 to v3.5.5 (main) ([#18444](https://github.com/grafana/loki/issues/18444))

*   **deps:** Update module github.com/grpc-ecosystem/go-grpc-middleware/v2 to v2.3.2 (main) ([#17652](https://github.com/grafana/loki/issues/17652)) ([988857e](https://github.com/grafana/loki/commit/988857ea45a6ccb64999791cb694b79427948a7a))

*   **deps:** Update module github.com/hashicorp/consul/api to v1.32.1 (main) ([#17653](https://github.com/grafana/loki/issues/17653)) ([44b9b64](https://github.com/grafana/loki/commit/44b9b6422c9a3f1bbbd5bbb65ca83ee9dbf6853d))

*   **deps:** Update module github.com/heroku/x to v0.5.2 (main) ([#18809](https://github.com/grafana/loki/issues/18809))

*   **deps:** Update module github.com/ibm/go-sdk-core/v5 to v5.21.0 (main) ([#18587](https://github.com/grafana/loki/issues/18587)) ([86a31ec](https://github.com/grafana/loki/commit/86a31eca0eee97cfd27065289e7e29b36627a502))

*   **deps:** Update module github.com/ibm/ibm-cos-sdk-go to v1.12.3 (main) ([#19281](https://github.com/grafana/loki/issues/19281))

*   **deps:** Update module github.com/ibm/sarama to v1.46.1 (main) ([#19282](https://github.com/grafana/loki/issues/19282))

*   **deps:** Update module github.com/minio/minio-go/v7 to v7.0.95 (main) ([#18514](https://github.com/grafana/loki/issues/18514)) ([70c176c](https://github.com/grafana/loki/commit/70c176cd9984f1908cbe184c62fb7af197072021))

*   **deps:** Update module github.com/ncw/swift/v2 to v2.0.4 (main) ([#18011](https://github.com/grafana/loki/issues/18011))

*   **deps:** Update module github.com/oklog/run to v1.2.0 (main) ([#18263](https://github.com/grafana/loki/issues/18263)) ([3011a6c](https://github.com/grafana/loki/commit/3011a6c7d67640356146aa4a9858d6dac7cc6fe7))

*   **deps:** Update module github.com/opentracing-contrib/go-grpc to v0.1.2 (main) ([#17164](https://github.com/grafana/loki/issues/17164)) ([23b47ce](https://github.com/grafana/loki/commit/23b47ce7a5c707dc046547165d9c2e8d812ec8ba))

*   **deps:** Update module github.com/oschwald/geoip2-golang to v1.13.0 (main) ([#18354](https://github.com/grafana/loki/issues/18354))

*   **deps:** Update module github.com/parquet-go/parquet-go to v0.25.1 (main) ([#18013](https://github.com/grafana/loki/issues/18013)) (#18013)

*   **deps:** Update module github.com/pressly/goose/v3 to v3.26.0 (main) ([#19417](https://github.com/grafana/loki/issues/19417))

*   **deps:** Update module github.com/prometheus/client_golang to v1.23.0 (main) ([#18674](https://github.com/grafana/loki/issues/18674)) ([07a627a](https://github.com/grafana/loki/commit/07a627a40d59f405f140d13d425e1b15b4fd1a8b))

*   **deps:** Update module github.com/prometheus/client_model to v0.6.2 (main) ([#17171](https://github.com/grafana/loki/issues/17171)) ([fa84382](https://github.com/grafana/loki/commit/fa8438278835f82af329fb5a00df7d9b0a398965))

*   **deps:** Update module github.com/prometheus/common to v0.65.0 (main) ([#18196](https://github.com/grafana/loki/issues/18196)) ([3ad1077](https://github.com/grafana/loki/commit/3ad1077cc6c8cbcfeadd3e32ffc169b865724fb9))

*   **deps:** Update module github.com/prometheus/prometheus to v0.304.2 (main) ([#18248](https://github.com/grafana/loki/issues/18248)) ([b2e1d7f](https://github.com/grafana/loki/commit/b2e1d7f267328203de078a065f7b4101d740192f))

*   **deps:** Update module github.com/prometheus/sigv4 to v0.2.1 (main) ([#18454](https://github.com/grafana/loki/issues/18454)) ([9ea365a](https://github.com/grafana/loki/commit/9ea365a96007541e062e1f7a469d90f6e64436de))

*   **deps:** Update module github.com/redis/go-redis/v9 to v9.12.1 (main) ([#18218](https://github.com/grafana/loki/issues/18218))

*   **deps:** Update module github.com/shirou/gopsutil/v4 to v4.25.9 (main) ([#19366](https://github.com/grafana/loki/issues/19366))

*   **deps:** Update module github.com/sony/gobreaker/v2 to v2.3.0 (main) ([#19418](https://github.com/grafana/loki/issues/19418))

*   **deps:** Update module github.com/spf13/afero to v1.15.0 (main) ([#19317](https://github.com/grafana/loki/issues/19317))

*   **deps:** Update module github.com/stretchr/testify to v1.11.1 (main) ([#19042](https://github.com/grafana/loki/issues/19042))

*   **deps:** Update module github.com/twmb/franz-go to v1.19.5 (main) ([#18039](https://github.com/grafana/loki/issues/18039))

*   **deps:** Update module github.com/twmb/franz-go/pkg/kadm to v1.16.1 (main) ([#18733](https://github.com/grafana/loki/issues/18733))

*   **deps:** Update module github.com/twmb/franz-go/pkg/kmsg to v1.11.2 (main) ([#17258](https://github.com/grafana/loki/issues/17258)) ([7c47a3e](https://github.com/grafana/loki/commit/7c47a3e46d6d976b397c0e9f191e4d4f2a369e35))

*   **deps:** Update module github.com/twmb/franz-go/plugin/kotel to v1.6.0 (main) ([#17194](https://github.com/grafana/loki/issues/17194)) ([9491fbb](https://github.com/grafana/loki/commit/9491fbb5b8399c5c4c3fdc4a46cae03b01c0ecea))

*   **deps:** Update module github.com/twmb/franz-go/plugin/kprom to v1.3.0 (main) ([#18596](https://github.com/grafana/loki/issues/18596)) ([5405a83](https://github.com/grafana/loki/commit/5405a834973397a4b3871f9052a815a54fbca2c8))

*   **deps:** Update module github.com/workiva/go-datastructures to v1.1.6 (main) ([#19287](https://github.com/grafana/loki/issues/19287))

*   **deps:** Update module go.etcd.io/bbolt to v1.4.3 (main) ([#18973](https://github.com/grafana/loki/issues/18973))

*   **deps:** Update module go.opentelemetry.io/collector/pdata to v1.43.0 (main) ([#19419](https://github.com/grafana/loki/issues/19419))

*   **deps:** Update module go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc to v0.63.0 (main) ([#18455](https://github.com/grafana/loki/issues/18455))

*   **deps:** Update module go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace to v0.63.0 (main) ([#19324](https://github.com/grafana/loki/issues/19324))

*   **deps:** Update module go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp to v0.63.0 (main) ([#19327](https://github.com/grafana/loki/issues/19327))

*   **deps:** Update module golang.org/x.crypto to v0.41.0 (main) ([#18767](https://github.com/grafana/loki/issues/18767))

*   **deps:** Update module golang.org/x.net to v0.43.0 (main) ([#18769](https://github.com/grafana/loki/issues/18769))

*   **deps:** Update module golang.org/x/crypto to v0.40.0 (main) ([#18406](https://github.com/grafana/loki/issues/18406)) ([8fa91c6](https://github.com/grafana/loki/commit/8fa91c6f6a39e10838b346b84c93ae307fd81a9f))

*   **deps:** Update module golang.org/x/net to v0.45.0 (main) ([#19420](https://github.com/grafana/loki/issues/19420))

*   **deps:** Update module golang.org/x/oauth2 to v0.31.0 (main) ([#19329](https://github.com/grafana/loki/issues/19329))

*   **deps:** Update module golang.org/x/sync to v0.16.0 (main) ([#18383](https://github.com/grafana/loki/issues/18383)) ([6b1204a](https://github.com/grafana/loki/commit/6b1204a0de38389788434413a8777fe100d96622))

*   **deps:** Update module golang.org/x/sys to v0.35.0 (main) ([#18759](https://github.com/grafana/loki/issues/18759)) ([9c748e0](https://github.com/grafana/loki/commit/9c748e0358b7ab495fc3d10334236b91d4db1e46))

*   **deps:** Update module golang.org/x/text to v0.28.0 (main) ([#18762](https://github.com/grafana/loki/issues/18762)) ([e6fb85c](https://github.com/grafana/loki/commit/e6fb85cdfc6c44158544c0b0b766e9ddc86a9b41))

*   **deps:** Update module golang.org/x/time to v0.13.0 (main) ([#19330](https://github.com/grafana/loki/issues/19330))

*   **deps:** Update module google.golang.org/api to v0.252.0 (main) ([#19421](https://github.com/grafana/loki/issues/19421))

*   **deps:** Update module google.golang.org/grpc to v1.75.1 (main) ([#19288](https://github.com/grafana/loki/issues/19288))

*   **deps:** Update module google.golang.org/protobuf to v1.36.9 (main) ([#19289](https://github.com/grafana/loki/issues/19289))

*   **deps:** Update module k8s.io/apimachinery to v0.33.4 (main) ([#18868](https://github.com/grafana/loki/issues/18868))

*   **deps:** Update dependency lucide-react to ^0.544.0 (main) ([#19310](https://github.com/grafana/loki/issues/19310))

*   **deps:** Update dependency react to v19.1.0 (main) ([#16949](https://github.com/grafana/loki/issues/16949)) ([404fd13](https://github.com/grafana/loki/commit/404fd13a9c53e5a5586938199b0f05bd42edbcea))

*   **deps:** Update dependency react-datepicker to v8.7.0 (main) ([#18984](https://github.com/grafana/loki/issues/18984))

*   **deps:** Update dependency react-dom to v19.1.0 (main) ([#16950](https://github.com/grafana/loki/issues/16950)) ([8d1dc9c](https://github.com/grafana/loki/commit/8d1dc9ce7fdcf45fa433bb3056dbfdd82f45a915))

*   **deps:** Update dependency react-hook-form to v7.62.0 (main) ([#18704](https://github.com/grafana/loki/issues/18704)) ([4bc9162](https://github.com/grafana/loki/commit/4bc916274b4108a6fff662730fb0c3469d216f68))

*   **deps:** Update dependency react-router-dom to v7.8.2 (main) ([#18971](https://github.com/grafana/loki/issues/18971))

*   **deps:** Update dependency recharts to v2.15.4 (main) ([#18187](https://github.com/grafana/loki/issues/18187)) ([7593bf5](https://github.com/grafana/loki/commit/7593bf5129664e56a572256f7e5cc2771474e573))

*   **deps:** Update dependency tailwind-merge to v3.3.1 (main) ([#18061](https://github.com/grafana/loki/issues/18061))

*   **deps:** Update dependency zod to v3.25.76 (main) ([#18359](https://github.com/grafana/loki/issues/18359)) ([eb1e039](https://github.com/grafana/loki/commit/eb1e03962463ba8fe120fe44ce02f1f8b6598d91))

*   **deps:** Update dependency zod to v4 (main) ([#18392](https://github.com/grafana/loki/issues/18392)) (#18392)

*   **deps:** Update module zombiezen.com/go/sqlite to v1.4.2 (main) ([#17903](https://github.com/grafana/loki/issues/17903))

*   **distributor:** Disable metadata topic writes ([#17437](https://github.com/grafana/loki/issues/17437)) ([46b2271](https://github.com/grafana/loki/commit/46b2271aacd26734979667da61d5c9d24a8efb2b))

*   **distributor:** Revert remove colons from level detection ([#16999](https://github.com/grafana/loki/issues/16999)) ([e678b61](https://github.com/grafana/loki/commit/e678b615c18f52a23862d5d3ff39102989ec8374))

*   **distributor:** Short circuit level detection when already detected ([#17028](https://github.com/grafana/loki/issues/17028)) ([58aa00a](https://github.com/grafana/loki/commit/58aa00a5f47bfd851fbd01d94f0523b82968f896))

*   **distributor:** Skip streams over limits in dry-run mode ([#17114](https://github.com/grafana/loki/issues/17114)) ([2cde9b1](https://github.com/grafana/loki/commit/2cde9b12e9336531b54241437150d3cd83e7529a))

*   **distributor:** Prevent panic when ContentLength is negative in Distributor RequestBodyTooLarge metrics ([#17054](https://github.com/grafana/loki/issues/17054)) ([9e9f534](https://github.com/grafana/loki/commit/9e9f534460527f25d28fa3f3e17cd1eb4148b39d))

*   **distributor:** Detect “Information” log level as “info” ([#18195](https://github.com/grafana/loki/issues/18195)) ([82263d3](https://github.com/grafana/loki/commit/82263d383a0ac6efac50c681f00d26cb2848d367))

*   **distributor:** Correctly register allowed log level fields ([#19261](https://github.com/grafana/loki/issues/19261))

*   **distributor:** Extended detected level for debug and critical level ([#18370](https://github.com/grafana/loki/issues/18370))

*   **docs:** Update configuration.md ([#17269](https://github.com/grafana/loki/issues/17269)) ([70de523](https://github.com/grafana/loki/commit/70de5235b7c0e5a549f4bbc7cd127956d595badb))

*   **docs:** Added instructions for how to upgrade zone-aware ingesters ([#18658](https://github.com/grafana/loki/issues/18658)) ([aff2cb0](https://github.com/grafana/loki/commit/aff2cb0694cae99847b73da914ee4abd2432cdd0))

*   **engine:** Don’t attempt to release batch reference on read for merge node ([#18913](https://github.com/grafana/loki/issues/18913))

*   **engine:** Fix bug in `SortMerge` which caused rows to be skipped due to incorrect sorting ([#18334](https://github.com/grafana/loki/issues/18334)) ([4fbe7c1](https://github.com/grafana/loki/commit/4fbe7c1a21a6443951bca3ad5e40712b24b4ef73))

*   **engine:** Fix out-of-bounds panic in SortMerge implementation ([#17967](https://github.com/grafana/loki/issues/17967))

*   **frontend:** Allow resolution of v6 addresses. ([#18251](https://github.com/grafana/loki/issues/18251)) ([8481b34](https://github.com/grafana/loki/commit/8481b34dd583d021e0dfa89d64298d2f36f75176))

*   **helm:** Add flush=true to preStop hook ([#16063](https://github.com/grafana/loki/issues/16063)) ([a375751](https://github.com/grafana/loki/commit/a375751e4dc126a27cd8784c802e07871803868d))

*   **helm:** Add init container configuration for backend, bloom builder, distributor, query-frontend, query-scheduler, read, write. ([#18709](https://github.com/grafana/loki/issues/18709))

*   **helm:** Add livenessProbe to read pods in Simple Scalable mode ([#17063](https://github.com/grafana/loki/issues/17063))

*   **helm:** Add missing log deletion endpoint to native ingress paths ([#14390](https://github.com/grafana/loki/issues/14390)) ([6db8b1f](https://github.com/grafana/loki/commit/6db8b1f60bdbd07b8d8e1628fd3ef6030e064e77))

*   **helm:** Add release namespace metadata to HorizontalPodAutoscaling that lack it ([#18453](https://github.com/grafana/loki/issues/18453)) ([faae40a](https://github.com/grafana/loki/commit/faae40ab788d91dc4b7dbf110bbc1d3fcf4bf29c))

*   **helm:** Add validation for loki.storage.bucketNames ([#13781](https://github.com/grafana/loki/issues/13781)) ([831c814](https://github.com/grafana/loki/commit/831c814f6c9356784a3aa2b248c7be150b241cbd))

*   **helm:** Admin-api should only be deployed in microservice mode ([#13655](https://github.com/grafana/loki/issues/13655))

*   **helm:** Allow loki to use hostPath volumes ([#17680](https://github.com/grafana/loki/issues/17680)) ([8e61a5b](https://github.com/grafana/loki/commit/8e61a5bd23a9d388f9111ea824aaf73aa37366ff))

*   **helm:** Allow metrics networkpolicy only from namespace ([#17555](https://github.com/grafana/loki/issues/17555)) ([3a9b8e8](https://github.com/grafana/loki/commit/3a9b8e88a3595d27b52b79dab7c3bb6351b86b99))

*   **helm:** Avoid double zonal ingester scrapping by not scrapping headless svc ([#19000](https://github.com/grafana/loki/issues/19000))

*   **helm:** Create namespaced RBAC when sidecar is enabled ([#16776](https://github.com/grafana/loki/issues/16776)) ([7c9003e](https://github.com/grafana/loki/commit/7c9003eae54ab9b5497b3abe14fab7f754057b64))

*   **helm:** Do not strip whitespace in target definitions for querier and read deployments ([#19464](https://github.com/grafana/loki/issues/19464))

*   **helm:** Ensure global.extraEnv and global.extraEnvFrom applied to all resources consistently ([#16828](https://github.com/grafana/loki/issues/16828)) ([ee479d0](https://github.com/grafana/loki/commit/ee479d098000690f09372136d08ee9ba99b9a853))

*   **helm:** Explicitly set registry for k8s-sidecar image ([#19233](https://github.com/grafana/loki/issues/19233))

*   **helm:** Fix global extra* values ([#17020](https://github.com/grafana/loki/issues/17020))

*   **helm:** Fix incorrect context references in Helm storage templates ([#18740](https://github.com/grafana/loki/issues/18740)) ([1f362c8](https://github.com/grafana/loki/commit/1f362c8182b95db2f8d4a3e84b624ee528c738d4))

*   **helm:** Fix PDB settings for chunksCache and resultsCache ([#18321](https://github.com/grafana/loki/issues/18321)) ([e03b9b9](https://github.com/grafana/loki/commit/e03b9b9f9210201ce593f31eb90b12c4f9e2b1b8))

*   **helm:** Fix setting X-Scope-OrgID header ([#18414](https://github.com/grafana/loki/issues/18414)) ([2f461c9](https://github.com/grafana/loki/commit/2f461c90e133fe139d75a2aa90ef4a534ddcae3a))

*   **helm:** Fix storage_config when use_thanos_objstore is set to true ([#17024](https://github.com/grafana/loki/issues/17024)) ([81866d7](https://github.com/grafana/loki/commit/81866d790cb1f3140d5ddf7f9e50a0083c7accd8))

*   **helm:** Fixed statement logic to enable annotations ([#17756](https://github.com/grafana/loki/issues/17756))

*   **helm:** Gateway Ingester endpoints points to inexistent service when zone aware replication is enabled ([#17362](https://github.com/grafana/loki/issues/17362)) ([395a711](https://github.com/grafana/loki/commit/395a71117275c10385799c1226ca1fda1ec0c003))

*   **helm:** Make loki.storage.bucketNames are optional, if builtin minio is enabled. ([#18653](https://github.com/grafana/loki/issues/18653)) ([409ccbd](https://github.com/grafana/loki/commit/409ccbdc4e686895e6795888ba6b56b7ae93f332))

*   **helm:** Missing S3 field in lokiStorageConfig templated value ([#18791](https://github.com/grafana/loki/issues/18791))

*   **helm:** Move loki-sc-rules to second position in containers ([#17937](https://github.com/grafana/loki/issues/17937)) ([6e72df3](https://github.com/grafana/loki/commit/6e72df395b8c5f3d6bb822d232ab2432be1c5767))

*   **helm:** Only validate the ruler key exists under loki.storage.bucketNames when an object storage bucket is being used ([#18665](https://github.com/grafana/loki/issues/18665)) ([0604477](https://github.com/grafana/loki/commit/0604477af256110e43dd467974f1afade028f605))

*   **helm:** Remove flaky enterprise test ([#19362](https://github.com/grafana/loki/issues/19362))

*   **helm:** Removing deprecated admin_api_directory to avoid config crash ([#18731](https://github.com/grafana/loki/issues/18731)) ([8cce03c](https://github.com/grafana/loki/commit/8cce03c534255a5ca38878bbdaf65da490fd49d6))

*   **helm:** Roll back change to Thanos ruler storage ([#18907](https://github.com/grafana/loki/issues/18907))

*   **helm:** Un-deprecate several features in `monitoring` block ([#19012](https://github.com/grafana/loki/issues/19012))

*   **helm:** Update querier, read, and single binary target definitions for UI enablement ([#19461](https://github.com/grafana/loki/issues/19461))

*   **helm:** Use correct serviceName in zone-aware ingester statefulsets ([#18558](https://github.com/grafana/loki/issues/18558)) ([2706302](https://github.com/grafana/loki/commit/2706302caced15fa5cd2b32247e74f556850e032))

*   **helm:** In helm chart fix indentation in nginx gateway config template handling ([#18167](https://github.com/grafana/loki/issues/18167)) ([4fe20a7](https://github.com/grafana/loki/commit/4fe20a7e506290a6b4f4c51571251f64dd9b5f56))

*   **helm:** Loki chart fails to render proper YAML when add more than one extra manifest ([#12911](https://github.com/grafana/loki/issues/12911)) ([cf12656](https://github.com/grafana/loki/commit/cf12656a148cee6a605c19c45b8c27e4050f2ece))

*   **helm:** Make helm use grpc for compactor address ([#17454](https://github.com/grafana/loki/issues/17454)) ([90003f6](https://github.com/grafana/loki/commit/90003f6d9b9c90249d360aa0648ed197aef1a2cd))

*   **helm:** Use gateway container port as nginx server port ([#18774](https://github.com/grafana/loki/issues/18774))

*   **helm:** Use strings in stead of integers for ports in CiliumNetworkPolicies ([#19252](https://github.com/grafana/loki/issues/19252))

*   **helm:** Websocket related proxy_set_header to locations back to resolve high CPU usage. ([#18800](https://github.com/grafana/loki/issues/18800))

*   **helm:** Use UDP/53 for DNS egress instead of named port ([#19073](https://github.com/grafana/loki/issues/19073))

*   **helm:** Add single-binary component to ingress NetworkPolicy ([#19229](https://github.com/grafana/loki/issues/19229))

*   **helm:** Canary only worked when gateway enabled ([#16758](https://github.com/grafana/loki/issues/16758))

*   **helm:** Enable ui in helm deployments ([#17562](https://github.com/grafana/loki/issues/17562))

*   **helm:** Update loki-helm-test image tag to latest commit ([#19227](https://github.com/grafana/loki/issues/19227))

*   **ingester:** Fix missing series in monolithic mode ([#17067](https://github.com/grafana/loki/issues/17067)) ([5625464](https://github.com/grafana/loki/commit/5625464332fc0b3371b744d60d36acaf2600665a))

*   **json parser:** Fix possible JSON log line corruption caused by `json` parser on query path ([#18056](https://github.com/grafana/loki/issues/18056))

*   **json, structured metadata:** Correctly handle escaping in json parsing API ([#17068](https://github.com/grafana/loki/issues/17068))

*   **json, structured metadata:** JSON-parsing cleanup ([#17072](https://github.com/grafana/loki/issues/17072)) ([2aed4c3](https://github.com/grafana/loki/commit/2aed4c3da5e97ea3c40091961395568f693bf1cf))

*   **kafka:** Remove duplicated metric from Kafka producer ([#18614](https://github.com/grafana/loki/issues/18614)) ([a67a460](https://github.com/grafana/loki/commit/a67a460e9d7db43a793b180f2e73584fbe2497bb))

*   **kafka:** Disable defaults address defaults ([#17825](https://github.com/grafana/loki/issues/17825))

*   **kafka:** Use cooperative active sticky load balancer ([#19160](https://github.com/grafana/loki/issues/19160))

*   **limits:** Adapt defaults and expose evict interval ([#17808](https://github.com/grafana/loki/issues/17808))

*   **limits:** Fix ingest-limits eviction metric ([#17779](https://github.com/grafana/loki/issues/17779))

*   **limits:** Read the consumer group and topic from the ingest-limits config ([#17831](https://github.com/grafana/loki/issues/17831))

*   **limits:** Set ready when all partitions ready ([#18092](https://github.com/grafana/loki/issues/18092)) ([a07bee5](https://github.com/grafana/loki/commit/a07bee5dc2aae2c0618aba8d049630597b21b611))

*   **limits:** Counter variables should not have total at the end (([#17982](https://github.com/grafana/loki/issues/17982))

*   **loki:** Return defaults for non-existent tenants on applied limits endpoint ([#17942](https://github.com/grafana/loki/issues/17942))

*   **logql:** Fix inconsistency with parsed field short circuiting ([#17104](https://github.com/grafana/loki/issues/17104)) ([88beefb](https://github.com/grafana/loki/commit/88beefb02acca7651d57e69dd5118598d829a904))

*   **logql:** While validating logql expression, detect and validate expression in label_replace ([#18470](https://github.com/grafana/loki/issues/18470)) ([d379de5](https://github.com/grafana/loki/commit/d379de501f93be62cb0f72948794276e817d2599))

*   **logql:** Implement approx-topk function on querier ([#17816](https://github.com/grafana/loki/issues/17816))

*   **logql:** Reduce allocations for JSON and logfmt parser ([#18637](https://github.com/grafana/loki/issues/18637))

*   **memberlist:** Allow resolution of advertise address from v6 interface ([#18250](https://github.com/grafana/loki/issues/18250)) ([8594d1c](https://github.com/grafana/loki/commit/8594d1ca282a9378091c122a2aa31d4b3af3f817))

*   **mixins:** Fix label generation for Loki logs dashboard ([#17412](https://github.com/grafana/loki/issues/17412)) ([da2b620](https://github.com/grafana/loki/commit/da2b620964e2b452598d2817107433e2e0092cc3))

*   **mixin:** Fix typo in Loki Reads dashboard TSDB row ([#18872](https://github.com/grafana/loki/issues/18872))

*   **objstore:** Ruler not starting and incorrect mkdir path when Thanos Store is enabled ([#16555](https://github.com/grafana/loki/issues/16555)) ([3da9f2c](https://github.com/grafana/loki/commit/3da9f2cae6cb6c01e185ef9a596cae8e3f782873))

*   **operator:** Fix type of maximum OpenShift version property ([#18066](https://github.com/grafana/loki/issues/18066)) ([f7c7dfa](https://github.com/grafana/loki/commit/f7c7dfa910d03e2ddc9c95c8d22fb3bff5c78e6b))

*   **operator:** Fix typo in docs regarding forcepathstyle ([#17725](https://github.com/grafana/loki/issues/17725))

*   **operator:** Update maximum OpenShift version ([#17954](https://github.com/grafana/loki/issues/17954))

*   **operator:** Update memberlist when ingester becomes unhealthy ([#17026](https://github.com/grafana/loki/issues/17026)) ([c63f0a9](https://github.com/grafana/loki/commit/c63f0a9d8d93398fc47d1992ac6370fe57c8e58f))

*   **operator:** Update webhook validator for alerts/rules ([#17824](https://github.com/grafana/loki/issues/17824))

*   **operator:** Updated AlertingRule sample to make it comply with the validation we apply ([#18671](https://github.com/grafana/loki/issues/18671))

*   **operator:** Upgrade OPA policy syntax for v1+ ([#18795](https://github.com/grafana/loki/issues/18795))

*   **otlp:** Calculate entry metadata size before adding resource/scope attributes ([#17629](https://github.com/grafana/loki/issues/17629)) ([2161c8c](https://github.com/grafana/loki/commit/2161c8c52c36ac2d6657dbc670472be2022ca90f))

*   **patterns:** Pattern persistence feature flag ([#18285](https://github.com/grafana/loki/issues/18285)) ([a206324](https://github.com/grafana/loki/commit/a206324ae3640d5f7615c2115fb3272256e95c6d))

*   **patterns:** Limit volume and frequency of persisted patterns ([#18362](https://github.com/grafana/loki/issues/18362)) ([c690827](https://github.com/grafana/loki/commit/c690827c6a655ada93806237d81643025ab53494))

*   **patterns:** Fix feature flag for enabling pattern persistence ([#18216](https://github.com/grafana/loki/issues/18216)) ([c167800](https://github.com/grafana/loki/commit/c167800b3f6e7edd7b3f06a9105245c98b7391dd))

*   **push:** Add guard clauses to prevent negative counter values ([#17056](https://github.com/grafana/loki/issues/17056)) ([9000de1](https://github.com/grafana/loki/commit/9000de1aa7a6508234ee58adb346549ac3df2648))

*   **push:** Fix guard clauses to prevent error spam in logs ([#17372](https://github.com/grafana/loki/issues/17372)) ([d70b20e](https://github.com/grafana/loki/commit/d70b20e37ffb788297bb42933aabc3fa5723f78c))

*   **push:** Fix push stats calculation ([#19319](https://github.com/grafana/loki/issues/19319))

*   **oltp:** Apply global otlp config to tenant config only when it is updated in the overrides ([#19213](https://github.com/grafana/loki/issues/19213))

*   **querier:** Fixes panic when filtering agg metrics from nil resp ([#17662](https://github.com/grafana/loki/issues/17662))

*   **querier:** Allow boolean numeric values in detected labels ([#16997](https://github.com/grafana/loki/issues/16997)) ([bfb935d](https://github.com/grafana/loki/commit/bfb935d893b6c3dec8d5fee539478c64d3012dd3))

*   **querier:** Fix integer overrun when calculating parallelism for very long time range queries ([#17428](https://github.com/grafana/loki/issues/17428)) ([82acbd5](https://github.com/grafana/loki/commit/82acbd58b22481df3999f34edcace200940ce79b))

*   **querier:** Better fix integer overrun when calculating parallelism for very long time range queries ([#17430](https://github.com/grafana/loki/issues/17430)) ([d660af3](https://github.com/grafana/loki/commit/d660af37fbc7dc9c7426999d14555c9bc688c565))

*   Revert “perf: Fix memory leak in cachedIterator ([#17628](https://github.com/grafana/loki/issues/17628))” ([#18687](https://github.com/grafana/loki/issues/18687)) ([0316740](https://github.com/grafana/loki/commit/03167408063088542d251a136d314471f09f33e9))

*   **ruler:** Correct log level verbosity in rule evaluation ([#19519](https://github.com/grafana/loki/issues/19519)) fix(ruler): Return StatusBadRequest on multiple org IDs (#17850)

*   **storage:** Fix nil pointer dereference in Volume method of the composite store ([#18064](https://github.com/grafana/loki/issues/18064)) ([fc7c018](https://github.com/grafana/loki/commit/fc7c0189c063d59d8933159faa9ab8f3e9df7f06))

*   **storage:** Use default config when building S3 client (backport k277) ([#19559](https://github.com/grafana/loki/issues/19559))

*   **stream-generator:** Split create/keep-alive streams routines ([#17815](https://github.com/grafana/loki/issues/17815))

*   **structured metadata:** Improve structured metadata label normalization performance ([#17332](https://github.com/grafana/loki/issues/17332)) ([87922da](https://github.com/grafana/loki/commit/87922da28d332115f41d514f98c47fafb26fc7c6))

*   **structured metadata:** Unescape JSON structured metadata string values ([#13919](https://github.com/grafana/loki/issues/13919)) ([9629d07](https://github.com/grafana/loki/commit/9629d07c60a25b27aeddb81af3ea6ceb9031fd52))

*   **structured metadata:** Ensure we do not Add duplicate structured metadata from stream labels and extracted map ([#18523](https://github.com/grafana/loki/issues/18523)) ([db72d63](https://github.com/grafana/loki/commit/db72d63211c2cc5208d207b5795d5109b74c16ca))

*   **tests:** Update kfake to fix tests and revert go-redis ([#18958](https://github.com/grafana/loki/issues/18958))

*   **tools:** Correct typo in appenPath function name ([#17917](https://github.com/grafana/loki/issues/17917))

*   **tsdb:** Avoid copying label values from tsdb unless required ([#17077](https://github.com/grafana/loki/issues/17077)) ([8e4b104](https://github.com/grafana/loki/commit/8e4b10408dacf7891d48b70eba451a95bcf72853))

*   **ui:** Fix UI build ([#17717](https://github.com/grafana/loki/issues/17717)) ([e01a2a9](https://github.com/grafana/loki/commit/e01a2a908a83006e2ecd71c1dffbf0982ec89d00))

*   **ui:** Downgrade UI’s @swc/core dep back to v1.13.5 ([#19345](https://github.com/grafana/loki/issues/19345))

*   **WAL:** Handle WAL corruption properly on startup ([#18175](https://github.com/grafana/loki/issues/18175)) ([1954f67](https://github.com/grafana/loki/commit/1954f67a50ca0dc40e77c49e2c6cc74014e5998a))
