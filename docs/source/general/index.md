### General information

En FFMT existen # variables que son la base de las bases de datos y fungen como containers dependiendo del proposito que se le quiera dar.
Estas son:

#### For data analisis and interpretation
- mt: (struct) MT structure donde se almacenan las funciones de transferencia

#### For processing
In nEMesis, there is a straightforward hierarchy: tasks > jobs > ts. Each task will contain a certain number of "jobs." nEMesis is designed so that each job covers a specific portion of the MT spectrum. Depending on the instrument used, one or more sampling frequencies are utilized, and these are stored separately in different files. Each job may contain 1 (single-site) or more (multi-site) stations. Dependiendo del numero de estaciones dera el tamanio de la matriz MT X.
- task: (struct) estructura que contiene informacion sobre el task a procesarse
- job: (Struct) estructursa que contienen los parametros de procesamiento
- ts: (struct) esctructura que contiene la informacion de las series de tiempo de cada una de las estaciones

#### For modeling
In MT2ModEM utilizamos la variable model que contiene la geometria del modelo. Esta estructura consta de varias 
