def qualities():
    qualities_list = {
        0: 'Normal',
        1: 'Genuine',
        3: 'Vintage',
        5: 'Unusual',  # defindex 134 for effect
        6: 'Unique',
        7: 'Community',
        8: 'Valve',
        9: 'Self-Made',
        11: 'Strange',  # defindex 214 holds strange kill/score count in value
        13: 'Haunted',
        14: 'Collectors',
        15: 'Decorated Weapon',
    }
    return qualities_list


def origins():
    item_origins = {
        0: 'Timed Drop',
        1: 'Achievement',
        2: 'Purchased',
        3: 'Traded',
        4: 'Crafted',
        5: 'Store Promotion',
        6: 'Gifted',
        7: 'Support Granted',
        8: 'Found in Crate',
        9: 'Earned',
        10: 'Third-Party Promotion',
        11: 'Wrapped Gift',
        12: 'Halloween Drop',
        13: 'Steam Purchase',
        14: 'Foreign Item',
        15: 'CD Key',
        16: 'Collection Reward',
        17: 'Preview Item',
        18: 'Steam Workshop Contribution',
        19: 'Periodic score reward',
        20: 'MvM Badge completion reward',
        21: 'MvM Squad surplus reward',
        22: 'Recipe output',
        23: 'Quest Drop',
        24: 'Quest Loaner Item',
        25: 'Trade-Up',
        26: 'Viral Competitive Beta Pass Spread',
        27: 'CYOA Blood Money Purchase',
        28: 'War Paint',
        29: 'Untradable Free Contract Reward'
    }
    return item_origins


