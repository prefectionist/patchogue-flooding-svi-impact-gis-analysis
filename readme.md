# Social Vulnerability Index (SVI) and Flood Risk impact in Patchogue, NY

## Purpose & Scope
The purpose of the project is first for learning the process of GIS analytics and second to potentially provide analytical information from actual government data and geographical resources.

## Initial Exploratory Research
Starting off, I wanted to research what existing analyses were available on the impact of flooding risk to regions with higher Social Vulnerability Indeces (SVI) and take a closer look at possible under-examined hamlets of Brookhaven Township in Suffolk County, NY. I arrived at the question "How are socially and economically vulnerable populations in the Village of Patchogue and neighboring communities exposed to current and projected flood risks, and what are the potential impacts?" to gain a better understanding of the topic.

## Regional Focus
I settled on the Incorporated Village of Patchogue, NY and the three surrounding towns of North Patchgoue, East Patchogue, and Blue Point as the focus of this analysis. With the study area being home to approximately 9.44% of the population of Brookhaven Town and just over 3% of Suffolk County, there would be significant potential social impact from flooding.

## Methodology & Process
After posing the initial question, the next steps were to :
1. Identify and acquire relevent:
  - data sources
  - polygons, shapefiles, and other map data
2. Import and clean the data
3. Analyze the cleaned data
4. Create visualizations and present findings. 

After obtaining polygons for the focus area. The next steps were to obtain:
- Social Vulnerability Index (SVI) table and map Data
- Current and future flood risk data.
- Sea level rise projections
- American Community Survey (ACS) 
- Basemaps from OpenStreetMaps (OSM) using QuickMapServices plugin

### SVI for New York
After obtaining the SVI census tract data for New York, I queried the records only pertaining to Suffolk County, NY (FIPS 36103) to improve query performance. Then I JOINed the TIGER tract  

## Sources used


## Tools
- QGIS
- CSV Files
- GDB (GeoDataBase)
- Shapefiles
- Git

## What was learned


### Data Sources
- 'Hamlet_Polygon' - [Suffolk County Open Data](https://opendata.suffolkcountyny.gov/)
- [SVI Data for New York](https://www.atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html)
- [Suffolk County, NY Trac]

### References
- [SVI Frequently Asked Questions (FAQs)](https://www.atsdr.cdc.gov/place-health/php/svi/svi-frequently-asked-questions-faqs.html)
- [100 & 500 Year Flood Zones in Suffolk County, NY](https://gis.suffolkcountyny.gov/portal/apps/webappviewer/index.html?id=3335037e07594e8aa4462e2978959ba6)
- [SUFFOLK COUNTY COASTAL RESILIENCE MEMORANDUM](https://suffolkcountyny.gov/portals/0/formsdocs/ecodev/Suffolk_County_Coastal_Resilience_Memorandum_Final_July_2024.pdf) 
- [Climate Change Vulnerabilities in the Coastal Mid-Atlantic Region](https://cbe.miis.edu/cgi/viewcontent.cgi?params=/context/publications/article/1009/&path_info=5.15.18.FinalMARCOReport.Climate_Change_Vulnerabilities_in_the_Coastal_Mid_Atlantic_Region.pdf)
    - 'Chapter 3: Coastal Vulnerability Analysis - pg. 44'
- [Map, Long Island's stormy future](https://www.newsday.com/nextli/data/map-long-islands-stormy-future-cyh0ndzv?utm_source=chatgpt.com)
- [Brookhaven, New York](https://en.wikipedia.org/wiki/Brookhaven,_New_York)