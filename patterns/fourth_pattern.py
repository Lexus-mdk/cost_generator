from flask import render_template, url_for
import re

class FourthPattern():
    template = 'fourth_temp.html'

    def __init__(self, data):

        data = [re.split(':', itm) for itm in re.split('\r\n', data)]
        if data[-1][0] == '':
            data.remove([''])

        self.data = data
        self.cost_count = len(data)

    def render_temp(self):

        return render_template(self.template, data = self.data, cost_count = self.cost_count)