import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()


# ---------------------------TABLES CREATION
c.execute('PRAGMA foreign_keys = ON')
c.execute('''Create table IF NOT EXISTS persons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT,
            lastName TEXT,
            UNIQUE(firstName, lastName) ON CONFLICT IGNORE
);''')
c.execute('''Create table IF NOT EXISTS scores(
            idPerson INTEGER,
            task INTEGER,
            score INTEGER,
            UNIQUE(idPerson, task) ON CONFLICT REPLACE,
            FOREIGN KEY (idPerson) REFERENCES persons(id) ON DELETE CASCADE

);''')
# ---------------------------END of TABLES CREATION


# ---------------------------FILL PERSONS TABLE
for line in open('score2.txt').readlines():
    elements = line.strip().split(" ")
    c.execute('INSERT INTO persons (firstName, lastName) VALUES (?,?);', (elements[2], elements[3]))
# --------------------------- END FILL PERSONS TABLE


# ---------------------------FILL SCORES TABLE
for line in open('score2.txt').readlines():
    elements = line.strip().split(" ")
    for row in c.execute('SELECT id from persons WHERE firstName = ? and lastName = ?', (elements[2], elements[3])):
        c.execute('INSERT INTO scores (idPerson, task, score) VALUES (?,?,?)', (row[0], elements[1], elements[4]))
        break
# ---------------------------END FILL SCORES TABLE


# ---------------------------QUERIES FOR REQUIREMENT CHECK

# --------------------------------DELETE BY ID
# c.execute('DELETE from persons where id = 2')
# --------------------------------END

# --------------------------------SHOW TOP 10 STUDENTS
print('\n')
print(c.execute('''
            SELECT firstName||' '||lastName as fullname, sum(score)
            FROM scores
            JOIN persons
            ON persons.id = scores.idPerson
            group by id
            order by SUM(score) desc
            limit(10);
''').fetchall())
# --------------------------------END

# --------------------------------SHOW TOP 10 HARDEST TASKS
print('\n')
print(c.execute('''
            SELECT task, SUM(score)
            FROM scores
            group by task
            order by SUM(score) asc
            limit(10);
''').fetchall())

# --------------------------------END
# ---------------------------END QUERIES FOR REQUIREMENT CHECK


# ---------------------------VIEW by ID-PERSON-TASK-SCORE
'''
SELECT idPerson, firstName||' '||lastName as fullname, task, score
FROM scores
JOIN persons
ON persons.id = scores.idPerson
ORDER BY idPerson,task asc
;
'''
# ---------------------------
conn.commit()
conn.close()
