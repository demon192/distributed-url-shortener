const form = document.getElementById("urlForm");
const longUrlInput = document.getElementById("longUrl");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const url = longUrlInput.value;

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/shorten?url=${encodeURIComponent(url)}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        resultDiv.innerHTML = `
            <p>Your Short URL:</p>
            <a href="${data.short_url}" target="_blank">${data.short_url}</a>
        `;

    } catch (error) {
        resultDiv.innerHTML = "Error connecting to API";
        console.error(error);
    }
});