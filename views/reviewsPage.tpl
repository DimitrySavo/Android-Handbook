<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="../static/index.css">
    <title>Reviews</title>
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
        </div>
    </header>

    <section class="reviews-section">
        <form class = "review-form">
            <input id="username" class="single-line-text" type="text" placeholder="Имя(будет видно остальным пользователям)"/>
            <input id="user-email" class="single-line-text" type="text" placeholder="E-mail(для авторизации)"/>
            <input id="user-review" class="multiline-text" type="text" placeholder="Оставьте ваш отзыв"/>
            <div class="starts-div">
                <input type="radio" class="like" name="rating">
                    <i class="fa fa-thumbs-up"></i>
                </input> 
                <input type="radio" class="dislike" name="rating">
                    <i class="fa fa-thumbs-down"></i>
                </input> 
            </div>
        </form>
    </section>
    
    <footer class="footer">
        <h1>© 2024 Android Handbook, inc</h1>
        <p>Last updated on March 20 2024</p>
        <p>Powered By bottle</p>
    </footer>
</body>
</html>