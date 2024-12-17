""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """
import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    return render_template('welcome.html')

@app.route('/ui_test_main_header')
def ui_test_main_header():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/ui_test_main_header.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/ui_test_main_footer')
def ui_test_main_footer():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/ui_test_main_footer.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/ui_test_main_flights_search')
def ui_test_main_flights_search():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/ui_test_main_flights_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/ui_test_main_hotels_search')
def ui_test_main_hotels_search():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/ui_test_main_hotels_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/ui_test_main_popular_flights')
def ui_test_main_popular_flights():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/ui_test_main_popular_flights.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


app.route('/api_test_main_personal_area')
def api_test_main_personal_area():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/api_test_main_personal_area.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/api_test_main_my_travel')
def api_test_main_my_travel():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/api_test_main_my_travel.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/api_test_main_contact_support')
def api_test_main_contact_support():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/api_test_main_contact_support.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/api_test_main_flights_search')
def api_test_main_flights_search():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/api_test_main_flights_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/api_test_main_hotels_search')
def api_test_main_hotels_search():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/api_test_main_hotels_search.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)

app.route('/allure_test')
def allure_test_ui():
    """ Эта функция запуская и отвечает за процесс возврата результата welcome.html. """
    cmd = ["./scriptsh/allure_test.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)




@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """
    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


@app.route("/run_ui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """
    cmd = ["./scriptsh/run_aut_lk.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
