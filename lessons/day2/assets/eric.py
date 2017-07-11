from bs4 import BeautifulSoup
from requests import get
from time import sleep
from selenium import webdriver

"""
d = webdriver.PhantomJS()

login_url = 'https://id.wsj.com/access/pages/wsj/us/signin.html?url=http%3A%2F%2Fwww.wsj.com&mg=id-wsj'

res = d.get(login_url)

u_input = d.find_element_by_xpath('//*[@id="username"]')
u_input.clear()
u_input.send_keys(username)

p_input = d.find_element_by_xpath('//*[@id="password"]')
p_input.clear()
p_input.send_keys(password)

res = d.find_element_by_xpath('//*[@id="submitButton"]').click()
"""

class Collect():

    sleep_time = 1.0
    d = webdriver.Chrome()

    """
    sleep_time
        request timeout
    """

    def _generate_links(self):

        """
        returns a generator that returns all links in order

        -> generator <string>

        """
        base_str = 'http://www.oddsportal.com/basketball/usa/nba-las-vegas-summer-league-{year}/results/'

        yield from [base_str.format(year = i) for i in range(2013,2017)]

        yield 'http://www.oddsportal.com/basketball/usa/nba-las-vegas-summer-league/results/'

    def _parse_single(self, url):

        """
        """

        html = get(url).text
        bs_obj = BeautifulSoup(html,'lxml')

        sleep(Collect.sleep_time)

        table = bs_obj.select("#tournamentTable")
        print (html)



        return 'fuck'

    def main(self):
        for url in  self._generate_links():

            foo = self._parse_single(url)
            break

        pass



if __name__ == "__main__":
    x = Collect()
    x.main()
