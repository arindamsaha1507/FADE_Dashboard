import pandas as pd
import yaml
from datetime import datetime, date, timedelta
import plotly.express as px
import sys

def yml_to_csv(fin, fout):

    with open(fin, 'r') as ff:
        try:
            dd = yaml.safe_load(ff)
        except yaml.YAMLError as exc:
            print(exc)

    dates = list(dd.keys())

    dates = [x for x in dates if x not in ['date_format', 'dd/mm/yyyy', 'keyworker_fraction']]

    print(dates)

    dates1 = [datetime.strptime(ii, "%d/%m/%Y").date() for ii in dates]

    del(dd['keyworker_fraction'])
    del(dd['dd/mm/yyyy'])
    del(dd['date_format'])

    cols = ['date', 'case_isolation', 'household_isolation', 'partial_closure', 'closure', 'work_from_home', 'mask_uptake', 'mask_uptake_shopping', 'social_distance', 'traffic_multiplier', 'track_trace_efficiency']
    df = pd.DataFrame(columns=cols)
    for i in range(len(dates)):
        row = dd[dates[i]]
        row['date'] = dates1[i]
        df = df.append(row, ignore_index=True)
    df = df.fillna('-')

    print(df)

    df.sort_values(by='date', inplace=True)
    df = df.reset_index(drop=True)

    df.to_csv(fout)

if __name__ == '__main__':
    fin = str(sys.argv[1])
    fout = str(sys.argv[2])
    print(fin)
    print(fout)
    yml_to_csv(fin, fout)