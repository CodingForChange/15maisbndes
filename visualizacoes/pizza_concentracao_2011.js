function drawVisualization() {
// Create and populate the data table.
var data = google.visualization.arrayToDataTable([
  ['Empresa', 'Valores'],
  ['15 maiores', 32283876532],
  ['Outras 368', 33456792682]
]);

// Create and draw the visualization.
new google.visualization.PieChart(document.getElementById('pizza_concentracao_2011')).
    draw(data, {title:"Concentração de Investimentos do BNDES em 2011"});
}
google.setOnLoadCallback(drawVisualization);

