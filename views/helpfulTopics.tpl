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
            <a href="/helpfulTopics" class="Header-link">Helpful topics</a>
            <a href = "/CurrentNews" class="Header-link">Current News</a>
        </div>
    </header>

    <section class="htopics-section">
        <div class="topics-col">
            % for item in topics:
            <div class="htopic">
                <img class="htopic-image" src="{{item.image}}" alt="htopic1"></img>
                <h2 class="htopic-title">{{item.title}}</h2>
                <p class="htopic-preview">{{item.text}}</p>
                <p class="htopic-link"><a href="{{item.url}}">{{ item.url }}</a></p>
            </div>
            % end
        </div>
        


        <section>
            <div class="htopic-new-topic">
                <form class="topic-form" action="/submitTopic" method="POST">
                    <label for="topicTitle">Title:</label>
                    <input type="text" id="topicTitle" name="topicTitle" required><br><br>
                    
                    <label for="topicText">Text:</label>
                    <textarea id="topicText" name="topicText" required></textarea><br><br>
                    
                    <label for="topicImage">Image URL:</label>
                    <input type="text" id="topicImage" name="topicImage" required><br><br>
                    
                    <label for="topicURL">Main Topic URL:</label>
                    <input type="text" id="topicURL" name="topicURL" required><br><br>
                    
                    <input type="submit" value="Submit">
                </form>
            </div>
        </section>
    </section>

    
    

    <footer class="footer">
        <h1>© 2024 Android Handbook, inc</h1>
        <p>Last updated on March 20 2024</p>
        <p>Powered By bottle</p>
    </footer>
</body>
</html>