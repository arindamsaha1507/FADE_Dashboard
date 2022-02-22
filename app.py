from flask import Flask, render_template, request
from plot_functions import plot_map, plot_demo, plot_measures, plot_results_overall, plot_results_hospitals, plot_aggregated_data, plot_spread
import subprocess
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', content='Test')

@app.route('/lithuania', methods=['GET', 'POST'])
def lithuania():

    msg1 = 'Enter the parameters to start simulation'
    spread_time = random.randint(0, 99)
    msg2 = 'Showing spread of infections on day ' + str(spread_time)

    if request.method == 'POST':
        # for i in range(int(request.form.get('reps'))):
        #     cmd = 'bash facs_script.sh klaipeda ' + request.form.get('sim_length') + ' ' + request.form.get('starting_infections') + ' ' + request.form.get('reps')
        #     subprocess.call(cmd, shell=True)
        # msg = request.form
        if request.form['but'] == 'but1':
            msg1 = 'Simulation submitted!'
        if request.form['but'] == 'but2':
            spread_time = int(request.form.get('spread_time'))
            msg2 = 'Showing spread of infections on day ' + request.form.get('spread_time')

    region_map = plot_map(fname='Data/lithuania/klaipeda/input/klaipeda_buildings.csv', zoom=8.0)
    demographics = plot_demo(fname='Data/lithuania/klaipeda/input/age-distr.csv', region='Klaipeda')
    measures = plot_measures(fname='Data/lithuania/klaipeda/input/measures_test.csv')

    latest_cases = plot_results_overall(filename='Data/lithuania/klaipeda/output/klaipeda-latest.csv')
    latest_hospitalisations = plot_results_hospitals(filename='Data/lithuania/klaipeda/output/klaipeda-latest.csv')

    all_cases = plot_aggregated_data(borough='klaipeda', observable=['susceptible', 'exposed', 'infectious', 'recovered', 'dead'], scenario=['extend'], res_dir='Data/lithuania/klaipeda/output/')
    all_hospitalisations = plot_aggregated_data(borough='klaipeda', observable=['num hospitalisations today', 'hospital bed occupancy', 'cum num hospitalisations today'], scenario=['extend'], res_dir='Data/lithuania/klaipeda/output/')

    spread = plot_spread(fname='Data/lithuania/klaipeda/output/covid_out_infections_0.csv', zoom=8.0, spread_time=spread_time)

    return render_template('country.html', 
    message1=msg1, 
    message2=msg2, 
    country='Lithuania', 
    region='Klaipeda', 
    maps=region_map, 
    demo=demographics, 
    measures=measures, 
    latest_cases=latest_cases,
    latest_hospitalisations=latest_hospitalisations, 
    all_cases=all_cases, 
    all_hospitalisations=all_hospitalisations,
    spread=spread)

@app.route('/about')
def about():
    return render_template('about.html', content='Test')
