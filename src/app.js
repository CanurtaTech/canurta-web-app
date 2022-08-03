d3.csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",
    function(err, rows) {
        function unpack(rows, key) {
            return rows.map(function(row) {
                return row[key];
            });
        }

        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: "AAPL High",
            x: unpack(rows, "Date"),
            y: unpack(rows, "AAPL.High"),
            line: { color: "#17BECF" },
        };

        var trace2 = {
            type: "scatter",
            mode: "lines",
            name: "AAPL Low",
            x: unpack(rows, "Date"),
            y: unpack(rows, "AAPL.Low"),
            line: { color: "#7F7F7F" },
        };

        var data = [trace1, trace2];

        var layout = {
            title: "Basic Time Series",
        };

        Plotly.newPlot("myDiv", data, layout);
    }
);


var trace1 = {
    type: "bar",
    x: [1, 2, 3, 4],
    y: [5, 10, 2, 8],
    marker: {
        color: "#C8A2C8",
        line: {
            width: 2.5,
        },
    },
};

var data = [trace1];

var layout = {
    title: "Responsive to window's size!",
    font: { size: 18 },
};

var config = { responsive: true };

Plotly.newPlot("myDiv1", data, layout, config);