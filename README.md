<a href="https://www.uvg.edu.gt/"><img align="left" src="https://www.uvg.edu.gt/wp-content/uploads/socialshare-logo.jpg" width="90" height="90"></a>
**_Corporate Master in Applied Data Science_**<br/>
**_Text Mining & Natural Language Processing_**<br/>
**_Catedratico: Pedro Alberto Aguilar Nuñez_**<br/>
<br/>

Integrantes:
- Aldo Montenegro Margnoni
- Gabriel Fernando Montenero Ortiz
- Axel Adolfo Muralles Carranza
- German Antonio Oliva Muralles

# Tarea 2 Scrapping wikipedia / tokens vs vocabulario

- [Descripcion](#descripcion)
- [Requerimientos](#requerimientos)
- [Instrucciones](#instrucciones)
- [Estructura del archivo de salida](#estructura-del-archivo-de-salida)
- [Descripcion del contenido del sitio web](#descripcion-del-contenido-del-sitio-web)
- [Contribuciones](#contribuciones)
- [Jupyter Notebook](#jupyter-notebook)


## Descripcion:

La tarea consiste en dos partes, la primera es el scrapping del texto de varios articulos de Wikipedia (en nuestro caso 500) para obtener un corpus de texto,
y la segunda parte en se trata del procesamiento incremental de estos textos de articulos para obtener la relacion entre la cantidad de tokens y el vocabulario.
## Requerimientos:
- Requiere instalacion de [Anaconda Distribution](https://www.anaconda.com/products/distribution) o [miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Instrucciones:

clonamos este repositorio en el directorio deseado desde una terminal, para windows podemos utilizar [Git Bash](https://gitforwindows.org/) 
```
git clone https://github.com/Text-Mining-and-NLP-workspace/Scrapping-wikipedia-tokens-vs-vocabulario.git
```
Desde la terminal o anaconda prompt (windows) creamis un ambiente virtual con conda (reemplazar my_enviroment con el nombre deseado)
```
conda create -n my_enviroment
```
cuando conda pregunte por la confirmacion responder con _y_
```
proceed ([y]/n)?
```
una vez creado el ambiente virtual, proceder a activarlo
```
conda activate my_enviroment
```
instalamos scrapy en nuestro ambiente
```
conda install scrapy -c conda-forge
```
nos cambiamos hacia el path en donde se clono el repositorio
```
cd Tarea-2-Scrapping-wikipedia-tokens-vs-vocabulario
```
Primero obtenemos el texto de varios articulos de wikipedia, para esto ejecutamos el siguiente comando para iniciar la spider y comenzar el scrapping
```
scrapy crawl token_VS_vocabulary
```
como salida se creara el archivo **_token_VS_vocabulary.json_** en nuestro directorio de trabajo el cual se puede procesar ya sea con el script python graph.py
```
python graph.py
```
como salida obtenermos el archivo de imagen **_token_VS_vocabulary_plot.png_** con la grafica de token VS vocabulary y la grafica del modelo utilizando la Ley de Heaps.
de igual manera se puede utilizar el notebook de jupyter [**_Token VS Vocabulary.ipynb_**](#jupyter-notebook) para procesar el archivo json y obtener las graficas deseadas

## Estructura del archivo de salida

El archivo de salida del scrapping tiene formato **json**, y consta de una coleccion de llaves  **text:** las cuales contienen en su valor el texto de un articulo de wikipedia.
<br/>
```
{
	{'text':'Este es un texto de ejemplo'} 
	...
}
```
<br/>


## Descripcion del Contenido del sitio Web 

## Contribuciones

- Aldo Montenegro Margnoni
    - a
<br/>

- Gabriel Fernando Montenero Ortiz
    - b
    
<br/>

- Axel Adolfo Muralles Carranza
    - c

<br/>

- German Antonio Oliva Muralles
    - d
<br/>

## Jupyter Notebook


