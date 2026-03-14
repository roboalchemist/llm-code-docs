# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst.md

# EnateAI - AI Analyst (Beta)

With the release of Enate AI's latest offering - AI Analyst - we're taking a significant step forward to let you seamlessly integrate AI-driven activities throughout your business process.

We're partnering with Microsoft on this to use the power of their very latest OpenAI technology right at the heart of things. So if you can ask OpenAI to perform a task, with EnateAI Analyst you can embed that to run automatically as part of your business process flow.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTY0ODMwMw==>" %}

You can add AI Analyst Actions throughout your cases and ask it to analyse documents which you supply it. You can massively reduce the time spent having to wade through huge data files performing intricate analysis, freeing up time for more valuable work.

The possibilities here are almost endless, and the power you've got at your fingertips is matched only by how simple it is to set up. There's no coding and you don't have to change a thing - just tell the system what the business rules are to run an analysis task and it will get on with it.

{% hint style="warning" %}
An important thing to note here: For the moment, this feature is being released in BETA only. As such, **it should not be used yet for full production purposes just yet.** You can however, start to test it out with real scenarios.&#x20;
{% endhint %}

Here's how you can get started setting up AI Analyst&#x20;

## Setting up an AI Analyst Action

Adding AI Analyst into your business processes is very simple to set up. Once you've switched on the 'AI Analyst' integration in Builder's Marketplace section, any time you want to create a new AI Analyst action to perform a specialist analysis activity, the steps are as follows:

1. **Create a new AI Policy** in the AI Analyst Configuration section of System Settings in Builder
2. **Test this policy with sample data** until you're happy with the output, then **Set Live**.
3. **Add 'AI Analyst' actions into your case process**, linking this to your new AI Policy. (Note: You will need to add a manual action directly after the AI Analyst action)

### Sample AI Policies

Creating a new AI Policy is simple - no code is required, you can simply write out the business rules / logic / policy for the activity in normal business language and the AI will understand it. You can easily get started by simply porting across the details of your business policy direct into an Enate AI Policy.

Take a look at some sample policy prompts to see what a policy might look like..

{% content-ref url="enateai-ai-analyst/ai-prompts" %}
[ai-prompts](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts)
{% endcontent-ref %}

### Switch on AI Analyst Integration in Marketplace

Go to the Marketplace section of Builder and filter down to 'AI Analyst'. Activate the EnateAI - AI Analyst Integration

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFbeX3dwmgW4ky0Rh5ewO%2FAIAnalyst1.png?alt=media&#x26;token=b1a6146c-5e83-4210-b9ec-2a2aa9c02763" alt=""><figcaption></figcaption></figure>

### Creating an AI Policy

Go to the 'AI Analyst Configuration' section of System Settings, and click to 'Create a Policy'. This will display an AI Policy for you to start to fill in with details of the analysis activity you want AI to undertake for you. Remember, you can just write this in normal business terms (see the prompts section for examples of this).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F8kquuUYdeHnRS0kCUwbb%2Fimage.png?alt=media&#x26;token=5acecc15-5c36-48bb-b385-fd1772ba53aa" alt=""><figcaption></figcaption></figure>

#### Components of an AI Policy

Here is the information you can define when setting up a new AI Policy:

* **Name** - give your Policy a sensible name so it can easily be identified from a list of other Policies, e.g. 'Invoice / Credit Note Reconciliation.
* **Input File Tags** - At runtime your AI will analyse one or more documents as its input. You can test with sample ones while you build, but at runtime you need to tell the system which files to grab. Setting the file Tags here tells the AI 'at runtime, grab the files in the Action which have these tags, and use them as your source for analysing. Examples might be: 'Bank File', 'HR Update', 'State Tax Rules'.
* **Output File Tag** - If your policy instructions ask for output to be provided in a file, you may want to tag that output file too, for easier use by other systems downstream. Example 'AI Reconciled'
* **AI Persona** - For best results when creating a policy with instructions prompts, it's good to give the AI as much context as you can - one important way to do this is to say what kind of person they should act as, e.g. 'Do this analysis activity as if you were a Bank clerk', or an HR executive, or an Accounts Payable expert. You should either define a new person here for your policy, or pick from the existing list if the relevant persona has already been defined.
* **Instructions for AI** - This is where the details of your instructions to the AI will go. This can simply be a copy/paste of your company policy for carrying out the activity, the rules and regulations for what to do, and how you'd like to receive the output.
* **AI Creativity Level -** This will produce subtly different output depending on the setting. you can choose to have a play around wither depending on what type of analysis you're asking for here. It defaults to a 'balanced' setting, but there's options to make the responses more creative or more precision-focused.

### Creating an AI Persona

A well-defined persona for your AI Analyst activity helps the AI do a better job when analysing and returning data to you. If the persona you're looking for isn't in the list to choose from, you should define one for this policy. At runtime, the AI will use this as input along with the more detailed instructions when determining what to do.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYVOsrt45gIEzJfmMjAjZ%2Fimage.png?alt=media&#x26;token=5700272a-058e-4722-82cd-7d16efad7fe8" alt=""><figcaption></figcaption></figure>

### Writing Instructions for AI&#x20;

Here's whether the main part of the input instructions to the AI get defined. Remember you don't need to be writing this as code, in fact it works much more effectively if you don't. If you've got existing rules and regulations which define that task, paste them in here and test your output.

