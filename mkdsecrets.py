import re
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension

class SecretsExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(
            SecretRemover(md), "secret_remover", 1)

class SecretRemover(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_line = self._hush(line)
            new_lines.append(new_line)
        return new_lines

    def _hush(self, line):
        line, count = re.subn(r'<secret>.*?</secret>', '', line)
        return line

def makeExtension(*args, **kwargs):
        return SecretsExtension(*args, **kwargs)

