// Get data from Flask
const labels = portfolioData.map(stock => stock.ticker);
const values = portfolioData.map(stock => stock.current_value);

const buyPrices = portfolioData.map(stock => stock.buy_price);
const currentPrices = portfolioData.map(stock => stock.current_price);

// ---------------- PIE CHART ----------------

const pieCanvas = document.getElementById("portfolioChart");

if (pieCanvas) {

    new Chart(pieCanvas, {
        type: "pie",

        data: {
            labels: labels,

            datasets: [{
                data: values,

                backgroundColor: [
                    "#2563eb",
                    "#22c55e",
                    "#f59e0b",
                    "#ef4444",
                    "#8b5cf6",
                    "#06b6d4",
                    "#ec4899",
                    "#14b8a6"
                ]
            }]
        },

        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "right"
                }
            }
        }
    });

}

// ---------------- BAR CHART ----------------

const comparisonCanvas = document.getElementById("comparisonChart");

if (comparisonCanvas) {

    new Chart(comparisonCanvas, {

        type: "bar",

        data: {

            labels: labels,

            datasets: [

                {
                    label: "Buy Price",

                    data: buyPrices,

                    backgroundColor: "#2563eb"
                },

                {
                    label: "Current Price",

                    data: currentPrices,

                    backgroundColor: "#22c55e"
                }

            ]
        },

        options: {

            responsive: true,

            scales: {
                y: {
                    beginAtZero: true
                }
            },

            plugins: {

                legend: {

                    position: "top"

                }

            }

        }

    });

}