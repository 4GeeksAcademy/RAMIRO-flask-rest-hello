from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Personas(db.Model):
    # __tablename__ = 'personas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    heigth= db.Column(db.Integer)
    mass= db.Column(db.Integer)
    hair_color= db.Column(db.String(250))
    sking_color= db.Column(db.String(250))
    eye_color= db.Column(db.String(250))
    gender= db.Column(db.String(250))
    birth_year= db.Column(db.String(50))
    favoritos_personas = db.relationship('Favoritos', backref='personas', lazy=True)


    def __repr__(self):
        return '<Personas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
        


class Planetas(db.Model):
    # __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    gravity = db.Column(db.Integer)
    diamer = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    favoritos_planetas = db.relationship('Favoritos', backref='planetas', lazy=True)


    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }




class Vehiculos(db.Model):
    # __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    modelo=db.Column(db.String(100))
    vehicle_class=db.Column(db.String(100))
    passangres=db.Column(db.Integer)
    length=db.Column(db.Integer)
    consumables=db.Column(db.String(100))
    favoritos_vehiculos = db.relationship('Favoritos', backref='vehiculos', lazy=True)

    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }




class Usuarios(db.Model):
    # __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apellido=db.Column(db.String(50))
    nombre_de_usuario=db.Column(db.String(50))
    contraseña=db.Column(db.String(50))
    email= db.Column(db.String(50))
    edad=db.Column(db.Integer)
    DNI =db.Column(db.Integer, nullable=False)
    favoritos_usuario = db.relationship('Favoritos', backref='usuarios', lazy=True)

    def __repr__(self):
        return '<Usuarios %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }




class Favoritos(db.Model):
    # __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    personas_id = db.Column(db.Integer, db.ForeignKey('personas.id'))
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))
    vehiculos_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    usuarios_DNI = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False )

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }