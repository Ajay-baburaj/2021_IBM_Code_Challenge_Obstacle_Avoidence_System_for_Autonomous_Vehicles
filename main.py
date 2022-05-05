from rrt import RRT
# from rrtbase import RRTmap, Robot
# from rrtbase import RRTgraph
# import time
# import math
# import pygame
# import random

import sqlite3
path_coordinate_list = []

if __name__ == '__main__':
    rrt = RRT((50,50),(930, 510), "ObstacleMap2.png", "DDR.png")
    running = True
    while running:
        try:
            path_coords = rrt.main()
            running = False
        except:
            running = True
    
    path_coordinate_list.append(path_coords)
    

# converting to pickle file
# rrt = RRT((50,50),(930, 510), "ObstacleMap2.png", "DDR.png")
# import pickle
# f = open('flask_api/rrt_file.pkl','wb')
# pickle.dump(rrt,f)
# f.close()

#connecting to database(sqlite)

coordinate_list_main = path_coordinate_list[0]

conn = sqlite3.connect('database.db')
c = conn.cursor()
 

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Xcordinate REAL, Ycordinate REAL)')
 
def data_entry():
    for i in range(len(coordinate_list_main)):
        tuple_a = coordinate_list_main[i]
        xcordinate = tuple_a[0]
        ycordinate = tuple_a[1]
        c.execute("INSERT INTO RecordONE (Xcordinate, Ycordinate) VALUES(?, ?)", (xcordinate, ycordinate))
        conn.commit()
 
create_table()
data_entry()
 
c.close()
conn.close()
