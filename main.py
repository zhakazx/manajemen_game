# Import library
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup ORM
Base = declarative_base()

# Model Game
class Game(Base):
    __tablename__ = 'games'
    id = Column(String(10), primary_key=True)
    nama = Column(String(100))
    genre = Column(String(100))

# Setup database
engine = create_engine("mysql+pymysql://root:@localhost/game_db")
# Inisialisasi session
Session = sessionmaker(bind=engine)
# Membuat session
session = Session()

# Membuat tabel jika belum ada
Base.metadata.create_all(engine)

# Menu tambah Game
def tambah_game():
    id_game = input("ID Game: ")
    nama = input("Nama Game: ")
    genre = input("Genre: ")

    game = Game(id=id_game, nama=nama, genre=genre)
    session.add(game)
    session.commit()
    print("Game berhasil ditambahkan!\n")

# Menu tampilkan Game
def tampilkan_game():
    games = session.query(Game).all()
    if not games:
        print("Belum ada game dalam daftar.\n")
        return

    print("\nDaftar Game Favorit:")
    for g in games:
        print(f"ID: {g.id} | Nama: {g.nama} | Genre: {g.genre}")
    print()

# Menu ubah Game
def ubah_game():
    id_game = input("Masukkan ID Game yang ingin diubah: ")
    game = session.query(Game).filter_by(id=id_game).first()
    if game:
        game.nama = input("Nama baru: ")
        game.genre = input("Genre baru: ")
        session.commit()
        print("Game berhasil diubah.\n")
    else:
        print("Game tidak ditemukan.\n")

# Menu hapus Game
def hapus_game():
    id_game = input("Masukkan ID Game yang ingin dihapus: ")
    game = session.query(Game).filter_by(id=id_game).first()
    if game:
        session.delete(game)
        session.commit()
        print("Game berhasil dihapus.\n")
    else:
        print("Game tidak ditemukan.\n")

# Menu utama
def menu():
    # Loop menu
    while True: 
        print("=== Menu Daftar Game Favorit ===")
        print("1. Tambah Game")
        print("2. Lihat Game")
        print("3. Ubah Game")
        print("4. Hapus Game")
        print("5. Keluar")

        # Input pilihan user
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            tambah_game()
        elif pilihan == "2":
            tampilkan_game()
        elif pilihan == "3":
            ubah_game()
        elif pilihan == "4":
            hapus_game()
        elif pilihan == "5":
            print("Sampai jumpa, Gamer!")
            break
        else:
            print("Pilihan tidak valid!\n")

# Menjalankan program
if __name__ == "__main__":
    menu()
