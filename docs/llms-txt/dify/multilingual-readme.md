# Source: https://docs.dify.ai/en/develop-plugin/features-and-specs/plugin-types/multilingual-readme.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Multilingual README

> This article introduces the file specifications for Dify plugins' multilingual READMEs and their display rule in Dify Marketplace.

You can create multilingual READMEs for your plugin, which will be displayed in [Dify Marketplace](https://marketplace.dify.ai) and other locations based on the user's preferred language.

### README **File Specifications**

| **Language**        | Required | Filename                    | Path                                                   | **Description**                                                  |
| :------------------ | :------- | :-------------------------- | :----------------------------------------------------- | :--------------------------------------------------------------- |
| **English**         | Yes      | `README.md`                 | Plugin root directory                                  | /                                                                |
| **Other Languages** | No       | `README_<language_code>.md` | In the `readme` folder under the plugin root directory | Currently supports Japanese, Portuguese, and Simplified Chinese. |

Here's an example of the directory structure:

```bash  theme={null}
...
├── main.py
├── manifest.yaml
├── readme
│   ├── README_ja_JP.md
│   ├── README_pt_BR.md
│   └── README_zh_Hans.md
├── README.md
...
```

### How Multilingual READMEs are Displayed **in Marketplace**

When your plugin has a README in the user's preferred language, the plugin's detail page in Dify Marketplace will display that language version of the README.

<img src="https://mintcdn.com/dify-6c0370d8/fW20SkOBxacYCkTW/images/plugin_details_page_en.jpeg?fit=max&auto=format&n=fW20SkOBxacYCkTW&q=85&s=a7c5c10ce618a56e3b74f972f171a942" alt="" width="2882" height="1920" data-path="images/plugin_details_page_en.jpeg" />

***

[Edit this page](https://github.com/langgenius/dify-docs/edit/main/en/develop-plugin/features-and-specs/plugin-types/multilingual-readme.mdx) | [Report an issue](https://github.com/langgenius/dify-docs/issues/new?template=docs.yml)


Built with [Mintlify](https://mintlify.com).