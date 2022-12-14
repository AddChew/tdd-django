import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Navigate to to-do app homepage
        self.browser.get('http://localhost:8000')

        # Check page title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        

if __name__ == '__main__':
    unittest.main()