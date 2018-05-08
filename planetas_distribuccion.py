import numpy as np
import matplotlib.pyplot  as plt

G= 6.674 *(10**-11)
masa_sol= 1.989*10**(30)

#r=posicion
#v=velocidad

r_mercurio= ([2.133679072387218e-01, -3.72731031176899e-01, -5.058864779204983e-03])
v_mercurio=[(1.892057222101034e-02, 1.5113838055059527e-02,-4.995475648824679e-04)]

r_tierra=[(-6.8577609665891080e-01, -7.327391341104329e-01, -6.644615610967885e-05)]
v_tierra=[(1.231562236067741e-02,-1.1773039883148583-02,1.210619824052227e-06)]

x_jupiter=[(-3.616450082845184e+00, -4.014244339308792e+00,9.754215806840760e-02 )]
v_jupiter=[(5.517283470150529e-03, -4.691963322519999e-03, -1.039452586609281e-04)]

mercurio=np.array ([r_mercurio,v_mercurio])
tierra=np.array([r_tierra,v_tierra])
jupiter=np.array([x_jupiter,v_jupiter])

#Valores de alpha entre 0 y 4
alpha=np.linspace (0.1,4,100)
print alpha

#Beta
beta= (v_mercurio**2)/(r_mercurio ** (1-alpha))
print beta

for i in range (1000):
    print i, beta (alpha)
    i=i+1

plt.figure()
plt.title('Distribucion Planetas')
plt.show()
plt.savefig('PropabilidadPlanetas.png')
