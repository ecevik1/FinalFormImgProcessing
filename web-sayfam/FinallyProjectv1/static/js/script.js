// This file contains JavaScript code for the web application, handling client-side interactions and functionality.

document.addEventListener("DOMContentLoaded", function() {
    const statusElement = document.getElementById("status");

    function fetchStatus() {
        fetch("/api/status")
            .then(response => response.json())
            .then(data => {
                updateStatus(data);
            })
            .catch(error => console.error("Error fetching status:", error));
    }

    function updateStatus(status) {
        statusElement.innerHTML = ""; // Clear previous status
        for (const [table, info] of Object.entries(status)) {
            const tableStatus = document.createElement("div");
            tableStatus.innerHTML = `${table}: ${info.occupied ? "Occupied" : "Available"} - People: ${info.people}`;
            statusElement.appendChild(tableStatus);
        }
    }

    setInterval(fetchStatus, 1000); // Fetch status every second
});