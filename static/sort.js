const bubbleSort = async () => {
    const input = document.querySelector('[name="input"]')?.value;
    const start = +new Date();
    const res = await fetch(`./bubbleSort?items=${input}`);
    const end = +new Date();
    await render(await res.json());
    document.querySelector('[name="time"]').value = end - start;
};

const quickSort = async () => {
    const input = document.querySelector('[name="input"]')?.value;
    const start = +new Date();
    const res = await fetch(`./quickSort?items=${input}`);
    const end = +new Date();
    await render(await res.json());
    document.querySelector('[name="time"]').value = end - start;
};

const mergeSort = async () => {
    const input = document.querySelector('[name="input"]')?.value;
    const start = +new Date();
    const res = await fetch(`./mergeSort?items=${input}`);
    const end = +new Date();
    await render(await res.json());
    document.querySelector('[name="time"]').value = end - start;
};

const setRandomList = (n = 1_000) => {
    const arr = Array.from(Array(n)).map((_, i) => Math.trunc(Math.random() * n));
    const uniq = Array.from(new Set(arr));
    document.querySelector('[name="input"]').value = uniq.sort(() => 0.5 - Math.random());
};

const render = async (sorted) => {
    document.querySelector('[name="output"]').value = sorted;
};
