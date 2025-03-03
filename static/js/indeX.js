
window.addEventListener("load", () => {
    var carousels = document.querySelectorAll(".carousel-3d");
    for (var i = 0; i < carousels.length; i++) {
        carousel(carousels[i]);
    }
});
function carousel(root) {
    var figure = root.querySelector("figure"),
    nav = root.querySelector("nav"),
    images = figure.children,
    n = images.length,
    gap = root.dataset.gap || 0,
    bfc = "bfc" in root.dataset,
    theta = 2 * Math.PI / n,
    currImage = 0;
    setupCarousel(n, parseFloat(getComputedStyle(images[0]).width));
    window.addEventListener("resize", () => {
        setupCarousel(n, parseFloat(getComputedStyle(images[0]).width));
    });
    setupNavigation();
    function setupCarousel(n, s) {
        var apothem = s / (2 * Math.tan(Math.PI / n));
        figure.style.transformOrigin = `50% 50% ${-apothem}px`;
        for (var i = 0; i < n; i++) images[i].style.padding = `0 ${gap}px`;
        for (i = 0; i < n; i++) {
            images[i].style.transformOrigin = `50% 50% ${-apothem}px`;
            images[i].style.transform = `rotateY(${i * theta}rad)`;
        }
        if (bfc)
        for (i = 0; i < n; i++) images[i].style.backfaceVisibility = "hidden";
        rotateCarousel(currImage);
    }
    function setupNavigation() {
        nav.addEventListener("click", onClick, true);
        function onClick(e) {
            e.stopPropagation();
            var t = e.target;
            if (t.tagName.toUpperCase() != "BUTTON") return;
            if (t.classList.contains("next")) {
                currImage++;
                } else {
                currImage--;
            }
            rotateCarousel(currImage);
        }
    }
    function rotateCarousel(imageIndex) {
        figure.style.transform = `rotateY(${imageIndex * -theta}rad)`;
    }
    var xClick;
    var mouseDown;
    /* Смена слайдов мышкой */    
    figure.onmousedown = (event) => {
        xClick = event.pageX;
        mouseDown = true;
    };
    figure.onmouseup = (event) => {
        mouseDown = false;
    };    
    figure.onmousemove = (event) => {
        if (mouseDown) {
            var xMove = event.pageX;
            if (Math.floor(xClick - xMove) > 5) {
                currImage++;
                rotateCarousel(currImage);
                mouseDown = false;
            }
            else if (Math.floor(xClick - xMove) < -5) {
                currImage--;
                rotateCarousel(currImage);
                mouseDown = false;
            }
        }
    };
    let cur;
    function showcur() {
        cur = setInterval(function() {
            currImage++;
            rotateCarousel(currImage);
        }, 2000);
    }
    function clearcur() {
        clearInterval(cur);
    }
    root.onmouseover  = function() {
        clearcur();
    }  
    root.onmouseout  = function() {
        showcur();
    }     
    showcur();
    /* Смена слайдов пальцем */    
    figure.ontouchstart = (event) => {
        xClick = event.changedTouches[0].pageX;
        mouseDown = true;
    };
    figure.ontouchend = (event) => {
        mouseDown = false;
    };    
    figure.ontouchmove = (event) => {
        if (mouseDown) {
            var xMove = event.changedTouches[0].pageX;
            if (Math.floor(xClick - xMove) > 5) {
                currImage++;
                rotateCarousel(currImage);
                mouseDown = false;
            }
            else if (Math.floor(xClick - xMove) < -5) {
                currImage--;
                rotateCarousel(currImage);
                mouseDown = false;
            }
        }
    };
}


/*Продукция*/
// переключение картинок
function myFunction(el, color) {
    let vsav = document.querySelector(`.prod${el}`).src
    document.querySelector(`.pr${el.substring(0, el.length - 1)}`).src = vsav

    const attributes = document.querySelectorAll(".add-to-cart"); // Получаем все элементы с классом add-to-cart
    attributes.forEach((element) => {
        element.setAttribute("data-img", vsav); // Устанавливаем атрибут data-img для каждого элемента
        element.setAttribute("data-color", color);
    });


}
// всплывающее окно
function openPopup(event) {
    var popup = document.querySelector('.popup');
    popup.style.display = 'block';
    const element = document.querySelector("main")
    element.style.filter = 'blur(5px)'
    const element2= document.querySelector(".grop")
    if (element2) {
        element2.style.top = '-30px'}
    const target = event.currentTarget; // Получаем элемент, на который нажали
    const productElement = target.closest('.produkt') || target.closest('.produkt_list'); // Находим  элемент с классом 'produkt' или '.produkt_list'
    if (!productElement) {
        console.error("Не удалось найти элемент с классами 'produkt' или 'produkt_list'");
        return; // Выходим из функции, если элемент не найден
    }
    const countInput = productElement.querySelector('input[name="count"]'); // Находим поле ввода количества
    const countValue = countInput.value; // Получаем значение количества

    const priceValue = parseFloat(target.dataset.price); // Получаем цену из атрибута data-price
    // Вычисляем общую стоимость
    const totalPrice = countValue * priceValue;
    console.log(totalPrice)
    console.log(target.dataset.name)


    document.querySelector('.shopprod1').innerText = target.dataset.name
    document.querySelector('.shopprod2').innerText = `Итого: ${totalPrice} руб`
    document.querySelector('.shopprod3').src = target.dataset.img || '';
    document.querySelector('.shopprod4').innerText = `Количество: ${countValue}`; // Устанавливаем количество
    document.querySelector('.shopprod5').innerText = target.dataset.color
    document.querySelector('.shopprod6').value = `${target.dataset.name} + ${totalPrice} + ${countValue} + ${target.dataset.color} + ${target.dataset.img || ''}`
    console.log(target.dataset.color)

}
function closePopup() {
    var popup = document.querySelector('.popup');
    popup.style.display = 'none';
    const element = document.querySelector("main")
    element.style.filter = 'none'
    const element2 = document.querySelector(".grop");
    if (element2) {
        element2.style.top = '80px';}
}