def weapons():
    weapons_list = {
        13: "Scattergun",
        200: "Scattergun",
        45: "Force-A-Nature",
        220: "The Shortstop",
        448: "The Soda Popper",
        669: "Festive Scattergun",
        772: "Baby Face\'s Blaster",
        799: "Silver Botkiller Scattergun Mk.I",
        808: "Gold Botkiller Scattergun Mk.I",
        888: "Rust Botkiller Scattergun Mk.I",
        897: "Blood Botkiller Scattergun Mk.I",
        906: "Carbonado Botkiller Scattergun Mk.I",
        915: "Diamond Botkiller Scattergun Mk.I",
        964: "Silver Botkiller Scattergun Mk.II",
        973: "Gold Botkiller Scattergun Mk.II",
        1078: "Festive Force-A-Nature",
        1103: "The Back Scatter",
        15002: "Night Terror",
        15015: "Tartan Torpedo",
        15021: "Country Crusher",
        15029: "Backcountry Blaster",
        15036: "Spruce Deuce",
        15053: "Current Event",
        15065: "Macabre Web",
        15069: "Nutcracker",
        15106: "Blue Mew",
        15107: "Flower Power",
        15108: "Shot to Hell",
        15131: "Coffin Nail",
        15151: "Killer Bee",
        15157: "Corsair",

        23: "Scout\'s Pistol",
        209: "Pistol",
        46: "Bonk! Atomic Punch",
        160: "Vintage Lugermorph",
        163: "Crit-a-Cola",
        222: "Mad Milk",
        294: "Lugermorph",
        449: "The Winger",
        773: "Pretty Boy\'s Pocket Pistol",
        812: "The Flying Guillotine",
        833: "The Flying Guillotine",
        1121: "Mutated Milk",
        1145: "Festive Bonk!",
        15013: "Red Rock Roscoe",
        15018: "Homemade Heater",
        15035: "Hickory Holepuncher",
        15041: "Local Hero",
        15046: "Black Dahlia",
        15056: "Sandstone Special",
        15060: "Macabre Web",
        15061: "Nutcracker",
        15100: "Blue Mew",
        15101: "Brain Candy",
        15102: "Shot to Hell",
        15126: "Dressed To Kill",
        15148: "Blitzkrieg",
        30666: "The C.A.P.P.E.R.",

        0: "Bat",
        190: "Bat",
        44: "The Sandman",
        221: "The Holy Mackerel",
        264: "Frying Pan",
        317: "The Candy Cane",
        325: "The Boston Basher",
        349: "Sun-on-a-Stick",
        355: "The Fan O\'War",
        423: "Saxxy",
        450: "The Atomizer",
        452: "Three-Rune Blade",
        474: "The Conscientious Objector",
        572: "Unarmed Combat",
        648: "The Wrap Assassin",
        660: "Festive Bat",
        880: "The Freedom Staff",
        939: "The Bat Outta Hell",
        954: "The Memory Maker",
        999: "Festive Holy Mackerel",
        1013: "The Ham Shank",
        1071: "Gold Frying Pan",
        1123: "The Necro Smasher",
        1127: "The Crossing Guard",
        30667: "Batsaber",
        30758: "Prinny Machete",

        18: "Rocket Launcher",
        205: "Rocket Launcher",
        127: "The Direct Hit",
        228: "The Black Box",
        237: "Rocket Jumper",
        414: "The Liberty Launcher",
        441: "The Cow Mangler 5000",
        513: "The Original",
        658: "Festive Rocket Launcher",
        730: "The Beggar\'s Bazooka",
        800: "Silver Botkiller Rocket Launcher Mk.I",
        809: "Gold Botkiller Rocket Launcher Mk.I",
        889: "Rust Botkiller Rocket Launcher Mk.I",
        898: "Blood Botkiller Rocket Launcher Mk.I",
        907: "Carbonado Botkiller Rocket Launcher Mk.I",
        916: "Diamond Botkiller Rocket Launcher Mk.I",
        965: "Silver Botkiller Rocket Launcher Mk.II",
        974: "Gold Botkiller Rocket Launcher Mk.II",
        1085: "Festive Black Box",
        1104: "The Air Strike",
        15006: "Woodland Warrior",
        15014: "Sand Cannon",
        15028: "American Pastoral",
        15043: "Smalltown Bringdown",
        15052: "Shell Shocker",
        15057: "Aqua Marine",
        15081: "Autumn",
        15104: "Blue Mew",
        15105: "Brain Candy",
        15129: "Coffin Nail",
        15130: "High Roller\'s",
        15150: "Warhawk",

        10: "Soldier\'s Shotgun",
        199: "Shotgun",
        129: "The Buff Banner",
        133: "Gunboats",
        226: "The Battalion\'s Backup",
        354: "The Concheror",
        415: "The Reserve Shooter",
        442: "The Righteous Bison",
        444: "The Mantreads",
        1001: "Festive Buff Banner",
        1101: "The B.A.S.E. Jumper",
        1141: "Festive Shotgun",
        1153: "Panic Attack",
        15003: "Backwoods Boomstick",
        15016: "Rustic Ruiner",
        15044: "Civic Duty",
        15047: "Lightning Rod",
        15085: "Autumn",
        15109: "Flower Power",
        15132: "Coffin Nail",
        15133: "Dressed to Kill",
        15152: "Red Bear",

        6: "Shovel",
        196: "Shovel",
        128: "The Equalizer",
        154: "The Pain Train",
        357: "The Half-Zatoichi",
        416: "The Market Gardener",
        447: "The Disciplinary Action",
        775: "The Escape Plan",

        21: "Flame Thrower",
        208: "Flame Thrower",
        40: "The Backburner",
        215: "The Degreaser",
        594: "The Phlogistinator",
        659: "Festive Flame Thrower",
        741: "The Rainblower",
        798: "Silver Botkiller Flame Thrower Mk.I",
        807: "Gold Botkiller Flame Thrower Mk.I",
        887: "Rust Botkiller Flame Thrower Mk.I",
        896: "Blood Botkiller Flame Thrower Mk.I",
        905: "Carbonado Botkiller Flame Thrower Mk.I",
        914: "Diamond Botkiller Flame Thrower Mk.I",
        963: "Silver Botkiller Flame Thrower Mk.II",
        972: "Gold Botkiller Flame Thrower Mk.II",
        1146: "Festive Backburner",
        1178: "Dragon\'s Fury",
        15005: "Forest Fire",
        15017: "Barn Burner",
        15030: "Bovine Blazemaker",
        15034: "Earth",
        15049: "Flash Fryer",
        15054: "Turbine Torcher",
        15066: "Autumn",
        15067: "Pumpkin Patch",
        15068: "Nutcracker",
        15089: "Balloonicorn",
        15090: "Rainbow",
        15115: "Coffin Nail",
        15141: "Warhawk",
        30474: "Nostromo Napalmer",

        12: "Pyro\'s Shotgun",
        39: "The Flare Gun",
        351: "The Detonator",
        595: "The Manmelter",
        740: "The Scorch Shot",
        1081: "Festive Flare Gun",
        1179: "Thermal Thruster",
        1180: "Gas Passer",

        2: "Fire Axe",
        192: "Fire Axe",
        38: "The Axtinguisher",
        153: "Homewrecker",
        214: "The Powerjack",
        326: "The Back Scratcher",
        348: "Sharpened Volcano Fragment",
        457: "The Postal Pummeler",
        466: "The Maul",
        593: "The Third Degree",
        739: "The Lollichop",
        813: "Neon Annihilator",
        834: "Neon Annihilator",
        1000: "The Festive Axtinguisher",
        1181: "Hot Hand",

        19: "Grenade Launcher",
        206: "Grenade Launcher",
        308: "The Loch-n-Load",
        405: "Ali Baba\'s Wee Booties",
        608: "The Bootlegger",
        996: "The Loose Cannon",
        1007: "Festive Grenade Launcher",
        1151: "The Iron Bomber",
        15077: "Autumn",
        15079: "Macabre Web",
        15091: "Rainbow",
        15092: "Sweet Dreams",
        15116: "Coffin Nail",
        15117: "Top Shelf",
        15142: "Warhawk",
        15158: "Butcher Bird",

        20: "Stickybomb Launcher",
        207: "Stickybomb Launcher",
        130: "The Scottish Resistance",
        131: "The Chargin\' Targe",
        265: "Sticky Jumper",
        406: "The Splendid Screen",
        661: "Festive Stickybomb Launcher",
        797: "Silver Botkiller Stickybomb Launcher Mk.I",
        806: "Gold Botkiller Stickybomb Launcher Mk.I",
        886: "Rust Botkiller Stickybomb Launcher Mk.I",
        895: "Blood Botkiller Stickybomb Launcher Mk.I",
        904: "Carbonado Botkiller Stickybomb Launcher Mk.I",
        913: "Diamond Botkiller Stickybomb Launcher Mk.I",
        962: "Silver Botkiller Stickybomb Launcher Mk.II",
        971: "Gold Botkiller Stickybomb Launcher Mk.II",
        1099: "The Tide Turner",
        1144: "Festive Targe",
        1150: "The Quickiebomb Launcher",
        15009: "Sudden Flurry",
        15012: "Carpet Bomber",
        15024: "Blasted Bombardier",
        15038: "Rooftop Wrangler",
        15045: "Liquid Asset",
        15048: "Pink Elephant",
        15082: "Autumn",
        15083: "Pumpkin Patch",
        15084: "Macabre Web",
        15113: "Sweet Dreams",
        15137: "Coffin Nail",
        15138: "Dressed to Kill",
        15155: "Blitzkrieg",

        1: "Bottle",
        191: "Bottle",
        132: "The Eyelander",
        172: "The Scotsman\'s Skullcutter",
        266: "Horseless Headless Horsemann\'s Headtaker",
        307: "Ullapool Caber",
        327: "The Claidheamh Mòr",
        404: "The Persian Persuader",
        482: "Nessie\'s Nine Iron",
        609: "The Scottish Handshake",
        1082: "Festive Eyelander",

        15: "Minigun",
        202: "Minigun",
        41: "Natascha",
        298: "Iron Curtain",
        312: "The Brass Beast",
        424: "Tomislav",
        654: "Festive Minigun",
        793: "Silver Botkiller Minigun Mk.I",
        802: "Gold Botkiller Minigun Mk.I",
        811: "The Huo-Long Heater",
        832: "The Huo-Long Heater",
        850: "Deflector (MvM only?)",
        882: "Rust Botkiller Minigun Mk.I",
        891: "Blood Botkiller Minigun Mk.I",
        900: "Carbonado Botkiller Minigun Mk.I",
        909: "Diamond Botkiller Minigun Mk.I",
        958: "Silver Botkiller Minigun Mk.II",
        967: "Gold Botkiller Minigun Mk.II",
        15004: "King of the Jungle",
        15020: "Iron Wood",
        15026: "Antique Annihilator",
        15031: "War Room",
        15040: "Citizen Pain",
        15055: "Brick House",
        15086: "Macabre Web",
        15087: "Pumpkin Patch",
        15088: "Nutcracker",
        15098: "Brain Candy",
        15099: "Mister Cuddles",
        15123: "Coffin Nail",
        15124: "Dressed to Kill",
        15125: "Top Shelf",
        15147: "Butcher Bird",

        11: "Heavy\'s Shotgun",
        42: "Sandvich",
        159: "The Dalokohs Bar",
        311: "The Buffalo Steak Sandvich",
        425: "The Family Business",
        433: "Fishcake",
        863: "Robo-Sandvich",
        1002: "Festive Sandvich",
        1190: "Second Banana",

        5: "Fists",
        195: "Fists",
        43: "The Killing Gloves of Boxing",
        239: "Gloves of Running Urgently",
        310: "Warrior\'s Spirit",
        331: "Fists of Steel",
        426: "The Eviction Notice",
        587: "Apoco-Fists",
        656: "The Holiday Punch",
        1084: "Festive Gloves of Running Urgently (G.R.U.)",
        1100: "The Bread Bite",
        1184: "Gloves of Running Urgently MvM",

        9: "Engineer\'s Shotgun",
        141: "The Frontier Justice",
        527: "The Widowmaker",
        588: "The Pomson 6000",
        997: "The Rescue Ranger",
        1004: "Festive Frontier Justice",

        22: "Engineer\'s Pistol",
        140: "The Wrangler",
        528: "The Short Circuit",
        1086: "Festive Wrangler",
        30668: "The Gigar Counter",

        7: "Wrench",
        197: "Wrench",
        142: "The Gunslinger",
        155: "The Southern Hospitality",
        169: "Golden Wrench",
        329: "The Jag",
        589: "The Eureka Effect",
        662: "Festive Wrench",
        795: "Silver Botkiller Wrench Mk.I",
        804: "Gold Botkiller Wrench Mk.I",
        884: "Rust Botkiller Wrench Mk.I",
        893: "Blood Botkiller Wrench Mk.I",
        902: "Carbonado Botkiller Wrench Mk.I",
        911: "Diamond Botkiller Wrench Mk.I",
        960: "Silver Botkiller Wrench Mk.II",
        969: "Gold Botkiller Wrench Mk.II",

        15073: "Nutcracker",
        15074: "Autumn",
        15075: "Boneyard",
        15139: "Dressed to Kill",
        15140: "Top Shelf",
        15114: "Torqued to Hell",
        15156: "Airwolf",

        25: "Construction PDA",
        737: "Construction PDA",

        26: "Destruction PDA",

        28: "Toolbox)",

        17: "Syringe Gun",
        204: "Syringe Gun",
        36: "The Blutsauger",
        305: "Crusader\'s Crossbow",
        412: "The Overdose",
        1079: "Festive Crusader\'s Crossbow",

        29: "Medi Gun",
        211: "Medi Gun(Renamed/Strange)",
        35: "The Kritzkrieg",
        411: "The Quick-Fix",
        663: "Festive Medi Gun",
        796: "Silver Botkiller Medi Gun Mk.I",
        805: "Gold Botkiller Medi Gun Mk.I",
        885: "Rust Botkiller Medi Gun Mk.I",
        894: "Blood Botkiller Medi Gun Mk.I",
        903: "Carbonado Botkiller Medi Gun Mk.I",
        912: "Diamond Botkiller Medi Gun Mk.I",
        961: "Silver Botkiller Medi Gun Mk.II",
        970: "Gold Botkiller Medi Gun Mk.II",
        998: "The Vaccinator",
        15008: "Masked Mender",
        15010: "Wrapped Reviver",
        15025: "Reclaimed Reanimator",
        15039: "Civil Servant",
        15050: "Spark of Life",
        15078: "Wildwood",
        15097: "Flower Power",
        15121: "Dressed To Kill",
        15122: "High Roller\'s",
        15145: "Blitzkrieg",
        15146: "Corsair",

        8: "Bonesaw",
        198: "Bonesaw",
        37: "The Ubersaw",
        173: "The Vita-Saw",
        304: "Amputator",
        413: "The Solemn Vow",
        1003: "Festive Ubersaw",
        1143: "Festive Bonesaw",

        14: "Sniper Rifle",
        201: "Sniper Rifle",
        56: "The Huntsman",
        230: "The Sydney Sleeper",
        402: "The Bazaar Bargain",
        526: "The Machina",
        664: "Festive Sniper Rifle",
        752: "The Hitman\'s Heatmaker",
        792: "Silver Botkiller Sniper Rifle Mk.I",
        801: "Gold Botkiller Sniper Rifle Mk.I",
        851: "The AWPer Hand",
        881: "Rust Botkiller Sniper Rifle Mk.I",
        890: "Blood Botkiller Sniper Rifle Mk.I",
        899: "Carbonado Botkiller Sniper Rifle Mk.I",
        908: "Diamond Botkiller Sniper Rifle Mk.I",
        957: "Silver Botkiller Sniper Rifle Mk.II",
        966: "Gold Botkiller Sniper Rifle Mk.II",
        1005: "Festive Huntsman",
        1092: "The Fortified Compound",
        1098: "The Classic",
        15000: "Night Owl",
        15007: "Purple Range",
        15019: "Lumber From Down Under",
        15023: "Shot in the Dark",
        15033: "Bogtrotter",
        15059: "Thunderbolt",
        15070: "Pumpkin Patch",
        15071: "Boneyard",
        15072: "Wildwood",
        15111: "Balloonicorn",
        15112: "Rainbow",
        15135: "Coffin Nail",
        15136: "Dressed to Kill",
        15154: "Airwolf",
        30665: "Shooting Star",

        16: "SMG",
        203: "SMG",
        57: "The Razorback",
        58: "Jarate",
        231: "Darwin\'s Danger Shield",
        642: "Cozy Camper",
        751: "The Cleaner\'s Carbine",
        1083: "Festive Jarate",
        1105: "The Self-Aware Beauty Mark",
        1149: "Festive SMG",
        15001: "Woodsy Widowmaker",
        15022: "Plaid Potshotter",
        15032: "Treadplate Tormenter",
        15037: "Team Sprayer",
        15058: "Low Profile",
        15076: "Wildwood",
        15110: "Blue Mew",
        15134: "High Roller\'s",
        15153: "Blitzkrieg",

        3: "Kukri",
        193: "Kukri",
        171: "The Tribalman\'s Shiv",
        232: "The Bushwacka",
        401: "The Shahanshah",

        24: "Revolver",
        210: "Revolver",
        61: "The Ambassador",
        161: "Big Kill",
        224: "L\'Etranger",
        460: "The Enforcer",
        525: "The Diamondback",
        1006: "Festive Ambassador",
        1142: "Festive Revolver",
        15011: "Psychedelic Slugger",
        15027: "Old Country",
        15042: "Mayor",
        15051: "Dead Reckoner",
        15062: "Boneyard",
        15063: "Wildwood",
        15064: "Macabre Web",
        15103: "Flower Power",
        15128: "Top Shelf",
        15127: "Coffin Nail",
        15149: "Blitzkrieg",

        735: "Sapper",
        736: "Sapper",
        810: "The Red-Tape Recorder",
        831: "The Red-Tape Recorder",
        933: "The Ap-Sap",
        1080: "Festive Sapper",
        1102: "The Snack Attack",

        4: "Knife",
        194: "Knife",
        225: "Your Eternal Reward",
        356: "Conniver\'s Kunai",

        461: "The Big Earner",
        574: "The Wanga Prick",
        638: "The Sharp Dresser",
        649: "The Spy-cicle",
        665: "Festive Knife",
        727: "The Black Rose",
        794: "Silver Botkiller Knife Mk.I",
        803: "Gold Botkiller Knife Mk.I",
        883: "Rust Botkiller Knife Mk.I",
        892: "Blood Botkiller Knife Mk.I",
        901: "Carbonado Botkiller Knife Mk.I",
        910: "Diamond Botkiller Knife Mk.I",
        959: "Silver Botkiller Knife Mk.II",
        968: "Gold Botkiller Knife Mk.II",
        15094: "Blue Mew",
        15095: "Brain Candy",
        15096: "Stabbed to Hell",
        15118: "Dressed to Kill",
        15119: "Top Shelf",
        15143: "Blitzkrieg",
        15144: "Airwolf",

        27: "Disguise Kit",

        30: "Invis Watch",
        212: "Invis Watch",
        59: "The Dead Ringer",
        60: "The Cloak and Dagger",
        297: "Enthusiast\'s Timepiece",
        947: "The Quackenbirdt"
    }
    return weapons_list


