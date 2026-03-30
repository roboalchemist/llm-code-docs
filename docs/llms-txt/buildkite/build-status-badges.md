# Source: https://buildkite.com/docs/pipelines/integrations/other/build-status-badges.md

# Build status badges

Build status badges help to visually show the current build state for a pipeline in places such as readmes and dashboards.

You can find your pipeline's status badge on the pipeline's **Settings** > **Build Badges** page.

## Scoping to a branch

By default the build status badge will show the last build's status. You can scope it to a specific branch by adding a `?branch` parameter to the URL. For example, to scope your badge to the `main` branch you would add: `?branch=main` to the URL.

## Scoping to a step

If you want to create a badge that represents a single step in the last build, you can scope it that step by adding a `?step` parameter to the URL. For example, to scope your badge to the `iOS Build` step you would add: `?step=iOS%20Build` to the URL. If you have multiple steps that match the given name it will show as passing only if all of the matching steps passed.

## Styles

You can set the style of the badge by passing in a `style` parameter:

<table class="status-badges__examples">
  <tbody>
    <tr>
      <th>Default</th>
      <td><img src="https://badge.buildkite.com/sample.svg?status=passing" /></td>
      <td><img src="https://badge.buildkite.com/sample.svg?status=failing" /></td>
      <td><img src="https://badge.buildkite.com/sample.svg?status=unknown" /></td>
    </tr>

      <tr>
        <th><code><span class="muted">?style=</span>square</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;style=square" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;style=square" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;style=square" /></td>
      </tr>
    
  </tbody>
</table>

The `square` style can also be referred to as `flat-square` to match any [shields.io badges](http://shields.io) you may use.

## Themes

You can change the colors of the badges by passing in a `theme` parameter:

<table class="status-badges__examples">
  <tbody>
    <tr>
      <th>Default</th>
      <td><img src="https://badge.buildkite.com/sample.svg?status=passing" /></td>
      <td><img src="https://badge.buildkite.com/sample.svg?status=failing" /></td>
      <td><img src="https://badge.buildkite.com/sample.svg?status=unknown" /></td>
    </tr>

      <tr>
        <th><code><span class="muted">?theme=</span>slack</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=slack" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=slack" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=slack" /></td>
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>github</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=github" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=github" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=github" /></td>
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>saturn</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=saturn" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=saturn" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=saturn" /></td>
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>flickr</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=flickr" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=flickr" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=flickr" /></td>
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>solarized</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=solarized" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=solarized" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=solarized" /></td>
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>mono</code></th>
        <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=mono" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=mono" /></td>
        <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=mono" /></td>
      </tr>
    
  </tbody>
</table>

## Custom themes

You can also create your own theme by passing a comma-separated list of color values instead of the theme name.

The format is `passing-bg-color,failing-bg-color,unknown-bg-color[,label-bg-color[,text-color,status-text-color]]`

For example:

<table class="status-badges__examples">
  <tbody>

      <tr>
        <th><code><span class="muted">?theme=</span>9c0,f93,0ad</code></th>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=9c0,f93,0ad" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=9c0,f93,0ad" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=9c0,f93,0ad" /></td>
        
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>9c0,f93,0ad,d6d6d6</code></th>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=9c0,f93,0ad,d6d6d6" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=9c0,f93,0ad,d6d6d6" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=9c0,f93,0ad,d6d6d6" /></td>
        
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>9c0,f93,0ad,d6d6d6,000</code></th>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=9c0,f93,0ad,d6d6d6,000" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=9c0,f93,0ad,d6d6d6,000" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=9c0,f93,0ad,d6d6d6,000" /></td>
        
      </tr>
    
      <tr>
        <th><code><span class="muted">?theme=</span>9c0,f93,0ad,d6d6d6,000,fff</code></th>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=passing&amp;theme=9c0,f93,0ad,d6d6d6,000,fff" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=failing&amp;theme=9c0,f93,0ad,d6d6d6,000,fff" /></td>
        
          <td><img src="https://badge.buildkite.com/sample.svg?status=unknown&amp;theme=9c0,f93,0ad,d6d6d6,000,fff" /></td>
        
      </tr>
    
  </tbody>
</table>

## Sample badge URLs

You can use the following URLs for testing your theme:

* https://badge.buildkite.com/sample.svg?status=passing
* https://badge.buildkite.com/sample.svg?status=failing
* https://badge.buildkite.com/sample.svg?status=unknown

## JSON output

You can get the JSON value of the status badge by specifying `.json` in the badge URL instead of `.svg`, including [branch scoping](#scoping-to-a-branch) and [step scoping](#scoping-to-a-step). For example:

```shell
$ curl https://badge.buildkite.com/3826789cf8890b426057e6fe1c4e683bdf04fa24d498885489.json?branch=main
{"status": "passing"}
```

Possible values for the `"status"` key are:

* `"passing"`
* `"failing"`
* `"unknown"`

## Contributing

Want to contribute a theme? Send a pull request to [buildkite/build-status-badge-themes](https://github.com/buildkite/build-status-badge-themes).
