import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument('--no-sandbox')
        # options.add_argument('disable-infobars')
        # options.add_argument("--disable-extensions")
        # options.add_argument("--start-fullscreen")
        # options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://the-internet.herokuapp.com/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
