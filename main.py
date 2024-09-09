from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
import pandas as pd

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    principal= """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Movies</title>
    <style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </style>
</head>
<style>

  body{
    background-color:yellow
  }

</style>
<body>
  <h1>Hola Mundo!!!</h1>
  <h6>En este espacio lo voy a rellenar con cosas... cuales no se aun</h6>
  <p>
  credula postero dolo asit quasi men parabellum nome nomelorem ipsum dolo asit quasi men parabellum nome nome deje quan mininum credula postero dolo asit quasi men parabellum nome nome deje
  asit quasi men parabellum nome nome deje lorem ipsum dolo asit quasi men parabellum nome nome deje quan mininum credula postero dolo asit quasi men parabellum nome nome deje
  lorem ipsum dolo asit quasi men parabellum men parabellum nome nome deje quan mininum credula postero dolo a parabellum nome nome deje
  lorem ipsum dolo asit quasi men parabellum nome nome deje quan mininum credula postero dolo asit quasi men parabellum nome nome deje</p>
  men parabellum nome nome deje quan mininum credula postero dolo alorem ipsum dolo asit quasi men parabellum nome nome deje quan mininum credula postero dolo asit quasi men parabellum nome nome deje
  lorem ipsum dolo asit quasi men parabellum nome nome deje quan mininum credula postero dolo asit quasi men parabellum nome nome deje
   dolo asit quasi men parabellum nome nome deje dolo asit quasi men parabellum nome nome deje dolo asit quasi men parabellum nome nome deje
  <div class=""><a href="https://pi1-mlops-vv02.onrender.com/docs" target="_blank"> #SoyHenry </a></div>
  <br>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>


        """    
    return principal

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    """esta funcion debe devolver la cantidad de peliculas estrenadas en determinado mes"""
    peliculas = pd.read_parquet("consultas/movies.parquet")
    mes_input = mes.capitalize()
    cant = peliculas['mes'].value_counts()[mes_input]
    return f"en el mes de {mes_input} fueron estrenadas {int(cant)} películas"


@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    """esta funcion debe devolver la cantidad de peliculas estrenadas en determinado dia"""
    peliculas = pd.read_parquet("consultas/movies.parquet")
    dia_input = dia.capitalize()
    cant = peliculas['dia_semana'].value_counts()[dia_input]
    return f"Los dias {dia_input} se estrenaron {int(cant)} películas"


@app.get('/score_titulo/{titulo}')
def score_titulo(titulo: str):
    peliculas = pd.read_parquet("consultas/movies.parquet")
    titulo_input = titulo.lower()
    busqueda = peliculas[peliculas['title'].str.lower()==titulo_input]
    if busqueda.empty:
        def busquedas_anidadas(lista):
            return ', '.join(map(str,lista))
        posible_busqueda = peliculas[peliculas['title'].str.lower().str.contains(titulo_input)]
        coincidencias = int(posible_busqueda.shape[0])
        lista_titulos = list(posible_busqueda['title'])
        return f"tu busqueda obtuvo {coincidencias} coincidencias: {busquedas_anidadas(lista_titulos)}"
    titulo = str(busqueda['title'].values[0])
    anio = int(busqueda['anio'].values[0])
    score = float(busqueda['popularity'].values[0])
    return f" el titulo {titulo} se estreno el año {anio} y hasta el dia de hoy tiene un score de {score}"

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo: str):
    return None


@app.get('/nombre_actor/{actor}')
def nombre_actor(actor: str):
    return None

@app.get('/nombre_director/{director}')
def nombre_director(director: str):
    return None