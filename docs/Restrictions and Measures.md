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
- **`track_trace_efficiency`**: Fraction of the population who escape the track and trace system.
- **`closure`**: List of building types which are closed for the public.
- **`partial_closure`**: List of tuples which define the extent of closures (on a scale from 0-1) for building types.

In addition to to list of dates, the `yml` file should also have a key called `keyworker_fraction` with a value giving the fraction of key workers in the population. This is the fraction of employees who go to the workplace despite the lock-down. A sample section of a measures file is given below.

```yaml
keyworker_fraction: 0.2

1/3/2020:
  case_isolation: True
  household_isolation: True
  traffic_multiplier: 0.8

12/3/2020:
  partial_closure: 
    leisure: 0.3
  work_from_home: 0.325
  social_distance: 0.25
  mask_uptake: 0.05
  traffic_multiplier: 0.4
  external_multiplier: 0.7

20/3/2020:
  closure: ["leisure"]
  partial_closure: 
    shopping: 0.3
  work_from_home: 0.45
  mask_uptake: 0.2
  mask_uptake_shopping: 0.6
  traffic_multiplier: 0.3
  external_multiplier: 0.7
```

The above example highlights following two two important features of the restrictions and measures file.

1. At the start of the simulations, no restrictions are assumed. In other words,

   ```yaml
   case_isolation: False
   household_isolation: False
   traffic_multiplier: 1.0
   external_multiplier: 1.0
   work_from_home: 0.0
   social_distancing: 0.0
   mask_uptake: 0.0
   mask_uptake_shopping: 0.0
   track_trace_efficiency: 1.0
   closure: []
   partial_closure: []
   ```
   
   Therefore, in the above example, on 1/3/2020, only `case_isolation` and `household_isolation` are switched to True. There are no other restrictions applied.
   
2. If for a particular date, a variable is not mentioned, then its value remains unchanged. In the above example, `social_distancing` is not mentioned for 20/3/2020. Therefore, its value is assumed to be 0.25, which remains unchanged from 12/3/2020.

