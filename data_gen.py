import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from functools import reduce
import pandas as pd
import random
from random import randint
import json

trail = "trail"
crp = "crp"
il6 = "il6"
tgfb = "tgfb"
tgfa = "tgfa"
il8 = "il8"
ip10 = "ip10"
rhr = "rhr"

def generate_user():    
    user_id = randint(100000, 999999)
    #result['user_id'] = user_id
    user_list = [user_id] * 90
    user_df = pd.DataFrame(user_list)
    
    date = pd.date_range('2022-1-1', periods=90, freq='d')
    date_df = pd.DataFrame(date)

    result = pd.concat([date_df, user_df],axis = 1, join = 'outer', ignore_index=False, sort=False)
    
    result.columns = ['date', 'user_id']
    return result

def biomarker_gen(upper, biomarker_name):
    values_month1  = []
    
    values_month2_2weeks = []
    values_month2_d15_21 = []
    values_month2_d22_28 = []
    
    values_month3_2weeks = []
    values_month3_d15_21 = []
    values_month3_d22_31 = []
    
    for date in range(31):
        values_month1.append(random.uniform(upper*1.03, upper*1.08))
    for date in range(14):    
        values_month2_2weeks.append(random.uniform(upper*1.03, upper*1.08))
    for date in range(7):
        values_month2_d15_21.append(random.uniform(upper*1.025, upper*1.035))
    for date in range(7):
        values_month2_d22_28.append(random.uniform(upper*0.99, upper*1.01))
    for date in range(14):
        values_month3_2weeks.append(random.uniform(upper*0.99, upper*1.01))
    for date in range(7):
        values_month3_d15_21.append(random.uniform(upper*0.90, upper*0.99))
    for date in range(10):
        values_month3_d22_31.append(random.uniform(upper*0.87, upper*0.89))


        
        df_m1 = pd.DataFrame (values_month1)
        
        df_m2_2wk = pd.DataFrame (values_month2_2weeks)
        df_m2_d15 = pd.DataFrame (values_month2_d15_21)
        df_m2_d22 = pd.DataFrame (values_month2_d22_28)
        
        df_m3_2wk = pd.DataFrame (values_month3_2weeks)
        df_m3_d15 = pd.DataFrame (values_month3_d15_21)
        df_m3_d22 = pd.DataFrame (values_month3_d22_31)
        
        periods = [df_m1, df_m2_2wk, df_m2_d15, df_m2_d22, df_m3_2wk, df_m3_d15, df_m3_d22]
        
        result = pd.concat(periods)
        
        result.columns = [biomarker_name]
        
        date = pd.date_range('2022-1-1', periods=90, freq='d')
        date_df = pd.DataFrame(date)
        
        result = result.append(date_df)
        result = result.apply(lambda x: pd.Series(x.dropna().values))
        result.columns = [biomarker_name, 'date']
        result = result[['date', biomarker_name]]
        
    return result

def hrv_gen(upper, lower):
    values_month1  = []
    
    values_month2_2weeks = []
    values_month2_d15_21 = []
    values_month2_d22_28 = []
    
    values_month3_2weeks = []
    values_month3_d15_21 = []
    values_month3_d22_31 = []
    
    for date in range(31):
        values_month1.append(random.uniform(lower*0.87, upper*0.89))
    for date in range(14):    
        values_month2_2weeks.append(random.uniform(lower*0.90, upper*0.99))
    for date in range(7):
        values_month2_d15_21.append(random.uniform(lower*0.90, upper*0.99))
    for date in range(7):
        values_month2_d22_28.append(random.uniform(lower*0.99, upper*1.01))
    for date in range(14):
        values_month3_2weeks.append(random.uniform(lower*0.99, upper*1.01))
    for date in range(7):
        values_month3_d15_21.append(random.uniform(lower*1.025, upper*1.035))
    for date in range(10):
        values_month3_d22_31.append(random.uniform(lower*1.03, upper*1.08))


        
        df_m1 = pd.DataFrame (values_month1)
        
        df_m2_2wk = pd.DataFrame (values_month2_2weeks)
        df_m2_d15 = pd.DataFrame (values_month2_d15_21)
        df_m2_d22 = pd.DataFrame (values_month2_d22_28)
        
        df_m3_2wk = pd.DataFrame (values_month3_2weeks)
        df_m3_d15 = pd.DataFrame (values_month3_d15_21)
        df_m3_d22 = pd.DataFrame (values_month3_d22_31)
        
        periods = [df_m1, df_m2_2wk, df_m2_d15, df_m2_d22, df_m3_2wk, df_m3_d15, df_m3_d22]
        
        result = pd.concat(periods)
        
        result.columns = ['hrv']
        
        date = pd.date_range('2022-1-1', periods=90, freq='d')
        date_df = pd.DataFrame(date)
        
        result = result.append(date_df)
        result = result.apply(lambda x: pd.Series(x.dropna().values))
        result.columns = ['hrv', 'date']
        result = result[['date', 'hrv']]
        
    return result

