import math
import os
import json
from typing import ClassVar, Dict, List, Tuple, Optional, TextIO

from BaseClasses import ItemClassification, MultiWorld, Tutorial, CollectionState 
from logging import warning
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from .Items import item_table, ApeEscape3Item, GROUPED_ITEMS
from .Locations import locaiton_table, base_locaiton_id, GROUPED_LOCATIONS
from .Regions import create_regions, ApeEscapeLevel
from .Rules import set_rules
from .Client import ApeEscapeClient
from .Strings import AE3Item, AE3Location
from .RAMAddress import RAM
from .Options import ApeEscape3Options
