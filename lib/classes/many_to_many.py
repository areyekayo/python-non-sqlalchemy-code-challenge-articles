class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Article already has a title.")
        elif isinstance(title, str) and (5 <= len(title) <= 50):
            self._title = title
        else:
         raise ValueError("Title must be a string and between 5 and 50 characters.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
             self._author = author
        else: raise Exception("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else: raise Exception("Magazine must be an instance of Magazine class")
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Author already has a name")
        elif isinstance(name, str) and 0 < len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
            

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = {article.magazine for article in self.articles()}
        return list(unique_magazines)

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        unique_topics = {magazine.category for magazine in self.magazines()}
        if unique_topics: return list(unique_topics)
        else: return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else: raise ValueError("Name must be a string and between 2 and 16 characters")
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category
        else: raise ValueError("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_authors = {article.author for article in self.articles()}
        return list(unique_authors)

    def article_titles(self):
        if self.articles():
            return [article.title for article in self.articles()]
        else: return None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        
        authors = [author for author, count in author_count.items() if count > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        top_magazine = max(cls.all, key=lambda magazine: len(magazine.articles()))
        return top_magazine if len(top_magazine.articles()) > 0 else None