def mood_gen():
    values_month1  = []
    
    values_month2_2weeks = []
    values_month2_d15_21 = []
    values_month2_d22_28 = []
    
    values_month3_2weeks = []
    values_month3_d15_21 = []
    values_month3_d22_31 = []
    
    for date in range(31):
        values_month1.append(random.randint(2, 4))
    for date in range(14):    
        values_month2_2weeks.append(random.randint(2, 4))
    for date in range(7):
        values_month2_d15_21.append(random.randint(4, 6))
    for date in range(7):
        values_month2_d22_28.append(random.randint(6, 7))
    for date in range(14):
        values_month3_2weeks.append(random.randint(7, 8))
    for date in range(7):
        values_month3_d15_21.append(random.randint(7, 9))
    for date in range(10):
        values_month3_d22_31.append(random.randint(8, 9))


        
        df_m1 = pd.DataFrame (values_month1)
        
        df_m2_2wk = pd.DataFrame (values_month2_2weeks)
        df_m2_d15 = pd.DataFrame (values_month2_d15_21)
        df_m2_d22 = pd.DataFrame (values_month2_d22_28)
        
        df_m3_2wk = pd.DataFrame (values_month3_2weeks)
        df_m3_d15 = pd.DataFrame (values_month3_d15_21)
        df_m3_d22 = pd.DataFrame (values_month3_d22_31)
        
        periods = [df_m1, df_m2_2wk, df_m2_d15, df_m2_d22, df_m3_2wk, df_m3_d15, df_m3_d22]
        
        result = pd.concat(periods)
        
        result.columns = ['mood']
        
        date = pd.date_range('2022-1-1', periods=90, freq='d')
        date_df = pd.DataFrame(date)
        
        result = result.append(date_df)
        result = result.apply(lambda x: pd.Series(x.dropna().values))
        result.columns = ['mood', 'date']
        result = result[['date', 'mood']]
        
    return result

def pain_gen():
    values_month1  = []
    
    values_month2_2weeks = []
    values_month2_d15_21 = []
    values_month2_d22_28 = []
    
    values_month3_2weeks = []
    values_month3_d15_21 = []
    values_month3_d22_31 = []
    
    for date in range(31):
        values_month1.append(random.randint(8, 9))
    for date in range(14):    
        values_month2_2weeks.append(random.randint(7, 9))
    for date in range(7):
        values_month2_d15_21.append(random.randint(7, 8))
    for date in range(7):
        values_month2_d22_28.append(random.randint(6, 7))
    for date in range(14):
        values_month3_2weeks.append(random.randint(4, 6))
    for date in range(7):
        values_month3_d15_21.append(random.randint(2, 4))
    for date in range(10):
        values_month3_d22_31.append(random.randint(2, 4))


        
        df_m1 = pd.DataFrame (values_month1)
        
        df_m2_2wk = pd.DataFrame (values_month2_2weeks)
        df_m2_d15 = pd.DataFrame (values_month2_d15_21)
        df_m2_d22 = pd.DataFrame (values_month2_d22_28)
        
        df_m3_2wk = pd.DataFrame (values_month3_2weeks)
        df_m3_d15 = pd.DataFrame (values_month3_d15_21)
        df_m3_d22 = pd.DataFrame (values_month3_d22_31)
        
        periods = [df_m1, df_m2_2wk, df_m2_d15, df_m2_d22, df_m3_2wk, df_m3_d15, df_m3_d22]
        
        result = pd.concat(periods)
        
        result.columns = ['SR_pain']
        
        date = pd.date_range('2022-1-1', periods=90, freq='d')
        date_df = pd.DataFrame(date)
        
        result = result.append(date_df)
        result = result.apply(lambda x: pd.Series(x.dropna().values))
        result.columns = ['SR_pain', 'date']
        result = result[['date', 'SR_pain']]
        
    return result

def generate_variables(lower, upper, variable):
    variable_list = []
    data_range = 90
    for x in range(data_range):
        if isinstance(lower, float):
            variable_list.append(random.uniform(lower, upper))
        else:
            variable_list.append(random.randint(lower, upper))
            
    variable_df = pd.DataFrame(variable_list)
    
    date = pd.date_range('2022-1-1', periods=90, freq='d')
    date_df = pd.DataFrame(date)

    result = pd.concat([date_df, variable_df],axis = 1, join = 'outer', ignore_index=False, sort=False)
    
    result.columns = ['date', variable]
    
    return result


