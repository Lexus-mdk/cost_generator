from flask import render_template, url_for
import re

class SecondPattern():
    template = 'second_temp.html'

    def __init__(self, data):
        self.page_count = int(data)


    def render_temp(self):

        return render_template(self.template, page_count = self.page_count)