function updateTables() {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            for (let id in data) {
                let table = document.getElementById(`Table${id.replace(' ', '')}`);
                if (table) {
                    // Doluysa "occupied", değilse "empty"
                    table.classList.toggle('occupied', data[id].occupied);
                    table.classList.toggle('empty', !data[id].occupied);

                    // Kişi sayısı güncelle (opsiyonel alan)
                    table.querySelector('.people-count').textContent = `Kişi Sayısı: ${data[id].people}`;
                }
            }
        })
        .catch(error => console.error('Veri alınamadı:', error));
}

// Sayfa yüklendikçe her 1 saniyede bir güncelle
setInterval(updateTables, 1000);
