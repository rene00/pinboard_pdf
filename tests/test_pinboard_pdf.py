import unittest
from pinboard_pdf import pinboard_pdf
import os


class TestPinboardPdfy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sanitize_filename(self):
        download_dir = '/foo/bar'
        url = 'http://example.org/article.html'
        filename = pinboard_pdf.sanitize_filename(url, download_dir)
        self.assertEqual(
            os.path.join(download_dir, 'example_org_article_html.pdf'),
            filename
        )

        url = 'https://example.org'
        filename = pinboard_pdf.sanitize_filename(url, download_dir)
        self.assertEqual(
            os.path.join(download_dir, 'example_org.pdf'),
            filename
        )

        url = 'https://example.org/'
        filename = pinboard_pdf.sanitize_filename(url, download_dir)
        self.assertEqual(
            os.path.join(download_dir, 'example_org.pdf'),
            filename
        )

        filename = pinboard_pdf.sanitize_filename(url, download_dir)
        self.assertEqual(
            os.path.join(download_dir, 'example_org.pdf'),
            filename
        )
