# -*- coding: utf-8 -*-
import time


class Outputer(object):
    def __init__(self):
        self._collected_data = []

    def add_data(self, new_data):
        if new_data is None:
            return
        print('add new data to output:%s' % new_data)
        self._collected_data.append(new_data)

    def output(self):
        _cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fout = open('resoult.html', 'w')
        fout.write('<html>\n')
        fout.write('    <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />\n ')
        fout.write('    <body>\n')
        fout.write('    <p>Time:%s, Count:%d</p>\n' % (_cur_time, len(self._collected_data)))
        fout.write('        <table border="8">\n')
        self._collected_data.sort(key=lambda x: x['community'], reverse=True)
        fout.write('            <tr>\n')
        fout.write('                <th>楼盘</th>\n')
        fout.write('                <th>均价</th>\n')
        fout.write('                <th>价格</th>\n')
        fout.write('                <th>面积</th>\n')
        fout.write('                <th>地址</th>\n')
        fout.write('                <th>链接</th>\n')
        fout.write('            </tr>\n')
        for data in self._collected_data:
            fout.write('            <tr>\n')
            try:
                fout.write('                <td>%s</td>\n' % data['community'])
                fout.write('                <td>%s</td>\n' % data['average_price'])
                fout.write('                <td>%s</td>\n' % data['total_price'])
                fout.write('                <td>%s</td>\n' % data['area'])
                fout.write('                <td>%s</td>\n' % data['address'])
                fout.write('                <td><a href=%s>%s</a></td>\n' % (data['url'], data['url']))

            except:
                print('output failed %s', data)
            fout.write('            </tr>\n')
        fout.write('        </table>\n')
        fout.write('    </body>\n')
        fout.write('</html>\n')