def scout_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def soldier_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def pyro_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def demoman_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def heavy_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def engineer_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def medic_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def sniper_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def spy_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def allclass_cosmetics():
    cosmetics_list = {

    }
    return cosmetics_list


def action_items():
    action_items_list = {

    }
    return action_items_list


def taunts():
    taunt_list = {

    }
    return taunt_list


def craft_items():
    craft_items_list = {

    }
    return craft_items_list


def tools():
    tools_list = {

    }
    return tools_list


# ˅ Attributes ˅ #######################################################################################################


# defindex 2025 || uses float_value
def killstreak():
    killstreak_tier_list = {
        1: 'Basic',
        2: 'Specialized',
        3: 'Professional'
    }
    return killstreak_tier_list


# defindex 2014 || uses float_value
def sheen():
    sheen_list = {
        1: 'Team Shine',
        2: 'Deadly Daffodil',
        3: 'Manndarin',
        4: 'Mean Green',
        5: 'Agonizing Emerald',
        6: 'Villainous Violet',
        7: 'Hot Rod'
    }
    return sheen_list


# defindex 2013 || uses float_value
def killstreaker():
    killstreaker_list = {
        2002: 'Fire Horns',
        2003: 'Cerebral Discharge',
        2004: 'Tornado',
        2005: 'Flames',
        2006: 'Singularity',
        2007: 'Incinerator',
        2008: 'Hypno-Beam',
    }
    return killstreaker_list


