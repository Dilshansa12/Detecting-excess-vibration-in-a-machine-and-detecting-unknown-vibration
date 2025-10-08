import numpy as np
import matplotlib.pyplot as plt


#non error values
Val_no_E = np.array([
    
[135,72,235],	
[98,74,233],	
[161,83,241],	
[42,101,232],	
[31,171,238],	
[143,143,246],	
[158,89,238],	
[58,176,241],	
[97,77,230],	
[124,155,245],	
[29,122,236],	
[160,120,241],	
[118,74,234],	
[22,120,232],	
[16,140,235],	
[91,172,244],	
[21,136,236],	
[155,125,241],	
[25,124,235],	
[42,106,233],	
[142,143,245],	



])



Ax=np.array([x[0] for x in Val_no_E])
Ay=np.array([x[1] for x in Val_no_E])
Az=np.array([x[2] for x in Val_no_E])
num=np.array([x for x in range(0,len(Val_no_E))])








#valueas withe error
Val_E=np.array([
[70,81,219],	
[86,170,24],	
[173,98,253],	
[92,79,214],	
[80,178,247],	
[160,109,17],	
[11,124,234],	
[42,177,254],	
[155,73,245],	
[57,85,229],	
[109,171,242],	
[174,96,238],	
[82,85,208],	
[125,163,250],	
[153,71,233],	
[52,181,245],	
[181,102,238],	
[14,165,235],	
[134,149,4],	
[29,101,232],	
[50,179,226],	



])

AxE=np.array([x[0] for x in Val_E])
AyE=np.array([x[1] for x in Val_E])
AzE=np.array([x[2] for x in Val_E])


#no 1 plot
plt.subplot(1, 3, 1)
plt.plot(num,Ax)
plt.plot(num,AxE)
plt.title("X-axix")
plt.axhline( 160, color='black',linestyle='dashed')#you can change your maximum vibration unit value from here and recognize excess vibrations to x direction
plt.axhline( 25, color='black',linestyle='dashed')#you can change your minimum vibration unit value from here and recognize excess vibrations to x direction

#no 2 plot
plt.subplot(1, 3, 2)
plt.plot(num,Ay)
plt.plot(num,AyE)
plt.title("Y-axix")
plt.axhline( 160, color='black',linestyle='dashed')#you can change your maximum vibration unit value from here and recognize excess vibrations to y direction
plt.axhline( 80, color='black',linestyle='dashed')#you can change your minimum vibration unit value from here and recognize excess vibrations to y direction

#no 3 plot
plt.subplot(1, 3, 3)
plt.plot(num,Az)
plt.plot(num,AzE)
plt.title("Z-axix")
plt.axhline( 250, color='black',linestyle='dashed')#you can change your maximum vibration unit value from here and recognize excess vibrations to z direction
plt.axhline( 230, color='black',linestyle='dashed')#you can change your minimum vibration unit value from here and recognize excess vibrations to z direction

plt.show()
