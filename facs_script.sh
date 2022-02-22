facs_dir='/home/arindam/Dropbox/Brunel/FACS/facs'
cur_dir='/home/arindam/Dropbox/Dashboard'

country='lithuania'

runfile='run.py'

transition_scenario="extend-lockdown"
transition_mode=1
output_dir="results"
location=$1
simulation_period=$2
starting_infections=$3
reps=$4

cmd="python3 $runfile --location=$location --transition_scenario=$transition_scenario --simulation_period=$simulation_period --output_dir=$output_dir --starting_infections=$starting_infections"

suffix='_buildings.csv'

cp $cur_dir/Data/$country/$location/input/age-distr.csv $facs_dir/covid_data/
cp $cur_dir/Data/$country/$location/input/$location$suffix $facs_dir/covid_data/
cd $facs_dir

$cmd
# $cmd | tee log.txt

datestamp=`date '+%F_%H:%M:%S'` 

suffix='--1.csv'
joiner='-'

cp $facs_dir/$output_dir/$location$joiner$transition_scenario$suffix $cur_dir/Data/$country/$location/output/$location$joiner$transition_scenario$joiner$datestamp$suffix

suffix1='-latest.csv'

cp $facs_dir/$output_dir/$location$joiner$transition_scenario$suffix $cur_dir/Data/$country/$location/output/$location$suffix1

cp $facs_dir/covid_out_infections_0.csv $cur_dir/Data/$country/$location/output/