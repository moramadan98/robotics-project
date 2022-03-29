# robotics-project
## calculate the FK, IK, FJ, IJ, and trajectory planning for any serial manipulator


### FK
calculate forward kinematic for any number of joints by :
-  getting no of joints from user
-  loop for each joint to get DH Parameter
-  pase no of joints and DH Parameter to **get_fk() function** return a metrix of A for each joint
-  after calculate all A matrix for each joint **get_final_fk() function** return final A matrix of end effector
-
