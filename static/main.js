const enqueue = async () => {
    const item = document.querySelector("input[name='item']").value;
    console.log('item:', item);
    const res = await fetch(`./enqueue?item=${item}`);
    renderQueue(await res.json());
};

const dequeue = async () => {
    const res = await fetch('./dequeue');
    renderQueue(await res.json());
};

const renderQueue = (queue) => {
    const queueDom = document.querySelector('.queue');
    queueDom.innerHTML = '';
    queue.forEach((e) => {
        const item = document.createElement('div');
        item.className = 'box';
        item.textContent = e;
        queueDom.appendChild(item);
    });
};
