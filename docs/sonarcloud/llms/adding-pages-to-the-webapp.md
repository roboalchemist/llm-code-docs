# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/adding-pages-to-the-webapp.md

# Adding pages to the webapp

SonarQube Server’s UI is built as a Single Page Application using [React](https://reactjs.org/). It provides the ability to add new pages to the UI using JavaScript. A page (or page extension) is a self-contained JavaScript application that runs in the SonarQube Server environment. You can find the example of page extensions in the [SonarQube](https://github.com/SonarSource/sonarqube) or [sonar-custom-plugin-example](https://github.com/SonarSource/sonar-custom-plugin-example/tree/7.x/) repositories on GitHub.

Note that for security reasons, pages added to the UI cannot include [inline scripts](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#unsafe_inline_script) and [unsafe eval](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#unsafe_eval_expressions) expressions.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Before reading this guide, make sure you know the [plugin-basics](https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/plugin-basics "mention").

### Create a Java class implementing PageDefinition <a href="#create-a-java-class-implementing-pagedefinition" id="create-a-java-class-implementing-pagedefinition"></a>

For each page, you’ll need to set a key and a name. The page key should have the format `plugin_key/page_id` (e.g.: `governance/project_dump`). The `plugin_key` is computed from the `<artifactId>` in your `pom.xml`, or can be set explicitly in the pom using the `<pluginKey>` parameter in the `sonar-packaging-maven-plugin` configuration. All the pages should be declared in this class. Here is an example.

```css-79elbk
import org.sonar.api.web.page.Page;
import org.sonar.api.web.page.PageDefinition;
import org.sonar.api.web.page.Context;

import static org.sonar.api.web.page.Page.Scope.COMPONENT;
import static org.sonar.api.web.page.Page.Qualifier.VIEW;
import static org.sonar.api.web.page.Page.Qualifier.SUB_VIEW;
 
public class MyPluginPageDefinition implements PageDefinition {
  @Override
  public void define(Context context) {
    context
      .addPage(Page.builder("my_plugin/global_page")
        .setName("Global Page")
        .build())
      .addPage(Page.builder("my_plugin/project_page")
        .setName("Project Page")
        .setScope(COMPONENT)
        .build())
      .addPage(Page.builder("my_plugin/portfolio_page")
        .setName("Portfolio Page")
        .setScope(COMPONENT)
        .setComponentQualifiers(VIEW, SUB_VIEW)
        .build())
      .addPage(Page.builder("my_plugin/admin_page")
        .setName("Admin Page")
        .setAdmin(true)
        .build());
  }
}
```

#### Configuring each page <a href="#configuring-each-page" id="configuring-each-page"></a>

There are 3 settings available when you define the page extensions using the `PageDefinition` class:

* `setAdmin(boolean admin)`: flag this page as restricted to users with "administer" permission. Defaults to `false`.
* `setScope(org.sonar.api.web.page.Page.Scope scope)`: set the scope of this page. Available scopes are `GLOBAL` (default), which will add this page to the main menu, and `COMPONENT`, which will add the page to a project, application, or portfolio menu (applications and portfolios only apply to Enterprise Edition and above).
* `setComponentQualifiers(org.sonar.api.web.page.Qualifier... qualifiers)`: if `setScope()` is set to `COMPONENT`, this sets to what kind of component the page applies to. Available qualifiers are `PROJECT`, `APP`, `VIEW` (portfolio), and `SUB_VIEW` (`APP`, `VIEW`, and `SUB_VIEW` only apply to Enterprise Edition and above). You can pass multiple qualifiers. If no qualifier is set, it will apply to all types.

### Create a JavaScript file per page <a href="#create-a-javascript-file-per-page" id="create-a-javascript-file-per-page"></a>

The `PageDefinition` will register each key as an available route in SonarQube Server. Whenever this route is visited, SonarQube Server will asynchronously fetch a single JavaScript file from your plugin’s `/static/` directory, and boot up your page’s application. This file should have the same name as the `page_id` you defined in your `PageDefinition` class. In the example in Step 1, you would need 4 different JavaScript files:

* `/static/global_page.js`
* `/static/project_page.js`
* `/static/portfolio_page.js`
* `/static/admin_page.js`

Each file *must* call the global `window.registerExtension()` function, and pass its *full key* as a first argument (`plugin_key/page_id`, e.g.: `governance/project_dump`). The second argument is the *start* callback. This function will be called once your page is started, and receive information about the current page as an argument (see below). The return value of the start callback depends on how you want to implement your page:

If you want to use [React](https://reactjs.org/), you should return a React Component:

```css-79elbk
// static/global_page.js
import React from "react";
import App from "./components/App";

window.registerExtension('my_plugin/global_page', function (options) {
return <App options={options} />
});
```

If you want to use any other framework, you should perform any start logic directly inside the start function body, and **return a shutdown callback**:

```css-79elbk
// static/global_page.js
const init = require("./my-app/init");

window.registerExtension('my_plugin/global_page', function (options) {
// Start up my custom application, passing the DOM element which will serve as
// the container.
init.boot(options.el, options.currentUser, options.component);

// Whenever the user leaves the page, cleanly shut everything down
// (i.e., remove event listeners, stop running timers, etc).
return function () {
  init.removeEventListeners();
  init.clearState();
  init.shutdown();
};
});
```

The `options` object will contain the following:

* `options.el`: A DOM node you must use to inject your content.
* `options.currentUser`: Information about the current user.
* (optional) `options.component`: Contains the information of the current project, application, or portfolio.
* (optional) `options.branchLike`: Contains the information of the current branch or pull request.

SonarQube Server doesn’t guarantee any JavaScript library availability at runtime (except React). If you need a library, include it in the final file.

#### CSS files <a href="#css-files" id="css-files"></a>

If you want a static CSS file to be loaded when your extension is bootstrapped, rather than using run-time inclusion of styles, you can pass `true` as a third parameter to the `window.registerExtension()` function. This will trigger the loading of a CSS file that *must* have the same basename as the registering JS file. I.e., if your extension JS file is `/static/global_page.js`, the CSS file must be called `/static/global_page.css`. The bootstrap will wait for the CSS file to be fully loaded before calling the `start` callback.

### Examples <a href="#examples" id="examples"></a>

We recommend checking out the [sonar-custom-plugin-example](https://github.com/SonarSource/sonar-custom-plugin-example/) repository. It contains detailed examples using several front-end frameworks, and its code is thoroughly documented. It also describes how to run a local development server to speed up the front-end development, without requiring a full rebuild and re-deploy to test your changes.
