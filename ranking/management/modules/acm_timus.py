#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
import urllib.parse

from common import REQ
from common import BaseModule, parsed_table
from first import first


class Statistic(BaseModule):

    def __init__(self, **kwargs):
        super(Statistic, self).__init__(**kwargs)
        if not self.standings_url:
            self.standings_url = self.url.replace('contest.aspx', 'monitor.aspx')

    def get_standings(self, users=None):
        result = {}

        page = REQ.get(self.standings_url)
        table = parsed_table.ParsedTable(html=page, xpath="//table[@class='monitor']//tr")
        problems_info = collections.OrderedDict()
        for r in table:
            row = {}
            problems = row.setdefault('problems', {})
            for k, v in list(r.items()):
                title = first(v.header.node.xpath('a[@title]/@title'))
                if k in ['Участник', 'Participant']:
                    row['member'] = v.value
                elif k in ['Место', 'Rank']:
                    row['place'] = v.value
                elif k in ['Время', 'Time']:
                    row['penalty'] = int(v.value)
                elif k in ['Решено', 'Solved']:
                    row['solving'] = int(v.value)
                elif len(k) == 1 and title is not None:
                    problems_info[k] = {'short': k, 'name': title}
                    url = first(v.header.node.xpath('a[@href]/@href'))
                    if url is not None:
                        problems_info[k]['url'] = urllib.parse.urljoin(self.standings_url, url)
                    if v.value:
                        p = problems.setdefault(k, {})
                        values = v.value.replace('–', '-').split(' ')
                        p['result'] = values[0]
                        if len(values) > 1:
                            p['time'] = values[1]
            result[row['member']] = row
        standings = {
            'result': result,
            'url': self.standings_url,
            'problems': list(problems_info.values()),
        }
        return standings


if __name__ == "__main__":
    statistic = Statistic(
        name='Later is better than never',
        url='http://acm.timus.ru/contest.aspx?id=423',
        standings_url=None,
        key='http://acm.timus.ru/contest.aspx?id=423',
    )
    from pprint import pprint
    pprint(statistic.get_standings())