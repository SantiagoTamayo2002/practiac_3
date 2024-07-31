var nodes = new vis.DataSet([
{id:0, label: "sintetica Podocarpus"},
{id:1, label: "punto de encuentro"},
{id:2, label: "calva y calva"},
{id:3, label: "Jogo Bonito"},
{id:4, label: "sinteticazo"},
{id:5, label: "Canchas Bernardo"},
{id:6, label: "Canchas los Geraneos"},
{id:7, label: "Estadio UNL"},
{id:8, label: "Sintetica Obrapia"},
{id:9, label: "cancha zarzas"}]);

 var edges = new vis.DataSet([{
from: 0, to: 2, label: "2.32"},{
from: 0, to: 1, label: "0.65"},{
from: 0, to: 8, label: "2.14"},{
from: 0, to: 4, label: "3.44"},{
from: 1, to: 0, label: "0.65"},{
from: 1, to: 2, label: "1.68"},{
from: 1, to: 7, label: "2.96"},{
from: 2, to: 0, label: "2.32"},{
from: 2, to: 1, label: "1.68"},{
from: 2, to: 3, label: "1.15"},{
from: 2, to: 9, label: "1.9"},{
from: 3, to: 2, label: "1.15"},{
from: 3, to: 5, label: "1.98"},{
from: 4, to: 0, label: "3.44"},{
from: 4, to: 8, label: "4.3"},{
from: 5, to: 3, label: "1.98"},{
from: 6, to: 7, label: "2.88"},{
from: 7, to: 1, label: "2.96"},{
from: 7, to: 6, label: "2.88"},{
from: 8, to: 0, label: "2.14"},{
from: 8, to: 4, label: "4.3"},{
from: 9, to: 2, label: "1.9"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);