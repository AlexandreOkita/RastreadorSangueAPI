import sys
from unittest.mock import patch
sys.path.insert(0, 'hospitals/hc_unicamp/hc_unicamp_crawler_function')

import unittest
from hc_unicamp_blood_status.unicamp_blood_center_crawler import UnicampBloodCenterCrawler, BloodSupplyStatus

class TestUnicampBloodCenterCrawler(unittest.TestCase):

    @patch('requests.get')
    def setUp(self, mock_get):
        """Set up a UnicampBloodCenterCrawler instance and a mock get response for testing."""
        with open('hospitals/hc_unicamp/hc_unicamp_crawler_function/tests/unit/mocked_blood_status.html', 'r') as file:
            mock_get.return_value.text = file.read()
        self.crawler = UnicampBloodCenterCrawler()

    def test_get_supply_with_status(self):
        """Test the get_supply_with_status method."""
        result = self.crawler.get_blood_suplies()
        
        self.assertEqual(result['AB+'], BloodSupplyStatus.STABLE.name)
        self.assertEqual(result['A+'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['B+'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['O+'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['A-'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['B-'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['O-'], BloodSupplyStatus.ALERT.name)
        self.assertEqual(result['AB-'], BloodSupplyStatus.CRITIC.name)

if __name__ == '__main__':
    unittest.main()