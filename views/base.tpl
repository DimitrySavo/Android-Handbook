<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/index.css">
    <title>{{ title }}</title>
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
            <!-- Тут замени на такое же название, как в файле с функцией -->
        </div>
    </header>

    <section class="main-section">
        <div class="nav-col">
            % for key, value in items.items():
                <ul class="headers-list">
                    <li>{{ key }}
                        <ul class="topics-list">
                            % for item in value:
                            <a href="/topics/{{ item }}">
                                <li>{{ item }}</li>
                            </a>
                            % end
                        </ul>
                    </li>
                </ul>
            % end
        </div>
        
        <div class="topic">
            {{ !topic }}
        </div>
    </section>

    <footer class="footer">
        <h1>© 2024 Android Handbook, inc</h1>
        <p>Last updated on March 20 2024</p>
        <p>Powered By bottle</p>
    </footer>
</body>
</html>