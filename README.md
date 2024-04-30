# Personalized News Digest Generator

This repository hosts a personalized news digest generator application project written in Python. The application fetches news from the News API based on the user's interests, retrieves the full texts of these news articles from their URLs using the Newspaper3k library, summarizes them with Langchain and Cohere, and presents them in digest form on an HTML page.

## How to Use?

1. Clone or download the repository.
   
   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install required modules using pip.
   
   ```bash
   pip install requests
   pip install langchain_cohere
   pip install langchain
   pip install configparser
   pip install newspaper3k
   pip install lxml_html_clean
   ```

3. Fill in your News API and Cohere API keys in the `config.ini` file.

4. Run the `Main.py` file.
   
   ```bash
   python Main.py
   ```

5. Enter the topics and categories you want to follow, to terminal.

6. Your digest will be ready in a few minutes. You can open it from the generated HTML file in folder.
   
Feel free to explore and customize the application according to your needs!
