import xml.etree.ElementTree as ET

#parse the xml file
tree = ET.parse("compiler.xml")
root = tree.getroot()
new_Data = []
#iterate through the book elements
for Book in root.findall('book'):
    #extract the required data
    Book_id = Book.get('id')
    Author_Name = Book.find('author').text
    Title = Book.find('title').text
    Genre = Book.find('genre').text
    Price = Book.find('price').text
    Publish_date = Book.find('publish_date').text
    Description = Book.find('description').text
    new_Data.append([Book_id, Author_Name, Title, Genre, Price, Publish_date, Description])

import pandas as pd #importing pandas builtin library
#creating an excel file using extracted data.
writer = pd.DataFrame(new_Data, columns=['Book_id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_date', 'Description'])
#writer.to_excel('Result_.xlsx', index=False)
writer.to_excel('Result_.xlsx', index=False)
