# mkdsecrets
A [Python-Markdown][PYTHON_MARKDOWN] preprocessor extension to convert content wrapped in `<secret></secret>` into `<span class="secret"></span>` elements instead. Effectively deleting the sensitive content entirely and replacing it with a visual HTML element that can be decorated however deemed best via css stylesheets.

# Installation
```shell
pip install git+https://github.com/TheMaverickProgrammer/python-markdown-secrets.git
```

[PYTHON_MARKDOWN]: https://github.com/waylan/Python-Markdown 
