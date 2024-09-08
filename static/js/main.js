document.addEventListener('DOMContentLoaded', () => {
    const clickButton = document.getElementById('click-button');
    const cookieCount = document.getElementById('cookie-count');

    clickButton.addEventListener('click', () => {
        fetch('/click', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                cookieCount.textContent = data.cookies;
            });
    });

    function updateStatus() {
        fetch('/status')
            .then(response => response.json())
            .then(data => {
                cookieCount.textContent = data.cookies;
            });
    }

    setInterval(updateStatus, 1000);
});