from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.liquido.negocioDaoControl import NegocioDaoControl
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from models.negocioGrafo import NegocioGrafo
from controls.tda.graph.recorridos.dikstra import Dijkstra
from controls.tda.graph.recorridos.floyd import Floyd
from flask_cors import CORS
router = Blueprint('router', __name__)

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/')
def home():
    pd = NegocioDaoControl()
    list = pd._lista
    if not list.isEmpty:
        list.sort_models('_nombre') #uso el método de busqueda de la lista para buscar por nombre
    return render_template('liquido/lista.html', lista=pd.to_dict_lista())

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/formulario')
def ver_negocio_guardar():
    return render_template('liquido/guardar.html')

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/grafo_negocio')
def grafo_negocio():
    negocio = NegocioDaoControl()
    list = negocio._lista
    if not list.isEmpty:
        list.sort_models('_nombre') 
    ng = NegocioGrafo()
    ng.get_graph
    return render_template('liquido/grafo.html' , negocios=negocio.to_dict_lista())

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/buscar-camino-corto', methods=['POST'])
def buscar_camino_corto():
    negociograph = NegocioGrafo()
    data = request.form
    search = Dijkstra(negociograph.get_graph, int(data['origen']), int(data['destino']))
    recorrido = search.__printPath__()
    return render_template('liquido/recorrido.html')

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/grafo_ver_admin')
def grafo_ver_admin():
    negocio = NegocioDaoControl()
    negociograph = NegocioGrafo()  
    negociograph.get_graph
    list = negocio._lista
    if not list.isEmpty:
        list.sort_models('_nombre')    
    return render_template('liquido/adyacencias.html', negocios=negocio.to_dict_lista(), 
                            grafonegocio=negociograph.obtainWeigths)

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/grafo_negocio/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    print(data)
    ng = NegocioGrafo()
    ng.get_graph.insert_edges(int(data['origen'])-1, int(data['destino'])-1)
    ng.save_graph
    return redirect('/negocio/grafo_ver_admin', code=302)

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////

@router.route('/negocio/guardar', methods=['POST'])
def negocio_guardar():
    negocio = NegocioDaoControl()
    data = request.form
    print(data)
    negocio._negocio._nombre = data['nombre']
    negocio._negocio._direccion = data['direccion']
    negocio._negocio._horario = data['horario']
    negocio._negocio._longitud = float(data['longitud'])
    negocio._negocio._latitud = float(data['latitud'])
    negocio.save
    return jsonify({"message": "Negocio guardado correctamente"})

#///////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////////////////////////////////////////