# defindex 134 || uses float_value
def unusuals():
    unusuals_list = {
        4: 'Community Sparkle',

        6: 'Green Confetti',
        7: 'Purple Confetti',
        8: 'Haunted Ghosts',
        9: 'Green Energy',
        10: 'Purple Energy',
        11: 'Circling TF Logo',
        12: 'Massed Flies',
        13: 'Burning Flames',
        14: 'Scorching Flames',
        15: 'Searing Plasma',
        16: 'Vivid Plasma',
        17: 'Sunbeams',
        18: 'Circling Peace Sign',
        19: 'Circling Heart',

        29: 'Stormy Storm',
        30: 'Blizzardy Storm',
        31: 'Nuts n\' Bolts',
        32: 'Orbiting Planets',
        33: 'Orbiting Fire',
        34: 'Bubbling',
        35: 'Smoking',
        36: 'Steaming',

        37: 'Flaming Lantern',
        38: 'Cloudy Moon',
        39: 'Cauldron Bubbles',
        40: 'Eerie Orbiting Fire',

        43: 'Knifestorm',
        44: 'Misty Skull',
        45: 'Harvest Moon',
        46: 'Secret to Everybody',
        47: 'Stormy 13th Hour',

        55: 'Aces High',
        56: 'Kill-a-Watt',
        57: 'Terror-Watt',
        58: 'Cloud 9',
        59: 'Aces High',
        60: 'Dead Presidents',
        61: 'Miami Nights',
        62: 'Disco Beat Down',

        63: 'Phosphorous',
        64: 'Sulphorous',
        65: 'Memory Leak',
        66: 'Overclocked',
        67: 'Electrostatic',
        68: 'Power Surge',
        69: 'Anti-Freeze',
        70: 'Time Warp',
        71: 'Green Black Hole',
        72: 'Roboactive',

        73: 'Arcana',
        74: 'Spellbound',
        75: 'Chiroptera Venenata',
        76: 'Poisoned Shadows',
        77: 'Something Burning This Way Comes',
        78: 'Hellfire',
        79: 'Darkblaze',
        80: 'Demonflame',

        81: 'Bonzo The All-Gnawing',
        82: 'Amaranthine',
        83: 'Stare from Beyond',
        84: 'The Ooze',
        85: 'Ghastly Ghosts Jr.',
        86: 'Haunted Phantasm Jr.',

        87: 'Frostbite',
        88: 'Molten Mallard',
        89: 'Morning glory',
        90: 'Death at Dusk',

        91: 'Abduction',
        92: 'Atomic',
        93: 'Subatomic',
        94: 'Electric Hat Protector',
        95: 'Magnetic Hat Protector',
        96: 'Voltaic Hat Protector',
        97: 'Galactic Codex',
        98: 'Ancient Codex',
        99: 'Nebula',

        100: 'Death by Disco',
        101: 'Mystery to Everyone',
        102: 'Puzzle to Me',
        103: 'Ether Trail',
        104: 'Nether Trail',
        105: 'Ancient Eldritch',
        106: 'Eldritch Flame',

        107: 'Neutron Star',
        108: 'Tesla Coil',
        109: 'Starstorm Insomnia',
        110: 'Starstorm Slumber',

        111: 'Brain Drain',
        112: 'Open Mind',
        113: 'Head of Steam',
        114: 'Galactic Gateway',
        115: 'The Eldritch Opening',
        116: 'The Dark Doorway',
        117: 'Ring of Fire',
        118: 'Vicious Circle',
        119: 'White Lightning',
        120: 'Omniscient Orb',
        121: 'Clairvoyance',

        122: 'Fifth Dimension',
        123: 'Vicious Vortex',
        124: 'Menacing Miasma',
        125: 'Abyssal Aura',
        126: 'Wicked Wood',
        127: 'Ghastly Grove',
        128: 'Mystical Medley',
        129: 'Ethereal Essence',
        130: 'Twisted Radiance',
        131: 'Violet Vortex',
        132: 'Verdant Vortex',
        133: 'Valiant Vortex',

        134: 'Sparkling Lights',
        135: 'Frozen Icefall',
        136: 'Fragmented Gluons',
        137: 'Fragmented Quarks',
        138: 'Fragmented Photons',
        139: 'Defragmenting Reality',
        140: 'Defragmenting Reality',
        141: 'Fragmenting Reality',
        142: 'Refragmenting Reality',
        143: 'Snowfallen',
        144: 'Snowblinded',
        145: 'Pyroland Daydream',
        146: 'Pyroland Daydream',

        147: 'Verdatica',
        148: 'Aromatica',
        149: 'Chromatica',
        150: 'Prismatica',
        151: 'Bee Swarm',
        152: 'Frisky Fireflies',
        153: 'Smoldering Spirits',
        154: 'Wandering Wisps',
        155: 'Kaleidoscope',

        156: 'Green Giggler',
        157: 'Laugh-O-Lantern',
        158: 'Plum Prankster',
        159: 'Pyroland Nightmare',
        160: 'Gravelly Ghoul',
        161: 'Vexed Volcanics',
        162: 'Gourdian Angel',
        163: 'Pumpkin Party',

        164: 'Frozen Fractals',
        165: 'Lavender Landfall',
        166: 'Special Snowfall',
        167: 'Divine Desire',
        168: 'Distant Dream',
        169: 'Violent Wintertide',
        170: 'Blighted Snowstorm',
        171: 'Pale Nimbus',
        172: 'Genus Plasmos',
        173: 'Serenus Lumen',
        174: 'Ventum Maris',
        175: 'Mirthful Mistletoe',
        176: 'Mirthful Mistletoe',

        177: 'Resonation',
        178: 'Aggradation',
        179: 'Lucidation',
        180: 'Stunning',
        181: 'Ardentum Saturnalis',
        182: 'Fragrancium Elementalis',
        183: 'Reverium Irregularis',
        184: 'Reverium Irregularis',
        185: 'Perennial Petals',
        186: 'Flavorsome Sunset',
        187: 'Raspberry Bloom',
        188: 'Iridescence',

        189: 'Tempered Thorns',
        190: 'Devilish Diablo',
        191: 'Severed Serration',
        192: 'Shrieking Shades',
        193: 'Restless Wraiths',
        194: 'Restless Wraiths',
        195: 'Infernal Wraith',
        196: 'Phantom Crown',
        197: 'Ancient Specter',
        198: 'Viridescent Peeper',
        199: 'Eyes of Molten',
        200: 'Ominous Stare',
        201: 'Pumpkin Moon',
        202: 'Frantic Spooker',
        203: 'Frightened Poltergeist',
        204: 'Energetic Haunter',

        205: 'Smissmas Tree',
        206: 'Hospitable Festivity',
        207: 'Condescending Embrace',
        208: 'Condescending Embrace',
        209: 'Sparkling Spruce',
        210: 'Glittering Juniper',
        211: 'Prismatic Pine',
        212: 'Spiraling Lights',
        213: 'Twisting Lights',
        214: 'Stardust Pathway',
        215: 'Flurry Rush',
        216: 'Spark of Smissmas',
        217: 'Spark of Smissmas',
        218: 'Polar Forecast',
        219: 'Shining Stag',
        220: 'Holiday Horns',
        221: 'Ardent Antlers',
        222: 'Ardent Antlers',
        223: 'Festive Lights',

        224: 'Crustacean Sensation',
        225: 'Crustacean Sensation',
        226: 'Frosted Decadence',
        227: 'Frosted Decadence',
        228: 'Sprinkled Delights',
        229: 'Terrestrial Favor',
        230: 'Tropical Thrill',
        231: 'Flourishing Passion',
        232: 'Dazzling Fireworks',
        233: 'Blazing Fireworks',
        234: 'Shimmering Fireworks',
        235: 'Twinkling Fireworks',
        236: 'Sparkling Fireworks',
        237: 'Glowing Fireworks',
        238: 'Glimmering Fireworks',
        239: 'Flying Lights',
        240: 'Flying Lights',
        241: 'Limelight',
        242: 'Shining Star',
        243: 'Cold Cosmos',
        244: 'Refracting Fractals',
        245: 'Startrance',
        246: 'Startrance',
        247: 'Starlush',
        248: 'Starfire',
        249: 'Stardust',
        250: 'Contagious Eruption',
        251: 'Daydream Eruption',
        252: 'Volcanic Eruption',
        253: 'Divine Sunlight',
        254: 'Audiophile',
        255: 'Soundwave',
        256: 'Synesthesia',

        257: 'Haunted Kraken',
        258: 'Eerie Kraken',
        259: 'Soulful Slice',
        260: 'Horsemann\'s Hack',
        261: 'Haunted Forever!',
        262: 'Haunted Forever!',
        263: 'Forever And Forever!',
        264: 'Cursed Forever!',
        265: 'Moth Plague',
        266: 'Malevolent Monoculi',
        267: 'Haunted Wick',
        268: 'Haunted Wick',
        269: 'Wicked Wick',
        270: 'Spectral Wick',

        271: 'Musical Maelstrom',
        272: 'Verdant Virtuoso',
        273: 'Silver Serenade',
        274: 'Cosmic Constellations',
        275: 'Cosmic Constellations',
        276: 'Dazzling Constellations',
        277: 'Tainted Frost',
        278: 'Starlight Haze',

        279: 'Hard Carry',
        280: 'Hard Carry',
        281: 'Jellyfish Field',
        282: 'Jellyfish Field',
        283: 'Jellyfish Hunter',
        284: 'Jellyfish Jam',
        285: 'Global Clusters',
        286: 'Celestial Starburst',
        287: 'Sylicone Succiduous',
        288: 'Sakura Smoke Bomb',
        289: 'Treasure Trove',
        290: 'Bubble Breeze',
        291: 'Fireflies',
        292: 'Mountain Halo'
    }
    return unusuals_list


