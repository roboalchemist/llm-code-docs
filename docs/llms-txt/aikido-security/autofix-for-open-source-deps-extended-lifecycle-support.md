# Source: https://help.aikido.dev/aikido-autofix/autofix-for-open-source-deps-extended-lifecycle-support.md

# Autofix for Open Source Deps: Extended Lifetime Support

Updating to the latest version of an open source dependency can be a difficult task as breaking changes require application changes. When updating to the latest version of a package is not a viable option, you can stay secure by using hardened libraries or Aikido's Extended Lifetime Support (ELS).

Aikido offers a catalog of packages that solve security issues in versions of packages that are no longer maintained. These packages are drop-in replacements and don't require application changes.

For example the 1.x versions of log4j have been out of maintenance since 2015, but are still used in many projects. Updating these projects to log4j 2.x is infeasible in many cases. 1.2.17 is the latest 1.x version of log4j, it contains the following critical CVEs:

* [CVE-2019-17571](https://nvd.nist.gov/vuln/detail/cve-2019-17571) - remote code execution
* &#x20;[CVE-2020-9493](https://nvd.nist.gov/vuln/detail/cve-2020-9493) - malicious code execution
* [CVE-2022-23305](https://nvd.nist.gov/vuln/detail/cve-2022-23305) - SQL injection

Our ELS version of log4j 1.2.17 fixes these critical CVEs without introducing breaking changes.

The ELS packages are created by [TuxCare](https://tuxcare.com/). TuxCare specializes in End-Of-Life security and ports patches to unmaintained versions of packages.

## AutoFix for Open Source Dependencies

Aikido AutoFix for open source dependencies will automatically propose an upgrade to an ELS version where available. This is visible on the [AutoFix dependency overview](https://app.aikido.dev/issues/fix) screen. The Java ELS packages are hosted on `maven.aikido.io`.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FLTBeaI0XKmD0nD6OHfG1%2Fimage.png?alt=media&#x26;token=0714e317-f44a-4a38-8502-a61030f399ac" alt=""><figcaption></figcaption></figure>

In order to then upgrade to the ELS version, you need to select this option in the AutoFix creation modal.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FlHMOMtmVacr3Z0MDvZtV%2Fimage.png?alt=media&#x26;token=eaf1ac48-5506-4bef-80f5-47016150e647" alt=""><figcaption></figcaption></figure>

## Availability

ELS packages are currently available for Java, JavaScript, Python and PHP. Supported packages are listed below:

<details>

<summary>JavaScript </summary>

angular\
angular-resource\
angular-sanitize\
angular-translate\
bigint-buffer\
bootstrap\
braces\
cookie\
copy-anything\
crypto-js\
devalue\
expr-eval\
express\
express-jwt\
form-data\
formidable\
i18next\
ip\
jsonpath-plus\
jsonpointer\
jsonwebtoken\
jspdf\
knex\
lodash\
lodash.template\
marked\
mongodb\
mongoose\
multer\
mysql2\
next\
node-forge\
pdfjs-dist\
picocolors\
pug\
pug-code-gen\
quill\
request\
rollup\
sentry-browser\
ssr-window\
tough-cookie\
undici\
vue\
vue-template-compiler

</details>

<details>

<summary>Java</summary>

com.google.guava:guava\
com.google.protobuf:protobuf-java\
com.lowagie:itext\
com.querydsl:querydsl-jpa\
com.squareup.okio:okio\
commons-httpclient:commons-httpclient\
dom4j:dom4j\
log4j:log4j\
org.apache.hadoop:hadoop-aws\
org.apache.hadoop:hadoop-common\
org.apache.hadoop:hadoop-hdfs-httpfs\
org.apache.hadoop:hadoop-openstack\
org.apache.hive.shims:hive-shims-0.23\
org.apache.hive.shims:hive-shims-common\
org.apache.hive:hive-druid-handler\
org.apache.hive:hive-exec\
org.apache.hive:hive-llap-common\
org.apache.hive:hive-llap-server\
org.apache.hive:hive-serde\
org.apache.hive:hive-service\
org.apache.hive:hive-service-rpc\
org.apache.hive:hive-shims\
org.apache.hive:hive-testutils\
org.apache.hive:hive-vector-code-gen\
org.apache.hive:spark-client\
org.apache.thrift:libthrift\
org.apache.tomcat.embed:tomcat-embed-core\
org.apache.tomcat.embed:tomcat-embed-jasper\
org.apache.tomcat.embed:tomcat-embed-websocket\
org.apache.tomcat:tomcat-catalina\
org.apache.tomcat:tomcat-coyote\
org.apache.velocity:velocity\
org.codehaus.jackson:jackson-mapper-asl\
org.json:json\
org.springframework.boot:spring-boot-starter-thymeleaf\
org.springframework:spring-aspects\
org.springframework:spring-beans\
org.springframework:spring-context\
org.springframework:spring-core\
org.springframework:spring-expression\
org.springframework:spring-instrument\
org.springframework:spring-instrument-tomcat\
org.springframework:spring-messaging\
org.springframework:spring-web\
org.springframework:spring-webflux\
org.springframework:spring-webmvc\
org.springframework:spring-websocket\
org.yaml:snakeyaml

</details>

<details>

<summary>Python</summary>

anyio\
cryptography\
django\
flask\
flask-cors\
future\
gunicorn\
idna\
jinja2\
pillow\
pymongo\
pypdf\
setuptools\
statsmodels\
torch\
urllib3\
waitress\
werkzeug

</details>

<details>

<summary>PHP</summary>

laravel/framework\
livewire/livewire\
symfony/process

</details>
