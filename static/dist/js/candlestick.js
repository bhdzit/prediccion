let chart = null;
function getDataPointsFromCSV(csv) {
  if (chart!=null) {
    chart.destroy();
  }

  var dataPoints = [];
  CanvasJS.addColorSet("greenShades", [
    //colorSet Array

    "#ff0000",
  ]);

  chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    theme: "light2", // "light1", "light2", "dark1", "dark2"
    exportEnabled: false,
    title: {
      text: "Datos Historicos",
    },

    axisX: {
      interval: 1,
      valueFormatString: "MMM",
    },
    axisY: {
      prefix: "$",
      title: "Price",
    },
    toolTip: {
      content:
        "Date: {x}<br /><strong>Price:</strong><br />Open: {y[0]}, Close: {y[3]}<br />High: {y[1]}, Low: {y[2]}",
    },
    colorSet: "greenShades",
    data: [
      {
        risingColor: "green",
        type: "candlestick",
        yValueFormatString: "$##0.00",
        dataPoints: dataPoints,
      },
    ],
  });


  for (let points of csv) {
    dataPoints.push({
      x: new Date(
        parseInt(points.fecha.split("/")[2]),
        parseInt(points.fecha.split("/")[0]),
        parseInt(points.fecha.split("/")[1])
      ),
      y: [
        parseFloat(points.open),
        parseFloat(points.high),
        parseFloat(points.low),
        parseFloat(points.close),
      ],
    });
  }
  chart.render();
}