When you're writing instructions that involve heavy reference of e.g. Excel sheet columns, you'll obviously have to write something adequately detailed and precise which refers to them accurately, a good guide is still to write it in a way that you would be explaining it to someone you wanted to carry out the activity (example as below shows detailed column references but then a more human "it won't be a perfect match but it should appear in there somewhere".

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLNSveltb7FPzult1wei9%2Fimage.png?alt=media&#x26;token=239f6f1a-1747-42f5-b2b1-344e18248c2f" alt=""><figcaption></figcaption></figure>

Be clear about exactly what you want the AI to do, and how you'd like to receive your output. For examples and notes on how to write good AI prompts for activities such as this, [check out this section](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts).

### Format for referencing your input documents within your instructions

While there are no fixed rules on how you format your instructions, if you want to make explicit reference to any of your Input documents, you can do so using a {{FileTag:NAME}} format. For example if you're created a tag called 'Bank', you can refer to this document in your instructions as **{{FileTag:Bank}}**

### Sample AI prompts

For more information and samples on how to write instructions, check out the link below:

{% content-ref url="enateai-ai-analyst/ai-prompts" %}
[ai-prompts](https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts)
{% endcontent-ref %}

## Testing your AI Policy

Once you're happy with all your policy input settings, the next step is to test it.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFsYaXHJeZKkiw2h3omc1%2Fimage.png?alt=media&#x26;token=35ecac46-8baa-40ad-8c1f-6a0135649d7b" alt=""><figcaption></figcaption></figure>

You'll be asked to upload a sample document for each input file tag you've specified. Once you've uploaded these you can run your test.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ftd4NPtuiBKyAroh1bQpN%2Fimage.png?alt=media&#x26;token=7614698e-dbf4-4e00-8091-3b3b778e42ec" alt=""><figcaption></figcaption></figure>

Once you have clicked to run your policy test, you will be taken to the ‘Test AI Policy’ screen. You'll see the first of three Testing sections (since you can test up to two further iterations of your policy after the first test).&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FK54fXD2AJaJ91Ngg54QC%2Fimage.png?alt=media&#x26;token=56a2d041-faa9-4f0e-8366-bcd0d7cdcb0c" alt=""><figcaption></figcaption></figure>

The prompt that you created for the AI Policy will be visible on screen and once the result has been returned, you will see either an output file or an error message will appear in the section above the prompt.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOd8MIaxnmk8TNgtGugR8%2Fimage.png?alt=media&#x26;token=c55af36e-cffa-49e5-aa14-192e72c06dd7" alt=""><figcaption></figcaption></figure>

Once you've viewed your test results, if you're happy with the output of the test you can go ahead and click to 'Save & Set This Policy Live', or just 'Save this Policy' if you don't yet wish to set live. Alternatively, you *can* choose to iterate your prompt with the help of AI..

#### Choosing to Iterate the prompt with AI

If you're not happy with the results you can select the 'Use AI to Iterate Prompt' button in the second section. The AI will then iterate the prompt used in the first test to improve it, and will then immediately rerun the test. You will be able to see the adjusted prompt text while you wait for the second test to complete running.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F1SHsijrNfVvVpnNFUyh0%2Fimage.png?alt=media&#x26;token=f95d2887-92b1-4c00-9719-52ad25f8b6e5" alt=""><figcaption></figcaption></figure>

Once the second test has been completed, you'll have exactly the same options available to you for the Policy for a final time: Save it; Save it & Set Live; or choose to iterate with AI and run the test one last time.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjKMkViQH3NTBZYlYbhF2%2Fimage.png?alt=media&#x26;token=e99e0541-1366-44c2-8205-54828ed011e8" alt=""><figcaption></figcaption></figure>

At any point you can choose which iteration of the prompt you wish to save or save and set live. Please note that once all three versions of the prompt have been tested, if you're still not happy with the results  you will need to start the process again in order to generate any further sets of test results.

## Adding AI Analyst Action into a Case process

Once you've set your new AI policy Live, all you need to do now is add an AI Analyst action into your case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FsG2TU4HDfuxGQ8z4Fir4%2Fimage.png?alt=media&#x26;token=ab820f73-a7ad-4f75-b1e0-9f76917b2fc0" alt=""><figcaption></figcaption></figure>

As part of the configuration, set your new AI Policy as the one which this action should use.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBEvMEkpnWsG2qdtQGuj4%2Fimage.png?alt=media&#x26;token=190b591a-92da-4a60-8622-61d399853fc2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Additional Requirement: When adding an AI Analyst Action into a Case flow, **you MUST also add a further action immediately after it in your flow which would allow an Agent to review the output of the AI Action**. This can be an action of type 'Manual', 'Manual with Peer Review' or 'Approval'. If you do not add an action like this immediately downstream of the AI Action, you will see a validation message when saving the Case process.
{% endhint %}

## Limitations of AI Analyst While in BETA Release

{% hint style="warning" %}
While the AI Analyst feature is released in Beta only, it should not be used for full production purposes, although can obviously be used to test the functionality. For now, the current feature can be used with the following known limitations, which will reduce over time as the underlying AI technology beds in:
{% endhint %}

1. Multiple output files cannot currently be generated&#x20;
2. If functions timeout in Azure, the AI Analyst action's status will remain set as 'In Progress', due to abruptly terminating Azure function (this should not be a problem in production environment)
3. AI reads a maximum of 100 rows currently, and is dependent on server availability (files of more than 100 rows of data are currently not allowed)
4. In case if AI fails to make a decision or a tasks defined in policy it will provide an error file (only if you defined that in AI policy prompt)
5. The following file formats are currently supported: \['c', 'cpp', 'csv', 'docx', 'html', 'java', 'json', 'md', 'pdf', 'php', 'pptx', 'py', 'rb', 'tex', 'txt', 'css', 'jpeg', 'jpg', 'js', 'gif', 'png', 'tar', 'ts', 'xlsx', 'xml', 'zip']
