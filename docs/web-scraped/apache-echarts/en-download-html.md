# Source: https://echarts.apache.org/en/download.html

Title: Download - Apache ECharts

URL Source: https://echarts.apache.org/en/download.html

Markdown Content:
Free to choose to download different versions, different topics, the map data you need. You can be customized according to your needs.

Apache ECharts TM

### Option 1: Install from downloaded source code or binary

| Version | Release Date | Download Source from a Mirror | Dist files on GitHub |
| --- | --- | --- | --- |
| 6.0.0 | 2025/7/30 | [Source](https://www.apache.org/dyn/closer.cgi/echarts/6.0.0/apache-echarts-6.0.0-src.zip) ([Signature](https://www.apache.org/dist/echarts/6.0.0/apache-echarts-6.0.0-src.zip.asc)[SHA512](https://www.apache.org/dist/echarts/6.0.0/apache-echarts-6.0.0-src.zip.sha512)) | [Dist](https://github.com/apache/echarts/tree/6.0.0/dist) |

[View Archived Versions](https://archive.apache.org/dist/echarts/?C=N;O=D)

**Note:** when downloading from a mirror please check the [SHA-512](https://www.apache.org/dev/release-signing#sha-checksum) and verify the [OpenPGP](https://www.apache.org/dev/release-signing#openpgp) compatible signature from the main [Apache site](https://www.apache.org/). Links are provided above (next to the release download link). This [KEYS](https://www.apache.org/dist/echarts/KEYS) file contains the public keys used for signing release. It is recommended that (when possible) a [web of trust](https://www.apache.org/dev/release-signing#web-of-trust) is used to confirm the identity of these keys.

#### To verify ECharts releases using GPG

1. Download the release apache-echarts-X.Y.Z-src.zip from a mirror site.
2. Download the signature file apache-echarts-X.Y.Z-src.zip.asc from [Apache](https://www.apache.org/dist/echarts/).
3. Download the [ECharts KEYS](https://www.apache.org/dist/echarts/KEYS) file.
4. gpg --import KEYS
5. gpg --verify apache-echarts-X.Y.Z-src.zip.asc

#### To perform a quick check using SHA-512

1. Download the release apache-echarts-X.Y.Z-src.zip from a mirror site.
2. Download the checksum apache-echarts-X.Y.Z-src.zip.512 from [Apache](https://www.apache.org/dist/echarts/).
3. shasum -a 512 apache-echarts-X.Y.Z-src.zip

#### License

Apache ECharts is licensed under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

### Option 2: Install from npm

`npm install echarts`

### Option 3: Custom Build

[Customize](https://echarts.apache.org/en/builder.html)

Choose the features you want and build the file online.

### Next Step

[Get Started](https://echarts.apache.org/handbook/en/get-started/)
