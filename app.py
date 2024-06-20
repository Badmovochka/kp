""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template
from requests import request


app = Flask(__name__)

@app.route("/")
def welcome():
    """Эта функция необходима для открытия главной страницы"""
    return render_template('index.html')

# @app.route("/error")
# def error():
#     """Эта функция запуская и отвечает за процесс возврата результата test_error.html."""
#     return render_template('index.html')

@app.route('/ui_test')
def trigger_ui_tests():
    cmd = ['./scriptsh/run_ui_tests.sh']
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html')

@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/run_allure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)

if __name__ == "__main__":
    app.run(debug=True)
