"""

@author: adriana alonso custodio
"""

import pandas as pd
datos =        [["Miguel",25],
                ["Andres",26],
                ["Luis",24],
                ["Adrian",21],
                ["Jesus", 25],
                ["Alicia", 24],
                ["Jose", 26],
                ["Fernanda", 28],
                ["Ana", 23],
                ["Henry",20]]
columnas =['Alumno','Edad']
df = pd.DataFrame(datos,columns=columnas,)
porprom = df.sort_values('Edad',ascending=False)                                                                       
porprom.head()
arx = porprom.iloc[0,:]
print ("La lista ingresada es la siguiente:")
print (df)
print()
print("El alumno con mayor edad es:")
print(arx)