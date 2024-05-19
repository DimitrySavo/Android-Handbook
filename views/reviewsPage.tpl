<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://kit.fontawesome.com/53ff410a04.js" crossorigin="anonymous"></script>
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
            <a href ="/CurrentNews" class="Header-link">Current News</a>
        </div>
    </header>

    <section class="reviews-section">
        <form class = "review-form" action="/submit_review" method="post">
            <input name="username" id="username" class="single-line-text" type="text" placeholder="Имя(будет видно остальным пользователям)"/>
            <input name="user-email" id="user-email" class="single-line-text" type="text" placeholder="E-mail(для авторизации)"/>
            <textarea name="user-review" id="user-review" class="multiline-text" placeholder="Оставьте ваш отзыв"></textarea>
            <div class="bottom-review-div">
                <div class="rating">
                    <input type="radio" class="radio-rating" name="rating" value="like">
                        <i class="fa-solid fa-thumbs-up fa-2xl icon like"></i>
                    </input> 
                    <input type="radio" class="radio-rating" name="rating" value="dislike">
                        <i class="fa fa-thumbs-down fa-2xl icon dislike"></i>
                    </input>  
                </div>
                
                <input type="submit" value="Send" class="send-review"></input>
            </div>
        </form>

        <div class="review-col">
                % for item in reviews: 
                <div class="review-container">
                    <h4 class="username-heading">
                        {{ item.username }}
                    </h4>
                    <span class="user-review">
                        {{ item.text }}
                    </span>
                    <span class="review-date-span">
                        Дата отзыва: {{ item.dateCreate }}
                    </span>
                    <div class="bottom-rating-container">
                        % if item.rating:
                            <i class="fa-solid fa-thumbs-up fa-2xl icon like"></i>
                        % else:
                            <i class="fa fa-thumbs-down fa-2xl icon dislike"></i>
                        % end   
                    </div>
                </div>
                % end
        </div>
    </section>
    
    <footer class="footer">
        <h1>© 2024 Android Handbook, inc</h1>
        <p>Last updated on March 20 2024</p>
        <p>Powered By bottle</p>
    </footer>
</body>
</html>