# import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import re


df = pd.read_csv('LA_rest_yelp_no_dupes.csv')
print(df.head())


# slightly awkward way of assigning colors
# df.loc[df['not on rubmaps'] == True, 'rub_color'] = 'steelblue'
# df.loc[df['not on rubmaps'] == False, 'rub_color'] = 'firebrick'

# df['rub_color'] = df.apply(lambda row: 'steelblue' if row['rating'] >= 4.5 else 'firebrick', axis=1 )
# print(df['rub_color'])

def colors(row):
    if row['rating'] >= 4.5: 
        return 'green'
    elif row['rating'] >= 4.0:
        return 'yellow'
    else:
        return 'firebrick'
    
    
    
df['plot_color'] = df.apply(colors, axis=1)


# df['plot_colors'] = df.apply(lambda row: 'green' if row['rating'] >= 4.5 else ('yellow' if row['rating']>=4 else 'firebrick'), axis=1 )

# print(df.head())

# exit()

df['hover_text'] = df['name'] + '<br>' + df['address'] + '<br>' + df['category_title'] + '<br>' + df['review_count'].astype(str)
# df['hover_text'] = df.apply(lambda row: row['hover_text'] if row['not on rubmaps'] == True else row['hover_text'] + '<br>' + row['search_field'], axis=1 )
fig = go.Figure(data=go.Scattermapbox(
                hovertext=df['hover_text'],
                hoverinfo='text',
                lon = df['lon'], lat = df['lat'], 
                marker=go.scattermapbox.Marker(color=df['plot_color'], size=df['review_count']/30, sizemode='area', sizemin=2,),
                
                

# hover_name=df['name_yelp'],  
# #hover_data=['address_yelp', 'rating', 'phone', 'search_field'],
                       
                    #    color=df['not on rubmaps'], size=df['review_count'], # size of markers, "pop" is one of the columns of gapminder
                     ))

# fig.update_geos(
#     center=dict(lon=32.7, lat=-117),

#     # projection_rotation=dict(lon=30, lat=30, roll=30),
#     # lataxis_range=[-50,20], lonaxis_range=[0, 200]
# )
# fig.update_geos(fitbounds="locations")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(
    hovermode='closest',
    mapbox=dict(

        bearing=0,
        center=go.layout.mapbox.Center(
           lon=34.0522, 
           lat=-118.2437
        ),
        pitch=4,
        zoom=9,
    )
)
# fig.update_layout(autosize=True, hovermode='closest',mapbox={
#     'zoom' : 3,
#     'center': {
#         'lat': -117,
#         'lon' : 32.7,
#     }


# })
fig.update_layout(
        title = 'Chow Down in Los Angeles? <br>(Check your ratings first!)',
        # center=dict(lon=34.0522, lat=-118.2437),
        # zoom = 10,
        # geo_scope='usa',
    
    )

fig.show()

fig.write_html('LA_chow_down.html')