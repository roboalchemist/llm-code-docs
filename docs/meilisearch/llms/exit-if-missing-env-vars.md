# exit if missing env vars
if "MEILI_HTTP_ADDR" not in os.environ:
    raise Exception("Missing MEILI_HTTP_ADDR env var")
if "MEILI_API_KEY" not in os.environ:
    raise Exception("Missing MEILI_API_KEY env var")
if "OPENAI_API_KEY" not in os.environ:
    raise Exception("Missing OPENAI_API_KEY env var")