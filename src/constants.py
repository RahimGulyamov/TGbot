from src.keyboard import EPL, LaLiga, SerieA, BunLiga, Ligue1

url_la_liga = 'https://en.wikipedia.org/wiki/2022%E2%80%9323_La_Liga'
url_ligue_1 = 'https://en.wikipedia.org/wiki/2022%E2%80%9323_Ligue_1'
url_bundesliga = 'https://en.wikipedia.org/wiki/2022%E2%80%9323_Bundesliga'
url_seria_a = 'https://en.wikipedia.org/wiki/2022%E2%80%9323_Serie_A'
url_premier_league = 'https://en.wikipedia.org/wiki/2022%E2%80%9323_Premier_League'

table_la_liga = 'La Liga table 🇪🇸:'
table_premier_league = 'English Premier League table 🏴󠁧󠁢󠁥󠁮󠁧󠁿:'
table_ligue_1 = 'Ligue 1 table 🇫🇷:'
table_bundesliga = 'BundesLiga table 🇩🇪:'
table_seria_a = 'Serie A table 🇮🇹:'


class League:
    def __init__(self, url, table_name):
        self.url = url
        self.table_name = table_name


main_leagues = {EPL: League(url_premier_league, table_premier_league),
                LaLiga: League(url_la_liga, table_la_liga),
                SerieA: League(url_seria_a, table_seria_a),
                BunLiga: League(url_bundesliga, table_bundesliga),
                Ligue1: League(url_ligue_1, table_ligue_1)}

removies = [
    '2023–24 UEFA Champions League', '2023–24 UEFA Europa League', 'None',
    '2023–24 UEFA Europa Conference League', '2023–24 EFL Championship',
    '2023–24 Segunda División', 'Template talk:2022–23 La Liga table',
    'Template:2022–23 La Liga table', 'Template:2022–23 Serie A table',
    'Template talk:2022–23 Serie A table', '2023–24 Serie B',
    'Template:2022–23 Bundesliga table', 'Template talk:2023–23 ',
    'Bundesliga table', '2022–23 Bundesliga', '2023–24 2. Bundesliga',
    'Template:2022–23 Ligue 1 table', 'Template talk:2022–23 Ligue 1 table',
    '2022–23 Ligue 1', '2023–24 Ligue 2', 'Template talk:2022–23 Bundesliga table',
    '2023–24 2. Bundesliga (page does not exist)'
]

str_max_len = 7
pts_num = 9
digital_ten = 10
