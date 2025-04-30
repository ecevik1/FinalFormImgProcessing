function updateTables() {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            const statusData = data.status;

            for (let id in statusData) {
                // ID'deki boşluğu kaldırarak eşleşme sağla
                let elementId = id.replace(/\s/g, ''); // Örn: "Table 11" → "Table11"
                let table = document.getElementById(elementId);

                if (table) {
                    // Tüm durumları sıfırla
                    table.classList.remove('occupied', 'empty', 'object-only');

                    // Duruma göre stil uygula
                    const state = statusData[id].status;
                    if (state === 'occupied') {
                        table.classList.add('occupied');
                        table.style.backgroundColor = 'red';
                        table.style.color = 'white';
                    } else if (state === 'object_only') {
                        table.classList.add('object-only');
                        table.style.backgroundColor = 'yellow';
                        table.style.color = 'black';
                    } else {
                        table.classList.add('empty');
                        table.style.backgroundColor = 'green';
                        table.style.color = 'white';
                    }

                    // Kişi sayısını güncelle
                    const countElem = table.querySelector('.people-count');
                    if (countElem) {
                        countElem.textContent = `Kişi Sayısı: ${statusData[id].people}`;
                    }
                }
            }

            // Zaman bilgisini güncelle
            const timeElement = document.getElementById("video-time");
            if (timeElement) {
                timeElement.textContent = `Zaman: ${data.time}s`;
            }

            // Canlı görüntü güncelle
            const img = document.getElementById("live-frame");
            if (img && data.frame) {
                img.src = "data:image/jpeg;base64," + data.frame;
            }
        })
        .catch(error => console.error('Veri alınamadı:', error));
}

// Her saniyede bir güncelle
setInterval(updateTables, 1000);
