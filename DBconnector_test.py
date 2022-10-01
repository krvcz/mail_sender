import DBconnector




def test_query_result():
    connector = DBconnector.Connector(':memory:', 'SELECT * FROM books')
    connector.connect_db()
    connector.cursor.execute('''CREATE TABLE books (
        id integer,
        mail text, 
        name text, 
        title text,
        return_at date)
        ''')
    connector.cursor.execute('''INSERT INTO books (id, mail, name, title, return_at) VALUES (1, 'hamerrek@test.email', 'Bartosz', 'Sukces to my', date())''')
    assert connector.query_result[0] == (1, 'hamerrek@test.email', 'Bartosz', 'Sukces to my', '2022-09-19')





