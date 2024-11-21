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
        self.sign_image_button = QPushButton("Görüntü İmzala")
        self.sign_image_button.clicked.connect(self.sign_image)
        self.verify_image_button = QPushButton("Görüntü İmzasını Doğrula")
        self.verify_image_button.clicked.connect(self.verify_image)

        layout.addWidget(self.sign_image_button)
        layout.addWidget(self.verify_image_button)

        # Metin imzalama
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Metni girin...")
        self.sign_text_button = QPushButton("Metni İmzala")
        self.sign_text_button.clicked.connect(self.sign_text)
        self.verify_text_button = QPushButton("Metin İmzasını Doğrula")
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

    def sign_image(self):
        image_path = self.file_path_input.text()
        if not image_path:
            self.show_error("Dosya yolu girilmedi!")
            return

        try:
            image_hash = mdhash.calculate_file_hash(image_path)
            r, s = mdsign.sign_data(image_hash, self.p, self.q, self.g, self.x)
            self.result_label.setText(f"Görüntü İmzası: r = {r}, s = {s}")
        except Exception as e:
            self.show_error(f"İmza hatası: {str(e)}")

    def verify_image(self):
        image_path = self.file_path_input.text()
        if not image_path:
            self.show_error("Dosya yolu girilmedi!")
            return

        try:
            image_hash = mdhash.calculate_file_hash(image_path)
            r, s = mdsign.sign_data(image_hash, self.p, self.q, self.g, self.x)  # Bu adımda r, s değerleri oluşturuluyor
            is_valid = mdsign.verify_data(image_hash, r, s, self.p, self.q, self.g, self.y)
            self.result_label.setText(f"Görüntü İmzası geçerli mi? {is_valid}")
        except Exception as e:
            self.show_error(f"Doğrulama hatası: {str(e)}")

    def sign_text(self):
        text = self.text_input.text()
        if not text:
            self.show_error("Metin girilmedi!")
            return

        try:
            text_hash = mdhash.calculate_text_hash(text)
            r, s = mdsign.sign_data(text_hash, self.p, self.q, self.g, self.x)
            self.result_label.setText(f"Metin İmzası: r = {r}, s = {s}")
        except Exception as e:
            self.show_error(f"İmza hatası: {str(e)}")

    def verify_text(self):
        text = self.text_input.text()
        if not text:
            self.show_error("Metin girilmedi!")
            return

        try:
            text_hash = mdhash.calculate_text_hash(text)
            r, s = mdsign.sign_data(text_hash, self.p, self.q, self.g, self.x)  # Bu adımda r, s değerleri oluşturuluyor
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
