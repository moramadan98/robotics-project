# -*- coding: utf-8 -*-
"""Copy of new_IK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G1qIdIXGSLW45qfr_Er_fQqmqZT0W_10
"""

#getting input DOF and DH parameter
import numpy as np
import sympy
#from pyrsistent import T

joint1_k = input("Enter kind of joint 1 ")
joint2_k = input("Enter kind of joint 2 ")

dict={0:'a',1:'alpha',2:'d',3:'theta'}
DH  = np.zeros( (2, 4) )
for i in range(2):
  for j in range(4):
    if(((joint1_k == 'R' and i==0) or (joint2_k == 'R' and i==1)) and j==3):
      continue
    elif (((joint1_k == 'P' and i==0) or (joint2_k == 'P' and i==1)) and j==2):
      continue
    else:
      DH[i][j]=float(input("Enter DH parameter for joint " +str(i) +" parameter "+dict[j]+' :'))
Xe = float(input("Enter x of end effector: "))
Ye = float(input("Enter y of end effector: "))
Ze=  float(input("Enter z of end effector: "))

1#display DOF and DH parameter
def disply_DH_parameter():
  #print('degree of fredom DOF: '+str(DOF))
  for i in range(2):
    for j in range(4):
      print("DH parameter for joint " +str(i) +" parameter "+dict[j]+': '+str(DH[i][j]))

disply_DH_parameter()

Xe,Ye,Ze

if(joint1_k == 'R'):
  var1='theta1'
else:
  var1='d1'
if(joint2_k == 'R'):
  var2='theta2'
else:
  var2='d2'

var1,var2

from sympy.solvers import solve
from sympy import Symbol
from sympy import *
from sympy import symbols, Eq, solve

#2 revolute joints   2D geometry
def get_ik_RR(x,y):
  D = (((x)**2)+((y)**2)-((DH[0][0])**2) -((DH[1][0])**2))/(2*(DH[0][0])*(DH[1][0]))
  point1_var2 = math.degrees(math.atan((math.sqrt(1-(D)**2))/ D))
  point2_var2 = math.degrees(math.atan((-math.sqrt(1-D**2))/ D))
  point1_var1 = (math.degrees(math.atan(y/x))) - math.degrees(math.atan((DH[1][0]*math.floor(math.sin(math.radians(point1_var2))))/(DH[0][0] +DH[1][0]*math.floor(math.cosh(math.radians(point1_var2))) )))
  point2_var1 = (math.degrees(math.atan(y/x))) - math.degrees(math.atan((DH[1][0]*math.floor(math.sin(math.radians(point2_var2))))/(DH[0][0] +DH[1][0]*math.floor(math.cosh(math.radians(point2_var2)))) ))
  return point1_var1,point2_var1,point1_var2,point2_var2

#theta1_v1 ,theta1_v2, theta2_v1 ,theta2_v2 = get_ik_RR()
#print("first value of theta1: "+str(theta1_v1)+" second value of theta1: "+str(theta1_v2)+"first value of theta2: "+str(theta2_v1)+" second value of theta2: "+str(theta2_v2))

# 2 prismatic joints 3d
import math
def get_ik_PP():
  b1 = math.floor(math.sin(math.radians(DH[0][3])))*math.floor(math.sin(math.radians(DH[0][1])))   # d2
  const1 = Xe - ((math.floor(math.cos(math.radians(DH[0][3])))*DH[1][0]*math.floor(math.cos(math.radians(DH[1][3]))))+(-math.floor(math.sin(math.radians(DH[0][3])))*math.floor(math.sin(math.radians(DH[1][3])))*math.floor(math.cos(math.radians(DH[0][1])))*DH[1][0])+(DH[0][0]*math.floor(math.cos(math.radians(DH[0][3])))))

  b2 = - math.floor(math.cos(math.radians(DH[0][3]))) * math.floor(math.sin(math.radians(DH[0][1])))  #d2
  const2 = Ye - ((math.floor(math.sin(math.radians(DH[0][3])))*math.floor(math.cos(math.radians(DH[1][3])))*DH[1][1])+(math.floor(math.cos(math.radians(DH[0][3])))*math.floor(math.cos(math.radians(DH[0][1])))*math.floor(math.sin(math.radians(DH[1][3])))*DH[1][0])+(DH[0][0]*math.floor(math.sin(math.radians(DH[0][3])))))

  a3 = 1  #d1
  b3 = math.floor(math.cos(math.radians(DH[0][1])))
  const3 = Ze - (math.floor(math.sin(math.radians(DH[0][1])))*math.floor(math.sin(math.radians(DH[1][3])))*DH[1][0])

  d2 = const1/b1
  #d = const2/b2
  d1 = (const3 - b3*d2)/a3
  return d2,d1

##################################################################################################
#trajectory
ti = [0.0 , math.pi/8 , math.pi/4]
x=[]
y=[]
x_dif = []
y_dif = []
theta1_v1 =[]
theta1_v2 = []
theta2_v1 = []
theta2_v2 = []
# z =600 
for i in ti:
  xi = 2+0.5* math.cos(i)
  xi_dif = -0.5 * math.sin(i)
  x.append(xi)
  yi = 1+0.5 *math.sin(i)
  yi_dif =0.5* math.cos(i)
  y.append(yi)
  x_dif.append(xi_dif)
  y_dif.append(yi_dif)

for j in range(len(x)):
  th1_v1 ,th1_v2, th2_v1 ,th2_v2 = get_ik_RR(x[j],y[j])
  theta1_v1.append(th1_v1)
  theta1_v2.append(th1_v2)
  theta2_v1.append(th2_v1)
  theta2_v2.append(th2_v2)
  
q1= np.array((2,1))
q1[1][1] = theta1_v1[0]
q1[2][1] = theta2_v1[0]

q2= np.array((2,1))
q2[1][1] = theta1_v1[1]
q2[2][1] = theta2_v1[1]

q3= np.array((2,1))
q3[1][1] = theta1_v1[2]
q3[2][1] = theta2_v1[2]

 

dh_1 = np.concatenate(DH,q1)
dh_2 = np.concatenate(DH,q2)
dh_3 = np.concatenate(DH,q3)



print("-------------------------------------------------")
print(x)
print("-------------------------------------------------")
print(y)
print("-------------------------------------------------")
print(theta1_v1)
print("-------------------------------------------------")
print(theta2_v1)
print("-------------------------------------------------")
print(theta1_v2)
print("-------------------------------------------------")
print(theta2_v2)
print("-------------------------------------------------")
print(x_dif)
print("-------------------------------------------------")
print(y_dif)

