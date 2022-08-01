#key word argument menggunakan tanda bintang dua **

def create_html(tag, text, **attributes):
    html = f"<{tag}"

    #looping argument keynya di sini

    for key, value in attributes.items():
        html = html + f" {key} ='{value}'"    

    html = html + f"> {text} </{tag}>"
    return html

html = create_html("p", "Hello Python", style="background_color:red;")

print (html)

html = create_html("a", "Ini Link", href="www.google.com", style="link", target="blank_")

print(html)

#bagaimana cara menambahkan href pada artibut a?

