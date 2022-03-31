from flask import Flask, render_template, request
from plot_functions import plot_map, plot_demo, plot_results_overall, \
    plot_results_hospitals, plot_aggregated_data, plot_spread, count_sim_results, plot_measures_yml
from submit_simulation import simulate
import threading
import random
import time
import os.path as osp
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', content='Test')

class district_class:
    def __init__(self, defaultCountry, defaultDistrict):
        self.country = defaultCountry
        self.district = defaultDistrict

    def create_page(self):
        msg1 = 'Enter the parameters to start simulation'
        spread_time = random.randint(0, 99)
        msg2 = 'Showing spread of infections on day ' + str(spread_time)

        if request.method == 'POST':

            if request.form['but'] == 'but1':
                for i in range(int(request.form.get('reps'))):
                    cmd = 'bash facs_script.sh ' + self.district + ' ' + request.form.get('sim_length') + ' ' + request.form.get('starting_infections') + ' ' + request.form.get('reps')
                    th = threading.Thread(target=simulate, args=(cmd,))
                    th.start()
                msg1 = 'Simulation submitted!'
            if request.form['but'] == 'but2':
                spread_time = int(request.form.get('spread_time'))
                msg2 = 'Showing spread of infections on day ' + request.form.get('spread_time')

        region_map, demographics, measures, latest_cases, latest_hospitalisations, cc = self.plot()

        msg3 = f'Showing plots for {cc} runs'

        output_path = osp.join("Data",self.country,self.district,"output/")
        all_cases = plot_aggregated_data(borough=self.district, observable=['susceptible', 'exposed', 'infectious', 'recovered', 'dead'], scenario=['extend'], res_dir=output_path)
        all_hospitalisations = plot_aggregated_data(borough=self.district, observable=['num hospitalisations today', 'hospital bed occupancy', 'cum num hospitalisations today'], scenario=['extend'], res_dir=output_path)

        spread_path = osp.join("Data",self.country,self.district,"output","covid_out_infections_0.csv")
        spread = plot_spread(fname=spread_path, zoom=8.0, spread_time=spread_time)

        return render_template('country.html',
        message1=msg1,
        message2=msg2,
        message3=msg3,
        country=self.country.title(),
        region=self.district.title(),
        maps=region_map,
        demo=demographics,
        measures=measures,
        latest_cases=latest_cases,
        latest_hospitalisations=latest_hospitalisations,
        all_cases=all_cases,
        all_hospitalisations=all_hospitalisations,
        spread=spread)

    def plot(self):
        region_path = osp.join("Data", self.country, self.district, "input", self.district + "_buildings.csv")
        demographics_path = osp.join("Data", self.country, self.district, "input", "age-distr.csv")
        measures_path = osp.join("Data", self.country, self.district, "input", "measures_" + self.district + ".yml")
        latest_cases_path = osp.join("Data", self.country,self. district, "output",self.district + "-latest.csv")
        latest_hospitalisations_path = osp.join("Data", self.country, self.district, "output", self.district + "-latest.csv")
        cc_path = osp.join("Data", self.country, self.district, "output")

        region_map = plot_map(fname=region_path, zoom=8.0)
        demographics = plot_demo(fname=demographics_path, region=self.district.capitalize())
        measures = plot_measures_yml(fname=measures_path)

        latest_cases = plot_results_overall(filename=latest_cases_path)
        latest_hospitalisations = plot_results_hospitals(filename=latest_hospitalisations_path)
        cc = count_sim_results(borough=self.district, scenario='extend', res_dir=cc_path)

        return region_map, demographics, measures, latest_cases, latest_hospitalisations, cc

    def set_region(self, country, district):
        self.country = country
        self.district = district


@app.route('/about')
def about():
    return render_template('about.html', content='Test')

@app.route('/create_page', methods=['GET', 'POST'])
def load_page():
    result=page.create_page()
    return result

@app.route('/set_region', methods=['POST'])
def set_region():
    output = request.get_json()
    result = json.loads(output) #this converts the json output to a python dictionary
    page.set_region(result['country'], result['district'])
    return "ok"

if __name__ == '__main__':
    page = district_class("lithuania","klaipeda")
    app.run(port=5000)