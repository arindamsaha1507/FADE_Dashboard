# Restrictions and Measures

The restrictions and measures including government interventions taken to mitigate the spread of disease are specified in a `yml` file named `measures_<location>.yml`. In this file, a list of dates on which the restrictions were imposed or modified is given. Corresponding to each date, a description of the restrictions are given. These restrictions can be defined in terms the following heads.

- **`case_isolation`**: A binary value which determines if infected people go into quarantine.
- **`household_isolation`**: A binary value which decides if all members of the household go into quarantine when at least one of its members is isolated.
- **`traffic_multiplier`**: Volume of internal traffic within the region as compared to the normal (a non-lock-down situation).
- **`external_multiplier`**: Volume of external traffic coming into (or going out of) the region as compared to the normal (a non-lock-down situation).
- **`work_from_home`**: Fraction of workforce which is working from home.
- **`social_distancing`**: Fraction of the population that complies with the social distancing guidelines.
- **`mask_uptake`**: Fraction of the population wearing masks outside of the house.
- **`mask_uptake_shopping`**: Fraction of the population wearing masks while in shops or supermarkets.
- **`track_trace_efficiency`**: Percentage of the population who escape the track and trace system.
- **`closure`**: List of building types which are closed for the public.
- **`partial_closure`**: List of tuples which define the extent of closures (on a scale from 0-1) for building types.

In addition to to list of dates, the `yml` file should also have a key called `keyworker_fraction` with a value giving the fraction of key workers in the population. This is the fraction of employees who go to the workplace despite the lock-down.