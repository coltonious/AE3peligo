from typing import Optional, Dict, Set
from BaseClasses import Location
from worlds.AE3.Strings import AE3Location

# idk if we need base address or not, but this is where they have it in AE1

class ApeEscapeLocation(Location):
    game: str = "Ape Escape 3"

GROUPED_LOCATIONS: Dict[str, Set[str]] = {}

location_table = {
    #0-0 TV Station
    AE3Location.W0L0UkkiPan.value: 1,
    #1-1 Seaside Resort
    AE3Location.W1L1UkkiPia.value: 2,
    AE3Location.W1L1Sarubo.value: 3,
    AE3Location.W1L1Salurin.value: 4,
    AE3Location.W1L1Ukkitan.value: 5,
    AE3Location.W1L1Nessal.value: 6,
    AE3Location.W1L1Morella.value: 7,
    AE3Location.W1L1UkkiBen.value: 8,
    AE3Location.W1L1Kankichi.value: 9,
    AE3Location.W1L1Tomezo.value: 10,
    AE3Location.W1L1Kamayan.value: 11,
    AE3Location.W1L1Taizo.value: 12,
    #1-2 Hide-n-Seek Forest
    AE3Location.W1L2UkkiPon.value: 13,
    AE3Location.W1L2Ukkian.value: 14,
    AE3Location.W1L2UkkiRed.value: 15,
    AE3Location.W1L2Rosalin.value: 16,
    AE3Location.W1L2Salubon.value: 17,
    AE3Location.W1L2Wolfmon.value: 18,
    AE3Location.W1L2Ukiko.value: 19,
    AE3Location.W1L2Lambomon.value: 20,
    AE3Location.W1L2Kreemon.value: 21,
    AE3Location.W1L2Ukkilei.value: 22,
    AE3Location.W1L2Spork.value: 23,
    AE3Location.W1L2KingGoat.value: 24,
    AE3Location.W1L2Marukichi.value: 25,
    AE3Location.W1L2Kikimon.value: 26,
    AE3Location.W1L2Kominato.value: 27,
    #1-3 Saru-Mon's Castle
    AE3Location.W1L3Ukkido.value: 28,
    AE3Location.W1L3PipoGuard.value: 29,
    AE3Location.W1L3Monderella.value: 30,
    AE3Location.W1L3UkkiIchi.value: 31,
    AE3Location.W1L3SaruMon.value: 32,
    AE3Location.W1L3Monga.value: 33,
    AE3Location.W1L3Ukkiton.value: 34,
    AE3Location.W1L3KingLeo.value: 35,
    AE3Location.W1L3Ukkii.value: 36,
    AE3Location.W1L3Saluto.value: 37,
    AE3Location.W1L3SAL1000.value: 38,
    AE3Location.W1L3Ukkinee.value: 39,
    AE3Location.W1L3KingsDouble.value: 40,
    AE3Location.W1L3Mattsun.value: 41,
    AE3Location.W1L3Miya.value: 42,
    AE3Location.W1L3MonSan.value: 43,
    #1-Boss
    AE3Location.W1LBMonkeyWhite: 44,
}

def createLocationGroups():
    #iterate through all locations
    for x in range (0, len(location_table) - 1):
        locname = list(location_table.keys())[x]
        #add to location group for each level
        if "0-0" in locname:
            GROUPED_LOCATIONS.setdefault("TV Station", []).append(locname)
        elif "1-1" in locname:
            GROUPED_LOCATIONS.setdefault("Seaside Resort", []).append(locname)
        elif "1-2" in locname:
            GROUPED_LOCATIONS.setdefault("Hide-n-Seek Forest", []).append(locname)
        elif "1-3" in locname:
            GROUPED_LOCATIONS.setdefault("Sarumon's Castle", []).append(locname)
        elif "1-b" in locname:
            GROUPED_LOCATIONS.setdefault("bosses", []).append(locname)
