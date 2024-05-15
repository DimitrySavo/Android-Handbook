<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/index.css">
    <link rel="stylesheet" href="../static/cards.css"> 
    <link rel="stylesheet" href="../static/styles.css">
    <title>Актуальные новости</title>
</head>
<body>
    <header class="header">
        <a href="/" class="Header-link">
            <h1>Android Handbook</h1>
        </a>
        <div class="nav-header">
            <a href="/About" class="Header-link">About Us</a>
            <a href="/Contacts" class="Header-link">Contacts</a>
            <a href="/Reviews" class="Header-link">Reviews</a>
            <a href="/CurrentNews" class="Header-link">Current News</a>
        </div>
    </header>

    <div class="container">
        <h1>Актуальные новости</h1>
          <!-- Форма для добавления новостных карточек -->
        <div id="add-news-form" >
            <form id="news-form" action="/submit" method="POST">
                <input type="text" name="title" placeholder="Заголовок">
                <input type="text" name="description" placeholder="Описание">
                <input type="url" name="image_url" placeholder="URL изображения">
                <input type="url" name="link" placeholder="Ссылка на новость">
                <button type="submit">Добавить</button>
            </form>
        </div>
        <div class="news-cards" id="news-cards">
            <!-- Карточки новостей -->
            <!-- Здесь будут отображаться карточки новостей -->
        </div>
    </div>

    <footer class="footer">
        <h1>© 2024 Android Handbook, inc</h1>
        <p>Last updated on March 20 2024</p>
        <p>Powered By bottle</p>
    </footer>

  

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const newsForm = document.getElementById('news-form');
            const newsCardsContainer = document.getElementById('news-cards');

            // Обработчик события отправки формы
            newsForm.addEventListener('submit', function(event) {
                event.preventDefault(); // Предотвращаем отправку формы по умолчанию

                // Создаем новый объект FormData для получения данных из формы
                const formData = new FormData(newsForm);

                // Отправляем запрос POST на сервер для добавления новой карточки новости
                fetch('/submit', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json()) // Парсим ответ сервера в формате JSON
                .then(data => {
                    // Полученные данные содержат информацию о добавленной карточке
                    // Создаем HTML-элемент для новой карточки
                    const newCardHTML = `
                        <div class="news-card" onclick="window.location.href='${data.link}'">
                            <img src="${data.image_url}">
                            <div class="card-description">
                                <h2>${data.title}</h2>
                                <p>${data.description}</p>
                            </div>
                        </div>
                    `;
                    // Вставляем новую карточку в контейнер для карточек новостей
                    newsCardsContainer.insertAdjacentHTML('afterbegin', newCardHTML);

                    // Очищаем поля формы после успешного добавления карточки
                    newsForm.reset();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            });
        });
    </script>

</body>
</html>

<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/index.css">
    <link rel="stylesheet" href="../static/cards.css"> 
    <title>Актуальные новости</title>
</head>
<body>
    <header class="header">
        <a href="/" class="Header-link">
            <h1>Android Handbook</h1>
        </a>
        <div class="nav-header">
            <a href="/About" class="Header-link">About Us</a>
            <a href="/Contacts" class="Header-link">Contacts</a>
            <a href="/Reviews" class="Header-link">Reviews</a>
            <a href="/CurrentNews" class="Header-link">Current News</a>
        </div>
    </header>


<div class="container">
    <h1>Актуальные новости</h1>
    <div class="news-cards">
        <div class="news-card" onclick="window.location.href='https://metanit.com/news/27.php'">
            <img src="../static/images/kotlinIcon.jpg">
            <div class="card-description">
                <h2>Вышел Kotlin 1.5.0</h2>
                <p>Что нового в новой версии языка? Прежде всего были добавлены новые фичи</p>
            </div>
        </div>
        <div class="news-card" onclick="window.location.href='https://metanit.com/news/27.php'">
            <img src="../static/images/kotlinIcon.jpg">
            <div class="card-description">
                <h2>Вышел Kotlin 1.5.0</h2>
                <p>Что нового в новой версии языка? Прежде всего были добавлены новые фичи</p>
            </div>
        </div>
        <div class="news-card" onclick="window.location.href='https://metanit.com/news/27.php'">
            <img src="../static/images/kotlinIcon.jpg">
            <div class="card-description">
                <h2>Вышел Kotlin 1.5.0</h2>
                <p>Что нового в новой версии языка? Прежде всего были добавлены новые фичи</p>
            </div>
        </div>
        <div class="news-card" onclick="window.location.href='https://metanit.com/news/27.php'">
            <img src="../static/images/kotlinIcon.jpg">
            <div class="card-description">
                <h2>.0</h2>
                <p>Что нового в новой версии языка? Прежде всего были добавлены новые фичи</p>
            </div>
        </div>
    </div>
</div>
<footer class="footer">
    <h1>© 2024 Android Handbook, inc</h1>
    <p>Last updated on March 20 2024</p>
    <p>Powered By bottle</p>
</footer>

<div id="add-news-form" style="display: none;">
    <form id="news-form">
        <input type="text" name="title" placeholder="Заголовок">
        <input type="text" name="description" placeholder="Описание">
        <input type="url" name="image_url" placeholder="URL изображения">
        <input type="url" name="link" placeholder="Ссылка на новость">
        <button type="submit">Добавить</button>
    </form>
</div>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const newsForm = document.getElementById('news-form');
        const newsCardsContainer = document.getElementById('news-cards');

        // Обработчик события отправки формы
        newsForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Предотвращаем отправку формы по умолчанию

            // Создаем новый объект FormData для получения данных из формы
            const formData = new FormData(newsForm);

            // Отправляем запрос POST на сервер для добавления новой карточки новости
            fetch('/add_news_card', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json()) // Парсим ответ сервера в формате JSON
            .then(data => {
                // Полученные данные содержат информацию о добавленной карточке
                // Создаем HTML-элемент для новой карточки
                const newCardHTML = `
                    <div class="news-card" onclick="window.location.href='${data.link}'">
                        <img src="${data.image_url}">
                        <div class="card-description">
                            <h2>${data.title}</h2>
                            <p>${data.description}</p>
                        </div>
                    </div>
                `;
                // Вставляем новую карточку в контейнер для карточек новостей
                newsCardsContainer.insertAdjacentHTML('afterbegin', newCardHTML);

                // Очищаем поля формы после успешного добавления карточки
                newsForm.reset();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
</script>

</body>
</html> -->