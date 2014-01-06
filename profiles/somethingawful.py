from datetime import datetime

import requests
import lxml.html


class SomethingAwful(object):
    def __init__(self, user, password):
        self.session = requests.session()
        self.login(user, password)

    def login(self, user, password):
        url = 'https://forums.somethingawful.com/account.php'
        data = {
            'action': 'login',
            'username': user,
            'password': password,
            'next': '/'
        }

        self.session.post(url, data=data)

    def get_profile(self, url):
        r = self.session.get(url).text
        html = lxml.html.fromstring(r)

        username = html.xpath('//td[@class="info"]/h3/text()')[0].split(" ")[1:]
        if len(username) > 1:
            username = " ".join(username)
        else:
            username = username[0]

        icq = html.xpath('//td[@class="info"]/dl[@class="contacts"]/dd[2]/span/text()')[0]
        aim = html.xpath('//td[@class="info"]/dl[@class="contacts"]/dd[3]/span/text()')[0]
        yahoo = html.xpath('//td[@class="info"]/dl[@class="contacts"]/dd[4]/span/text()')[0]
        regdate = html.xpath('//dl[@class="additional"]/dd[1]/text()')[0]
        postcount = int(html.xpath('//dl[@class="additional"]/dd[2]/text()')[0])
        postrate = html.xpath('//dl[@class="additional"]/dd[3]/text()')[0]
        lastpost = html.xpath('//dl[@class="additional"]/dd[4]/text()')[0].rstrip() #remove newlines, tabs
        
        additional = lxml.html.tostring(html.xpath('//dl[@class="additional"]')[0])
        if 'Location' in additional:
            location = additional.partition('Location</dt><dd>')[2].partition('</dd>')[0]
            occupation = additional.partition('Occupation</dt><dd>')[2].partition('</dd>')[0]
        else:
            location = 'Unknown'
            occupation = additional.partition('Occupation</dt><dd>')[2].partition('</dd>')[0]
            
        userid = html.xpath("//form[1]/input[@name='userid']/@value")[0]

        profile = {
            'username': username,
            'userid': userid,
            'icq': icq,
            'aim': aim,
            'yahoo': yahoo,
            'regdate': regdate,
            'postcount': postcount,
            'postrate': postrate,
            'lastpost': lastpost,
            'occupation': occupation,
            'location': location
        }

        d = datetime.strptime(profile['regdate'], '%b %d, %Y')
        profile['regdate'] = d

        return profile
