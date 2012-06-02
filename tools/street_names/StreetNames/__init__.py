""" Utility functions for handling street names.

>>> short_street_name('Wodehouse Avenue')
'Wodehouse Ave.'

>>> short_street_name('Wodehouse Rd')
'Wodehouse Rd.'

>>> short_street_name('Wodehouse Street North')
'Wodehouse St. N'

>>> short_street_name('South Wodehouse Boulevard')
'S Wodehouse Blvd.'

>>> short_street_name('East Highway')
'East Hwy.'

>>> short_street_name('North Expressway Northeast')
'North Expwy. NE'

>>> short_street_name('SW North Lane')
'SW North Ln.'

>>> short_street_name('Street Dr')
'Street Dr.'

>>> short_street_name('Road Street North')
'Road St. N'

>>> short_street_name('Parkway')
'Parkway'
"""
__version__ = '0.1.4'

_directions = {
    'north': 'N', 'northeast': 'NE',
    'east': 'E',  'southeast': 'SE',
    'south': 'S', 'southwest': 'SW',
    'west': 'W',  'northwest': 'NW',
    'n': 'N', 'ne': 'NE',
    'e': 'E', 'se': 'SE',
    'e': 'S', 'sw': 'SW',
    'w': 'W', 'ne': 'NW'
}

_types = {
    'ave': 'Ave.',
    'avenue': 'Ave.',
    'blvd': 'Blvd.',
    'boulevard': 'Blvd.',
    'court': 'Ct.',
    'ct': 'Ct.',
    'dr': 'Dr.',
    'drive': 'Dr.',
    'expressway': 'Expwy.',
    'expwy': 'Expwy.',
    'freeway': 'Fwy.',
    'fwy': 'Fwy.',
    'highway': 'Hwy.',
    'hwy': 'Hwy.',
    'lane': 'Ln.',
    'ln': 'Ln.',
    'parkway': 'Pkwy.',
    'pkwy': 'Pkwy.',
    'pl': 'Pl.',
    'place': 'Pl.',
    'rd': 'Rd.',
    'road': 'Rd.',
    'st': 'St.',
    'street': 'St.',
    'ter': 'Ter.',
    'terrace': 'Ter.',
    'tr': 'Tr.',
    'trail': 'Tr.',
    'way': 'Wy.',
    'wy': 'Wy.',
}

def short_street_name(long_name):
    """ Shorten a long street name, e.g. "Main Street" to "Main St".
    """
    parts = long_name.strip().split()
    keys = long_name.strip().lower().split()
    
    if len(parts) >= 3 and keys[0] in _directions and keys[-1] in _types:
        #
        # like "North Herp Derp Road"
        #
        parts[0] = _directions[keys[0]]
        parts[-1] = _types[keys[-1]]
    
    elif len(parts) >= 3 and keys[-2] in _types and keys[-1] in _directions:
        #
        # like "Herp Derp Road North"
        #
        parts[-2] = _types[keys[-2]]
        parts[-1] = _directions[keys[-1]]
    
    elif len(parts) >= 2 and keys[-1] in _types:
        #
        # like "Herp Derp Road"
        #
        parts[-1] = _types[keys[-1]]
    
    return ' '.join(parts)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