def generate_patients(patients):    
    
    patients = range(patients)
    
    ip10 = "ip10"
    trail_upper = 20
    crp_upper = 3
    il6_upper = 14.5
    tgfb_upper = 6.2
    tgfa_upper = 21.1
    il8_upper = 6.1
    ip10_upper = 20
    
    patient_list = []
    
    
    
    for x in patients:
        
        
        trail_df = biomarker_gen(trail_upper, trail)
        crp_df = biomarker_gen(crp_upper, crp)
        il6_df = biomarker_gen(il6_upper, il6)
        tgfb_df = biomarker_gen(tgfb_upper, tgfb)
        tgfa_df = biomarker_gen(tgfa_upper, tgfa)
        il8_df = biomarker_gen(il8_upper, il8)
        ip10_df = biomarker_gen(ip10_upper, ip10)
        rhr_df = generate_variables(65, 70, 'rhr')
        cal_df = generate_variables(1600, 2400, 'calories')
        sleep_df = generate_variables(300, 480, 'sleep')
        temp_df = generate_variables(36.5, 37.2, 'skin_temp')
        mood_df = mood_gen()
        pain_df = pain_gen()
        hrv_df = hrv_gen(72, 46.3)
        user_df = generate_user()
    
        data_frames = [trail_df, crp_df, il6_df, tgfb_df, tgfa_df, il8_df, ip10_df, rhr_df, cal_df, sleep_df, temp_df, mood_df, pain_df, hrv_df, user_df]
        
        patient = reduce(lambda  left,right: pd.merge(left,right,on=['date'],
                                            how='left'), data_frames)
        #patient.date = patient.date.apply(lambda x: x.date())
        patient.date = patient.date.apply(lambda x: x.strftime('%Y-%m-%d'))
        
        patient_list.append(patient)
    
    return patient_list

def Merge(canurta_data_dict, range_dictionary):
    return(canurta_data_dict.update(range_dictionary))

def create_JSON(list_of_dfs):
    results = pd.concat(list_of_dfs)
    results.reset_index(drop=True, inplace=True)
    results = results.to_json('temp_patients.json', orient='index')
    obj = json.load(open('temp_patients.json'))
    obj = {'Patient_info': obj}
    Merge(obj, range_dictionary)
    # Serializing json  
    json_object = json.dumps(obj, indent = 4)
    # Writing to "canurta_json.json"
    with open("canurta_json.json", "w") as outfile:
        outfile.write(json_object)
    
    return print("Full JSON created")

def JSON_dashboard(list_of_dfs):
    results = pd.concat(list_of_dfs)
    results.reset_index(drop=True, inplace=True)
    results = results.to_json('temp_patients.json', orient='index')
    obj = json.load(open('temp_patients.json'))
    json_object = json.dumps(obj, indent = 4)
    # Writing to "canurta_json.json"
    with open("canurta_dashboard.json", "w") as outfile:
        outfile.write(json_object)
    
    return print("Dashboard JSON created")
        
trail_df = biomarker_gen(20, trail)
crp_df = biomarker_gen(3, crp)
il6_df = biomarker_gen(14.5, il6)
tgfb_df = biomarker_gen(6.2, tgfb)
tgfa_df = biomarker_gen(21.1, tgfa)
il8_df = biomarker_gen(6.1, il8)
ip10_df = biomarker_gen(20, ip10)
rhr_df = biomarker_gen(20, ip10)

data_frames = [trail_df, crp_df, il6_df, tgfb_df, tgfa_df, il8_df, ip10_df]

patient_1 = reduce(lambda  left,right: pd.merge(left,right,on=['date'],
                                            how='left'), data_frames)

range_dictionary = {'healthy_ranges': {
    "IP-10": {"original": "10 to 20 pg mL−1 (± 0.2)",
              "lower": 10,
              "upper": 20,
              "units": "pg mL−1 (± 0.2)"
    },
    "TRAIL": {"original": "5 to 20 pg mL−1 (± 2.5)",
              "lower": 5,
              "upper": 20,
              "units": "pg mL−1 (± 2.5)"
    },
    "CRP": {"original": "0.05 to 3 ng mL−1 (±1.34)",
              "lower": 0.05,
              "upper": 3,
              "units": "ng mL−1 (±1.34)"
    },
    "TNFa": {"original": "0.110±0.030 pg mL−1",
              "lower": 0.110,
              "upper": 0.030,
              "units": "pg mL−1"
    },
    "Il-6": {"original": "0.089±0.012 pg mL−1",
              "lower": 0.089,
              "upper": 0.012,
              "units": "pg mL−1"
    },
    "Il-8": {"original": "1.5 to 6.1 pg mL−1",
              "lower": 1.5,
              "upper": 6.1,
              "units": "pg mL−1"
    },
    "TGFb": {"original": "1.7 to 6.2 pg mL−1",
              "lower": 1.7,
              "upper": 6.2,
              "units": "pg mL−1"
    },
    "HRV": {"original": "46.3 and 72.0",
              "lower": 46.3,
              "upper": 72.0,
              "units": "tbd"
    }}}
    
# Convert DataFrame to JSON

list_of_df = generate_patients(25)
create_JSON(list_of_df)
JSON_dashboard(list_of_df)

