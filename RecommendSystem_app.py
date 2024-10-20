import streamlit as st
import pandas as pd
import textwrap


# Load and Cache the data
@st.cache_data(persist=True)
def getdata():
    games_df = pd.read_csv('Games_dataset.csv', index_col=0)
    similarity_df = pd.read_csv('sim_matrix.csv', index_col=0)
    return games_df, similarity_df


games_df, similarity_df = getdata()[0], getdata()[1]

#<span style="color: red;">Text with red color</span>', unsafe_allow_html=True
# Sidebar
st.sidebar.markdown('<strong><span style="color: #8B2500;font-size: 26px;"> Game recommendation</span></strong>',unsafe_allow_html=True)

st.sidebar.markdown('An app by [Long Do](https://doophilong.github.io/Portfolio/)')
st.sidebar.image('pexels-pixabay-275033.jpg', use_column_width=True)
st.sidebar.markdown('<strong><span style="color: #EE4000;font-size: 26px;">:slot_machine: Choose your game !!!</span></strong>',unsafe_allow_html=True)
ph = st.sidebar.empty()
genres = games_df['Genre'].unique().tolist()
selected_genre = st.sidebar.selectbox('Filter by Genre', ['All'] + genres)

genres = games_df['Genre'].unique().tolist()
selected_genres = st.sidebar.multiselect('Filter by Genre(s)', genres)

# Sidebar: Add slider or selectbox for release year range
min_year = int(games_df['Release Year'].min())
max_year = int(games_df['Release Year'].max())
selected_year_range = st.sidebar.slider(
    'Filter by Release Year',
    min_value=min_year, max_value=max_year,
    value=(min_year, max_year)
)

genres = games_df['Genre'].unique().tolist()
selected_genre = st.sidebar.selectbox('Filter by Genre', ['All'] + genres)

# Apply filter if selected
if selected_genre != 'All':
    filtered_games = games_df[games_df['Genre'] == selected_genre]
else:
    filtered_games = games_df

selected_game = ph.selectbox(
    'Select a game from the filtered list: (you can type it as well)',
    [''] + filtered_games['Title'].to_list(),
    key='default',
    format_func=lambda x: 'Select a game' if x == '' else x
)


    # Results
    cols = ['Genre', 'Developer', 'Publisher', 'North America', 'Rest of countries']
    
   # sidebar_bg('pexels-marko-blazevic-2708981.jpg')
    st.markdown("# The recommended games for [{}]({}) are:".format(selected_game, link))
    for idx, row in matches.iterrows():
        st.markdown('### {} - {}'.format(str(idx + 1), row['Title']))
        st.markdown(
            '{} [[...]](https://en.wikipedia.org{})'.format(textwrap.wrap(row['Plots'][0:], 600)[0], row['Link']))
        st.table(pd.DataFrame(row[cols]).T.set_index('Genre'))
        st.markdown('Link to wiki page: [{}](https://en.wikipedia.org{})'.format(row['Title'], row['Link']))
        

else:

        st.markdown('# Game recommendation :video_game:')
        st.text('')
        st.markdown('> _So you have a Nintendo Switch, just finished an amazing game, and would like '
                    'to get recommendations for similar games?_')
        st.text('')
        st.markdown("This app lets you select a game from the dropdown menu and you'll get five "
                    'recommendations that are the closest to your game according to the gameplay and/or plot.')
        st.text('')
        st.warning(':point_left: Select a game from the dropdown menu!')
