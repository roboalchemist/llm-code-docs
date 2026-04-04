# Source: https://docs.wandb.ai/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Weights & Biases Documentation

> View the documentation for all Weights & Biases products

export const ProductCard = ({title, iconSrc, href, subtitle, children, className = ''}) => {
  const handleCardClick = e => {
    let target = e.target;
    while (target && target !== e.currentTarget) {
      if (target.tagName === 'A') {
        return;
      }
      target = target.parentElement;
    }
    if (href) {
      window.location.href = href;
    }
  };
  return <div className="group flex overflow-hidden rounded-lg border border-gray-200 dark:border-gray-800 hover:shadow-md transition-all p-6" onClick={handleCardClick} style={{
    cursor: href ? 'pointer' : 'default'
  }}>
      {}
      {iconSrc && <div className="flex-shrink-0 mr-4" style={{
    marginTop: '-12px'
  }}>
          <img src={iconSrc} alt={title} width="60" height="60" className="w-[60px] h-[60px]" />
        </div>}
      
      {}
      <div className="flex-1">
        <h2 className="text-xl font-normal mb-2" style={{
    fontFamily: '"Source Serif 4", serif'
  }}>
          {title}
        </h2>
        {subtitle && <h3 className="text-base font-semibold mb-3 text-gray-700 dark:text-gray-300">
            {subtitle}
          </h3>}
        <div className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">
          {children}
        </div>
      </div>
    </div>;
};

export const HomeWrapper = ({children, padding = "0"}) => {
  return <div className={padding}>{children}</div>;
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

<HomeWrapper>
  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
    <ProductCard title="W&B Models" iconSrc="icons/cropped-models.svg" href="/models" subtitle="Develop AI models">
      Use W\&B Models to manage AI model development. Features include training, fine-tuning, reporting, automating hyperparameter sweeps, and utilizing the model registry for versioning and reproducibility.

      <br />

      <br />

      • <a href="/models">Introduction</a><br />
      • <a href="/models/quickstart">Quickstart</a><br />
      • <a href="https://www.youtube.com/watch?v=tHAFujRhZLA">YouTube Tutorial</a><br />
    </ProductCard>

    <ProductCard title="W&B Weave" iconSrc="icons/cropped-weave.svg" href="/weave" subtitle="Use AI models in your app">
      Use W\&B Weave to manage AI models in your code. Features include tracing, output evaluation, cost estimates, and a hosted inference service and playground for comparing different large language models (LLMs) and settings.

      <br />

      <br />

      • <a href="/weave">Introduction</a><br />
      • <a href="/weave/quickstart">Quickstart</a><br />
      • <a href="https://www.youtube.com/watch?v=IQcGGNLN3zo">YouTube Demo</a><br />
    </ProductCard>

    <ProductCard title="W&B Inference" iconSrc="icons/cropped-inference.svg" href="/inference" subtitle="Access foundation models">
      Use W\&B Inference to access leading open-source foundation models through an OpenAI-compatible API. Features include multiple model options, usage tracking, and integration with Weave for tracing and evaluation.

      <br />

      <br />

      • <a href="/inference">Introduction</a><br />
      • <a href="https://wandb.ai/inference">Try in Playground</a>
    </ProductCard>

    <ProductCard title="W&B Training" iconSrc="icons/cropped-training.svg" href="/training" subtitle="Post-train your models">
      Now in public preview, use W\&B Training to post-train large language models using serverless reinforcement learning (RL). Features include fully managed GPU infrastructure, integration with ART and RULER, and automatic scaling for multi-turn agentic tasks.

      <br />

      <br />

      • <a href="/training">Introduction</a><br />
      • <a href="/training/prerequisites">Quickstart</a><br />
    </ProductCard>
  </div>
</HomeWrapper>
