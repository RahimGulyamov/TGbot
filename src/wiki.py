import requests
from bs4 import BeautifulSoup as BS
from googletrans import Translator

tr = Translator()


class Football:
    """
    This class responsible for parsing table from wiki.
    """

    def __init__(self, url, leng):
        self.URL = url  # setting url of site
        self.leng = leng  # setting language for translating
        self.rank = ''  # for table
        self.error = ''  # for error messages

    def update(self):
        """
        This function responsible for updating parce from wiki
        """
        r = requests.get(self.URL)
        html = BS(r.text, 'lxml')
        table = html.find('table', {'class': 'wikitable', 'style': 'text-align:center;'})
        links1 = table.find_all('a')
        links2 = table.find_all('td')
        club = []
        point = []
        points = []
        lst1 = ''
        num = ''
        MAXLEN = 7
        PTSNUM = 9
        DIGITAL = 10


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

        for pt in links2:
            point.append(pt.get_text())
        for link in links1:
            club.append(link.get('title'))
            for i in removies:
                try:
                    if str(club[-1]) == i:
                        club.remove(club[-1])
                except:
                    pass

        for j in point:
            if len(str(j)) < MAXLEN:
                lst1 = lst1 + str(j)

        lst1 = lst1.replace('\n', ' ')
        lst1 = lst1.replace('[a]', '')
        lst1 = lst1.replace('[b]', ' ')
        lst1 = lst1.replace('[]', '')
        lst1 = "".join(c for c in lst1 if not c.isalpha())
        lst = lst1.split()

        for k in range(1, len(lst) + 1):
            if k % PTSNUM == 0:
                points.append(lst[k - 1])

        j = 1
        for i in range(len(points)):
            if j < DIGITAL:
                num = ' ' + str(j)
            else:
                num = str(j)

            self.rank = self.rank + num + ' | ' + str(points[i]) + ' | ' + \
                        str(club[i]) + '\n'
            j += 1

        self.rank = 'Pos|Pts |     Team     ' + \
                    '\n' + '-------------------------' + '\n' + self.rank

        if self.leng != 'en':
            self.rank = tr.translate(self.rank, dest=self.leng).text

        self.error = '<i>Неправильный ввод. Выбери другую лигу)</i>'
        self.error = tr.translate(self.error, dest=self.leng).text

    def get_rank(self):
        """
        This function only return rank
        :return: self.rank
        """
        return self.rank

    def get_error(self):
        """
        This function only return error
        :return: self.error
        """
        return self.error
