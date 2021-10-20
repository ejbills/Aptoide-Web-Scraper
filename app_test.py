import unittest

from web_scraper import scrape, url_validation

class TestApp(unittest.TestCase):

    def test_blank_page(self):
        expected_result = ['No data found', 'No data found',
                           'No data found', 'No data found',
                           'No data found']

        result = scrape('https://aptoide.com/')
        self.assertEqual(result, expected_result)

    def test_scrape_title(self):
        expected_result = ['Lords Mobile: Tower Defense']

        result = scrape('https://lords-mobile.en.aptoide.com/')
        self.assertEqual(result[0], expected_result[0])

    def test_url(self):
        result = url_validation('non-valid-url')
        self.assertEqual(result, False)

        result = url_validation('https://lords-mobile.en.aptoide.com/')
        self.assertEqual(result, True)