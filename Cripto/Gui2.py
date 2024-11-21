import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox
import Key_Create as mdkey
import Hash_Check as mdhash
import Dsa_Signature as mdsign

class DsaApp(QWidget):
    def __init__(self):
        super().__init__()

        # DSA anahtarlarını üret
        self.p, self.q, self.g, self.x, self.y = mdkey.Practical_outline_production()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DSA İmza ve Doğrulama")
        self.setGeometry(100, 100, 600, 400)

        # QSS stili ile modern bir görünüm için ayarları uyguluyoruz
        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
                color: #ECF0F1;
                font-family: "Arial";
                font-size: 14px;
            }

            QLabel {
                font-size: 18px;
                color: #ECF0F1;
            }

            QLineEdit {
                background-color: #34495E;
                color: #ECF0F1;
                border: 1px solid #2980B9;
                padding: 5px;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #2980B9;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #3498DB;
            }

            QPushButton:pressed {
                background-color: #1ABC9C;
            }

            QVBoxLayout {
                margin: 0;
                padding: 20px;
            }

            QHBoxLayout {
                margin: 10px;
            }
        """)

        layout = QVBoxLayout()

        # Başlık
        title_label = QLabel("DSA İmza ve Doğrulama Uygulaması")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Dosya imzalama
        file_layout = QHBoxLayout()
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText("İmzalayacağınız dosyanın yolunu seçin...")
        file_button = QPushButton("Dosya Seç")
        file_button.clicked.connect(self.select_file)
        file_layout.addWidget(self.file_path_input)
        file_layout.addWidget(file_button)

        layout.addLayout(file_layout)

        # Görüntü imzalama ve doğrulama
        self.sign_image_button = QPushButton("Görüntü İmzala ve Kaydet")
        self.sign_image_button.clicked.connect(self.sign_and_save_image)
        self.verify_image_button = QPushButton("Şifreli Görüntüyü Doğrula")
        self.verify_image_button.clicked.connect(self.verify_image)

        layout.addWidget(self.sign_image_button)
        layout.addWidget(self.verify_image_button)

        # Metin imzalama
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Metni girin...")
        self.sign_text_button = QPushButton("Metni İmzala ve Kaydet")
        self.sign_text_button.clicked.connect(self.sign_and_save_text)
        self.verify_text_button = QPushButton("Şifreli Metni Doğrula")
        self.verify_text_button.clicked.connect(self.verify_text)

        layout.addWidget(self.text_input)
        layout.addWidget(self.sign_text_button)
        layout.addWidget(self.verify_text_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Dosya Seç", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            self.file_path_input.setText(file_path)

    def sign_and_save_image(self):
        image_path = self.file_path_input.text()
        if not image_path:
            self.show_error("Dosya yolu girilmedi!")
            return

        try:
            # Dosyanın hash'ini hesapla
            image_hash = mdhash.calculate_file_hash(image_path)
            r, s = mdsign.sign_data(image_hash, self.p, self.q, self.g, self.x)

            # Kaydetme işlemi için dosya adı seç
            file_name, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "Text Files (*.txt)")
            if file_name:
                # Şifreli veriyi dosyaya kaydet
                with open(file_name, "w") as f:
                    f.write(f"r: {r}\ns: {s}\n")

                self.result_label.setText(f"Görüntü başarıyla imzalandı ve kaydedildi. ({file_name})")

        except Exception as e:
            self.show_error(f"İmza hatası: {str(e)}")

    def verify_image(self):
        # Şifreli veriyi dosyadan oku
        file_path, _ = QFileDialog.getOpenFileName(self, "Doğrulamak için dosya seç", "", "Text Files (*.txt)")
        if not file_path:
            self.show_error("Doğrulamak için dosya seçilmedi!")
            return

        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
                r = int(lines[0].split(":")[1].strip())
                s = int(lines[1].split(":")[1].strip())

            # Dosyanın hash'ini hesapla
            image_path = self.file_path_input.text()
            if not image_path:
                self.show_error("Dosya yolu girilmedi!")
                return

            image_hash = mdhash.calculate_file_hash(image_path)
            is_valid = mdsign.verify_data(image_hash, r, s, self.p, self.q, self.g, self.y)

            self.result_label.setText(f"Görüntü İmzası geçerli mi? {is_valid}")

        except Exception as e:
            self.show_error(f"Doğrulama hatası: {str(e)}")

    def sign_and_save_text(self):
        text = self.text_input.text()
        if not text:
            self.show_error("Metin girilmedi!")
            return

        try:
            # Metnin hash'ini hesapla
            text_hash = mdhash.calculate_text_hash(text)
            r, s = mdsign.sign_data(text_hash, self.p, self.q, self.g, self.x)

            # Kaydetme işlemi için dosya adı seç
            file_name, _ = QFileDialog.getSaveFileName(self, "Kaydet", "", "Text Files (*.txt)")
            if file_name:
                # Şifreli metni kaydet
                with open(file_name, "w") as f:
                    f.write(f"r: {r}\ns: {s}\n")

                self.result_label.setText(f"Metin başarıyla imzalandı ve kaydedildi. ({file_name})")

        except Exception as e:
            self.show_error(f"İmza hatası: {str(e)}")

    def verify_text(self):
        # Şifreli metni dosyadan oku
        file_path, _ = QFileDialog.getOpenFileName(self, "Doğrulamak için dosya seç", "", "Text Files (*.txt)")
        if not file_path:
            self.show_error("Doğrulamak için dosya seçilmedi!")
            return

        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
                r = int(lines[0].split(":")[1].strip())
                s = int(lines[1].split(":")[1].strip())

            # Metnin hash'ini hesapla
            text = self.text_input.text()
            if not text:
                self.show_error("Metin girilmedi!")
                return

            text_hash = mdhash.calculate_text_hash(text)
            is_valid = mdsign.verify_data(text_hash, r, s, self.p, self.q, self.g, self.y)

            self.result_label.setText(f"Metin İmzası geçerli mi? {is_valid}")

        except Exception as e:
            self.show_error(f"Doğrulama hatası: {str(e)}")

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Hata")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DsaApp()
    window.show()
    sys.exit(app.exec())
