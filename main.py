from rrt import RRT
# from rrtbase import RRTmap, Robot
# from rrtbase import RRTgraph
# import time
# import math
# import pygame
# import random
if __name__ == '__main__':
    rrt = RRT((50,50),(930, 510), "ObstacleMap2.png", "DDR.png")
    running = True
    while running:
        try:
            path_coords = rrt.main()
            running = False
        except:
            running = True

    print("coords:",path_coords)

# converting to pickle file
# rrt = RRT((50,50),(930, 510), "ObstacleMap2.png", "DDR.png")
# import pickle
# f = open('flask_api/rrt_file.pkl','wb')
# pickle.dump(rrt,f)
# f.close()