# defindex 2041 || uses value
def taunt_unusuals():
    taunt_unusuals_list = {
        3001: 'Showstopper',
        3002: 'Showstopper',
        3003: 'Holy Grail',
        3004: '\'72',
        3005: 'Fountain of Delight',
        3006: 'Screaming Tiger',
        3007: 'Skill Gotten Gains',
        3008: 'Midnight Whirlwind',
        3009: 'Silver Cyclone',
        3010: 'Mega Strike',

        3011: 'Haunted Phantasm',
        3012: 'Ghastly Ghosts',

        3013: 'Hellish Inferno',
        3014: 'Spectral Swirl',
        3015: 'Infernal Flames',
        3016: 'Infernal Smoke',

        3017: 'Acid Bubbles of Envy',
        3018: 'Flammable Bubbles of Attraction',
        3019: 'Poisonous Bubbles of Regret',
        3020: 'Roaring Rockets',
        3021: 'Spooky Night',
        3022: 'Ominous Night',

        3023: 'Bewitched',
        3024: 'Accursed',
        3025: 'Enchanted',
        3026: 'Static Mist',
        3027: 'Eerie Lightning',
        3028: 'Terrifying Thunder',
        3029: 'Jarate Shock',
        3030: 'Nether Void',

        3031: 'Good-Hearted Goodies',
        3032: 'Wintery Wisp',
        3033: 'Arctic Aurora',
        3034: 'Winter Spirit',
        3035: 'Festive Spirit',
        3036: 'Magical Spirit',

        3037: 'Spectral Escort',
        3038: 'Astral Presence',
        3039: 'Arcane Assistance',
        3040: 'Arcane Assistance',
        3041: 'Emerald Allurement',
        3042: 'Pyrophoric Personality',
        3043: 'Spellbound Aspect',
        3044: 'Static Shock',
        3045: 'Veno Shock',
        3046: 'Toxic Terrors',
        3047: 'Arachnid Assault',
        3048: 'Creepy Crawlies',

        3049: 'Delightful Star',
        3050: 'Frosted Star',
        3051: 'Apotheosis',
        3052: 'Ascension',
        3053: 'Reindoonicorn Rancher',
        3054: 'Reindoonicorn Rancher',
        3055: 'Twinkling Lights',
        3056: 'Shimmering Lights',

        3059: 'Spectral Shackles',
        3060: 'Cursed Confinement',
        3061: 'Cavalier de Carte',
        3062: 'Cavalier de Carte',
        3063: 'Hollow Flourish',
        3064: 'Magic Shuffle',
        3065: 'Vigorous Pulse',
        3066: 'Thundering Spirit',
        3067: 'Galvanic Defiance',
        3068: 'Wispy Halos',
        3069: 'Nether Wisps',
        3070: 'Aurora Borealis',
        3071: 'Aurora Australis',
        3072: 'Aurora Polaris',

        3073: 'Amethyst Winds',
        3074: 'Golden Gusts',
        3075: 'Smissmas Swirls',
        3076: 'Smissmas Swirls',
        3077: 'Minty Cypress',
        3078: 'Pristine Pine',
        3079: 'Sparkly Spruce',
        3080: 'Sparkly Spruce',
        3081: 'Festive Fever',
        3082: 'Festive Fever',
        3083: 'Golden Glimmer',
        3084: 'Frosty Silver',
        3085: 'Glamorous Dazzle',
        3086: 'Glamorous Dazzle',
        3087: 'Sublime Snowstorm',

        3088: 'Marigold Ritual',
        3089: 'Marigold Ritual',
        3090: 'Pungent Poison',
        3091: 'Blazed Brew',
        3092: 'Mysterious Mixture',
        3093: 'Linguistic Deviation',
        3094: 'Aurelian Seal',
        3095: 'Runic Imprisonment',
        3096: 'Runic Imprisonment',
        3097: 'Prismatic Haze',
        3098: 'Rising Ritual',
        3099: 'Rising Ritual',
        3100: 'Bloody Grip',
        3101: 'Bloody Grip',
        3102: 'Toxic Grip',
        3103: 'Infernal Grip',
        3104: 'Death Grip',

        3105: 'Charged Arcane',
        3106: 'Thunderous Rage',
        3107: 'Convulsive Fiery',
        3108: 'Festivized Formation',
        3109: 'Festivized Formation',
        3110: 'Twirling Spirits',
        3111: 'Squash n\' Twist',
        3112: 'Midnight Sparklers',
        3113: 'Boundless Blizzard',

        3114: 'Solar Scorched',
        3115: 'Deepsea Rave',
        3116: 'Deepsea Rave',
        3117: 'Blooming Beacon',
        3118: 'Beaming Beacon',
        3119: 'Blazing Beacon',
        3120: 'Floppin\' Frenzy',
        3121: 'Pastel Trance',
        3122: 'Pastel Trance',
        3123: 'Wildflower Meadows',
    }
    return taunt_unusuals_list


