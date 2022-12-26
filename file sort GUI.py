import os
import shutil
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Création de tous les widgets de l'interface
        self.source_label = QtWidgets.QLabel('Source Folder :')
        self.source_edit = QtWidgets.QLineEdit()
        self.source_button = QtWidgets.QPushButton('Browse...')
        self.destination_label = QtWidgets.QLabel('Destination Folder :')
        self.destination_edit = QtWidgets.QLineEdit()
        self.destination_button = QtWidgets.QPushButton('Browse...')
        self.extension_label = QtWidgets.QLabel('File extension :')
        self.extension_edit = QtWidgets.QLineEdit()
        self.move_button = QtWidgets.QPushButton('Move Files')

        # Création du layout principal
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.source_label, 0, 0)
        layout.addWidget(self.source_edit, 0, 1)
        layout.addWidget(self.source_button, 0, 2)
        layout.addWidget(self.destination_label, 1, 0)
        layout.addWidget(self.destination_edit, 1, 1)
        layout.addWidget(self.destination_button, 1, 2)
        layout.addWidget(self.extension_label, 2, 0)
        layout.addWidget(self.extension_edit, 2, 1)
        layout.addWidget(self.move_button, 3, 1, 1, 2)
        self.setLayout(layout)

        # Connexion des signaux aux slots
        self.source_button.clicked.connect(self.browse_source)
        self.destination_button.clicked.connect(self.browse_destination)
        self.move_button.clicked.connect(self.move_files)

        # Affichage de la fenêtre
        self.setWindowTitle('Files Sorter')
        self.setWindowIcon(QtGui.QIcon('my_icon.png'))
        self.show()

    def browse_source(self):
        # Ouvre une boîte de dialogue pour sélectionner un dossier
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        # Met à jour le champ de saisie du chemin du dossier source
        self.source_edit.setText(folder)

    def browse_destination(self):
        # Ouvre une boîte de dialogue pour sélectionner un dossier
        folder = QtWidgets.QFileDialog.getExistingDirectory()
        # Met à jour le champ de saisie du chemin du dossier de destination
        self.destination_edit.setText(folder)

    def move_files(self):
        # Récupère les chemins des dossiers source et de destination
        source_folder = self.source_edit.text()
        destination_folder = self.destination_edit.text()
        # Récupère l'extension de fichier spécifiée
        file_extension = self.extension_edit.text()
        # Flag pour savoir si le déplacement a réussi ou non
        success = True
        # Parcourt récursivement tous les fichiers et dossiers du dossier source
        for root, dirs, files in os.walk(source_folder):
            # Parcourt tous les fichiers du dossier courant
            for filename in files:
                # Récupère le chemin complet du fichier
                file_path = os.path.join(root, filename)
                # Récupère l'extension du fichier
                file_ext = os.path.splitext(file_path)[1]
                # Si l'extension du fichier est celle spécifiée
                if file_ext == file_extension:
                    try:
                        # Déplace le fichier vers le dossier de destination
                        shutil.move(file_path, destination_folder)
                    except Exception as e:
                        # Si le déplacement a échoué, met le flag success à False
                        success = False
                        # Affiche un message d'erreur
                        QMessageBox.warning(self, 'Erreur', str(e))
                        break
        # Si le déplacement a réussi, affiche un message de validation
        if success:
            QMessageBox.information(self, 'Succès', 'Les fichiers ont été déplacés avec succès !')
        else:
            QMessageBox.information(self, "Echec", "Nik ta mere")



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()