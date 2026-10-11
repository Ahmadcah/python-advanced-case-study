"""Studi Kasus 3 - Sistem Keamanan Akun & Audit Log Login."""

import re
from datetime import datetime
from functools import wraps

# Username: min 5 karakter, hanya huruf & angka
POLA_USERNAME = r"^[A-Za-z0-9]{5,}$"
# Password: min 8 karakter, minimal 1 angka
POLA_PASSWORD = r"^(?=.*\d).{8,}$"


class User:
    """Model pengguna dengan username & password terenkapsulasi."""

    def __init__(self, username, password):
        self.username = username  # lewat setter -> validasi
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.fullmatch(POLA_USERNAME, value):
            raise ValueError("Username minimal 5 karakter dan hanya huruf/angka.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not re.fullmatch(POLA_PASSWORD, value):
            raise ValueError("Password minimal 8 karakter dan mengandung angka.")
        self._password = value


def audit_log(func):
    """Decorator: catat timestamp, username, dan status BERHASIL/DITOLAK + alasan.

    Hint: bungkus func dengan @wraps; gunakan try/except ValueError.
    """

    @wraps(func)
    def wrapper(username, password):
        try:
            user = func(username, password)
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"USERNAME={username} STATUS=BERHASIL"
            )
            return user
        except ValueError as exc:
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"USERNAME={username} STATUS=DITOLAK - {exc}"
            )
            return None

    return wrapper


@audit_log
def login(username, password):
    """Coba buat User dari kredensial; ValueError jika format salah."""
    return User(username, password)


def main():
    # TODO: tiga skenario
    # 1. username tidak valid (mis. terlalu pendek / ada simbol)
    # 2. password pendek atau tanpa angka
    # 3. login sukses
    print("=== Case 1: Username tidak valid ===")
    login("ab!", "Password1")

    print("\n=== Case 2: Password pendek atau tanpa angka ===")
    login("fajar89", "short")

    print("\n=== Case 3: Login sukses ===")
    login("fajar89", "Password1")


if __name__ == "__main__":
    main()
