from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///recetas.db', echo=False, future=True)
Session = sessionmaker(bind=engine, autoflush=False, future=True)

class Recetas(Base):
    __tablename__ = 'recetas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ingredientes = Column(Text, nullable=False)
    pasos = Column(Text, nullable=False)

Base.metadata.create_all(engine)

def agregar_receta(nombre, ingredientes, pasos):
    with Session() as session:
        nueva_receta = Recetas(nombre=nombre, ingredientes=ingredientes, pasos=pasos)
        session.add(nueva_receta)
        session.commit()

def leer_recetas():
    with Session() as session:
        return session.query(Recetas).all()
    

def actualizar_receta(nombre, nuevo_nombre=None, nuevos_ingredientes=None, nuevos_pasos=None):
    with Session() as session:
        receta = session.query(Recetas).filter_by(nombre=nombre).first()
        if receta:
            receta.nombre = nuevo_nombre or receta.nombre
            receta.ingredientes = nuevos_ingredientes or receta.ingredientes
            receta.pasos = nuevos_pasos or receta.pasos
            session.commit()
            print("Receta actualizada exitosamente.")
        else:
            print("Hay un Error: No se encontró la receta especificada.")

def eliminar_receta(nombre):
    with Session() as session:
        receta = session.query(Recetas).filter_by(nombre=nombre).first()
        if receta:
            session.delete(receta)
            session.commit()
            print("Receta eliminada exitosamente.")
        else:
            print("Hay un Error: No se encontró la receta especificada.")

def menu_principal():
    while True:
        print("\n Libro de Recetas ")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta ")
        print("c) Eliminar receta ")
        print("d) Ver recetas")
        print("e) Salir")

        opcion = input("Seleccione una opción: ").lower()
        if opcion == 'a':
            nombre = input("Nombre de la receta: ")
            ingredientes = input("Ingredientes (separados por comas): ")
            pasos = input("Pasos (separados por comas): ")
            agregar_receta(nombre, ingredientes, pasos)
        elif opcion == 'b':
            nombre = input("Nombre de la receta a actualizar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            nuevos_ingredientes = input("Nuevos ingredientes (dejar vacío para no cambiar): ")
            nuevos_pasos = input("Nuevos pasos (dejar vacío para no cambiar): ")
            actualizar_receta(nombre, nuevo_nombre, nuevos_ingredientes, nuevos_pasos)
        elif opcion == 'c':
            nombre = input("Nombre de la receta a eliminar: ")
            eliminar_receta(nombre)
        elif opcion == 'd':
            recetas = leer_recetas()
            if recetas:
                print("\nRecetas registradas:")
                for receta in recetas:
                    print(f"ID: {receta.id}, Nombre: {receta.nombre}, Ingredientes: {receta.ingredientes}, Pasos: {receta.pasos}")
        elif opcion == 'e':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida. Elija una opcion del menu.\n")

if __name__ == "__main__":
    menu_principal()
   


