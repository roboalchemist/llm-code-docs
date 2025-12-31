# Source: https://huggingface.co/docs/hub/storage-limits.md

# Storage limits

At Hugging Face we aim to provide the AI community with significant volumes of **free storage space for public repositories**. We bill for storage space for **private repositories**, above a free tier (see table below).

> [!TIP]
> Storage limits and policies apply to both model and dataset repositories on the Hub.

We [optimize our infrastructure](https://huggingface.co/blog/xethub-joins-hf) continuously to [scale our storage](https://x.com/julien_c/status/1821540661973160339) for the coming years of growth in AI and Machine learning.

We do have mitigations in place to prevent abuse of free public storage, and in general we ask users and organizations to make sure any uploaded large model or dataset is **as useful to the community as possible** (as represented by numbers of likes or downloads, for instance). Finally, upgrade to a paid Organization or User (PRO) account to unlock higher limits.

## Storage plans

| Type of account          | Public storage                                                     | Private storage              |
| ------------------------ | ------------------------------------------------------------------ | ---------------------------- |
| Free user or org         | Best-effort\* 🙏  usually up to 5TB for impactful work         | 100GB                        |
| PRO                      | Up to 10TB included\* ✅  grants available for impactful work† | 1TB + pay-as-you-go          |
| Team Organizations       | 12TB base + 1TB per seat ✅                                        | 1TB per seat + pay-as-you-go |
| Enterprise Organizations | 500TB base + 1TB per seat 🏆                                       | 1TB per seat + pay-as-you-go |

💡 [Team or Enterprise Organizations](https://huggingface.co/enterprise) include 1TB of private storage per seat in the subscription: for example, if your organization has 40 members, then you have 40TB of included private storage.

\* We aim to continue providing the AI community with generous free storage space for public repositories. Beyond the first few gigabytes, please use this resource responsibly by uploading content that offers genuine value to other users. If you need substantial storage space, you will need to upgrade to [PRO, Team or Enterprise](https://huggingface.co/pricing).

† We work with impactful community members to ensure it is as easy as possible for them to unlock large storage limits. If your models or datasets consistently get many likes and downloads and you hit limits, get in touch.

### Pay-as-you-go price

Above the included 1TB (or 1TB per seat) of private storage in [PRO](https://huggingface.co/subscribe/pro) and [Team or Enterprise Organizations](https://huggingface.co/enterprise), private storage is invoiced at **$25/TB/month**, in 1TB increments. See our [billing doc](./billing) for more details.

## Repository limitations and recommendations

In parallel to storage limits at the account (user or organization) level, there are some limitations to be aware of when dealing with a large amount of data in a specific repo. Given the time it takes to stream the data,
getting an upload/push to fail at the end of the process or encountering a degraded experience, be it on hf.co or when working locally, can be very annoying. In the following section, we describe our recommendations on how to best structure your large repos.

### Recommendations

We gathered a list of tips and recommendations for structuring your repo. If you are looking for more practical tips, check out [this guide](https://huggingface.co/docs/huggingface_hub/main/en/guides/upload#tips-and-tricks-for-large-uploads) on how to upload large amount of data using the Python library.

| Characteristic     | Recommended        | Tips                                                   |
| ----------------   | ------------------ | ------------------------------------------------------ |
| Repo size          | -                  | contact us for large repos (TBs of data)               |
| Files per repo     | 
```

For example:

```bash
git log --all -p -S 68d45e234eb4a928074dfd868cead0219ab85354cc53d20e772753c6bb9169d3

commit 5af368743e3f1d81c2a846f7c8d4a028ad9fb021
Date:   Sun Apr 28 02:01:18 2024 +0200

    Update LayerNorm tensor names to weight and bias

diff --git a/model.safetensors b/model.safetensors
index a090ee7..e79c80e 100644
--- a/model.safetensors
+++ b/model.safetensors
@@ -1,3 +1,3 @@
 version https://git-lfs.github.com/spec/v1
-oid sha256:68d45e234eb4a928074dfd868cead0219ab85354cc53d20e772753c6bb9169d3
+oid sha256:0bb7a1683251b832d6f4644e523b325adcf485b7193379f5515e6083b5ed174b
 size 440449768

commit 0a6aa9128b6194f4f3c4db429b6cb4891cdb421b (origin/pr/28)
Date:   Wed Nov 16 15:15:39 2022 +0000

    Adding `safetensors` variant of this model (#15)
    
    
    - Adding `safetensors` variant of this model (18c87780b5e54825a2454d5855a354ad46c5b87e)
    
    
    Co-authored-by: Nicolas Patry 

diff --git a/model.safetensors b/model.safetensors
new file mode 100644
index 0000000..a090ee7
--- /dev/null
+++ b/model.safetensors
@@ -0,0 +1,3 @@
+version https://git-lfs.github.com/spec/v1
+oid sha256:68d45e234eb4a928074dfd868cead0219ab85354cc53d20e772753c6bb9169d3
+size 440449768

commit 18c87780b5e54825a2454d5855a354ad46c5b87e (origin/pr/15)
Date:   Thu Nov 10 09:35:55 2022 +0000

    Adding `safetensors` variant of this model

diff --git a/model.safetensors b/model.safetensors
new file mode 100644
index 0000000..a090ee7
--- /dev/null
+++ b/model.safetensors
@@ -0,0 +1,3 @@
+version https://git-lfs.github.com/spec/v1
+oid sha256:68d45e234eb4a928074dfd868cead0219ab85354cc53d20e772753c6bb9169d3
+size 440449768

```

