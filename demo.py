import numpy as np
import pandas as pd
from pyecharts import Timeline
from pyecharts import Map


gdp = pd.read_csv("score10-18.csv",encoding="GB2312", index_col="Country")
# countrycode = gdp["Country"]
timeline = Timeline(is_auto_play=1,timeline_bottom=0)

col_names = gdp.columns.values.tolist()
max_gdp = 0
min_gdp = np.inf

for col_name in col_names[1:]:
    colmax = max(gdp[col_name])
    colmin = min(gdp[col_name])
    if colmax > max_gdp:
        max_gdp = colmax
    if colmin < min_gdp:
        min_gdp = colmin

def normal(num):
    return np.log(num+1)
    # return num

for col_name in col_names[0:]:
    value = list(gdp[col_name])
    pre_value = []

    for val in value:
        if np.isnan(val):
            pre_value.append(0)
        else:
            pre_value.append(normal(val))

    value = pre_value
    attr = list(gdp.index)
    map = Map("Score of Peacekeeping 2010-2018",width=1200,height=600)

    map.add("score",attr,value, maptype="world", is_visualmap=True,
            visual_text_color="#000",is_map_symbol_show=False,
            visual_range=[normal(min_gdp),normal(max_gdp)],
            visual_range_text=["%.3f"%normal(min_gdp),"%.3f"%normal(max_gdp)],
            visual_top="center"
            )
    timeline.add(map,col_name)
timeline.render()