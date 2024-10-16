> En esta unidad pueden encontrar un archivo con mediciones de temperatura durante dos meses.
> 
> El objetivo es analizar la información y comparar la temperatura media de Agosto vs Septiembre. Hacer el análisis primero con los datos actuales, luego aplicar las técnicas de limpieza que crean convenientes y volver a hacer el análisis. Compartirme luego por correo o en comentarios vuestros resultados.

## Corrección:
### Duplicidad
* Líneas 11 y 12 están duplicadas, elimino una.
* Líneas 23 y 24 están duplicadas, elimino una.

### Outliers
* Línea 13 tiene un valor de 0, esto es muy raro teniendo en cuenta los datos de su entorno, debe deberse a un error en los sensores.
* Línea 54 tiene un valor de 59, esto es muy raro teniendo en cuenta los datos de su entorno, debe deberse a un error en los sensores.

Para corregir esto voy a hacer recoger el promedio de sus datos vecinos :
* En el primero voy a coger el valor del vecino superior e inferior $(30×2)/2 = 30$.
* En el segundo voy a coger el valor del vecino superior e inferior $(20+18)/2 = 19$.

### Reconstrucción
* Entre las líneas 29 y 30 falta una medición.
* Entre las líneas 59 y 60 faltan dos mediciones.

Para corregir esto voy a hacer recoger el promedio de sus datos vecinos:
 * En el primer caso voy a coger el valor del vecino superior e inferior $(23+24)/2 = 23.5$ y lo voy a redondear al entero más próximo al encontrarse todos los datos como enteros *24*.
* En el segundo caso voy a coger el valor de sus dos vecinos superiores y el del inferior al ser dos filas en lugar de una $(15×3+14)/4 = 14.75$ y lo voy a redondear al entero más próximo al encontrarse todos los datos como enteros *15*.

### Resultado
En el fichero [Original](Ej_Limp.xlsx) La media del mes 8 es: 24.4375
En el fichero [Original](Ej_Limp.xlsx) La media del mes 9 es: 24.607142857142858

En el fichero [Actualizado](Ej_Limp_Actualizado.xlsx) La media del mes 8 es: 25.161290322580644
En el fichero [Actualizado](Ej_Limp_Actualizado.xlsx) La media del mes 9 es: 22.63333333333333

Como podemos observar la limpieza de datos que he realizado ha provocado un cambio de $|24.4375 - 25.161290322580644| = 0.723790323$ grados en el mes de Agosto y de $|24.607142857142858 − 22.63333333333333| = 1.973809524$ grados en el mes de Septiembre.

En el mes de Agosto la medición no se visto tan afectada ya que la medición que faltaba estaba muy cerca de la media y aunque hayamos eliminado dos datos con valor superior esta hemos añadido otro que se corresponde con el valor máximo (De hecho es por esto que el resultado final es mayor que el original).

Por otra parte en el mes de Septiembre notamos una diferencia bastante más brusca principalmente porque hemos modificado un dato outlier con un valor del doble del máximo de la población dejándolo finalmente con un valor de 5 grados menos que la media original, lo cual se ha visto reforzado al introducir un dato nuevo con un valor inferior a la media.