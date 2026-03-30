# Source: https://docs.wandb.ai/models/reports/embed-reports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Embed W&B reports directly into Notion or with an HTML IFrame element.

# Embed a report

## HTML iframe element

Select the **Share** button on the upper right hand corner within a report. A modal window will appear. Within the modal window, select **Copy embed code**. The copied code will render within an Inline Frame (IFrame)  HTML element. Paste the copied code into an iframe HTML element of your choice.

<Note>
  Only **public** reports are viewable when embedded.
</Note>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/get_embed_url.gif?s=e05c89e84294fac3458371de33fd969f" alt="Getting embed code" width="1425" height="721" data-path="images/reports/get_embed_url.gif" />
</Frame>

## Confluence

The proceeding animation demonstrates how to insert the direct link to the report within an IFrame cell in Confluence.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/embed_iframe_confluence.gif?s=57f7b54f8a23f04c627e7e80ca2503f6" alt="Embedding in Confluence" width="1425" height="721" data-path="images/reports/embed_iframe_confluence.gif" />
</Frame>

## Notion

The proceeding animation demonstrates how to insert a report into a Notion document using an Embed block in Notion and the report's embedded code.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/uqPGOvf46GQ1vVUB/images/reports/embed_iframe_notion.gif?s=7ab3667a21ca039bcfbb195b929d3050" alt="Embedding in Notion" width="1425" height="738" data-path="images/reports/embed_iframe_notion.gif" />
</Frame>

## Gradio

You can use the `gr.HTML` element to embed W\&B Reports within Gradio Apps and use them within Hugging Face Spaces.

```python  theme={null}
import gradio as gr


def wandb_report(url):
    iframe = f'<iframe src={url} style="border:none;height:1024px;width:100%">'
    return gr.HTML(iframe)


with gr.Blocks() as demo:
    report = wandb_report(
        "https://wandb.ai/_scott/pytorch-sweeps-demo/reports/loss-22-10-07-16-00-17---VmlldzoyNzU2NzAx"
    )
demo.launch()
```

##
