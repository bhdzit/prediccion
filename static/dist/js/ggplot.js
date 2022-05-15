let ggplot = null;
function dibujarPredicion(csv) {
  let labels = csv.map(function (item) {
    let fecha = ("" + item.fecha).split("/");
    return fecha[1] + "/" + fecha[0] + "/" + fecha[2];
  });

  let y = csv.map(function (item) {
    return item.y;
  });

  const genericOptions = {
    fill: false,
    interaction: {
      intersect: false,
    },
    radius: 0,
  };

  const skipped = (ctx, value) =>
    ctx.p0.skip || ctx.p1.skip ? value : undefined;
  const down = (ctx, value) =>
    ctx.p0.parsed.y > ctx.p1.parsed.y ? value : undefined;

  if (ggplot != null) {
    ggplot.destroy();
  }

  ggplot = new Chart(document.getElementById("myChart"), {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Precio",
          data: y,
          borderColor: "rgb(75, 192, 192)",
          segment: {
            borderColor: (ctx) =>
              skipped(ctx, "rgb(0,0,0,0.2)") || down(ctx, "rgb(192,75,75)"),
            borderDash: (ctx) => skipped(ctx, [6, 6]),
          },
          spanGaps: true,
        },
      ],
    },
    options: genericOptions,
  });
}
