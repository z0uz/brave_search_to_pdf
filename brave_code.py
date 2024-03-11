from brave import Brave
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(search_results, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    y = 750
    for result in search_results:
        c.drawString(100, y, f"Title: {result.get('title', 'N/A')}")
        c.drawString(100, y - 20, f"URL: {result.get('url', 'N/A')}")
        description = result.get('snippet', 'N/A')
        c.drawString(100, y - 40, f"Description: {description}")
        y -= 60
    c.save()

def search_and_save_results(api_key, query, num_results, filename):
    brave = Brave(api_key=api_key)
    total_results = []
    batch_size = 10  # Number of results to fetch per request
    offset = 0
    while len(total_results) < num_results:
        search_results = brave.search(q=query, count=batch_size, offset=offset)
        total_results.extend(search_results.web_results)
        offset += batch_size
    create_pdf(total_results[:num_results], filename)

def main():
    api_key = input("Enter your Brave API key: ")
    query = input("Enter your search query: ")
    num_results = int(input("Enter number of results: "))
    filename = input("Enter output PDF filename: ")
    search_and_save_results(api_key, query, num_results, filename)

if __name__ == "__main__":
    main()
