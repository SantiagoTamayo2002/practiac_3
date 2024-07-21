from flask import Blueprint, flash, jsonify, abort, request, render_template, redirect, url_for 
from controller.canchaDaoControl import CanchaDaoControl
from flask_cors import CORS

from controller.negocioGrafoControl import NegocioGrafo
router = Blueprint('router', __name__)


#////////////////////////////////////////////////////////////////////////////////////////

@router.route('/')
def home():
    return render_template("template.html")

#////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////
#lista de canchas
@router.route('/negocios')
def lista_canchas():
    ndc = CanchaDaoControl()
    list = ndc._list()
    return render_template("negocio/lista.html", lista= ndc.to_dic_lista(list))

#////////////////////////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////
#Guardar cancha gracias al DAOcontrol
@router.route('/negocios/ver')
def ver_guardar():
    return render_template("negocio/guardar.html")\

#////////////////////////////////////////////////////////////////////////////////////////7

#////////////////////////////////////////////////////////////////////////////////////////7
#editar canchas gracias al DAOcontrol y las posición
@router.route('/negocio/editar/<pos>')
def ver_editar(pos):
    pd = CanchaDaoControl()
    nene = pd._get(int(pos))
    return render_template("negocio/editar.html", data = nene)

#////////////////////////////////////////////////////////////////////////////////////////7

#////////////////////////////////////////////////////////////////////////////////////////7
#guardar negocio
@router.route('/negocio/guardar', methods=["POST"])
def guardar_negocios():
    ndc = CanchaDaoControl()
    data = request.form
    if not "nombre" in data.keys():
        abort(400)
    ndc._negocio._nombre = data["nombre"]
    ndc._negocio._direccion = data["direccion"]
    ndc._negocio._precio = data["precio"]
    ndc._negocio._lng = data["longitud"]
    ndc._negocio._lat = data["latitud"]
    ndc.save
    return redirect("/negocios", code=302)


@router.route('/negocio/eliminar', methods=["POST"])
def eliminar_cancha():
    ndc = CanchaDaoControl()
    pos = request.form["id"]
    ndc._delete(int(pos) - 1)
    return redirect("/negocios", code=302)


@router.route('/grafo')
def grafo():
    return render_template("d3/grafo.html")


#///////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/grafo_negocio')
def grafo_negocio():
    nc = NegocioGrafo()
    nc.create_graph()
    return render_template("d3/grafo.html")

#///////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////
@router.route('/negocio/grafo_admin')
def grafo_admin():
    ndc = CanchaDaoControl()
    list = ndc._list()
    if not list.isEmpty:
        list.sort_models('_nombre', 2)
    canchas = list.toArray
    distancias = calcular_distancias(canchas)
    return render_template("negocio/grafo.html", lista = canchas, distancias = distancias)
#///////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////

def calcular_distancias(negocios):
    distancias = []
    for i in range(len(negocios)):
        fila = []
        for j in range(len(negocios)):
            if i == j:
                fila.append(None)
            else:
                lat1, lon1 = float(negocios[i]._lat), float(negocios[i]._lng)
                lat2, lon2 = float(negocios[j]._lat), float(negocios[j]._lng)
                distancia = NegocioGrafo.haversine(lat1, lon1, lat2, lon2)
                fila.append(distancia)
        distancias.append(fila)
    return distancias

#///////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocios/crear_ady', methods=["POST"])
def crear_ady():
    nc = CanchaDaoControl()
    data = request.form
    origen_id = int(data["origen"])
    destino_id = int(data["destino"])
    if origen_id == destino_id:
        flash('Por favor, seleccione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_admin'))
    negocioOrigen = nc._list().binary_search_models(origen_id, "_id")
    negocioDestino = nc._list().binary_search_models(destino_id, "_id")
    if negocioOrigen and negocioDestino:
        ng = NegocioGrafo()
        distancia = ng.create_graph(negocioOrigen, negocioDestino) 
        flash(f'Adyacencia creada correctamente con una distancia de {distancia:.2f} km', 'success')
    else:
        flash('Error al encontrar los negocios seleccionados', 'error')
    return redirect(url_for('router.grafo_admin'))
