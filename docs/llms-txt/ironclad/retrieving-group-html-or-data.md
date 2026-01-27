# Source: https://clickwrap-developer.ironcladapp.com/docs/retrieving-group-html-or-data.md

# Retrieving Clickwrap HTML or Data

At certain times, you may not be able to utilize one of our SDKs or our JavaScript Snippet but need a way to present your Clickwrap or at least retrieve data about the Clickwrap. Fortunately, this is still a possibility with our Activity API.

> 🚧 Heads Up
>
> Going this route typically requires heavy customization that would normally be provided by one of our SDKs or our JavaScript Library. Technical support may be limited.

## Endpoints

We have two available endpoints, which both allow you to retrieve data about a Group set up within your Ironclad Clickwrap account:

* `https://pactsafe.io/load/html` — [API Reference Page](https://clickwrap-developer.ironcladapp.com/reference/retrieve-group-html)
* `https://pactsafe.io/load/json` — [API Reference Page](https://clickwrap-developer.ironcladapp.com/reference/retrieve-group-json)

## Usage Examples

### Retrieve Group HTML

In some scenarios, you may want to load the Group data server-side rather than using the JavaScript Library/SDKs. You may also need the HTML and appropriate CSS styling as well. This is possible with the `/load/html` endpoint, which contains data fairly similar to what our JavaScript library would normally contain.

This would require doing a `GET` with `https://pactsafe.io/load/html?sid=YOUR_SITE_ACCESS_ID&gkey=YOUR_GROUP_KEY`, which will return data with the styling and HTML for the clickwrap chosen within your Group settings.

As an example, with my test group, I receive the following HTML data:

```html
<div id="ps-group-example-web-group" class="ps-group ps-style-combined" data-gid="6972" data-key="example-web-group"
  data-rdid="5f64fd8094c03836a4a744b4"
  data-legal="https://vault.pactsafe.io/s/790d7014-9806-4acc-8b8a-30c4987f3a95/legal.html">
  <style scoped>
    #ps-group-example-web-group *,
    #ps-group-example-web-group div {
      border: 0;
      margin: 0;
      padding: 0;
      min-height: 0;
      max-height: none;
      min-width: 0;
      max-width: none;
    }

    #ps-group-example-web-group a {
      font-size: 1em;
    }

    #ps-group-example-web-group a:hover {
      text-decoration: underline;
    }

    #ps-group-example-web-group div,
    #ps-group-example-web-group p,
    #ps-group-example-web-group span {
      color: #444;
    }

    #ps-group-example-web-group div.ps-contract {
      display: block;
      padding: 0 0 25px;
      margin: 0;
      color: #444;
      font-size: 13px;
      line-height: 1.5;
    }

    #ps-group-example-web-group div.ps-checkbox-container {
      display: block;
      font-size: 1em;
      line-height: 1.65;
      padding: 0 0 0 20px;
      margin: 0;
    }

    #ps-group-example-web-group input[type="checkbox"].ps-contract-target {
      display: inline;
      vertical-align: middle;
      width: auto;
      min-height: 0;
      max-height: none;
      min-width: 0;
      max-width: none;
      padding: 0;
      margin: 0 0 0 -20px;
      cursor: pointer;
    }

    #ps-group-example-web-group label.ps-contract-label {
      display: inline;
      vertical-align: middle;
      padding: 0;
      margin: 0 0 0 6px;
      text-transform: none;
      cursor: pointer;
    }

    #ps-group-example-web-group a.ps-contract-link {
      display: inline;
    }
  </style>
  <div id="ps-contracts-6972" class="ps-contract" data-multiple="true" data-cid="54147,54146"
    data-vid="5e3060462985a640d78aba14,5e95dcf23e634b0aac650716"
    data-mjvid="5e3060462985a640d78aba14,5e95dcf23e634b0aac650716" style="display: none;">
    <div class="ps-checkbox-container ps-checkbox-line">
      <input type="checkbox" class="ps-contract-target ps-combined-target ps-checkbox"
        id="ps-contract-checkbox-group-6972" name="ps-contract-checkbox-group-6972"
        value="54147:5e3060462985a640d78aba14,54146:5e95dcf23e634b0aac650716">
      <label for="ps-contract-checkbox-group-6972" class="ps-contract-label">I understand and agree to <a
          href="https://vault.pactsafe.io/s/790d7014-9806-4acc-8b8a-30c4987f3a95/legal.html?g=6972#contract-rki1kxfps"
          data-ckey="contract-rki1kxfps" target="_blank" class="ps-contract-link">Terms of Service</a> and <a
          href="https://vault.pactsafe.io/s/790d7014-9806-4acc-8b8a-30c4987f3a95/legal.html?g=6972#privacy-policy"
          data-ckey="privacy-policy" target="_blank" class="ps-contract-link">Privacy Policy</a>.</label>
    </div>
  </div>
</div>
```

This gives me the data I need to create the Clickwrap within my own environment.

> 🚧 Functionality Caveat
>
> Functionality for the Clickwrap requires custom code when our JavaScript library is not being used.

### Retrieve Group JSON

Say for example you have a mobile native app where our JavaScript Library may not be the best fit for implementation. Instead, you may want to grab the raw JSON data for the Group that can be used for your environment.

You could then do a `GET https://pactsafe.io/load/json?sid=YOUR_SITE_ACCESS_IDgkey=YOUR_GROUP_KEY`  to retrieve JSON data about the group.

As an example, with my test group, I receive the following JSON data:

```json
{
  "key": "example-web-group",
  "type": "group",
  "style": "combined",
  "group": 6972,
  "container_selector": "contracts-container",
  "signer_id_selector": "",
  "form_selector": "",
  "block_form_submission": true,
  "force_scroll": false,
  "alert_message": "Before you can submit this form, you must accept all of our legal contracts.",
  "confirmation_email": false,
  "triggered": false,
  "legal_center_url": "https://vault.pactsafe.io/s/790d7014-9806-4acc-8b8a-30c4987f3a95/legal.html",
  "acceptance_language": "I understand and agree to {{contracts}}.",
  "contract_data": {
    "54146": {
      "published_version": "5e95dcf23e634b0aac650716",
      "title": "Privacy Policy",
      "key": "privacy-policy",
      "change_summary": ""
    },
    "54147": {
      "published_version": "5e3060462985a640d78aba14",
      "title": "Terms of Service",
      "key": "contract-rki1kxfps",
      "change_summary": ""
    }
  },
  "contracts": [54147, 54146],
  "versions": ["5e3060462985a640d78aba14", "5e95dcf23e634b0aac650716"],
  "major_versions": ["5e3060462985a640d78aba14", "5e95dcf23e634b0aac650716"],
  "render_id": "5f64c0cddbf1201742e99b0b",
  "rendered_time": 1600438477,
  "auto_run": true,
  "display_all": false,
  "contract_html": "...",
  "locale": "en-us"
}
```

This gives you most of the information you would need about the Group to create your own Clickwrap and/or retrieve the required information for sending acceptance.