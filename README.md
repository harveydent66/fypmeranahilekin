# Game recommendation system
![image](https://github.com/DooPhiLong/Game-recommendation-system/assets/120476961/9ea48faa-b205-4172-a815-c5d3e540c866)

## 💼 Case study 

### Requirement
Collect data about games from websites, then based on information about the gameplay or plot of the game, perform text analysis using machine learning methods related to natural language , to identify games with similar gameplay or storylines. Finally, build a recommendation application. When the user chooses a game, the system will automatically suggest 5 other games with the most similar gameplay or plot.
### application
- Products recommendation in the e-commerce or retail sector.
- Films recommendation in the online cinema industry.
- Information recommendation in the searching system like Google, Facebook...
- etc..
- 
## Crawl game data from website
I have crawled data from the table object [List of Nintendo Switch games (Q–Z)](https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(Q%E2%80%93Z)) from the Wikipedia website using python with 2 libraries Request and BeautifulSoup.
### Data crawled (787 games with 9 features)
20 samples
![image](https://github.com/DooPhiLong/Game-recommendation-system/assets/120476961/97896a55-75a5-435b-87fe-24e9efea8b92)

- **Title :** Name of game.
- **Link :** Link to detail information about the game.
- **Gener :** Type of game.
- **Developer :** Game Developer.
- **Publisher :** Game Publisher.
- **Released in Japan :** Game release date in Japan.
- **North America :** Game release date in North America.
- **Rest of countries :** Game release date in Rest of countries.
- **Plots :** Plot of the game.
### Source code
[Click here](https://github.com/DooPhiLong/Game-recommendation-system/blob/main/drawlData_soup.py)

## Game plots similarity analysis
I have performed text analysis in "Plots" features using machine learning methods in the field of natural language processing such as data cleaning (Tokenlization, Stopword elemination, Word stemming), semantic vectorization (TF-IDF), and building similarity coefficient matrices among game plots.
### Similarity coefficient matrices among game plots
Samples of 10 games 
![image](https://github.com/DooPhiLong/Game-recommendation-system/assets/120476961/bd9674a9-ad18-4a42-b396-80bca2d212e6)
- A matrix with Name of game are also the Column title and Row index
- The numbers represent the similarity of each pair of games (Limited from 0 to 1), The smaller the number, the more similar the two games are
### Source code
[Click here](https://github.com/DooPhiLong/Game-recommendation-system/blob/main/Model_similarity.py)

## Build an game recommendation system app
I used python and the streamlit library to create a game recommendation application, to illustrate the similarity analysis between games in the section above. When the user chooses a game, the system will suggest 5 other games with similar gameplay or plots.
### App
[Click here](https://game-recommendation-system.streamlit.app/)
### Source code
[Click here](https://github.com/DooPhiLong/Game-recommendation-system/blob/main/RecommendSystem_app.py)

  




