Use the generalized roads to help with the angle and curve issues.
Give them a uniqueID when they've been dissolved and then cutup.

Automated Text Placement
Significantly Improve Your Success with These Steps

Hans van der Maarel - Red Geographics

hans@redgeographics.com
twitter: @redgeographics

Methods
1.Classification
2.Abbreviate names
3.Filter street name length vs street length
4.Filter street name length vs street crookedness

Classification
•Should already be present in source data
•More important features get higher priority, different font etc.

Examples:

Broadway > B’way
Fifth Avenue > 5th Av.
Martin Luther King Jr. Way > M.L.K Way

Burgemeester Jonkheer Quarles van Uffordlaan > Burg.Jhr.Quarl. v Uffrdln.
Jonkheer Meester G.W. Molleruslaan > Jhr.Mr.GW Moll.ln.
Laan van de Mensenrechten > Ln. v/d Mensenr.

Warning:

Beware of “pre-abbreviated” data

Street name length vs street length
•Calculate whether street is long enough for label
•If not, use condensed font and/or more strict rules
•2 or 3 levels

The Formula

( number of characters ) / ( street length / average letter width )

If < 1 street is long enough for label
If > 1 label is too long for street

Crookedness

•Calculate circularity of convex hull? (lower = better)
•Calculate point/length ratio? (higher = better)
•Calculate angularity? (lower = better)

Crookedness, part 2
•Stricter placement rules
•Different font
•Label on a generalized line

Further work / Improvements:

•Letter-width lookup table
•Seamlessly combine all these methods
•Find a way to measure good text placement
•Extend to point and area features

Solutions:

Create more layers!
•Pre-processing GIS data
•Force software to act human

http://kelsocartography.com/presentations/2011/pcd_2011/hans_van_der_Maarel_Improve_text_placement_results_NACIS2011.pdf

Exclusion list:

Roads like "The Avenue", "The Green" etc should not normally be abbreviated.

Further reading:

* [Contour lines](http://www.cartotalk.com/lofiversion/index.php?t1499.html) - Charlie Frye in CartoTalk

1.	Too many labels are a bad characteristic as the information on the map is covered up.
2.	Contour labels should either be oriented uphill or oriented to the page. If the former method is used, then it is generally considered a kindness to map readers to place more labels on the south facing slopes as these will be right side up for reading.
3.	The labels should be on a straight base line; curves cause the numbers to be oriented in a fashion that can be difficult to read.
4.	Contour labels should be along fairly straight sections of a contour line. This because the label will blank out a portion of the line and the map reader is left to infer the location of the contour line; a straight line is much easier and more likely to be inferred correctly. 
5.	Do not add extra ink, as it will impede viewing of relevant geographic representations. Extra ink includes such as thousands separators, for example use 1850, not 1,850; and unit of measurement abbreviations, which should be provided as part of the map?s legend. 
6.	[Visually] break the contour lines around and behind the label. A 0.5 point (1/144 inch) gap around the contour label is usually sufficient. This is because the contour label is ideally in the same color as the contour line. [This can be accomplished with a text halo]
7.	Index contour labels are most needed near the tops of ridges, bottoms of valleys, and along dramatic changes in slope. 
8.	Avoid placing labels on the portions of contour lines that trend north to south.
9.	Do not ladder or stagger labels to form any sort of obvious pattern. The key word is obvious; as subtle patterns will actually help map readers in finding additional contour labels quickly. Obvious patterns will jump out at map readers, not only distracting them, but also creating false patterns in the landscape. 
10. Among other items from the USGS: good judgement on the part of the cartographer and editor.