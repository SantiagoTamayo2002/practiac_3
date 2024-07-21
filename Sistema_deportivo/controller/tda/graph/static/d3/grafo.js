var nodes = new vis.DataSet([
{id: 1, label: "1 Alas Bielas"},
{id: 2, label: "2 La chucheria"},
{id: 3, label: "3 Los Foraneos"},
{id: 4, label: "4 EL placer"}
]);

var edges = new vis.DataSet([
{from: 2, to: 3, label: "0.3374145787651516 km"},
{from: 3, to: 2, label: "0.3374145787651516 km"}
]);

var container = document.getElementById("mynetwork");
var data = {nodes: nodes, edges: edges};
var options = {};
var network = new vis.Network(container, data, options);
