from PIL import Image
import pytesseract
from unidecode import unidecode
from common import BloodSupply
from common import BloodSupplyStatus

TOP_CROP_OFFSET = 200
BOTTOM_CROP_OFFSET = 160

FHB_BLOOD_STATUS_MAPPING = {
    'critico': BloodSupplyStatus.CRITIC,
    'baixo': BloodSupplyStatus.ALERT,
    'regular': BloodSupplyStatus.REGULAR,
    'adequado': BloodSupplyStatus.STABLE
}

def __crop_relevant_image_content(original: Image) -> Image:
    width, height = original.size
    return original.crop((0, TOP_CROP_OFFSET, width, height - BOTTOM_CROP_OFFSET))

def retrieve_blood_status_from_image(source: Image) -> BloodSupply:
    treatedImage = __crop_relevant_image_content(source)
    rawContent = pytesseract.image_to_string(treatedImage, config='--psm 6') # Using mode 6 as the content is mostly horizontal lines

    # using unidecode to avoid diacritics, as I feel it could be somewhat unpredictable
    sanitizedContent = (unidecode(word).lower() for word in rawContent.split())
    parsedStatus = [candidate for candidate in sanitizedContent if candidate in FHB_BLOOD_STATUS_MAPPING.keys()]

    if len(parsedStatus) != 8:
        raise Exception("Failed to retrieve the expected blood status from image")
    
    return BloodSupply(
        oPlus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[0]],
        oMinus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[1]],
        bPlus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[2]],
        bMinus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[3]],
        abPlus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[4]],
        abMinus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[5]],
        aPlus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[6]],
        aMinus = FHB_BLOOD_STATUS_MAPPING[parsedStatus[7]]
    )
