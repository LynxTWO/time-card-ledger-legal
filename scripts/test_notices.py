"""Preserve license payloads and usable local navigation when rendering."""
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from render_notices import ROOT, page_content, render


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.blocks = []
        self.in_pre = False
        self.scripts = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'a': self.links.append(attrs.get('href', ''))
        if tag == 'script': self.scripts += 1
        if tag == 'pre': self.in_pre = True; self.blocks.append('')

    def handle_endtag(self, tag):
        if tag == 'pre': self.in_pre = False

    def handle_data(self, data):
        if self.in_pre: self.blocks[-1] += data


class Notices(unittest.TestCase):
    def test_every_original_license_is_preserved(self):
        raw = (ROOT / 'licenses/THIRD_PARTY_NOTICES.txt').read_bytes()
        source = raw.decode().replace('\r\n', '\n')
        original = re.findall(r'^```[^\n]*\n(.*?)^```\s*$', source, re.M | re.S)
        self.assertGreater(len(original), 250)
        page = Page(); page.feed(render(source))
        self.assertEqual(page.blocks, original)
        self.assertEqual(hashlib.sha256(raw).digest(), hashlib.sha256((ROOT / 'licenses/THIRD_PARTY_NOTICES.txt').read_bytes()).digest())

    def test_all_inventory_links_resolve(self):
        page = Page(); page.feed((ROOT / 'licenses/index.html').read_text())
        self.assertEqual(len(page.ids), len(set(page.ids)))
        for link in page.links:
            if link.startswith('#'): self.assertIn(link[1:], page.ids)
        self.assertEqual(page.scripts, 0)
        self.assertIn('./THIRD_PARTY_NOTICES.txt', page.links)

    def test_license_markup_is_literal_and_raw_html_is_disabled(self):
        source = '<script>bad()</script>\n\n```text\n<svg onload="bad()">& letters\n```\n'
        page = Page(); page.feed(render(source))
        self.assertEqual(page.scripts, 0)
        self.assertEqual(page.blocks, ['<svg onload="bad()">& letters\n'])

    def test_render_is_repeatable_and_preserves_page_prose(self):
        current = (ROOT / 'licenses/index.html').read_text()
        raw = (ROOT / 'licenses/THIRD_PARTY_NOTICES.txt').read_bytes()
        self.assertEqual(page_content(current, raw), current)
        self.assertEqual(page_content(page_content(current, raw), raw), current)


if __name__ == '__main__':
    unittest.main()
