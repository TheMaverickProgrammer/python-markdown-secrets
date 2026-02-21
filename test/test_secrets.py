import re
import pathlib
import unittest
import textwrap
import subprocess
import markdown
import mkdsecrets

class TestSecrets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        secrets = mkdsecrets.SecretsExtension()
        cls.markdowner = markdown.Markdown(extensions=[secrets])

    def assertExpectedMarkdown(self, md_input, expected_output):
        output = self.markdowner.convert(textwrap.dedent(md_input))
        expected = textwrap.dedent(expected_output)
        self.assertEqual(output, expected)

    def test_line(self):
        md_input = 'hello <secret>world</secret>'
        self.assertExpectedMarkdown(md_input, '<p>hello <span class="secret"></span></p>')

    def test_multiline(self):
        md_input = """\
                hello <secret>
                world
                </secret>"""
        expected_result = """\
                <p>hello </p>
                <p><span class="secret"></span></p>"""
        self.assertExpectedMarkdown(md_input, expected_result)

if __name__ == '__main__':
    unittest.main()
