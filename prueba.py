from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    nombre = Column(String(50))
    edad = Column(Integer)

engine = create_engine('sqlite:///base-usuarios.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

nuevo_usuario = Usuario(nombre='Pedro', edad=30)
session.add(nuevo_usuario)
session.commit()

usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario.nombre, usuario.edad)

session.close()