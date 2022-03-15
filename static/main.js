let queueDom;

const enqueue = async (el) => {
    const item = document.querySelector("input[name='item']").value;
    if (item === '') return;
    el.disabled = true;
    console.log('item:', item);
    const res = await fetch(`./enqueue?item=${item}`);
    await renderEnqueue(await res.json());
    el.disabled = false;
};

const dequeue = async (el) => {
    el.disabled = true;
    const res = await fetch('./dequeue');
    const items = await res.json();
    await renderDequeue(items);
    el.disabled = false;
};

const addItem = (e) => {
    const item = document.createElement('div');
    item.className = 'box';
    item.textContent = e;
    queueDom.appendChild(item);
};

const renderEnqueue = async (queue) => {
    queueDom = document.querySelector('.queue');
    queueDom.innerHTML = '';
    queueDom.classList.add('enqueue');
    queue.slice(0, -1).forEach(addItem);
    addItem(queue.slice(-1));
    await new Promise((res) => setTimeout(() => res(queueDom.classList.remove('enqueue')), 1000));
};

const renderDequeue = async (queue) => {
    const firstIn = document.querySelector('.queue .box');
    firstIn.classList.add('dequeue');
    await new Promise((res) => setTimeout(() => res(firstIn.remove()), 1000));
};
