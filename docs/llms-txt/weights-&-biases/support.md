# Source: https://docs.wandb.ai/support/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Support

export const HelpQuestionForm = () => {
  const [value, setValue] = useState("");
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    setValue(params.get("assistant") || "");
  }, []);
  const handleSubmit = e => {
    e.preventDefault();
    const trimmed = value.trim();
    if (!trimmed) return;
    const url = new URL(window.location.href);
    url.searchParams.set("assistant", trimmed);
    window.location.href = url.toString();
  };
  return <form onSubmit={handleSubmit} className="mb-8 mt-8">
      <div className="flex gap-2 flex-wrap">
        <input id="help-question" type="text" value={value} onChange={e => setValue(e.target.value)} placeholder="Ask your question..." className="flex-1 min-w-[200px] px-4 py-2 rounded-lg border border-zinc-950/20 dark:border-white/20 bg-white dark:bg-zinc-950 text-zinc-950 dark:text-white placeholder-zinc-500 focus:outline-none focus:ring-2 focus:ring-primary-500" aria-label="Ask your question" />
        <button type="submit" className="inline-flex items-center gap-2 whitespace-nowrap px-4 py-2 rounded-lg bg-primary text-white font-medium hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" class="size-4 shrink-0 text-gray-700 group-hover/ai:text-gray-800 dark:text-gray-400 dark:group-hover/ai:text-gray-200"><g fill="white"><path d="M5.658,2.99l-1.263-.421-.421-1.263c-.137-.408-.812-.408-.949,0l-.421,1.263-1.263,.421c-.204,.068-.342,.259-.342,.474s.138,.406,.342,.474l1.263,.421,.421,1.263c.068,.204,.26,.342,.475,.342s.406-.138,.475-.342l.421-1.263,1.263-.421c.204-.068,.342-.259,.342-.474s-.138-.406-.342-.474Z" fill="white" data-stroke="none" stroke="none"></path><polygon points="9.5 2.75 11.412 7.587 16.25 9.5 11.412 11.413 9.5 16.25 7.587 11.413 2.75 9.5 7.587 7.587 9.5 2.75" fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></polygon></g></svg>
          Ask AI
        </button>
      </div>
    </form>;
};

export const Banner = ({title, background, children, home}) => {
  useEffect(() => {
    if (home) {
      const header = document.querySelector("div#content-area > header#header");
      if (header) {
        header.style.display = "none";
      }
      const mdxContent = document.querySelector("div.mdx-content");
      if (mdxContent) {
        mdxContent.style.marginTop = "0";
      }
    }
    return () => {
      const header = document.querySelector("div#content-area > header#header");
      if (header) {
        header.style.display = "";
      }
      const mdxContent = document.querySelector("div.mdx-content");
      if (mdxContent) {
        mdxContent.style.marginTop = "";
      }
    };
  }, [home]);
  return <div className="relative w-full min-h-[200px] bg-gray-900 bg-cover bg-center bg-no-repeat rounded-lg overflow-hidden" style={{
    backgroundImage: `url('${background}')`
  }}>
      <div className="absolute inset-0 bg-black bg-opacity-40"></div>
      <div className="relative z-10 flex flex-col justify-center h-full px-8 py-12 text-white">
        <h2 className="font-serif text-2xl text-white font-normal mb-4 leading-tight mt-4">{title}</h2>
        <div className="text-gray-200 leading-relaxed">{children}</div>
      </div>
    </div>;
};

<Banner title="How can we help?" background="/images/support/support_banner.png">
  Search for help from support articles, product documentation,<br />
  and the W\&B community.
</Banner>

<HelpQuestionForm />

## Browse support articles by product

<CardGroup cols={3}>
  <Card title="W&B Models" href="/support/models/index" arrow="true" icon="https://mintcdn.com/wb-21fd5541/NC1-xMMdE5yuKjPX/icons/cropped-models.svg?fit=max&auto=format&n=NC1-xMMdE5yuKjPX&q=85&s=c23ce5a772e5247c36f9f2a734177019" width="38" height="39" data-path="icons/cropped-models.svg">
    180 articles · 33 tags
  </Card>

  <Card title="W&B Weave" href="/support/weave/index" arrow="true" icon="https://mintcdn.com/wb-21fd5541/NC1-xMMdE5yuKjPX/icons/cropped-weave.svg?fit=max&auto=format&n=NC1-xMMdE5yuKjPX&q=85&s=ae6c5f30b6a30aa030c28d10bb2feca7" width="31" height="36" data-path="icons/cropped-weave.svg">
    15 articles · 8 tags
  </Card>

  <Card title="W&B Inference" href="/support/inference/index" arrow="true" icon="https://mintcdn.com/wb-21fd5541/NC1-xMMdE5yuKjPX/icons/cropped-inference.svg?fit=max&auto=format&n=NC1-xMMdE5yuKjPX&q=85&s=57f50ec28879b79645577e85c4a78494" width="42" height="35" data-path="icons/cropped-inference.svg">
    7 articles · 5 tags
  </Card>
</CardGroup>

## Featured articles

### W\&B Models

<Card title="How can I configure the name of the run in my training code?" href="/support/models/articles/how-can-i-configure-the-name-of-the-run-" arrow="true" horizontal>
  At the beginning of the training script, call wandb.init wit...

  <Badge stroke shape="pill" color="orange" size="md">[Experiments](/support/models/tags/experiments)</Badge>
</Card>

<Card title="How do I use custom CLI commands with sweeps?" href="/support/models/articles/how-do-i-use-custom-cli-commands-with-sw" arrow="true" horizontal>
  You can use W\&B Sweeps with custom CLI commands if training ...

  <Badge stroke shape="pill" color="orange" size="md">[Sweeps](/support/models/tags/sweeps)</Badge>
</Card>

<Card title="Is it possible to save metrics offline and sync them to W&B later?" href="/support/models/articles/is-it-possible-to-save-metrics-offline-a" arrow="true" horizontal>
  By default, wandb.init starts a process that syncs metrics i...

  <Badge stroke shape="pill" color="orange" size="md">[Experiments](/support/models/tags/experiments)</Badge> <Badge stroke shape="pill" color="orange" size="md">[Environment Variables](/support/models/tags/environment-variables)</Badge> <Badge stroke shape="pill" color="orange" size="md">[Metrics](/support/models/tags/metrics)</Badge>
</Card>

<Card title="What does wandb.init do to my training process?" href="/support/models/articles/what-does-wandbinit-do-to-my-training-pr" arrow="true" horizontal>
  When wandb.init runs in a training script, an API call creat...

  <Badge stroke shape="pill" color="orange" size="md">[Environment Variables](/support/models/tags/environment-variables)</Badge> <Badge stroke shape="pill" color="orange" size="md">[Experiments](/support/models/tags/experiments)</Badge>
</Card>

<Card title="Still can't find what you are looking for?" href="mailto:support@wandb.com" icon="circle-info">
  Contact support
</Card>
