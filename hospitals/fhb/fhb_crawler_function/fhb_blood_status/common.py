from dataclasses import dataclass
from enum import Enum
from typing import Dict

class BloodSupplyStatus(Enum):
    CRITIC = 0
    ALERT = 1
    REGULAR = 2
    STABLE = 3

@dataclass
class BloodSupply:
    oPlus: BloodSupplyStatus
    oMinus: BloodSupplyStatus
    aPlus: BloodSupplyStatus
    aMinus: BloodSupplyStatus
    bPlus: BloodSupplyStatus
    bMinus: BloodSupplyStatus
    abPlus: BloodSupplyStatus
    abMinus: BloodSupplyStatus

    def toDynamoData(self) -> Dict[str, str]:
        return {
            'o_plus_status': self.oPlus.name,
            'o_minus_status': self.oMinus.name,
            'a_plus_status': self.aPlus.name,
            'a_minus_status': self.aMinus.name,
            'b_plus_status': self.bPlus.name,
            'b_minus_status': self.bMinus.name,
            'ab_plus_status': self.abPlus.name,
            'ab_minus_status': self.abMinus.name
        }