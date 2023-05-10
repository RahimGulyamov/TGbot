import requests
from bs4 import BeautifulSoup as BS
from googletrans import Translator
from src.constants import removies, str_max_len, pts_num, digital_ten

tr = Translator()


def proper_string(string):
    string = string.replace('\n', ' ')
    string = string.replace('[a]', '')
    string = string.replace('[b]', ' ')
    string = string.replace('[]', '')
    string = "".join(c for c in string if not c.isalpha())
    string = string.split()
    return string


class Football:
    """
    This class responsible for parsing table from wiki.
    """

    def __init__(self, url, lang):
        self.URL = url  # setting url of site
        self.lang = lang  # setting language for translating
        self.rank = ''  # for table
        self.error = ''  # for error messages

    def update(self):
        """
        This function responsible for updating parce from wiki
        """
        req = requests.get(self.URL)
        html = BS(req.text, 'lxml')
        table = html.find('table', {'class': 'wikitable', 'style': 'text-align:center;'})
        links1 = table.find_all('a')
        links2 = table.find_all('td')
        club, point, points = [], [], []
        lst1 = ''

        for pt in links2:
            point.append(pt.get_text())
        for link in links1:
            club.append(link.get('title'))
            if str(club[-1]) in removies:
                club.remove(club[-1])

        for j in point:
            if len(str(j)) < str_max_len:
                lst1 = lst1 + str(j)

        lst = proper_string(lst1)

        for k in range(1, len(lst) + 1):
            if k % pts_num == 0:
                points.append(lst[k - 1])

        for i in range(len(points)):
            num = (' ' if i + 1 < digital_ten else '') + str(i + 1)
            self.rank = self.rank + num + ' | ' + str(points[i]) + ' | ' + str(club[i]) + '\n'

        self.rank = 'Pos|Pts |     Team     ' + '\n' + '-------------------------' + '\n' + self.rank
        self.rank = tr.translate(self.rank, dest=self.lang).text

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
        self.error = '<i>Неправильный ввод. Выбери другую лигу)</i>'
        self.error = tr.translate(self.error, dest=self.lang).text
        return self.error
