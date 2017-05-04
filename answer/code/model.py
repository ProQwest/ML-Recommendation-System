import os
import numpy as np
import random
import time

def cal_error(rating, u_id, m_id, U, M, users, movies):
    u_index = u_id -1
    m_index = m_id -1
    pred = 0.0
    vu = np.append(users[u_index], U[u_index])
    vm = np.append(M[m_index], movies[m_index])
    pred = vu.dot(vm)
    return rating - pred

def get_step(error):
    if abs(error) >= 0.3:
        return abs(error) / 100.0
    if abs(error) >= 0.1:
        return abs(error) **2
    return abs(error)

def update(U, M, users, movies, error, u_id, m_id):
    u_index = u_id -1
    m_index = m_id -1
    step = get_step(error)
    l = 0.1
    try:
        U[u_index] = U[u_index] - step * (-1*error*movies[m_index] +l*U[u_index])
        M[m_index] = M[m_index] - step * (-1*error*users[u_index]  +l*M[m_index])
        return 0
    except:
        print 'error in update'
        return 1

def cal_RMSE(U, M, users, movies, train):
    u_matrix = np.append(users, U, 1)
    m_matrix = np.append(M, movies, 1)
    matrix = u_matrix.dot(m_matrix.T)
    length = train.shape[0]
    s = 0.0
    for i in range(length):
        s += np.square(train[i][2] - matrix[train[i][0]-1][train[i][1]-1])
    s = s / length
    return np.sqrt(s)

def SGD(U, M, users, movies, train):
    RMSE_interval = 2
    cnt = 0
    length = train.shape[0]
    while True:
        for i in range(length):
            u_id = train[i][0]
            m_id = train[i][1]
            rating = train[i][2]
            error = cal_error(rating, u_id, m_id, U, M, users, movies)
            if update(U, M, users, movies, error, u_id, m_id):
                print 'update failed'
                break
        print 'epoch ======'

        if cnt % RMSE_interval == 0:
            print time.ctime(), 'iteration: ', cnt
            RMSE = cal_RMSE(U, M, users, movies, train)
            print 'RMSE = ', RMSE
            if RMSE <= 0.872:
                break
        cnt += 1
    print 'SGD finish '

def predict(U, M, users, movies, test):
    result = np.array([])
    length = test.shape[0]
    u_matrix = np.append(users, U, 1)
    m_matrix = np.append(M, movies, 1)
    matrix = u_matrix.dot(m_matrix.T)
    for i in range(length):
        u_i = test[i][0]-1
        m_i = test[i][1]-1
        result = np.append(result, [matrix[u_i][m_i]], 0)
    return result
