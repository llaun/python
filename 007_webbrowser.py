import webbrowser

text = input("input: ")
url = "https://translate.google.co.kr/#en/ko/" + text

webbrowser.open(url)
