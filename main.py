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

def cari_game_berdasarkan_nama():
    keyword = input("Masukkan kata kunci nama game: ").lower()
    hasil = session.query(Game).filter(Game.nama.ilike(f"%{keyword}%")).all()
    
    if not hasil:
        print("Tidak ditemukan game dengan nama tersebut.\n")
    else:
        print("\nHasil Pencarian:")
        for g in hasil:
            print(f"ID: {g.id} | Nama: {g.nama} | Genre: {g.genre}")
        print()

def cari_game_berdasarkan_genre():
    keyword = input("Masukkan genre game: ").lower()
    hasil = session.query(Game).filter(Game.genre.ilike(f"%{keyword}%")).all()
    
    if not hasil:
        print("Tidak ditemukan game dengan genre tersebut.\n")
    else:
        print("\nHasil Pencarian Berdasarkan Genre:")
        for g in hasil:
            print(f"ID: {g.id} | Nama: {g.nama} | Genre: {g.genre}")
        print()

def cari_game_berdasarkan_id():
    id_game = input("Masukkan ID Game: ")
    game = session.query(Game).filter_by(id=id_game).first()
    
    if game:
        print(f"\nGame ditemukan:")
        print(f"ID: {game.id} | Nama: {game.nama} | Genre: {game.genre}\n")
    else:
        print("Game dengan ID tersebut tidak ditemukan.\n")

def menu():
    while True: 
        print("=== Menu Daftar Game Favorit ===")
        print("1. Tambah Game")
        print("2. Lihat Game")
        print("3. Ubah Game")
        print("4. Hapus Game")
        print("5. Cari Game berdasarkan Nama")
        print("6. Cari Game berdasarkan Genre")
        print("7. Cari Game berdasarkan ID")  # <- Tambahan fitur ini
        print("8. Keluar")  # <- Update angka keluar

        pilihan = input("Pilih menu (1-8): ")
        if pilihan == "1":
            tambah_game()
        elif pilihan == "2":
            tampilkan_game()
        elif pilihan == "3":
            ubah_game()
        elif pilihan == "4":
            hapus_game()
        elif pilihan == "5":
            cari_game_berdasarkan_nama()
        elif pilihan == "6":
            cari_game_berdasarkan_genre()
        elif pilihan == "7":
            cari_game_berdasarkan_id()  # <- Panggil fungsi baru
        elif pilihan == "8":
            print("Sampai jumpa, Gamer!")
            break
        else:
            print("Pilihan tidak valid!\n")

# Menjalankan program
if __name__ == "__main__":
    menu()
