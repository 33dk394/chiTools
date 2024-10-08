import itertools
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def gen_data(part_num: int, ret_num: int, tool_num: int, pre1tool_num: int, pre2tool_num: int, chuck_num: int) -> pd.DataFrame:
    lst_part = [f'Part_{i}' for i in range(1, part_num)]
    lst_ret = [f'Ret_{i}' for i in range(1, ret_num)]
    lst_tool = [f'Tool_{i}' for i in range(1, tool_num)]
    lst_pre1 = [f'Pre1Tool_{i}' for i in range(1, pre1tool_num)]
    lst_pre2 = [f'Pre2Tool_{i}' for i in range(1, pre2tool_num)]
    lst_chuck = [f'Chuck_{i}' for i in range(1, chuck_num)]
    
    lst_comb = [lst_part, lst_ret, lst_tool, lst_pre1, lst_pre2, lst_chuck]
    feat_lst = ["Part", "Reticle", "Tool", "Prev1Tool", "Prev2Tool", "ChuckID"]
    df_data = pd.DataFrame([i for i in itertools.product(*lst_comb)], columns=feat_lst)
    df_data.to_csv("./df_data.csv", index=False)
    return df_data

def label_encode_data(df_data: pd.DataFrame, lst_feat: list):
    lst_label_encoder = []
    df_data_le = pd.DataFrame()
    
    for feat in lst_feat:
        label_encoder = LabelEncoder()
        df_data_le[feat] = label_encoder.fit_transform(df_data[feat])
        lst_label_encoder.append(label_encoder)
        
    return df_data_le, lst_label_encoder

def onehot_encode_data(df_data_le: pd.DataFrame) -> np.ndarray:
    ohe = OneHotEncoder()
    res = ohe.fit_transform(df_data_le).toarray()
    return res