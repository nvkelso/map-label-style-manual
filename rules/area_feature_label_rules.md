For multipart features:

**What, where:**

* If a single label per feature part, then that label should be near the centroid for the largest part.
* If auto: also label extra parts that are above a certain size per the scale (zoom) of the map. (Can the label fit.)
* If every part: each part's label should be near it's centroid.

**Big features:**

(measured in terms of page units)

* Add letter space to "spread" the type to match the size of the feature.

**Types of Features with Indeterminate Boundaries**
Named Marine Water Bodies - Hydrography - Must Nest, No OverlapsNamed Physiographic Features - Physiography - May Nest or Have Partial OverlapsNamed Islands and Island Chains and Groups - Physiography and Hydrography - Must Nest, No OverlapsNeighborhoods and Districts, Vernacular Regions - Cultural and Transportation - May Nest or Have Partial OverlapsLand Cover, Geology, Soils and Other Overlays - Overlays - No Overlaps

**Feature Geometry Types**

A set of seven feature types that are used to specify label classes and variations in label placement properties were developed. 
1. Long 
2. Long and Skinny 
3. Oblong 
4. Round5. Snaky or Pronged 
6. Splotch 
7. Snaky or Pronged and Skinny

**Calculating feature geometry types:**

In order to create the information that is stored in these fields, a Python script was written and uses an ArcGIS 9.2 geoprocessing command called ÒGEOM- ETRY:HULLRECTANGLEÓ. This command returns a string containing the eight coordinates of the MBR. With these coordinates the RatioL2W and MBRArea field values can be set. The values for the LabelType field are set based on the following pseudo-code logic:
If RatioL2W < 4 and MBRArea > 60% Label Type = "Roundish"
Elseif RatioL2W < 8 and MBRArea > 25% LabelType = "Oblong"
Elseif RatioL2W >= 8 and MBRArea > 10% LabelType = "Long"
Elseif RatioL2W >= 8 and MBRArea <= 10% LabelType = "Long and Skinny"
Else 

  If RatioL2W < 4 and MBRArea >= 20% Label type = "Splotch" 

  Elseif RatioL2W < 8 and MBRArea > 12% Label Type = "Snaky or Pronged" 

  Elseif RatioL2W < 8 and MBRArea <=12% Label Type = "Snaky or Pronged and Skinny"


This logic is essentially first determining whether the shape is round-ish, and if not, if it is oblong or long, and if not, if it is a splotch, or snaky or pronged. The specific thresholds may need to be tuned to spe- cific cartographic requirements.

**Label placement per feature type:**

Round-ish
i.	Placement: Curved
ii.	May overrun by 36 pts 

iii.	Allow asymmetric overrun = true

iv.	Char. Space = up to 200% 

v.	Reduce font from 14 pts. to 10 pts. by 1 pt. increments 

Oblong 

i. Placement: Curved 

ii. May overrun by 12 pts 

iii. Char. Space = up to 300%

Long
i. Placement: Curved 

ii. Try Horizontal First = true 

iii. May Stack = true 

iv. Character Spacing = up to 200%

Long and Skinny

i. Placement: Boundary 

ii. May Place Outside = true 

iii. Offset = 4 pts 

iv. Char. Space = up to 240% 

v. Background Label = true

Splotch

i. Placement: Curved 

ii. Char. Space = up to 300% 

iii.Reduce Font from 14 pts. to 10 pts. by 1 pt. increments
Snaky or Pronged

i. Placement: Curved 

ii. May overrun by 12 pts 

iii. Char. Space = up to 400%

Snaky or Pronged and Skinny

i.	Placement: Boundary

ii.	May Place Outside = true 

iii.	Offset = 4 pts

iv.	Char. Space = up to 240% 

v.	Background Label = true


**Sources and further reading:**

* [A Multi-scale, Multipurpose GIS Data Model to Add Named Features of the Natural Landscape to Maps](http://nacis.org/documents_upload/cp55fall2006.pdf) - Cartographic Perspectives Number 55, Fall 2006. Aileen Buckley abuckley@esri.comCharlie Frye cfrye@esri.com Cartographic Research and Special Projects Group Environmental Systems Research Institute, Inc. Redlands, CA

* [Shape Types for Labeling Natural Polygon Features with Maplex](http://nacis.org/documents_upload/cp54spring2006.pdf) - Cartographic Perspectives Number 54, Spring 2006. Charlie Frye Environmental Systems Research Institute, Inc. cfrye@esri.com