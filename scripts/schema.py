from peewee import SqliteDatabase, Model, TextField, IntegerField
import os
os.remove("mydata.db")

db = SqliteDatabase("mydata.db")


class Movie(Model):
    class Meta:
        database = db
        
    title = TextField(null=False, index=True)


db.connect()
db.create_tables([Movie])

new_movie = Movie.create(
    title = "movie"
)

new_movie.save()

for m in Movie.select():
    print(m.title)
