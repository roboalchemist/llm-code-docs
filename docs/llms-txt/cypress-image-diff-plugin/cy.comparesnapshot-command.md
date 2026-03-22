# Source: https://cypress.visual-image-diff.dev/getting-started/cy.comparesnapshot-command.md

# cy.compareSnapshot command

`cy.compareSnapshot` command could be use in a most basic way:

```
cy.compareSnapshot('header')
```

or in a more configurable way:

```
cy.compareSnapshot({
  name: 'header',
  testThreshold: 0.2
})
```

* Available options are:

<table><thead><tr><th width="188">Option</th><th width="206">Type</th><th width="160">Required/Default value</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>string</code></td><td>required</td><td>The name of the snapshots that will be generated</td></tr><tr><td><code>nameTemplate</code></td><td><code>string</code></td><td><code>undefined</code></td><td>The snapshot naming pattern. Same as <a href="custom-config-file/name_template">NAME_TEMPLATE</a>, but with higher precedence</td></tr><tr><td><code>testThreshold</code></td><td><code>number</code></td><td><code>0</code></td><td>A number between <code>0</code> and <code>1</code> that represents the allowed percentage of pixels that can be different between the two snapshots</td></tr><tr><td><code>retryOptions</code></td><td><a href="https://www.npmjs.com/package/cypress-recurse#options"><code>Partial&#x3C;RecurseDefaults></code></a></td><td><code>{ limit:1 }</code></td><td>Config objects passed to <a href="https://www.npmjs.com/package/cypress-recurse#options">cypress-recurse</a></td></tr><tr><td><code>exactName</code></td><td><code>boolean</code></td><td><code>false</code></td><td>If set to <code>true</code>, will use the given name as it is without transforming it to <code>[spec_file_name]-[name]</code></td></tr><tr><td><code>cypressScreenshotOptions</code></td><td><a href="https://docs.cypress.io/api/commands/screenshot"><code>Partial&#x3C;Cypress.ScreenshotOptions &#x26; Cypress.Loggable &#x26; Cypress.Timeoutable></code></a></td><td><code>undefined</code></td><td>options object to change the default behavior of <code>cy.screenshot()</code></td></tr></tbody></table>
