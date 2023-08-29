document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById('generateButton');
    const imageContainer = document.getElementById('imageContainer');
    let currentImage = null;  // Rappresenta l'elemento <img> corrente

    generateButton.addEventListener('click', function() {
        if (currentImage) {
            currentImage.remove();  // Rimuove l'immagine corrente se esiste
        }

        // Chiama l'API Python per generare l'immagine
        fetch('http://localhost:5000/generate_image')
            .then(response => response.json())
            .then(data => {
                const imageElement = document.createElement('img');
                imageElement.src = `data:image/png;base64,${data.image}`;
                imageContainer.appendChild(imageElement);
                currentImage = imageElement;  // Imposta l'immagine corrente
            });
    });
});
