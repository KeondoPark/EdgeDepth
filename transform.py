from scipy.spatial.transform import Rotation
from numpy.linalg import norm
import math
import time
import numpy as np
import array

def rotation_ply(filename):
    with open(filename,'r') as input_file:
        header_cnt = 8
        cnt = 0
        all_lines = input_file.readlines()
        header = all_lines[:header_cnt]
        data = all_lines[header_cnt:261518 + header_cnt]

        #point_cloud2 = [[float(item) for item in line] for line in point_cloud]
        print(data[:10])
        point_cloud = []

        for line in data:
            line_split = line.strip().split(' ')
            new_line = []
            for item in line_split:
                new_line.append(float(item))
            point_cloud.append(new_line)
        

        print(header)
        print(point_cloud[:10])

        
        axis = [1,0,0]
        axis = axis / norm(axis)
        print(axis)
        theta = math.pi/2
        rot = Rotation.from_rotvec(theta * axis)

        new_point_cloud = rot.apply(point_cloud)

        with open('rotated_pc.ply','w') as output_file:
            output_file.writelines(header)
            for line in new_point_cloud.tolist():
                print_line = ''
                for item in line:
                    print_line += "{:.5f}".format(item) + ' '
                print_line += '\n'
                output_file.write(print_line)
                
if __name__ == '__main__':
    start = time.time()
    rotation_ply('snapshot_1616566593.1071548.ply')
    end = time.time()
    print("Transformation:", end - start)



'''
import numpy as np
import quaternion as quat
import math

v = [3,5,0]
axis = [0,0,1]
theta = math.pi()/2 # radian

vector = np.array([0.]+v)
rot_axis = np.array([0.]+axis)
axis_angle = (theta*0.5) * rot_axis / np.linalg.norm(rot_axis)

vec = quat.quaternion(*v)
qlog = quat.quaternion(*axis_angle)
q = np.exp(qlog)

v_prime = q * vec * np.conjugate(q)

v_prime_vec = v_prime.imag
print(v_prime_vec)
'''
