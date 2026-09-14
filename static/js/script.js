// ================================
// DecodeLabs - Caesar Cipher
// Red Hacker Theme JavaScript
// ================================

// Matrix Rain Effect
const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()';
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

function drawMatrix() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#ff0000';
    ctx.font = fontSize + 'px Courier New';

    drops.forEach((y, x) => {
        const letter = letters[Math.floor(Math.random() * letters.length)];
        ctx.fillText(letter, x * fontSize, y * fontSize);
        if (y * fontSize > canvas.height && Math.random() > 0.975) {
            drops[x] = 0;
        }
        drops[x]++;
    });
}

setInterval(drawMatrix, 50);

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

function updateShift() {
    const shift = document.getElementById('shiftSlider').value;
    document.getElementById('shiftValue').textContent = shift;
}

async function processText(action) {
    const text = document.getElementById('inputText').value;
    const shift = document.getElementById('shiftSlider').value;
    const bruteCard = document.getElementById('bruteCard');
    const outputCard = document.getElementById('outputCard');
    const outputLabel = document.getElementById('outputLabel');
    const outputText = document.getElementById('outputText');

    if (!text.trim()) {
        outputText.value = 'ERROR: No input detected. Enter a message!';
        outputCard.style.display = 'block';
        return;
    }

    const response = await fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, shift, action })
    });

    const data = await response.json();

    if (action === 'brute') {
        bruteCard.style.display = 'block';
        outputCard.style.display = 'none';
        const bruteResults = document.getElementById('bruteResults');
        bruteResults.innerHTML = '';

        data.result.forEach(item => {
            const div = document.createElement('div');
            div.className = 'brute-item';
            div.innerHTML = '<span class="brute-shift">SHIFT ' + item.shift + ':</span><span class="brute-text">' + item.text + '</span>';
            bruteResults.appendChild(div);
        });
        return;
    }

    bruteCard.style.display = 'none';
    outputCard.style.display = 'block';

    if (action === 'encrypt') {
        outputLabel.textContent = 'ENCRYPTED OUTPUT';
        outputText.value = data.result;
    } else {
        outputLabel.textContent = 'DECRYPTED OUTPUT';
        outputText.value = data.result;
    }
}

function copyOutput() {
    const output = document.getElementById('outputText');
    navigator.clipboard.writeText(output.value);
    const btn = document.querySelector('.btn-copy');
    btn.textContent = 'COPIED!';
    setTimeout(() => {
        btn.textContent = 'COPY OUTPUT';
    }, 2000);
}
