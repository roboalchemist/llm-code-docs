Apart from training/testing scripts, We provide lots of useful tools under the
`tools/` directory.

# Log Analysis

`tools/analysis_tools/analyze_logs.py` plots loss/mAP curves given a training
log file. Run `pip install seaborn` first to install the dependency.

```
python tools/analysis_tools/analyze_logs.py plot_curve [--keys ${KEYS}] [--eval-interval ${EVALUATION_INTERVAL}] [--title ${TITLE}] [--legend ${LEGEND}] [--backend ${BACKEND}] [--style ${STYLE}] [--out ${OUT_FILE}]

```