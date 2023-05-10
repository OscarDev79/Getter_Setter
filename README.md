Ya que en Python no existe como tal los Getter y Setter.
Pero a partir de la version 3.10  tenemos el decorador @Property 
el cual le indica a Python que el metodo debe ser tratado como un atributo de solo lectura
de esta manera podemos  tener un Getter en nuestro codigo Python
Para tener nuestro Setter implementamos un decorador con el mismo nombre que el metodo de lectura
