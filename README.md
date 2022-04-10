# FADE_Dashboard

FADE _(FACS Aapplication Dashboard for End-users)_ is an integrated dashboard for [FACS](https://github.com/djgroen/facs). It is developed to 
- Assist the pre-processing of input data required by FACS.
- Visualisation of output data produced by FACS.

To run the application,
1. Clone the repository.
1. Install the packages given in `requirements.txt`.
2. Inside the `Data` derectory, orgsnise the input and output files as
   ```
    Data
    ├── lithuania
    │   └── klaipeda
    │       ├── input
    │       │   ├── age-distr.csv
    │       │   ├── klaipeda_buildings.csv
    │       │   ├── measures_klaipeda.yml
    │       │   └── measures_test.csv
    │       └── output
    │           ├── covid_out_infections_0.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_00:04:33--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_00:19:19--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_00:30:16--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_00:41:08--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_00:51:49--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_01:02:51--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_01:13:54--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_01:24:17--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_01:35:14--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_01:45:58--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_19:10:37--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-22_19:50:21--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_07:33:34--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_10:27:16--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_17:34:09--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_17:34:36--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_17:34:48--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_17:35:03--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_19:07:25--1.csv
    │           ├── klaipeda-extend-lockdown-2022-02-23_19:59:43--1.csv
    │           └── klaipeda-latest.csv
    └── turkey
        ├── cankaya
        │   ├── input
        │   │   ├── age-distr.csv
        │   │   ├── cankaya_buildings.csv
        │   │   └── measures_cankaya.yml
        │   └── output
        │       ├── cankaya-extend-lockdown-2022-02-22_00_04_33--1.csv
        │       ├── cankaya-latest.csv
        │       └── covid_out_infections_0.csv
        └── sultanbeyli
            ├── input
            │   ├── age-distr.csv
            │   ├── measures_sultanbeyli.yml
            │   └── sultanbeyli_buildings.csv
            └── output
                ├── covid_out_infections_0.csv
                ├── sultanbeyli-extend-lockdown-2022-02-22_00_04_33--1.csv
                └── sultanbeyli-latest.csv
   ```
3. Run `python app.py`.
