This Python script utilizes the Brave Search API to perform searches based on user input and saves the search results to a PDF file. 
It provides a simple command-line interface where users can input their Brave API key, specify the search query, and choose the number of search results to fetch.

Features:
Fetches search results from the Brave Search API.
Supports customization of the search query and number of results.
Saves the search results (title, URL, and description) to a PDF file for easy reference.
Handles errors gracefully, ensuring smooth execution even with incomplete search results.

Usage:
Install the brave package using pip install brave.
Run the script (python brave_search_to_pdf.py).
Enter your Brave API key when prompted.
Provide the search query and the number of results to fetch.
The script will generate a PDF file containing the search results.

Requirements:
Python 3.x
brave package (installable via pip)
ReportLab library (automatically installed with ReportLab)
