#訓練使用
#TA的基金存在04基金有些會顯示為4，經研判問題發生原因有可能跟CSV檔案讀取有關，因此此function將cover此問題
#Author : Yuchi Li 
def deletzero(x):
    if type(x) == str  and x[0] == "0":
        x = x[1:]
    if type(x) == int:
        x = str(x)
    return x
    
#訓練使用
#根據LSTM特性將資料製作成符合時間序列的型態
#Author : Arleigh Chang
#2020/08/20 Updated : Yuchi Li 
def train_windows(df:pd.DataFrame,learn_target,drop_list, ref_day=3, predict_day=1):

    X_train, Y_train = [], []
    Total = df.shape[0]
    while len(df) <=3:
        insert = df.iloc[0,:]
        insert = insert.to_frame().T
        df = pd.concat([insert,df],axis=0)

    # 產生一個新欄位放前一天贖回報酬率當特徵
    prev_ROI = df[learn_target].tolist()
    prev_ROI.insert(0,0)
    prev_ROI.pop(-1)
    # 將target放到最後一欄
    target = df[learn_target].values
    df =df.drop(drop_list,axis=1)
    df['pre_Redem_ROI'] = prev_ROI
    df[learn_target] = target
    df = df.apply(pd.to_numeric, errors='coerce')
    for i in range(df.shape[0]-ref_day):
        X_train.append(np.array(df.iloc[i:i+ref_day,:-1]))
        Y_train.append(np.array(df.iloc[i+ref_day:i+ref_day+predict_day][learn_target]))
    return np.array(X_train), np.array(Y_train)

### by基金和戶號且按照時間先後
#Author : Yuchi Li 
#2020/08/21 Updated : Arleigh Chang 
def groupBF_FUND(df:pd.DataFrame,learn_target:str,drop_list:list):
    convert_x_store = []
    convert_y_store = []
    for i in df['BF_NO'].unique():
        bf = df[df['BF_NO']==i]
        for j in bf['FUND_ID'].unique():
            groupby = bf[bf['FUND_ID']==j]
            if len(groupby)>=2:
                groupby = groupby.sort_values(by=['REDEM_NAV_DATE'])
                X_train,Y_train = train_windows(groupby,learn_target,drop_list)
                convert_x_store = convert_x_store+list(X_train)
                convert_y_store = convert_y_store+list(Y_train)
    return np.array(convert_x_store),np.array(convert_y_store)          
       
