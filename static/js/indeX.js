
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

document.querySelector('.shopprod3').src = target.dataset.img || '';
     document.getElementById('product_name_display').innerText = target.dataset.name; // Название товара
    document.getElementById('product_color_display').innerText = target.dataset.color; // Цвет товара
    document.getElementById('product_count_display').innerText = countValue; // Количество товара
    document.getElementById('product_total_display').innerText = totalPrice; // Сумма

    // Устанавливаем значения в скрытые поля
    document.getElementById('product_name').value = target.dataset.name; // Название товара
    document.getElementById('product_color').value = target.dataset.color; // Цвет товара
    document.getElementById('product_count').value = countValue; // Количество товара
    document.getElementById('product_total').value = totalPrice; // Сумма


//    document.querySelector('.shopprod6').value = `${target.dataset.name} + ${totalPrice} + ${countValue} + ${target.dataset.color} + ${target.dataset.img || ''}`
    console.log(target.dataset.color)

}
function closePopup() {
    var popup = document.querySelector('.popup');
    popup.style.display = 'none';
    const element = document.querySelector("main")
    element.style.filter = 'none'
    const element2 = document.querySelector(".grop");
    if (element2) {
        element2.style.top = '110px';}
}
//function info(event) {
//    // Получаем элемент, на который нажали
//    const button = event.currentTarget;
//    // Получаем значение data-color
//    const color = button.getAttribute('data-color');
//    const name = button.getAttribute('data-name');
//    const price = button.getAttribute('data-price');
//    const noteId = button.getAttribute('data-id'); // Убедитесь, что вы добавили data-id в кнопку
//
//    // Получаем количество из поля ввода
//    const quantityInput = document.getElementById(`count-${noteId}`);
//    const quantity = quantityInput ? quantityInput.value : 1; // Устанавливаем значение по умолчанию, если поле не найдено
//
//    // Выводим информацию в alert
//    alert(`Товар: ${name}\nЦвет: ${color}\nКоличество: ${quantity}\nЦена: ${price} рублей`);
//}

//$(".popup").on('submit', '.form-example', function(event){
//
//  event.preventDefault()
//  let form = $(".form-example")
//  let url = form.attr('action')
//
//  $.ajax({
//    type: 'POST',
//    url: url,
//    data: form.serialize(),
//    success: function(response) {
//            console.log(response);
//               if (response.success) {
//                    alert('Ваш заказ принят, мы свяжемся с вами в ближайшее время!');
//                    closePopup();
//                } else {
//                    alert('Произошла ошибка: ' + response.error);
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('Ошибка при отправке данных: ' + error);
//            }
//  })
//});
// бургер меню
// Получаем элементы бургер-меню и навигации
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');

// Добавляем обработчик события на клик по бургер-меню
burger.addEventListener('click', () => {
    // Переключаем класс "active" у навигации
    nav.classList.toggle('active');

    // Анимация бургер-меню
    burger.classList.toggle('active');
});



// Функция для добавления товара в корзину
function info(event) {
    const button = event.currentTarget; // Получаем элемент кнопки
    const dataName = button.getAttribute('data-name');
    const dataColor = button.getAttribute('data-color');
    const dataPrice = button.getAttribute('data-price');
    const noteId = button.getAttribute('data-id'); // Извлекаем ID товара

    const countElement = document.getElementById(`count-${noteId}`); // Получаем элемент input по ID
    const quantity = parseInt(countElement.value); // Извлекаем значение и преобразуем в число

    // Проверяем количество
    if (quantity < 1) {
        alert("Количество должно быть больше 0.");
        return;
    }

    // Создаем объект данных для отправки на сервер
    const data = {
        id: noteId,
        name: dataName,
        color: dataColor,
        price: dataPrice,
        quantity: quantity
    };
    console.log(data)
    // Отправляем данные на сервер
    fetch(`/add_to_cart/${noteId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Получаем CSRF-токен
        },
        body: JSON.stringify(data) // Отправляем данные в формате JSON
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data.message); // Выводим сообщение об успешном добавлении
        updateCartCount(); // Обновляем количество товаров в корзине

        // Отображаем сообщение на странице
        displayMessage(data.message); // Функция для отображения сообщения
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

// Функция для отображения сообщения на странице
function displayMessage(message) {
    const messageContainer = document.getElementById('message-container'); // Элемент для отображения сообщения
    messageContainer.innerHTML = `<div class="alert alert-success">${message}</div>`; // Создаем элемент с сообщением
    setTimeout(() => {
        messageContainer.innerHTML = ''; // Удаляем сообщение через 3 секунды
    }, 3000);
}

function displayMessage(message) {
    const messageContainer = document.getElementById('message-container'); // Элемент для отображения сообщения
    messageContainer.innerHTML = `<div class="alert alert-success">${message}</div>`; // Создаем элемент с сообщением
    messageContainer.classList.add('show'); // Добавляем класс для анимации

    setTimeout(() => {
        messageContainer.classList.remove('show'); // Удаляем класс через 3 секунды
        setTimeout(() => {
            messageContainer.innerHTML = ''; // Удаляем сообщение через 3 секунды после исчезновения
        }, 500); // Время, соответствующее времени анимации
    }, 3000);
}
// Функция для получения CSRF-токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Функция для обновления количества товаров в корзине
function updateCartCount() {
    fetch('/cart/count/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cart-count').innerText = data.count; // Обновляем элемент с количеством
        });
}
function checkMaxValue(input) {
    if (input.value > 30) {
        input.value = 30; // Устанавливаем значение в 30, если больше
    }
}

function filterOrders(tableBodyId, selectedStatus) {

    const rows = document.querySelectorAll(`#${tableBodyId} tr[data-status]`);
    rows.forEach(row => {
        const status = row.getAttribute('data-status'); // Получаем статус строки
        // Проверяем, соответствует ли статус выбранному значению фильтра
        if (selectedStatus === "" || status === selectedStatus) {
            row.style.display = ""; // Показываем строку
        } else {
            row.style.display = "none"; // Скрываем строку
        }
    });
}

// Функция для инициализации фильтрации по умолчанию
function initializeFilters() {
    // Фильтруем каждую таблицу по статусу "pending"
    filterOrders('orders-table-body', 'pending');
    filterOrders('shop-table-body', 'pending');
    filterOrders('feedback-table-body', 'pending');
}

// Вызываем функцию инициализации при загрузке страницы
window.onload = initializeFilters;

