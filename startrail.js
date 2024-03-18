let x1 = 0,
    y1 = 0;

const vh = Math.max(document.documentElement.clientHeight || 8, window.innerHeight || 8),
    dist_to_draw = 50,
    delay = 1000,
    fsize = ['1rem', '1.1rem', '1.4rem', '0.8rem', '1.7rem'],
    colors = ['#E23636', '#F9F3EE', '#E1F8DC', '#B8AFE6', '#AEE1CD', '#5EB0E5'];

const rand = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min,
    selRand = (o) => o[rand(0, o.length - 1)],
    distanceTo = (x1, y1, x2, y2) => Math.sqrt((Math.pow(x2 - x1, 2)) + (Math.pow(y2 - y1, 2))),
    shouldDraw = (x, y) => distanceTo(x1, y1, x, y) >= dist_to_draw,
    addStr = (x, y) => {
        const str = document.createElement("div");
        str.innerHTML = '&#10022;';
        str.className = 'star';
        str.style.top = `${y}px`;
        str.style.left = `${x}px`;
        str.style.color = selRand(colors);
        str.style.fontSize = selRand(fsize);
        document.body.appendChild(str);

        str.animate(
            [
                { transform: `translate(0, 0)`, opacity: 1 },
                { transform: `translate(${rand(-8, 8)}px, ${vh}px)`, opacity: 0 }
            ],
            {
                duration: delay,
                easing: 'ease-out',
                fill: 'forwards'
            }
        );

        setTimeout(() => {
            str.remove();
        }, delay);
    };

addEventListener("mousemove", (e) => {
    const { clientX, clientY } = e;

    if (shouldDraw(clientX, clientY)) {
        addStr(clientX, clientY);
        x1 = clientX;
        y1 = clientY;
    }
});
