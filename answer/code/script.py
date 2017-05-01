import os, time, random, math
import numpy as np

curr_path = os.getcwd()
user_path = curr_path + '/../../users.dat'
result_path = curr_path + '/../results.csv'
train_path = curr_path + '/../../training_rating.dat'
movie_path = curr_path + '/../../movies.dat'
test_path = curr_path + '/../../testing.dat'

def process_user():
    user = np.loadtxt(user_path, dtype = str, delimiter='::')
    users = np.zeros((user.shape[0],30))
    U = np.zeros((user.shape[0],19))

    for i in range(user.shape[0]):
        if user[i][1] == 'F':
            users[i][1] = 1
        else:
            users[i][0] = 1

        age = float(user[i][2])

        if   age <= 1: users[i][2] = 1
        elif age <=18: users[i][3] = 1
        elif age <=25: users[i][4] = 1
        elif age <=35: users[i][5] = 1
        elif age <=45: users[i][6] = 1
        elif age <=50: users[i][7] = 1
        else :         users[i][8] = 1

        occu = int(user[i][3])
        users[i][occu + 8] = 1

        U[i] = np.random.rand(U.shape[1])

    assert (users.shape[0] == U.shape[0])
    assert (U.shape[1]  == 19)
    return U, users


def process_test():
    return

def process_movie():
    dic = {}
    dic['Action']       = 0
    dic['Adventure']    = 1
    dic['Animation']    = 2
    dic['Children\'s']  = 3
    dic['Comedy']       = 4
    dic['Crime']        = 5
    dic['Documentary']  = 6
    dic['Drama']        = 7
    dic['Fantasy']      = 8
    dic['Film-Noir']    = 9
    dic['Horror']       = 10
    dic['Musical']      = 11
    dic['Mystery']      = 12
    dic['Romance']      = 13
    dic['Sci-Fi']       = 14
    dic['Thriller']     = 15
    dic['War']          = 16
    dic['Western']      = 17

    inp = np.loadtxt(movie_path, dtype = str, delimiter='::')
    movies = np.zeros((inp.shape[0],19))
    M = np.zeros((inp.shape[0],30))
    for i in range(inp.shape[0]):
        M[i] = np.random.rand(M.shape[1])
        temp = inp[i][1].split('|')
        movies[i][18] = 1
        for key in temp:
            movies[i][dic[key]] = 1

    return M , movies


def process_train():
    return


def write_result():
    return

def main():
    U, users = process_user()
    M, movies = process_movie()
    print 'program finish'


if __name__ == '__main__':
    main()
