document.getElementById('predictionForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    // Get input values
    const age = document.getElementById('age').value;
    const chestPain = document.getElementById('chestPain').value;
    const maxHeartRate = document.getElementById('maxHeartRate').value;

    try {
        // Send data to the backend for prediction
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ age, chestPain, maxHeartRate }),
        });

        if (!response.ok) {
            throw new Error('Failed to get a valid response from the server');
        }

        const result = await response.json();
        document.getElementById('result').innerText = `Prediction: ${result.prediction}`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred. Please try again.${error.message}';
    }
});
