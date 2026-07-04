import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    condition=(
        (triangle['x']+triangle['y']>triangle['z']) &
        (triangle['x']+triangle['z']>triangle['y']) &
        (triangle['z']+triangle['y']>triangle['x']) 
    )
    triangle['triangle']=np.where(condition,'Yes','No')
    return triangle