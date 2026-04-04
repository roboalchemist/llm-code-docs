# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/faqs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs

> You have questions, we have (some) answers!

### Text Classification

1. [How to find mislabeled samples?](https://www.loom.com/share/19b5eb751b7c4d1598fafdbc552a4a82)

2. [How to analyze misclassified samples?](https://www.loom.com/share/8fbcf48384964bdb9aa60d21310a3a6f)

3. [What is DEP and how to use it?](https://www.loom.com/share/a49dfbd68a624bcfaff5601bf3c6b449)

4. [How to inspect my model's embeddings?](https://www.loom.com/share/f5e0e38d265b4a818b89892dd8ee5600)

5. [How to best leverage Similarity Search?](https://www.loom.com/share/f9dae455fcfa4442b738f2ccbb3b155f)

### Named Entity Recognition

1. [NER: What's new?](https://www.loom.com/share/eebad1acedac49a3851216bbf509f83b)

2. [How to identify spans that were hard to train on?](https://www.loom.com/share/4843dd3c79124b2c80c399915ba5c68e)
   1. *Most Frequent High DEP words*

   2. *Span-level Embeddings*

3. What do the different Error Types mean?
   1. [Ghost Span Errors](https://www.loom.com/share/96f941703a424f4993cf38105ee262e3)

   2. [Missed Span Errors](https://www.loom.com/share/a70cf72e9bb9445496ed5b186a76a710)

   3. [Span Shift Errors](https://www.loom.com/share/92e4cd59389e4c31bedcde852c912d0a)

   4. [Wrong Tag Errors](https://www.loom.com/share/1e945e1245344452ac5b745ea6139d18)

### Questions

* [**How do I install the Galileo Python client?**](/galileo/how-to-and-faq/faqs#q-how-do-i-install-the-galileo-python-client)

* [**I'm seeing errors importing dataquality in jupyter/google colab**](/galileo/how-to-and-faq/faqs#q-im-seeing-errors-importing-dataquality-in-jupyter-google-colab)

* [**My run finished, but there's no data in the console! What went wrong?**](/galileo/how-to-and-faq/faqs#q-my-run-finished-but-theres-no-data-in-the-console-what-went-wrong)

* [**Can I Log custom metadata to my dataset?**](/galileo/how-to-and-faq/faqs#q-can-i-log-custom-metadata-to-my-dataset)

* [**How do I disable Galileo logging during model training?**](/galileo/how-to-and-faq/faqs#q-how-do-i-disable-galileo-logging-during-model-training)

* [**How do I load a Galileo exported file for re-training?**](/galileo/how-to-and-faq/faqs#q-how-do-i-load-a-galileo-exported-file-for-re-training)

* [**How do I get my NER data into huggingface format?**](/galileo/how-to-and-faq/faqs#q-how-do-i-get-my-ner-data-into-huggingface-format)

* [**My spans JSON column for my NER data can't be loaded with json.loads**](/galileo/how-to-and-faq/faqs#q-my-spansjson-column-for-my-ner-data-cant-be-loaded-with-json.loads)

* [**Galileo marked an incorrect span as a span shift error, but it looks like a wront tag error. What's going on?**](/galileo/how-to-and-faq/faqs#q-galileo-marked-an-incorrect-span-as-a-span-shift-error-but-it-looks-like-a-wrong-tag-error.-whats)

* [**What do you mean when you say the deployment logs are written to Google Cloud?**](/galileo/how-to-and-faq/faqs#q-what-do-you-mean-when-you-say-the-deployment-logs-are-written-to-google-cloud)

* [**Does Galileo store data in the cloud?**](/galileo/how-to-and-faq/faqs#q-does-galileo-store-data-in-the-cloud)

* [**Where are the client logs stored?**](/galileo/how-to-and-faq/faqs#q-where-are-the-client-logs-stored)

* [**Do you offer air-gapped deployments?**](/galileo/how-to-and-faq/faqs#q-do-you-offer-air-gapped-deployments)

* [**How do I contact Galileo?**](/galileo/how-to-and-faq/faqs#q-how-do-i-contact-galileo)

* [**How do I convert my vaex dataframe to pandas when using dq.metrics.get\_dataframe?**](/galileo/how-to-and-faq/faqs#q-how-do-i-convert-my-vaex-dataframe-to-a-pandas-dataframe-when-using-the-dq.metrics.get_dataframe)

* [**Importing dataquality throws a permissions error \`PermissionError\`**](/galileo/how-to-and-faq/faqs#q-importing-dataquality-throws-a-permissions-error-permissionerror)

* [**vaex-core fails to build with Python 3.10 on MacOs Monterey**](/galileo/how-to-and-faq/faqs#q-vaex-core-fails-to-build-with-python-3.10-on-macos-monterey)

* [**Training a model is really slow. Can I make it go faster?**](/galileo/how-to-and-faq/faqs#q-training-a-model-is-really-slow.-can-i-make-it-go-faster)

### Q: How do I install the Galileo Python client?

```
pip install dataquality
```

### Q: I'm seeing errors importing dataquality in Jupyter / Google Colab

Make sure you running at least `dataquality >= 0.8.6` The first thing to try in this case it to **restart your kernel**. Dataquality uses certain python packages that require your kernel to be restarted after installation. In Jupyter you can click "Kernel -> Restart"

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e896021025f22728c5dcde7a6205baf8" data-og-width="982" width="982" data-og-height="438" height="438" data-path="images/faq-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0306d24b3aa4517e725d952203d763af 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=680deb47b78f927b8cfebf9ac99f49df 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0af3a5002f57d5376c49ed754fe5c177 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9cf17dbc14987a62c95e97bc1c143965 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=27104cd2869e92b4333b7654998b565e 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-1.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e2bb704e55d185bf1525306b1965997e 2500w" />
</Frame>

In Colab you can click "Runtime -> Disconnect and delete runtime"

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b839cdd1bf4ef63c0b138c45e1294c49" data-og-width="1120" width="1120" data-og-height="686" height="686" data-path="images/fasq-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1023bf560f337e22b2a7df3dd90e7024 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=790d825de426800fa9fe13c3ead44fea 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e27e5bd7983c82a1e1663034f0294e1c 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=57a4f3fe4e0a246640962e02dde5de1f 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=27d85bd7b16a77dbc9b73ada6d6c5505 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/fasq-2.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=86b7460d61c9acd56dc9ae7f1818efba 2500w" />
</Frame>

If you already had [vaex](https://github.com/vaexio) installed on your machine prior to installing `dataquality,` there is a known bug when upgrading. **Solution:** `pip uninstall -y vaex-core vaex-hdf5 && pip install --upgrade --force-reinstall dataquality` \`\`**And then restart your jupyter/colab kernel**

### Q: My run finished, but there's no data in the console! What went wrong?

Make sure you ran `dq.finish()` after the run.

t's possible that:

* your run hasn't finished processing

* you've logged some data incorrectly

* you may have found a bug (congrats!

First, to see what happened to your data, you can run `dq.wait_for_run()` (you can optionally pass in the project and run name, or the most recent will be used)

This function will wait for your run to finish processing. If it's completed, check the console again by refreshing.

If that shows an exception, your run failed to be processed. You can see the logs from your model training by running `dq.get_dq_log_file()` which will download and return the path to your logfile. That may indicate the issue. Feel free to reach out to us for more help!

### Q: Can I log custom metadata to my dataset?

Yes (glad you asked)! You can attach any metadata fields you'd like to your original dataset, as long as they are primitive datatypes (numbers and strings).

In all available logging functions for input data, you can attach custom metadata:

```py  theme={null}
df = pd.DataFrame(
    {
        "id": [0,1,2,3],
        "text": ["sen 1","sen 2","sen 3","sen 4"],
        "label": [0, 1, 1, 0],
        "customer_score": [0.66, 0.98, 0.12, 0.05],
        "sentiment": ["happy", "sad", "happy", "angry"]
    }
)

dq.log_dataset(df, meta=["customer_score", "sentiment"])
```

```py  theme={null}
texts = [
    "Text sample 1",
    "Text sample 2",
    "Text sample 3",
    "Text sample 4"
]
labels = ["B", "C", "A", "A"]
meta = {
    "sample_importance": ["high", "low", "low", "medium"]
    "quality_ranking": [9.7, 2.4, 5.5, 1.2]
}
ids = [0, 1, 2, 3]
split = "training"

dq.log_data_samples(texts=texts, labels=labels, ids=ids, meta=meta split=split)
```

This data will show up in the console under the column dropdown

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=5e0e7258150aa42ce8c0e551f3c26dee" data-og-width="900" width="900" data-og-height="290" height="290" data-path="images/faq-8.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b6b6e271984d4487d79706d52d63a6bb 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=2bee5c49195a14216ccb0fb15919c634 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=80393718fb5a22c21936b1622b120648 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=869ef306e2d383c84999f424c4fbc8aa 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=40321df68c8f6cdce3a2414c75e237fe 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-8.avif?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=4031ce2b7162065dd38e775aa2f1762c 2500w" />
</Frame>

And you can see any performance metric grouped by your categorical metadata

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d45269c1e9a27428128ecac0bff9f463" data-og-width="786" width="786" data-og-height="1228" height="1228" data-path="images/faq-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=5a65b0f797a2a5d8adee6a52492772b1 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d05188985e94eca909987190cf242ad8 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=6ad1b5ef6e99c4a19267d4a2f6225222 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7bd6d8c6548bf167dab05d143610a30d 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e85c00c10a57f749dc15168f424ee301 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-3.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=5524d2edb0079e811ebfed00660b23de 2500w" />
</Frame>

Lastly, once active, you can further filter your data by your metadata fields, helping find high-value cohorts

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b7f88e76e8856bb3a63dd5d08b82a0f9" data-og-width="900" width="900" data-og-height="295" height="295" data-path="images/faq-4.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=16273150069525987c388e464346c88a 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=96a53cb8e0adf15787ab4d349a760dba 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7d83f923285c5c469206dbd8ba3a74f0 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=83d0bc5c2d7cfc419b419b5376701ddb 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d2f1cd9eb79980673f6aa1caf9c0fab3 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-4.avif?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e927fd1c6ed0e4c1837fd06324c984ff 2500w" />
</Frame>

\*\*\*\*

### Q: How do I disable Galileo logging during model training?

***

See Disabling Galileo

### Q: How do I load a Galileo exported file for re-training?

***

```py  theme={null}
from datasets import Dataset, dataset_dict
file_name_train = "exported_galileo_sample_file_train.parquet"
file_name_val = "exported_galileo_sample_file_val.parquet"
file_name_test = "exported_galileo_sample_file_test.parquet"
ds_train = Dataset.from_parquet(file_name_train)
ds_val = Dataset.from_parquet(file_name_val)
ds_test = Dataset.from_parquet(file_name_test)

ds_exported = dataset_dict.DatasetDict({"train": ds_train, "validation": ds_val, "test": ds_test})
labels = ds_new["train"]["ner_labels"][0]

tokenized_datasets = hf.tokenize_and_log_dataset(ds_exported, tokenizer, labels)
train_dataloader = hf.get_dataloader(tokenized_datasets["train"], collate_fn=data_collator, batch_size=MINIBATCH_SIZE, shuffle=True)
val_dataloader = hf.get_dataloader(tokenized_datasets["validation"], collate_fn=data_collator, batch_size=MINIBATCH_SIZE, shuffle=False)
test_dataloader = hf.get_dataloader(tokenized_datasets["test"], collate_fn=data_collator, batch_size=MINIBATCH_SIZE, shuffle=False)
```

### Q: How do I get my NER data into huggingface format?

***

```py  theme={null}
import dataquality as dq
from datasets import Dataset

dq.login()
# A vaex dataframe
df = dq.metrics.get_dataframe(
    project_name, run_name, split, hf_format=True, tagging_schema="BIO"
)
df.export("data.parquet")
ds = Dataset.from_parquet("data.parquet")
```

### Q: My `spans` JSON column for my NER data can't be loaded with `json.loads`

If you're seeing an error similar to: `JSONDecodeError: Expecting ',' delimiter: line 1 column 84 (char 83)` It's likely the case that you have some data in your `text` field that is not valid json (extra quotes `"` or `'`). Unfortunately, we cannot modify the content of your span text, but we can strip out the `text` field with some regex. Given a pandas dataframe `df` with column `spans` (from a Galileo export) you can replace `df["spans"] = df.apply(json.loads)` with (make sure to `import re`) `df["spans"] = df.apply(lambda row: json.loads(re.sub(r","text".}", "}", row)))`

### Q: Galileo marked an incorrect span as a span shift error, but it looks like a wrong tag error. What's going on?

Great observation! Let's take a real example below, from the WikiNER IT dataset. As you can see, the `Anemone apennina` clearly looks like a wrong tag error (correct span boundaries, incorrect class prediction), but is marked as a span shift.

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0bb6e2a7fe749275359d5c9888635ac1" data-og-width="2304" width="2304" data-og-height="348" height="348" data-path="images/faq-5.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8d18f94db21b919caa08867486c92e3f 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=153300d344524c43f983540c1189f79f 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=344589ab003f7ff386b47f2a8f99d8ab 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1d32144e5b84a7fecc670ff4512586c1 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=4c3a4c35c7637a57fb53f233ff4dc4a7 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-5.avif?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=71a6141a35520ce984ac64fd20e0068b 2500w" />
</Frame>

We can further validate this with `dq.metrics.get_dataframe`. We can see that there are 2 spans with identical character boundaries, one with a label and one without (which is the prediction span).

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=02a2a67a4382f295de3474657296705d" data-og-width="1140" width="1140" data-og-height="594" height="594" data-path="images/faq-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=cfb882e913075c6ccfa2fbdfd6552175 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=cac696201acd1d7985d745392e6155f3 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=d2fea9246bd512adf8097e62af5e5f40 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=63ebb86ed508632234d5e7940c4f9864 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=020e4682059d1cd0f8bad496d1c09ed9 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-7.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=a919e068524bd0940a36a807f5e18650 2500w" />
</Frame>

So what is going on here? When Galileo computes error types for each span, they are computed at the *byte-pair (BPE)* level using the span **token** indices, not \*\*\*\* the **character** indices. When looking at the console, however, you are seeing the **character** level indices, because that's much more intuitive view of your data. That conversion from **token** (fine-grained) to \*\*character\*\* (coarse-grained) level indices can cause index differences to overlap as a result of less-granular information.

We can again validate this with `dq.metrics` by looking at the raw data logged to Galileo. As we can see, at the **token** level, the span start and end indices do not align, and in fact overlap (ids 21948 and 21950), which is the reason for the span\_shift error <Icon icon="face-smiling-hands" />

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=3d99476a58644bf334ddc3a53e07dd4f" data-og-width="1484" width="1484" data-og-height="436" height="436" data-path="images/faq-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=bc4dd199ca95fe2405d18a4eeac975f5 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=107461535892f4fb330043e5298f2f09 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1ca16d59df90172c4ec68fa74b6712f5 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=3cc72d1a37fa12336f95b9edf6634571 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b747a59864da292a02125157527af1a9 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/faq-6.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c677cf27d497d95deb0d17215c9fad06 2500w" />
</Frame>

### Q: What do you mean when you say the deployment logs are written to Google Cloud?

We manage deployments and updates to the versions of services running in your cluster via Github Actions. Each deployment/update produces logs that go into a bucket on Galileo's cloud (GCP). During our private deployment process \*\*\*\* (for Enterprise users), we allow customers to provide us with their emails, so they can have access to these deployment logs.

### Q: Where are the client logs stored?

The client logs are stored in the home (\~) folder of the machine where the training occurs.

### Q: Does Galileo store data in the cloud?

For Enterprise Users, data does not leave the customer VPC/Data Center. For users of the Free version of our product, we store data and model outputs in secured servers in the cloud. We pride ourselves in taking data security very seriously.

### Q: Do you offer air-gapped deployments?

Yes, we do! Contact us to learn more.

### Q: How do I contact Galileo?

You can write us at team\[at]rungalileo.io

### Q: How do I convert my vaex dataframe to a pandas DataFrame when using the `dq.metrics.get_dataframe`

Simply add `dq.metrics.get_dataframe(...).to_pandas_df()`

### **Importing dataquality throws a permissions error** `**PermissionError**`

Galileo creates a folder in your system's `HOME` directory. If you are seeing a `PermissionsError` it means that your system does not have access to your current `HOME` directory. This may happen in an automated CI system like AWS Glue. To overcome this, simply change your `HOME` python Environment Variable to somewhere accessible. For example, the current directory you are in

```py  theme={null}
import os

# Set the HOME directory to the current working directory
os.environ["HOME"] = os.getcwd()
import dataquality as dq
```

This will only affect the current python runtime, it will not change your system's `HOME` directory. Because of that, if you run a new python script in this environment again, you will need to set the `HOME` variable in each new runtime.

### Q: vaex-core fails to build with Python 3.10 on MacOs Monterey

When installing dataquality with python 3.10 on MacOS Monterey you might encounter an issue when building vaex-core binaries. To fix any issues that come up, please follow the instructions in the failure output which may include running `xcodebuild -runFirstLaunch` and also allowing for any clang permission requests that pop up.

### Q: Training a model is really slow. Can I make it go faster?

For larger datasets you can speed up model training by running CUDA.

**Note: You** ***must*** **be running CUDA 11.X for this functionality to work.**

Cuda's CUML libraries require CUDA 11.X to work properly. You can check your CUDA version by running `nvcc -V`. **Do not run nvidia-smi**, that does not give you the true CUDA version. To learn more about this installation or to do it manually, see the [installation guide](https://docs.rapids.ai/install).

If you are training on datasets in the millions, and noticing that the Galileo processing is slowing down at the "Dimensionality Reduction" stage, you can optionally run those steps on the GPU/TPU that you are training your model with.

In order to leverage this feature, simply install `dataquality` with the `[cuda]` extra.

```
pip install 'dataquality[cuda]' --extra-index-url=https://pypi.nvidia.com/
```

We pass in the `extra-index-url` to the install, because the extra required packages are hosted by Nvidia, and exist on Nvidia's personal pypi repository, not the standard pypi repository.

After running that installation, dataquality will automatically pick up on the available libraries, and leverage your GPU/TPU to apply the dimensionality reduction.

**Please validate that the installation ran correctly by running** `import cuml` **in your environment.** This must complete successfully.

To manually install these packages (at your own risk), you can run

```
pip install cuml-cu11 ucx-py-cu11 rmm-cu11 raft-dask-cu11 pylibraft-cu11 dask-cudf-cu11 cudf-cu11  --extra-index-url=https://pypi.nvidia.com/
```
