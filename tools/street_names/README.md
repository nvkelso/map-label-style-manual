StreetNames
===========

`StreetNames` provides utility functions for handling street names.

Current version is 0.1.5. Install from PyPI with `pip`:

    pip install StreetNames

`short_street_name`
------------------

Shorten a long U.S. street name, e.g. "Main Street" to "Main St".

Examples:

    short_street_name('Wodehouse Avenue') == 'Wodehouse Ave'
    short_street_name('Wodehouse Street North') == 'Wodehouse St N'
    short_street_name('South Wodehouse Boulevard') == 'S Wodehouse Blvd'
    short_street_name('East Highway') == 'East Hwy'
    short_street_name('North Expressway Northeast') == 'North Expwy NE'
    short_street_name('Southwest North Lane') == 'SW North Ln'
    short_street_name('Street Drive') == 'Street Dr'
    short_street_name('Road Street North') == 'Road St N'
