class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(
            self.title,
            self.author,
            self.pages
        )

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is detroyed!")

myb = Book("Python", "Jose", 200)
print(myb)
print(len(myb))
del myb
