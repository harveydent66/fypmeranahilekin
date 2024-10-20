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
# Sidebar
st.sidebar.markdown('<strong><span style="color: #8B2500;font-size: 26px;"> Game recommendation</span></strong>', unsafe_allow_html=True)
st.sidebar.markdown('An app by [Long Do](https://doophilong.github.io/Portfolio/)')
st.sidebar.image('pexels-pixabay-275033.jpg', use_column_width=True)
st.sidebar.markdown('<strong><span style="color: #EE4000;font-size: 26px;">:slot_machine: Choose your game !!!</span></strong>', unsafe_allow_html=True)

# Filters in the Sidebar
# 1. Filter by Genre
genres = games_df['Genre'].unique().tolist()
selected_genres = st.sidebar.multiselect('Filter by Genre(s)', genres)

# 2. Filter by Developer
developers = games_df['Developer'].unique().tolist()
selected_developers = st.sidebar.multiselect('Filter by Developer(s)', developers)

# 3. Filter by Publisher
publishers = games_df['Publisher'].unique().tolist()
selected_publishers = st.sidebar.multiselect('Filter by Publisher(s)', publishers)

# 4. Filter by Release Year Range
min_year = int(games_df['Release Year'].min())
max_year = int(games_df['Release Year'].max())
selected_year_range = st.sidebar.slider('Filter by Release Year', min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Apply filters
filtered_games = games_df.copy()

# Apply genre filter if any genres are selected
if selected_genres:
    filtered_games = filtered_games[filtered_games['Genre'].isin(selected_genres)]

# Apply developer filter if any developers are selected
if selected_developers:
    filtered_games = filtered_games[filtered_games['Developer'].isin(selected_developers)]

# Apply publisher filter if any publishers are selected
if selected_publishers:
    filtered_games = filtered_games[filtered_games['Publisher'].isin(selected_publishers)]

# Apply release year filter
filtered_games = filtered_games[
    (filtered_games['Release Year'] >= selected_year_range[0]) &
    (filtered_games['Release Year'] <= selected_year_range[1])
]

# Game Selection Dropdown
ph = st.sidebar.empty()
selected_game = ph.selectbox(
    'Select one among the filtered games (you can type it as well):',
    [''] + filtered_games['Title'].to_list(), 
    key='default',
    format_func=lambda x: 'Select a game' if x == '' else x
)
# Recommendations
if selected_game:

    link = 'https://en.wikipedia.org' + games_df[games_df.Title == selected_game].Link.values[0]

    # DF query
    matches = similarity_df[selected_game].sort_values()[1:6]
    matches = matches.index.tolist()
    matches = games_df.set_index('Title').loc[matches]
    matches.reset_index(inplace=True)

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
