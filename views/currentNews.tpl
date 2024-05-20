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
                <input type="text" name="title" placeholder="Заголовок" required maxlength="30">
                <input type="text" name="description" placeholder="Описание" required maxlength="150">
                <input type="url" name="image_url" placeholder="URL изображения" required>
                <input type="url" name="link" placeholder="Ссылка на новость" required>
                <input type="date" name="date" required="true" max="2024-05-21">
                <button type="submit">Добавить</button>
            </form>
        </div>
        <div class="news-cards" id="news-cards">
            <!-- Карточки новостей -->
            <!-- Здесь будут отображаться карточки новостей -->
            % for card in news_cards:
            <div class="news-card" data-link="{{ card['link'] }}" onclick="redirectToLink(this)">
                <img src="{{ card['image_url'] }}">
                <div class="card-description">
                    <h2>{{ card['title'] }}</h2>
                    <p>{{ card['description'] }}</p>
                    <p>{{ card['date'] }}</p>
                </div>
            </div>
            % end
        </div>
    </div>
    <script>
        function redirectToLink(element) {
            var link = element.getAttribute('data-link');
            window.location.href = link;
        }
    </script>
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
                                <p>${data.date}</p>
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
