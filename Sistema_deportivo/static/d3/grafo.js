
        var nodes = new vis.DataSet([{'id': 1, 'label': 'punto de encuentro'}, {'id': 2, 'label': 'sintetica Podocarpus'}, {'id': 3, 'label': 'calva y calva'}, {'id': 4, 'label': 'Jogo Bonito'}]);
        var edges = new vis.DataSet([{'from': 1, 'to': 2, 'label': '0.40 km', 'length': 396.2261227836101}, {'from': 1, 'to': 3, 'label': '0.58 km', 'length': 580.0603024099096}, {'from': 1, 'to': 4, 'label': '1.10 km', 'length': 1100.610101037558}, {'from': 2, 'to': 3, 'label': '0.21 km', 'length': 209.45579769968478}, {'from': 2, 'to': 4, 'label': '1.35 km', 'length': 1354.2701760311518}, {'from': 3, 'to': 4, 'label': '1.41 km', 'length': 1410.6168645649238}]);
        var container = document.getElementById("mynetwork");
        var data = { nodes: nodes, edges: edges };
        var options = {};
        var network = new vis.Network(container, data, options);
        