from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""

### Intro

The melting of the permafrost is one of the biggest yet least-talked-about consequences of global warming. 
The permafrost is a layer of frozen soil, located in areas near the arctic, that stays frozen for several 
years. There are many concerns with permafrost melting, but one of the biggest issues is related to its 
effect on the climate. There is an estimated three times more organic (and digestible) material stored in 
the permafrost than there is in all the forests left on the planet. As permafrost melts, more materials in 
the permafrost are decomposed. This leads to more carbon dioxide being released into the atmosphere, 
warming up the globe. 

Above the permafrost is a layer of soil known as **the active layer** that freezes and thaws annually. As the 
global average temperature increases, the permafrost melts, and the active layer thickness (also known as 
the thaw depth) increases. The increase in temperature then speeds up the thawing process, thus creating a 
positive feedback-loop, exacerbating the climate problem. Another major problem is that **unearthing 
long-frozen microbes and bacteria may introduce diseases that may cause outbreaks**. It may be possible that 
outbreaks, epidemics and pandemics could become more and more frequent in the coming years."""),

html.Div([
    
    html.Img(src = 'https://assets.nrdc.org/sites/default/files/styles/full_content--retina/public/media-uploads/guide_permafrost_579215990_rm_ds_2400.jpg?itok=mY63upPu'),
    html.H1("*Permafrost melting in the arctic region of Svalbard, Norway, Credits: Jeff Vangua/Getty*"),
    style = {'position' : 'center', 'width' : '50%', 'height' : '50%'})], style = {'textAlign':'center'}),

dcc.Markdown("""
**This project’s goal is to project future active layer thickness** in Samoylov, Russia, one of the many sites 
where permafrost has been closely monitored over the years, to bring more awareness to the issue of thawing 
permafrost. It could also serve as a platform that policy-makers, researchers, and students could use to study
how the melting of the permafrost can affect their environment, so they can make the necessary environmental 
regulations to curb climate change.


The data that we used to fit this model is data from 2002-2018 from the **Samoylov station from the Circumpolar 
Active Layer Monitoring (CALM) program database.** 

Users can use this interactive dashboard by inputting dates and see the change in active layer thickness over 
time.


### Sources and Citations:

**Samoylov Dataset:**
Boike, Julia, Nitzbon, Jan, Anders, Katharina, Grigoriev, Mikhail N, Bolshiyanov, Dimitry Yu, Langer, Moritz, … Kutzbach, Lars. (2019).
Measurements in soil and air at Samoylov Station (2002-2018) version 201908 (Version 201908) [Data set]. http://doi.org/10.1594/PANGAEA.905236

**References:**
- https://www.vox.com/2017/9/6/16062174/permafrost-melting
- https://eos.org/editor-highlights/permafrost-thaws-rapidly-as-arctic-river-flooding-increases
- https://machinelearningmastery.com/sarima-for-time-series-forecasting-in-python/

**UI Reference:** https://towardsdatascience.com/how-to-create-an-interactive-dash-web-application-11ea210aa6d9



""")]

