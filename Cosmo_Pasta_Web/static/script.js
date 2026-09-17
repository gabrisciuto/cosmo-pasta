const filters = document.querySelectorAll('.filter');
const cards = document.querySelectorAll('.dish');

function showCategory(category) {
    cards.forEach(card => {
        card.style.display = card.dataset.category === String(category) ? '' : 'none';
    });
}

filters.forEach(filter => {
    filter.addEventListener('click', () => {
        filters.forEach(x => x.classList.remove('active'));
        filter.classList.add('active');
        showCategory(filter.dataset.category);
    });
});

if (filters.length) showCategory(0);

const cart = [];
const box = document.getElementById('cart');
const items = document.getElementById('items');
const total = document.getElementById('total');
const count = document.getElementById('count');

function draw() {
    items.innerHTML = '';
    let sum = 0;
    cart.forEach((item, index) => {
        sum += item.price;
        const row = document.createElement('div');
        row.className = 'line';
        row.innerHTML = `<span>${item.name}</span><b>€${item.price.toFixed(2)} <button data-index="${index}">×</button></b>`;
        items.appendChild(row);
    });
    total.textContent = '€' + sum.toFixed(2);
    count.textContent = cart.length;
    items.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', () => {
            cart.splice(Number(button.dataset.index), 1);
            draw();
        });
    });
}

document.querySelectorAll('.add').forEach(button => {
    button.addEventListener('click', () => {
        cart.push({ name: button.dataset.name, price: Number(button.dataset.price) });
        draw();
        box.classList.add('open');
    });
});

document.getElementById('openCart')?.addEventListener('click', () => box.classList.add('open'));
document.getElementById('close')?.addEventListener('click', () => box.classList.remove('open'));
document.querySelector('.hamb')?.addEventListener('click', () => {
    document.querySelector('.nav nav')?.classList.toggle('mobile-open');
});
