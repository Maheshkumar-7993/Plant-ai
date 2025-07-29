const uploadBtn = document.getElementById('upload-btn');
const imageInput = document.getElementById('image-upload');
const progressBar = document.getElementById('progress-bar');
const progressContainer = document.getElementById('progress-container');
const uploadedImageContainer = document.getElementById('uploaded-image-container');
const uploadedImage = document.getElementById('uploaded-image');
const resultContainer = document.getElementById('result-container');

uploadBtn.addEventListener('click', () => {
    if (imageInput.files.length === 0) {
        alert('Please select an image to upload.');
        return;
    }

    const file = imageInput.files[0];

    // Validate file type
    const allowedExtensions = ['image/png', 'image/jpeg', 'image/jpg'];
    if (!allowedExtensions.includes(file.type)) {
        alert('Invalid file type. Please upload an image in PNG, JPG, or JPEG format.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    // Show progress bar and reset its value
    progressContainer.style.display = 'block';
    progressBar.style.width = '0%';

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);

    // Handle upload progress
    xhr.upload.onprogress = (event) => {
        if (event.lengthComputable) {
            const percentComplete = (event.loaded / event.total) * 100;
            progressBar.style.width = `${percentComplete}%`;
        }
    };

    // Handle successful response
    xhr.onload = () => {
        progressContainer.style.display = 'none';

        try {
            const response = JSON.parse(xhr.responseText);

            if (xhr.status === 200) {
                const predictedClass = response.predicted_class || 'Unknown';
                const confidence = response.confidence !== undefined ? Number(response.confidence).toFixed(2) : 'N/A';

                // Display results
                resultContainer.innerHTML = `
                    <h3>Prediction Results:</h3>
                    <p><strong>Disease:</strong> ${predictedClass}</p>
                    <p><strong>Confidence:</strong> ${confidence}%</p>
                `;
            } else if (response.message) {
                resultContainer.innerHTML = `<p style="color: orange;">${response.message}</p>`;
            } else {
                resultContainer.innerHTML = `<p style="color: red;">Error: ${response.error || 'An unknown error occurred.'}</p>`;
            }
        } catch (error) {
            resultContainer.innerHTML = `<p style="color: red;">An error occurred while processing the response.</p>`;
            console.error('Response parsing error:', error);
        }
    };

    // Handle errors during the request
    xhr.onerror = () => {
        progressContainer.style.display = 'none';
        resultContainer.innerHTML = `<p style="color: red;">An error occurred during the upload. Please try again.</p>`;
    };

    // Send the request
    xhr.send(formData);

    // Display the uploaded image preview
    uploadedImage.src = URL.createObjectURL(file);
    uploadedImage.style.display = 'block';
    uploadedImageContainer.style.display = 'block';
});
