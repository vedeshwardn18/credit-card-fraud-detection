const API_URL = "http://127.0.0.1:5000";

let fraudChart = null;
let trendChart = null;

async function loadStats() {

    const response =
        await fetch(`${API_URL}/stats`);

    const data =
        await response.json();

    document.getElementById(
        "totalTransactions"
    ).innerText =
        data.total_transactions;

    document.getElementById(
        "totalFraud"
    ).innerText =
        data.total_fraud;

    document.getElementById(
        "fraudRate"
    ).innerText =
        data.fraud_rate + "%";

    const legitimate =
        data.total_transactions -
        data.total_fraud;

    updateFraudChart(
        legitimate,
        data.total_fraud
    );
}

function updateFraudChart(
    legitimate,
    fraud
) {

    const ctx =
        document.getElementById(
            "fraudChart"
        );

    if (fraudChart) {
        fraudChart.destroy();
    }

    fraudChart = new Chart(
        ctx,
        {
            type: "pie",
            data: {
                labels: [
                    "Legitimate",
                    "Fraud"
                ],
                datasets: [{
                    data: [
                        legitimate,
                        fraud
                    ]
                }]
            }
        }
    );
}

async function loadTransactions() {

    const response =
        await fetch(
            `${API_URL}/transactions`
        );

    const data =
        await response.json();

    let rows = "";

    const labels = [];
    const amounts = [];

    data.reverse().forEach(tx => {

        labels.push(tx.id);
        amounts.push(tx.amount);

        const badge =
            tx.prediction === "Fraud"
            ? '<span class="fraud-badge">Fraud</span>'
            : '<span class="safe-badge">Legitimate</span>';

        rows += `
            <tr>
                <td>${tx.id}</td>
                <td>${tx.amount}</td>
                <td>${badge}</td>
                <td>${tx.created_at}</td>
            </tr>
        `;
    });

    document.getElementById(
        "transactionTable"
    ).innerHTML = rows;

    updateTrendChart(
        labels,
        amounts
    );
}

function updateTrendChart(
    labels,
    amounts
) {

    const ctx =
        document.getElementById(
            "trendChart"
        );

    if (trendChart) {
        trendChart.destroy();
    }

    trendChart = new Chart(
        ctx,
        {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Transaction Amount",
                    data: amounts,
                    tension: 0.3
                }]
            }
        }
    );
}

async function loadAlerts() {

    const response =
        await fetch(
            `${API_URL}/alerts`
        );

    const data =
        await response.json();

    let alerts = "";

    data.forEach(alert => {

        alerts += `
            <div class="alert">
                Fraud Transaction:
                Rs. ${alert.amount}
                (${alert.created_at})
            </div>
        `;
    });

    document.getElementById(
        "alerts"
    ).innerHTML = alerts;
}

async function loadDashboard() {

    await loadStats();
    await loadTransactions();
    await loadAlerts();
}

loadDashboard();

setInterval(() => {
    loadDashboard();
}, 5000);