from multiprocessing import managers
from statistics import variance
import numpy as np
def calculate(list_of_numbers):
    if len(list_of_numbers)!=9:
        raise ValueError("List must contain nine numbers.")
    else:
        mat=np.array(list_of_numbers).reshape(3,3)
    mean=[]
    mna0=np.mean(mat,axis=0)
    mna1=np.mean(mat,axis=1)
    mnf=np.mean(mat)
    mean.append(mna0.tolist())
    mean.append(mna1.tolist())
    mean.append(mnf)
    variance=[]
    va0=np.var(mat,axis=0)
    va1=np.var(mat,axis=1)
    vf=np.var(mat)
    variance.append(va0.tolist())
    variance.append(va1.tolist())
    variance.append(vf)
    std=[]
    st0=np.std(mat,axis=0)
    st1=np.std(mat,axis=1)
    sf=np.std(mat)
    std.append(st0.tolist())
    std.append(st1.tolist())
    std.append(sf)
    max=[]
    mx0=np.max(mat,axis=0)
    mx1=np.max(mat,axis=1)
    mf=np.max(mat)
    max.append(mx0.tolist())
    max.append(mx1.tolist())
    max.append(mf)
    min=[]
    mn0=np.min(mat,axis=0)
    mn1=np.min(mat,axis=1)
    mf=np.min(mat)
    min.append(mn0.tolist())
    min.append(mn1.tolist())
    min.append(mf)
    sum=[]
    sm0=np.sum(mat,axis=0)
    sm1=np.sum(mat,axis=1)
    sf=np.sum(mat)
    sum.append(sm0.tolist())
    sum.append(sm1.tolist())
    sum.append(sf)
    return {'mean':mean,
            'variance':variance,
            'standard deviation':std,
            'max':max,
            'min':min,
            'sum':sum}


    

