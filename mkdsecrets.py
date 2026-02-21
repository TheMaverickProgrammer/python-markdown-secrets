import re
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

newHtml = '<span class="secret"></span>'

class SecretsExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            SecretRemover(md), "secret_remover", 1)

class SecretRemover(Preprocessor):
    def run(self, lines):
        new_lines = []
        is_multi = False
        # B/c mkdocs feeds us one line at a time,
        # re.S will not work here to match the entire
        # <secret>...</secret> expression across multiple lines.
        # Instead, we check to see how many matches against the multiline
        # was obtained. If > 0, then we switch to a variant that looks
        # for the matching end tag instead.
        for line in lines:
            if not is_multi:
                new_line, is_multi = self._hushLine(line)
            else:
                new_line, is_multi = self._hushTail(line)
            new_lines.append(new_line)
        return new_lines

    def _hushLine(self, line):
        line = re.sub(r'<secret>.*?</secret>', newHtml, line)
        line, count = re.subn(r'<secret>.*?', '', line)
        return line, bool(count)

    def _hushTail(self, line):
        new_line, count = re.subn(r'.*?</secret>', newHtml, line, count=1)

        if count > 0:
            return self._hushLine(new_line)
        else:
            return ('', True)

def makeExtension(*args, **kwargs):
        return SecretsExtension(*args, **kwargs)