# defindex 134 || uses float_value
def weapon_unusuals():
    weapon_unusuals_list = {
        701: 'Hot',
        702: 'Isotope',
        703: 'Cool',
        704: 'Energy Orb'
    }
    return weapon_unusuals_list


# defindex 142 default, 261 Blu variation || uses float_value
def paints():
    paints_list = {
        3100495: 'A Color Similar to Slate',
        8208497: 'A Deep Commitment to Purple',
        1315860: 'A Distinctive Lack of Hue',
        12377523: 'A Mann\'s Mint',
        2960676: 'After Eight',
        8289918: 'Aged Moustache Grey',
        15132390: 'An Extraordinary Abundance of Tinge',
        15185211: 'Australium Gold',
        14204632: 'Color No. 216-190-216',
        15308410: 'Dark Salmon Injustice',
        8421376: 'Drably Olive',
        7511618: 'Indubitably Green',
        13595446: 'Mann Co. Orange',
        10843461: 'Muskelmannbraun',
        5322826: 'Noble Hatter\'s Violet',
        12955537: 'Peculiarly Drab Tincture',
        16738740: 'Pink as Hell',
        6901050: 'Radigan Conagher Brown',
        3329330: 'The Bitter Taste of Defeat and Lime',
        15787660: 'The Color of a Gentlemann\'s Business Pants',
        8154199: 'Ye Olde Rustic Colour',
        4345659: 'Zepheniah\'s Greed',
        6637376: 'An Air of Debonair',
        3874595: 'Balaclavas Are Forever',
        12807213: 'Cream Spirit',
        4732984: 'Operator\'s Overalls',
        12073019: 'Team Spirit',
        8400928: 'The Value of Teamwork',
        11049612: 'Waterlogged Lab Coat'
    }
    return paints_list


# defindex 1004 || uses float_value
def paint_spells():
    paint_spells_list = {
        0: 'Die Job',
        1: 'Chromatic Corruption',
        2: 'Putrescent Pigmentation',
        3: 'Spectral Spectrum',
        4: 'Sinister Staining'
    }
    return paint_spells_list


# defindex 1005 || uses float_value
def fp_spells():
    fp_spells_list = {
        1: 'Team Spirit Footprints',
        2: 'Team Spirit Footprints?',
        8421376: 'Gangreen Footprints',
        3100495: 'Corpse Grey Footprints',
        5322826: 'Violent Violet Footprints',
        13595446: 'Rotten Orange Footprints',
        8208497: 'Headless Horseshoes'
    }
    return fp_spells_list
