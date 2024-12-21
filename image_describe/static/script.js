const imageInput = document.getElementById('imageInput');
const submitBtn = document.querySelector('.submit-btn');
const resultDiv = document.getElementById('result');
const imagePreview = document.getElementById('imagePreview');
const loadingSpinner = document.getElementById('loadingSpinner');

imageInput.addEventListener('change', () => {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block';
        };
        reader.readAsDataURL(file);
        submitBtn.disabled = false;
        resultDiv.innerHTML = '';
    } else {
        imagePreview.style.display = 'none';
        submitBtn.disabled = true;
        resultDiv.innerHTML = '';
    }
});

document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    if (!imageInput.files.length) {
        resultDiv.innerHTML = "Please select an image.";
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);

    loadingSpinner.style.display = 'block';
    resultDiv.innerHTML = '';
    submitBtn.disabled = true;

    try {
        const response = await fetch('/api/describe', {
            method: 'POST',
            body: formData
        });

        loadingSpinner.style.display = 'none';
        submitBtn.disabled = false;

        if (!response.ok) {
            const err = await response.json();
            resultDiv.innerHTML = "Error: " + (err.error || 'Unknown error');
            return;
        }

        const data = await response.json();
        resultDiv.innerHTML = `<strong>Caption:</strong> ${data.description}`;
    } catch (error) {
        loadingSpinner.style.display = 'none';
        submitBtn.disabled = false;
        console.error(error);
        resultDiv.innerHTML = "An error occurred while processing your request.";
    }
});