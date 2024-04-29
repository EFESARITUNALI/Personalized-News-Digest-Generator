import config
from news import fetch_news, get_article_text
from summaries import summarize_article

def get_user_interests():
    print("Welcome to the personalized news digest application!")
    print("Please enter the topics and categories you want to follow (separated by commas):")
    interests_input = input("Topics and categories: ").strip()
    return [interest.strip() for interest in interests_input.split(",")]

def generate_html_content(articles, counter):
    html_content = open("html_skeleton.txt", 'r').read()
    for idx, article in enumerate(articles, 5*counter+1):
        try:
            article_text = get_article_text(article['url'])
            summary = summarize_article(article['title']+article['content']+article_text)
            html_content += f"""<div class="article">
                                    <h2>{idx}. {article['title']}</h2>
                                    <img src='{article['urlToImage']}' alt='Image not available' style='max-width: 100%;'>
                                    <p>{summary}</p>
                                    <a href='{article['url']}'>Read original</a>
                                </div>"""
        except Exception as e:
            print(f"Error processing article: {e}")
    return html_content

def main():
    interests = get_user_interests()
    articles = fetch_news(interests)
    if not articles:
        print("No news articles found based on your interests.")
        return
    
    counter = 0
    while counter < len(articles) // 5:
        html_content = generate_html_content(articles[counter * 5 : (counter + 1) * 5], counter)
        filename = f"news_digest_{counter + 1}.html"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(html_content)
            print(f"News digest generated successfully. You can view it in {filename}")
            
            choice = input(f"Would you like to see page {counter + 2}? (y/n): ").strip().lower()
            if choice != 'y':
                break
            counter += 1
        except Exception as e:
            print(f"Error generating news digest: {e}")
    print("End of your digest, see you next time!")

if __name__ == "__main__":
    main()