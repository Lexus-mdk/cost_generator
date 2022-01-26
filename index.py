from flask import Flask, request, render_template
from patterns.first_pattern import FirstPattern
from patterns.second_pattern import SecondPattern
from patterns.third_pattern import ThirdPattern
from patterns.fourth_pattern import FourthPattern



# 
class Class():
    # List of patterns name
    classes_list = {
        'first_pattern': FirstPattern,
        'second_pattern': SecondPattern,
        'third_pattern': ThirdPattern,
        'fourth_pattern': FourthPattern
    }

    def __init__(self, pattern_name, data):
        self.pattern_name = pattern_name
        self.data = data
    
    def render_class(self):
        render_pattern = self.classes_list[self.pattern_name](self.data)
        return render_pattern.render_temp()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/printhtml', methods = ['POST', 'GET']) 
def render_html():
    if request.method == 'POST' and request.get_data():
        render = Class(request.form['pattern'], request.form['data'])
        return render.render_class()


app.run()