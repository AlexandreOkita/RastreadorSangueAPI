from PIL import Image
import unittest
from fhb_blood_status import fhb_image_parser
from fhb_blood_status.common import BloodSupplyStatus

class TestFhbImageParser(unittest.TestCase):
    def setUp(self):
        self.image = Image.open('tests/resources/sample_blood_supply.png')

    def test_image_parsing(self):
        """Test the retrieve_blood_status_from_image function."""
        result = fhb_image_parser.retrieve_blood_status_from_image(self.image)
        
        # Unfortunately python's enum compare fails across modules, so we must compare strings...
        self.assertEqual(result.oPlus.name, BloodSupplyStatus.ALERT.name)
        self.assertEqual(result.oMinus.name, BloodSupplyStatus.CRITIC.name)
        self.assertEqual(result.bPlus.name, BloodSupplyStatus.STABLE.name)
        self.assertEqual(result.bMinus.name, BloodSupplyStatus.ALERT.name)
        self.assertEqual(result.abPlus.name, BloodSupplyStatus.STABLE.name)
        self.assertEqual(result.abMinus.name, BloodSupplyStatus.ALERT.name)
        self.assertEqual(result.aPlus.name, BloodSupplyStatus.REGULAR.name)
        self.assertEqual(result.aMinus.name, BloodSupplyStatus.REGULAR.name)

if __name__ == '__main__':
    unittest.main()