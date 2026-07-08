import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['Duration']=employees['out_time']-employees['in_time']
    temp_df=employees.groupby(['event_day','emp_id'],as_index=False)['Duration'].sum()
    temp_df.rename(columns={'Duration':'total_time','event_day':'day'},inplace=True)
    return temp_df