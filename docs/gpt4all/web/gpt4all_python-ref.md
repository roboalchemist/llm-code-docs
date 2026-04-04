# GPT4All Documentation

Source: https://docs.gpt4all.io/gpt4all_python/ref.html

---

[ ![logo](../assets/nomic.png) ](../index.html "GPT4All") GPT4All

[ nomic-ai/gpt4all  ](https://github.com/nomic-ai/gpt4all "Go to repository")

  * [ GPT4All Documentation  ](../index.html)
  * [ Quickstart  ](../gpt4all_desktop/quickstart.html)
  * [ Chats  ](../gpt4all_desktop/chats.html)
  * [ Models  ](../gpt4all_desktop/models.html)
  * [ LocalDocs  ](../gpt4all_desktop/localdocs.html)
  * [ Settings  ](../gpt4all_desktop/settings.html)
  * [ Chat Templates  ](../gpt4all_desktop/chat_templates.html)
  * Cookbook  Cookbook 
    * [ Local AI Chat with Microsoft Excel  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-microsoft-excel.html)
    * [ Local AI Chat with your Google Drive  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-google-drive.html)
    * [ Local AI Chat with your Obsidian Vault  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-Obsidian.html)
    * [ Local AI Chat with your OneDrive  ](../gpt4all_desktop/cookbook/use-local-ai-models-to-privately-chat-with-One-Drive.html)
  * API Server  API Server 
    * [ GPT4All API Server  ](../gpt4all_api_server/home.html)
  * Python SDK  Python SDK 
    * [ GPT4All Python SDK  ](home.html)
    * [ Monitoring  ](monitoring.html)
    * SDK Reference  [ SDK Reference  ](ref.html) Table of contents 
      * GPT4All 
        * backend 
        * device 
        * __init__ 
        * chat_session 
        * close 
        * download_model 
        * generate 
        * list_gpus 
        * list_models 
        * retrieve_model 
      * Embed4All 
        * __init__ 
        * close 
        * embed 
  * Help  Help 
    * [ FAQ  ](../gpt4all_help/faq.html)
    * [ Troubleshooting  ](../gpt4all_help/troubleshooting.html)

Table of contents

  * GPT4All 
    * backend 
    * device 
    * __init__ 
    * chat_session 
    * close 
    * download_model 
    * generate 
    * list_gpus 
    * list_models 
    * retrieve_model 
  * Embed4All 
    * __init__ 
    * close 
    * embed 

# GPT4All Python SDK Reference

####  `GPT4All`

Python class that handles instantiation, downloading, generation and chat with
GPT4All models.

Source code in `gpt4all/gpt4all.py`

    
    
    191
    192
    193
    194
    195
    196
    197
    198
    199
    200
    201
    202
    203
    204
    205
    206
    207
    208
    209
    210
    211
    212
    213
    214
    215
    216
    217
    218
    219
    220
    221
    222
    223
    224
    225
    226
    227
    228
    229
    230
    231
    232
    233
    234
    235
    236
    237
    238
    239
    240
    241
    242
    243
    244
    245
    246
    247
    248
    249
    250
    251
    252
    253
    254
    255
    256
    257
    258
    259
    260
    261
    262
    263
    264
    265
    266
    267
    268
    269
    270
    271
    272
    273
    274
    275
    276
    277
    278
    279
    280
    281
    282
    283
    284
    285
    286
    287
    288
    289
    290
    291
    292
    293
    294
    295
    296
    297
    298
    299
    300
    301
    302
    303
    304
    305
    306
    307
    308
    309
    310
    311
    312
    313
    314
    315
    316
    317
    318
    319
    320
    321
    322
    323
    324
    325
    326
    327
    328
    329
    330
    331
    332
    333
    334
    335
    336
    337
    338
    339
    340
    341
    342
    343
    344
    345
    346
    347
    348
    349
    350
    351
    352
    353
    354
    355
    356
    357
    358
    359
    360
    361
    362
    363
    364
    365
    366
    367
    368
    369
    370
    371
    372
    373
    374
    375
    376
    377
    378
    379
    380
    381
    382
    383
    384
    385
    386
    387
    388
    389
    390
    391
    392
    393
    394
    395
    396
    397
    398
    399
    400
    401
    402
    403
    404
    405
    406
    407
    408
    409
    410
    411
    412
    413
    414
    415
    416
    417
    418
    419
    420
    421
    422
    423
    424
    425
    426
    427
    428
    429
    430
    431
    432
    433
    434
    435
    436
    437
    438
    439
    440
    441
    442
    443
    444
    445
    446
    447
    448
    449
    450
    451
    452
    453
    454
    455
    456
    457
    458
    459
    460
    461
    462
    463
    464
    465
    466
    467
    468
    469
    470
    471
    472
    473
    474
    475
    476
    477
    478
    479
    480
    481
    482
    483
    484
    485
    486
    487
    488
    489
    490
    491
    492
    493
    494
    495
    496
    497
    498
    499
    500
    501
    502
    503
    504
    505
    506
    507
    508
    509
    510
    511
    512
    513
    514
    515
    516
    517
    518
    519
    520
    521
    522
    523
    524
    525
    526
    527
    528
    529
    530
    531
    532
    533
    534
    535
    536
    537
    538
    539
    540
    541
    542
    543
    544
    545
    546
    547
    548
    549
    550
    551
    552
    553
    554
    555
    556
    557
    558
    559
    560
    561
    562
    563
    564
    565
    566
    567
    568
    569
    570
    571
    572
    573
    574
    575
    576
    577
    578
    579
    580
    581
    582
    583
    584
    585
    586
    587
    588
    589
    590
    591
    592
    593
    594
    595
    596
    597
    598
    599
    600
    601
    602
    603
    604
    605
    606
    607
    608
    609
    610
    611
    612
    613
    614
    615
    616
    617
    618
    619
    620
    621
    622
    623
    624
    625
    626
    627
    628
    629
    630
    631
    632
    633
    634
    635
    636
    637
    638
    639
    640
    641
    642
    643
    644
    645
    646
    647
    648

|

    
    
    class GPT4All:
        """
        Python class that handles instantiation, downloading, generation and chat with GPT4All models.
        """
    
        def __init__(
            self,
            model_name: str,
            *,
            model_path: str | os.PathLike[str] | None = None,
            model_type: str | None = None,
            allow_download: bool = True,
            n_threads: int | None = None,
            device: str | None = None,
            n_ctx: int = 2048,
            ngl: int = 100,
            verbose: bool = False,
        ):
            """
            Constructor
    
            Args:
                model_name: Name of GPT4All or custom model. Including ".gguf" file extension is optional but encouraged.
                model_path: Path to directory containing model file or, if file does not exist, where to download model.
                    Default is None, in which case models will be stored in `~/.cache/gpt4all/`.
                model_type: Model architecture. This argument currently does not have any functionality and is just used as
                    descriptive identifier for user. Default is None.
                allow_download: Allow API to download models from gpt4all.io. Default is True.
                n_threads: number of CPU threads used by GPT4All. Default is None, then the number of threads are determined automatically.
                device: The processing unit on which the GPT4All model will run. It can be set to:
                    - "cpu": Model will run on the central processing unit.
                    - "gpu": Use Metal on ARM64 macOS, otherwise the same as "kompute".
                    - "kompute": Use the best GPU provided by the Kompute backend.
                    - "cuda": Use the best GPU provided by the CUDA backend.
                    - "amd", "nvidia": Use the best GPU provided by the Kompute backend from this vendor.
                    - A specific device name from the list returned by `GPT4All.list_gpus()`.
                    Default is Metal on ARM64 macOS, "cpu" otherwise.
    
                    Note: If a selected GPU device does not have sufficient RAM to accommodate the model, an error will be thrown, and the GPT4All instance will be rendered invalid. It's advised to ensure the device has enough memory before initiating the model.
                n_ctx: Maximum size of context window
                ngl: Number of GPU layers to use (Vulkan)
                verbose: If True, print debug messages.
            """
    
            self.model_type = model_type
            self._chat_session: ChatSession | None = None
    
            device_init = None
            if sys.platform == "darwin":
                if device is None:
                    backend = "auto"  # "auto" is effectively "metal" due to currently non-functional fallback
                elif device == "cpu":
                    backend = "cpu"
                else:
                    if platform.machine() != "arm64" or device != "gpu":
                        raise ValueError(f"Unknown device for this platform: {device}")
                    backend = "metal"
            else:
                backend = "kompute"
                if device is None or device == "cpu":
                    pass  # use kompute with no device
                elif device in ("cuda", "kompute"):
                    backend = device
                    device_init = "gpu"
                elif device.startswith("cuda:"):
                    backend = "cuda"
                    device_init = _remove_prefix(device, "cuda:")
                else:
                    device_init = _remove_prefix(device, "kompute:")
    
            # Retrieve model and download if allowed
            self.config: ConfigType = self.retrieve_model(model_name, model_path=model_path, allow_download=allow_download, verbose=verbose)
            self.model = LLModel(self.config["path"], n_ctx, ngl, backend)
            if device_init is not None:
                self.model.init_gpu(device_init)
            self.model.load_model()
            # Set n_threads
            if n_threads is not None:
                self.model.set_thread_count(n_threads)
    
        def __enter__(self) -> Self:
            return self
    
        def __exit__(
            self, typ: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None,
        ) -> None:
            self.close()
    
        def close(self) -> None:
            """Delete the model instance and free associated system resources."""
            self.model.close()
    
        @property
        def backend(self) -> Literal["cpu", "kompute", "cuda", "metal"]:
            """The name of the llama.cpp backend currently in use. One of "cpu", "kompute", "cuda", or "metal"."""
            return self.model.backend
    
        @property
        def device(self) -> str | None:
            """The name of the GPU device currently in use, or None for backends other than Kompute or CUDA."""
            return self.model.device
    
        @property
        def current_chat_session(self) -> list[MessageType] | None:
            return None if self._chat_session is None else self._chat_session.history
    
        @current_chat_session.setter
        def current_chat_session(self, history: list[MessageType]) -> None:
            if self._chat_session is None:
                raise ValueError("current_chat_session may only be set when there is an active chat session")
            self._chat_session.history[:] = history
    
        @staticmethod
        def list_models() -> list[ConfigType]:
            """
            Fetch model list from https://gpt4all.io/models/models3.json.
    
            Returns:
                Model list in JSON format.
            """
            resp = requests.get("https://gpt4all.io/models/models3.json")
            if resp.status_code != 200:
                raise ValueError(f"Request failed: HTTP {resp.status_code} {resp.reason}")
            return resp.json()
    
        @classmethod
        def retrieve_model(
            cls,
            model_name: str,
            model_path: str | os.PathLike[str] | None = None,
            allow_download: bool = True,
            verbose: bool = False,
        ) -> ConfigType:
            """
            Find model file, and if it doesn't exist, download the model.
    
            Args:
                model_name: Name of model.
                model_path: Path to find model. Default is None in which case path is set to
                    ~/.cache/gpt4all/.
                allow_download: Allow API to download model from gpt4all.io. Default is True.
                verbose: If True (default), print debug messages.
    
            Returns:
                Model config.
            """
    
            model_filename = append_extension_if_missing(model_name)
    
            # get the config for the model
            config: ConfigType = {}
            if allow_download:
                models = cls.list_models()
                if (model := next((m for m in models if m["filename"] == model_filename), None)) is not None:
                    config.update(model)
    
            # Validate download directory
            if model_path is None:
                try:
                    os.makedirs(DEFAULT_MODEL_DIRECTORY, exist_ok=True)
                except OSError as e:
                    raise RuntimeError("Failed to create model download directory") from e
                model_path = DEFAULT_MODEL_DIRECTORY
            else:
                model_path = Path(model_path)
    
            if not model_path.exists():
                raise FileNotFoundError(f"Model directory does not exist: {model_path!r}")
    
            model_dest = model_path / model_filename
            if model_dest.exists():
                config["path"] = str(model_dest)
                if verbose:
                    print(f"Found model file at {str(model_dest)!r}", file=sys.stderr)
            elif allow_download:
                # If model file does not exist, download
                filesize = config.get("filesize")
                config["path"] = str(cls.download_model(
                    model_filename, model_path, verbose=verbose, url=config.get("url"),
                    expected_size=None if filesize is None else int(filesize), expected_md5=config.get("md5sum"),
                ))
            else:
                raise FileNotFoundError(f"Model file does not exist: {model_dest!r}")
    
            return config
    
        @staticmethod
        def download_model(
            model_filename: str,
            model_path: str | os.PathLike[str],
            verbose: bool = True,
            url: str | None = None,
            expected_size: int | None = None,
            expected_md5: str | None = None,
        ) -> str | os.PathLike[str]:
            """
            Download model from gpt4all.io.
    
            Args:
                model_filename: Filename of model (with .gguf extension).
                model_path: Path to download model to.
                verbose: If True (default), print debug messages.
                url: the models remote url (e.g. may be hosted on HF)
                expected_size: The expected size of the download.
                expected_md5: The expected MD5 hash of the download.
    
            Returns:
                Model file destination.
            """
    
            # Download model
            if url is None:
                url = f"https://gpt4all.io/models/gguf/{model_filename}"
    
            def make_request(offset=None):
                headers = {}
                if offset:
                    print(f"\nDownload interrupted, resuming from byte position {offset}", file=sys.stderr)
                    headers["Range"] = f"bytes={offset}-"  # resume incomplete response
                    headers["Accept-Encoding"] = "identity"  # Content-Encoding changes meaning of ranges
                response = requests.get(url, stream=True, headers=headers)
                if response.status_code not in (200, 206):
                    raise ValueError(f"Request failed: HTTP {response.status_code} {response.reason}")
                if offset and (response.status_code != 206 or str(offset) not in response.headers.get("Content-Range", "")):
                    raise ValueError("Connection was interrupted and server does not support range requests")
                if (enc := response.headers.get("Content-Encoding")) is not None:
                    raise ValueError(f"Expected identity Content-Encoding, got {enc}")
                return response
    
            response = make_request()
    
            total_size_in_bytes = int(response.headers.get("content-length", 0))
            block_size = 2**20  # 1 MB
    
            partial_path = Path(model_path) / (model_filename + ".part")
    
            with open(partial_path, "w+b") as partf:
                try:
                    with tqdm(desc="Downloading", total=total_size_in_bytes, unit="iB", unit_scale=True) as progress_bar:
                        while True:
                            last_progress = progress_bar.n
                            try:
                                for data in response.iter_content(block_size):
                                    partf.write(data)
                                    progress_bar.update(len(data))
                            except ChunkedEncodingError as cee:
                                if cee.args and isinstance(pe := cee.args[0], ProtocolError):
                                    if len(pe.args) >= 2 and isinstance(ir := pe.args[1], IncompleteRead):
                                        assert progress_bar.n <= ir.partial  # urllib3 may be ahead of us but never behind
                                        # the socket was closed during a read - retry
                                        response = make_request(progress_bar.n)
                                        continue
                                raise
                            if total_size_in_bytes != 0 and progress_bar.n < total_size_in_bytes:
                                if progress_bar.n == last_progress:
                                    raise RuntimeError("Download not making progress, aborting.")
                                # server closed connection prematurely - retry
                                response = make_request(progress_bar.n)
                                continue
                            break
    
                    # verify file integrity
                    file_size = partf.tell()
                    if expected_size is not None and file_size != expected_size:
                        raise ValueError(f"Expected file size of {expected_size} bytes, got {file_size}")
                    if expected_md5 is not None:
                        partf.seek(0)
                        hsh = hashlib.md5()
                        with tqdm(desc="Verifying", total=file_size, unit="iB", unit_scale=True) as bar:
                            while chunk := partf.read(block_size):
                                hsh.update(chunk)
                                bar.update(len(chunk))
                        if hsh.hexdigest() != expected_md5.lower():
                            raise ValueError(f"Expected MD5 hash of {expected_md5!r}, got {hsh.hexdigest()!r}")
                except:
                    if verbose:
                        print("Cleaning up the interrupted download...", file=sys.stderr)
                    try:
                        os.remove(partial_path)
                    except OSError:
                        pass
                    raise
    
                # flush buffers and sync the inode
                partf.flush()
                _fsync(partf)
    
            # move to final destination
            download_path = Path(model_path) / model_filename
            try:
                os.rename(partial_path, download_path)
            except FileExistsError:
                try:
                    os.remove(partial_path)
                except OSError:
                    pass
                raise
    
            if verbose:
                print(f"Model downloaded to {str(download_path)!r}", file=sys.stderr)
            return download_path
    
        @overload
        def generate(
            self, prompt: str, *, max_tokens: int = ..., temp: float = ..., top_k: int = ..., top_p: float = ...,
            min_p: float = ..., repeat_penalty: float = ..., repeat_last_n: int = ..., n_batch: int = ...,
            n_predict: int | None = ..., streaming: Literal[False] = ..., callback: ResponseCallbackType = ...,
        ) -> str: ...
        @overload
        def generate(
            self, prompt: str, *, max_tokens: int = ..., temp: float = ..., top_k: int = ..., top_p: float = ...,
            min_p: float = ..., repeat_penalty: float = ..., repeat_last_n: int = ..., n_batch: int = ...,
            n_predict: int | None = ..., streaming: Literal[True], callback: ResponseCallbackType = ...,
        ) -> Iterable[str]: ...
        @overload
        def generate(
            self, prompt: str, *, max_tokens: int = ..., temp: float = ..., top_k: int = ..., top_p: float = ...,
            min_p: float = ..., repeat_penalty: float = ..., repeat_last_n: int = ..., n_batch: int = ...,
            n_predict: int | None = ..., streaming: bool, callback: ResponseCallbackType = ...,
        ) -> Any: ...
    
        def generate(
            self,
            prompt         : str,
            *,
            max_tokens     : int                  = 200,
            temp           : float                = 0.7,
            top_k          : int                  = 40,
            top_p          : float                = 0.4,
            min_p          : float                = 0.0,
            repeat_penalty : float                = 1.18,
            repeat_last_n  : int                  = 64,
            n_batch        : int                  = 8,
            n_predict      : int | None           = None,
            streaming      : bool                 = False,
            callback       : ResponseCallbackType = empty_response_callback,
        ) -> Any:
            """
            Generate outputs from any GPT4All model.
    
            Args:
                prompt: The prompt for the model to complete.
                max_tokens: The maximum number of tokens to generate.
                temp: The model temperature. Larger values increase creativity but decrease factuality.
                top_k: Randomly sample from the top_k most likely tokens at each generation step. Set this to 1 for greedy decoding.
                top_p: Randomly sample at each generation step from the top most likely tokens whose probabilities add up to top_p.
                min_p: Randomly sample at each generation step from the top most likely tokens whose probabilities are at least min_p.
                repeat_penalty: Penalize the model for repetition. Higher values result in less repetition.
                repeat_last_n: How far in the models generation history to apply the repeat penalty.
                n_batch: Number of prompt tokens processed in parallel. Larger values decrease latency but increase resource requirements.
                n_predict: Equivalent to max_tokens, exists for backwards compatibility.
                streaming: If True, this method will instead return a generator that yields tokens as the model generates them.
                callback: A function with arguments token_id:int and response:str, which receives the tokens from the model as they are generated and stops the generation by returning False.
    
            Returns:
                Either the entire completion or a generator that yields the completion token by token.
            """
    
            # Preparing the model request
            generate_kwargs: dict[str, Any] = dict(
                temp           = temp,
                top_k          = top_k,
                top_p          = top_p,
                min_p          = min_p,
                repeat_penalty = repeat_penalty,
                repeat_last_n  = repeat_last_n,
                n_batch        = n_batch,
                n_predict      = n_predict if n_predict is not None else max_tokens,
            )
    
            # Prepare the callback, process the model response
            full_response = ""
    
            def _callback_wrapper(token_id: int, response: str) -> bool:
                nonlocal full_response
                full_response += response
                return callback(token_id, response)
    
            last_msg_rendered = prompt
            if self._chat_session is not None:
                session = self._chat_session
                def render(messages: list[MessageType]) -> str:
                    return session.template.render(
                        messages=messages,
                        add_generation_prompt=True,
                        **self.model.special_tokens_map,
                    )
                session.history.append(MessageType(role="user", content=prompt))
                prompt = render(session.history)
                if len(session.history) > 1:
                    last_msg_rendered = render(session.history[-1:])
    
            # Check request length
            last_msg_len = self.model.count_prompt_tokens(last_msg_rendered)
            if last_msg_len > (limit := self.model.n_ctx - 4):
                raise ValueError(f"Your message was too long and could not be processed ({last_msg_len} > {limit}).")
    
            # Send the request to the model
            if streaming:
                def stream() -> Iterator[str]:
                    yield from self.model.prompt_model_streaming(prompt, _callback_wrapper, **generate_kwargs)
                    if self._chat_session is not None:
                        self._chat_session.history.append(MessageType(role="assistant", content=full_response))
                return stream()
    
            self.model.prompt_model(prompt, _callback_wrapper, **generate_kwargs)
            if self._chat_session is not None:
                self._chat_session.history.append(MessageType(role="assistant", content=full_response))
            return full_response
    
        @contextmanager
        def chat_session(
            self,
            system_message: str | Literal[False] | None = None,
            chat_template: str | None = None,
        ):
            """
            Context manager to hold an inference optimized chat session with a GPT4All model.
    
            Args:
                system_message: An initial instruction for the model, None to use the model default, or False to disable. Defaults to None.
                chat_template: Jinja template for the conversation, or None to use the model default. Defaults to None.
            """
    
            if system_message is None:
                system_message = self.config.get("systemMessage", False)
    
            if chat_template is None:
                if "name" not in self.config:
                    raise ValueError("For sideloaded models or with allow_download=False, you must specify a chat template.")
                if "chatTemplate" not in self.config:
                    raise NotImplementedError("This model appears to have a built-in chat template, but loading it is not "
                                              "currently implemented. Please pass a template to chat_session() directly.")
                if (tmpl := self.config["chatTemplate"]) is None:
                    raise ValueError(f"The model {self.config['name']!r} does not support chat.")
                chat_template = tmpl
    
            history = []
            if system_message is not False:
                history.append(MessageType(role="system", content=system_message))
            self._chat_session = ChatSession(
                template=_jinja_env.from_string(chat_template),
                history=history,
            )
            try:
                yield self
            finally:
                self._chat_session = None
    
        @staticmethod
        def list_gpus() -> list[str]:
            """
            List the names of the available GPU devices.
    
            Returns:
                A list of strings representing the names of the available GPU devices.
            """
            return LLModel.list_gpus()
      
  
---|---  
  
#####  `backend: Literal['cpu', 'kompute', 'cuda', 'metal']` `property`

The name of the llama.cpp backend currently in use. One of "cpu", "kompute",
"cuda", or "metal".

#####  `device: str | None` `property`

The name of the GPU device currently in use, or None for backends other than
Kompute or CUDA.

#####  `__init__(model_name, *, model_path=None, model_type=None,
allow_download=True, n_threads=None, device=None, n_ctx=2048, ngl=100,
verbose=False)`

Constructor

Parameters:

  * **`model_name`** (`str`) â 

Name of GPT4All or custom model. Including ".gguf" file extension is optional
but encouraged.

  * **`model_path`** (`str | PathLike[str] | None`, default: `None` ) â 

Path to directory containing model file or, if file does not exist, where to
download model. Default is None, in which case models will be stored in
`~/.cache/gpt4all/`.

  * **`model_type`** (`str | None`, default: `None` ) â 

Model architecture. This argument currently does not have any functionality
and is just used as descriptive identifier for user. Default is None.

  * **`allow_download`** (`bool`, default: `True` ) â 

Allow API to download models from gpt4all.io. Default is True.

  * **`n_threads`** (`int | None`, default: `None` ) â 

number of CPU threads used by GPT4All. Default is None, then the number of
threads are determined automatically.

  * **`device`** (`str | None`, default: `None` ) â 

The processing unit on which the GPT4All model will run. It can be set to: \-
"cpu": Model will run on the central processing unit. \- "gpu": Use Metal on
ARM64 macOS, otherwise the same as "kompute". \- "kompute": Use the best GPU
provided by the Kompute backend. \- "cuda": Use the best GPU provided by the
CUDA backend. \- "amd", "nvidia": Use the best GPU provided by the Kompute
backend from this vendor. \- A specific device name from the list returned by
`GPT4All.list_gpus()`. Default is Metal on ARM64 macOS, "cpu" otherwise.

Note: If a selected GPU device does not have sufficient RAM to accommodate the
model, an error will be thrown, and the GPT4All instance will be rendered
invalid. It's advised to ensure the device has enough memory before initiating
the model.

  * **`n_ctx`** (`int`, default: `2048` ) â 

Maximum size of context window

  * **`ngl`** (`int`, default: `100` ) â 

Number of GPU layers to use (Vulkan)

  * **`verbose`** (`bool`, default: `False` ) â 

If True, print debug messages.

Source code in `gpt4all/gpt4all.py`

    
    
    196
    197
    198
    199
    200
    201
    202
    203
    204
    205
    206
    207
    208
    209
    210
    211
    212
    213
    214
    215
    216
    217
    218
    219
    220
    221
    222
    223
    224
    225
    226
    227
    228
    229
    230
    231
    232
    233
    234
    235
    236
    237
    238
    239
    240
    241
    242
    243
    244
    245
    246
    247
    248
    249
    250
    251
    252
    253
    254
    255
    256
    257
    258
    259
    260
    261
    262
    263
    264
    265
    266
    267
    268
    269

|

    
    
    def __init__(
        self,
        model_name: str,
        *,
        model_path: str | os.PathLike[str] | None = None,
        model_type: str | None = None,
        allow_download: bool = True,
        n_threads: int | None = None,
        device: str | None = None,
        n_ctx: int = 2048,
        ngl: int = 100,
        verbose: bool = False,
    ):
        """
        Constructor
    
        Args:
            model_name: Name of GPT4All or custom model. Including ".gguf" file extension is optional but encouraged.
            model_path: Path to directory containing model file or, if file does not exist, where to download model.
                Default is None, in which case models will be stored in `~/.cache/gpt4all/`.
            model_type: Model architecture. This argument currently does not have any functionality and is just used as
                descriptive identifier for user. Default is None.
            allow_download: Allow API to download models from gpt4all.io. Default is True.
            n_threads: number of CPU threads used by GPT4All. Default is None, then the number of threads are determined automatically.
            device: The processing unit on which the GPT4All model will run. It can be set to:
                - "cpu": Model will run on the central processing unit.
                - "gpu": Use Metal on ARM64 macOS, otherwise the same as "kompute".
                - "kompute": Use the best GPU provided by the Kompute backend.
                - "cuda": Use the best GPU provided by the CUDA backend.
                - "amd", "nvidia": Use the best GPU provided by the Kompute backend from this vendor.
                - A specific device name from the list returned by `GPT4All.list_gpus()`.
                Default is Metal on ARM64 macOS, "cpu" otherwise.
    
                Note: If a selected GPU device does not have sufficient RAM to accommodate the model, an error will be thrown, and the GPT4All instance will be rendered invalid. It's advised to ensure the device has enough memory before initiating the model.
            n_ctx: Maximum size of context window
            ngl: Number of GPU layers to use (Vulkan)
            verbose: If True, print debug messages.
        """
    
        self.model_type = model_type
        self._chat_session: ChatSession | None = None
    
        device_init = None
        if sys.platform == "darwin":
            if device is None:
                backend = "auto"  # "auto" is effectively "metal" due to currently non-functional fallback
            elif device == "cpu":
                backend = "cpu"
            else:
                if platform.machine() != "arm64" or device != "gpu":
                    raise ValueError(f"Unknown device for this platform: {device}")
                backend = "metal"
        else:
            backend = "kompute"
            if device is None or device == "cpu":
                pass  # use kompute with no device
            elif device in ("cuda", "kompute"):
                backend = device
                device_init = "gpu"
            elif device.startswith("cuda:"):
                backend = "cuda"
                device_init = _remove_prefix(device, "cuda:")
            else:
                device_init = _remove_prefix(device, "kompute:")
    
        # Retrieve model and download if allowed
        self.config: ConfigType = self.retrieve_model(model_name, model_path=model_path, allow_download=allow_download, verbose=verbose)
        self.model = LLModel(self.config["path"], n_ctx, ngl, backend)
        if device_init is not None:
            self.model.init_gpu(device_init)
        self.model.load_model()
        # Set n_threads
        if n_threads is not None:
            self.model.set_thread_count(n_threads)
      
  
---|---  
  
#####  `chat_session(system_message=None, chat_template=None)`

Context manager to hold an inference optimized chat session with a GPT4All
model.

Parameters:

  * **`system_message`** (`str | Literal[False] | None`, default: `None` ) â 

An initial instruction for the model, None to use the model default, or False
to disable. Defaults to None.

  * **`chat_template`** (`str | None`, default: `None` ) â 

Jinja template for the conversation, or None to use the model default.
Defaults to None.

Source code in `gpt4all/gpt4all.py`

    
    
    601
    602
    603
    604
    605
    606
    607
    608
    609
    610
    611
    612
    613
    614
    615
    616
    617
    618
    619
    620
    621
    622
    623
    624
    625
    626
    627
    628
    629
    630
    631
    632
    633
    634
    635
    636
    637
    638

|

    
    
    @contextmanager
    def chat_session(
        self,
        system_message: str | Literal[False] | None = None,
        chat_template: str | None = None,
    ):
        """
        Context manager to hold an inference optimized chat session with a GPT4All model.
    
        Args:
            system_message: An initial instruction for the model, None to use the model default, or False to disable. Defaults to None.
            chat_template: Jinja template for the conversation, or None to use the model default. Defaults to None.
        """
    
        if system_message is None:
            system_message = self.config.get("systemMessage", False)
    
        if chat_template is None:
            if "name" not in self.config:
                raise ValueError("For sideloaded models or with allow_download=False, you must specify a chat template.")
            if "chatTemplate" not in self.config:
                raise NotImplementedError("This model appears to have a built-in chat template, but loading it is not "
                                          "currently implemented. Please pass a template to chat_session() directly.")
            if (tmpl := self.config["chatTemplate"]) is None:
                raise ValueError(f"The model {self.config['name']!r} does not support chat.")
            chat_template = tmpl
    
        history = []
        if system_message is not False:
            history.append(MessageType(role="system", content=system_message))
        self._chat_session = ChatSession(
            template=_jinja_env.from_string(chat_template),
            history=history,
        )
        try:
            yield self
        finally:
            self._chat_session = None
      
  
---|---  
  
#####  `close()`

Delete the model instance and free associated system resources.

Source code in `gpt4all/gpt4all.py`

    
    
    279
    280
    281

|

    
    
    def close(self) -> None:
        """Delete the model instance and free associated system resources."""
        self.model.close()
      
  
---|---  
  
#####  `download_model(model_filename, model_path, verbose=True, url=None,
expected_size=None, expected_md5=None)` `staticmethod`

Download model from gpt4all.io.

Parameters:

  * **`model_filename`** (`str`) â 

Filename of model (with .gguf extension).

  * **`model_path`** (`str | PathLike[str]`) â 

Path to download model to.

  * **`verbose`** (`bool`, default: `True` ) â 

If True (default), print debug messages.

  * **`url`** (`str | None`, default: `None` ) â 

the models remote url (e.g. may be hosted on HF)

  * **`expected_size`** (`int | None`, default: `None` ) â 

The expected size of the download.

  * **`expected_md5`** (`str | None`, default: `None` ) â 

The expected MD5 hash of the download.

Returns:

  * `str | PathLike[str]` â 

Model file destination.

Source code in `gpt4all/gpt4all.py`

    
    
    377
    378
    379
    380
    381
    382
    383
    384
    385
    386
    387
    388
    389
    390
    391
    392
    393
    394
    395
    396
    397
    398
    399
    400
    401
    402
    403
    404
    405
    406
    407
    408
    409
    410
    411
    412
    413
    414
    415
    416
    417
    418
    419
    420
    421
    422
    423
    424
    425
    426
    427
    428
    429
    430
    431
    432
    433
    434
    435
    436
    437
    438
    439
    440
    441
    442
    443
    444
    445
    446
    447
    448
    449
    450
    451
    452
    453
    454
    455
    456
    457
    458
    459
    460
    461
    462
    463
    464
    465
    466
    467
    468
    469
    470
    471
    472
    473
    474
    475
    476
    477
    478
    479
    480
    481
    482
    483
    484
    485
    486
    487
    488
    489
    490
    491

|

    
    
    @staticmethod
    def download_model(
        model_filename: str,
        model_path: str | os.PathLike[str],
        verbose: bool = True,
        url: str | None = None,
        expected_size: int | None = None,
        expected_md5: str | None = None,
    ) -> str | os.PathLike[str]:
        """
        Download model from gpt4all.io.
    
        Args:
            model_filename: Filename of model (with .gguf extension).
            model_path: Path to download model to.
            verbose: If True (default), print debug messages.
            url: the models remote url (e.g. may be hosted on HF)
            expected_size: The expected size of the download.
            expected_md5: The expected MD5 hash of the download.
    
        Returns:
            Model file destination.
        """
    
        # Download model
        if url is None:
            url = f"https://gpt4all.io/models/gguf/{model_filename}"
    
        def make_request(offset=None):
            headers = {}
            if offset:
                print(f"\nDownload interrupted, resuming from byte position {offset}", file=sys.stderr)
                headers["Range"] = f"bytes={offset}-"  # resume incomplete response
                headers["Accept-Encoding"] = "identity"  # Content-Encoding changes meaning of ranges
            response = requests.get(url, stream=True, headers=headers)
            if response.status_code not in (200, 206):
                raise ValueError(f"Request failed: HTTP {response.status_code} {response.reason}")
            if offset and (response.status_code != 206 or str(offset) not in response.headers.get("Content-Range", "")):
                raise ValueError("Connection was interrupted and server does not support range requests")
            if (enc := response.headers.get("Content-Encoding")) is not None:
                raise ValueError(f"Expected identity Content-Encoding, got {enc}")
            return response
    
        response = make_request()
    
        total_size_in_bytes = int(response.headers.get("content-length", 0))
        block_size = 2**20  # 1 MB
    
        partial_path = Path(model_path) / (model_filename + ".part")
    
        with open(partial_path, "w+b") as partf:
            try:
                with tqdm(desc="Downloading", total=total_size_in_bytes, unit="iB", unit_scale=True) as progress_bar:
                    while True:
                        last_progress = progress_bar.n
                        try:
                            for data in response.iter_content(block_size):
                                partf.write(data)
                                progress_bar.update(len(data))
                        except ChunkedEncodingError as cee:
                            if cee.args and isinstance(pe := cee.args[0], ProtocolError):
                                if len(pe.args) >= 2 and isinstance(ir := pe.args[1], IncompleteRead):
                                    assert progress_bar.n <= ir.partial  # urllib3 may be ahead of us but never behind
                                    # the socket was closed during a read - retry
                                    response = make_request(progress_bar.n)
                                    continue
                            raise
                        if total_size_in_bytes != 0 and progress_bar.n < total_size_in_bytes:
                            if progress_bar.n == last_progress:
                                raise RuntimeError("Download not making progress, aborting.")
                            # server closed connection prematurely - retry
                            response = make_request(progress_bar.n)
                            continue
                        break
    
                # verify file integrity
                file_size = partf.tell()
                if expected_size is not None and file_size != expected_size:
                    raise ValueError(f"Expected file size of {expected_size} bytes, got {file_size}")
                if expected_md5 is not None:
                    partf.seek(0)
                    hsh = hashlib.md5()
                    with tqdm(desc="Verifying", total=file_size, unit="iB", unit_scale=True) as bar:
                        while chunk := partf.read(block_size):
                            hsh.update(chunk)
                            bar.update(len(chunk))
                    if hsh.hexdigest() != expected_md5.lower():
                        raise ValueError(f"Expected MD5 hash of {expected_md5!r}, got {hsh.hexdigest()!r}")
            except:
                if verbose:
                    print("Cleaning up the interrupted download...", file=sys.stderr)
                try:
                    os.remove(partial_path)
                except OSError:
                    pass
                raise
    
            # flush buffers and sync the inode
            partf.flush()
            _fsync(partf)
    
        # move to final destination
        download_path = Path(model_path) / model_filename
        try:
            os.rename(partial_path, download_path)
        except FileExistsError:
            try:
                os.remove(partial_path)
            except OSError:
                pass
            raise
    
        if verbose:
            print(f"Model downloaded to {str(download_path)!r}", file=sys.stderr)
        return download_path
      
  
---|---  
  
#####  `generate(prompt, *, max_tokens=200, temp=0.7, top_k=40, top_p=0.4,
min_p=0.0, repeat_penalty=1.18, repeat_last_n=64, n_batch=8, n_predict=None,
streaming=False, callback=empty_response_callback)`

Generate outputs from any GPT4All model.

Parameters:

  * **`prompt`** (`str`) â 

The prompt for the model to complete.

  * **`max_tokens`** (`int`, default: `200` ) â 

The maximum number of tokens to generate.

  * **`temp`** (`float`, default: `0.7` ) â 

The model temperature. Larger values increase creativity but decrease
factuality.

  * **`top_k`** (`int`, default: `40` ) â 

Randomly sample from the top_k most likely tokens at each generation step. Set
this to 1 for greedy decoding.

  * **`top_p`** (`float`, default: `0.4` ) â 

Randomly sample at each generation step from the top most likely tokens whose
probabilities add up to top_p.

  * **`min_p`** (`float`, default: `0.0` ) â 

Randomly sample at each generation step from the top most likely tokens whose
probabilities are at least min_p.

  * **`repeat_penalty`** (`float`, default: `1.18` ) â 

Penalize the model for repetition. Higher values result in less repetition.

  * **`repeat_last_n`** (`int`, default: `64` ) â 

How far in the models generation history to apply the repeat penalty.

  * **`n_batch`** (`int`, default: `8` ) â 

Number of prompt tokens processed in parallel. Larger values decrease latency
but increase resource requirements.

  * **`n_predict`** (`int | None`, default: `None` ) â 

Equivalent to max_tokens, exists for backwards compatibility.

  * **`streaming`** (`bool`, default: `False` ) â 

If True, this method will instead return a generator that yields tokens as the
model generates them.

  * **`callback`** (`ResponseCallbackType`, default: `empty_response_callback` ) â 

A function with arguments token_id:int and response:str, which receives the
tokens from the model as they are generated and stops the generation by
returning False.

Returns:

  * `Any` â 

Either the entire completion or a generator that yields the completion token
by token.

Source code in `gpt4all/gpt4all.py`

    
    
    512
    513
    514
    515
    516
    517
    518
    519
    520
    521
    522
    523
    524
    525
    526
    527
    528
    529
    530
    531
    532
    533
    534
    535
    536
    537
    538
    539
    540
    541
    542
    543
    544
    545
    546
    547
    548
    549
    550
    551
    552
    553
    554
    555
    556
    557
    558
    559
    560
    561
    562
    563
    564
    565
    566
    567
    568
    569
    570
    571
    572
    573
    574
    575
    576
    577
    578
    579
    580
    581
    582
    583
    584
    585
    586
    587
    588
    589
    590
    591
    592
    593
    594
    595
    596
    597
    598
    599

|

    
    
    def generate(
        self,
        prompt         : str,
        *,
        max_tokens     : int                  = 200,
        temp           : float                = 0.7,
        top_k          : int                  = 40,
        top_p          : float                = 0.4,
        min_p          : float                = 0.0,
        repeat_penalty : float                = 1.18,
        repeat_last_n  : int                  = 64,
        n_batch        : int                  = 8,
        n_predict      : int | None           = None,
        streaming      : bool                 = False,
        callback       : ResponseCallbackType = empty_response_callback,
    ) -> Any:
        """
        Generate outputs from any GPT4All model.
    
        Args:
            prompt: The prompt for the model to complete.
            max_tokens: The maximum number of tokens to generate.
            temp: The model temperature. Larger values increase creativity but decrease factuality.
            top_k: Randomly sample from the top_k most likely tokens at each generation step. Set this to 1 for greedy decoding.
            top_p: Randomly sample at each generation step from the top most likely tokens whose probabilities add up to top_p.
            min_p: Randomly sample at each generation step from the top most likely tokens whose probabilities are at least min_p.
            repeat_penalty: Penalize the model for repetition. Higher values result in less repetition.
            repeat_last_n: How far in the models generation history to apply the repeat penalty.
            n_batch: Number of prompt tokens processed in parallel. Larger values decrease latency but increase resource requirements.
            n_predict: Equivalent to max_tokens, exists for backwards compatibility.
            streaming: If True, this method will instead return a generator that yields tokens as the model generates them.
            callback: A function with arguments token_id:int and response:str, which receives the tokens from the model as they are generated and stops the generation by returning False.
    
        Returns:
            Either the entire completion or a generator that yields the completion token by token.
        """
    
        # Preparing the model request
        generate_kwargs: dict[str, Any] = dict(
            temp           = temp,
            top_k          = top_k,
            top_p          = top_p,
            min_p          = min_p,
            repeat_penalty = repeat_penalty,
            repeat_last_n  = repeat_last_n,
            n_batch        = n_batch,
            n_predict      = n_predict if n_predict is not None else max_tokens,
        )
    
        # Prepare the callback, process the model response
        full_response = ""
    
        def _callback_wrapper(token_id: int, response: str) -> bool:
            nonlocal full_response
            full_response += response
            return callback(token_id, response)
    
        last_msg_rendered = prompt
        if self._chat_session is not None:
            session = self._chat_session
            def render(messages: list[MessageType]) -> str:
                return session.template.render(
                    messages=messages,
                    add_generation_prompt=True,
                    **self.model.special_tokens_map,
                )
            session.history.append(MessageType(role="user", content=prompt))
            prompt = render(session.history)
            if len(session.history) > 1:
                last_msg_rendered = render(session.history[-1:])
    
        # Check request length
        last_msg_len = self.model.count_prompt_tokens(last_msg_rendered)
        if last_msg_len > (limit := self.model.n_ctx - 4):
            raise ValueError(f"Your message was too long and could not be processed ({last_msg_len} > {limit}).")
    
        # Send the request to the model
        if streaming:
            def stream() -> Iterator[str]:
                yield from self.model.prompt_model_streaming(prompt, _callback_wrapper, **generate_kwargs)
                if self._chat_session is not None:
                    self._chat_session.history.append(MessageType(role="assistant", content=full_response))
            return stream()
    
        self.model.prompt_model(prompt, _callback_wrapper, **generate_kwargs)
        if self._chat_session is not None:
            self._chat_session.history.append(MessageType(role="assistant", content=full_response))
        return full_response
      
  
---|---  
  
#####  `list_gpus()` `staticmethod`

List the names of the available GPU devices.

Returns:

  * `list[str]` â 

A list of strings representing the names of the available GPU devices.

Source code in `gpt4all/gpt4all.py`

    
    
    640
    641
    642
    643
    644
    645
    646
    647
    648

|

    
    
    @staticmethod
    def list_gpus() -> list[str]:
        """
        List the names of the available GPU devices.
    
        Returns:
            A list of strings representing the names of the available GPU devices.
        """
        return LLModel.list_gpus()
      
  
---|---  
  
#####  `list_models()` `staticmethod`

Fetch model list from https://gpt4all.io/models/models3.json.

Returns:

  * `list[ConfigType]` â 

Model list in JSON format.

Source code in `gpt4all/gpt4all.py`

    
    
    303
    304
    305
    306
    307
    308
    309
    310
    311
    312
    313
    314

|

    
    
    @staticmethod
    def list_models() -> list[ConfigType]:
        """
        Fetch model list from https://gpt4all.io/models/models3.json.
    
        Returns:
            Model list in JSON format.
        """
        resp = requests.get("https://gpt4all.io/models/models3.json")
        if resp.status_code != 200:
            raise ValueError(f"Request failed: HTTP {resp.status_code} {resp.reason}")
        return resp.json()
      
  
---|---  
  
#####  `retrieve_model(model_name, model_path=None, allow_download=True,
verbose=False)` `classmethod`

Find model file, and if it doesn't exist, download the model.

Parameters:

  * **`model_name`** (`str`) â 

Name of model.

  * **`model_path`** (`str | PathLike[str] | None`, default: `None` ) â 

Path to find model. Default is None in which case path is set to
~/.cache/gpt4all/.

  * **`allow_download`** (`bool`, default: `True` ) â 

Allow API to download model from gpt4all.io. Default is True.

  * **`verbose`** (`bool`, default: `False` ) â 

If True (default), print debug messages.

Returns:

  * `ConfigType` â 

Model config.

Source code in `gpt4all/gpt4all.py`

    
    
    316
    317
    318
    319
    320
    321
    322
    323
    324
    325
    326
    327
    328
    329
    330
    331
    332
    333
    334
    335
    336
    337
    338
    339
    340
    341
    342
    343
    344
    345
    346
    347
    348
    349
    350
    351
    352
    353
    354
    355
    356
    357
    358
    359
    360
    361
    362
    363
    364
    365
    366
    367
    368
    369
    370
    371
    372
    373
    374
    375

|

    
    
    @classmethod
    def retrieve_model(
        cls,
        model_name: str,
        model_path: str | os.PathLike[str] | None = None,
        allow_download: bool = True,
        verbose: bool = False,
    ) -> ConfigType:
        """
        Find model file, and if it doesn't exist, download the model.
    
        Args:
            model_name: Name of model.
            model_path: Path to find model. Default is None in which case path is set to
                ~/.cache/gpt4all/.
            allow_download: Allow API to download model from gpt4all.io. Default is True.
            verbose: If True (default), print debug messages.
    
        Returns:
            Model config.
        """
    
        model_filename = append_extension_if_missing(model_name)
    
        # get the config for the model
        config: ConfigType = {}
        if allow_download:
            models = cls.list_models()
            if (model := next((m for m in models if m["filename"] == model_filename), None)) is not None:
                config.update(model)
    
        # Validate download directory
        if model_path is None:
            try:
                os.makedirs(DEFAULT_MODEL_DIRECTORY, exist_ok=True)
            except OSError as e:
                raise RuntimeError("Failed to create model download directory") from e
            model_path = DEFAULT_MODEL_DIRECTORY
        else:
            model_path = Path(model_path)
    
        if not model_path.exists():
            raise FileNotFoundError(f"Model directory does not exist: {model_path!r}")
    
        model_dest = model_path / model_filename
        if model_dest.exists():
            config["path"] = str(model_dest)
            if verbose:
                print(f"Found model file at {str(model_dest)!r}", file=sys.stderr)
        elif allow_download:
            # If model file does not exist, download
            filesize = config.get("filesize")
            config["path"] = str(cls.download_model(
                model_filename, model_path, verbose=verbose, url=config.get("url"),
                expected_size=None if filesize is None else int(filesize), expected_md5=config.get("md5sum"),
            ))
        else:
            raise FileNotFoundError(f"Model file does not exist: {model_dest!r}")
    
        return config
      
  
---|---  
  
####  `Embed4All`

Python class that handles embeddings for GPT4All.

Source code in `gpt4all/gpt4all.py`

    
    
     69
     70
     71
     72
     73
     74
     75
     76
     77
     78
     79
     80
     81
     82
     83
     84
     85
     86
     87
     88
     89
     90
     91
     92
     93
     94
     95
     96
     97
     98
     99
    100
    101
    102
    103
    104
    105
    106
    107
    108
    109
    110
    111
    112
    113
    114
    115
    116
    117
    118
    119
    120
    121
    122
    123
    124
    125
    126
    127
    128
    129
    130
    131
    132
    133
    134
    135
    136
    137
    138
    139
    140
    141
    142
    143
    144
    145
    146
    147
    148
    149
    150
    151
    152
    153
    154
    155
    156
    157
    158
    159
    160
    161
    162
    163
    164
    165
    166
    167
    168
    169
    170
    171
    172
    173
    174
    175
    176
    177
    178
    179
    180
    181
    182
    183
    184
    185
    186
    187
    188

|

    
    
    class Embed4All:
        """
        Python class that handles embeddings for GPT4All.
        """
    
        MIN_DIMENSIONALITY = 64
    
        def __init__(self, model_name: str | None = None, *, n_threads: int | None = None, device: str | None = None, **kwargs: Any):
            """
            Constructor
    
            Args:
                n_threads: number of CPU threads used by GPT4All. Default is None, then the number of threads are determined automatically.
                device: The processing unit on which the embedding model will run. See the `GPT4All` constructor for more info.
                kwargs: Remaining keyword arguments are passed to the `GPT4All` constructor.
            """
            if model_name is None:
                model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"
            self.gpt4all = GPT4All(model_name, n_threads=n_threads, device=device, **kwargs)
    
        def __enter__(self) -> Self:
            return self
    
        def __exit__(
            self, typ: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None,
        ) -> None:
            self.close()
    
        def close(self) -> None:
            """Delete the model instance and free associated system resources."""
            self.gpt4all.close()
    
        # return_dict=False
        @overload
        def embed(
            self, text: str, *, prefix: str | None = ..., dimensionality: int | None = ..., long_text_mode: str = ...,
            return_dict: Literal[False] = ..., atlas: bool = ..., cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> list[float]: ...
        @overload
        def embed(
            self, text: list[str], *, prefix: str | None = ..., dimensionality: int | None = ..., long_text_mode: str = ...,
            return_dict: Literal[False] = ..., atlas: bool = ..., cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> list[list[float]]: ...
        @overload
        def embed(
            self, text: str | list[str], *, prefix: str | None = ..., dimensionality: int | None = ...,
            long_text_mode: str = ..., return_dict: Literal[False] = ..., atlas: bool = ...,
            cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> list[Any]: ...
    
        # return_dict=True
        @overload
        def embed(
            self, text: str, *, prefix: str | None = ..., dimensionality: int | None = ..., long_text_mode: str = ...,
            return_dict: Literal[True], atlas: bool = ..., cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> EmbedResult[list[float]]: ...
        @overload
        def embed(
            self, text: list[str], *, prefix: str | None = ..., dimensionality: int | None = ..., long_text_mode: str = ...,
            return_dict: Literal[True], atlas: bool = ..., cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> EmbedResult[list[list[float]]]: ...
        @overload
        def embed(
            self, text: str | list[str], *, prefix: str | None = ..., dimensionality: int | None = ...,
            long_text_mode: str = ..., return_dict: Literal[True], atlas: bool = ...,
            cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> EmbedResult[list[Any]]: ...
    
        # return type unknown
        @overload
        def embed(
            self, text: str | list[str], *, prefix: str | None = ..., dimensionality: int | None = ...,
            long_text_mode: str = ..., return_dict: bool = ..., atlas: bool = ...,
            cancel_cb: EmbCancelCallbackType | None = ...,
        ) -> Any: ...
    
        def embed(
            self, text: str | list[str], *, prefix: str | None = None, dimensionality: int | None = None,
            long_text_mode: str = "mean", return_dict: bool = False, atlas: bool = False,
            cancel_cb: EmbCancelCallbackType | None = None,
        ) -> Any:
            """
            Generate one or more embeddings.
    
            Args:
                text: A text or list of texts to generate embeddings for.
                prefix: The model-specific prefix representing the embedding task, without the trailing colon. For Nomic
                    Embed, this can be `search_query`, `search_document`, `classification`, or `clustering`. Defaults to
                    `search_document` or equivalent if known; otherwise, you must explicitly pass a prefix or an empty
                    string if none applies.
                dimensionality: The embedding dimension, for use with Matryoshka-capable models. Defaults to full-size.
                long_text_mode: How to handle texts longer than the model can accept. One of `mean` or `truncate`.
                return_dict: Return the result as a dict that includes the number of prompt tokens processed.
                atlas: Try to be fully compatible with the Atlas API. Currently, this means texts longer than 8192 tokens
                    with long_text_mode="mean" will raise an error. Disabled by default.
                cancel_cb: Called with arguments (batch_sizes, backend_name). Return true to cancel embedding.
    
            Returns:
                With return_dict=False, an embedding or list of embeddings of your text(s).
                With return_dict=True, a dict with keys 'embeddings' and 'n_prompt_tokens'.
    
            Raises:
                CancellationError: If cancel_cb returned True and embedding was canceled.
            """
            if dimensionality is None:
                dimensionality = -1
            else:
                if dimensionality <= 0:
                    raise ValueError(f"Dimensionality must be None or a positive integer, got {dimensionality}")
                if dimensionality < self.MIN_DIMENSIONALITY:
                    warnings.warn(
                        f"Dimensionality {dimensionality} is less than the suggested minimum of {self.MIN_DIMENSIONALITY}."
                        " Performance may be degraded."
                    )
            try:
                do_mean = {"mean": True, "truncate": False}[long_text_mode]
            except KeyError:
                raise ValueError(f"Long text mode must be one of 'mean' or 'truncate', got {long_text_mode!r}")
            result = self.gpt4all.model.generate_embeddings(text, prefix, dimensionality, do_mean, atlas, cancel_cb)
            return result if return_dict else result["embeddings"]
      
  
---|---  
  
#####  `__init__(model_name=None, *, n_threads=None, device=None, **kwargs)`

Constructor

Parameters:

  * **`n_threads`** (`int | None`, default: `None` ) â 

number of CPU threads used by GPT4All. Default is None, then the number of
threads are determined automatically.

  * **`device`** (`str | None`, default: `None` ) â 

The processing unit on which the embedding model will run. See the `GPT4All`
constructor for more info.

  * **`kwargs`** (`Any`, default: `{}` ) â 

Remaining keyword arguments are passed to the `GPT4All` constructor.

Source code in `gpt4all/gpt4all.py`

    
    
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87

|

    
    
    def __init__(self, model_name: str | None = None, *, n_threads: int | None = None, device: str | None = None, **kwargs: Any):
        """
        Constructor
    
        Args:
            n_threads: number of CPU threads used by GPT4All. Default is None, then the number of threads are determined automatically.
            device: The processing unit on which the embedding model will run. See the `GPT4All` constructor for more info.
            kwargs: Remaining keyword arguments are passed to the `GPT4All` constructor.
        """
        if model_name is None:
            model_name = "all-MiniLM-L6-v2.gguf2.f16.gguf"
        self.gpt4all = GPT4All(model_name, n_threads=n_threads, device=device, **kwargs)
      
  
---|---  
  
#####  `close()`

Delete the model instance and free associated system resources.

Source code in `gpt4all/gpt4all.py`

    
    
    97
    98
    99

|

    
    
    def close(self) -> None:
        """Delete the model instance and free associated system resources."""
        self.gpt4all.close()
      
  
---|---  
  
#####  `embed(text, *, prefix=None, dimensionality=None,
long_text_mode='mean', return_dict=False, atlas=False, cancel_cb=None)`

Generate one or more embeddings.

Parameters:

  * **`text`** (`str | list[str]`) â 

A text or list of texts to generate embeddings for.

  * **`prefix`** (`str | None`, default: `None` ) â 

The model-specific prefix representing the embedding task, without the
trailing colon. For Nomic Embed, this can be `search_query`,
`search_document`, `classification`, or `clustering`. Defaults to
`search_document` or equivalent if known; otherwise, you must explicitly pass
a prefix or an empty string if none applies.

  * **`dimensionality`** (`int | None`, default: `None` ) â 

The embedding dimension, for use with Matryoshka-capable models. Defaults to
full-size.

  * **`long_text_mode`** (`str`, default: `'mean'` ) â 

How to handle texts longer than the model can accept. One of `mean` or
`truncate`.

  * **`return_dict`** (`bool`, default: `False` ) â 

Return the result as a dict that includes the number of prompt tokens
processed.

  * **`atlas`** (`bool`, default: `False` ) â 

Try to be fully compatible with the Atlas API. Currently, this means texts
longer than 8192 tokens with long_text_mode="mean" will raise an error.
Disabled by default.

  * **`cancel_cb`** (`EmbCancelCallbackType | None`, default: `None` ) â 

Called with arguments (batch_sizes, backend_name). Return true to cancel
embedding.

Returns:

  * `Any` â 

With return_dict=False, an embedding or list of embeddings of your text(s).

  * `Any` â 

With return_dict=True, a dict with keys 'embeddings' and 'n_prompt_tokens'.

Raises:

  * `CancellationError` â 

If cancel_cb returned True and embedding was canceled.

Source code in `gpt4all/gpt4all.py`

    
    
    145
    146
    147
    148
    149
    150
    151
    152
    153
    154
    155
    156
    157
    158
    159
    160
    161
    162
    163
    164
    165
    166
    167
    168
    169
    170
    171
    172
    173
    174
    175
    176
    177
    178
    179
    180
    181
    182
    183
    184
    185
    186
    187
    188

|

    
    
    def embed(
        self, text: str | list[str], *, prefix: str | None = None, dimensionality: int | None = None,
        long_text_mode: str = "mean", return_dict: bool = False, atlas: bool = False,
        cancel_cb: EmbCancelCallbackType | None = None,
    ) -> Any:
        """
        Generate one or more embeddings.
    
        Args:
            text: A text or list of texts to generate embeddings for.
            prefix: The model-specific prefix representing the embedding task, without the trailing colon. For Nomic
                Embed, this can be `search_query`, `search_document`, `classification`, or `clustering`. Defaults to
                `search_document` or equivalent if known; otherwise, you must explicitly pass a prefix or an empty
                string if none applies.
            dimensionality: The embedding dimension, for use with Matryoshka-capable models. Defaults to full-size.
            long_text_mode: How to handle texts longer than the model can accept. One of `mean` or `truncate`.
            return_dict: Return the result as a dict that includes the number of prompt tokens processed.
            atlas: Try to be fully compatible with the Atlas API. Currently, this means texts longer than 8192 tokens
                with long_text_mode="mean" will raise an error. Disabled by default.
            cancel_cb: Called with arguments (batch_sizes, backend_name). Return true to cancel embedding.
    
        Returns:
            With return_dict=False, an embedding or list of embeddings of your text(s).
            With return_dict=True, a dict with keys 'embeddings' and 'n_prompt_tokens'.
    
        Raises:
            CancellationError: If cancel_cb returned True and embedding was canceled.
        """
        if dimensionality is None:
            dimensionality = -1
        else:
            if dimensionality <= 0:
                raise ValueError(f"Dimensionality must be None or a positive integer, got {dimensionality}")
            if dimensionality < self.MIN_DIMENSIONALITY:
                warnings.warn(
                    f"Dimensionality {dimensionality} is less than the suggested minimum of {self.MIN_DIMENSIONALITY}."
                    " Performance may be degraded."
                )
        try:
            do_mean = {"mean": True, "truncate": False}[long_text_mode]
        except KeyError:
            raise ValueError(f"Long text mode must be one of 'mean' or 'truncate', got {long_text_mode!r}")
        result = self.gpt4all.model.generate_embeddings(text, prefix, dimensionality, do_mean, atlas, cancel_cb)
        return result if return_dict else result["embeddings"]
      
  
---|---

